config = {
    'metadata_version': '0.1',
    'module_name': 'nitclk',
    'module_version': '0.1.0.dev0',
    'c_function_prefix': 'niTClk_',
    'driver_name': 'NI-TClk',
    'session_class_description': 'An NI-TClk session.',
    'session_handle_parameter_name': 'sessions',
    'library_info':
    {
        'Windows': {
            '32bit': {'name': 'nitclk.dll', 'type': 'windll'},
            '64bit': {'name': 'nitclk_64.dll', 'type': 'cdll'},
        },
        'Linux': {
            '64bit': {'name': 'libnitclk.so', 'type': 'cdll'},
        },
    },
    'context_manager_name': {
        'task': 'acquisition',
        'initiate_function': 'Initiate',
        'abort_function': None,
    },
    'init_function': 'InitForDocumentation',
    'close_function': None,
    'custom_types': [],
    'last_tested_version': '18.1.1',
    'repeated_capabilities': [],
}

