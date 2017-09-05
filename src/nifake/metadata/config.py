config = {
    'metadata_version': '1.0',
    'module_name': 'nifake',
    'module_version': '0.2.0.dev0',
    'c_function_prefix': 'niFake_',
    'driver_name': 'NI-FAKE',
    'session_description': 'An NI-FAKE session to a fake MI driver whose sole purpose is to test nimi-python code generation',
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
    'context_manager': [
        {
            #TODO(marcoskirsch): I question the need for this, need to understand how it's used better.
            'direction': 'input'
        },
    ]
}

