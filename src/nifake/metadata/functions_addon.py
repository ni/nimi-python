# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

functions_override_metadata = {
    # TODO: delete this when there's no difference from functions.py content
    'SetRuntimeEnvironment': {
        'codegen_method': 'private',
        'method_templates': [
            {
                'documentation_filename': 'none',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'none'  # will (intentionally) keep this method out of session.py, despite the codegen_method being private
            }
        ],
    }
}


