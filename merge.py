import re
import pprint

functions = {

    #### Init / Close

    'InitWithOptions': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'resourceName',
                'type': 'ViString',
                'documentation': {
                    'caution': 'This is just some string.',
                    'description': 'Contains the **resource\_name** of the device to initialize.',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'idQuery',
                'type': 'ViBoolean',
                'documentation': {
                    'description': 'NI-FAKE is probably not needed.',
                    'table_body': [['VI\\_TRUE (default)', '1', 'Perform ID Query'], ['VI\\_FALSE', '0', 'Skip ID Query']],
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'resetDevice',
                'type': 'ViBoolean',
                'documentation': {
                    'description': 'Specifies whether to reset',
                    'table_body': [['VI\\_TRUE (default)', '1', 'Reset Device'], ['VI\\_FALSE', '0', "Don't Reset"]],
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'optionString',
                'type': 'ViString',
                'documentation': {
                    'description': 'Some options',
                },
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Returns a ViSession handle that you use.',
                },
            },
        ],
        'documentation': {
            'description': 'Creates a new IVI instrument driver session.',
        },
    },

    'close': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session.',
                },
            },
        ],
        'documentation': {
            'description': 'Closes the specified session and deallocates resources that it reserved.',
        },
    },

    #### Initiate / Abort

    'Initiate': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session.',
                },
            },
        ],
        'documentation': {
            'description': 'Initiates a thingie.',
        },
    },

    'Abort': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session.',
                },
            },
        ],
        'documentation': {
            'description': 'Aborts a previously initiated thingie.',
        },
    },

    #### Attribute getters
    # TODO(marcoskirsch) clean up

    'GetAttributeViBoolean': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session.',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'channelName',
                'type': 'ViConstString',
                'documentation': {
                    'description': 'This is the channel(s) that this function will apply to.',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeId',
                'type': 'ViAttr',
                'documentation': {
                    'description': 'Pass the ID of an attribute.',
                },
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'attributeValue',
                'type': 'ViBoolean',
                'documentation': {
                    'description': 'Returns the value of the attribute.',
                },
            },
        ],
        'documentation': {
            'description': 'Queries the value of a ViBoolean attribute.',
        },
    },

    'GetAttributeViInt32': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session.',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'channelName',
                'type': 'ViConstString',
                'documentation': {
                    'description': 'This is the channel(s) that this function will apply to.',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeId',
                'type': 'ViAttr',
                'documentation': {
                    'description': 'Pass the ID of an attribute.',
                },
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'attributeValue',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Returns the value of the attribute.',
                },
            },
        ],
        'documentation': {
            'description': 'Queries the value of a ViInt32 attribute.',
        },
    },
    'GetAttributeViReal64': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session.',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'channelName',
                'type': 'ViConstString',
                'documentation': {
                    'description': 'This is the channel(s) that this function will apply to.',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeId',
                'type': 'ViAttr',
                'documentation': {
                    'description': 'Pass the ID of an attribute.',
                },
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'attributeValue',
                'type': 'ViReal64',
                'documentation': {
                    'description': 'Returns the value of the attribute.',
                },
            },
        ],
        'documentation': {
            'description': 'Queries the value of a ViReal attribute.',
        },

    },
    'GetAttributeViSession': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session.',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'channelName',
                'type': 'ViConstString',
                'documentation': {
                    'description': 'This is the channel(s) that this function will apply to.',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeId',
                'type': 'ViAttr',
                'documentation': {
                    'description': 'Pass the ID of an attribute.',
                },
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'attributeValue',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Returns the value of the attribute.',
                },
            },
        ],
        'documentation': {
            'description': 'Queries the value of a ViSession attribute.',
        },
    },
    'GetAttributeViString': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session.',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'channelName',
                'type': 'ViConstString',
                'documentation': {
                    'description': 'This is the channel(s) that this function will apply to.',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeId',
                'type': 'ViAttr',
                'documentation': {
                    'description': 'Pass the ID of an attribute.',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'bufferSize',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Number of bytes in attributeValue. You can IVI-dance with this.',
                },
            },
            {
                'direction': 'out',
                'enum': None,
                'is_buffer': True,
                'name': 'attributeValue',
                'type': 'ViChar',
                'documentation': {
                    'description': 'Returns the value of the attribute.',
                },
            },
        ],
        'documentation': {
            'description': 'Queries the value of a ViBoolean attribute.',
        },
    },

    #### Attribute setters
    # TODO(marcoskirsch) clean up

    'SetAttributeViBoolean': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session.',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'channelName',
                'type': 'ViConstString',
                'documentation': {
                    'description': 'This is the channel(s) that this function will apply to.',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeId',
                'type': 'ViAttr',
                'documentation': {
                    'description': 'Pass the ID of an attribute.',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeValue',
                'type': 'ViBoolean',
                'documentation': {
                    'description': 'Pass the value that you want to set the attribute to.',
                },
            },
        ],
        'documentation': {
            'description': 'This function sets the value of a ViBoolean attribute.',
        },
    },
    'SetAttributeViInt32': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session.',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'channelName',
                'type': 'ViConstString',
                'documentation': {
                    'description': 'This is the channel(s) that this function will apply to.',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeId',
                'type': 'ViAttr',
                'documentation': {
                    'description': 'Pass the ID of an attribute.',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeValue',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Pass the value that you want to set the attribute to.',
                },
            },
        ],
        'documentation': {
            'description': 'This function sets the value of a ViInt32 attribute.',
        },
    },
    'SetAttributeViReal64': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session.',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'channelName',
                'type': 'ViConstString',
                'documentation': {
                    'description': 'This is the channel(s) that this function will apply to.',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeId',
                'type': 'ViAttr',
                'documentation': {
                    'description': 'Pass the ID of an attribute.',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeValue',
                'type': 'ViReal64',
                'documentation': {
                    'description': 'Pass the value that you want to set the attribute to.',
                },
            },
        ],
        'documentation': {
            'description': 'This function sets the value of a ViReal64 attribute.',
        },
    },
    'SetAttributeViSession': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session.',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'channelName',
                'type': 'ViConstString',
                'documentation': {
                    'description': 'This is the channel(s) that this function will apply to.',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeId',
                'type': 'ViAttr',
                'documentation': {
                    'description': 'Pass the ID of an attribute.',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeValue',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Pass the value that you want to set the attribute to.',
                },
            },
        ],
        'documentation': {
            'description': 'This function sets the value of a ViSession attribute.',
        },
    },
    'SetAttributeViString': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session.',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'channelName',
                'type': 'ViConstString',
                'documentation': {
                    'description': 'This is the channel(s) that this function will apply to.',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeId',
                'type': 'ViAttr',
                'documentation': {
                    'description': 'Pass the ID of an attribute.',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'is_buffer': True,
                'name': 'attributeValue',
                'type': 'ViChar',
                'documentation': {
                    'description': 'Pass the value that you want to set the attribute to.',
                },
            },
        ],
        'documentation': {
            'description': 'This function sets the value of a ViString attribute.',
        },
    },

    #### Error functions
    #TODO(marcoskirsch) clean up

    'GetError': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session.',
                },
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'errorCode',
                'type': 'ViStatus',
                'documentation': {
                    'description': 'Returns errorCode for the session. If you pass 0 for bufferSize, you can pass VI\_NULL for this.',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'bufferSize',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Number of bytes in description buffer.',
                },
            },
            {
                'direction': 'out',
                'enum': None,
                'is_buffer': True,
                'name': 'description',
                'type': 'ViChar',
                'documentation': {
                    'description': 'At least bufferSize big, string comes out here.',
                },
            },
        ],
        'documentation': {
            'description': 'Returns the error information associated with the session.',
        },
    },

    'GetErrorMessage': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session.',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'errorCode',
                'type': 'ViStatus',
                'documentation': {
                    'description': 'The error code returned for which you want to get a string.',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'buffer_size',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Number of bytes allocated for errorMessage',
                },
            },
            {
                'direction': 'out',
                'enum': None,
                'is_buffer': True,
                'name': 'errorMessage',
                'type': 'ViChar',
                'documentation': {
                    'description': 'Error information formatted into a user-readable string.',
                },
            },
        ],
        'documentation': {
            'description': 'Returns the errorMessage as a user-readable string. Uses IVI-dance',
        },
    },

    'error_message': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session.',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'errorCode',
                'type': 'ViStatus',
                'documentation': {
                    'description': 'The errorCode returned from the instrument.',
                },
            },
            {
                'direction': 'out',
                'enum': None,
                'is_buffer': True,
                'name': 'errorMessage',
                'type': 'ViChar',
                'documentation': {
                    'description': 'The error information formatted into a string.',
                },
            },
        ],
        'documentation': {
            'description': 'Takes the errorCode returned by a functiona and returns it as a user-readable string.',
        },
    },

    'ClearError': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session.',
                },
            },
        ],
        'documentation': {
            'description': 'Clears the error for the current thread and session',
        },
    },

    #### Different function cases

    'SimpleFunction': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session. You obtain the **vi**',
                },
            },
        ],
        'documentation': {
            'description': 'This function takes no parameters other than the session.',
        },
    },

    'OneInputFunction': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session. You obtain the **vi**',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'aNumber',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Contains a number',
                },
            },
        ],
        'documentation': {
            'description': 'This function takes one parameter other than the session.',
        },
    },

    'TwoInputFunction': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session. You obtain the **vi**',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'aNumber',
                'type': 'ViReal64',
                'documentation': {
                    'description': 'Contains a number',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'aString',
                'type': 'ViChar',
                'documentation': {
                    'description': 'Contains a string',
                },
            },
        ],
        'documentation': {
            'description': 'This function takes two parameters other than the session.',
        },
    },

    'GetANumber': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session.',
                },
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'aNumber',
                'type': 'ViInt16',
                'documentation': {
                    'description': 'Contains a number.',
                },
            },
        ],
        'documentation': {
            'description': 'Returns a number.',
            'note': 'This function rules!',
        },
    },

    'GetABoolean': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session.',
                },
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'aBoolean',
                'type': 'ViBoolean',
                'documentation': {
                    'description': 'Contains a boolean.',
                },
            },
        ],
        'documentation': {
            'description': 'Returns a boolean.',
            'note': 'This function rules!',
        },
    },

    'GetAStringOfFixedMaximumSize': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session.',
                },
            },
            {
                'direction': 'out',
                'enum': None,
                'is_buffer': True,
                'name': 'aString',
                'type': 'ViChar',
                'documentation': {
                    'description': 'String comes back here. Buffer must be 256 big.',
                },
            },
        ],
        'documentation': {
            'description': 'Illustrates resturning a string of fixed size.',
        },
    },

    'GetAStringWithSpecifiedMaximumSize': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session.',
                },
            },
            {
                'direction': 'out',
                'enum': None,
                'is_buffer': True,
                'name': 'aString',
                'type': 'ViChar',
                'documentation': {
                    'description': 'String comes back here. Buffer must be at least bufferSize big.',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'bufferSize',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Buffersize of the string.',
                },
            },
        ],
        'documentation': {
            'description': 'Illustrates resturning a string where user specifies the size.',
        },
    },

    'ReturnANumberAndAString': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session.',
                },
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'aNumber',
                'type': 'ViInt16',
                'documentation': {
                    'description': 'Contains a number.',
                },
            },
            {
                'direction': 'out',
                'enum': None,
                'is_buffer': True,
                'name': 'aString',
                'type': 'ViChar',
                'documentation': {
                    'description': 'Contains a string.',
                },
            },
        ],
        'documentation': {
            'description': 'Returns a number and a string.',
            'note': 'This function rules!',
        },
    },

    'Read': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session.',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'maximumTime',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Specifies the **maximum\_time** allowed in years.',
                },
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'reading',
                'type': 'ViReal64',
                'documentation': {
                    'description': 'The measured value.',
                },
            },
        ],
        'documentation': {
            'description': 'Acquires a single measurement and returns the measured value.',
        },
    },

    'ReadMultiPoint': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session.',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'maximumTime',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Specifies the **maximum\_time** allowed in years.',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'arraySize',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Number of measurements to acquire.',
                },
            },
            {
                'direction': 'out',
                'enum': None,
                'is_buffer': True,
                'name': 'readingArray',
                'type': 'ViReal64',
                'documentation': {
                    'description': 'An array of measurement values.',
                    'note': 'The size must be at least arraySize.',
                },
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'actualNumberOfPoints',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Indicates the number of measured values actually retrieved.',
                },
            },
        ],
        'documentation': {
            'description': 'Acquires multiple measurements and returns an array of measured values.',
        },
    },

    'GetEnumValue': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session.',
                },
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'aQuantity',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'This is an amount.',
                    'note': 'The amount will be between -2^31 and (2^31-1)',
                },
            },
            {
                'direction': 'out',
                'enum': 'Turtle',
                'name': 'aTurtle',
                'type': 'ViInt16',
                'documentation': {
                    'description': 'Indicates a ninja turtle',
                    'table_body': [['0', 'Leonardo'], ['1', 'Donatello'], ['2', 'Raphael'], ['3', 'Mich elangelo']],
                },
            },
        ],
        'documentation': {
            'description': 'Returns an enum value',
            'note': 'Splinter is not supported.',
        },
    },

    #TODO(marcoskirsch): Lots more cases to add:
    #     Returning arrays (not strings) through all 3 mechanisms
    #     Returning strings using ivi-dance
    #     Returning lots of numbers
    #     Taking parameters of all types
    #     Input buffers ans trings
    #     Returning parameters of all types
    #     Enums enums enums
    #     Waveforms as inputs and outputs
    #     ... etc

}

