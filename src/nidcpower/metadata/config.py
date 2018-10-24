config = {
    'metadata_version': '1.0',
    'module_name': 'nidcpower',
    'module_version': '1.0.2.dev0',
    'c_function_prefix': 'niDCPower_',
    'driver_name': 'NI-DCPower',
    'session_class_description': 'An NI-DCPower session to a National Instruments Programmable Power Supply or Source Measure Unit.',
    'session_handle_parameter_name': 'vi',
    'library_info':
    {
        'Windows': {
            '32bit': {'name': 'nidcpower_32.dll', 'type': 'windll'},
            '64bit': {'name': 'nidcpower_64.dll', 'type': 'cdll'},
        },
        'Linux': {
            '64bit': {'name': 'libnidcpower.so', 'type': 'cdll'},
        },
    },
    'context_manager_name': {
        'task': 'acquisition',
        'initiate_function': 'Initiate',
        'abort_function': 'Abort',
    },
    'init_function': 'InitializeWithChannels',
    'close_function': 'close',
    'custom_types': [],
    'last_tested_version': '18.1.1',
    'repeated_capabilities': [
        {'python_name': 'channels', 'prefix': '', },
    ],
}

