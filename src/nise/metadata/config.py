# -*- coding: utf-8 -*-
# This file is generated from NI Switch Executive API metadata version 21.0.0d0
config = {
    'api_version': '21.0.0d0',
    'c_function_prefix': 'niSE_',
    'close_function': 'CloseSession',
    'context_manager_name': {
    },
    'custom_types': [
    ],
    'driver_name': 'NI Switch Executive',
    'driver_registry': 'Switch Executive',
    'extra_errors_used': [
        'InvalidRepeatedCapabilityError'
    ],
    'init_function': 'OpenSession',
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'nise',
                'type': 'cdll'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'nise.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'nise.dll',
                'type': 'cdll'
            }
        }
    },
    'metadata_version': '2.0',
    'module_name': 'nise',
    'repeated_capabilities': [
    ],
    'session_class_description': 'An NI Switch Executive session',
    'session_handle_parameter_name': 'vi',
    'use_locking': False
}
