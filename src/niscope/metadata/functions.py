# -*- coding: utf-8 -*-
# This file is generated from API metadata for NI-SCOPE version 19.1.0d28
functions = {
    'Abort': {
        'documentation': {
            'description': '\nAborts an acquisition and returns the digitizer to the Idle state. Call\nthis function if the digitizer times out waiting for a trigger.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'AcquisitionStatus': {
        'documentation': {
            'description': '\nReturns status information about the acquisition to the **status**\noutput parameter.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns whether the acquisition is complete, in progress, or unknown.\n\n**Defined Values**\n\nNISCOPE_VAL_ACQ_COMPLETE\n\nNISCOPE_VAL_ACQ_IN_PROGRESS\n\nNISCOPE_VAL_ACQ_STATUS_UNKNOWN\n'
                },
                'enum': 'AcquisitionStatus',
                'name': 'acquisitionStatus',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ActualMeasWfmSize': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Returns the total available size of an array measurement acquisition.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe `array\nmeasurement <REPLACE_DRIVER_SPECIFIC_URL_2(array_measurements_refs)>`__\nto perform.\n'
                },
                'enum': 'ArrayMeasurement',
                'name': 'arrayMeasFunction',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the size (in number of samples) of the resulting analysis\nwaveform.\n'
                },
                'name': 'measWaveformSize',
                'type': 'ViInt32'
            }
        ],
        'render_in_session_base': True,
        'returns': 'ViStatus'
    },
    'ActualNumWfms': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nHelps you to declare appropriately sized waveforms. NI-SCOPE handles the\nchannel list parsing for you.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the number of records times the number of channels; if you are\noperating in DDC mode (NI 5620/5621 only), this value is multiplied by\ntwo.\n'
                },
                'name': 'numWfms',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ActualRecordLength': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nReturns the actual number of points the digitizer acquires for each\nchannel. After configuring the digitizer for an acquisition, call this\nfunction to determine the size of the waveforms that the digitizer\nacquires. The value is equal to or greater than the minimum number of\npoints specified in any of the Configure Horizontal functions.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the actual number of points the digitizer acquires for each\nchannel; NI-SCOPE returns the value held in the\nNISCOPE_ATTR_HORZ_RECORD_LENGTH attribute.\n'
                },
                'name': 'recordLength',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'AddWaveformProcessing': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nAdds one measurement to the list of processing steps that are completed\nbefore the measurement. The processing is added on a per channel basis,\nand the processing measurements are completed in the same order they are\nregistered. All measurement library parameters—the attributes starting\nwith NISCOPE_ATTR_MEAS—are cached at the time of registering the\nprocessing, and this set of parameters is used during the processing\nstep. The processing measurements are streamed, so the result of the\nfirst processing step is used as the input for the next step. The\nprocessing is done before any other measurements.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe `array\nmeasurement <REPLACE_DRIVER_SPECIFIC_URL_2(array_measurements_refs)>`__\nto add.\n'
                },
                'enum': 'ArrayMeasurement',
                'name': 'measFunction',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'AdjustRefTrigTs': {
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
                'name': 'recordNum',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'num',
                'type': 'ViUInt64'
            },
            {
                'direction': 'in',
                'name': 'den',
                'type': 'ViUInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'AdjustSampleClockRelativeDelay': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nConfigures the relative sample clock delay (in seconds) when using the\ninternal clock. Each time this function is called, the sample clock is\ndelayed from the reference clock by the specified amount of time.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nHow long the digitizer waits after receiving the trigger to start\nacquiring data. Refer to NISCOPE_ATTR_TRIGGER_DELAY_TIME for more\ninformation.\n'
                },
                'name': 'delay',
                'type': 'ViReal64'
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
                'name': 'repCapName',
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
    'AutoSetup': {
        'documentation': {
            'description': '\nAutomatically configures the instrument. When you call this function,\nthe digitizer senses the input signal and automatically configures many\nof the instrument settings. If a signal is detected on a channel, the\ndriver chooses the smallest available vertical range that is larger than\nthe signal range. For example, if the signal is a 1.2 V\\ :sub:`pk-pk`\nsine wave, and the device supports 1 V and 2 V vertical ranges, the\ndriver will choose the 2 V vertical range for that channel.\n\nIf no signal is found on any analog input channel, a warning is\nreturned, and all channels are enabled. A channel is considered to have\na signal present if the signal is at least 10% of the smallest vertical\nrange available for that channel.\n\nThe following settings are changed:\n',
            'table_body': [
                [
                    '**General**'
                ],
                [
                    'Acquisition mode',
                    'Normal'
                ],
                [
                    'Reference clock',
                    'Internal'
                ],
                [
                    '**Vertical**'
                ],
                [
                    'Vertical coupling',
                    'AC (DC for NI 5621)'
                ],
                [
                    'Vertical bandwidth',
                    'Full'
                ],
                [
                    'Vertical range',
                    'Changed by auto setup'
                ],
                [
                    'Vertical offset',
                    '0 V'
                ],
                [
                    'Probe attenuation',
                    'Unchanged by auto setup'
                ],
                [
                    'Input impedance',
                    'Unchanged by auto setup'
                ],
                [
                    '**Horizontal**'
                ],
                [
                    'Sample rate',
                    'Changed by auto setup'
                ],
                [
                    'Min record length',
                    'Changed by auto setup'
                ],
                [
                    'Enforce realtime',
                    'True'
                ],
                [
                    'Number of Records',
                    'Changed to 1'
                ],
                [
                    '**Triggering**'
                ],
                [
                    'Trigger type',
                    'Edge if signal present, otherwise immediate'
                ],
                [
                    'Trigger channel',
                    'Lowest numbered channel with a signal present'
                ],
                [
                    'Trigger slope',
                    'Positive'
                ],
                [
                    'Trigger coupling',
                    'DC'
                ],
                [
                    'Reference position',
                    '50%'
                ],
                [
                    'Trigger level',
                    '50% of signal on trigger channel'
                ],
                [
                    'Trigger delay',
                    '0'
                ],
                [
                    'Trigger holdoff',
                    '0'
                ],
                [
                    'Trigger output',
                    'None'
                ]
            ]
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'CableSenseSignalStart': {
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
    'CableSenseSignalStop': {
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
    'CachedFetch': {
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
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'numSamples',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'dataType',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'wfm',
                'type': 'void'
            },
            {
                'direction': 'out',
                'name': 'wfmInfo',
                'type': 'niScope_wfmInfo'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalAdjustAccessoryGainAndOffset': {
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
                'name': 'posFs',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'gnd',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'negFs',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalAdjustCompensationAttenuator': {
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
                'name': 'range',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalAdjustDcm': {
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
                'name': 'stimulusFreq',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalAdjustFrequencyResponse': {
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
                'name': 'range',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'stimulusFreq',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'stimulusAmp',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalAdjustInternalReference': {
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
                'name': 'option',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'stimulus',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalAdjustOffset': {
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
                'name': 'range',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalAdjustOffsetRange': {
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
                'name': 'range',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'stimulus',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalAdjustRange': {
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
                'name': 'range',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'stimulus',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalAdjustVcxo': {
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
                'name': 'stimulusFreq',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalChangePassword': {
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
                'name': 'oldPassword',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'newPassword',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalEnd': {
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
            }
        ],
        'returns': 'ViStatus'
    },
    'CalFetchCount': {
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
                'name': 'whichOne',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'calibrationCount',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalFetchDate': {
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
                'name': 'whichOne',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'year',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'month',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'day',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalFetchInternalReference': {
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
                'name': 'whichReference',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'internalRefValue',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalFetchMiscInfo': {
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
                'name': 'miscInfo',
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalFetchTemperature': {
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
                'name': 'whichOne',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'temperature',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalGetAdcVoltageEeprom': {
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
                'name': 'adcVoltageGain',
                'type': 'ViReal32'
            },
            {
                'direction': 'out',
                'name': 'adcVoltageOffset',
                'type': 'ViReal32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalGetFrEeprom': {
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
                'name': 'numCoefficients',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'polynomialFitCoefficients',
                'type': 'ViReal32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalGetSerialDacVoltageEeprom': {
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
                'name': 'serialDacVolts',
                'type': 'ViReal32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalMeasureRISDistribution': {
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
                'name': 'maxTime',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'minBinPercent',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'distributionSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'distribution',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalRouteInternalReference': {
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
                'name': 'option',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'whichReference',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalSelfCalibrate': {
        'documentation': {
            'description': '\nSelf-calibrates most NI digitizers, including all SMC-based devices and\nmost Traditional NI-DAQ (Legacy) devices. To verify that your digitizer\nsupports self-calibration, refer to `Features Supported by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__.\n\nFor SMC-based digitizers, if the self-calibration is performed\nsuccessfully in a regular session, the calibration constants are\nimmediately stored in the self-calibration area of the EEPROM. If the\nself-calibration is performed in an external calibration session, the\ncalibration constants take effect immediately for the duration of the\nsession. However, they are not stored in the EEPROM until\nniScope_CalEnd is called with **action** set to\nNISCOPE_VAL_ACTION_STORE and no errors occur.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'default_value': 'Option.SELF_CALIBRATE_ALL_CHANNELS',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe calibration option. Use VI_NULL for a normal self-calibration\noperation or NISCOPE_VAL_CAL_RESTORE_EXTERNAL_CALIBRATION to\nrestore the previous calibration.\n'
                },
                'enum': 'Option',
                'name': 'option',
                'type': 'ViInt32'
            }
        ],
        'python_name': 'self_cal',
        'returns': 'ViStatus'
    },
    'CalSetAccessorySource': {
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
                'name': 'calSource',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalSetAdcVoltageEeprom': {
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
                'name': 'adcVoltageGain',
                'type': 'ViReal32'
            },
            {
                'direction': 'in',
                'name': 'adcVoltageOffset',
                'type': 'ViReal32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalSetFrEeprom': {
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
                'name': 'numCoefficients',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'polynomialFitCoefficients',
                'type': 'ViReal32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalSetSerialDacVoltageEeprom': {
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
                'name': 'serialDacVolts',
                'type': 'ViReal32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalStart': {
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
                'name': 'newSessionHandle',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalStoreInternalReference': {
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
                'name': 'whichReference',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'internalRefValue',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalStoreMiscInfo': {
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
                'name': 'miscInfo',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'Calibrate': {
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
                'name': 'channel',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'calibrationOperation',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'referenceVoltage',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CancelFetch': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'TBD'
        },
        'parameters': [
            {
                'direction': 'in',
                'name': 'resourceName',
                'type': 'ViRsrc'
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckAttributeViBoolean': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Verifies the validity of a value you specify for a ViBoolean attribute.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The ID of an attribute'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe value that you want to verify for the attribute. Some values might\nnot be valid depending on the current settings of the instrument\nsession.\n'
                },
                'name': 'value',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckAttributeViInt32': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Verifies the validity of a value you specify for a ViInt32 attribute.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe value that you want to verify for the attribute. Some values might\nnot be valid depending on the current settings of the instrument\nsession.\n'
                },
                'name': 'value',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckAttributeViInt64': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Verifies the validity of a value you specify for a ViInt64 attribute.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe value that you want to verify for the attribute. Some values might\nnot be valid depending on the current settings of the instrument\nsession.\n'
                },
                'name': 'value',
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckAttributeViReal64': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Verifies the validity of a value you specify for a ViReal64 attribute.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe value that you want to verify for the attribute. Some values might\nnot be valid depending on the current settings of the instrument\nsession.\n'
                },
                'name': 'value',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckAttributeViSession': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Verifies the validity of a value you specify for a ViSession attribute.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe value that you want to verify for the attribute. Some values might\nnot be valid depending on the current settings of the instrument\nsession.\n'
                },
                'name': 'value',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckAttributeViString': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Verifies the validity of a value you specify for a ViString attribute.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe value that you want to verify for the attribute. Some values might\nnot be valid depending on the current settings of the instrument\nsession.\n'
                },
                'name': 'value',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearError': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nClears the error information for the current execution thread and the\nIVI session you specify. If you pass VI_NULL for the Instrument Handle\nparameter, this function clears the error information only for the\ncurrent execution thread.\n',
            'note': '\nThis function is included for compliance with the IviScope Class\nSpecification.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearErrorInfo': {
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
    'ClearInterchangeWarnings': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Clears the list of current interchange warnings.',
            'note': '\nThis function is included for compliance with the IviScope Class\nSpecification.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearWaveformMeasurementStats': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nClears the waveform stats on the channel and measurement you specify. If\nyou want to clear all of the measurements, use\nNISCOPE_VAL_ALL_MEASUREMENTS in the **clearableMeasurementFunction**\nparameter.\n\nEvery time a measurement is called, the statistics information is\nupdated, including the min, max, mean, standard deviation, and number of\nupdates. This information is fetched with\nniScope_FetchMeasurementStats. The multi-acquisition array measurements\nare also cleared with this function.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'default_value': '_ClearableMeasurement.ALL_MEASUREMENTS',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe `scalar\nmeasurement <REPLACE_DRIVER_SPECIFIC_URL_2(scalar_measurements_refs)>`__\nor `array\nmeasurement <REPLACE_DRIVER_SPECIFIC_URL_2(array_measurements_refs)>`__\nto clear the stats for.\n'
                },
                'enum': 'ClearableMeasurement',
                'name': 'clearableMeasurementFunction',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearWaveformProcessing': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nClears the list of processing steps assigned to the given channel. The\nprocessing is added using the niScope_AddWaveformProcessing function,\nwhere the processing steps are completed in the same order in which they\nare registered. The processing measurements are streamed, so the result\nof the first processing step is used as the input for the next step. The\nprocessing is also done before any other measurements.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'Commit': {
        'documentation': {
            'description': '\nCommits to hardware all the parameter settings associated with the task.\nUse this function if you want a parameter change to be immediately\nreflected in the hardware. This function is not supported for\nTraditional NI-DAQ (Legacy) devices.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureAcquisition': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nConfigures how the digitizer acquires data and fills the waveform\nrecord.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the manner in which the digitizer acquires data and fills the\nwaveform record; NI-SCOPE sets NISCOPE_ATTR_ACQUISITION_TYPE to this\nvalue.\n\n**Defined Values**\n\nNISCOPE_VAL_NORMAL\n\nNISCOPE_VAL_FLEXRES\n\nNISCOPE_VAL_DDC\n',
                    'note': '\nNISCOPE_VAL_DDC applies to the NI 5620/5621 only. To use DDC mode in\nthe NI 5142/5622, leave **acquisitionType** set to NISCOPE_VAL_NORMAL\nand set NISCOPE_ATTR_DDC_ENABLED to True.\n'
                },
                'name': 'acquisitionType',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureAcquisitionRecord': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nThis function is included for compliance with the IviScope Class\nSpecification.\n\nConfigures the most commonly configured attributes of the instrument\nacquisition subsystem.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the time per record.\n\nUnits: Seconds.\n'
                },
                'name': 'timePerRecord',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the minimum number of points you require in the record for each\nchannel. Call niScope_ActualRecordLength to obtain the actual record\nlength used.\n\nValid Values: 1 – available onboard memory\n'
                },
                'name': 'minNumPoints',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the position of the first point in the waveform record\nrelative to the trigger event.\n'
                },
                'name': 'acquisitionStartTime',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureAcquisitionType': {
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
                'name': 'acquisitionType',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureChanCharacteristics': {
        'documentation': {
            'description': '\nConfigures the attributes that control the electrical characteristics of\nthe channel—the input impedance and the bandwidth.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe input impedance for the channel; NI-SCOPE sets\nNISCOPE_ATTR_INPUT_IMPEDANCE to this value.\n'
                },
                'name': 'inputImpedance',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe bandwidth for the channel; NI-SCOPE sets\nNISCOPE_ATTR_MAX_INPUT_FREQUENCY to this value. Pass 0 for this\nvalue to use the hardware default bandwidth. Pass –1 for this value to\nachieve full bandwidth.\n'
                },
                'name': 'maxInputFrequency',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureChannel': {
        'codegen_method': 'no',
        'documentation': {
            'description': "\nThis function is included for compliance with the IviScope Class\nSpecification.\n\nConfigures the most commonly configured attributes of the instrument's\nchannel subsystem.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe channel to configure. For more information, refer to `channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm\',\'cvichannelstringsyntaxforc)>`__.\n\nDefault Value: "0"\n'
                },
                'name': 'channel',
                'type': 'ViString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the voltage range for the specified channel(s).'
                },
                'name': 'range',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSelects the DC offset added to the specified channel(s).\n\nDefault Value: 0\n'
                },
                'name': 'offset',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecify how you want the digitizer to couple the input signal for the\nchannel.\n\nDefined Values\n\nNISCOPE_VAL_AC (0)\n\nNISCOPE_VAL_DC (1)\n\nNISCOPE_VAL_GND (2)\n\nA certain amount of delay is required for the coupling capacitor to\ncharge after changing vertical coupling from DC to AC. This delay is\ntypically:\n\n| Low Impedance Source—150 ms\n| 10X Probe—1.5 s\n| 100X Probe—15 s\n'
                },
                'name': 'coupling',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the probe attenuation for the specified channel(s).\n\nDefault Value: 1.00\n\nValid Range: 1.00 – 100\n\nIf you have a probe with *y*\\ X attenuation, set this parameter to *y*.\nFor example, enter a value of 10 for a 10X probe.\n'
                },
                'name': 'probeAttenuation',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecify whether to enable the digitizer to acquire data for the channel\nwhen you call niScope_InitiateAcquisition or niScope_ReadWaveform.\n\n| Default Value:\n| NISCOPE_VAL_TRUE (1)\n\nDefined Values\n\n| NISCOPE_VAL_TRUE (1)—Acquire data on this channel\n| NISCOPE_VAL_FALSE (0)—Do not acquire data on this channel\n'
                },
                'name': 'enabled',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureClock': {
        'codegen_method': 'no',
        'documentation': {
            'description': "\nConfigures the attributes for synchronizing the digitizer to a reference\nor sending the digitizer's reference clock output to be used as a\nsynchronizing clock for other digitizers.\n",
            'note': '\nSome features are not supported by all digitizers. Refer to `Features\nSupported by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for\nmore information.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the input source for the reference clock to which the 100 MHz\nsample clock is phase-locked. Refer to\nNISCOPE_ATTR_INPUT_CLOCK_SOURCE for more information.\n'
                },
                'name': 'inputClockSource',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nSpecifies the output source for the reference clock to which another\nscope's sample clock can be phased-locked. Refer to\nNISCOPE_ATTR_OUTPUT_CLOCK_SOURCE for more information\n"
                },
                'name': 'outputClockSource',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nFor the NI 5102, specifies the line on which the sample clock is sent or\nreceived. For the NI 5112/5620/5621/5911, specifies the line on which\nthe one time sync pulse is sent or received. This line should be the\nsame for all devices to be synchronized. Refer to\nNISCOPE_ATTR_CLOCK_SYNC_PULSE_SOURCE for more information.\n'
                },
                'name': 'clockSyncPulseSource',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies whether you want the device to be a master or a slave. The\nmaster device is typically the originator of the trigger signal and\nclock sync pulse. For a standalone device, set this attribute to\nVI_FALSE.\n\nRefer to NISCOPE_ATTR_MASTER_ENABLE for more information.\n'
                },
                'name': 'masterEnabled',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureDigitalTrigger': {
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
                'name': 'slope',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureEdgeTrigger': {
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
                'name': 'level',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'triggerCoupling',
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
    'ConfigureEdgeTriggerSource': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSets the edge triggering attributes. An edge trigger occurs when the\ntrigger signal specified with the source parameter passes through the\nvoltage threshold specified with the level parameter and has the slope\nspecified with the slope parameter.\n\nThis function affects instrument behavior only if the triggerType is\nNISCOPE_VAL_EDGE. Set the trigger type and trigger coupling before\ncalling this function.\n\nIf the trigger source is one of the analog input channels, you must\nconfigure the vertical range, vertical offset, vertical coupling, probe\nattenuation, and the maximum input frequency before calling this\nfunction.\n',
            'note': '\nThis function is included for compliance with the IviScope Class\nSpecification.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe voltage threshold for the trigger. Refer to\nNISCOPE_ATTR_TRIGGER_LEVEL for more information.\n'
                },
                'name': 'source',
                'type': 'ViString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe voltage threshold for the trigger. Refer to\nNISCOPE_ATTR_TRIGGER_LEVEL for more information.\n'
                },
                'name': 'level',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies whether you want a rising edge or a falling edge to trigger\nthe digitizer. Refer to NISCOPE_ATTR_TRIGGER_SLOPE for more\ninformation.\n'
                },
                'name': 'slope',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureEqualizationFilterCoefficients': {
        'documentation': {
            'description': '\nConfigures the custom coefficients for the equalization FIR filter on\nthe device. This filter is designed to compensate the input signal for\nartifacts introduced to the signal outside of the digitizer. Because\nthis filter is a generic FIR filter, any coefficients are valid.\nCoefficient values should be between +1 and –1.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The number of coefficients being passed in the **coefficients** array.'
                },
                'name': 'numberOfCoefficients',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe custom coefficients for the equalization FIR filter on the device.\nThese coefficients should be between +1 and –1. You can obtain the\nnumber of coefficients from the\n`NISCOPE_ATTR_EQUALIZATION_NUM_COEFFICIENTS <cviNISCOPE_ATTR_EQUALIZATION_NUM_COEFFICIENTS.html>`__\nattribute. The\n`NISCOPE_ATTR_EQUALIZATION_FILTER_ENABLED <cviNISCOPE_ATTR_EQUALIZATION_FILTER_ENABLED.html>`__\nattribute must be set to TRUE to enable the filter.\n'
                },
                'name': 'coefficients',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfCoefficients'
                },
                'type': 'ViReal64[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureGlitchTriggerSource': {
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
                'name': 'triggerSource',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'level',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'glitchWidth',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'glitchPolarity',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'glitchCondition',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureHorizontal': {
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
                'name': 'timePerRecord',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'minNumPts',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'refPosition',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureHorizontalRate': {
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
                'name': 'minSampleRate',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'minNumPts',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'refPosition',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureHorizontalTiming': {
        'documentation': {
            'description': '\nConfigures the common properties of the horizontal subsystem for a\nmultirecord acquisition in terms of minimum sample rate.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe sampling rate for the acquisition. Refer to\nNISCOPE_ATTR_MIN_SAMPLE_RATE for more information.\n'
                },
                'name': 'minSampleRate',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe minimum number of points you need in the record for each channel;\ncall niScope_ActualRecordLength to obtain the actual record length\nused.\n\nValid Values: Greater than 1; limited by available memory\n'
                },
                'name': 'minNumPts',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe position of the Reference Event in the waveform record specified as\na percentage.\n'
                },
                'name': 'refPosition',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The number of records to acquire'
                },
                'name': 'numRecords',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIndicates whether the digitizer enforces real-time measurements or\nallows equivalent-time (RIS) measurements; not all digitizers support\nRIS—refer to `Features Supported by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for\nmore information.\n\nDefault value: VI_TRUE\n\n**Defined Values**\n\nVI_TRUE—Allow real-time acquisitions only\n\nVI_FALSE—Allow real-time and equivalent-time acquisitions\n'
                },
                'name': 'enforceRealtime',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureHysteresisTrigger': {
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
                'name': 'level',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'hysteresis',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'triggerCoupling',
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
    'ConfigureMemory': {
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
                'name': 'writeAddressInBytes',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'recordSizeInBytes',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'numRecords',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureMultiHorizontal': {
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
                'name': 'timePerRecord',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'minNumPts',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'refPosition',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'numRecords',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureMultiHorizontalRate': {
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
                'name': 'minSampleRate',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'minNumPts',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'refPosition',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'numRecords',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureNumberOfRecords': {
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
                'name': 'specifier',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'mode',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'numberOfRecords',
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureNumberOfSamples': {
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
                'name': 'specifier',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'mode',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'minNumberOfSamples',
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureRefLevels': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nThis function is included for compliance with the IviScope Class\nSpecification.\n\nConfigures the reference levels for all channels of the digitizer. The\nlevels may be set on a per channel basis by setting\nNISCOPE_ATTR_MEAS_CHAN_HIGH_REF_LEVEL,\nNISCOPE_ATTR_MEAS_CHAN_LOW_REF_LEVEL, and\nNISCOPE_ATTR_MEAS_CHAN_MID_REF_LEVEL\n\nThis function configures the reference levels for waveform measurements.\nCall this function before calling niScope_FetchMeasurement to take a\nrise time, fall time, width negative, width positive, duty cycle\nnegative, or duty cycle positive measurement.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': 10.0,
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the low reference you want the digitizer to use for waveform\nmeasurements.\n\nUnits: Either a percentage or voltage based on\nNISCOPE_ATTR_MEAS_REF_LEVEL_UNITS. A percentage is calculated with\nthe voltage low and voltage high measurements representing 0% and 100%,\nrespectively.\n\nDefault Value: 10.0\n'
                },
                'name': 'low',
                'type': 'ViReal64'
            },
            {
                'default_value': 50.0,
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the mid reference you want the digitizer to use for waveform\nmeasurements.\n\nUnits: Either a percentage or voltage based on\nNISCOPE_ATTR_MEAS_REF_LEVEL_UNITS. A percentage is calculated with\nthe voltage low and voltage high measurements representing 0% and 100%,\nrespectively.\n\nDefault Value: 50.0\n'
                },
                'name': 'mid',
                'type': 'ViReal64'
            },
            {
                'default_value': 90.0,
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the high reference you want the digitizer to use for waveform\nmeasurements.\n\nUnits: Either a percentage or voltage based on\nNISCOPE_ATTR_MEAS_REF_LEVEL_UNITS. A percentage is calculated with\nthe voltage low and voltage high measurements representing 0% and 100%,\nrespectively.\n\nDefault Value: 90.0\n'
                },
                'name': 'high',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureRuntTriggerSource': {
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
                'name': 'triggerSource',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'runtLowThreshold',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'runtHighTreshold',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'runtPolarity',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSampleRate': {
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
                'name': 'specifier',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'desiredSampleRate',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTrigger': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nConfigures the common attributes of the trigger subsystem.\n\nWhen you use niScope_ReadWaveform, the instrument waits for a trigger.\nYou specify the type of trigger for which the instrument waits with the\nTrigger Type parameter.\n\nIf the instrument requires multiple waveform acquisitions to build a\ncomplete waveform, it waits for the length of time you specify with the\n**holdoff** parameter to elapse since the previous trigger. The\ninstrument then waits for the next trigger.\n',
            'note': '\nThis function is included for compliance with the IviScope Class\nSpecification.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the type of trigger for which the digitizer will wait.'
                },
                'name': 'triggerType',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe length of time the digitizer waits after detecting a trigger before\nenabling NI-SCOPE to detect another trigger. Refer to\nNISCOPE_ATTR_TRIGGER_HOLDOFF for more information.\n'
                },
                'name': 'holdoff',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTriggerCoupling': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Sets the trigger coupling attribute.',
            'note': '\nThis function is included for compliance with the IviScope Class\nSpecification.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecify how you want the instrument to couple the trigger signal.\n\nDefined Values\n\n NISCOPE_VAL_AC (0)\n\n NISCOPE_VAL_DC (1)\n\nNISCOPE_VAL_HF_REJECT (2)\n\nNISCOPE_VAL_LF_REJECT (3)\n\nNISCOPE_VAL_AC_PLUS_HF_REJECT (1001)\n'
                },
                'name': 'coupling',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTriggerDigital': {
        'documentation': {
            'description': '\nConfigures the common properties of a digital trigger.\n\nWhen you initiate an acquisition, the digitizer waits for the start\ntrigger, which is configured through the NISCOPE_ATTR_ACQ_ARM_SOURCE\n(Start Trigger Source) attribute. The default is immediate. Upon\nreceiving the start trigger the digitizer begins sampling pretrigger\npoints. After the digitizer finishes sampling pretrigger points, the\ndigitizer waits for a reference (stop) trigger that you specify with a\nfunction such as this one. Upon receiving the reference trigger the\ndigitizer finishes the acquisition after completing posttrigger\nsampling. With each Configure Trigger function, you specify\nconfiguration parameters such as the trigger source and the amount of\ntrigger delay.\n',
            'note': '\nFor multirecord acquisitions, all records after the first record are\nstarted by using the Advance Trigger Source. The default is immediate.\n\nYou can adjust the amount of pre-trigger and post-trigger samples using\nthe reference position parameter on the\nniScope_ConfigureHorizontalTiming function. The default is half of the\nrecord length.\n\nSome features are not supported by all digitizers. Refer to `Features\nSupported by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for\nmore information.\n\nDigital triggering is not supported in RIS mode.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the trigger source. Refer to NISCOPE_ATTR_TRIGGER_SOURCE\nfor defined values.\n'
                },
                'name': 'triggerSource',
                'type': 'ViConstString'
            },
            {
                'default_value': 'TriggerSlope.POSITIVE',
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies whether you want a rising edge or a falling edge to trigger\nthe digitizer. Refer to NISCOPE_ATTR_TRIGGER_SLOPE for more\ninformation.\n'
                },
                'enum': 'TriggerSlope',
                'name': 'slope',
                'type': 'ViInt32'
            },
            {
                'default_value': 'datetime.timedelta(seconds=0.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe length of time the digitizer waits after detecting a trigger before\nenabling NI-SCOPE to detect another trigger. Refer to\nNISCOPE_ATTR_TRIGGER_HOLDOFF for more information.\n'
                },
                'name': 'holdoff',
                'python_api_converter_name': 'convert_timedelta_to_seconds',
                'type': 'ViReal64',
                'type_in_documentation': 'float in seconds or datetime.timedelta'
            },
            {
                'default_value': 'datetime.timedelta(seconds=0.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nHow long the digitizer waits after receiving the trigger to start\nacquiring data. Refer to NISCOPE_ATTR_TRIGGER_DELAY_TIME for more\ninformation.\n'
                },
                'name': 'delay',
                'python_api_converter_name': 'convert_timedelta_to_seconds',
                'type': 'ViReal64',
                'type_in_documentation': 'float in seconds or datetime.timedelta'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTriggerEdge': {
        'documentation': {
            'description': '\nConfigures common properties for analog edge triggering.\n\nWhen you initiate an acquisition, the digitizer waits for the start\ntrigger, which is configured through the NISCOPE_ATTR_ACQ_ARM_SOURCE\n(Start Trigger Source) attribute. The default is immediate. Upon\nreceiving the start trigger the digitizer begins sampling pretrigger\npoints. After the digitizer finishes sampling pretrigger points, the\ndigitizer waits for a reference (stop) trigger that you specify with a\nfunction such as this one. Upon receiving the reference trigger the\ndigitizer finishes the acquisition after completing posttrigger\nsampling. With each Configure Trigger function, you specify\nconfiguration parameters such as the trigger source and the amount of\ntrigger delay.\n',
            'note': '\nSome features are not supported by all digitizers. Refer to `Features\nSupported by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for\nmore information.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the trigger source. Refer to NISCOPE_ATTR_TRIGGER_SOURCE\nfor defined values.\n'
                },
                'name': 'triggerSource',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe voltage threshold for the trigger. Refer to\nNISCOPE_ATTR_TRIGGER_LEVEL for more information.\n'
                },
                'name': 'level',
                'type': 'ViReal64'
            },
            {
                'default_value': 'TriggerSlope.POSITIVE',
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies whether you want a rising edge or a falling edge to trigger\nthe digitizer. Refer to NISCOPE_ATTR_TRIGGER_SLOPE for more\ninformation.\n'
                },
                'enum': 'TriggerSlope',
                'name': 'slope',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nApplies coupling and filtering options to the trigger signal. Refer to\nNISCOPE_ATTR_TRIGGER_COUPLING for more information.\n'
                },
                'enum': 'TriggerCoupling',
                'name': 'triggerCoupling',
                'type': 'ViInt32'
            },
            {
                'default_value': 'datetime.timedelta(seconds=0.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe length of time the digitizer waits after detecting a trigger before\nenabling NI-SCOPE to detect another trigger. Refer to\nNISCOPE_ATTR_TRIGGER_HOLDOFF for more information.\n'
                },
                'name': 'holdoff',
                'python_api_converter_name': 'convert_timedelta_to_seconds',
                'type': 'ViReal64',
                'type_in_documentation': 'float in seconds or datetime.timedelta'
            },
            {
                'default_value': 'datetime.timedelta(seconds=0.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nHow long the digitizer waits after receiving the trigger to start\nacquiring data. Refer to NISCOPE_ATTR_TRIGGER_DELAY_TIME for more\ninformation.\n'
                },
                'name': 'delay',
                'python_api_converter_name': 'convert_timedelta_to_seconds',
                'type': 'ViReal64',
                'type_in_documentation': 'float in seconds or datetime.timedelta'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTriggerGlitch': {
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
                'name': 'triggerSource',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'level',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'glitchWidth',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'glitchPolarity',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'glitchCondition',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'triggerCoupling',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'holdoff',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'delay',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTriggerHysteresis': {
        'documentation': {
            'description': '\nConfigures common properties for analog hysteresis triggering. This kind\nof trigger specifies an additional value, specified in the\n**hysteresis** parameter, that a signal must pass through before a\ntrigger can occur. This additional value acts as a kind of buffer zone\nthat keeps noise from triggering an acquisition.\n\nWhen you initiate an acquisition, the digitizer waits for the start\ntrigger, which is configured through the\nNISCOPE_ATTR_ACQ_ARM_SOURCE. The default is immediate. Upon\nreceiving the start trigger the digitizer begins sampling pretrigger\npoints. After the digitizer finishes sampling pretrigger points, the\ndigitizer waits for a reference (stop) trigger that you specify with a\nfunction such as this one. Upon receiving the reference trigger the\ndigitizer finishes the acquisition after completing posttrigger\nsampling. With each Configure Trigger function, you specify\nconfiguration parameters such as the trigger source and the amount of\ntrigger delay.\n',
            'note': '\nSome features are not supported by all digitizers. Refer to `Features\nSupported by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for\nmore information.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the trigger source. Refer to NISCOPE_ATTR_TRIGGER_SOURCE\nfor defined values.\n'
                },
                'name': 'triggerSource',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe voltage threshold for the trigger. Refer to\nNISCOPE_ATTR_TRIGGER_LEVEL for more information.\n'
                },
                'name': 'level',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe size of the hysteresis window on either side of the **level** in\nvolts; the digitizer triggers when the trigger signal passes through the\nhysteresis value you specify with this parameter, has the slope you\nspecify with **slope**, and passes through the **level**. Refer to\nNISCOPE_ATTR_TRIGGER_HYSTERESIS for defined values.\n'
                },
                'name': 'hysteresis',
                'type': 'ViReal64'
            },
            {
                'default_value': 'TriggerSlope.POSITIVE',
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies whether you want a rising edge or a falling edge to trigger\nthe digitizer. Refer to NISCOPE_ATTR_TRIGGER_SLOPE for more\ninformation.\n'
                },
                'enum': 'TriggerSlope',
                'name': 'slope',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nApplies coupling and filtering options to the trigger signal. Refer to\nNISCOPE_ATTR_TRIGGER_COUPLING for more information.\n'
                },
                'enum': 'TriggerCoupling',
                'name': 'triggerCoupling',
                'type': 'ViInt32'
            },
            {
                'default_value': 'datetime.timedelta(seconds=0.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe length of time the digitizer waits after detecting a trigger before\nenabling NI-SCOPE to detect another trigger. Refer to\nNISCOPE_ATTR_TRIGGER_HOLDOFF for more information.\n'
                },
                'name': 'holdoff',
                'python_api_converter_name': 'convert_timedelta_to_seconds',
                'type': 'ViReal64',
                'type_in_documentation': 'float in seconds or datetime.timedelta'
            },
            {
                'default_value': 'datetime.timedelta(seconds=0.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nHow long the digitizer waits after receiving the trigger to start\nacquiring data. Refer to NISCOPE_ATTR_TRIGGER_DELAY_TIME for more\ninformation.\n'
                },
                'name': 'delay',
                'python_api_converter_name': 'convert_timedelta_to_seconds',
                'type': 'ViReal64',
                'type_in_documentation': 'float in seconds or datetime.timedelta'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTriggerImmediate': {
        'documentation': {
            'description': '\nConfigures common properties for immediate triggering. Immediate\ntriggering means the digitizer triggers itself.\n\nWhen you initiate an acquisition, the digitizer waits for a trigger. You\nspecify the type of trigger that the digitizer waits for with a\nConfigure Trigger function, such as niScope_ConfigureTriggerImmediate.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTriggerOutput': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nConfigures the digitizer to generate a signal pulse that other\ndigitizers can detect when configured for digital triggering.\n\nFor Traditional NI-DAQ devices, exported signals are still present in\nthe route after the session is closed. You must clear the route before\nclosing the session, or call niScope_reset.\n\nTo clear the route, call this function again and route\nNISCOPE_VAL_NONE to the line that you had exported. For example, if\nyou originally called this function with the trigger event\nNISCOPE_VAL_STOP_TRIGGER_EVENT routed to the trigger output\nNISCOPE_VAL_RTSI_0, you would call this function again with\nNISCOPE_VAL_NONE routed to NISCOPE_VAL_RTSI_0 to clear the route.\n',
            'note': '\nThis function is obsolete. Consider using niScope_ExportSignal\ninstead.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the condition in which this device generates a digital pulse.'
                },
                'name': 'triggerEvent',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the hardware signal line on which the digital pulse is\ngenerated.\n\n**Valid Values**\n\n| NISCOPE_VAL_NO_EVENT\n| NISCOPE_VAL_STOP_TRIGGER_EVENT\n| NISCOPE_VAL_START_TRIGGER_EVENT\n| NISCOPE_VAL_END_OF_ACQUISITION_EVENT\n| NISCOPE_VAL_END_OF_RECORD_EVENT\n'
                },
                'name': 'triggerOutput',
                'type': 'ViString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTriggerRunt': {
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
                'name': 'triggerSource',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'runtLowThreshold',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'runtHighTreshold',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'runtPolarity',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'triggerCoupling',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'holdoff',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'delay',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTriggerSoftware': {
        'documentation': {
            'description': '\nConfigures common properties for software triggering.\n\nWhen you initiate an acquisition, the digitizer waits for the start\ntrigger, which is configured through the NISCOPE_ATTR_ACQ_ARM_SOURCE\n(Start Trigger Source) attribute. The default is immediate. Upon\nreceiving the start trigger the digitizer begins sampling pretrigger\npoints. After the digitizer finishes sampling pretrigger points, the\ndigitizer waits for a reference (stop) trigger that you specify with a\nfunction such as this one. Upon receiving the reference trigger the\ndigitizer finishes the acquisition after completing posttrigger\nsampling. With each Configure Trigger function, you specify\nconfiguration parameters such as the trigger source and the amount of\ntrigger delay.\n\nTo trigger the acquisition, use niScope_SendSoftwareTriggerEdge.\n',
            'note': '\nSome features are not supported by all digitizers. Refer to `Features\nSupported by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for\nmore information.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': 'datetime.timedelta(seconds=0.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe length of time the digitizer waits after detecting a trigger before\nenabling NI-SCOPE to detect another trigger. Refer to\nNISCOPE_ATTR_TRIGGER_HOLDOFF for more information.\n'
                },
                'name': 'holdoff',
                'python_api_converter_name': 'convert_timedelta_to_seconds',
                'type': 'ViReal64',
                'type_in_documentation': 'float in seconds or datetime.timedelta'
            },
            {
                'default_value': 'datetime.timedelta(seconds=0.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nHow long the digitizer waits after receiving the trigger to start\nacquiring data. Refer to NISCOPE_ATTR_TRIGGER_DELAY_TIME for more\ninformation.\n'
                },
                'name': 'delay',
                'python_api_converter_name': 'convert_timedelta_to_seconds',
                'type': 'ViReal64',
                'type_in_documentation': 'float in seconds or datetime.timedelta'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTriggerSource': {
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
                'name': 'triggerSource',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'triggerType',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'triggerDelay',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'holdoff',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTriggerVideo': {
        'documentation': {
            'description': '\nConfigures the common properties for video triggering, including the\nsignal format, TV event, line number, polarity, and enable DC restore. A\nvideo trigger occurs when the digitizer finds a valid video signal sync.\n\nWhen you initiate an acquisition, the digitizer waits for the start\ntrigger, which is configured through the NISCOPE_ATTR_ACQ_ARM_SOURCE\n(Start Trigger Source) attribute. The default is immediate. Upon\nreceiving the start trigger the digitizer begins sampling pretrigger\npoints. After the digitizer finishes sampling pretrigger points, the\ndigitizer waits for a reference (stop) trigger that you specify with a\nfunction such as this one. Upon receiving the reference trigger the\ndigitizer finishes the acquisition after completing posttrigger\nsampling. With each Configure Trigger function, you specify\nconfiguration parameters such as the trigger source and the amount of\ntrigger delay.\n',
            'note': '\nSome features are not supported by all digitizers. Refer to `Features\nSupported by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for\nmore information.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the trigger source. Refer to NISCOPE_ATTR_TRIGGER_SOURCE\nfor defined values.\n'
                },
                'name': 'triggerSource',
                'type': 'ViConstString'
            },
            {
                'default_value': False,
                'direction': 'in',
                'documentation': {
                    'description': '\nOffsets each video line so the clamping level (the portion of the video\nline between the end of the color burst and the beginning of the active\nimage) is moved to zero volt. Refer to\nNISCOPE_ATTR_ENABLE_DC_RESTORE for defined values.\n'
                },
                'name': 'enableDcRestore',
                'type': 'ViBoolean'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the type of video signal sync the digitizer should look for.\nRefer to NISCOPE_ATTR_TV_TRIGGER_SIGNAL_FORMAT for more\ninformation.\n'
                },
                'enum': 'VideoSignalFormat',
                'name': 'signalFormat',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the TV event you want to trigger on. You can trigger on a\nspecific or on the next coming line or field of the signal.\n'
                },
                'enum': 'VideoTriggerEvent',
                'name': 'event',
                'type': 'ViInt32'
            },
            {
                'default_value': 1,
                'direction': 'in',
                'documentation': {
                    'description': '\nSelects the line number to trigger on. The line number range covers an\nentire frame and is referenced as shown on `Vertical Blanking and\nSynchronization\nSignal <REPLACE_DRIVER_SPECIFIC_URL_1(gray_scale_image)>`__. Refer to\nNISCOPE_ATTR_TV_TRIGGER_LINE_NUMBER for more information.\n\nDefault value: 1\n'
                },
                'name': 'lineNumber',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the polarity of the video signal sync.'
                },
                'enum': 'VideoPolarity',
                'name': 'polarity',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nApplies coupling and filtering options to the trigger signal. Refer to\nNISCOPE_ATTR_TRIGGER_COUPLING for more information.\n'
                },
                'enum': 'TriggerCoupling',
                'name': 'triggerCoupling',
                'type': 'ViInt32'
            },
            {
                'default_value': 'datetime.timedelta(seconds=0.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe length of time the digitizer waits after detecting a trigger before\nenabling NI-SCOPE to detect another trigger. Refer to\nNISCOPE_ATTR_TRIGGER_HOLDOFF for more information.\n'
                },
                'name': 'holdoff',
                'python_api_converter_name': 'convert_timedelta_to_seconds',
                'type': 'ViReal64',
                'type_in_documentation': 'float in seconds or datetime.timedelta'
            },
            {
                'default_value': 'datetime.timedelta(seconds=0.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nHow long the digitizer waits after receiving the trigger to start\nacquiring data. Refer to NISCOPE_ATTR_TRIGGER_DELAY_TIME for more\ninformation.\n'
                },
                'name': 'delay',
                'python_api_converter_name': 'convert_timedelta_to_seconds',
                'type': 'ViReal64',
                'type_in_documentation': 'float in seconds or datetime.timedelta'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTriggerWidth': {
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
                'name': 'triggerSource',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'level',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'widthLowThreshold',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'widthHighTreshold',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'widthPolarity',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'widthCondition',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'triggerCoupling',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'holdoff',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'delay',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTriggerWindow': {
        'documentation': {
            'description': '\nConfigures common properties for analog window triggering. A window\ntrigger occurs when a signal enters or leaves a window you specify with\nthe **high level** or **low level** parameters.\n\nWhen you initiate an acquisition, the digitizer waits for the start\ntrigger, which is configured through the NISCOPE_ATTR_ACQ_ARM_SOURCE\n(Start Trigger Source) attribute. The default is immediate. Upon\nreceiving the start trigger the digitizer begins sampling pretrigger\npoints. After the digitizer finishes sampling pretrigger points, the\ndigitizer waits for a reference (stop) trigger that you specify with a\nfunction such as this one. Upon receiving the reference trigger the\ndigitizer finishes the acquisition after completing posttrigger\nsampling. With each Configure Trigger function, you specify\nconfiguration parameters such as the trigger source and the amount of\ntrigger delay.\n\nTo trigger the acquisition, use niScope_SendSoftwareTriggerEdge.\n',
            'note': '\nSome features are not supported by all digitizers. Refer to `Features\nSupported by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for\nmore information.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the trigger source. Refer to NISCOPE_ATTR_TRIGGER_SOURCE\nfor defined values.\n'
                },
                'name': 'triggerSource',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPasses the voltage threshold you want the digitizer to use for low\ntriggering.\n'
                },
                'name': 'lowLevel',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPasses the voltage threshold you want the digitizer to use for high\ntriggering.\n'
                },
                'name': 'highLevel',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies whether you want the trigger to occur when the signal enters\nor leaves a window.\n'
                },
                'enum': 'TriggerWindowMode',
                'name': 'windowMode',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nApplies coupling and filtering options to the trigger signal. Refer to\nNISCOPE_ATTR_TRIGGER_COUPLING for more information.\n'
                },
                'enum': 'TriggerCoupling',
                'name': 'triggerCoupling',
                'type': 'ViInt32'
            },
            {
                'default_value': 'datetime.timedelta(seconds=0.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe length of time the digitizer waits after detecting a trigger before\nenabling NI-SCOPE to detect another trigger. Refer to\nNISCOPE_ATTR_TRIGGER_HOLDOFF for more information.\n'
                },
                'name': 'holdoff',
                'python_api_converter_name': 'convert_timedelta_to_seconds',
                'type': 'ViReal64',
                'type_in_documentation': 'float in seconds or datetime.timedelta'
            },
            {
                'default_value': 'datetime.timedelta(seconds=0.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nHow long the digitizer waits after receiving the trigger to start\nacquiring data. Refer to NISCOPE_ATTR_TRIGGER_DELAY_TIME for more\ninformation.\n'
                },
                'name': 'delay',
                'python_api_converter_name': 'convert_timedelta_to_seconds',
                'type': 'ViReal64',
                'type_in_documentation': 'float in seconds or datetime.timedelta'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTvTriggerLineNumber': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nThis function is included for compliance with the IviScope Class\nSpecification.\n\nConfigures the TV line upon which the instrument triggers. The line\nnumber is absolute and not relative to the field of the TV signal.\n\nThis function affects instrument behavior only if the trigger type is\nset to NISCOPE_VAL_TV_TRIGGER and the TV trigger event is set to\nNISCOPE_VAL_TV_EVENT_LINE_NUMBER. Call\nniScope_ConfigureTVTriggerSource to set the TV trigger event before\ncalling this function.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecify the line number of the signal you want to trigger off of. The\nvalid ranges of the attribute depend on the signal format configured.\n\nDefault Value: 1\n',
                    'table_body': [
                        [
                            'M-NTSC, 480i, 480p',
                            '1 to 525'
                        ],
                        [
                            'BG/PAL, SECAM, 576i, 576p',
                            '1 to 625'
                        ],
                        [
                            '720p',
                            '1 to 750'
                        ],
                        [
                            '1080i,1080p',
                            '1 to 1,125'
                        ]
                    ],
                    'table_header': [
                        'Signal Format',
                        'Line Numbers'
                    ]
                },
                'name': 'lineNumber',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTvTriggerSource': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nConfigures the instrument for TV triggering. It configures the TV signal\nformat, the event, and the signal polarity.\n\nThis function affects instrument behavior only if the trigger type is\nNISCOPE_VAL_TV_TRIGGER. Set the trigger type and trigger coupling\nbefore calling this function.\n',
            'note': '\nThis function is included for compliance with the IviScope Class\nSpecification.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the source you want the digitizer to monitor for a trigger.\n\nDefined Values\n\n| "0"—Channel 0\n| "1"—Channel 1\n| NISCOPE_VAL_EXTERNAL—Analog External Trigger Input\n'
                },
                'name': 'source',
                'type': 'ViString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the Video/TV signal format.\n\nDefined Values\n\n| NISCOPE_VAL_NTSC (1)\n| NISCOPE_VAL_PAL (2)\n| NISCOPE_VAL_SECAM (3)\n'
                },
                'name': 'signalFormat',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nVideo/TV event to trigger off of.\n\nDefined Values\n\n| NISCOPE_VAL_TV_EVENT_FIELD1 (1)—trigger on field 1 of the signal\n| NISCOPE_VAL_TV_EVENT_FIELD2 (2)—trigger on field 2 of the signal\n| NISCOPE_VAL_TV_EVENT_ANY_FIELD (3)—trigger on the first field\n  acquired\n| NISCOPE_VAL_TV_EVENT_ANY_LINE (4)—trigger on the first line\n  acquired\n| NISCOPE_VAL_TV_EVENT_LINE_NUMBER (5)—trigger on a specific line\n  of a video signal. Valid values vary depending on the signal format\n  configured.\n'
                },
                'name': 'event',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\n| Specifies the polarity of the video signal to trigger off of.\n\nDefined Values\n\n| NISCOPE_VAL_TV_POSITIVE (1)\n| NISCOPE_VAL_TV_NEGATIVE (2)\n'
                },
                'name': 'polarity',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureVertical': {
        'documentation': {
            'description': '\nConfigures the most commonly configured attributes of the digitizer\nvertical subsystem, such as the range, offset, coupling, probe\nattenuation, and the channel.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the vertical range Refer to NISCOPE_ATTR_VERTICAL_RANGE for\nmore information.\n'
                },
                'name': 'range',
                'type': 'ViReal64'
            },
            {
                'default_value': 0.0,
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the vertical offset. Refer to NISCOPE_ATTR_VERTICAL_OFFSET\nfor more information.\n'
                },
                'name': 'offset',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies how to couple the input signal. Refer to\nNISCOPE_ATTR_VERTICAL_COUPLING for more information.\n'
                },
                'enum': 'VerticalCoupling',
                'name': 'coupling',
                'type': 'ViInt32'
            },
            {
                'default_value': 1.0,
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the probe attenuation. Refer to\nNISCOPE_ATTR_PROBE_ATTENUATION for valid values.\n'
                },
                'name': 'probeAttenuation',
                'type': 'ViReal64'
            },
            {
                'default_value': True,
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies whether the channel is enabled for acquisition. Refer to\nNISCOPE_ATTR_CHANNEL_ENABLED for more information.\n'
                },
                'name': 'enabled',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureWidthTriggerSource': {
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
                'name': 'triggerSource',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'level',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'widthLowThreshold',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'widthHighTreshold',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'widthPolarity',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'widthCondition',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureWindowTrigger': {
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
                'name': 'lowLevel',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'highLevel',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'triggerCoupling',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'windowMode',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateConfigurationList': {
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
                'name': 'listName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'numberOfListAttribute',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'activeAttributesIds',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViAttr[]'
            },
            {
                'direction': 'in',
                'name': 'setAsActiveList',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateConfigurationListStep': {
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
                'name': 'setAsActiveStep',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'DeleteConfigurationList': {
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
                'name': 'listName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'DigitalPotControl': {
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
                'name': 'deltaValue',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'storeValue',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'Disable': {
        'documentation': {
            'description': '\nAborts any current operation, opens data channel relays, and releases\nRTSI and PFI lines.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'DownloadWave': {
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
                'name': 'waveMode',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'waveSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'wave',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ErrorHandler': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nTakes the error code returned by NI-SCOPE functions and returns the\ninterpretation as a user-readable string.\n',
            'note': '\nYou can pass VI_NULL as the instrument handle, which is useful to\ninterpret errors after niScope_init has failed.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe error code that is returned from any of the instrument driver\nfunctions.\n'
                },
                'name': 'errorCode',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nSpecifies the function in which the error occurred. You can pass in a\nstring no longer than MAX_FUNCTION_NAME_SIZE. If you pass in a valid\nstring, this source is included in the **errorDescription** string. For\nexample:\n\n"Error <**errorCode**> at <**errorSource**>"\n\nIf you pass in NULL or an empty string, this parameter is ignored.\n'
                },
                'name': 'errorSource',
                'type': 'ViChar[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the interpreted error code as a user readable message string;\nyou must pass a ViChar array at least MAX_ERROR_DESCRIPTION bytes in\nlength.\n'
                },
                'name': 'errorDescription',
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ExportAttributeConfigurationBuffer': {
        'documentation': {
            'description': '\nExports the attribute configuration of the session to a configuration\nbuffer.\n\nYou can export and import session attribute configurations only between\ndevices with identical model numbers, channel counts, and onboard memory\nsizes.\n\nThis function verifies that the attributes you have configured for the\nsession are valid. If the configuration is invalid, NI‑SCOPE returns an\nerror.\n\n**Related Topics:**\n\n`Attributes and Attribute\nFunctions <REPLACE_DRIVER_SPECIFIC_URL_1(attributes_and_attribute_functions)>`__\n\n`Setting Attributes Before Reading\nAttributes <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the size, in bytes, of the byte array to export. If you enter\n0, this function returns the needed size.\n'
                },
                'name': 'sizeInBytes',
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
                    'value': 'sizeInBytes'
                },
                'type': 'ViInt8[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ExportAttributeConfigurationFile': {
        'documentation': {
            'description': '\nExports the attribute configuration of the session to the specified\nfile.\n\nYou can export and import session attribute configurations only between\ndevices with identical model numbers, channel counts, and onboard memory\nsizes.\n\nThis function verifies that the attributes you have configured for the\nsession are valid. If the configuration is invalid, NI‑SCOPE returns an\nerror.\n\n**Related Topics:**\n\n`Attributes and Attribute\nFunctions <REPLACE_DRIVER_SPECIFIC_URL_1(attributes_and_attribute_functions)>`__\n\n`Setting Attributes Before Reading\nAttributes <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the absolute path to the file to contain the exported\nattribute configuration. If you specify an empty or relative path, this\nfunction returns an error.\n**Default file extension:** .niscopeconfig\n'
                },
                'name': 'filePath',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ExportAttributes': {
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
    'ExportSignal': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nConfigures the digitizer to generate a signal that other devices can\ndetect when configured for digital triggering or sharing clocks. The\n**signal** parameter specifies what condition causes the digitizer to\ngenerate the signal. The **outputTerminal** parameter specifies where to\nsend the signal on the hardware (such as a PFI connector or RTSI line).\n\nIn cases where multiple instances of a particular signal exist, use the\n**signalIdentifier** input to specify which instance to control. For\nnormal signals, only one instance exists and you should leave this\nparameter set to the empty string. You can call this function multiple\ntimes and set each available line to a different signal.\n\nTo unprogram a specific line on device, call this function with the\nsignal you no longer want to export and set **outputTerminal** to\nNISCOPE_VAL_NONE.\n',
            'note': 'This function replaces niScope_ConfigureTriggerOutput.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nsignal (clock, trigger, or event) to export.\n\n**Defined Values**\n',
                    'table_body': [
                        [
                            'NISCOPE_VAL_REF_TRIGGER',
                            '(1)',
                            'Generate a pulse when detecting the Stop/Reference trigger.'
                        ],
                        [
                            'NISCOPE_VAL_START_TRIGGER',
                            '(2)',
                            'Generate a pulse when detecting a Start trigger.'
                        ],
                        [
                            'NISCOPE_VAL_END_OF_ACQUISITION_EVENT',
                            '(3)',
                            'Generate a pulse when the acquisition finishes.'
                        ],
                        [
                            'NISCOPE_VAL_END_OF_RECORD_EVENT',
                            '(4)',
                            'Generate a pulse at the end of the record.'
                        ],
                        [
                            'NISCOPE_VAL_ADVANCE_TRIGGER',
                            '(5)',
                            'Generate a pulse when detecting an Advance trigger.'
                        ],
                        [
                            'NISCOPE_VAL_READY_FOR_ADVANCE_EVENT',
                            '(6)',
                            'Asserts when the digitizer is ready to advance to the next record.'
                        ],
                        [
                            'NISCOPE_VAL_READY_FOR_START_EVENT',
                            '(7)',
                            'Asserts when the digitizer is initiated and ready to accept a Start trigger and begin sampling.'
                        ],
                        [
                            'NISCOPE_VAL_READY_FOR_REF_EVENT',
                            '(10)',
                            'Asserts when the digitizer is ready to accept a Reference trigger.'
                        ],
                        [
                            'NISCOPE_VAL_REF_CLOCK',
                            '(100)',
                            'Export the Reference clock for the digitizer to the specified terminal.'
                        ],
                        [
                            'NISCOPE_VAL_SAMPLE_CLOCK',
                            '(101)',
                            'Export the Sample clock for the digitizer to the specified terminal.'
                        ],
                        [
                            'NISCOPE_VAL_5V_OUT',
                            '(13)',
                            'Exports a 5 V power supply.'
                        ]
                    ]
                },
                'enum': 'ExportableSignals',
                'name': 'signal',
                'type': 'ViInt32'
            },
            {
                'default_value': '"None"',
                'direction': 'in',
                'documentation': {
                    'description': 'Describes the signal being exported.'
                },
                'name': 'signalIdentifier',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies the hardware signal line on which the digital pulse is\ngenerated.\n\n**Defined Values**\n',
                    'table_body': [
                        [
                            'NISCOPE_VAL_RTSI_0',
                            '("VAL_RTSI_0")'
                        ],
                        [
                            'NISCOPE_VAL_RTSI_1',
                            '("VAL_RTSI_1")'
                        ],
                        [
                            'NISCOPE_VAL_RTSI_2',
                            '("VAL_RTSI_2")'
                        ],
                        [
                            'NISCOPE_VAL_RTSI_3',
                            '("VAL_RTSI_3")'
                        ],
                        [
                            'NISCOPE_VAL_RTSI_4',
                            '("VAL_RTSI_4")'
                        ],
                        [
                            'NISCOPE_VAL_RTSI_5',
                            '("VAL_RTSI_5")'
                        ],
                        [
                            'NISCOPE_VAL_RTSI_6',
                            '("VAL_RTSI_6")'
                        ],
                        [
                            'NISCOPE_VAL_RTSI_7',
                            '("VAL_RTSI_7")'
                        ],
                        [
                            'NISCOPE_VAL_PXI_STAR',
                            '("VAL_PXI_STAR")'
                        ],
                        [
                            'NISCOPE_VAL_PFI_0',
                            '("VAL_PFI_0")'
                        ],
                        [
                            'NISCOPE_VAL_PFI_1',
                            '("VAL_PFI_1")'
                        ],
                        [
                            'NISCOPE_VAL_PFI_2',
                            '("VAL_PFI_2")'
                        ],
                        [
                            'NISCOPE_VAL_CLK_OUT',
                            '("VAL_CLK_OUT")'
                        ]
                    ]
                },
                'name': 'outputTerminal',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'FancyFetch': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': '\nReturns the waveform from a previously initiated acquisition that the\ndigitizer acquires for the specified channel. This function returns\nscaled voltage waveforms.\n\nThis function may return multiple waveforms depending on the number of\nchannels, the acquisition type, and the number of records you specify.',
            'note': 'Some functionality, such as time stamping, is not supported in all digitizers.'
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
                    'description': 'The instrument handle you obtain from niScope_init that identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The channel(s) to fetch from.'
                },
                'name': 'channelList',
                'type': 'ViString'
            },
            {
                'default_value': None,
                'direction': 'in',
                'documentation': {
                    'description': 'The maximum number of samples to fetch for each waveform. If the acquisition finishes with fewer points than requested, some devices return partial data if the acquisition finished, was aborted, or a timeout of 0 was used. If it fails to complete within the timeout period, the function raises.'
                },
                'name': 'numSamples',
                'type': 'ViInt32'
            },
            {
                'default_value': 'FetchRelativeTo.PRETRIGGER',
                'direction': 'in',
                'documentation': {
                    'description': 'Position to start fetching within one record.'
                },
                'enum': 'FetchRelativeTo',
                'name': 'relativeTo',
                'type': 'ViInt32'
            },
            {
                'default_value': 0,
                'direction': 'in',
                'documentation': {
                    'description': 'Offset in samples to start fetching data within each record. The offset can be positive or negative.'
                },
                'name': 'offset',
                'type': 'ViInt32'
            },
            {
                'default_value': 0,
                'direction': 'in',
                'documentation': {
                    'description': 'Zero-based index of the first record to fetch.'
                },
                'name': 'recordNumber',
                'type': 'ViInt32'
            },
            {
                'default_value': None,
                'direction': 'in',
                'documentation': {
                    'description': 'Number of records to fetch. Use -1 to fetch all configured records.'
                },
                'name': 'numRecords',
                'type': 'ViInt32'
            },
            {
                'default_value': 'datetime.timedelta(seconds=5.0)',
                'direction': 'in',
                'documentation': {
                    'description': 'The time to wait for data to be acquired; using 0 for this parameter tells NI-SCOPE to fetch whatever is currently available. Using -1 seconds for this parameter implies infinite timeout.'
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds',
                'type': 'ViReal64',
                'type_in_documentation': 'float in seconds or datetime.timedelta'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns an array of classes with the following timing and scaling information about each waveform:\n\n-  **relative_initial_x** (float) the time (in seconds) from the trigger to the first sample in the fetched waveform\n-  **absolute_initial_x** (float) timestamp (in seconds) of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output.\n-  **x_increment** (float) the time between points in the acquired waveform in seconds\n-  **channel** (str) channel name this waveform was asquire from\n-  **record** (int) record number of this waveform\n-  **gain** (float) the gain factor of the given channel; useful for scaling binary data with the following formula:\n\n    .. math::\n\n        voltage = binary data * gain factor + offset\n\n-  **offset** (float) the offset factor of the given channel; useful for scaling binary data with the following formula:\n\n    .. math::\n\n        voltage = binary data * gain factor + offset\n\n- **samples** (array of float) floating point array of samples. Length will be of the actual samples acquired\n'
                },
                'name': 'wfmInfo',
                'size': {
                    'mechanism': 'python-code',
                    'value': '(num_samples * self._actual_num_wfms())'
                },
                'type': 'struct niScope_wfmInfo[]'
            }
        ],
        'python_name': 'fetch',
        'returns': 'ViStatus'
    },
    'FancyGetEqualizationFilterCoefficients': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': 'Retrieves the custom coefficients for the equalization FIR filter on the device. This filter is designed to compensate the input signal for artifacts introduced to the signal outside of the digitizer. Because this filter is a generic FIR filter, any coefficients are valid. Coefficient values should be between +1 and –1.'
        },
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'get_equalization_filter_coefficients'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The instrument handle you obtain from niScope_init that identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The channel to configure.'
                },
                'name': 'channel',
                'type': 'ViString'
            }
        ],
        'python_name': 'get_equalization_filter_coefficients',
        'returns': 'ViStatus'
    },
    'FancyRead': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': '\nInitiates an acquisition, waits for it to complete, and retrieves the\ndata. The process is similar to calling niScope_InitiateAcquisition,\nniScope_AcquisitionStatus, and niScope_Fetch. The only difference is\nthat with niScope_Read, you enable all channels specified with\n**channelList** before the acquisition; in the other method, you enable\nthe channels with niScope_ConfigureVertical.\n\nThis function may return multiple waveforms depending on the number of\nchannels, the acquisition type, and the number of records you specify.',
            'note': 'Some functionality, such as time stamping, is not supported in all digitizers.'
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
                    'description': 'The instrument handle you obtain from niScope_init that identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The channel(s) to read from.'
                },
                'name': 'channelList',
                'type': 'ViString'
            },
            {
                'default_value': None,
                'direction': 'in',
                'documentation': {
                    'description': 'The maximum number of samples to fetch for each waveform. If the acquisition finishes with fewer points than requested, some devices return partial data if the acquisition finished, was aborted, or a timeout of 0 was used. If it fails to complete within the timeout period, the function raises.'
                },
                'name': 'numSamples',
                'type': 'ViInt32'
            },
            {
                'default_value': 'FetchRelativeTo.PRETRIGGER',
                'direction': 'in',
                'documentation': {
                    'description': 'Position to start fetching within one record.'
                },
                'enum': 'FetchRelativeTo',
                'name': 'relativeTo',
                'type': 'ViInt32'
            },
            {
                'default_value': 0,
                'direction': 'in',
                'documentation': {
                    'description': 'Offset in samples to start fetching data within each record. The offset can be positive or negative.'
                },
                'name': 'offset',
                'type': 'ViInt32'
            },
            {
                'default_value': 0,
                'direction': 'in',
                'documentation': {
                    'description': 'Zero-based index of the first record to fetch.'
                },
                'name': 'recordNumber',
                'type': 'ViInt32'
            },
            {
                'default_value': None,
                'direction': 'in',
                'documentation': {
                    'description': 'Number of records to fetch. Use -1 to fetch all configured records.'
                },
                'name': 'numRecords',
                'type': 'ViInt32'
            },
            {
                'default_value': 'datetime.timedelta(seconds=5.0)',
                'direction': 'in',
                'documentation': {
                    'description': 'The time to wait for data to be acquired; using 0 for this parameter tells NI-SCOPE to fetch whatever is currently available. Using -1 seconds for this parameter implies infinite timeout.'
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds',
                'type': 'ViReal64',
                'type_in_documentation': 'float in seconds or datetime.timedelta'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns an array of classes with the following timing and scaling information about each waveform:\n\n-  **relative_initial_x** (float) the time (in seconds) from the trigger to the first sample in the fetched waveform\n-  **absolute_initial_x** (float) timestamp (in seconds) of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output.\n-  **x_increment** (float) the time between points in the acquired waveform in seconds\n-  **channel** (str) channel name this waveform was asquire from\n-  **record** (int) record number of this waveform\n-  **gain** (float) the gain factor of the given channel; useful for scaling binary data with the following formula:\n\n    .. math::\n\n        voltage = binary data * gain factor + offset\n\n-  **offset** (float) the offset factor of the given channel; useful for scaling binary data with the following formula:\n\n    .. math::\n\n        voltage = binary data * gain factor + offset\n\n- **samples** (array of float) floating point array of samples. Length will be of the actual samples acquired\n'
                },
                'name': 'wfmInfo',
                'size': {
                    'mechanism': 'python-code',
                    'value': '(num_samples * self._actual_num_wfms())'
                },
                'type': 'struct niScope_wfmInfo[]'
            }
        ],
        'python_name': 'read',
        'returns': 'ViStatus'
    },
    'Fetch': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nReturns the waveform from a previously initiated acquisition that the\ndigitizer acquires for the specified channel. This function returns\nscaled voltage waveforms.\n\nThis function may return multiple waveforms depending on the number of\nchannels, the acquisition type, and the number of records you specify.\n',
            'note': '\nYou can use niScope_Read instead of this function. niScope_Read\nstarts an acquisition on all enabled channels, waits for the acquisition\nto complete, and returns the waveform for the specified channel.\n\nSome functionality, such as time stamping, is not supported in all\ndigitizers. Refer to `Features Supported by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for\nmore information.\n'
        },
        'method_name_for_documentation': 'fetch',
        'method_templates': [
            {
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            },
            {
                'method_python_name_suffix': '_into_numpy',
                'session_filename': 'numpy_read_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'default_value': 'datetime.timedelta(seconds=5.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe time to wait in seconds for data to be acquired; using 0 for this\nparameter tells NI-SCOPE to fetch whatever is currently available. Using\n-1 for this parameter implies infinite timeout.\n'
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds',
                'type': 'ViReal64',
                'type_in_documentation': 'float in seconds or datetime.timedelta'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe maximum number of samples to fetch for each waveform. If the\nacquisition finishes with fewer points than requested, some devices\nreturn partial data if the acquisition finished, was aborted, or a\ntimeout of 0 was used. If it fails to complete within the timeout\nperiod, the function returns an error.\n'
                },
                'name': 'numSamples',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns an array whose length is the **numSamples** times number of\nwaveforms. Call niScope_ActualNumwfms to determine the number of\nwaveforms.\n\nNI-SCOPE returns this data sequentially, so all record 0 waveforms are\nfirst. For example, with a channel list of 0,1, you would have the\nfollowing index values:\n\nindex 0 = record 0, channel 0\n\nindex *x* = record 0, channel 1\n\nindex 2\\ *x* = record 1, channel 0\n\nindex 3\\ *x* = record 1, channel 1\n\nWhere *x* = the record length\n'
                },
                'name': 'waveform',
                'numpy': True,
                'size': {
                    'mechanism': 'python-code',
                    'value': '(num_samples * self._actual_num_wfms())'
                },
                'type': 'ViReal64[]',
                'use_array': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns an array of structures with the following timing and scaling\ninformation about each waveform:\n\n-  **relativeInitialX**—the time (in seconds) from the trigger to the\n   first sample in the fetched waveform\n-  **absoluteInitialX**—timestamp (in seconds) of the first fetched\n   sample. This timestamp is comparable between records and\n   acquisitions; devices that do not support this parameter use 0 for\n   this output.\n-  **xIncrement**—the time between points in the acquired waveform in\n   seconds\n-  **actualSamples**—the actual number of samples fetched and placed in\n   the waveform array\n-  **gain**—the gain factor of the given channel; useful for scaling\n   binary data with the following formula:\n\nvoltage = binary data × gain factor + offset\n\n-  **offset**—the offset factor of the given channel; useful for scaling\n   binary data with the following formula:\n\nvoltage = binary data × gain factor + offset\n\nCall niScope_ActualNumWfms to determine the size of this array.\n'
                },
                'name': 'wfmInfo',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'self._actual_num_wfms()'
                },
                'type': 'struct niScope_wfmInfo[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchArrayMeasurement': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nObtains a waveform from the digitizer and returns the specified\nmeasurement array. This function may return multiple waveforms depending\non the number of channels, the acquisition type, and the number of\nrecords you specify.\n',
            'note': '\nSome functionality, such as time stamping, is not supported in all\ndigitizers. Refer to `Features Supported by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for\nmore information.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'default_value': 'datetime.timedelta(seconds=5.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe time to wait in seconds for data to be acquired; using 0 for this\nparameter tells NI-SCOPE to fetch whatever is currently available. Using\n-1 for this parameter implies infinite timeout.\n'
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds',
                'type': 'ViReal64',
                'type_in_documentation': 'float in seconds or datetime.timedelta'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe `array\nmeasurement <REPLACE_DRIVER_SPECIFIC_URL_2(array_measurements_refs)>`__\nto perform.\n'
                },
                'enum': 'ArrayMeasurement',
                'name': 'arrayMeasFunction',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe maximum number of samples returned in the measurement waveform array\nfor each waveform measurement. Use niScope_ActualMeasWfmSize to\ndetermine the number of available samples.\n',
                    'note': '\nUse the attribute NISCOPE_ATTR_FETCH_MEAS_NUM_SAMPLES to set the\nnumber of samples to fetch when performing a measurement. For more\ninformation about when to use this attribute, refer to the `NI\nKnowledgeBase <javascript:WWW(WWW_KB_MEAS)>`__.\n'
                },
                'name': 'measWfmSize',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'self._actual_meas_wfm_size(array_meas_function)'
                },
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns an array whose length is the number of waveforms times\n**measWfmSize**; call niScope_ActualNumWfms to determine the number of\nwaveforms; call niScope_ActualMeasWfmSize to determine the size of each\nwaveform.\n\nNI-SCOPE returns this data sequentially, so all record 0 waveforms are\nfirst. For example, with channel list of 0, 1, you would have the\nfollowing index values:\n\nindex 0 = record 0, channel 0\n\nindex *x* = record 0, channel 1\n\nindex 2\\ *x* = record 1, channel 0\n\nindex 3\\ *x* = record 1, channel 1\n\nWhere *x* = the record length\n'
                },
                'name': 'measWfm',
                'size': {
                    'mechanism': 'python-code',
                    'value': '(self._actual_meas_wfm_size(array_meas_function) * self._actual_num_wfms())'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns an array of structures with the following timing and scaling\ninformation about each waveform:\n\n-  **relativeInitialX**—the time (in seconds) from the trigger to the\n   first sample in the fetched waveform\n-  **absoluteInitialX**—timestamp (in seconds) of the first fetched\n   sample. This timestamp is comparable between records and\n   acquisitions; devices that do not support this parameter use 0 for\n   this output.\n-  **xIncrement**—the time between points in the acquired waveform in\n   seconds\n-  **actualSamples**—the actual number of samples fetched and placed in\n   the waveform array\n-  **gain**—the gain factor of the given channel; useful for scaling\n   binary data with the following formula:\n\nvoltage = binary data × gain factor + offset\n\n-  **offset**—the offset factor of the given channel; useful for scaling\n   binary data with the following formula:\n\nvoltage = binary data × gain factor + offset\n\nCall niScope_ActualNumWfms to determine the size of this array.\n'
                },
                'name': 'wfmInfo',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'self._actual_num_wfms()'
                },
                'type': 'struct niScope_wfmInfo[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchBinary16': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nRetrieves data from a previously initiated acquisition and returns\nbinary 16-bit waveforms. This function may return multiple waveforms\ndepending on the number of channels, the acquisition type, and the\nnumber of records you specify.\n\nRefer to `Using Fetch\nFunctions <REPLACE_DRIVER_SPECIFIC_URL_1(using_fetch_functions)>`__ for\nmore information on using this function.\n',
            'note': '\nSome functionality, such as time stamping, is not supported in all\ndigitizers. Refer to `Features Supported by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for\nmore information.\n'
        },
        'method_name_for_documentation': 'fetch_into',
        'method_templates': [
            {
                'method_python_name_suffix': '_into_numpy',
                'session_filename': 'numpy_read_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'default_value': 'datetime.timedelta(seconds=5.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe time to wait in seconds for data to be acquired; using 0 for this\nparameter tells NI-SCOPE to fetch whatever is currently available. Using\n-1 for this parameter implies infinite timeout.\n'
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds',
                'type': 'ViReal64',
                'type_in_documentation': 'float in seconds or datetime.timedelta'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe maximum number of samples to fetch for each waveform. If the\nacquisition finishes with fewer points than requested, some devices\nreturn partial data if the acquisition finished, was aborted, or a\ntimeout of 0 was used. If it fails to complete within the timeout\nperiod, the function returns an error.\n'
                },
                'name': 'numSamples',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns an array whose length is the **numSamples** times number of\nwaveforms. Call niScope_ActualNumwfms to determine the number of\nwaveforms.\n\nNI-SCOPE returns this data sequentially, so all record 0 waveforms are\nfirst. For example, with a channel list of 0,1, you would have the\nfollowing index values:\n\nindex 0 = record 0, channel 0\n\nindex *x* = record 0, channel 1\n\nindex 2\\ *x* = record 1, channel 0\n\nindex 3\\ *x* = record 1, channel 1\n\nWhere *x* = the record length\n'
                },
                'name': 'waveform',
                'numpy': True,
                'size': {
                    'mechanism': 'python-code',
                    'value': '(num_samples * self._actual_num_wfms())'
                },
                'type': 'ViInt16[]',
                'use_array': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns an array of structures with the following timing and scaling\ninformation about each waveform:\n\n-  **relativeInitialX**—the time (in seconds) from the trigger to the\n   first sample in the fetched waveform\n-  **absoluteInitialX**—timestamp (in seconds) of the first fetched\n   sample. This timestamp is comparable between records and\n   acquisitions; devices that do not support this parameter use 0 for\n   this output.\n-  **xIncrement**—the time between points in the acquired waveform in\n   seconds\n-  **actualSamples**—the actual number of samples fetched and placed in\n   the waveform array\n-  **gain**—the gain factor of the given channel; useful for scaling\n   binary data with the following formula:\n\nvoltage = binary data × gain factor + offset\n\n-  **offset**—the offset factor of the given channel; useful for scaling\n   binary data with the following formula:\n\nvoltage = binary data × gain factor + offset\n\nCall niScope_ActualNumWfms to determine the size of this array.\n'
                },
                'name': 'wfmInfo',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'self._actual_num_wfms()'
                },
                'type': 'struct niScope_wfmInfo[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchBinary16Waveform': {
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
                'name': 'retrievalOffset',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'waveformSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'waveformArray',
                'type': 'ViInt16'
            },
            {
                'direction': 'out',
                'name': 'actualPoints',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'initialX',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'xIncrement',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'gainFactor',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'verticalOffset',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchBinary32': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nRetrieves data from a previously initiated acquisition and returns\nbinary 32-bit waveforms. This function may return multiple waveforms\ndepending on the number of channels, the acquisition type, and the\nnumber of records you specify.\n\nRefer to `Using Fetch\nFunctions <REPLACE_DRIVER_SPECIFIC_URL_1(using_fetch_functions)>`__ for\nmore information on using this function.\n',
            'note': '\nSome functionality, such as time stamping, is not supported in all\ndigitizers. Refer to `Features Supported by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for\nmore information.\n'
        },
        'method_name_for_documentation': 'fetch_into',
        'method_templates': [
            {
                'method_python_name_suffix': '_into_numpy',
                'session_filename': 'numpy_read_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'default_value': 'datetime.timedelta(seconds=5.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe time to wait in seconds for data to be acquired; using 0 for this\nparameter tells NI-SCOPE to fetch whatever is currently available. Using\n-1 for this parameter implies infinite timeout.\n'
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds',
                'type': 'ViReal64',
                'type_in_documentation': 'float in seconds or datetime.timedelta'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe maximum number of samples to fetch for each waveform. If the\nacquisition finishes with fewer points than requested, some devices\nreturn partial data if the acquisition finished, was aborted, or a\ntimeout of 0 was used. If it fails to complete within the timeout\nperiod, the function returns an error.\n'
                },
                'name': 'numSamples',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns an array whose length is the **numSamples** times number of\nwaveforms. Call niScope_ActualNumwfms to determine the number of\nwaveforms.\n\nNI-SCOPE returns this data sequentially, so all record 0 waveforms are\nfirst. For example, with a channel list of 0,1, you would have the\nfollowing index values:\n\nindex 0 = record 0, channel 0\n\nindex *x* = record 0, channel 1\n\nindex 2\\ *x* = record 1, channel 0\n\nindex 3\\ *x* = record 1, channel 1\n\nWhere *x* = the record length\n'
                },
                'name': 'waveform',
                'numpy': True,
                'size': {
                    'mechanism': 'python-code',
                    'value': '(num_samples * self._actual_num_wfms())'
                },
                'type': 'ViInt32[]',
                'use_array': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns an array of structures with the following timing and scaling\ninformation about each waveform:\n\n-  **relativeInitialX**—the time (in seconds) from the trigger to the\n   first sample in the fetched waveform\n-  **absoluteInitialX**—timestamp (in seconds) of the first fetched\n   sample. This timestamp is comparable between records and\n   acquisitions; devices that do not support this parameter use 0 for\n   this output.\n-  **xIncrement**—the time between points in the acquired waveform in\n   seconds\n-  **actualSamples**—the actual number of samples fetched and placed in\n   the waveform array\n-  **gain**—the gain factor of the given channel; useful for scaling\n   binary data with the following formula:\n\nvoltage = binary data × gain factor + offset\n\n-  **offset**—the offset factor of the given channel; useful for scaling\n   binary data with the following formula:\n\nvoltage = binary data × gain factor + offset\n\nCall niScope_ActualNumWfms to determine the size of this array.\n'
                },
                'name': 'wfmInfo',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'self._actual_num_wfms()'
                },
                'type': 'struct niScope_wfmInfo[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchBinary32Waveform': {
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
                'name': 'retrievalOffset',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'waveformSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'waveformArray',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'actualPoints',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'initialX',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'xIncrement',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'gainFactor',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'verticalOffset',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchBinary8': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nRetrieves data from a previously initiated acquisition and returns\nbinary 8-bit waveforms. This function may return multiple waveforms\ndepending on the number of channels, the acquisition type, and the\nnumber of records you specify.\n\nRefer to `Using Fetch\nFunctions <REPLACE_DRIVER_SPECIFIC_URL_1(using_fetch_functions)>`__ for\nmore information on using this function.\n',
            'note': '\nSome functionality, such as time stamping, is not supported in all\ndigitizers. Refer to `Features Supported by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for\nmore information.\n'
        },
        'method_name_for_documentation': 'fetch_into',
        'method_templates': [
            {
                'method_python_name_suffix': '_into_numpy',
                'session_filename': 'numpy_read_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'default_value': 'datetime.timedelta(seconds=5.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe time to wait in seconds for data to be acquired; using 0 for this\nparameter tells NI-SCOPE to fetch whatever is currently available. Using\n-1 for this parameter implies infinite timeout.\n'
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds',
                'type': 'ViReal64',
                'type_in_documentation': 'float in seconds or datetime.timedelta'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe maximum number of samples to fetch for each waveform. If the\nacquisition finishes with fewer points than requested, some devices\nreturn partial data if the acquisition finished, was aborted, or a\ntimeout of 0 was used. If it fails to complete within the timeout\nperiod, the function returns an error.\n'
                },
                'name': 'numSamples',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns an array whose length is the **numSamples** times number of\nwaveforms. Call niScope_ActualNumwfms to determine the number of\nwaveforms.\n\nNI-SCOPE returns this data sequentially, so all record 0 waveforms are\nfirst. For example, with a channel list of 0,1, you would have the\nfollowing index values:\n\nindex 0 = record 0, channel 0\n\nindex *x* = record 0, channel 1\n\nindex 2\\ *x* = record 1, channel 0\n\nindex 3\\ *x* = record 1, channel 1\n\nWhere *x* = the record length\n'
                },
                'name': 'waveform',
                'numpy': True,
                'size': {
                    'mechanism': 'python-code',
                    'value': '(num_samples * self._actual_num_wfms())'
                },
                'type': 'ViInt8[]',
                'use_array': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns an array of structures with the following timing and scaling\ninformation about each waveform:\n\n-  **relativeInitialX**—the time (in seconds) from the trigger to the\n   first sample in the fetched waveform\n-  **absoluteInitialX**—timestamp (in seconds) of the first fetched\n   sample. This timestamp is comparable between records and\n   acquisitions; devices that do not support this parameter use 0 for\n   this output.\n-  **xIncrement**—the time between points in the acquired waveform in\n   seconds\n-  **actualSamples**—the actual number of samples fetched and placed in\n   the waveform array\n-  **gain**—the gain factor of the given channel; useful for scaling\n   binary data with the following formula:\n\nvoltage = binary data × gain factor + offset\n\n-  **offset**—the offset factor of the given channel; useful for scaling\n   binary data with the following formula:\n\nvoltage = binary data × gain factor + offset\n\nCall niScope_ActualNumWfms to determine the size of this array.\n'
                },
                'name': 'wfmInfo',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'self._actual_num_wfms()'
                },
                'type': 'struct niScope_wfmInfo[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchBinary8Waveform': {
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
                'name': 'retrievalOffset',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'waveformSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'waveformArray',
                'type': 'ViInt8'
            },
            {
                'direction': 'out',
                'name': 'actualPoints',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'initialX',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'xIncrement',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'gainFactor',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'verticalOffset',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchComplex': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nRetrieves data that the digitizer has acquired from a previously\ninitiated acquisition and returns a one-dimensional array of complex,\nscaled waveforms.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe time to wait in seconds for data to be acquired; using 0 for this\nparameter tells NI-SCOPE to fetch whatever is currently available. Using\n-1 for this parameter implies infinite timeout.\n'
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds',
                'type': 'ViReal64',
                'type_in_documentation': 'float in seconds or datetime.timedelta'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe maximum number of samples to fetch for each waveform. If the\nacquisition finishes with fewer points than requested, some devices\nreturn partial data if the acquisition finished, was aborted, or a\ntimeout of 0 was used. If it fails to complete within the timeout\nperiod, the function returns an error.\n'
                },
                'name': 'numSamples',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns an array whose length is the **numSamples** times number of\nwaveforms. Call niScope_ActualNumwfms to determine the number of\nwaveforms.\n'
                },
                'name': 'wfm',
                'size': {
                    'mechanism': 'python-code',
                    'value': None
                },
                'type': 'NIComplexNumber[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns an array of structures with the following timing and scaling\ninformation about each waveform:\n\n-  **relativeInitialX**—the time (in seconds) from the trigger to the\n   first sample in the fetched waveform\n-  **absoluteInitialX**—timestamp (in seconds) of the first fetched\n   sample. This timestamp is comparable between records and\n   acquisitions; devices that do not support this parameter use 0 for\n   this output.\n-  **xIncrement**—the time between points in the acquired waveform in\n   seconds\n-  **actualSamples**—the actual number of samples fetched and placed in\n   the waveform array\n-  **gain**—the gain factor of the given channel; useful for scaling\n   binary data with the following formula:\n\nvoltage = binary data × gain factor + offset\n\n-  **offset**—the offset factor of the given channel; useful for scaling\n   binary data with the following formula:\n\nvoltage = binary data × gain factor + offset\n\nCall niScope_ActualNumWfms to determine the size of this array.\n'
                },
                'name': 'wfmInfo',
                'size': {
                    'mechanism': 'python-code',
                    'value': None
                },
                'type': 'struct niScope_wfmInfo[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchComplexBinary16': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nRetrieves data from single channels and records. Returns a\none-dimensional array of complex binary 16-bit waveforms.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe time to wait in seconds for data to be acquired; using 0 for this\nparameter tells NI-SCOPE to fetch whatever is currently available. Using\n-1 for this parameter implies infinite timeout.\n'
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds',
                'type': 'ViReal64',
                'type_in_documentation': 'float in seconds or datetime.timedelta'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe maximum number of samples to fetch for each waveform. If the\nacquisition finishes with fewer points than requested, some devices\nreturn partial data if the acquisition finished, was aborted, or a\ntimeout of 0 was used. If it fails to complete within the timeout\nperiod, the function returns an error.\n'
                },
                'name': 'numSamples',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns an array whose length is the **numSamples** times number of\nwaveforms. Call niScope_ActualNumwfms to determine the number of\nwaveforms.\n'
                },
                'name': 'wfm',
                'size': {
                    'mechanism': 'python-code',
                    'value': None
                },
                'type': 'NIComplexI16[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns an array of structures with the following timing and scaling\ninformation about each waveform:\n\n-  **relativeInitialX**—the time (in seconds) from the trigger to the\n   first sample in the fetched waveform\n-  **absoluteInitialX**—timestamp (in seconds) of the first fetched\n   sample. This timestamp is comparable between records and\n   acquisitions; devices that do not support this parameter use 0 for\n   this output.\n-  **xIncrement**—the time between points in the acquired waveform in\n   seconds\n-  **actualSamples**—the actual number of samples fetched and placed in\n   the waveform array\n-  **gain**—the gain factor of the given channel; useful for scaling\n   binary data with the following formula:\n\nvoltage = binary data × gain factor + offset\n\n-  **offset**—the offset factor of the given channel; useful for scaling\n   binary data with the following formula:\n\nvoltage = binary data × gain factor + offset\n\nCall niScope_ActualNumWfms to determine the size of this array.\n'
                },
                'name': 'wfmInfo',
                'size': {
                    'mechanism': 'python-code',
                    'value': None
                },
                'type': 'struct niScope_wfmInfo[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchDispatcher': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': '\nReturns the waveform from a previously initiated acquisition that the\ndigitizer acquires for the specified channel. This function returns\nscaled voltage waveforms.\n\nThis function may return multiple waveforms depending on the number of\nchannels, the acquisition type, and the number of records you specify.',
            'note': 'Some functionality, such as time stamping, is not supported in all digitizers.'
        },
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '_into',
                'session_filename': 'fetch_waveform'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The instrument handle you obtain from niScope_init that identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The channel(s) to fetch from.'
                },
                'name': 'channelList',
                'type': 'ViString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nnumpy array of the appropriate type and size the should be acquired as a 1D array. Size should be **num_samples** times number of waveforms. Call niScope_ActualNumWfms to determine the number of waveforms.\n\nTypes supported are\n\n- `numpy.float64`\n- `numpy.int8`\n- `numpy.in16`\n- `numpy.int32`\n\nExample:\n\n.. code-block:: python\n\n    waveform = numpy.ndarray(num_samples * session.actual_num_wfms(), dtype=numpy.float64)\n    wfm_info = session['0,1'].fetch_into(num_samples, waveform, timeout=5.0)"
                },
                'name': 'waveform',
                'numpy': True,
                'type': 'ViReal64',
                'use_array': True
            },
            {
                'default_value': 'FetchRelativeTo.PRETRIGGER',
                'direction': 'in',
                'documentation': {
                    'description': 'Position to start fetching within one record.'
                },
                'enum': 'FetchRelativeTo',
                'name': 'relativeTo',
                'type': 'ViInt32'
            },
            {
                'default_value': 0,
                'direction': 'in',
                'documentation': {
                    'description': 'Offset in samples to start fetching data within each record.The offset can be positive or negative.'
                },
                'name': 'offset',
                'type': 'ViInt32'
            },
            {
                'default_value': 0,
                'direction': 'in',
                'documentation': {
                    'description': 'Zero-based index of the first record to fetch.'
                },
                'name': 'recordNumber',
                'type': 'ViInt32'
            },
            {
                'default_value': None,
                'direction': 'in',
                'documentation': {
                    'description': 'Number of records to fetch. Use -1 to fetch all configured records.'
                },
                'name': 'numRecords',
                'type': 'ViInt32'
            },
            {
                'default_value': 'datetime.timedelta(seconds=5.0)',
                'direction': 'in',
                'documentation': {
                    'description': 'The time to wait in seconds for data to be acquired; using 0 for this parameter tells NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout.'
                },
                'name': 'timeout',
                'type': 'ViReal64',
                'type_in_documentation': 'float in seconds or datetime.timedelta'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns an array of classed with the following timing and scaling information about each waveform:\n\n-  **relative_initial_x** (float) the time (in seconds) from the trigger to the first sample in the fetched waveform\n-  **absolute_initial_x** (float) timestamp (in seconds) of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output.\n-  **x_increment** (float) the time between points in the acquired waveform in seconds\n-  **channel** (str) channel name this waveform was asquire from\n-  **record** (int) record number of this waveform\n-  **gain** (float) the gain factor of the given channel; useful for scaling binary data with the following formula:\n\n    .. math::\n\n        voltage = binary data * gain factor + offset\n\n-  **offset** (float) the offset factor of the given channel; useful for scaling binary data with the following formula:\n\n    .. math::\n\n        voltage = binary data * gain factor + offset\n\n- **samples** (array of float) floating point array of samples. Length will be of the actual samples acquired\n'
                },
                'name': 'wfmInfo',
                'type': 'struct niScope_wfmInfo'
            }
        ],
        'python_name': 'fetch',
        'returns': 'ViStatus'
    },
    'FetchMeasurement': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nFetches a waveform from the digitizer and performs the specified\nwaveform measurement. Refer to `Using Fetch\nFunctions <REPLACE_DRIVER_SPECIFIC_URL_1(using_fetch_functions)>`__ for\nmore information.\n\nMany of the measurements use the low, mid, and high reference levels.\nYou configure the low, mid, and high references by using\nNISCOPE_ATTR_MEAS_CHAN_LOW_REF_LEVEL,\nNISCOPE_ATTR_MEAS_CHAN_MID_REF_LEVEL, and\nNISCOPE_ATTR_MEAS_CHAN_HIGH_REF_LEVEL to set each channel\ndifferently.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'default_value': 'datetime.timedelta(seconds=5.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe time to wait in seconds for data to be acquired; using 0 for this\nparameter tells NI-SCOPE to fetch whatever is currently available. Using\n-1 for this parameter implies infinite timeout.\n'
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds',
                'type': 'ViReal64',
                'type_in_documentation': 'float in seconds or datetime.timedelta'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe `scalar\nmeasurement <REPLACE_DRIVER_SPECIFIC_URL_2(scalar_measurements_refs)>`__\nto be performed.\n'
                },
                'enum': 'ScalarMeasurement',
                'name': 'scalarMeasFunction',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nContains an array of all measurements acquired; call\nniScope_ActualNumWfms to determine the array length.\n'
                },
                'name': 'result',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'self._actual_num_wfms()'
                },
                'type': 'ViReal64[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchMeasurementStats': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nObtains a waveform measurement and returns the measurement value. This\nfunction may return multiple statistical results depending on the number\nof channels, the acquisition type, and the number of records you\nspecify.\n\nYou specify a particular measurement type, such as rise time, frequency,\nor voltage peak-to-peak. The waveform on which the digitizer calculates\nthe waveform measurement is from an acquisition that you previously\ninitiated. The statistics for the specified measurement function are\nreturned, where the statistics are updated once every acquisition when\nthe specified measurement is fetched by any of the Fetch Measurement\nfunctions. If a Fetch Measurement function has not been called, this\nfunction fetches the data on which to perform the measurement. The\nstatistics are cleared by calling\nniScope_ClearWaveformMeasurementStats. Refer to `Using Fetch\nFunctions <REPLACE_DRIVER_SPECIFIC_URL_1(using_fetch_functions)>`__ for\nmore information on incorporating fetch functions in your application.\n\nMany of the measurements use the low, mid, and high reference levels.\nYou configure the low, mid, and high references with\nNISCOPE_ATTR_MEAS_CHAN_LOW_REF_LEVEL,\nNISCOPE_ATTR_MEAS_CHAN_MID_REF_LEVEL, and\nNISCOPE_ATTR_MEAS_CHAN_HIGH_REF_LEVEL to set each channel\ndifferently.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'default_value': 'datetime.timedelta(seconds=5.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe time to wait in seconds for data to be acquired; using 0 for this\nparameter tells NI-SCOPE to fetch whatever is currently available. Using\n-1 for this parameter implies infinite timeout.\n'
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds',
                'type': 'ViReal64',
                'type_in_documentation': 'float in seconds or datetime.timedelta'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe `scalar\nmeasurement <REPLACE_DRIVER_SPECIFIC_URL_2(scalar_measurements_refs)>`__\nto be performed on each fetched waveform.\n'
                },
                'enum': 'ScalarMeasurement',
                'name': 'scalarMeasFunction',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the resulting measurement'
                },
                'name': 'result',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'self._actual_num_wfms()'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the mean scalar value, which is obtained by averaging each\nniScope_FetchMeasurementStats call.\n'
                },
                'name': 'mean',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'self._actual_num_wfms()'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the standard deviation of the most recent **numInStats**\nmeasurements.\n'
                },
                'name': 'stdev',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'self._actual_num_wfms()'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the smallest scalar value acquired (the minimum of the\n**numInStats** measurements).\n'
                },
                'name': 'min',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'self._actual_num_wfms()'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the largest scalar value acquired (the maximum of the\n**numInStats** measurements).\n'
                },
                'name': 'max',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'self._actual_num_wfms()'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the number of times niScope_FetchMeasurementStats has been\ncalled.\n'
                },
                'name': 'numInStats',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'self._actual_num_wfms()'
                },
                'type': 'ViInt32[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchMinMaxWaveform': {
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
                'name': 'waveformSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'minWaveform',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'in',
                'name': 'maxWaveform',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'out',
                'name': 'actualPoints',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'initialX',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'xIncrement',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchMultiBinary16Waveform': {
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
                'name': 'recordNumber',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'retrievalOffset',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'waveformSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'waveformArray',
                'type': 'ViInt16'
            },
            {
                'direction': 'out',
                'name': 'actualPoints',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'initialX',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'xIncrement',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'gainFactor',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'verticalOffset',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchMultiBinary32Waveform': {
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
                'name': 'recordNumber',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'retrievalOffset',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'waveformSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'waveformArray',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'actualPoints',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'initialX',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'xIncrement',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'gainFactor',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'verticalOffset',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchMultiBinary8Waveform': {
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
                'name': 'recordNumber',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'retrievalOffset',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'waveformSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'waveformArray',
                'type': 'ViInt8'
            },
            {
                'direction': 'out',
                'name': 'actualPoints',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'initialX',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'xIncrement',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'gainFactor',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'verticalOffset',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchMultiMinMaxWaveform': {
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
                'name': 'recordNumber',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'retrievalOffset',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'waveformSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'minWaveform',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'in',
                'name': 'maxWaveform',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'out',
                'name': 'actualPoints',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'initialX',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'xIncrement',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchMultiWaveform': {
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
                'name': 'recordNumber',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'retrievalOffset',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'waveformSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'waveformArray',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'actualPoints',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'initialX',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'xIncrement',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchMultiWaveformMeasurement': {
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
                'name': 'channel',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'recordNumber',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'measFunction',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'measurement',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchWaveform': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nReturns the waveform from a previously initiated acquisition that the\ndigitizer acquires for the channel you specify.\n\nniScope_InitiateAcquisition starts an acquisition on the channels that\nyou enable with niScope_ConfigureVertical. The digitizer acquires\nwaveforms for the enabled channels concurrently. You use\nniScope_AcquisitionStatus to determine when the acquisition is\ncomplete. You must call this function separately for each enabled\nchannel to obtain the waveforms.\n\nYou can call niScope_ReadWaveform instead of\nniScope_InitiateAcquisition. niScope_ReadWaveform starts an\nacquisition on all enabled channels, waits for the acquisition to\ncomplete, and returns the waveform for the channel you specify. Call\nthis function to obtain the waveforms for each of the remaining\nchannels.\n',
            'note': '\nThis function is included for compliance with the IviScope Class\nSpecification.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe channel to configure. For more information, refer to `channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm\',\'cvichannelstringsyntaxforc)>`__.\n\nDefault Value: "0"\n'
                },
                'name': 'channel',
                'type': 'ViString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The number of elements to insert into the **waveform** array.'
                },
                'name': 'waveformSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the waveform that the digitizer acquires.\n\nUnits: volts\n\n| Notes:\n| If the digitizer cannot sample a point in the waveform, this function\n  returns an error.\n'
                },
                'name': 'waveform',
                'size': {
                    'mechanism': 'python-code',
                    'value': None
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nIndicates the actual number of points the function placed in the\n**waveform** array.\n'
                },
                'name': 'actualPoints',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nIndicates the time of the first point in the **waveform** array relative\nto the Reference Position.\n\nUnits: seconds\n\nFor example, if the digitizer acquires the first point in the\n**waveform** array 1 second before the trigger, this parameter returns\nthe value –1.0. If the acquisition of the first point occurs at the same\ntime as the trigger, this parameter returns the value 0.0.\n'
                },
                'name': 'initialX',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nIndicates the length of time between points in the **waveform** array.\n\nUnits: seconds\n'
                },
                'name': 'xIncrement',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchWaveformFromOffset': {
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
                'name': 'retrievalOffset',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'waveformSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'waveformArray',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'actualPoints',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'initialX',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'xIncrement',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchWaveformMeasurement': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nConfigure the appropriate reference levels before calling this function.\nYou can configure the low, mid, and high references by setting the\nfollowing attributes:\n\n| NISCOPE_ATTR_MEAS_HIGH_REF\n| NISCOPE_ATTR_MEAS_LOW_REF\n| NISCOPE_ATTR_MEAS_MID_REF\n',
            'note': '\nThis function is included for compliance with the IviScope Class\nSpecification.\n\nYou can use niScope_ReadWaveformMeasurement instead of this function.\nniScope_ReadWaveformMeasurement starts an acquisition on all enabled\nchannels, waits for the acquisition to complete, obtains a waveform\nmeasurement on the specified channel, and returns the waveform for the\nspecified channel. Call this function separately to obtain any other\nwaveform measurements on a specific channel.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe channel to configure. For more information, refer to `channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm\',\'cvichannelstringsyntaxforc)>`__.\n\nDefault Value: "0"\n'
                },
                'name': 'channel',
                'type': 'ViString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Characteristic of the acquired waveform to be measured.'
                },
                'name': 'measFunction',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The measured value.'
                },
                'name': 'measurement',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchWaveformMeasurementArray': {
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
                'name': 'channel',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'recordNumber',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'measFunction',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'measArraySize',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'measArray',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'out',
                'name': 'actualPoints',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'initialX',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'xIncrement',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchWaveformMeasurementStats': {
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
                'name': 'channel',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'recordNumber',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'measFunction',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'measurement',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'mean',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'stdev',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'min',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'max',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'numInStats',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'FlushEepromMap': {
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
                'name': 'option',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'whichEeprom',
                'type': 'ViInt32'
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
                'name': 'flags',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'supported',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViBoolean': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nQueries the value of a ViBoolean attribute. You can use this function to\nget the values of instrument-specific attributes and inherent IVI\nattributes. If the attribute represents an instrument state, this\nfunction performs instrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled and the currently cached value is invalid.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the current value of the attribute; pass the address of a\nViBoolean variable.\n'
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
            'description': '\nQueries the value of a ViInt32 attribute. You can use this function to\nget the values of instrument-specific attributes and inherent IVI\nattributes. If the attribute represents an instrument state, this\nfunction performs instrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled and the currently cached value is invalid.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the current value of the attribute.'
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
            'description': '\nQueries the value of a ViInt64 attribute. You can use this function to\nget the values of instrument-specific attributes and inherent IVI\nattributes. If the attribute represents an instrument state, this\nfunction performs instrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled and the currently cached value is invalid.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the current value of the attribute.'
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
            'description': '\nQueries the value of a ViReal64 attribute. You can use this function to\nget the values of instrument-specific attributes and inherent IVI\nattributes. If the attribute represents an instrument state, this\nfunction performs instrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled and the currently cached value is invalid.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the current value of the attribute; pass the address of a\nViReal64 variable.\n'
                },
                'name': 'value',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViSession': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nQueries the value of a ViSession attribute. You can use this function to\nget the values of instrument-specific attributes and inherent IVI\nattributes. If the attribute represents an instrument state, this\nfunction performs instrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled and the currently cached value is invalid.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the current value of the attribute; pass the address of a\nViSession variable.\n'
                },
                'name': 'value',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViString': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nQueries the value of a ViString attribute. You can use this function to\nget the values of instrument-specific attributes and inherent IVI\nattributes. If the attribute represents an instrument state, this\nfunction performs instrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled and the currently cached value is invalid.\n\nYou must provide a ViChar array to serve as a buffer for the value. You\npass the number of bytes in the buffer as the **bufSize**. If the\ncurrent value of the attribute, including the terminating NUL byte, is\nlarger than the size you indicate in the **bufSize**, the function\ncopies (**bufSize** – 1) bytes into the buffer, places an ASCII NUL byte\nat the end of the buffer, and returns the **bufSize** you must pass to\nget the entire value. For example, if the value is 123456 and the\n**bufSize** is 4, the function places 123 into the buffer and returns 7.\nIf you want to call this function just to get the required buffer size,\nyou can pass 0 for the **bufSize** and VI_NULL for the **value**.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The number of bytes in the ViChar array you specify for **value**.'
                },
                'name': 'bufSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe buffer in which the function returns the current value of the\nattribute; the buffer must be of type ViChar and have at least as many\nbytes as indicated in the **bufSize**.\n'
                },
                'name': 'value',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufSize'
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
                'name': 'channelList',
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
                'name': 'channelList',
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
                'name': 'channelList',
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
                'name': 'channelList',
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
                'name': 'channelList',
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
                'name': 'channelList',
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
    'GetChannelName': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nReturns the channel string that is in the channel table at an index you\nspecify. Not applicable to National Instruments digitizers.\n',
            'note': '\nThis function is included for compliance with the IviScope Class\nSpecification.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'A 1-based index into the channel table.'
                },
                'name': 'index',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPasses the number of bytes in the ViChar array you specify for the\n**description** parameter.\n\nIf the error description, including the terminating NULL byte, contains\nmore bytes than you indicate in this parameter, the function copies\nBufferSize - 1 bytes into the buffer, places an ASCII NULL byte at the\nend of the buffer, and returns the buffer size you must pass to get the\nentire value. For example, if the value is "123456" and the Buffer Size\nis 4, the function places "123" into the buffer and returns 7.\n\nIf you pass a negative number, the function copies the value to the\nbuffer regardless of the number of bytes in the value.\n'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the channel string that is in the channel table at the index you\nspecify. Do not modify the contents of the channel string.\n'
                },
                'name': 'channelString',
                'size': {
                    'mechanism': 'python-code',
                    'value': None
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
                'name': 'name',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetConfiguredEepromFields': {
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
                'name': 'fields',
                'type': 'ViChar[]'
            },
            {
                'direction': 'in',
                'name': 'numFields',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'maxLength',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'whichEeprom',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetEepromMap': {
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
                'name': 'mapText',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViString[]'
            },
            {
                'direction': 'in',
                'name': 'mapTextLength',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'name': 'whichEeprom',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetEepromMapName': {
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
                'name': 'field',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'name': 'name',
                'type': 'ViChar[]'
            },
            {
                'direction': 'in',
                'name': 'maxLength',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'whichEeprom',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetEepromMapValue': {
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
                'name': 'field',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'whichEeprom',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetElaborationString': {
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
                'name': 'stringCode',
                'type': 'ViStatus'
            },
            {
                'direction': 'in',
                'name': 'errorBufferSize',
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
    'GetEqualizationFilterCoefficients': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nRetrieves the custom coefficients for the equalization FIR filter on the\ndevice. This filter is designed to compensate the input signal for\nartifacts introduced to the signal outside of the digitizer. Because\nthis filter is a generic FIR filter, any coefficients are valid.\nCoefficient values should be between +1 and –1.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channel',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The number of coefficients being passed in the **coefficients** array.'
                },
                'name': 'numberOfCoefficients',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe custom coefficients for the equalization FIR filter on the device.\nThese coefficients should be between +1 and –1. You can obtain the\nnumber of coefficients from the\n`NISCOPE_ATTR_EQUALIZATION_NUM_COEFFICIENTS <cviNISCOPE_ATTR_EQUALIZATION_NUM_COEFFICIENTS.html>`__\nattribute.\n'
                },
                'name': 'coefficients',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfCoefficients'
                },
                'type': 'ViReal64[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetError': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nReads an error code and message from the error queue. National\nInstruments digitizers do not contain an error queue. Errors are\nreported as they occur. Therefore, this function does not detect errors.\n',
            'note': '\nThis function is included for compliance with the IviScope Class\nSpecification.\n'
        },
        'is_error_handling': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nPasses the number of bytes in the ViChar array you specify for the\nDescription parameter.\n\nIf the error description, including the terminating NULL byte, contains\nmore bytes than you indicate in this parameter, the function copies\n**bufferSize** – 1 bytes into the buffer, places an ASCII NULL byte at\nthe end of the buffer, and returns the buffer size you must pass to get\nthe entire value. For example, if the value is "123456" and the Buffer\nSize is 4, the function places "123" into the buffer and returns 7.\n\nIf you pass a negative number, the function copies the value to the\nbuffer regardless of the number of bytes in the value.\n\nIf you pass 0, you can pass VI_NULL for the **description** parameter.\n'
                },
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the Error Code that is returned from any of the instrument driver\nfunctions.\n'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the error description for the IVI session or execution thread.\n\nIf there is no description, the function returns an empty string. The\nbuffer must contain at least as many elements as the value you specify\nwith the Buffer Size parameter.\n\nIf you pass 0 for the **bufferSize**, you can pass VI_NULL for this\nparameter.\n'
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
                'type': 'ViString[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetErrorMessage': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nReturns the error code from an NI-SCOPE function as a user-readable\nstring. Use VI_NULL as the default instrument handle.\n\nYou must call this function twice. For the first call, set\n**bufferSize** to 0 to prevent the function from populating the error\nmessage. Instead, the function returns the size of the error string. Use\nthe returned size to create a buffer, then call the function again,\npassing in the new buffer and setting **bufferSize** equal to the size\nthat was returned in the first function call.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe error code that is returned from any of the instrument driver\nfunctions.\n'
                },
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The number of characters you specify for the **errorMessage** parameter.'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns a char buffer that will be populated with the error message. It\nshould be at least as large as the buffer size.\n'
                },
                'name': 'errorMessage',
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetErrorMessageWithLanguage': {
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
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
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
            },
            {
                'direction': 'in',
                'name': 'language',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetFrequencyResponse': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nGets the frequency response of the digitizer for the current\nconfigurations of the channel attributes. Not all digitizers support\nthis function.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channel',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe array size for the frequencies, amplitudes, and phases arrays that\nyou pass in to the other parameters.\n\nTo determine the sizes of the buffers to allocate for the frequencies,\namplitudes, and phases arrays, pass a value of 0 to the **buffer_size**\nparameter and a value of NULL to the **frequencies** parameter. In this\ncase, the value returned by the **numberOfFrequencies** parameter is the\nsize of the arrays necessary to hold the frequencies, amplitudes, and\nphases. Allocate three arrays of this size, then call this function\nagain (with correct **buffer_size** parameter) to retrieve the actual\nvalues.\n'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe array of frequencies that corresponds with the amplitude and phase\nresponse of the device.\n'
                },
                'name': 'frequencies',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViReal64[]',
                'use_array': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe array of amplitudes that correspond with the magnitude response of\nthe device.\n'
                },
                'name': 'amplitudes',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViReal64[]',
                'use_array': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe array of phases that correspond with the phase response of the\ndevice.\n'
                },
                'name': 'phases',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViReal64[]',
                'use_array': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the number of frequencies in the returned spectrum.'
                },
                'name': 'numberOfFrequencies',
                'type': 'ViInt32',
                'use_in_python_api': False
            }
        ],
        'returns': 'ViStatus'
    },
    'GetGlobalLanguage': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'TBD'
        },
        'parameters': [
        ],
        'returns': 'ViInt32'
    },
    'GetNextCoercionRecord': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nReturns the coercion information associated with the IVI session. This\nfunction retrieves and clears the oldest instance in which the\ninstrument driver coerced a value you specified to another value.\n\nIf you set NISCOPE_ATTR_RECORD_COERCIONS to VI_TRUE, NI-SCOPE keeps\na list of all coercions it makes on ViInt32 or ViReal64 values that you\npass to instrument driver functions. Use this function to retrieve\ninformation from that list.\n',
            'note': '\nThis function is included for compliance with the IviScope Class\nSpecification.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPasses the number of bytes in the ViChar array you specify for the\nDescription parameter.\n\nIf the error description, including the terminating NULL byte, contains\nmore bytes than you indicate in this parameter, the function copies\n**bufferSize** – 1 bytes into the buffer, places an ASCII NULL byte at\nthe end of the buffer, and returns the buffer size you must pass to get\nthe entire value. For example, if the value is "123456" and the\n**bufferSize** is 4, the function places "123" into the buffer and\nreturns 7.\n\nIf you pass a negative number, the function copies the value to the\nbuffer regardless of the number of bytes in the value.\n\nIf you pass 0, you can pass VI_NULL for the Description buffer\nparameter.\n'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the next coercion record for the IVI session. If there are no\ncoercions records, the function returns an empty string. The buffer must\ncontain at least as many elements as the value you specify with the\n**bufferSize** parameter.\n'
                },
                'name': 'record',
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetNextInterchangeWarning': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nReturns the interchangeability warnings associated with the IVI session.\nIt retrieves and clears the oldest instance in which the class driver\nrecorded an interchangeability warning. Interchangeability warnings\nindicate that using your application with a different instrument might\ncause different behavior.\n\nUse this function to retrieve interchangeability warnings. The driver\nperforms interchangeability checking when\nNISCOPE_ATTR_INTERCHANGE_CHECK is set to VI_TRUE. The function\nreturns an empty string in the **interchangeWarning** parameter if no\ninterchangeability warnings remain for the session.\n\nIn general, the instrument driver generates interchangeability warnings\nwhen an attribute that affects the behavior of the instrument is in a\nstate that you did not specify.\n',
            'note': '\nThis function is included for compliance with the IviScope Class\nSpecification.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPasses the number of bytes in the ViChar array you specify for the\n**Description** parameter.\n\nIf the error description, including the terminating NULL byte, contains\nmore bytes than you indicate in this parameter, the function copies\n**bufferSize**; – 1 bytes into the buffer, places an ASCII NULL byte at\nthe end of the buffer, and returns the buffer size you must pass to get\nthe entire value. For example, if the value is "123456" and the Buffer\nSize is 4, the function places "123" into the buffer and returns 7.\n\nIf you pass a negative number, the function copies the value to the\nbuffer regardless of the number of bytes in the value.\n\nIf you pass 0, you can pass VI_NULL for the Description buffer\nparameter.\n'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the next interchange warning for the IVI session. If there are\nno interchange warnings, the function returns an empty string. The\nbuffer must contain at least as many elements as the value you specify\nwith the **bufferSize** parameter.\n'
                },
                'name': 'interchangeWarning',
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetNormalizationCoefficients': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nReturns coefficients that can be used to convert binary data to\nnormalized and calibrated data.\n\nRefer to `Scaling and Normalization of Binary\nData <Digitizers.chm::/scaling_and_norm_binary_data.html>`__ for more\ninformation about how to use this function.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe array size for the **coefficentInfo** parameter.\n\nTo determine the size of the buffer to allocate for **coefficientInfo**,\npass a value of 0 to the **buffersize** parameter and a value of NULL to\nthe **coefficientInfo** parameter. In this case, the return value of the\n**numberOfCoefficientSets** parameter is the size of the array necessary\nto hold the coefficient structures. Allocate an array of\nniScope_coefficientInfo structures of this size, then call this\nfunction again (with the correct **bufferSize** parameter) to retrieve\nthe actual values.\n'
                },
                'name': 'arraySize',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nAn array of structures containing gain and offset coefficients for a\ngiven channel.\n'
                },
                'name': 'coefficientInfo',
                'type': 'void'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the number of coefficient sets returned in the\n**coefficientInfo** array.\n'
                },
                'name': 'numberOfCoefficientSets',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetNumberOfEepromFields': {
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
                'name': 'numberOfFields',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'maxFieldNameLength',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'whichEeprom',
                'type': 'ViInt32'
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
    'GetRefTrigMasterTsCorrection': {
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
                'name': 'recordNum',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'num',
                'type': 'ViUInt64'
            },
            {
                'direction': 'out',
                'name': 'den',
                'type': 'ViUInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetScalingCoefficients': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nReturns coefficients that can be used to scale binary data to volts.\n\nRefer to `Scaling and Normalization of Binary\nData <Digitizers.chm::/scaling_and_norm_binary_data.html>`__ for more\ninformation about how to use this function.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe array size for the **coefficentInfo** parameter.\n\nTo determine the size of the buffer to allocate for **coefficientInfo**,\npass a value of 0 to the **buffersize** parameter and a value of NULL to\nthe **coefficientInfo** parameter. In this case, the return value of the\n**numberOfCoefficientSets** parameter is the size of the array necessary\nto hold the coefficient structures. Allocate an array of\nniScope_coefficientInfo structures of this size, then call this\nfunction again (with the correct **bufferSize** parameter) to retrieve\nthe actual values.\n'
                },
                'name': 'arraySize',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nAn array of structures containing gain and offset coefficients for a\ngiven channel.\n'
                },
                'name': 'coefficientInfo',
                'type': 'void'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the number of coefficient sets returned in the\n**coefficientInfo** array.\n'
                },
                'name': 'numberOfCoefficientSets',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetStartTimestampInformation': {
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
                'name': 'sysTimeIn128BitsT1',
                'type': 'ViUInt32'
            },
            {
                'direction': 'out',
                'name': 'sysTimeIn128BitsT2',
                'type': 'ViUInt32'
            },
            {
                'direction': 'out',
                'name': 'sysTimeIn128BitsT3',
                'type': 'ViUInt32'
            },
            {
                'direction': 'out',
                'name': 'sysTimeIn128BitsT4',
                'type': 'ViUInt32'
            },
            {
                'direction': 'out',
                'name': 'deviceTimeInAbsoluteTimeUnits',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetStreamEndpointHandle': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nReturns a writer endpoint that can be used with NI-P2P to configure a\npeer-to-peer stream with a digitizer endpoint.\n\n-  `Peer-to-Peer Streaming <digitizers.chm::/5160_P2P.html>`__\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe stream endpoint FIFO to configure. Refer to the device-specific\ndocumentation for peer-to-peer streaming in the *High-Speed Digitizers\nHelp* for more information.\n'
                },
                'name': 'streamName',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns a reference to a peer-to-peer writer FIFO that can be used to\ncreate a peer-to-peer streaming session.\n'
                },
                'name': 'writerHandle',
                'type': 'ViUInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ImportAttributeConfigurationBuffer': {
        'documentation': {
            'description': '\nImports an attribute configuration to the session from the specified\nconfiguration buffer.\n\nYou can export and import session attribute configurations only between\ndevices with identical model numbers, channel counts, and onboard memory\nsizes.\n\n**Related Topics:**\n\n`Attributes and Attribute\nFunctions <REPLACE_DRIVER_SPECIFIC_URL_1(attributes_and_attribute_functions)>`__\n\n`Setting Attributes Before Reading\nAttributes <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__\n',
            'note': '\nYou cannot call this function while the session is in a running state,\nsuch as while acquiring a signal.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the size, in bytes, of the byte array to import. If you enter\n0, this function returns the needed size.\n'
                },
                'name': 'sizeInBytes',
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
                    'value': 'sizeInBytes'
                },
                'type': 'ViInt8[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ImportAttributeConfigurationFile': {
        'documentation': {
            'description': '\nImports an attribute configuration to the session from the specified\nfile.\n\nYou can export and import session attribute configurations only between\ndevices with identical model numbers, channel counts, and onboard memory\nsizes.\n\n**Related Topics:**\n\n`Attributes and Attribute\nFunctions <REPLACE_DRIVER_SPECIFIC_URL_1(attributes_and_attribute_functions)>`__\n\n`Setting Attributes Before Reading\nAttributes <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__\n',
            'note': '\nYou cannot call this function while the session is in a running state,\nsuch as while acquiring a signal.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the absolute path to the file containing the attribute\nconfiguration to import. If you specify an empty or relative path, this\nfunction returns an error.\n**Default File Extension:** .niscopeconfig\n'
                },
                'name': 'filePath',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ImportAttributes': {
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
    'InitWithOptions': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nPerforms the following initialization actions:\n\n-  Creates a new IVI instrument driver and optionally sets the initial\n   state of the following session properties: Range Check, Cache,\n   Simulate, Record Value Coercions\n-  Opens a session to the specified device using the interface and\n   address you specify for the **resourceName**\n-  Resets the digitizer to a known state if **resetDevice** is set to\n   VI_TRUE\n-  Queries the instrument ID and verifies that it is valid for this\n   instrument driver if the **IDQuery** is set to VI_TRUE\n-  Returns an instrument handle that you use to identify the instrument\n   in all subsequent instrument driver function calls\n'
        },
        'method_name_for_documentation': '__init__',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'caution': '\nTraditional NI-DAQ and NI-DAQmx device names are not case-sensitive.\nHowever, all IVI names, such as logical names, are case-sensitive. If\nyou use logical names, driver session names, or virtual names in your\nprogram, you must make sure that the name you use matches the name in\nthe IVI Configuration Store file exactly, without any variations in the\ncase of the characters.\n',
                    'description': '\n| Specifies the resource name of the device to initialize\n\nFor Traditional NI-DAQ devices, the syntax is DAQ::\\ *n*, where *n* is\nthe device number assigned by MAX, as shown in Example 1.\n\nFor NI-DAQmx devices, the syntax is just the device name specified in\nMAX, as shown in Example 2. Typical default names for NI-DAQmx devices\nin MAX are Dev1 or PXI1Slot1. You can rename an NI-DAQmx device by\nright-clicking on the name in MAX and entering a new name.\n\nAn alternate syntax for NI-DAQmx devices consists of DAQ::NI-DAQmx\ndevice name, as shown in Example 3. This naming convention allows for\nthe use of an NI-DAQmx device in an application that was originally\ndesigned for a Traditional NI-DAQ device. For example, if the\napplication expects DAQ::1, you can rename the NI-DAQmx device to 1 in\nMAX and pass in DAQ::1 for the resource name, as shown in Example 4.\n\nIf you use the DAQ::\\ *n* syntax and an NI-DAQmx device name already\nexists with that same name, the NI-DAQmx device is matched first.\n\nYou can also pass in the name of an IVI logical name or an IVI virtual\nname configured with the IVI Configuration utility, as shown in Example\n5. A logical name identifies a particular virtual instrument. A virtual\nname identifies a specific device and specifies the initial settings for\nthe session.\n',
                    'table_body': [
                        [
                            '1',
                            'Traditional NI-DAQ device',
                            'DAQ::1 (1 = device number)'
                        ],
                        [
                            '2',
                            'NI-DAQmx device',
                            'myDAQmxDevice (myDAQmxDevice = device name)'
                        ],
                        [
                            '3',
                            'NI-DAQmx device',
                            'DAQ::myDAQmxDevice (myDAQmxDevice = device name)'
                        ],
                        [
                            '4',
                            'NI-DAQmx device',
                            'DAQ::2 (2 = device name)'
                        ],
                        [
                            '5',
                            'IVI logical name or IVI virtual name',
                            'myLogicalName (myLogicalName = name)'
                        ]
                    ],
                    'table_header': [
                        'Example',
                        'Device Type',
                        'Syntax'
                    ]
                },
                'name': 'resourceName',
                'type': 'ViRsrc'
            },
            {
                'default_value': False,
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecify whether to perform an ID query.\n\nWhen you set this parameter to VI_TRUE, NI-SCOPE verifies that the\ndevice you initialize is a type that it supports.\n\nWhen you set this parameter to VI_FALSE, the function initializes the\ndevice without performing an ID query.\n\n**Defined Values**\n\n| VI_TRUE—Perform ID query\n| VI_FALSE—Skip ID query\n\n**Default Value**: VI_TRUE\n'
                },
                'name': 'idQuery',
                'type': 'ViBoolean'
            },
            {
                'default_value': False,
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecify whether to reset the device during the initialization process.\n\nDefault Value: VI_TRUE\n\n**Defined Values**\n\nVI_TRUE (1)—Reset device\n\nVI_FALSE (0)—Do not reset device\n',
                    'note': '\nFor the NI 5112, repeatedly resetting the device may cause excessive\nwear on the electromechanical relays. Refer to `NI 5112\nElectromechanical Relays <REPLACE_DRIVER_SPECIFIC_URL_1(5112_relays)>`__\nfor recommended programming practices.\n'
                },
                'name': 'resetDevice',
                'type': 'ViBoolean'
            },
            {
                'default_value': '""',
                'direction': 'in',
                'documentation': {
                    'description': '\n| Specifies initialization commands. The following table lists the\n  attributes and the name you use in the **optionString** to identify\n  the attribute.\n\nDefault Values: "Simulate=0,RangeCheck=1,QueryInstrStatus=1,Cache=1"\n\nYou can use the option string to simulate a device. The DriverSetup flag\nspecifies the model that is to be simulated and the type of the model.\nOne example to simulate an NI PXI-5102 would be as follows:\n\nOption String: Simulate = 1, DriverSetup = Model:5102; BoardType:PXI\n\nRefer to the example niScope EX Simulated Acquisition for more\ninformation on simulation.\n\nYou can also use the option string to attach an accessory such as the\nNI 5900 to your digitizer session to allow the seamless use of the\naccessory:\n\nOption String: DriverSetup = Accessory:Dev1\n\nRefer to the example niScope EX External Amplifier for more information.\n',
                    'table_body': [
                    ]
                },
                'name': 'optionString',
                'python_api_converter_name': 'convert_init_with_options_dictionary',
                'type': 'ViConstString',
                'type_in_documentation': 'dict'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns a session handle that you can use to identify the device in all\nsubsequent NI-SCOPE function calls.\n'
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
    'InitiateAcquisition': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nInitiates a waveform acquisition.\n\nAfter calling this function, the digitizer leaves the Idle state and\nwaits for a trigger. The digitizer acquires a waveform for each channel\nyou enable with niScope_ConfigureVertical.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
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
    'IsDeviceReady': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nCall this function to determine whether the device is ready for use or\nthe device is still undergoing initialization.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'caution': '\nTraditional NI-DAQ and NI-DAQmx device names are not case-sensitive.\nHowever, all IVI names, such as logical names, are case-sensitive. If\nyou use logical names, driver session names, or virtual names in your\nprogram, you must make sure that the name you use matches the name in\nthe IVI Configuration Store file exactly, without any variations in the\ncase of the characters.\n',
                    'description': '\n**resourceName** specifies the resource name of the device to\ninitialize.\n\nresourceName Examples\n\nFor Traditional NI-DAQ devices, the syntax is DAQ::\\ *n*, where *n* is\nthe device number assigned by MAX, as shown in Example 1.\n\nFor NI-DAQmx devices, the syntax is just the device name specified in\nMAX, as shown in Example 2. Typical default names for NI-DAQmx devices\nin MAX are Dev1 or PXI1Slot1. You can rename an NI-DAQmx device by\nright-clicking on the name in MAX and entering a new name.\n\nAn alternate syntax for NI-DAQmx devices consists of DAQ::\\ *NI-DAQmx\ndevice name*, as shown in Example 3. This naming convention allows for\nthe use of an NI-DAQmx device in an application that was originally\ndesigned for a Traditional NI-DAQ device. For example, if the\napplication expects DAQ::1, you can rename the NI-DAQmx device to 1 in\nMAX and pass in DAQ::1 for the resource name, as shown in Example 4.\n\nIf you use the DAQ::\\ *n* syntax and an NI-DAQmx device name already\nexists with that same name, the NI-DAQmx device is matched first.\n\nYou can also pass in the name of an IVI logical name or an IVI virtual\nname configured with the IVI Configuration utility, as shown in Example\n5. A logical name identifies a particular virtual instrument. A virtual\nname identifies a specific device and specifies the initial settings for\nthe session.\n',
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
                    'description': '\nUse only "" or a null pointer. If you specify a channel, NI-SCOPE will\nreturn an error.\n'
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns True if the device is ready to use, or False if the device is\nstill initializing.\n'
                },
                'name': 'deviceReady',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'IsInvalidWfmElement': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nDetermines whether a value you pass from the waveform array is invalid.\nAfter the read and fetch waveform functions execute, each element in the\nwaveform array contains either a voltage or a value indicating that the\ninstrument could not sample a voltage.\n',
            'note': '\nThis function is included for compliance with the IviScope Class\nSpecification.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass one of the values from the waveform array returned by the read and\nfetch waveform functions.\n'
                },
                'name': 'elementValue',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns whether the element value is a valid voltage or a value\nindicating that the digitizer could not sample a voltage.\n\nReturn values:\n\n| VI_TRUE—The element value indicates that the instrument could not\n  sample the voltage.\n| VI_FALSE—The element value is a valid voltage.\n'
                },
                'name': 'isInvalid',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'IviClose': {
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
    'LVGenericFetchSelfAlloc': {
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
                'name': 'channel',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'numSamples',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'dataType',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'wfmInfo',
                'type': 'tWfmInfo'
            },
            {
                'direction': 'out',
                'name': 'wfm',
                'type': 'ViTypelessLVArrayHdl'
            }
        ],
        'returns': 'ViStatus'
    },
    'LVGenericMultiFetchSelfAlloc': {
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
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'numSamples',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'dataType',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'wfmInfo',
                'type': 'tWfmInfoArrayHdl'
            },
            {
                'direction': 'out',
                'name': 'wfm',
                'type': 'tLV2DArrayHdl'
            }
        ],
        'returns': 'ViStatus'
    },
    'LockSession': {
        'documentation': {
            'description': '\nObtains a multithread lock on the instrument session. Before doing so,\nit waits until all other execution threads have released their locks on\nthe instrument session. Other threads might have obtained a lock on this\nsession in the following ways:\n\n-  Your application called niScope_LockSession\n-  A call to the instrument driver locked the session\n-  A call to the IVI engine locked the session\n\nAfter your call to niScope_LockSession returns successfully, no other\nthreads can access the instrument session until you call\nniScope_UnlockSession. Use niScope_LockSession and\nniScope_UnlockSession around a sequence of calls to instrument driver\nfunctions if you require that the instrument retain its settings through\nthe end of the sequence.\n\nYou can safely make nested calls to niScope_LockSession within the same\nthread. To completely unlock the session, you must balance each call to\nniScope_LockSession with a call to niScope_UnlockSession. If, however,\nyou use the **callerHasLock** in all calls to niScope_LockSession and\nniScope_UnlockSession within a function, the IVI Library locks the\nsession only once within the function regardless of the number of calls\nyou make to niScope_LockSession. This allows you to call\nniScope_UnlockSession just once at the end of the function.\n'
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
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThis parameter serves as a convenience. If you do not want to use this\nparameter, pass VI_NULL.\n\nUse this parameter in complex functions to keep track of whether you\nhave obtained a lock and therefore need to unlock the session. Pass the\naddress of a local ViBoolean variable. In the declaration of the local\nvariable, initialize it to VI_FALSE. Pass the address of the same local\nvariable to any other calls you make to niScope_LockSession or\nniScope_UnlockSession in the same function.\n'
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
    'LvCalStart': {
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
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'LvGenericFetch': {
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
                'name': 'channel',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'numSamples',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'dataType',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'actualSamples',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'absoluteInitialX',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'relativeInitialX',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'xIncrement',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'offset',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'gain',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'reserved1',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'reserved2',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'wfm',
                'type': 'void'
            }
        ],
        'returns': 'ViStatus'
    },
    'LvGenericFetchArrayMeasurement': {
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
                'name': 'channel',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'arrayMeasFunction',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'measWfmSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'actualSamples',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'absoluteInitialX',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'relativeInitialX',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'xIncrement',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'offset',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'gain',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'reserved1',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'reserved2',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'measWfm',
                'type': 'void'
            }
        ],
        'returns': 'ViStatus'
    },
    'LvGenericMultiFetch': {
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
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'numSamples',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'dataType',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'actualSamples',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'absoluteInitialX',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'relativeInitialX',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'xIncrement',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'offset',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'gain',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'reserved1',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'reserved2',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'wfm',
                'type': 'void'
            }
        ],
        'returns': 'ViStatus'
    },
    'LvGenericMultiFetchArrayMeasurement': {
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
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'arrayMeasFunction',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'measWfmSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'actualSamples',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'absoluteInitialX',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'relativeInitialX',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'xIncrement',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'offset',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'gain',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'reserved1',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'reserved2',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'measWfm',
                'type': 'void'
            }
        ],
        'returns': 'ViStatus'
    },
    'LvGenericMultiFetchSelfAlloc3D': {
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
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'numSamples',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'dataType',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'wfmInfo',
                'type': 'void'
            },
            {
                'direction': 'out',
                'name': 'wfm',
                'type': 'void'
            }
        ],
        'returns': 'ViStatus'
    },
    'LvGenericMultiRead': {
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
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'numSamples',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'dataType',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'actualSamples',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'absInitialX',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'relInitialX',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'xIncrement',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'offset',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'gain',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'reserved1',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'reserved2',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'wfm',
                'type': 'void'
            }
        ],
        'returns': 'ViStatus'
    },
    'LvGenericRead': {
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
                'name': 'channel',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'numSamples',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'dataType',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'actualSamples',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'absInitialX',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'relInitialX',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'xIncrement',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'offset',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'gain',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'reserved1',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'reserved2',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'wfm',
                'type': 'void'
            }
        ],
        'returns': 'ViStatus'
    },
    'LvGetError': {
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
                'type': 'ViStatus'
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'description',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViString[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'LvGetErrorMessage': {
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
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
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
    'LvIsDeviceReady': {
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
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'name': 'deviceReady',
                'type': 'ViBoolean'
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
    'LvIsDeviceReserved': {
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
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'name': 'deviceReserved',
                'type': 'ViBoolean'
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
    'LvSingleFetchMeasurement': {
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
                'name': 'channel',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'scalarMeasFunction',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'result',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'LvSingleFetchMeasurementStats': {
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
                'name': 'channel',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'scalarMeasFunction',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'result',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'mean',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'stdev',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'min',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'max',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'numInStats',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'LvSingleReadMeasurement': {
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
                'name': 'channel',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'scalarMeasFunction',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'result',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'MemoryFetch': {
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
                'name': 'channel',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'recordNum',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'byteAddress',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'numBytes',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'wfm',
                'type': 'void'
            }
        ],
        'returns': 'ViStatus'
    },
    'ParseNumberOfChannels': {
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
                'name': 'channel',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'name': 'numChannels',
                'type': 'ViUInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'PokeSatcr': {
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
                'name': 'size',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'streamNumber',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ProbeCompensationSignalStart': {
        'documentation': {
            'description': 'Starts the 1 kHz square wave output on PFI 1 for probe compensation.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ProbeCompensationSignalStop': {
        'documentation': {
            'description': 'Stops the 1 kHz square wave output on PFI 1 for probe compensation.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'Read': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nInitiates an acquisition, waits for it to complete, and retrieves the\ndata. The process is similar to calling niScope_InitiateAcquisition,\nniScope_AcquisitionStatus, and niScope_Fetch. The only difference is\nthat with niScope_Read, you enable all channels specified with\n**channelList** before the acquisition; in the other method, you enable\nthe channels with niScope_ConfigureVertical.\n\nThis function may return multiple waveforms depending on the number of\nchannels, the acquisition type, and the number of records you specify.\n',
            'note': '\nSome functionality is not supported in all digitizers. Refer to\n`Features Supported by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for\nmore information.\n'
        },
        'method_name_for_documentation': 'read',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'default_value': 'datetime.timedelta(seconds=5.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe time to wait in seconds for data to be acquired; using 0 for this\nparameter tells NI-SCOPE to fetch whatever is currently available. Using\n-1 for this parameter implies infinite timeout.\n'
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds',
                'type': 'ViReal64',
                'type_in_documentation': 'float in seconds or datetime.timedelta'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe maximum number of samples to fetch for each waveform. If the\nacquisition finishes with fewer points than requested, some devices\nreturn partial data if the acquisition finished, was aborted, or a\ntimeout of 0 was used. If it fails to complete within the timeout\nperiod, the function returns an error.\n'
                },
                'name': 'numSamples',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns an array whose length is the **numSamples** times number of\nwaveforms. Call niScope_ActualNumwfms to determine the number of\nwaveforms.\n\nNI-SCOPE returns this data sequentially, so all record 0 waveforms are\nfirst. For example, with a channel list of 0,1, you would have the\nfollowing index values:\n\nindex 0 = record 0, channel 0\n\nindex *x* = record 0, channel 1\n\nindex 2\\ *x* = record 1, channel 0\n\nindex 3\\ *x* = record 1, channel 1\n\nWhere *x* = the record length\n'
                },
                'name': 'waveform',
                'size': {
                    'mechanism': 'python-code',
                    'value': '(num_samples * self._actual_num_wfms())'
                },
                'type': 'ViReal64[]',
                'use_array': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns an array of structures with the following timing and scaling\ninformation about each waveform:\n\n-  **relativeInitialX**—the time (in seconds) from the trigger to the\n   first sample in the fetched waveform\n-  **absoluteInitialX**—timestamp (in seconds) of the first fetched\n   sample. This timestamp is comparable between records and\n   acquisitions; devices that do not support this parameter use 0 for\n   this output.\n-  **xIncrement**—the time between points in the acquired waveform in\n   seconds\n-  **actualSamples**—the actual number of samples fetched and placed in\n   the waveform array\n-  **gain**—the gain factor of the given channel; useful for scaling\n   binary data with the following formula:\n\nvoltage = binary data × gain factor + offset\n\n-  **offset**—the offset factor of the given channel; useful for scaling\n   binary data with the following formula:\n\nvoltage = binary data × gain factor + offset\n\nCall niScope_ActualNumWfms to determine the size of this array.\n'
                },
                'name': 'wfmInfo',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'self._actual_num_wfms()'
                },
                'type': 'struct niScope_wfmInfo[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadEeprom': {
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
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'sizeInBytes',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'data',
                'type': 'ViUInt8'
            },
            {
                'direction': 'in',
                'name': 'whichEeprom',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadMeasurement': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nInitiates an acquisition, waits for it to complete, and performs the\nspecified waveform measurement for a single channel and record or for\nmultiple channels and records.\n\nRefer to `Using Fetch\nFunctions <REPLACE_DRIVER_SPECIFIC_URL_1(using_fetch_functions)>`__ for\nmore information.\n\nMany of the measurements use the low, mid, and high reference levels.\nYou configure the low, mid, and high references by using\nNISCOPE_ATTR_MEAS_CHAN_LOW_REF_LEVEL,\nNISCOPE_ATTR_MEAS_CHAN_MID_REF_LEVEL, and\nNISCOPE_ATTR_MEAS_CHAN_HIGH_REF_LEVEL to set each channel\ndifferently.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'default_value': 'datetime.timedelta(seconds=5.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe time to wait in seconds for data to be acquired; using 0 for this\nparameter tells NI-SCOPE to fetch whatever is currently available. Using\n-1 for this parameter implies infinite timeout.\n'
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds',
                'type': 'ViReal64',
                'type_in_documentation': 'float in seconds or datetime.timedelta'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe `scalar\nmeasurement <REPLACE_DRIVER_SPECIFIC_URL_2(scalar_measurements_refs)>`__\nto be performed\n'
                },
                'enum': 'ScalarMeasurement',
                'name': 'scalarMeasFunction',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nContains an array of all measurements acquired. Call\nniScope_ActualNumWfms to determine the array length.\n'
                },
                'name': 'result',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'self._actual_num_wfms()'
                },
                'type': 'ViReal64[]',
                'use_array': True
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadMinMaxWaveform': {
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
                'name': 'waveformSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'maxTime',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'minWaveform',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'in',
                'name': 'maxWaveform',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'out',
                'name': 'actualPoints',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'initialX',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'xIncrement',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadMiteEeprom': {
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
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'sizeInBytes',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'data',
                'type': 'ViUInt8'
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
                'name': 'size',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'offset',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'ViUInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadSerial': {
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
                'name': 'lowDataWord',
                'type': 'ViUInt32'
            },
            {
                'direction': 'out',
                'name': 'highDataWord',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'name': 'address',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'numberOfBits',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'mode',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'clockRate',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'polarity',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadWaveform': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nInitiates an acquisition on the channels that you enable with\nniScope_ConfigureVertical. This function then waits for the acquisition\nto complete and returns the waveform for the channel you specify. Call\nniScope_FetchWaveform to obtain the waveforms for each of the remaining\nenabled channels without initiating another acquisition.\n\nUse niScope_ActualRecordLength to determine the required size for the\n**waveform** array.\n',
            'note': '\nThis function is included for compliance with the IviScope Class\nSpecification.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe channel to configure. For more information, refer to `channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm\',\'cvichannelstringsyntaxforc)>`__.\n\nDefault Value: "0"\n'
                },
                'name': 'channel',
                'type': 'ViString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The number of elements to insert into the **waveform** array.'
                },
                'name': 'waveformSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the maximum length of time in which to allow the read waveform\noperation to complete.\n\nIf the operation does not complete within this time interval, the\nfunction returns the NISCOPE_ERROR_MAX_TIME_EXCEEDED error code.\nWhen this occurs, you can call niScope_Abort to cancel the read\nwaveform operation and return the digitizer to the idle state.\n\nUnits: milliseconds\n\n| Other Defined Values\n| NISCOPE_VAL_MAX_TIME_NONE\n| NISCOPE_VAL_MAX_TIME_INFINITE\n'
                },
                'name': 'maxTime',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the waveform that the digitizer acquires.\nUnits: volts\n'
                },
                'name': 'waveform',
                'size': {
                    'mechanism': 'python-code',
                    'value': None
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nIndicates the actual number of points the function placed in the\n**waveform** array.\n'
                },
                'name': 'actualPoints',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nIndicates the time of the first point in the **waveform** array relative\nto the Reference Position.\n\nUnits: seconds\n\nFor example, if the digitizer acquires the first point in the\n**waveform** array 1 second before the trigger, this parameter returns\nthe value –1.0. If the acquisition of the first point occurs at the same\ntime as the trigger, this parameter returns the value 0.0.\n'
                },
                'name': 'initialX',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nIndicates the length of time between points in the **waveform** array.\n\nUnits: seconds\n'
                },
                'name': 'xIncrement',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadWaveformMeasurement': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nInitiates a new waveform acquisition and returns a specified waveform\nmeasurement from a specific channel.\n\nThis function initiates an acquisition on the channels that you enable\nwith the niScope_ConfigureVertical function. It then waits for the\nacquisition to complete, obtains a waveform measurement on the channel\nyou specify, and returns the measurement value. You specify a particular\nmeasurement type, such as rise time, frequency, or voltage peak-to-peak.\n\nYou can call the niScope_FetchWaveformMeasurement function separately\nto obtain any other waveform measurement on a specific channel without\ninitiating another acquisition.\n\nYou must configure the appropriate reference levels before calling this\nfunction. Configure the low, mid, and high references by calling\nniScope_ConfigureRefLevels or by setting the following attributes:\n\n| NISCOPE_ATTR_MEAS_HIGH_REF\n| NISCOPE_ATTR_MEAS_LOW_REF\n| NISCOPE_ATTR_MEAS_MID_REF\n',
            'note': '\nThis function is included for compliance with the IviScope Class\nSpecification.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe channel to configure. For more information, refer to `channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm\',\'cvichannelstringsyntaxforc)>`__.\n\nDefault Value: "0"\n'
                },
                'name': 'channel',
                'type': 'ViString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The scalar measurement to perform.'
                },
                'name': 'measFunction',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the maximum length of time in which to allow the read waveform\noperation to complete.\n\nIf the operation does not complete within this time interval, the\nfunction returns the NISCOPE_ERROR_MAX_TIME_EXCEEDED error code.\nWhen this occurs, you can call niScope_Abort to cancel the read\nwaveform operation and return the digitizer to the idle state.\n\nUnits: milliseconds\n'
                },
                'name': 'maxTime',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The measured value.'
                },
                'name': 'measurement',
                'type': 'ViReal64'
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
    'RequestBaselineMonitoringEvent': {
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
    'ResetAllAttributes': {
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
    'ResetAttribute': {
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
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr'
            }
        ],
        'returns': 'ViStatus'
    },
    'ResetDevice': {
        'documentation': {
            'description': '\nPerforms a hard reset of the device. Acquisition stops, all routes are\nreleased, RTSI and PFI lines are tristated, hardware is configured to\nits default state, and all session attributes are reset to their default\nstate.\n\n-  `Thermal Shutdown <digitizers.chm::/Thermal_Shutdown.html>`__\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
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
            'description': '\nWhen developing a complex test system that consists of multiple test\nmodules, it is generally a good idea to design the test modules so that\nthey can run in any order. To do so requires ensuring that each test\nmodule completely configures the state of each instrument it uses.\n\n| If a particular test module does not completely configure the state of\n  an instrument, the state of the instrument depends on the\n  configuration from a previously executed test module.\n| If you execute the test modules in a different order, the behavior of\n  the instrument and therefore the entire test module is likely to\n  change.\n\n| This change in behavior is generally instrument-specific and\n  represents an interchangeability problem. You can use this function to\n  test for such cases. After you call this function, the\n  interchangeability checking algorithms in the specific driver ignore\n  all previous configuration operations.\n| By calling this function at the beginning of a test module, you can\n  determine whether the test module has dependencies on the operation of\n  previously executed test modules.\n\nThis function does not clear the interchangeability warnings from the\nlist of previously recorded interchangeability warnings. If you want to\nguarantee that niScope_GetNextInterchangeWarning only returns those\ninterchangeability warnings that are generated after calling this\nfunction, you must clear the list of interchangeability warnings.\n\nYou can clear the interchangeability warnings list by repeatedly calling\nniScope_GetNextInterchangeWarning until no more interchangeability\nwarnings are returned. If you are not interested in the content of those\nwarnings, you can call niScope_ClearInterchangeWarnings.\n',
            'note': '\nThis function is included for compliance with the IviScope Class\nSpecification.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ResetWithDefaults': {
        'documentation': {
            'description': '\nPerforms a software reset of the device, returning it to the default\nstate and applying any initial default settings from the IVI\nConfiguration Store.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
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
            }
        ],
        'returns': 'ViStatus'
    },
    'SampleMode': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Returns the sample mode the digitizer is currently using.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the sample mode the digitizer is currently using; NI-SCOPE\nreturns the value of the NISCOPE_ATTR_SAMPLE_MODE attribute.\n'
                },
                'name': 'sampleMode',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'SampleRate': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nReturns the effective sample rate, in samples per second, of the\nacquired waveform using the current configuration. Refer to `Coercions\nof Horizontal\nParameters <REPLACE_DRIVER_SPECIFIC_URL_1(horizontal_parameters)>`__ for\nmore information about sample rate coercion.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the effective sample rate of the acquired waveform the digitizer\nacquires for each channel; the driver returns the value held in the\nNISCOPE_ATTR_HORZ_SAMPLE_RATE attribute.\n'
                },
                'name': 'sampleRate',
                'type': 'ViReal64'
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
    'SendSoftwareTriggerEdge': {
        'documentation': {
            'description': '\nSends the selected trigger to the digitizer. Call this function if you\ncalled niScope_ConfigureTriggerSoftware when you want the Reference\ntrigger to occur. You can also call this function to override a misused\nedge, digital, or hysteresis trigger. If you have configured\nNISCOPE_ATTR_ACQ_ARM_SOURCE, NISCOPE_ATTR_ARM_REF_TRIG_SRC, or\nNISCOPE_ATTR_ADV_TRIG_SRC, call this function when you want to send\nthe corresponding trigger to the digitizer.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the type of trigger to send to the digitizer.\n\n**Defined Values**\n\n| NISCOPE_VAL_SOFTWARE_TRIGGER_START (0L)\n|  NISCOPE_VAL_SOFTWARE_TRIGGER_ARM_REFERENCE (1L)\n| NISCOPE_VAL_SOFTWARE_TRIGGER_REFERENCE (2L)\n| NISCOPE_VAL_SOFTWARE_TRIGGER_ADVANCE (3L)\n'
                },
                'enum': 'WhichTrigger',
                'name': 'whichTrigger',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'SendSwTrigger': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSends a command to trigger the digitizer. Call this function after you\ncall niScope_ConfigureTriggerSoftware.\n',
            'note': '\nThis function is included for compliance with the IviScope Class\nSpecification. Consider using niScope_SendSoftwareTriggerEdge instead.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViBoolean': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nSets the value of a ViBoolean attribute. This is a low-level function\nthat you can use to set the values of instrument-specific attributes and\ninherent IVI attributes. If the attribute represents an instrument\nstate, this function performs instrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled and the currently cached value is invalid or\n   is different than the value you specify.\n',
            'note': '\nNI-SCOPE contains high-level functions that set most of the instrument\nattributes. Use the high-level driver functions as much as possible\nbecause they handle order dependencies and multithread locking for you.\nIn addition, the high-level functions perform status checking only after\nsetting all of the attributes. In contrast, when you set multiple\nattributes using the SetAttribute functions, the functions check the\ninstrument status after each call. Also, when state caching is enabled,\nthe high-level functions that configure multiple attributes perform\ninstrument I/O only for the attributes whose value you change. Thus, you\ncan safely call the high-level functions without the penalty of\nredundant instrument I/O.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe value that you want to set the attribute to. Some values might not\nbe valid depending on the current settings of the instrument session.\n'
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
            'description': '\nSets the value of a ViInt32 attribute. This is a low-level function that\nyou can use to set the values of instrument-specific attributes and\ninherent IVI attributes. If the attribute represents an instrument\nstate, this function performs instrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled and the currently cached value is invalid or\n   is different than the value you specify.\n',
            'note': '\nNI-SCOPE contains high-level functions that set most of the instrument\nattributes. Use the high-level functions as much as possible because\nthey handle order dependencies and multithread locking for you. In\naddition, high-level functions perform status checking only after\nsetting all of the attributes. In contrast, when you set multiple\nattributes using the Set Attribute functions, the functions check the\ninstrument status after each call. Also, when state caching is enabled,\nthe high-level functions that configure multiple attributes perform\ninstrument I/O only for the attributes whose value you change. Thus, you\ncan safely call the high-level functions without the penalty of\nredundant instrument I/O.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe value that you want to set the attribute. Some values might not be\nvalid depending on the current settings of the instrument session.\n'
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
            'description': '\nSets the value of a ViInt64 attribute. This is a low-level function that\nyou can use to set the values of instrument-specific attributes and\ninherent IVI attributes. If the attribute represents an instrument\nstate, this function performs instrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled and the currently cached value is invalid or\n   is different than the value you specify.\n',
            'note': '\nNI-SCOPE contains high-level functions that set most of the instrument\nattributes. Use the high-level functions as much as possible because\nthey handle order dependencies and multithread locking for you. In\naddition, high-level functions perform status checking only after\nsetting all of the attributes. In contrast, when you set multiple\nattributes using the Set Attribute functions, the functions check the\ninstrument status after each call. Also, when state caching is enabled,\nthe high-level functions that configure multiple attributes perform\ninstrument I/O only for the attributes whose value you change. Thus, you\ncan safely call the high-level functions without the penalty of\nredundant instrument I/O.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe value that you want to set the attribute. Some values might not be\nvalid depending on the current settings of the instrument session.\n'
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
            'description': '\nSets the value of a ViReal64 attribute. This is a low-level function\nthat you can use to set the values of instrument-specific attributes and\ninherent IVI attributes. If the attribute represents an instrument\nstate, this function performs instrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled and the currently cached value is invalid or\n   is different than the value you specify.\n',
            'note': '\nNI-SCOPE contains high-level functions that set most of the instrument\nattributes. Use the high-level driver functions as much as possible\nbecause they handle order dependencies and multithread locking for you.\nIn addition, the high-level functions perform status checking only after\nsetting all of the attributes. In contrast, when you set multiple\nattributes using the Set Attribute functions, the functions check the\ninstrument status after each call. Also, when state caching is enabled,\nthe high-level functions that configure multiple attributes perform\ninstrument I/O only for the attributes whose value you change. Thus, you\ncan safely call the high-level functions without the penalty of\nredundant instrument I/O.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe value that you want to set the attribute to. Some values might not\nbe valid depending on the current settings of the instrument session.\n'
                },
                'name': 'value',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViReal64Array': {
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
                'name': 'repCapName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'name': 'numberOfElements',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'elements',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViSession': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSets the value of a ViSession attribute. This is a low-level function\nthat you can use to set the values of instrument-specific attributes and\ninherent IVI attributes. If the attribute represents an instrument\nstate, this function performs instrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled and the currently cached value is invalid or\n   is different than the value you specify.\n',
            'note': '\nNI-SCOPE contains high-level functions that set most of the instrument\nattributes. Use the high-level driver functions as much as possible\nbecause they handle order dependencies and multithread locking for you.\nIn addition, the high-level functions perform status checking only after\nsetting all of the attributes. In contrast, when you set multiple\nattributes using the Set Attribute functions, the functions check the\ninstrument status after each call. Also, when state caching is enabled,\nthe high-level functions that configure multiple attributes perform\ninstrument I/O only for the attributes whose value you change. Thus, you\ncan safely call the high-level functions without the penalty of\nredundant instrument I/O.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe value that you want to set the attribute to. Some values might not\nbe valid depending on the current settings of the instrument session.\n'
                },
                'name': 'value',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViString': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nSets the value of a ViString attribute.\n\nThis is a low-level function that you can use to set the values of\ninstrument-specific attributes and inherent IVI attributes. If the\nattribute represents an instrument state, this function performs\ninstrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled and the currently cached value is invalid or\n   is different than the value you specify.\n',
            'note': '\nNI-SCOPE contains high-level functions that set most of the instrument\nattributes. Use the high-level driver functions as much as possible\nbecause they handle order dependencies and multithread locking for you.\nIn addition, the high-level functions perform status checking only after\nsetting all of the attributes. In contrast, when you set multiple\nattributes using the SetAttribute functions, the functions check the\ninstrument status after each call. Also, when state caching is enabled,\nthe high-level functions that configure multiple attributes perform\ninstrument I/O only for the attributes whose value you change. Thus, you\ncan safely call the high-level functions without the penalty of\nredundant instrument I/O.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe value that you want to set the attribute to. Some values might not\nbe valid depending on the current settings of the instrument session.\n'
                },
                'name': 'value',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetDdcFilterCoefficients': {
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
                'name': 'channel',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'coefficientType',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'numCoefficients',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'coefficients',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetEepromMapValue': {
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
                'name': 'field',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'type',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'integerValue',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'floatValue',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'whichEeprom',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetGlobalLanguage': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'TBD'
        },
        'parameters': [
            {
                'direction': 'in',
                'name': 'language',
                'type': 'ViInt32'
            }
        ],
        'returns': 'void'
    },
    'SizeOfDataType': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'TBD'
        },
        'parameters': [
            {
                'direction': 'in',
                'name': 'dataType',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViInt32'
    },
    'UnlockSession': {
        'documentation': {
            'description': '\nReleases a lock that you acquired on an instrument session using\nniScope_LockSession.\n'
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
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThis parameter serves as a convenience; if you do not want to use this\nparameter, pass VI_NULL.\n\nUse this parameter in complex functions to keep track of whether you\nhave obtained a lock and therefore need to unlock the session; pass the\naddress of a local ViBoolean variable; in the declaration of the local\nvariable, initialize it to VI_FALSE; pass the address of the same local\nvariable to any other calls you make to niScope_LockSession or\nniScope_UnlockSession in the same function.\n'
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
    'WaitForAcquisitionToFinish': {
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
                'name': 'maxTime',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteEeprom': {
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
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'sizeInBytes',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'data',
                'type': 'ViUInt8'
            },
            {
                'direction': 'in',
                'name': 'whichEeprom',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteMiteEeprom': {
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
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'sizeInBytes',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'data',
                'type': 'ViUInt8'
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
                'name': 'size',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'offset',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'ViUInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteSerial': {
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
                'name': 'lowDataWord',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'name': 'highDataWord',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'name': 'address',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'numberOfBits',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'mode',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'clockRate',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'polarity',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'synchronousWrite',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'close': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nWhen you are finished using an instrument driver session, you must call\nthis function to perform the following actions:\n\n-  Closes the instrument I/O session.\n-  Destroys the IVI session and all of its attributes.\n-  Deallocates any memory resources used by the IVI session.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
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
            'description': 'Takes the **Error_Code** returned by the instrument driver functions, interprets it, and returns it as a user-readable string.'
        },
        'is_error_handling': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session. You obtain the **vi** parameter from niScope_init or niScope_InitWithOptions. The default is None.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The **error_code** returned from the instrument. The default is 0, indicating VI_SUCCESS.'
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
            'description': '\nReads an error code and message from the error queue. National\nInstruments digitizers do not contain an error queue. Errors are\nreported as they occur. Therefore, this function does not detect errors.\n',
            'note': '\nThis function is included for compliance with the IviScope Class\nSpecification.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the error code for the session or execution thread. If you pass\n0 for the Buffer Size, you can pass VI_NULL for this parameter.\n'
                },
                'name': 'errCode',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nFormats the error code into a user-readable message string. The array\nmust contain at least 256 elements (ViChar[256]).\n'
                },
                'name': 'errMessage',
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'fancy_self_test': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': '\nRuns the instrument self-test routine and returns the test result(s). Refer to the\ndevice-specific help topics for an explanation of the message contents.\n\nRaises `SelfTestError` on self test failure. Attributes on exception object:\n\n- code - failure code from driver\n- message - status message from driver\n',
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
                    'description': 'The instrument handle you obtain from niScope_init that identifies a particular instrument session.'
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
            'description': '\nPerforms the following initialization actions:\n\n-  Creates a new IVI instrument driver session\n-  Opens a session to the specific driver using the interface and\n   address you specify in the **resourceName**\n-  Queries the instrument ID and checks that it is valid for NI-SCOPE,\n   if the **IDQuery** is set to VI_TRUE\n-  Resets the digitizer to a known state, if **resetDevice** is set to\n   VI_TRUE\n-  Sends initialization commands to set the instrument to the state\n   necessary for the operation of the instrument driver\n-  Returns an instrument handle that you use to identify the instrument\n   in all subsequent instrument driver function calls\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'caution': '\nTraditional NI-DAQ and NI-DAQmx device names are not case-sensitive.\nHowever, all IVI names, such as logical names, are case-sensitive. If\nyou use logical names, driver session names, or virtual names in your\nprogram, you must make sure that the name you use matches the name in\nthe IVI Configuration Store file exactly, without any variations in the\ncase of the characters.\n',
                    'description': '\n**resourceName** specifies the resource name of the device to\ninitialize.\n\nresourceName Examples\n\nFor Traditional NI-DAQ devices, the syntax is DAQ::\\ *n*, where *n* is\nthe device number assigned by MAX, as shown in Example 1.\n\nFor NI-DAQmx devices, the syntax is just the device name specified in\nMAX, as shown in Example 2. Typical default names for NI-DAQmx devices\nin MAX are Dev1 or PXI1Slot1. You can rename an NI-DAQmx device by\nright-clicking on the name in MAX and entering a new name.\n\nAn alternate syntax for NI-DAQmx devices consists of DAQ::\\ *NI-DAQmx\ndevice name*, as shown in Example 3. This naming convention allows for\nthe use of an NI-DAQmx device in an application that was originally\ndesigned for a Traditional NI-DAQ device. For example, if the\napplication expects DAQ::1, you can rename the NI-DAQmx device to 1 in\nMAX and pass in DAQ::1 for the resource name, as shown in Example 4.\n\nIf you use the DAQ::\\ *n* syntax and an NI-DAQmx device name already\nexists with that same name, the NI-DAQmx device is matched first.\n\nYou can also pass in the name of an IVI logical name or an IVI virtual\nname configured with the IVI Configuration utility, as shown in Example\n5. A logical name identifies a particular virtual instrument. A virtual\nname identifies a specific device and specifies the initial settings for\nthe session.\n',
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
                    'description': '\nSpecify whether to perform an ID query.\n\nWhen you set this parameter to VI_TRUE, NI-SCOPE verifies that the\ndevice you initialize is a type that it supports.\n\nWhen you set this parameter to VI_FALSE, the function initializes the\ndevice without performing an ID query.\n\n**Defined Values**\n\n| VI_TRUE—Perform ID query\n| VI_FALSE—Skip ID query\n\n**Default Value**: VI_TRUE\n'
                },
                'name': 'idQuery',
                'type': 'ViBoolean'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecify whether to reset the device during the initialization process.\n\n**Defined Values**\n\n| VI_TRUE—Reset device\n| VI_FALSE—Do not reset device\n\n**Default Value**: VI_TRUE\n',
                    'note': '\nFor the NI 5112, repeatedly resetting the device may cause excessive\nwear on the electromechanical relays. Refer to `NI 5112\nElectromechanical Relays <REPLACE_DRIVER_SPECIFIC_URL_1(5112_relays)>`__\nfor recommended programming practices.\n'
                },
                'name': 'resetDevice',
                'type': 'ViBoolean'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns a session handle that you can use to identify the device in all\nsubsequent NI-SCOPE function calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'reset': {
        'documentation': {
            'description': "\nStops the acquisition, releases routes, and all session attributes are\nreset to their `default\nstates <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cviattribute_defaults)>`__.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
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
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the instrument driver software revision numbers in the form of a\nstring; you must pass a ViChar array at least\nIVI_MAX_MESSAGE_BUF_SIZE bytes in length.\n'
                },
                'name': 'driverRevision',
                'type': 'ViChar[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the instrument firmware revision numbers in the form of a\nstring; you must pass a ViChar array at least\nIVI_MAX_MESSAGE_BUF_SIZE bytes in length.\n'
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
            'description': 'Runs the instrument self-test routine and returns the test result(s).'
        },
        'method_name_for_documentation': 'self_test',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThis control contains the value returned from the instrument self-test.\n\n**Self-Test Code Description**\n\n0—Self-test passed\n\n1—Self-test failed\n'
                },
                'name': 'selfTestResult',
                'type': 'ViInt16'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the self-test response string from the instrument. Refer to the\ndevice-specific help topics for an explanation of the string contents;\nyou must pass a ViChar array at least IVI_MAX_MESSAGE_BUF_SIZE bytes\nin length.\n'
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
