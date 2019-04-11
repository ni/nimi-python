# -*- coding: utf-8 -*-
# This file is generated from API metadata for NI-SWITCH version 19.1.0d0
config = {
    'c_function_prefix': 'niSwitch_',
    'close_function': 'Close',
    'context_manager_name': {
        'abort_function': 'AbortScan',
        'initiate_function': 'InitiateScan',
        'task': 'scan'
    },
    'custom_types': [
    ],
    'driver_name': 'NI-SWITCH',
    'init_function': 'InitWithTopology',
    'last_tested_version': '19.1.0d0',
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'libniswitch.so',
                'type': 'cdll'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'niswitch_32.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'niswitch_64.dll',
                'type': 'cdll'
            }
        }
    },
    'metadata_version': '2.0',
    'module_name': 'niswitch',
    'repeated_capabilities': [
        {
            'prefix': '',
            'python_name': 'channels'
        }
    ],
    'session_class_description': 'An NI-SWITCH session to a National Instruments Switch Module',
    'session_handle_parameter_name': 'vi'
}