functions_codegen_method = {
    'InitWithOptions':          { 'codegen_method': 'private',  },
    'Initiate':                 { 'codegen_method': 'private',  },
    'close':                    { 'codegen_method': 'private',  },
    'Abort':                    { 'codegen_method': 'private',  },
    'GetAttributeViBoolean':    { 'codegen_method': 'private',  }, # All Set/Get Attribute functions are private
    'GetAttributeViInt32':      { 'codegen_method': 'private',  }, # All Set/Get Attribute functions are private
    'GetAttributeViReal64':     { 'codegen_method': 'private',  }, # All Set/Get Attribute functions are private
    'GetAttributeViSession':    { 'codegen_method': 'private',  }, # All Set/Get Attribute functions are private
    'GetAttributeViString':     { 'codegen_method': 'private',  }, # All Set/Get Attribute functions are private
    'SetAttributeViBoolean':    { 'codegen_method': 'private',  }, # All Set/Get Attribute functions are private
    'SetAttributeViInt32':      { 'codegen_method': 'private',  }, # All Set/Get Attribute functions are private
    'SetAttributeViReal64':     { 'codegen_method': 'private',  }, # All Set/Get Attribute functions are private
    'SetAttributeViSession':    { 'codegen_method': 'private',  }, # All Set/Get Attribute functions are private
    'SetAttributeViString':     { 'codegen_method': 'private',  }, # All Set/Get Attribute functions are private
    'GetError':                 { 'codegen_method': 'private',  },
    'GetErrorMessage':          { 'codegen_method': 'private',  },
    'ClearError':               { 'codegen_method': 'private',  },
}

