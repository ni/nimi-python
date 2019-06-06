# -*- coding: utf-8 -*-
# This file is generated from API metadata for NI-Digital Pattern Driver version 19.0.0d32
config = {
    'c_function_prefix': 'niDigital_',
    'close_function': 'Close',
    'context_manager_name': {
        'abort_function': 'Abort',
        'initiate_function': 'Initiate',
        'task': 'acquisition'
    },
    'custom_types': [
    ],
    'driver_name': 'NI-Digital Pattern Driver',
    'enum_whitelist_suffix': [
    ],
    'init_function': 'InitWithOptions',
    'api_version': '19.0.0d32',
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'libnidigital.so',
                'type': 'cdll'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'nidigital_32.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'nidigital_64.dll',
                'type': 'cdll'
            }
        }
    },
    'metadata_version': '2.0',
    'module_name': 'nidigital',
    'repeated_capabilities': [
        {
            'prefix': '',
            'python_name': 'channels'
        }
    ],
    'session_class_description': 'An NI-Digital session',
    'session_handle_parameter_name': 'vi'
}
