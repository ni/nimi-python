
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
'description': 'Mean average.',
},
            },
            {
                'name': 'MEDIAN',
                'value': 1,
'documentation': {
'description': 'Median average.',
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
                'name': 'NISCOPE_VAL_NORMAL',
                'value': 0,
'documentation': {
'description': 'Sets the digitizer to normal resolution mode. The digitizer can use real-time sampling or equivalent-time sampling.',
},
            },
            {
                'name': 'NISCOPE_VAL_FLEXRES',
                'value': 1001,
'documentation': {
'description': 'Sets the digitizer to flexible resolution mode if supported.  The digitizer uses different hardware configurations to change the resolution depending on the sampling rate used.',
},
            },
            {
                'name': 'NISCOPE_VAL_DDC',
                'value': 1002,
'documentation': {
'description': 'Sets the digitizer to DDC mode on the NI 5620/5621.',
},
            },
        ],
    },
    'AddressType': {
        'values': [
            {
                'name': 'NISCOPE_VAL_ADDR_PHYSICAL',
                'value': 0,
'documentation': {
'description': 'Physical address.',
},
            },
            {
                'name': 'NISCOPE_VAL_ADDR_VIRTUAL',
                'value': 1,
'documentation': {
'description': 'Virtual address.',
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
'description': 'Specifies magnitude data as the source.',
},
            },
            {
                'name': 'Q_DATA',
                'value': 3,
'documentation': {
'description': 'Specifies Q data as the source.',
},
            },
            {
                'name': 'PHASE_DATA',
                'value': 4,
'documentation': {
'description': 'Specifies phase data as the source.',
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
'description': 'Disabled',
},
            },
            {
                'name': 'ENABLED',
                'value': 1,
'documentation': {
'description': 'Enabled',
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
'description': 'Does not acquire a waveform for the channel.',
},
            },
            {
                'name': 'ENABLED',
                'value': 1,
'documentation': {
'description': 'Acquires a waveform for the channel.',
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
'description': 'Allow both real-time and equivalent-time measurements.',
},
            },
            {
                'name': 'ENABLED',
                'value': 1,
'documentation': {
'description': 'Allow only real-time measurements.',
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
'description': 'Use multiple interleaved ADCs to acquire data for this channel.',
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
'description': '',
},
            },
            {
                'name': 'RIGHT',
                'value': 2,
'documentation': {
'description': '',
},
            },
        ],
    },
    'DataProcessingMode': {
        'values': [
            {
                'name': 'NISCOPE_VAL_REAL',
                'value': 0,
'documentation': {
'description': 'The waveform data points are real numbers (I data).',
},
            },
            {
                'name': 'NISCOPE_VAL_COMPLEX',
                'value': 1,
'documentation': {
'description': 'The waveform data points are complex numbers (IQ data).',
},
            },
        ],
    },
    'DiscriminatorFIRInputSource': {
        'values': [
            {
                'name': 'NISCOPE_VAL_PHASE',
                'value': 0,
'documentation': {
'description': 'Sets the discriminator FIR input source to phase.',
},
            },
            {
                'name': 'NISCOPE_VAL_MAGNITUDE',
                'value': 1,
'documentation': {
'description': 'Sets the discriminator FIR input source to magnitude.',
},
            },
            {
                'name': 'NISCOPE_VAL_RESAMPLER',
                'value': 2,

            },
            {
                'name': 'RESAMPLER',
                'value': 3,
'documentation': {
'description': 'Sets the discriminator FIR input source to resampler.',
},
            },
        ],
    },
    'DiscriminatorFIRSymmetry': {
        'values': [
            {
                'name': 'NISCOPE_VAL_SYMMETRIC',
                'value': 0,
'documentation': {
'description': 'Sets the discriminator FIR symmetry to symmetric.',
},
            },
            {
                'name': 'NISCOPE_VAL_ASYMMETRIC',
                'value': 1,
'documentation': {
'description': 'Sets the discriminator FIR symmetry to asymmetric.',
},
            },
        ],
    },
    'DiscriminatorFIRSymmetryType': {
        'values': [
            {
                'name': 'NISCOPE_VAL_EVEN',
                'value': 0,
'documentation': {
'description': 'Sets the discriminator FIR symmetry type to even.',
},
            },
            {
                'name': 'NISCOPE_VAL_ODD',
                'value': 1,
'documentation': {
'description': 'Sets the discriminator FIR symmetry type to odd.',
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
'description': 'No window.',
},
            },
            {
                'name': 'HANNING',
                'value': 409,
'documentation': {
'description': 'Specifies a Hanning window.',
},
            },
            {
                'name': 'FLAT_TOP',
                'value': 410,
'documentation': {
'description': 'Specifies a Flat Top window.',
},
            },
            {
                'name': 'HAMMING',
                'value': 420,
'documentation': {
'description': 'Specifies a Hamming window.',
},
            },
            {
                'name': 'TRIANGLE',
                'value': 423,
'documentation': {
'description': 'Specifies a Triangle window.',
},
            },
            {
                'name': 'BLACKMAN',
                'value': 424,
'documentation': {
'description': 'Specifies a Blackman window.',
},
            },
        ],
    },
    'FetchRelativeTo': {
        'values': [
            {
                'name': 'NISCOPE_VAL_READ_POINTER',
                'value': 388,
'documentation': {
'description': 'The read pointer is set to zero when a new acquisition is initiated. After every fetch the read pointer is incremeted to be the sample after the last sample retrieved.  Therefore, you can repeatedly fetch relative to the read pointer for a continuous acquisition program.',
},
            },
            {
                'name': 'NISCOPE_VAL_PRETRIGGER',
                'value': 477,
'documentation': {
'description': 'Fetches relative to the first pretrigger point requested with niScope_ConfigureHorizontalTiming.',
},
            },
            {
                'name': 'NISCOPE_VAL_NOW',
                'value': 481,
'documentation': {
'description': 'Fetch data at the last sample acquired.',
},
            },
            {
                'name': 'NISCOPE_VAL_START',
                'value': 482,
'documentation': {
'description': 'Fetch data starting at the first point sampled by the digitizer.',
},
            },
            {
                'name': 'NISCOPE_VAL_TRIGGER',
                'value': 483,
'documentation': {
'description': 'Fetch at the first posttrigger sample.',
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
'description': 'Specifies lowpass as the filter type.',
},
            },
            {
                'name': 'HIGHPASS',
                'value': 1,
'documentation': {
'description': 'Specifies highpass as the filter type.',
},
            },
            {
                'name': 'BANDPASS',
                'value': 2,
'documentation': {
'description': 'Specifies bandpass as the filter type.',
},
            },
            {
                'name': 'BANDSTOP',
                'value': 3,
'documentation': {
'description': 'Specifies bandstop as the filter type.',
},
            },
        ],
    },
    'FlexFIRAntialiasFilterType': {
        'values': [
            {
                'name': 'NISCOPE_VAL_48_TAP_STANDARD',
                'value': 0,
'documentation': {
'description': 'This filter is optimized for alias protection and frequency-domain flatness',
},
            },
            {
                'name': 'NISCOPE_VAL_48_TAP_HANNING',
                'value': 1,
'documentation': {
'description': 'This filter is optimized for the lowest possible bandwidth for a 48 tap filter and maximizes the SNR',
},
            },
            {
                'name': 'NISCOPE_VAL_16_TAP_HANNING',
                'value': 2,
'documentation': {
'description': 'This filter is optimized for the lowest possible bandwidth for a 16 tap filter and maximizes the SNR',
},
            },
            {
                'name': 'NISCOPE_VAL_8_TAP_HANNING',
                'value': 3,
'documentation': {
'description': 'This filter is optimized for the lowest possible bandwidth for a 8 tap filter and maximizes the SNR',
},
            },
        ],
    },
    'NotificationType': {
        'values': [
            {
                'name': 'NISCOPE_VAL_NOTIFY_NEVER',
                'value': 0,
'documentation': {
'description': 'Never send notification.',
},
            },
            {
                'name': 'NISCOPE_VAL_NOTIFY_DONE',
                'value': 1,
'documentation': {
'description': 'Notify when digitizer acquisition is done.',
},
            },
        ],
    },
    'OverflowErrorReporting': {
        'values': [
            {
                'name': 'NISCOPE_VAL_ERROR_REPORTING_ERROR',
                'value': 0,
'documentation': {
'description': '''
Execution stops and NI-SCOPE returns an error when an overflow has
occurred in the OSP block.
''',
},
            },
            {
                'name': 'NISCOPE_VAL_ERROR_REPORTING_WARNING',
                'value': 1,
'documentation': {
'description': '''
Execution continues and NI-SCOPE returns a warning when an overflow has
occurred in the OSP block.
''',
},
            },
            {
                'name': 'NISCOPE_VAL_ERROR_REPORTING_DISABLED',
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
'description': 'Reference level percentages are computed using the min/max method.',
},
            },
            {
                'name': 'BASETOP',
                'value': 2,
'documentation': {
'description': 'Reference level percentages are computed using the base/top method.',
},
            },
        ],
    },
    'ProgFIRFilterRealComplex': {
        'values': [
            {
                'name': 'REAL',
                'value': 0,
'documentation': {
'description': 'Sets a dual real filter.',
},
            },
            {
                'name': 'COMPLEX',
                'value': 1,
'documentation': {
'description': 'Sets a complex filter.',
},
            },
        ],
    },
    'ProgFIRFilterSymmetry': {
        'values': [
            {
                'name': 'NISCOPE_VAL_SYMMETRIC',
                'value': 0,
'documentation': {
'description': 'Sets a symmetric filter.',
},
            },
            {
                'name': 'NISCOPE_VAL_ASYMMETRIC',
                'value': 1,
'documentation': {
'description': 'Sets an asymmetric filter.',
},
            },
        ],
    },
    'ProgFIRFilterSymmetryType': {
        'values': [
            {
                'name': 'NISCOPE_VAL_EVEN',
                'value': 0,
'documentation': {
'description': 'Sets the discriminator FIR symmetry type to even.',
},
            },
            {
                'name': 'NISCOPE_VAL_ODD',
                'value': 1,
'documentation': {
'description': 'Sets the discriminator FIR symmetry type to odd.',
},
            },
        ],
    },
    'QInputtoCoordConverter': {
        'values': [
            {
                'name': 'I_AND_Q',
                'value': 0,
'documentation': {
'description': 'Enables the Q input to coordinate converter.',
},
            },
            {
                'name': 'Q_ZEROED',
                'value': 1,
'documentation': {
'description': 'Zeroes out the Q input the to coordinate converter.',
},
            },
        ],
    },
    'RISMethod': {
        'values': [
            {
                'name': 'NISCOPE_VAL_RIS_EXACT_NUM_AVERAGES',
                'value': 1,
'documentation': {
'description': 'Acquires exactly the specified number of records for each bin in the RIS acquisition.  An error is returned from the fetch function if the RIS acquisition does not successfully acquire the specified number of waveforms within the timeout period.  You may call the fetch function again to allow more time for the acquisition to finish.',
},
            },
            {
                'name': 'NISCOPE_VAL_RIS_MIN_NUM_AVERAGES',
                'value': 2,
'documentation': {
'description': '''
Each RIS sample is the average of a least a minimum number of randomly
distributed points.
''',
},
            },
            {
                'name': 'NISCOPE_VAL_RIS_INCOMPLETE',
                'value': 3,
'documentation': {
'description': 'Returns the RIS waveform after the specified timeout even if it is incomplete.  If no waveforms have been acquired in certain bins, these bins will have a NaN (when fetching scaled data) or a zero (when fetching binary data). A warning (positive error code) is returned from the fetch function if the RIS acquisition did not finish.  The acquisition aborts when data is returned.',
},
            },
            {
                'name': 'NISCOPE_VAL_RIS_LIMITED_BIN_WIDTH',
                'value': 5,
'documentation': {
'description': 'Limits the waveforms in the various bins to be within 200 ps of the center of the bin.',
},
            },
        ],
    },
    'RefLevelUnits': {
        'values': [
            {
                'name': 'VOLTS',
                'value': 0,
'documentation': {
'description': 'Specifies that the reference levels are given in units of volts.',
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
                'name': 'NISCOPE_VAL_ANALOG_DETECTION_CIRCUIT',
                'value': 0,
'documentation': {
'description': 'use the hardware analog circuitry to implement the reference trigger.  This option will trigger before any onboard signal processing.',
},
            },
            {
                'name': 'NISCOPE_VAL_DDC_OUTPUT',
                'value': 1,
'documentation': {
'description': 'use the onboard signal processing logic to implement the reference trigger.  This option will trigger based on the onboard signal processed data.',
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
'description': 'Resampler enabled.',
},
            },
            {
                'name': 'HB_1_ENABLED',
                'value': 2,
'documentation': {
'description': 'HB 1 enabled.',
},
            },
            {
                'name': 'RESAMPLER_AND_HB_1',
                'value': 3,
'documentation': {
'description': 'Resampler and HB 1.',
},
            },
            {
                'name': 'BOTH_HB_FILTERS',
                'value': 6,
'documentation': {
'description': 'Both HB Filters.',
},
            },
            {
                'name': 'RESAMPLER_AND_BOTH_HB_FILTERS',
                'value': 7,
'documentation': {
'description': 'Resampler and Both HB Filters.',
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
'description': 'Data is streamed from the start trigger.',
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
'description': 'Data is streamed relative to the sync trigger and reference position.',
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
'description': 'Specifies CLKIN as the source for Syncout CLK.',
},
            },
            {
                'name': 'PROCCLK',
                'value': 1,
'documentation': {
'description': 'Specifies PROCCLK as the source for Syncout CLK.',
},
            },
        ],
    },
    'TerminalConfiguration': {
        'values': [
            {
                'name': 'NISCOPE_VAL_SINGLE_ENDED',
                'value': 0,
'documentation': {
'description': 'Channel is single ended',
},
            },
            {
                'name': 'NISCOPE_VAL_UNBALANCED_DIFFERENTIAL',
                'value': 1,
'documentation': {
'description': 'Channel is unbalanced differential',
},
            },
            {
                'name': 'NISCOPE_VAL_DIFFERENTIAL',
                'value': 2,
'documentation': {
'description': 'Channel is differential',
},
            },
        ],
    },
    'TimingNCOFreqOffsetBits': {
        'values': [
            {
                'name': '_8_BITS',
                'value': 0,
'documentation': {
'description': 'Specifies 8 offset bits in the timing NCO.',
},
            },
            {
                'name': '_16_BITS',
                'value': 1,
'documentation': {
'description': 'Specifies 16 offset bits in the timing NCO.',
},
            },
            {
                'name': '_24_BITS',
                'value': 2,
'documentation': {
'description': 'Specifies 24 offset bits in the timing NCO.',
},
            },
            {
                'name': '_32_BITS',
                'value': 3,
'documentation': {
'description': 'Specifies 32 offset bits in the timing NCO.',
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
                'name': 'LF_REJECT',
                'value': 4,
'documentation': {
'description': 'LF Reject filter.',
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
    'TriggerModifier': {
        'values': [
            {
                'name': 'NISCOPE_VAL_NO_TRIGGER_MOD',
                'value': 1,
'documentation': {
'description': 'Normal triggering.',
},
            },
            {
                'name': 'NISCOPE_VAL_AUTO',
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
                'name': 'NISCOPE_VAL_NEGATIVE',
                'value': 0,
'documentation': {
'description': 'Falling edge',
},
            },
            {
                'name': 'NISCOPE_VAL_POSITIVE',
                'value': 1,
'documentation': {
'description': 'Rising edge',
},
            },
        ],
    },
    'TriggerType': {
        'values': [
            {
                'name': 'NISCOPE_VAL_EDGE_TRIGGER',
                'value': 1,
'documentation': {
'description': 'Configures the digitizer for edge triggering.  An edge trigger occurs when the trigger signal crosses the trigger level specified with the set trigger slope.  You configure the trigger level and slope with niScope_ConfigureTriggerEdge.',
},
            },
            {
                'name': 'NISCOPE_VAL_TV_TRIGGER',
                'value': 5,
'documentation': {
'description': 'Configures the digitizer for video/TV triggering.   You configure the video trigger parameters like signal Format, Line to trigger off of, Polarity, and Enable DC Restore with niScope_ConfigureTriggerVideo.',
},
            },
            {
                'name': 'NISCOPE_VAL_IMMEDIATE_TRIGGER',
                'value': 6,
'documentation': {
'description': 'Configures the digitizer for immediate triggering.   An immediate trigger occurs as soon as the pretrigger samples are acquired.',
},
            },
            {
                'name': 'NISCOPE_VAL_HYSTERESIS_TRIGGER',
                'value': 1001,
'documentation': {
'description': 'Configures the digitizer for hysteresis triggering.  A hysteresis trigger occurs when the trigger signal crosses the trigger level with the specified slope and passes through the hysteresis window you specify. You configure the trigger level, slope, and hysteresis with niScope_ConfigureTriggerHysteresis.',
},
            },
            {
                'name': 'NISCOPE_VAL_DIGITAL_TRIGGER',
                'value': 1002,
'documentation': {
'description': 'Configures the digitizer for digital triggering. A digital trigger occurs when the trigger signal has the specified slope. You configure the trigger slope with niScope_ConfigureTriggerDigital.',
},
            },
            {
                'name': 'NISCOPE_VAL_WINDOW_TRIGGER',
                'value': 1003,
'documentation': {
'description': 'Configures the digitizer for window triggering.  A window trigger occurs when the trigger signal enters or leaves the window defined by the values you specify with the Low Window Level, High Window Level, and Window Mode Parameters.  You configure the low window level high window level, and window mode with niScope_ConfigureTriggerWindow.',
},
            },
            {
                'name': 'NISCOPE_VAL_SOFTWARE_TRIGGER',
                'value': 1004,
'documentation': {
'description': 'Configures the digitizer for software triggering.  A software trigger occurs when niScope_SendSoftwareTrigger is called.',
},
            },
        ],
    },
    'TriggerWindowMode': {
        'values': [
            {
                'name': 'NISCOPE_VAL_ENTERING_WINDOW',
                'value': 0,
'documentation': {
'description': 'Trigger upon entering the window',
},
            },
            {
                'name': 'NISCOPE_VAL_LEAVING_WINDOW',
                'value': 1,
'documentation': {
'description': 'Trigger upon leaving the window',
},
            },
        ],
    },
    'VerticalCoupling': {
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
                'name': 'NISCOPE_VAL_GND',
                'value': 2,
'documentation': {
'description': 'GND coupling',
},
            },
        ],
    },
    'VideoPolarity': {
        'values': [
            {
                'name': 'NISCOPE_VAL_TV_POSITIVE',
                'value': 1,
'documentation': {
'description': 'Specifies that the video signal has positive polarity.',
},
            },
            {
                'name': 'NISCOPE_VAL_TV_NEGATIVE',
                'value': 2,
'documentation': {
'description': 'Specifies that the video signal has negative polarity.',
},
            },
        ],
    },
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
                'name': 'M_PAL',
                'value': 4,
'documentation': {
'description': 'Specifies M-PAL signal format.',
},
            },
            {
                'name': '_480I59_94_FPS',
                'value': 5,
'documentation': {
'description': 'Specifies 480i/59.94 signal format.',
},
            },
            {
                'name': '_480I60_FPS',
                'value': 6,
'documentation': {
'description': 'Specifies 480i/60 signal format.',
},
            },
            {
                'name': '_480P59_94_FPS',
                'value': 7,
'documentation': {
'description': 'Specifies 480p/59.94 signal format.',
},
            },
            {
                'name': '_480P60_FPS',
                'value': 8,
'documentation': {
'description': 'Specifies 480p/60 Fps signal format.',
},
            },
            {
                'name': '_576I60_FPS',
                'value': 9,
'documentation': {
'description': 'Specifies 576i/60 fps signal format.',
},
            },
            {
                'name': '_576P50_FPS',
                'value': 10,
'documentation': {
'description': 'Specifies 576p/50 Fps signal format.',
},
            },
            {
                'name': '_720P30_FPS',
                'value': 11,
'documentation': {
'description': 'Specifies 720p/30 Fps signal format.',
},
            },
            {
                'name': '_720P50_FPS',
                'value': 12,
'documentation': {
'description': 'Specifies 720p/50 Fps signal format.',
},
            },
            {
                'name': '_720P59_94_FPS',
                'value': 13,
'documentation': {
'description': 'Specifies 720p/59.94 Fps signal format.',
},
            },
            {
                'name': '_720P60_FPS',
                'value': 14,
'documentation': {
'description': 'Specifies 720p/60 Fps signal format.',
},
            },
            {
                'name': '_1080I50_FPS',
                'value': 15,
'documentation': {
'description': 'Specifies 1080i/50 fps signal format.',
},
            },
            {
                'name': '_1080I59_94_FPS',
                'value': 16,
'documentation': {
'description': 'Specifies 1080i/59.94 fps signal format.',
},
            },
            {
                'name': '_1080I60_FPS',
                'value': 17,
'documentation': {
'description': 'Specifies 1080i/60 fps signal format.',
},
            },
            {
                'name': '_1080P24_FPS',
                'value': 18,
'documentation': {
'description': 'Specifies 1080p/24 Fps signal format.',
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
    'VideoTriggerEvent': {
        'values': [
            {
                'name': 'NISCOPE_VAL_TV_EVENT_FIELD1',
                'value': 1,
'documentation': {
'description': 'Trigger on field 1 of the signal',
},
            },
            {
                'name': 'NISCOPE_VAL_TV_EVENT_FIELD2',
                'value': 2,
'documentation': {
'description': 'Trigger on field 2 of the signal',
},
            },
            {
                'name': 'NISCOPE_VAL_TV_EVENT_ANY_FIELD',
                'value': 3,
'documentation': {
'description': 'Trigger on the first field acquired',
},
            },
            {
                'name': 'NISCOPE_VAL_TV_EVENT_ANY_LINE',
                'value': 4,
'documentation': {
'description': 'Trigger on the first line acquired',
},
            },
            {
                'name': 'NISCOPE_VAL_TV_EVENT_LINE_NUMBER',
                'value': 5,
'documentation': {
'description': 'Trigger on a specific line of a video signal.  Valid values vary depending on the signal format configured.',
},
            },
        ],
    },
}
