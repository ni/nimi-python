# -*- coding: utf-8 -*-
# This file is generated from NI-ModInst API metadata version 23.0.0d6
config = {
    'api_version': '23.0.0d6',
    'c_function_prefix': 'niModInst_',
    'close_function': 'CloseInstalledDevicesSession',
    'context_manager_name': {
    },
    'custom_types': [
    ],
    'driver_name': 'NI-ModInst',
    'extra_errors_used': [
    ],
    'grpc_service_class_prefix': 'NiModInst',
    'init_function': 'OpenInstalledDevicesSession',
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'nimodinst',
                'type': 'cdll'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'niModInst.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'niModInst_64.dll',
                'type': 'cdll'
            }
        }
    },
    'module_name': 'nimodinst',
    'repeated_capabilities': [
    ],
    'session_class_description': 'A NI-ModInst session to get device information',
    'session_handle_parameter_name': 'handle'
}
