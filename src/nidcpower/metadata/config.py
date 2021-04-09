# -*- coding: utf-8 -*-
# This file is generated from NI-DCPower API metadata version 21.0.0d48
config = {
    'api_version': '21.0.0d48',
    'c_function_prefix': 'niDCPower_',
    'close_function': 'close',
    'context_manager_name': {
        'abort_function': 'AbortWithChannels',
        'initiate_function': 'InitiateWithChannels',
        'task': 'acquisition'
    },
    'custom_types': [
    ],
    'driver_name': 'NI-DCPower',
    'extra_errors_used': [
        'InvalidRepeatedCapabilityError',
        'SelfTestError'
    ],
    'init_function': 'InitializeWithChannels',
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'nidcpower',
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
    'session_handle_parameter_name': 'vi',
    'uses_nitclk': False
}
