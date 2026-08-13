# -*- coding: utf-8 -*-
# This file is generated from NI-RFSA API metadata version 26.5.0d9999
functions = {
    'Abort': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Stops an acquisition previously started with the nirfsa_Initiate function or the nirfsa_ReadPowerSpectrumF64 function.\n\nYou can also use the nirfsa_Abort function to stop a self-calibration. Calling this function is optional, unless you want to stop an acquisition before it is complete or you are continuously acquiring data.\n\nYou can stop the following kinds of acquisitions:\n\n- Triggered spectrum acquisitions that have not yet been triggered\n- Multispan acquisitions in progress\n- Average spectrum acquisitions in progress\n- Single-record spectrum acquisitions in progress\n- Streaming in progress\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
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
    'ChangeExternalCalibrationPassword': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Changes the password that is required to initialize an external calibration session.\n\n**Supported Devices**: PXIe-5601/5603/5605/5606, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function and identifies a particular instrument session.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the old (current) external calibration password.\n\nThe maximum length of the password varies by device.',
                },
                'name': 'oldPassword',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the new (desired) external calibration password.\n\nThe maximum length of the password varies by device.',
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
    'CheckAcquisitionStatus': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Checks the status of the acquisition.\n\nUse this function to check for any errors that may occur during signal acquisition or to check whether the device has completed the acquisition operation.\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`NI RF Vector Signal Analyzer State Diagram <https://www.ni.com/docs/en-US/bundle/pxie-5667-feature/page/hardware-state-diagram.html>`_',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns signal acquisition status.\n\n|Value          |Description                                     |\n|:---------|:------------------------------------|\n| VI_TRUE  | Signal acquisition is complete.     |\n| VI_FALSE | Signal acquisition is not complete. |',
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
    'ClearSelfCalibrateRange': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Clears the data obtained from the nirfsa_SelfCalibrateRange function.\n\n**Supported Devices**: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
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
    'close': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Closes the session to the device.\n\nIf you close a session that has Soft Front Panel (SFP) session access enabled, any application connected to the shared device session is no longer usable. Refer to `Debugging Your Application Using SFP Session Access <https://www.ni.com/docs/en-US/bundle/ni-rfsa-sfp/page/rfsasfp/using_session_access_sfp_top.html>`_ for more information about using SFP session access.\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860',
        },
        'included_in_proto': True,
        'grpc_name': 'Close',
        'is_error_handling': False,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
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
    'Commit': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Commits settings to hardware.\n\nCalling this function is optional. Settings are automatically committed to hardware when you call the nirfsa_Initiate function, the read IQ single record complex F64 function, or the nirfsa_ReadPowerSpectrumF64 function.\n\n----\n**Note**\nThis function does not wait for settling time, unlike the nirfsa_Initiate function.\n\n----\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`NI RF Vector Signal Analyzer State Diagram <https://www.ni.com/docs/en-US/bundle/pxie-5667-feature/page/hardware-state-diagram.html>`_',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
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
            'description': '\nSelects the linear interpolation method.\n\nIf the carrier frequency does not match a row in the de-embedding table, NI-RFSA performs a linear interpolation based on the entries in the de-embedding table to determine the parameters to use for de-embedding.\n\n**Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).',
                },
                'name': 'port',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the table.',
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
                            'NIRFSA_VAL_LINEAR_INTERPOLATION_FORMAT_REAL_AND_IMAGINARY',
                            'Results in a linear interpolation of the real portion of the complex number and a separate linear interpolation of the complex portion.'
                        ],
                        [
                            'NIRFSA_VAL_LINEAR_INTERPOLATION_FORMAT_MAGNITUDE_AND_PHASE',
                            'Results in a linear interpolation of the magnitude and a separate linear interpolation of the phase.'
                        ],
                        [
                            'NIRFSA_VAL_LINEAR_INTERPOLATION_FORMAT_MAGNITUDE_DB_AND_PHASE',
                            'Results in a linear interpolation of the magnitude, in decibels, and a separate linear interpolation of the phase.'
                        ]
                    ],
                    'table_header': [
                        'Name',
                        'Description'
                    ]
                },
                'enum': 'LinearInterpolationFormat',
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
            'description': '\nSelects the nearest interpolation method.\n\nNI-RFSA uses the parameters of the table nearest to the carrier frequency for de-embedding.\n\n**Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).',
                },
                'name': 'port',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the table.',
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
            'description': '\nSelects the spline interpolation method.\n\nIf the carrier frequency does not match a row in the de-embedding table, NI-RFSA performs a spline interpolation based on the entries in the de-embedding table to determine the parameters to use for de-embedding.\n\n**Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).',
                },
                'name': 'port',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the table.',
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
    'ConfigureDigitalEdgeAdvanceTrigger': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Configures the device to wait for a digital edge Advance Trigger.\n\nThe Advance Trigger indicates where a new record begins.\n\n----\n**Note**\n This function is not supported if you set the **acquisitionType** parameter to NIRFSA_VAL_SPECTRUM using the nirfsa_ConfigureAcquisitionType function or if you set the NIRFSA_ATTR_ACQUISITION_TYPE attribute to NIRFSA_VAL_SPECTRUM.\n\n----\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the source of the digital edge for the Advance Trigger.\n\n| Value                                           | Description                                                                                                                                                                                                                |\n|:-------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|\n| NIRFSA_VAL_PFI0 (\'PFI0\')               | The trigger is received on PFI 0. For the PXIe-5841 with PXIe-5655, the trigger is received on the PXIe-5841 PFI 0.                                                                                            |\n| NIRFSA_VAL_PFI1 (\'PFI1\')               | The trigger is received on PFI 1.                                                                                                                                                                              |\n| NIRFSA_VAL_PXI_TRIG0 (\'PXI_Trig0\')     | The trigger is received on PXI trigger line 0.                                                                                                                                                                 |\n| NIRFSA_VAL_PXI_TRIG1 (\'PXI_Trig1\')     | The trigger is received on PXI trigger line 1.                                                                                                                                                                 |\n| NIRFSA_VAL_PXI_TRIG2 (\'PXI_Trig2\')     | The trigger is received on PXI trigger line 2.                                                                                                                                                                 |\n| NIRFSA_VAL_PXI_TRIG3 (\'PXI_Trig3\')     | The trigger is received on PXI trigger line 3.                                                                                                                                                                 |\n| NIRFSA_VAL_PXI_TRIG4 (\'PXI_Trig4\')     | The trigger is received on PXI trigger line 4.                                                                                                                                                                 |\n| NIRFSA_VAL_PXI_TRIG5 (\'PXI_Trig5\')     | The trigger is received on PXI trigger line 5.                                                                                                                                                                 |\n| NIRFSA_VAL_PXI_TRIG6 (\'PXI_Trig6\')     | The trigger is received on PXI trigger line 6.                                                                                                                                                                 |\n| NIRFSA_VAL_PXI_TRIG7 (\'PXI_Trig7\')     | The trigger is received on PXI trigger line 7.                                                                                                                                                                 |\n| NIRFSA_VAL_PXI_STAR (\'PXI_STAR\')       | The trigger is received on the PXI star trigger line. This value is not supported for PXIe-5644/5645/5646 devices.                                                                                             |\n| NIRFSA_VAL_PXIE_DSTARB (\'PXIE_DSTARB\') | The trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860.                                                                        |\n| NIRFSA_VAL_TIMER_EVENT (\'TimerEvent\')  | The trigger is received from Timer Event on the digitizer. This value is valid on only the PXIe-5820/5840/5841/5842/5860 and for digital edge Advance Triggers on the PXIe-5644/5645/5646 and PXIe-5663E/5665. |\n| NIRFSA_VAL_DIO_PFI0 (\'PFI0\')               | The trigger is received on PFI 0 of the DIO Terminal.                                                                                                                                                          |\n| NIRFSA_VAL_DIO_PFI1(\'PFI1\')               | The trigger is received on PFI 1 of the DIO Terminal.                                                                                                                                                          |\n| NIRFSA_VAL_DIO_PFI2 (\'PFI2\')               | The trigger is received on PFI 2 of the DIO Terminal.                                                                                                                                                          |\n| NIRFSA_VAL_DIO_PFI3 (\'PFI3\')               | The trigger is received on PFI 3 of the DIO Terminal.                                                                                                                                                          |\n| NIRFSA_VAL_DIO_PFI4 (\'PFI4\')               | The trigger is received on PFI 4 of the DIO Terminal.                                                                                                                                                          |\n| NIRFSA_VAL_DIO_PFI5 (\'PFI5\')               | The trigger is received on PFI 5 of the DIO Terminal.                                                                                                                                                          |\n| NIRFSA_VAL_DIO_PFI6 (\'PFI6\')               | The trigger is received on PFI 6 of the DIO Terminal.                                                                                                                                                          |\n| NIRFSA_VAL_DIO_PFI7 (\'PFI7\')               | The trigger is received on PFI 7 of the DIO Terminal. |',
                },
                'grpc_name': 'source_raw',
                'name': 'source',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the trigger edge to detect. The default value is NIRFSA_VAL_RISING_EDGE.\n\n| Value                              | Description                                |\n|:------------------------------|:--------------------------------|\n| NIRFSA_VAL_RISING_EDGE (900)  | NI-RFSA detects a rising edge.  |\n| NIRFSA_VAL_FALLING_EDGE (901) | NI-RFSA detects a falling edge. |',
                },
                'enum': 'AdvanceTriggerDigitalEdgeEdge',
                'name': 'edge',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ConfigureDigitalEdgeRefTrigger': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Configures the device to wait for a digital edge Reference Trigger to mark a reference point within the record.\n\nYou can use this trigger with the `NI-TClk API <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/user-manual-welcome.html>`_.\n\n----\n**Note**\n The PXIe-5644/5645/5646 does not support the NI-TClk API.\n\n----\n\n----\n**Note**\n This function is not supported if you set the **acquisitionType** parameter to NIRFSA_VAL_SPECTRUM using the nirfsa_ConfigureAcquisitionType function or if you set the NIRFSA_ATTR_ACQUISITION_TYPE attribute to NIRFSA_VAL_SPECTRUM.\n\n----\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the source of the digital edge for the Reference trigger.\n\n|Value                                            |Description                                                                                                                                                                                                                               |\n|:-------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|\n| NIRFSA_VAL_PFI0 (\'PFI0\')               | The trigger is received on PFI 0. For the PXIe-5841 with PXIe-5655, the trigger is received on the PXIe-5841 PFI 0.                                                                                                           |\n| NIRFSA_VAL_PFI1 (\'PFI1\')               | The trigger is received on PFI 1.                                                                                                                                                                                             |\n| NIRFSA_VAL_PXI_TRIG0 (\'PXI_Trig0\')     | The trigger is received on PXI trigger line 0.                                                                                                                                                                                |\n| NIRFSA_VAL_PXI_TRIG1 (\'PXI_Trig1\')     | The trigger is received on PXI trigger line 1.                                                                                                                                                                                |\n| NIRFSA_VAL_PXI_TRIG2 (\'PXI_Trig2\')     | The trigger is received on PXI trigger line 2.                                                                                                                                                                                |\n| NIRFSA_VAL_PXI_TRIG3 (\'PXI_Trig3\')     | The trigger is received on PXI trigger line 3.                                                                                                                                                                                |\n| NIRFSA_VAL_PXI_TRIG4 (\'PXI_Trig4\')     | The trigger is received on PXI trigger line 4.                                                                                                                                                                                |\n| NIRFSA_VAL_PXI_TRIG5 (\'PXI_Trig5\')     | The trigger is received on PXI trigger line 5.                                                                                                                                                                                |\n| NIRFSA_VAL_PXI_TRIG6 (\'PXI_Trig6\')     | The trigger is received on PXI trigger line 6.                                                                                                                                                                                |\n| NIRFSA_VAL_PXI_TRIG7 (\'PXI_Trig7\')     | The trigger is received on PXI trigger line 7.                                                                                                                                                                                |\n| NIRFSA_VAL_PXI_STAR (\'PXI_STAR\')       | The trigger is received on the PXI star trigger line. This value is not supported for PXIe-5644/5645/5646 devices.                                                                                                            |\n| NIRFSA_VAL_PXIE_DSTARB (\'PXIE_DSTARB\') | The trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860.                                                                        |\n| NIRFSA_VAL_TIMER_EVENT (\'TimerEvent\')  | The trigger is received from Timer Event on the digitizer. This value is valid on only the PXIe-5820/5840/5841/5842/5860 and for digital edge Advance Triggers on the PXIe-5644/5645/5646 and PXIe-5663E/5665. |\n| NIRFSA_VAL_DIO_PFI0 (\'PFI0\')               | The trigger is received on PFI 0 of the DIO Terminal.                                                                                                                                                          |\n| NIRFSA_VAL_DIO_PFI1(\'PFI1\')               | The trigger is received on PFI 1 of the DIO Terminal.                                                                                                                                                          |\n| NIRFSA_VAL_DIO_PFI2 (\'PFI2\')               | The trigger is received on PFI 2 of the DIO Terminal.                                                                                                                                                          |\n| NIRFSA_VAL_DIO_PFI3 (\'PFI3\')               | The trigger is received on PFI 3 of the DIO Terminal.                                                                                                                                                          |\n| NIRFSA_VAL_DIO_PFI4 (\'PFI4\')               | The trigger is received on PFI 4 of the DIO Terminal.                                                                                                                                                          |\n| NIRFSA_VAL_DIO_PFI5 (\'PFI5\')               | The trigger is received on PFI 5 of the DIO Terminal.                                                                                                                                                          |\n| NIRFSA_VAL_DIO_PFI6 (\'PFI6\')               | The trigger is received on PFI 6 of the DIO Terminal.                                                                                                                                                          |\n| NIRFSA_VAL_DIO_PFI7 (\'PFI7\')               | The trigger is received on PFI 7 of the DIO Terminal.                                                                                                                                                          |',
                },
                'grpc_name': 'source_raw',
                'name': 'source',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the trigger edge to detect. The default value is NIRFSA_VAL_RISING_EDGE.\n\n|Value                               |Description                                 |\n|:------------------------------|:--------------------------------|\n| NIRFSA_VAL_RISING_EDGE (900)  | NI-RFSA detects a rising edge.  |\n| NIRFSA_VAL_FALLING_EDGE (901) | NI-RFSA detects a falling edge. |',
                },
                'enum': 'ReferenceTriggerDigitalEdgeEdge',
                'name': 'edge',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'default_value': '0',
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of samples to store for each record that was acquired in the time period immediately before the trigger occurred.',
                },
                'name': 'pretriggerSamples',
                'type': 'ViInt64',
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
            'description': 'Configures the device to wait for a digital edge Start Trigger at the beginning of the acquisition.\n\nYou can use this trigger with the `NI-TClk API <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/user-manual-welcome.html>`_.\n\n----\n**Note**\n The PXIe-5644/5645/5646 does not support the NI-TClk API.\n\n----\n\n----\n**Note**\n This function is not supported if you set the **acquisitionType** parameter to NIRFSA_VAL_SPECTRUM using the nirfsa_ConfigureAcquisitionType function or if you set the NIRFSA_ATTR_ACQUISITION_TYPE attribute to NIRFSA_VAL_SPECTRUM.\n\n----\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the source of the digital edge for the Start Trigger.\n\n| Value                                           | Description                                                                                                                                                                                                               |\n|:-------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|\n| NIRFSA_VAL_PFI0 (\'PFI0\')               | The trigger is received on PFI 0. For the PXIe-5841 with PXIe-5655, the trigger is received on the PXIe-5841 PFI 0.                                                                                            |\n| NIRFSA_VAL_PFI1 (\'PFI1\')               | The trigger is received on PFI 1.                                                                                                                                                                              |\n| NIRFSA_VAL_PXI_TRIG0 (\'PXI_Trig0\')     | The trigger is received on PXI trigger line 0.                                                                                                                                                                 |\n| NIRFSA_VAL_PXI_TRIG1 (\'PXI_Trig1\')     | The trigger is received on PXI trigger line 1.                                                                                                                                                                 |\n| NIRFSA_VAL_PXI_TRIG2 (\'PXI_Trig2\')     | The trigger is received on PXI trigger line 2.                                                                                                                                                                 |\n| NIRFSA_VAL_PXI_TRIG3 (\'PXI_Trig3\')     | The trigger is received on PXI trigger line 3.                                                                                                                                                                 |\n| NIRFSA_VAL_PXI_TRIG4 (\'PXI_Trig4\')     | The trigger is received on PXI trigger line 4.                                                                                                                                                                 |\n| NIRFSA_VAL_PXI_TRIG5 (\'PXI_Trig5\')     | The trigger is received on PXI trigger line 5.                                                                                                                                                                 |\n| NIRFSA_VAL_PXI_TRIG6 (\'PXI_Trig6\')     | The trigger is received on PXI trigger line 6.                                                                                                                                                                 |\n| NIRFSA_VAL_PXI_TRIG7 (\'PXI_Trig7\')     | The trigger is received on PXI trigger line 7.                                                                                                                                                                 |\n| NIRFSA_VAL_PXI_STAR (\'PXI_STAR\')       | The trigger is received on the PXI star trigger line. This value is not supported for PXIe-5644/5645/5646 devices.                                                                                             |\n| NIRFSA_VAL_PXIE_DSTARB (\'PXIE_DSTARB\') | The trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860.                                                                        |\n| NIRFSA_VAL_TIMER_EVENT (\'TimerEvent\')  | The trigger is received from Timer Event on the digitizer. This value is valid on only the PXIe-5820/5840/5841/5842/5860 and for digital edge Advance Triggers on the PXIe-5644/5645/5646 and PXIe-5663E/5665. |\n| NIRFSA_VAL_DIO_PFI0 (\'PFI1\')               | The trigger is received on PFI 0 of the DIO Terminal.                                                                                                                                                          |\n| NIRFSA_VAL_DIO_PFI1(\'PFI2\')               | The trigger is received on PFI 1 of the DIO Terminal.                                                                                                                                                          |\n| NIRFSA_VAL_DIO_PFI2 (\'PFI3\')               | The trigger is received on PFI 2 of the DIO Terminal.                                                                                                                                                          |\n| NIRFSA_VAL_DIO_PFI3 (\'PFI4\')               | The trigger is received on PFI 3 of the DIO Terminal.                                                                                                                                                          |\n| NIRFSA_VAL_DIO_PFI4 (\'PFI5\')               | The trigger is received on PFI 4 of the DIO Terminal.                                                                                                                                                          |\n| NIRFSA_VAL_DIO_PFI5 (\'PFI6\')               | The trigger is received on PFI 5 of the DIO Terminal.                                                                                                                                                          |\n| NIRFSA_VAL_DIO_PFI6 (\'PFI7\')               | The trigger is received on PFI 6 of the DIO Terminal.                                                                                                                                                          |\n| NIRFSA_VAL_DIO_PFI7 (\'PFI8\')               | The trigger is received on PFI 7 of the DIO Terminal.                                                                                                                                                          |',
                },
                'grpc_name': 'source_raw',
                'name': 'source',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the trigger edge to detect. The default value is NIRFSA_VAL_RISING_EDGE.\n\n| Value                              | Description                                |\n|:------------------------------|:--------------------------------|\n| NIRFSA_VAL_RISING_EDGE (900)  | NI-RFSA detects a rising edge.  |\n| NIRFSA_VAL_FALLING_EDGE (901) | NI-RFSA detects a falling edge. |',
                },
                'enum': 'StartTriggerDigitalEdgeEdge',
                'name': 'edge',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ConfigureIQPowerEdgeRefTrigger': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Configures the device to wait for the complex power of the I/Q data to cross the specified threshold to mark a reference point within the record.\n\nTo trigger on burst signals, add a minimum quiet time, configured with the NIRFSA_ATTR_REF_TRIGGER_MINIMUM_QUIET_TIME attribute, to ensure the trigger does not occur in the middle of a burst if the acquisition starts while a burst is being generated. The quiet time should be set to a value smaller than the time between bursts, but large enough to ignore power changes within a burst.\n\nYou can use this trigger with the `NI-TClk API <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/user-manual-welcome.html>`_.\n\n----\n**Note**\n This function is not supported if you set the **acquisitionType** parameter to NIRFSA_VAL_SPECTRUM using the nirfsa_ConfigureAcquisitionType function or if you set the NIRFSA_ATTR_ACQUISITION_TYPE attribute to NIRFSA_VAL_SPECTRUM.\n\n----\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_',
        },
        'grpc_name': 'ConfigureIQPowerEdgeRefTrigger',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the source of the RF signal for the power edge Reference trigger. The only supported value is "0".',
                },
                'name': 'source',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the threshold, in dBm, above or below which the device triggers.',
                },
                'name': 'level',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies whether the device detects a positive or negative slope on the trigger signal. The default value is NIRFSA_VAL_RISING_SLOPE.\n\n| Value                                | Description                                                |\n|:--------------------------------|:-------------------------------------------------|\n| NIRFSA_VAL_RISING_SLOPE (1000)  | NI-RFSA detects a rising edge (positive slope).  |\n| NIRFSA_VAL_FALLING_SLOPE (1001) | NI-RFSA detects a falling edge (negative slope). |',
                },
                'enum' : 'ReferenceTriggerIqPowerEdgeSlope',
                'name': 'slope',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'default_value': '0',
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of samples to store for each record that was acquired in the time period immediately before the trigger occurred.',
                },
                'name': 'pretriggerSamples',
                'type': 'ViInt64',
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
            'description': 'Configures the NI-RFSA device Reference Clock.\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5694, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`PXI-5661 Reference Clock <https://www.ni.com/docs/en-US/bundle/pxi-5661-feature/page/reference-clock.html>`_\n\n`PXIe-5663 Timing Configurations <https://www.ni.com/docs/en-US/bundle/pxie-5663-5663e-feature/page/timing-configurations.html>`_\n\n`PXIe-5665 Timing Configurations <https://www.ni.com/docs/en-US/bundle/pxie-5665-feature/page/timing-configurations.html>`_\n\n`PXIe-5667 Timing Configurations <https://www.ni.com/docs/en-US/bundle/pxie-5667-feature/page/timing-configurations.html>`_\n\n`PXIe-5668 Timing Configurations <https://www.ni.com/docs/en-US/bundle/pxie-5668-feature/page/timing-configurations.html>`_\n\n`PXIe-5830 Timing Configurations <https://www.ni.com/docs/en-US/bundle/pxie-5830-feature/page/timing-configurations.html>`_\n\n`PXIe-5831 Timing Configurations <https://www.ni.com/docs/en-US/bundle/pxie-5831/page/timing-configurations.html>`_',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'specifies the source of the Reference Clock signal.\n| Clock Source          | Description |\n|-----------------------|-------------|\n| **Onboard Clock (default)** | Uses the onboard Reference Clock as the clock source. <br/>**PXIe-5830/5831/5832**-<br>- PXIe-5830: Connect PXIe-5820 REF IN to PXIe-3621 REF OUT. <br>- PXIe-5831: Connect PXIe-5820 REF IN to PXIe-3622 REF OUT. <br>- PXIe-5832: Connect PXIe-5820 REF IN to PXIe-3623 REF OUT. <br/>**PXIe-5831 with PXIe-5653**-<br>- Connect PXIe-5820 REF IN to PXIe-3622 REF OUT. <br>- Connect PXIe-5653 REF OUT (10 MHz) to PXIe-3622 REF IN. <br/>**PXIe-5832 with PXIe-5653**-<br>- Connect PXIe-5820 REF IN to PXIe-3623 REF OUT. <br>- Connect PXIe-5653 REF OUT (10 MHz) to PXIe-3623 REF IN. <br/>**PXIe-5841 with PXIe-5655**-<br>- Lock to PXIe-5655 onboard clock. Connect REF OUT on PXIe-5655 to PXIe-5841 REF IN. <br/>**PXIe-5842**-<br>- Lock to PXIe-5655 onboard clock. Use cables as shown in the Getting Started Guide. |\n| **RefIn** | Uses the signal at the front panel REF IN connector. <br/>**PXIe-5830/5831/5832**-<br>- PXIe-5830: Connect PXIe-5820 REF IN to PXIe-3621 REF OUT; lock external signal to PXIe-3621 REF IN. <br>- PXIe-5831: Connect PXIe-5820 REF IN to PXIe-3622 REF OUT; lock external signal to PXIe-3622 REF IN. <br>- PXIe-5832: Connect PXIe-5820 REF IN to PXIe-3623 REF OUT; lock external signal to PXIe-3623 REF IN. <br/>**PXIe-5831 with PXIe-5653**-<br>- Connect PXIe-5820 REF IN to PXIe-3622 REF OUT. <br>- Connect PXIe-5653 REF OUT (10 MHz) to PXIe-3622 REF IN. <br>- Lock external signal to PXIe-5653 REF IN. <br/>**PXIe-5832 with PXIe-5653**-<br>- Connect PXIe-5820 REF IN to PXIe-3623 REF OUT. <br>- Connect PXIe-5653 REF OUT (10 MHz) to PXIe-3623 REF IN. <br>- Lock external signal to PXIe-5653 REF IN. <br/>**PXIe-5841 with PXIe-5655**-<br>- Lock to signal at REF IN on PXIe-5655. Connect REF OUT on PXIe-5655 to PXIe-5841 REF IN. <br/>**PXIe-5842**-<br>- Lock to signal at REF IN on PXIe-5655. Use cables as shown in the Getting Started Guide. |\n| **PXI Clock** | Uses the PXI_CLK signal present on the PXI backplane. |\n| **PXI_ClkMaster** | Valid only for PXIe-5831 with PXIe-5653 and PXIe-5832 with PXIe-5653. <br/>**PXIe-5831 with PXIe-5653**-<br>- NI-RFSG configures PXIe-5653 to export Reference Clock. <br>- Configures PXIe-5820 and PXIe-3622 to use PXI_Clk. <br>- Connect PXIe-5653 REF OUT (10 MHz) to PXI chassis REF IN. <br/>**PXIe-5832 with PXIe-5653**-<br>- NI-RFSG configures PXIe-5653 to export Reference Clock. <br>- Configures PXIe-5820 and PXIe-3623 to use PXI_Clk. <br>- Connect PXIe-5653 REF OUT (10 MHz) to PXI chassis REF IN. |',
                },
                'name': 'clockSource',
                'enum': 'ReferenceClockSource',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'specifies the Reference Clock rate, in hertz (Hz), of the signal present at the REF IN or CLK IN connector. This parameter is only valid when the **ref clock source** parameter is set to **RefIn**. The default value is Auto (-1.0), which allows NI-RFSG to use the default Reference Clock rate for the device or automatically detect the Reference Clock rate, if supported. Refer to the Reference Clock Rate property for possible values.',
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
    'ConfigureSoftwareEdgeAdvanceTrigger': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Configures the device to wait for a software Advance Trigger.\n\nThe Advance Trigger indicates where a new record begins. The device waits until you call the nirfsa_SendSoftwareEdgeTrigger function to assert the trigger.\n\n----\n**Note**\n This function is not supported if you set the **acquisitionType** parameter to NIRFSA_VAL_SPECTRUM using the nirfsa_ConfigureAcquisitionType function or if you set the NIRFSA_ATTR_ACQUISITION_TYPE attribute to NIRFSA_VAL_SPECTRUM.\n\n----\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
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
    'ConfigureSoftwareEdgeRefTrigger': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Configures the device to wait for a software Reference Trigger to mark a reference point within the record.\n\nThe device waits until you call the nirfsa_SendSoftwareEdgeTrigger function to assert the trigger.\n\nYou can use this trigger with the `NI-TClk API <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/user-manual-welcome.html>`_.\n\n----\n**Note**\n The PXIe-5644/5645/5646 does not support the NI-TClk API.\n\n----\n\n----\n**Note**\n This function is not supported if you set the **acquisitionType** parameter to NIRFSA_VAL_SPECTRUM using the nirfsa_ConfigureAcquisitionType function or if you set the NIRFSA_ATTR_ACQUISITION_TYPE attribute to NIRFSA_VAL_SPECTRUM.\n\n----\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of samples to store for each record that was acquired in the time period immediately before the trigger occurred.',
                },
                'name': 'pretriggerSamples',
                'default_value': '0',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ConfigureSoftwareEdgeStartTrigger': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Configures the device to wait for a software Start Trigger at the beginning of the acquisition.\n\nThe device waits until you call the nirfsa_SendSoftwareEdgeTrigger function to assert the trigger.\n\nYou can use this trigger with the `NI-TClk API <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/user-manual-welcome.html>`_.\n\n----\n**Note**\n The PXIe-5644/5645/5646 does not support the NI-TClk API.\n\n----\n\n----\n**Note**\n This function is not supported if you set the **acquisitionType** parameter to NIRFSA_VAL_SPECTRUM using the nirfsa_ConfigureAcquisitionType function or if you set the NIRFSA_ATTR_ACQUISITION_TYPE attribute to NIRFSA_VAL_SPECTRUM.\n\n----\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
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
    'ConfigureSpectrumFrequencyCenterSpan': {
        'codegen_method': 'private',
        'method_name_for_documentation': 'configure_spectrum_frequency',
        'documentation': {
            'description': 'Configures the span and center frequency of the spectrum read by NI-RFSA.\n\nA spectrum acquisition consists of data surrounding the center frequency.\n\n----\n**Note**\nIf you configure the spectrum span to a value larger than the instantaneous bandwidth of the device, NI-RFSA performs multiple acquisitions and combines them into a spectrum of the size you requested.\n\n----\n\n----\n**Note**\n For the PXIe-5663/5663E, NI-RFSA does not support multispan acquisitions from frequency ranges that correspond with different instantaneous bandwidths. For example, you cannot configure a multispan acquisition that acquires one span from 110 MHz to 120 MHz and a second from 120 MHz to 130 MHz because the bandwidths that correspond to each span are different (10 MHz and 20 MHz, respectively).\n\n----\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies which channels to apply settings. Specify an empty string as the value of this parameter.',
                },
                'is_repeated_capability': True,
                'repeated_capability_type': 'channels',
                'name': 'channelList',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the center frequency in a spectrum acquisition. The value is expressed in hertz (Hz). The NI-RFSA device you use determines the valid range. Refer to your device specifications document for more information about frequency range.',
                },
                'name': 'centerFrequency',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the span of a spectrum acquisition. The value is expressed in hertz (Hz).\n\n----\n\n*Note* For the PXIe-5663/5663E/5665/5667/5668, NI-RFSA enables dithering by default. The dither noise can appear in your passband and affect your measurements. Refer to the NIRFSA_ATTR_DIGITIZER_DITHER_ENABLED attribute for more information about dithering.\n\n----',
                },
                'name': 'span',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ConfigureSpectrumFrequencyStartStop': {
        'codegen_method': 'private',
        'method_name_for_documentation': 'configure_spectrum_frequency',
        'documentation': {
            'description': 'Configures the start and stop frequencies of a spectrum read by NI-RFSA.\n\n----\n**Note**\nIf you configure the spectrum span (**NIRFSA_ATTR_STOP_FREQUENCY**  **NIRFSA_ATTR_START_FREQUENCY**) to a value larger than the instantaneous bandwidth of the device, NI-RFSA performs multiple acquisitions and combines them into a spectrum of the size you request.\n\n----\n\n----\n**Note**\n For the PXIe-5663/5663E, NI-RFSA does not support multispan acquisitions from frequency ranges that correspond with different instantaneous bandwidths. For example, you cannot configure a multispan acquisition that acquires one span from 110 MHz to 120 MHz and a second from 120 MHz to 130 MHz because the bandwidths that correspond to each span are different (10 MHz and 20 MHz, respectively).\n\n----\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies which channels to apply settings. Specify an empty string as the value of this parameter.',
                },
                'is_repeated_capability': True,
                'repeated_capability_type': 'channels',
                'name': 'channelList',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the lower limit of a span of frequencies. This value is expressed in hertz (Hz).',
                },
                'name': 'startFrequency',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the upper limit of a span of frequencies. This value is expressed in hertz (Hz).',
                },
                'name': 'stopFrequency',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ConfigureSpectrumFrequencyDispatcher': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': 'Configures the frequency range of a spectrum acquisition.\n\nYou can specify the frequency range using either center frequency and span, or start and stop frequencies.\n\n----\n**Note**\nIf you configure the spectrum span to a value larger than the instantaneous bandwidth of the device, NI-RFSA performs multiple acquisitions and combines them into a spectrum of the size you requested.\n\n----\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860',
        },
        'included_in_proto': False,
        'is_error_handling': False,
        'method_name_for_documentation': 'configure_spectrum_frequency',
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '',
                'session_filename': 'configure_spectrum_frequency'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies which channels to apply settings. Specify an empty string as the value of this parameter.',
                },
                'is_repeated_capability': True,
                'repeated_capability_type': 'channels',
                'name': 'channelList',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'default_value': 'None',
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the center frequency in a spectrum acquisition. The value is expressed in hertz (Hz). Must be used together with **span**.',
                },
                'name': 'centerFrequency',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'default_value': 'None',
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the span of a spectrum acquisition. The value is expressed in hertz (Hz). Must be used together with **center_frequency**.',
                },
                'name': 'span',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'default_value': 'None',
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the lower limit of a span of frequencies. The value is expressed in hertz (Hz). Must be used together with **stop_frequency**.',
                },
                'name': 'startFrequency',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'default_value': 'None',
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the upper limit of a span of frequencies. The value is expressed in hertz (Hz). Must be used together with **start_frequency**.',
                },
                'name': 'stopFrequency',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'python_name': 'configure_spectrum_frequency',
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'CreateDeembeddingSparameterTableS2PFile': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nCreates an S-parameter de-embedding table for the port based on the specified S2P file.\n\nIf you only create one table for a port, NI-RFSA automatically selects that table to de-embed the measurement.\n\n**Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`De-embedding Overview <https://www.ni.com/docs/en-US/bundle/pxie-5840/page/de-embedding-overview.html>`_\n\n`S-parameters <https://www.ni.com/docs/en-US/bundle/pxie-5840/page/de-embedding-overview.html#GUID-0AD828DE-398A-45C6-ABBA-4208DEB7DE1B__GUID-67A69775-E4DB-4FA2-84FE-C05977ED4184>`_',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).',
                },
                'name': 'port',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the table. The name must be unique for a given port, but not across ports. If you use the same name as an existing table, the table is replaced.',
                },
                'name': 'tableName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the path to the S2P file that contains de-embedding information for the specified port.',
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
                            'NIRFSA_VAL_PORT1_TOWARDS_DUT',
                            'Port 1 of the S2P is oriented towards the DUT port.'
                        ],
                        [
                            'NIRFSA_VAL_PORT2_TOWARDS_DUT',
                            'Port 2 of the S2P is oriented towards the DUT port.'
                        ]
                    ],
                    'table_header': [
                        'Name',
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
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'DeleteAllDeembeddingTables': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nDeletes all configured de-embedding tables for the session.\n\n**Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
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
            'description': '\nDeletes the selected de-embedding table for a given port.\n\n**Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).',
                },
                'name': 'port',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the table.',
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
    'DisableAdvanceTrigger': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Configures the device to not use an Advance Trigger.\n\nThis function is necessary only if you configured an Advance Trigger in the past and now want to disable it.\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
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
    'DisableRefTrigger': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Configures the device to not wait for a Reference Trigger to mark a reference point within a record.\n\nThis function is necessary only if you previously configured a Reference trigger in the past and now want to disable it.\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5668, PXIe-5820/5840/5841/5842/5860\n\n**Related Topics**\n\n`Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
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
    'DisableStartTrigger': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Configures the device to not wait for a Start Trigger at the beginning of the acquisition.\n\nThis function is necessary only if you previously configured a Start Trigger in the past and now want to disable it.\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
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
    'EnableSessionAccess': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Enables or disables SFP session access for the specified instrument.\n\nSFP session access allows the NI-RFSA Soft Front Panel (SFP) to access a device with an existing open session and can help you debug your code. To enable session access, pass VI_TRUE to the **enabled** parameter. To disable session access, pass VI_FALSE to the **enabled** parameter.\n\nRefer to `Configuring SFP Session Access using LabWindows/CVI or C <https://www.ni.com/docs/en-US/bundle/ni-rfsa-sfp/page/rfsasfp/configuring_session_access_labwindows.html>`_ for more information about SFP session access.\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694, PXIe-5830/5831/5832/5840/5841/5842/5860\n\n----\n**Note**\nNI-RFSA does not support NI-TClk when driver session debugging is enabled.\n\n----',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Enables or disables SFP session access for the specified device.\n\n| Value         | Description                         |\n|:---------|:-------------------------|\n| VI_TRUE  | Enables session access.  |\n| VI_FALSE | Disables session access. |',
                },
                'name': 'enable',
                'type': 'ViBoolean',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ErrorMessage': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Converts an error code returned by an NI-RFSA function into a user-readable string.\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5840',
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
                    'description': 'The ViSession handle that you obtain from nirfsa_Init or nirfsa_InitWithOptions. The handle identifies a particular instrument session.\n\nYou can pass VI_NULL for this parameter. Passing VI_NULL is useful when nirfsa_Init or nirfsa_InitWithOptions fails.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Passes the **errorCode** parameter that is returned from any NI-RFSA function.',
                },
                'grpc_name': 'status_code',
                'name': 'errorCode',
                'type': 'ViStatus',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the user-readable message string that corresponds to the error code you specify.\n\nYou must pass a ViChar array with 1024 bytes or more to this parameter. Only the first 1024 bytes of the array are used.',
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
    'CreateDeembeddingSparameterTableArray': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nCreates an s-parameter de-embedding table for the port from the input data.\n\nIf you only create one table for a port, NI-RFSA automatically selects that table to de-embed the measurement.\n\n**Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`De-embedding Overview <https://www.ni.com/docs/en-US/bundle/pxie-5840/page/de-embedding-overview.html>`_',
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsa_Init function or the nirfsa_InitWithOptions function and identifies a particular instrument session.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).',
                },
                'name': 'port',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the table. The name must be unique for a given port, but not across ports. If you use the same name as an existing table, the table is replaced.',
                },
                'name': 'tableName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the frequencies for the NIRFSA_ATTR_SPARAMETER_TABLE rows. Frequencies must be unique and in ascending order.',
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
                    'description': 'Specifies the size of the frequency array.',
                },
                'name': 'frequenciesSize',
                'type': 'ViInt32',
                'use_array': False
            },
            {
                'array_dimensions': 3,
                'complex_array_representation': 'complex_number_array',
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the S-parameters for each frequency. S-parameters for each frequency are placed in the array in the following order: s11, s12, s21, s22.',
                },
                'name': 'sparameterTable',
                'numpy': True,
                'size': {
                    'mechanism': 'len',
                    'value': 'sparameterTableSize'
                },
                'type': 'NIComplexNumber[]',
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the size of the S-parameter table array.',
                },
                'name': 'sparameterTableSize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': False
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of DUT ports.',
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
                            'NIRFSA_VAL_PORT1_TOWARDS_DUT',
                            'Port 1 of the S2P is oriented towards the DUT port.'
                        ],
                        [
                            'NIRFSA_VAL_PORT2_TOWARDS_DUT',
                            'Port 2 of the S2P is oriented towards the DUT port.'
                        ]
                    ],
                    'table_header': [
                        'Name',
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
    'FancyCreateDeembeddingSparameterTableArray': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': '\nCreates an s-parameter de-embedding table for the port from the input data.\n\nIf you only create one table for a port, NI-RFSA automatically selects that table to de-embed the measurement.\n\n**Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`De-embedding Overview<https://www.ni.com/docs/en-US/bundle/pxie-5840/page/de-embedding-overview.html>`_',
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsa_Init function or the nirfsa_InitWithOptions function and identifies a particular instrument session.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).',
                },
                'name': 'port',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the table. The name must be unique for a given port, but not across ports. If you use the same name as an existing table, the table is replaced.',
                },
                'name': 'tableName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the frequencies for the NIRFSA_ATTR_SPARAMETER_TABLE rows. Frequencies must be unique and in ascending order.',
                },
                'name': 'frequencies',
                'numpy': True,
                'type': 'ViReal64[]',
                'type_in_documentation': 'numpy.array(dtype=numpy.float64)',
                'use_in_python_api': True
            },
            {
                'array_dimensions': 3,
                'complex_array_representation': 'complex_number_array',
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the S-parameters for each frequency. S-parameters for each frequency are placed in the array in the following order: s11, s12, s21, s22.',
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
                            'NIRFSA_VAL_PORT1_TOWARDS_DUT',
                            'Port 1 of the S2P is oriented towards the DUT port.'
                        ],
                        [
                            'NIRFSA_VAL_PORT2_TOWARDS_DUT',
                            'Port 2 of the S2P is oriented towards the DUT port.'
                        ]
                    ],
                    'table_header': [
                        'Name',
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
    'GetDeembeddingSparameters': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nReturns the S-parameters used for de-embedding a measurement on the selected port.\n\nThis includes interpolation of the parameters based on the configured carrier frequency. This function returns an empty array if no de-embedding is done.\n\nIf you want to call this function just to get the required buffer size, you can pass 0 for **S-parameter Size** and VI_NULL for the **S-parameters** buffer.\n\n**Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860',
            'note': 'The port orientation for the returned S-parameters is normalized to NIRFSA_VAL_PORT1_TOWARDS_DUT.'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'numpy_method',
                'library_interpreter_filename': 'get_deembedding_sparameter',
                'method_python_name_suffix': '',
                'session_filename': 'none'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsa_Init function or the nirfsa_InitWithOptions function and identifies a particular instrument session.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'array_dimensions': 2,
                'complex_array_representation': 'complex_number_array',
                'direction': 'out',
                'documentation': {
                    'description': 'Returns an array of S-parameters. The S-parameters are returned in the following order: s11, s12, s21, s22.',
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
                    'description': 'Specifies the size of the array that is returned by the NIRFSA_ATTR_SPARAMETERS output.',
                },
                'name': 'sparametersArraySize',
                'type': 'ViInt32',
                'use_array': False
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the number of S-parameters.',
                },
                'name': 'numberOfSparameters',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the number of S-parameter ports. The **sparameter** array is always *n* x *n*, where span *n* is the number of ports.',
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
            'description': '\nReturns the number of S-parameter ports.',
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsa_Init function or the nirfsa_InitWithOptions function and identifies a particular instrument session.',
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the number of S-parameter ports. The **sparameter** array is always *n* x *n*, where span *n* is the number of ports.',
                },
                'name': 'numberOfPorts',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'FancyGetDeembeddingSparameters': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': '\nReturns the S-parameters used for de-embedding a measurement on the selected port.\n\nThis includes interpolation of the parameters based on the configured carrier frequency. This function returns an empty array if no de-embedding is done.\n\nIf you want to call this function just to get the required buffer size, you can pass 0 for **S-parameter Size** and VI_NULL for the **S-parameters** buffer.\n\n**Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860',
            'note': 'The port orientation for the returned S-parameters is normalized to NIRFSA_VAL_PORT1_TOWARDS_DUT.'
        },
        'included_in_proto': True,
        'method_name_for_documentation': 'get_deembedding_sparameters',
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsa_Init function or the nirfsa_InitWithOptions function and identifies a particular instrument session.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'array_dimensions': 2,
                'complex_array_representation': 'complex_number_array',
                'direction': 'out',
                'documentation': {
                    'description': 'Returns an array of S-parameters. The S-parameters are returned in the following order: s11, s12, s21, s22.',
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
    'ReadIqSingleRecordDispatcher': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': 'Initiates an acquisition and fetches a single I/Q data record.\n\nDo not use this function if you have configured the device to continuously acquire data samples or to acquire multiple records.\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`None (Trigger Type) <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/no-trigger.html>`_',
        },
        'included_in_proto': False,
        'is_error_handling': False,
        'method_name_for_documentation': 'read_iq_single_record',
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '_into',
                'session_filename': 'read_iq_single_record'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies which channels to apply settings. Specify an empty string as the value of this parameter.',
                },
                'is_repeated_capability': True,
                'repeated_capability_type': 'channels',
                'name': 'channelList',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies in seconds the time allotted for the function to complete before returning a timeout error. A value of  specifies the function waits until all data is available.',
                },
                'default_value': 'hightime.timedelta(seconds=10.0)',
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds',
                'use_array': False,
                'use_in_python_api': True,
            },
            {
                'complex_array_representation': 'complex_number_array',
                'direction': 'in',
                'documentation': {
                    'description': 'Returns the acquired waveform. Allocate an NIComplexNumber array at least as large as the number of samples configured in the nirfsa_ConfigureNumberOfSamples function.',
                },
                'name': 'iq_data_array',
                'numpy': True,
                'size': {'mechanism': 'fixed', 'value': 1},
                'type': 'NIComplexNumber[]',
                'type_in_documentation': 'numpy array of numpy.complex64, numpy array of numpy.complex128 or interleaved complex data in the form of numpy array of numpy.int16',
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the size of the array for the NIRFSA_ATTR_DATA parameter. The array needs to be at least as large as the number of samples configured in the nirfsa_ConfigureNumberOfSamples function.',
                },
                'name': 'dataArraySize',
                'size': {'mechanism': 'python-code', 'value': '0 if iq_data_array is None else len(iq_data_array)'},
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': False
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Contains the absolute and relative timestamps for the operation, the time interval (dt), and the actual number of samples read.\n\nThe following list provides more information about each of these properties:\n\n- **absolute timestamp** Returns the timestamp, in seconds, of the first fetched sample that is comparable between records and acquisitions.\n\n----\n\nThe value of the absolute timestamp returned is always 0 for the PXIe-5644/5645/5646, PXIe-5668, and PXIe-5820/5830/5831/5832/5840/5841/5842/5860.\n\n----\n\n- **relative timestamp** Returns a timestamp that corresponds to the difference, in seconds, between the first sample returned and the Reference Trigger location. The timestamp is zero if the Reference Trigger has not occurred.\n\n----\n\n\nThe value of the relative timestamp returned is always 0 for the PXIe-5644/5645/5646.\n\n----\n\n- **dt** Returns the time interval between data points in the acquired signal. The I/Q data sample rate is the reciprocal of this value.\n- **actual samples read** Returns an integer representing the number of samples in the waveform.\n- **offset** Returns the offset to scale data, (*b*), in *mx* + *b* form.\n- **gain** Returns the gain to scale data, (*m*), in *mx* + *b* form.',
                },
                'name': 'wfmInfo',
                'type': 'niRFSA_wfmInfo',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'python_name': 'read_iq_single_record',
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'ReadIQSingleRecordComplexF64': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Initiates an acquisition and fetches a single I/Q data record.\n\nDo not use this function if you have configured the device to continuously acquire data samples or to acquire multiple records.\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`None (Trigger Type) <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/no-trigger.html>`_',
        },
        'grpc_name': 'ReadIQSingleRecordComplexF64',
        'included_in_proto': True,
        'is_error_handling': False,
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies which channels to apply settings. Specify an empty string as the value of this parameter.',
                },
                'name': 'channelList',
                'is_repeated_capability': True,
                'repeated_capability_type': 'channels',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies in seconds the time allotted for the function to complete before returning a timeout error. A value of  specifies the function waits until all data is available.',
                },
                'default_value': 'hightime.timedelta(seconds=10.0)',
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds',
                'use_array': False,
                'use_in_python_api': True,
            },
            {
                'complex_array_representation': 'complex_number_array',
                'direction': 'in',
                'documentation': {
                    'description': 'Returns the acquired waveform. Allocate an NIComplexNumber array at least as large as the number of samples configured in the nirfsa_ConfigureNumberOfSamples function.',
                },
                'name': 'iq_data_array',
                'numpy': True,
                'size': {'mechanism': 'fixed', 'value': 1},
                'type': 'NIComplexNumber[]',
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the size of the array for the NIRFSA_ATTR_DATA parameter. The array needs to be at least as large as the number of samples configured in the nirfsa_ConfigureNumberOfSamples function.',
                },
                'name': 'dataArraySize',
                'size': {'mechanism': 'python-code', 'value': '0 if iq_data_array is None else len(iq_data_array)'},
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': False
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Contains the absolute and relative timestamps for the operation, the time interval (dt), and the actual number of samples read.\n\nThe following list provides more information about each of these properties:\n\n- **absolute timestamp** Returns the timestamp, in seconds, of the first fetched sample that is comparable between records and acquisitions.\n\n----\n\nThe value of the absolute timestamp returned is always 0 for the PXIe-5644/5645/5646, PXIe-5668, and PXIe-5820/5830/5831/5832/5840/5841/5842/5860.\n\n----\n\n- **relative timestamp** Returns a timestamp that corresponds to the difference, in seconds, between the first sample returned and the Reference Trigger location. The timestamp is zero if the Reference Trigger has not occurred.\n\n----\n\n\nThe value of the relative timestamp returned is always 0 for the PXIe-5644/5645/5646.\n\n----\n\n- **dt** Returns the time interval between data points in the acquired signal. The I/Q data sample rate is the reciprocal of this value.\n- **actual samples read** Returns an integer representing the number of samples in the waveform.\n- **offset** Returns the offset to scale data, (*b*), in *mx* + *b* form.\n- **gain** Returns the gain to scale data, (*m*), in *mx* + *b* form.',
                },
                'name': 'wfmInfo',
                'type': 'niRFSA_wfmInfo',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'FetchIQMultiRecordComplexF32': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Fetches I/Q data from multiple records in an acquisition.\n\nA fetch transfers acquired waveform data from device memory to computer memory. The data was acquired to onboard memory previously by the hardware after the acquisition was initiated.\n\nThis function is not necessary if you use the read IQ single record complex F64 function because the read IQ single record complex F64 function performs the fetch as part of the function.\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`None (Trigger Type) <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/no-trigger.html>`_',
        },
        'grpc_name': 'FetchIQMultiRecordComplexF32',
        'included_in_proto': True,
        'method_name_for_documentation': 'fetch_iq_multi_record',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies which channels to apply settings. Specify an empty string as the value of this parameter.',
                },
                'is_repeated_capability': True,
                'repeated_capability_type': 'channels',
                'name': 'channelList',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the first record to retrieve. Record numbers are zero-based. The default value is 0.',
                },
                'name': 'startingRecord',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of records to fetch.',
                },
                'name': 'numberOfRecords',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of samples per record.',
                },
                'name': 'numberOfSamples',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '**PXI-5661, PXIe-5663/5665/5667** Specifies the time, in seconds, allotted for the function to complete before returning a timeout error.\n\n**PXIe-5644/5645/5646, PXIe-5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860** Specifies the time, in seconds, allotted to receive the reference trigger.\n\n----\n\nFor all supported devices, a value of  specifies the function waits until all data is available. A value of 0 specifies the function immediately returns available data.\n\n----',
                },
                'default_value': 'hightime.timedelta(seconds=10.0)',
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'complex_array_representation': 'complex_number_array',
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies a pre-allocated 2D numpy array of shape (number_of_records, number_of_samples) to be filled with the acquired I/Q waveforms. Each row corresponds to one record. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.',
                },
                'name': 'iq_data_arrays',
                'numpy': True,
                'size': {'mechanism': 'passed-in', 'value': 'numberOfSamples'},
                'type': 'NIComplexNumberF32[]',
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Contains the absolute and relative timestamps for the operation, the time interval (dt), and the actual number of samples read. Each element of this array corresponds to a record.\n\nThe following list provides more information about each of these properties:\n\n- **absolute timestamp** Returns the timestamp, in seconds, of the first fetched sample that is comparable between records and acquisitions.\n\n----\n\nThe value of the absolute timestamp returned is always 0 for the PXIe-5644/5645/5646, PXIe-5668, and PXIe-5820/5840/5841/5842/5860.\n\n----\n\n- **relative timestamp** Returns a timestamp that corresponds to the difference, in seconds, between the first sample returned and the Reference Trigger location. The timestamp is zero if the Reference Trigger has not occurred.\n\n----\n\nThe value of the relative timestamp returned is always 0 for the PXIe-5644/5645/5646.\n\n----\n\n- **dt** Returns the time interval between data points in the acquired signal. The I/Q data sample rate is the reciprocal of this value.\n- **actual samples read** Returns an integer representing the number of samples in the waveform.The actual number of samples for each record can vary if the NIRFSA ATTR NUMBER OF SAMPLES attribute changes per step during RF list mode.\n- **offset** Returns the offset to scale data, (*b*), in *mx* + *b* form.\n- **gain** Returns the gain to scale data, (*m*), in *mx* + *b* form.',
                },
                'name': 'wfmInfo',
                'type': 'niRFSA_wfmInfo',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'FetchIQMultiRecordComplexF64': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Fetches I/Q data from multiple records in an acquisition.\n\nA fetch transfers acquired waveform data from device memory to computer memory. The data was acquired to onboard memory previously by the hardware after the acquisition was initiated.\n\nThis function is not necessary if you use the read IQ single record complex F64 function because the read IQ single record complex F64 function performs the fetch as part of the function.\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`None (Trigger Type) <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/no-trigger.html>`_',
        },
        'grpc_name': 'FetchIQMultiRecordComplexF64',
        'included_in_proto': True,
        'is_error_handling': False,
        'method_name_for_documentation': 'fetch_iq_multi_record',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies which channels to apply settings. Specify an empty string as the value of this parameter.',
                },
                'is_repeated_capability': True,
                'repeated_capability_type': 'channels',
                'name': 'channelList',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the first record to retrieve. Record numbers are zero-based. The default value is 0.',
                },
                'name': 'startingRecord',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of records to fetch.',
                },
                'name': 'numberOfRecords',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of samples per record.',
                },
                'name': 'numberOfSamples',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '**PXI-5661, PXIe-5663/5665/5667** Specifies the time, in seconds, allotted for the function to complete before returning a timeout error.\n\n**PXIe-5644/5645/5646, PXIe-5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860** Specifies the time, in seconds, allotted to receive the reference trigger.\n\n----\n\nFor all supported devices, a value of  specifies the function waits until all data is available. A value of 0 specifies the function immediately returns available data.\n\n----',
                },
                'default_value': 'hightime.timedelta(seconds=10.0)',
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'complex_array_representation': 'complex_number_array',
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies a pre-allocated 2D numpy array of shape (number_of_records, number_of_samples) to be filled with the acquired I/Q waveforms. Each row corresponds to one record. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.',
                },
                'name': 'iq_data_arrays',
                'numpy': True,
                'size': {'mechanism': 'passed-in', 'value': 'numberOfSamples'},
                'type': 'NIComplexNumber[]',
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Contains the absolute and relative timestamps for the operation, the time interval (dt), and the actual number of samples read. Each element of this array corresponds to a record.\n\nThe following list provides more information about each of these properties:\n\n- **absolute timestamp** Returns the timestamp, in seconds, of the first fetched sample that is comparable between records and acquisitions.\n\n----\n\nThe value of the absolute timestamp returned is always 0 for the PXIe-5644/5645/5646, PXIe-5668, and PXIe-5820/5840/5841/5842/5860.\n\n----\n\n- **relative timestamp** Returns a timestamp that corresponds to the difference, in seconds, between the first sample returned and the Reference Trigger location. The timestamp is zero if the Reference Trigger has not occurred.\n\n----\n\nThe value of the relative timestamp returned is always 0 for the PXIe-5644/5645/5646.\n\n----\n\n- **dt** Returns the time interval between data points in the acquired signal. The I/Q data sample rate is the reciprocal of this value.\n- **actual samples read** Returns an integer representing the number of samples in the waveform.The actual number of samples for each record can vary if the NIRFSA ATTR NUMBER OF SAMPLES attribute changes per step during RF list mode.\n- **offset** Returns the offset to scale data, (*b*), in *mx* + *b* form.\n- **gain** Returns the gain to scale data, (*m*), in *mx* + *b* form.',
                },
                'name': 'wfmInfo',
                'type': 'niRFSA_wfmInfo',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'FetchIQMultiRecordComplexI16': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Fetches binary I/Q data from multiple records in an acquisition.\n\nFetching transfers acquired waveform data from device memory to computer memory. The data was acquired to onboard memory previously by the hardware after the acquisition was initiated.\n\nThis function is not necessary if you use the read IQ single record complex F64 function because the read IQ single record complex F64 function performs the fetch as part of the function.\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`None (Trigger Type) <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/no-trigger.html>`_',
        },
        'grpc_name': 'FetchIQMultiRecordComplexI16',
        'included_in_proto': True,
        'is_error_handling': False,
        'method_name_for_documentation': 'fetch_iq_multi_record',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies which channels to apply settings. Specify an empty string as the value of this parameter.',
                },
                'is_repeated_capability': True,
                'repeated_capability_type': 'channels',
                'name': 'channelList',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the first record to retrieve. Record numbers are zero-based. The default value is 0.',
                },
                'name': 'startingRecord',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of records to fetch.',
                },
                'name': 'numberOfRecords',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of samples per record.',
                },
                'name': 'numberOfSamples',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '**PXI-5661, PXIe-5663/5665/5667** Specifies the time, in seconds, allotted for the function to complete before returning a timeout error.\n\n**PXIe-5644/5645/5646, PXIe-5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860** Specifies the time, in seconds, allotted to receive the reference trigger.\n\n----\n\nFor all supported devices, a value of  specifies the function waits until all data is available. A value of 0 specifies the function immediately returns available data.\n\n----',
                },
                'default_value': 'hightime.timedelta(seconds=10.0)',
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'complex_array_representation': 'interleaved_real_number_array',
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies a pre-allocated 2D numpy array of shape (number_of_records, number_of_samples) to be filled with the acquired I/Q waveforms. Each row corresponds to one record. The real and imaginary parts of this interleaved data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.',
                },
                'name': 'iq_data_arrays',
                'numpy': True,
                'size': {'mechanism': 'passed-in', 'value': 'numberOfSamples'},
                'type': 'NIComplexI16[]',
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Contains the absolute and relative timestamps for the operation, the time interval (dt), and the actual number of samples read. Each element of this array corresponds to a record.\n\nThe following list provides more information about each of these properties:\n\n- **absolute timestamp** Returns the timestamp, in seconds, of the first fetched sample that is comparable between records and acquisitions.\n\n----\n\nThe value of the absolute timestamp returned is always 0 for the PXIe-5644/5645/5646, PXIe-5668, and PXIe-5820/5830/5831/5832/5840/5841/5842/5860.\n\n----\n\n- **relative timestamp** Returns a timestamp that corresponds to the difference, in seconds, between the first sample returned and the Reference Trigger location. The timestamp is zero if the Reference Trigger has not occurred.\n\n----\n\nThe value of the relative timestamp returned is always 0 for the PXIe-5644/5645/5646.\n\n----\n\n- **dt** Returns the time interval between data points in the acquired signal. The I/Q data sample rate is the reciprocal of this value.\n- **actual samples read** Returns an integer representing the number of samples in the waveform.The actual number of samples for each record can vary if the NIRFSA ATTR NUMBER OF SAMPLES attribute changes per step during RF list mode.\n- **offset** Returns the offset to scale data, (*b*), in *mx* + *b* form.\n- **gain** Returns the gain to scale data, (*m*), in *mx* + *b* form.',
                },
                'name': 'wfmInfo',
                'type': 'niRFSA_wfmInfo',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'FetchIqMultiRecordDispatcher': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': 'Fetches I/Q data from multiple records in an acquisition.\n\nA fetch transfers acquired waveform data from device memory to computer memory. The data was acquired to onboard memory previously by the hardware after the acquisition was initiated.\n\nThis function accepts a data_type parameter to specify the desired data format: numpy.complex64, numpy.complex128, or numpy.int16.\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`None (Trigger Type) <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/no-trigger.html>`_',
        },
        'included_in_proto': False,
        'is_error_handling': False,
        'method_name_for_documentation': 'fetch_iq_multi_record',
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '_into',
                'session_filename': 'fetch_iq_multi_record'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies which channels to apply settings. Specify an empty string as the value of this parameter.',
                },
                'is_repeated_capability': True,
                'repeated_capability_type': 'channels',
                'name': 'channelList',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'default_value': 0,
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the first record to retrieve. Record numbers are zero-based. The default value is 0.',
                },
                'name': 'startingRecord',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'default_value': None,
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of records to fetch.',
                },
                'name': 'numberOfRecords',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'default_value': None,
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of samples per record.',
                },
                'name': 'numberOfSamples',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'complex_array_representation': 'complex_number_array',
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies a pre-allocated 2D numpy array of shape (number_of_records, number_of_samples) to be filled with the acquired I/Q data. Each row corresponds to one record. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.',
                },
                'name': 'iq_data_arrays',
                'numpy': True,
                'type': 'NIComplexNumber[]',
                'type_in_documentation': '2D numpy.array of numpy.complex64, 2D numpy.array of numpy.complex128 or interleaved complex data in the form of 2D numpy.array of numpy.int16',
                'use_in_python_api': True
            },
            {
                'default_value': 'hightime.timedelta(seconds=10.0)',
                'direction': 'in',
                'documentation': {
                    'description': '**PXI-5661, PXIe-5663/5665/5667** Specifies the time, in seconds, allotted for the function to complete before returning a timeout error.\n\n**PXIe-5644/5645/5646, PXIe-5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860** Specifies the time, in seconds, allotted to receive the reference trigger.\n\n----\n\nFor all supported devices, a value of  specifies the function waits until all data is available. A value of 0 specifies the function immediately returns available data.\n\n----',
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'python_name': 'fetch_iq_multi_record',
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'FetchIQSingleRecordComplexF32': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Fetches I/Q data from a single record in an acquisition.\n\nThe fetch transfers acquired waveform data from device memory to computer memory. The data was acquired to onboard memory previously by the hardware after the acquisition was initiated.\n\nThis function is not necessary if you use the read IQ single record complex F64 function because the read IQ single record complex F64 function performs the fetch as part of the function.\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`None (Trigger Type) <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/no-trigger.html>`_',
        },
        'grpc_name': 'FetchIQSingleRecordComplexF32',
        'included_in_proto': True,
        'is_error_handling': False,
        'method_name_for_documentation': 'fetch_iq_single_record',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies which channels to apply settings. Specify an empty string as the value of this parameter.',
                },
                'is_repeated_capability': True,
                'repeated_capability_type': 'channels',
                'name': 'channelList',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the record to retrieve. Record numbers are zero-based.',
                },
                'name': 'recordNumber',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of samples to fetch. The value must specify the array size of the NIRFSA_ATTR_DATA parameter.',
                },
                'name': 'numberOfSamples',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '**PXI-5661, PXIe-5663/5665/5667** Specifies the time, in seconds, allotted for the function to complete before returning a timeout error.\n\n**PXIe-5644/5645/5646, PXIe-5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860** Specifies the time, in seconds, allotted to receive the reference trigger.\n\n----\n\nFor all supported devices, a value of  specifies the function waits until all data is available. A value of 0 specifies the function immediately returns available data.\n\n----',
                },
                'default_value': 'hightime.timedelta(seconds=10.0)',
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'complex_array_representation': 'complex_number_array',
                'direction': 'in',
                'documentation': {
                    'description': 'Returns the acquired waveform. Allocate an NIComplexNumberF32 array at least as large as **NIRFSA_ATTR_NUMBER_OF_SAMPLES**.',
                },
                'name': 'iq_data_array',
                'numpy': True,
                'size': {'mechanism': 'passed-in', 'value': 'numberOfSamples'},
                'type': 'NIComplexNumberF32[]',
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Contains the absolute and relative timestamps for the operation, the time interval (dt), and the actual number of samples read.\n\nThe following list provides more information about each of these properties:\n\n- **absolute timestamp** Returns the timestamp, in seconds, of the first fetched sample that is comparable between records and acquisitions.\n\n----\n\nThe value of the absolute timestamp returned is always 0 for the PXIe-5644/5645/5646, PXIe-5668, and PXIe-5820/5830/5831/5832/5840/5841/5842/5860.\n\n----\n\n- **relative timestamp** Returns a timestamp that corresponds to the difference, in seconds, between the first sample returned and the Reference Trigger location. The timestamp is zero if the Reference Trigger has not occurred.\n\n----\n\nThe value of the relative timestamp returned is always 0 for the PXIe-5644/5645/5646.\n\n----\n\n- **dt** Returns the time interval between data points in the acquired signal. The I/Q data sample rate is the reciprocal of this value.\n- **actual samples read** Returns an integer representing the number of samples in the waveform.\n- **offset** Returns the offset to scale data, (*b*), in *mx* + *b* form.\n- **gain** Returns the gain to scale data, (*m*), in *mx* + *b* form.',
                },
                'name': 'wfmInfo',
                'type': 'niRFSA_wfmInfo',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'FetchIQSingleRecordComplexF64': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Fetches I/Q data from a single record in an acquisition.\n\nThe fetch transfers acquired waveform data from device memory to computer memory. The data was acquired to onboard memory previously by the hardware after the acquisition was initiated.\n\nThis function is not necessary if you use the read IQ single record complex F64 function because the read IQ single record complex F64 function performs the fetch as part of the function.\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`None (Trigger Type) <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/no-trigger.html>`_',
        },
        'grpc_name': 'FetchIQSingleRecordComplexF64',
        'included_in_proto': True,
        'is_error_handling': False,
        'method_name_for_documentation': 'fetch_iq_single_record',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies which channels to apply settings. Specify an empty string as the value of this parameter.',
                },
                'is_repeated_capability': True,
                'repeated_capability_type': 'channels',
                'name': 'channelList',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the record to retrieve. Record numbers are zero-based.',
                },
                'name': 'recordNumber',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of samples to fetch. The value must specify the array size of the NIRFSA_ATTR_DATA parameter.',
                },
                'name': 'numberOfSamples',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '**PXI-5661, PXIe-5663/5665/5667** Specifies the time, in seconds, allotted for the function to complete before returning a timeout error.\n\n**PXIe-5644/5645/5646, PXIe-5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860** Specifies the time, in seconds, allotted to receive the reference trigger.\n\n----\n\nFor all supported devices, a value of  specifies the function waits until all data is available. A value of 0 specifies the function immediately returns available data.\n\n----',
                },
                'default_value': 'hightime.timedelta(seconds=10.0)',
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'complex_array_representation': 'complex_number_array',
                'direction': 'in',
                'documentation': {
                    'description': 'Returns the acquired waveform. Allocate an NIComplexNumber array at least as large as **NIRFSA_ATTR_NUMBER_OF_SAMPLES**.',
                },
                'name': 'iq_data_array',
                'numpy': True,
                'size': {'mechanism': 'passed-in', 'value': 'numberOfSamples'},
                'type': 'NIComplexNumber[]',
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Contains the absolute and relative timestamps for the operation, the time interval (dt), and the actual number of samples read.\n\nThe following list provides more information about each of these properties:\n\n- **absolute timestamp** Returns the timestamp, in seconds, of the first fetched sample that is comparable between records and acquisitions.\n\n----\n\nThe value of the absolute timestamp returned is always 0 for the PXIe-5644/5645/5646, PXIe-5668, and PXIe-5820/5830/5831/5832/5840/5841/5842/5860.\n\n----\n\n- **relative timestamp** Returns a timestamp that corresponds to the difference, in seconds, between the first sample returned and the Reference Trigger location. The timestamp is zero if the Reference Trigger has not occurred.\n\n----\n\nThe value of the relative timestamp returned is always 0 for the PXIe-5644/5645/5646.\n\n----\n\n- **dt** Returns the time interval between data points in the acquired signal. The I/Q data sample rate is the reciprocal of this value.\n- **actual samples read** Returns an integer representing the number of samples in the waveform.\n- **offset** Returns the offset to scale data, (*b*), in *mx* + *b* form.\n- **gain** Returns the gain to scale data, (*m*), in *mx* + *b* form.',
                },
                'name': 'wfmInfo',
                'type': 'niRFSA_wfmInfo',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'FetchIQSingleRecordComplexI16': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Fetches binary I/Q data from a single record in an acquisition.\n\nThe fetch transfers acquired waveform data from device memory to computer memory. The data was acquired to onboard memory previously by the hardware after the acquisition was initiated.\n\nThis function is not necessary if you use the read IQ single record complex F64 function because the read IQ single record complex F64 function performs the fetch as part of the function.\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`None (Trigger Type) <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/no-trigger.html>`_',
        },
        'grpc_name': 'FetchIQSingleRecordComplexI16',
        'included_in_proto': True,
        'is_error_handling': False,
        'method_name_for_documentation': 'fetch_iq_single_record',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies which channels to apply settings. Specify an empty string as the value of this parameter.',
                },
                'is_repeated_capability': True,
                'repeated_capability_type': 'channels',
                'name': 'channelList',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the record to retrieve. Record numbers are zero-based.',
                },
                'name': 'recordNumber',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of samples to fetch. The value must specify the array size of the NIRFSA_ATTR_DATA parameter.',
                },
                'name': 'numberOfSamples',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '**PXI-5661, PXIe-5663/5665/5667** Specifies the time, in seconds, allotted for the function to complete before returning a timeout error.\n\n**PXIe-5644/5645/5646, PXIe-5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860** Specifies the time, in seconds, allotted to receive the reference trigger.\n\n----\n\nFor all supported devices, a value of  specifies the function waits until all data is available. A value of 0 specifies the function immediately returns available data.\n\n----',
                },
                'default_value': 'hightime.timedelta(seconds=10.0)',
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'complex_array_representation': 'interleaved_real_number_array',
                'direction': 'in',
                'documentation': {
                    'description': 'Returns the acquired waveform. Allocate an NIComplexI16 array at least as large as **NIRFSA_ATTR_NUMBER_OF_SAMPLES**.',
                },
                'name': 'iq_data_array',
                'numpy': True,
                'size': {'mechanism': 'passed-in', 'value': 'numberOfSamples'},
                'type': 'NIComplexI16[]',
                'use_array': True,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Contains the absolute and relative timestamps for the operation, the time interval (dt), and the actual number of samples read.\n\nThe following list provides more information about each of these properties:\n\n- **absolute timestamp** Returns the timestamp, in seconds, of the first fetched sample that is comparable between records and acquisitions.\n\n----\n\nThe value of the absolute timestamp returned is always 0 for the PXIe-5644/5645/5646, PXIe-5668, and PXIe-5820/5830/5831/5832/5840/5841/5842/5860.\n\n----\n\n- **relative timestamp** Returns a timestamp that corresponds to the difference, in seconds, between the first sample returned and the Reference Trigger location. The timestamp is zero if the Reference Trigger has not occurred.\n\n----\n\nThe value of the relative timestamp returned is always 0 for the PXIe-5644/5645/5646.\n\n----\n\n- **dt** Returns the time interval between data points in the acquired signal. The I/Q data sample rate is the reciprocal of this value.\n- **actual samples read** Returns an integer representing the number of samples in the waveform.\n- **offset** Returns the offset to scale data, (*b*), in *mx* + *b* form.\n- **gain** Returns the gain to scale data, (*m*), in *mx* + *b* form.',
                },
                'name': 'wfmInfo',
                'type': 'niRFSA_wfmInfo',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'FetchIqSingleRecordDispatcher': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': 'Fetches I/Q data from a single record in an acquisition.\n\nThe fetch transfers acquired waveform data from device memory to computer memory. The data was acquired to onboard memory previously by the hardware after the acquisition was initiated.\n\nThis function accepts a data_type parameter to specify the desired data format: numpy.complex64, numpy.complex128, or numpy.int16.\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`None (Trigger Type) <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/no-trigger.html>`_',
        },
        'included_in_proto': False,
        'is_error_handling': False,
        'method_name_for_documentation': 'fetch_iq_single_record',
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '_into',
                'session_filename': 'fetch_iq_single_record'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies which channels to apply settings. Specify an empty string as the value of this parameter.',
                },
                'is_repeated_capability': True,
                'repeated_capability_type': 'channels',
                'name': 'channelList',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'default_value': 0,
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the record to retrieve. Record numbers are zero-based.',
                },
                'name': 'recordNumber',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'default_value': None,
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of samples to fetch. The value must specify the array size of the NIRFSA_ATTR_DATA parameter.',
                },
                'name': 'numberOfSamples',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'complex_array_representation': 'complex_number_array',
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the pre-allocated numpy array to be filled with the acquired I/Q data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.',
                },
                'name': 'iq_data_array',
                'numpy': True,
                'type': 'NIComplexNumber[]',
                'type_in_documentation': 'numpy array of numpy.complex64, numpy array of numpy.complex128 or interleaved complex data in the form of numpy array of numpy.int16',
                'use_in_python_api': True
            },
            {
                'default_value': 'hightime.timedelta(seconds=10.0)',
                'direction': 'in',
                'documentation': {
                    'description': '**PXI-5661, PXIe-5663/5665/5667** Specifies the time, in seconds, allotted for the function to complete before returning a timeout error.\n\n**PXIe-5644/5645/5646, PXIe-5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860** Specifies the time, in seconds, allotted to receive the reference trigger.\n\n----\n\nFor all supported devices, a value of  specifies the function waits until all data is available. A value of 0 specifies the function immediately returns available data.\n\n----',
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'python_name': 'fetch_iq_single_record',
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'GetAttributeViBoolean': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Queries the value of a ViBoolean attribute.\n\nYou can use this low-level function to get the values of inherent IVI attributes and instrument-specific attributes.\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the channel on which to check the attribute value if the attribute is channel based. If the attribute is not channel based, set this parameter to "" (empty string) or VI_NULL.',
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.',
                },
                'name': 'attributeId',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the current value of the attribute. Pass the address of a ViBoolean variable.',
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
            'description': 'Queries the value of a ViInt32 attribute.\n\nYou can use this low-level function to get the values of inherent IVI attributes and instrument-specific attributes.\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the channel on which to check the attribute value if the attribute is channel based. If the attribute is not channel based, set this parameter to "" (empty string) or VI_NULL.',
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.',
                },
                'name': 'attributeId',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the current value of the attribute. Pass the address of a ViInt32 variable.',
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
            'description': 'Queries the value of a ViInt64 attribute.\n\nYou can use this low-level function to get the values of inherent IVI attributes and instrument-specific attributes.\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the channel on which to check the attribute value if the attribute is channel based. If the attribute is not channel based, set this parameter to "" (empty string) or VI_NULL.',
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.',
                },
                'name': 'attributeId',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the current value of the attribute. Pass the address of a ViInt64 variable.',
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
            'description': 'Queries the value of a ViReal64 attribute.\n\nYou can use this low-level function to get the values of inherent IVI attributes and instrument-specific attributes.\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the channel on which to check the attribute value if the attribute is channel based. If the attribute is not channel based, set this parameter to "" (empty string) or VI_NULL.',
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.',
                },
                'name': 'attributeId',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the current value of the attribute. Pass the address of a ViReal64 variable.',
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
            'description': 'Queries the value of a ViSession attribute.\n\nYou can use this low-level function to get the values of inherent IVI attributes and instrument-specific attributes.\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the channel on which to check the attribute value if the attribute is channel based. If the attribute is not channel based, set this parameter to "" (empty string) or VI_NULL.',
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.',
                },
                'name': 'attributeId',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the current value of the attribute. Pass the address of a ViSession variable.',
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
            'description': 'Queries the value of a ViString attribute.\n\nYou can use this low-level function to get the values of inherent IVI attributes and instrument-specific attributes.\n\nYou must provide a ViChar array to serve as a buffer for the value. You pass the number of bytes in the buffer as the **NIRFSA_ATTR_BUF_SIZE** parameter. If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **NIRFSA_ATTR_BUF_SIZE** parameter, the function copies buffer size  1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.\n\nIf you want to call this function just to get the required buffer size, you can pass 0 for **NIRFSA_ATTR_BUF_SIZE** and VI_NULL for the **attributeValue** buffer.\n\n**Supported Devices:** PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the channel on which to check the attribute value if the attribute is channel based. If the attribute is not channel based, set this parameter to "" (empty string) or VI_NULL.',
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.',
                },
                'name': 'attributeId',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the number of bytes in the ViChar buffer you specify for the attribute value parameter.\n\nIf you pass 0, you can pass VI_NULL for the attribute value buffer parameter.',
                },
                'name': 'bufSize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The buffer in which the function returns the current value of the attribute. The buffer must be of type ViChar and have at least as many bytes as indicated in **NIRFSA_ATTR_BUF_SIZE**.\n\nIf you specify 0 for the **NIRFSA_ATTR_BUF_SIZE** parameter, you can pass VI_NULL for this parameter.',
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
            'description': 'Retrieves and then clears the IVI error information for the session or the current execution thread.\n\n----\n**Note**\nIf the **NIRFSA_ATTR_ERROR_DESCRIPTION_BUFFER_SIZE** parameter is 0, this function does not clear the error information. By passing 0 to **NIRFSA_ATTR_ERROR_DESCRIPTION_BUFFER_SIZE**, you can determine the buffer size required to read the entire error description string. You can then call this function again with a sufficiently large buffer.\n\nIf you specify a valid IVI session for the NIRFSA_ATTR_VI parameter, this function retrieves and then clears the error information for the session. If you pass VI_NULL for NIRFSA_ATTR_VI, this function retrieves and then clears the error information for the current execution thread. If NIRFSA_ATTR_VI is an invalid session, this function does nothing and returns an error. Normally, the error information describes the first error that occurred since you last called this function or the nirfsa_ClearError function.\n\n----\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5840',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the error code for the session or execution thread. If you pass 0 for the **NIRFSA_ATTR_ERROR_DESCRIPTION_BUFFER_SIZE** parameter, you can pass VI_NULL for this parameter.',
                },
                'name': 'errorCode',
                'type': 'ViStatus',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Passes the number of bytes in the ViChar array you specify in **description**.\n\nIf the error description, including the terminating NULL byte, contains more bytes than you indicate in this parameter, the function copies **NIRFSA_ATTR_ERROR_DESCRIPTION_BUFFER_SIZE**  1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the size of the buffer that you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.\n\nIf you pass 0, you can pass VI_NULL for the **NIRFSA_ATTR_ERROR_DESCRIPTION** parameter.',
                },
                'name': 'errorDescriptionBufferSize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the error description for the IVI session or execution thread. If there is no description, this function returns an empty string.\n\nThe buffer must contain at least as many elements as the value you specify with the **NIRFSA_ATTR_ERROR_DESCRIPTION_BUFFER_SIZE** parameter. If the error description, including the terminating NULL byte, contains more bytes than you indicate in this parameter, the function copies **NIRFSA_ATTR_ERROR_DESCRIPTION_BUFFER_SIZE**  1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the size of the buffer, in the **status** return value, that you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.\n\nIf you pass 0, you can pass VI_NULL for the this parameter.',
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
    'GetLastExtCalLastDateAndTime': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': '\nReturns the date and time of the last successful external calibration.\n\nThe time returned is 24-hour (military) local time; for example, if the device was calibrated at 2:30PM, this function returns\n\n14 for the hours parameter and\n\n30 for the minutes parameter.\n\n**Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5696, PXIe-5820/5830/5831/5832/5840/5841/5842/5860',
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
        'python_name': 'get_ext_cal_last_date_and_time',
        'real_datetime_call': 'GetExtCalLastDateAndTime',
        'returns': 'ViStatus'
    },
    'GetLastSelfCalLastDateAndTime': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': '\nReturns the date and time of the last successful self-calibration.\n\nThe time returned is 24-hour local time. For example, if the device was calibrated at 2:30PM, this function returns\n\n14 for the hours parameter and\n\n30 for the minutes parameter.\n\n**Supported Devices** : PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860',
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
                    'description': 'Specifies the self-calibration step to query for the last successful self-calibration date and time data.',
                },
                'enum': 'SelfCalibrationStep',
                'name': 'selfCalibrationStep',
                'type': 'ViInt64'
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
        'python_name': 'get_self_cal_last_date_and_time',
        'real_datetime_call': 'GetSelfCalLastDateAndTime',
        'returns': 'ViStatus'
    },
    'GetExtCalLastDateAndTime': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Returns the date and time of the last successful external calibration.\n\nThe time returned is 24-hour local time, and the date is returned as integer values. For example, if the device was calibrated at 2:30 PM on December 31, 2010, this function returns 14 for the NIRFSA_ATTR_HOUR parameter, 30 for the NIRFSA_ATTR_MINUTE parameter, 12 for the NIRFSA_ATTR_MONTH parameter, 31 for the NIRFSA_ATTR_DAY parameter, and 2010 for the NIRFSA_ATTR_YEAR parameter.\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860',
        },
        'included_in_proto': True,
        'method_name_for_documentation': 'get_ext_cal_last_date_and_time',
        'is_error_handling': False,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init, nirfsa_InitWithOptions, or nirfsa_InitExtCal function and identifies a particular instrument session.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the year of the last external calibration.',
                },
                'name': 'year',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the month of the last external calibration.',
                },
                'name': 'month',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the day of the last external calibration.',
                },
                'name': 'day',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the hour of the last external calibration.',
                },
                'name': 'hour',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the minute of the last external calibration.',
                },
                'name': 'minute',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },            
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'GetExtCalRecommendedInterval': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the recommended interval between external calibrations, in months.\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init, nirfsa_InitWithOptions, or nirfsa_InitExtCal function and identifies a particular instrument session.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the recommended maximum interval between external calibrations, in months.',
                },
                'name': 'months',
                'python_api_converter_name': 'convert_month_to_timedelta',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or int in months',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'GetFetchBacklog': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the number of points acquired that have not yet been fetched.\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies which channels to apply settings. Specify an empty string as the value of this parameter.',
                },
                'is_repeated_capability': True,
                'repeated_capability_type': 'channels',
                'name': 'channelList',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the record from which to read the backlog. Record numbers are zero-based.',
                },
                'name': 'recordNumber',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the number of samples available to read for the requested record.',
                },
                'name': 'backlog',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'GetFrequencyResponse': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the requested device response type, based on current NI-RFSA settings. The PXI-5661 and PXIe-5663/5663E/5665/5667/5668 automatically corrects the IF and RF response when you set the Digital IF Equalization Enabled property to TRUE. If you are using external digitizer mode, you can use information returned from this VI to correct your measurement.\n\nRefer to the *Factory Calibration* topic for your device for more information about frequency-response calibration.\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies which channels to apply settings. Specify an empty string as the value of this parameter.',
                },
                'is_repeated_capability': True,
                'repeated_capability_type': 'channels',
                'name': 'channelList',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the size of the array you specify for the NIRFSA_ATTR_FREQUENCIES, **NIRFSA_ATTR_MAGNITUDE_RESPONSE**, and **NIRFSA_ATTR_PHASE_RESPONSE** parameters.',
                },
                'name': 'bufferSize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns an array containing the frequencies, in hertz (Hz), that correspond to the response data.\n\nPass VI_NULL if you do not want to use this parameter.',
                },
                'name': 'frequencies',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'numberOfFrequencies'
                },
                'type': 'ViReal64[]',
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns an array containing the magnitude of the requested response, in decibels (dB). The magnitude response is normalized to the center frequency at each frequency in the NIRFSA_ATTR_FREQUENCIES array.\n\nPass VI_NULL if you do not want to use this parameter.',
                },
                'name': 'magnitudeResponse',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'numberOfFrequencies'
                },
                'type': 'ViReal64[]',
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns an array containing the phase of the requested response, in radians. The phase response is normalized to the center frequency at each frequency entry in the NIRFSA_ATTR_FREQUENCIES array.\n\nPass VI_NULL if you do not want to use this parameter. This array may contain zeros if the device does not contain a stored phase response in its calibration data.',
                },
                'name': 'phaseResponse',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'numberOfFrequencies'
                },
                'type': 'ViReal64[]',
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the required number of elements in the NIRFSA_ATTR_FREQUENCIES array and the response arrays. If **NIRFSA_ATTR_BUFFER_SIZE** is 0, this parameter returns the expected array size. The expected array size depends on which NI-RFSA device you use (PXI-5661, PXIe-5663/5663E/5665) and on the current settings (PXIe-5663/5663E/5665 only).',
                },
                'name': 'numberOfFrequencies',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'GetSelfCalLastDateAndTime': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Returns the date and time of the last successful self-calibration.\n\nThe time returned is 24-hour local time, and the date is returned as integer values. For example, if the device was calibrated at 2:30 PM on December 31, 2010, this function returns 14 for the NIRFSA_ATTR_HOUR parameter, 30 for the NIRFSA_ATTR_MINUTE parameter, 12 for the NIRFSA_ATTR_MONTH parameter, 31 for the NIRFSA_ATTR_DAY parameter, and 2010 for the NIRFSA_ATTR_YEAR parameter.\n\n----\n**Note**\nFor the PXIe-5644/5645/5646, you must select NIRFSA_VAL_SELF_CAL_IMAGE_SUPPRESSION for the **NIRFSA_ATTR_SELF_CALIBRATION_STEP** parameter.\n\n----\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860',
        },
        'grpc_name': 'GetSelfCalLastDateAndTime',
        'included_in_proto': True,
        'method_name_for_documentation': 'get_self_calibration_date_and_time',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the self-calibration step to query for the last successful self-calibration date and time data.',
                    'table_body': [
                        [
                            'SelfCalibrationStep.PRESELECTOR_ALIGNMENT',
                            'Calls for preselector alignment.'
                        ],
                        [
                            'SelfCalibrationStep.GAIN_REFERENCE',
                            'Measures the changes in gain since the last external calibration was run.'
                        ],
                        [
                            'SelfCalibrationStep.IF_FLATNESS',
                            'Measures the IF response of the entire system for each of the supported IF filters'
                        ],
                        [
                            'SelfCalibrationStep.DIGITIZER_SELF_CAL',
                            'Calls for digitizer self-calibration, if the digitizer is associated with the RF downconverter.'
                        ],
                        [
                            'SelfCalibrationStep.LO_SELF_CAL',
                            'Calls for LO self-calibration, if the LO source module is associated with the RF downconverter.'
                        ],
                        [
                            'SelfCalibrationStep.AMPLITUDE_ACCURACY',
                            'Selects the Amplitude Accuracy self-calibration step.'
                        ],
                        [
                            'SelfCalibrationStep.RESIDUAL_LO_POWER',
                            'Selects the Residual LO Power self-calibration step.'
                        ],
                        [
                            'SelfCalibrationStep.IMAGE_SUPPRESSION',
                            'Selects the Image Suppression self-calibration step.'
                        ],
                        [
                            'SelfCalibrationStep.SYNTHESIZER_ALIGNMENT',
                            'Selects the Synthesizer Alignment self-calibration step.'
                        ],
                        [
                            'SelfCalibrationStep.DC_OFFSET',
                            'Selects the DC Offset self-calibration step.'
                        ]
                    ],
                    'table_header': [
                        'Name',
                        'Description'
                    ]
                },
                'enum': 'SelfCalibrationStep',
                'grpc_name': 'self_calibration_step',
                'name': 'selfCalibrationStep',
                'type': 'ViInt64',
                'type_in_documentation': 'Bitwise combination of enums.SelfCalibrationStep flags',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the year of the last external calibration.',
                },
                'name': 'year',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the month of the last external calibration.',
                },
                'name': 'month',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the day of the last external calibration.',
                },
                'name': 'day',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the year of the last external calibration. It is expressed as an integer.',
                },
                'name': 'hour',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the minute of the last external calibration.',
                },
                'name': 'minute',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'GetScalingCoefficients': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns coefficients you can use to convert unscaled data to scaled I/Q data.\n\nAcquired data may be unscaled when sent by a peer-to-peer stream or fetched as unscaled data. Use this function to obtain nirfsa_GetScalingCoefficients structures in the **NIRFSA_ATTR_COEFFICIENT_INFO** array that provide gain and offset values you can use to scale this data into the actual I/Q values. The **NIRFSA_ATTR_COEFFICIENT_INFO** array returns one element for each channel specified in the **NIRFSA_ATTR_CHANNEL_LIST** parameter. The element order matches the order specified by the **NIRFSA_ATTR_CHANNEL_LIST** parameter. To get the actual I/Q values, scale the unscaled data from an acquisition by multiplying it by the gain value of the appropriate **NIRFSA_ATTR_COEFFICIENT_INFO** element then adding the offset from the same element.\n\n----\n**Note**\nThe coefficients are calculated by NI-RFSA for the current configuration of the device, so they are only valid for acquisitions obtained with the same device configuration.\n\n----\n\nTo get the required size of the array, call this function with **NIRFSA_ATTR_ARRAY_SIZE** set to 0 and NULL for the **NIRFSA_ATTR_COEFFICIENT_INFO** array. This function returns the required size in the **NIRFSA_ATTR_NUMBER_OF_COEFFICIENT_SETS** parameter.\n\n**Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies which channels to apply settings. Specify an empty string as the value of this parameter.',
                },
                'is_repeated_capability': True,
                'repeated_capability_type': 'channels',
                'name': 'channelList',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the size of the array you specify for the **NIRFSA_ATTR_COEFFICIENT_INFO** parameter.',
                },
                'name': 'arraySize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Specifies the array for storing the coefficient info.\n\n- **offset** is the number that should be added to the data from a peer-to-peer stream after the gain has been applied if you want to scale unscaled data.\n- **gain** returns the multiplier that you should use to scale data obtained from a peer-to-peer stream.',
                },
                'name': 'coefficientInfo',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'numberOfCoefficientSets'
                },
                'type': 'niRFSA_coefficientInfo[]',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the number of valid coefficient sets.',
                },
                'name': 'numberOfCoefficientSets',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'GetSelfCalLastTemp': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the temperature, in degrees Celsius, at the last successful self-calibration.\n\n----\n**Note**\nFor the PXIe-5644/5645/5646, you must select NIRFSA_VAL_SELF_CAL_IMAGE_SUPPRESSION for the **selfCalibrationStep** parameter.\n\n----\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831 (IF only)/5832 (IF only)/5840/5841/5842/5860',
        },
        'grpc_name': 'GetSelfCalLastTemp',
        'included_in_proto': True,
        'is_error_handling': False,
        'python_name': 'get_self_calibration_temperature',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the self-calibration step to query for the last successful self-calibration date and time data.',
                    'table_body': [
                        [
                            'SelfCalibrationStep.PRESELECTOR_ALIGNMENT',
                            'Calls for preselector alignment.'
                        ],
                        [
                            'SelfCalibrationStep.GAIN_REFERENCE',
                            'Measures the changes in gain since the last external calibration was run.'
                        ],
                        [
                            'SelfCalibrationStep.IF_FLATNESS',
                            'Measures the IF response of the entire system for each of the supported IF filters'
                        ],
                        [
                            'SelfCalibrationStep.DIGITIZER_SELF_CAL',
                            'Calls for digitizer self-calibration, if the digitizer is associated with the RF downconverter.'
                        ],
                        [
                            'SelfCalibrationStep.LO_SELF_CAL',
                            'Calls for LO self-calibration, if the LO source module is associated with the RF downconverter.'
                        ],
                        [
                            'SelfCalibrationStep.AMPLITUDE_ACCURACY',
                            'Selects the Amplitude Accuracy self-calibration step.'
                        ],
                        [
                            'SelfCalibrationStep.RESIDUAL_LO_POWER',
                            'Selects the Residual LO Power self-calibration step.'
                        ],
                        [
                            'SelfCalibrationStep.IMAGE_SUPPRESSION',
                            'Selects the Image Suppression self-calibration step.'
                        ],
                        [
                            'SelfCalibrationStep.SYNTHESIZER_ALIGNMENT',
                            'Selects the Synthesizer Alignment self-calibration step.'
                        ],
                        [
                            'SelfCalibrationStep.DC_OFFSET',
                            'Selects the DC Offset self-calibration step.'
                        ]
                    ],
                    'table_header': [
                        'Name',
                        'Description'
                    ]
                },
                'enum': 'SelfCalibrationStep',
                'grpc_name': 'self_calibration_step',
                'name': 'selfCalibrationStep',
                'type': 'ViInt64',
                'type_in_documentation': 'Bitwise combination of enums.SelfCalibrationStep flags',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the temperature, in degrees Celsius, of the device at the last successful self-calibration.',
                },
                'grpc_name': 'temp',
                'name': 'temperature',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'GetTerminalName': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the fully qualified name of the signal being queried.\n\nSignals can be triggers, clocks, or events.\n\nYou can pass the **NIRFSA_ATTR_TERMINAL_NAME** parameter that is returned to the **source** parameter of a configure trigger function.\n\n**Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Events <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/events.html>`_',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the signal for which you want to query the terminal.',
                    'table_body': [
                        [
                            'Signal.START_TRIGGER',
                            'NI-RFSA routes a Start Trigger.'
                        ],
                        [
                            'Signal.REF_TRIGGER',
                            'NI-RFSA routes a Reference'
                        ],
                        [
                            'Signal.ADVANCE_TRIGGER',
                            'NI-RFSA routes an Advance'
                        ],
                        [
                            'Signal.READY_FOR_START_EVENT',
                            'NI-RFSA routes a Ready for Start Event.'
                        ],
                        [
                            'Signal.READY_FOR_REF_EVENT',
                            'NI-RFSA routes a Ready for Reference Event..'
                        ],
                        [
                            'Signal.END_OF_RECORD_EVENT',
                            'NI-RFSA routes a End of Record Event.'
                        ],
                        [
                            'Signal.DONE_EVENT',
                            'NI-RFSA routes a Done Event.'
                        ],
                        [
                            'Signal.REF_CLOCK',
                            'NI-RFSA routes a Reference Clock.'
                        ],
                        [
                            'Signal.USER',
                            'NI-RFSA routes a User Defined Signal.'
                        ]
                    ],
                    'table_header': [
                        'Name',
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
                    'description': 'Specifies a particular instance of a trigger. NI-RFSA does not support this parameter.',
                },
                'default_value': '""',
                'name': 'signalIdentifier',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Passes the number of bytes in the ViChar buffer that you allocate for the **NIRFSA_ATTR_TERMINAL_NAME** parameter.',
                },
                'name': 'bufferSize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the fully qualified name of the signal being queried.',
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
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'InitWithOptions': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Creates a new session for the device.\n\nThis function sets the initial value of certain attributes and sends initialization commands to reset all hardware modules to a known state necessary for NI-RFSA operation.\n\nTo create a new session, pass the downconverter resource name for the RF vector signal analyzer to the **resource name** parameter.\n\nYou can access the device session this VI creates using the NI-RFSA Soft Front Panel (SFP). Accessing the device session with the SFP can help you debug your code. Refer to `Debugging Your Application Using SFP Session Access <https://www.ni.com/docs/en-US/bundle/ni-rfsa-sfp/page/rfsasfp/using_session_access_sfp_top.html>`_ for more information about accessing your session with the SFP.\n\n----\n**Note**\nBefore initializing your device, you must first associate the modules that comprise your device in MAX. After associating the modules, pass the resource name of the device to this function to initialize all the modules. Refer to `Associating NI-RFSA Modules <https://www.ni.com/docs/en-US/bundle/ni-rfsa-max/page/maxrfsa/mi_rf_associating.html>`_ for information about MAX association.\n\n----\n\n----\n**Note**\nFor multichannel devices such as the PXIe-5860, the resource name must include the channel number to use. The channel number is specified by appending *ChannelNumber* to the device name, where *ChannelNumber* is the channel number (0, 1, etc.). For example, if the device name is PXI1Slot2 and you want to use channel 0, use the resource name PXI1Slot2/0.\n\n----\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Driver Setup Options <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/driver-setup-options.html>`_',
        },
        'included_in_proto': True,
        'method_name_for_documentation': '__init__',
        'is_error_handling': False,
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
                    'description': 'Specifies the resource name of the device to initialize.\n\nFor NI-RFSA devices, the syntax is the device name specified in MAX. The typical default name for your device in MAX is PXI1Slot2. You can rename your device by right-clicking the name in MAX, selecting **Rename** from the drop-down menu, and entering a new name. You can also pass in the name of an IVI logical name configured with the IVI Configuration utility. For additional information, refer to the **Installed Devices IVI** topic of the *Measurement & Automation Explorer Help*.\n\nDevice names are not case-sensitive. However, IVI logical names are case-sensitive. If you use an IVI logical name, verify the name is identical to the name shown in the IVI Configuration Utility.',
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
                    'description': 'Specifies whether you want NI-RFSA to perform an ID query.\n\n**Defined Values** :',
                    'table_body': [
                        [
                            'Perform ID query.'
                        ],
                        [
                            'Do not perform ID query.'
                        ]
                    ],
                    'table_header': [
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
                    'description': 'Specifies whether the NI-RFSA device is reset during the initialization procedure.\n\n**Defined Values** :',
                    'table_body': [
                        [
                            'Reset the device.'
                        ],
                        [
                            'Do not reset device.'
                        ]
                    ],
                    'table_header': [
                        'Description'
                    ]
                },
                    'grpc_name': 'reset',
                    'name': 'resetDevice',
                'type': 'ViBoolean',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'default_value': '""',
                'direction': 'in',
                'documentation': {
                    'description': 'Sets the initial value of certain attributes for the session. The attributes shown in the following table are used in this parameter.\n\n| Name             | Attribute                                                                                                                                  |\n|:-----------------|:-------------------------------------------------------------------------------------------------------------------------------------------|\n| RangeCheck       | NIRFSA_ATTR_RANGE_CHECK                         |\n| QueryInstrStatus | NIRFSA_ATTR_QUERY_INSTRUMENT_STATUS |\n| Cache            | NIRFSA_ATTR_CACHE                                     |\n| RecordCoercions  | NIRFSA_ATTR_RECORD_COERCIONS               |\n| DriverSetup      | NIRFSA_ATTR_DRIVER_SETUP                       |\n| Simulate         | NIRFSA_ATTR_SIMULATE                               |\n\nThe format of this string is *AttributeName=Value*, where *AttributeName* is the name of the attribute and *Value* is the value to which the attribute will be set. For example, you can simulate the PXIe-5663 using the following strings:\n\n*Simulate=1, DriverSetup=Model:5663\\E*.\n\n*Simulate=1, DriverSetup=Model:5601*; *Digitizer:5622; LO:5652; LOBoardType:PXIe*.\n\nTo set multiple attributes, separate their assignments with a comma.\n\nRefer to `Driver Setup Options <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/driver-setup-options.html>`_ for more information about the driver setup string.\n\nNote: To simulate a device using the PXIe-5622 25 MHz digitizer, set the *Digitizer* field to 5622_25MHz_DDC and the *Simulate* field to 1. You can set the *Digitizer* field to 5622_25MHz_DDC only when using the PXIe-5665.',
                },
                'name': 'optionString',
                'python_api_converter_name': 'convert_init_with_options_dictionary',
                'type': 'ViConstString',
                'type_in_documentation': 'dict',
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Identifies your instrument session.',
                },
                'grpc_name': 'vi',
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
            'description': 'Commits settings to hardware, waits for hardware settling, and starts an acquisition.\n\nYou can use this function in conjunction with one of the niRFSA fetch I/Q functions to retrieve acquired I/Q data, or you can use the read IQ single record complex F64 function to both initiate the acquisition and retrieve I/Q data at one time.\n\n----\n**Note**\nIf you are using external digitizer mode, this function commits settings and waits for settling, but it does not start an acquisition. Notice that using the nirfsa_Commit function on its own commits settings to hardware, but the device does not wait for hardware settling.\n\n----\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`None (Trigger Type) <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/no-trigger.html>`_\n\n`RF List Mode <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html>`_\n\n`NI RF Vector Signal Analyzer State Diagram <https://www.ni.com/docs/en-US/bundle/pxie-5668-feature/page/hardware-state-diagram.html>`_',
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
    },
    'IsSelfCalValid': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Indicates which calibration steps contain valid calibration data.\n\nTo omit steps with valid calibration data from self-calibration, you can pass the **NIRFSA_ATTR_VALID_STEPS** parameter to the **stepsToOmit** parameter of the nirfsa_SelfCalibrate function.\n\n**Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667/5668',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns VI_TRUE if all the calibration data is valid and VI_FALSE if any of the calibration data is invalid.',
                },
                'name': 'selfCalValid',
                'type': 'ViBoolean',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns valid steps.\n\n----\nIf two or more calibration steps are valid, this parameter returns a bitwise-OR combination of the calibration steps. For example, if both NIRFSA_VAL_SELF_CAL_IF_FLATNESS and NIRFSA_VAL_SELF_CAL_LO_SELF_CAL steps are valid, NI-RFSA returns the following string:\n\nNIRFSA_VAL_SELF_CAL_IF_FLATNESS |\n\nNIRFSA_VAL_SELF_CAL_LO_SELF_CAL\n\n----',
                    'table_body': [
                        [
                            'SelfCalSteps.DIGITIZER_SELF_CAL',
                            'Omits the Image Suppression step. If you omit this step, the Residual Sideband Image performance is not adjusted.'
                        ],
                        [
                            'SelfCalSteps.PRESELECTOR_ALIGNMENT',
                            'Omits the LO Self Cal step. If you omit this step, the power level of the LO is not adjusted.'
                        ],
                        [
                            'SelfCalSteps.OMIT_NONE',
                            'No calibration steps are omitted.'
                        ],
                        [
                            'SelfCalSteps.GAIN_REFERENCE',
                            'Omits the Power Level Accuracy step. If you omit this step, the power level accuracy of the device is not adjusted.'
                        ],
                        [
                            'SelfCalSteps.IF_FLATNESS',
                            'Omits the Residual LO Power step. If you omit this step, the Residual LO Power performance is not adjusted.'
                        ],
                        [
                            'SelfCalSteps.LO_SELF_CAL',
                            'Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.'
                        ],
                        [
                            'SelfCalSteps.AMPLITUDE_ACCURACY',
                            'Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.'
                        ],
                        [
                            'SelfCalSteps.RESIDUAL_LO_POWER',
                            'Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.'
                        ],
                        [
                            'SelfCalSteps.IMAGE_SUPPRESSION',
                            'Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.'
                        ],
                        [
                            'SelfCalSteps.SYNTHESIZER_ALIGNMENT',
                            'Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.'
                        ],
                        [
                            'SelfCalSteps.DC_OFFSET',
                            'Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.'
                        ]
                    ],
                    'table_header': [
                        'Name',
                        'Description'
                    ]
                },
                'enum': 'SelfCalSteps',
                'name': 'validSteps',
                'type': 'ViInt64',
                'type_in_documentation': 'Bitwise combination of enums.SelfCalSteps flags',
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
            'description': '\nLoads the configurations from the specified file to the NI-RFSA driver session.\n\nThe VI does an implicit reset before loading the configurations from the file.\n\n**Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842/5860',
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsa_Init function or the nirfsa_InitWithOptions function and identifies a particular instrument session.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the channel.',
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the absolute path of the file from which the NI-RFSA loads the configurations.',
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
            'description': 'Obtains a multithread lock on the instrument session.\n\nBefore doing so, this function waits until all other execution threads have released their locks on the instrument session.\n\nOther threads might have obtained a lock on this session in the following ways:\n\n- Your application already called this function.\n- A call to NI-RFSA locked the session.\n\nAfter the call to this function returns successfully, no other threads can access the instrument session until you call the nirfsa_UnlockSession function. Use the nirfsa_LockSession function and the nirfsa_UnlockSession function around a sequence of calls to NI-RFSA functions if you require that the NI-RFSA device retain its settings through the end of the sequence.\n\nYou can safely make nested calls to the nirfsa_LockSession function within the same thread. To completely unlock the session, balance each call to the nirfsa_LockSession function with a call to the nirfsa_UnlockSession function. If, however, you use **NIRFSA_ATTR_CALLER_HAS_LOCK** in all calls to the nirfsa_LockSession function and the nirfsa_UnlockSession function within a function, the IVI Library locks the session only once within the function regardless of the number of calls you make to the nirfsa_LockSession function. Locking the session only once allows you to call the nirfsa_UnlockSession function just once at the end of the function.\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Keeps track of whether you obtain a lock and therefore need to unlock the session in complex functions. Pass the address of a local ViBoolean variable. In the declaration of the local variable, initialize it to VI_FALSE. Pass the address of the same local variable to any other calls you make to this function or the nirfsa_UnlockSession function in the same function.\n\nThis parameter serves as a convenience. If you do not want to use this parameter, pass VI_NULL.\n\nThe nirfsa_LockSession function and the nirfsa_UnlockSession function each inspect the current value and take the actions shown in the following table.\n\n| Function             | Boolean Value | Action                                                                                               |\n|:---------------------|:--------------|:-----------------------------------------------------------------------------------------------------|\n| nirfsa_LockSession   | VI_TRUE       | The nirfsa_LockSession function does not lock the session again.                                     |\n|                      | VI_FALSE      | The nirfsa_LockSession function obtains the lock and sets the value of the parameter to VI_TRUE.     |\n| nirfsa_UnlockSession | VI_FALSE      | The nirfsa_UnlockSession function does not attempt to unlock the session.                            |\n|                      | VI_TRUE       | The nirfsa_UnlockSession function releases the lock and sets the value of the parameter to VI_FALSE. |\n\nThus, you can call the nirfsa_UnlockSession function at the end of your function regardless of whether you actually have the lock.',
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
    'PerformThermalCorrection': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Corrects for temperature variations while acquiring the same signal for an extended period of time in a continuous acquisition.\n\nNI-RFSA internally acquires the temperature every time you initiate an acquisition. If you are performing a continuous acquisition, National Instruments recommends calling this function once every 10 minutes in a stable temperature environment to periodically update temperature calibration. If the ambient temperature varies, call this function more frequently.\n\n----\n**Note**\nYou cannot call this function if your device is operating in `RF list mode <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html>`_.\n\n----\n\nRefer to the *Thermal Management* section for your device for more information about typical operating temperatures.\n\n**Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694, PXIe-5830/5831/5832/5840/5841/5842',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
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
    'ReadPowerSpectrumF32': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Initiates a spectrum acquisition and returns power spectrum data.\n\n----\n**Note**\n Under certain configurations, negative infinity is returned from this VI. If the Reference Level is very high and if the Signal Bandwidth is comparatively less, the ADC returns zero, which equates to negative infinity in dBm. This is expected behavior.\n\n----\n\n**Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860',
        },
        'included_in_proto': True,
        'method_name_for_documentation': 'read_power_spectrum',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies which channels to apply settings. Specify an empty string as the value of this parameter.',
                },
                'is_repeated_capability': True,
                'repeated_capability_type': 'channels',
                'name': 'channelList',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'default_value': 'hightime.timedelta(seconds=10.0)',
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the time, in seconds, allotted for the function to complete before returning a timeout error. A value of specifies the function waits until all data is available.',
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Returns power spectrum data. Allocate an array as large as **NIRFSA_ATTR_DATA_ARRAY_SIZE**.',
                },
                'name': 'powerSpectrumDataArray',
                'numpy': True,
                'size': {'mechanism': 'fixed', 'value': 1},
                'type': 'ViReal32[]',
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the size of the array that is returned by the **NIRFSA_ATTR_POWER_SPECTRUM_DATA** parameter. Use the nirfsa_GetNumberOfSpectralLines function to obtain the array size to allocate. The array must be at least as large as the number of spectral lines that NI-RFSA computes for the power spectrum.',
                },
                'name': 'dataArraySize',
                'size': {'mechanism': 'python-code', 'value': 'len(power_spectrum_data_array)'},
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': False
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns additional information about the **NIRFSA_ATTR_POWER_SPECTRUM_DATA** array. This information includes the frequency, in hertz (Hz), corresponding to the first element in the array, the frequency increment, in Hz, between adjacent array elements, and the number of spectral lines the function returned.',
                },
                'name': 'spectrumInfo',
                'type': 'niRFSA_spectrumInfo',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ReadPowerSpectrumF64': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Initiates a spectrum acquisition and returns power spectrum data.\n\n----\n**Note**\n Under certain configurations, negative infinity is returned from this VI. If the Reference Level is very high and if the Signal Bandwidth is comparatively less, the ADC returns zero, which equates to negative infinity in dBm. This is expected behavior.\n\n----\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5830/5831/5832/5840/5841/5842/5860',
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_name_for_documentation': 'read_power_spectrum',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies which channels to apply settings. Specify an empty string as the value of this parameter.',
                },
                'is_repeated_capability': True,
                'repeated_capability_type': 'channels',
                'name': 'channelList',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'default_value': 'hightime.timedelta(seconds=10.0)',
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the time, in seconds, allotted for the function to complete before returning a timeout error. A value of specifies the function waits until all data is available.',
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies a pre-allocated numpy array to be filled with power spectrum data. Allocate an array at least as large as the number of spectral lines returned by the get_number_of_spectral_lines method.',
                },
                'name': 'powerSpectrumDataArray',
                'numpy': True,
                'size': {'mechanism': 'fixed', 'value': 1},
                'type': 'ViReal64[]',
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the size of the array that is returned by the **NIRFSA_ATTR_POWER_SPECTRUM_DATA** parameter. Use the nirfsa_GetNumberOfSpectralLines function to obtain the array size to allocate. The array must be at least as large as the number of spectral lines that NI-RFSA computes for the power spectrum.',
                },
                'name': 'dataArraySize',
                'size': {'mechanism': 'python-code', 'value': 'len(power_spectrum_data_array)'},
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': False
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns additional information about the **NIRFSA_ATTR_POWER_SPECTRUM_DATA** array. This information includes the frequency, in hertz (Hz), corresponding to the first element in the array, the frequency increment, in Hz, between adjacent array elements, and the number of spectral lines the function returned.',
                },
                'name': 'spectrumInfo',
                'type': 'niRFSA_spectrumInfo',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ReadPowerSpectrumDispatcher': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': 'Initiates a spectrum acquisition and returns power spectrum data.\n\n----\n**Note**\n Under certain configurations, negative infinity is returned from this VI. If the Reference Level is very high and if the Signal Bandwidth is comparatively less, the ADC returns zero, which equates to negative infinity in dBm. This is expected behavior.\n\n----\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5830/5831/5832/5840/5841/5842/5860',
        },
        'included_in_proto': False,
        'is_error_handling': False,
        'method_name_for_documentation': 'read_power_spectrum',
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '_into',
                'session_filename': 'read_power_spectrum'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies which channels to apply settings. Specify an empty string as the value of this parameter.',
                },
                'is_repeated_capability': True,
                'repeated_capability_type': 'channels',
                'name': 'channelList',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies a pre-allocated numpy array to be filled with power spectrum data. The dtype of this array determines the data format: numpy.float64 or numpy.float32. Allocate an array at least as large as the number of spectral lines returned by the get_number_of_spectral_lines method.',
                },
                'name': 'powerSpectrumDataArray',
                'numpy': True,
                'type': 'ViReal64[]',
                'type_in_documentation': 'numpy.array of numpy.float64 or numpy.array of numpy.float32',
                'use_in_python_api': True
            },
            {
                'default_value': None,
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the expected number of spectral lines. If None, falls back to self.number_of_spectral_lines.',
                },
                'name': 'dataArraySize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'default_value': 'hightime.timedelta(seconds=10.0)',
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the time, in seconds, allotted for the function to complete before returning a timeout error. A value of specifies the function waits until all data is available.',
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'python_name': 'read_power_spectrum',
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'reset': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Resets all properties to default values, deletes all de-embedding tables, and stops the export of all external signals and events.\n\nFor the PXI-5600, this function does not reset the PXI Clock signal that is driven by devices installed in the Trigger Controller Slot, also known as the System Timing Slot.\n\nThis function resets all configured routes for the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842/5860 in NI-RFSA and NI-RFSG. To avoid resetting routes on the device that are in use by NI-RFSG sessions, NI recommends using the nirfsa_ResetWithOptions function, with **stepsToOmit** set to NIRFSA_VAL_RESET_WITH_OPTIONS_ROUTES.\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_\n\n`Events <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/events.html>`_',
        },
        'grpc_name': 'Reset',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
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
    'ResetDevice': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Performs a hard reset on the device.\n\nA hard reset consists of the following actions:\n\n- Signal acquisition is stopped.\n- All routes are released.\n- External bidirectional terminals are tristated.\n- FPGAs are reset.\n- Hardware is configured to its default state.\n- All session attributes are reset to their default states.\n\nDuring a device reset, routes of signals between this and other devices are released, regardless of which device created the route. For example, a trigger signal exported to a PXI trigger line that is used by another device is no longer exported.\n\nOn the PXI-5600, if you are driving the PXI_CLK10 line, you continue to drive the clock even after a device reset. To stop driving the PXI_CLK10 line, use the nirfsa_ConfigurePxiChassisClk10 function and set the **pxiClk10Source** parameter to NIRFSA_VAL_NONE or set the NIRFSA_ATTR_PXI_CHASSIS_CLK10_SOURCE attribute to NIRFSA_VAL_NONE.\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
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
    'ResetWithOptions': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Resets all properties to default values and specifies steps to omit during the reset process, such as signal routes.\n\nFor the PXI-5600, this function does not reset the PXI Clock signal that is driven by devices installed in the Star Trigger Controller Slot, also known as the System Timing Slot.\n\nBy default, this function resets all properties to their default values, deletes all de-embedding tables, aborts generation, clears all routes, and resets session properties to initial values. You can specify steps to omit using the steps to omit parameter. For example, if you specify NIRFSA_VAL_RESET_WITH_OPTIONS_ROUTES for the **NIRFSA_ATTR_STEPS_TO_OMIT** parameter, this function does not release signal routes during the reset process.\n\nWhen routes of signals between two devices are released, they are released regardless of which device created the route.\n\nTo avoid resetting routes on PXIe-5820/5830/5831/5832/5840/5841/5842/5860 that are in use by NI-RFSG sessions, NI recommends using this function instead of nirfsa_Reset, with **NIRFSA_ATTR_STEPS_TO_OMIT** set to NIRFSA_VAL_RESET_WITH_OPTIONS_ROUTES.\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_\n\n`Events <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/events.html>`_',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies a list of steps to skip during the reset process. The default value is NIRFSA_VAL_RESET_WITH_OPTIONS_NONE, which specifies that no step is omitted during reset.\n\nNote:NIRFSA_VAL_RESET_WITH_OPTIONS_ROUTES is not supported in external calibration or alignment sessions.\n\nNote:NIRFSA_VAL_RESET_WITH_OPTIONS_ROUTES is not supported for the PXI-5600/5661.',
                    'table_body': [
                        [
                            'ResetWithOptionsStepsToOmit.DEEMBEDDING_TABLES',
                            'Omits deleting de-embedding tables. This step is valid only for the PXIe-5830/5831/5832/5840.'
                        ],
                        [
                            'ResetWithOptionsStepsToOmit.NONE',
                            'No step is omitted during reset.'
                        ],
                        [
                            'ResetWithOptionsStepsToOmit.ROUTES',
                            'Omits the routing reset step. Routing is preserved after a reset. However, routing related properties are reset to default, and routing is released if the default properties are committed after a reset.'
                        ]
                    ],
                    'table_header': [
                        'Name',
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
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'SaveConfigurationsToFile': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nSaves the configurations of the session to the specified file.\n\n**Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842/5860',
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsa_Init function or the nirfsa_InitWithOptions function and identifies a particular instrument session.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the channel.',
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the absolute path of the file to which the NI-RFSA saves the configurations.',
                },
                'name': 'filePath',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'SelfCalibrateRange': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Self-calibrates all configurations within the specified frequency and reference level limits.\n\nSelf-calibration range data is valid until you restart the system or call the nirfsa_ClearSelfCalibrateRange function.\n\nNI recommends that no external signals are present on the RF In port while the calibration is taking place.\n\n----\n**Note**\nThis function does not update self-calibration date and temperature.\n\n----\n\nFor best results, NI recommends that you perform a complete self-calibration without omitting any steps. However, if certain aspects of performance are less important for your application, you can omit that step for faster execution.\n\n----\n**Note**\nIf there is an existing NI-RFSG session open for the same PXIe-5820/5830/5831/5832/5840/5841/5842/5860 while this function runs, it may remain open but cannot be used for operations that access the hardware, for example niRFSG Commit or niRFSG Initiate.\n\n----\n\n----\n**Note**\nIf there is an existing NI-RFSG session open for the same PXIe-5644/5645/5646, it may remain open but cannot be used while this function runs.\n\n----\n\n**Supported Devices**: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies which calibration steps to skip as part of the self-calibration process. A value of 0 specifies all supported calibration steps are performed.\n\n----\n\nTo omit two or more calibration steps, specify a bitwise-OR combination of the following constants. For example, if you wanted to omit NIRFSA_VAL_SELF_CAL_AMPLITUDE_ACCURACY and NIRFSA_VAL_SELF_CAL_LO_SELF_CAL, you would pass the following string to the nirfsa_SelfCalibrate function: NIRFSA_VAL_SELF_CAL_AMPLITUDE_ACCURACY | NIRFSA_VAL_SELF_CAL_LO_SELF_CAL\n\n----\n\n| Value                                          |  Description                                                                                                                                                                                                                     |\n|:------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|\n| NIRFSA_VAL_RESET_WITH_OPTIONS_NONE             | No step is omitted during self-calibration.                                                                                                                                                                           |\n| NIRFSA_VAL_SELF_CAL_PRESELECTOR_ALIGNMENT | Not used by this function.                                                                                                                                                                                            |\n| NIRFSA_VAL_SELF_CAL_GAIN_REFERENCE        | Not used by this function.                                                                                                                                                                                            |\n| NIRFSA_VAL_SELF_CAL_IF_FLATNESS           | Not used by this function.                                                                                                                                                                                            |\n| NIRFSA_VAL_SELF_CAL_DIGITIZER_SELF_CAL    | Not used by this function.                                                                                                                                                                                            |\n| NIRFSA_VAL_SELF_CAL_LO_SELF_CAL           | Omits the Local Oscillator (LO) Self Cal step. If you omit this step and the nirfsa_IsSelfCalValid function indicates the calibration data for this step is invalid, the LO phase-locked loop (PLL) may fail to lock. |\n| NIRFSA_VAL_SELF_CAL_AMPLITUDE_ACCURACY    | Omits the Amplitude Accuracy step. If you omit this step, the absolute accuracy of the device is not adjusted.                                                                                                        |\n| NIRFSA_VAL_SELF_CAL_RESIDUAL_LO_POWER     | Omits the Residual LO Power step. If you omit this step, the Residual LO Power performance is not adjusted.                                                                                                           |\n|NIRFSA_VAL_SELF_CAL_IMAGE_SUPPRESSION      | Omits the Image Suppression step. If you omit this step, the Residual Sideband Image Performance is not adjusted.                                                                                                     |\n| NIRFSA_VAL_SELF_CAL_SYNTHESIZER_ALIGNMENT | Omits the Synthesizer Alignment step. If you omit this step, the LO PLL is not adjusted. This step is not valid for the PXIe-5820.                                                                                    |\n| NIRFSA_VAL_SELF_CAL_DC_OFFSET             | Omits the DC Offset step. This step applies only to the PXIe-5820.                                                                                                                                                    |',
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
                    'description': 'Specifies the minimum RF frequency in Hz.',
                },
                'grpc_name': 'min_frequency',
                'name': 'minimumFrequency',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the maximum RF frequency in Hz.',
                },
                'grpc_name': 'max_frequency',
                'name': 'maximumFrequency',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the minimum reference level in dBm.',
                },
                'grpc_name': 'min_reference_level',
                'name': 'minimumReferenceLevel',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the maximum reference level in dBm.',
                },
                'grpc_name': 'max_reference_level',
                'name': 'maximumReferenceLevel',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'SendSoftwareEdgeTrigger': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Sends a trigger to the device when you use a software version of a supported trigger and the device is waiting for the trigger to be sent.\n\nYou can also use this function to override a hardware trigger.\n\nThis function returns an error in the following situations:\n\n- You configure an invalid trigger.\n- You set the **acquisitionType** to NIRFSA_VAL_SPECTRUM using the nirfsa_ConfigureAcquisitionType function.\n- You have not previously called the nirfsa_Initiate function.\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Software Trigger <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/software-edge-trigger.html>`_\n\n`Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the trigger to send.\n\n**Default Value:** NIRFSA_VAL_START_TRIGGER\n\n**Defined Values:**',
                    'table_body': [
                        [
                            'NIRFSA_VAL_START_TRIGGER',
                            'Specifies the Start Trigger.'
                        ],
                        [
                            'NIRFSA_VAL_SCRIPT_TRIGGER',
                            'Specifies the Script Trigger.'
                        ]
                    ],
                    'table_header': [
                        'Name',
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
                    'description': 'Specifies a particular instance of a trigger. NI-RFSA does not currently support this parameter.',
                },
                'default_value': '""',
                'name': 'triggerIdentifier',
                'type': 'ViConstString',
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
            'description': 'Sets the value of a ViBoolean attribute.\n\nUse this low-level function to set the values of inherent IVI attributes and instrument-specific attributes.\n\nNI-RFSA contains high-level functions that set most of the instrument attributes. NI recommends you use the high-level functions as much as possible. High-level functions handle order dependencies and multithread locking for you.\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the channel on which to check the attribute value if the attribute is channel based. If the attribute is not channel based, set this parameter to "" (empty string) or VI_NULL.',
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.',
                },
                'name': 'attributeId',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value to which you want to set the attribute.\n\n----\n\nSome of the values might not be valid depending on the current state of the instrument session.\n\n----',
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
            'description': 'Sets the value of a ViInt32 attribute.\n\nUse this low-level function to set the values of inherent IVI attributes and instrument-specific attributes.\n\nNI-RFSA contains high-level functions that set most of the instrument attributes. NI recommends you use the high-level functions as much as possible. High-level functions handle order dependencies and multithread locking for you.\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the channel on which to check the attribute value if the attribute is channel-based. If the attribute is not channel based, set this parameter to "" (empty string) or VI_NULL.',
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.',
                },
                'name': 'attributeId',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value to which you want to set the attribute.\n\n----\n\nSome of the values might not be valid depending on the current state of the instrument session.\n\n----',
                },
                'grpc_enum': 'NiRFSAInt32AttributeValues',
                'grpc_mapped_enum': 'NiRFSAInt32AttributeValuesMapped',
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
            'description': 'Sets the value of a ViInt64 attribute.\n\nUse this low-level function to set the values of inherent IVI attributes and instrument-specific attributes.\n\nNI-RFSA contains high-level functions that set most of the instrument attributes. NI recommends you use the high-level functions as much as possible. High-level functions handle order dependencies and multithread locking for you.\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the channel on which to check the attribute value if the attribute is channel based. If the attribute is not channel based, set this parameter to "" (empty string) or VI_NULL.',
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.',
                },
                'name': 'attributeId',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value to which you want to set the attribute.\n\n----\n\nSome of the values might not be valid depending on the current state of the instrument session.\n\n----',
                },
                'grpc_name': 'value_raw',
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
            'description': 'Sets the value of a ViReal64 attribute.\n\nUse this low-level function to set the values of inherent IVI attributes, and instrument-specific attributes.\n\nNI-RFSA contains high-level functions that set most of the instrument attributes. NI recommends you use the high-level functions as much as possible. High-level functions handle order dependencies and multithread-locking for you.\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the channel on which to check the attribute value if the attribute is channel based. If the attribute is not channel based, set this parameter to "" (empty string) or VI_NULL.',
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.',
                },
                'name': 'attributeId',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value to which you want to set the attribute.\n\n----\n\nSome of the values might not be valid depending on the current state of the instrument session.\n\n----',
                },
                'grpc_enum': 'NiRFSAReal64AttributeValues',
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
            'description': 'Sets the value of a ViSession attribute.\n\nUse this low-level function to set the values of inherent IVI attributes and instrument-specific attributes.\n\nNI-RFSA contains high-level functions that set most of the instrument attributes. NI recommends you use the high-level functions as much as possible. High-level functions handle order dependencies and multithread locking for you.\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the channel on which to check the attribute value if the attribute is channel based. If the attribute is not channel based, set this parameter to "" (empty string) or VI_NULL.',
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.',
                },
                'name': 'attributeId',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value to which you want to set the attribute.\n\n----\n\nSome of the values might not be valid depending on the current state of the instrument session.\n\n----',
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
            'description': 'Sets the value of a ViString attribute.\n\nUse this low-level function to set the values of inherent IVI attributes and instrument-specific attributes.\n\nNI-RFSA contains high-level functions that set most of the instrument attributes. NI recommends you use the high-level functions as much as possible. High-level functions handle order dependencies and multithread locking for you.\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the channel on which to check the attribute value if the attribute is channel based. If the attribute is not channel based, set this parameter to "" (empty string) or VI_NULL.',
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.',
                },
                'name': 'attributeId',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value to which you want to set the attribute.\n\n----\n\nSome of the values might not be valid depending on the current state of the instrument session.\n\n----',
                },
                'grpc_mapped_enum': 'NiRFSAStringAttributeValuesMapped',
                'name': 'value',
                'type': 'ViConstString',
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
            'description': 'Releases a lock obtained on an NI-RFSA device session by calling the nirfsa_LockSession function.\n\nRefer to the nirfsa_LockSession function for additional information on session locks.\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698',
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
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.',
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Keeps track of whether you obtain a lock and therefore need to unlock the session in complex functions. Pass the address of a local ViBoolean variable. In the declaration of the local variable, initialize it to VI_FALSE. Pass the address of the same local variable to any other calls you make to this function or the nirfsa_UnlockSession function in the same function.\n\nThis parameter serves as a convenience. If you do not want to use this parameter, pass VI_NULL.\n\nThe nirfsa_LockSession function and the nirfsa_UnlockSession function each inspect the current value and take the actions shown in the following table.\n\n| Function             | Boolean Value | Action                                                                                               |\n|:---------------------|:--------------|:-----------------------------------------------------------------------------------------------------|\n| nirfsa_LockSession   | VI_TRUE       | The nirfsa_LockSession function does not lock the session again.                                     |\n|                      | VI_FALSE      | The nirfsa_LockSession function obtains the lock and sets the value of the parameter to VI_TRUE.     |\n| nirfsa_UnlockSession | VI_FALSE      | The nirfsa_UnlockSession function does not attempt to unlock the session.                            |\n|                      | VI_TRUE       | The nirfsa_UnlockSession function releases the lock and sets the value of the parameter to VI_FALSE. |\n\nThus, you can call the nirfsa_UnlockSession function at the end of your function regardless of whether you actually have the lock.',
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
    'fancy_self_test': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': '\nPerforms a self-test on the NI-RFSA device and returns the test results.\n\nThis function performs a simple series of tests to ensure that the NI-RFSA device is powered up and responding.\n\nThis function does not affect external I/O connections or connections between devices. Complete functional testing and calibration are not performed by this function. The NI-RFSA device must be in the Configuration state before you call this function.\n\n**Supported Devices** : PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Device Warm-Up <https://www.ni.com/docs/en-US/bundle/rfsa/page/rfsa/warmup.html>`_',
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
        'grpc_name': 'FancySelfTest',
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsa_Init function or the nirfsa_InitWithOptions function and identifies a particular instrument session.',
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
            'description': 'Performs a self-test on the NI-RFSA device and returns the test results.\n\nThis function performs a simple series of tests to ensure that the NI-RFSA device is powered up and responding.\n\nThis function does not affect external I/O connections or connections between devices. Complete functional testing and calibration are not performed by this function. The NI-RFSA device must be in the Configuration state before you call this function.\n\n**Supported Devices** : PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Device Warm-Up <https://www.ni.com/docs/en-US/bundle/rfsa/page/rfsa/warmup.html>`_',
        },
        'grpc_name': 'SelfTest',
        'included_in_proto': True,
        'method_name_for_documentation': 'self_test',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsa_Init function or the nirfsa_InitWithOptions function and identifies a particular instrument session.',
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'This parameter contains the value returned from the NI-RFSA device self test.',
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
                'grpc_name': 'test_result',
                'name': 'selfTestResult',
                'type': 'ViInt16'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the self-test response string from the NI-RFSA device. For an explanation of the string contents, refer to the **status** parameter of this function.\n\nYou must pass a ViChar array with at least 256 bytes.',
                },
                'grpc_name': 'test_message',
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
}
