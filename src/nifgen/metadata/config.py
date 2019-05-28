# -*- coding: utf-8 -*-
# This file is generated from API metadata for NI-FGEN version 19.1.0d0
config = {
    'c_function_prefix': 'niFgen_',
    'close_function': 'Close',
    'context_manager_name': {
        'abort_function': 'AbortGeneration',
        'initiate_function': 'InitiateGeneration',
        'task': 'generation'
    },
    'custom_types': [
    ],
    'driver_name': 'NI-FGEN',
    'init_function': 'InitializeWithChannels',
    'api_version': '19.1.0d0',
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'libfgen.so',
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
    'session_handle_parameter_name': 'vi'
}
