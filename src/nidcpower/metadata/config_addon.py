# We need to maintain the version here since it needs to be updated by the build process on GitHub
config_additional_config = {
    'module_version': '1.4.2.dev0',
    'latest_runtime_version_tested_against': '21.3.0',
    'custom_types': [
        # Redundant, since these custom types are also in the base config.py file.
        #  See issue 1495 (https://github.com/ni/nimi-python/issues/1495)
        {
            'ctypes_type': 'struct_NILCRLoadCompensationSpot',
            'file_name': 'ni_lcr_load_compensation_spot',
            'python_name': 'NILCRLoadCompensationSpot'
        },
        {
            'ctypes_type': 'struct_NILCRMeasurement',
            'file_name': 'ni_lcr_measurement',
            'python_name': 'NILCRMeasurement'
        }
    ]
}
