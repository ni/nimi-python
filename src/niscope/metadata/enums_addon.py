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
                'name': 'NTSC',
                'value': 1,
'documentation': {
'description': 'NTSC signal format supports line numbers from 1 to 525',
},
            },
            {
                'name': 'PAL',
                'value': 2,
'documentation': {
'description': 'PAL signal format supports line numbers from 1 to 625',
},
            },
            {
                'name': 'SECAM',
                'value': 3,
'documentation': {
'description': 'SECAM signal format supports line numbers from 1 to 625',
},
            },
            {
                'name': 'M_PAL',
                'value': 1001,
'documentation': {
'description': 'M-PAL signal format supports line numbers from 1 to 525',
},
            },
            {
                'name': '_480I_59_94_FIELDS_PER_SECOND',
                'value': 1010,
'documentation': {
'description': '480 lines, interlaced, 59.94 fields per second',
},
            },
            {
                'name': '_480I_60_FIELDS_PER_SECOND',
                'value': 1011,
'documentation': {
'description': '480 lines, interlaced, 60 fields per second',
},
            },
            {
                'name': '_480P_59_94_FRAMES_PER_SECOND',
                'value': 1015,
'documentation': {
'description': '480 lines, progressive, 59.94 frames per second',
},
            },
            {
                'name': '_480P_60_FRAMES_PER_SECOND',
                'value': 1016,
'documentation': {
'description': '480 lines, progressive,60 frames per second',
},
            },
            {
                'name': '_576I_50_FIELDS_PER_SECOND',
                'value': 1020,
'documentation': {
'description': '576 lines, interlaced, 50 fields per second',
},
            },
            {
                'name': '_576P_50_FRAMES_PER_SECOND',
                'value': 1025,
'documentation': {
'description': '576 lines, progressive, 50 frames per second',
},
            },
            {
                'name': '_720P_50_FRAMES_PER_SECOND',
                'value': 1031,
'documentation': {
'description': '720 lines, progressive, 50 frames per second',
},
            },
            {
                'name': '_720P_59_94_FRAMES_PER_SECOND',
                'value': 1032,
'documentation': {
'description': '720 lines, progressive, 59.94 frames per second',
},
            },
            {
                'name': '_720P_60_FRAMES_PER_SECOND',
                'value': 1033,
'documentation': {
'description': '720 lines, progressive, 60 frames per second',
},
            },
            {
                'name': '_1080I_50_FIELDS_PER_SECOND',
                'value': 1040,
'documentation': {
'description': '1,080 lines, interlaced, 50 fields per second',
},
            },
            {
                'name': '_1080I_59_94_FIELDS_PER_SECOND',
                'value': 1041,
'documentation': {
'description': '1,080 lines, interlaced, 59.94 fields per second',
},
            },
            {
                'name': '_1080I_60_FIELDS_PER_SECOND',
                'value': 1042,
'documentation': {
'description': '1,080 lines, interlaced, 60 fields per second',
},
            },
            {
                'name': '_1080P_24_FRAMES_PER_SECOND',
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
                'name': 'AC',
                'value': 0,
'documentation': {
'description': 'AC coupling',
},
            },
            {
                'name': 'DC',
                'value': 1,
'documentation': {
'description': 'DC coupling',
},
            },
            {
                'name': 'HF_REJECT',
                'value': 2,
'documentation': {
'description': 'Highpass filter coupling',
},
            },
            {
                'name': 'LF_REJECT',
                'value': 3,
'documentation': {
'description': 'Lowpass filter coupling',
},
            },
            {
                'name': 'AC_PLUS_HF_REJECT',
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
                'name': 'SELF_CALIBRATE_ALL_CHANNELS',
                'value': 0,
                'documentation': {
                    'description': 'Self Calibrating all Channels',
                },
            },
            {
                'name': 'RESTORE_EXTERNAL_CALIBRATION',
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
   'TriggerSourceDigital': {
        'values': [
            {
                'name': 'RTSI_0',
                'value': 'VAL_RTSI_0',
            },
            {
                'name': 'RTSI_1',
                'value': 'VAL_RTSI_1',
            },
            {
                'name': 'RTSI_2',
                'value': 'VAL_RTSI_2',
            },
            {
                'name': 'RTSI_3',
                'value': 'VAL_RTSI_3',
            },
            {
                'name': 'RTSI_4',
                'value': 'VAL_RTSI_4',
            },
            {
                'name': 'RTSI_5',
                'value': 'VAL_RTSI_5',
            },
            {
                'name': 'RTSI_6',
                'value': 'VAL_RTSI_6',
            },
            {
                'name': 'PFI_0',
                'value': 'VAL_PFI_0',
            },
            {
                'name': 'PFI_1',
                'value': 'VAL_PFI_1',
            },
            {
                'name': 'PFI_2',
                'value': 'VAL_PFI_2',
            },
            {
                'name': 'PXI_STAR',
                'value': 'VAL_PXI_STAR',
            },
            {
                'name': 'AUX_0_PFI_0',
                'value': 'VAL_AUX_0_PFI_0',
            },
            {
                'name': 'AUX_0_PFI_1',
                'value': 'VAL_AUX_0_PFI_1',
            },
            {
                'name': 'AUX_0_PFI_2',
                'value': 'VAL_AUX_0_PFI_2',
            },
            {
                'name': 'AUX_0_PFI_3',
                'value': 'VAL_AUX_0_PFI_3',
            },
            {
                'name': 'AUX_0_PFI_4',
                'value': 'VAL_AUX_0_PFI_4',
            },
            {
                'name': 'AUX_0_PFI_5',
                'value': 'VAL_AUX_0_PFI_5',
            },
            {
                'name': 'VAL_AUX_0_PFI_6',
                'value': 'VAL_AUX_0_PFI_6',
            },
            {
                'name': 'VAL_AUX_0_PFI_7',
                'value': 'VAL_AUX_0_PFI_7',
            },
        ],
    },
   'TriggerSource': {
        'values': [
            {
                'name': 'Channel_0',
                'value': 0,
            },
            {
                'name': 'Channel_1',
                'value': 1,
            },
            {
                'name': 'Channel_2',
                'value': 2,
            },
            {
                'name': 'Channel_3',
                'value': 3,
            },
            {
                'name': 'Channel_4',
                'value': 4,
            },
            {
                'name': 'Channel_5',
                'value': 5,
            },
            {
                'name': 'Channel_6',
                'value': 6,
            },
            {
                'name': 'Channel_7',
                'value': 7,
            },
            {
                'name': 'VAL_EXTERNAL',
                'value': 'VAL_EXTERNAL',
            },
        ],
    },
}
