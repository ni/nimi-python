config = {
    'metadata_version': '1.0',
    'module_name': 'nifgen',
    'module_version': '1.1.0.dev0',
    'c_function_prefix': 'niFgen_',
    'driver_name': 'NI-FGEN',
    'session_class_description': 'An NI-FGEN session to a National Instruments Signal Generator.',
    'session_handle_parameter_name': 'vi',
    'library_info':
    {
        'Windows': {
            '32bit': {'name': 'nifgen_32.dll', 'type': 'windll'},
            '64bit': {'name': 'nifgen_64.dll', 'type': 'cdll'},
        },
        'Linux': {
            '64bit': {'name': 'libfgen.so', 'type': 'cdll'},
        },
    },
    'context_manager_name': {
        'task': 'generation',
        'initiate_function': 'InitiateGeneration',
        'abort_function': 'AbortGeneration',
    },
    'init_function': 'InitializeWithChannels',
    'close_function': 'close',
    'custom_types': [],
    'last_tested_version': '18.1.0',
    'repeated_capabilities': [
        {'python_name': 'channels', 'prefix': '', },
        {'python_name': 'script_triggers', 'prefix': 'ScriptTrigger', },
        {'python_name': 'markers', 'prefix': 'Marker', },
    ],
}

