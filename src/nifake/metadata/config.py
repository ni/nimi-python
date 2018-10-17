config = {
    'metadata_version': '1.0',
    'module_name': 'nifake',
    'module_version': '1.0.2.dev0',
    'c_function_prefix': 'niFake_',
    'driver_name': 'NI-FAKE',
    'session_class_description': 'An NI-FAKE session to a fake MI driver whose sole purpose is to test nimi-python code generation',
    'session_handle_parameter_name': 'vi',
    'library_info':
    {
        'Windows': {
            '32bit': {'name': 'nifake_32.dll', 'type': 'windll'},
            '64bit': {'name': 'nifake_64.dll', 'type': 'cdll'},
        },
        'Linux': {
            '64bit': {'name': 'libnifake.so', 'type': 'cdll'},
        },
    },
    'context_manager_name': {
        'task': 'acquisition',
        'initiate_function': 'Initiate',
        'abort_function': 'Abort',
    },
    'init_function': 'InitWithOptions',
    'custom_types': [
        {'file_name': 'custom_struct', 'python_name': 'CustomStruct', 'ctypes_type': 'custom_struct', },
    ],
    'enum_whitelist_suffix': ['_POINT_FIVE'],
    'repeated_capabilities': [
        {'python_name': 'channels', 'prefix': '', },
    ],
}

