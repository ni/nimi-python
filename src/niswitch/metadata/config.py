# -*- coding: utf-8 -*-
# This file is generated from NI-SWITCH API metadata version 23.0.0d75
config = {
    'api_version': '23.0.0d75',
    'c_function_prefix': 'niSwitch_',
    'close_function': 'close',
    'context_manager_name': {
        'abort_function': 'AbortScan',
        'initiate_function': 'InitiateScan',
        'task': 'scan'
    },
    'custom_types': [
    ],
    'driver_name': 'NI-SWITCH',
    'extra_errors_used': [
        'InvalidRepeatedCapabilityError',
        'SelfTestError'
    ],
    'grpc_service_class_prefix': 'NiSwitch',
    'init_function': 'InitWithTopology',
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'niswitch',
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
    'module_name': 'niswitch',
    'repeated_capabilities': [
        {
            'prefix': '',
            'python_name': 'channels'
        }
    ],
    'session_class_description': 'An NI-SWITCH session to an NI switch module.',
    'session_handle_parameter_name': 'vi'
}
