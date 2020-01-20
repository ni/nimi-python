# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

functions_override_metadata = {
    'ImportAttributeConfigurationBuffer': {
        'parameters': {
            2: {'python_api_converter_name': 'convert_import_buffer', }
        },
    },
    'ExportAttributeConfigurationBuffer': {
        'parameters': {
            2: {
                'python_api_converter_name': 'convert_buffer_to_bytes',
                'use_array': True,
            },
        },
    },
}


