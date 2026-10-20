# -*- coding: utf-8 -*-
# This file is generated from NI-Digital Pattern Driver API metadata version 26.8.0f154
config = {
    'api_version': '26.8.0f154',
    'c_function_prefix': 'niDigital_',
    'close_function': 'close',
    'context_manager_name': {
        'abort_function': 'Abort',
        'initiate_function': 'Initiate',
        'task': 'burst'
    },
    'custom_types': [
        {
            'ctypes_type': 'struct_InternalPattern',
            'file_name': 'internal_pattern',
            'grpc_name': 'InternalPattern',
            'python_name': 'InternalPattern'
        }
    ],
    'driver_name': 'NI-Digital Pattern Driver',
    'enum_whitelist_suffix': [
    ],
    'extra_errors_used': [
        'InvalidRepeatedCapabilityError',
        'SelfTestError'
    ],
    'grpc_service_class_prefix': 'NiDigital',
    'init_function': 'InitWithOptions',
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'nidigital',
                'type': 'cdll'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'niDigital_32.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'niDigital_64.dll',
                'type': 'cdll'
            }
        }
    },
    'module_name': 'nidigital',
    'proto_name': 'nidigitalpattern',
    'repeated_capabilities': [
        {
            'prefix': '',
            'python_name': 'channels'
        },
        {
            'prefix': '',
            'python_name': 'pins'
        },
        {
            'prefix': '',
            'python_name': 'instruments'
        },
        {
            'prefix': 'patternOpcodeEvent',
            'python_name': 'pattern_opcode_events'
        },
        {
            'prefix': 'conditionalJumpTrigger',
            'python_name': 'conditional_jump_triggers'
        },
        {
            'prefix': 'site',
            'python_name': 'sites'
        },
        {
            'prefix': 'RIOEvent',
            'python_name': 'rio_events'
        },
        {
            'prefix': 'RIOTrigger',
            'python_name': 'rio_triggers'
        },
        {
            'documentation': {
                'description': 'TMU repeated capabilities identify the time measurement unit contexts for an instrument. Valid TMU identifiers are tmu0 and tmu1. The numeric portion of the identifier may be used without the "tmu" prefix. In that case, the correct prefix will be added when the driver function call is made. When accessing TMUs from an instrument context, select one TMU identifier at a time.',
                'examples': [
                    "session.instruments['PXI1Slot2'].time_measurement_units[0].tmu_enabled = True",
                    "session.instruments['PXI1Slot2'].time_measurement_units['tmu0'].tmu_enabled = True"
                ]
            },
            'prefix': 'tmu',
            'python_name': 'time_measurement_units'
        }
    ],
    'session_class_description': 'An NI-Digital Pattern Driver session',
    'session_handle_parameter_name': 'vi',
    'uses_nitclk': True
}
