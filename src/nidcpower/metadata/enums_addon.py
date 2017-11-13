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
    'ExportSignal': {
        'values': [
            {
                'name': 'SOURCE_COMPLETE_EVENT',
                'value': 1030,
                'documentation': {
                    'description': 'Exports the Source Complete event.',
                },
            },
            {
                'name': 'MEASURE_COMPLETE_EVENT',
                'value': 1031,
                'documentation': {
                    'description': 'Exports the Measure Complete event.',
                },
            },
            {
                'name': 'SEQUENCE_ITERATION_COMPLETE_EVENT',
                'value': 1032,
                'documentation': {
                    'description': 'Exports the Sequence Iteration Complete event.',
                },
            },  
            {
                'name': 'SEQUENCE_ENGINE_DONE_EVENT',
                'value': 1033,
                'documentation': {
                    'description': 'Exports the Sequence Engine Done event.',
                },
            },
            {
                'name': 'PULSE_COMPLETE_EVENT',
                'value': 1051,
                'documentation': {
                    'description': 'Exports the Pulse Complete event.',
                },
            },
            {
                'name': 'READY_FOR_PULSE_TRIGGER_EVENT',
                'value': 1052,
                'documentation': {
                    'description': 'Exports the Ready Pulse Trigger event.',
                },
            },
            {
                'name': 'START_TRIGGER',
                'value': 1034,
                'documentation': {
                    'description': 'Exports the Start trigger.',
                },
            },
            {
                'name': 'SOURCE_TRIGGER',
                'value': 1035,
                'documentation': {
                    'description': 'Exports the Source trigger.',
                },
            },
            {
                'name': 'MEASURE_TRIGGER',
                'value': 1036,
                'documentation': {
                    'description': 'Exports the Measure trigger.',
                },
            },
            {
                'name': 'SEQUENCE_ADVANCE_TRIGGER',
                'value': 1037,
                'documentation': {
                    'description': 'Exports the Sequence Advance trigger.',
                },
            },
            {
                'name': 'PULSE_TRIGGER',
                'value': 1053,
                'documentation': {
                    'description': 'Exports the Pulse trigger.',
                },
            },          
        ],
    },
}


