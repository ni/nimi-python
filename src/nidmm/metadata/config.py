config = {
    'module_name': 'nidmm',
    'module_version': '0.1',
    'c_function_prefix': 'niDMM_',
    'driver_name': 'NI-DMM',
    'files_to_generate': ['attributes.py', 'enums.py', 'library.py', 'session.py', 'errors.py', '__init__.py'],
    'session_description': 'An NI-DMM session to a National Instruments Digital Multimeter',
    'library_name':
    {
        'Windows': {'32bit': 'nidmm_32.dll', '64bit': 'nidmm_64.dll'},
        'Linux': {'64bit': 'libnidmm.so'}
    }
}

