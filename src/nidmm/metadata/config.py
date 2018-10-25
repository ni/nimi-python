config = {
    'metadata_version': '1.0',
    'module_name': 'nidmm',
    'module_version': '1.1.0',
    'c_function_prefix': 'niDMM_',
    'driver_name': 'NI-DMM',
    'session_class_description': 'An NI-DMM session to a National Instruments Digital Multimeter',
    'session_handle_parameter_name': 'vi',
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
    'context_manager_name': {
        'task': 'acquisition',
        'initiate_function': 'Initiate',
        'abort_function': 'Abort',
    },
    'init_function': 'InitWithOptions',
    'close_function': 'close',
    'driver_urls': {
        'REPLACE_DRIVER_SPECIFIC_URL_1': 'http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/{0}/',
    },
    'custom_types': [],
    'last_tested_version': '18.1.0',
    'repeated_capabilities': [],
}


