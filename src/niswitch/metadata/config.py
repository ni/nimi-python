config = {
    'metadata_version': '1.0',
    'module_name': 'niswitch',
    'module_version': '1.0.1.dev0',
    'c_function_prefix': 'niSwitch_',
    'driver_name': 'NI-SWITCH',
    'session_class_description': 'An NI-SWITCH session to a National Instruments Switch Module',
    'session_handle_parameter_name': 'vi',
    'library_info':
    {
        'Windows': {
            '32bit': {'name': 'niswitch_32.dll', 'type': 'windll'},
            '64bit': {'name': 'niswitch_64.dll', 'type': 'cdll'},
        },
        'Linux': {
            '64bit': {'name': 'libniswitch.so', 'type': 'cdll'},
        },
    },
    'context_manager_name': {
        'task': 'scan',
        'initiate_function': 'InitiateScan',
        'abort_function': 'AbortScan',
    },
    'init_function': 'InitWithTopology',
    'custom_types': [],
    'last_tested_version': '17.0.0',
    'repeated_capabilities': [
        {'python_name': 'channels', 'prefix': '', },
    ],
}

