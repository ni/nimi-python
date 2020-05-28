# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

functions_override_metadata = {
}

functions_additional_internal_cal_fetch_temperature = {
    'CalFetchTemperature': {
        'codegen_method': 'private',
        'method_name_for_documentation': '_cal_fetch_temperature',
        'documentation': {
            'description': 'Returns the **Temperature** in degrees Celsius during the last external calibration procedure.',
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session. You obtain the **vi** parameter from niScope_init.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the type of calibration performed (external or self-calibration).',
                    'table_body': [
                        [
                            'NIDMM_VAL_INTERNAL_AREA (default)',
                            '0',
                            'Self-Calibration'
                        ],
                        [
                            'NIDMM_VAL_EXTERNAL_AREA',
                            '1',
                            'External Calibration'
                        ]
                    ]
                },
                'name': 'calType',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the **temperature** in degrees Celsius during the last calibration.'
                },
                'name': 'temperature',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    }
}

functions_additional_internal_cal_fetch_date = {
    'CalFetchDate': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Returns the date and time of the last calibration performed.',
        },
        'method_name_for_documentation': '_cal_fetch_date',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session. You obtain the **vi** parameter from niScope_init.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the type of calibration performed (external or self-calibration).',
                    'table_body': [
                        [
                            'NIDMM_VAL_INTERNAL_AREA (default)',
                            '0',
                            'Self-Calibration'
                        ],
                        [
                            'NIDMM_VAL_EXTERNAL_AREA',
                            '1',
                            'External Calibration'
                        ]
                    ]
                },
                'name': 'calType',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates the **month** of the last calibration.'
                },
                'name': 'month',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates the **day** of the last calibration.'
                },
                'name': 'day',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates the **year** of the last calibration.'
                },
                'name': 'year',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates the **hour** of the last calibration.'
                },
                'name': 'hour',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates the **minute** of the last calibration.'
                },
                'name': 'minute',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    }
}

functions_additional_get_self_cal_last_date_and_time = {
    'FancyGetLastSelfCalDateAndTime': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': 'Returns the date and time of the last self calibration performed.',
        },
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_self_cal_last_date'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session. You obtain the **vi** parameter from niScope_init.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates the **datetime** of the last calibration.'
                },
                'name': 'datetime',
                'type': 'ViInt32'
            }
        ],
        'python_name': 'get_self_cal_last_date_and_time',
        'returns': 'ViStatus'
    }
}

functions_additional_get_ext_cal_last_date_and_time = {
    'FancyGetLastExtCalDateAndTime': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': 'Returns the date and time of the last external calibration performed.',
        },
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_ext_cal_last_date'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session. You obtain the **vi** parameter from niScope_init.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates the **datetime** of the last calibration.'
                },
                'name': 'datetime',
                'type': 'ViInt32'
            }
        ],
        'python_name': 'get_ext_cal_last_date_and_time',
        'returns': 'ViStatus'
    }
}

functions_additional_get_self_cal_last_temp = {
    'FancyGetLastSelfCalTemp': {
        'codegen_method': 'python-only',
        'python_name': 'get_self_cal_last_temp',
        'documentation': {
            'description': 'Returns the **Temperature** in degrees Celsius during the last self calibration procedure.',
        },
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_self_cal_last_temp'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The instrument handle you obtain from niScope_init that identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the **temperature** in degrees Celsius during the last calibration.'
                },
                'name': 'temperature',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    }
}

functions_additional_get_ext_cal_last_temp = {
    'FancyGetLastExtCalTemp': {
        'codegen_method': 'python-only',
        'python_name': 'get_ext_cal_last_temp',
        'documentation': {
            'description': 'Returns the **Temperature** in degrees Celsius during the last external calibration procedure.',
        },
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_ext_cal_last_temp'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session. You obtain the **vi** parameter from niScope_init.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the **temperature** in degrees Celsius during the last calibration.'
                },
                'name': 'temperature',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    }
}

functions_additional_get_cal_user_info = {
    'CalFetchMiscInfo': {
        'documentation': {
            'description': 'Returns the miscellaneous information you can store during an external calibration using niScope Cal Store Misc Info.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session. You obtain the **vi** parameter from niScope_init.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'A string containing up to four characters of miscellaneous information stored in the EEPROM.'
                },
                'name': 'miscellaneousInformation',
                'size': {
                    'mechanism': 'fixed',
                    'value': 4
                },
                'type': 'ViString'
            }
        ],
        'python_name': 'get_cal_user_info',
        'returns': 'ViStatus'
    }
}

