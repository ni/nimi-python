config = {
    'metadata_version': '1.0',
    'module_name': 'nimodinst',
    'module_version': '0.1',
    'c_function_prefix': 'niModInst_',
    'driver_name': 'NI-ModInst',
    'session_description': 'An NI-ModInst session to a National Instruments Digital Multimeter',
    'library_name':
    {
        'Windows': {'32bit': 'nimodinst.dll', '64bit': 'nimodinst_64.dll'},
        'Linux': {'64bit': 'libnimodinst.so'}
    }
}

