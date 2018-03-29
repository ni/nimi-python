# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

# We are not code genning enums that have been marked as obsolete prior to the initial
# Python API bindings release
# We also do not codegen enums associated with P2P or External Calibration since neither 
# are supported in Python
enums_codegen_method = {
    'CalADCInput': { 'codegen_method': 'no', },  # Calibration Enum - not supported in Python
}

enums_additional_enums = {
    'RelativeTo': {
        'values': [
            {
                'name': 'NIFGEN_VAL_WAVEFORM_POSITION_START',
                'value': 0,
            },
            {
                'name': 'NIFGEN_VAL_WAVEFORM_POSITION_CURRENT',
                'value': 1,
            },
        ],
    },
    'TriggerWhen': {
        'values': [
            {
                'name': 'NIFGEN_VAL_ACTIVE_HIGH',
                'value': 101,
            },
            {
                'name': 'NIFGEN_VAL_ACTIVE_LOW',
                'value': 102,
            },
        ],
    },
    'ByteOrder': {
        'values': [
            {
                'name': 'NIFGEN_VAL_LITTLE_ENDIAN',
                'value': 0,
            },
            {
                'name': 'NIFGEN_VAL_BIG_ENDIAN',
                'value': 1,
            },
        ],
    },
    'Signal': {
        'values': [
            {
                'name': 'NIFGEN_VAL_ONBOARD_REFERENCE_CLOCK',
                'value': 1019,
            },
            {
                'name': 'NIFGEN_VAL_SYNC_OUT',
                'value': 1002,
            },
            {
                'name': 'NIFGEN_VAL_START_TRIGGER',
                'value': 1004,
            },
            {
                'name': 'NIFGEN_VAL_MARKER_EVENT',
                'value': 1001,
            },
            {
                'name': 'NIFGEN_VAL_SAMPLE_CLOCK_TIMEBASE',
                'value': 1006,
            },
            {
                'name': 'NIFGEN_VAL_SYNCHRONIZATION',
                'value': 1007,
            },
            {
                'name': 'NIFGEN_VAL_SAMPLE_CLOCK',
                'value': 101,
            },
            {
                'name': 'NIFGEN_VAL_REFERENCE_CLOCK',
                'value': 102,
            },
            {
                'name': 'NIFGEN_VAL_SCRIPT_TRIGGER',
                'value': 103,
            },
            {
                'name': 'NIFGEN_VAL_READY_FOR_START_EVENT',
                'value': 105,
            },
            {
                'name': 'NIFGEN_VAL_STARTED_EVENT',
                'value': 106,
            },
            {
                'name': 'NIFGEN_VAL_DONE_EVENT',
                'value': 107,
            },
            {
                'name': 'NIFGEN_VAL_DATA_MARKER_EVENT',
                'value': 108,
            },
        ],
    },
    'HardwareState': {
        'values': [
            {
                'name': 'NIFGEN_VAL_IDLE',
                'value': 0,
            },
            {
                'name': 'NIFGEN_VAL_WAITING_FOR_START_TRIGGER',
                'value': 1,
            },
            {
                'name': 'NIFGEN_VAL_RUNNING',
                'value': 2,
            },
            {
                'name': 'NIFGEN_VAL_DONE',
                'value': 3,
            },
            {
                'name': 'NIFGEN_VAL_HARDWARE_ERROR',
                'value': 4,
            },
        ],
    },
}

# TODO(bhaswath): Move this enum together with other enums once Issue #624 is fixed.
replacement_enums = {
    'Trigger': {
        'values': [
            {
                'name': 'NIFGEN_VAL_START_TRIGGER',
                'value': 1004,
            },
            {
                'name': 'NIFGEN_VAL_SCRIPT_TRIGGER',
                'value': 103,
            },
        ],
    },
}
