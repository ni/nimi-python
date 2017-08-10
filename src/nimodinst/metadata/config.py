config = {
    'metadata_version': '1.0',
    'module_name': 'nimodinst',
    'module_version': '0.1.0.dev3',
    'c_function_prefix': 'niModInst_',
    'driver_name': 'NI-ModInst',
    'session_description': 'A NI-ModInst session to get device information',
    'library_info':
    {
        'Windows': {
            '32bit': {'name': 'nimodinst.dll', 'type': 'windll'},
            '64bit': {'name': 'nimodinst_64.dll', 'type': 'cdll'},
        },
        'Linux': {
            '64bit': {'name': 'libnimodinst.so', 'type': 'cdll'},
        },
    }
}

