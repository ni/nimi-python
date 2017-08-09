config = {
    'metadata_version': '1.0',
    'module_name': 'nidmm',
    'module_version': '0.1.0.dev3',
    'c_function_prefix': 'niDMM_',
    'driver_name': 'NI-DMM',
    'session_description': 'An NI-DMM session to a National Instruments Digital Multimeter',
    'library_info':
    {
        'Windows': {
            '32bit': {'name': 'nidmm_32.dll', 'type': 'windll'},
            '64bit': {'name': 'nidmm_64.dll', 'type': 'cdll'},
        },
        'Linux': {
            '64bit': {'name': 'libnidmm.so', 'type': 'cdll'},
        },
    },
    'context_manager': [
        {
            'direction': 'input'
        },
    ]
}