# Attach the given parameter to the given enum from enums.py
functions_enums = {
    'GetEnumValue':                 { 'parameters': { 2: { 'enum': 'Turtle',    }, }, },
}

# TODO(texasaggie97) can we get rid of this now that we are code generating the ivi-dance method of buffer retrieval? Issue #259
functions_params_types = {
    'GetAttributeViString':         { 'parameters': { 4: { 'type': 'ViString',                  }, }, },
    'SetAttributeViString':         { 'parameters': { 3: { 'type': 'ViString',                  }, }, },
    'GetError':                     { 'parameters': { 3: { 'type': 'ViString',                  }, }, },
}

# This is the additional information needed by the code generator to properly generate the buffer retrieval mechanism
# {'is_buffer': True} is required for all parameters that are arrays. Some were able to be detected as an array when
#   generating functions.py. This sets 'is_buffer' for those parameters where the dectection didn't work
# {'size': <size information>} is required for all output buffers.
# <size information> is a dictionary with two keys: 'mechanism' and 'value'.
#   'mechanism' can be:
#       'fixed':        The size is known ahead of time, usually defined by the API.
#                       'value' should be an int.
#       'passed-in':    When the size comes from another parameter.
#                       'value' should be the name of the parameter through which this is specified.
#       'ivi-dance':    When the size is determined by calling into the function using a size of zero and
#                       interpreting the return value as a size rather than an error.
#                       'value' should be the name of the parameter through which the size (0, then the real
#                       one) is passed in. This parameter won't exist in the corresponding Python Session method.
functions_buffer_info = {
    'GetError':                             { 'parameters': { 3: { 'size': {'mechanism':'ivi-dance', 'value':'bufferSize' }, }, }, },
    'GetErrorMessage':                      { 'parameters': { 3: { 'size': {'mechanism':'ivi-dance', 'value':'buffer_size'}, }, }, },
    'ReadMultiPoint':                       { 'parameters': { 3: { 'size': {'mechanism':'passed-in', 'value':'arraySize'  }, }, }, },
    'GetAttributeViString':                 { 'parameters': { 4: { 'size': {'mechanism':'ivi-dance', 'value':'bufferSize' }, }, }, },
    'GetAStringWithSpecifiedMaximumSize':   { 'parameters': { 1: { 'size': {'mechanism':'passed-in', 'value':'bufferSize' }, }, }, },
    'InitWithOptions':                      { 'parameters': { 0: { 'is_buffer': True, },
                                                              3: { 'is_buffer': True, }, }, },
    'GetAttributeViBoolean':                { 'parameters': { 1: { 'is_buffer': True, }, }, },
    'GetAttributeViInt32':                  { 'parameters': { 1: { 'is_buffer': True, }, }, },
    'GetAttributeViReal64':                 { 'parameters': { 1: { 'is_buffer': True, }, }, },
    'GetAttributeViSession':                { 'parameters': { 1: { 'is_buffer': True, }, }, },
    'GetAttributeViString':                 { 'parameters': { 1: { 'is_buffer': True, }, }, },
    'SetAttributeViBoolean':                { 'parameters': { 1: { 'is_buffer': True, }, }, },
    'SetAttributeViInt32':                  { 'parameters': { 1: { 'is_buffer': True, }, }, },
    'SetAttributeViReal64':                 { 'parameters': { 1: { 'is_buffer': True, }, }, },
    'SetAttributeViSession':                { 'parameters': { 1: { 'is_buffer': True, }, }, },
    'SetAttributeViString':                 { 'parameters': { 1: { 'is_buffer': True, }, }, },
}

