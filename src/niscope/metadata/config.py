config = {
    'metadata_version': '1.0',
    'module_name': 'niscope',
    'module_version': '1.0.1',
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
            '64bit': {'name': 'libniscope.so', 'type': 'cdll'},
        },
    },
    'context_manager_name': {
        'task': 'acquisition',
        'initiate_function': 'InitiateAcquisition',
        'abort_function': 'Abort',
    },
    'init_function': 'InitWithOptions',
    'custom_types': [
        {'file_name': 'waveform_info', 'python_name': 'WaveformInfo', 'ctypes_type': 'struct_niScope_wfmInfo', },
    ],
    'last_tested_version': '17.0.2',
    'repeated_capabilities': [
        {'python_name': 'channels', 'prefix': '', },
    ],
}

