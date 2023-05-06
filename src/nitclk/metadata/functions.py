# -*- coding: utf-8 -*-
# This file is generated from NI-TClk API metadata version 23.3.0f84
functions = {
    'ConfigureForHomogeneousTriggers': {
        'documentation': {
            'description': '\nConfigures the attributes commonly required for the TClk synchronization\nof device sessions with homogeneous triggers in a single PXI chassis or\na single PC. Use niTClk_ConfigureForHomogeneousTriggers to configure\nthe attributes for the reference clocks, start triggers, reference\ntriggers, script triggers, and pause triggers. If\nniTClk_ConfigureForHomogeneousTriggers cannot perform all the steps\nappropriate for the given sessions, it returns an error. If an error is\nreturned, use the instrument driver functions and attributes for signal\nrouting, along with the following NI-TClk attributes:\nNITCLK_ATTR_START_TRIGGER_MASTER_SESSION\nNITCLK_ATTR_REF_TRIGGER_MASTER_SESSION\nNITCLK_ATTR_PAUSE_TRIGGER_MASTER_SESSION\nniTClk_ConfigureForHomogeneousTriggers affects the following clocks and\ntriggers: - Reference clocks - Start triggers - Reference triggers -\nScript triggers - Pause triggers Reference Clocks\nniTClk_ConfigureForHomogeneousTriggers configures the reference clocks\nif they are needed. Specifically, if the internal sample clocks or\ninternal sample clock timebases are used, and the reference clock source\nis not configured--or is set to None (no trigger\nconfigured)--niTClk_ConfigureForHomogeneousTriggers configures the\nfollowing: PXI--The reference clock source on all devices is set to be\nthe 10 MHz PXI backplane clock (PXI_CLK10). PCI--One of the devices\nexports its 10 MHz onboard reference clock to RTSI 7. The reference\nclock source on all devices is set to be RTSI 7. Note: If the reference\nclock source is set to a value other than None,\nniTClk_ConfigureForHomogeneousTriggers cannot configure the reference\nclock source. Start Triggers If the start trigger is set to None (no\ntrigger configured) for all sessions, the sessions are configured to\nshare the start trigger. The start trigger is shared by: - Implicitly\nexporting the start trigger from one session - Configuring the other\nsessions for digital edge start triggers with sources corresponding to\nthe exported start trigger - Setting\nNITCLK_ATTR_START_TRIGGER_MASTER_SESSION to the session that is\nexporting the trigger for all sessions If the start triggers are None\nfor all except one session, niTClk_ConfigureForHomogeneousTriggers\nconfigures the sessions to share the start trigger from the one excepted\nsession. The start trigger is shared by: - Implicitly exporting start\ntrigger from the session with the start trigger that is not None -\nConfiguring the other sessions for digital-edge start triggers with\nsources corresponding to the exported start trigger - Setting\nNITCLK_ATTR_START_TRIGGER_MASTER_SESSION to the session that is\nexporting the trigger for all sessions If start triggers are configured\nfor all sessions, niTClk_ConfigureForHomogeneousTriggers does not\naffect the start triggers. Start triggers are considered to be\nconfigured for all sessions if either of the following conditions is\ntrue: - No session has a start trigger that is None - One session has a\nstart trigger that is None, and all other sessions have start triggers\nother than None. The one session with the None trigger must have\nNITCLK_ATTR_START_TRIGGER_MASTER_SESSION set to itself, indicating\nthat the session itself is the start trigger master Reference Triggers\nniTClk_ConfigureForHomogeneousTriggers configures sessions that support\nreference triggers to share the reference triggers if the reference\ntriggers are None (no trigger configured) for all except one session.\nThe reference triggers are shared by: - Implicitly exporting the\nreference trigger from the session whose reference trigger is not None -\nConfiguring the other sessions that support the reference trigger for\ndigital-edge reference triggers with sources corresponding to the\nexported reference trigger - Setting\nNITCLK_ATTR_REF_TRIGGER_MASTER_SESSION to the session that is\nexporting the trigger for all sessions that support reference trigger If\nthe reference triggers are configured for all sessions that support\nreference triggers, niTClk_ConfigureForHomogeneousTriggers does not\naffect the reference triggers. Reference triggers are considered to be\nconfigured for all sessions if either one or the other of the following\nconditions is true: - No session has a reference trigger that is None -\nOne session has a reference trigger that is None, and all other sessions\nhave reference triggers other than None. The one session with the None\ntrigger must have NITCLK_ATTR_REF_TRIGGER_MASTER_SESSION set to\nitself, indicating that the session itself is the reference trigger\nmaster Reference Trigger Holdoffs Acquisition sessions may be configured\nwith the reference trigger. For acquisition sessions, when the reference\ntrigger is shared, niTClk_ConfigureForHomogeneousTriggers configures\nthe holdoff attributes (which are instrument driver specific) on the\nreference trigger master session so that the session does not recognize\nthe reference trigger before the other sessions are ready. This\ncondition is only relevant when the sample clock rates, sample clock\ntimebase rates, sample counts, holdoffs, and/or any delays for the\nacquisitions are different. When the sample clock rates, sample clock\ntimebase rates, and/or the sample counts are different in acquisition\nsessions sharing the reference trigger, you should also set the holdoff\nattributes for the reference trigger master using the instrument driver.\nPause Triggers\nniTClk_ConfigureForHomogeneousTriggers configures generation sessions\nthat support pause triggers to share them, if the pause triggers are\nNone (no trigger configured) for all except one session. The pause\ntriggers are shared by: - Implicitly exporting the pause trigger from\nthe session whose script trigger is not None - Configuring the other\nsessions that support the pause trigger for digital-edge pause triggers\nwith sources corresponding to the exported pause trigger - Setting\nNITCLK_ATTR_PAUSE_TRIGGER_MASTER_SESSION to the session that is\nexporting the trigger for all sessions that support script triggers If\nthe pause triggers are configured for all generation sessions that\nsupport pause triggers, niTClk_ConfigureForHomogeneousTriggers does not\naffect pause triggers. Pause triggers are considered to be configured\nfor all sessions if either one or the other of the following conditions\nis true: - No session has a pause trigger that is None - One session has\na pause trigger that is None and all other sessions have pause triggers\nother than None. The one session with the None trigger must have\nNITCLK_ATTR_PAUSE_TRIGGER_MASTER_SESSION set to itself, indicating\nthat the session itself is the pause trigger master Note: TClk\nsynchronization is not supported for pause triggers on acquisition\nsessions.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of elements in the sessions array'
                },
                'name': 'sessionCount',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'sessions is an array of sessions that are being synchronized.'
                },
                'is_session_handle': False,
                'name': 'sessions',
                'python_api_converter_name': 'convert_to_nitclk_session_number_list',
                'size': {
                    'mechanism': 'len',
                    'value': 'sessionCount'
                },
                'type': 'ViSession[]',
                'type_in_documentation': 'list of instrument-specific sessions or nitclk.SessionReference instances'
            }
        ],
        'returns': 'ViStatus'
    },
    'FinishSyncPulseSenderSynchronize': {
        'documentation': {
            'description': 'Finishes synchronizing the Sync Pulse Sender.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of elements in the sessions array'
                },
                'name': 'sessionCount',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'sessions is an array of sessions that are being synchronized.'
                },
                'is_session_handle': False,
                'name': 'sessions',
                'python_api_converter_name': 'convert_to_nitclk_session_number_list',
                'size': {
                    'mechanism': 'len',
                    'value': 'sessionCount'
                },
                'type': 'ViSession[]',
                'type_in_documentation': 'list of instrument-specific sessions or nitclk.SessionReference instances'
            },
            {
                'default_value': 'hightime.timedelta(seconds=0.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nMinimal period of TClk, expressed in seconds. Supported values are\nbetween 0.0 s and 0.050 s (50 ms). Minimal period for a single\nchassis/PC is 200 ns. If the specified value is less than 200 ns,\nNI-TClk automatically coerces minTime to 200 ns. For multichassis\nsynchronization, adjust this value to account for propagation delays\nthrough the various devices and cables.\n'
                },
                'name': 'minTime',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViReal64': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Gets the value of an NI-TClk ViReal64 attribute.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'session references the sessions being synchronized.'
                },
                'name': 'session',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass VI_NULL or an empty string'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe ID of the attribute that you want to get Supported Attribute\nNITCLK_ATTR_SAMPLE_CLOCK_DELAY\n'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The value that you are getting'
                },
                'name': 'value',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViSession': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Gets the value of an NI-TClk ViSession attribute.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'session references the sessions being synchronized.'
                },
                'name': 'session',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass VI_NULL or an empty string'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe ID of the attribute that you want to set Supported Attributes\nNITCLK_ATTR_START_TRIGGER_MASTER_SESSION\nNITCLK_ATTR_REF_TRIGGER_MASTER_SESSION\nNITCLK_ATTR_PAUSE_TRIGGER_MASTER_SESSION\n'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The value that you are getting'
                },
                'is_session_handle': False,
                'name': 'value',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViString': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nThis function queries the value of an NI-TClk ViString attribute. You\nmust provide a ViChar array to serve as a buffer for the value. You pass\nthe number of bytes in the buffer as bufSize. If the current value of\nthe attribute, including the terminating NULL byte, is larger than the\nsize you indicate in bufSize, the function copies bufSize minus 1 bytes\ninto the buffer, places an ASCII NULL byte at the end of the buffer, and\nreturns the array size that you must pass to get the entire value. For\nexample, if the value is "123456" and bufSize is 4, the function places\n"123" into the buffer and returns 7. If you want to call\nniTClk_GetAttributeViString just to get the required array size, pass 0\nfor bufSize and VI_NULL for the value.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'session references the sessions being synchronized.'
                },
                'name': 'session',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass VI_NULL or an empty string'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe ID of the attribute that you want to get Supported Attributes\nNITCLK_ATTR_SYNC_PULSE_SOURCE\nNITCLK_ATTR_SYNC_PULSE_CLOCK_SOURCE\nNITCLK_ATTR_EXPORTED_SYNC_PULSE_OUTPUT_TERMINAL\n'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe number of bytes in the ViChar array that you specify for the value\nparameter\n'
                },
                'name': 'bufSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The value that you are getting'
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
    'GetExtendedErrorInfo': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nReports extended error information for the most recent NI-TClk function\nthat returned an error. To establish the function that returned an\nerror, use the return values of the individual functions because once\nniTClk_GetExtendedErrorInfo reports an errorString, it does not report\nan empty string again.\n'
        },
        'included_in_proto': True,
        'is_error_handling': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'none'
            }
        ],
        'parameters': [
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nExtended error description. If errorString is NULL, then it is not large\nenough to hold the entire error description. In this case, the return\nvalue of niTClk_GetExtendedErrorInfo is the size that you should use\nfor niTClk_GetExtendedErrorInfo to return the full error string.\n'
                },
                'name': 'errorString',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'errorStringSize'
                },
                'type': 'ViChar[]'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSize of the errorString. If errorStringSize is 0, then it is not large\nenough to hold the entire error description. In this case, the return\nvalue of niTClk_GetExtendedErrorInfo is the size that you should use\nfor niTClk_GetExtendedErrorInfo to return the full error string.\n'
                },
                'name': 'errorStringSize',
                'type': 'ViUInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'Initiate': {
        'documentation': {
            'description': '\nInitiates the acquisition or generation sessions specified, taking into\nconsideration any special requirements needed for synchronization. For\nexample, the session exporting the TClk-synchronized start trigger is\nnot initiated until after niTClk_Initiate initiates all the sessions\nthat import the TClk-synchronized start trigger.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of elements in the sessions array'
                },
                'name': 'sessionCount',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'sessions is an array of sessions that are being synchronized.'
                },
                'is_session_handle': False,
                'name': 'sessions',
                'python_api_converter_name': 'convert_to_nitclk_session_number_list',
                'size': {
                    'mechanism': 'len',
                    'value': 'sessionCount'
                },
                'type': 'ViSession[]',
                'type_in_documentation': 'list of instrument-specific sessions or nitclk.SessionReference instances'
            }
        ],
        'returns': 'ViStatus'
    },
    'IsDone': {
        'documentation': {
            'description': '\nMonitors the progress of the acquisitions and/or generations\ncorresponding to sessions.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of elements in the sessions array'
                },
                'name': 'sessionCount',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'sessions is an array of sessions that are being synchronized.'
                },
                'is_session_handle': False,
                'name': 'sessions',
                'python_api_converter_name': 'convert_to_nitclk_session_number_list',
                'size': {
                    'mechanism': 'len',
                    'value': 'sessionCount'
                },
                'type': 'ViSession[]',
                'type_in_documentation': 'list of instrument-specific sessions or nitclk.SessionReference instances'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nIndicates that the operation is done. The operation is done when each\nsession has completed without any errors or when any one of the sessions\nreports an error.\n'
                },
                'name': 'done',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViReal64': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nSets the value of an NI-TClk VIReal64 attribute.\nniTClk_SetAttributeViReal64 is a low-level function that you can use to\nset the values NI-TClk attributes. NI-TClk contains high-level functions\nthat set most of the attributes. It is best to use the high-level\nfunctions as much as possible.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'session references the sessions being synchronized.'
                },
                'name': 'session',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass VI_NULL or an empty string'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe ID of the attribute that you want to set Supported Attribute\nNITCLK_ATTR_SAMPLE_CLOCK_DELAY\n'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The value for the attribute'
                },
                'grpc_name': 'value_raw',
                'name': 'value',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViSession': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nSets the value of an NI-TClk ViSession attribute.\nniTClk_SetAttributeViSession is a low-level function that you can use\nto set the values NI-TClk attributes. NI-TClk contains high-level\nfunctions that set most of the attributes. It is best to use the\nhigh-level functions as much as possible.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'session references the sessions being synchronized.'
                },
                'name': 'session',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass VI_NULL or an empty string'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe ID of the attribute that you want to set Supported Attributes\nNITCLK_ATTR_START_TRIGGER_MASTER_SESSION\nNITCLK_ATTR_REF_TRIGGER_MASTER_SESSION\nNITCLK_ATTR_PAUSE_TRIGGER_MASTER_SESSION\n'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The value for the attribute'
                },
                'is_session_handle': False,
                'name': 'value',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViString': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nSets the value of an NI-TClk VIString attribute.\nniTClk_SetAttributeViString is a low-level function that you can use to\nset the values of NI-TClk attributes. NI-TClk contain high-level\nfunctions that set most of the attributes. It is best to use the\nhigh-level functions as much as possible.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'session references the sessions being synchronized.'
                },
                'name': 'session',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass VI_NULL or an empty string'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the ID of the attribute that you want to set Supported Attributes\nNITCLK_ATTR_SYNC_PULSE_SOURCE\nNITCLK_ATTR_SYNC_PULSE_CLOCK_SOURCE\nNITCLK_ATTR_EXPORTED_SYNC_PULSE_OUTPUT_TERMINAL\n'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value for the attribute'
                },
                'grpc_name': 'value_raw',
                'name': 'value',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetupForSyncPulseSenderSynchronize': {
        'documentation': {
            'description': 'Configures the TClks on all the devices and prepares the Sync Pulse Sender for synchronization'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of elements in the sessions array'
                },
                'name': 'sessionCount',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'sessions is an array of sessions that are being synchronized.'
                },
                'is_session_handle': False,
                'name': 'sessions',
                'python_api_converter_name': 'convert_to_nitclk_session_number_list',
                'size': {
                    'mechanism': 'len',
                    'value': 'sessionCount'
                },
                'type': 'ViSession[]',
                'type_in_documentation': 'list of instrument-specific sessions or nitclk.SessionReference instances'
            },
            {
                'default_value': 'hightime.timedelta(seconds=0.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nMinimal period of TClk, expressed in seconds. Supported values are\nbetween 0.0 s and 0.050 s (50 ms). Minimal period for a single\nchassis/PC is 200 ns. If the specified value is less than 200 ns,\nNI-TClk automatically coerces minTime to 200 ns. For multichassis\nsynchronization, adjust this value to account for propagation delays\nthrough the various devices and cables.\n'
                },
                'name': 'minTime',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            }
        ],
        'returns': 'ViStatus'
    },
    'Synchronize': {
        'documentation': {
            'description': '\nSynchronizes the TClk signals on the given sessions. After\nniTClk_Synchronize executes, TClk signals from all sessions are\nsynchronized. Note: Before using this NI-TClk function, verify that your\nsystem is configured as specified in the PXI Trigger Lines and RTSI\nLines topic of the NI-TClk Synchronization Help. You can locate this\nhelp file at Start>>Programs>>National Instruments>>NI-TClk.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of elements in the sessions array'
                },
                'name': 'sessionCount',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'sessions is an array of sessions that are being synchronized.'
                },
                'is_session_handle': False,
                'name': 'sessions',
                'python_api_converter_name': 'convert_to_nitclk_session_number_list',
                'size': {
                    'mechanism': 'len',
                    'value': 'sessionCount'
                },
                'type': 'ViSession[]',
                'type_in_documentation': 'list of instrument-specific sessions or nitclk.SessionReference instances'
            },
            {
                'default_value': 'hightime.timedelta(seconds=0.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nMinimal period of TClk, expressed in seconds. Supported values are\nbetween 0.0 s and 0.050 s (50 ms). Minimal period for a single\nchassis/PC is 200 ns. If the specified value is less than 200 ns,\nNI-TClk automatically coerces minTime to 200 ns. For multichassis\nsynchronization, adjust this value to account for propagation delays\nthrough the various devices and cables.\n'
                },
                'name': 'minTclkPeriod',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            }
        ],
        'returns': 'ViStatus'
    },
    'SynchronizeToSyncPulseSender': {
        'documentation': {
            'description': 'Synchronizes the other devices to the Sync Pulse Sender.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of elements in the sessions array'
                },
                'name': 'sessionCount',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'sessions is an array of sessions that are being synchronized.'
                },
                'is_session_handle': False,
                'name': 'sessions',
                'python_api_converter_name': 'convert_to_nitclk_session_number_list',
                'size': {
                    'mechanism': 'len',
                    'value': 'sessionCount'
                },
                'type': 'ViSession[]',
                'type_in_documentation': 'list of instrument-specific sessions or nitclk.SessionReference instances'
            },
            {
                'default_value': 'hightime.timedelta(seconds=0.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nMinimal period of TClk, expressed in seconds. Supported values are\nbetween 0.0 s and 0.050 s (50 ms). Minimal period for a single\nchassis/PC is 200 ns. If the specified value is less than 200 ns,\nNI-TClk automatically coerces minTime to 200 ns. For multichassis\nsynchronization, adjust this value to account for propagation delays\nthrough the various devices and cables.\n'
                },
                'name': 'minTime',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            }
        ],
        'returns': 'ViStatus'
    },
    'WaitUntilDone': {
        'documentation': {
            'description': '\nCall this function to pause execution of your program until the\nacquisitions and/or generations corresponding to sessions are done or\nuntil the function returns a timeout error. niTClk_WaitUntilDone is a\nblocking function that periodically checks the operation status. It\nreturns control to the calling program if the operation completes\nsuccessfully or an error occurs (including a timeout error). This\nfunction is most useful for finite data operations that you expect to\ncomplete within a certain time.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of elements in the sessions array'
                },
                'name': 'sessionCount',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'sessions is an array of sessions that are being synchronized.'
                },
                'is_session_handle': False,
                'name': 'sessions',
                'python_api_converter_name': 'convert_to_nitclk_session_number_list',
                'size': {
                    'mechanism': 'len',
                    'value': 'sessionCount'
                },
                'type': 'ViSession[]',
                'type_in_documentation': 'list of instrument-specific sessions or nitclk.SessionReference instances'
            },
            {
                'default_value': 'hightime.timedelta(seconds=0.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe amount of time in seconds that niTClk_WaitUntilDone waits for the\nsessions to complete. If timeout is exceeded, niTClk_WaitUntilDone\nreturns an error.\n'
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            }
        ],
        'returns': 'ViStatus'
    }
}
