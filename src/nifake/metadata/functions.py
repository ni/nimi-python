# -*- coding: utf-8 -*-
# This file contains function metadata for NI-FAKE, a fake driver
# whose purpose is to test the nimi-python codegenerator.

#TODO(marcoskirsch): We need to expand this metadata, to have combinations for every case of:
# (inputs) * (outputs) * (codegen_method) * (buffers) * etc
# For now, add a handful by hand as a starting point.

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
                    'description': 'Contains the **resource_name** of the device to initialize.',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'idQuery',
                'type': 'ViBoolean',
                'documentation': {
                    'description': 'NI-FAKE is probably not needed.',
                    'table_body': [['VI_TRUE (default)', '1', 'Perform ID Query'], ['VI_FALSE', '0', 'Skip ID Query']],
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'resetDevice',
                'type': 'ViBoolean',
                'documentation': {
                    'description': 'Specifies whether to reset',
                    'table_body': [['VI_TRUE (default)', '1', 'Reset Device'], ['VI_FALSE', '0', "Don't Reset"]],
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
    #TODO(marcoskirsch) clean up

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
    'GetAttributeViInt64': {
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
                'type': 'ViInt64',
                'documentation': {
                    'description': 'Returns the value of the attribute.',
                },
            },
        ],
        'documentation': {
            'description': 'Queries the value of a ViInt64 attribute.',
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
                'name': 'attributeValue',
                'type': 'ViChar[]',
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
    #TODO(marcoskirsch) clean up

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
    'SetAttributeViInt64': {
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
                'type': 'ViInt64',
                'documentation': {
                    'description': 'Pass the value that you want to set the attribute to.',
                },
            },
        ],
        'documentation': {
            'description': 'This function sets the value of a ViInt64 attribute.',
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
                'name': 'attributeValue',
                'type': 'ViChar[]',
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
                    'description': 'Returns errorCode for the session. If you pass 0 for bufferSize, you can pass VI_NULL for this.',
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
                'name': 'description',
                'type': 'ViChar[]',
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
                'name': 'errorMessage',
                'type': 'ViChar[]',
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
                'name': 'errorMessage',
                'type': 'ViChar[]',
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

    'PoorlyNamedSimpleFunction': {
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
                'type': 'ViChar[]',
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

    'GetAnIviDanceString': {
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
                'name': 'bufferSize',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Number of bytes in aString You can IVI-dance with this.',
                },
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'aString',
                'type': 'ViChar[]',
                'documentation': {
                    'description': 'Returns the string.',
                },
            },
        ],
        'documentation': {
            'description': 'Returns a string using the IVI dance.',
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
                'name': 'aString',
                'type': 'ViChar[]',
                'documentation': {
                    'description': 'String comes back here. Buffer must be 256 big.',
                },
            },
        ],
        'documentation': {
            'description': 'Illustrates resturning a string of fixed size.',
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
                'name': 'aString',
                'type': 'ViChar[]',
                'documentation': {
                    'description': 'Contains a string. Buffer must be 256 bytes or larger.',
                },
            },
        ],
        'documentation': {
            'description': 'Returns a number and a string.',
            'note': 'This function rules!',
        },
    },
    
    'GetAStringUsingPythonCode': {
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
                'name': 'aNumber',
                'type': 'ViInt16',
                'documentation': {
                    'description': 'Contains a number.',
                },
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'aString',
                'type': 'ViChar[]',
                'documentation': {
                    'description': 'Contains a string of length aNumber.',
                },
            },
        ],
        'documentation': {
            'description': 'Returns a number and a string.',
            'note': 'This function rules!',
        },
    },

    'Use64BitNumber': {
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
                'name': 'input',
                'type': 'ViInt64',
                'documentation': {
                    'description': 'A big number on its way in.',
                },
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'output',
                'type': 'ViInt64',
                'documentation': {
                    'description': 'A big number on its way out.',
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
                'type': 'ViReal64',
                'documentation': {
                    'description': 'Specifies the **maximum_time** allowed in seconds.',
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

    'ReadFromChannel': {
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
                'name': 'maximumTime',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Specifies the **maximum_time** allowed in microseconds.',
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

    'EnumInputFunctionWithDefaults': {
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
            'description': 'This function takes one parameter other than the session, which happens to be an enum and has a default value defined in functions_addon.',
        },
    },
    'BoolArrayOutputFunction': {
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
                'name': 'numberOfElements',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Number of elements in the array.',
                },
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'anArray',
                'type': 'ViBoolean[]',
                'documentation': {
                    'description': 'Contains an array of booleans',
                },
            },
        ],
        'documentation': {
            'description': 'This function returns an array of booleans.',
        },
    },
    'EnumArrayOutputFunction': {
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
                'name': 'numberOfElements',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Number of elements in the array.',
                },
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'anArray',
                'type': 'ViInt16[]',
                'documentation': {
                    'description': 'Contains an array of enums, stored as 16 bit integers under the hood ',
                },
            },
        ],
        'documentation': {
            'description': 'This function returns an array of enums, stored as 16 bit integers under the hood.',
        },
    },

    'ReturnMultipleTypes': {
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
            {
                'direction': 'out',
                'enum': None,
                'name': 'anInt32',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Contains a 32-bit integer.',
                },
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'anInt64',
                'type': 'ViInt64',
                'documentation': {
                    'description': 'Contains a 64-bit integer.',
                },
            },
            {
                'direction': 'out',
                'enum': 'Turtle',
                'name': 'anIntEnum',
                'type': 'ViInt16',
                'documentation': {
                    'description': 'Indicates a ninja turtle',
                    'table_body': [['0', 'Leonardo'], ['1', 'Donatello'], ['2', 'Raphael'], ['3', 'Mich elangelo']],
                },
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'aFloat',
                'type': 'ViReal64',
                'documentation': {
                    'description': 'The measured value.',
                },
            },
            {
                'direction': 'out',
                'enum': 'FloatEnum',
                'name': 'aFloatEnum',
                'type': 'ViReal64',
                'documentation': {
                    'description': 'A float enum.',
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
                'name': 'anArray',
                'type': 'ViReal64[]',
                'documentation': {
                    'description': 'An array of measurement values.',
                    'note': 'The size must be at least arraySize.',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'stringSize',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Number of bytes allocated for aString',
                },
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'aString',
                'type': 'ViChar[]',
                'documentation': {
                    'description': 'An IVI dance string.',
                },
            },
        ],
        'documentation': {
            'description': 'Returns multiple types.',
        },
    },

    'MultipleArrayTypes': {
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
                'name': 'outputArraySize',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Size of the array that will be returned.',
                },
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'outputArray',
                'type': 'ViReal64[]',
                'documentation': {
                    'description': 'Array that will be returned.',
                    'note': 'The size must be at least outputArraySize.',
                },
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'outputArrayOfFixedLength',
                'type': 'ViReal64[]',
                'documentation': {
                    'description': 'An array of doubles with fixed size.',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'inputArraySizes',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Size of inputArrayOfFloats and inputArrayOfIntegers',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'inputArrayOfFloats',
                'type': 'ViReal64[]',
                'documentation': {
                    'description': 'Array of floats',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'inputArrayOfIntegers',
                'type': 'ViInt16[]',
                'documentation': {
                    'description': 'Array of integers. Optional. If passed in then size must match that of inputArrayOfFloats.',
                },
            },        
        ],
        'documentation': {
            'description': 'Receives and returns multiple types of arrays.',
        },
    },

    'ParametersAreMultipleTypes': {
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
                'name': 'aBoolean',
                'type': 'ViBoolean',
                'documentation': {
                    'description': 'Contains a boolean.',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'anInt32',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Contains a 32-bit integer.',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'anInt64',
                'type': 'ViInt64',
                'documentation': {
                    'description': 'Contains a 64-bit integer.',
                },
            },
            {
                'direction': 'in',
                'enum': 'Turtle',
                'name': 'anIntEnum',
                'type': 'ViInt16',
                'documentation': {
                    'description': 'Indicates a ninja turtle',
                    'table_body': [['0', 'Leonardo'], ['1', 'Donatello'], ['2', 'Raphael'], ['3', 'Mich elangelo']],
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'aFloat',
                'type': 'ViReal64',
                'documentation': {
                    'description': 'The measured value.',
                },
            },
            {
                'direction': 'in',
                'enum': 'FloatEnum',
                'name': 'aFloatEnum',
                'type': 'ViReal64',
                'documentation': {
                    'description': 'A float enum.',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'stringSize',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Number of bytes allocated for aString',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'aString',
                'type': 'ViChar[]',
                'documentation': {
                    'description': 'An IVI dance string.',
                },
            },
        ],
        'documentation': {
            'description': 'Has parameters of multiple types.',
        },
    },
    'GetArrayUsingIVIDance': {
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
                'name': 'arraySize',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Specifies the size of the buffer for copyint arrayOut onto.',
                },
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'arrayOut',
                'type': 'ViReal64[]',
                'documentation': {
                    'description': 'The array returned by this function',
                },
            },
        ],
        'documentation': {
            'description': 'This function returns an array of float whose size is determined with the IVI dance.',
        },
    },
    'SetCustomType': {
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
                'name': 'cs',
                'type': 'custom_struct',
                'documentation': {
                    'description': 'Set using custom type',
                },
            },
        ],
        'documentation': {
            'description': 'This function takes a custom type.',
        },
    },
    'SetCustomTypeArray': {
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
                'name': 'numberOfElements',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Number of elements in the array.',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'cs',
                'type': 'custom_struct[]',
                'documentation': {
                    'description': 'Set using custom type',
                },
            },
        ],
        'documentation': {
            'description': 'This function takes an array of custom types.',
        },
    },
    'GetCustomType': {
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
                'name': 'cs',
                'type': 'custom_struct',
                'documentation': {
                    'description': 'Set using custom type',
                },
            },
        ],
        'documentation': {
            'description': 'This function returns a custom type.',
        },
    },
    'GetCustomTypeArray': {
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
                'name': 'numberOfElements',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Number of elements in the array.',
                },
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'cs',
                'type': 'custom_struct[]',
                'documentation': {
                    'description': 'Get using custom type',
                },
            },
        ],
        'documentation': {
            'description': 'This function returns a custom type.',
        },
    },
    'GetArraySizeForPythonCode': {
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
                'name': 'sizeOut',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Size of array',
                },
            },
        ],
        'documentation': {
            'description': 'This function returns the size of the array for use in python-code size mechanism.',
        },
    },
    'GetArrayForPythonCodeDouble': {
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
                'name': 'numberOfElements',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Number of elements in the array.',
                },
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'arrayOut',
                'type': 'ViReal64[]',
                'documentation': {
                    'description': 'Array of double using puthon-code size mechanism',
                },
            },
        ],
        'documentation': {
            'description': 'This function returns an array for use in python-code size mechanism.',
        },
    },
    'GetArrayForPythonCodeCustomType': {
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
                'name': 'numberOfElements',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Number of elements in the array.',
                },
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'arrayOut',
                'type': 'custom_struct[]',
                'documentation': {
                    'description': 'Array of custom type using puthon-code size mechanism',
                },
            },
        ],
        'documentation': {
            'description': 'This function returns an array for use in python-code size mechanism.',
        },
    },
    'FetchWaveform': {
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
                }
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'numberOfSamples',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Number of samples to return',
                },
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'waveformData',
                'type': 'ViReal64[]',
                'documentation': {
                    'description': 'Samples fetched from the device. Array should be numberOfSamples big.',
                },
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'actualNumberOfSamples',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Number of samples actually fetched.',
                },
            },
        ],
        'documentation': {
            'description': 'Returns waveform data.',
        },
    },
    'WriteWaveform': {
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
                }
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'numberOfSamples',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'How many samples the waveform contains.',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'waveform',
                'type': 'ViReal64[]',
                'documentation': {
                    'description': 'Waveform data.',
                },
            },
        ],
        'documentation': {
            'description': 'Writes waveform to the driver',
        },
    },
    'GetCalDateAndTime': {
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
                'name': 'calType',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Specifies the type of calibration performed (external or self-calibration).',
                },
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'Month',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Indicates the **month** of the last calibration.',
                },
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'Day',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Indicates the **day** of the last calibration.',
                },
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'Year',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Indicates the **year** of the last calibration.',
                },
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'Hour',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Indicates the **hour** of the last calibration.',
                },
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'Minute',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Indicates the **minute** of the last calibration.',
                },
            },
        ],
        'documentation': {
            'description': 'Returns the date and time of the last calibration performed.',
        },
    },
    'self_test': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session. You obtain the **vi** parameter from niFake_InitWithOptions.',
                    },
            },
            {
                'direction': 'out',
                'name': 'selfTestResult',
                'type': 'ViInt16',
                'documentation': {
                    'description': 'Contains the value returned from the instrument self-test. Zero indicates success.',
                },
            },
            {
                'direction': 'out',
                'name': 'selfTestMessage',
                'type': 'ViChar[ ]',
                'documentation': {
                    'description': 'This parameter contains the string returned from the instrument self-test. The array must contain at least 256 elements.'
                },
            },
        ],
        'documentation': {
            'description': 'Performs a self-test.',
        },
    },
    'GetCalInterval': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session.',
                },
            },
            {
                'direction': 'out',
                'name': 'Months',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Specifies the recommended maximum interval, in **months**, between external calibrations.',
                },
            },
        ],
        'documentation': {
            'description': 'Returns the recommended maximum interval, in **months**, between external calibrations.',
        },
    },
    'LockSession': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session.',
                },
            },
            {
                'direction': 'out',
                'name': 'callerHasLock',
                'type': 'ViBoolean',
                'documentation': {
                    'description': 'Optional',
                },
            },
        ],
        'documentation': {
            'description': 'Lock.',
        },
    },
    'UnlockSession': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session.',
                },
            },
            {
                'direction': 'out',
                'name': 'callerHasLock',
                'type': 'ViBoolean',
                'documentation': {
                    'description': 'Optional',
                },
            },
        ],
        'documentation': {
            'description': 'Unlock',
        },
    },
    'MultipleArraysSameSize': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session.',
                },
            },
            {
                'direction': 'in',
                'name': 'Values1',
                'type': 'ViReal64[]',
                'documentation': {
                    'description': 'Array 1 of same size.',
                },
            },
            {
                'direction': 'in',
                'name': 'Values2',
                'type': 'ViReal64[]',
                'documentation': {
                    'description': 'Array 2 of same size.',
                },
            },
            {
                'direction': 'in',
                'name': 'Values3',
                'type': 'ViReal64[]',
                'documentation': {
                    'description': 'Array 3 of same size.',
                },
            },
            {
                'direction': 'in',
                'name': 'Values4',
                'type': 'ViReal64[]',
                'documentation': {
                    'description': 'Array 4 of same size.',
                },
            },
            {
                'direction': 'in',
                'name': 'Size',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Size for all arrays',
                },
            },
        ],
        'documentation': {
            'description': 'Function to test multiple arrays that use the same size',
        },
    },
}
