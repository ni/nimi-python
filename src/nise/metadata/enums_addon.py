# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here.
# We are not code genning enums that have been marked as obsolete prior to the initial
# Python API bindings release
# We also do not codegen enums associated with P2P or External Calibration since neither 
# are supported in Python
enums_codegen_method = {
}

# Need additional enums for functions that use enums. Enum names & values come from LabVIEW API
enums_additional_enums = {
    'MulticonnectMode': {
        'values': [
            {
                'name': 'DEFAULT',
                'value': -1,
'documentation': {
'description': 'Default',
},
            },
            {
                'name': 'NO_MULTICONNECT',
                'value': 0,
'documentation': {
'description': 'No multiconnect',
},
            },
            {
                'name': 'MULTICONNECT',
                'value': 1,
'documentation': {
'description': 'Multiconnect',
},
            },
        ],
    },
    'OperationOrder': {
        'values': [
            {
                'name': 'BREAK_BEFORE_MAKE',
                'value': 1,
'documentation': {
'description': 'Break before make',
},
            },
            {
                'name': 'BREAK_AFTER_MAKE',
                'value': 2,
'documentation': {
'description': 'Break after make',
},
            },
        ],
    },
    'ExpandAction': {
        'values': [
            {
                'name': 'EXPAND_TO_ROUTES',
                'value': 0,
'documentation': {
'description': 'Expand to routes',
},
            },
            {
                'name': 'EXPAND_TO_PATHS',
                'value': 1,
'documentation': {
'description': 'Expand to paths',
},
            },
        ],
    },
    'PathCapability': {
        'values': [
            {
                'name': 'PATH_NEEDS_HARDWIRE',
                'value': -2,
'documentation': {
'description': 'Path needs hardwire',
},
            },
            {
                'name': 'PATH_NEEDS_CONFIG_CHANNEL',
                'value': -1,
'documentation': {
'description': 'Path needs config channel',
},
            },
            {
                'name': 'PATH_AVAILABLE',
                'value': 1,
'documentation': {
'description': 'Path available',
},
            },
            {
                'name': 'PATH_EXISTS',
                'value': 2,
'documentation': {
'description': 'Path exists',
},
            },
            {
                'name': 'PATH_UNSUPPORTED',
                'value': 3,
'documentation': {
'description': 'Path Unsupported',
},
            },
            {
                'name': 'RESOURCE_IN_USE',
                'value': 4,
'documentation': {
'description': 'Resource in use',
},
            },
            {
                'name': 'EXCLUSION_CONFLICT',
                'value': 5,
'documentation': {
'description': 'Exclusion conflict',
},
            },
            {
                'name': 'CHANNEL_NOT_AVAILABLE',
                'value': 6,
'documentation': {
'description': 'Channel not available',
},
            },
            {
                'name': 'CHANNELS_HARDWIRED',
                'value': 7,
'documentation': {
'description': 'Channels hardwired',
},
            },
        ],
    },
}
