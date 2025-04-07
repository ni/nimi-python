# -*- coding: utf-8 -*-
# This file is generated from NI-RFSG API metadata version 25.5.0d9999
functions = {
    'Abort': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Stops signal generation.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'AllocateArbWaveform': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Allocates onboard memory space for the arbitrary waveform. Use this function to specify the total size of a waveform before writing the data. Use this function only if you are calling the niRFSG_WriteArbWaveform function multiple times to write a large waveform in smaller blocks. The NI-RFSG device must be in the Configuration state before you call this function.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name used to identify the waveform. This string is case-insensitive and alphanumeric, and it does not use reserved words.'
                },
                'name': 'waveformName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of samples to reserve in the onboard memory for the specified waveform. Each I/Q pair is considered one sample.'
                },
                'name': 'sizeInSamples',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ChangeExternalCalibrationPassword': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Changes the external calibration password of the device.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the old (current) external calibration password. This password is case sensitive.'
                },
                'name': 'oldPassword',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the new (desired) external calibration password.'
                },
                'name': 'newPassword',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'CheckAttributeViBoolean': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Checks the validity of a value you specify for a ViBoolean attribute.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attribute',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value that you want to verify as a valid value for the attribute.'
                },
                'name': 'value',
                'type': 'ViBoolean',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'CheckAttributeViInt32': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Checks the validity of a value you specify for a ViInt32 attribute.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attribute',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value that you want to verify as a valid value for the attribute.'
                },
                'grpc_enum': 'NiRFSGInt32AttributeValues',
                'name': 'value',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'CheckAttributeViInt64': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Checks the validity of a value you specify for a ViInt64 attribute.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attribute',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value that you want to verify as a valid value for the attribute.'
                },
                'grpc_enum': 'NiRFSGInt64AttributeValues',
                'name': 'value',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'CheckAttributeViReal64': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Checks the validity of a value you specify for a ViReal64 attribute.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attribute',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value that you want to verify as a valid value for the attribute.'
                },
                'grpc_enum': 'NiRFSGReal64AttributeValues',
                'name': 'value',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'CheckAttributeViSession': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Checks the validity of a value you specify for a ViSession attribute.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attribute',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value that you want to verify as a valid value for the attribute.'
                },
                'name': 'value',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'CheckAttributeViString': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Checks the validity of a value you specify for a ViString attribute.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attribute',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value that you want to verify as a valid value for the attribute. The value must be a NULL-terminated string.'
                },
                'grpc_mapped_enum': 'NiRFSGStringAttributeValuesMapped',
                'name': 'value',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'CheckGenerationStatus': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Checks the status of the generation. Call this function to check for any errors that might occur during the signal generation or to check whether the device has finished generating.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns information about the completion of signal generation.'
                },
                'name': 'isDone',
                'type': 'ViBoolean',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'CheckIfScriptExists': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns whether the script that you specify as NIRFSG_ATTR_SCRIPT_NAME exists.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the script. This string is case-insensitive.'
                },
                'name': 'scriptName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns VI_TRUE if the script exists.'
                },
                'name': 'scriptExists',
                'type': 'ViBoolean',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'CheckIfWaveformExists': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns whether the waveform that you specify as NIRFSG_ATTR_WAVEFORM_NAME exists.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name used to store the waveform. This string is case-insensitive.'
                },
                'name': 'waveformName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns VI_TRUE if the waveform exists.'
                },
                'name': 'waveformExists',
                'type': 'ViBoolean',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ClearAllArbWaveforms': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Deletes all currently defined waveforms and scripts. The NI-RFSG device must be in the Configuration state before you call this function.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ClearArbWaveform': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Deletes a specified waveform from the pool of currently defined waveforms. The NI-RFSG device must be in the Configuration state before you call this function.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Name of the stored waveform to delete.'
                },
                'name': 'name',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ClearError': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Clears the error information associated with the session. If you pass VI_NULL for the NIRFSG_ATTR_VI parameter, this function clears the error information for the current execution thread.',
            'note': 'The niRFSG_GetError function clears the error information after it is retrieved. A call to the niRFSG_ClearError function is necessary only when you do not use a call to the niRFSG_GetError function to retrieve error information.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ClearSelfCalibrateRange': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Clears the data obtained from the niRFSG_SelfCalibrateRange function.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'Commit': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Programs the device with the correct settings. Calling this function moves the NI-RFSG device from the Configuration state to the Committed state. After this function executes, a change to any attribute reverts the NI-RFSG device to the Configuration state.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ConfigureDeembeddingTableInterpolationLinear': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Selects the linear interpolation method. If the carrier frequency does not match a row in the de-embedding table, NI-RFSG performs a linear interpolation based on the entries in the de-embedding table to determine the parameters to use for de-embedding.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is '' (empty string)."
                },
                'name': 'port',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the table.'
                },
                'name': 'tableName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the format of parameters to interpolate.'
                },
                'enum': 'Format',
                'name': 'format',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ConfigureDeembeddingTableInterpolationNearest': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Selects the nearest interpolation method. NI-RFSG uses the parameters of the table nearest to the carrier frequency for de-embedding.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is '' (empty string)."
                },
                'name': 'port',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the table.'
                },
                'name': 'tableName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ConfigureDeembeddingTableInterpolationSpline': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Selects the spline interpolation method. If the carrier frequency does not match a row in the de-embedding table, NI-RFSG performs a spline interpolation based on the entries in the de-embedding table to determine the parameters to use for de-embedding.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is '' (empty string)."
                },
                'name': 'port',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the table.'
                },
                'name': 'tableName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ConfigureDigitalEdgeScriptTrigger': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Configures the specified Script Trigger for digital edge triggering. The NI-RFSG device must be in the Configuration state before calling this function.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the Script Trigger to configure.'
                },
                'name': 'triggerId',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the source terminal for the digital edge Script Trigger. NI-RFSG sets the NIRFSG_ATTR_DIGITAL_EDGE_SCRIPT_TRIGGER_SOURCE attribute to this value.'
                },
                'name': 'source',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the active edge for the digital edge Script Trigger. NI-RFSG sets the NIRFSG_ATTR_DIGITAL_EDGE_SCRIPT_TRIGGER_EDGE attribute to this value.'
                },
                'name': 'edge',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ConfigureDigitalEdgeStartTrigger': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Configures the Start Trigger for digital edge triggering. The NI-RFSG device must be in the Configuration state before calling this function.',
            'note': 'For the PXIe-5654/5654 with PXIe-5696, the Start Trigger is valid only with a timer-based list when RF list mode is enabled.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the source terminal for the digital edge trigger. NI-RFSG sets the NIRFSG_ATTR_DIGITAL_EDGE_START_TRIGGER_SOURCE attribute to this value.'
                },
                'name': 'source',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the active edge for the Start Trigger. NI-RFSG sets the NIRFSG_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE attribute to this value.'
                },
                'name': 'edge',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ConfigureDigitalLevelScriptTrigger': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Configures a specified Script Trigger for digital level triggering. The NI-RFSG device must be in the Configuration state before calling this function.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the Script Trigger to configure.'
                },
                'name': 'triggerId',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the trigger source terminal for the digital level Script Trigger. NI-RFSG sets the NIRFSG_ATTR_DIGITAL_LEVEL_SCRIPT_TRIGGER_SOURCE attribute to this value.'
                },
                'name': 'source',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the active level for the digital level Script Trigger. NI-RFSG sets the NIRFSG_ATTR_DIGITAL_LEVEL_SCRIPT_TRIGGER_ACTIVE_LEVEL attribute to this value.'
                },
                'name': 'level',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ConfigureDigitalModulationUserDefinedWaveform': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the message signal used for digital modulation when the NIRFSG_ATTR_DIGITAL_MODULATION_WAVEFORM_TYPE attribute is set to NIRFSG_VAL_USER_DEFINED.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of samples in the message signal.'
                },
                'name': 'numberOfSamples',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the user-defined message signal used for digital modulation.'
                },
                'name': 'userDefinedWaveform',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfSamples'
                },
                'type': 'ViInt8[]',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ConfigureGenerationMode': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Configures the NI-RFSG device to generate a continuous sine tone (CW), apply I/Q (vector) modulation to the RF output signal, or generate arbitrary waveforms according to scripts. The NI-RFSG device must be in the Configuration state before you call this function.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the mode used by NI-RFSG for generating an RF output signal.'
                },
                'name': 'generationMode',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ConfigureOutputEnabled': {
        'codegen_method': 'public',
        'documentation': {
            'description': ' Enables or disables signal output. Setting NIRFSG_ATTR_OUTPUT_ENABLED to VI_FALSE while in the Generation state attenuates the generated signal so that no signal is output.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies whether you want to enable or disable the output.'
                },
                'name': 'outputEnabled',
                'type': 'ViBoolean',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ConfigureP2PEndpointFullnessStartTrigger': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Configures the Start Trigger to detect peer-to-peer endpoint fullness. Generation begins when the number of samples in the peer-to-peer endpoint reaches the threshold specified by the NIRFSG_ATTR_P2P_ENDPOINT_FULLNESS_LEVEL parameter. The NI-RFSG device must be in the Configuration state before calling this function.',
            'note': 'Due to an additional internal FIFO in the RF signal generator, the writer peer actually writes 2,304 bytes more than the quantity of data specified by this function to satisfy the trigger level.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the quantity of data in the FIFO endpoint that asserts the trigger. Units are samples per channel. The default value is -1, which allows NI-RFSG to select the appropriate fullness value.'
                },
                'name': 'p2pEndpointFullnessLevel',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ConfigurePowerLevelType': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the way the driver interprets the NIRFSG_ATTR_POWER_LEVEL attribute. In average power mode, NI-RFSG automatically scales waveform data to use the maximum dynamic range. In peak power mode, waveforms are scaled according to the NIRFSG_ATTR_ARB_WAVEFORM_SOFTWARE_SCALING_FACTOR attribute.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the way the driver interprets the value of the NIRFSG_ATTR_POWER_LEVEL attribute. NI-RFSG sets the NIRFSG_ATTR_POWER_LEVEL_TYPE attribute to this value.'
                },
                'name': 'powerLevelType',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ConfigurePxiChassisClk10': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the signal to drive the 10MHz Reference Clock on the PXI backplane. This option can only be configured when the PXI-5610 is in Slot 2 of the PXI chassis. The NI-RFSG device must be in the Configuration state before you call this function.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the source of the Reference Clock signal.'
                },
                'name': 'pxiClk10Source',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ConfigureRF': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Configures the frequency and power level of the RF output signal. The PXI-5670/5671, PXIe-5672, and PXIe-5860 device must be in the Configuration state before calling this function. The PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5654/5654 with PXIe-5696, PXIe-5673/5673E, and PXIe-5830/5831/5832/5840/5841/5842 device can be in the Configuration or Generation state when you call this function.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the frequency of the generated RF signal, in hertz. For arbitrary waveform generation, this parameter specifies the center frequency of the signal.'
                },
                'name': 'frequency',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies either the average power level or peak power level of the generated RF signal, depending on the NIRFSG_ATTR_POWER_LEVEL_TYPE attribute.'
                },
                'name': 'powerLevel',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ConfigureRefClock': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Configures the NI-RFSG device Reference Clock. The Reference Clock ensures that the NI-RFSG devices are operating from a common timebase. The NI-RFSG device must be in the Configuration state before calling this function.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the source of Reference Clock signal.'
                },
                'name': 'refClockSource',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the Reference Clock rate, in hertz (Hz), of the signal present at the REF IN or CLK IN connector. The default value is NIRFSG_VAL_AUTO, which allows NI-RFSG to use the default Reference Clock rate for the device or automatically detect the Reference Clock rate, if supported. This parameter is only valid when the NIRFSG_ATTR_REF_CLOCK_SOURCE parameter is set to NIRFSG_VAL_CLK_IN_STR, NIRFSG_VAL_REF_IN_STR or NIRFSG_VAL_REF_IN_2_STR. Refer to the NIRFSG_ATTR_REF_CLOCK_RATE attribute for possible values.'
                },
                'name': 'refClockRate',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ConfigureSignalBandwidth': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Configures the signal bandwidth of the arbitrary waveform. The NI-RFSG device must be in the Configuration state before you call this function. Based on your signal bandwidth, NI-RFSG decides whether to configure the upconverter center frequency on the PXI-5670/5671 or PXIe-5672 in increments of 1MHz or 5MHz. Failure to configure signal bandwidth may result in the signal being placed outside the upconverter passband.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the signal bandwidth used by NI-RFSG to generate an RF output signal. NI-RFSG sets the NIRFSG_ATTR_SIGNAL_BANDWIDTH attribute to this value.'
                },
                'name': 'signalBandwidth',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ConfigureSoftwareScriptTrigger': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Configures the Script Trigger for software triggering. Refer to the niRFSG_SendSoftwareEdgeTrigger function for more information about using the software Script Trigger. The NI-RFSG device must be in the Configuration state before calling this function.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the Script Trigger to configure.'
                },
                'name': 'triggerId',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ConfigureSoftwareStartTrigger': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Configures the Start Trigger for software triggering. Refer to the niRFSG_SendSoftwareEdgeTrigger function for more information about using a software trigger. The NI-RFSG device must be in the Configuration state before calling this function.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'CreateDeembeddingSparameterTableS2PFile': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Creates an S-parameter de-embedding table for the port based on the specified S2P file.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'yet to be defined'
                },
                'name': 'port',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'yet to be defined'
                },
                'name': 'tableName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'yet to be defined'
                },
                'name': 's2pFilePath',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'yet to be defined'
                },
                'name': 'sparameterOrientation',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'DeleteAllDeembeddingTables': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Deletes all configured de-embedding tables for the session.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'DeleteDeembeddingTable': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Deletes the selected de-embedding table for a given port.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is '' (empty string)."
                },
                'name': 'port',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the table.'
                },
                'name': 'tableName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'Disable': {
        'codegen_method': 'public',
        'documentation': {
            'description': ' Places the instrument in a quiescent state where it has minimal or no impact on the system to which it is connected.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'DisableScriptTrigger': {
        'codegen_method': 'public',
        'documentation': {
            'description': ' Configures the device not to wait for the specified Script Trigger. Call this function only if you previously configured a Script Trigger and now want it disabled. The NI-RFSG device must be in the Configuration state before you call this function.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the Script trigger to configure.'
                },
                'name': 'triggerId',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'DisableStartTrigger': {
        'codegen_method': 'public',
        'documentation': {
            'description': ' Configures the device not to wait for a Start Trigger. This function is necessary only if you previously configured a Start Trigger and now want it disabled. The NI-RFSG device must be in the Configuration state before calling this function.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ExportSignal': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Routes signals (triggers, clocks, and events) to a specified output terminal. The NI-RFSG device must be in the Configuration state before you call this function.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': ' Specifies the type of signal to route.'
                },
                'name': 'signal',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "Specifies which instance of the selected signal to export. This parameter is useful when you set the NIRFSG_ATTR_SIGNAL parameter to NIRFSG_VAL_SCRIPT_TRIGGER or NIRFSG_VAL_MARKER_EVENT. Otherwise, set the NIRFSG_ATTR_SIGNAL_IDENTIFIER parameter to '' (empty string)."
                },
                'name': 'signalIdentifier',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the terminal where the signal is exported. You can choose not to export any signal. For the PXIe-5841 with PXIe-5655, the signal is exported to the terminal on the PXIe-5841.'
                },
                'name': 'outputTerminal',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'GetAttributeViBoolean': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Queries the value of a ViBoolean attribute.Use this low-level function to get the values of inherent IVI attributes, class-defined attributes, and instrument-specific attributes.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attribute',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the current value of the attribute. Pass the address of a ViBoolean variable.'
                },
                'name': 'value',
                'type': 'ViBoolean',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'GetAttributeViInt32': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Queries the value of a ViInt32 attribute. Use this low-level function to get the values of inherent IVI attributes, class-defined attributes, and instrument-specific attributes.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attribute',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the current value of the attribute. Pass the address of a ViInt32 variable.'
                },
                'name': 'value',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'GetAttributeViInt64': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Queries the value of a ViInt64 attribute.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attribute',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the current value of the attribute. Pass the address of a ViInt64 variable.'
                },
                'name': 'value',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'GetAttributeViReal64': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Queries the value of a ViReal64 attribute.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attribute',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the current value of the attribute. Pass the address of a ViReal64 variable.'
                },
                'name': 'value',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'GetAttributeViSession': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Queries the value of a ViSession attribute.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attribute',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the current value of the attribute. Pass the address of a ViSession variable.'
                },
                'name': 'value',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'GetAttributeViString': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Queries the value of a ViString attribute.Use this low-level function to get the values of inherent IVI attributes, class-defined attributes, and instrument-specific attributes.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attribute',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the number of bytes in the ViChar buffer you specify for the **waveformNames** parameter.'
                },
                'name': 'bufSize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The buffer in which the function returns the current value of the attribute. The buffer must be of type ViChar and have at least as many bytes as indicated in the **bufferSize** parameter.'
                },
                'name': 'value',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufSize'
                },
                'type': 'ViChar[]',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'GetError': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Retrieves and then clears the IVI error information for the session or the current execution thread.',
            'note': 'If the **bufferSize** parameter is 0, this function does not clear the error information. By passing 0 to the **bufferSize** parameter, you can determine the buffer size required to obtain the entire NIRFSG_ATTR_ERROR_DESCRIPTION string. You can then call this function again with a sufficiently large buffer. If you specify a valid IVI session for the NIRFSG_ATTR_VI parameter, this function retrieves and clears the error information for the session. If you pass VI_NULL for the NIRFSG_ATTR_VI parameter, this function retrieves and clears the error information for the current execution thread. If the NIRFSG_ATTR_VI parameter is an invalid session, this function does nothing and returns an error. Normally, the error information describes the first error that occurred since the user last called this function or the niRFSG_ClearError function.'
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
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the error code for the session or execution thread. If you pass 0 for the **BufferSize** parameter, you can pass VI_NULL for this parameter.'
                },
                'name': 'errorCode',
                'type': 'ViStatus',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'default_value': '256',
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the number of bytes in the ViChar array you specify for the **description** parameter.'
                },
                'name': 'errorDescriptionBufferSize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the NIRFSG_ATTR_ERROR_DESCRIPTION for the IVI session or execution thread.'
                },
                'name': 'errorDescription',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'errorDescriptionBufferSize'
                },
                'type': 'ViChar[]',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'GetExternalCalibrationLastDateAndTime': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Returns the date and time of the last successful external calibration. The time returned is 24-hour (military) local time; for example, if the device was calibrated at 2:30PM, this function returns 14 for the hours parameter and 30 for the minutes parameter.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_name_for_documentation': 'get_external_calibration_last_date_and_time',
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the year of the last successful calibration.'
                },
                'name': 'year',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the month of the last successful calibration.'
                },
                'name': 'month',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the day of the last successful calibration.'
                },
                'name': 'day',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the hour of the last successful calibration.'
                },
                'name': 'hour',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the minute of the last successful calibration.'
                },
                'name': 'minute',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the second of the last successful calibration.'
                },
                'name': 'second',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'GetLastExtCalLastDateAndTime': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': 'TBD'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '',
                'session_filename': 'datetime_wrappers'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'name': 'lastCalDatetime',
                'type': 'hightime.datetime'
            }
        ],
        'python_name': 'get_external_calibration_last_date_and_time',
        'real_datetime_call': 'GetExternalCalibrationLastDateAndTime',
        'returns': 'ViStatus'
    },
    'GetLastSelfCalLastDateAndTime': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': 'TBD'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '',
                'session_filename': 'datetime_wrappers'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'name': 'lastCalDatetime',
                'type': 'hightime.datetime'
            }
        ],
        'python_name': 'get_self_calibration_last_date_and_time',
        'real_datetime_call': 'GetSelfCalibrationDateAndTime',
        'returns': 'ViStatus'
    },
    'GetMaxSettablePower': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the maximum settable output power level for the current configuration.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns maximum settable power level in dBm.'
                },
                'name': 'value',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'GetSelfCalibrationDateAndTime': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Returns the date and time of the last successful self-calibration. The time returned is 24-hour local time. For example, if the device was calibrated at 2:30PM, this function returns 14 for the hours parameter and 30 for the minutes parameter.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_name_for_documentation': 'get_self_calibration_date_and_time',
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies from which stand-alone module to retrieve the last successful self-calibration date and time.'
                },
                'name': 'module',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the year of the last successful calibration.'
                },
                'name': 'year',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the month of the last successful calibration.'
                },
                'name': 'month',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the day of the last successful calibration.'
                },
                'name': 'day',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the hour of the last successful calibration.'
                },
                'name': 'hour',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the minute of the last successful calibration.'
                },
                'name': 'minute',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the second of the last successful calibration.'
                },
                'name': 'second',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'GetSelfCalibrationTemperature': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the temperature, in degrees Celsius, of the device at the last successful self-calibration.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies from which stand-alone module to retrieve the last successful self-calibration temperature.'
                },
                'name': 'module',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the temperature, in degrees Celsius, of the device at the last successful self-calibration.'
                },
                'name': 'temperature',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'GetStreamEndpointHandle': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns a reader endpoint handle that can be used with NI-P2P to configure a peer-to-peer stream with an RF signal generator endpoint.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the stream endpoint FIFO to configure.'
                },
                'name': 'streamEndpoint',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the reader endpoint handle that is used with NI-P2P to create a stream with the NI-RFSG device as an endpoint.'
                },
                'name': 'readerHandle',
                'type': 'ViUInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'GetWaveformBurstStartLocations': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Returns the burst start locations of the waveform stored in the NI-RFSG session.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "Specifies the waveform name and the marker name. Example: 'waveform::waveform0/marker0'"
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the size of the burst start locations array.'
                },
                'name': 'numberOfLocations',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the burst start locations stored in the NI-RFSG session for the waveform that you specified in the NIRFSG_ATTR_CHANNEL_NAME parameter. This value is expressed in samples.'
                },
                'name': 'locations',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the required size for the output array if you pass NULL to NIRFSG_ATTR_LOCATIONS parameter.'
                },
                'name': 'requiredSize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'GetWaveformBurstStopLocations': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Returns the burst stop locations of the waveform stored in the NI-RFSG session.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "Specifies the waveform name and the marker name. Example: 'waveform::waveform0/marker0'"
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the size of the burst start locations array.'
                },
                'name': 'numberOfLocations',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the burst start locations stored in the NI-RFSG session for the waveform that you specified in the NIRFSG_ATTR_CHANNEL_NAME parameter. This value is expressed in samples.'
                },
                'name': 'locations',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the required size for the output array if you pass NULL to NIRFSG_ATTR_LOCATIONS parameter.'
                },
                'name': 'requiredSize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'GetWaveformMarkerEventLocations': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Returns the marker locations associated with the waveform and the marker stored in the NI-RFSG session.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the size of the locations array.'
                },
                'name': 'numberOfLocations',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the marker locations stored in the NI-RFSG database for the channel you specified in the NIRFSG_ATTR_CHANNEL_NAME parameter. This value is expressed in samples.'
                },
                'name': 'locations',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the required size for the output array if you pass NULL to **Locations** parameter.'
                },
                'name': 'requiredSize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'InitWithOptions': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Opens a session to the device you specify as the NIRFSG_ATTR_RESOURCE_NAME and returns a ViSession handle that you use to identify the NI-RFSG device in all subsequent NI-RFSG function calls. This function also configures the device through the NIRFSG_ATTR_OPTION_STRING input.',
            'note': 'For multichannel devices such as the PXIe-5860, the resource name must include the channel number to use. The channel number is specified by appending /*ChannelNumber* to the device name, where *ChannelNumber* is the channel number (0, 1, etc.). For example, if the device name is PXI1Slot2 and you want to use channel 0, use the resource name PXI1Slot2/0.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_name_for_documentation': '__init__',
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'initialization_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the resource name of the device to initialize.'
                },
                'name': 'resourceName',
                'type': 'ViRsrc',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies whether you want NI-RFSG to perform an ID query.'
                },
                'name': 'idQuery',
                'type': 'ViBoolean',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies whether you want to reset the NI-RFSG device during the initialization procedure.'
                },
                'name': 'resetDevice',
                'type': 'ViBoolean',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the initial value of certain attributes for the session. The following table lists the attributes and the name you pass in this parameter to identify the attribute.'
                },
                'name': 'optionString',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns a ViSession handle that you use to identify the NI-RFSG device in all subsequent NI-RFSG function calls.'
                },
                'name': 'newVi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'Initiate': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Initiates signal generation, causing the NI-RFSG device to leave the Configuration state and enter the Generation state. If the settings have not been committed to the device before you call this function, they are committed by this function. The operation returns when the RF output signal settles. To return to the Configuration state, call the niRFSG_Abort function.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'LoadConfigurationsFromFile': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Loads the configurations from the specified file to the NI-RFSG driver session. The VI does an implicit reset before loading the configurations from the file.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the absolute path of the file from which the NI-RFSG loads the configurations.'
                },
                'name': 'filePath',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'LockSession': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Obtains a multithread lock on the instrument session. Before doing so, this function waits until all other execution threads have released their locks on the instrument session.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'lock',
                'library_interpreter_filename': 'lock',
                'method_python_name_suffix': '',
                'session_filename': 'lock'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Keeps track of whether you obtain a lock and therefore need to unlock the session. Pass the address of a local ViBoolean variable. In the declaration of the local variable, initialize it to VI_FALSE. Pass the address of the same local variable to any other calls you make to the niRFSG_LockSession function or the niRFSG_UnlockSession function in the same function.'
                },
                'name': 'callerHasLock',
                'type': 'ViBoolean',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'python_name': 'lock',
        'render_in_session_base': True,
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'PerformPowerSearch': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Performs a power search if the NIRFSG_ATTR_ALC_CONTROL attribute is disabled. Calling this function disables modulation for a short time while the device levels the output signal.',
            'note': 'Power search temporarily enables the ALC, so ensure the appropriate included cable is connected between the PXIe-5654 ALCIN connector and the PXIe-5696 ALCOUT connector to successfully perform a power search.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'PerformThermalCorrection': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Corrects for any signal drift due to environmental temperature variation when generating the same signal for extended periods of time without a parameter change. Under normal circumstances of short-term signal generation, NI-RFSG performs thermal correction automatically by ensuring stable power levels, and you do not need to call this function.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'QueryArbWaveformCapabilities': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Queries and returns the waveform capabilities of the NI-RFSG device. These capabilities are related to the current device configuration. The NI-RFSG device must be in the Configuration or the Generation state before calling this function.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the value of the NIRFSG_ATTR_ARB_MAX_NUMBER_WAVEFORMS attribute. This value is the maximum number of waveforms you can write.'
                },
                'name': 'maxNumberWaveforms',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the value of the NIRFSG_ATTR_ARB_WAVEFORM_QUANTUM attribute. If the waveform quantum is *q*, then the size of the waveform that you write should be a multiple of *q*. The units are expressed in samples.'
                },
                'name': 'waveformQuantum',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the value of the NIRFSG_ATTR_ARB_WAVEFORM_SIZE_MIN attribute. The number of samples of the waveform that you write must be greater than or equal to this value.'
                },
                'name': 'minWaveformSize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the value of the NIRFSG_ATTR_ARB_WAVEFORM_SIZE_MAX attribute. The number of samples of the waveform that you write must be less than or equal to this value.'
                },
                'name': 'maxWaveformSize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ReadAndDownloadWaveformFromFileTDMS': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Reads the waveforms from a TDMS file and downloads one waveform into each of the NI RF vector signal generators.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name used to store the waveform. This string is case-insensitive.'
                },
                'name': 'waveformName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the absolute path to the TDMS file from which the NI-RFSG reads the waveforms.'
                },
                'name': 'filePath',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the index of the waveform to be read from the TDMS file.'
                },
                'name': 'waveformIndex',
                'type': 'ViUInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'Reset': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Resets all attributes to their default values and moves the NI-RFSG device to the Configuration state. This function aborts the generation, deletes all de-embedding tables, clears all routes, and resets session attributes to their initial values. During a reset, routes of signals between this and other devices are released, regardless of which device created the route.',
            'note': 'This function resets all configured routes for the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842/5860 in NI-RFSA and NI-RFSG.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ResetAttribute': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Resets the attribute to its default value.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ResetDevice': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Performs a hard reset on the device.',
            'note': 'You must call the niRFSG_ResetDevice function if the NI-RFSG device has shut down because of a high-temperature condition.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ResetWithDefaults': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Performs a software reset of the device, returning it to the default state and applying any initial default settings from the IVI Configuration Store.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'SaveConfigurationsToFile': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Saves the configurations of the session to the specified file.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the absolute path of the file to which the NI-RFSG saves the configurations.'
                },
                'name': 'filePath',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'SelectArbWaveform': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the waveform that is generated upon a call to the niRFSG_Initiate function when the **generationMode** parameter of the niRFSG_ConfigureGenerationMode function is set to NIRFSG_VAL_ARB_WAVEFORM. You must specify a waveform using the NIRFSG_ATTR_NAME parameter if you have written multiple waveforms. The NI-RFSG device must be in the Configuration state before you call this function.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the stored waveform to generate. This is a case-insensitive alphanumeric string that does not use reserved words. NI-RFSG sets the NIRFSG_ATTR_ARB_SELECTED_WAVEFORM attribute to this value.'
                },
                'name': 'name',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'SelfCal': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Performs an internal self-calibration on the device and associated modules that support self-calibration. If the calibration is successful, new calibration data and constants are stored in the onboard nonvolatile memory of the module.',
            'note': 'If there is an existing NI-RFSA session open for the same PXIe-5820/5830/5831/5832/5840/5841/5842/5860 while this function runs, it may remain open but cannot be used for operations that access the hardware, for example niRFSA_Commit or niRFSA_Initiate.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'SelfCalibrateRange': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Self-calibrates all configurations within the specified frequency and peak power level limits.',
            'note': 'If there is an existing NI-RFSA session open for the same PXIe-5820/5830/5831/5832/5840/5841/5842 while this function runs, it may remain open but cannot be used for operations that access the hardware, for example niRFSA_Commit or niRFSA_Initiate.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies which calibration steps to skip during the self-calibration process. The default value is an empty array, which indicates that no calibration steps are omitted.'
                },
                'name': 'stepsToOmit',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the minimum frequency to calibrate.'
                },
                'name': 'minFrequency',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the maximum frequency to calibrate.'
                },
                'name': 'maxFrequency',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the minimum power level to calibrate.'
                },
                'name': 'minPowerLevel',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the maximum power level to calibrate.'
                },
                'name': 'maxPowerLevel',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'SelfTest': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Performs a self-test on the NI-RFSG device and returns the test results. This function performs a simple series of tests to ensure that the NI-RFSG device is powered up and responding.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'This parameter contains the value returned from the NI-RFSG device self test.'
                },
                'name': 'selfTestResult',
                'type': 'ViInt16'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Returns the self-test response string from the NI-RFSG device. For an explanation of the string contents, refer to the **status** parameter of this function.'
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
    },
    'SendSoftwareEdgeTrigger': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Forces a trigger to occur. The specified trigger generates regardless of whether the trigger has been configured as a software trigger.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the trigger to send.'
                },
                'name': 'trigger',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "Specifies the Script Trigger to configure. This parameter is valid only when you set the NIRFSG_ATTR_TRIGGER parameter to NIRFSG_VAL_START_TRIGGER. Otherwise, set the NIRFSG_ATTR_TRIGGER_IDENTIFIER parameter to '' (empty string)."
                },
                'name': 'triggerIdentifier',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'render_in_session_base': True,
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'SetArbWaveformNextWritePosition': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Configures the start position to use for writing a waveform before calling the niRFSG_WriteArbWaveform function. This function allows you to write to arbitrary locations within the waveform. These settings apply only to the next write to the waveform specified by the **name** input of the niRFSG_AllocateArbWaveform function or the niRFSG_WriteArbWaveform function. Subsequent writes to that waveform begin where the last write ended, unless this function is called again.',
            'note': 'If you use this function to write the waveform that is currently generating, an undefined output may result.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the waveform. This string is case-insensitive and alphanumeric, and it cannot use `reserved words <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/scripting_instructions.html>`_ '
                },
                'name': 'waveformName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the reference position in the waveform. The position and NIRFSG_ATTR_OFFSET together determine where to start loading data into the waveform.'
                },
                'name': 'relativeTo',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the offset from the **relative to** parameter at which to start loading the data into the waveform.'
                },
                'name': 'offset',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'SetAttributeViBoolean': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Sets the value of a ViBoolean attribute.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attribute',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value to which you want to set the attribute.'
                },
                'name': 'value',
                'type': 'ViBoolean',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'SetAttributeViInt32': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Sets the value of a ViInt32 attribute.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attribute',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the value to which you want to set the attribute.'
                },
                'grpc_enum': 'NiRFSGInt32AttributeValues',
                'name': 'value',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'SetAttributeViInt64': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Sets the value of a ViInt64 attribute.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attribute',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value to which you want to set the attribute.'
                },
                'grpc_enum': 'NiRFSGInt64AttributeValues',
                'name': 'value',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'SetAttributeViReal64': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Sets the value of a ViReal64 attribute.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attribute',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value to which you want to set the attribute.'
                },
                'grpc_enum': 'NiRFSGReal64AttributeValues',
                'name': 'value',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'SetAttributeViSession': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Sets the value of a ViSession attribute.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attribute',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value to which you want to set the attribute.'
                },
                'name': 'value',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'SetAttributeViString': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Sets the value of a ViString attribute.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attribute',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value to which you want to set the attribute.'
                },
                'grpc_mapped_enum': 'NiRFSGStringAttributeValuesMapped',
                'name': 'value',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'SetWaveformBurstStartLocations': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Configures the start location of the burst in samples where the burst refers to the active portion of a waveform.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "Specifies the waveform name and the marker name. Example: 'waveform::waveform0/marker0'"
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the size of the burst start locations array.'
                },
                'name': 'numberOfLocations',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the burst start locations stored in the NI-RFSG session for the waveform that you specified in the NIRFSG_ATTR_CHANNEL_NAME parameter. This value is expressed in samples.'
                },
                'name': 'locations',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'SetWaveformBurstStopLocations': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Configures the stop location of the burst in samples where the burst refers to the active portion of a waveform.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the size of the burst stop locations array.'
                },
                'name': 'numberOfLocations',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Specifies the burst stop locations, in samples, to store in the NI-RFSG session.'
                },
                'name': 'locations',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'SetWaveformMarkerEventLocations': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Configures the marker locations associated with waveform and marker in the NI-RFSG session.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the size of the locations array.'
                },
                'name': 'numberOfLocations',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Specifies the marker location, in samples, to store in the NI-RFSG database.'
                },
                'name': 'locations',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'UnlockSession': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Releases a lock obtained on an NI-RFSG device session by calling the niRFSG_LockSession function.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'unlock',
                'library_interpreter_filename': 'unlock',
                'method_python_name_suffix': '',
                'session_filename': 'unlock'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Keeps track of whether you obtain a lock and therefore need to unlock the session. Pass the address of a local ViBoolean variable. In the declaration of the local variable, initialize it to VI_FALSE. Pass the address of the same local variable to any other calls you make to the niRFSG_LockSession function or the niRFSG_UnlockSession function in the same function.'
                },
                'name': 'callerHasLock',
                'type': 'ViBoolean',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'python_name': 'unlock',
        'render_in_session_base': True,
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'WaitUntilSettled': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Waits until the RF output signal has settled. This function is useful for devices that support changes while in the Generation state. Call this function after making a dynamic change to wait for the output signal to settle.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the maximum time the function waits for the output to settle. If the maximum time is exceeded, this function returns an error. The units are expressed in milliseconds.'
                },
                'name': 'maxTimeMilliseconds',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'WriteP2PEndpointI16': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Writes an array of 16-bit integer data to the peer-to-peer endpoint. Use this function to write initial data from the host to the endpoint before starting generation to avoid an underflow when you start the generation.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the stream endpoint FIFO to configure.'
                },
                'name': 'streamEndpoint',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of samples to write into the endpoint FIFO.'
                },
                'name': 'numberOfSamples',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the array of data to write into the endpoint FIFO. The binary data is left-justified.'
                },
                'name': 'endpointData',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfSamples'
                },
                'type': 'ViInt16[]',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'WriteScript': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Writes a script to the device to control waveform generation in Script mode. First, configure your device for Script mode by calling the niRFSG_ConfigureGenerationMode function. The NI-RFSG device must be in the Configuration state before calling the niRFSG_WriteScript function.',
            'note': 'If you are using an RF vector signal transceiver (VST) device, some script instructions may not be supported.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies a string containing a syntactically correct script. NI-RFSG supports multiple scripts that are selected with the NIRFSG_ATTR_SELECTED_SCRIPT attribute. Refer to `Scripting Instructions <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/scripting_instructions.html>`_ for more information about using scripts.'
                },
                'name': 'script',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'close': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Aborts any signal generation in progress and destroys the instrument driver session.',
            'note': 'After calling this function, you cannot use NI-RFSG again until you call the niRFSG_Init function or the niRFSG_InitWithOptions function.'
        },
        'grpc_name': 'Close',
        'included_in_proto': True,
        'is_error_handling': False,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the niRFSG_Init function or the niRFSG_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'python_name': '_close',
        'returns': 'ViStatus',
        'use_session_lock': False
    }
}
