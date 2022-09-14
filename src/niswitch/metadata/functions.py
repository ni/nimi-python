# -*- coding: utf-8 -*-
# This file is generated from NI-SWITCH API metadata version 22.8.0d32
functions = {
    'AbortScan': {
        'documentation': {
            'description': '\nAborts the scan in progress. Initiate a scan with\nniSwitch_InitiateScan. If the switch module is not scanning,\nNISWITCH_ERROR_NO_SCAN_IN_PROGRESS error is returned.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'python_name': 'abort',
        'returns': 'ViStatus'
    },
    'CanConnect': {
        'documentation': {
            'description': '\nVerifies that a path between channel 1 and channel 2 can be created. If\na path is possible in the switch module, the availability of that path\nis returned given the existing connections. If the path is possible but\nin use, a NISWITCH_WARN_IMPLICIT_CONNECTION_EXISTS warning is\nreturned.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nInput one of the channel names of the desired path. Pass the other\nchannel name as the channel 2 parameter. Refer to Devices Overview for\nvalid channel names for the switch module. Examples of valid channel\nnames: ch0, com0, ab0, r1, c2, cjtemp Default value: ""\n'
                },
                'name': 'channel1',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nInput one of the channel names of the desired path. Pass the other\nchannel name as the channel 1 parameter. Refer to Devices Overview for\nvalid channel names for the switch module. Examples of valid channel\nnames: ch0, com0, ab0, r1, c2, cjtemp Default value: ""\n'
                },
                'name': 'channel2',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nIndicates whether a path is valid. Possible values include:\n\n- NISWITCH_VAL_PATH_AVAILABLE 1\n- NISWITCH_VAL_PATH_EXISTS 2\n- NISWITCH_VAL_PATH_UNSUPPORTED 3\n- NISWITCH_VAL_RESOURCE_IN_USE 4\n- NISWITCH_VAL_SOURCE_CONFLICT 5\n- NISWITCH_VAL_CHANNEL_NOT_AVAILABLE 6\n\nNotes: (1)\nNISWITCH_VAL_PATH_AVAILABLE indicates that the driver can create the\npath at this time. (2) NISWITCH_VAL_PATH_EXISTS indicates that the\npath already exists. (3) NISWITCH_VAL_PATH_UNSUPPORTED indicates that\nthe instrument is not capable of creating a path between the channels\nyou specify. (4) NISWITCH_VAL_RESOURCE_IN_USE indicates that although\nthe path is valid, the driver cannot create the path at this moment\nbecause the switch device is currently using one or more of the required\nchannels to create another path. You must destroy the other path before\ncreating this one. (5) NISWITCH_VAL_SOURCE_CONFLICT indicates that\nthe instrument cannot create a path because both channels are connected\nto a different source channel. (6)\nNISWITCH_VAL_CHANNEL_NOT_AVAILABLE indicates that the driver cannot\ncreate a path between the two channels because one of the channels is a\nconfiguration channel and thus unavailable for external connections.\n'
                },
                'enum': 'PathCapability',
                'name': 'pathCapability',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'Commit': {
        'documentation': {
            'description': '\nDownloads the configured scan list and trigger settings to hardware.\nCalling niSwitch_Commit optional as it is implicitly called during\nniSwitch_InitiateScan. Use niSwitch_Commit to arm triggers in a given\norder or to control when expensive hardware operations are performed.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'Connect': {
        'documentation': {
            'description': '\nCreates a path between channel 1 and channel 2. The driver calculates\nand uses the shortest path between the two channels. Refer to Immediate\nOperations for information about Channel Usage types. If a path is not\navailable, the function returns one of the following errors: -\nNISWITCH_ERROR_EXPLICIT_CONNECTION_EXISTS, if the two channels are\nalready explicitly connected by calling either the niSwitch_Connect or\nniSwitch_SetPath function. -\nNISWITCH_ERROR_IS_CONFIGURATION_CHANNEL, if a channel is a\nconfiguration channel. Error elaboration contains information about\nwhich of the two channels is a configuration channel. -\nNISWITCH_ERROR_ATTEMPT_TO_CONNECT_SOURCES, if both channels are\nconnected to a different source. Error elaboration contains information\nabout sources channel 1 and 2 connect to. -\nNISWITCH_ERROR_CANNOT_CONNECT_TO_ITSELF, if channels 1 and 2 are\none and the same channel. - NISWITCH_ERROR_PATH_NOT_FOUND, if the\ndriver cannot find a path between the two channels. Note: Paths are\nbidirectional. For example, if a path exists between channels CH1 and\nCH2, then the path also exists between channels CH2 and CH1.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nInput one of the channel names of the desired path. Pass the other\nchannel name as the channel 2 parameter. Refer to Devices Overview for\nvalid channel names for the switch module. Examples of valid channel\nnames: ch0, com0, ab0, r1, c2, cjtemp Default value: None\n'
                },
                'name': 'channel1',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nInput one of the channel names of the desired path. Pass the other\nchannel name as the channel 1 parameter. Refer to Devices Overview for\nvalid channel names for the switch module. Examples of valid channel\nnames: ch0, com0, ab0, r1, c2, cjtemp Default value: None\n'
                },
                'name': 'channel2',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConnectMultiple': {
        'documentation': {
            'description': '\nCreates the connections between channels specified in Connection List.\nSpecify connections with two endpoints only or the explicit path between\ntwo endpoints. NI-SWITCH calculates and uses the shortest path between\nthe channels. Refer to Setting Source and Configuration Channels for\ninformation about channel usage types. In the event of an error,\nconnecting stops at the point in the list where the error occurred. If a\npath is not available, the function returns one of the following errors:\n- NISWITCH_ERROR_EXPLICIT_CONNECTION_EXISTS, if the two channels are\nalready explicitly connected. -\nNISWITCH_ERROR_IS_CONFIGURATION_CHANNEL, if a channel is a\nconfiguration channel. Error elaboration contains information about\nwhich of the two channels is a configuration channel. -\nNISWITCH_ERROR_ATTEMPT_TO_CONNECT_SOURCES, if both channels are\nconnected to a different source. Error elaboration contains information\nabout sources channel 1 and 2 to connect. -\nNISWITCH_ERROR_CANNOT_CONNECT_TO_ITSELF, if channels 1 and 2 are\none and the same channel. - NISWITCH_ERROR_PATH_NOT_FOUND, if the\ndriver cannot find a path between the two channels. Note: Paths are\nbidirectional. For example, if a path exists between channels ch1 and\nch2, then the path also exists between channels ch1 and ch2.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nConnection List specifies a list of connections between channels to\nmake. NI-SWITCH validates the connection list, and aborts execution of\nthe list if errors are returned. Refer to Connection and Disconnection\nList Syntax for valid connection list syntax and examples. Refer to\nDevices Overview for valid channel names for the switch module. Example\nof a valid connection list: c0 -> r1, [c2 -> r2 -> c3] In this example,\nr2 is a configuration channel. Default value: None\n'
                },
                'name': 'connectionList',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'Disable': {
        'documentation': {
            'description': '\nPlaces the switch module in a quiescent state where it has minimal or no\nimpact on the system to which it is connected. All channels are\ndisconnected and any scan in progress is aborted.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'Disconnect': {
        'documentation': {
            'description': '\nThis function destroys the path between two channels that you create\nwith the niSwitch_Connect or niSwitch_SetPath function. If a path is\nnot connected or not available, the function returns the\nIVISWTCH_ERROR_NO_SUCH_PATH error.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nInput one of the channel names of the path to break. Pass the other\nchannel name as the channel 2 parameter. Refer to Devices Overview for\nvalid channel names for the switch module. Examples of valid channel\nnames: ch0, com0, ab0, r1, c2, cjtemp Default value: None\n'
                },
                'name': 'channel1',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nInput one of the channel names of the path to break. Pass the other\nchannel name as the channel 1 parameter. Refer to Devices Overview for\nvalid channel names for the switch module. Examples of valid channel\nnames: ch0, com0, ab0, r1, c2, cjtemp Default value: None\n'
                },
                'name': 'channel2',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisconnectAll': {
        'documentation': {
            'description': '\nBreaks all existing paths. If the switch module cannot break all paths,\nNISWITCH_WARN_PATH_REMAINS warning is returned.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisconnectMultiple': {
        'documentation': {
            'description': '\nBreaks the connections between channels specified in Disconnection List.\nIf no connections exist between channels, NI-SWITCH returns an error. In\nthe event of an error, the VI stops at the point in the list where the\nerror occurred.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nDisconnection List specifies a list of connections between channels to\nbreak. NI-SWITCH validates the disconnection list, and aborts execution\nof the list if errors are returned. Refer to Connection and\nDisconnection List Syntax for valid disconnection list syntax and\nexamples. Refer to Devices Overview for valid channel names for the\nswitch module. Example of a valid disconnection list: c0 -> r1, [c2 ->\nr2 -> c3] In this example, r2 is a configuration channel. Default value:\nNone\n'
                },
                'name': 'disconnectionList',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViBoolean': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nThis function queries the value of a ViBoolean attribute. You can use\nthis function to get the values of instrument specific attributes and\ninherent IVI attributes. If the attribute represents an instrument\nstate, this function performs instrument I/O in the following cases: -\nState caching is disabled for the entire session or for the particular\nattribute. - State caching is enabled and the currently cached value is\ninvalid.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSome attributes are unique per channel. For these, pass the name of the\nchannel. Other attributes are unique per switch device. Pass VI_NULL or\nan empty string for this parameter. Default Value: ""\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the ID of an attribute. From the function panel window, you can use\nthis control as follows. - Click on the control or press , , or , to\ndisplay a dialog box containing a hierarchical list of the available\nattributes. Attributes whose value cannot be set are dim. Help text is\nshown for each attribute. Select an attribute by double-clicking on it\nor by selecting it and then pressing . A ring control at the top of the\ndialog box allows you to see all IVI attributes or only the attributes\nof the ViInt32 type. If you choose to see all IVI attributes, the data\ntypes appear to the right of the attribute names in the list box. The\ndata types that are not consistent with this function are dim. If you\nselect an attribute data type that is dim, LabWindows/CVI transfers you\nto the function panel for the corresponding function that is consistent\nwith the data type. - If you want to enter a variable name, press to\nchange this ring control to a manual input box. - If the attribute in\nthis ring control has constants as valid values, you can view the\nconstants by moving to the Attribute Value control and pressing .\n'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the current value of the attribute. Pass the address of a\nViBoolean variable. From the function panel window, you can use this\ncontrol as follows. - If the attribute currently showing in the\nAttribute ID ring control has constants as valid values, you can view a\nlist of the constants by pressing on this control. Select a value by\ndouble-clicking on it or by selecting it and then pressing .\n'
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
            'description': '\nThis function queries the value of a ViInt32 attribute. You can use this\nfunction to get the values of instrument specific attributes and\ninherent IVI attributes. If the attribute represents an instrument\nstate, this function performs instrument I/O in the following cases: -\nState caching is disabled for the entire session or for the particular\nattribute. - State caching is enabled and the currently cached value is\ninvalid.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSome attributes are unique per channel. For these, pass the name of the\nchannel. Other attributes are unique per switch device. Pass VI_NULL or\nan empty string for this parameter. Default Value: ""\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the ID of an attribute. From the function panel window, you can use\nthis control as follows. - Click on the control or press , , or , to\ndisplay a dialog box containing a hierarchical list of the available\nattributes. Attributes whose value cannot be set are dim. Help text is\nshown for each attribute. Select an attribute by double-clicking on it\nor by selecting it and then pressing . A ring control at the top of the\ndialog box allows you to see all IVI attributes or only the attributes\nof the ViInt32 type. If you choose to see all IVI attributes, the data\ntypes appear to the right of the attribute names in the list box. The\ndata types that are not consistent with this function are dim. If you\nselect an attribute data type that is dim, LabWindows/CVI transfers you\nto the function panel for the corresponding function that is consistent\nwith the data type. - If you want to enter a variable name, press to\nchange this ring control to a manual input box. - If the attribute in\nthis ring control has constants as valid values, you can view the\nconstants by moving to the Attribute Value control and pressing .\n'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the current value of the attribute. Pass the address of a\nViInt32 variable. From the function panel window, you can use this\ncontrol as follows. - If the attribute currently showing in the\nAttribute ID ring control has constants as valid values, you can view a\nlist of the constants by pressing on this control. Select a value by\ndouble-clicking on it or by selecting it and then pressing .\n'
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
            'description': '\nThis function queries the value of a ViReal64 attribute. You can use\nthis function to get the values of instrument specific attributes and\ninherent IVI attributes. If the attribute represents an instrument\nstate, this function performs instrument I/O in the following cases: -\nState caching is disabled for the entire session or for the particular\nattribute. - State caching is enabled and the currently cached value is\ninvalid.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSome attributes are unique per channel. For these, pass the name of the\nchannel. Other attributes are unique per switch device. Pass VI_NULL or\nan empty string for this parameter. Default Value: ""\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the ID of an attribute. From the function panel window, you can use\nthis control as follows. - Click on the control or press , , or , to\ndisplay a dialog box containing a hierarchical list of the available\nattributes. Attributes whose value cannot be set are dim. Help text is\nshown for each attribute. Select an attribute by double-clicking on it\nor by selecting it and then pressing . A ring control at the top of the\ndialog box allows you to see all IVI attributes or only the attributes\nof the ViInt32 type. If you choose to see all IVI attributes, the data\ntypes appear to the right of the attribute names in the list box. The\ndata types that are not consistent with this function are dim. If you\nselect an attribute data type that is dim, LabWindows/CVI transfers you\nto the function panel for the corresponding function that is consistent\nwith the data type. - If you want to enter a variable name, press to\nchange this ring control to a manual input box. - If the attribute in\nthis ring control has constants as valid values, you can view the\nconstants by moving to the Attribute Value control and pressing .\n'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the current value of the attribute. Pass the address of a\nViReal64 variable. From the function panel window, you can use this\ncontrol as follows. - If the attribute currently showing in the\nAttribute ID ring control has constants as valid values, you can view a\nlist of the constants by pressing on this control. Select a value by\ndouble-clicking on it or by selecting it and then pressing .\n'
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
            'description': '\nThis function queries the value of a ViString attribute. You can use\nthis function to get the values of instrument specific attributes and\ninherent IVI attributes. If the attribute represents an instrument\nstate, this function performs instrument I/O in the following cases: -\nState caching is disabled for the entire session or for the particular\nattribute. - State caching is enabled and the currently cached value is\ninvalid. You must provide a ViChar array to serve as a buffer for the\nvalue. You pass the number of bytes in the buffer as the Array Size\nparameter. If the current value of the attribute, including the\nterminating NULL byte, is larger than the size you indicate in the Array\nSize parameter, the function copies Array Size-1 bytes into the buffer,\nplaces an ASCII NULL byte at the end of the buffer, and returns the\narray size you must pass to get the entire value. For example, if the\nvalue is "123456" and the Array Size is 4, the function places "123"\ninto the buffer and returns 7. If you want to call this function just to\nget the required array size, you can pass 0 for the Array Size and\nVI_NULL for the Attribute Value buffer. If you want the function to\nfill in the buffer regardless of the number of bytes in the value, pass\na negative number for the Array Size parameter.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSome attributes are unique per channel. For these, pass the name of the\nchannel. Other attributes are unique per switch device. Pass VI_NULL or\nan empty string for this parameter. Default Value: ""\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the ID of an attribute. From the function panel window, you can use\nthis control as follows. - Click on the control or press , , or , to\ndisplay a dialog box containing a hierarchical list of the available\nattributes. Attributes whose value cannot be set are dim. Help text is\nshown for each attribute. Select an attribute by double-clicking on it\nor by selecting it and then pressing . A ring control at the top of the\ndialog box allows you to see all IVI attributes or only the attributes\nof the ViInt32 type. If you choose to see all IVI attributes, the data\ntypes appear to the right of the attribute names in the list box. The\ndata types that are not consistent with this function are dim. If you\nselect an attribute data type that is dim, LabWindows/CVI transfers you\nto the function panel for the corresponding function that is consistent\nwith the data type. - If you want to enter a variable name, press to\nchange this ring control to a manual input box. - If the attribute in\nthis ring control has constants as valid values, you can view the\nconstants by moving to the Attribute Value control and pressing .\n'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the number of bytes in the ViChar array you specify for the\nAttribute Value parameter. If the current value of the attribute,\nincluding the terminating NUL byte, contains more bytes that you\nindicate in this parameter, the function copies Array Size-1 bytes into\nthe buffer, places an ASCII NUL byte at the end of the buffer, and\nreturns the array size you must pass to get the entire value. For\nexample, if the value is "123456" and the Array Size is 4, the function\nplaces "123" into the buffer and returns 7. If you pass a negative\nnumber, the function copies the value to the buffer regardless of the\nnumber of bytes in the value. If you pass 0, you can pass VI_NULL for\nthe Attribute Value buffer parameter. Default Value:512\n'
                },
                'name': 'arraySize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe buffer in which the function returns the current value of the\nattribute. The buffer must be of type ViChar and have at least as many\nbytes as indicated in the Array Size parameter. If the current value of\nthe attribute, including the terminating NUL byte, contains more bytes\nthat you indicate in this parameter, the function copies Array Size-1\nbytes into the buffer, places an ASCII NUL byte at the end of the\nbuffer, and returns the array size you must pass to get the entire\nvalue. For example, if the value is "123456" and the Array Size is 4,\nthe function places "123" into the buffer and returns 7. If you specify\n0 for the Array Size parameter, you can pass VI_NULL for this\nparameter. From the function panel window, you can use this control as\nfollows. - If the attribute currently showing in the Attribute ID ring\ncontrol has constants as valid values, you can view a list of the\nconstants by pressing on this control. Select a value by double-clicking\non it or by selecting it and then pressing .\n'
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
            'description': '\nReturns the channel string that is in the channel table at the specified\nindex. Use niSwitch_GetChannelName in a For Loop to get a complete list\nof valid channel names for the switch module. Use the Channel Count\nattribute to determine the number of channels.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA 1-based index into the channel table. Default value: 1 Maximum value:\nValue of Channel Count attribute.\n'
                },
                'name': 'index',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the number of bytes in the ViChar array you specify for the Channel\nName Buffer parameter. If the channel name string, including the\nterminating NUL byte, contains more bytes than you indicate in this\nparameter, the function copies Buffer Size - 1 bytes into the buffer,\nplaces an ASCII NUL byte at the end of the buffer, and returns the\nbuffer size you must pass to get the entire value. For example, if the\nvalue is "123456" and the Buffer Size is 4, the function places "123"\ninto the buffer and returns 7. If you pass a negative number, the\nfunction copies the value to the buffer regardless of the number of\nbytes in the value. If you pass 0, you can pass VI_NULL for the\nCoercion Record buffer parameter. Default Value: None\n'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the channel name that is in the channel table at the index you\nspecify.\n'
                },
                'name': 'channelNameBuffer',
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
            'description': '\nThis function retrieves and then clears the IVI error information for\nthe session or the current execution thread. One exception exists: If\nthe buffer_size parameter is 0, the function does not clear the error\ninformation. By passing 0 for the buffer size, the caller can ascertain\nthe buffer size required to get the entire error description string and\nthen call the function again with a sufficiently large buffer. If the\nuser specifies a valid IVI session for the InstrumentHandle parameter,\nGet Error retrieves and then clears the error information for the\nsession. If the user passes VI_NULL for the InstrumentHandle parameter,\nthis function retrieves and then clears the error information for the\ncurrent execution thread. If the InstrumentHandle parameter is an\ninvalid session, the function does nothing and returns an error.\nNormally, the error information describes the first error that occurred\nsince the user last called niSwitch_GetError or niSwitch_ClearError.\n'
        },
        'is_error_handling': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the error code for the session or execution thread. If you pass\n0 for the Buffer Size, you can pass VI_NULL for this parameter.\n'
                },
                'name': 'code',
                'type': 'ViStatus'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the number of bytes in the ViChar array you specify for the\nDescription parameter. If the error description, including the\nterminating NUL byte, contains more bytes than you indicate in this\nparameter, the function copies buffer_size - 1 bytes into the buffer,\nplaces an ASCII NUL byte at the end of the buffer, and returns the\nbuffer size you must pass to get the entire value. For example, if the\nvalue is "123456" and the Buffer Size is 4, the function places "123"\ninto the buffer and returns 7. If you pass a negative number, the\nfunction copies the value to the buffer regardless of the number of\nbytes in the value. If you pass 0, you can pass VI_NULL for the\nDescription buffer parameter. Default Value: None\n'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the error description for the IVI session or execution thread.\nIf there is no description, the function returns an empty string. The\nbuffer must contain at least as many elements as the value you specify\nwith the Buffer Size parameter. If the error description, including the\nterminating NUL byte, contains more bytes than you indicate with the\nBuffer Size parameter, the function copies Buffer Size - 1 bytes into\nthe buffer, places an ASCII NUL byte at the end of the buffer, and\nreturns the buffer size you must pass to get the entire value. For\nexample, if the value is "123456" and the Buffer Size is 4, the function\nplaces "123" into the buffer and returns 7. If you pass 0 for the Buffer\nSize, you can pass VI_NULL for this parameter.\n'
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
    'GetPath': {
        'documentation': {
            'description': '\nReturns a string that identifies the explicit path created with\nniSwitch_Connect. Pass this string to niSwitch_SetPath to establish\nthe exact same path in future connections. In some cases, multiple paths\nare available between two channels. When you call niSwitch_Connect, the\ndriver selects an available path. With niSwitch_Connect, there is no\nguarantee that the driver selected path will always be the same path\nthrough the switch module. niSwitch_GetPath only returns those paths\nexplicitly created by niSwitch Connect Channels or niSwitch_SetPath.\nFor example, if you connect channels CH1 and CH3,and then channels CH2\nand CH3, an explicit path between channels CH1 and CH2 does not exist an\nerror is returned\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nInput one of the channel names of the desired path. Pass the other\nchannel name as the channel 2 parameter. Refer to Devices Overview for\nvalid channel names for the switch module. Examples of valid channel\nnames: ch0, com0, ab0, r1, c2, cjtemp Default value: ""\n'
                },
                'name': 'channel1',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nInput one of the channel names of the desired path. Pass the other\nchannel name as the channel 1 parameter. Refer to Devices Overview for\nvalid channel names for the switch module. Examples of valid channel\nnames: ch0, com0, ab0, r1, c2, cjtemp Default value: ""\n'
                },
                'name': 'channel2',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the number of bytes in the ViChar array you specify for the Path\nList parameter. If the current value of the attribute, including the\nterminating NULL byte, contains more bytes that you indicate in this\nparameter, the function copies Buffer Size - 1 bytes into the buffer,\nplaces an ASCII NULL byte at the end of the buffer, and returns the\nbuffer size you must pass to get the entire value. For example, if the\nvalue is "R1->C1" and the Buffer Size is 4, the function places "R1-"\ninto the buffer and returns 7. If you pass 0, you can pass VI_NULL for\nthe Path parameter. This enables you to find out the path size and to\nallocate the buffer of the appropriate size before calling this function\nagain.\n'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nA string composed of comma-separated paths between channel 1 and channel\n2. The first and last names in the path are the endpoints of the path.\nAll other channels in the path are configuration channels. Examples of\nreturned paths: ch0->com0, com0->ab0\n'
                },
                'name': 'path',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetRelayCount': {
        'documentation': {
            'description': '\nReturns the number of times the relay has changed from Closed to Open.\nRelay count is useful for tracking relay lifetime and usage. Call\nniSwitch_WaitForDebounce before niSwitch_GetRelayCount to ensure an\naccurate count. Refer to the Relay Count topic in the NI Switches Help\nto determine if the switch module supports relay counting.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nName of the relay. Default value: None Examples of valid relay names:\nch0, ab0, 1wire, hlselect Refer to Devices Overview for a list of valid\nrelay names for the switch module.\n'
                },
                'name': 'relayName',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The number of relay cycles.'
                },
                'name': 'relayCount',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetRelayName': {
        'documentation': {
            'description': '\nReturns the relay name string that is in the relay list at the specified\nindex. Use niSwitch_GetRelayName in a For Loop to get a complete list\nof valid relay names for the switch module. Use the Number of Relays\nattribute to determine the number of relays.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA 1-based index into the channel table. Default value: 1 Maximum value:\nValue of Channel Count attribute.\n'
                },
                'name': 'index',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the number of bytes in the ViChar array you specify for the Relay\nName Buffer parameter. If the relay name string, including the\nterminating NUL byte, contains more bytes than you indicate in this\nparameter, the function copies Buffer Size - 1 bytes into the buffer,\nplaces an ASCII NUL byte at the end of the buffer, and returns the\nbuffer size you must pass to get the entire value. For example, if the\nvalue is "123456" and the Buffer Size is 4, the function places "123"\ninto the buffer and returns 7. If you pass a negative number, the\nfunction copies the value to the buffer regardless of the number of\nbytes in the value. If you pass 0, you can pass VI_NULL for the\nCoercion Record buffer parameter. Default Value: None\n'
                },
                'name': 'relayNameBufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the relay name for the index you specify.'
                },
                'name': 'relayNameBuffer',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'relayNameBufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetRelayPosition': {
        'documentation': {
            'description': '\nReturns the relay position for the relay specified in the Relay Name\nparameter.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nName of the relay. Default value: None Examples of valid relay names:\nch0, ab0, 1wire, hlselect Refer to Devices Overview for a list of valid\nrelay names for the switch module.\n'
                },
                'name': 'relayName',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nIndicates whether the relay is open or closed. NISWITCH_VAL_OPEN 10\nNISWITCH_VAL_CLOSED 11\n'
                },
                'enum': 'RelayPosition',
                'name': 'relayPosition',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'InitWithTopology': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nReturns a session handle used to identify the switch in all subsequent\ninstrument driver calls and sets the topology of the switch.\nniSwitch_InitWithTopology creates a new IVI instrument driver session\nfor the switch specified in the resourceName parameter. The driver uses\nthe topology specified in the topology parameter and overrides the\ntopology specified in MAX. Note: When initializing an NI SwitchBlock\ndevice with topology, you must specify the toplogy created when you\nconfigured the device in MAX, using either\nNISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY or the toplogy string of the\ndevice. Refer to the Initializing with Toplogy for NI SwitchBlock\nDevices topic in the NI Switches Help for information about determining\nthe topology string of an NI SwitchBlock device. By default, the switch\nis reset to a known state. Enable simulation by specifying the topology\nand setting the simulate parameter to VI_TRUE.\n'
        },
        'method_name_for_documentation': '__init__',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nResource name of the switch module to initialize. Default value: None\nSyntax: Optional fields are shown in square brackets ([]). Configured in\nMAX Under Valid Syntax Devices and Interfaces DeviceName Traditional\nNI-DAQ Devices SCXI[chassis ID]::slot number PXI System PXI[bus\nnumber]::device number TIP: IVI logical names are also valid for the\nresource name. Default values for optional fields: chassis ID = 1 bus\nnumber = 0 Example resource names: Resource Name Description SC1Mod3\nNI-DAQmx module in chassis "SC1" slot 3 MySwitch NI-DAQmx module renamed\nto "MySwitch" SCXI1::3 Traditional NI-DAQ module in chassis 1, slot 3\nSCXI::3 Traditional NI-DAQ module in chassis 1, slot 3 PXI0::16 PXI bus\n0, device number 16 PXI::16 PXI bus 0, device number 16\n'
                },
                'name': 'resourceName',
                'type': 'ViRsrc'
            },
            {
                'default_value': '"Configured Topology"',
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the topology name you want to use for the switch you specify with\nResource Name parameter. You can also pass\nNISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY to use the last topology that\nwas configured for the device in MAX. Default Value:\nNISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY Valid Values:\nNISWITCH_TOPOLOGY_1127_1_WIRE_64X1_MUX\nNISWITCH_TOPOLOGY_1127_2_WIRE_32X1_MUX\nNISWITCH_TOPOLOGY_1127_2_WIRE_4X8_MATRIX\nNISWITCH_TOPOLOGY_1127_4_WIRE_16X1_MUX\nNISWITCH_TOPOLOGY_1127_INDEPENDENT\nNISWITCH_TOPOLOGY_1128_1_WIRE_64X1_MUX\nNISWITCH_TOPOLOGY_1128_2_WIRE_32X1_MUX\nNISWITCH_TOPOLOGY_1128_2_WIRE_4X8_MATRIX\nNISWITCH_TOPOLOGY_1128_4_WIRE_16X1_MUX\nNISWITCH_TOPOLOGY_1128_INDEPENDENT\nNISWITCH_TOPOLOGY_1129_2_WIRE_16X16_MATRIX\nNISWITCH_TOPOLOGY_1129_2_WIRE_8X32_MATRIX\nNISWITCH_TOPOLOGY_1129_2_WIRE_4X64_MATRIX\nNISWITCH_TOPOLOGY_1129_2_WIRE_DUAL_8X16_MATRIX\nNISWITCH_TOPOLOGY_1129_2_WIRE_DUAL_4X32_MATRIX\nNISWITCH_TOPOLOGY_1129_2_WIRE_QUAD_4X16_MATRIX\nNISWITCH_TOPOLOGY_1130_1_WIRE_256X1_MUX\nNISWITCH_TOPOLOGY_1130_1_WIRE_DUAL_128X1_MUX\nNISWITCH_TOPOLOGY_1130_1_WIRE_4X64_MATRIX\nNISWITCH_TOPOLOGY_1130_1_WIRE_8x32_MATRIX\nNISWITCH_TOPOLOGY_1130_1_WIRE_OCTAL_32X1_MUX\nNISWITCH_TOPOLOGY_1130_1_WIRE_QUAD_64X1_MUX\nNISWITCH_TOPOLOGY_1130_1_WIRE_SIXTEEN_16X1_MUX\nNISWITCH_TOPOLOGY_1130_2_WIRE_4X32_MATRIX\nNISWITCH_TOPOLOGY_1130_2_WIRE_128X1_MUX\nNISWITCH_TOPOLOGY_1130_2_WIRE_OCTAL_16X1_MUX\nNISWITCH_TOPOLOGY_1130_2_WIRE_QUAD_32X1_MUX\nNISWITCH_TOPOLOGY_1130_4_WIRE_64X1_MUX\nNISWITCH_TOPOLOGY_1130_4_WIRE_QUAD_16X1_MUX\nNISWITCH_TOPOLOGY_1130_INDEPENDENT NISWITCH_TOPOLOGY_1160_16_SPDT\nNISWITCH_TOPOLOGY_1161_8_SPDT\nNISWITCH_TOPOLOGY_1163R_OCTAL_4X1_MUX\nNISWITCH_TOPOLOGY_1166_16_DPDT NISWITCH_TOPOLOGY_1166_32_SPDT\nNISWITCH_TOPOLOGY_1167_INDEPENDENT\nNISWITCH_TOPOLOGY_1169_100_SPST NISWITCH_TOPOLOGY_1169_50_DPST\nNISWITCH_TOPOLOGY_1175_1_WIRE_196X1_MUX\nNISWITCH_TOPOLOGY_1175_2_WIRE_98X1_MUX\nNISWITCH_TOPOLOGY_1175_2_WIRE_95X1_MUX\nNISWITCH_TOPOLOGY_1190_QUAD_4X1_MUX\nNISWITCH_TOPOLOGY_1191_QUAD_4X1_MUX\nNISWITCH_TOPOLOGY_1192_8_SPDT NISWITCH_TOPOLOGY_1193_32X1_MUX\nNISWITCH_TOPOLOGY_1193_16X1_TERMINATED_MUX\nNISWITCH_TOPOLOGY_1193_DUAL_16X1_MUX\nNISWITCH_TOPOLOGY_1193_DUAL_8X1_TERMINATED_MUX\nNISWITCH_TOPOLOGY_1193_QUAD_8X1_MUX\nNISWITCH_TOPOLOGY_1193_QUAD_4X1_TERMINATED_MUX\nNISWITCH_TOPOLOGY_1193_INDEPENDENT\nNISWITCH_TOPOLOGY_1194_QUAD_4X1_MUX\nNISWITCH_TOPOLOGY_1195_QUAD_4X1_MUX\nNISWITCH_TOPOLOGY_2501_1_WIRE_48X1_MUX\nNISWITCH_TOPOLOGY_2501_1_WIRE_48X1_AMPLIFIED_MUX\nNISWITCH_TOPOLOGY_2501_2_WIRE_24X1_MUX\nNISWITCH_TOPOLOGY_2501_2_WIRE_24X1_AMPLIFIED_MUX\nNISWITCH_TOPOLOGY_2501_2_WIRE_DUAL_12X1_MUX\nNISWITCH_TOPOLOGY_2501_2_WIRE_QUAD_6X1_MUX\nNISWITCH_TOPOLOGY_2501_2_WIRE_4X6_MATRIX\nNISWITCH_TOPOLOGY_2501_4_WIRE_12X1_MUX\nNISWITCH_TOPOLOGY_2503_1_WIRE_48X1_MUX\nNISWITCH_TOPOLOGY_2503_2_WIRE_24X1_MUX\nNISWITCH_TOPOLOGY_2503_2_WIRE_DUAL_12X1_MUX\nNISWITCH_TOPOLOGY_2503_2_WIRE_QUAD_6X1_MUX\nNISWITCH_TOPOLOGY_2503_2_WIRE_4X6_MATRIX\nNISWITCH_TOPOLOGY_2503_4_WIRE_12X1_MUX\nNISWITCH_TOPOLOGY_2510_INDEPENDENT\nNISWITCH_TOPOLOGY_2512_INDEPENDENT\nNISWITCH_TOPOLOGY_2514_INDEPENDENT\nNISWITCH_TOPOLOGY_2515_INDEPENDENT NISWITCH_TOPOLOGY_2520_80_SPST\nNISWITCH_TOPOLOGY_2521_40_DPST NISWITCH_TOPOLOGY_2522_53_SPDT\nNISWITCH_TOPOLOGY_2523_26_DPDT\nNISWITCH_TOPOLOGY_2524_1_WIRE_128X1_MUX\nNISWITCH_TOPOLOGY_2524_1_WIRE_DUAL_64X1_MUX\nNISWITCH_TOPOLOGY_2524_1_WIRE_QUAD_32X1_MUX\nNISWITCH_TOPOLOGY_2524_1_WIRE_OCTAL_16X1_MUX\nNISWITCH_TOPOLOGY_2524_1_WIRE_SIXTEEN_8X1_MUX\nNISWITCH_TOPOLOGY_2525_2_WIRE_64X1_MUX\nNISWITCH_TOPOLOGY_2525_2_WIRE_DUAL_32X1_MUX\nNISWITCH_TOPOLOGY_2525_2_WIRE_QUAD_16X1_MUX\nNISWITCH_TOPOLOGY_2525_2_WIRE_OCTAL_8X1_MUX\nNISWITCH_TOPOLOGY_2525_2_WIRE_SIXTEEN_4X1_MUX\nNISWITCH_TOPOLOGY_2526_1_WIRE_158X1_MUX\nNISWITCH_TOPOLOGY_2526_2_WIRE_79X1_MUX\nNISWITCH_TOPOLOGY_2527_1_WIRE_64X1_MUX\nNISWITCH_TOPOLOGY_2527_1_WIRE_DUAL_32X1_MUX\nNISWITCH_TOPOLOGY_2527_2_WIRE_32X1_MUX\nNISWITCH_TOPOLOGY_2527_2_WIRE_DUAL_16X1_MUX\nNISWITCH_TOPOLOGY_2527_4_WIRE_16X1_MUX\nNISWITCH_TOPOLOGY_2527_INDEPENDENT\nNISWITCH_TOPOLOGY_2529_2_WIRE_DUAL_4X16_MATRIX\nNISWITCH_TOPOLOGY_2529_2_WIRE_8X16_MATRIX\nNISWITCH_TOPOLOGY_2529_2_WIRE_4X32_MATRIX\nNISWITCH_TOPOLOGY_2530_1_WIRE_128X1_MUX\nNISWITCH_TOPOLOGY_2530_1_WIRE_DUAL_64X1_MUX\nNISWITCH_TOPOLOGY_2530_1_WIRE_4x32_MATRIX\nNISWITCH_TOPOLOGY_2530_1_WIRE_8x16_MATRIX\nNISWITCH_TOPOLOGY_2530_1_WIRE_OCTAL_16X1_MUX\nNISWITCH_TOPOLOGY_2530_1_WIRE_QUAD_32X1_MUX\nNISWITCH_TOPOLOGY_2530_2_WIRE_4x16_MATRIX\nNISWITCH_TOPOLOGY_2530_2_WIRE_64X1_MUX\nNISWITCH_TOPOLOGY_2530_2_WIRE_DUAL_32X1_MUX\nNISWITCH_TOPOLOGY_2530_2_WIRE_QUAD_16X1_MUX\nNISWITCH_TOPOLOGY_2530_4_WIRE_32X1_MUX\nNISWITCH_TOPOLOGY_2530_4_WIRE_DUAL_16X1_MUX\nNISWITCH_TOPOLOGY_2530_INDEPENDENT\nNISWITCH_TOPOLOGY_2531_1_WIRE_4X128_MATRIX\nNISWITCH_TOPOLOGY_2531_1_WIRE_8X64_MATRIX\nNISWITCH_TOPOLOGY_2531_1_WIRE_DUAL_4X64_MATRIX\nNISWITCH_TOPOLOGY_2531_1_WIRE_DUAL_8X32_MATRIX\nNISWITCH_TOPOLOGY_2531_2_WIRE_4X64_MATRIX\nNISWITCH_TOPOLOGY_2531_2_WIRE_8X32_MATRIX\nNISWITCH_TOPOLOGY_2532_1_WIRE_16X32_MATRIX\nNISWITCH_TOPOLOGY_2532_1_WIRE_4X128_MATRIX\nNISWITCH_TOPOLOGY_2532_1_WIRE_8X64_MATRIX\nNISWITCH_TOPOLOGY_2532_1_WIRE_DUAL_16X16_MATRIX\nNISWITCH_TOPOLOGY_2532_1_WIRE_DUAL_4X64_MATRIX\nNISWITCH_TOPOLOGY_2532_1_WIRE_DUAL_8X32_MATRIX\nNISWITCH_TOPOLOGY_2532_1_WIRE_SIXTEEN_2X16_MATRIX\nNISWITCH_TOPOLOGY_2532_2_WIRE_16X16_MATRIX\nNISWITCH_TOPOLOGY_2532_2_WIRE_4X64_MATRIX\nNISWITCH_TOPOLOGY_2532_2_WIRE_8X32_MATRIX\nNISWITCH_TOPOLOGY_2532_2_WIRE_DUAL_4X32_MATRIX\nNISWITCH_TOPOLOGY_2533_1_WIRE_4X64_MATRIX\nNISWITCH_TOPOLOGY_2534_1_WIRE_8X32_MATRIX\nNISWITCH_TOPOLOGY_2535_1_WIRE_4X136_MATRIX\nNISWITCH_TOPOLOGY_2536_1_WIRE_8X68_MATRIX\nNISWITCH_TOPOLOGY_2540_1_WIRE_8X9_MATRIX\nNISWITCH_TOPOLOGY_2541_1_WIRE_8X12_MATRIX\nNISWITCH_TOPOLOGY_2542_QUAD_2X1_TERMINATED_MUX\nNISWITCH_TOPOLOGY_2543_DUAL_4X1_TERMINATED_MUX\nNISWITCH_TOPOLOGY_2544_8X1_TERMINATED_MUX\nNISWITCH_TOPOLOGY_2545_4X1_TERMINATED_MUX\nNISWITCH_TOPOLOGY_2546_DUAL_4X1_MUX\nNISWITCH_TOPOLOGY_2547_8X1_MUX NISWITCH_TOPOLOGY_2548_4_SPDT\nNISWITCH_TOPOLOGY_2549_TERMINATED_2_SPDT\nNISWITCH_TOPOLOGY_2554_4X1_MUX\nNISWITCH_TOPOLOGY_2555_4X1_TERMINATED_MUX\nNISWITCH_TOPOLOGY_2556_DUAL_4X1_MUX\nNISWITCH_TOPOLOGY_2557_8X1_MUX NISWITCH_TOPOLOGY_2558_4_SPDT\nNISWITCH_TOPOLOGY_2559_TERMINATED_2_SPDT\nNISWITCH_TOPOLOGY_2564_16_SPST NISWITCH_TOPOLOGY_2564_8_DPST\nNISWITCH_TOPOLOGY_2565_16_SPST NISWITCH_TOPOLOGY_2566_16_SPDT\nNISWITCH_TOPOLOGY_2566_8_DPDT NISWITCH_TOPOLOGY_2567_INDEPENDENT\nNISWITCH_TOPOLOGY_2568_15_DPST NISWITCH_TOPOLOGY_2568_31_SPST\nNISWITCH_TOPOLOGY_2569_100_SPST NISWITCH_TOPOLOGY_2569_50_DPST\nNISWITCH_TOPOLOGY_2570_20_DPDT NISWITCH_TOPOLOGY_2570_40_SPDT\nNISWITCH_TOPOLOGY_2571_66_SPDT\nNISWITCH_TOPOLOGY_2575_1_WIRE_196X1_MUX\nNISWITCH_TOPOLOGY_2575_2_WIRE_98X1_MUX\nNISWITCH_TOPOLOGY_2575_2_WIRE_95X1_MUX\nNISWITCH_TOPOLOGY_2576_2_WIRE_64X1_MUX\nNISWITCH_TOPOLOGY_2576_2_WIRE_DUAL_32X1_MUX\nNISWITCH_TOPOLOGY_2576_2_WIRE_OCTAL_8X1_MUX\nNISWITCH_TOPOLOGY_2576_2_WIRE_QUAD_16X1_MUX\nNISWITCH_TOPOLOGY_2576_2_WIRE_SIXTEEN_4X1_MUX\nNISWITCH_TOPOLOGY_2576_INDEPENDENT\nNISWITCH_TOPOLOGY_2584_1_WIRE_12X1_MUX\nNISWITCH_TOPOLOGY_2584_1_WIRE_DUAL_6X1_MUX\nNISWITCH_TOPOLOGY_2584_2_WIRE_6X1_MUX\nNISWITCH_TOPOLOGY_2584_INDEPENDENT\nNISWITCH_TOPOLOGY_2585_1_WIRE_10X1_MUX\nNISWITCH_TOPOLOGY_2586_10_SPST NISWITCH_TOPOLOGY_2586_5_DPST\nNISWITCH_TOPOLOGY_2590_4X1_MUX NISWITCH_TOPOLOGY_2591_4X1_MUX\nNISWITCH_TOPOLOGY_2593_16X1_MUX\nNISWITCH_TOPOLOGY_2593_8X1_TERMINATED_MUX\nNISWITCH_TOPOLOGY_2593_DUAL_8X1_MUX\nNISWITCH_TOPOLOGY_2593_DUAL_4X1_TERMINATED_MUX\nNISWITCH_TOPOLOGY_2593_INDEPENDENT NISWITCH_TOPOLOGY_2594_4X1_MUX\nNISWITCH_TOPOLOGY_2595_4X1_MUX\nNISWITCH_TOPOLOGY_2596_DUAL_6X1_MUX\nNISWITCH_TOPOLOGY_2597_6X1_TERMINATED_MUX\nNISWITCH_TOPOLOGY_2598_DUAL_TRANSFER\nNISWITCH_TOPOLOGY_2599_2_SPDT NISWITCH_TOPOLOGY_2720_INDEPENDENT\nNISWITCH_TOPOLOGY_2722_INDEPENDENT\nNISWITCH_TOPOLOGY_2725_INDEPENDENT\nNISWITCH_TOPOLOGY_2727_INDEPENDENT\nNISWITCH_TOPOLOGY_2737_2_WIRE_4X64_MATRIX\nNISWITCH_TOPOLOGY_2738_2_WIRE_8X32_MATRIX\nNISWITCH_TOPOLOGY_2739_2_WIRE_16X16_MATRIX\nNISWITCH_TOPOLOGY_2746_QUAD_4X1_MUX\nNISWITCH_TOPOLOGY_2747_DUAL_8X1_MUX\nNISWITCH_TOPOLOGY_2748_16X1_MUX\nNISWITCH_TOPOLOGY_2790_INDEPENDENT\nNISWITCH_TOPOLOGY_2796_DUAL_6X1_MUX\nNISWITCH_TOPOLOGY_2797_6X1_TERMINATED_MUX\nNISWITCH_TOPOLOGY_2798_DUAL_TRANSFER\nNISWITCH_TOPOLOGY_2799_2_SPDT\n'
                },
                'name': 'topology',
                'type': 'ViConstString'
            },
            {
                'default_value': False,
                'direction': 'in',
                'documentation': {
                    'description': "\nEnables simulation of the switch module specified in the resource name\nparameter. Valid Values: VI_TRUE - simulate VI_FALSE - Don't simulate\n(Default Value)\n"
                },
                'name': 'simulate',
                'type': 'ViBoolean'
            },
            {
                'default_value': False,
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies whether to reset the switch module during the initialization\nprocess. Valid Values: VI_TRUE - Reset Device (Default Value) VI_FALSE\n- Currently unsupported. The device will not reset.\n'
                },
                'name': 'resetDevice',
                'type': 'ViBoolean'
            },
            {
                'default_value': '""',
                'direction': 'out',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'InitiateScan': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nCommits the configured scan list and trigger settings to hardware and\ninitiates the scan. If niSwitch Commit was called earlier, niSwitch\nInitiate Scan only initiates the scan and returns immediately. Once the\nscanning operation begins, you cannot perform any other operation other\nthan GetAttribute, AbortScan, or SendSoftwareTrigger. All other\nfunctions return NISWITCH_ERROR_SCAN_IN_PROGRESS. To stop the\nscanning operation, To stop the scanning operation, call\nniSwitch_AbortScan.\n'
        },
        'method_name_for_documentation': 'initiate',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'LockSession': {
        'documentation': {
            'description': "\nThis function obtains a multithread lock on the instrument session.\nBefore it does so, it waits until all other execution threads have\nreleased their locks on the instrument session. Other threads might have\nobtained a lock on this session in the following ways: - The user's\napplication called niSwitch_LockSession. - A call to the instrument\ndriver locked the session. - A call to the IVI engine locked the\nsession. After your call to niSwitch_LockSession returns successfully,\nno other threads can access the instrument session until you call\nniSwitch_UnlockSession. Use niSwitch_LockSession and\nniSwitch_UnlockSession around a sequence of calls to instrument driver\nfunctions if you require that the instrument retain its settings through\nthe end of the sequence. You can safely make nested calls to\nniSwitch_LockSession within the same thread. To completely unlock the\nsession, you must balance each call to niSwitch_LockSession with a call\nto niSwitch_UnlockSession. If, however, you use the Caller Has Lock\nparameter in all calls to niSwitch_LockSession and\nniSwitch_UnlockSession within a function, the IVI Library locks the\nsession only once within the function regardless of the number of calls\nyou make to niSwitch_LockSession. This allows you to call\nniSwitch_UnlockSession just once at the end of the function.\n"
        },
        'method_templates': [
            {
                'documentation_filename': 'lock',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'lock'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThis parameter serves as a convenience. If you do not want to use this\nparameter, pass VI_NULL. Use this parameter in complex functions to\nkeep track of whether you obtain a lock and therefore need to unlock the\nsession. Pass the address of a local ViBoolean variable. In the\ndeclaration of the local variable, initialize it to VI_FALSE. Pass the\naddress of the same local variable to any other calls you make to\nniSwitch_LockSession or niSwitch_UnlockSession in the same function.\nThe parameter is an input/output parameter. niSwitch_LockSession and\nniSwitch_UnlockSession each inspect the current value and take the\nfollowing actions: - If the value is VI_TRUE, niSwitch_LockSession\ndoes not lock the session again. If the value is VI_FALSE,\nniSwitch_LockSession obtains the lock and sets the value of the\nparameter to VI_TRUE. - If the value is VI_FALSE,\nniSwitch_UnlockSession does not attempt to unlock the session. If the\nvalue is VI_TRUE, niSwitch_UnlockSession releases the lock and sets\nthe value of the parameter to VI_FALSE. Thus, you can, call\nniSwitch_UnlockSession at the end of your function without worrying\nabout whether you actually have the lock. Example: ViStatus TestFunc\n(ViSession vi, ViInt32 flags) { ViStatus error = VI_SUCCESS; ViBoolean\nhaveLock = VI_FALSE; if (flags & BIT_1) { viCheckErr(\nniSwitch_LockSession(vi, &haveLock;)); viCheckErr( TakeAction1(vi)); if\n(flags & BIT_2) { viCheckErr( niSwitch_UnlockSession(vi, &haveLock;));\nviCheckErr( TakeAction2(vi)); viCheckErr( niSwitch_LockSession(vi,\n&haveLock;); } if (flags & BIT_3) viCheckErr( TakeAction3(vi)); }\nError: /\\* At this point, you cannot really be sure that you have the\nlock. Fortunately, the haveLock variable takes care of that for you. \\*/\nniSwitch_UnlockSession(vi, &haveLock;); return error; }\n'
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
    'RelayControl': {
        'documentation': {
            'description': '\nControls individual relays of the switch. When controlling individual\nrelays, the protection offered by setting the usage of source channels\nand configuration channels, and by enabling or disabling analog bus\nsharing on the NI SwitchBlock, does not apply. Refer to the device book\nfor your switch in the NI Switches Help to determine if the switch\nsupports individual relay control.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nName of the relay. Default value: None Examples of valid relay names:\nch0, ab0, 1wire, hlselect Refer to Devices Overview for a list of valid\nrelay names for the switch module.\n'
                },
                'name': 'relayName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies whether to open or close a given relay. Default value: Relay\nClose Defined values: NISWITCH_VAL_OPEN_RELAY\nNISWITCH_VAL_CLOSE_RELAY (Default Value)\n'
                },
                'enum': 'RelayAction',
                'name': 'relayAction',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ResetWithDefaults': {
        'documentation': {
            'description': '\nResets the switch module and applies initial user specified settings\nfrom the logical name used to initialize the session. If the session was\ncreated without a logical name, this function is equivalent to\nniSwitch_reset.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'RouteScanAdvancedOutput': {
        'documentation': {
            'description': '\nRoutes the scan advanced output trigger from a trigger bus line (TTLx)\nto the front or rear connector.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe scan advanced trigger destination. Valid locations are the\nNISWITCH_VAL_FRONTCONNECTOR and NISWITCH_VAL_REARCONNECTOR. Default\nvalue: NISWITCH_VAL_FRONTCONNECTOR\n'
                },
                'enum': 'ScanAdvancedOutput',
                'name': 'scanAdvancedOutputConnector',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe trigger line to route the scan advanced output trigger from the\nfront or rear connector. Select NISWITCH_VAL_NONE to break an existing\nroute. Default value: None Valid Values: NISWITCH_VAL_NONE\nNISWITCH_VAL_TTL0 NISWITCH_VAL_TTL1 NISWITCH_VAL_TTL2\nNISWITCH_VAL_TTL3 NISWITCH_VAL_TTL4 NISWITCH_VAL_TTL5\nNISWITCH_VAL_TTL6 NISWITCH_VAL_TTL7\n'
                },
                'enum': 'ScanAdvancedOutput',
                'name': 'scanAdvancedOutputBusLine',
                'type': 'ViInt32'
            },
            {
                'default_value': False,
                'direction': 'in',
                'documentation': {
                    'description': '\nIf VI_TRUE, inverts the input trigger signal from falling to rising or\nvice versa. Default value: VI_FALSE\n'
                },
                'name': 'invert',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'RouteTriggerInput': {
        'documentation': {
            'description': '\nRoutes the input trigger from the front or rear connector to a trigger\nbus line (TTLx). To disconnect the route, call this function again and\nspecify None for trigger bus line parameter.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe location of the input trigger source on the switch module. Valid\nlocations are the NISWITCH_VAL_FRONTCONNECTOR and\nNISWITCH_VAL_REARCONNECTOR. Default value:\nNISWITCH_VAL_FRONTCONNECTOR\n'
                },
                'enum': 'TriggerInput',
                'name': 'triggerInputConnector',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe trigger line to route the input trigger. Select NISWITCH_VAL_NONE\nto break an existing route. Default value: None Valid Values:\nNISWITCH_VAL_NONE NISWITCH_VAL_TTL0 NISWITCH_VAL_TTL1\nNISWITCH_VAL_TTL2 NISWITCH_VAL_TTL3 NISWITCH_VAL_TTL4\nNISWITCH_VAL_TTL5 NISWITCH_VAL_TTL6 NISWITCH_VAL_TTL7\n'
                },
                'enum': 'TriggerInput',
                'name': 'triggerInputBusLine',
                'type': 'ViInt32'
            },
            {
                'default_value': False,
                'direction': 'in',
                'documentation': {
                    'description': '\nIf VI_TRUE, inverts the input trigger signal from falling to rising or\nvice versa. Default value: VI_FALSE\n'
                },
                'name': 'invert',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'SendSoftwareTrigger': {
        'documentation': {
            'description': '\nSends a software trigger to the switch module specified in the NI-SWITCH\nsession. When the trigger input is set to NISWITCH_VAL_SOFTWARE_TRIG\nthrough either the niSwitch_ConfigureScanTrigger or the\nNISWITCH_ATTR_TRIGGER_INPUT attribute, the scan does not proceed from\na semi-colon (wait for trigger) until niSwitch_SendSoftwareTrigger is\ncalled.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
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
            'description': '\nThis function sets the value of a ViBoolean attribute. This is a\nlow-level function that you can use to set the values of\ninstrument-specific attributes and inherent IVI attributes. If the\nattribute represents an instrument state, this function performs\ninstrument I/O in the following cases: - State caching is disabled for\nthe entire session or for the particular attribute. - State caching is\nenabled and the currently cached value is invalid or is different than\nthe value you specify. This instrument driver contains high-level\nfunctions that set most of the instrument attributes. It is best to use\nthe high-level driver functions as much as possible. They handle order\ndependencies and multithread locking for you. In addition, they perform\nstatus checking only after setting all of the attributes. In contrast,\nwhen you set multiple attributes using the SetAttribute functions, the\nfunctions check the instrument status after each call. Also, when state\ncaching is enabled, the high-level functions that configure multiple\nattributes perform instrument I/O only for the attributes whose value\nyou change. Thus, you can safely call the high-level functions without\nthe penalty of redundant instrument I/O.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSome attributes are unique per channel. For these, pass the name of the\nchannel. Other attributes are unique per switch device. Pass VI_NULL or\nan empty string for this parameter. Default Value: ""\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the ID of an attribute. From the function panel window, you can use\nthis control as follows. - Click on the control or press , , or , to\ndisplay a dialog box containing a hierarchical list of the available\nattributes. Attributes whose value cannot be set are dim. Help text is\nshown for each attribute. Select an attribute by double-clicking on it\nor by selecting it and then pressing . Read-only attributes appear dim\nin the list box. If you select a read-only attribute, an error message\nappears. A ring control at the top of the dialog box allows you to see\nall IVI attributes or only the attributes of the ViInt32 type. If you\nchoose to see all IVI attributes, the data types appear to the right of\nthe attribute names in the list box. The data types that are not\nconsistent with this function are dim. If you select an attribute data\ntype that is dim, LabWindows/CVI transfers you to the function panel for\nthe corresponding function that is consistent with the data type. - If\nyou want to enter a variable name, press to change this ring control to\na manual input box. - If the attribute in this ring control has\nconstants as valid values, you can view the constants by moving to the\nAttribute Value control and pressing .\n'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the value to which you want to set the attribute. From the function\npanel window, you can use this control as follows. - If the attribute\ncurrently showing in the Attribute ID ring control has constants as\nvalid values, you can view a list of the constants by pressing on this\ncontrol. Select a value by double-clicking on it or by selecting it and\nthen pressing . Note: Some of the values might not be valid depending on\nthe current settings of the instrument session. Default Value: none\n'
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
            'description': '\nThis function sets the value of a ViInt32 attribute. This is a low-level\nfunction that you can use to set the values of instrument-specific\nattributes and inherent IVI attributes. If the attribute represents an\ninstrument state, this function performs instrument I/O in the following\ncases: - State caching is disabled for the entire session or for the\nparticular attribute. - State caching is enabled and the currently\ncached value is invalid or is different than the value you specify. This\ninstrument driver contains high-level functions that set most of the\ninstrument attributes. It is best to use the high-level driver functions\nas much as possible. They handle order dependencies and multithread\nlocking for you. In addition, they perform status checking only after\nsetting all of the attributes. In contrast, when you set multiple\nattributes using the SetAttribute functions, the functions check the\ninstrument status after each call. Also, when state caching is enabled,\nthe high-level functions that configure multiple attributes perform\ninstrument I/O only for the attributes whose value you change. Thus, you\ncan safely call the high-level functions without the penalty of\nredundant instrument I/O.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSome attributes are unique per channel. For these, pass the name of the\nchannel. Other attributes are unique per switch device. Pass VI_NULL or\nan empty string for this parameter. Default Value: ""\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the ID of an attribute. From the function panel window, you can use\nthis control as follows. - Click on the control or press , , or , to\ndisplay a dialog box containing a hierarchical list of the available\nattributes. Attributes whose value cannot be set are dim. Help text is\nshown for each attribute. Select an attribute by double-clicking on it\nor by selecting it and then pressing . Read-only attributes appear dim\nin the list box. If you select a read-only attribute, an error message\nappears. A ring control at the top of the dialog box allows you to see\nall IVI attributes or only the attributes of the ViInt32 type. If you\nchoose to see all IVI attributes, the data types appear to the right of\nthe attribute names in the list box. The data types that are not\nconsistent with this function are dim. If you select an attribute data\ntype that is dim, LabWindows/CVI transfers you to the function panel for\nthe corresponding function that is consistent with the data type. - If\nyou want to enter a variable name, press to change this ring control to\na manual input box. - If the attribute in this ring control has\nconstants as valid values, you can view the constants by moving to the\nAttribute Value control and pressing .\n'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the value to which you want to set the attribute. From the function\npanel window, you can use this control as follows. - If the attribute\ncurrently showing in the Attribute ID ring control has constants as\nvalid values, you can view a list of the constants by pressing on this\ncontrol. Select a value by double-clicking on it or by selecting it and\nthen pressing . Note: Some of the values might not be valid depending on\nthe current settings of the instrument session. Default Value: none\n'
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
            'description': '\nThis function sets the value of a ViReal64 attribute. This is a\nlow-level function that you can use to set the values of\ninstrument-specific attributes and inherent IVI attributes. If the\nattribute represents an instrument state, this function performs\ninstrument I/O in the following cases: - State caching is disabled for\nthe entire session or for the particular attribute. - State caching is\nenabled and the currently cached value is invalid or is different than\nthe value you specify. This instrument driver contains high-level\nfunctions that set most of the instrument attributes. It is best to use\nthe high-level driver functions as much as possible. They handle order\ndependencies and multithread locking for you. In addition, they perform\nstatus checking only after setting all of the attributes. In contrast,\nwhen you set multiple attributes using the SetAttribute functions, the\nfunctions check the instrument status after each call. Also, when state\ncaching is enabled, the high-level functions that configure multiple\nattributes perform instrument I/O only for the attributes whose value\nyou change. Thus, you can safely call the high-level functions without\nthe penalty of redundant instrument I/O.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSome attributes are unique per channel. For these, pass the name of the\nchannel. Other attributes are unique per switch device. Pass VI_NULL or\nan empty string for this parameter. Default Value: ""\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the ID of an attribute. From the function panel window, you can use\nthis control as follows. - Click on the control or press , , or , to\ndisplay a dialog box containing a hierarchical list of the available\nattributes. Attributes whose value cannot be set are dim. Help text is\nshown for each attribute. Select an attribute by double-clicking on it\nor by selecting it and then pressing . Read-only attributes appear dim\nin the list box. If you select a read-only attribute, an error message\nappears. A ring control at the top of the dialog box allows you to see\nall IVI attributes or only the attributes of the ViInt32 type. If you\nchoose to see all IVI attributes, the data types appear to the right of\nthe attribute names in the list box. The data types that are not\nconsistent with this function are dim. If you select an attribute data\ntype that is dim, LabWindows/CVI transfers you to the function panel for\nthe corresponding function that is consistent with the data type. - If\nyou want to enter a variable name, press to change this ring control to\na manual input box. - If the attribute in this ring control has\nconstants as valid values, you can view the constants by moving to the\nAttribute Value control and pressing .\n'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the value to which you want to set the attribute. From the function\npanel window, you can use this control as follows. - If the attribute\ncurrently showing in the Attribute ID ring control has constants as\nvalid values, you can view a list of the constants by pressing on this\ncontrol. Select a value by double-clicking on it or by selecting it and\nthen pressing . Note: Some of the values might not be valid depending on\nthe current settings of the instrument session. Default Value: none\n'
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
            'description': '\nThis function sets the value of a ViString attribute. This is a\nlow-level function that you can use to set the values of\ninstrument-specific attributes and inherent IVI attributes. If the\nattribute represents an instrument state, this function performs\ninstrument I/O in the following cases: - State caching is disabled for\nthe entire session or for the particular attribute. - State caching is\nenabled and the currently cached value is invalid or is different than\nthe value you specify. This instrument driver contains high-level\nfunctions that set most of the instrument attributes. It is best to use\nthe high-level driver functions as much as possible. They handle order\ndependencies and multithread locking for you. In addition, they perform\nstatus checking only after setting all of the attributes. In contrast,\nwhen you set multiple attributes using the SetAttribute functions, the\nfunctions check the instrument status after each call. Also, when state\ncaching is enabled, the high-level functions that configure multiple\nattributes perform instrument I/O only for the attributes whose value\nyou change. Thus, you can safely call the high-level functions without\nthe penalty of redundant instrument I/O.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSome attributes are unique per channel. For these, pass the name of the\nchannel. Other attributes are unique per switch device. Pass VI_NULL or\nan empty string for this parameter. Default Value: ""\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the ID of an attribute. From the function panel window, you can use\nthis control as follows. - Click on the control or press , , or , to\ndisplay a dialog box containing a hierarchical list of the available\nattributes. Attributes whose value cannot be set are dim. Help text is\nshown for each attribute. Select an attribute by double-clicking on it\nor by selecting it and then pressing . Read-only attributes appear dim\nin the list box. If you select a read-only attribute, an error message\nappears. A ring control at the top of the dialog box allows you to see\nall IVI attributes or only the attributes of the ViInt32 type. If you\nchoose to see all IVI attributes, the data types appear to the right of\nthe attribute names in the list box. The data types that are not\nconsistent with this function are dim. If you select an attribute data\ntype that is dim, LabWindows/CVI transfers you to the function panel for\nthe corresponding function that is consistent with the data type. - If\nyou want to enter a variable name, press to change this ring control to\na manual input box. - If the attribute in this ring control has\nconstants as valid values, you can view the constants by moving to the\nAttribute Value control and pressing .\n'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the value to which you want to set the attribute. From the function\npanel window, you can use this control as follows. - If the attribute\ncurrently showing in the Attribute ID ring control has constants as\nvalid values, you can view a list of the constants by pressing on this\ncontrol. Select a value by double-clicking on it or by selecting it and\nthen pressing . Note: Some of the values might not be valid depending on\nthe current settings of the instrument session. Default Value: none\n'
                },
                'name': 'attributeValue',
                'type': 'ViString'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetPath': {
        'documentation': {
            'description': '\nConnects two channels by specifying an explicit path in the path list\nparameter. niSwitch_SetPath is particularly useful where path\nrepeatability is important, such as in calibrated signal paths. If this\nis not necessary, use niSwitch_Connect.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA string composed of comma-separated paths between channel 1 and channel\n2. The first and last names in the path are the endpoints of the path.\nEvery other channel in the path are configuration channels. Example of a\nvalid path list string: ch0->com0, com0->ab0. In this example, com0 is a\nconfiguration channel. Default value: None Obtain the path list for a\npreviously created path with niSwitch_GetPath.\n'
                },
                'name': 'pathList',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'UnlockSession': {
        'documentation': {
            'description': '\nThis function releases a lock that you acquired on an instrument session\nusing niSwitch_LockSession. Refer to niSwitch_LockSession for\nadditional information on session locks.\n'
        },
        'method_templates': [
            {
                'documentation_filename': 'unlock',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'unlock'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThis parameter serves as a convenience. If you do not want to use this\nparameter, pass VI_NULL. Use this parameter in complex functions to\nkeep track of whether you obtain a lock and therefore need to unlock the\nsession. Pass the address of a local ViBoolean variable. In the\ndeclaration of the local variable, initialize it to VI_FALSE. Pass the\naddress of the same local variable to any other calls you make to\nniSwitch_LockSession or niSwitch_UnlockSession in the same function.\nThe parameter is an input/output parameter. niSwitch_LockSession and\nniSwitch_UnlockSession each inspect the current value and take the\nfollowing actions: - If the value is VI_TRUE, niSwitch_LockSession\ndoes not lock the session again. If the value is VI_FALSE,\nniSwitch_LockSession obtains the lock and sets the value of the\nparameter to VI_TRUE. - If the value is VI_FALSE,\nniSwitch_UnlockSession does not attempt to unlock the session. If the\nvalue is VI_TRUE, niSwitch_UnlockSession releases the lock and sets\nthe value of the parameter to VI_FALSE. Thus, you can, call\nniSwitch_UnlockSession at the end of your function without worrying\nabout whether you actually have the lock. Example: ViStatus TestFunc\n(ViSession vi, ViInt32 flags) { ViStatus error = VI_SUCCESS; ViBoolean\nhaveLock = VI_FALSE; if (flags & BIT_1) { viCheckErr(\nniSwitch_LockSession(vi, &haveLock;)); viCheckErr( TakeAction1(vi)); if\n(flags & BIT_2) { viCheckErr( niSwitch_UnlockSession(vi, &haveLock;));\nviCheckErr( TakeAction2(vi)); viCheckErr( niSwitch_LockSession(vi,\n&haveLock;); } if (flags & BIT_3) viCheckErr( TakeAction3(vi)); }\nError: /\\* At this point, you cannot really be sure that you have the\nlock. Fortunately, the haveLock variable takes care of that for you. \\*/\nniSwitch_UnlockSession(vi, &haveLock;); return error; }\n'
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
    'WaitForDebounce': {
        'documentation': {
            'description': '\nPauses until all created paths have settled. If the time you specify\nwith the Maximum Time (ms) parameter elapsed before the switch paths\nhave settled, this function returns the\nNISWITCH_ERROR_MAX_TIME_EXCEEDED error.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': 'hightime.timedelta(milliseconds=5000)',
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the maximum length of time to wait for all relays in the\nswitch module to activate or deactivate. If the specified time elapses\nbefore all relays active or deactivate, a timeout error is returned.\nDefault Value:5000 ms\n'
                },
                'name': 'maximumTimeMs',
                'python_api_converter_name': 'convert_timedelta_to_milliseconds_int32',
                'type': 'ViInt32',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or int in milliseconds'
            }
        ],
        'returns': 'ViStatus'
    },
    'WaitForScanComplete': {
        'documentation': {
            'description': '\nPauses until the switch module stops scanning or the maximum time has\nelapsed and returns a timeout error. If the time you specify with the\nMaximum Time (ms) parameter elapsed before the scanning operation has\nfinished, this function returns the NISWITCH_ERROR_MAX_TIME_EXCEEDED\nerror.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': 'hightime.timedelta(milliseconds=5000)',
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the maximum length of time to wait for the switch module to\nstop scanning. If the specified time elapses before the scan ends,\nNISWITCH_ERROR_MAX_TIME_EXCEEDED error is returned. Default\nValue:5000 ms\n'
                },
                'name': 'maximumTimeMs',
                'python_api_converter_name': 'convert_timedelta_to_milliseconds_int32',
                'type': 'ViInt32',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or int in milliseconds'
            }
        ],
        'returns': 'ViStatus'
    },
    'close': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nTerminates the NI-SWITCH session and all of its attributes and\ndeallocates any memory resources the driver uses. Notes: (1) You must\nunlock the session before calling niSwitch_close. (2) After calling\nniSwitch_close, you cannot use the instrument driver again until you\ncall niSwitch_init or niSwitch_InitWithOptions.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
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
            'description': '\nConverts an error code returned by NI-SWITCH into a user-readable\nstring. Generally this information is supplied in error out of any\nNI-SWITCH VI. Use niSwitch_error_message for a static lookup of an\nerror code description.\n'
        },
        'is_error_handling': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nStatus code returned by any NI-SWITCH function. Default Value: 0\n(VI_SUCCESS)\n'
                },
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe error information formatted into a string. You must pass a ViChar\narray with at least 256 bytes.\n'
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
            'description': '\nVerifies that the driver can communicate with the switch module.\n\nRaises `SelfTestError` on self test failure. Attributes on exception object:\n\n- code - failure code from driver\n- message - status message from driver\n',
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
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_self_test'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'A particular NI-SWITCH session established with niSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init and used for all subsequent NI-SWITCH calls.'
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
            'description': '\nDisconnects all created paths and returns the switch module to the state\nat initialization. Configuration channel and source channel settings\nremain unchanged.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
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
            'description': 'Verifies that the driver can communicate with the switch module.'
        },
        'method_name_for_documentation': 'self_test',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Value returned from the switch device self-test. Passed 0 Failed 1'
                },
                'name': 'selfTestResult',
                'type': 'ViInt16'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nSelf-test response string from the switch device. You must pass a ViChar\narray with at least 256 bytes.\n'
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
