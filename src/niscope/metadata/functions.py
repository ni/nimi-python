# -*- coding: utf-8 -*-
# This file is generated from NI-SCOPE API metadata version 20.5.0d7
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
    'AddWaveformProcessing': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nAdds one measurement to the list of processing steps that are completed\nbefore the measurement. The processing is added on a per channel basis,\nand the processing measurements are completed in the same order they are\nregistered. All measurement library parameters—the attributes starting\nwith "meas_"—are cached at the time of registering the\nprocessing, and this set of parameters is used during the processing\nstep. The processing measurements are streamed, so the result of the\nfirst processing step is used as the input for the next step. The\nprocessing is done before any other measurements.\n'
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
    'CalFetchDate': {
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
                'enum': 'CalibrationTypes',
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
    'CalFetchTemperature': {
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
    'ClearWaveformMeasurementStats': {
        'codegen_method': 'public',
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
                'default_value': 'ClearableMeasurement.ALL_MEASUREMENTS',
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
        'codegen_method': 'public',
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
                'default_value': 'hightime.timedelta(seconds=0.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe length of time the digitizer waits after detecting a trigger before\nenabling NI-SCOPE to detect another trigger. Refer to\nNISCOPE_ATTR_TRIGGER_HOLDOFF for more information.\n'
                },
                'name': 'holdoff',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            },
            {
                'default_value': 'hightime.timedelta(seconds=0.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nHow long the digitizer waits after receiving the trigger to start\nacquiring data. Refer to NISCOPE_ATTR_TRIGGER_DELAY_TIME for more\ninformation.\n'
                },
                'name': 'delay',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
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
                'default_value': 'hightime.timedelta(seconds=0.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe length of time the digitizer waits after detecting a trigger before\nenabling NI-SCOPE to detect another trigger. Refer to\nNISCOPE_ATTR_TRIGGER_HOLDOFF for more information.\n'
                },
                'name': 'holdoff',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            },
            {
                'default_value': 'hightime.timedelta(seconds=0.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nHow long the digitizer waits after receiving the trigger to start\nacquiring data. Refer to NISCOPE_ATTR_TRIGGER_DELAY_TIME for more\ninformation.\n'
                },
                'name': 'delay',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
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
                'default_value': 'hightime.timedelta(seconds=0.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe length of time the digitizer waits after detecting a trigger before\nenabling NI-SCOPE to detect another trigger. Refer to\nNISCOPE_ATTR_TRIGGER_HOLDOFF for more information.\n'
                },
                'name': 'holdoff',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            },
            {
                'default_value': 'hightime.timedelta(seconds=0.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nHow long the digitizer waits after receiving the trigger to start\nacquiring data. Refer to NISCOPE_ATTR_TRIGGER_DELAY_TIME for more\ninformation.\n'
                },
                'name': 'delay',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
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
                'default_value': 'hightime.timedelta(seconds=0.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe length of time the digitizer waits after detecting a trigger before\nenabling NI-SCOPE to detect another trigger. Refer to\nNISCOPE_ATTR_TRIGGER_HOLDOFF for more information.\n'
                },
                'name': 'holdoff',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            },
            {
                'default_value': 'hightime.timedelta(seconds=0.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nHow long the digitizer waits after receiving the trigger to start\nacquiring data. Refer to NISCOPE_ATTR_TRIGGER_DELAY_TIME for more\ninformation.\n'
                },
                'name': 'delay',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
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
                'default_value': 'hightime.timedelta(seconds=0.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe length of time the digitizer waits after detecting a trigger before\nenabling NI-SCOPE to detect another trigger. Refer to\nNISCOPE_ATTR_TRIGGER_HOLDOFF for more information.\n'
                },
                'name': 'holdoff',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            },
            {
                'default_value': 'hightime.timedelta(seconds=0.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nHow long the digitizer waits after receiving the trigger to start\nacquiring data. Refer to NISCOPE_ATTR_TRIGGER_DELAY_TIME for more\ninformation.\n'
                },
                'name': 'delay',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTriggerWindow': {
        'documentation': {
            'description': '\nConfigures common properties for analog window triggering. A window\ntrigger occurs when a signal enters or leaves a window you specify with\nthe **high level** or **low level** parameters.\n\nWhen you initiate an acquisition, the digitizer waits for the start\ntrigger, which is configured through the NISCOPE_ATTR_ACQ_ARM_SOURCE\n(Start Trigger Source) attribute. The default is immediate. Upon\nreceiving the start trigger the digitizer begins sampling pretrigger\npoints. After the digitizer finishes sampling pretrigger points, the\ndigitizer waits for a reference (stop) trigger that you specify with a\nfunction such as this one. Upon receiving the reference trigger the\ndigitizer finishes the acquisition after completing posttrigger\nsampling. With each Configure Trigger function, you specify\nconfiguration parameters such as the trigger source and the amount of\ntrigger delay.\n\nTo trigger the acquisition, use niScope_SendSoftwareTriggerEdge.\n',
            'note': 'Some features are not supported by all digitizers.'
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
                'default_value': 'hightime.timedelta(seconds=0.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe length of time the digitizer waits after detecting a trigger before\nenabling NI-SCOPE to detect another trigger. Refer to\nNISCOPE_ATTR_TRIGGER_HOLDOFF for more information.\n'
                },
                'name': 'holdoff',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            },
            {
                'default_value': 'hightime.timedelta(seconds=0.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nHow long the digitizer waits after receiving the trigger to start\nacquiring data. Refer to NISCOPE_ATTR_TRIGGER_DELAY_TIME for more\ninformation.\n'
                },
                'name': 'delay',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
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
                'python_api_converter_name': 'convert_to_bytes',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'sizeInBytes'
                },
                'type': 'ViInt8[]',
                'type_in_documentation': 'bytes',
                'use_array': True
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
                'default_value': 'hightime.timedelta(seconds=5.0)',
                'direction': 'in',
                'documentation': {
                    'description': 'The time to wait for data to be acquired; using 0 for this parameter tells NI-SCOPE to fetch whatever is currently available. Using -1 seconds for this parameter implies infinite timeout.'
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'python_type': 'hightime.timedelta, datetime.timedelta, or float',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns a list of class instances with the following timing and scaling information about each waveform:\n\n-  **relative_initial_x** (float) the time (in seconds) from the trigger to the first sample in the fetched waveform\n-  **absolute_initial_x** (float) timestamp (in seconds) of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output.\n-  **x_increment** (float) the time between points in the acquired waveform in seconds\n-  **channel** (str) channel name this waveform was acquired from\n-  **record** (int) record number of this waveform\n-  **gain** (float) the gain factor of the given channel; useful for scaling binary data with the following formula:\n\n    .. math::\n\n        voltage = binary data * gain factor + offset\n\n-  **offset** (float) the offset factor of the given channel; useful for scaling binary data with the following formula:\n\n    .. math::\n\n        voltage = binary data * gain factor + offset\n\n- **samples** (array of float) floating point array of samples. Length will be of the actual samples acquired\n'
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
    'FancyGetExtCalLastDateAndTime': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': 'Returns the date and time of the last external calibration performed.'
        },
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_get_cal_last_date'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session. You obtain the **vi** parameter from niScope_init.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates the **date** of the last calibration. A hightime.datetime object is returned, but only contains resolution to the day.'
                },
                'name': 'lastCalDatetime',
                'python_type': 'hightime.timedelta, datetime.timedelta, or float',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            }
        ],
        'python_name': 'get_ext_cal_last_date_and_time',
        'returns': 'ViStatus'
    },
    'FancyGetExtCalLastTemp': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': 'Returns the onboard temperature, in degrees Celsius, of an oscilloscope at the time of the last successful external calibration.\nThe temperature returned by this node is an onboard temperature read from a sensor on the surface of the oscilloscope. This temperature should not be confused with the environmental temperature of the oscilloscope surroundings. During operation, the onboard temperature is normally higher than the environmental temperature.\nTemperature-sensitive parameters are calibrated during self-calibration. Therefore, the self-calibration temperature is usually more important to read than the external calibration temperature.'
        },
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_get_cal_last_temp'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session. You obtain the **vi** parameter from niScope_init.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the **temperature** in degrees Celsius during the last calibration.'
                },
                'name': 'temperature',
                'type': 'ViReal64'
            }
        ],
        'python_name': 'get_ext_cal_last_temp',
        'returns': 'ViStatus'
    },
    'FancyGetSelfCalLastDateAndTime': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': 'Returns the date and time of the last self calibration performed.'
        },
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_get_cal_last_date'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session. You obtain the **vi** parameter from niScope_init.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates the **date** of the last calibration. A hightime.datetime object is returned, but only contains resolution to the day.'
                },
                'name': 'lastCalDatetime',
                'python_type': 'hightime.timedelta, datetime.timedelta, or float',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            }
        ],
        'python_name': 'get_self_cal_last_date_and_time',
        'returns': 'ViStatus'
    },
    'FancyGetSelfCalLastTemp': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': 'Returns the onboard temperature, in degrees Celsius, of an oscilloscope at the time of the last successful self calibration.\nThe temperature returned by this node is an onboard temperature read from a sensor on the surface of the oscilloscope. This temperature should not be confused with the environmental temperature of the oscilloscope surroundings. During operation, the onboard temperature is normally higher than the environmental temperature.\nTemperature-sensitive parameters are calibrated during self-calibration. Therefore, the self-calibration temperature is usually more important to read than the external calibration temperature.'
        },
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_get_cal_last_temp'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session. You obtain the **vi** parameter from niScope_init.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the **temperature** in degrees Celsius during the last calibration.'
                },
                'name': 'temperature',
                'type': 'ViReal64'
            }
        ],
        'python_name': 'get_self_cal_last_temp',
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
                'default_value': 'hightime.timedelta(seconds=5.0)',
                'direction': 'in',
                'documentation': {
                    'description': 'The time to wait for data to be acquired; using 0 for this parameter tells NI-SCOPE to fetch whatever is currently available. Using -1 seconds for this parameter implies infinite timeout.'
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'python_type': 'hightime.timedelta, datetime.timedelta, or float',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns a list of class instances with the following timing and scaling information about each waveform:\n\n-  **relative_initial_x** (float) the time (in seconds) from the trigger to the first sample in the fetched waveform\n-  **absolute_initial_x** (float) timestamp (in seconds) of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output.\n-  **x_increment** (float) the time between points in the acquired waveform in seconds\n-  **channel** (str) channel name this waveform was acquired from\n-  **record** (int) record number of this waveform\n-  **gain** (float) the gain factor of the given channel; useful for scaling binary data with the following formula:\n\n    .. math::\n\n        voltage = binary data * gain factor + offset\n\n-  **offset** (float) the offset factor of the given channel; useful for scaling binary data with the following formula:\n\n    .. math::\n\n        voltage = binary data * gain factor + offset\n\n- **samples** (array of float) floating point array of samples. Length will be of the actual samples acquired\n'
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
                'default_value': 'hightime.timedelta(seconds=5.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe time to wait in seconds for data to be acquired; using 0 for this\nparameter tells NI-SCOPE to fetch whatever is currently available. Using\n-1 for this parameter implies infinite timeout.\n'
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
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
                    'description': '\nReturns a list of class instances with the following timing and scaling\ninformation about each waveform:\n\n-  **relativeInitialX**—the time (in seconds) from the trigger to the\n   first sample in the fetched waveform\n-  **absoluteInitialX**—timestamp (in seconds) of the first fetched\n   sample. This timestamp is comparable between records and\n   acquisitions; devices that do not support this parameter use 0 for\n   this output.\n-  **xIncrement**—the time between points in the acquired waveform in\n   seconds\n-  **actualSamples**—the actual number of samples fetched and placed in\n   the waveform array\n-  **gain**—the gain factor of the given channel; useful for scaling\n   binary data with the following formula:\n\nvoltage = binary data × gain factor + offset\n\n-  **offset**—the offset factor of the given channel; useful for scaling\n   binary data with the following formula:\n\nvoltage = binary data × gain factor + offset\n\nCall niScope_ActualNumWfms to determine the size of this array.\n'
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
                'default_value': 'hightime.timedelta(seconds=5.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe time to wait in seconds for data to be acquired; using 0 for this\nparameter tells NI-SCOPE to fetch whatever is currently available. Using\n-1 for this parameter implies infinite timeout.\n'
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
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
                    'description': '\nThe maximum number of samples returned in the measurement waveform array\nfor each waveform measurement. Use niScope_ActualMeasWfmSize to determine the number\nof available samples. Default Value: None (returns all available samples).\n',
                    'note': '\nUse the attribute NISCOPE_ATTR_FETCH_MEAS_NUM_SAMPLES to set the\nnumber of samples to fetch when performing a measurement. For more\ninformation about when to use this attribute, refer to the `NI\nKnowledgeBase <javascript:WWW(WWW_KB_MEAS)>`__.\n'
                },
                'name': 'measurementWaveformSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns an array whose length is the number of waveforms times\n**measurementWaveformSize**; call niScope_ActualNumWfms to determine the number of\nwaveforms; call niScope_ActualMeasWfmSize to determine the size of each\nwaveform.\n\nNI-SCOPE returns this data sequentially, so all record 0 waveforms are\nfirst. For example, with channel list of 0, 1, you would have the\nfollowing index values:\n\nindex 0 = record 0, channel 0\n\nindex *x* = record 0, channel 1\n\nindex 2\\ *x* = record 1, channel 0\n\nindex 3\\ *x* = record 1, channel 1\n\nWhere *x* = the record length\n'
                },
                'name': 'measWfm',
                'size': {
                    'mechanism': 'python-code',
                    'value': '(measurement_waveform_size * self._actual_num_wfms())'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns a list of class instances with the following timing and scaling\ninformation about each waveform:\n\n-  **relativeInitialX**—the time (in seconds) from the trigger to the\n   first sample in the fetched waveform\n-  **absoluteInitialX**—timestamp (in seconds) of the first fetched\n   sample. This timestamp is comparable between records and\n   acquisitions; devices that do not support this parameter use 0 for\n   this output.\n-  **xIncrement**—the time between points in the acquired waveform in\n   seconds\n-  **actualSamples**—the actual number of samples fetched and placed in\n   the waveform array\n-  **gain**—the gain factor of the given channel; useful for scaling\n   binary data with the following formula:\n\nvoltage = binary data × gain factor + offset\n\n-  **offset**—the offset factor of the given channel; useful for scaling\n   binary data with the following formula:\n\nvoltage = binary data × gain factor + offset\n\nCall niScope_ActualNumWfms to determine the size of this array.\n'
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
                'default_value': 'hightime.timedelta(seconds=5.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe time to wait in seconds for data to be acquired; using 0 for this\nparameter tells NI-SCOPE to fetch whatever is currently available. Using\n-1 for this parameter implies infinite timeout.\n'
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
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
                    'description': '\nReturns a list of class instances with the following timing and scaling\ninformation about each waveform:\n\n-  **relativeInitialX**—the time (in seconds) from the trigger to the\n   first sample in the fetched waveform\n-  **absoluteInitialX**—timestamp (in seconds) of the first fetched\n   sample. This timestamp is comparable between records and\n   acquisitions; devices that do not support this parameter use 0 for\n   this output.\n-  **xIncrement**—the time between points in the acquired waveform in\n   seconds\n-  **actualSamples**—the actual number of samples fetched and placed in\n   the waveform array\n-  **gain**—the gain factor of the given channel; useful for scaling\n   binary data with the following formula:\n\nvoltage = binary data × gain factor + offset\n\n-  **offset**—the offset factor of the given channel; useful for scaling\n   binary data with the following formula:\n\nvoltage = binary data × gain factor + offset\n\nCall niScope_ActualNumWfms to determine the size of this array.\n'
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
                'default_value': 'hightime.timedelta(seconds=5.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe time to wait in seconds for data to be acquired; using 0 for this\nparameter tells NI-SCOPE to fetch whatever is currently available. Using\n-1 for this parameter implies infinite timeout.\n'
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
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
                    'description': '\nReturns a list of class instances with the following timing and scaling\ninformation about each waveform:\n\n-  **relativeInitialX**—the time (in seconds) from the trigger to the\n   first sample in the fetched waveform\n-  **absoluteInitialX**—timestamp (in seconds) of the first fetched\n   sample. This timestamp is comparable between records and\n   acquisitions; devices that do not support this parameter use 0 for\n   this output.\n-  **xIncrement**—the time between points in the acquired waveform in\n   seconds\n-  **actualSamples**—the actual number of samples fetched and placed in\n   the waveform array\n-  **gain**—the gain factor of the given channel; useful for scaling\n   binary data with the following formula:\n\nvoltage = binary data × gain factor + offset\n\n-  **offset**—the offset factor of the given channel; useful for scaling\n   binary data with the following formula:\n\nvoltage = binary data × gain factor + offset\n\nCall niScope_ActualNumWfms to determine the size of this array.\n'
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
                'default_value': 'hightime.timedelta(seconds=5.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe time to wait in seconds for data to be acquired; using 0 for this\nparameter tells NI-SCOPE to fetch whatever is currently available. Using\n-1 for this parameter implies infinite timeout.\n'
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
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
                    'description': '\nReturns a list of class instances with the following timing and scaling\ninformation about each waveform:\n\n-  **relativeInitialX**—the time (in seconds) from the trigger to the\n   first sample in the fetched waveform\n-  **absoluteInitialX**—timestamp (in seconds) of the first fetched\n   sample. This timestamp is comparable between records and\n   acquisitions; devices that do not support this parameter use 0 for\n   this output.\n-  **xIncrement**—the time between points in the acquired waveform in\n   seconds\n-  **actualSamples**—the actual number of samples fetched and placed in\n   the waveform array\n-  **gain**—the gain factor of the given channel; useful for scaling\n   binary data with the following formula:\n\nvoltage = binary data × gain factor + offset\n\n-  **offset**—the offset factor of the given channel; useful for scaling\n   binary data with the following formula:\n\nvoltage = binary data × gain factor + offset\n\nCall niScope_ActualNumWfms to determine the size of this array.\n'
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
                    'description': "\nnumpy array of the appropriate type and size that should be acquired as a 1D array. Size should be **num_samples** times number of waveforms. Call niScope_ActualNumWfms to determine the number of waveforms.\n\nTypes supported are\n\n- `numpy.float64`\n- `numpy.int8`\n- `numpy.in16`\n- `numpy.int32`\n\nExample:\n\n.. code-block:: python\n\n    waveform = numpy.ndarray(num_samples * session.actual_num_wfms(), dtype=numpy.float64)\n    wfm_info = session['0,1'].fetch_into(waveform, timeout=5.0)"
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
                'default_value': 'hightime.timedelta(seconds=5.0)',
                'direction': 'in',
                'documentation': {
                    'description': 'The time to wait in seconds for data to be acquired; using 0 for this parameter tells NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout.'
                },
                'name': 'timeout',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns a list of class instances with the following timing and scaling information about each waveform:\n\n-  **relative_initial_x** (float) the time (in seconds) from the trigger to the first sample in the fetched waveform\n-  **absolute_initial_x** (float) timestamp (in seconds) of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output.\n-  **x_increment** (float) the time between points in the acquired waveform in seconds\n-  **channel** (str) channel name this waveform was acquired from\n-  **record** (int) record number of this waveform\n-  **gain** (float) the gain factor of the given channel; useful for scaling binary data with the following formula:\n\n    .. math::\n\n        voltage = binary data * gain factor + offset\n\n-  **offset** (float) the offset factor of the given channel; useful for scaling binary data with the following formula:\n\n    .. math::\n\n        voltage = binary data * gain factor + offset\n\n- **samples** (array of float) floating point array of samples. Length will be of the actual samples acquired\n'
                },
                'name': 'wfmInfo',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'self._actual_num_wfms()'
                },
                'type': 'struct niScope_wfmInfo[]'
            }
        ],
        'python_name': 'fetch',
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
                'default_value': 'hightime.timedelta(seconds=5.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe time to wait in seconds for data to be acquired; using 0 for this\nparameter tells NI-SCOPE to fetch whatever is currently available. Using\n-1 for this parameter implies infinite timeout.\n'
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
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
                'python_api_converter_name': 'convert_to_bytes',
                'size': {
                    'mechanism': 'len',
                    'value': 'sizeInBytes'
                },
                'type': 'ViInt8[]',
                'type_in_documentation': 'bytes'
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
                'default_value': 'hightime.timedelta(seconds=5.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe time to wait in seconds for data to be acquired; using 0 for this\nparameter tells NI-SCOPE to fetch whatever is currently available. Using\n-1 for this parameter implies infinite timeout.\n'
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
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
                    'description': '\nReturns a list of class instances with the following timing and scaling\ninformation about each waveform:\n\n-  **relativeInitialX**—the time (in seconds) from the trigger to the\n   first sample in the fetched waveform\n-  **absoluteInitialX**—timestamp (in seconds) of the first fetched\n   sample. This timestamp is comparable between records and\n   acquisitions; devices that do not support this parameter use 0 for\n   this output.\n-  **xIncrement**—the time between points in the acquired waveform in\n   seconds\n-  **actualSamples**—the actual number of samples fetched and placed in\n   the waveform array\n-  **gain**—the gain factor of the given channel; useful for scaling\n   binary data with the following formula:\n\nvoltage = binary data × gain factor + offset\n\n-  **offset**—the offset factor of the given channel; useful for scaling\n   binary data with the following formula:\n\nvoltage = binary data × gain factor + offset\n\nCall niScope_ActualNumWfms to determine the size of this array.\n'
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
        'python_name': '_close',
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
