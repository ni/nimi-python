# -*- coding: utf-8 -*-
# This file is generated from API metadata for NI-DCPower version 19.1.0d33
config = {
    'c_function_prefix': 'niDCPower_',
    'close_function': 'Close',
    'context_manager_name': {
        'abort_function': 'Abort',
        'initiate_function': 'Initiate',
        'task': 'acquisition'
    },
    'custom_types': [
    ],
    'driver_name': 'NI-DCPower',
    'init_function': 'InitializeWithChannels',
    'api_version': '19.1.0d33',
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'libnidcpower.so',
                'type': 'cdll'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'nidcpower_32.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'nidcpower_64.dll',
                'type': 'cdll'
            }
        }
    },
    'metadata_version': '2.0',
    'module_name': 'nidcpower',
    'repeated_capabilities': [
        {
            'prefix': '',
            'python_name': 'channels'
        }
    ],
    'session_class_description': 'An NI-DCPower session to a National Instruments Programmable Power Supply or Source Measure Unit.',
    'session_handle_parameter_name': 'vi'
}
