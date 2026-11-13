# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

functions_override_metadata = {
}

# Used to test multiple session context managers. See config_addon.py
functions_additional_generation = {
    'AbortGeneration': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Aborts a previously initiated generation.'
        },
        'included_in_proto': False,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'render_in_session_base': True,
        'returns': 'ViStatus'
    },
    'InitiateGeneration': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Initiates a generation.'
        },
        'included_in_proto': False,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'render_in_session_base': True,
        'returns': 'ViStatus'
    },
}


