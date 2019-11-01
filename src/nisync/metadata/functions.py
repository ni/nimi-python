# -*- coding: utf-8 -*-
# This file is generated from NI-Sync API metadata version 20.0.0d0
functions = {
    'CalAdjustClk10PhaseVoltage': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nThis function adjusts the Clk10 Phase CalDAC voltage. NOTE: The voltage\nis not committed to the calibration ROM unless the Action parameter to\nniSync_CloseExtCal is set to "Commit". NOTE: This operation will only\nsucceed if invoked on an external calibration session, i.e. a session\ncreated with niSync_InitExtCal. NOTE: The existing Clk10 Phase CalDAC\nvoltage can be retrieved using the niSync_CalGetClk10PhaseVoltage\nfunction.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_InitExtCal. The handle\nidentifies a particular instrument session. Default Value: None\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis parameter specifies the new voltage value, in units of volts, for\nthe Clk10 Phase CalDAC voltage.\n'
                },
                'name': 'newVoltage',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThis parameter returns the previous Clk10 Phase CalDAC voltage, in units\nof volts.\n'
                },
                'name': 'oldVoltage',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalAdjustDdsInitialPhase': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'TBD'
        },
        'parameters': [
            {
                'direction': 'in',
                'name': 'extCalVi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'measuredPhase',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'oldPhase',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalAdjustDdsStartPulsePhaseVoltage': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nThis function adjusts the DDS Start Pulse Phase CalDAC voltage. NOTE:\nThe voltage is not committed to the calibration ROM unless the Action\nparameter to niSync_CloseExtCal is set to "Commit". NOTE: This\noperation will only succeed if invoked on an external calibration\nsession, i.e. a session created with niSync_InitExtCal. NOTE: The\nexisting DDS Start Pulse Phase CalDAC voltage can be retrieved using the\nniSync_CalGetDDSStartPulsePhaseVoltage function.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_InitExtCal. The handle\nidentifies a particular instrument session. Default Value: None\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis parameter specifies the new voltage value, in units of volts, for\nthe DDS Start Pulse Phase CalDAC voltage.\n'
                },
                'name': 'newVoltage',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThis parameter returns the previous DDS Start Pulse Phase CalDAC\nvoltage, in units of volts.\n'
                },
                'name': 'oldVoltage',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalAdjustOscillatorVoltage': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nThis function adjusts the OCXO/TCXO CalDAC voltage. NOTE: The voltage is\nnot committed to the calibration ROM unless the Action parameter to\nniSync_CloseExtCal is set to "Commit". NOTE: This operation will only\nsucceed if invoked on an external calibration session, i.e. a session\ncreated with niSync_InitExtCal. NOTE: The existing OCXO/TCXO CalDAC\nvoltage can be retrieved using the niSync_CalGetOscillatorVoltage\nfunction.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_InitExtCal. The handle\nidentifies a particular instrument session. Default Value: None\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis parameter specifies the new voltage value, in units of volts, for\nthe OCXO/TCXO CalDAC voltage.\n'
                },
                'name': 'newVoltage',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThis parameter returns the previous OCXO/TCXO CalDAC voltage, in units\nof volts.\n'
                },
                'name': 'oldVoltage',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalGetClk10PhaseVoltage': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nThis function returns the existing Clk10 Phase CalDAC voltage, in units\nof volts. Note: A calibration password is not required to use this\nfunction. It can be called with an instrument handle created with either\nniSync_init or niSync_InitExtCal.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis parameter specifies the session handle that you obtain from\nniSync_init or niSync_InitExtCal. The handle identifies a particular\ninstrument session. Default Value: None\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThis function returns the existing Clk10 Phase CalDAC voltage, in units\nof volts.\n'
                },
                'name': 'voltage',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalGetDdsInitialPhase': {
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
                'name': 'phase',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalGetDdsStartPulsePhaseVoltage': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nThis function returns the existing DDS Start Pulse Phase CalDAC voltage,\nin units of volts. Note: A calibration password is not required to use\nthis function. It can be invoked with an instrument handle created with\neither niSync_init or niSync_InitExtCal.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis parameter specifies the session handle that you obtain from\nniSync_init or niSync_InitExtCal. The handle identifies a particular\ninstrument session. Default Value: None\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThis parameter returns the existing DDS Start Pulse Phase CalDAC\nvoltage, in units of volts.\n'
                },
                'name': 'voltage',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalGetOscillatorVoltage': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nThis function returns the existing OCXO/TCXO CalDAC voltage, in units of\nvolts. Note: A calibration password is not required to use this\nfunction. It can be invoked with an instrument handle created with\neither niSync_init or niSync_InitExtCal.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis parameter specifies the session handle that you obtain from\nniSync_init or niSync_InitExtCal. The handle identifies a particular\ninstrument session. Default Value: None\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThis parameter returns the existing OCXO/TCXO CalDAC voltage, in units\nof volts.\n'
                },
                'name': 'voltage',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ChangeExtCalPassword': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nThis function changes the external calibration password for the module.\nNOTE: The existing calibration password must be supplied for this\noperation to succeed.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis parameter specifies the session handle that you obtain from\nniSync_init or niSync_InitExtCal. The handle identifies a particular\ninstrument session. Default Value: None\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis parameter specifies the old external calibration password for the\nmodule.\n',
                    'note': '\nThis parameter must exactly match the value in the\nmodule\'s calibration ROM for this operation to succeed. Default Value:\n""\n'
                },
                'name': 'oldPassword',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis parameter specifies the new external calibration password for the\nmodule. Default Value: ""\n'
                },
                'name': 'newPassword',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearClock': {
        'documentation': {
            'description': '\nThis function clears a clock created by the niSync_CreateClock\nfunction. Once the clock is cleared, the associated terminal may be used\nfor other operations. When this function is called, the specified line\nis tri-stated.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nAn input string enumeration that specifies the terminal containing the\ndigital signal that is the specified clock. Valid Values:\nNISYNC_VAL_PFI0 NISYNC_VAL_PFI1 NISYNC_VAL_PFI2\nNISYNC_VAL_PXITRIG0 NISYNC_VAL_PXITRIG1 NISYNC_VAL_PXITRIG2\nNISYNC_VAL_PXITRIG3 NISYNC_VAL_PXITRIG4 NISYNC_VAL_PXITRIG5\nNISYNC_VAL_PXITRIG6 NISYNC_VAL_PXITRIG7 NISYNC_VAL_PXISTAR0\nNISYNC_VAL_PXISTAR1 NISYNC_VAL_PXISTAR2 NISYNC_VAL_PXISTAR3\nNISYNC_VAL_PXISTAR4 NISYNC_VAL_PXISTAR5 NISYNC_VAL_PXISTAR6\nNISYNC_VAL_PXISTAR7 NISYNC_VAL_PXISTAR8 NISYNC_VAL_PXISTAR9\nNISYNC_VAL_PXISTAR10 NISYNC_VAL_PXISTAR11 NISYNC_VAL_PXISTAR12\nNISYNC_VAL_ALL_CONNECTED If NISYNC_VAL_ALL_CONNECTED is specified,\nall clocks created within the context of this session are cleared.\n'
                },
                'name': 'terminal',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearFutureTimeEvents': {
        'documentation': {
            'description': '\nThis function clears future time events created by the\nniSync_CreateFutureTimeEvent function that have not yet occurred. Once\nthe future time events are cleared, the associated terminal can be used\nfor other operations. When this function is called, the specified line\nis tri-stated.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nAn input string enumeration that specifies the terminal that will no\nlonger generate future time events. Valid Values: NISYNC_VAL_PFI0\nNISYNC_VAL_PFI1 NISYNC_VAL_PFI2 NISYNC_VAL_PXITRIG0\nNISYNC_VAL_PXITRIG1 NISYNC_VAL_PXITRIG2 NISYNC_VAL_PXITRIG3\nNISYNC_VAL_PXITRIG4 NISYNC_VAL_PXITRIG5 NISYNC_VAL_PXITRIG6\nNISYNC_VAL_PXITRIG7 NISYNC_VAL_PXISTAR0 NISYNC_VAL_PXISTAR1\nNISYNC_VAL_PXISTAR2 NISYNC_VAL_PXISTAR3 NISYNC_VAL_PXISTAR4\nNISYNC_VAL_PXISTAR5 NISYNC_VAL_PXISTAR6 NISYNC_VAL_PXISTAR7\nNISYNC_VAL_PXISTAR8 NISYNC_VAL_PXISTAR9 NISYNC_VAL_PXISTAR10\nNISYNC_VAL_PXISTAR11 NISYNC_VAL_PXISTAR12\nNISYNC_VAL_ALL_CONNECTED If NISYNC_VAL_ALL_CONNECTED is specified,\nall future time events created within the context of this session are\ncleared.\n'
                },
                'name': 'terminal',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'CloseExtCal': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nThis function performs the following operations: - Closes the instrument\nI/O session. - Commits the external calibration constants to the\nmodule\'s calibration ROM, if the action parameter is set to "Commit". -\nDestroys the instrument driver session and all of its attributes. -\nDeallocates any memory resources the driver uses. Note: If the session\nis locked, you must unlock the session before calling\nniSync_CloseExtCal. Note: After calling niSync_CloseExtCal, you cannot\nuse the instrument driver again until you call niSync_init or\nniSync_InitExtCal.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe ViSession handle that you obtain from the test_init or\ntest_InitWithOptions function. The handle identifies a particular\ninstrument session. Default Value: None\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThis input specifies whether or not the external calibration constants\nset using the CalAdjust functions should be committed to the module's\ncalibration ROM. Valid Values: NISYNC_VAL_EXT_CAL_ABORT (Default\nValue) NISYNC_VAL_EXT_CAL_COMMIT\n"
                },
                'name': 'action',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureFpga': {
        'documentation': {
            'description': '\nThis function programs the FPGA on the module with an alternate\nbitstream file. The bitstream is specified using an absolute path to a\nlocation on disk. NOTE: This function is an advanced operation and\nshould be used with caution.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'This input specifies the full path to an FPGA bitstream file on disk.'
                },
                'name': 'fpgaProgramPath',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConnectClkTerminals': {
        'documentation': {
            'description': '\nThis function connects a source clock terminal to a destination clock\nterminal. A clock terminal connection is characterized by its source\nterminal and destination terminal.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis input specifies the source clock terminal to connect to the\ndestination terminal. Valid Values: NISYNC_VAL_CLKIN (Default Value)\nNISYNC_VAL_CLK10 NISYNC_VAL_OSCILLATOR NISYNC_VAL_DDS\nNISYNC_VAL_PFILVDS0 NISYNC_VAL_PFILVDS1 NISYNC_VAL_PFILVDS2\nNISYNC_VAL_PXIEDSTARC0 NISYNC_VAL_PXIEDSTARC1\nNISYNC_VAL_PXIEDSTARC2 NISYNC_VAL_PXIEDSTARC3\nNISYNC_VAL_PXIEDSTARC4 NISYNC_VAL_PXIEDSTARC5\nNISYNC_VAL_PXIEDSTARC6 NISYNC_VAL_PXIEDSTARC7\nNISYNC_VAL_PXIEDSTARC8 NISYNC_VAL_PXIEDSTARC9\nNISYNC_VAL_PXIEDSTARC10 NISYNC_VAL_PXIEDSTARC11\nNISYNC_VAL_PXIEDSTARC12 NISYNC_VAL_PXIEDSTARC13\nNISYNC_VAL_PXIEDSTARC14 NISYNC_VAL_PXIEDSTARC15\nNISYNC_VAL_PXIEDSTARC16 NISYNC_VAL_PXIEDSTARA\n',
                    'note': '\nEach\nPXIe_DStarC trigger is mapped to a single slot. This mapping is vendor\nspecific. Your chassis documentation may describe this mapping in\naddition to the chassis.ini and pxisys.ini system description files the\nPXI Specification requires.\n'
                },
                'name': 'sourceTerminal',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis input specifies the destination clock terminal that the source\nterminal will connect to. Valid Values: NISYNC_VAL_CLK10_IN (Default\nValue) NISYNC_VAL_CLKOUT NISYNC_VAL_BOARD_CLK NISYNC_VAL_PFILVDS0\nNISYNC_VAL_PFILVDS1 NISYNC_VAL_PFILVDS2 NISYNC_VAL_PXIEDSTARA0\nNISYNC_VAL_PXIEDSTARA1 NISYNC_VAL_PXIEDSTARA2\nNISYNC_VAL_PXIEDSTARA3 NISYNC_VAL_PXIEDSTARA4\nNISYNC_VAL_PXIEDSTARA5 NISYNC_VAL_PXIEDSTARA6\nNISYNC_VAL_PXIEDSTARA7 NISYNC_VAL_PXIEDSTARA8\nNISYNC_VAL_PXIEDSTARA9 NISYNC_VAL_PXIEDSTARA10\nNISYNC_VAL_PXIEDSTARA11 NISYNC_VAL_PXIEDSTARA12\nNISYNC_VAL_PXIEDSTARA13 NISYNC_VAL_PXIEDSTARA14\nNISYNC_VAL_PXIEDSTARA15 NISYNC_VAL_PXIEDSTARA16\n',
                    'note': '\nEach\nPXIe_DStarA trigger is mapped to a single slot. This mapping is vendor\nspecific. Your chassis documentation may describe this mapping in\naddition to the chassis.ini and pxisys.ini system description files the\nPXI Specification requires.\n'
                },
                'name': 'destinationTerminal',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConnectSwTrigToTerminal': {
        'documentation': {
            'description': '\nThis function connects the global software trigger terminal to a\ndestination trigger terminal. A software trigger terminal connection is\ncharacterized by its source terminal, destination terminal, and a\nsynchronization clock. The signal at the destination terminal can be\ninverted, synchronized to the rising or falling edge of the\nsynchronization clock, and delayed by up to 15 synchronization clock\ncycles.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis input specifies the source software trigger terminal to connect to\nthe destination terminal. Valid Values: NISYNC_VAL_SWTRIG_GLOBAL\n(Default Value)\n'
                },
                'name': 'sourceTerminal',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis input specifies the destination trigger terminal that the global\nsoftware trigger terminal will connect to. Valid Values:\nNISYNC_VAL_PXITRIG0 (Default Value) NISYNC_VAL_PXITRIG1\nNISYNC_VAL_PXITRIG2 NISYNC_VAL_PXITRIG3 NISYNC_VAL_PXITRIG4\nNISYNC_VAL_PXITRIG5 NISYNC_VAL_PXITRIG6 NISYNC_VAL_PXITRIG7\nNISYNC_VAL_PXISTAR0 NISYNC_VAL_PXISTAR1 NISYNC_VAL_PXISTAR2\nNISYNC_VAL_PXISTAR3 NISYNC_VAL_PXISTAR4 NISYNC_VAL_PXISTAR5\nNISYNC_VAL_PXISTAR6 NISYNC_VAL_PXISTAR7 NISYNC_VAL_PXISTAR8\nNISYNC_VAL_PXISTAR9 NISYNC_VAL_PXISTAR10 NISYNC_VAL_PXISTAR11\nNISYNC_VAL_PXISTAR12 NISYNC_VAL_PXISTAR13 NISYNC_VAL_PXISTAR14\nNISYNC_VAL_PXISTAR15 NISYNC_VAL_PXISTAR16 NISYNC_VAL_PXISTAR\nNISYNC_VAL_PFI0 NISYNC_VAL_PFI1 NISYNC_VAL_PFI2 NISYNC_VAL_PFI3\nNISYNC_VAL_PFI4 NISYNC_VAL_PFI5 NISYNC_VAL_PFILVDS0\nNISYNC_VAL_PFILVDS1 NISYNC_VAL_PFILVDS2 NISYNC_VAL_PXIEDSTARB0\nNISYNC_VAL_PXIEDSTARB1 NISYNC_VAL_PXIEDSTARB2\nNISYNC_VAL_PXIEDSTARB3 NISYNC_VAL_PXIEDSTARB4\nNISYNC_VAL_PXIEDSTARB5 NISYNC_VAL_PXIEDSTARB6\nNISYNC_VAL_PXIEDSTARB7 NISYNC_VAL_PXIEDSTARB8\nNISYNC_VAL_PXIEDSTARB9 NISYNC_VAL_PXIEDSTARB10\nNISYNC_VAL_PXIEDSTARB11 NISYNC_VAL_PXIEDSTARB12\nNISYNC_VAL_PXIEDSTARB13 NISYNC_VAL_PXIEDSTARB14\nNISYNC_VAL_PXIEDSTARB15 NISYNC_VAL_PXIEDSTARB16\nNISYNC_VAL_PXIEDSTARC\n',
                    'note': '\nEach PXI_Star and PXIe_DStarB trigger is\nmapped to a single slot. This mapping is vendor specific. Your chassis\ndocumentation may describe this mapping in addition to the chassis.ini\nand pxisys.ini system description files the PXI Specification requires.\n'
                },
                'name': 'destinationTerminal',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis input specifies the synchronization clock to use to synchronize the\ndestination terminal with the global software trigger terminal.\n',
                    'note': [
                        '\r\nAsynchronous connections are not valid for software trigger terminal\r\nconnections.',
                        '\r\nThe source of the synchronization clock for software trigger connections\r\nis determined by the destination terminal trigger "zone" ("front" for\r\nthe PFI lines, and "rear" for the PXI\\_Trig and PXI\\_Star terminals).\r\nThe source of the synchronization clock for a given trigger zone can be\r\nselected using the NISYNC\\_ATTR\\_FRONT\\_SYNC\\_CLK\\_SRC (PFI zone) and\r\nNISYNC\\_ATTR\\_REAR\\_SYNC\\_CLK\\_SRC (PXI backplane zone) attributes.\r\nValid Values: NISYNC\\_VAL\\_SYNC\\_CLK\\_FULLSPEED (Default Value)\r\nNISYNC\\_VAL\\_SYNC\\_CLK\\_DIV1 NISYNC\\_VAL\\_SYNC\\_CLK\\_DIV2'
                    ]
                },
                'name': 'synchronizationClock',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis input specifies whether or not the global software trigger terminal\nshould be inverted at the destination terminal. Valid Values:\nNISYNC_VAL_DONT_INVERT (Default Value) NISYNC_VAL_INVERT\n'
                },
                'name': 'invert',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis input specifies the synchronization clock update edge that the\nglobal software trigger should be propagated on. Valid Values:\nNISYNC_VAL_UPDATE_EDGE_RISING (Default Value)\nNISYNC_VAL_UPDATE_EDGE_FALLING\n'
                },
                'name': 'updateEdge',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis input specifies the number of seconds to delay the global software\ntrigger pulse. The delay must be a multiple of the synchronization clock\nperiod. The global software trigger can be delayed up to 15 clock cycles\nfor each route. Default Value: 0.00 seconds\n',
                    'note': '\nThis input is not\nsupported on the PXIe-6674.\n'
                },
                'name': 'delay',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConnectTrigTerminals': {
        'documentation': {
            'description': '\nThis function connects a source trigger terminal to a destination\ntrigger terminal. A trigger terminal connection is characterized by its\nsource terminal, destination terminal, and a synchronization clock. The\nsignal at the destination terminal can be inverted and synchronized to\nthe rising or falling edge of the synchronization clock.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis input specifies the source trigger terminal to connect to the\ndestination terminal.\n',
                    'note': [
                        ' Each PXI\\_Star and PXIe\\_DStarC trigger is\r\nmapped to a single slot. This mapping is vendor specific. Your chassis\r\ndocumentation may describe this mapping in addition to the chassis.ini\r\nand pxisys.ini system description files the PXI Specification requires.',
                        ' The source of the synchronization clock for\r\ntrigger connections is determined by the destination terminal (either\r\nthe PFI sync clock zone or the backplane sync clock zone). Also, the two\r\ndivided versions of the synchronization clock are shared between the PFI\r\nsync clock zone and the backplane sync clock zone. Valid Values:\r\nNISYNC\\_VAL\\_PXITRIG0 (Default Value) NISYNC\\_VAL\\_PXITRIG1\r\nNISYNC\\_VAL\\_PXITRIG2 NISYNC\\_VAL\\_PXITRIG3 NISYNC\\_VAL\\_PXITRIG4\r\nNISYNC\\_VAL\\_PXITRIG5 NISYNC\\_VAL\\_PXITRIG6 NISYNC\\_VAL\\_PXITRIG7\r\nNISYNC\\_VAL\\_PXISTAR0 NISYNC\\_VAL\\_PXISTAR1 NISYNC\\_VAL\\_PXISTAR2\r\nNISYNC\\_VAL\\_PXISTAR3 NISYNC\\_VAL\\_PXISTAR4 NISYNC\\_VAL\\_PXISTAR5\r\nNISYNC\\_VAL\\_PXISTAR6 NISYNC\\_VAL\\_PXISTAR7 NISYNC\\_VAL\\_PXISTAR8\r\nNISYNC\\_VAL\\_PXISTAR9 NISYNC\\_VAL\\_PXISTAR10 NISYNC\\_VAL\\_PXISTAR11\r\nNISYNC\\_VAL\\_PXISTAR12 NISYNC\\_VAL\\_PXISTAR13 NISYNC\\_VAL\\_PXISTAR14\r\nNISYNC\\_VAL\\_PXISTAR15 NISYNC\\_VAL\\_PXISTAR16 NISYNC\\_VAL\\_PXISTAR\r\nNISYNC\\_VAL\\_PFI0 NISYNC\\_VAL\\_PFI1 NISYNC\\_VAL\\_PFI2 NISYNC\\_VAL\\_PFI3\r\nNISYNC\\_VAL\\_PFI4 NISYNC\\_VAL\\_PFI5 NISYNC\\_VAL\\_PFILVDS0\r\nNISYNC\\_VAL\\_PFILVDS1 NISYNC\\_VAL\\_PFILVDS2 NISYNC\\_VAL\\_GND\r\nNISYNC\\_VAL\\_SYNC\\_CLK\\_FULLSPEED NISYNC\\_VAL\\_SYNC\\_CLK\\_DIV1\r\nNISYNC\\_VAL\\_SYNC\\_CLK\\_DIV2 NISYNC\\_VAL\\_CLKIN NISYNC\\_VAL\\_PXIEDSTARC0\r\nNISYNC\\_VAL\\_PXIEDSTARC1 NISYNC\\_VAL\\_PXIEDSTARC2\r\nNISYNC\\_VAL\\_PXIEDSTARC3 NISYNC\\_VAL\\_PXIEDSTARC4\r\nNISYNC\\_VAL\\_PXIEDSTARC5 NISYNC\\_VAL\\_PXIEDSTARC6\r\nNISYNC\\_VAL\\_PXIEDSTARC7 NISYNC\\_VAL\\_PXIEDSTARC8\r\nNISYNC\\_VAL\\_PXIEDSTARC9 NISYNC\\_VAL\\_PXIEDSTARC10\r\nNISYNC\\_VAL\\_PXIEDSTARC11 NISYNC\\_VAL\\_PXIEDSTARC12\r\nNISYNC\\_VAL\\_PXIEDSTARC13 NISYNC\\_VAL\\_PXIEDSTARC14\r\nNISYNC\\_VAL\\_PXIEDSTARC15 NISYNC\\_VAL\\_PXIEDSTARC16\r\nNISYNC\\_VAL\\_PXIEDSTARB'
                    ]
                },
                'name': 'sourceTerminal',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis input specifies the destination trigger terminal that the source\nterminal will connect to. Valid Values: NISYNC_VAL_PXITRIG0\nNISYNC_VAL_PXITRIG1 (Default Value) NISYNC_VAL_PXITRIG2\nNISYNC_VAL_PXITRIG3 NISYNC_VAL_PXITRIG4 NISYNC_VAL_PXITRIG5\nNISYNC_VAL_PXITRIG6 NISYNC_VAL_PXITRIG7 NISYNC_VAL_PXISTAR0\nNISYNC_VAL_PXISTAR1 NISYNC_VAL_PXISTAR2 NISYNC_VAL_PXISTAR3\nNISYNC_VAL_PXISTAR4 NISYNC_VAL_PXISTAR5 NISYNC_VAL_PXISTAR6\nNISYNC_VAL_PXISTAR7 NISYNC_VAL_PXISTAR8 NISYNC_VAL_PXISTAR9\nNISYNC_VAL_PXISTAR10 NISYNC_VAL_PXISTAR11 NISYNC_VAL_PXISTAR12\nNISYNC_VAL_PXISTAR13 NISYNC_VAL_PXISTAR14 NISYNC_VAL_PXISTAR15\nNISYNC_VAL_PXISTAR16 NISYNC_VAL_PXISTAR NISYNC_VAL_PFI0\nNISYNC_VAL_PFI1 NISYNC_VAL_PFI2 NISYNC_VAL_PFI3 NISYNC_VAL_PFI4\nNISYNC_VAL_PFI5 NISYNC_VAL_PFILVDS0 NISYNC_VAL_PFILVDS1\nNISYNC_VAL_PFILVDS2 NISYNC_VAL_PXIEDSTARB0 NISYNC_VAL_PXIEDSTARB1\nNISYNC_VAL_PXIEDSTARB2 NISYNC_VAL_PXIEDSTARB3\nNISYNC_VAL_PXIEDSTARB4 NISYNC_VAL_PXIEDSTARB5\nNISYNC_VAL_PXIEDSTARB6 NISYNC_VAL_PXIEDSTARB7\nNISYNC_VAL_PXIEDSTARB8 NISYNC_VAL_PXIEDSTARB9\nNISYNC_VAL_PXIEDSTARB10 NISYNC_VAL_PXIEDSTARB11\nNISYNC_VAL_PXIEDSTARB12 NISYNC_VAL_PXIEDSTARB13\nNISYNC_VAL_PXIEDSTARB14 NISYNC_VAL_PXIEDSTARB15\nNISYNC_VAL_PXIEDSTARB16 NISYNC_VAL_PXIEDSTARC\n',
                    'note': '\nEach PXI_Star\nand PXIe_DStarB trigger is mapped to a single slot. This mapping is\nvendor specific. Your chassis documentation may describe this mapping in\naddition to the chassis.ini and pxisys.ini system description files the\nPXI Specification requires.\n'
                },
                'name': 'destinationTerminal',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis input specifies the synchronization clock to use to synchronize the\ndestination terminal with the source terminal for this connection.\n',
                    'note': '\nThe source of the synchronization clock for trigger connections is\ndetermined by the destination terminal trigger "zone" ("front" for the\nPFI lines, and "rear" for the PXI_Trig and PXI_Star terminals). The\nsource of the synchronization clock for a given trigger zone can be\nselected using the NISYNC_ATTR_FRONT_SYNC_CLK_SRC (PFI zone) and\nNISYNC_ATTR_REAR_SYNC_CLK_SRC (PXI backplane zone) attributes.\nValid Values: NISYNC_VAL_SYNC_CLK_ASYNC\nNISYNC_VAL_SYNC_CLK_FULLSPEED NISYNC_VAL_SYNC_CLK_DIV1\nNISYNC_VAL_SYNC_CLK_DIV2\n'
                },
                'name': 'synchronizationClock',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis input specifies whether or not the signal at the source terminal\nshould be inverted at the destination terminal.\n',
                    'note': '\nThe source and\ndestination must be connected synchronously for the signal to be\ninverted. Valid Values: NISYNC_VAL_DONT_INVERT (Default Value)\nNISYNC_VAL_INVERT\n'
                },
                'name': 'invert',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis input specifies the synhronization clock update edge that a\nconnected signal should be propagated on. Note that the source and\ndestination terminals must be connected synchronously for this parameter\nto apply. Valid Values: NISYNC_VAL_UPDATE_EDGE_RISING (Default\nValue) NISYNC_VAL_UPDATE_EDGE_FALLING\n'
                },
                'name': 'updateEdge',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateClock': {
        'documentation': {
            'description': '\nThis function creates a clock synchronized to the board time associated\nwith the specified instrument handle. The terminal associated with this\nclock cannot be used for other operations until the clock is cleared\nwith the niSync_ClearClock function or the session is closed with the\nniSync_Close function. When this function is called, the digital signal\non the specified terminal is driven low until the clock starts.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nAn input string enumeration that specifies the terminal containing the\ndigital signal that is the specified clock. Valid Values:\nNISYNC_VAL_PXITRIG0 NISYNC_VAL_PXITRIG1 NISYNC_VAL_PXITRIG2\nNISYNC_VAL_PXITRIG3 NISYNC_VAL_PXITRIG4 NISYNC_VAL_PXITRIG5\nNISYNC_VAL_PXITRIG6 NISYNC_VAL_PXITRIG7 NISYNC_VAL_PXISTAR0\nNISYNC_VAL_PXISTAR1 NISYNC_VAL_PXISTAR2 NISYNC_VAL_PXISTAR3\nNISYNC_VAL_PXISTAR4 NISYNC_VAL_PXISTAR5 NISYNC_VAL_PXISTAR6\nNISYNC_VAL_PXISTAR7 NISYNC_VAL_PXISTAR8 NISYNC_VAL_PXISTAR9\nNISYNC_VAL_PXISTAR10 NISYNC_VAL_PXISTAR11 NISYNC_VAL_PXISTAR12\n'
                },
                'name': 'terminal',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nAn input integer that specifies the high ticks of the clock generated on\nthe specified terminal. The clock resolution, which can be queried using\nthe NISYNC_ATTR_1588_CLK_RESOLUTION attribute, determines the length\nof a tick.\n'
                },
                'name': 'highTicks',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nAn input integer that specifies the low ticks of the clock generated on\nthe specified terminal. The clock resolution, which can be queried using\nthe NISYNC_ATTR_1588_CLK_RESOLUTION attribute, determines the length\nof a tick.\n'
                },
                'name': 'lowTicks',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nAn input integer that specifies a portion of the board time when the\nclock generated on the specified terminal will start. Note that NI-Sync\nsupports only the time range between 1 January 1970 and 1 January 2100.\nTherefore, the specified number of seconds is assumed to be within the\nsupported time range. Specify 0 to start the clock immediately.\n'
                },
                'name': 'startTimeSeconds',
                'python_api_converter_name': 'convert_timedelta_to_seconds',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nAn input integer that specifies a portion of the board time when the\nclock generated on the specified terminal will start. Note that NI-Sync\nsupports only the time range between 1 January 1970 and 1 January 2100.\nTherefore, the specified number of nanoseconds is assumed to be within\nthe supported time range. Specify 0 to start the clock immediately.\n'
                },
                'name': 'startTimeNanoseconds',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nAn input integer that specifies a portion of the board time when the\nclock generated on the specified terminal will start. Note that NI-Sync\nsupports only the time range between 1 January 1970 and 1 January 2100.\nTherefore, the specified number of fractional nanoseconds is assumed to\nbe within the supported time range. Specify 0 to start the clock\nimmediately.\n'
                },
                'name': 'startTimeFractionalNsecs',
                'type': 'ViUInt16'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nAn input integer that specifies a portion of the board time when the\nclock generated on the specified terminal will stop. Note that NI-Sync\nsupports only the time range between 1 January 1970 and 1 January 2100.\nTherefore, the specified number of seconds is assumed to be within the\nsupported time range. Specify 0 to never stop the clock.\n'
                },
                'name': 'stopTimeSeconds',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nAn input integer that specifies a portion of the board time when the\nclock generated on the specified terminal will stop. Note that NI-Sync\nsupports only the time range between 1 January 1970 and 1 January 2100.\nTherefore, the specified number of nanoseconds is assumed to be within\nthe supported time range. Specify 0 to never stop the clock.\n'
                },
                'name': 'stopTimeNanoseconds',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nAn input integer that specifies a portion of the board time when the\nclock generated on the specified terminal will stop. Note that NI-Sync\nsupports only the time range between 1 January 1970 and 1 January 2100.\nTherefore, the specified number of fractional nanoseconds is assumed to\nbe within the supported time range. Specify 0 to never stop the clock.\n'
                },
                'name': 'stopTimeFractionalNsecs',
                'type': 'ViUInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateFutureTimeEvent': {
        'documentation': {
            'description': '\nThis function creates a future time event that is synchronized to the\nboard time associated with the specified session handle. To create\nmultiple future time events, invoke this function multiple times. The\nterminal associated with this future time event cannot be used for\noperations other than generating future time events until the future\ntime events are cleared with the niSync_ClearFutureTimeEvents function\nor the session is closed with the niSync_close function. When this\nfunction is invoked, the digital signal on the specified terminal is\ndriven low until the first future time event occurs. Note: The NI-Sync\nfamily of devices uses the TAI timescale.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nAn input string that specifies the terminal generating the digital\nsignal whose state is set to the specified value. Valid Values:\nNISYNC_VAL_PFI0 NISYNC_VAL_PFI1 NISYNC_VAL_PFI2\nNISYNC_VAL_PXITRIG0 NISYNC_VAL_PXITRIG1 NISYNC_VAL_PXITRIG2\nNISYNC_VAL_PXITRIG3 NISYNC_VAL_PXITRIG4 NISYNC_VAL_PXITRIG5\nNISYNC_VAL_PXITRIG6 NISYNC_VAL_PXITRIG7 NISYNC_VAL_PXISTAR0\nNISYNC_VAL_PXISTAR1 NISYNC_VAL_PXISTAR2 NISYNC_VAL_PXISTAR3\nNISYNC_VAL_PXISTAR4 NISYNC_VAL_PXISTAR5 NISYNC_VAL_PXISTAR6\nNISYNC_VAL_PXISTAR7 NISYNC_VAL_PXISTAR8 NISYNC_VAL_PXISTAR9\nNISYNC_VAL_PXISTAR10 NISYNC_VAL_PXISTAR11 NISYNC_VAL_PXISTAR12\n'
                },
                'name': 'terminal',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nAn input integer enumeration that specifies the level to set the digital\nsignal to at the specified time. Valid Values: NISYNC_VAL_LEVEL_LOW\nNISYNC_VAL_LEVEL_HIGH\n'
                },
                'name': 'outputLevel',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nAn input integer that specifies a portion of the board time that\nspecifies when to change to the specified state of the digital signal on\nthe specified terminal. Note that NI-Sync supports only the time range\nbetween 1 January 1970 and 1 January 2100. Therefore, the specified\nnumber of seconds is assumed to be within the supported time range.\nSpecify 0 to generate the future time event immediately.\n'
                },
                'name': 'timeSeconds',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nAn input integer that specifies a portion of the board time that\nspecifies when to change to the specified state of the digital signal on\nthe specified terminal. Note that NI-Sync supports only the time range\nbetween 1 January 1970 and 1 January 2100. Therefore, the specified\nnumber of nanoseconds is assumed to be within the supported time range.\nSpecify 0 to generate the future time event immediately.\n'
                },
                'name': 'timeNanoseconds',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nAn input integer that specifies a portion of the board time that\nspecifies when to change to the specified state of the digital signal on\nthe specified terminal. Note that NI-Sync supports only the time range\nbetween 1 January 1970 and 1 January 2100. Therefore, the specified\nnumber of fractional nanoseconds is assumed to be within the supported\ntime range. Specify 0 to generate the future time event immediately.\n'
                },
                'name': 'timeFractionalNanoseconds',
                'type': 'ViUInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisableGpsTimestamping': {
        'documentation': {
            'description': '\nThis function disables timestamping enabled by\nniSync_EnableGPSTimestamping.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisableIrigTimestamping': {
        'documentation': {
            'description': '\nThis function disables timestamping enabled by\nniSync_EnableIRIGTimestamping. The associated terminal may be used for\nother operations once timestamping has been disabled.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nAn input string that specifies the terminal to which the IRIG input is\nconnected.\n'
                },
                'name': 'terminalName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisableTimeStampTrigger': {
        'documentation': {
            'description': '\nThis function disables a time stamp trigger enabled by the\nniSync_EnableTimeStampTrigger function. Once the time stamp trigger is\ndisabled, the associated terminal may be used for other operations.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nAn input string enumeration that specifies the terminal containing the\ndigital signal that is the trigger to stop time stamping. Valid Values:\nNISYNC_VAL_PFI0 NISYNC_VAL_PFI1 NISYNC_VAL_PFI2\nNISYNC_VAL_PXITRIG0 NISYNC_VAL_PXITRIG1 NISYNC_VAL_PXITRIG2\nNISYNC_VAL_PXITRIG3 NISYNC_VAL_PXITRIG4 NISYNC_VAL_PXITRIG5\nNISYNC_VAL_PXITRIG6 NISYNC_VAL_PXITRIG7 NISYNC_VAL_PXISTAR0\nNISYNC_VAL_PXISTAR1 NISYNC_VAL_PXISTAR2 NISYNC_VAL_PXISTAR3\nNISYNC_VAL_PXISTAR4 NISYNC_VAL_PXISTAR5 NISYNC_VAL_PXISTAR6\nNISYNC_VAL_PXISTAR7 NISYNC_VAL_PXISTAR8 NISYNC_VAL_PXISTAR9\nNISYNC_VAL_PXISTAR10 NISYNC_VAL_PXISTAR11 NISYNC_VAL_PXISTAR12\nNISYNC_VAL_ALL_CONNECTED If NISYNC_VAL_ALL_CONNECTED is specified,\nall time stamp triggers enabled within the context of this session are\ndisabled.\n'
                },
                'name': 'terminal',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisconnectClkTerminals': {
        'documentation': {
            'description': '\nThis function disconnects a source clock terminal from a destination\nclock terminal.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis input specifies the source clock terminal to disconnect from the\ndestination terminal. The source and destination terminals must be\nconnected for this operation to succeed. Valid Values:\nNISYNC_VAL_CLKIN NISYNC_VAL_CLK10 NISYNC_VAL_OSCILLATOR\nNISYNC_VAL_DDS NISYNC_VAL_PFILVDS0 NISYNC_VAL_PFILVDS1\nNISYNC_VAL_PFILVDS2 NISYNC_VAL_PXIEDSTARC0 NISYNC_VAL_PXIEDSTARC1\nNISYNC_VAL_PXIEDSTARC2 NISYNC_VAL_PXIEDSTARC3\nNISYNC_VAL_PXIEDSTARC4 NISYNC_VAL_PXIEDSTARC5\nNISYNC_VAL_PXIEDSTARC6 NISYNC_VAL_PXIEDSTARC7\nNISYNC_VAL_PXIEDSTARC8 NISYNC_VAL_PXIEDSTARC9\nNISYNC_VAL_PXIEDSTARC10 NISYNC_VAL_PXIEDSTARC11\nNISYNC_VAL_PXIEDSTARC12 NISYNC_VAL_PXIEDSTARC13\nNISYNC_VAL_PXIEDSTARC14 NISYNC_VAL_PXIEDSTARC15\nNISYNC_VAL_PXIEDSTARC16 NISYNC_VAL_PXIEDSTARA\nNISYNC_VAL_ALL_CONNECTED (Default Value)\n',
                    'note': '\nEach PXIe_DStarC\ntrigger is mapped to a single slot. This mapping is vendor specific.\nYour chassis documentation may describe this mapping in addition to the\nchassis.ini and pxisys.ini system description files the PXI\nSpecification requires.\n'
                },
                'name': 'sourceTerminal',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis input specifies the destination clock terminal that the source\nterminal will disconnect from. The source and destination must be\nconnected for this operation to succeed. Valid Values:\nNISYNC_VAL_CLKIN NISYNC_VAL_CLK10_IN NISYNC_VAL_CLKOUT\nNISYNC_VAL_BOARD_CLK NISYNC_VAL_PFILVDS0 NISYNC_VAL_PFILVDS1\nNISYNC_VAL_PFILVDS2 NISYNC_VAL_PXIEDSTARA0 NISYNC_VAL_PXIEDSTARA1\nNISYNC_VAL_PXIEDSTARA2 NISYNC_VAL_PXIEDSTARA3\nNISYNC_VAL_PXIEDSTARA4 NISYNC_VAL_PXIEDSTARA5\nNISYNC_VAL_PXIEDSTARA6 NISYNC_VAL_PXIEDSTARA7\nNISYNC_VAL_PXIEDSTARA8 NISYNC_VAL_PXIEDSTARA9\nNISYNC_VAL_PXIEDSTARA10 NISYNC_VAL_PXIEDSTARA11\nNISYNC_VAL_PXIEDSTARA12 NISYNC_VAL_PXIEDSTARA13\nNISYNC_VAL_PXIEDSTARA14 NISYNC_VAL_PXIEDSTARA15\nNISYNC_VAL_PXIEDSTARA16 NISYNC_VAL_ALL_CONNECTED (Default Value)\n',
                    'note': '\nEach PXIe_DStarA trigger is mapped to a single slot. This mapping\nis vendor specific. Your chassis documentation may describe this mapping\nin addition to the chassis.ini and pxisys.ini system description files\nthe PXI Specification requires.\n'
                },
                'name': 'destinationTerminal',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisconnectSwTrigFromTerminal': {
        'documentation': {
            'description': '\nThis function disconnects the global software trigger terminal from a\ndestination trigger terminal.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis input specifies the source software trigger terminal to disconnect\nfrom the destination terminal. The global software trigger must be\nconnected to the destination terminal for this operation to succeed.\nValid Values: NISYNC_VAL_SWTRIG_GLOBAL (Default Value)\n'
                },
                'name': 'sourceTerminal',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis input specifies the destination trigger terminal that the global\nsoftware trigger terminal will disconnect from. The global software\ntrigger must be connected to the destination terminal for this operation\nto succeed. Valid Values: NISYNC_VAL_PXITRIG0 NISYNC_VAL_PXITRIG1\nNISYNC_VAL_PXITRIG2 NISYNC_VAL_PXITRIG3 NISYNC_VAL_PXITRIG4\nNISYNC_VAL_PXITRIG5 NISYNC_VAL_PXITRIG6 NISYNC_VAL_PXITRIG7\nNISYNC_VAL_PXISTAR0 NISYNC_VAL_PXISTAR1 NISYNC_VAL_PXISTAR2\nNISYNC_VAL_PXISTAR3 NISYNC_VAL_PXISTAR4 NISYNC_VAL_PXISTAR5\nNISYNC_VAL_PXISTAR6 NISYNC_VAL_PXISTAR7 NISYNC_VAL_PXISTAR8\nNISYNC_VAL_PXISTAR9 NISYNC_VAL_PXISTAR10 NISYNC_VAL_PXISTAR11\nNISYNC_VAL_PXISTAR12 NISYNC_VAL_PXISTAR13 NISYNC_VAL_PXISTAR14\nNISYNC_VAL_PXISTAR15 NISYNC_VAL_PXISTAR16 NISYNC_VAL_PXISTAR\nNISYNC_VAL_PFI0 NISYNC_VAL_PFI1 NISYNC_VAL_PFI2 NISYNC_VAL_PFI3\nNISYNC_VAL_PFI4 NISYNC_VAL_PFI5 NISYNC_VAL_PFILVDS0\nNISYNC_VAL_PFILVDS1 NISYNC_VAL_PFILVDS2 NISYNC_VAL_PXIEDSTARB0\nNISYNC_VAL_PXIEDSTARB1 NISYNC_VAL_PXIEDSTARB2\nNISYNC_VAL_PXIEDSTARB3 NISYNC_VAL_PXIEDSTARB4\nNISYNC_VAL_PXIEDSTARB5 NISYNC_VAL_PXIEDSTARB6\nNISYNC_VAL_PXIEDSTARB7 NISYNC_VAL_PXIEDSTARB8\nNISYNC_VAL_PXIEDSTARB9 NISYNC_VAL_PXIEDSTARB10\nNISYNC_VAL_PXIEDSTARB11 NISYNC_VAL_PXIEDSTARB12\nNISYNC_VAL_PXIEDSTARB13 NISYNC_VAL_PXIEDSTARB14\nNISYNC_VAL_PXIEDSTARB15 NISYNC_VAL_PXIEDSTARB16\nNISYNC_VAL_PXIEDSTARC NISYNC_VAL_ALL_CONNECTED (Default Value)\n',
                    'note': '\nEach PXI_Star and PXIe_DStarB trigger is mapped to a single\nslot. This mapping is vendor specific. Your chassis documentation may\ndescribe this mapping in addition to the chassis.ini and pxisys.ini\nsystem description files the PXI Specification requires.\n'
                },
                'name': 'destinationTerminal',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisconnectTrigTerminals': {
        'documentation': {
            'description': '\nThis function disconnects a source trigger terminal from a destination\ntrigger terminal.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis input specifies the source trigger terminal to disconnect from the\ndestination terminal. The source and destination terminals must be\nconnected for this operation to succeed. Valid Values:\nNISYNC_VAL_PXITRIG0 NISYNC_VAL_PXITRIG1 NISYNC_VAL_PXITRIG2\nNISYNC_VAL_PXITRIG3 NISYNC_VAL_PXITRIG4 NISYNC_VAL_PXITRIG5\nNISYNC_VAL_PXITRIG6 NISYNC_VAL_PXITRIG7 NISYNC_VAL_PXISTAR0\nNISYNC_VAL_PXISTAR1 NISYNC_VAL_PXISTAR2 NISYNC_VAL_PXISTAR3\nNISYNC_VAL_PXISTAR4 NISYNC_VAL_PXISTAR5 NISYNC_VAL_PXISTAR6\nNISYNC_VAL_PXISTAR7 NISYNC_VAL_PXISTAR8 NISYNC_VAL_PXISTAR9\nNISYNC_VAL_PXISTAR10 NISYNC_VAL_PXISTAR11 NISYNC_VAL_PXISTAR12\nNISYNC_VAL_PXISTAR13 NISYNC_VAL_PXISTAR14 NISYNC_VAL_PXISTAR15\nNISYNC_VAL_PXISTAR16 NISYNC_VAL_PXISTAR NISYNC_VAL_PFI0\nNISYNC_VAL_PFI1 NISYNC_VAL_PFI2 NISYNC_VAL_PFI3 NISYNC_VAL_PFI4\nNISYNC_VAL_PFI5 NISYNC_VAL_PFILVDS0 NISYNC_VAL_PFILVDS1\nNISYNC_VAL_PFILVDS2 NISYNC_VAL_GND NISYNC_VAL_SYNC_CLK_FULLSPEED\nNISYNC_VAL_SYNC_CLK_DIV1 NISYNC_VAL_SYNC_CLK_DIV2\nNISYNC_VAL_CLKIN NISYNC_VAL_PXIEDSTARC0 NISYNC_VAL_PXIEDSTARC1\nNISYNC_VAL_PXIEDSTARC2 NISYNC_VAL_PXIEDSTARC3\nNISYNC_VAL_PXIEDSTARC4 NISYNC_VAL_PXIEDSTARC5\nNISYNC_VAL_PXIEDSTARC6 NISYNC_VAL_PXIEDSTARC7\nNISYNC_VAL_PXIEDSTARC8 NISYNC_VAL_PXIEDSTARC9\nNISYNC_VAL_PXIEDSTARC10 NISYNC_VAL_PXIEDSTARC11\nNISYNC_VAL_PXIEDSTARC12 NISYNC_VAL_PXIEDSTARC13\nNISYNC_VAL_PXIEDSTARC14 NISYNC_VAL_PXIEDSTARC15\nNISYNC_VAL_PXIEDSTARC16 NISYNC_VAL_PXIEDSTARB\nNISYNC_VAL_ALL_CONNECTED (Default Value)\n',
                    'note': '\nEach PXI_Star and\nPXIe_DStarC trigger is mapped to a single slot. This mapping is vendor\nspecific. Your chassis documentation may describe this mapping in\naddition to the chassis.ini and pxisys.ini system description files the\nPXI Specification requires.\n'
                },
                'name': 'sourceTerminal',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis input specifies the destination trigger terminal that the source\nterminal disconnect from. The source and destination terminals must be\nconnected for this operation to succeed. Valid Values:\nNISYNC_VAL_PXITRIG0 NISYNC_VAL_PXITRIG1 NISYNC_VAL_PXITRIG2\nNISYNC_VAL_PXITRIG3 NISYNC_VAL_PXITRIG4 NISYNC_VAL_PXITRIG5\nNISYNC_VAL_PXITRIG6 NISYNC_VAL_PXITRIG7 NISYNC_VAL_PXISTAR0\nNISYNC_VAL_PXISTAR1 NISYNC_VAL_PXISTAR2 NISYNC_VAL_PXISTAR3\nNISYNC_VAL_PXISTAR4 NISYNC_VAL_PXISTAR5 NISYNC_VAL_PXISTAR6\nNISYNC_VAL_PXISTAR7 NISYNC_VAL_PXISTAR8 NISYNC_VAL_PXISTAR9\nNISYNC_VAL_PXISTAR10 NISYNC_VAL_PXISTAR11 NISYNC_VAL_PXISTAR12\nNISYNC_VAL_PXISTAR13 NISYNC_VAL_PXISTAR14 NISYNC_VAL_PXISTAR15\nNISYNC_VAL_PXISTAR16 NISYNC_VAL_PXISTAR NISYNC_VAL_PFI0\nNISYNC_VAL_PFI1 NISYNC_VAL_PFI2 NISYNC_VAL_PFI3 NISYNC_VAL_PFI4\nNISYNC_VAL_PFI5 NISYNC_VAL_PFILVDS0 NISYNC_VAL_PFILVDS1\nNISYNC_VAL_PFILVDS2 NISYNC_VAL_PXIEDSTARB0 NISYNC_VAL_PXIEDSTARB1\nNISYNC_VAL_PXIEDSTARB2 NISYNC_VAL_PXIEDSTARB3\nNISYNC_VAL_PXIEDSTARB4 NISYNC_VAL_PXIEDSTARB5\nNISYNC_VAL_PXIEDSTARB6 NISYNC_VAL_PXIEDSTARB7\nNISYNC_VAL_PXIEDSTARB8 NISYNC_VAL_PXIEDSTARB9\nNISYNC_VAL_PXIEDSTARB10 NISYNC_VAL_PXIEDSTARB11\nNISYNC_VAL_PXIEDSTARB12 NISYNC_VAL_PXIEDSTARB13\nNISYNC_VAL_PXIEDSTARB14 NISYNC_VAL_PXIEDSTARB15\nNISYNC_VAL_PXIEDSTARB16 NISYNC_VAL_PXIEDSTARC\nNISYNC_VAL_ALL_CONNECTED (Default Value)\n',
                    'note': '\nEach PXI_Star and\nPXIe_DStarB trigger is mapped to a single slot. This mapping is vendor\nspecific. Your chassis documentation may describe this mapping in\naddition to the chassis.ini and pxisys.ini system description files the\nPXI Specification requires.\n'
                },
                'name': 'destinationTerminal',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'EnableGpsTimestamping': {
        'documentation': {
            'description': '\nThis function enables timestamping of the GPS pulse per second\nsynchronized to the board time associated with the specified instrument\nhandle.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'EnableIrigTimestamping': {
        'documentation': {
            'description': '\nThis function enables timestamping IRIG decodes synchronized to the\nboard time associated with the specified instrument handle. The terminal\nassociated with this timestamp cannot be used for other operations until\ntimestamping is disabled with niSync_DisableIRIGTimestamping or the\nsession is closed with niSync_close.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nAn input integer enumeration of the IRIG input being supplied. Valid\nValues: NISYNC_VAL_IRIG_TYPE_IRIGB_DC\nNISYNC_VAL_IRIG_TYPE_IRIGB_AM (Default)\n'
                },
                'name': 'irigType',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nAn input string that specifies the terminal to which the IRIG input is\nconnected.\n'
                },
                'name': 'terminalName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'EnableTimeStampTrigger': {
        'documentation': {
            'description': '\nThis function enables time stamping of a specified trigger synchronized\nto the board time associated with the specified session handle. The\nterminal associated with this time stamp trigger cannot be used for\nother operations until the time stamp trigger is disabled with the\nniSync_DisableTimeStampTrigger function or the session is closed with\nthe niSync_Close function.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nAn input string enumeration that specifies the terminal containing the\ndigital signal that is the trigger to start time stamping. Valid Values:\nNISYNC_VAL_PFI0 NISYNC_VAL_PFI1 NISYNC_VAL_PFI2\nNISYNC_VAL_PXITRIG0 NISYNC_VAL_PXITRIG1 NISYNC_VAL_PXITRIG2\nNISYNC_VAL_PXITRIG3 NISYNC_VAL_PXITRIG4 NISYNC_VAL_PXITRIG5\nNISYNC_VAL_PXITRIG6 NISYNC_VAL_PXITRIG7 NISYNC_VAL_PXISTAR0\nNISYNC_VAL_PXISTAR1 NISYNC_VAL_PXISTAR2 NISYNC_VAL_PXISTAR3\nNISYNC_VAL_PXISTAR4 NISYNC_VAL_PXISTAR5 NISYNC_VAL_PXISTAR6\nNISYNC_VAL_PXISTAR7 NISYNC_VAL_PXISTAR8 NISYNC_VAL_PXISTAR9\nNISYNC_VAL_PXISTAR10 NISYNC_VAL_PXISTAR11 NISYNC_VAL_PXISTAR12\n'
                },
                'name': 'terminal',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nAn input integer enumeration that specifies the trigger conditions.\nValid Values: NISYNC_VAL_EDGE_RISING NISYNC_VAL_EDGE_FALLING\nNISYNC_VAL_EDGE_ANY\n'
                },
                'name': 'activeEdge',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'EnableTimeStampTriggerWithDecimation': {
        'documentation': {
            'description': '\nThis function enables time stamping of a specified trigger synchronized\nto the board time associated with the specified session handle. The\nterminal associated with this time stamp trigger cannot be used for\nother operations until the time stamp trigger is disabled with the\nniSync_DisableTimeStampTrigger function or the session is closed with\nthe niSync_Close function.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nAn input string enumeration that specifies the terminal containing the\ndigital signal that is the trigger to start time stamping. Valid Values:\nNISYNC_VAL_PFI0 NISYNC_VAL_PFI1 NISYNC_VAL_PFI2\nNISYNC_VAL_PXITRIG0 NISYNC_VAL_PXITRIG1 NISYNC_VAL_PXITRIG2\nNISYNC_VAL_PXITRIG3 NISYNC_VAL_PXITRIG4 NISYNC_VAL_PXITRIG5\nNISYNC_VAL_PXITRIG6 NISYNC_VAL_PXITRIG7 NISYNC_VAL_PXISTAR0\nNISYNC_VAL_PXISTAR1 NISYNC_VAL_PXISTAR2 NISYNC_VAL_PXISTAR3\nNISYNC_VAL_PXISTAR4 NISYNC_VAL_PXISTAR5 NISYNC_VAL_PXISTAR6\nNISYNC_VAL_PXISTAR7 NISYNC_VAL_PXISTAR8 NISYNC_VAL_PXISTAR9\nNISYNC_VAL_PXISTAR10 NISYNC_VAL_PXISTAR11 NISYNC_VAL_PXISTAR12\n'
                },
                'name': 'terminal',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nAn input integer enumeration that specifies the trigger conditions.\nValid Values: NISYNC_VAL_EDGE_RISING NISYNC_VAL_EDGE_FALLING\nNISYNC_VAL_EDGE_ANY\n'
                },
                'name': 'activeEdge',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nAn input specifying how frequently to timestamp incoming trigger events.\nFor example, if you pass in a value of 4, every fourth event is\ntimestamped. The default is 1. This value must be greater than or equal\nto 1.\n'
                },
                'name': 'decimationCount',
                'type': 'ViUInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'Get1588Time': {
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
                'name': 'timeSeconds',
                'type': 'ViUInt32'
            },
            {
                'direction': 'out',
                'name': 'timeNanoseconds',
                'type': 'ViUInt32'
            },
            {
                'direction': 'out',
                'name': 'timeFractionalNanoseconds',
                'type': 'ViUInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViBoolean': {
        'documentation': {
            'description': 'This function sets the value of a ViBoolean attribute.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSince NI-Sync does not include any channel-based attributes, this\nparameter is ignored. Default Value: ""\n'
                },
                'name': 'activeItem',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'This parameter specifies the ID of the attribute you wish to get.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nPass the value to which you want to set the attribute. From the function\npanel window, you can use this control as follows. - If the attribute\ncurrently showing in the Attribute ID ring control has constants as\nvalid values, you can view a list of the constants by pressing on this\ncontrol. Select a value by double-clicking on it or by selecting it and\nthen pressing .\n',
                    'note': '\nSome of the values might not be valid depending on\nthe current settings of the instrument session. Default Value: none\n'
                },
                'name': 'attributeValue',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViInt32': {
        'documentation': {
            'description': 'This function queries the value of a ViInt32 attribute.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSince NI-Sync does not include any channel-based attributes, this\nparameter is ignored. Default Value: ""\n'
                },
                'name': 'activeItem',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'This parameter specifies the ID of the attribute you wish to get.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the current value of the attribute. Pass the address of a\nViInt32 variable. From the function panel window, you can use this\ncontrol as follows. - If the attribute currently showing in the\nAttribute ID ring control has named constants as valid values, you can\nview a list of the constants by pressing on this control. Select a value\nby double-clicking on it or by selecting it and then pressing .\n'
                },
                'name': 'attributeValue',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViReal64': {
        'documentation': {
            'description': 'This function queries the value of a ViReal64 attribute.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSince NI-Sync does not include any channel-based attributes, this\nparameter is ignored. Default Value: ""\n'
                },
                'name': 'activeItem',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'This parameter specifies the ID of the attribute you wish to get.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the current value of the attribute. Pass the address of a\nViReal64 variable. From the function panel window, you can use this\ncontrol as follows. - If the attribute currently showing in the\nAttribute ID ring control has named constants as valid values, you can\nview a list of the constants by pressing on this control. Select a value\nby double-clicking on it or by selecting it and then pressing .\n'
                },
                'name': 'attributeValue',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViString': {
        'documentation': {
            'description': '\nThis function queries the value of a ViString attribute. You can use\nthis function to get the values of instrument- specific attributes and\ninherent IVI attributes. If the attribute represents an instrument\nstate, this function performs instrument I/O in the following cases: -\nState caching is disabled for the entire session or for the particular\nattribute. - State caching is enabled and the currently cached value is\ninvalid. You must provide a ViChar array to serve as a buffer for the\nvalue. You pass the number of bytes in the buffer as the Buffer Size\nparameter. If the current value of the attribute, including the\nterminating NUL byte, is larger than the size you indicate in the Buffer\nSize parameter, the function copies Buffer Size - 1 bytes into the\nbuffer, places an ASCII NUL byte at the end of the buffer, and returns\nthe buffer size you must pass to get the entire value. For example, if\nthe value is "123456" and the Buffer Size is 4, the function places\n"123" into the buffer and returns 7. If you want to call this function\njust to get the required buffer size, you can pass 0 for the Buffer Size\nand VI_NULL for the Attribute Value buffer. If you want the function to\nfill in the buffer regardless of the number of bytes in the value, pass\na negative number for the Buffer Size parameter.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSince NI-Sync does not include any channel-based attributes, this\nparameter is ignored. Default Value: ""\n'
                },
                'name': 'activeItem',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'This parameter specifies the ID of the attribute you wish to get.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the number of bytes in the ViChar array you specify for the\nAttribute Value parameter. If the current value of the attribute,\nincluding the terminating NUL byte, contains more bytes that you\nindicate in this parameter, the function copies Buffer Size - 1 bytes\ninto the buffer, places an ASCII NUL byte at the end of the buffer, and\nreturns the buffer size you must pass to get the entire value. For\nexample, if the value is "123456" and the Buffer Size is 4, the function\nplaces "123" into the buffer and returns 7. If you pass a negative\nnumber, the function copies the value to the buffer regardless of the\nnumber of bytes in the value. If you pass 0, you can pass VI_NULL for\nthe Attribute Value buffer parameter. Default Value: 256\n'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe buffer in which the function returns the current value of the\nattribute. The buffer must be of type ViChar and have at least as many\nbytes as indicated in the Buffer Size parameter. If the current value of\nthe attribute, including the terminating NUL byte, contains more bytes\nthat you indicate in this parameter, the function copies Buffer Size - 1\nbytes into the buffer, places an ASCII NUL byte at the end of the\nbuffer, and returns the buffer size you must pass to get the entire\nvalue. For example, if the value is "123456" and the Buffer Size is 4,\nthe function places "123" into the buffer and returns 7. If you specify\n0 for the Buffer Size parameter, you can pass VI_NULL for this\nparameter. From the function panel window, you can use this control as\nfollows. - If the attribute currently showing in the Attribute ID ring\ncontrol has named constants as valid values, you can view a list of the\nconstants by pressing on this control. Select a value by double-clicking\non it or by selecting it and then pressing .\n'
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
    'GetClkTerminalConnectionInfo': {
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
                'name': 'destTerminal',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'srcTerminal',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViString[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetExtCalLastDateAndTime': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nThis function returns the last external calibration date and time, in\nGreenwich Mean Time (GMT), for the module. Note: A calibration password\nis not required to use this function. It can be invoked with an\ninstrument handle created with either niSync_init or\nniSync_InitExtCal.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis parameter specifies the session handle that you obtain from\nniSync_init or niSync_InitExtCal. The handle identifies a particular\ninstrument session. Default Value: None\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': "\nThis parameter returns the year of the module's last external\ncalibration.\n"
                },
                'name': 'year',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': "\nThis parameter returns the month of the module's last external\ncalibration. Valid Values: 0 - January 1 - February ... 12 - December\n"
                },
                'name': 'month',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': "\nThis parameter returns the day of the module's last external\ncalibration. Valid Values: days of the month, in the range 1 .. 31\n"
                },
                'name': 'day',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': "\nThis parameter returns the hour of the module's last external\ncalibration. Valid Values: hours, in the range 0 .. 23\n"
                },
                'name': 'hour',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': "\nThis parameter returns the minute of the module's last external\ncalibration. Valid Values: minutes, in the range 0 .. 59\n"
                },
                'name': 'minute',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetExtCalLastTemp': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nThis function returns the last external calibration temperature, in\ndegrees celcius, for the module. Note: A calibration password is not\nrequired to use this function. It can be invoked with an instrument\nhandle created with either niSync_init or niSync_InitExtCal.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis parameter specifies the session handle that you obtain from\nniSync_init or niSync_InitExtCal. The handle identifies a particular\ninstrument session. Default Value: None\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': "\nThis parameter returns the temperature, in degrees celcius, of the\nmodule's last external calibration.\n"
                },
                'name': 'temperature',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetExtCalRecommendedInterval': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nThis function returns the recommended external calibration interval, in\nunits of months, for the module. Note: A calibration password is not\nrequired to use this function. It can be invoked with an instrument\nhandle created with either niSync_init or niSync_InitExtCal.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis parameter specifies the session handle that you obtain from\nniSync_init or niSync_InitExtCal. The handle identifies a particular\ninstrument session. Default Value: None\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThis parameter returns the external calibration interval, in units of\nmonths, for the module.\n'
                },
                'name': 'months',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetLocation': {
        'documentation': {
            'description': '\nThis function returns the last calculated location of the onboard GPS\nreceiver. The function returns latitude and longitude in degrees and\naltitude in meters. An external GPS antenna must be connected to receive\nvalid data from this function. For best results, allow the GPS receiver\nto complete a self survey before reading location.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nAn input double pointer. The caller of this function must allocate a\nViReal64 and pass the pointer in this argument. The function sets the\nViReal64 value to the latitude reported by the onboard GPS receiver.\nNegative values represent southern latitude. Positive values represent\nnorthern latitude.\n'
                },
                'name': 'latitude',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nAn input double pointer. The caller of this function must allocate a\nViReal64 and pass the pointer in this argument. The function sets the\nViReal64 value to the longitude reported by the onboard GPS receiver.\nNegative values represent western longitude. Positive values represent\neastern longitude.\n'
                },
                'name': 'longitude',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nAn input double pointer. The caller of this function must allocate a\nViReal64 and pass the pointer in this argument. The function sets the\nViReal64 value to the altitude reported by the onboard GPS receiver.\nReturns current altitude in meters (WGS-84 earth ellipsoid).\n'
                },
                'name': 'altitude',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetSwTrigConnectionInfo': {
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
                'name': 'destTerminal',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'srcTerminal',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViString[]'
            },
            {
                'direction': 'in',
                'name': 'syncClk',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViString[]'
            },
            {
                'direction': 'out',
                'name': 'invert',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'updateEdge',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'delay',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetTime': {
        'documentation': {
            'description': '\nThis function gets the board time associated with the specified session\nhandle. Note: NI-Sync supports only the time range between 1 January\n1970 and 1 January 2100. Therefore, if the supported time range has\nended, an error is returned. Note: The NI-Sync family of devices uses\nthe TAI timescale\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'An output integer that specifies a portion of the board time.'
                },
                'name': 'timeSeconds',
                'type': 'ViUInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'An output integer that specifies a portion of the board time.'
                },
                'name': 'timeNanoseconds',
                'type': 'ViUInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'An output integer that specifies a portion of the board time.'
                },
                'name': 'timeFractionalNanoseconds',
                'type': 'ViUInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetTimeReferenceNames': {
        'documentation': {
            'description': 'TBD'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nAn integer that specifies the seconds portion of the time to which the\nboard time will be set. Note that NI-Sync supports setting the initial\ntime between 0 hours on 1 January 1970 and 0 hours on 1 January 2100.\nThis parameter is ignored unless the timeSource parameter is set to\nNISYNC_VAL_INIT_TIME_SRC_MANUAL.\n'
                },
                'name': 'bufferSize',
                'type': 'ViUInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe buffer in which the function returns the current value of the\nattribute. The buffer must be of type ViChar and have at least as many\nbytes as indicated in the Buffer Size parameter. If the current value of\nthe attribute, including the terminating NUL byte, contains more bytes\nthat you indicate in this parameter, the function copies Buffer Size - 1\nbytes into the buffer, places an ASCII NUL byte at the end of the\nbuffer, and returns the buffer size you must pass to get the entire\nvalue. For example, if the value is "123456" and the Buffer Size is 4,\nthe function places "123" into the buffer and returns 7. If you specify\n0 for the Buffer Size parameter, you can pass VI_NULL for this\nparameter. From the function panel window, you can use this control as\nfollows. - If the attribute currently showing in the Attribute ID ring\ncontrol has named constants as valid values, you can view a list of the\nconstants by pressing on this control. Select a value by double-clicking\non it or by selecting it and then pressing .\n'
                },
                'name': 'timeReferenceNames',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetTrigTerminalConnectionInfo': {
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
                'name': 'destTerminal',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'srcTerminal',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViString[]'
            },
            {
                'direction': 'in',
                'name': 'syncClock',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViString[]'
            },
            {
                'direction': 'out',
                'name': 'invert',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'updateEdge',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetVelocity': {
        'documentation': {
            'description': '\nThis function returns the last calculated velocity of the onboard GPS\nreceiver. The function returns east velocity, north velocity, and up\nvelocity in meters per second. An external GPS antenna must be connected\nto receive valid data from this function, and the GPS receiver must be\nconfigured for Mobile Mode to receive nonzero velocity values.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nAn input double pointer. The caller of this function must allocate a\nViReal64 and pass the pointer in this argument. The function sets the\nViReal64 value to the eastVelocity reported by the onboard GPS receiver.\nNegative values represent west velocity. Positive values represent east\nvelocity.\n'
                },
                'name': 'eastVelocity',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nAn input double pointer. The caller of this function must allocate a\nViReal64 and pass the pointer in this argument. The function sets the\nViReal64 value to the northVelocity reported by the onboard GPS\nreceiver. Negative values represent south velocity. Positive values\nrepresent north velocity.\n'
                },
                'name': 'northVelocity',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nAn input double pointer. The caller of this function must allocate a\nViReal64 and pass the pointer in this argument. The function sets the\nViReal64 value to the upVelocity reported by the onboard GPS receiver.\nNegative values represent down velocity. Positive values represent up\nvelocity.\n'
                },
                'name': 'upVelocity',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'InitExtCal': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nThis function initializes an external calibration session to a module.\nThe function returns an instrument driver session that can be used to\nadjust calibration constants for the module. You must supply the\nexternal calibration password for the operation to succeed. The external\ncalibration session must be closed using niSync_CloseExtCal.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nResource name of the module to initialize. Syntax: Optional fields are\nshown in square brackets ([]). Configured in MAX Under Valid Syntax PXI\nSystem PXI[bus number]::device number\n',
                    'note': '\nVISA aliases are also valid\nfor the resource name. Example resource names: Resource Name Description\nPXI16::15::INSTR PXI bus 16, device number 15 PXI::15::INSTR PXI bus 0,\ndevice number 15 PXI4::9::INSTR PXI bus 4, device number 9 Default\nValue: ""\n'
                },
                'name': 'resourceName',
                'type': 'ViRsrc'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis input specifies the external calibration password for the module.\nThe password must exactly match the value stored in the calibration ROM\nof the module for the operation to succeed.\n',
                    'note': '\nThe external\ncalibration password can be changed using the\nniSync_ChangeExtCalpassword function. Default Value: ""\n'
                },
                'name': 'password',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns a ViSession handle that you use to identify the instrument in\nall subsequent instrument driver function calls. Notes: Although you can\ncreate more than one NI-Sync session for the same resource, it is best\nnot to do so. A better approach is to use the same NI-Sync session in\nmultiple execution threads. You can use VISA functions viLock and\nviUnlock to protect sections of code that require exclusive access to\nthe resource.\n'
                },
                'name': 'calibrationInstrumentHandle',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'MeasureFrequency': {
        'documentation': {
            'description': '\nThis function measures the frequency of the signal at the specified\nterminal for a specified duration. The function returns the frequency,\nthe calculated error, and the actual duration of the frequency\nmeasurement.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis input specifies the source terminal of the signal to measure. Valid\nValues: NISYNC_VAL_PFI0 (Default Value) NISYNC_VAL_PFI1\nNISYNC_VAL_PFI2 NISYNC_VAL_PFI3 NISYNC_VAL_PFI4 NISYNC_VAL_PFI5\nNISYNC_VAL_PFILVDS0 NISYNC_VAL_PFILVDS1 NISYNC_VAL_PFILVDS2\nNISYNC_VAL_PXITRIG0 NISYNC_VAL_PXITRIG1 NISYNC_VAL_PXITRIG2\nNISYNC_VAL_PXITRIG3 NISYNC_VAL_PXITRIG4 NISYNC_VAL_PXITRIG5\nNISYNC_VAL_PXITRIG6 NISYNC_VAL_PXITRIG7 NISYNC_VAL_PXISTAR0\nNISYNC_VAL_PXISTAR1 NISYNC_VAL_PXISTAR2 NISYNC_VAL_PXISTAR3\nNISYNC_VAL_PXISTAR4 NISYNC_VAL_PXISTAR5 NISYNC_VAL_PXISTAR6\nNISYNC_VAL_PXISTAR7 NISYNC_VAL_PXISTAR8 NISYNC_VAL_PXISTAR9\nNISYNC_VAL_PXISTAR10 NISYNC_VAL_PXISTAR11 NISYNC_VAL_PXISTAR12\nNISYNC_VAL_PXISTAR13 NISYNC_VAL_PXISTAR14 NISYNC_VAL_PXISTAR15\nNISYNC_VAL_PXISTAR16 NISYNC_VAL_PXISTAR NISYNC_VAL_PXIEDSTARC0\nNISYNC_VAL_PXIEDSTARC1 NISYNC_VAL_PXIEDSTARC2\nNISYNC_VAL_PXIEDSTARC3 NISYNC_VAL_PXIEDSTARC4\nNISYNC_VAL_PXIEDSTARC5 NISYNC_VAL_PXIEDSTARC6\nNISYNC_VAL_PXIEDSTARC7 NISYNC_VAL_PXIEDSTARC8\nNISYNC_VAL_PXIEDSTARC9 NISYNC_VAL_PXIEDSTARC10\nNISYNC_VAL_PXIEDSTARC11 NISYNC_VAL_PXIEDSTARC12\nNISYNC_VAL_PXIEDSTARC13 NISYNC_VAL_PXIEDSTARC14\nNISYNC_VAL_PXIEDSTARC15 NISYNC_VAL_PXIEDSTARC16\nNISYNC_VAL_PXIEDSTARB NISYNC_VAL_OSCILLATOR NISYNC_VAL_CLKIN\n'
                },
                'name': 'sourceTerminal',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis input specifies the duration of the frequency measurement, in units\nof seconds. The duration should be a multiple of the PXI_Clk10 signal\nperiod, i.e. it should be specified in multiples of 100 ns. If the\nduration is not a multiple of the PXI_Clk10 period, it will be coerced\nto the closest multiple. Default Value: 0.00000100 seconds\n'
                },
                'name': 'duration',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThis parameter returns the actual duration, in units of seconds, used in\nthe frequency measurement. The measurement duration will be a multiple\nof the PXI_Clk10 period, i.e. it is a multiple of 100ns.\n'
                },
                'name': 'actualDuration',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThis parameter returns the frequency measured at the PFI0 terminal, in\nunits of Hz. The measurable frequency range is approximately 0.1 Hz to\n105 MHz.\n'
                },
                'name': 'measuredFrequency',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThis parameter returns the error calculated for the frequency\nmeasurement. The formula used to calculate the error is: Measurement\nError = 1 / (Actual Duration) where "Actual Duration" is the value\nreturned in the Actual Duration parameter, i.e. the actual duration of\nthe measurement.\n'
                },
                'name': 'frequencyError',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'MeasureFrequencyEx': {
        'documentation': {
            'description': '\nThis function measures the frequency of the signal at the specified\nterminal for a specified duration. The function returns the frequency,\nthe calculated error, and the actual duration of the frequency\nmeasurement.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis input specifies the source terminal of the signal to measure. Valid\nValues: NISYNC_VAL_PFI0 (Default Value) NISYNC_VAL_PFI1\nNISYNC_VAL_PFI2 NISYNC_VAL_PFI3 NISYNC_VAL_PFI4 NISYNC_VAL_PFI5\nNISYNC_VAL_PFILVDS0 NISYNC_VAL_PFILVDS1 NISYNC_VAL_PFILVDS2\nNISYNC_VAL_PXITRIG0 NISYNC_VAL_PXITRIG1 NISYNC_VAL_PXITRIG2\nNISYNC_VAL_PXITRIG3 NISYNC_VAL_PXITRIG4 NISYNC_VAL_PXITRIG5\nNISYNC_VAL_PXITRIG6 NISYNC_VAL_PXITRIG7 NISYNC_VAL_PXISTAR0\nNISYNC_VAL_PXISTAR1 NISYNC_VAL_PXISTAR2 NISYNC_VAL_PXISTAR3\nNISYNC_VAL_PXISTAR4 NISYNC_VAL_PXISTAR5 NISYNC_VAL_PXISTAR6\nNISYNC_VAL_PXISTAR7 NISYNC_VAL_PXISTAR8 NISYNC_VAL_PXISTAR9\nNISYNC_VAL_PXISTAR10 NISYNC_VAL_PXISTAR11 NISYNC_VAL_PXISTAR12\nNISYNC_VAL_PXISTAR13 NISYNC_VAL_PXISTAR14 NISYNC_VAL_PXISTAR15\nNISYNC_VAL_PXISTAR16 NISYNC_VAL_PXISTAR NISYNC_VAL_PXIEDSTARC0\nNISYNC_VAL_PXIEDSTARC1 NISYNC_VAL_PXIEDSTARC2\nNISYNC_VAL_PXIEDSTARC3 NISYNC_VAL_PXIEDSTARC4\nNISYNC_VAL_PXIEDSTARC5 NISYNC_VAL_PXIEDSTARC6\nNISYNC_VAL_PXIEDSTARC7 NISYNC_VAL_PXIEDSTARC8\nNISYNC_VAL_PXIEDSTARC9 NISYNC_VAL_PXIEDSTARC10\nNISYNC_VAL_PXIEDSTARC11 NISYNC_VAL_PXIEDSTARC12\nNISYNC_VAL_PXIEDSTARC13 NISYNC_VAL_PXIEDSTARC14\nNISYNC_VAL_PXIEDSTARC15 NISYNC_VAL_PXIEDSTARC16\nNISYNC_VAL_PXIEDSTARB NISYNC_VAL_OSCILLATOR NISYNC_VAL_CLKIN\n'
                },
                'name': 'sourceTerminal',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis input specifies the duration of the frequency measurement, in units\nof seconds. The duration should be a multiple of the PXI_Clk10 signal\nperiod, i.e. it should be specified in multiples of 100 ns. If the\nduration is not a multiple of the PXI_Clk10 period, it will be coerced\nto the closest multiple. Default Value: 0.00000100 seconds\n'
                },
                'name': 'duration',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'decimationCount',
                'type': 'ViUInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThis parameter returns the actual duration, in units of seconds, used in\nthe frequency measurement. The measurement duration will be a multiple\nof the PXI_Clk10 period, i.e. it is a multiple of 100ns.\n'
                },
                'name': 'actualDuration',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThis parameter returns the frequency measured at the PFI0 terminal, in\nunits of Hz. The measurable frequency range is approximately 0.1 Hz to\n105 MHz.\n'
                },
                'name': 'measuredFrequency',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThis parameter returns the error calculated for the frequency\nmeasurement. The formula used to calculate the error is: Measurement\nError = 1 / (Actual Duration) where "Actual Duration" is the value\nreturned in the Actual Duration parameter, i.e. the actual duration of\nthe measurement.\n'
                },
                'name': 'frequencyError',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'PersistConfig': {
        'documentation': {
            'description': '\nThis function will copy the sync configuration from volatile storage to\npermanent storage.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadCurrentTemperature': {
        'documentation': {
            'description': '\nThis function reads the current module temperature, in degrees celcius.\nNote: A calibration password is not required to use this function. It\ncan be invoked with an instrument handle created with either\nniSync_init or niSync_InitExtCal.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis parameter specifies the session handle that you obtain from\nniSync_init or niSync_InitExtCal. The handle identifies a particular\ninstrument session. Default Value: None\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThis parameter returns the temperature, in degrees celcius, of the\ntiming and synchronization module.\n'
                },
                'name': 'temperature',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadLastGpsTimestamp': {
        'documentation': {
            'description': '\nThis function returns the last timestamp received of the GPS pulse per\nsecond. The read operation is a single-timestamp, nonblocking read. That\nis, the newest timestamp is returned. If no valid timestamp has ever\nbeen received, a value of zero is returned for the timestamp and the\ndecoded time. A single timestamp can be read multiple times; only the\nreception of a subsequent timestamp updates the values returned. The\nfunction does not block waiting for a new timestamp to become available.\nPrior to calling niSync_ReadLastGPSTimestamp, it is expected that\ntimestamping has been enabled by calling niSync_EnableGPSTimestamping.\nNote: The NI-Sync family of devices uses the TAI timescale. Note: You\ncan combine the values returned in timestampSeconds,\ntimestampNanoseconds, and timestampFractionalNanoseconds to get the\nboard time the GPS pulse per second was received. You can combine the\nvalues returned in gpsSeconds, gpsNanoseconds, and\ngpsFractionalNanoseconds to get the time reported by the onboard GPS\nreceiver.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nAn input integer pointer. The caller of this function must allocate a\nViUInt32 and pass the pointer in this argument. The function sets the\nViUInt32 value to the seconds field of when the timestamp occurred.\n'
                },
                'name': 'timeSeconds',
                'type': 'ViUInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nAn input integer pointer. The caller of this function must allocate a\nViUInt32 and pass the pointer in this argument. The function sets the\nViUInt32 value to the nanoseconds field of when the timestamp occurred.\n'
                },
                'name': 'timeNanoseconds',
                'type': 'ViUInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nAn input integer pointer. The caller of this function must allocate a\nViUInt16 and pass the pointer in this argument. The function sets the\nViUInt16 value to the fractional nanoseconds field of when the timestamp\noccurred.\n'
                },
                'name': 'timeFractionalNanoseconds',
                'type': 'ViUInt16'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nAn input integer pointer. The caller of this function must allocate a\nViUInt32 and pass the pointer in this argument. The function sets the\nViUInt32 value to the seconds field of time reported by the onboard GPS\nreceiver.\n'
                },
                'name': 'gpsSeconds',
                'type': 'ViUInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nAn input integer pointer. The caller of this function must allocate a\nViUInt32 and pass the pointer in this argument. The function sets the\nViUInt32 value to the nanoseconds field of the time reported by the\nonboard GPS receiver.\n'
                },
                'name': 'gpsNanoseconds',
                'type': 'ViUInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nAn input integer pointer. The caller of this function must allocate a\nViUInt16 and pass the pointer in this argument. The function sets the\nViUInt16 value to the fractional nanoseconds field of the time reported\nby the onboard GPS receiver.\n'
                },
                'name': 'gpsFractionalNanoseconds',
                'type': 'ViUInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadLastIrigTimestamp': {
        'documentation': {
            'description': '\nThis function returns the last IRIG timestamp received. The read\noperation is a single-timestamp, nonblocking read. That is, the newest\ntimestamp is returned. If no valid timestamp has ever been received, a\nvalue of zero is returned for the timestamp and the decoded time. A\nsingle timestamp can be read multiple times; only the reception of a\nsubsequent timestamp will update the values returned. The function does\nnot block waiting for a new timestamp to become available. Prior to\ncalling niSync_ReadLastIRIGTimestamp, it is expected that timestamping\nhas been enabled by calling niSync_EnableIRIGTimestamping. Note: The\nNI-Sync family of devices uses the TAI timescale. Note: You can combine\nthe values returned in timestampSeconds, timestampNanoseconds, and\ntimestampFractionalNanoseconds to get the board time the IRIG message\nwas received. You can combine the values returned in irigbSeconds,\nirigbNanoseconds, and irigbFractionalNanoseconds to get the time\nreported in the IRIG message.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nAn input integer pointer. The caller of this function must allocate a\nViUInt32 and pass the pointer in this argument. The function sets the\nViUInt32 value to the seconds field of when the timestamp occurred.\n'
                },
                'name': 'timeSeconds',
                'type': 'ViUInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nAn input integer pointer. The caller of this function must allocate a\nViUInt32 and pass the pointer in this argument. The function sets the\nViUInt32 value to the nanoseconds field of when the timestamp occurred.\n'
                },
                'name': 'timeNanoseconds',
                'type': 'ViUInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nAn input integer pointer. The caller of this function must allocate a\nViUInt16 and pass the pointer in this argument. The function sets the\nViUInt16 value to the fractional nanoseconds field of when the timestamp\noccurred.\n'
                },
                'name': 'timeFractionalNanoseconds',
                'type': 'ViUInt16'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nAn input integer pointer. The caller of this function must allocate a\nViUInt32 and pass the pointer in this argument. The function sets the\nViUInt32 value to the seconds field of time reported in the IRIG\nmessage.\n'
                },
                'name': 'irigSeconds',
                'type': 'ViUInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nAn input integer pointer. The caller of this function must allocate a\nViUInt32 and pass the pointer in this argument. The function sets the\nViUInt32 value to the nanoseconds field of the time reported in the IRIG\nmessage.\n'
                },
                'name': 'irigNanoseconds',
                'type': 'ViUInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nAn input integer pointer. The caller of this function must allocate a\nViUInt16 and pass the pointer in this argument. The function sets the\nViUInt16 value to the fractional nanoseconds field of the time reported\nin the IRIG message.\n'
                },
                'name': 'irigFractionalNanoseconds',
                'type': 'ViUInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadMultipleTriggerTimeStamp': {
        'documentation': {
            'description': '\nThis function reads trigger time stamps from the internal software\nbuffer for the specified terminal. The read operation is a destructive,\nblocking read. That is, the oldest unread time stamp associated with the\nspecified terminal is returned. When a time stamp is read, it is removed\nfrom the buffer. The function does not return until the time stamps\nrequested are available to be read, or the specified timeout elapses. If\nthe internal software buffer associated with the specified terminal is\nfull, time stamp operations for that terminal are suspended. Also, an\nerror specifying that the internal software buffer overflowed is\nreturned when the niSync_ReadMultipleTriggertimestamp function is\ninvoked. If the hardware time stamp buffer is full, all trigger time\nstamp operations are suspended. Also, an error specifying that the\nhardware time stamp buffer overflowed is returned when the\nniSync_ReadMultipleTriggertimestamp function is invoked. That is, the\nniSync_ReadMultipleTriggertimestamp function continues to return\npreviously generated time stamps, despite the overflow condition, until\nno time stamps are available. To clear this error condition, the\nniSync_DisabletimestampTrigger function must be invoked. Note that\nNI-Sync supports only the time range between 1 January 1970 and 1\nJanuary 2100. Therefore, if the supported time range ends before a time\nstamp is captured, an error is returned. Note: If timestampsToRead is\nnot equal to timestampsRead, the data held in the output arrays from\nindex timestampsRead to the end of the arrays is uninitialized, and\nshould be considered invalid.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nAn input string that specifies the terminal containing the digital\nsignal that is the trigger whose oldest unread time stamp will be read.\n'
                },
                'name': 'terminal',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nAn input integer specifying the number of time stamps to read. If the\nnumber of time stamps is not available before the timeout elapses, the\nnumber read before the timeout occurred is returned.\n'
                },
                'name': 'timeStampsToRead',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nAn input floating-point number that specifies the number of seconds to\nwait for a time stamp to be generated before returning a timeout error.\n'
                },
                'name': 'timeout',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nAn input pointer to an array of ViUInt32 values. The caller of this\nfunction must allocate an array of ViUInt32s of size timestampsToRead\nand pass the pointer to the array in this argument. The function sets\nthe values of the ViUInt32s to the seconds field of when the time stamp\noccurred. After the function returns, index 0 holds the earliest\noccurring seconds value, and the value returned in timestampsRead, minus\none, is the index in which the latest occurring seconds value is stored.\n'
                },
                'name': 'timeSeconds',
                'type': 'ViUInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nAn input pointer to an array of ViUInt32 values. The caller of this\nfunction must allocate an array of ViUInt32s of size timestampsToRead\nand pass the pointer to the array in this argument. The function sets\nthe values of the ViUInt32s to the nanoseconds field of when the time\nstamp occurred. After the function returns, index 0 holds the earliest\noccurring nanoseconds value, and the value returned in timestampsRead,\nminus one, is the index in which the latest occurring nanoseconds value\nis stored.\n'
                },
                'name': 'timeNanoseconds',
                'type': 'ViUInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nAn input pointer to an array of ViUInt16 values. The caller of this\nfunction must allocate an array of ViUInt16s of size timestampsToRead\nand pass the pointer to the array in this argument. The function sets\nthe values of the ViUInt16s to the fractional nanoseconds field of when\nthe time stamp occurred. After the function returns, index 0 holds the\nearliest occurring fractional nanoseconds value, and the value returned\nin timestampsRead, minus one, is the index in which the latest occurring\nfractional nanoseconds value is stored.\n'
                },
                'name': 'timeFractionalNanoseconds',
                'type': 'ViUInt16'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nAn input pointer to an array of ViInt32s. The caller of this function\nmust allocate an array of ViUInt32s of size timestampsToRead and pass\nthe pointer to the array in this argument. After the function returns,\nindex 0 holds the earliest occurring detectedEdge value, and the value\nreturned in timestampsRead, minus one, is the index in which the latest\noccurring detectedEdge value is stored. Each detectedEdge is an integer\nenumeration that specifies the detected trigger condition. Valid Values:\nNISYNC_VAL_EDGE_RISING NISYNC_VAL_EDGE_FALLING\n'
                },
                'name': 'detectedEdgeBuffer',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nAn input pointer to a ViUInt32. The caller of this function must\nallocate a ViUInt32 and pass the pointer to the array in this argument.\nWhen the function returns, the value at this pointer is set to the\nnumber of actual time stamps read. This value may be different than\ntimestampsToRead if a timeout or other error occurs while reading time\nstamps.\n'
                },
                'name': 'timeStampsRead',
                'type': 'ViUInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadTriggerTimeStamp': {
        'documentation': {
            'description': '\nThis function reads a trigger time stamp from the internal software\nbuffer for the specified terminal. The read operation is a\nsingle-time-stamp, destructive, blocking read. That is, the oldest\nunread time stamp associated with the specified terminal is returned.\nWhen a time stamp is read, it is removed from the buffer. The function\ndoes not return until a time stamp is available to be read or the\nspecified timeout elapses. If the internal software buffer associated\nwith the specified terminal is full, time stamp operations for that\nterminal are suspended and an error, specifying that the internal\nsoftware buffer overflowed, is returned when the\nniSync_ReadTriggerTimeStamp function is invoked. If the hardware\ntime-stamp buffer is full, all trigger time stamp operations are\nsuspended and an error, specifying that the hardware time-stamp buffer\noverflowed, is returned when the niSync_ReadTriggerTimeStamp function\nis invoked. That is, the niSync_ReadTriggerTimeStamp function continues\nto return previously generated time stamps, despite the overflow\ncondition, until no time stamps are available. To clear this error\ncondition, the niSync_DisableTimeStampTrigger function must be invoked.\nNote: NI-Sync supports only the time range between 1 January 1970 and 1\nJanuary 2100. Therefore, if the supported time range ends before a time\nstamp is captured, an error is returned. Note: The NI-Sync family of\ndevices uses the TAI timescale.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nAn input string enumeration that specifies the terminal containing the\ndigital signal that is the trigger whose oldest unread time stamp will\nbe read. Valid Values: NISYNC_VAL_PFI0 NISYNC_VAL_PFI1\nNISYNC_VAL_PFI2 NISYNC_VAL_PXITRIG0 NISYNC_VAL_PXITRIG1\nNISYNC_VAL_PXITRIG2 NISYNC_VAL_PXITRIG3 NISYNC_VAL_PXITRIG4\nNISYNC_VAL_PXITRIG5 NISYNC_VAL_PXITRIG6 NISYNC_VAL_PXITRIG7\nNISYNC_VAL_PXISTAR0 NISYNC_VAL_PXISTAR1 NISYNC_VAL_PXISTAR2\nNISYNC_VAL_PXISTAR3 NISYNC_VAL_PXISTAR4 NISYNC_VAL_PXISTAR5\nNISYNC_VAL_PXISTAR6 NISYNC_VAL_PXISTAR7 NISYNC_VAL_PXISTAR8\nNISYNC_VAL_PXISTAR9 NISYNC_VAL_PXISTAR10 NISYNC_VAL_PXISTAR11\nNISYNC_VAL_PXISTAR12\n'
                },
                'name': 'terminal',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nAn input floating-point number that specifies the number of seconds to\nwait for a time stamp to be generated before returning a timeout error.\nDefault Value: 10 seconds\n'
                },
                'name': 'timeout',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nAn output integer that specifies a portion of the board time when the\ntrigger associated with the specified terminal was detected.\n'
                },
                'name': 'timeSeconds',
                'type': 'ViUInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nAn output integer that specifies a portion of the board time when the\ntrigger associated with the specified terminal was detected.\n'
                },
                'name': 'timeNanoseconds',
                'type': 'ViUInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nAn output integer that specifies a portion of the board time when the\ntrigger associated with the specified terminal was detected.\n'
                },
                'name': 'timeFractionalNanoseconds',
                'type': 'ViUInt16'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nAn output integer enumeration that specifies the detected trigger\ncondition. Valid Values: NISYNC_VAL_EDGE_RISING\nNISYNC_VAL_EDGE_FALLING\n'
                },
                'name': 'detectedEdge',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ResetFrequency': {
        'documentation': {
            'description': '\nThis function resets the internal frequency at which the board time\nincrements to the default value.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'SendSoftwareTrigger': {
        'documentation': {
            'description': '\nThis function sends a pulse on the global software trigger terminal. The\nglobal software trigger terminal must be connected to a destination\nterminal for this operation to have any effect.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis input specifies the source software trigger terminal to send. When\nthis function is invoked, the global software trigger will be sent\nsimultaneously to all destination terminals that it is connected to.\nValid Values: NISYNC_VAL_SWTRIG_GLOBAL (Default Value)\n'
                },
                'name': 'sourceTerminal',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViBoolean': {
        'documentation': {
            'description': 'This function sets the value of a ViBoolean attribute.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSince NI-Sync does not include any channel-based attributes, this\nparameter is ignored. Default Value: ""\n'
                },
                'name': 'activeItem',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'This parameter specifies the ID of the attribute you wish to set.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the value to which you want to set the attribute. From the function\npanel window, you can use this control as follows. - If the attribute\ncurrently showing in the Attribute ID ring control has constants as\nvalid values, you can view a list of the constants by pressing on this\ncontrol. Select a value by double-clicking on it or by selecting it and\nthen pressing .\n',
                    'note': '\nSome of the values might not be valid depending on\nthe current settings of the instrument session. Default Value: none\n'
                },
                'name': 'attributeValue',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViInt32': {
        'documentation': {
            'description': 'This function sets the value of a ViInt32 attribute.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSince NI-Sync does not include any channel-based attributes, this\nparameter is ignored. Default Value: ""\n'
                },
                'name': 'activeItem',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'This parameter specifies the ID of the attribute you wish to set.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the value to which you want to set the attribute. From the function\npanel window, you can use this control as follows. - If the attribute\ncurrently showing in the Attribute ID ring control has constants as\nvalid values, you can view a list of the constants by pressing on this\ncontrol. Select a value by double-clicking on it or by selecting it and\nthen pressing .\n',
                    'note': '\nSome of the values might not be valid depending on\nthe current settings of the instrument session. Default Value: none\n'
                },
                'name': 'attributeValue',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViReal64': {
        'documentation': {
            'description': 'This function sets the value of a ViReal64 attribute.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSince NI-Sync does not include any channel-based attributes, this\nparameter is ignored. Default Value: ""\n'
                },
                'name': 'activeItem',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'This parameter specifies the ID of the attribute you wish to set.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the value to which you want to set the attribute. From the function\npanel window, you can use this control as follows. - If the attribute\ncurrently showing in the Attribute ID ring control has constants as\nvalid values, you can view a list of the constants by pressing on this\ncontrol. Select a value by double-clicking on it or by selecting it and\nthen pressing .\n',
                    'note': '\nSome of the values might not be valid depending on\nthe current settings of the instrument session. Default Value: none\n'
                },
                'name': 'attributeValue',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViString': {
        'documentation': {
            'description': '\nThis function sets the value of a ViString attribute. This is a\nlow-level function that you can use to set the values of\ninstrument-specific attributes and inherent IVI attributes. If the\nattribute represents an instrument state, this function performs\ninstrument I/O in the following cases: - State caching is disabled for\nthe entire session or for the particular attribute. - State caching is\nenabled and the currently cached value is invalid or is different than\nthe value you specify. This instrument driver contains high-level\nfunctions that set most of the instrument attributes. It is best to use\nthe high-level driver functions as much as possible. They handle order\ndependencies and multithread locking for you. In addition, they perform\nstatus checking only after setting all of the attributes. In contrast,\nwhen you set multiple attributes using the SetAttribute functions, the\nfunctions check the instrument status after each call. Also, when state\ncaching is enabled, the high-level functions that configure multiple\nattributes perform instrument I/O only for the attributes whose value\nyou change. Thus, you can safely call the high-level functions without\nthe penalty of redundant instrument I/O.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSince NI-Sync does not include any channel-based attributes, this\nparameter is ignored. Default Value: ""\n'
                },
                'name': 'activeItem',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'This parameter specifies the ID of the attribute you wish to set.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the value to which you want to set the attribute. From the function\npanel window, you can use this control as follows. - If the attribute\ncurrently showing in the Attribute ID ring control has constants as\nvalid values, you can view a list of the constants by pressing on this\ncontrol. Select a value by double-clicking on it or by selecting it and\nthen pressing .\n',
                    'note': '\nSome of the values might not be valid depending on\nthe current settings of the instrument session. Default Value: none\n'
                },
                'name': 'attributeValue',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetTime': {
        'documentation': {
            'description': '\nThis function sets the absolute board time to the time specified. This\nfunction leaves the internal frequency at which the board time\nincrements unchanged. Note: The NI-Sync family of devices uses the TAI\ntimescale.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nAn input integer enumeration that specifies the time source for the\nboard time. Valid Values: NISYNC_VAL_INIT_TIME_SRC_SYSTEM_CLK\n(Default) NISYNC_VAL_INIT_TIME_SRC_MANUAL\n'
                },
                'name': 'timeSource',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nAn integer that specifies the seconds portion of the time to which the\nboard time will be set. Note that NI-Sync supports setting the initial\ntime between 0 hours on 1 January 1970 and 0 hours on 1 January 2100.\nThis parameter is ignored unless the timeSource parameter is set to\nNISYNC_VAL_INIT_TIME_SRC_MANUAL.\n'
                },
                'name': 'timeSeconds',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nAn integer that specifies the nanoseconds portion of the time to which\nthe board time will be set. Note that NI-Sync supports setting the\ninitial time between 0 hours on 1 January 1970 and 0 hours on 1 January\n2100. This parameter is ignored unless the timeSource parameter is set\nto NISYNC_VAL_INIT_TIME_SRC_MANUAL.\n'
                },
                'name': 'timeNanoseconds',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nAn integer that specifies the fractional nanoseconds portion of the time\nto which the board time will be set. Note that NI-Sync supports setting\nthe initial time between 0 hours on 1 January 1970 and 0 hours on 1\nJanuary 2100. This parameter is ignored unless the timeSource parameter\nis set to NISYNC_VAL_INIT_TIME_SRC_MANUAL.\n'
                },
                'name': 'timeFractionalNanoseconds',
                'type': 'ViUInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetTimeReference1588OrdinaryClock': {
        'documentation': {
            'description': "\nThis function sets the time reference of the device associated with the\nspecified instrument handle. The time reference set is used to update\nthe value and frequency of the board time such that the board time\nreflects the time reference's time as closely as possible. The board\ntime is then used for tasks such as creating future time events, clocks,\nand timestamping triggers. This function is a nonblocking call that\nreturns immediately regardless of the state of the time reference set.\nSetting the time reference is a systemwide (per device) configuration\nthat persists after the session exits. The time reference is not\nreservable; the last call to set the time reference takes precedence. If\nthe time reference set is not providing valid time information, the\nboard time free runs from the last known time at the last frequency that\nwas applied. Note: When a device's board time and the configured time\nreference's time vary by more than 1 ms, a macro phase adjustment may be\nnecessary. A macro phase adjustment is when the board time is adjusted\nby a significant amount and, therefore, the board time no longer\natomically increments. This should not occur on a well designed and\nstable time reference. If this occurs, future time events, clocks, and\ntime stamps may be affected. If the board time is set forward, future\ntime events and clock transitions that were missed occur immediately. If\nthe board time is set backward, future time events and clock transitions\nare delayed. Note: An alternative to calling this function is to\nconfigure the default configured Time Reference through Measurement &\nAutomation Explorer. The state configured is then reapplied at every\nrestart. Note: Closing the session that calls this VI does not alter the\nvalue of the configured Time Reference. Note: The NI-Sync family of\ndevices uses the TAI timescale. This function sets the Time Reference of\nthe device to 1588.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetTimeReference8021As': {
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
    'SetTimeReferenceFreeRunning': {
        'documentation': {
            'description': "\nThis function sets the time reference of the device associated with the\nspecified instrument handle. The time reference set is used to update\nthe value and frequency of the board time such that the board time\nreflects the time reference's time as closely as possible. The board\ntime is then used for tasks such as creating future time events, clocks,\nand timestamping triggers. This function is a nonblocking call that\nreturns immediately regardless of the state of the time reference set.\nSetting the time reference is a systemwide (per device) configuration\nthat persists after the session exits. The time reference is not\nreservable; the last call to set the time reference takes precedence. If\nthe time reference set is not providing valid time information, the\nboard time free runs from the last known time at the last frequency that\nwas applied. Note: When a device's board time and the configured time\nreference's time vary by more than 1 ms, a macro phase adjustment may be\nnecessary. A macro phase adjustment is when the board time is adjusted\nby a significant amount and, therefore, the board time no longer\natomically increments. This should not occur on a well designed and\nstable time reference. If this occurs, future time events, clocks, and\ntime stamps may be affected. If the board time is set forward, future\ntime events and clock transitions that were missed occur immediately. If\nthe board time is set backward, future time events and clock transitions\nare delayed. Note: An alternative to calling this function is to\nconfigure the default configured Time Reference through Measurement &\nAutomation Explorer. The state configured is then reapplied at every\nrestart. Note: Closing the session that calls this VI does not alter the\nvalue of the configured Time Reference. Note: The NI-Sync family of\ndevices uses the TAI timescale. This function sets the Time Reference of\nthe device to free running. The board time is guaranteed to atomically\nincrement at the last calculated frequency. No external stimuli will\nalter the board time or frequency.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetTimeReferenceGps': {
        'documentation': {
            'description': "\nThis function sets the time reference of the device associated with the\nspecified instrument handle. The time reference set is used to update\nthe value and frequency of the board time such that the board time\nreflects the time reference's time as closely as possible. The board\ntime is then used for tasks such as creating future time events, clocks,\nand timestamping triggers. This function is a nonblocking call that\nreturns immediately regardless of the state of the time reference set.\nSetting the time reference is a systemwide (per device) configuration\nthat persists after the session exits. The time reference is not\nreservable; the last call to set the time reference takes precedence. If\nthe time reference set is not providing valid time information, the\nboard time free runs from the last known time at the last frequency that\nwas applied. Note: When a device's board time and the configured time\nreference's time vary by more than 1 ms, a macro phase adjustment may be\nnecessary. A macro phase adjustment is when the board time is adjusted\nby a significant amount and, therefore, the board time no longer\natomically increments. This should not occur on a well designed and\nstable time reference. If this occurs, future time events, clocks, and\ntime stamps may be affected. If the board time is set forward, future\ntime events and clock transitions that were missed occur immediately. If\nthe board time is set backward, future time events and clock transitions\nare delayed. Note: An alternative to calling this function is to\nconfigure the default configured Time Reference through Measurement &\nAutomation Explorer. The state configured is then reapplied at every\nrestart. Note: Closing the session that calls this VI does not alter the\nvalue of the configured Time Reference. Note: The NI-Sync family of\ndevices uses the TAI timescale. This function sets the Time Reference of\nthe device to GPS.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetTimeReferenceIrig': {
        'documentation': {
            'description': "\nThis function sets the time reference of the device associated with the\nspecified instrument handle. The time reference set is used to update\nthe value and frequency of the board time such that the board time\nreflects the time reference's time as closely as possible. The board\ntime is then used for tasks such as creating future time events, clocks,\nand timestamping triggers. This function is a nonblocking call that\nreturns immediately regardless of the state of the time reference set.\nSetting the time reference is a systemwide (per device) configuration\nthat persists after the session exits. The time reference is not\nreservable; the last call to set the time reference takes precedence. If\nthe time reference set is not providing valid time information, the\nboard time free runs from the last known time at the last frequency that\nwas applied. Note: When a device's board time and the configured time\nreference's time vary by more than 1 ms, a macro phase adjustment may be\nnecessary. A macro phase adjustment is when the board time is adjusted\nby a significant amount and, therefore, the board time no longer\natomically increments. This should not occur on a well designed and\nstable time reference. If this occurs, future time events, clocks, and\ntime stamps may be affected. If the board time is set forward, future\ntime events and clock transitions that were missed occur immediately. If\nthe board time is set backward, future time events and clock transitions\nare delayed. Note: An alternative to calling this function is to\nconfigure the default configured Time Reference through Measurement &\nAutomation Explorer. The state configured is then reapplied every\nrestart. Note: Closing the session that calls this VI does not alter the\nvalue of the configured Time Reference. Note: The NI-Sync family of\ndevices uses the TAI timescale. This function sets the Time Reference of\nthe device to IRIG.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nAn input integer enumeration of the IRIG input being supplied. Valid\nValues: NISYNC_VAL_IRIG_TYPE_IRIGB_DC\nNISYNC_VAL_IRIG_TYPE_IRIGB_AM (Default)\n'
                },
                'name': 'irigType',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nAn input string that specifies the terminal to which the IRIG input is\nconnected.\n'
                },
                'name': 'terminalName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetTimeReferencePps': {
        'documentation': {
            'description': "\nThis function sets the time reference of the device associated with the\nspecified instrument handle. The time reference set is used to update\nthe value and frequency of the board time such that the board time\nreflects the time reference's time as closely as possible. The board\ntime is then used for tasks such as creating future time events, clocks,\nand timestamping triggers. This function is a nonblocking call that\nreturns immediately regardless of the state of the time reference set.\nSetting the time reference is a systemwide (per device) configuration\nthat persists after the session exits. The time reference is not\nreservable; the last call to set the time reference takes precedence. If\nthe time reference set is not providing valid time information, the\nboard time free runs from the last known time at the last frequency that\nwas applied. Note: When a device's board time and the configured time\nreference's time vary by more than 1 ms, a macro phase adjustment may be\nnecessary. A macro phase adjustment is when the board time is adjusted\nby a significant amount and, therefore, the board time no longer\natomically increments. This should not occur on a well designed and\nstable time reference. If this occurs, future time events, clocks, and\ntime stamps may be affected. If the board time is set forward, future\ntime events and clock transitions that were missed occur immediately. If\nthe board time is set backward, future time events and clock transitions\nare delayed. Note: An alternative to calling this function is to\nconfigure the default configured Time Reference through Measurement &\nAutomation Explorer. The state configured is then reapplied at every\nrestart. Note: Closing the session that calls this VI does not alter the\nvalue of the configured Time Reference. Note: The NI-Sync family of\ndevices uses the TAI timescale. This function sets the Time Reference of\nthe device to PPS (pulse per second).\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nAn input string that specifies the terminal to which the PPS is\nsupplied.\n'
                },
                'name': 'terminalName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nAn input Boolean that specifies whether to use the user-supplied time or\nthe OS system time to represent the time at which the first pulse is\nreceived. If false, the OS system time is read at the time the first\npulse is received, and it is used to set the board time. If true, the\nuser-specified initial time is used to set the board time when the first\npulse is recevied. Every subsequent pulse is interpreted to be received\none second later, and the board time adjusted accordingly.\n'
                },
                'name': 'useManualTime',
                'type': 'ViBoolean'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nAn input integer that specifies the seconds field of the time to apply\nas the board time when the first pulse is received if useManualTime was\nset to VI_TRUE.\n'
                },
                'name': 'initialTimeSeconds',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nAn input integer that specifies the nanoseconds field of the time to\napply as the board time when the first pulse is received if\nuseManualTime was set to VI_TRUE.\n'
                },
                'name': 'initialNanoseconds',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nAn input integer that specifies the fractional nanoseconds field of the\ntime to apply as the board time when the first pulse is received if\nuseManualTime was set to VI_TRUE.\n'
                },
                'name': 'initialFractionalNanoseconds',
                'type': 'ViUInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'Start1588': {
        'documentation': {
            'description': '\nThis function starts participation in 1588. Note that this function\nreturns as soon as participation begins and does not wait until the 1588\nclock has reached a steady state. For clocks, future time events, and\ntriggered time stamps to be synchronized with respect to other devices\nparticipating in 1588, this function should be invoked, 1588 should be\nset as the Time Reference, and the 1588 clock should reach a steady\nstate before any of these operations are invoked. Note that you do not\nneed to invoke this function in the same session as these other\noperations, but rather you can invoke it in a separate session\nassociated with the same device. Note: An alternative to calling this\nfunction is to configure the 1588 default state through Measurement &\nAutomation Explorer. The state configured is then reapplied at every\nrestart. Note: Closing the session that calls this function does not\nstop 1588. Stop 1588 must be called explicitly from any session to stop\n1588 participation. Note: If the clock participating in 1588 enters the\nfaulty state, and 1588 is configured as the Time Reference, future time\nevents, clocks, and time stamps are no longer synchronized with other\n1588 devices participating in PTP. This should not occur on a well\ndesigned and stable network. You can check for this condition by\nmonitoring the 1588 clock state property.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'Start8021As': {
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
    'StartPtp': {
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
                'name': 'initialTimeSource',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'initialTimeSeconds',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'name': 'initialTimeNanoseconds',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'name': 'initialTimeFractionalNanoseconds',
                'type': 'ViUInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'Stop1588': {
        'documentation': {
            'description': 'This function stops participation in 1588.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'Stop8021As': {
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
    'StopPtp': {
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
    'close': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nThis function performs the following operations: - Closes the NI-Sync\nI/O session. - Destroys the NI-Sync session and all of its attributes. -\nDeallocates any memory resources the NI-Sync driver uses. Note: If the\nsession is locked, you must unlock the session before calling\nniSync_close. Note: After calling niSync_close, you cannot use the\ninstrument driver again until you call niSync_init. Note: If any clocks\nhave been created with the niSync_CreateClock function in the context\nof this session and have not been cleared, this function clears them. If\nany future time events have been created with the\nniSync_CreateFutureTimeEvent function in the context of this session\nand have not occurred or been cleared, this function clears them. If any\ntime stamp triggers have been enabled with the\nniSync_EnableTimeStampTrigger function in the context of this session\nand have not been disabled, this function clears them.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'error_message': {
        'documentation': {
            'description': '\nThis function converts a status code returned by an NI-Sync driver\nfunction into a user-readable string.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session. You can pass VI_NULL for\nthis parameter. This is useful when one of the initialize functions\nfail.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the Status parameter that is returned from any of the instrument\ndriver functions. Default Value: 0 (VI_SUCCESS)\n'
                },
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the user-readable message string that corresponds to the status\ncode you specify. You must pass a ViChar array at least 256 bytes in\nsize.\n'
                },
                'name': 'errorMessage',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'init': {
        'documentation': {
            'description': '\nThis function performs the following initialization actions: - Creates a\nnew NI-Sync instrument driver session. - Opens a session to the\nspecified device using the interface and address you specify for the\nResource Name parameter. - If the ID Query parameter is set to VI_TRUE,\nthis function queries the instrument ID and checks that it is valid for\nthis instrument driver. - If the Reset parameter is set to VI_TRUE,\nthis function resets the module to a known state. Returns a ViSession\nhandle that you use to identify the instrument in all subsequent\ninstrument driver function calls. - Returns an instrument handle that\nyou use to identify the instrument in all subsequent instrument driver\nfunction calls.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nResource name of the switch module to initialize. The resource name is\nassigned in Measurement & Automation Explorer (MAX). Syntax PXI[bus\nnumber]::device number NI-DAQmx name Optional fields are shown in square\nbrackets ([]).\n',
                    'note': '\nVISA aliases are also valid for the resource name.\nExample resource names: Resource Name Description Dev1 DAQmx name\nPXI1Slot5 DAQmx name PXI0::15::INSTR PXI bus 0, device number 15\nPXI::15::INSTR PXI bus 0, device number 15 PXI4::9::INSTR PXI bus 4,\ndevice number 9\n'
                },
                'name': 'resourceName',
                'type': 'ViRsrc'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis parameter is ignored. Because NI-Sync supports multiple timing and\nsynchronization modules, it always queries the device to determine which\ndevice is installed. Valid Values: VI_TRUE - Query the device (Default\nValue) VI_FALSE - Do not query the device\n'
                },
                'name': 'idQuery',
                'type': 'ViBoolean'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nSpecify whether you want the to reset the timing and synchronization\nmodule during the initialization procedure. Valid Range: VI_TRUE (1) -\nReset Device VI_FALSE (0) - Don't Reset (Default Value)\n"
                },
                'name': 'resetDevice',
                'type': 'ViBoolean'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns a ViSession handle that you use to identify the instrument in\nall subsequent instrument driver function calls.\n',
                    'note': '\nAlthough you can\ncreate more than one NI-Sync session for the same resource, it is best\nnot to do so. A better approach is to use the same NI-Sync session in\nmultiple execution threads. You can use VISA functions viLock and\nviUnlock to protect sections of code that require exclusive access to\nthe resource.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'python_name': 'init',
        'returns': 'ViStatus'
    },
    'reset': {
        'documentation': {
            'description': '\nThis function resets the module to a known state. Resetting the module\nperforms the following operations: - All terminal connections are\ndisconnected. - The DDS frequency is set to 0 Hz if DDS is supported. -\nAll PFI front panel terminals are set to 50 input impedance. - The front\n(PFI) and rear (PXI backplane) zone synchronization clock sources are\nset to PXI_Clk10. Resetting the module performs the following\noperations on a timing and synchronization module capable of 1588. - Any\nparticipation in PTP is stopped. - The 1588 clock is reset to the\ncurrent system time. - All clocks and future time events are cleared. -\nAll time stamp triggers are disabled.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'revision_query': {
        'documentation': {
            'description': '\nThis function returns the revision numbers of the NI-Sync driver and the\nfirmware of the module.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the NI-Sync software revision numbers in the form of a string.',
                    'note': 'You must pass a ViChar array at least 256 bytes in size.'
                },
                'name': 'instrumentDriverRevision',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the module firmware revision numbers in the form of a string.',
                    'note': 'You must pass a ViChar array at least 256 bytes in size.'
                },
                'name': 'firmwareRevision',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'self_test': {
        'documentation': {
            'description': "\nThis function runs the module's self test routine and returns the test\nresult(s). Note: Currently, this operation does nothing.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niSync_init. The handle\nidentifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': "\nThis control contains the value returned from the instrument self test.\nZero means success. For any other code, see the device's operator's\nmanual. Self-Test Code Description\n--------------------------------------- 0 Passed self test 1 Self test\nfailed\n"
                },
                'name': 'selfTestResult',
                'type': 'ViInt16'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': "\nReturns the self-test response string from the instrument. See the\ndevice's operation manual for an explanation of the string's contents.\n",
                    'note': 'You must pass a ViChar array at least 256 bytes in size.'
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
