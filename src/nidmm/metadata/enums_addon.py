# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. enums.py is code generated

enums_override_metadata = {
    # TODO (ni-jfitzger): delete this override once python_name is corrected for each value. See https://github.com/ni/nimi-python/issues/2072
    'ThermistorType': {
        'values': [
            {
                'documentation': {
                    'description': 'Custom'
                },
                'name': 'NIDMM_VAL_TEMP_THERMISTOR_CUSTOM',
                'value': 0
            },
            {
                'documentation': {
                    'description': '44004'
                },
                'name': 'NIDMM_VAL_TEMP_THERMISTOR_44004',
                'python_name': 'THERMISTOR_44004',
                'value': 1
            },
            {
                'documentation': {
                    'description': '44006'
                },
                'name': 'NIDMM_VAL_TEMP_THERMISTOR_44006',
                'python_name': 'THERMISTOR_44006',
                'value': 2
            },
            {
                'documentation': {
                    'description': '44007'
                },
                'name': 'NIDMM_VAL_TEMP_THERMISTOR_44007',
                'python_name': 'THERMISTOR_44007',
                'value': 3
            }
        ]
    },
}

