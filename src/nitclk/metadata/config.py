# -*- coding: utf-8 -*-
# This file is generated from NI-TClk API metadata version 255.0.0d0
config = {
    'api_version': '255.0.0d0',
    'c_function_prefix': 'niTClk_',
    'close_function': None,
    'context_manager_name': {
        'abort_function': None,
        'initiate_function': 'Initiate',
        'task': 'acquisition'
    },
    'custom_types': [
    ],
    'driver_name': 'NI-TClk',
    'init_function': 'InitForDocumentation',
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'libnitclk.so',
                'type': 'cdll'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'nitclk.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'nitclk_64.dll',
                'type': 'cdll'
            }
        }
    },
    'metadata_version': '2.0',
    'module_name': 'nitclk',
    'repeated_capabilities': [
    ],
    'session_class_description': 'An NI-TClk session.',
    'session_handle_parameter_name': 'sessions'
}
