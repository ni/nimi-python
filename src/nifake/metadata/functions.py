# -*- coding: utf-8 -*-
# This file is generated from NI-FAKE API metadata version 0.2.0d23
functions = {
    'Abort': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Aborts a previously initiated thingie.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'BoolArrayOutputFunction': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'This function returns an array of booleans.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session. You obtain the **vi**'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of elements in the array.'
                },
                'name': 'numberOfElements',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Contains an array of booleans'
                },
                'name': 'anArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfElements'
                },
                'type': 'ViBoolean[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearError': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Clears the error for the current thread and session'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'EnumArrayOutputFunction': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'This function returns an array of enums, stored as 16 bit integers under the hood.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session. You obtain the **vi**'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of elements in the array.'
                },
                'name': 'numberOfElements',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Contains an array of enums, stored as 16 bit integers under the hood '
                },
                'enum': 'Turtle',
                'name': 'anArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfElements'
                },
                'type': 'ViInt16[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'EnumInputFunctionWithDefaults': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'This function takes one parameter other than the session, which happens to be an enum and has a default value defined in functions_addon.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session. You obtain the **vi**'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': 'Turtle.LEONARDO',
                'direction': 'in',
                'documentation': {
                    'description': 'Indicates a ninja turtle',
                    'table_body': [
                        [
                            '0',
                            'Leonardo'
                        ],
                        [
                            '1',
                            'Donatello'
                        ],
                        [
                            '2',
                            'Raphael'
                        ],
                        [
                            '3',
                            'Mich elangelo'
                        ]
                    ]
                },
                'enum': 'Turtle',
                'name': 'aTurtle',
                'type': 'ViInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchWaveform': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns waveform data.'
        },
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            },
            {
                'documentation_filename': 'numpy_method',
                'method_python_name_suffix': '_into',
                'session_filename': 'numpy_read_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of samples to return'
                },
                'name': 'numberOfSamples',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Samples fetched from the device. Array should be numberOfSamples big.'
                },
                'name': 'waveformData',
                'numpy': True,
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfSamples'
                },
                'type': 'ViReal64[]',
                'use_array': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Number of samples actually fetched.'
                },
                'name': 'actualNumberOfSamples',
                'type': 'ViInt32',
                'use_in_python_api': False
            }
        ],
        'returns': 'ViStatus'
    },
    'GetABoolean': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns a boolean.',
            'note': 'This function rules!'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Contains a boolean.'
                },
                'name': 'aBoolean',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetANumber': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns a number.',
            'note': 'This function rules!'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Contains a number.'
                },
                'name': 'aNumber',
                'type': 'ViInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAStringOfFixedMaximumSize': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Illustrates resturning a string of fixed size.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'String comes back here. Buffer must be 256 big.'
                },
                'name': 'aString',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAStringUsingPythonCode': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns a number and a string.',
            'note': 'This function rules!'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Contains a number.'
                },
                'name': 'aNumber',
                'type': 'ViInt16'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Contains a string of length aNumber.'
                },
                'name': 'aString',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'a_number'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAnIviDanceString': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns a string using the IVI dance.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of bytes in aString You can IVI-dance with this.'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the string.'
                },
                'name': 'aString',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAnIviDanceWithATwistString': {
        'codegen_method': 'public',
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
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'aString',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'actualSize'
                },
                'type': 'ViChar[]'
            },
            {
                'direction': 'out',
                'name': 'actualSize',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetArrayForPythonCodeCustomType': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'This function returns an array for use in python-code size mechanism.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of elements in the array.'
                },
                'name': 'numberOfElements',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'self.get_array_size_for_python_code()'
                },
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Array of custom type using puthon-code size mechanism'
                },
                'name': 'arrayOut',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'self.get_array_size_for_python_code()'
                },
                'type': 'struct CustomStruct[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetArrayForPythonCodeDouble': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'This function returns an array for use in python-code size mechanism.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of elements in the array.'
                },
                'name': 'numberOfElements',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'self.get_array_size_for_python_code()'
                },
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Array of double using puthon-code size mechanism'
                },
                'name': 'arrayOut',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'self.get_array_size_for_python_code()'
                },
                'type': 'ViReal64[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetArraySizeForPythonCode': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'This function returns the size of the array for use in python-code size mechanism.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Size of array'
                },
                'name': 'sizeOut',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetArrayUsingIviDance': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'This function returns an array of float whose size is determined with the IVI dance.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the size of the buffer for copyint arrayOut onto.'
                },
                'name': 'arraySize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The array returned by this function'
                },
                'name': 'arrayOut',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'arraySize'
                },
                'type': 'ViReal64[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViBoolean': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Queries the value of a ViBoolean attribute.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'This is the channel(s) that this function will apply to.'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the value of the attribute.'
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
            'description': 'Queries the value of a ViInt32 attribute.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'This is the channel(s) that this function will apply to.'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the value of the attribute.'
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
            'description': 'Queries the value of a ViInt64 attribute.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'This is the channel(s) that this function will apply to.'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the value of the attribute.'
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
            'description': 'Queries the value of a ViReal attribute.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'This is the channel(s) that this function will apply to.'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the value of the attribute.'
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
            'description': 'Queries the value of a ViSession attribute.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'This is the channel(s) that this function will apply to.'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the value of the attribute.'
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
            'description': 'Queries the value of a ViBoolean attribute.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'This is the channel(s) that this function will apply to.'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of bytes in attributeValue. You can IVI-dance with this.'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the value of the attribute.'
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
    'GetAttributeWithOptionsViInt32': {
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
                'name': 'retrievalmode',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'attributeValue',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeWithOptionsViReal64': {
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
                'name': 'retrievalmode',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'attributeValue',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeWithOptionsViString': {
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
                'name': 'retrievalmode',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
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
    'GetCalDateAndTime': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Returns the date and time of the last calibration performed.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the type of calibration performed (external or self-calibration).'
                },
                'name': 'calType',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates the **month** of the last calibration.'
                },
                'name': 'month',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates the **day** of the last calibration.'
                },
                'name': 'day',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates the **year** of the last calibration.'
                },
                'name': 'year',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates the **hour** of the last calibration.'
                },
                'name': 'hour',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates the **minute** of the last calibration.'
                },
                'name': 'minute',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetCalInterval': {
        'documentation': {
            'description': 'Returns the recommended maximum interval, in **months**, between external calibrations.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Specifies the recommended maximum interval, in **months**, between external calibrations.'
                },
                'name': 'months',
                'python_api_converter_name': 'convert_month_to_timedelta',
                'type': 'ViInt32',
                'type_in_documentation': 'datetime.timedelta'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetChannelName': {
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
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'nameSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'name',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'nameSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetCustomType': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'This function returns a custom type.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Set using custom type'
                },
                'name': 'cs',
                'type': 'struct CustomStruct'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetCustomTypeArray': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'This function returns a custom type.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of elements in the array.'
                },
                'name': 'numberOfElements',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Get using custom type'
                },
                'name': 'cs',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfElements'
                },
                'type': 'struct CustomStruct[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetEnumValue': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns an enum value',
            'note': 'Splinter is not supported.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'This is an amount.',
                    'note': 'The amount will be between -2^31 and (2^31-1)'
                },
                'name': 'aQuantity',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates a ninja turtle',
                    'table_body': [
                        [
                            '0',
                            'Leonardo'
                        ],
                        [
                            '1',
                            'Donatello'
                        ],
                        [
                            '2',
                            'Raphael'
                        ],
                        [
                            '3',
                            'Mich elangelo'
                        ]
                    ]
                },
                'enum': 'Turtle',
                'name': 'aTurtle',
                'type': 'ViInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetError': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Returns the error information associated with the session.'
        },
        'is_error_handling': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns errorCode for the session. If you pass 0 for bufferSize, you can pass VI_NULL for this.'
                },
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of bytes in description buffer.'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'At least bufferSize big, string comes out here.'
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
    'GetErrorMessage': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Returns the errorMessage as a user-readable string. Uses IVI-dance'
        },
        'is_error_handling': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The error code returned for which you want to get a string.'
                },
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of bytes allocated for errorMessage'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Error information formatted into a user-readable string.'
                },
                'name': 'errorMessage',
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
    'GetLastCalDateAndTime': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': 'Returns the date and time of the last calibration performed.'
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
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the type of calibration performed (external or self-calibration).'
                },
                'name': 'calType',
                'type': 'ViInt32'
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
        'python_name': 'get_cal_date_and_time',
        'real_datetime_call': 'GetCalDateAndTime',
        'returns': 'ViStatus'
    },
    'InitWithOptions': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Creates a new IVI instrument driver session.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'caution': 'This is just some string.',
                    'description': 'Contains the **resource_name** of the device to initialize.'
                },
                'name': 'resourceName',
                'type': 'ViString'
            },
            {
                'default_value': False,
                'direction': 'in',
                'documentation': {
                    'description': 'NI-FAKE is probably not needed.',
                    'table_body': [
                        [
                            'VI_TRUE (default)',
                            '1',
                            'Perform ID Query'
                        ],
                        [
                            'VI_FALSE',
                            '0',
                            'Skip ID Query'
                        ]
                    ]
                },
                'name': 'idQuery',
                'type': 'ViBoolean',
                'use_in_python_api': False
            },
            {
                'default_value': False,
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies whether to reset',
                    'table_body': [
                        [
                            'VI_TRUE (default)',
                            '1',
                            'Reset Device'
                        ],
                        [
                            'VI_FALSE',
                            '0',
                            "Don't Reset"
                        ]
                    ]
                },
                'name': 'resetDevice',
                'type': 'ViBoolean'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Some options'
                },
                'name': 'optionString',
                'python_api_converter_name': 'convert_init_with_options_dictionary',
                'type': 'ViConstString',
                'type_in_documentation': 'dict'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns a ViSession handle that you use.'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'InitializeWithChannels': {
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
                'name': 'optionString',
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
    'Initiate': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Initiates a thingie.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'LockSession': {
        'documentation': {
            'description': 'Lock.'
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
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Optional'
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
    'MultipleArrayTypes': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Receives and returns multiple types of arrays.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Size of the array that will be returned.'
                },
                'name': 'outputArraySize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Array that will be returned.',
                    'note': 'The size must be at least outputArraySize.'
                },
                'name': 'outputArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'outputArraySize'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'An array of doubles with fixed size.'
                },
                'name': 'outputArrayOfFixedLength',
                'size': {
                    'mechanism': 'fixed',
                    'value': 3
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Size of inputArrayOfFloats and inputArrayOfIntegers'
                },
                'name': 'inputArraySizes',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Array of floats'
                },
                'name': 'inputArrayOfFloats',
                'size': {
                    'mechanism': 'len',
                    'value': 'inputArraySizes'
                },
                'type': 'ViReal64[]'
            },
            {
                'default_value': None,
                'direction': 'in',
                'documentation': {
                    'description': 'Array of integers. Optional. If passed in then size must match that of inputArrayOfFloats.'
                },
                'name': 'inputArrayOfIntegers',
                'size': {
                    'mechanism': 'len',
                    'value': 'inputArraySizes'
                },
                'type': 'ViInt16[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'MultipleArraysSameSize': {
        'documentation': {
            'description': 'Function to test multiple arrays that use the same size'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Array 1 of same size.'
                },
                'name': 'values1',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Array 2 of same size.'
                },
                'name': 'values2',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Array 3 of same size.'
                },
                'name': 'values3',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Array 4 of same size.'
                },
                'name': 'values4',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Size for all arrays'
                },
                'name': 'size',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'OneInputFunction': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'This function takes one parameter other than the session.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session. You obtain the **vi**'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Contains a number'
                },
                'name': 'aNumber',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'OneOutputFunction': {
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
                'name': 'aNumber',
                'type': 'ViInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'ParametersAreMultipleTypes': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Has parameters of multiple types.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Contains a boolean.'
                },
                'name': 'aBoolean',
                'type': 'ViBoolean'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Contains a 32-bit integer.'
                },
                'name': 'anInt32',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Contains a 64-bit integer.'
                },
                'name': 'anInt64',
                'type': 'ViInt64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Indicates a ninja turtle',
                    'table_body': [
                        [
                            '0',
                            'Leonardo'
                        ],
                        [
                            '1',
                            'Donatello'
                        ],
                        [
                            '2',
                            'Raphael'
                        ],
                        [
                            '3',
                            'Mich elangelo'
                        ]
                    ]
                },
                'enum': 'Turtle',
                'name': 'anIntEnum',
                'type': 'ViInt16'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The measured value.'
                },
                'name': 'aFloat',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'A float enum.'
                },
                'enum': 'FloatEnum',
                'name': 'aFloatEnum',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of bytes allocated for aString'
                },
                'name': 'stringSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'An IVI dance string.'
                },
                'name': 'aString',
                'size': {
                    'mechanism': 'len',
                    'value': 'stringSize'
                },
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'PoorlyNamedSimpleFunction': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'This function takes no parameters other than the session.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session. You obtain the **vi**'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'python_name': 'simple_function',
        'returns': 'ViStatus'
    },
    'Read': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Acquires a single measurement and returns the measured value.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the **maximum_time** allowed in seconds.'
                },
                'name': 'maximumTime',
                'python_api_converter_name': 'convert_timedelta_to_seconds',
                'type': 'ViReal64',
                'type_in_documentation': 'datetime.timedelta'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The measured value.'
                },
                'name': 'reading',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadFromChannel': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Acquires a single measurement and returns the measured value.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'This is the channel(s) that this function will apply to.'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the **maximum_time** allowed in microseconds.'
                },
                'name': 'maximumTime',
                'python_api_converter_name': 'convert_timedelta_to_microseconds',
                'type': 'ViInt32',
                'type_in_documentation': 'datetime.timedelta'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The measured value.'
                },
                'name': 'reading',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ResetAttribute': {
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
            }
        ],
        'returns': 'ViStatus'
    },
    'ReturnANumberAndAString': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns a number and a string.',
            'note': 'This function rules!'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Contains a number.'
                },
                'name': 'aNumber',
                'type': 'ViInt16'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Contains a string. Buffer must be 256 bytes or larger.'
                },
                'name': 'aString',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReturnMultipleTypes': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns multiple types.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Contains a boolean.'
                },
                'name': 'aBoolean',
                'type': 'ViBoolean'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Contains a 32-bit integer.'
                },
                'name': 'anInt32',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Contains a 64-bit integer.'
                },
                'name': 'anInt64',
                'type': 'ViInt64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates a ninja turtle',
                    'table_body': [
                        [
                            '0',
                            'Leonardo'
                        ],
                        [
                            '1',
                            'Donatello'
                        ],
                        [
                            '2',
                            'Raphael'
                        ],
                        [
                            '3',
                            'Mich elangelo'
                        ]
                    ]
                },
                'enum': 'Turtle',
                'name': 'anIntEnum',
                'type': 'ViInt16'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The measured value.'
                },
                'name': 'aFloat',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'A float enum.'
                },
                'enum': 'FloatEnum',
                'name': 'aFloatEnum',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of measurements to acquire.'
                },
                'name': 'arraySize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'An array of measurement values.',
                    'note': 'The size must be at least arraySize.'
                },
                'name': 'anArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arraySize'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of bytes allocated for aString'
                },
                'name': 'stringSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'An IVI dance string.'
                },
                'name': 'aString',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'stringSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViBoolean': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'This function sets the value of a ViBoolean attribute.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'This is the channel(s) that this function will apply to.'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value that you want to set the attribute to.'
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
            'description': 'This function sets the value of a ViInt32 attribute.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'This is the channel(s) that this function will apply to.'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value that you want to set the attribute to.'
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
            'description': 'This function sets the value of a ViInt64 attribute.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'This is the channel(s) that this function will apply to.'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value that you want to set the attribute to.'
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
            'description': 'This function sets the value of a ViReal64 attribute.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'This is the channel(s) that this function will apply to.'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value that you want to set the attribute to.'
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
            'description': 'This function sets the value of a ViSession attribute.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'This is the channel(s) that this function will apply to.'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value that you want to set the attribute to.'
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
            'description': 'This function sets the value of a ViString attribute.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'This is the channel(s) that this function will apply to.'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value that you want to set the attribute to.'
                },
                'name': 'attributeValue',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetCustomType': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'This function takes a custom type.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Set using custom type'
                },
                'name': 'cs',
                'type': 'struct CustomStruct'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetCustomTypeArray': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'This function takes an array of custom types.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of elements in the array.'
                },
                'name': 'numberOfElements',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Set using custom type'
                },
                'name': 'cs',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfElements'
                },
                'type': 'struct CustomStruct[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'TwoInputFunction': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'This function takes two parameters other than the session.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session. You obtain the **vi**'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Contains a number'
                },
                'name': 'aNumber',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Contains a string'
                },
                'name': 'aString',
                'type': 'ViString'
            }
        ],
        'returns': 'ViStatus'
    },
    'UnlockSession': {
        'documentation': {
            'description': 'Unlock'
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
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Optional'
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
    'Use64BitNumber': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns a number and a string.',
            'note': 'This function rules!'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'A big number on its way in.'
                },
                'name': 'input',
                'type': 'ViInt64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'A big number on its way out.'
                },
                'name': 'output',
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteWaveform': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Writes waveform to the driver'
        },
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            },
            {
                'documentation_filename': 'numpy_method',
                'method_python_name_suffix': '_numpy',
                'session_filename': 'numpy_write_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'How many samples the waveform contains.'
                },
                'name': 'numberOfSamples',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Waveform data.'
                },
                'name': 'waveform',
                'numpy': True,
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfSamples'
                },
                'type': 'ViReal64[]',
                'use_array': True
            }
        ],
        'returns': 'ViStatus'
    },
    'close': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Closes the specified session and deallocates resources that it reserved.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
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
            'description': 'Takes the errorCode returned by a functiona and returns it as a user-readable string.'
        },
        'is_error_handling': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The errorCode returned from the instrument.'
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
            'description': 'Performs a self-test'
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
                    'description': 'Identifies a particular instrument session. You obtain the **vi** parameter from niDMM_init or niDMM_InitWithOptions.'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'python_name': 'self_test',
        'returns': 'ViStatus'
    },
    'self_test': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Performs a self-test.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session. You obtain the **vi** parameter from niFake_InitWithOptions.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Contains the value returned from the instrument self-test. Zero indicates success.'
                },
                'name': 'selfTestResult',
                'type': 'ViInt16'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'This parameter contains the string returned from the instrument self-test. The array must contain at least 256 elements.'
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
