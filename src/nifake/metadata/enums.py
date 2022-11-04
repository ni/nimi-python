# -*- coding: utf-8 -*-
# This file is generated from NI-FAKE API metadata version 23.0.0d76
enums = {
    'AltColor': {
        'values': [
            {
                'name': 'NIFAKE_VAL_RED',
                'value': 1
            },
            {
                'name': 'NIFAKE_VAL_BLUE',
                'value': 2
            },
            {
                'name': 'NIFAKE_VAL_YELLOW',
                'value': 5
            },
            {
                'name': 'NIFAKE_VAL_BLACK',
                'value': 42
            }
        ]
    },
    'BeautifulColor': {
        'values': [
            {
                'name': 'NIFAKE_VAL_PINK',
                'value': 44
            },
            {
                'name': 'NIFAKE_VAL_AQUA',
                'value': 43
            },
            {
                'name': 'NIFAKE_VAL_GREEN',
                'value': 45
            },
            {
                'name': 'NIFAKE_VAL_BLACK',
                'value': 42
            }
        ]
    },
    'Color': {
        'values': [
            {
                'documentation': {
                    'description': 'Like blood.'
                },
                'name': 'NIFAKE_VAL_RED',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Like the sky.'
                },
                'name': 'NIFAKE_VAL_BLUE',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Like a banana.'
                },
                'name': 'NIFAKE_VAL_YELLOW',
                'value': 5
            },
            {
                'documentation': {
                    'description': "Like this developer's conscience."
                },
                'name': 'NIFAKE_VAL_BLACK',
                'value': 42
            }
        ]
    },
    'ColorObsolete': {
        'values': [
            {
                'name': 'NIFAKE_VAL_RED',
                'value': 1
            },
            {
                'name': 'NIFAKE_VAL_BLUE',
                'value': 2
            },
            {
                'name': 'NIFAKE_VAL_YELLOW',
                'value': 5
            },
            {
                'name': 'NIFAKE_VAL_BLACK',
                'value': 42
            }
        ]
    },
    'ColorPrivate': {
        'values': [
            {
                'name': 'NIFAKE_VAL_RED',
                'value': 1
            },
            {
                'name': 'NIFAKE_VAL_BLUE',
                'value': 2
            },
            {
                'name': 'NIFAKE_VAL_YELLOW',
                'value': 5
            },
            {
                'name': 'NIFAKE_VAL_BLACK',
                'value': 42
            }
        ]
    },
    'DecimalMixedNumber': {
        'values': [
            {
                'name': 'NIFAKE_VAL_TWENTY_TWO',
                'value': 22.0
            },
            {
                'name': 'NIFAKE_VAL_TWO_POINT_TWO',
                'value': 2.2
            },
            {
                'name': 'NIFAKE_VAL_NEGATIVE_THREE',
                'value': -3.0
            },
            {
                'name': 'NIFAKE_VAL_MAX_INT_32',
                'value': 2147483647.0
            },
            {
                'name': 'NIFAKE_VAL_MAX_INT_32_PLUS_ONE',
                'value': 2147483648.0
            },
            {
                'name': 'NIFAKE_VAL_MIN_INT_32',
                'value': -2147483648.0
            },
            {
                'name': 'NIFAKE_VAL_MIN_INT_32_MINUS_ONE',
                'value': -2147483649.0
            }
        ]
    },
    'DecimalWholeNumberMapped': {
        'values': [
            {
                'name': 'NIFAKE_VAL_NEGATIVE_ONE',
                'value': -1.0
            },
            {
                'name': 'NIFAKE_VAL_TWENTY_TWO',
                'value': 22.0
            },
            {
                'name': 'NIFAKE_VAL_ZERO',
                'value': 0.0
            }
        ]
    },
    'EnumWithConverter': {
        'codegen_method': 'public',
        'converted_value_to_enum_function_name': 'convert_to_enum_with_converter_enum',
        'enum_to_converted_value_function_name': 'convert_from_enum_with_converter_enum',
        'values': [
            {
                'converts_to_value': True,
                'name': 'NIFAKE_VAL_RED',
                'value': 1
            },
            {
                'converts_to_value': False,
                'name': 'NIFAKE_VAL_BLUE',
                'value': 2
            },
            {
                'converts_to_value': 'yellow',
                'name': 'NIFAKE_VAL_YELLOW',
                'value': 5
            },
            {
                'converts_to_value': 42,
                'name': 'NIFAKE_VAL_BLACK',
                'value': 42
            }
        ]
    },
    'EnumWithGrpcNameValues': {
        'values': [
            {
                'name': 'NIFAKE_VAL_ONE',
                'value': 1
            },
            {
                'name': 'NIFAKE_VAL_TWO',
                'value': 2
            }
        ]
    },
    'FloatEnum': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies 3.5 digits resolution.'
                },
                'name': 'NIFAKE_VAL_THREE_POINT_FIVE',
                'value': 3.5
            },
            {
                'documentation': {
                    'description': 'Specifies 4.5 digits resolution.'
                },
                'name': 'NIFAKE_VAL_FOUR_POINT_FIVE',
                'value': 4.5
            },
            {
                'documentation': {
                    'description': 'Specifies 5.5 digits resolution.'
                },
                'name': 'NIFAKE_VAL_FIVE_POINT_FIVE',
                'value': 5.5
            },
            {
                'documentation': {
                    'description': 'Specifies 6.5 digits resolution.'
                },
                'name': 'NIFAKE_VAL_SIX_POINT_FIVE',
                'value': 6.5
            },
            {
                'documentation': {
                    'description': 'Specifies 7.5 digits resolution.'
                },
                'name': 'NIFAKE_VAL_SEVEN_POINT_FIVE',
                'value': 7.5
            }
        ]
    },
    'MobileOSNames': {
        'values': [
            {
                'documentation': {
                    'description': 'Most popular OS.'
                },
                'name': 'NIFAKE_VAL_ANDROID',
                'value': 'Android'
            },
            {
                'documentation': {
                    'description': 'Most secure OS.'
                },
                'name': 'NIFAKE_VAL_IOS',
                'value': 'iOS'
            },
            {
                'documentation': {
                    'description': 'Remember Symbian?.'
                },
                'name': 'NIFAKE_VAL_NONE',
                'value': 'None'
            }
        ]
    },
    'Turtle': {
        'values': [
            {
                'documentation': {
                    'description': 'Wields two katanas.'
                },
                'name': 'NIFAKE_VAL_LEONARDO',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Uses a bo staff.'
                },
                'name': 'NIFAKE_VAL_DONATELLO',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Has a pair of sai.'
                },
                'name': 'NIFAKE_VAL_RAPHAEL',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Owns nunchucks.'
                },
                'name': 'NIFAKE_VAL_MICHELANGELO',
                'value': 3
            }
        ]
    }
}
