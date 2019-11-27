# -*- coding: utf-8 -*-
# This file is generated from NI-FGEN API metadata version 19.6.0d4
config = {
    'api_version': '19.6.0d4',
    'c_function_prefix': 'niFgen_',
    'close_function': 'close',
    'context_manager_name': {
        'abort_function': 'AbortGeneration',
        'initiate_function': 'InitiateGeneration',
        'task': 'generation'
    },
    'custom_types': [
    ],
    'driver_name': 'NI-FGEN',
    'init_function': 'InitializeWithChannels',
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'nifgen',
                'type': 'cdll'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'nifgen_32.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'nifgen_64.dll',
                'type': 'cdll'
            }
        }
    },
    'metadata_version': '2.0',
    'module_name': 'nifgen',
    'repeated_capabilities': [
        {
            'prefix': '',
            'python_name': 'channels'
        },
        {
            'prefix': 'ScriptTrigger',
            'python_name': 'script_triggers'
        },
        {
            'prefix': 'Marker',
            'python_name': 'markers'
        }
    ],
    'session_class_description': 'An NI-FGEN session to a National Instruments Signal Generator.',
    'session_handle_parameter_name': 'vi',
    'supports_nitclk': True
}
