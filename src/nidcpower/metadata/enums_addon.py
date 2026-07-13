# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. enums.py is code generated

enums_override_metadata = {
    # TODO (ni-jfitzger): delete this override once python_name is corrected for each value. See https://github.com/ni/nimi-python/issues/2072
    'ComplianceLimitSymmetry': {
        'values': [
            {
                'documentation': {
                    'description': 'Compliance limits are specified symmetrically about 0.'
                },
                'name': 'NIDCPOWER_VAL_COMPLIANCE_LIMIT_SYMMETRY_SYMMETRIC',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Compliance limits can be specified asymmetrically with respect to 0.'
                },
                'name': 'NIDCPOWER_VAL_COMPLIANCE_LIMIT_SYMMETRY_ASYMMETRIC',
                'value': 1
            }
        ]
    },
    # TODO (ni-jfitzger): delete this override once python_name is corrected for each value. See https://github.com/ni/nimi-python/issues/2072
    'Event': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies the Source Complete event.'
                },
                'name': 'NIDCPOWER_VAL_SOURCE_COMPLETE_EVENT',
                'python_name': 'SOURCE_COMPLETE',
                'value': 1030
            },
            {
                'documentation': {
                    'description': 'Specifies the Measure Complete event.'
                },
                'name': 'NIDCPOWER_VAL_MEASURE_COMPLETE_EVENT',
                'python_name': 'MEASURE_COMPLETE',
                'value': 1031
            },
            {
                'documentation': {
                    'description': 'Specifies the Sequence Iteration Complete event.'
                },
                'name': 'NIDCPOWER_VAL_SEQUENCE_ITERATION_COMPLETE_EVENT',
                'python_name': 'SEQUENCE_ITERATION_COMPLETE',
                'value': 1032
            },
            {
                'documentation': {
                    'description': 'Specifies the Sequence Engine Done event.'
                },
                'name': 'NIDCPOWER_VAL_SEQUENCE_ENGINE_DONE_EVENT',
                'python_name': 'SEQUENCE_ENGINE_DONE',
                'value': 1033
            },
            {
                'documentation': {
                    'description': 'Specifies the Pulse Complete event.'
                },
                'name': 'NIDCPOWER_VAL_PULSE_COMPLETE_EVENT',
                'python_name': 'PULSE_COMPLETE',
                'value': 1051
            },
            {
                'documentation': {
                    'description': 'Specifies the Ready for Pulse Trigger event.'
                },
                'name': 'NIDCPOWER_VAL_READY_FOR_PULSE_TRIGGER_EVENT',
                'python_name': 'READY_FOR_PULSE_TRIGGER',
                'value': 1052
            }
        ]
    },
    # TODO (ni-jfitzger): delete this override once python_name is corrected for each value. See https://github.com/ni/nimi-python/issues/2072
    'SendSoftwareEdgeTriggerType': {
        'values': [
            {
                'documentation': {
                    'description': 'Asserts the Start trigger.'
                },
                'name': 'NIDCPOWER_VAL_START_TRIGGER',
                'python_name': 'START',
                'value': 1034
            },
            {
                'documentation': {
                    'description': 'Asserts the Source trigger.'
                },
                'name': 'NIDCPOWER_VAL_SOURCE_TRIGGER',
                'python_name': 'SOURCE',
                'value': 1035
            },
            {
                'documentation': {
                    'description': 'Asserts the Measure trigger.'
                },
                'name': 'NIDCPOWER_VAL_MEASURE_TRIGGER',
                'python_name': 'MEASURE',
                'value': 1036
            },
            {
                'documentation': {
                    'description': 'Asserts the Sequence Advance trigger.'
                },
                'name': 'NIDCPOWER_VAL_SEQUENCE_ADVANCE_TRIGGER',
                'python_name': 'SEQUENCE_ADVANCE',
                'value': 1037
            },
            {
                'documentation': {
                    'description': 'Asserts the Pulse trigger.'
                },
                'name': 'NIDCPOWER_VAL_PULSE_TRIGGER',
                'python_name': 'PULSE',
                'value': 1053
            },
            {
                'documentation': {
                    'description': 'Asserts the Shutdown trigger.'
                },
                'name': 'NIDCPOWER_VAL_SHUTDOWN_TRIGGER',
                'python_name': 'SHUTDOWN',
                'value': 1118
            }
        ]
    },
}

