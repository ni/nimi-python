# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

# We are not code genning enums that have been marked as obsolete prior to the initial
# Python API bindings release
# We also do not codegen enums associated with P2P or External Calibration since neither 
# are supported in Python
enums_codegen_method = {
}

replacement_enums = {
    'DigitsResolution': {
        'values': [
            {
                'name': 'NIDMM_VAL_DIGITS_RESOLUTION_THREEPOINTFIVE',
                'value': 3.5,
            },
            {
                'name': 'NIDMM_VAL_DIGITS_RESOLUTION_FOURPOINTFIVE',
                'value': 4.5,
            },
            {
                'name': 'NIDMM_VAL_DIGITS_RESOLUTION_FIVEPOINTFIVE',
                'value': 5.5,
            },
            {
                'name': 'NIDMM_VAL_DIGITS_RESOLUTION_SIXPOINTFIVE',
                'value': 6.5,
            },
            {
                'name': 'NIDMM_VAL_DIGITS_RESOLUTION_SEVENPOINTFIVE',
                'value': 7.5,
            },
        ],
    },
}
