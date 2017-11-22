# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

# We are not code genning enums that have been marked as obsolete prior to the initial
# Python API bindings release
# We also do not codegen enums associated with P2P or External Calibration since neither 
# are supported in Python
enums_codegen_method = {
}

# We explicitly don't start with enums_ since we don't want this merged. These will replace the existing enums
# Once NI Internal CAR #675174 is fixed, this can be removed along with the overwrite code in __init__.py
replacement_enums = {
    'VideoSignalFormat': {
        'values': [
            {
                'name': 'NISCOPE_VAL_NTSC',
                'value': 1,
'documentation': {
'description': 'NTSC signal format supports line numbers from 1 to 525',
},
            },
            {
                'name': 'NISCOPE_VAL_PAL',
                'value': 2,
'documentation': {
'description': 'PAL signal format supports line numbers from 1 to 625',
},
            },
            {
                'name': 'NISCOPE_VAL_SECAM',
                'value': 3,
'documentation': {
'description': 'SECAM signal format supports line numbers from 1 to 625',
},
            },
            {
                'name': 'NISCOPE_VAL_M_PAL',
                'value': 1001,
'documentation': {
'description': 'M-PAL signal format supports line numbers from 1 to 525',
},
            },
            {
                'name': 'NISCOPE_VAL_480I_59_94_FIELDS_PER_SECOND',
                'value': 1010,
'documentation': {
'description': '480 lines, interlaced, 59.94 fields per second',
},
            },
            {
                'name': 'NISCOPE_VAL_480I_60_FIELDS_PER_SECOND',
                'value': 1011,
'documentation': {
'description': '480 lines, interlaced, 60 fields per second',
},
            },
            {
                'name': 'NISCOPE_VAL_480P_59_94_FRAMES_PER_SECOND',
                'value': 1015,
'documentation': {
'description': '480 lines, progressive, 59.94 frames per second',
},
            },
            {
                'name': 'NISCOPE_VAL_480P_60_FRAMES_PER_SECOND',
                'value': 1016,
'documentation': {
'description': '480 lines, progressive,60 frames per second',
},
            },
            {
                'name': 'NISCOPE_VAL_576I_50_FIELDS_PER_SECOND',
                'value': 1020,
'documentation': {
'description': '576 lines, interlaced, 50 fields per second',
},
            },
            {
                'name': 'NISCOPE_VAL_576P_50_FRAMES_PER_SECOND',
                'value': 1025,
'documentation': {
'description': '576 lines, progressive, 50 frames per second',
},
            },
            {
                'name': 'NISCOPE_VAL_720P_50_FRAMES_PER_SECOND',
                'value': 1031,
'documentation': {
'description': '720 lines, progressive, 50 frames per second',
},
            },
            {
                'name': 'NISCOPE_VAL_720P_59_94_FRAMES_PER_SECOND',
                'value': 1032,
'documentation': {
'description': '720 lines, progressive, 59.94 frames per second',
},
            },
            {
                'name': 'NISCOPE_VAL_720P_60_FRAMES_PER_SECOND',
                'value': 1033,
'documentation': {
'description': '720 lines, progressive, 60 frames per second',
},
            },
            {
                'name': 'NISCOPE_VAL_1080I_50_FIELDS_PER_SECOND',
                'value': 1040,
'documentation': {
'description': '1,080 lines, interlaced, 50 fields per second',
},
            },
            {
                'name': 'NISCOPE_VAL_1080I_59_94_FIELDS_PER_SECOND',
                'value': 1041,
'documentation': {
'description': '1,080 lines, interlaced, 59.94 fields per second',
},
            },
            {
                'name': 'NISCOPE_VAL_1080I_60_FIELDS_PER_SECOND',
                'value': 1042,
'documentation': {
'description': '1,080 lines, interlaced, 60 fields per second',
},
            },
            {
                'name': 'NISCOPE_VAL_1080P_24_FRAMES_PER_SECOND',
                'value': 1045,
'documentation': {
'description': '1,080 lines, progressive, 24 frames per second',
},
            },
        ],
    },
    'TriggerCoupling': {
        'values': [
            {
                'name': 'NISCOPE_VAL_AC',
                'value': 0,
'documentation': {
'description': 'AC coupling',
},
            },
            {
                'name': 'NISCOPE_VAL_DC',
                'value': 1,
'documentation': {
'description': 'DC coupling',
},
            },
            {
                'name': 'NISCOPE_VAL_HF_REJECT',
                'value': 2,
'documentation': {
'description': 'Highpass filter coupling',
},
            },
            {
                'name': 'NISCOPE_VAL_LF_REJECT',
                'value': 3,
'documentation': {
'description': 'Lowpass filter coupling',
},
            },
            {
                'name': 'NISCOPE_VAL_AC_PLUS_HF_REJECT',
                'value': 1001,
'documentation': {
'description': 'Highpass and lowpass filter coupling',
},
            },
        ],
    },
}
