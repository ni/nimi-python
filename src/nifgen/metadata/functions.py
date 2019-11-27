# -*- coding: utf-8 -*-
# This file is generated from NI-FGEN API metadata version 19.6.0d4
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
    'ExportAttributeConfigurationBuffer': {
        'documentation': {
            'description': '\nExports the attribute configuration of the session to a configuration\nbuffer.\n\nYou can export and import session attribute configurations only between\ndevices with identical model numbers, channel counts, and onboard memory\nsizes.\n\nThis function verifies that the attributes you have configured for the\nsession are valid. If the configuration is invalid, NI‑FGEN returns an\nerror.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niFgen_init that identifies a\nparticular instrument session.\n'
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
            'description': '\nExports the attribute configuration of the session to the specified\nfile.\n\nYou can export and import session attribute configurations only between\ndevices with identical model numbers, channel counts, and onboard memory\nsizes.\n\nThis function verifies that the attributes you have configured for the\nsession are valid. If the configuration is invalid, NI‑FGEN returns an\nerror.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niFgen_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the absolute path to the file to contain the exported\nattribute configuration. If you specify an empty or relative path, this\nfunction returns an error.\n**Default file extension:** .nifgenconfig\n'
                },
                'name': 'filePath',
                'type': 'ViConstString'
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
    'GetChannelName': {
        'documentation': {
            'description': '\nReturns the channel string that is in the channel table at an index you\nspecify.\n',
            'note': '\nThis function is included for compliance with the IviFgen Class\nSpecification.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niFgen_init that identifies a\nparticular instrument session.\n'
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
    'ImportAttributeConfigurationBuffer': {
        'documentation': {
            'description': '\nImports an attribute configuration to the session from the specified\nconfiguration buffer.\n\nYou can export and import session attribute configurations only between\ndevices with identical model numbers, channel counts, and onboard memory\nsizes.\n\n\n',
            'note': '\nYou cannot call this function while the session is in a running state,\nsuch as while generating a signal.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niFgen_init that identifies a\nparticular instrument session.\n'
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
            'description': '\nImports an attribute configuration to the session from the specified\nfile.\n\nYou can export and import session attribute configurations only between\ndevices with identical model numbers, channel counts, and onboard memory\nsizes.\n',
            'note': '\nYou cannot call this function while the session is in a running state,\nsuch as while generating a signal.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niFgen_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the absolute path to the file containing the attribute\nconfiguration to import. If you specify an empty or relative path, this\nfunction returns an error.\n**Default File Extension:** .nifgenconfig\n'
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
        'python_name': '_close',
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
