# -*- coding: utf-8 -*-
# This file is generated from API metadata for NI-ModInst version 255.0.0d4
config = {
    'c_function_prefix': 'niModInst_',
    'close_function': 'CloseInstalledDevicesSession',
    'custom_types': [
    ],
    'driver_name': 'NI-ModInst',
    'init_function': 'OpenInstalledDevicesSession',
    'last_tested_version': '255.0.0d4',
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'libnimodinst.so',
                'type': 'cdll'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'nimodinst.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'nimodinst_64.dll',
                'type': 'cdll'
            }
        }
    },
    'metadata_version': '2.0',
    'module_name': 'nimodinst',
    'repeated_capabilities': [
    ],
    'session_class_description': 'A NI-ModInst session to get device information',
    'session_handle_parameter_name': 'handle'
}
