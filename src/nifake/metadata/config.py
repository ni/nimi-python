# -*- coding: utf-8 -*-
# This file is generated from NI-FAKE API metadata version 22.5.0d9999
config = {
    'api_version': '22.5.0d9999',
    'c_function_prefix': 'niFake_',
    'close_function': 'close',
    'context_manager_name': {
        'abort_function': 'Abort',
        'initiate_function': 'Initiate',
        'task': 'acquisition'
    },
    'custom_types': [
        {
            'ctypes_type': 'struct_CustomStruct',
            'file_name': 'custom_struct',
            'python_name': 'CustomStruct'
        },
        {
            'ctypes_type': 'struct_CustomStructNestedTypedef',
            'file_name': 'custom_struct_nested_typedef',
            'python_name': 'CustomStructNestedTypedef'
        },
        {
            'ctypes_type': 'struct_CustomStructTypedef',
            'file_name': 'custom_struct_typedef',
            'python_name': 'CustomStructTypedef'
        }
    ],
    'driver_name': 'NI-FAKE',
    'enum_whitelist_suffix': [
        '_POINT_FIVE'
    ],
    'extra_errors_used': [
        'InvalidRepeatedCapabilityError',
        'SelfTestError',
        'DriverTooNewError'
    ],
    'init_function': 'InitWithOptions',
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'nifake',
                'type': 'cdll'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'nifake_32.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'nifake_64.dll',
                'type': 'cdll'
            }
        }
    },
    'metadata_version': '2.0',
    'module_name': 'nifake',
    'repeated_capabilities': [
        {
            'prefix': '',
            'python_name': 'channels'
        },
        {
            'prefix': 'site',
            'python_name': 'sites'
        },
        {
            'prefix': '',
            'python_name': 'instruments'
        }
    ],
    'session_class_description': 'An NI-FAKE session to a fake MI driver whose sole purpose is to test nimi-python code generation',
    'session_handle_parameter_name': 'vi',
    'uses_nitclk': True
}
