# -*- coding: utf-8 -*-
# This file is generated from NI-FGEN API metadata version 24.5.0d38
config = {
    'api_version': '24.5.0d38',
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
    'extra_errors_used': [
        'InvalidRepeatedCapabilityError',
        'SelfTestError'
    ],
    'grpc_service_class_prefix': 'NiFgen',
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
                'name': 'niFgen_32.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'niFgen_64.dll',
                'type': 'cdll'
            }
        }
    },
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
        },
        {
            'prefix': 'DataMarker',
            'python_name': 'data_markers'
        }
    ],
    'session_class_description': 'An NI-FGEN session to an NI signal generator.',
    'session_handle_parameter_name': 'vi',
    'uses_nitclk': True
}
