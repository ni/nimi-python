
# -*- coding: utf-8 -*-
# This file is code generated, do not make changes here.
#  If the generated information is not correct for python
#  changes can be made in enums_addon.py and they will be
#  applied at build time.

enums = {
    'AGCAverageControl': {
        'values': [
            {
                'name': 'MEAN',
                'value': 0,
'documentation': {
'description': '''
Mean average.
''',
},
            },
            {
                'name': 'MEDIAN',
                'value': 1,
'documentation': {
'description': '''
Median average.
''',
},
            },
        ],
    },
    'AOUTParallelOutputSource': {
        'values': [
            {
                'name': 'I_DATA',
                'value': 0,
'documentation': {
'description': '''
Specifies I data as the source for the AOUT parallel output from the
DDC.
''',
},
            },
            {
                'name': 'MAGNITUDE_DATA',
                'value': 1,
'documentation': {
'description': '''
Specifies magnitude data as the source for the AOUT parallel output from
the DDC.
''',
},
            },
            {
                'name': 'FREQUENCY_DATA',
                'value': 2,
'documentation': {
'description': '''
Specifies frequency data as the source for the AOUT parallel output from
the DDC.
''',
},
            },
        ],
    },
    'AcquisitionType': {
        'values': [
            {
                'name': 'NORMAL',
                'value': 0,
'documentation': {
'description': '''
Sets the digitizer to normal resolution mode. The digitizer can use
real-time sampling or equivalent-time sampling.
''',
},
            },
            {
                'name': 'FLEX_RES',
                'value': 1001,
'documentation': {
'description': '''
Sets the digitizer to flexible resolution mode, if supported. The
digitizer uses different hardware configurations to change the
resolution depending on the sampling rate used.
''',
},
            },
            {
                'name': 'DDC',
                'value': 1002,
'documentation': {
'description': '''
Sets the NI 5620/5621digitizer to DDC mode.
''',
},
            },
        ],
    },
    'AddressType': {
        'values': [
            {
                'name': 'PHYSICAL',
                'value': 0,
'documentation': {
'description': '''
Physical address.
''',
},
            },
            {
                'name': 'VIRTUAL',
                'value': 1,
'documentation': {
'description': '''
Virtual address.
''',
},
            },
        ],
    },
    'BOUTParallelOutputSource': {
        'values': [
            {
                'name': 'MAGNITUDE_DATA',
                'value': 1,
'documentation': {
'description': '''
Specifies magnitude data as the source.
''',
},
            },
            {
                'name': 'Q_DATA',
                'value': 3,
'documentation': {
'description': '''
Specifies Q data as the source.
''',
},
            },
            {
                'name': 'PHASE_DATA',
                'value': 4,
'documentation': {
'description': '''
Specifies phase data as the source.
''',
},
            },
        ],
    },
    'BoolEnableDisable': {
        'values': [
            {
                'name': 'DISABLED',
                'value': 0,
'documentation': {
'description': '''
Disabled
''',
},
            },
            {
                'name': 'ENABLED',
                'value': 1,
'documentation': {
'description': '''
Enabled
''',
},
            },
        ],
    },
    'BoolEnableDisableChan': {
        'values': [
            {
                'name': 'DISABLED',
                'value': 0,
'documentation': {
'description': '''
Does not acquire a waveform for the channel.
''',
},
            },
            {
                'name': 'ENABLED',
                'value': 1,
'documentation': {
'description': '''
Acquires a waveform for the channel.
''',
},
            },
        ],
    },
    'BoolEnableDisableIQ': {
        'values': [
            {
                'name': 'DISABLED',
                'value': 0,
'documentation': {
'description': '''
A scalar fetch returns an array of waveforms in the following format:
III...QQQ...
''',
},
            },
            {
                'name': 'ENABLED',
                'value': 1,
'documentation': {
'description': '''
(Default) A scalar fetch returns an array of waveforms in the following
format: IQIQIQ...
''',
},
            },
        ],
    },
    'BoolEnableDisableRealtime': {
        'values': [
            {
                'name': 'DISABLED',
                'value': 0,
'documentation': {
'description': '''
Allow both real-time and equivalent-time measurements.
''',
},
            },
            {
                'name': 'ENABLED',
                'value': 1,
'documentation': {
'description': '''
Allow only real-time measurements.
''',
},
            },
        ],
    },
    'BoolEnableDisableTIS': {
        'values': [
            {
                'name': 'DISABLED',
                'value': 0,
'documentation': {
'description': '''
(Default) Use only this channel's ADC to acquire data for this channel.
''',
},
            },
            {
                'name': 'ENABLED',
                'value': 1,
'documentation': {
'description': '''
Use multiple interleaved ADCs to acquire data for this channel.
''',
},
            },
        ],
    },
    'CoordinateConverterInput': {
        'values': [
            {
                'name': 'RESAMPLER_HB',
                'value': 0,
'documentation': {
'description': '''
Selects the HB filter as the source for the input to the coordinate
converter.
''',
},
            },
            {
                'name': 'PROGRAMMABLE_FIR',
                'value': 1,
'documentation': {
'description': '''
Selects the programmable FIR filter as the source for the input to the
coordinate converter.
''',
},
            },
        ],
    },
    'DataJustificationMode': {
        'values': [
            {
                'name': 'LEFT',
                'value': 1,
'documentation': {
'description': '''

''',
},
            },
            {
                'name': 'RIGHT',
                'value': 2,
'documentation': {
'description': '''

''',
},
            },
        ],
    },
    'DataProcessingMode': {
        'values': [
            {
                'name': 'REAL',
                'value': 0,
'documentation': {
'description': '''
The waveform data points are real numbers (I data).
''',
},
            },
            {
                'name': 'COMPLEX',
                'value': 1,
'documentation': {
'description': '''
The waveform data points are complex numbers (IQ data).
''',
},
            },
        ],
    },
    'DiscriminatorFIRInputSource': {
        'values': [
            {
                'name': 'PHASE',
                'value': 0,
'documentation': {
'description': '''
Sets the discriminator FIR input source to phase.
''',
},
            },
            {
                'name': 'MAGNITUDE',
                'value': 1,
'documentation': {
'description': '''
Sets the discriminator FIR input source to magnitude.
''',
},
            },
            {
                'name': 'RESAMPLER',
                'value': 3,
'documentation': {
'description': '''
Sets the discriminator FIR input source to resampler.
''',
},
            },
        ],
    },
    'DiscriminatorFIRSymmetry': {
        'values': [
            {
                'name': 'SYMMETRIC',
                'value': 0,
'documentation': {
'description': '''
Sets the discriminator FIR symmetry to symmetric.
''',
},
            },
            {
                'name': 'ASYMMETRIC',
                'value': 1,
'documentation': {
'description': '''
Sets the discriminator FIR symmetry to asymmetric.
''',
},
            },
        ],
    },
    'DiscriminatorFIRSymmetryType': {
        'values': [
            {
                'name': 'EVEN',
                'value': 0,
'documentation': {
'description': '''
Sets the discriminator FIR symmetry type to even.
''',
},
            },
            {
                'name': 'ODD',
                'value': 1,
'documentation': {
'description': '''
Sets the discriminator FIR symmetry type to odd.
''',
},
            },
        ],
    },
    'FIRFilterWindow': {
        'values': [
            {
                'name': 'NONE',
                'value': 0,
'documentation': {
'description': '''
No window.
''',
},
            },
            {
                'name': 'HANNING',
                'value': 409,
'documentation': {
'description': '''
Specifies a Hanning window.
''',
},
            },
            {
                'name': 'FLAT_TOP',
                'value': 410,
'documentation': {
'description': '''
Specifies a Flat Top window.
''',
},
            },
            {
                'name': 'HAMMING',
                'value': 420,
'documentation': {
'description': '''
Specifies a Hamming window.
''',
},
            },
            {
                'name': 'TRIANGLE',
                'value': 423,
'documentation': {
'description': '''
Specifies a Triangle window.
''',
},
            },
            {
                'name': 'BLACKMAN',
                'value': 424,
'documentation': {
'description': '''
Specifies a Blackman window.
''',
},
            },
        ],
    },
    'FetchRelativeTo': {
        'values': [
            {
                'name': 'READ_POINTER',
                'value': 388,
'documentation': {
'description': '''
The read pointer is set to zero when a new acquisition is initiated.
After every fetch the read pointer is incremented to be the sample after
the last sample retrieved. Therefore, you can repeatedly fetch relative
to the read pointer for a continuous acquisition program.
''',
},
            },
            {
                'name': 'PRETRIGGER',
                'value': 477,
'documentation': {
'description': '''
Fetches relative to the first pretrigger point requested with the
niScope Configure Horizontal Timing VI.
''',
},
            },
            {
                'name': 'NOW',
                'value': 481,
'documentation': {
'description': '''
Fetch data at the last sample acquired.
''',
},
            },
            {
                'name': 'START',
                'value': 482,
'documentation': {
'description': '''
Fetch data starting at the first point sampled by the digitizer.
''',
},
            },
            {
                'name': 'TRIGGER',
                'value': 483,
'documentation': {
'description': '''
Fetch at the first posttrigger sample.
''',
},
            },
        ],
    },
    'FilterType': {
        'values': [
            {
                'name': 'LOWPASS',
                'value': 0,
'documentation': {
'description': '''
Specifies lowpass as the filter type.
''',
},
            },
            {
                'name': 'HIGHPASS',
                'value': 1,
'documentation': {
'description': '''
Specifies highpass as the filter type.
''',
},
            },
            {
                'name': 'BANDPASS',
                'value': 2,
'documentation': {
'description': '''
Specifies bandpass as the filter type.
''',
},
            },
            {
                'name': 'BANDSTOP',
                'value': 3,
'documentation': {
'description': '''
Specifies bandstop as the filter type.
''',
},
            },
        ],
    },
    'FlexFIRAntialiasFilterType': {
        'values': [
            {
                'name': '_48_TAP_STANDARD',
                'value': 0,
'documentation': {
'description': '''
48 Tap Standard filter is optimized for alias protection and
frequency-domain flatness.
''',
},
            },
            {
                'name': '_48_TAP_HANNING',
                'value': 1,
'documentation': {
'description': '''
48 Tap Hanning filter is optimized for the lowest possible bandwidth for
a 48 tap filter and maximizes the SNR.
''',
},
            },
            {
                'name': '_16_TAP_HANNING',
                'value': 2,
'documentation': {
'description': '''
16 Tap Hanning is optimized for the lowest possible bandwidth for a 16
tap filter and maximizes the SNR.
''',
},
            },
            {
                'name': '_8_TAP_HANNING',
                'value': 3,
'documentation': {
'description': '''
8 Tap Hanning filter is optimized for the lowest possible bandwidth for
a 8 tap filter and maximizes the SNR.
''',
},
            },
        ],
    },
    'NotificationType': {
        'values': [
            {
                'name': 'NEVER',
                'value': 0,
'documentation': {
'description': '''
Never send notification.
''',
},
            },
            {
                'name': 'DONE',
                'value': 1,
'documentation': {
'description': '''
Notify when digitizer acquisition is done.
''',
},
            },
        ],
    },
    'OverflowErrorReporting': {
        'values': [
            {
                'name': 'ERROR',
                'value': 0,
'documentation': {
'description': '''
Execution stops and NI-SCOPE returns an error when an overflow has
occurred in the OSP block.
''',
},
            },
            {
                'name': 'WARNING',
                'value': 1,
'documentation': {
'description': '''
Execution continues and NI-SCOPE returns a warning when an overflow has
occurred in the OSP block.
''',
},
            },
            {
                'name': 'DISABLED',
                'value': 2,
'documentation': {
'description': '''
NI-SCOPE does not return an error when an overflow has occurred in the
OSP block.
''',
},
            },
        ],
    },
    'PercentageMethod': {
        'values': [
            {
                'name': 'LOWHIGH',
                'value': 0,
'documentation': {
'description': '''
Specifies that the reference level percentages should be computed using
the low/high method,
''',
},
            },
            {
                'name': 'MINMAX',
                'value': 1,
'documentation': {
'description': '''
Reference level percentages are computed using the min/max method.
''',
},
            },
            {
                'name': 'BASETOP',
                'value': 2,
'documentation': {
'description': '''
Reference level percentages are computed using the base/top method.
''',
},
            },
        ],
    },
    'Prog.FIRFilterReal/Complex': {
        'values': [
            {
                'name': 'REAL',
                'value': 0,
'documentation': {
'description': '''
Sets a dual real filter.
''',
},
            },
            {
                'name': 'COMPLEX',
                'value': 1,
'documentation': {
'description': '''
Sets a complex filter.
''',
},
            },
        ],
    },
    'Prog.FIRFilterSymmetry': {
        'values': [
            {
                'name': 'SYMMETRIC',
                'value': 0,
'documentation': {
'description': '''
Sets a symmetric filter.
''',
},
            },
            {
                'name': 'ASYMMETRIC',
                'value': 1,
'documentation': {
'description': '''
Sets an asymmetric filter.
''',
},
            },
        ],
    },
    'Prog.FIRFilterSymmetryType': {
        'values': [
            {
                'name': 'EVEN',
                'value': 0,
'documentation': {
'description': '''
Sets the discriminator FIR symmetry type to even.
''',
},
            },
            {
                'name': 'ODD',
                'value': 1,
'documentation': {
'description': '''
Sets the discriminator FIR symmetry type to odd.
''',
},
            },
        ],
    },
    'QInputtoCoord.Converter': {
        'values': [
            {
                'name': 'I_AND_Q',
                'value': 0,
'documentation': {
'description': '''
Enables the Q input to coordinate converter.
''',
},
            },
            {
                'name': 'Q_ZEROED',
                'value': 1,
'documentation': {
'description': '''
Zeroes out the Q input the to coordinate converter.
''',
},
            },
        ],
    },
    'RISMethod': {
        'values': [
            {
                'name': 'EXACT_NUM_AVG_',
                'value': 1,
'documentation': {
'description': '''
Acquires exactly the specified number of records for each bin in the RIS
acquisition.
''',
},
            },
            {
                'name': 'MIN_NUM_AVG_',
                'value': 2,
'documentation': {
'description': '''
Each RIS sample is the average of a least a minimum number of randomly
distributed points.
''',
},
            },
            {
                'name': 'INCOMPLETE',
                'value': 3,
'documentation': {
'description': '''
If RIS does not complete in the allotted fetch time, the Fetch VI should
abort and return the incomplete data. Any missing samples appear as NaN
when fetching scaled data or zero when fetching binary data. A warning
with a positive error code is returned from the Fetch VI if the RIS
acquisition did not finish. The acquisition is aborted when data is
returned.
''',
},
            },
            {
                'name': 'LIMIT_BIN_WIDTH',
                'value': 5,
'documentation': {
'description': '''
Each RIS sample is the average of Min Num Avg points distributed close
to the sample period boundaries (within 200 ps). Points falling between
sample periods are ignored.
''',
},
            },
        ],
    },
    'Ref.LevelUnits': {
        'values': [
            {
                'name': 'VOLTS',
                'value': 0,
'documentation': {
'description': '''
Specifies that the reference levels are given in units of volts.
''',
},
            },
            {
                'name': 'PERCENTAGE',
                'value': 1,
'documentation': {
'description': '''
(Default) Specifies that the reference levels are given in percentage
units.
''',
},
            },
        ],
    },
    'RefTriggerDetectorLocation': {
        'values': [
            {
                'name': 'ANALOG_DETECTION_CIRCUIT',
                'value': 0,
'documentation': {
'description': '''
(Default) Uses the hardware analog circuitry to implement the reference
trigger. This option detects trigger conditions by analyzing the
unprocessed analog signal.
''',
},
            },
            {
                'name': 'DDC_OUTPUT',
                'value': 1,
'documentation': {
'description': '''
Uses the onboard signal processing logic to implement the reference
trigger. This option detects trigger conditions by analyzing the
processed digital signal.
''',
},
            },
        ],
    },
    'ResamplerFilterMode': {
        'values': [
            {
                'name': 'RESAMPLER_ENABLED',
                'value': 1,
'documentation': {
'description': '''
Resampler enabled.
''',
},
            },
            {
                'name': 'HB_1_ENABLED',
                'value': 2,
'documentation': {
'description': '''
HB 1 enabled.
''',
},
            },
            {
                'name': 'RESAMPLER_AND_HB_1',
                'value': 3,
'documentation': {
'description': '''
Resampler and HB 1.
''',
},
            },
            {
                'name': 'BOTH_HB_FILTERS',
                'value': 6,
'documentation': {
'description': '''
Both HB Filters.
''',
},
            },
            {
                'name': 'RESAMPLER_AND_BOTH_HB_FILTERS',
                'value': 7,
'documentation': {
'description': '''
Resampler and Both HB Filters.
''',
},
            },
        ],
    },
    'StreamingPositionType': {
        'values': [
            {
                'name': 'START_TRIGGER',
                'value': 0,
'documentation': {
'description': '''
Data is streamed from the start trigger.
''',
},
            },
            {
                'name': 'REFERENCE_TRIGGER',
                'value': 1,
'documentation': {
'description': '''
Data is streamed relative to the reference trigger and reference
position.
''',
},
            },
            {
                'name': 'SYNC_TRIGGER',
                'value': 2,
'documentation': {
'description': '''
Data is streamed relative to the sync trigger and reference position.
''',
},
            },
        ],
    },
    'SyncoutCLKSelect': {
        'values': [
            {
                'name': 'CLKIN',
                'value': 0,
'documentation': {
'description': '''
Specifies CLKIN as the source for Syncout CLK.
''',
},
            },
            {
                'name': 'PROCCLK',
                'value': 1,
'documentation': {
'description': '''
Specifies PROCCLK as the source for Syncout CLK.
''',
},
            },
        ],
    },
    'TerminalConfiguration': {
        'values': [
            {
                'name': 'SINGLE_ENDED',
                'value': 0,
'documentation': {
'description': '''
Single-ended channel terminal configuration.
''',
},
            },
            {
                'name': 'UNBALANCED_DIFFERENTIAL',
                'value': 1,
'documentation': {
'description': '''
Unbalanced differential channel terminal configuration.
''',
},
            },
            {
                'name': 'DIFFERENTIAL',
                'value': 2,
'documentation': {
'description': '''
Differential channel terminal configuration.
''',
},
            },
        ],
    },
    'TimingNCOFreq.OffsetBits': {
        'values': [
            {
                'name': '_8_BITS',
                'value': 0,
'documentation': {
'description': '''
Specifies 8 offset bits in the timing NCO.
''',
},
            },
            {
                'name': '_16_BITS',
                'value': 1,
'documentation': {
'description': '''
Specifies 16 offset bits in the timing NCO.
''',
},
            },
            {
                'name': '_24_BITS',
                'value': 2,
'documentation': {
'description': '''
Specifies 24 offset bits in the timing NCO.
''',
},
            },
            {
                'name': '_32_BITS',
                'value': 3,
'documentation': {
'description': '''
Specifies 32 offset bits in the timing NCO.
''',
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
'description': '''
AC coupled
''',
},
            },
            {
                'name': 'DC',
                'value': 1,
'documentation': {
'description': '''
DC coupled
''',
},
            },
            {
                'name': 'HF_REJECT',
                'value': 3,
'documentation': {
'description': '''
HF Reject filter.
''',
},
            },
            {
                'name': 'LF_REJECT',
                'value': 4,
'documentation': {
'description': '''
LF Reject filter.
''',
},
            },
            {
                'name': 'AC_PLUS_HF_REJECT',
                'value': 1001,
'documentation': {
'description': '''
AC Plus HF Reject filter.
''',
},
            },
        ],
    },
    'TriggerModifier': {
        'values': [
            {
                'name': 'NONE',
                'value': 1,
'documentation': {
'description': '''
Normal triggering.
''',
},
            },
            {
                'name': 'AUTO_TRIGGER',
                'value': 2,
'documentation': {
'description': '''
Software will trigger an acquisition automatically if no trigger arrives
after a certain amount of time.
''',
},
            },
        ],
    },
    'TriggerSlope': {
        'values': [
            {
                'name': 'NEGATIVE',
                'value': 0,
'documentation': {
'description': '''
Specifies a falling edge (negative slope).
''',
},
            },
            {
                'name': 'POSITIVE',
                'value': 1,
'documentation': {
'description': '''
Specifies a rising edge (positive slope).
''',
},
            },
        ],
    },
    'TriggerType': {
        'values': [
            {
                'name': 'EDGE',
                'value': 1,
'documentation': {
'description': '''
Specifies an edge trigger.
''',
},
            },
            {
                'name': 'VIDEO',
                'value': 5,
'documentation': {
'description': '''
Specifies a video trigger.
''',
},
            },
            {
                'name': 'IMMEDIATE',
                'value': 6,
'documentation': {
'description': '''
Specifies an immediate trigger.
''',
},
            },
            {
                'name': 'HYSTERESIS',
                'value': 1001,
'documentation': {
'description': '''
Specifies a hysteresis trigger.
''',
},
            },
            {
                'name': 'DIGITAL',
                'value': 1002,
'documentation': {
'description': '''
Specifies a digital trigger.
''',
},
            },
            {
                'name': 'WINDOW',
                'value': 1003,
'documentation': {
'description': '''
Specifies a window trigger.
''',
},
            },
            {
                'name': 'SOFTWARE',
                'value': 1004,
'documentation': {
'description': '''
Specifies a software trigger.
''',
},
            },
        ],
    },
    'TriggerWindowMode': {
        'values': [
            {
                'name': 'ENTERING',
                'value': 0,
'documentation': {
'description': '''
Trigger occurs when a signal enters a window.
''',
},
            },
            {
                'name': 'LEAVING',
                'value': 1,
'documentation': {
'description': '''
Trigger occurs when a signal leaves a window.
''',
},
            },
        ],
    },
    'VerticalCoupling': {
        'values': [
            {
                'name': 'AC',
                'value': 0,
'documentation': {
'description': '''
AC coupled
''',
},
            },
            {
                'name': 'DC',
                'value': 1,
'documentation': {
'description': '''
DC coupled
''',
},
            },
            {
                'name': 'GROUND',
                'value': 2,
'documentation': {
'description': '''
Ground coupled
''',
},
            },
        ],
    },
    'VideoPolarity': {
        'values': [
            {
                'name': 'POSITIVE',
                'value': 1,
'documentation': {
'description': '''
Specifies that the video signal has positive polarity.
''',
},
            },
            {
                'name': 'NEGATIVE',
                'value': 2,
'documentation': {
'description': '''
Specifies that the video signal has negative polarity.
''',
},
            },
        ],
    },
    'VideoSignalFormat': {
        'values': [
            {
                'name': 'M_NTSC',
                'value': 1,
'documentation': {
'description': '''
Specifies M-NTSC signal format.
''',
},
            },
            {
                'name': 'BG_PAL',
                'value': 2,
'documentation': {
'description': '''
Specifies BG/PAL signal format.
''',
},
            },
            {
                'name': 'SECAM',
                'value': 3,
'documentation': {
'description': '''
Specifies SECAM signal format.
''',
},
            },
            {
                'name': 'M_PAL',
                'value': 4,
'documentation': {
'description': '''
Specifies M-PAL signal format.
''',
},
            },
            {
                'name': '_480I59_94_FPS',
                'value': 5,
'documentation': {
'description': '''
Specifies 480i/59.94 signal format.
''',
},
            },
            {
                'name': '_480I60_FPS',
                'value': 6,
'documentation': {
'description': '''
Specifies 480i/60 signal format.
''',
},
            },
            {
                'name': '_480P59_94_FPS',
                'value': 7,
'documentation': {
'description': '''
Specifies 480p/59.94 signal format.
''',
},
            },
            {
                'name': '_480P60_FPS',
                'value': 8,
'documentation': {
'description': '''
Specifies 480p/60 Fps signal format.
''',
},
            },
            {
                'name': '_576I60_FPS',
                'value': 9,
'documentation': {
'description': '''
Specifies 576i/60 fps signal format.
''',
},
            },
            {
                'name': '_576P50_FPS',
                'value': 10,
'documentation': {
'description': '''
Specifies 576p/50 Fps signal format.
''',
},
            },
            {
                'name': '_720P30_FPS',
                'value': 11,
'documentation': {
'description': '''
Specifies 720p/30 Fps signal format.
''',
},
            },
            {
                'name': '_720P50_FPS',
                'value': 12,
'documentation': {
'description': '''
Specifies 720p/50 Fps signal format.
''',
},
            },
            {
                'name': '_720P59_94_FPS',
                'value': 13,
'documentation': {
'description': '''
Specifies 720p/59.94 Fps signal format.
''',
},
            },
            {
                'name': '_720P60_FPS',
                'value': 14,
'documentation': {
'description': '''
Specifies 720p/60 Fps signal format.
''',
},
            },
            {
                'name': '_1080I50_FPS',
                'value': 15,
'documentation': {
'description': '''
Specifies 1080i/50 fps signal format.
''',
},
            },
            {
                'name': '_1080I59_94_FPS',
                'value': 16,
'documentation': {
'description': '''
Specifies 1080i/59.94 fps signal format.
''',
},
            },
            {
                'name': '_1080I60_FPS',
                'value': 17,
'documentation': {
'description': '''
Specifies 1080i/60 fps signal format.
''',
},
            },
            {
                'name': '_1080P24_FPS',
                'value': 18,
'documentation': {
'description': '''
Specifies 1080p/24 Fps signal format.
''',
},
            },
        ],
    },
    'VideoTriggerEvent': {
        'values': [
            {
                'name': 'FIELD_1',
                'value': 1,
'documentation': {
'description': '''
Trigger on field 1 of the signal.
''',
},
            },
            {
                'name': 'FIELD_2',
                'value': 2,
'documentation': {
'description': '''
Trigger on field 2 of the signal.
''',
},
            },
            {
                'name': 'ANY_FIELD',
                'value': 3,
'documentation': {
'description': '''
Trigger on any field of the signal.
''',
},
            },
            {
                'name': 'ANY_LINE',
                'value': 4,
'documentation': {
'description': '''
Trigger on the first line acquired.
''',
},
            },
            {
                'name': 'LINE_NUMBER',
                'value': 5,
'documentation': {
'description': '''
Trigger on a specific line of a video signal. Valid values vary
depending on the signal format.
''',
},
            },
        ],
    },
}
