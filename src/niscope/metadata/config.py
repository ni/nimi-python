# -*- coding: utf-8 -*-
# This file is generated from NI-SCOPE API metadata version 23.0.0d91
config = {
    'api_version': '23.0.0d91',
    'c_function_prefix': 'niScope_',
    'close_function': 'close',
    'context_manager_name': {
        'abort_function': 'Abort',
        'initiate_function': 'InitiateAcquisition',
        'task': 'acquisition'
    },
    'custom_types': [
        {
            'ctypes_type': 'struct_niScope_wfmInfo',
            'file_name': 'waveform_info',
            'grpc_name': 'WaveformInfo',
            'python_name': 'WaveformInfo'
        }
    ],
    'driver_name': 'NI-SCOPE',
    'extra_errors_used': [
        'InvalidRepeatedCapabilityError',
        'SelfTestError'
    ],
    'grpc_service_class_prefix': 'NiScope',
    'init_function': 'InitWithOptions',
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'niscope',
                'type': 'cdll'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'niScope_32.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'niScope_64.dll',
                'type': 'cdll'
            }
        }
    },
    'module_name': 'niscope',
    'repeated_capabilities': [
        {
            'prefix': '',
            'python_name': 'channels'
        },
        {
            'prefix': '',
            'python_name': 'instruments'
        }
    ],
    'session_class_description': 'An NI-SCOPE session to an NI digitizer.',
    'session_handle_parameter_name': 'vi',
    'uses_nitclk': True
}
