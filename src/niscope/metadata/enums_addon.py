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
    'ArrayMeasurement': {
        'values': [
            #{  # (TODO) Jaleel: Recheck after Issue#618 fixed
            #    'name': "None",
            #    'value': 4000,
            #    'documentation': {
            #        'description': 'None',
            #    },
            #},
            {
                'name': 'Last_Acq._Histogram',
                'value': 4001,
                'documentation': {
                    'description': 'Last Acquisition Histogram ',
                },
            },
            {
                'name': 'Multi_Acq._Voltage_Histogram',
                'value': 4004,
                'documentation': {
                    'description': 'Multi Acquisition Voltage Histogram',
                },
            },
            {
                'name': 'Multi_Acq._Time_Histogram',
                'value': 4005,
                'documentation': {
                    'description': 'Multi Acquisition Time Histogram',
                },
            },
            {
                'name': 'Multi_Acq._Average',
                'value': 4016,
                'documentation': {
                    'description': 'Multi Acquisition Average',
                },
            },
            {
                'name': 'Polynomial_Interpolation',
                'value': 4011,
                'documentation': {
                    'description': 'Polynomial Interpolation',
                },
            },
            {
                'name': 'Array_Integral',
                'value': 4006,
                'documentation': {
                    'description': 'Array Integral',
                },
            },
            {
                'name': 'Derivative',
                'value': 4007,
                'documentation': {
                    'description': 'Derivative',
                },
            },
            {
                'name': 'Inverse',
                'value': 4008,
                'documentation': {
                    'description': 'Inverse',
                },
            },
            {
                'name': 'Multiply_Channels',
                'value': 4012,
                'documentation': {
                    'description': 'Multiply Channels',
                },
            },
            {
                'name': 'Add_Channels',
                'value': 4013,
                'documentation': {
                    'description': 'Add Channels',
                },
            },
            {
                'name': 'Subtract_Channels',
                'value': 4014,
                'documentation': {
                    'description': 'Subtract Channels',
                },
            },
            {
                'name': 'Divide_Channels',
                'value': 4015,
                'documentation': {
                    'description': 'Divide Channels',
                },
            },
            {
                'name': 'Array_Offset',
                'value': 4025,
                'documentation': {
                    'description': 'Array Offset',
                },
            },
            {
                'name': 'Array_Gain',
                'value': 4026,
                'documentation': {
                    'description': 'Array Gain',
                },
            },
            {
                'name': 'Hanning_Window',
                'value': 4009,
                'documentation': {
                    'description': 'Hanning Window',
                },
            },
            {
                'name': 'Flat_Top_Window',
                'value': 4010,
                'documentation': {
                    'description': 'Flat Top Window',
                },
            },
            {
                'name': 'Hamming_Window',
                'value': 4020,
                'documentation': {
                    'description': 'Hamming Window',
                },
            },
            {
                'name': 'Triangle_Window',
                'value': 4023,
                'documentation': {
                    'description': 'Triangle Window',
                },
            },
            {
                'name': 'Blackman_Window',
                'value': 4024,
                'documentation': {
                    'description': 'Blackman Window',
                },
            },
            {
                'name': 'FIR_Windowed_Filter',
                'value': 4021,
                'documentation': {
                    'description': 'FIR Windowed Filter',
                },
            },
            {
                'name': 'Bessel_IIR_Filter',
                'value': 4022,
                'documentation': {
                    'description': 'Bessel IIR Filter',
                },
            },
            {
                'name': 'Butterworth_IIR_Filter',
                'value': 4017,
                'documentation': {
                    'description': 'Butterworth IIR Filter',
                },
            },
            {
                'name': 'Chebyshev_IIR_Filter',
                'value': 4018,
                'documentation': {
                    'description': 'Chebyshev IIR Filter',
                },
            },
            {
                'name': 'FFT_Phase_Spectrum',
                'value': 4002,
                'documentation': {
                    'description': 'FFT Phase Spectrum',
                },
            },
            {
                'name': 'FFT_Amp._Spectrum_(Volts_RMS)',  # (TODO) Jaleel: Recheck after Issue#619 fixed
                'value': 4003,
                'documentation': {
                    'description': 'FFT Amp. Spectrum (Volts RMS)',
                },
            },
            {
                'name': 'FFT_Amp._Spectrum_(dB)',  
                'value': 4019,
                'documentation': {
                    'description': 'FFT Amp. Spectrum (dB)',
                },
            },
        ],
    },
    'Option': {
        'values': [
            {
                'name': 'Self_Calibrate_All_Channels',
                'value': 0,
                'documentation': {
                    'description': 'Self Calibrating all Channels',
                },
            },
            {
                'name': 'Restore_External_Calibration',
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
                'name':'All_Measurements',
                'value':10000,
            },
            {
                'name':'Multi_Acq._Voltage_Histogram',
                'value':4004,
            },
            {
                'name':'Multi_Acq._Time_Histogram',
                'value':4005,
            },
            {
                'name':'Multi_Acq._Average',
                'value':4016,
            },
            {
                'name':'Frequency',
                'value':2,
            },
            {
                'name':'Period',
                'value':3,
            },
            {
                'name':'Average_Period',
                'value':1015,
            },          
            {
                'name':'Rise_Time',
                'value':0,
            },
            {
                'name':'Fall_Time',
                'value':1,
            },          
            {
                'name':'Rising_Slew_Rate',
                'value':1010,
            },          
            {
                'name':'Falling_Slew_Rate',
                'value':1011,
            },          
            {
                'name':'Overshoot',
                'value':18,
            },          
            {
                'name':'Preshoot',
                'value':19,
            },          
            {
                'name':'Voltage_RMS',
                'value':4,
            },          
            {
                'name':'Voltage_Cycle_RMS',
                'value':16,
            },          
            {
                'name':'AC_Estimate',
                'value':1012,
            },          
            {
                'name':'FFT_Amplitude',
                'value':1009,
            },          
            {
                'name':'Voltage_Average',
                'value':10,
            },          
            {
                'name':'Voltage_Cycle_Average',
                'value':17,
            },          
            {
                'name':'DC_Estimate',
                'value':1013,
            },
            {
                'name':'Voltage_Max',
                'value':6,
            },
            {
                'name':'Voltage_Min',
                'value':7,
            },
            {
                'name':'Voltage_Peak-to-Peak',  # (TODO) Jaleel: Recheck after Issue#619 fixed
                'value':5,
            },  
            {
                'name':'Voltage_High',
                'value':8,
            },
            {
                'name':'Voltage_Low',
                'value':9,
            },
            {
                'name':'Voltage_Amplitude',
                'value':15,
            },
            {
                'name':'Voltage_Top',
                'value':1007,
            },
            {
                'name':'Voltage_Base',
                'value':1006,
            },
            {
                'name':'Voltage_Base-to-Top',  # (TODO) Jaleel: Recheck after Issue#619 fixed
                'value':1017,
            },
            {
                'name':'Negative_Width',
                'value':11,
            },
            {
                'name':'Positive_Width',
                'value':12,
            },
            {
                'name':'Negative_Duty_Cycle',
                'value':13,
            },
            {
                'name':'Positive_Duty_Cycle',
                'value':14,
            },
            {
                'name':'Integral',
                'value':1005,
            },
            {
                'name':'Area',
                'value':1003,
            },
            {
                'name':'Cycle_Area',
                'value':1004,
            },
            
            {
                'name':'Time_Delay',
                'value':1014,
            },
            {
                'name':'Phase_Delay',
                'value':1018,
            },
            {
                'name':'Low_Ref_Volts',
                'value':1000,
            },
            {
                'name':'Mid_Ref_Volts',
                'value':1001,
            },
            {
                'name':'High_Ref_Volts',
                'value':1002,
            },
            {
                'name':'Volt._Hist._Mean',
                'value':2000,
            },
            {
                'name':'Volt._Hist._Stdev',
                'value':2001,
            },
            {
                'name':'Volt._Hist._Median',
                'value':2003,
            },
            {
                'name':'Volt._Hist._Mode',
                'value':2010,
            },
            {
                'name':'Volt._Hist._Max',
                'value':2005,
            },
            {
                'name':'Volt._Hist._Min',
                'value':2006,
            },
            {
                'name':'Volt._Hist._Peak-to-Peak',  # (TODO) Jaleel: Recheck after Issue#619 fixed
                'value':2002,
            },
            {
                'name':'Volt._Hist._Mean_+_Stdev',  # (TODO) Jaleel: Recheck after Issue#619 fixed
                'value':2007,
            },
            {
                'name':'Volt._Hist._Mean_+_2_Stdev',  # (TODO) Jaleel: Recheck after Issue#619 fixed
                'value':2008,
            },
            {
                'name':'Volt._Hist._Mean_+_3_Stdev',  # (TODO) Jaleel: Recheck after Issue#619 fixed
                'value':2009,
            },
            {
                'name':'Volt._Hist._Hits',
                'value':2004,
            },
            {
                'name':'Volt._Hist._New_Hits',
                'value':2011,
            },
            {
                'name':'Time_Hist._Mean',
                'value':3000,
            },
            {
                'name':'Time_Hist._Stdev',
                'value':3001,
            },
            {
                'name':'Time_Hist._Median',
                'value':3003,
            },
            {
                'name':'Time_Hist._Mode',
                'value':3010,
            },
            {
                'name':'Time_Hist._Max',
                'value':3005,
            },
            {
                'name':'Time_Hist._Min',
                'value':3006,
            },
            {
                'name':'Time_Hist._Peak-to-Peak',  # (TODO) Jaleel: Recheck after Issue#619 fixed
                'value':3002,
            },
            {
                'name':'Time_Hist._Mean_+_Stdev',  # (TODO) Jaleel: Recheck after Issue#619 fixed
                'value':3007,
            },
            {
                'name':'Time_Hist._Mean_+_2_Stdev',  # (TODO) Jaleel: Recheck after Issue#619 fixed
                'value':3008,
            },
            {
                'name':'Time_Hist._Mean_+_3_Stdev',  # (TODO) Jaleel: Recheck after Issue#619 fixed
                'value':3009,
            },
            {
                'name':'Time_Hist._Hits',
                'value':3004,
            },
            {
                'name':'Time_Hist._New_Hits',
                'value':3011,
            },          
        ],
    },
    'InputImpedance': {
        'values': [
            {
                'name': '1_mega_ohm',
                'value': 0,
            },
            {
                'name': '50_ohms',
                'value': 2,
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
                'name': 'PXI_Star_Trigger',
                'value': 'VAL_PXI_STAR',
            },
            {
                'name': 'AUX_0/PFI_0',
                'value': 'VAL_AUX_0_PFI_0',  # (TODO) Jaleel: Recheck after Issue#619 fixed
            },
            {
                'name': 'AUX_0/PFI_1',
                'value': 'VAL_AUX_0_PFI_1',  # (TODO) Jaleel: Recheck after Issue#619 fixed
            },
            {
                'name': 'AUX_0/PFI_2',
                'value': 'VAL_AUX_0_PFI_2',  # (TODO) Jaleel: Recheck after Issue#619 fixed
            },
            {
                'name': 'AUX_0/PFI_3',
                'value': 'VAL_AUX_0_PFI_3',  # (TODO) Jaleel: Recheck after Issue#619 fixed
            },
            {
                'name': 'AUX_0/PFI_4',  # (TODO) Jaleel: Recheck after Issue#619 fixed
                'value': 'VAL_AUX_0_PFI_4',
            },
            {
                'name': 'AUX_0/PFI_5',  # (TODO) Jaleel: Recheck after Issue#619 fixed
                'value': 'VAL_AUX_0_PFI_5',
            },
            {
                'name': 'AUX_0/PFI_6',  # (TODO) Jaleel: Recheck after Issue#619 fixed
                'value': 'VAL_AUX_0_PFI_6',
            },
            {
                'name': 'AUX_0/PFI_7',  # (TODO) Jaleel: Recheck after Issue#619 fixed
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
                'name': 'External TRIG',
                'value': 'VAL_EXTERNAL',
            },
        ],
    },
   'ExportableSignals': {   
        'values': [
            #{  # (TODO) Jaleel: Recheck after Issue#618 fixed
            #    'name': 'None',
            #    'value': 0,
            #},
            {
                'name': 'Start_Trigger',
                'value': 2,
            },
            {
                'name': 'Advance_Trigger',
                'value': 5,
            },
            {
                'name': 'Reference_Trigger',
                'value': 1,
            },
            {
                'name': 'End_of_Record_Event',
                'value': 4,
            },
            {
                'name': 'End_of_Acquisition_Event',
                'value': 3,
            },
            {
                'name': 'Ready_for_Start_Event',
                'value': 7,
            },
            {
                'name': 'Ready_for_Advance_Event',
                'value': 6,
            },
            {
                'name': 'Ready_for_Reference_Event',
                'value': 10,
            },
            {
                'name': 'Reference_Clock',
                'value': 100,
            },
            {
                'name': 'Sample_Clock',
                'value': 101,
            },
            {
                'name': '5_Volt_Power',
                'value': 13,
            },
        ],
    },
   #'WhichSignal': {  # (TODO) Jaleel: Recheck after Issue#618 fixed
   #     'values': [
   #        {
   #             'name': 'None',
   #             'value': 'None',
   #         },
   # 	],
   #},
   'ExportDestinations': {   
        'values': [
            #{  # (TODO) Jaleel: Recheck after Issue#618 fixed  
            #    'name': 'None',
            #    'value': 'VAL_NO_SOURCE',
            #},
			{
                'name': 'PXI_Trigger_Line_0/RTSI_0',  # (TODO) Jaleel: Recheck after Issue#619 fixed
                'value': 'VAL_RTSI_0',
            },
			{
                'name': 'PXI_Trigger_Line_1/RTSI_1',  # (TODO) Jaleel: Recheck after Issue#619 fixed
                'value': 'VAL_RTSI_1',
            },
			{
                'name': 'PXI_Trigger_Line_2/RTSI_2',  # (TODO) Jaleel: Recheck after Issue#619 fixed
                'value': 'VAL_RTSI_2',
            },
			{
                'name': 'PXI_Trigger_Line_3/RTSI_3',  # (TODO) Jaleel: Recheck after Issue#619 fixed
                'value': 'VAL_RTSI_3',
            },
			{
                'name': 'PXI_Trigger_Line_4/RTSI_4',  # (TODO) Jaleel: Recheck after Issue#619 fixed
                'value': 'VAL_RTSI_4',
            },
			{
                'name': 'PXI_Trigger_Line_5/RTSI_5',  # (TODO) Jaleel: Recheck after Issue#619 fixed
                'value': 'VAL_RTSI_5',
            },
			{
                'name': 'PXI_Trigger_Line_6/RTSI_6',  # (TODO) Jaleel: Recheck after Issue#619 fixed
                'value': 'VAL_RTSI_6',
            },
			{
                'name': 'PXI_Trigger_Line_7/RTSI_7_(RTSI_Clock)',  # (TODO) Jaleel: Recheck after Issue#619 fixed
                'value': 'VAL_RTSI_7',
            },
			{
                'name': 'PXI_Star_Trigger',
                'value': 'VAL_PXI_STAR',
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
                'name': 'Clock_Out',
                'value': 'VAL_CLK_OUT',
            },
			{
                'name': 'AUX_0/PFI_0',  # (TODO) Jaleel: Recheck after Issue#619 fixed
                'value': 'VAL_AUX_0_PFI_0',
            },
			{
                'name': 'AUX_0/PFI_1',  # (TODO) Jaleel: Recheck after Issue#619 fixed
                'value': 'VAL_AUX_0_PFI_1',
            },
			{
                'name': 'AUX_0/PFI_2',  # (TODO) Jaleel: Recheck after Issue#619 fixed
                'value': 'VAL_AUX_0_PFI_2',
            },
			{
                'name': 'AUX_0/PFI_3',  # (TODO) Jaleel: Recheck after Issue#619 fixed
                'value': 'VAL_AUX_0_PFI_3',
            },
			{
                'name': 'AUX_0/PFI_4',  # (TODO) Jaleel: Recheck after Issue#619 fixed
                'value': 'VAL_AUX_0_PFI_4',
            },
			{
                'name': 'AUX_0/PFI_5',  # (TODO) Jaleel: Recheck after Issue#619 fixed
                'value': 'VAL_AUX_0_PFI_5',
            },
			{
                'name': 'AUX_0/PFI_6',  # (TODO) Jaleel: Recheck after Issue#619 fixed
                'value': 'VAL_AUX_0_PFI_6',
            },
			{
                'name': 'AUX_0/PFI_7',  # (TODO) Jaleel: Recheck after Issue#619 fixed
                'value': 'VAL_AUX_0_PFI_7',
            },
		],
	},	
}