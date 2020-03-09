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
                'name': 'NIDCPOWER_VAL_START',
                'value': 1034,
            },
            {
                'name': 'NIDCPOWER_VAL_SOURCE',
                'value': 1035,
            },
            {
                'name': 'NIDCPOWER_VAL_MEASURE',
                'value': 1036,
            },
            {
                'name': 'NIDCPOWER_VAL_SEQUENCE_ADVANCE',
                'value': 1037,
            },
            {
                'name': 'NIDCPOWER_VAL_PULSE',
                'value': 1053,
            },
        ],
    },
    'Event': {
        'values': [
            {
                'name': 'NIDCPOWER_VAL_SOURCE_COMPLETE',
                'value': 1030,
            },
            {
                'name': 'NIDCPOWER_VAL_MEASURE_COMPLETE',
                'value': 1031,
            },
            {
                'name': 'NIDCPOWER_VAL_SEQUENCE_ITERATION_COMPLETE',
                'value': 1032,
            },
            {
                'name': 'NIDCPOWER_VAL_SEQUENCE_ENGINE_DONE',
                'value': 1033,
            },
            {
                'name': 'NIDCPOWER_VAL_PULSE_COMPLETE',
                'value': 1051,
            },
            {
                'name': 'NIDCPOWER_VAL_READY_FOR_PULSE_TRIGGER',
                'value': 1052,
            },
        ],
    },
    'MeasurementTypes': {
        'values': [
            {
                'name': 'NIDCPOWER_VAL_MEASURE_CURRENT',
                'value': 0,
                'documentation': {
                    'description': 'The device measures current.',
                },
            },
            {
                'name': 'NIDCPOWER_VAL_MEASURE_VOLTAGE',
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
                'name': 'NIDCPOWER_VAL_OUTPUT_CONSTANT_VOLTAGE',
                'value': 0,
                'documentation': {
                    'description': 'The device maintains a constant voltage by adjusting the current ',
                },
            },
            {
                'name': 'NIDCPOWER_VAL_OUTPUT_CONSTANT_CURRENT',
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
                'name': 'NIDCPOWER_VAL_SOURCE_COMPLETE_EVENT',
                'value': 1030,
                'documentation': {
                    'description': 'Exports the Source Complete event.',
                },
            },
            {
                'name': 'NIDCPOWER_VAL_MEASURE_COMPLETE_EVENT',
                'value': 1031,
                'documentation': {
                    'description': 'Exports the Measure Complete event.',
                },
            },
            {
                'name': 'NIDCPOWER_VAL_SEQUENCE_ITERATION_COMPLETE_EVENT',
                'value': 1032,
                'documentation': {
                    'description': 'Exports the Sequence Iteration Complete event.',
                },
            },  
            {
                'name': 'NIDCPOWER_VAL_SEQUENCE_ENGINE_DONE_EVENT',
                'value': 1033,
                'documentation': {
                    'description': 'Exports the Sequence Engine Done event.',
                },
            },
            {
                'name': 'NIDCPOWER_VAL_PULSE_COMPLETE_EVENT',
                'value': 1051,
                'documentation': {
                    'description': 'Exports the Pulse Complete event.',
                },
            },
            {
                'name': 'NIDCPOWER_VAL_READY_FOR_PULSE_TRIGGER_EVENT',
                'value': 1052,
                'documentation': {
                    'description': 'Exports the Ready Pulse Trigger event.',
                },
            },
            {
                'name': 'NIDCPOWER_VAL_START_TRIGGER',
                'value': 1034,
                'documentation': {
                    'description': 'Exports the Start trigger.',
                },
            },
            {
                'name': 'NIDCPOWER_VAL_SOURCE_TRIGGER',
                'value': 1035,
                'documentation': {
                    'description': 'Exports the Source trigger.',
                },
            },
            {
                'name': 'NIDCPOWER_VAL_MEASURE_TRIGGER',
                'value': 1036,
                'documentation': {
                    'description': 'Exports the Measure trigger.',
                },
            },
            {
                'name': 'NIDCPOWER_VAL_SEQUENCE_ADVANCE_TRIGGER',
                'value': 1037,
                'documentation': {
                    'description': 'Exports the Sequence Advance trigger.',
                },
            },
            {
                'name': 'NIDCPOWER_VAL_PULSE_TRIGGER',
                'value': 1053,
                'documentation': {
                    'description': 'Exports the Pulse trigger.',
                },
            },          
        ],
    },
    'PowerLineFrequency': {}, # Enum metadata actually contains constants.
    'CurrentLimitAutorange': {},  # Delete because boolean values only
    'CurrentLevelAutorange': {},  # Delete because boolean values only
    'VoltageLevelAutorange': {},  # Delete because boolean values only
    'VoltageLimitAutorange': {},  # Delete because boolean values only
    'tBoolean': {},  # Enum just represents True/False
}