# ORIGINAL
def merge_dicts(into, outof):
    '''merge_dicts

    Recursively merges the two passed in dictionaries.
    '''
    for item in sorted(outof):
        if type(outof[item]) is dict:
            if item in into:
                merge_dicts(into[item], outof[item])
            elif type(into) is list:
                for item2 in outof[item]:
                    into[item][item2] = outof[item][item2]
            else:                
                # Handle regex in addon
                for item2 in into:
                    if re.search(item, item2):
                        assert type(into[item2]) is dict
                        merge_dicts(into[item2], outof[item])
        else:
            into[item] = outof[item]


'''
# Python 3.5 only
def merge_dicts(a, b):
    destination = a.copy()
    for item in sorted(b):
        if item in a:
            destination[item] =
        if type(a) is dict and type(b) is dict:
            return {**a, **b}
        if type(a) is
'''

def do_the_test(a, b, expected):
    actual   = a.copy()
    merge_dicts(actual, b)
    assert expected == actual, "\na = {0}\nb = {1}\nexpected = {2}\nactual = {3}".format(a, b, expected, actual)

def test_merge_1():
    a        = {'a':1, 'b':2}
    b        = {}
    expected = {'a':1, 'b':2}
    do_the_test(a,b, expected)

def test_merge_2():
    a        = {'a':1, 'b':2}
    b        = {'c':3}
    expected = {'a':1, 'b':2, 'c':3}
    do_the_test(a,b, expected)

