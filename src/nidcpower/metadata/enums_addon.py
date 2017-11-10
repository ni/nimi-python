# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

# We are not code genning enums that have been marked as obsolete prior to the initial
# Python API bindings release
# We also do not codegen enums associated with P2P or External Calibration since neither 
# are supported in Python
enums_codegen_method = {
}

enums_additional_enums = {
    'SendSoftwareEdgeTriggerType': {
        'values': [
            {
                'name': 'START',
                'value': 1034,
            },
            {
                'name': 'SOURCE',
                'value': 1035,
            },
            {
                'name': 'MEASURE',
                'value': 1036,
            },
            {
                'name': 'SEQUENCE_ADVANCE',
                'value': 1037,
            },
            {
                'name': 'PULSE',
                'value': 1053,
            },
        ],
    },
    'Event': {
        'values': [
            {
                'name': 'SOURCE_COMPLETE',
                'value': 1030,
            },
            {
                'name': 'MEASURE_COMPLETE',
                'value': 1031,
            },
            {
                'name': 'SEQUENCE_ITERATION_COMPLETE',
                'value': 1032,
            },
            {
                'name': 'SEQUENCE_ENGINE_DONE',
                'value': 1033,
            },
            {
                'name': 'PULSE_COMPLETE',
                'value': 1051,
            },
            {
                'name': 'READY_FOR_PULSE_TRIGGER',
                'value': 1052,
            },
        ],
    },
    'MeasurementTypes': {
        'values': [
            {
                'name': 'MEASURE_CURRENT',
                'value': 0,
                'documentation': {
                    'description': 'The device measures current.',
                },
            },
            {
                'name': 'MEASURE_VOLTAGE',
                'value': 1,
                'documentation': {
                    'description': 'The device measures voltage.',
                },
            }
        ],
    },
    'OutputStates': {
        'values': [
            {
                'name': 'OUTPUT_CONSTANT_VOLTAGE',
                'value': 0,
                'documentation': {
                    'description': 'The device maintains a constant voltage by adjusting the current ',
                },
            },
            {
                'name': 'OUTPUT_CONSTANT_CURRENT',
                'value': 1,
                'documentation': {
                    'description': 'The device maintains a constant current by adjusting the voltage.',
                },
            }
        ],
    },
}


