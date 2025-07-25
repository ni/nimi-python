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
    'enum_whitelist_prefix': [
        'RANGE_',
        'CLOCK_RATE_'
    ],
    'enum_whitelist_suffix': [
        '_HERTZ',
        '_KILOHERTZ',
        '_MEGAHERTZ',
        '_GIGAHERTZ',
        '_TOWARDS_DUT'
    ],
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
            'python_name': 'waveforms'
        },
        {
            'prefix': '',
            'python_name': 'ports'
        },
        {
            'prefix': 'LO',
            'python_name': 'los'
        },
        {
            'prefix': '',
            'python_name': 'device_temperatures'
        },
        {
            'prefix': '',
            'python_name': 'channels'
        }
    ],
    'session_class_description': 'An NI-RFSG session to the NI-RFSG driver',
    'session_handle_parameter_name': 'vi',
    'uses_nitclk': True
}
