# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

functions_override_metadata = {
}

functions_additional_get_ext_cal_last_temp = {
    'FancyGetExtCalLastTemp': {
        'codegen_method': 'python-only',
        'python_name': 'get_ext_cal_last_temp',
        'documentation': {
            'description': 'Returns the **Temperature** during the last external calibration procedure.',
        },
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_get_cal_last_temp'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the **temperature** during the last external calibration.'
                },
                'name': 'temperature',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    }
}

functions_additional_get_self_cal_last_temp = {
    'FancyGetSelfCalLastTemp': {
        'codegen_method': 'python-only',
        'python_name': 'get_self_cal_last_temp',
        'documentation': {
            'description': 'Returns the **Temperature** during the last self calibration procedure.',
        },
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_get_cal_last_temp'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the **temperature** during the last self calibration.'
                },
                'name': 'temperature',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    }
}

functions_additional_get_ext_cal_last_date_and_time = {
    'FancyGetExtCalLastDateAndTime': {
        'codegen_method': 'python-only',
    	'python_name': 'get_ext_cal_last_date_and_time',
        'documentation': {
            'description': 'Returns the date and time of the last external calibration performed.',
        },
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_get_cal_last_date_and_time'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session. You obtain the **vi** parameter from niDMM_init or niDMM_InitWithOptions. The default is None.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates date and time of the last external calibration.'
                },
                'name': 'last_cal_datetime',
                'type': 'hightime.datetime'
            }
        ],
        'returns': 'ViStatus'
    }
}

functions_additional_get_self_cal_last_date_and_time = {
    'FancyGetSelfCalLastDateAndTime': {
        'codegen_method': 'python-only',
    	'python_name': 'get_self_cal_last_date_and_time',
        'documentation': {
            'description': 'Returns the date and time of the last self calibration performed.',
        },
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_get_cal_last_date_and_time'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session. You obtain the **vi** parameter from niDMM_init or niDMM_InitWithOptions. The default is None.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates date and time of the last self calibration.'
                },
                'name': 'last_cal_datetime',
                'type': 'hightime.datetime'
            }
        ],
        'returns': 'ViStatus'
    }
}
