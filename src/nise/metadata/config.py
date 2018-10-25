config = {
    'metadata_version': '0.1',
    'module_name': 'nise',
    'module_version': '0.2.0.dev0',
    'c_function_prefix': 'niSE_',
    'driver_name': 'NI Switch Executive',
    'driver_registry': 'Switch Executive',
    'session_class_description': 'An NI Switch Executive session',
    'session_handle_parameter_name': 'vi',
    'library_info':
    {
        'Windows': {
            '32bit': {'name': 'nise.dll', 'type': 'windll'},
            '64bit': {'name': 'nise.dll', 'type': 'cdll'},
        },
        'Linux': {
            '64bit': {'name': 'libnise.so', 'type': 'cdll'},
        },
    },
    'context_manager_name': {},
    'init_function': 'OpenSession',
    'close_function': 'CloseSession',
    'driver_urls': {
        'REPLACE_DRIVER_SPECIFIC_URL_1': 'http://zone.ni.com/reference/en-XX/help/370404J-01/',
    },
    'custom_types': [],
    'last_tested_version': '18.0.0',
    'repeated_capabilities': [],
}


