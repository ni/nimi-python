# -*- coding: utf-8 -*-
# This file is generated from NI-Digital Pattern Driver API metadata version 22.0.0d53
config = {
    'api_version': '22.0.0d53',
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
    'extra_errors_used': [
        'InvalidRepeatedCapabilityError',
        'SelfTestError'
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
                'name': 'niDigital_32.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'niDigital_64.dll',
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
            'python_name': 'pins'
        },
        {
            'prefix': '',
            'python_name': 'instruments'
        },
        {
            'prefix': 'patternOpcodeEvent',
            'python_name': 'pattern_opcode_events'
        },
        {
            'prefix': 'conditionalJumpTrigger',
            'python_name': 'conditional_jump_triggers'
        },
        {
            'prefix': 'site',
            'python_name': 'sites'
        },
        {
            'prefix': 'RIOEvent',
            'python_name': 'rio_events'
        },
        {
            'prefix': 'RIOTrigger',
            'python_name': 'rio_triggers'
        }
    ],
    'session_class_description': 'An NI-Digital Pattern Driver session',
    'session_handle_parameter_name': 'vi',
    'uses_nitclk': True
}
