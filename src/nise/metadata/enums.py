# -*- coding: utf-8 -*-
# This file is generated from NI Switch Executive API metadata version 24.3.0d13
enums = {
    'ExpandAction': {
        'values': [
            {
                'documentation': {
                    'description': 'Expand to routes'
                },
                'name': 'NISE_VAL_EXPAND_TO_ROUTES',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Expand to paths'
                },
                'name': 'NISE_VAL_EXPAND_TO_PATHS',
                'value': 1
            }
        ]
    },
    'MulticonnectMode': {
        'values': [
            {
                'documentation': {
                    'description': 'Default'
                },
                'name': 'NISE_VAL_DEFAULT',
                'value': -1
            },
            {
                'documentation': {
                    'description': 'No multiconnect'
                },
                'name': 'NISE_VAL_NO_MULTICONNECT',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Multiconnect'
                },
                'name': 'NISE_VAL_MULTICONNECT',
                'value': 1
            }
        ]
    },
    'OperationOrder': {
        'values': [
            {
                'documentation': {
                    'description': 'Break before make'
                },
                'name': 'NISE_VAL_BREAK_BEFORE_MAKE',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Break after make'
                },
                'name': 'NISE_VAL_BREAK_AFTER_MAKE',
                'value': 2
            }
        ]
    },
    'PathCapability': {
        'values': [
            {
                'documentation': {
                    'description': 'Path needs hardwire'
                },
                'name': 'NISE_VAL_PATH_NEEDS_HARDWIRE',
                'value': -2
            },
            {
                'documentation': {
                    'description': 'Path needs config channel'
                },
                'name': 'NISE_VAL_PATH_NEEDS_CONFIG_CHANNEL',
                'value': -1
            },
            {
                'documentation': {
                    'description': 'Path available'
                },
                'name': 'NISE_VAL_PATH_AVAILABLE',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Path exists'
                },
                'name': 'NISE_VAL_PATH_EXISTS',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Path Unsupported'
                },
                'name': 'NISE_VAL_PATH_UNSUPPORTED',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'Resource in use'
                },
                'name': 'NISE_VAL_RESOURCE_IN_USE',
                'value': 4
            },
            {
                'documentation': {
                    'description': 'Exclusion conflict'
                },
                'name': 'NISE_VAL_EXCLUSION_CONFLICT',
                'value': 5
            },
            {
                'documentation': {
                    'description': 'Channel not available'
                },
                'name': 'NISE_VAL_CHANNEL_NOT_AVAILABLE',
                'value': 6
            },
            {
                'documentation': {
                    'description': 'Channels hardwired'
                },
                'name': 'NISE_VAL_CHANNELS_HARDWIRED',
                'value': 7
            }
        ]
    }
}
