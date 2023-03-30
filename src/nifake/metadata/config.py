# -*- coding: utf-8 -*-
# This file is generated from NI-FAKE API metadata version 23.5.0d4
config = {
    'api_version': '23.5.0d4',
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
            'grpc_name': 'FakeCustomStruct',
            'python_name': 'CustomStruct'
        },
        {
            'ctypes_type': 'struct_CustomStructNestedTypedef',
            'file_name': 'custom_struct_nested_typedef',
            'grpc_name': 'CustomStructNestedTypedef',
            'python_name': 'CustomStructNestedTypedef'
        },
        {
            'ctypes_type': 'struct_CustomStructTypedef',
            'file_name': 'custom_struct_typedef',
            'grpc_name': 'CustomStructTypedef',
            'python_name': 'CustomStructTypedef'
        }
    ],
    'driver_name': 'NI-FAKE',
    'enum_whitelist_suffix': [
        '_POINT_FIVE'
    ],
    'extra_errors_used': [
        'InvalidRepeatedCapabilityError',
        'SelfTestError'
    ],
    'grpc_service_class_prefix': 'NiFake',
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
