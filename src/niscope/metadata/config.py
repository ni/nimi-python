config = {
    'metadata_version': '1.0',
    'module_name': 'niscope',
    'module_version': '0.4.0.dev0',
    'c_function_prefix': 'niScope_',
    'driver_name': 'NI-SCOPE',
    'session_class_description': 'An NI-SCOPE session to a National Instruments Digitizer.',
    'session_handle_parameter_name': 'vi',
    'library_info':
    {
        'Windows': {
            '32bit': {'name': 'niscope_32.dll', 'type': 'windll'},
            '64bit': {'name': 'niscope_64.dll', 'type': 'cdll'},
        },
        'Linux': {
            '64bit': {'name': 'libscope.so', 'type': 'cdll'},
        },
    },
    'context_manager_name': {
        'task': 'acquisition',
        'initiate_function': 'InitiateAcquisition',
        'abort_function': 'Abort',
    },
    'init_function': 'InitWithOptions',
}

