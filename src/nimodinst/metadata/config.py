config = {
    'metadata_version': '1.0',
    'module_name': 'nimodinst',
    'module_version': '0.8.0',
    'c_function_prefix': 'niModInst_',
    'driver_name': 'NI-ModInst',
    'session_class_description': 'A NI-ModInst session to get device information',
    'session_handle_parameter_name': 'handle',
    'library_info':
    {
        'Windows': {
            '32bit': {'name': 'nimodinst.dll', 'type': 'windll'},
            '64bit': {'name': 'nimodinst_64.dll', 'type': 'cdll'},
        },
        'Linux': {
            '64bit': {'name': 'libnimodinst.so', 'type': 'cdll'},
        },
    },
    'custom_types': [],
    'last_tested_version': '17.0.0',
    'repeated_capabilities': [],
    'use_session_lock': False,
    'init_function': 'OpenInstalledDevicesSession',
}

