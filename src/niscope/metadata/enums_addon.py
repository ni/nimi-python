# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

# We are not code genning enums that have been marked as obsolete prior to the initial
# Python API bindings release
# We also do not codegen enums associated with P2P or External Calibration since neither
# are supported in Python
enums_codegen_method = {
}

enums_additional_enums = {
    'BoolEnableDisable': {},  # Delete because boolean values only
    'BoolEnableDisableChan': {},  # Delete because boolean values only
    'BoolEnableDisableIQ': {},  # Delete because boolean values only
    'BoolEnableDisableRealtime': {},  # Delete because boolean values only
    'BoolEnableDisableTIS': {},  # Delete because boolean values only
}

# Override names that can't be directly converted from C names into valid Python names
enums_override_values = {
    'FlexFIRAntialiasFilterType': { 'values': {
        0: { 'python_name': 'FOURTYEIGHT_TAP_STANDARD', },
        1: { 'python_name': 'FOURTYEIGHT_TAP_HANNING', },
        2: { 'python_name': 'SIXTEEN_TAP_HANNING', },
        3: { 'python_name': 'EIGHT_TAP_HANNING', },
    }, },
}

# We explicitly don't start with enums_ since we don't want this merged. These will replace the existing enums
# Once NI Internal CAR #675174 is fixed, this can be removed along with the overwrite code in __init__.py
# (TODO): Jaleel: Update dictionary_name after issue#624
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
                'name': 'NISCOPE_VAL_VIDEO_480I_59_94_FIELDS_PER_SECOND',
                'value': 1010,
                'documentation': {
                    'description': '480 lines, interlaced, 59.94 fields per second',
                },
            },
            {
                'name': 'NISCOPE_VAL_VIDEO_480I_60_FIELDS_PER_SECOND',
                'value': 1011,
                'documentation': {
                    'description': '480 lines, interlaced, 60 fields per second',
                },
            },
            {
                'name': 'NISCOPE_VAL_VIDEO_480P_59_94_FRAMES_PER_SECOND',
                'value': 1015,
                'documentation': {
                    'description': '480 lines, progressive, 59.94 frames per second',
                },
            },
            {
                'name': 'NISCOPE_VAL_VIDEO_480P_60_FRAMES_PER_SECOND',
                'value': 1016,
                'documentation': {
                    'description': '480 lines, progressive,60 frames per second',
                },
            },
            {
                'name': 'NISCOPE_VAL_VIDEO_576I_50_FIELDS_PER_SECOND',
                'value': 1020,
                'documentation': {
                    'description': '576 lines, interlaced, 50 fields per second',
                },
            },
            {
                'name': 'NISCOPE_VAL_VIDEO_576P_50_FRAMES_PER_SECOND',
                'value': 1025,
                'documentation': {
                    'description': '576 lines, progressive, 50 frames per second',
                },
            },
            {
                'name': 'NISCOPE_VAL_VIDEO_720P_50_FRAMES_PER_SECOND',
                'value': 1031,
                'documentation': {
                    'description': '720 lines, progressive, 50 frames per second',
                },
            },
            {
                'name': 'NISCOPE_VAL_VIDEO_720P_59_94_FRAMES_PER_SECOND',
                'value': 1032,
                'documentation': {
                    'description': '720 lines, progressive, 59.94 frames per second',
                },
            },
            {
                'name': 'NISCOPE_VAL_VIDEO_720P_60_FRAMES_PER_SECOND',
                'value': 1033,
                'documentation': {
                    'description': '720 lines, progressive, 60 frames per second',
                },
            },
            {
                'name': 'NISCOPE_VAL_VIDEO_1080I_50_FIELDS_PER_SECOND',
                'value': 1040,
                'documentation': {
                    'description': '1,080 lines, interlaced, 50 fields per second',
                },
            },
            {
                'name': 'NISCOPE_VAL_VIDEO_1080I_59_94_FIELDS_PER_SECOND',
                'value': 1041,
                'documentation': {
                    'description': '1,080 lines, interlaced, 59.94 fields per second',
                },
            },
            {
                'name': 'NISCOPE_VAL_VIDEO_1080I_60_FIELDS_PER_SECOND',
                'value': 1042,
                'documentation': {
                    'description': '1,080 lines, interlaced, 60 fields per second',
                },
            },
            {
                'name': 'NISCOPE_VAL_VIDEO_1080P_24_FRAMES_PER_SECOND',
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
    'Option': {
        'values': [
            {
                'name': 'NISCOPE_VAL_SELF_CALIBRATE_ALL_CHANNELS',
                'value': 0,
                'documentation': {
                    'description': 'Self Calibrating all Channels',
                },
            },
            {
                'name': 'NISCOPE_VAL_RESTORE_EXTERNAL_CALIBRATION',
                'value': 1,
                'documentation': {
                    'description': 'Restore External Calibration.',
                },
            },
        ],
    },
    'ClearableMeasurement': {
        'values': [
            {
                'name':'ALL_MEASUREMENTS',
                'value':10000,
            },
            {
                'name':'MULTI_ACQ_VOLTAGE_HISTOGRAM',
                'value':4004,
            },
            {
                'name':'MULTI_ACQ_TIME_HISTOGRAM',
                'value':4005,
            },
            {
                'name':'MULTI_ACQ_AVERAGE',
                'value':4016,
            },
            {
                'name':'FREQUENCY',
                'value':2,
            },
            {
                'name':'AVERAGE_FREQUENCY',
                'value':1016,
            },
            {
                'name':'FFT_FREQUENCY',
                'value':1008,
            },
            {
                'name':'PERIOD',
                'value':3,
            },
            {
                'name':'AVERAGE_PERIOD',
                'value':1015,
            },
            {
                'name':'RISE_TIME',
                'value':0,
            },
            {
                'name':'FALL_TIME',
                'value':1,
            },
            {
                'name':'RISE_SLEW_RATE',
                'value':1010,
            },
            {
                'name':'FALL_SLEW_RATE',
                'value':1011,
            },
            {
                'name':'OVERSHOOT',
                'value':18,
            },
            {
                'name':'PRESHOOT',
                'value':19,
            },
            {
                'name':'VOLTAGE_RMS',
                'value':4,
            },
            {
                'name':'VOLTAGE_CYCLE_RMS',
                'value':16,
            },
            {
                'name':'AC_ESTIMATE',
                'value':1012,
            },
            {
                'name':'FFT_AMPLITUDE',
                'value':1009,
            },
            {
                'name':'VOLTAGE_AVERAGE',
                'value':10,
            },
            {
                'name':'VOLTAGE_CYCLE_AVERAGE',
                'value':17,
            },
            {
                'name':'DC_ESTIMATE',
                'value':1013,
            },
            {
                'name':'VOLTAGE_MAX',
                'value':6,
            },
            {
                'name':'VOLTAGE_MIN',
                'value':7,
            },
            {
                'name':'VOLTAGE_PEAK_TO_PEAK',
                'value':5,
            },
            {
                'name':'VOLTAGE_HIGH',
                'value':8,
            },
            {
                'name':'VOLTAGE_LOW',
                'value':9,
            },
            {
                'name':'AMPLITUDE',
                'value':15,
            },
            {
                'name':'VOLTAGE_TOP',
                'value':1007,
            },
            {
                'name':'VOLTAGE_BASE',
                'value':1006,
            },
            {
                'name':'VOLTAGE_BASE_TO_TOP',
                'value':1017,
            },
            {
                'name':'WIDTH_NEG',
                'value':11,
            },
            {
                'name':'WIDTH_POS',
                'value':12,
            },
            {
                'name':'DUTY_CYCLE_NEG',
                'value':13,
            },
            {
                'name':'DUTY_CYCLE_POS',
                'value':14,
            },
            {
                'name':'INTEGRAL',
                'value':1005,
            },
            {
                'name':'AREA',
                'value':1003,
            },
            {
                'name':'CYCLE_AREA',
                'value':1004,
            },

            {
                'name':'TIME_DELAY',
                'value':1014,
            },
            {
                'name':'PHASE_DELAY',
                'value':1018,
            },
            {
                'name':'LOW_REF_VOLTS',
                'value':1000,
            },
            {
                'name':'MID_REF_VOLTS',
                'value':1001,
            },
            {
                'name':'HIGH_REF_VOLTS',
                'value':1002,
            },
            {
                'name':'VOLTAGE_HISTOGRAM_MEAN',
                'value':2000,
            },
            {
                'name':'VOLTAGE_HISTOGRAM_STDEV',
                'value':2001,
            },
            {
                'name':'VOLTAGE_HISTOGRAM_MEDIAN',
                'value':2003,
            },
            {
                'name':'VOLTAGE_HISTOGRAM_MODE',
                'value':2010,
            },
            {
                'name':'VOLTAGE_HISTOGRAM_MAX',
                'value':2005,
            },
            {
                'name':'VOLTAGE_HISTOGRAM_MIN',
                'value':2006,
            },
            {
                'name':'VOLTAGE_HISTOGRAM_PEAK_TO_PEAK',
                'value':2002,
            },
            {
                'name':'VOLTAGE_HISTOGRAM_MEAN_PLUS_STDEV',
                'value':2007,
            },
            {
                'name':'VOLTAGE_HISTOGRAM_MEAN_PLUS_2_STDEV',
                'value':2008,
            },
            {
                'name':'VOLTAGE_HISTOGRAM_MEAN_PLUS_3_STDEV',
                'value':2009,
            },
            {
                'name':'VOLTAGE_HISTOGRAM_HITS',
                'value':2004,
            },
            {
                'name':'VOLTAGE_HISTOGRAM_NEW_HITS',
                'value':2011,
            },
            {
                'name':'TIME_HISTOGRAM_MEAN',
                'value':3000,
            },
            {
                'name':'TIME_HISTOGRAM_STDEV',
                'value':3001,
            },
            {
                'name':'TIME_HISTOGRAM_MEDIAN',
                'value':3003,
            },
            {
                'name':'TIME_HISTOGRAM_MODE',
                'value':3010,
            },
            {
                'name':'TIME_HISTOGRAM_MAX',
                'value':3005,
            },
            {
                'name':'TIME_HISTOGRAM_MIN',
                'value':3006,
            },
            {
                'name':'TIME_HISTOGRAM_PEAK_TO_PEAK',
                'value':3002,
            },
            {
                'name':'TIME_HISTOGRAM_MEAN_PLUS_STDEV',
                'value':3007,
            },
            {
                'name':'TIME_HISTOGRAM_MEAN_PLUS_2_STDEV',
                'value':3008,
            },
            {
                'name':'TIME_HISTOGRAM_MEAN_PLUS_3_STDEV',
                'value':3009,
            },
            {
                'name':'TIME_HISTOGRAM_HITS',
                'value':3004,
            },
            {
                'name':'TIME_HISTOGRAM_NEW_HITS',
                'value':3011,
            },
        ],
    },
    'ExportableSignals': {
        'values': [
            {
                'name': 'NISCOPE_VAL_START_TRIGGER',
                'value': 2,
            },
            {
                'name': 'NISCOPE_VAL_ADVANCE_TRIGGER',
                'value': 5,
            },
            {
                'name': 'NISCOPE_VAL_REF_TRIGGER',
                'value': 1,
            },
            {
                'name': 'NISCOPE_VAL_END_OF_RECORD_EVENT',
                'value': 4,
            },
            {
                'name': 'NISCOPE_VAL_END_OF_ACQUISITION_EVENT',
                'value': 3,
            },
            {
                'name': 'NISCOPE_VAL_READY_FOR_START_EVENT',
                'value': 7,
            },
            {
                'name': 'NISCOPE_VAL_READY_FOR_ADVANCE_EVENT',
                'value': 6,
            },
            {
                'name': 'NISCOPE_VAL_READY_FOR_REF_EVENT',
                'value': 10,
            },
            {
                'name': 'NISCOPE_VAL_REF_CLOCK',
                'value': 100,
            },
            {
                'name': 'NISCOPE_VAL_SAMPLE_CLOCK',
                'value': 101,
            },
            {
                'name': 'NISCOPE_VAL_5V_OUT',
                'python_name': 'FIVE_V_OUT',
                'value': 13,
            },
        ],
    },
    'WhichTrigger': {
        'values': [
            {
                'name': 'NISCOPE_VAL_SOFTWARE_TRIGGER_START',
                'value': 0,
            },
            {
                'name': 'NISCOPE_VAL_SOFTWARE_TRIGGER_ARM_REFERENCE',
                'value': 1,
            },
            {
                'name': 'NISCOPE_VAL_SOFTWARE_TRIGGER_REFERENCE',
                'value': 2,
            },
            {
                'name': 'NISCOPE_VAL_SOFTWARE_TRIGGER_ADVANCE',
                'value': 3,
            },
        ],
    },
    'ScalarMeasurement': {
        'values': [
            {
                'name': 'NISCOPE_VAL_NO_MEASUREMENT',
                'value': 4000,
                'documentation': {
                    'description': 'None',
                },
            },
            {
                'name': 'NISCOPE_VAL_FREQUENCY',
                'value': 2,
            },
            {
                'name': 'NISCOPE_VAL_AVERAGE_FREQUENCY',
                'value': 1016,
            },
            {
                'name': 'NISCOPE_VAL_FFT_FREQUENCY',
                'value': 1008,
            },
            {
                'name': 'NISCOPE_VAL_PERIOD',
                'value': 3,
            },
            {
                'name': 'NISCOPE_VAL_AVERAGE_PERIOD',
                'value': 1015,
            },
            {
                'name': 'NISCOPE_VAL_RISE_TIME',
                'value': 0,
            },
            {
                'name': 'NISCOPE_VAL_FALL_TIME',
                'value': 1,
            },
            {
                'name': 'NISCOPE_VAL_RISE_SLEW_RATE',
                'value': 1010,
            },
            {
                'name': 'NISCOPE_VAL_FALL_SLEW_RATE',
                'value': 1011,
            },
            {
                'name': 'NISCOPE_VAL_OVERSHOOT',
                'value': 18,
            },
            {
                'name': 'NISCOPE_VAL_PRESHOOT',
                'value': 19,
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_RMS',
                'value': 4,
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_CYCLE_RMS',
                'value': 16,
            },
            {
                'name': 'NISCOPE_VAL_AC_ESTIMATE',
                'value': 1012,
            },
            {
                'name': 'NISCOPE_VAL_FFT_AMPLITUDE',
                'value': 1009,
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_AVERAGE',
                'value': 10,
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_CYCLE_AVERAGE',
                'value': 17,
            },
            {
                'name': 'NISCOPE_VAL_DC_ESTIMATE',
                'value': 1013,
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_MAX',
                'value': 6,
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_MIN',
                'value': 7,
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_PEAK_TO_PEAK',
                'value': 5,
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HIGH',
                'value': 8,
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_LOW',
                'value': 9,
            },
            {
                'name': 'NISCOPE_VAL_AMPLITUDE',
                'value': 15,
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_TOP',
                'value': 1007,
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_BASE',
                'value': 1006,
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_BASE_TO_TOP',
                'value': 1017,
            },
            {
                'name': 'NISCOPE_VAL_WIDTH_NEG',
                'value': 11,
            },
            {
                'name': 'NISCOPE_VAL_WIDTH_POS',
                'value': 12,
            },
            {
                'name': 'NISCOPE_VAL_DUTY_CYCLE_NEG',
                'value': 13,
            },
            {
                'name': 'NISCOPE_VAL_DUTY_CYCLE_POS',
                'value': 14,
            },
            {
                'name': 'NISCOPE_VAL_INTEGRAL',
                'value': 1005,
            },
            {
                'name': 'NISCOPE_VAL_AREA',
                'value': 1003,
            },
            {
                'name': 'NISCOPE_VAL_CYCLE_AREA',
                'value': 1004,
            },
            {
                'name': 'NISCOPE_VAL_TIME_DELAY',
                'value': 1014,
            },
            {
                'name': 'NISCOPE_VAL_PHASE_DELAY',
                'value': 1018,
            },
            {
                'name': 'NISCOPE_VAL_LOW_REF_VOLTS',
                'value': 1000,
            },
            {
                'name': 'NISCOPE_VAL_MID_REF_VOLTS',
                'value': 1001,
            },
            {
                'name': 'NISCOPE_VAL_HIGH_REF_VOLTS',
                'value': 1002,
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN',
                'value': 2000,
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_STDEV',
                'value': 2001,
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEDIAN',
                'value': 2003,
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_MODE',
                'value': 2010,
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_MAX',
                'value': 2005,
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_MIN',
                'value': 2006,
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_PEAK_TO_PEAK',
                'value': 2002,
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN_PLUS_STDEV',
                'value': 2007,
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN_PLUS_2_STDEV',
                'value': 2008,
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN_PLUS_3_STDEV',
                'value': 2009,
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_HITS',
                'value': 2004,
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_NEW_HITS',
                'value': 2011,
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_MEAN',
                'value': 3000,
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_STDEV',
                'value': 3001,
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_MEDIAN',
                'value': 3003,
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_MODE',
                'value': 3010,
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_MAX',
                'value': 3005,
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_MIN',
                'value': 3006,
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_PEAK_TO_PEAK',
                'value': 3002,
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_MEAN_PLUS_STDEV',
                'value': 3008,
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_MEAN_PLUS_2_STDEV',
                'value': 3009,
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_HITS',
                'value': 3004,
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_NEW_HITS',
                'value': 3011,
            },
        ],
    },
    'AcquisitionStatus': {
        'values': [
            {
                'name': 'NISCOPE_VAL_ACQ_COMPLETE',
                'value': 1,
            },
            {
                'name': 'NISCOPE_VAL_ACQ_IN_PROGRESS',
                'value': 0,
            },
            {
                'name': 'NISCOPE_VAL_ACQ_STATUS_UNKNOWN',
                'value': -1,
            },
        ],
    },
    'ArrayMeasurement': {
        'values': [
            {
                'name': 'NISCOPE_VAL_NO_MEASUREMENT',
                'value': 4000,
                'documentation': {
                    'description': 'None',
                },
            },
            {
                'name': 'NISCOPE_VAL_LAST_ACQ_HISTOGRAM',
                'value': 4001,
                'documentation': {
                    'description': 'Last Acquisition Histogram ',
                },
            },
            {
                'name': 'NISCOPE_VAL_MULTI_ACQ_VOLTAGE_HISTOGRAM',
                'value': 4004,
                'documentation': {
                    'description': 'Multi Acquisition Voltage Histogram',
                },
            },
            {
                'name': 'NISCOPE_VAL_MULTI_ACQ_TIME_HISTOGRAM',
                'value': 4005,
                'documentation': {
                    'description': 'Multi Acquisition Time Histogram',
                },
            },
            {
                'name': 'NISCOPE_VAL_MULTI_ACQ_AVERAGE',
                'value': 4016,
                'documentation': {
                    'description': 'Multi Acquisition Average',
                },
            },
            {
                'name': 'NISCOPE_VAL_POLYNOMIAL_INTERPOLATION',
                'value': 4011,
                'documentation': {
                    'description': 'Polynomial Interpolation',
                },
            },
            {
                'name': 'NISCOPE_VAL_ARRAY_INTEGRAL',
                'value': 4006,
                'documentation': {
                    'description': 'Array Integral',
                },
            },
            {
                'name': 'NISCOPE_VAL_DERIVATIVE',
                'value': 4007,
                'documentation': {
                    'description': 'Derivative',
                },
            },
            {
                'name': 'NISCOPE_VAL_INVERSE',
                'value': 4008,
                'documentation': {
                    'description': 'Inverse',
                },
            },
            {
                'name': 'NISCOPE_VAL_MULTIPLY_CHANNELS',
                'value': 4012,
                'documentation': {
                    'description': 'Multiply Channels',
                },
            },
            {
                'name': 'NISCOPE_VAL_ADD_CHANNELS',
                'value': 4013,
                'documentation': {
                    'description': 'Add Channels',
                },
            },
            {
                'name': 'NISCOPE_VAL_SUBTRACT_CHANNELS',
                'value': 4014,
                'documentation': {
                    'description': 'Subtract Channels',
                },
            },
            {
                'name': 'NISCOPE_VAL_DIVIDE_CHANNELS',
                'value': 4015,
                'documentation': {
                    'description': 'Divide Channels',
                },
            },
            {
                'name': 'NISCOPE_VAL_ARRAY_OFFSET',
                'value': 4025,
                'documentation': {
                    'description': 'Array Offset',
                },
            },
            {
                'name': 'NISCOPE_VAL_ARRAY_GAIN',
                'value': 4026,
                'documentation': {
                    'description': 'Array Gain',
                },
            },
            {
                'name': 'NISCOPE_VAL_HANNING_WINDOW',
                'value': 4009,
                'documentation': {
                    'description': 'Hanning Window',
                },
            },
            {
                'name': 'NISCOPE_VAL_FLAT_TOP_WINDOW',
                'value': 4010,
                'documentation': {
                    'description': 'Flat Top Window',
                },
            },
            {
                'name': 'NISCOPE_VAL_HAMMING_WINDOW',
                'value': 4020,
                'documentation': {
                    'description': 'Hamming Window',
                },
            },
            {
                'name': 'NISCOPE_VAL_TRIANGLE_WINDOW',
                'value': 4023,
                'documentation': {
                    'description': 'Triangle Window',
                },
            },
            {
                'name': 'NISCOPE_VAL_BLACKMAN_WINDOW',
                'value': 4024,
                'documentation': {
                    'description': 'Blackman Window',
                },
            },
            {
                'name': 'NISCOPE_VAL_WINDOWED_FIR_FILTER',
                'value': 4021,
                'documentation': {
                    'description': 'FIR Windowed Filter',
                },
            },
            {
                'name': 'NISCOPE_VAL_BESSEL_FILTER',
                'value': 4022,
                'documentation': {
                    'description': 'Bessel IIR Filter',
                },
            },
            {
                'name': 'NISCOPE_VAL_BUTTERWORTH_FILTER',
                'value': 4017,
                'documentation': {
                    'description': 'Butterworth IIR Filter',
                },
            },
            {
                'name': 'NISCOPE_VAL_CHEBYSHEV_FILTER',
                'value': 4018,
                'documentation': {
                    'description': 'Chebyshev IIR Filter',
                },
            },
            {
                'name': 'NISCOPE_VAL_FFT_PHASE_SPECTRUM',
                'value': 4002,
                'documentation': {
                    'description': 'FFT Phase Spectrum',
                },
            },
            {
                'name': 'NISCOPE_VAL_FFT_AMP_SPECTRUM_VOLTS_RMS',
                'value': 4003,
                'documentation': {
                    'description': 'FFT Amp. Spectrum (Volts RMS)',
                },
            },
            {
                'name': 'NISCOPE_VAL_FFT_AMP_SPECTRUM_DB',
                'value': 4019,
                'documentation': {
                    'description': 'FFT Amp. Spectrum (dB)',
                },
            },
        ],
    },
}
