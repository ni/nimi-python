config = {
    'module_name': 'nidmm',
    'module_version': '0.1',
    'c_function_prefix': 'niDMM_',
    'session_description': 'An NI-DMM session to a National Instruments Digital Multimeter',
    'library_windows':
    {
        '32': 'nidmm_32.dll',
        '64': 'nidmm_64.dll'
    },
    'library_linux':
    {
        '32': 'nidmm_32.so',
        '64': 'nidmm_64.so'
    },
}

