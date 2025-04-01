# -*- coding: utf-8 -*-
# This file is generated from NI-RFSG API metadata version 25.5.0d9999
config = {
    'api_version': '25.5.0d9999',
    'c_function_prefix': 'niRFSG_',
    'close_function': 'close',
    'context_manager_name': {
        'abort_function': 'Abort',
        'initiate_function': 'Initiate',
        'task': 'generation'
    },
    'custom_types': [
    ],
    'driver_name': 'NI-RFSG',
    'enum_whitelist_suffix': [
        '_POINT_FIVE'
    ],
    'extra_errors_used': [
        'InvalidRepeatedCapabilityError',
        'SelfTestError'
    ],
    'grpc_service_class_prefix': 'NiRFSG',
    'init_function': 'InitWithOptions',
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'nirfsg',
                'type': 'cdll'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'niRFSG.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'niRFSG_64.dll',
                'type': 'cdll'
            }
        }
    },
    'module_name': 'nirfsg',
    'repeated_capabilities': [
        {
            'prefix': 'marker',
            'python_name': 'markers'
        },
        {
            'prefix': 'scripttrigger',
            'python_name': 'script_triggers'
        },
        {
            'prefix': 'waveform::',
            'python_name': 'waveform'
        },
        {
            'prefix': '',
            'python_name': 'deembedding_port'
        }
    ],
    'session_class_description': 'An NI-RFSG session to the RFSG driver',
    'session_handle_parameter_name': 'vi',
    'uses_nitclk': True
}
