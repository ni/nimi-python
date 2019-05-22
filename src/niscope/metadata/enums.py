# -*- coding: utf-8 -*-
# This file is generated from API metadata for NI-SCOPE version 19.1.0d28
enums = {
    'AcquisitionStatus': {
        'values': [
            {
                'name': 'NISCOPE_VAL_ACQ_COMPLETE',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_ACQ_IN_PROGRESS',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_ACQ_STATUS_UNKNOWN',
                'value': -1
            }
        ]
    },
    'AcquisitionType': {
        'values': [
            {
                'documentation': {
                    'description': 'Sets the digitizer to normal resolution mode. The digitizer can use real-time sampling or equivalent-time sampling.'
                },
                'name': 'NISCOPE_VAL_NORMAL',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Sets the digitizer to flexible resolution mode if supported.  The digitizer uses different hardware configurations to change the resolution depending on the sampling rate used.'
                },
                'name': 'NISCOPE_VAL_FLEXRES',
                'value': 1001
            },
            {
                'documentation': {
                    'description': 'Sets the digitizer to DDC mode on the NI 5620/5621.'
                },
                'name': 'NISCOPE_VAL_DDC',
                'value': 1002
            }
        ]
    },
    'AddressType': {
        'values': [
            {
                'documentation': {
                    'description': 'Physical address.'
                },
                'name': 'NISCOPE_VAL_ADDR_PHYSICAL',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Virtual address.'
                },
                'name': 'NISCOPE_VAL_ADDR_VIRTUAL',
                'value': 1
            }
        ]
    },
    'AgcAverageControl': {
        'values': [
            {
                'documentation': {
                    'description': 'Mean average.'
                },
                'name': 'NISCOPE_VAL_MEAN',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Median average.'
                },
                'name': 'NISCOPE_VAL_MEDIAN',
                'value': 1
            }
        ]
    },
    'AoutParallelOutputSource': {
        'values': [
            {
                'documentation': {
                    'description': '\nSpecifies I data as the source for the AOUT parallel output from the\nDDC.\n'
                },
                'name': 'NISCOPE_VAL_I_DATA',
                'value': 0
            },
            {
                'documentation': {
                    'description': '\nSpecifies magnitude data as the source for the AOUT parallel output from\nthe DDC.\n'
                },
                'name': 'NISCOPE_VAL_MAGNITUDE_DATA',
                'value': 1
            },
            {
                'documentation': {
                    'description': '\nSpecifies frequency data as the source for the AOUT parallel output from\nthe DDC.\n'
                },
                'name': 'NISCOPE_VAL_FREQUENCY_DATA',
                'value': 2
            }
        ]
    },
    'ArrayMeasurement': {
        'values': [
            {
                'documentation': {
                    'description': 'None'
                },
                'name': 'NISCOPE_VAL_NO_MEASUREMENT',
                'value': 4000
            },
            {
                'documentation': {
                    'description': 'Last Acquisition Histogram '
                },
                'name': 'NISCOPE_VAL_LAST_ACQ_HISTOGRAM',
                'value': 4001
            },
            {
                'documentation': {
                    'description': 'Multi Acquisition Voltage Histogram'
                },
                'name': 'NISCOPE_VAL_MULTI_ACQ_VOLTAGE_HISTOGRAM',
                'value': 4004
            },
            {
                'documentation': {
                    'description': 'Multi Acquisition Time Histogram'
                },
                'name': 'NISCOPE_VAL_MULTI_ACQ_TIME_HISTOGRAM',
                'value': 4005
            },
            {
                'documentation': {
                    'description': 'Multi Acquisition Average'
                },
                'name': 'NISCOPE_VAL_MULTI_ACQ_AVERAGE',
                'value': 4016
            },
            {
                'documentation': {
                    'description': 'Polynomial Interpolation'
                },
                'name': 'NISCOPE_VAL_POLYNOMIAL_INTERPOLATION',
                'value': 4011
            },
            {
                'documentation': {
                    'description': 'Array Integral'
                },
                'name': 'NISCOPE_VAL_ARRAY_INTEGRAL',
                'value': 4006
            },
            {
                'documentation': {
                    'description': 'Derivative'
                },
                'name': 'NISCOPE_VAL_DERIVATIVE',
                'value': 4007
            },
            {
                'documentation': {
                    'description': 'Inverse'
                },
                'name': 'NISCOPE_VAL_INVERSE',
                'value': 4008
            },
            {
                'documentation': {
                    'description': 'Multiply Channels'
                },
                'name': 'NISCOPE_VAL_MULTIPLY_CHANNELS',
                'value': 4012
            },
            {
                'documentation': {
                    'description': 'Add Channels'
                },
                'name': 'NISCOPE_VAL_ADD_CHANNELS',
                'value': 4013
            },
            {
                'documentation': {
                    'description': 'Subtract Channels'
                },
                'name': 'NISCOPE_VAL_SUBTRACT_CHANNELS',
                'value': 4014
            },
            {
                'documentation': {
                    'description': 'Divide Channels'
                },
                'name': 'NISCOPE_VAL_DIVIDE_CHANNELS',
                'value': 4015
            },
            {
                'documentation': {
                    'description': 'Array Offset'
                },
                'name': 'NISCOPE_VAL_ARRAY_OFFSET',
                'value': 4025
            },
            {
                'documentation': {
                    'description': 'Array Gain'
                },
                'name': 'NISCOPE_VAL_ARRAY_GAIN',
                'value': 4026
            },
            {
                'documentation': {
                    'description': 'Hanning Window'
                },
                'name': 'NISCOPE_VAL_HANNING_WINDOW',
                'value': 4009
            },
            {
                'documentation': {
                    'description': 'Flat Top Window'
                },
                'name': 'NISCOPE_VAL_FLAT_TOP_WINDOW',
                'value': 4010
            },
            {
                'documentation': {
                    'description': 'Hamming Window'
                },
                'name': 'NISCOPE_VAL_HAMMING_WINDOW',
                'value': 4020
            },
            {
                'documentation': {
                    'description': 'Triangle Window'
                },
                'name': 'NISCOPE_VAL_TRIANGLE_WINDOW',
                'value': 4023
            },
            {
                'documentation': {
                    'description': 'Blackman Window'
                },
                'name': 'NISCOPE_VAL_BLACKMAN_WINDOW',
                'value': 4024
            },
            {
                'documentation': {
                    'description': 'FIR Windowed Filter'
                },
                'name': 'NISCOPE_VAL_WINDOWED_FIR_FILTER',
                'value': 4021
            },
            {
                'documentation': {
                    'description': 'Bessel IIR Filter'
                },
                'name': 'NISCOPE_VAL_BESSEL_FILTER',
                'value': 4022
            },
            {
                'documentation': {
                    'description': 'Butterworth IIR Filter'
                },
                'name': 'NISCOPE_VAL_BUTTERWORTH_FILTER',
                'value': 4017
            },
            {
                'documentation': {
                    'description': 'Chebyshev IIR Filter'
                },
                'name': 'NISCOPE_VAL_CHEBYSHEV_FILTER',
                'value': 4018
            },
            {
                'documentation': {
                    'description': 'FFT Phase Spectrum'
                },
                'name': 'NISCOPE_VAL_FFT_PHASE_SPECTRUM',
                'value': 4002
            },
            {
                'documentation': {
                    'description': 'FFT Amp. Spectrum (Volts RMS)'
                },
                'name': 'NISCOPE_VAL_FFT_AMP_SPECTRUM_VOLTS_RMS',
                'value': 4003
            },
            {
                'documentation': {
                    'description': 'FFT Amp. Spectrum (dB)'
                },
                'name': 'NISCOPE_VAL_FFT_AMP_SPECTRUM_DB',
                'value': 4019
            }
        ]
    },
    'BoolEnableDisable': {
        'values': [
            {
                'documentation': {
                    'description': 'Disabled'
                },
                'name': 'NISCOPE_VAL_DISABLED',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Enabled'
                },
                'name': 'NISCOPE_VAL_ENABLED',
                'value': 1
            }
        ]
    },
    'BoolEnableDisableChan': {
        'values': [
            {
                'documentation': {
                    'description': 'Does not acquire a waveform for the channel.'
                },
                'name': 'NISCOPE_VAL_DISABLED',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Acquires a waveform for the channel.'
                },
                'name': 'NISCOPE_VAL_ENABLED',
                'value': 1
            }
        ]
    },
    'BoolEnableDisableIq': {
        'values': [
            {
                'documentation': {
                    'description': '\nA scalar fetch returns an array of waveforms in the following format:\nIII...QQQ...\n'
                },
                'name': 'NISCOPE_VAL_DISABLED',
                'value': 0
            },
            {
                'documentation': {
                    'description': '\n(Default) A scalar fetch returns an array of waveforms in the following\nformat: IQIQIQ...\n'
                },
                'name': 'NISCOPE_VAL_ENABLED',
                'value': 1
            }
        ]
    },
    'BoolEnableDisableRealtime': {
        'values': [
            {
                'documentation': {
                    'description': 'Allow both real-time and equivalent-time measurements.'
                },
                'name': 'NISCOPE_VAL_DISABLED',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Allow only real-time measurements.'
                },
                'name': 'NISCOPE_VAL_ENABLED',
                'value': 1
            }
        ]
    },
    'BoolEnableDisableTis': {
        'values': [
            {
                'documentation': {
                    'description': "\n(Default) Use only this channel's ADC to acquire data for this channel.\n"
                },
                'name': 'NISCOPE_VAL_DISABLED',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Use multiple interleaved ADCs to acquire data for this channel.'
                },
                'name': 'NISCOPE_VAL_ENABLED',
                'value': 1
            }
        ]
    },
    'BoutParallelOutputSource': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies magnitude data as the source.'
                },
                'name': 'NISCOPE_VAL_MAGNITUDE_DATA',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Specifies Q data as the source.'
                },
                'name': 'NISCOPE_VAL_Q_DATA',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'Specifies phase data as the source.'
                },
                'name': 'NISCOPE_VAL_PHASE_DATA',
                'value': 4
            }
        ]
    },
    'ClearableMeasurement': {
        'values': [
            {
                'name': 'NISCOPE_VAL_ALL_MEASUREMENTS',
                'value': 10000
            },
            {
                'name': 'NISCOPE_VAL_MULTI_ACQ_VOLTAGE_HISTOGRAM',
                'value': 4004
            },
            {
                'name': 'NISCOPE_VAL_MULTI_ACQ_TIME_HISTOGRAM',
                'value': 4005
            },
            {
                'name': 'NISCOPE_VAL_MULTI_ACQ_AVERAGE',
                'value': 4016
            },
            {
                'name': 'NISCOPE_VAL_FREQUENCY',
                'value': 2
            },
            {
                'name': 'NISCOPE_VAL_AVERAGE_FREQUENCY',
                'value': 1016
            },
            {
                'name': 'NISCOPE_VAL_FFT_FREQUENCY',
                'value': 1008
            },
            {
                'name': 'NISCOPE_VAL_PERIOD',
                'value': 3
            },
            {
                'name': 'NISCOPE_VAL_AVERAGE_PERIOD',
                'value': 1015
            },
            {
                'name': 'NISCOPE_VAL_RISE_TIME',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_FALL_TIME',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_RISE_SLEW_RATE',
                'value': 1010
            },
            {
                'name': 'NISCOPE_VAL_FALL_SLEW_RATE',
                'value': 1011
            },
            {
                'name': 'NISCOPE_VAL_OVERSHOOT',
                'value': 18
            },
            {
                'name': 'NISCOPE_VAL_PRESHOOT',
                'value': 19
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_RMS',
                'value': 4
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_CYCLE_RMS',
                'value': 16
            },
            {
                'name': 'NISCOPE_VAL_AC_ESTIMATE',
                'value': 1012
            },
            {
                'name': 'NISCOPE_VAL_FFT_AMPLITUDE',
                'value': 1009
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_AVERAGE',
                'value': 10
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_CYCLE_AVERAGE',
                'value': 17
            },
            {
                'name': 'NISCOPE_VAL_DC_ESTIMATE',
                'value': 1013
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_MAX',
                'value': 6
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_MIN',
                'value': 7
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_PEAK_TO_PEAK',
                'value': 5
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HIGH',
                'value': 8
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_LOW',
                'value': 9
            },
            {
                'name': 'NISCOPE_VAL_AMPLITUDE',
                'value': 15
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_TOP',
                'value': 1007
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_BASE',
                'value': 1006
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_BASE_TO_TOP',
                'value': 1017
            },
            {
                'name': 'NISCOPE_VAL_WIDTH_NEG',
                'value': 11
            },
            {
                'name': 'NISCOPE_VAL_WIDTH_POS',
                'value': 12
            },
            {
                'name': 'NISCOPE_VAL_DUTY_CYCLE_NEG',
                'value': 13
            },
            {
                'name': 'NISCOPE_VAL_DUTY_CYCLE_POS',
                'value': 14
            },
            {
                'name': 'NISCOPE_VAL_INTEGRAL',
                'value': 1005
            },
            {
                'name': 'NISCOPE_VAL_AREA',
                'value': 1003
            },
            {
                'name': 'NISCOPE_VAL_CYCLE_AREA',
                'value': 1004
            },
            {
                'name': 'NISCOPE_VAL_TIME_DELAY',
                'value': 1014
            },
            {
                'name': 'NISCOPE_VAL_PHASE_DELAY',
                'value': 1018
            },
            {
                'name': 'NISCOPE_VAL_LOW_REF_VOLTS',
                'value': 1000
            },
            {
                'name': 'NISCOPE_VAL_MID_REF_VOLTS',
                'value': 1001
            },
            {
                'name': 'NISCOPE_VAL_HIGH_REF_VOLTS',
                'value': 1002
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN',
                'value': 2000
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_STDEV',
                'value': 2001
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEDIAN',
                'value': 2003
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_MODE',
                'value': 2010
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_MAX',
                'value': 2005
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_MIN',
                'value': 2006
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_PEAK_TO_PEAK',
                'value': 2002
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN_PLUS_STDEV',
                'value': 2007
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN_PLUS_2_STDEV',
                'value': 2008
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN_PLUS_3_STDEV',
                'value': 2009
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_HITS',
                'value': 2004
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_NEW_HITS',
                'value': 2011
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_MEAN',
                'value': 3000
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_STDEV',
                'value': 3001
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_MEDIAN',
                'value': 3003
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_MODE',
                'value': 3010
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_MAX',
                'value': 3005
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_MIN',
                'value': 3006
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_PEAK_TO_PEAK',
                'value': 3002
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_MEAN_PLUS_STDEV',
                'value': 3007
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_MEAN_PLUS_2_STDEV',
                'value': 3008
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_MEAN_PLUS_3_STDEV',
                'value': 3009
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_HITS',
                'value': 3004
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_NEW_HITS',
                'value': 3011
            }
        ]
    },
    'CoordinateConverterInput': {
        'values': [
            {
                'documentation': {
                    'description': '\nSelects the HB filter as the source for the input to the coordinate\nconverter.\n'
                },
                'name': 'NISCOPE_VAL_RESAMPLER_HB',
                'value': 0
            },
            {
                'documentation': {
                    'description': '\nSelects the programmable FIR filter as the source for the input to the\ncoordinate converter.\n'
                },
                'name': 'NISCOPE_VAL_PROGRAMMABLE_FIR',
                'value': 1
            }
        ]
    },
    'DataJustificationMode': {
        'values': [
            {
                'documentation': {
                    'description': ''
                },
                'name': 'NISCOPE_VAL_LEFT',
                'value': 1
            },
            {
                'documentation': {
                    'description': ''
                },
                'name': 'NISCOPE_VAL_RIGHT',
                'value': 2
            }
        ]
    },
    'DataProcessingMode': {
        'values': [
            {
                'documentation': {
                    'description': 'The waveform data points are real numbers (I data).'
                },
                'name': 'NISCOPE_VAL_REAL',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'The waveform data points are complex numbers (IQ data).'
                },
                'name': 'NISCOPE_VAL_COMPLEX',
                'value': 1
            }
        ]
    },
    'DiscriminatorFIRInputSource': {
        'values': [
            {
                'documentation': {
                    'description': 'Sets the discriminator FIR input source to phase.'
                },
                'name': 'NISCOPE_VAL_PHASE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Sets the discriminator FIR input source to magnitude.'
                },
                'name': 'NISCOPE_VAL_MAGNITUDE',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Sets the discriminator FIR input source to resampler.'
                },
                'name': 'NISCOPE_VAL_RESAMPLER',
                'value': 2
            }
        ]
    },
    'DiscriminatorFIRSymmetry': {
        'values': [
            {
                'documentation': {
                    'description': 'Sets the discriminator FIR symmetry to symmetric.'
                },
                'name': 'NISCOPE_VAL_SYMMETRIC',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Sets the discriminator FIR symmetry to asymmetric.'
                },
                'name': 'NISCOPE_VAL_ASYMMETRIC',
                'value': 1
            }
        ]
    },
    'DiscriminatorFIRSymmetryType': {
        'values': [
            {
                'documentation': {
                    'description': 'Sets the discriminator FIR symmetry type to even.'
                },
                'name': 'NISCOPE_VAL_EVEN',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Sets the discriminator FIR symmetry type to odd.'
                },
                'name': 'NISCOPE_VAL_ODD',
                'value': 1
            }
        ]
    },
    'ExportableSignals': {
        'values': [
            {
                'name': 'NISCOPE_VAL_START_TRIGGER',
                'value': 2
            },
            {
                'name': 'NISCOPE_VAL_ADVANCE_TRIGGER',
                'value': 5
            },
            {
                'name': 'NISCOPE_VAL_REF_TRIGGER',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_END_OF_RECORD_EVENT',
                'value': 4
            },
            {
                'name': 'NISCOPE_VAL_END_OF_ACQUISITION_EVENT',
                'value': 3
            },
            {
                'name': 'NISCOPE_VAL_READY_FOR_START_EVENT',
                'value': 7
            },
            {
                'name': 'NISCOPE_VAL_READY_FOR_ADVANCE_EVENT',
                'value': 6
            },
            {
                'name': 'NISCOPE_VAL_READY_FOR_REF_EVENT',
                'value': 10
            },
            {
                'name': 'NISCOPE_VAL_REF_CLOCK',
                'value': 100
            },
            {
                'name': 'NISCOPE_VAL_SAMPLE_CLOCK',
                'value': 101
            },
            {
                'name': 'NISCOPE_VAL_5V_OUT',
                'python_name': 'FIVE_V_OUT',
                'value': 13
            }
        ]
    },
    'FIRFilterWindow': {
        'values': [
            {
                'documentation': {
                    'description': 'No window.'
                },
                'name': 'NISCOPE_VAL_NONE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Specifies a Hanning window.'
                },
                'name': 'NISCOPE_VAL_HANNING',
                'value': 409
            },
            {
                'documentation': {
                    'description': 'Specifies a Flat Top window.'
                },
                'name': 'NISCOPE_VAL_FLAT_TOP',
                'value': 410
            },
            {
                'documentation': {
                    'description': 'Specifies a Hamming window.'
                },
                'name': 'NISCOPE_VAL_HAMMING',
                'value': 420
            },
            {
                'documentation': {
                    'description': 'Specifies a Triangle window.'
                },
                'name': 'NISCOPE_VAL_TRIANGLE',
                'value': 423
            },
            {
                'documentation': {
                    'description': 'Specifies a Blackman window.'
                },
                'name': 'NISCOPE_VAL_BLACKMAN',
                'value': 424
            }
        ]
    },
    'FetchRelativeTo': {
        'values': [
            {
                'documentation': {
                    'description': 'The read pointer is set to zero when a new acquisition is initiated. After every fetch the read pointer is incremeted to be the sample after the last sample retrieved.  Therefore, you can repeatedly fetch relative to the read pointer for a continuous acquisition program.'
                },
                'name': 'NISCOPE_VAL_READ_POINTER',
                'value': 388
            },
            {
                'documentation': {
                    'description': 'Fetches relative to the first pretrigger point requested with niScope_ConfigureHorizontalTiming.'
                },
                'name': 'NISCOPE_VAL_PRETRIGGER',
                'value': 477
            },
            {
                'documentation': {
                    'description': 'Fetch data at the last sample acquired.'
                },
                'name': 'NISCOPE_VAL_NOW',
                'value': 481
            },
            {
                'documentation': {
                    'description': 'Fetch data starting at the first point sampled by the digitizer.'
                },
                'name': 'NISCOPE_VAL_START',
                'value': 482
            },
            {
                'documentation': {
                    'description': 'Fetch at the first posttrigger sample.'
                },
                'name': 'NISCOPE_VAL_TRIGGER',
                'value': 483
            }
        ]
    },
    'FilterType': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies lowpass as the filter type.'
                },
                'name': 'NISCOPE_VAL_LOWPASS',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Specifies highpass as the filter type.'
                },
                'name': 'NISCOPE_VAL_HIGHPASS',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Specifies bandpass as the filter type.'
                },
                'name': 'NISCOPE_VAL_BANDPASS',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Specifies bandstop as the filter type.'
                },
                'name': 'NISCOPE_VAL_BANDSTOP',
                'value': 3
            }
        ]
    },
    'FlexFIRAntialiasFilterType': {
        'values': [
            {
                'documentation': {
                    'description': 'This filter is optimized for alias protection and frequency-domain flatness'
                },
                'name': 'NISCOPE_VAL_48_TAP_STANDARD',
                'python_name': 'FOURTYEIGHT_TAP_STANDARD',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'This filter is optimized for the lowest possible bandwidth for a 48 tap filter and maximizes the SNR'
                },
                'name': 'NISCOPE_VAL_48_TAP_HANNING',
                'python_name': 'FOURTYEIGHT_TAP_HANNING',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'This filter is optimized for the lowest possible bandwidth for a 16 tap filter and maximizes the SNR'
                },
                'name': 'NISCOPE_VAL_16_TAP_HANNING',
                'python_name': 'SIXTEEN_TAP_HANNING',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'This filter is optimized for the lowest possible bandwidth for a 8 tap filter and maximizes the SNR'
                },
                'name': 'NISCOPE_VAL_8_TAP_HANNING',
                'python_name': 'EIGHT_TAP_HANNING',
                'value': 3
            }
        ]
    },
    'NotificationType': {
        'values': [
            {
                'documentation': {
                    'description': 'Never send notification.'
                },
                'name': 'NISCOPE_VAL_NOTIFY_NEVER',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Notify when digitizer acquisition is done.'
                },
                'name': 'NISCOPE_VAL_NOTIFY_DONE',
                'value': 1
            }
        ]
    },
    'Option': {
        'values': [
            {
                'documentation': {
                    'description': 'Self Calibrating all Channels'
                },
                'name': 'NISCOPE_VAL_SELF_CALIBRATE_ALL_CHANNELS',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Restore External Calibration.'
                },
                'name': 'NISCOPE_VAL_RESTORE_EXTERNAL_CALIBRATION',
                'value': 1
            }
        ]
    },
    'OverflowErrorReporting': {
        'values': [
            {
                'documentation': {
                    'description': '\nExecution stops and NI-SCOPE returns an error when an overflow has\noccurred in the OSP block.\n'
                },
                'name': 'NISCOPE_VAL_ERROR_REPORTING_ERROR',
                'value': 0
            },
            {
                'documentation': {
                    'description': '\nExecution continues and NI-SCOPE returns a warning when an overflow has\noccurred in the OSP block.\n'
                },
                'name': 'NISCOPE_VAL_ERROR_REPORTING_WARNING',
                'value': 1
            },
            {
                'documentation': {
                    'description': '\nNI-SCOPE does not return an error when an overflow has occurred in the\nOSP block.\n'
                },
                'name': 'NISCOPE_VAL_ERROR_REPORTING_DISABLED',
                'value': 2
            }
        ]
    },
    'PercentageMethod': {
        'values': [
            {
                'documentation': {
                    'description': '\nSpecifies that the reference level percentages should be computed using\nthe low/high method,\n'
                },
                'name': 'NISCOPE_VAL_LOWHIGH',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Reference level percentages are computed using the min/max method.'
                },
                'name': 'NISCOPE_VAL_MINMAX',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Reference level percentages are computed using the base/top method.'
                },
                'name': 'NISCOPE_VAL_BASETOP',
                'value': 2
            }
        ]
    },
    'ProgFIRFilterRealComplex': {
        'values': [
            {
                'documentation': {
                    'description': 'Sets a dual real filter.'
                },
                'name': 'NISCOPE_VAL_REAL',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Sets a complex filter.'
                },
                'name': 'NISCOPE_VAL_COMPLEX',
                'value': 1
            }
        ]
    },
    'ProgFIRFilterSymmetry': {
        'values': [
            {
                'documentation': {
                    'description': 'Sets a symmetric filter.'
                },
                'name': 'NISCOPE_VAL_SYMMETRIC',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Sets an asymmetric filter.'
                },
                'name': 'NISCOPE_VAL_ASYMMETRIC',
                'value': 1
            }
        ]
    },
    'ProgFIRFilterSymmetryType': {
        'values': [
            {
                'documentation': {
                    'description': 'Sets the discriminator FIR symmetry type to even.'
                },
                'name': 'NISCOPE_VAL_EVEN',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Sets the discriminator FIR symmetry type to odd.'
                },
                'name': 'NISCOPE_VAL_ODD',
                'value': 1
            }
        ]
    },
    'QInputToCoordConverter': {
        'values': [
            {
                'documentation': {
                    'description': 'Enables the Q input to coordinate converter.'
                },
                'name': 'NISCOPE_VAL_I_AND_Q',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Zeroes out the Q input the to coordinate converter.'
                },
                'name': 'NISCOPE_VAL_Q_ZEROED',
                'value': 1
            }
        ]
    },
    'RISMethod': {
        'values': [
            {
                'documentation': {
                    'description': 'Acquires exactly the specified number of records for each bin in the RIS acquisition.  An error is returned from the fetch function if the RIS acquisition does not successfully acquire the specified number of waveforms within the timeout period.  You may call the fetch function again to allow more time for the acquisition to finish.'
                },
                'name': 'NISCOPE_VAL_RIS_EXACT_NUM_AVERAGES',
                'value': 1
            },
            {
                'documentation': {
                    'description': '\nEach RIS sample is the average of a least a minimum number of randomly\ndistributed points.\n'
                },
                'name': 'NISCOPE_VAL_RIS_MIN_NUM_AVERAGES',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Returns the RIS waveform after the specified timeout even if it is incomplete.  If no waveforms have been acquired in certain bins, these bins will have a NaN (when fetching scaled data) or a zero (when fetching binary data). A warning (positive error code) is returned from the fetch function if the RIS acquisition did not finish.  The acquisition aborts when data is returned.'
                },
                'name': 'NISCOPE_VAL_RIS_INCOMPLETE',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'Limits the waveforms in the various bins to be within 200 ps of the center of the bin.'
                },
                'name': 'NISCOPE_VAL_RIS_LIMITED_BIN_WIDTH',
                'value': 5
            }
        ]
    },
    'RefLevelUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies that the reference levels are given in units of volts.'
                },
                'name': 'NISCOPE_VAL_VOLTS',
                'value': 0
            },
            {
                'documentation': {
                    'description': '\n(Default) Specifies that the reference levels are given in percentage\nunits.\n'
                },
                'name': 'NISCOPE_VAL_PERCENTAGE',
                'value': 1
            }
        ]
    },
    'RefTriggerDetectorLocation': {
        'values': [
            {
                'documentation': {
                    'description': 'use the hardware analog circuitry to implement the reference trigger.  This option will trigger before any onboard signal processing.'
                },
                'name': 'NISCOPE_VAL_ANALOG_DETECTION_CIRCUIT',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'use the onboard signal processing logic to implement the reference trigger.  This option will trigger based on the onboard signal processed data.'
                },
                'name': 'NISCOPE_VAL_DDC_OUTPUT',
                'value': 1
            }
        ]
    },
    'ResamplerFilterMode': {
        'values': [
            {
                'documentation': {
                    'description': 'Resampler enabled.'
                },
                'name': 'NISCOPE_VAL_RESAMPLER_ENABLED',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'HB 1 enabled.'
                },
                'name': 'NISCOPE_VAL_HB_1_ENABLED',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Resampler and HB 1.'
                },
                'name': 'NISCOPE_VAL_RESAMPLER_AND_HB_1',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'Both HB Filters.'
                },
                'name': 'NISCOPE_VAL_BOTH_HB_FILTERS',
                'value': 6
            },
            {
                'documentation': {
                    'description': 'Resampler and Both HB Filters.'
                },
                'name': 'NISCOPE_VAL_RESAMPLER_AND_BOTH_HB_FILTERS',
                'value': 7
            }
        ]
    },
    'ScalarMeasurement': {
        'values': [
            {
                'documentation': {
                    'description': 'None'
                },
                'name': 'NISCOPE_VAL_NO_MEASUREMENT',
                'value': 4000
            },
            {
                'name': 'NISCOPE_VAL_FREQUENCY',
                'value': 2
            },
            {
                'name': 'NISCOPE_VAL_AVERAGE_FREQUENCY',
                'value': 1016
            },
            {
                'name': 'NISCOPE_VAL_FFT_FREQUENCY',
                'value': 1008
            },
            {
                'name': 'NISCOPE_VAL_PERIOD',
                'value': 3
            },
            {
                'name': 'NISCOPE_VAL_AVERAGE_PERIOD',
                'value': 1015
            },
            {
                'name': 'NISCOPE_VAL_RISE_TIME',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_FALL_TIME',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_RISE_SLEW_RATE',
                'value': 1010
            },
            {
                'name': 'NISCOPE_VAL_FALL_SLEW_RATE',
                'value': 1011
            },
            {
                'name': 'NISCOPE_VAL_OVERSHOOT',
                'value': 18
            },
            {
                'name': 'NISCOPE_VAL_PRESHOOT',
                'value': 19
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_RMS',
                'value': 4
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_CYCLE_RMS',
                'value': 16
            },
            {
                'name': 'NISCOPE_VAL_AC_ESTIMATE',
                'value': 1012
            },
            {
                'name': 'NISCOPE_VAL_FFT_AMPLITUDE',
                'value': 1009
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_AVERAGE',
                'value': 10
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_CYCLE_AVERAGE',
                'value': 17
            },
            {
                'name': 'NISCOPE_VAL_DC_ESTIMATE',
                'value': 1013
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_MAX',
                'value': 6
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_MIN',
                'value': 7
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_PEAK_TO_PEAK',
                'value': 5
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HIGH',
                'value': 8
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_LOW',
                'value': 9
            },
            {
                'name': 'NISCOPE_VAL_AMPLITUDE',
                'value': 15
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_TOP',
                'value': 1007
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_BASE',
                'value': 1006
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_BASE_TO_TOP',
                'value': 1017
            },
            {
                'name': 'NISCOPE_VAL_WIDTH_NEG',
                'value': 11
            },
            {
                'name': 'NISCOPE_VAL_WIDTH_POS',
                'value': 12
            },
            {
                'name': 'NISCOPE_VAL_DUTY_CYCLE_NEG',
                'value': 13
            },
            {
                'name': 'NISCOPE_VAL_DUTY_CYCLE_POS',
                'value': 14
            },
            {
                'name': 'NISCOPE_VAL_INTEGRAL',
                'value': 1005
            },
            {
                'name': 'NISCOPE_VAL_AREA',
                'value': 1003
            },
            {
                'name': 'NISCOPE_VAL_CYCLE_AREA',
                'value': 1004
            },
            {
                'name': 'NISCOPE_VAL_TIME_DELAY',
                'value': 1014
            },
            {
                'name': 'NISCOPE_VAL_PHASE_DELAY',
                'value': 1018
            },
            {
                'name': 'NISCOPE_VAL_LOW_REF_VOLTS',
                'value': 1000
            },
            {
                'name': 'NISCOPE_VAL_MID_REF_VOLTS',
                'value': 1001
            },
            {
                'name': 'NISCOPE_VAL_HIGH_REF_VOLTS',
                'value': 1002
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN',
                'value': 2000
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_STDEV',
                'value': 2001
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEDIAN',
                'value': 2003
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_MODE',
                'value': 2010
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_MAX',
                'value': 2005
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_MIN',
                'value': 2006
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_PEAK_TO_PEAK',
                'value': 2002
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN_PLUS_STDEV',
                'value': 2007
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN_PLUS_2_STDEV',
                'value': 2008
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN_PLUS_3_STDEV',
                'value': 2009
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_HITS',
                'value': 2004
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_NEW_HITS',
                'value': 2011
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_MEAN',
                'value': 3000
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_STDEV',
                'value': 3001
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_MEDIAN',
                'value': 3003
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_MODE',
                'value': 3010
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_MAX',
                'value': 3005
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_MIN',
                'value': 3006
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_PEAK_TO_PEAK',
                'value': 3002
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_MEAN_PLUS_STDEV',
                'value': 3007
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_MEAN_PLUS_2_STDEV',
                'value': 3008
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_HITS',
                'value': 3004
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_NEW_HITS',
                'value': 3011
            }
        ]
    },
    'StreamingPositionType': {
        'values': [
            {
                'documentation': {
                    'description': 'Data is streamed from the start trigger.'
                },
                'name': 'NISCOPE_VAL_START_TRIGGER',
                'value': 2
            },
            {
                'documentation': {
                    'description': '\nData is streamed relative to the reference trigger and reference\nposition.\n'
                },
                'name': 'NISCOPE_VAL_REFERENCE_TRIGGER',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Data is streamed relative to the sync trigger and reference position.'
                },
                'name': 'NISCOPE_VAL_SYNC_TRIGGER',
                'value': 2
            }
        ]
    },
    'SyncoutClkSelect': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies CLKIN as the source for Syncout CLK.'
                },
                'name': 'NISCOPE_VAL_CLKIN',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Specifies PROCCLK as the source for Syncout CLK.'
                },
                'name': 'NISCOPE_VAL_PROCCLK',
                'value': 1
            }
        ]
    },
    'TerminalConfiguration': {
        'values': [
            {
                'documentation': {
                    'description': 'Channel is single ended'
                },
                'name': 'NISCOPE_VAL_SINGLE_ENDED',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Channel is unbalanced differential'
                },
                'name': 'NISCOPE_VAL_UNBALANCED_DIFFERENTIAL',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Channel is differential'
                },
                'name': 'NISCOPE_VAL_DIFFERENTIAL',
                'value': 2
            }
        ]
    },
    'TimingNcoFreqOffsetBits': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies 8 offset bits in the timing NCO.'
                },
                'name': 'NISCOPE_VAL__8_BITS',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Specifies 16 offset bits in the timing NCO.'
                },
                'name': 'NISCOPE_VAL__16_BITS',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Specifies 24 offset bits in the timing NCO.'
                },
                'name': 'NISCOPE_VAL__24_BITS',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Specifies 32 offset bits in the timing NCO.'
                },
                'name': 'NISCOPE_VAL__32_BITS',
                'value': 3
            }
        ]
    },
    'TriggerCoupling': {
        'values': [
            {
                'documentation': {
                    'description': 'AC coupling'
                },
                'name': 'NISCOPE_VAL_AC',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'DC coupling'
                },
                'name': 'NISCOPE_VAL_DC',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Highpass filter coupling'
                },
                'name': 'NISCOPE_VAL_HF_REJECT',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'Lowpass filter coupling'
                },
                'name': 'NISCOPE_VAL_LF_REJECT',
                'value': 4
            },
            {
                'documentation': {
                    'description': 'Highpass and lowpass filter coupling'
                },
                'name': 'NISCOPE_VAL_AC_PLUS_HF_REJECT',
                'value': 1001
            }
        ]
    },
    'TriggerModifier': {
        'values': [
            {
                'documentation': {
                    'description': 'Normal triggering.'
                },
                'name': 'NISCOPE_VAL_NO_TRIGGER_MOD',
                'value': 1
            },
            {
                'documentation': {
                    'description': '\nSoftware will trigger an acquisition automatically if no trigger arrives\nafter a certain amount of time.\n'
                },
                'name': 'NISCOPE_VAL_AUTO',
                'value': 2
            }
        ]
    },
    'TriggerSlope': {
        'values': [
            {
                'documentation': {
                    'description': 'Falling edge'
                },
                'name': 'NISCOPE_VAL_NEGATIVE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Rising edge'
                },
                'name': 'NISCOPE_VAL_POSITIVE',
                'value': 1
            }
        ]
    },
    'TriggerType': {
        'values': [
            {
                'documentation': {
                    'description': 'Configures the digitizer for edge triggering.  An edge trigger occurs when the trigger signal crosses the trigger level specified with the set trigger slope.  You configure the trigger level and slope with niScope_ConfigureTriggerEdge.'
                },
                'name': 'NISCOPE_VAL_EDGE_TRIGGER',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Configures the digitizer for video/TV triggering.   You configure the video trigger parameters like signal Format, Line to trigger off of, Polarity, and Enable DC Restore with niScope_ConfigureTriggerVideo.'
                },
                'name': 'NISCOPE_VAL_TV_TRIGGER',
                'value': 5
            },
            {
                'documentation': {
                    'description': 'Configures the digitizer for immediate triggering.   An immediate trigger occurs as soon as the pretrigger samples are acquired.'
                },
                'name': 'NISCOPE_VAL_IMMEDIATE_TRIGGER',
                'value': 6
            },
            {
                'documentation': {
                    'description': 'Configures the digitizer for hysteresis triggering.  A hysteresis trigger occurs when the trigger signal crosses the trigger level with the specified slope and passes through the hysteresis window you specify. You configure the trigger level, slope, and hysteresis with niScope_ConfigureTriggerHysteresis.'
                },
                'name': 'NISCOPE_VAL_HYSTERESIS_TRIGGER',
                'value': 1001
            },
            {
                'documentation': {
                    'description': 'Configures the digitizer for digital triggering. A digital trigger occurs when the trigger signal has the specified slope. You configure the trigger slope with niScope_ConfigureTriggerDigital.'
                },
                'name': 'NISCOPE_VAL_DIGITAL_TRIGGER',
                'value': 1002
            },
            {
                'documentation': {
                    'description': 'Configures the digitizer for window triggering.  A window trigger occurs when the trigger signal enters or leaves the window defined by the values you specify with the Low Window Level, High Window Level, and Window Mode Parameters.  You configure the low window level high window level, and window mode with niScope_ConfigureTriggerWindow.'
                },
                'name': 'NISCOPE_VAL_WINDOW_TRIGGER',
                'value': 1003
            },
            {
                'documentation': {
                    'description': 'Configures the digitizer for software triggering.  A software trigger occurs when niScope_SendSoftwareTrigger is called.'
                },
                'name': 'NISCOPE_VAL_SOFTWARE_TRIGGER',
                'value': 1004
            }
        ]
    },
    'TriggerWindowMode': {
        'values': [
            {
                'documentation': {
                    'description': 'Trigger upon entering the window'
                },
                'name': 'NISCOPE_VAL_ENTERING_WINDOW',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Trigger upon leaving the window'
                },
                'name': 'NISCOPE_VAL_LEAVING_WINDOW',
                'value': 1
            }
        ]
    },
    'VerticalCoupling': {
        'values': [
            {
                'documentation': {
                    'description': 'AC coupling'
                },
                'name': 'NISCOPE_VAL_AC',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'DC coupling'
                },
                'name': 'NISCOPE_VAL_DC',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'GND coupling'
                },
                'name': 'NISCOPE_VAL_GND',
                'value': 2
            }
        ]
    },
    'VideoPolarity': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies that the video signal has positive polarity.'
                },
                'name': 'NISCOPE_VAL_TV_POSITIVE',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Specifies that the video signal has negative polarity.'
                },
                'name': 'NISCOPE_VAL_TV_NEGATIVE',
                'value': 2
            }
        ]
    },
    'VideoSignalFormat': {
        'values': [
            {
                'documentation': {
                    'description': 'NTSC signal format supports line numbers from 1 to 525'
                },
                'name': 'NISCOPE_VAL_NTSC',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'PAL signal format supports line numbers from 1 to 625'
                },
                'name': 'NISCOPE_VAL_PAL',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'SECAM signal format supports line numbers from 1 to 625'
                },
                'name': 'NISCOPE_VAL_SECAM',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'M-PAL signal format supports line numbers from 1 to 525'
                },
                'name': 'NISCOPE_VAL_M_PAL',
                'value': 1001
            },
            {
                'documentation': {
                    'description': '480 lines, interlaced, 59.94 fields per second'
                },
                'name': 'NISCOPE_VAL_VIDEO_480I_59_94_FIELDS_PER_SECOND',
                'value': 1010
            },
            {
                'documentation': {
                    'description': '480 lines, interlaced, 60 fields per second'
                },
                'name': 'NISCOPE_VAL_VIDEO_480I_60_FIELDS_PER_SECOND',
                'value': 1011
            },
            {
                'documentation': {
                    'description': '480 lines, progressive, 59.94 frames per second'
                },
                'name': 'NISCOPE_VAL_VIDEO_480P_59_94_FRAMES_PER_SECOND',
                'value': 1015
            },
            {
                'documentation': {
                    'description': '480 lines, progressive,60 frames per second'
                },
                'name': 'NISCOPE_VAL_VIDEO_480P_60_FRAMES_PER_SECOND',
                'value': 1016
            },
            {
                'documentation': {
                    'description': '576 lines, interlaced, 50 fields per second'
                },
                'name': 'NISCOPE_VAL_VIDEO_576I_50_FIELDS_PER_SECOND',
                'value': 1020
            },
            {
                'documentation': {
                    'description': '576 lines, progressive, 50 frames per second'
                },
                'name': 'NISCOPE_VAL_VIDEO_576P_50_FRAMES_PER_SECOND',
                'value': 1025
            },
            {
                'documentation': {
                    'description': '720 lines, progressive, 50 frames per second'
                },
                'name': 'NISCOPE_VAL_VIDEO_720P_50_FRAMES_PER_SECOND',
                'value': 1031
            },
            {
                'documentation': {
                    'description': '720 lines, progressive, 59.94 frames per second'
                },
                'name': 'NISCOPE_VAL_VIDEO_720P_59_94_FRAMES_PER_SECOND',
                'value': 1032
            },
            {
                'documentation': {
                    'description': '720 lines, progressive, 60 frames per second'
                },
                'name': 'NISCOPE_VAL_VIDEO_720P_60_FRAMES_PER_SECOND',
                'value': 1033
            },
            {
                'documentation': {
                    'description': '1,080 lines, interlaced, 50 fields per second'
                },
                'name': 'NISCOPE_VAL_VIDEO_1080I_50_FIELDS_PER_SECOND',
                'value': 1040
            },
            {
                'documentation': {
                    'description': '1,080 lines, interlaced, 59.94 fields per second'
                },
                'name': 'NISCOPE_VAL_VIDEO_1080I_59_94_FIELDS_PER_SECOND',
                'value': 1041
            },
            {
                'documentation': {
                    'description': '1,080 lines, interlaced, 60 fields per second'
                },
                'name': 'NISCOPE_VAL_VIDEO_1080I_60_FIELDS_PER_SECOND',
                'value': 1042
            },
            {
                'documentation': {
                    'description': '1,080 lines, progressive, 24 frames per second'
                },
                'name': 'NISCOPE_VAL_VIDEO_1080P_24_FRAMES_PER_SECOND',
                'value': 1045
            }
        ]
    },
    'VideoTriggerEvent': {
        'values': [
            {
                'documentation': {
                    'description': 'Trigger on field 1 of the signal'
                },
                'name': 'NISCOPE_VAL_TV_EVENT_FIELD1',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Trigger on field 2 of the signal'
                },
                'name': 'NISCOPE_VAL_TV_EVENT_FIELD2',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Trigger on the first field acquired'
                },
                'name': 'NISCOPE_VAL_TV_EVENT_ANY_FIELD',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'Trigger on the first line acquired'
                },
                'name': 'NISCOPE_VAL_TV_EVENT_ANY_LINE',
                'value': 4
            },
            {
                'documentation': {
                    'description': 'Trigger on a specific line of a video signal.  Valid values vary depending on the signal format configured.'
                },
                'name': 'NISCOPE_VAL_TV_EVENT_LINE_NUMBER',
                'value': 5
            }
        ]
    },
    'WhichTrigger': {
        'values': [
            {
                'name': 'NISCOPE_VAL_SOFTWARE_TRIGGER_START',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_SOFTWARE_TRIGGER_ARM_REFERENCE',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_SOFTWARE_TRIGGER_REFERENCE',
                'value': 2
            },
            {
                'name': 'NISCOPE_VAL_SOFTWARE_TRIGGER_ADVANCE',
                'value': 3
            }
        ]
    }
}
