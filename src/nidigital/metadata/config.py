# -*- coding: utf-8 -*-
# This file is generated from NI-Digital Pattern Driver API metadata version 19.0.0a0
config = {
    'api_version': '19.0.0a0',
    'c_function_prefix': 'niDigital_',
    'close_function': 'close',
    'context_manager_name': {
        'abort_function': 'Abort',
        'initiate_function': 'Initiate',
        'task': 'burst'
    },
    'custom_types': [
    ],
    'driver_name': 'NI-Digital Pattern Driver',
    'enum_whitelist_suffix': [
    ],
    'init_function': 'InitWithOptions',
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'nidigital',
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
        },
        {
            'prefix': '',
            'python_name': 'pins',
        },
        # These need to be added here since merging 'repeated_capabilities' with something
        # here and something in config_addons.py doesn't work
        {
            'prefix': 'conditionalJumpTrigger',
            'python_name': 'conditional_jump_triggers',
        },
        {
            'prefix': 'patternOpcodeEvent',
            'python_name': 'pattern_opcode_events',
        },
    ],
    'session_class_description': 'An NI-Digital session',
    'session_handle_parameter_name': 'vi',
    'supports_nitclk': True,
}