def test_merge_3():
    a        = {}
    b        = {'a':1, 'b':2}
    expected = {'a':1, 'b':2}
    do_the_test(a,b, expected)

def test_merge_4():
    a        = {'a':1, 'b':2}
    b        = {'b':3, 'c':4}
    expected = {'a':1, 'b':3, 'c':4}
    do_the_test(a,b, expected)

def test_merge_5():
    a        = {'a':1, 'b':{'b1':5, 'b2':6}}
    b        = {'b':{'b3':7}, 'c':4}
    expected = {'a':1, 'b':{'b1':5, 'b2':6, 'b3':7}, 'c':4}
    do_the_test(a,b, expected)

def test_merge_6():
    a        = {'a':1, 'b':{'b1':5, 'b2':6}, 'c':['x', 'y', 'z']}
    b        = {'b':{'b3':7, 'b1':8}, 'c':{0:'r', 1:'s', 2:'t'}}
    expected = {'a':1, 'b':{'b1':8, 'b2':6, 'b3':7}, 'c':['r', 's', 't']}
    do_the_test(a,b, expected)

def test_merge_6():
    a        = {'a':1, 'b':{'b1':2, 'b2':3}, 'c':['x', 'y', 'z']}
    b        = {'b':{'b3':7, 'b1':8}, 'c':{0:'r', 1:'s', 2:'t'}}
    expected = {'a':1, 'b':{'b1':8, 'b2':3, 'b3':7}, 'c':['r', 's', 't']}
    do_the_test(a,b, expected)

def test_merge_7():
    a        = {'aaa':{}, 'aaaa':{'x':98}, 'aaaaa':{}, 'bbb':{'bbb1':2, 'bbb2':3}, 'ccc':['x', 'y', 'z']}
    b        = {'a+':{'z':99}}
    expected = {'aaa':{'z':99}, 'aaaa':{'x':98, 'z':99}, 'aaaaa':{'z':99}, 'bbb':{'bbb1':2, 'bbb2':3}, 'ccc':['x', 'y', 'z']}
    do_the_test(a,b, expected)

merge_dicts(functions, functions_codegen_method)
merge_dicts(functions, functions_enums)
merge_dicts(functions, functions_params_types)

pprint.pprint(functions)

print("done!")