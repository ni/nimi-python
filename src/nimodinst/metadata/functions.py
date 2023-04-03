# -*- coding: utf-8 -*-
# This file is generated from NI-ModInst API metadata version 23.0.0d6
functions = {
    'CloseInstalledDevicesSession': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nCleans up the NI-ModInst session created by a call to\nniModInst_OpenInstalledDevicesSession. Call this function when you are\nfinished using the session handle and do not use this handle again.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe NI-ModInst session handle created by\nniModInst_OpenInstalledDevicesSession.\n'
                },
                'name': 'handle',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetExtendedErrorInfo': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nReturns detailed information about the last error that occurred in the\ncurrent thread during a call to one of the NI-ModInst functions. When\none of the other functions returns a negative value as its return value,\nimmediately call this function to get detailed information about the\nerror. Because error information is stored on a thread-by-thread basis,\nbe sure to call this function in the same thread that called the\nfunction that returned an error. The extended error information is\nreturned as a string. To find out the length of the error information\nstring before you allocate a buffer for it, call this function and pass\n0 as the errorInfoBufferSize parameter or NULL as the errorInfo\nparameter. When you do this, the function returns the size of the buffer\nrequired to hold the error information string as its return value. You\ncan then allocate an appropriately sized string character buffer and\ncall this function again.\n'
        },
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
                    'description': '\nThe size of the buffer allocated and passed in as the errorInfo\nparameter. The buffer should be large enough to hold the errorInfo\nstring (including a NULL terminating character). The size of the buffer\nallocated and passed in as the errorInfo parameter. The buffer should be\nlarge enough to hold the errorInfo string (including a NULL terminating\ncharacter). Refer to the function help to find out how to determine the\nexact buffer size required.\n'
                },
                'name': 'errorInfoBufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The character buffer into which the error information string is copied.'
                },
                'name': 'errorInfo',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'errorInfoBufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetInstalledDeviceAttributeViInt32': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nReturns an integer attribute specified by the attributeID parameter for\na device specified by the handle and index parameters. The handle\nparameter is expected to be a valid handle returned by\nniModInst_OpenInstalledDevicesSession. It therefore acts as a handle to\na list of installed devices. The index parameter specifies the device in\nthe list for which you want the attribute.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe NI-ModInst session handle created by\nniModInst_OpenInstalledDevicesSession.\n'
                },
                'name': 'handle',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA zero-based index that specifies the device for which you want the\nattribute. This index parameter should be between 0 and (deviceCount -\n1), inclusive, where deviceCount is the number of installed devices\nreturned by niModInst_OpenInstalledDevicesSession.\n'
                },
                'name': 'index',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe ID of the integer attribute you want to query. Valid Values Slot\nNumber--the slot (for example, in a PXI chassis) in which the device is\ninstalled. This attribute can only be queried for PXI devices installed\nin a chassis that has been properly identified in MAX. Chassis\nNumber--the number of the chassis in which the device is installed. This\nattribute can only be queried for PXI devices installed in a chassis\nthat has been properly identified in MAX. Bus Number--the bus on which\nthe device has been enumerated. Socket Number--the socket number on\nwhich the device has been enumerated. Notes The bus number and socket\nnumber can be used to form a VISA resource string for this device, of\nthe form "PXI::::INSTR". Traditional NI-DAQ devices do not support the\nchassis number, bus number, and socket number attributes.\n'
                },
                'name': 'attributeId',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nA pointer to a signed 32-bit integer variable that receives the value of\nthe requested attribute.\n'
                },
                'name': 'attributeValue',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetInstalledDeviceAttributeViString': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nReturns a string attribute specified by the attributeID parameter for a\ndevice specified by the handle and index parameters. The handle\nparameter is expected to be a valid handle returned by\nniModInst_OpenInstalledDevicesSession. Therefore, it acts as a handle\nto a list of installed devices. The index parameter specifies for which\ndevice in the list you want the attribute. To find out the length of the\ndevice name string before you allocate a buffer for it, simply call this\nfunction and pass 0 as the attributeValueBufferSize parameter or NULL as\nthe attributeValue parameter. When you do this, the function returns the\nsize of the buffer required to hold the attribute value string as its\nreturn value. You can then allocate an appropriately sized character\nbuffer and call this function again.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe NI-ModInst session handle created by\nniModInst_OpenInstalledDevicesSession.\n'
                },
                'name': 'handle',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA zero-based index that specifies the device for which you want the\nattribute. This index parameter should be between 0 and (deviceCount -\n1), inclusive, where deviceCount is the number of installed devices\nreturned by niModInst_OpenInstalledDevicesSession.\n'
                },
                'name': 'index',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe ID of the string attribute you want to query. Valid Values\nNIMODINST_ATTR_DEVICE_NAME--the name of the device, which can be used\nto open an instrument driver session for that device\nNIMODINST_ATTR_DEVICE_MODEL--the model of the device (for example, NI\nPXI-5122) NIMODINST_ATTR_SERIAL_NUMBER--the serial number of the\ndevice\n'
                },
                'name': 'attributeId',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe size of the buffer allocated and passed in as the attributeValue\nparameter. The buffer should be large enough to hold the attribute value\nstring (including a NULL terminating character). Refer to the\nDescription section for information on how to determine the exact buffer\nsize required.\n'
                },
                'name': 'attributeValueBufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The character buffer into which the attribute value string is copied.'
                },
                'name': 'attributeValue',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'attributeValueBufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'OpenInstalledDevicesSession': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nCreates a handle to a list of installed devices supported by the\nspecified driver. Call this function and pass in the name of an NI \ninstrument driver, such as "NI-SCOPE". This function\nsearches the system and constructs a list of all the installed devices\nthat are supported by that driver, and then returns both a handle to\nthis list and the number of devices found. The handle is used with other\nfunctions to query for attributes such as device name and model, and to\nsafely discard the list when finished. Note This handle reflects the\nsystem state when the handle is created (that is, when you call this\nfunction. If you remove devices from the system or rename them in\nMeasurement & Automation Explorer (MAX), this handle may not refer to an\naccurate list of devices. You should destroy the handle using\nniModInst_CloseInstalledDevicesSession and create a new handle using\nthis function.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA string specifying the driver whose supported devices you want to find.\nThis string is not case-sensitive. Some examples are: NI-SCOPE niScope\nNI-FGEN niFgen NI-HSDIO niHSDIO NI-DMM niDMM NI-SWITCH niSwitch Note If\nyou use the empty string for this parameter, NI-ModInst creates a list\nof all Modular Instruments devices installed in the system.\n'
                },
                'name': 'driver',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nA pointer to a ViSession variable that receives the value of the\nNI-ModInst session handle. This value acts as a handle to the list of\ninstalled devices and is used in other NI-ModInst functions.\n'
                },
                'name': 'handle',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nA pointer to an integer variable that receives the number of devices\nfound in the system that are supported by the driver specified in the\ndriver parameter.\n'
                },
                'name': 'deviceCount',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    }
}
