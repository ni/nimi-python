# -*- coding: utf-8 -*-
# This file is generated from NI-RFSG API metadata version 25.8.0d9999
functions = {
    'Abort': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nStops signal generation.\n\n**Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`NI-RFSG Programming State Model <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5670_programming_state_model.html>`_'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'AllocateArbWaveform': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nAllocates onboard memory space for the arbitrary waveform.\n\nUse this function to specify the total size of a waveform before writing the data. Use this function only if you are calling the nirfsg_WriteArbWaveform function multiple times to write a large waveform in smaller blocks.\n\nThe NI-RFSG device must be in the Configuration state before you call this function.\n\n**Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Streaming Waveform Data <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/streaming_waveform_data.html>`_'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
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
        'returns': 'ViStatus'
    },
    'ChangeExternalCalibrationPassword': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nChanges the external calibration password of the device.\n\n**Supported Devices:** PXIe-5611, PXIe-5653/5654, PXIe-5673/5673E, PXIe-5696, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
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
        'returns': 'ViStatus'
    },
    'CheckAttributeViBoolean': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nChecks the validity of a value you specify for a ViBoolean attribute.'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.\n\nExample:\n\n"waveform::waveform0/marker0"'
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
                    'description': 'Pass the value that you want to verify as a valid value for the attribute.',
                    'note': 'Some of the values might not be valid depending on the current settings of the instrument session.'
                },
                'name': 'value',
                'type': 'ViBoolean',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckAttributeViInt32': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nChecks the validity of a value you specify for a ViInt32 attribute.'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.\n\nExample:\n\n"waveform::waveform0/marker0"'
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
                    'description': 'Pass the value that you want to verify as a valid value for the attribute.',
                    'note': 'Some of the values might not be valid depending on the current settings of the instrument session.'
                },
                'grpc_enum': 'NiRFSGInt32AttributeValues',
                'name': 'value',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckAttributeViInt64': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nChecks the validity of a value you specify for a ViInt64 attribute.'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.\n\nExample:\n\n"waveform::waveform0/marker0"'
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
                    'description': 'Pass the value that you want to verify as a valid value for the attribute.',
                    'note': 'Some of the values might not be valid depending on the current settings of the instrument session.'
                },
                'grpc_enum': 'NiRFSGInt64AttributeValues',
                'name': 'value',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckAttributeViReal64': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nChecks the validity of a value you specify for a ViReal64 attribute.'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.\n\nExample:\n\n"waveform::waveform0/marker0"'
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
                    'description': 'Pass the value that you want to verify as a valid value for the attribute.',
                    'note': 'Some of the values might not be valid depending on the current settings of the instrument session.'
                },
                'grpc_enum': 'NiRFSGReal64AttributeValues',
                'name': 'value',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckAttributeViSession': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nChecks the validity of a value you specify for a ViSession attribute.'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.\n\nExample:\n\n"waveform::waveform0/marker0"'
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
                    'description': 'Pass the value that you want to verify as a valid value for the attribute.',
                    'note': 'Some of the values might not be valid depending on the current settings of the instrument session.'
                },
                'name': 'value',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckAttributeViString': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nChecks the validity of a value you specify for a ViString attribute.'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.\n\nExample:\n\n"waveform::waveform0/marker0"'
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
                    'description': 'Pass the value that you want to verify as a valid value for the attribute. The value must be a NULL-terminated string.',
                    'note': 'Some of the values might not be valid depending on the current settings of the instrument session.'
                },
                'grpc_mapped_enum': 'NiRFSGStringAttributeValuesMapped',
                'name': 'value',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckGenerationStatus': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nChecks the status of the generation.\n\nCall this function to check for any errors that might occur during the signal generation or to check whether the device has finished generating.\n\n**Supported Devices** : PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`NI-RFSG Instrument Driver Programming Flow <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/progflow.html>`'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns information about the completion of signal generation.\n\n**Defined Values** :',
                    'table_body': [
                        [
                            'VI_TRUE',
                            'Signal generation is complete.'
                        ],
                        [
                            'VI_FALSE',
                            'Signal generation is occurring.'
                        ]
                    ],
                    'table_header': [
                        'Value',
                        'Description'
                    ]
                },
                'name': 'isDone',
                'type': 'ViBoolean',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckIfScriptExists': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nReturns whether the script that you specify as NIRFSG_ATTR_SCRIPT_NAME exists.\n\n**Supported Devices** : PXIe-5673/5673E. PXIe-5830/5831/5840/5841/5842/5860'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
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
                    'description': 'Returns VI_TRUE if the script exists.\n\n**Defined Values** :',
                    'table_body': [
                        [
                            'VI_TRUE',
                            'The script exists.'
                        ],
                        [
                            'VI_FALSE',
                            'The script does not exist.'
                        ]
                    ],
                    'table_header': [
                        'Value',
                        'Description'
                    ]
                },
                'name': 'scriptExists',
                'type': 'ViBoolean',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckIfWaveformExists': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nReturns whether the waveform that you specify as NIRFSG_ATTR_WAVEFORM_NAME exists.\n\n**Supported Devices** : PXIe-5673/5673E, PXIe-5830/5831/5840/5841/5842/5860'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
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
                    'description': 'Returns VI_TRUE if the waveform exists.\n\n**Defined Values** :',
                    'table_body': [
                        [
                            'VI_TRUE',
                            'The waveform exists.'
                        ],
                        [
                            'VI_FALSE',
                            'The waveform does not exist.'
                        ]
                    ],
                    'table_header': [
                        'Value',
                        'Description'
                    ]
                },
                'name': 'waveformExists',
                'type': 'ViBoolean',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearAllArbWaveforms': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nDeletes all currently defined waveforms and scripts.\n\nThe NI-RFSG device must be in the Configuration state before you call this function.\n\n**Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearArbWaveform': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nDeletes a specified waveform from the pool of currently defined waveforms.\n\nThe NI-RFSG device must be in the Configuration state before you call this function.\n\n**Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
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
        'returns': 'ViStatus'
    },
    'ClearError': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nClears the error information associated with the session.\n\nIf you pass VI_NULL for the NIRFSG_ATTR_VI parameter, this function clears the error information for the current execution thread.\n\nThe IVI Engine also maintains this error information separately for each thread. This feature of the IVI Engine is useful if you do not have a session handle to pass to the nirfsg_ClearError function or the nirfsg_GetError function, which occurs when a call to the nirfsg_Init function or the nirfsg_InitWithOptions function fails.\n\n**Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5840/5841/5842/5860',
            'note': 'The nirfsg_GetError function clears the error information after it is retrieved. A call to the nirfsg_ClearError function is necessary only when you do not use a call to the nirfsg_GetError function to retrieve error information.'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearSelfCalibrateRange': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nClears the data obtained from the nirfsg_SelfCalibrateRange function.\n\n**Supported Devices** : PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'Commit': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nPrograms the device with the correct settings.\n\nCalling this function moves the NI-RFSG device from the Configuration state to the Committed state. After this function executes, a change to any attribute reverts the NI-RFSG device to the Configuration state.\n\n**Supported devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`NI-RFSG Programming State Model <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5670_programming_state_model.html>`_'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureDeembeddingTableInterpolationLinear': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nSelects the linear interpolation method.\n\nIf the carrier frequency does not match a row in the de-embedding table, NI-RFSG performs a linear interpolation based on the entries in the de-embedding table to determine the parameters to use for de-embedding.\n\n**Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).'
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
                    'description': 'Specifies the format of parameters to interpolate. **Defined Values** :',
                    'table_body': [
                        [
                            'NIRFSG_VAL_LINEAR_INTERPOLATION_FORMAT_REAL_AND_IMAGINARY',
                            '26000 (0x6590)',
                            'Results in a linear interpolation of the real portion of the complex number and a separate linear interpolation of the complex portion.'
                        ],
                        [
                            'NIRFSG_VAL_LINEAR_INTERPOLATION_FORMAT_MAGNITUDE_AND_PHASE',
                            '26001 (0x6591)',
                            'Results in a linear interpolation of the magnitude and a separate linear interpolation of the phase.'
                        ],
                        [
                            'NIRFSG_VAL_LINEAR_INTERPOLATION_FORMAT_MAGNITUDE_DB_AND_PHASE',
                            '26002 (0x6592)',
                            'Results in a linear interpolation of the magnitude, in decibels, and a separate linear interpolation of the phase.'
                        ]
                    ],
                    'table_header': [
                        'Name',
                        'Value',
                        'Description'
                    ]
                },
                'enum': 'Format',
                'name': 'format',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureDeembeddingTableInterpolationNearest': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nSelects the nearest interpolation method.\n\nNI-RFSG uses the parameters of the table nearest to the carrier frequency for de-embedding.\n\n**Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).'
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
        'returns': 'ViStatus'
    },
    'ConfigureDeembeddingTableInterpolationSpline': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nSelects the spline interpolation method.\n\nIf the carrier frequency does not match a row in the de-embedding table, NI-RFSG performs a spline interpolation based on the entries in the de-embedding table to determine the parameters to use for de-embedding.\n\n**Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).'
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
        'returns': 'ViStatus'
    },
    'ConfigureDigitalEdgeScriptTrigger': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nConfigures the specified Script Trigger for digital edge triggering.\n\nThe NI-RFSG device must be in the Configuration state before calling this function.\n\n**Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_\n\n`Digital Edge Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/trigger_edge.html>`_'
        },
        'has_repeated_capability': True,
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
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
                'is_repeated_capability': True,
                'name': 'triggerId',
                'repeated_capability_type': 'script_triggers',
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
                'enum': 'ScriptTriggerDigitalEdgeEdge',
                'grpc_enum': None,
                'name': 'edge',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'repeated_capability_type': 'script_triggers',
        'returns': 'ViStatus'
    },
    'ConfigureDigitalEdgeStartTrigger': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nConfigures the Start Trigger for digital edge triggering.\n\nThe NI-RFSG device must be in the Configuration state before calling this function.\n\n**Supported Devices** : PXIe-5644/5645/5646, PXIe-5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_\n\n`Digital Edge Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/trigger_edge.html>`_',
            'note': 'For the PXIe-5654/5654 with PXIe-5696, the Start Trigger is valid only with a timer-based list when RF list mode is enabled.'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
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
                'enum': 'StartTriggerDigitalEdgeEdge',
                'grpc_enum': None,
                'name': 'edge',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureDigitalLevelScriptTrigger': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nConfigures a specified Script Trigger for digital level triggering.\n\nThe NI-RFSG device must be in the Configuration state before calling this function.\n\n**Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_\n\n`Digital Level Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/trigger_level.html>`_'
        },
        'has_repeated_capability': True,
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
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
                'is_repeated_capability': True,
                'name': 'triggerId',
                'repeated_capability_type': 'script_triggers',
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
        'repeated_capability_type': 'script_triggers',
        'returns': 'ViStatus'
    },
    'ConfigureDigitalModulationUserDefinedWaveform': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nSpecifies the message signal used for digital modulation when the NIRFSG_ATTR_DIGITAL_MODULATION_WAVEFORM_TYPE attribute is set to NIRFSG_VAL_USER_DEFINED.\n\n**Supported Devices** : PXI/PXIe-5650/5651/5652'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
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
        'returns': 'ViStatus'
    },
    'ConfigurePxiChassisClk10': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nSpecifies the signal to drive the 10MHz Reference Clock on the PXI backplane.\n\nThis option can only be configured when the PXI-5610 is in Slot 2 of the PXI chassis. The NI-RFSG device must be in the Configuration state before you call this function.\n\n**Supported Devices** : PXI-5610, PXI-5670/5671\n\n**Related Topics**\n\n`Timing Configurations <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/timing_configurations.html>`_\n\n`System Reference Clock <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pxi_clk10.html>`_'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
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
        'returns': 'ViStatus'
    },
    'ConfigureRF': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nConfigures the frequency and power level of the RF output signal.\n\nThe PXI-5670/5671, PXIe-5672, and PXIe-5860 device must be in the Configuration state before calling this function. The PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5654/5654 with PXIe-5696, PXIe-5673/5673E, and PXIe-5830/5831/5832/5840/5841/5842 device can be in the Configuration or Generation state when you call this function.\n\n**Supported Devices** : PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`NI-RFSG Instrument Driver Programming Flow <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/progflow.html>`_'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the frequency of the generated RF signal, in hertz. For arbitrary waveform generation, this parameter specifies the center frequency of the signal.\n\n**Units** : hertz (Hz)'
                },
                'name': 'frequency',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies either the average power level or peak power level of the generated RF signal, depending on the NIRFSG_ATTR_POWER_LEVEL_TYPE attribute.\n\n**Units** : dBm'
                },
                'name': 'powerLevel',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureRefClock': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nConfigures the NI-RFSG device Reference Clock.\n\nThe Reference Clock ensures that the NI-RFSG devices are operating from a common timebase. The NI-RFSG device must be in the Configuration state before calling this function.\n\n**Supported Devices** : PXI-5610, PXIe-5644/5645/5646, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`PXIe-5672 Timing Configurations <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/timing_configurations.html>`_\n\n`PXIe-5673 Timing Configurations <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/10mhzreference_phase1.html>`_\n\n`PXIe-5673E Timing Configurations <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/10mhzreference.html>`_\n\n`PXIe-5830 Timing Configurations <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/timing_configurations.html>`_\n\n`PXIe-5831 Timing Configurations <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/timing_configurations.html>`_'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the source of Reference Clock signal.',
                    'table_body': [
                        [
                            '"OnboardClock"',
                            ' Uses the onboard Reference Clock as the clock source. **PXIe-5830/5831/5832** :For the PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For the PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For the PXIe-5832, connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. **PXIe-5831 with PXIe-5653** :Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. **PXIe-5832 with PXIe-5653** :Connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3623 REF IN connector. **PXIe-5841 with PXIe-5655** :Lock to the PXIe-5655 onboard clock. Connect the REF OUT connector on the PXIe-5655 to the PXIe-5841 REF IN connector. **PXIe-5842** :Lock to the PXIe-5655 onboard clock. Cables between modules are required as shown in the Getting Started Guide for the instrument.'
                        ],
                        [
                            '"RefIn"',
                            'Uses the clock signal present at the front panel REF IN connector as the clock source. **PXIe-5830/5831/5832** :For the PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For the PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For the PXIe-5832, connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. For the PXIe-5830, lock the external signal to the PXIe-3621 REF IN connector. For the PXIe-5831, lock the external signal to the PXIe-3622 REF IN connector. For the PXIe-5832, lock the external signal to the PXIe-3623 REF IN connector. **PXIe-5831 with PXIe-5653** :Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector. **PXIe-5832 with PXIe-5653** :Connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3623 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector.  **PXIe-5841 with PXIe-5655** :Lock to the signal at the REF IN connector on the associated PXIe-5655. Connect the PXIe-5655 REF OUT connector to the PXIe-5841 REF IN connector. **PXIe-5842** :Lock to the signal at the REF IN connector on the associated PXIe-5655. Cables between modules are required as shown in the Getting Started Guide for the instrument.'
                        ],
                        [
                            '"PXI_CLK"',
                            'Uses the PXI_CLK signal, which is present on the PXI backplane, as the clock source.'
                        ],
                        [
                            '"ClkIn"',
                            'Uses the clock signal present at the front panel CLK IN connector as the clock source. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5831 with PXIe-5653/5832/5832 with PXIe-5653/5840/5841/5841 with PXIe-5655/5842.'
                        ],
                        [
                            '"RefIn2"',
                            '\\-'
                        ],
                        [
                            '"PXI_ClkMaster"',
                            'This value is valid on only the PXIe-5831 with PXIe-5653 and PXIe-5832 with PXIe-5653. **PXIe-5831 with PXIe-5653** :NI-RFSG configures the PXIe-5653 to export the Reference clock and configures the PXIe-5820 and PXIe-3622 to use PXI_Clk as the Reference Clock source. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector. **PXIe-5832 with PXIe-5653** :NI-RFSG configures the PXIe-5653 to export the Reference clock and configures the PXIe-5820 and PXIe-3623 to use PXI_Clk as the Reference Clock source. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector.'
                        ]
                    ],
                    'table_header': [
                        'Possible Values',
                        'Description'
                    ]
                },
                'name': 'refClockSource',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the Reference Clock rate, in hertz (Hz), of the signal present at the REF IN or CLK IN connector. The default value is NIRFSG_VAL_AUTO, which allows NI-RFSG to use the default Reference Clock rate for the device or automatically detect the Reference Clock rate, if supported. This parameter is only valid when the NIRFSG_ATTR_REF_CLOCK_SOURCE parameter is set to ClkIn, RefIn or RefIn2. Refer to the NIRFSG_ATTR_REF_CLOCK_RATE attribute for possible values.'
                },
                'name': 'refClockRate',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSoftwareScriptTrigger': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nConfigures the Script Trigger for software triggering.\n\nRefer to the nirfsg_SendSoftwareEdgeTrigger function for more information about using the software Script Trigger. The NI-RFSG device must be in the Configuration state before calling this function.\n\n**Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_\n\n`Trigger Types <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/trigger_types.html>`_'
        },
        'has_repeated_capability': True,
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
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
                'is_repeated_capability': True,
                'name': 'triggerId',
                'repeated_capability_type': 'script_triggers',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'repeated_capability_type': 'script_triggers',
        'returns': 'ViStatus'
    },
    'ConfigureSoftwareStartTrigger': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nConfigures the Start Trigger for software triggering.\n\nRefer to the nirfsg_SendSoftwareEdgeTrigger function for more information about using a software trigger. The NI-RFSG device must be in the Configuration state before calling this function.\n\n**Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_\n\n`Trigger Types <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/trigger_types.html>`_'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateDeembeddingSparameterTableArray': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nCreates an s-parameter de-embedding table for the port from the input data.\n\nIf you only create one table for a port, NI-RFSG automatically selects that table to de-embed the measurement.\n\n**Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`De-embedding Overview <https://www.ni.com/docs/en-US/bundle/pxie-5840/page/de-embedding-overview.html>`_'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'numpy_method',
                'library_interpreter_filename': 'numpy_write_method',
                'method_python_name_suffix': '',
                'session_filename': 'numpy_write_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).'
                },
                'name': 'port',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the table. The name must be unique for a given port, but not across ports. If you use the same name as an existing table, the table is replaced.'
                },
                'name': 'tableName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the frequencies for the NIRFSG_ATTR_SPARAMETER_TABLE rows. Frequencies must be unique and in ascending order.'
                },
                'name': 'frequencies',
                'numpy': True,
                'size': {
                    'mechanism': 'len',
                    'value': 'frequenciesSize'
                },
                'type': 'ViReal64[]',
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the size of the frequency array.'
                },
                'name': 'frequenciesSize',
                'type': 'ViInt32',
                'use_array': False
            },
            {
                'array_dimension': 3,
                'complex_type': 'numpy',
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the S-parameters for each frequency. S-parameters for each frequency are placed in the array in the following order: s11, s12, s21, s22.'
                },
                'name': 'sparameterTable',
                'numpy': True,
                'type': 'NIComplexNumber[]',
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the size of the S-parameter table array.'
                },
                'name': 'sparameterTableSize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': False
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of DUT ports.'
                },
                'name': 'numberOfPorts',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': False
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the orientation of the input data relative to the port on the DUT port.\n\n**Defined Values** :',
                    'table_body': [
                        [
                            'NIRFSG_VAL_PORT1_TOWARDS_DUT',
                            '24000 (0x5dc0)',
                            'Port 1 of the S2P is oriented towards the DUT port.'
                        ],
                        [
                            'NIRFSG_VAL_PORT2_TOWARDS_DUT',
                            '24001 (0x5dc1)',
                            'Port 2 of the S2P is oriented towards the DUT port.'
                        ]
                    ],
                    'table_header': [
                        'Name',
                        'Value',
                        'Description'
                    ]
                },
                'enum': 'SparameterOrientation',
                'name': 'sparameterOrientation',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateDeembeddingSparameterTableS2PFile': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nCreates an S-parameter de-embedding table for the port based on the specified S2P file.\n\nIf you only create one table for a port, NI-RFSG automatically selects that table to de-embed the measurement.\n\n**Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`De-embedding Overview <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/de_embedding_overview.html>`_\n\n`S-parameters <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/s_parameters.html>`_'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842 is empty string.'
                },
                'name': 'port',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the table. The name must be unique for a given port, but not across ports. If you use the same name as an existing table, the table is replaced.'
                },
                'name': 'tableName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the path to the S2P file that contains de-embedding information for the specified port.'
                },
                'name': 's2pFilePath',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': ' Specifies the orientation of the data in the S2P file relative to the port on the DUT port. **Defined Values** :',
                    'table_body': [
                        [
                            'NIRFSG_VAL_PORT1_TOWARDS_DUT',
                            '24000 (0x5dc0)',
                            'Port 1 of the S2P is oriented towards the DUT port.'
                        ],
                        [
                            'NIRFSG_VAL_PORT2_TOWARDS_DUT',
                            '24001 (0x5dc1)',
                            'Port 2 of the S2P is oriented towards the DUT port.'
                        ]
                    ],
                    'table_header': [
                        'Name',
                        'Value',
                        'Description'
                    ]
                },
                'enum': 'SparameterOrientation',
                'name': 'sparameterOrientation',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'DeleteAllDeembeddingTables': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nDeletes all configured de-embedding tables for the session.\n\n**Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'DeleteDeembeddingTable': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nDeletes the selected de-embedding table for a given port.\n\n**Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).'
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
        'returns': 'ViStatus'
    },
    'Disable': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nPlaces the instrument in a quiescent state where it has minimal or no impact on the system to which it is connected.\n\n**Supported Devices** : PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXI-5670/5671, PXIe-5672/5673/5673E'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'DisableScriptTrigger': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nConfigures the device not to wait for the specified Script Trigger.\n\nCall this function only if you previously configured a Script Trigger and now want it disabled. The NI-RFSG device must be in the Configuration state before you call this function.\n\n**Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_'
        },
        'has_repeated_capability': True,
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
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
                'is_repeated_capability': True,
                'name': 'triggerId',
                'repeated_capability_type': 'script_triggers',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'repeated_capability_type': 'script_triggers',
        'returns': 'ViStatus'
    },
    'DisableStartTrigger': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nConfigures the device not to wait for a Start Trigger.\n\nThis function is necessary only if you previously configured a Start Trigger and now want it disabled. The NI-RFSG device must be in the Configuration state before calling this function.\n\n**Supported Devices** : PXIe-5644/5645/5646, PXIe-5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'ErrorMessage': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nConverts an error code returned by an NI-RFSG function into a user-readable string.\n\n**Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'is_error_handling': True,
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
                    'description': 'The ViSession handle that you obtain from nirfsg_Init or nirfsg_InitWithOptions. The handle identifies a particular instrument session.\n\nYou can pass VI_NULL for this parameter. Passing VI_NULL is useful when nirfsg_Init or nirfsg_InitWithOptions fails.\n\n**Default Value** : VI_NULL'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the status parameter that is returned from any NI-RFSG function.\n\n**Default Value** : 0 (VI_SUCCESS)'
                },
                'name': 'errorCode',
                'type': 'ViStatus',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Returns the user-readable message string that corresponds to the status code you specify.\n\nYou must pass a ViChar array with at least 256 bytes to this parameter.'
                },
                'name': 'errorMessage',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'ErrorQuery': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nReads an error code and an error message from the instrument error queue.\n\n**Supported Devices** : PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5840/5841/5842/5860'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the error code read from the instrument error queue.'
                },
                'name': 'errorCode',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the error message string read from the instrument error message queue.\n\nYou must pass a ViChar array with at least 256 bytes.'
                },
                'name': 'errorMessage',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'FancyCreateDeembeddingSparameterTableArray': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': '\nCreates an s-parameter de-embedding table for the port from the input data.\n\nIf you only create one table for a port, NI-RFSG automatically selects that table to de-embed the measurement.\n\n**Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`De-embedding Overview<https://www.ni.com/docs/en-US/bundle/pxie-5840/page/de-embedding-overview.html>`_'
        },
        'included_in_proto': True,
        'method_name_for_documentation': 'create_deembedding_sparameter_table_array',
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '',
                'session_filename': 'create_deembedding_sparameter_table_array'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).'
                },
                'name': 'port',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the table. The name must be unique for a given port, but not across ports. If you use the same name as an existing table, the table is replaced.'
                },
                'name': 'tableName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the frequencies for the NIRFSG_ATTR_SPARAMETER_TABLE rows. Frequencies must be unique and in ascending order.'
                },
                'name': 'frequencies',
                'numpy': True,
                'type': 'ViReal64[]',
                'type_in_documentation': 'numpy.array(dtype=numpy.float64)',
                'use_in_python_api': True
            },
            {
                'array_dimension': 3,
                'complex_type': 'numpy',
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the S-parameters for each frequency. S-parameters for each frequency are placed in the array in the following order: s11, s12, s21, s22.'
                },
                'name': 'sparameterTable',
                'numpy': True,
                'type': 'NIComplexNumber[]',
                'type_in_documentation': 'numpy.array(dtype=numpy.complex128)',
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the orientation of the input data relative to the port on the DUT port.\n\n**Defined Values** :',
                    'table_body': [
                        [
                            'NIRFSG_VAL_PORT1_TOWARDS_DUT',
                            '24000 (0x5dc0)',
                            'Port 1 of the S2P is oriented towards the DUT port.'
                        ],
                        [
                            'NIRFSG_VAL_PORT2_TOWARDS_DUT',
                            '24001 (0x5dc1)',
                            'Port 2 of the S2P is oriented towards the DUT port.'
                        ]
                    ],
                    'table_header': [
                        'Name',
                        'Value',
                        'Description'
                    ]
                },
                'enum': 'SparameterOrientation',
                'grpc_enum': None,
                'name': 'sparameterOrientation',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'python_name': 'create_deembedding_sparameter_table_array',
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'FancyGetDeembeddingSparameters': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': '\nReturns the S-parameters used for de-embedding a measurement on the selected port.\n\nThis includes interpolation of the parameters based on the configured carrier frequency. This function returns an empty array if no de-embedding is done.\n\nIf you want to call this function just to get the required buffer size, you can pass 0 for **S-parameter Size** and VI_NULL for the **S-parameters** buffer.\n\n**Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860',
            'note': 'The port orientation for the returned S-parameters is normalized to NIRFSG_VAL_PORT1_TOWARDS_DUT.'
        },
        'included_in_proto': True,
        'method_name_for_documentation': 'get_deembedding_sparameters',
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '',
                'session_filename': 'get_deembedding_sparameter'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'array_dimension': 2,
                'complex_type': 'numpy',
                'direction': 'out',
                'documentation': {
                    'description': 'Returns an array of S-parameters. The S-parameters are returned in the following order: s11, s12, s21, s22.'
                },
                'name': 'sparameters',
                'numpy': True,
                'type': 'NIComplexNumber[]',
                'type_in_documentation': 'numpy.array(dtype=numpy.complex128)',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'python_name': 'get_deembedding_sparameters',
        'returns': None,
        'use_session_lock': False
    },
    'GetAllNamedWaveformNames': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nReturn names of the waveforms present in the memory.\n\n**Supported Devices** :PXIe-5830/5831/5840/5841/5842E'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns a string having waveform names separated by commas.'
                },
                'name': 'waveformNames',
                'python_api_converter_name': 'convert_comma_separated_string_to_list',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the number of bytes in the ViChar buffer you specify for the NIRFSG_ATTR_WAVEFORM_NAMES parameter.\n\nIf you pass 0, you can pass VI_NULL for the NIRFSG_ATTR_WAVEFORM_NAMES parameter.'
                },
                'name': 'bufferSize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Fetch the number of bytes needed to pass in the NIRFSG_ATTR_BUFFER_SIZE parameter.\n\nIt can be fetch by passing VI_NULL in the NIRFSG_ATTR_WAVEFORM_NAMES parameter.'
                },
                'name': 'actualBufferSize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAllScriptNames': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nReturn names of the scripts present in the memory.\n\n**Supported Devices** :PXIe-5830/5831/5840/5841/5842E'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns a string having script names separated by commas.'
                },
                'name': 'scriptNames',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the number of bytes in the ViChar buffer you specify for the **waveformNames** parameter.\n\nIf you pass 0, you can pass VI_NULL for the **waveformNames** parameter.'
                },
                'name': 'bufferSize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Fetch the number of bytes needed to pass in the NIRFSG_ATTR_BUFFER_SIZE parameter.\n\nIt can be fetch by passing VI_NULL in the NIRFSG_ATTR_SCRIPT_NAMES parameter.'
                },
                'name': 'actualBufferSize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViBoolean': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nQueries the value of a ViBoolean attribute.\n\nUse this low-level function to get the values of inherent IVI attributes, class-defined attributes, and instrument-specific attributes. If the attribute represents an instrument state, this function performs instrument I/O in the following cases:\n\n- State caching is disabled for the entire session or for the particular attribute.\n- State caching is enabled, and the currently cached value is invalid.'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.\n\nExample:\n\n"waveform::waveform0/marker0"'
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
        'returns': 'ViStatus'
    },
    'GetAttributeViInt32': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nQueries the value of a ViInt32 attribute.\n\nUse this low-level function to get the values of inherent IVI attributes, class-defined attributes, and instrument-specific attributes. If the attribute represents an instrument state, this function performs instrument I/O in the following cases:\n\n- State caching is disabled for the entire session or for the particular attribute.\n- State caching is enabled, and the currently cached value is invalid.'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.\n\nExample:\n\n"waveform::waveform0/marker0"'
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
        'returns': 'ViStatus'
    },
    'GetAttributeViInt64': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nQueries the value of a ViInt64 attribute.\n\nYou can use this low-level function to get the values of inherent IVI attributes, class-defined attributes, and instrument-specific attributes. If the attribute represents an instrument state, this function performs instrument I/O in the following cases:\n\n- State caching is disabled for the entire session or for the particular attribute.\n- State caching is enabled, and the currently cached value is invalid.'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.\n\nExample:\n\n"waveform::waveform0/marker0"'
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
        'returns': 'ViStatus'
    },
    'GetAttributeViReal64': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nQueries the value of a ViReal64 attribute.\n\nUse this low-level function to get the values of inherent IVI attributes, class-defined attributes, and instrument-specific attributes. If the attribute represents an instrument state, this function performs instrument I/O in the following cases:\n\n- State caching is disabled for the entire session or for the particular attribute.\n- State caching is enabled, and the currently cached value is invalid.'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.\n\nExample:\n\n"waveform::waveform0/marker0"'
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
        'returns': 'ViStatus'
    },
    'GetAttributeViSession': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nQueries the value of a ViSession attribute.\n\nUse this low-level function to get the values of inherent IVI attributes, class-defined attributes, and instrument-specific attributes. If the attribute represents an instrument state, this function performs instrument I/O in the following cases:\n\n- State caching is disabled for the entire session or for the particular attribute.\n- State caching is enabled, and the currently cached value is invalid.'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.\n\nExample:\n\n"waveform::waveform0/marker0"'
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
        'returns': 'ViStatus'
    },
    'GetAttributeViString': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nQueries the value of a ViString attribute.\n\nUse this low-level function to get the values of inherent IVI attributes, class-defined attributes, and instrument-specific attributes. If the attribute represents an instrument state, this function performs instrument I/O in the following cases:\n\n- State caching is disabled for the entire session or for the particular attribute.\n- State caching is enabled, and the currently cached value is invalid.\n\nYou must provide a ViString (ViChar array) to serve as a buffer for the value. Pass the number of bytes in the buffer as the Buffer Size parameter. If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the buffer size parameter, the function copies buffer size-1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.\n\nTo call this function to get only the required buffer size, pass 0 for the buffer size and VI_NULL for the attribute value buffer.'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.\n\nExample:\n\n"waveform::waveform0/marker0"'
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
                    'description': 'Pass the number of bytes in the ViChar buffer you specify for the **waveformNames** parameter.\n\nIf you pass 0, you can pass VI_NULL for the **waveformNames** parameter.'
                },
                'name': 'bufSize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The buffer in which the function returns the current value of the attribute. The buffer must be of type ViChar and have at least as many bytes as indicated in the **bufferSize** parameter.\n\nIf you specify 0 for the **bufferSize** parameter, you can pass VI_NULL for this parameter.'
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
        'returns': 'ViStatus'
    },
    'GetChannelName': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nReturns the channel string that is in the channel table at an index you specify.\n\n**Supported Devices** : PXI-5670/5671, PXIe-5672/5673/5673E'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies a one-based index into the channel table.'
                },
                'name': 'index',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the size of the buffer for the channel string.'
                },
                'name': 'bufferSize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns a channel string from the channel table at the index you specify in the Index parameter. Do not modify the contents of the channel string.'
                },
                'name': 'name',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'GetDeembeddingSparameters': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nReturns the S-parameters used for de-embedding a measurement on the selected port.\n\nThis includes interpolation of the parameters based on the configured carrier frequency. This function returns an empty array if no de-embedding is done.\n\nIf you want to call this function just to get the required buffer size, you can pass 0 for **S-parameter Size** and VI_NULL for the **S-parameters** buffer.\n\n**Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860',
            'note': 'The port orientation for the returned S-parameters is normalized to NIRFSG_VAL_PORT1_TOWARDS_DUT.'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'numpy_method',
                'library_interpreter_filename': 'numpy_read_method',
                'method_python_name_suffix': '',
                'session_filename': 'numpy_read_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'array_dimension': 2,
                'complex_type': 'numpy',
                'direction': 'out',
                'documentation': {
                    'description': 'Returns an array of S-parameters. The S-parameters are returned in the following order: s11, s12, s21, s22.'
                },
                'name': 'sparameters',
                'numpy': True,
                'type': 'NIComplexNumber[]',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the size of the array that is returned by the NIRFSG_ATTR_SPARAMETERS output.'
                },
                'name': 'sparametersArraySize',
                'type': 'ViInt32',
                'use_array': False
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the number of S-parameters.'
                },
                'name': 'numberOfSparameters',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the number of S-parameter ports. The **sparameter** array is always *n* x *n*, where span *n* is the number of ports.'
                },
                'name': 'numberOfPorts',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'GetDeembeddingTableNumberOfPorts': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nReturns the number of S-parameter ports.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the number of S-parameter ports. The **sparameter** array is always *n* x *n*, where span *n* is the number of ports.'
                },
                'name': 'numberOfPorts',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetError': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nRetrieves and then clears the IVI error information for the session or the current execution thread.\n\n**Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5840/5841/5842/5860',
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
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
                    'description': 'Pass the number of bytes in the ViChar array you specify for the **description** parameter.\n\nIf the NIRFSG_ATTR_ERROR_DESCRIPTION, including the terminating NULL byte, contains more bytes than you indicate in this parameter, the function copies **bufferSize** - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. Forexample, if the value is 123456 and the buffer size is 4, the function places 123 into the buffer and returns 7. If you pass 0, you can pass VI_NULL for the **description** parameter.\n\n**Default Value** : None'
                },
                'name': 'errorDescriptionBufferSize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the NIRFSG_ATTR_ERROR_DESCRIPTION for the IVI session or execution thread.\n\nIf there is no description, the function returns an empty string. The buffer must contain at least as many elements as the value you specify with the **bufferSize** parameter. If the NIRFSG_ATTR_ERROR_DESCRIPTION, including the terminating NULL byte, contains more bytes than you indicate with the **bufferSize** parameter, the function copies **bufferSize** - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is 123456 and the buffer size is 4, the function places 123 into the buffer and returns 7. If you pass 0, you can pass VI_NULL for this parameter.'
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
            'description': '\nReturns the date and time of the last successful external calibration.\n\nThe time returned is 24-hour (military) local time; for example, if the device was calibrated at 2:30PM, this function returns\n\n14 for the hours parameter and\n\n30 for the minutes parameter.\n\n**Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5696, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'method_name_for_documentation': 'get_external_calibration_last_date_and_time',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
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
        'returns': 'ViStatus'
    },
    'GetLastExtCalLastDateAndTime': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': '\nReturns the date and time of the last successful external calibration.\n\nThe time returned is 24-hour (military) local time; for example, if the device was calibrated at 2:30PM, this function returns\n\n14 for the hours parameter and\n\n30 for the minutes parameter.\n\n**Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5696, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
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
            'description': '\nReturns the date and time of the last successful self-calibration.\n\nThe time returned is 24-hour local time. For example, if the device was calibrated at 2:30PM, this function returns\n\n14 for the hours parameter and\n\n30 for the minutes parameter.\n\n**Supported Devices** : PXI-5610, PXIe-5644/5645/5646, PXIe-5653, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
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
                'documentation': {
                    'description': 'Specifies from which stand-alone module to retrieve the last successful self-calibration date and time.'
                },
                'enum': 'Module',
                'grpc_enum': None,
                'name': 'module',
                'type': 'ViInt32'
            },
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
            'description': '\nReturns the maximum settable output power level for the current configuration.\n\n**Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
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
        'returns': 'ViStatus'
    },
    'GetSelfCalibrationDateAndTime': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nReturns the date and time of the last successful self-calibration.\n\nThe time returned is 24-hour local time. For example, if the device was calibrated at 2:30PM, this function returns\n\n14 for the hours parameter and\n\n30 for the minutes parameter.\n\n**Supported Devices** : PXI-5610, PXIe-5644/5645/5646, PXIe-5653, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'method_name_for_documentation': 'get_self_calibration_date_and_time',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
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
                'enum': 'Module',
                'grpc_enum': None,
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
        'returns': 'ViStatus'
    },
    'GetSelfCalibrationTemperature': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nReturns the temperature, in degrees Celsius, of the device at the last successful self-calibration.\n\n**Supported Devices** : PXI-5610, PXIe-5653, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831 (IF only)/5832 (IF only)/5840/5841/5842/5860'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies from which stand-alone module to retrieve the last successful self-calibration temperature. \n                    **Default Value** : NIRFSG_VAL_PRIMARY_MODULE\n                    **Defined Values** :\n                    ',
                    'table_body': [
                        [
                            'NIRFSG_VAL_PRIMARY_MODULE',
                            '13000 (0x32c8)',
                            'The stand-alone device or the main module in a multi-module device.'
                        ],
                        [
                            'NIRFSG_VAL_AWG',
                            '13001 (0x32c9)',
                            'The AWG associated with the primary module.'
                        ],
                        [
                            'NIRFSG_VAL_LO',
                            '13002 (0x32ca)',
                            'The LO associated with the primary module.'
                        ]
                    ],
                    'table_header': [
                        'Name',
                        'Value',
                        'Description'
                    ]
                },
                'enum': 'Module',
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
        'returns': 'ViStatus'
    },
    'GetTerminalName': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nReturns the fully-qualified name of the specified signal.\n\nThe fully-qualified name is helpful to automatically route signals in a multisegment chassis.\n\n**Supported Devices** : PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Triggers <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/triggers.html>`_\n\n`Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_\n\n`Syntax for Terminal Names <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/syntax_for_terminal_names.html>`_'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the signal to query. **Defined Values** :\n                    ',
                    'table_body': [
                        [
                            'NIRFSG_VAL_START_TRIGGER',
                            '0 (0x0)',
                            'Exports a Start Trigger.'
                        ],
                        [
                            'NIRFSG_VAL_SCRIPT_TRIGGER',
                            '1 (0x1)',
                            'Exports a Script Trigger.'
                        ],
                        [
                            'NIRFSG_VAL_MARKER_EVENT',
                            '2 (0x2)',
                            'Exports a Marker Event.'
                        ],
                        [
                            'NIRFSG_VAL_REF_CLOCK',
                            '3 (0x3)',
                            'Exports the Reference Clock.'
                        ],
                        [
                            'NIRFSG_VAL_STARTED_EVENT',
                            '4 (0x4)',
                            'Exports a Started Event.'
                        ],
                        [
                            'NIRFSG_VAL_DONE_EVENT',
                            '5 (0x5)',
                            'Exports a Done Event.'
                        ],
                        [
                            'NIRFSG_VAL_CONFIGURATION_LIST_STEP_TRIGGER',
                            '6 (0x6)',
                            'Exports a Configuration List Step Trigger.'
                        ],
                        [
                            'NIRFSG_VAL_CONFIGURATION_SETTLED_EVENT',
                            '7 (0x7)',
                            'Exports a Configuration Settled Event.'
                        ]
                    ],
                    'table_header': [
                        'Name',
                        'Value',
                        'Description'
                    ]
                },
                'enum': 'Signal',
                'name': 'signal',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies which instance of the selected signal to query. This parameter is necessary when you set the NIRFSG_ATTR_SIGNAL parameter to NIRFSG_VAL_SCRIPT_TRIGGER or NIRFSG_VAL_MARKER_EVENT  . Otherwise, set the NIRFSG_ATTR_SIGNAL_IDENTIFIER parameter to "" (empty string). **Possible Values** :\n                    ',
                    'table_body': [
                        [
                            '"marker0"',
                            'Specifies Marker 0.'
                        ],
                        [
                            '"marker1"',
                            'Specifies Marker 1.'
                        ],
                        [
                            '"marker2"',
                            'Specifies Marker 2.'
                        ],
                        [
                            '"marker3"',
                            'Specifies Marker 3.'
                        ],
                        [
                            '"scriptTrigger0"',
                            'Specifies Script Trigger 0.'
                        ],
                        [
                            '"scriptTrigger1"',
                            'Specifies Script Trigger 1.'
                        ],
                        [
                            '"scriptTrigger2"',
                            'Specifies Script Trigger 2.'
                        ],
                        [
                            '"scriptTrigger3"',
                            'Specifies Script Trigger 3.'
                        ]
                    ],
                    'table_header': [
                        'Possible Value',
                        'Description'
                    ]
                },
                'name': 'signalIdentifier',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the number of bytes in the ViChar buffer you specify for the **NIRFSG_ATTR_TERMINAL_NAME** parameter.\n\nIf you pass 0, you can pass VI_NULL for the **NIRFSG_ATTR_TERMINAL_NAME** parameter.'
                },
                'name': 'bufferSize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the string to use as the source for other devices.'
                },
                'name': 'terminalName',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'GetWaveformBurstStartLocations': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nReturns the burst start locations of the waveform stored in the NI-RFSG session.\n\n**Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842'
        },
        'has_repeated_capability': True,
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name. Example: "waveform::waveform0/marker0"'
                },
                'is_repeated_capability': True,
                'name': 'channelName',
                'repeated_capability_type': 'waveforms',
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
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'numberOfLocations',
                    'value_twist': 'requiredSize'
                },
                'type': 'ViReal64[]',
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
        'repeated_capability_type': 'waveforms',
        'returns': 'ViStatus'
    },
    'GetWaveformBurstStopLocations': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nReturns the burst stop locations of the waveform stored in the NI-RFSG session.\n\n**Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842'
        },
        'has_repeated_capability': True,
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name. Example: "waveform::waveform0/marker0"'
                },
                'is_repeated_capability': True,
                'name': 'channelName',
                'repeated_capability_type': 'waveforms',
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
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'numberOfLocations',
                    'value_twist': 'requiredSize'
                },
                'type': 'ViReal64[]',
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
        'repeated_capability_type': 'waveforms',
        'returns': 'ViStatus'
    },
    'GetWaveformMarkerEventLocations': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nReturns the marker locations associated with the waveform and the marker stored in the NI-RFSG session.\n\n**Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842'
        },
        'has_repeated_capability': True,
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.\n\nExample:\n\n"waveform::waveform0/marker0"'
                },
                'is_repeated_capability': True,
                'name': 'channelName',
                'repeated_capability_type': 'markers',
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
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'numberOfLocations',
                    'value_twist': 'requiredSize'
                },
                'type': 'ViReal64[]',
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
        'repeated_capability_type': 'markers',
        'returns': 'ViStatus'
    },
    'InitWithOptions': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nOpens a session to the device you specify as the NIRFSG_ATTR_RESOURCE_NAME and returns a ViSession handle that you use to identify the NI-RFSG device in all subsequent NI-RFSG function calls.\n\nThis function also configures the device through the NIRFSG_ATTR_OPTION_STRING input.\n\n**Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Simulating an NI RF Signal Generator <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/simulate.html>`_',
            'note': 'For multichannel devices such as the PXIe-5860, the resource name must include the channel number to use. The channel number is specified by appending /*ChannelNumber* to the device name, where *ChannelNumber* is the channel number (0, 1, etc.). For example, if the device name is PXI1Slot2 and you want to use channel 0, use the resource name PXI1Slot2/0.'
        },
        'included_in_proto': True,
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
                    'description': 'Specifies the resource name of the device to initialize.\n\nFor NI-DAQmx devices, the syntax is the device name specified in MAX. Typical default names for NI-DAQmx devices in MAX are Dev2 or PXISlot2. You can rename an NI-DAQmx device in MAX.\n\nYou can also specify the name of an IVI logical name configured with the IVI Configuration utility. Refer to the *IVI* topic of the *Measurement & Automation Explorer Help* for more information.',
                    'note': 'NI-RFSG device names are not case-sensitive. However, all IVI names, such as logical names, are case-sensitive. If you use an IVI logical name, make sure the name is identical to the name shown in the IVI Configuration Utility.'
                },
                'name': 'resourceName',
                'type': 'ViRsrc',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'default_value': False,
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies whether you want NI-RFSG to perform an ID query.\n\n**Defined Values** :',
                    'table_body': [
                        [
                            'VI_TRUE (1)',
                            'Perform ID query.'
                        ],
                        [
                            'VI_FALSE (0)',
                            'Do not perform ID query.'
                        ]
                    ],
                    'table_header': [
                        'Value',
                        'Description'
                    ]
                },
                'name': 'idQuery',
                'type': 'ViBoolean',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'default_value': False,
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies whether you want to reset the NI-RFSG device during the initialization procedure.\n\n**Defined Values** :',
                    'table_body': [
                        [
                            'VI_TRUE (1)',
                            'Reset device.'
                        ],
                        [
                            'VI_FALSE (0)',
                            'Do not reset device.'
                        ]
                    ],
                    'table_header': [
                        'Value',
                        'Description'
                    ]
                },
                'name': 'resetDevice',
                'type': 'ViBoolean',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'default_value': '""',
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the initial value of certain attributes for the session. The following table lists the attributes and the name you pass in this parameter to identify the attribute.\n\nThe format of this string consists of the following relations:\n"AttributeName=Value"\n\nwhere\n*AttributeName* is the name of the attribute and *Value* is the value to which the attribute is set. To set multiple attributes, separate their assignments with a comma, as shown in the following option string:\n\n"RangeCheck=1,QueryInstrStatus=0,Cache=1,DriverSetup=AWG:pxi1slot4"\n\nThe `DriverSetup string <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/driver_setup_string.html>`_ is required in order to simulate a specific device.',
                    'table_body': [
                        [
                            'RangeCheck',
                            'NIRFSG_ATTR_RANGE_CHECK'
                        ],
                        [
                            'QueryInstrStatus',
                            'NIRFSG_ATTR_QUERY_INSTRUMENT_STATUS'
                        ],
                        [
                            'Cache',
                            'NIRFSG_ATTR_CACHE'
                        ],
                        [
                            'RecordCoercions',
                            'NIRFSG_ATTR_RECORD_COERCIONS'
                        ],
                        [
                            'Simulate',
                            'NIRFSG_ATTR_SIMULATE'
                        ]
                    ],
                    'table_header': [
                        'Name',
                        'Attribute Name'
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
            'description': '\nInitiates signal generation, causing the NI-RFSG device to leave the Configuration state and enter the Generation state.\n\nIf the settings have not been committed to the device before you call this function, they are committed by this function. The operation returns when the RF output signal settles. To return to the Configuration state, call the nirfsg_Abort function.\n\n**Supported Devices** : PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`NI-RFSG Instrument Driver Programming Flow <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/progflow.html>`_'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'LoadConfigurationsFromFile': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nLoads the configurations from the specified file to the NI-RFSG driver session.\n\nThe VI does an implicit reset before loading the configurations from the file.\n\n**Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the channel.'
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
        'returns': 'ViStatus'
    },
    'LockSession': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nObtains a multithread lock on the instrument session.\n\nBefore doing so, this function waits until all other execution threads have released their locks on the instrument session.\n\nOther threads might have obtained a lock on this session in the following ways:\n\n- Your application already called the nirfsg_LockSession function.\n- A call to NI-RFSG locked the session.\n\nAfter the call to this function returns successfully, no other threads can access the instrument session until you call the nirfsg_UnlockSession function. Use the nirfsg_LockSession function and the nirfsg_UnlockSession function around a sequence of calls to NI-RFSG functions if you require that the NI-RFSG device retain its settings through the end of the sequence.\n\nYou can safely make nested calls to the nirfsg_LockSession function within the same thread. To completely unlock the session, balance each call to the nirfsg_LockSession function with a call to the nirfsg_UnlockSession function. If, however, you use the NIRFSG_ATTR_CALLER_HAS_LOCK parameter in all calls to the nirfsg_LockSession function and the nirfsg_UnlockSession function within a function, the IVI Library locks the session only once within the function regardless of the number of calls you make to the nirfsg_LockSession function. Locking the session only once allows you to call nirfsg_UnlockSession just once at the end of the function.\n\n**Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5840/5841/5842/5860'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Keeps track of whether you obtain a lock and therefore need to unlock the session. Pass the address of a local ViBoolean variable. In the declaration of the local variable, initialize it to VI_FALSE. Pass the address of the same local variable to any other calls you make to the nirfsg_LockSession function or the nirfsg_UnlockSession function in the same function.\n\nThis parameter serves as a convenience. If you do not want to use this parameter, pass VI_NULL.\n\nThe parameter is an input/output parameter. The nirfsg_LockSession function and the nirfsg_UnlockSession each inspect the current value and take the following actions:\n\n- If the value is VI_TRUE, the nirfsg_LockSession function does not lock the session again. If the value is VI_FALSE, the nirfsg_LockSession function obtains the lock and sets the value of the parameter to VI_TRUE.\n- If the value is VI_FALSE, the nirfsg_UnlockSession function does not attempt to unlock the session. If the value is VI_TRUE, the nirfsg_UnlockSession function releases the lock and sets the value of the parameter to VI_FALSE.\n\nThus, you can call the nirfsg_UnlockSession function at the end of your function without worrying about whether you have the lock.\n\nExample:\n\nViStatus TestFunc (ViSession vi, ViInt32 flags)\n{\nViStatus error = VI_SUCCESS;\nViBoolean haveLock = VI_FALSE;\n\nif (flags & BIT_1)\n{\nviCheckErr( nirfsg_LockSession(vi, &haveLock));\nviCheckErr( TakeAction1(vi));\nif (flags & BIT_2)\n{\nviCheckErr( nirfsg_UnlockSession(vi, &haveLock));\nviCheckErr( TakeAction2(vi));\nviCheckErr( nirfsg_LockSession(vi, &haveLock));\n}\nif (flags & BIT_3)\nviCheckErr( TakeAction3(vi));\n}\n\nError:\n\nAt this point, you cannot really be sure that you have the lock.\nFortunately, the haveLock variable takes care of that for you.\n\nnirfsg_UnlockSession(vi, &haveLock);\nreturn error;\n}'
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
            'description': '\nPerforms a power search if the NIRFSG_ATTR_ALC_CONTROL attribute is disabled.\n\nCalling this function disables modulation for a short time while the device levels the output signal.\n\n**Supported Devices** : PXIe-5654 with PXIe-5696\n\n**Related Topics**\n\n`Power Search <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_power_search.html>`_',
            'note': 'Power search temporarily enables the ALC, so ensure the appropriate included cable is connected between the PXIe-5654 ALCIN connector and the PXIe-5696 ALCOUT connector to successfully perform a power search.'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'PerformThermalCorrection': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nCorrects for any signal drift due to environmental temperature variation when generating the same signal for extended periods of time without a parameter change.\n\nUnder normal circumstances of short-term signal generation, NI-RFSG performs thermal correction automatically by ensuring stable power levels, and you do not need to call this function.\n\nUse this function when generating the same signal for an extended period of time in a temperature-fluctuating environment. The NI-RFSG device must be in the Generation state before calling this function.\n\n**Supported Devices** : PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Thermal Management <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/thermal_management.html>`_\n\n`Impairment Calibration <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/vector_calibration.html>`_'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'QueryArbWaveformCapabilities': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nQueries and returns the waveform capabilities of the NI-RFSG device.\n\nThese capabilities are related to the current device configuration. The NI-RFSG device must be in the Configuration or the Generation state before calling this function.\n\n**Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
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
        'returns': 'ViStatus'
    },
    'ReadAndDownloadWaveformFromFileTDMS': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nReads the waveforms from a TDMS file and downloads one waveform into each of the NI RF vector signal generators.\n\nThis function reads the following information from the TDMS file and writes it into the NI-RFSG session:\n\n- Sample Rate\n- PAPR\n- Runtime Scaling\n- RF Blanking Marker Locations\n- RF Blanking Enabled\n- Burst Start Locations\n- Burst Stop Locations\n- RF Blanking Marker Source\n- Signal Bandwidth\n- Waveform Size\n\nIf RF blanking marker locations are present in the file but burst locations are not present, burst locations are calculated from RF blanking marker locations and stored in the NI-RFSG session.\n\n**Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name used to store the waveform. This string is case-insensitive.\n\nExample:\n\n"waveform::waveform0"'
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
        'returns': 'ViStatus'
    },
    'ResetAttribute': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nResets the attribute to its default value.\n\n**Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the channel.'
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
        'returns': 'ViStatus'
    },
    'ResetDevice': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nPerforms a hard reset on the device which consists of the following actions:\n\n- Signal generation is stopped.\n- All routes are released.\n- External bidirectional terminals are tristated.\n- FPGAs are reset.\n- Hardware is configured to its default state.\n- All session attributes are reset to their default states.\n\nDuring a device reset, routes of signals between this and other devices are released, regardless of which device created the route.\n\n- PXI-5610, PXI-5670/5671, PXIe-5672-- After calling this function, the device requires 25 seconds before returning to full functionality. NI-RFSG enforces this condition by adding a wait, if needed, the next time you try to access the device.\n\n**Supported Devices** : PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E\n\n**Related Topics**\n\n`Thermal Shutdown <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/thermal_shutdown_monitoring_5650_5651_5652.html>`_',
            'note': 'You must call the nirfsg_ResetDevice function if the NI-RFSG device has shut down because of a high-temperature condition.'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'ResetWithDefaults': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nPerforms a software reset of the device, returning it to the default state and applying any initial default settings from the IVI Configuration Store.\n\n**Supported Devices** : PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696,PXI-5670/5671, PXIe-5672/5673/5673E'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'ResetWithOptions': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nResets all properties to default values and specifies steps to omit during the reset process, such as signal routes.\n\nBy default, this function exhibits the same behavior as nirfsg_Reset. You can specify steps to omit using the steps to omit parameter. For example, if you specify NIRFSG_VAL_RESET_WITH_OPTIONS_ROUTES for the NIRFSG_ATTR_STEPS_TO_OMIT parameter, this function does not release signal routes during the reset process.\n\nWhen routes of signals between two devices are released, they are released regardless of which device created the route.\n\nTo avoid resetting routes on PXIe-5820/5830/5831/5832/5840/5841/5842/5860 that are in use by NI-RFSA sessions, NI recommends using this function instead of nirfsg_Reset, with NIRFSG_ATTR_STEPS_TO_OMIT set to NIRFSG_VAL_RESET_WITH_OPTIONS_ROUTES.\n\n**Supported Devices** : PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Triggers <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/triggers.html>`_\n\n`Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies a list of steps to skip during the reset process. The default value is NIRFSG_VAL_RESET_WITH_OPTIONS_NONE, which specifies that no step is omitted during reset. **Defined Values** :',
                    'note': 'NIRFSG_VAL_RESET_WITH_OPTIONS_ROUTES is not supported in external calibration or alignment sessions.\nYou can combine multiple enums.ResetWithOptionsStepsToOmit flags using the bitwise OR (|) operator.',
                    'table_body': [
                        [
                            'NIRFSG_VAL_RESET_WITH_OPTIONS_NONE',
                            '0 (0x0)',
                            'No step is omitted during reset.'
                        ],
                        [
                            'NIRFSG_VAL_RESET_WITH_OPTIONS_WAVEFORMS',
                            '1 (0x1)',
                            'Omits clearing waveforms.'
                        ],
                        [
                            'NIRFSG_VAL_RESET_WITH_OPTIONS_SCRIPTS',
                            '2 (0x2)',
                            'Omits clearing scripts.'
                        ],
                        [
                            'NIRFSG_VAL_RESET_WITH_OPTIONS_ROUTES',
                            '4 (0x4)',
                            'Omits the routing reset step. Routing is preserved after a reset. However, routing related properties are reset to default, and routing is released if the default properties are committed after a reset.'
                        ],
                        [
                            'NIRFSG_VAL_RESET_WITH_OPTIONS_DEEMBEDDING_TABLES',
                            '8 (0x8)',
                            'Omits deleting de-embedding tables. This step is valid only for the PXIe-5830/5831/5832/5840.'
                        ]
                    ],
                    'table_header': [
                        'Name',
                        'Value',
                        'Description'
                    ]
                },
                'enum': 'ResetWithOptionsStepsToOmit',
                'name': 'stepsToOmit',
                'type': 'ViUInt64',
                'type_in_documentation': 'Bitwise combination of enums.ResetWithOptionsStepsToOmit flags',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'RevisionQuery': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nReturns the revision numbers of the NI-RFSG driver and the instrument firmware.\n\n**Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the value of the NIRFSG_ATTR_SPECIFIC_DRIVER_REVISION attribute in the form of a string.\n\nYou must pass a ViChar array with at least 256 bytes.'
                },
                'name': 'instrumentDriverRevision',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the value of the NIRFSG_ATTR_INSTRUMENT_FIRMWARE_REVISION attribute in the form of a string.\n\nYou must pass a ViChar array with at least 256 bytes.'
                },
                'name': 'firmwareRevision',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'SaveConfigurationsToFile': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nSaves the configurations of the session to the specified file.\n\n**Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the channel.'
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
        'returns': 'ViStatus'
    },
    'SelectArbWaveform': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nSpecifies the waveform that is generated upon a call to the nirfsg_Initiate function when the generation_mode property is set to NIRFSG_VAL_ARB_WAVEFORM.\n\nYou must specify a waveform using the NIRFSG_ATTR_NAME parameter if you have written multiple waveforms. The NI-RFSG device must be in the Configuration state before you call this function.\n\n**Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Assigning Properties or Attributes to a Waveform <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/assigning_properties_or_attributes_to_a_waveform.html>`_'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
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
        'returns': 'ViStatus'
    },
    'SelfCal': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nPerforms an internal self-calibration on the device and associated modules that support self-calibration.\n\nIf the calibration is successful, new calibration data and constants are stored in the onboard nonvolatile memory of the module.\n\nThe PXIe-5841 maintains separate self-calibration data for both the PXIe-5841 standalone and when associated with the PXIe-5655. Use this function once for each intended configuration.\n\n**Supported Devices** : PXI-5610, PXIe-5653, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860',
            'note': 'If there is an existing NI-RFSA session open for the same PXIe-5820/5830/5831/5832/5840/5841/5842/5860 while this function runs, it may remain open but cannot be used for operations that access the hardware, for example niRFSA_Commit or niRFSA_Initiate.'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'SelfCalibrateRange': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nSelf-calibrates all configurations within the specified frequency and peak power level limits.\n\nSelf-calibration range data is valid until you restart the system or call the nirfsg_ClearSelfCalibrateRange function.\n\nNI recommends that no external signals are present on the RF In or IQ In ports during the calibration.\n\nFor best results, NI recommends that you perform self-calibration without omitting any steps. However, if certain aspects of performance are less important for your application, you can omit certain steps for faster calibration.\n\n**Supported Devices** : PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842',
            'note': '- This function does not update self-calibration date and temperature.\n\n - If there is an existing NI-RFSA session open for the same PXIe-5644/5645/5646, it may remain open but cannot be used while this function runs.\n\n - If there is an existing NI-RFSA session open for the same PXIe-5820/5830/5831/5832/5840/5841/5842 while this function runs, it may remain open but cannot be used for operations that access the hardware, for example niRFSA_Commit or niRFSA_Initiate.'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies which calibration steps to skip during the self-calibration process. The default value is an empty array, which indicates that no calibration steps are omitted.\n\n**Default Value** : NIRFSG_VAL_SELF_CAL_OMIT_NONE\n\n**Defined Values:**',
                    'note': 'You can combine multiple enums.SelfCalibrateRangeStepsToOmit flags using the bitwise OR (|) operator.',
                    'table_body': [
                        [
                            'NIRFSG_VAL_SELF_CAL_OMIT_NONE',
                            '0 (0x0)',
                            'No calibration steps are omitted.'
                        ],
                        [
                            'NIRFSG_VAL_SELF_CAL_LO_SELF_CAL',
                            '1 (0x1)',
                            'Omits the LO Self Cal step. If you omit this step, the power level of the LO is not adjusted.'
                        ],
                        [
                            'NIRFSG_VAL_SELF_CAL_POWER_LEVEL_ACCURACY',
                            '2 (0x2)',
                            'Omits the Power Level Accuracy step. If you omit this step, the power level accuracy of the device is not adjusted.'
                        ],
                        [
                            'NIRFSG_VAL_SELF_CAL_RESIDUAL_LO_POWER',
                            '4 (0x4)',
                            'Omits the Residual LO Power step. If you omit this step, the Residual LO Power performance is not adjusted.'
                        ],
                        [
                            'NIRFSG_VAL_SELF_CAL_IMAGE_SUPPRESSION',
                            '8 (0x8)',
                            'Omits the Image Suppression step. If you omit this step, the Residual Sideband Image performance is not adjusted.'
                        ],
                        [
                            'NIRFSG_VAL_SELF_CAL_SYNTHESIZER_ALIGNMENT',
                            '16 (0x10)',
                            'Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.'
                        ]
                    ],
                    'table_header': [
                        'Name',
                        'Value',
                        'Description'
                    ]
                },
                'enum': 'SelfCalibrateRangeStepsToOmit',
                'name': 'stepsToOmit',
                'type': 'ViInt64',
                'type_in_documentation': 'Bitwise combination of enums.SelfCalibrateRangeStepsToOmit flags',
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
        'returns': 'ViStatus'
    },
    'SelfTest': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nPerforms a self-test on the NI-RFSG device and returns the test results.\n\nThis function performs a simple series of tests to ensure that the NI-RFSG device is powered up and responding.\n\nThis function does not affect external I/O connections or connections between devices. Complete functional testing and calibration are not performed by this function. The NI-RFSG device must be in the Configuration state before you call this function.\n\n**Supported Devices** : PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Device Warm-Up <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/warmup.html>`_'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'This parameter contains the value returned from the NI-RFSG device self test.',
                    'table_body': [
                        [
                            '0',
                            'Self test passed'
                        ],
                        [
                            '1',
                            'Self test failed'
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
                'direction': 'in',
                'documentation': {
                    'description': 'Returns the self-test response string from the NI-RFSG device. For an explanation of the string contents, refer to the **status** parameter of this function.\n\nYou must pass a ViChar array with at least 256 bytes.'
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
            'description': '\nForces a trigger to occur.\n\nThe specified trigger generates regardless of whether the trigger has been configured as a software trigger.\n\n**Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Triggers <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/triggers.html>`_'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the trigger to send.\n\n**Default Value:** NIRFSG_VAL_START_TRIGGER\n\n**Defined Values:**',
                    'table_body': [
                        [
                            'NIRFSG_VAL_START_TRIGGER',
                            '0 (0x0)',
                            'Specifies the Start Trigger.'
                        ],
                        [
                            'NIRFSG_VAL_SCRIPT_TRIGGER',
                            '1 (0x1)',
                            'Specifies the Script Trigger.'
                        ]
                    ],
                    'table_header': [
                        'Name',
                        'Value',
                        'Description'
                    ]
                },
                'enum': 'SoftwareTriggerType',
                'name': 'trigger',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the Script Trigger to configure. This parameter is valid only when you set the NIRFSG_ATTR_TRIGGER parameter to NIRFSG_VAL_START_TRIGGER. Otherwise, set the NIRFSG_ATTR_TRIGGER_IDENTIFIER parameter to "" (empty string).\n\n**Default Value:** "" (empty string)\n\n**Possible Values:**',
                    'table_body': [
                        [
                            'scriptTrigger0',
                            'Specifies Script Trigger 0.'
                        ],
                        [
                            'scriptTrigger1',
                            'Specifies Script Trigger 1.'
                        ],
                        [
                            'scriptTrigger2',
                            'Specifies Script Trigger 2.'
                        ],
                        [
                            'scriptTrigger3',
                            'Specifies Script Trigger 3.'
                        ],
                        [
                            '',
                            'None (no signal to export)'
                        ]
                    ],
                    'table_header': [
                        'Possible Value',
                        'Description'
                    ]
                },
                'name': 'triggerIdentifier',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'render_in_session_base': True,
        'returns': 'ViStatus'
    },
    'SetArbWaveformNextWritePosition': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nConfigures the start position to use for writing a waveform before calling the nirfsg_WriteArbWaveform function.\n\nThis function allows you to write to arbitrary locations within the waveform. These settings apply only to the next write to the waveform specified by the **name** input of the nirfsg_AllocateArbWaveform function or the nirfsg_WriteArbWaveform function. Subsequent writes to that waveform begin where the last write ended, unless this function is called again.\n\n**Supported Devices** : PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860',
            'note': 'If you use this function to write the waveform that is currently generating, an undefined output may result.'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the waveform. This string is case-insensitive and alphanumeric, and it cannot use `reserved words <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/scripting_instructions.html>`_.'
                },
                'name': 'waveformName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the reference position in the waveform. The position and NIRFSG_ATTR_OFFSET together determine where to start loading data into the waveform.\n\n**Defined Values:**',
                    'table_body': [
                        [
                            'NIRFSG_VAL_START_OF_WAVEFORM',
                            '8000 (0x1f40)',
                            'The reference position is relative to the start of the waveform.'
                        ],
                        [
                            'NIRFSG_VAL_CURRENT_POSITION',
                            '8001 (0x1f41)',
                            'The reference position is relative to the current position.'
                        ]
                    ],
                    'table_header': [
                        'Name',
                        'Value',
                        'Description'
                    ]
                },
                'enum': 'RelativeTo',
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
        'returns': 'ViStatus'
    },
    'SetAttributeViBoolean': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nSets the value of a ViBoolean attribute.\n\nUse this low-level function to set the values of inherent IVI attributes, class-defined attributes, and instrument-specific attributes. If the attribute represents an instrument state, this function performs instrument I/O in the following cases:\n\n- State caching is disabled for the entire session or for the particular attribute.\n- State caching is enabled, and the currently cached value is invalid or is different than the value you specify.\n\nNI-RFSG contains high-level functions that set most of the instrument attributes. Use the high-level driver functions as much as possible, as they handle order dependencies and multithread locking. The high-level functions also perform status checking only after setting all of the attributes. In contrast, when you set multiple attributes using the SetAttribute functions, the functions check the instrument status after each call.\n\nAlso, when state caching is enabled, the high-level functions that configure multiple attributes perform instrument I/O only for the attributes whose value you change. Thus, you can safely call the high-level functions without the penalty of redundant instrument I/O.'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.\n\nExample:\n\n"waveform::waveform0/marker0"'
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
                    'description': 'Pass the value to which you want to set the attribute.',
                    'note': 'Some values may not be valid. The allowed values depend on the current settings of the instrument session.'
                },
                'name': 'value',
                'type': 'ViBoolean',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViInt32': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nSets the value of a ViInt32 attribute.\n\nUse this low-level function to set the values of inherent IVI attributes, class-defined attributes, and instrument-specific attributes. If the attribute represents an instrument state, this function performs instrument I/O in the following cases:\n\n- State caching is disabled for the entire session or for the particular attribute.\n- State caching is enabled, and the currently cached value is invalid or is different than the value you specify.\n\nNI-RFSG contains high-level functions that set most of the instrument attributes. Use the high-level driver functions as much as possible, as they handle order dependencies and multithread locking. The high-level functions also perform status checking only after setting all of the attributes. In contrast, when you set multiple attributes using the SetAttribute functions, the functions check the instrument status after each call.\n\nAlso, when state caching is enabled, the high-level functions that configure multiple attributes perform instrument I/O only for the attributes whose value you change. Thus, you can safely call the high-level functions without the penalty of redundant instrument I/O.'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.\n\nExample:\n\n"waveform::waveform0/marker0"'
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
                    'description': 'Specifies the value to which you want to set the attribute.',
                    'note': 'Some values may not be valid. The allowed values depend on the current settings of the instrument session.'
                },
                'grpc_enum': 'NiRFSGInt32AttributeValues',
                'name': 'value',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViInt64': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nSets the value of a ViInt64 attribute.\n\nUse this low-level function to set the values of inherent IVI attributes, class-defined attributes, and instrument-specific attributes. If the attribute represents an instrument state, this function performs instrument I/O in the following cases:\n\n- State caching is disabled for the entire session or for the particular attribute.\n- State caching is enabled, and the currently cached value is invalid or is different than the value you specify.\n\nNI-RFSG contains high-level functions that set most of the instrument attributes. Use the high-level driver functions as much as possible, as they handle order dependencies and multithread locking. The high-level functions also perform status checking only after setting all of the attributes. In contrast, when you set multiple attributes using the SetAttribute functions, the functions check the instrument status after each call.\n\nAlso, when state caching is enabled, the high-level functions that configure multiple attributes perform instrument I/O only for the attributes whose value you change. Thus, you can safely call the high-level functions without the penalty of redundant instrument I/O.'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.\n\nExample:\n\n"waveform::waveform0/marker0"'
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
                    'description': 'Pass the value to which you want to set the attribute.\n\n<blockquote>\nSome values may not be valid. The allowed values depend on the current settings of the instrument session.\n</blockquote>'
                },
                'grpc_enum': 'NiRFSGInt64AttributeValues',
                'name': 'value',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViReal64': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nSets the value of a ViReal64 attribute.\n\nUse this low-level function to set the values of inherent IVI attributes, class-defined attributes, and instrument-specific attributes. If the attribute represents an instrument state, this function performs instrument I/O in the following cases:\n\n- State caching is disabled for the entire session or for the particular attribute.\n- State caching is enabled, and the currently cached value is invalid or is different than the value you specify.\n\nNI-RFSG contains high-level functions that set most of the instrument attributes. Use the high-level driver functions as much as possible, as they handle order dependencies and multithread locking. The high-level functions also perform status checking only after setting all of the attributes. In contrast, when you set multiple attributes using the SetAttribute functions, the functions check the instrument status after each call.\n\nAlso, when state caching is enabled, the high-level functions that configure multiple attributes perform instrument I/O only for the attributes whose value you change. Thus, you can safely call the high-level functions without the penalty of redundant instrument I/O.'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.\n\nExample:\n\n"waveform::waveform0/marker0"'
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
                    'description': 'Pass the value to which you want to set the attribute.',
                    'note': 'Some values may not be valid. The allowed values depend on the current settings of the instrument session.'
                },
                'grpc_enum': 'NiRFSGReal64AttributeValues',
                'name': 'value',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViSession': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nSets the value of a ViSession attribute.\n\nUse this low-level function to set the values of inherent IVI attributes, class-defined attributes, and instrument-specific attributes. If the attribute represents an instrument state, this function performs instrument I/O in the following cases:\n\n- State caching is disabled for the entire session or for the particular attribute.\n- State caching is enabled, and the currently cached value is invalid or is different than the value you specify.\n\nNI-RFSG contains high-level functions that set most of the instrument attributes. Use the high-level driver functions as much as possible, as they handle order dependencies and multithread locking. The high-level functions also perform status checking only after setting all of the attributes. In contrast, when you set multiple attributes using the SetAttribute functions, the functions check the instrument status after each call.\n\nAlso, when state caching is enabled, the high-level functions that configure multiple attributes perform instrument I/O only for the attributes whose value you change. Thus, you can safely call the high-level functions without the penalty of redundant instrument I/O.'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.\n\nExample:\n\n"waveform::waveform0/marker0"'
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
                    'description': 'Pass the value to which you want to set the attribute.',
                    'note': 'Some values may not be valid. The allowed values depend on the current settings of the instrument session.'
                },
                'name': 'value',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViString': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nSets the value of a ViString attribute.\n\nUse this low-level function to set the values of inherent IVI attributes, class-defined attributes, and instrument-specific attributes. If the attribute represents an instrument state, this function performs instrument I/O in the following cases:\n\n- State caching is disabled for the entire session or for the particular attribute.\n- State caching is enabled, and the currently cached value is invalid or is different than the value you specify.\n\nNI-RFSG contains high-level functions that set most of the instrument attributes. Use the high-level driver functions as much as possible, as they handle order dependencies and multithread locking. The high-level functions also perform status checking only after setting all of the attributes. In contrast, when you set multiple attributes using the SetAttribute functions, the functions check the instrument status after each call.\n\nAlso, when state caching is enabled, the high-level functions that configure multiple attributes perform instrument I/O only for the attributes whose value you change. Thus, you can safely call the high-level functions without the penalty of redundant instrument I/O.'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.\n\nExample:\n\n"waveform::waveform0/marker0"'
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
                    'description': 'Pass the value to which you want to set the attribute.',
                    'note': 'Some values may not be valid. The allowed values depend on the current settings of the instrument session.'
                },
                'grpc_mapped_enum': 'NiRFSGStringAttributeValuesMapped',
                'name': 'value',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'SetWaveformBurstStartLocations': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nConfigures the start location of the burst in samples where the burst refers to the active portion of a waveform.\n\n**Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842'
        },
        'has_repeated_capability': True,
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name. Example: "waveform::waveform0/marker0"'
                },
                'is_repeated_capability': True,
                'name': 'channelName',
                'repeated_capability_type': 'waveforms',
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
                'use_array': False
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Returns the burst start locations stored in the NI-RFSG session for the waveform that you specified in the NIRFSG_ATTR_CHANNEL_NAME parameter. This value is expressed in samples.'
                },
                'name': 'locations',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfLocations'
                },
                'type': 'ViReal64[]',
                'use_in_python_api': True
            }
        ],
        'repeated_capability_type': 'waveforms',
        'returns': 'ViStatus'
    },
    'SetWaveformBurstStopLocations': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nConfigures the stop location of the burst in samples where the burst refers to the active portion of a waveform.\n\n**Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842'
        },
        'has_repeated_capability': True,
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.\n\nExample:\n\n"waveform::waveform0/marker0"'
                },
                'is_repeated_capability': True,
                'name': 'channelName',
                'repeated_capability_type': 'waveforms',
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
                'use_array': False
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the burst stop locations, in samples, to store in the NI-RFSG session.'
                },
                'name': 'locations',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfLocations'
                },
                'type': 'ViReal64[]',
                'use_in_python_api': True
            }
        ],
        'repeated_capability_type': 'waveforms',
        'returns': 'ViStatus'
    },
    'SetWaveformMarkerEventLocations': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nConfigures the marker locations associated with waveform and marker in the NI-RFSG session.\n\n**Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842'
        },
        'has_repeated_capability': True,
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.\n\nExample:\n\n"waveform::waveform0/marker0"'
                },
                'is_repeated_capability': True,
                'name': 'channelName',
                'repeated_capability_type': 'markers',
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
                'use_array': False
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the marker location, in samples, to store in the NI-RFSG database.'
                },
                'name': 'locations',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfLocations'
                },
                'type': 'ViReal64[]',
                'use_in_python_api': True
            }
        ],
        'repeated_capability_type': 'markers',
        'returns': 'ViStatus'
    },
    'UnlockSession': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nReleases a lock obtained on an NI-RFSG device session by calling the nirfsg_LockSession function.\n\n**Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5840/5841/5842/5860'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Keeps track of whether you obtain a lock and therefore need to unlock the session. Pass the address of a local ViBoolean variable. In the declaration of the local variable, initialize it to VI_FALSE. Pass the address of the same local variable to any other calls you make to the nirfsg_LockSession function or the nirfsg_UnlockSession function in the same function.\n\nThis parameter serves as a convenience. If you do not want to use this parameter, pass VI_NULL.\n\nThe parameter is an input/output parameter. The nirfsg_LockSession function and the nirfsg_UnlockSession each inspect the current value and take the following actions:\n\n- If the value is VI_TRUE, the nirfsg_LockSession function does not lock the session again. If the value is VI_FALSE, the nirfsg_LockSession function obtains the lock and sets the value of the parameter to VI_TRUE.\n- If the value is VI_FALSE, the nirfsg_UnlockSession function does not attempt to unlock the session. If the value is VI_TRUE, the nirfsg_UnlockSession function releases the lock and sets the value of the parameter to VI_FALSE.\n\nThus, you can call the nirfsg_UnlockSession function at the end of your function without worrying about whether you have the lock.\n\nExample:\n\nViStatus TestFunc (ViSession vi, ViInt32 flags)\n{\nViStatus error = VI_SUCCESS;\nViBoolean haveLock = VI_FALSE;\n\nif (flags & BIT_1)\n{\nviCheckErr( nirfsg_LockSession(vi, &haveLock));\nviCheckErr( TakeAction1(vi));\nif (flags & BIT_2)\n{\nviCheckErr( nirfsg_UnlockSession(vi, &haveLock));\nviCheckErr( TakeAction2(vi));\nviCheckErr( nirfsg_LockSession(vi, &haveLock));\n}\nif (flags & BIT_3)\nviCheckErr( TakeAction3(vi));\n}\n\nError:\n\nAt this point, you cannot really be sure that you have the lock.\nFortunately, the haveLock variable takes care of that for you.\n\nnirfsg_UnlockSession(vi, &haveLock);\nreturn error;\n}'
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
            'description': '\nWaits until the RF output signal has settled. This function is useful for devices that support changes while in the Generation state.\n\nCall this function after making a dynamic change to wait for the output signal to settle.\n\nYou can also call this function after calling the nirfsg_Commit function to wait for changes to settle. The nirfsg_WaitUntilSettled function is not required after calling the nirfsg_Initiate function because the nirfsg_Initiate automatically waits for the output to settle.\n\n**Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the maximum time the function waits for the output to settle. If the maximum time is exceeded, this function returns an error. The units are expressed in milliseconds.\n\n**Default Value** : 10000'
                },
                'name': 'maxTimeMilliseconds',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteArbWaveformComplexF32': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nWrites an arbitrary waveform to the NI-RFSG device starting at the position of the last data written in onboard memory.\n\nThis function accepts the complex baseband data in the form of complex singles. If the waveform to write is already allocated using the nirfsg_AllocateArbWaveform function, the more_data_pending parameter is ignored. The PXI-5670/5671 must be in the Configuration state before you call this function. When streaming is enabled, you can call this function when the PXIe-5672/5673/5673E or PXIe-5820/5830/5831/5832/5840/5841/5842/5860 is in the Generation state.\n\n**Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Streaming <https://www.ni.com/docs/en-US/bundle/ni-rfsg/page/streaming.html>`_\n\n`Assigning Properties or Attributes to a Waveform <https://www.ni.com/docs/en-US/bundle/ni-rfsg/page/assigning-properties-or-attributes-to-a-wavef.html>`_',
            'note': 'On the PXIe-5644/5645/5646, PXIe-5672/5673/5673E, and PXIe-5820/5830/5831/5832/5840/5841/5842/5860, the more_data_pending parameter is always ignored. To write data in blocks on these devices, you must allocate the waveform before writing it.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_name_for_documentation': 'write_arb_waveform',
        'method_templates': [
            {
                'documentation_filename': 'numpy_method',
                'library_interpreter_filename': 'numpy_write_method',
                'method_python_name_suffix': '',
                'session_filename': 'numpy_write_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
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
                    'description': 'Specifies the number of samples in both of the data arrays.'
                },
                'name': 'numberOfSamples',
                'type': 'ViInt32',
                'use_array': False
            },
            {
                'complex_type': 'numpy',
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the array of data to load into the waveform. The array must have at least as many elements as the value in the **size_in_samples** parameter in the nirfsg_AllocateArbWaveform function.'
                },
                'name': 'waveformDataArray',
                'numpy': True,
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfSamples'
                },
                'type': 'NIComplexNumberF32[]',
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies whether or not the data block contains the end of the waveform. Set this parameter to VI_TRUE to allow data to be appended later to the waveform. Splitting the waveform into multiple data blocks can reduce the memory requirements of the write operation. Append data to a previously written waveform by using the same waveform in the NIRFSG_ATTR_WAVEFORM_NAME parameter. Set more_data_pending to VI_FALSE to indicate that this data block contains the end of the waveform. If the waveform is already allocated, this parameter is ignored.'
                },
                'name': 'moreDataPending',
                'type': 'ViBoolean',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteArbWaveformComplexF64': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nWrites an arbitrary waveform to the NI-RFSG device starting at the position of the last data written in onboard memory.\n\nThis function accepts the complex baseband data in the form of complex doubles. If the waveform to write is already allocated using the nirfsg_AllocateArbWaveform, the more_data_pending parameter is ignored. The PXI-5670/5671 must be in the Configuration state before you call this function. When streaming is enabled, you can call this function when the PXIe-5672/5673/5673E or PXIe-5820/5830/5831/5832/5840/5841/5842 is in the Generation state.\n\n**Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842\n\n**Related Topics**\n\n`Streaming <https://www.ni.com/docs/en-US/bundle/ni-rfsg/page/streaming.html>`_\n\n`Assigning Properties or Attributes to a Waveform <https://www.ni.com/docs/en-US/bundle/ni-rfsg/page/assigning-properties-or-attributes-to-a-wavef.html>`_',
            'note': 'On the PXIe-5644/5645/5646, PXIe-5672/5673/5673E, and PXIe-5820/5830/5831/5832/5840/5841/5842, the more_data_pending parameter is always ignored. To write data in blocks on these devices, you must allocate the waveform before writing it.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_name_for_documentation': 'write_arb_waveform',
        'method_templates': [
            {
                'documentation_filename': 'numpy_method',
                'library_interpreter_filename': 'numpy_write_method',
                'method_python_name_suffix': '',
                'session_filename': 'numpy_write_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
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
                    'description': 'Specifies the number of samples in the data array.'
                },
                'name': 'numberOfSamples',
                'type': 'ViInt32',
                'use_array': False
            },
            {
                'complex_type': 'numpy',
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the array of data to load into the waveform. The array must have at least as many elements as the value in the **size_in_samples** parameter in the nirfsg_AllocateArbWaveform function.'
                },
                'name': 'waveformDataArray',
                'numpy': True,
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfSamples'
                },
                'type': 'NIComplexNumber[]',
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies whether or not the data block contains the end of the waveform. Set this parameter to VI_TRUE to allow data to be appended later to the waveform. Splitting the waveform into multiple data blocks can reduce the memory requirements of the write operation. Append data to a previously written waveform by using the same waveform in the **name** parameter. Set more_data_pending to VI_FALSE to indicate that this data block contains the end of the waveform. If the waveform is already allocated, this parameter is ignored.'
                },
                'name': 'moreDataPending',
                'type': 'ViBoolean',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteArbWaveformComplexI16': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nWrites an arbitrary waveform to the NI-RFSG device starting at the position of the last data written in onboard memory.\n\nThis function accepts the interleaved I/Q data of a complex baseband signal. The PXI-5670/5671 must be in the Configuration state before you call this function. When streaming is enabled, this function can be called when the PXIe-5672/5673/5673E or PXIe-5820/5830/5831/5832/5840/5841/5842/5860 is in the Generation state.\n\n**Supported Devices** : PXIe-5644/5645/5646, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Streaming <https://www.ni.com/docs/en-US/bundle/ni-rfsg/page/streaming.html>`_\n\n`Assigning Properties or Attributes to a Waveform <https://www.ni.com/docs/en-US/bundle/ni-rfsg/page/assigning-properties-or-attributes-to-a-wavef.html>`_',
            'note': 'This function only supports NIRFSG_VAL_PEAK_POWER mode as specified in the NIRFSG_ATTR_POWER_LEVEL_TYPE attribute. If you download a waveform when using this function, you cannot set the NIRFSG_ATTR_POWER_LEVEL_TYPE to NIRFSG_VAL_AVERAGE_POWER without causing error in the output.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_name_for_documentation': 'write_arb_waveform',
        'method_templates': [
            {
                'documentation_filename': 'numpy_method',
                'library_interpreter_filename': 'numpy_write_method',
                'method_python_name_suffix': '',
                'session_filename': 'numpy_write_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
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
                    'description': 'Specifies the number of samples in the data array.'
                },
                'name': 'numberOfSamples',
                'type': 'ViInt32',
                'use_array': False
            },
            {
                'complex_type': 'interleaved',
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the array of data to load into the waveform. The array must have at least as many elements as the value in the **size_in_samples** parameter in the nirfsg_AllocateArbWaveform function.'
                },
                'name': 'waveformDataArray',
                'numpy': True,
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfSamples'
                },
                'type': 'NIComplexI16[]',
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteArbWaveformDispatcher': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': '\nWrites an arbitrary waveform to the NI-RFSG device starting at the position of the last data written in onboard memory.\n\nThis function accepts the complex baseband data in the form of numpy array of numpy.complex64 or numpy.complex128 or interleaved numpy array of numpy.int16. If the waveform to write is already allocated using the nirfsg_AllocateArbWaveform, the more_data_pending parameter is ignored. The PXI-5670/5671 must be in the Configuration state before you call this function. When streaming is enabled, you can call this function when the PXIe-5672/5673/5673E or PXIe-5820/5830/5831/5832/5840/5841/5842/5860 is in the Generation state.\n\n**Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Streaming <https://www.ni.com/docs/en-US/bundle/ni-rfsg/page/streaming.html>`_\n\n`Assigning Properties or Attributes to a Waveform <https://www.ni.com/docs/en-US/bundle/ni-rfsg/page/assigning-properties-or-attributes-to-a-wavef.html>`_',
            'note': 'On the PXIe-5644/5645/5646, PXIe-5672/5673/5673E, and PXIe-5820/5830/5831/5832/5840/5841/5842/5860, the more_data_pending parameter is always ignored. To write data in blocks on these devices, you must allocate the waveform before writing it.\nIf you are writing interleaved numpy array of numpy.int16, then this function only supports NIRFSG_VAL_PEAK_POWER mode as specified in the NIRFSG_ATTR_POWER_LEVEL_TYPE attribute. If you download a waveform as interleaved numpy array of numpy.int16 when using this function, you cannot set the NIRFSG_ATTR_POWER_LEVEL_TYPE to NIRFSG_VAL_AVERAGE_POWER without causing error in the output.'
        },
        'included_in_proto': False,
        'is_error_handling': False,
        'method_name_for_documentation': 'write_arb_waveform',
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '',
                'session_filename': 'write_arb_waveform'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
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
                'complex_type': 'numpy',
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the array of data to load into the waveform. The array must have at least as many elements as the value in the **size_in_samples** parameter in the nirfsg_AllocateArbWaveform function.'
                },
                'name': 'waveformDataArray',
                'numpy': True,
                'type': 'NIComplexNumber[]',
                'type_in_documentation': 'numpy array of numpy.complex64, numpy array of numpy.complex128 or interleaved complex data in the form of numpy array of numpy.int16',
                'use_in_python_api': True
            },
            {
                'default_value': False,
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies whether or not the data block contains the end of the waveform. Set this parameter to VI_TRUE to allow data to be appended later to the waveform. Splitting the waveform into multiple data blocks can reduce the memory requirements of the write operation. Append data to a previously written waveform by using the same waveform in the **name** parameter. Set more_data_pending to VI_FALSE to indicate that this data block contains the end of the waveform. If the waveform is already allocated, this parameter is ignored.'
                },
                'name': 'moreDataPending',
                'type': 'ViBoolean',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'python_name': 'write_arb_waveform',
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'WriteScript': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nWrites a script to the device to control waveform generation in Script mode.\n\nFirst, configure your device for Script mode by setting the generation_mode property. The NI-RFSG device must be in the Configuration state before calling the nirfsg_WriteScript function.\n\n**Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Scripting Instructions <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/scripting_instructions.html>`_--Refer to this topic for more information about VST restrictions on scripts.\n\n`Common Scripting Use Cases <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/scripting_use_cases.html>`_',
            'note': 'If you are using an RF vector signal transceiver (VST) device, some script instructions may not be supported.'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
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
        'returns': 'ViStatus'
    },
    'close': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nAborts any signal generation in progress and destroys the instrument driver session.\n\n**Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`NI-RFSG Instrument Driver Programming Flow <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/progflow.html>`_\n\n`NI-RFSG Programming State Model <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5670_programming_state_model.html>`_'
        },
        'grpc_name': 'Close',
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
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
    },
    'reset': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nResets all attributes to their default values and moves the NI-RFSG device to the Configuration state.\n\nThis function aborts the generation, deletes all de-embedding tables, clears all routes, and resets session attributes to their initial values. During a reset, routes of signals between this and other devices are released, regardless of which device created the route.\n\nGenerally, calling this function instead of the nirfsg_ResetDevice function is acceptable. The nirfsg_Reset function executes faster than the nirfsg_ResetDevice function.\n\nTo avoid resetting routes on the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842/5860 that are in use by NI-RFSA sessions, NI recommends using the nirfsg_ResetWithOptions function, with **stepsToOmit** set to NIRFSG_VAL_RESET_WITH_OPTIONS_ROUTES .\n\n**Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860',
            'note': 'This function resets all configured routes for the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842/5860 in NI-RFSA and NI-RFSG.'
        },
        'grpc_name': 'Reset',
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    }
}
