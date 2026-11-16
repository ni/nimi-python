# We need to maintain the version here since it needs to be updated by the build process on GitHub
config_additional_config = {
    'module_version': '1.5.1.dev0',
}

# Replaces the single context manager from config.py to test multiple session context managers
config_additional_context_managers = {
    'context_manager_name': [
        {
            'abort_function': 'Abort',
            'initiate_function': 'Initiate',
            'task': 'acquisition'
        },
        {
            'abort_function': 'AbortGeneration',
            'initiate_function': 'InitiateGeneration',
            'method_name': 'initiate_generation',
            'task': 'generation'
        }
    ],
}
