# -*- coding: utf-8 -*-
# This file is generated from NI-FGEN API metadata version 23.0.0d13
enums = {
    'AnalogPath': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies use of the main path.  NI-FGEN chooses the amplifier based on the user-specified gain.'
                },
                'name': 'NIFGEN_VAL_MAIN_ANALOG_PATH',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Specifies use of the direct path.'
                },
                'name': 'NIFGEN_VAL_DIRECT_ANALOG_PATH',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Specifies use of the low-gain amplifier in the main path, no matter  what value the user specifies for gain. This setting limits the output  range.'
                },
                'name': 'NIFGEN_VAL_FIXED_LOW_GAIN_ANALOG_PATH',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Specifies use of the high-gain amplifier in the main path.'
                },
                'name': 'NIFGEN_VAL_FIXED_HIGH_GAIN_ANALOG_PATH',
                'value': 3
            }
        ]
    },
    'ArbitrarySequenceHandle': {
        'values': [
            {
                'name': 'NIFGEN_VAL_FIRST_SEQUENCE_HANDLE',
                'value': 100000
            },
            {
                'name': 'NIFGEN_VAL_LAST_SEQUENCE_HANDLE',
                'value': 109999
            },
            {
                'name': 'NIFGEN_VAL_NO_SEQUENCE',
                'value': -1
            }
        ]
    },
    'ArbitraryWaveformHandle': {
        'values': [
            {
                'name': 'NIFGEN_VAL_FIRST_WAVEFORM_HANDLE',
                'value': 10000
            },
            {
                'name': 'NIFGEN_VAL_LAST_WAVEFORM_HANDLE',
                'value': 10999
            },
            {
                'name': 'NIFGEN_VAL_NO_WAVEFORM',
                'value': -1
            }
        ]
    },
    'BurstCount': {
        'values': [
            {
                'name': 'NIFGEN_VAL_GENERATE_CONTINUOUS',
                'value': -1
            }
        ]
    },
    'BusType': {
        'values': [
            {
                'documentation': {
                    'description': 'Indicates an invalid bus type.'
                },
                'name': 'NIFGEN_VAL_BUS_INVALID',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Indicates the signal generator is the AT bus type.'
                },
                'name': 'NIFGEN_VAL_BUS_AT',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Indicates the signal generator is the PCI bus type.'
                },
                'name': 'NIFGEN_VAL_BUS_PCI',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Indicates the signal generator is the PXI bus type.'
                },
                'name': 'NIFGEN_VAL_BUS_PXI',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'Indicates the signal generator is the VXI bus type.'
                },
                'name': 'NIFGEN_VAL_BUS_VXI',
                'value': 4
            },
            {
                'documentation': {
                    'description': 'Indicates the signal generator is the PCI-CMA bus type.'
                },
                'name': 'NIFGEN_VAL_BUS_PCMCIA',
                'value': 5
            },
            {
                'documentation': {
                    'description': 'Indicates the signal generator is the PXI Express bus type.'
                },
                'name': 'NIFGEN_VAL_BUS_PXIE',
                'value': 6
            }
        ]
    },
    'ByteOrder': {
        'values': [
            {
                'name': 'NIFGEN_VAL_LITTLE_ENDIAN',
                'value': 0
            },
            {
                'name': 'NIFGEN_VAL_BIG_ENDIAN',
                'value': 1
            }
        ]
    },
    'CalAdcInput': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies that the ADC measures the analog output.'
                },
                'name': 'NIFGEN_VAL_ANALOG_OUTPUT',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Specifies that the ADC measures the internal voltage reference.'
                },
                'name': 'NIFGEN_VAL_INTERNAL_VOLTAGE_REFERENCE',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Specifies that the ADC measures the ground voltage.'
                },
                'name': 'NIFGEN_VAL_GROUND',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Specifies that the ADC measures the differential analog output.'
                },
                'name': 'NIFGEN_VAL_ANALOG_OUTPUT_DIFFERENTIAL',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'Specifies that the ADC measures the positive differential analog output.'
                },
                'name': 'NIFGEN_VAL_ANALOG_OUTPUT_PLUS',
                'value': 4
            },
            {
                'documentation': {
                    'description': 'Specifies that the ADC measures the negative differential analog output.'
                },
                'name': 'NIFGEN_VAL_ANALOG_OUTPUT_MINUS',
                'value': 5
            },
            {
                'documentation': {
                    'description': 'Specifies that the ADC measures the idle analog output.'
                },
                'name': 'NIFGEN_VAL_ANALOG_OUTPUT_IDLE',
                'value': 6
            }
        ]
    },
    'ClockMode': {
        'values': [
            {
                'documentation': {
                    'description': 'High resolution sampling—Sample rate is generated by a high–resolution clock source.'
                },
                'name': 'NIFGEN_VAL_HIGH_RESOLUTION',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Divide down sampling—Sample rates are generated by dividing the source frequency.'
                },
                'name': 'NIFGEN_VAL_DIVIDE_DOWN',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Automatic Selection—NI-FGEN selects between the divide–down and high–resolution clocking modes.'
                },
                'name': 'NIFGEN_VAL_AUTOMATIC',
                'value': 2
            }
        ]
    },
    'DataMarkerEventLevelPolarity': {
        'values': [
            {
                'documentation': {
                    'description': 'When the operation is ready to start, the Ready for Start  event level is high.'
                },
                'name': 'NIFGEN_VAL_ACTIVE_HIGH',
                'value': 101
            },
            {
                'documentation': {
                    'description': 'When the operation is ready to start, the Ready for Start  event level is low.'
                },
                'name': 'NIFGEN_VAL_ACTIVE_LOW',
                'value': 102
            }
        ]
    },
    'DataProcessingMode': {
        'values': [
            {
                'documentation': {
                    'description': 'The waveform data points are real numbers (I data).'
                },
                'name': 'NIFGEN_VAL_OSP_REAL',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'The waveform data points are complex numbers (I/Q data).'
                },
                'name': 'NIFGEN_VAL_OSP_COMPLEX',
                'value': 1
            }
        ]
    },
    'DoneEventActiveLevel': {
        'values': [
            {
                'documentation': {
                    'description': 'When the operation is ready to start, the Ready for Start  event level is high.'
                },
                'name': 'NIFGEN_VAL_ACTIVE_HIGH',
                'value': 101
            },
            {
                'documentation': {
                    'description': 'When the operation is ready to start, the Ready for Start  event level is low.'
                },
                'name': 'NIFGEN_VAL_ACTIVE_LOW',
                'value': 102
            }
        ]
    },
    'DoneEventDelayUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies the pulse width in Sample clock periods.'
                },
                'name': 'NIFGEN_VAL_SAMPLE_CLOCK_PERIODS',
                'value': 101
            },
            {
                'documentation': {
                    'description': 'Specifies the pulse width in seconds.'
                },
                'name': 'NIFGEN_VAL_SECONDS',
                'value': 102
            }
        ]
    },
    'DoneEventOutputBehavior': {
        'values': [
            {
                'documentation': {
                    'description': 'Triggers a pulse for a specified period of time.'
                },
                'name': 'NIFGEN_VAL_PULSE',
                'value': 101
            },
            {
                'documentation': {
                    'description': 'Shifts high or low while the event is active, depending  on the active state you specify.'
                },
                'name': 'NIFGEN_VAL_LEVEL',
                'value': 102
            }
        ]
    },
    'DoneEventPulsePolarity': {
        'values': [
            {
                'documentation': {
                    'description': 'When the operation is ready to start, the Ready for Start  event level is high.'
                },
                'name': 'NIFGEN_VAL_ACTIVE_HIGH',
                'value': 101
            },
            {
                'documentation': {
                    'description': 'When the operation is ready to start, the Ready for Start  event level is low.'
                },
                'name': 'NIFGEN_VAL_ACTIVE_LOW',
                'value': 102
            }
        ]
    },
    'DoneEventPulseWidthUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies the pulse width in Sample clock periods.'
                },
                'name': 'NIFGEN_VAL_SAMPLE_CLOCK_PERIODS',
                'value': 101
            },
            {
                'documentation': {
                    'description': 'Specifies the pulse width in seconds.'
                },
                'name': 'NIFGEN_VAL_SECONDS',
                'value': 102
            }
        ]
    },
    'FilterType': {
        'values': [
            {
                'documentation': {
                    'description': 'Applies a flat filter to the data with the passband value specified  in the NIFGEN_ATTR_OSP_FIR_FILTER_FLAT_PASSBAND attribute.'
                },
                'name': 'NIFGEN_VAL_OSP_FLAT',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Applies a raised cosine filter to the data with the alpha value  specified in the NIFGEN_ATTR_OSP_FIR_FILTER_RAISED_COSINE_ALPHA attribute.'
                },
                'name': 'NIFGEN_VAL_OSP_RAISED_COSINE',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Applies a root raised cosine filter to the data with the alpha value  specified in the NIFGEN_ATTR_OSP_FIR_FILTER_ROOT_RAISED_COSINE_ALPHA attribute.'
                },
                'name': 'NIFGEN_VAL_OSP_ROOT_RAISED_COSINE',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Applies a Gaussian filter to the data with the BT value specified in the  NIFGEN_ATTR_OSP_FIR_FILTER_GAUSSIAN_BT attribute.'
                },
                'name': 'NIFGEN_VAL_OSP_GAUSSIAN',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'Applies a custom filter to the data. If NIFGEN_VAL_OSP_CUSTOM is selected,  you must provide a set of FIR filter coefficients with the  niFgen_ConfigureCustomFIRFilterCoefficients function.'
                },
                'name': 'NIFGEN_VAL_OSP_CUSTOM',
                'value': 4
            }
        ]
    },
    'FrequencyListHandle': {
        'values': [
            {
                'name': 'NIFGEN_VAL_FIRST_FREQ_LIST_HANDLE',
                'value': 200000
            },
            {
                'name': 'NIFGEN_VAL_LAST_FREQ_LIST_HANDLE',
                'value': 209999
            },
            {
                'name': 'NIFGEN_VAL_NO_FREQ_LIST',
                'value': -1
            }
        ]
    },
    'FrequencyListOptions': {
        'values': [
            {
                'name': 'NIFGEN_VAL_ALL_FLISTS',
                'value': -1
            }
        ]
    },
    'HardwareState': {
        'values': [
            {
                'name': 'NIFGEN_VAL_IDLE',
                'value': 0
            },
            {
                'name': 'NIFGEN_VAL_WAITING_FOR_START_TRIGGER',
                'value': 100
            },
            {
                'name': 'NIFGEN_VAL_RUNNING',
                'value': 200
            },
            {
                'name': 'NIFGEN_VAL_DONE',
                'value': 600
            },
            {
                'name': 'NIFGEN_VAL_HARDWARE_ERROR',
                'value': 1000
            }
        ]
    },
    'IdleBehavior': {
        'values': [
            {
                'documentation': {
                    'description': 'While in an Idle or Wait state, the output signal remains  at the last voltage generated prior to entering the state.'
                },
                'name': 'NIFGEN_VAL_HOLD_LAST_VALUE',
                'value': 400
            },
            {
                'documentation': {
                    'description': 'While in an Idle or Wait state, the output signal remains  at the value configured in the Idle or Wait value attribute.'
                },
                'name': 'NIFGEN_VAL_JUMP_TO_VALUE',
                'value': 401
            }
        ]
    },
    'LoadImpedance': {
        'values': [
            {
                'name': 'NIFGEN_VAL_MATCHED_LOAD_IMPEDANCE',
                'value': -1.0
            }
        ]
    },
    'MarkerEventDelayUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies the pulse width in Sample clock periods.'
                },
                'name': 'NIFGEN_VAL_SAMPLE_CLOCK_PERIODS',
                'value': 101
            },
            {
                'documentation': {
                    'description': 'Specifies the pulse width in seconds.'
                },
                'name': 'NIFGEN_VAL_SECONDS',
                'value': 102
            }
        ]
    },
    'MarkerEventOutputBehavior': {
        'values': [
            {
                'documentation': {
                    'description': 'Triggers a pulse for a specified period of time.'
                },
                'name': 'NIFGEN_VAL_PULSE',
                'value': 101
            },
            {
                'documentation': {
                    'description': 'Shifts high or low while the event is active, depending  on the active state you specify.'
                },
                'name': 'NIFGEN_VAL_LEVEL',
                'value': 102
            },
            {
                'documentation': {
                    'description': '\nChanges to high or low while the event is active, depending on the\nactive state you specify.\n'
                },
                'name': 'NIFGEN_VAL_TOGGLE',
                'value': 103
            }
        ]
    },
    'MarkerEventPulsePolarity': {
        'values': [
            {
                'documentation': {
                    'description': 'When the operation is ready to start, the Ready for Start  event level is high.'
                },
                'name': 'NIFGEN_VAL_ACTIVE_HIGH',
                'value': 101
            },
            {
                'documentation': {
                    'description': 'When the operation is ready to start, the Ready for Start  event level is low.'
                },
                'name': 'NIFGEN_VAL_ACTIVE_LOW',
                'value': 102
            }
        ]
    },
    'MarkerEventPulseWidthUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies the pulse width in Sample clock periods.'
                },
                'name': 'NIFGEN_VAL_SAMPLE_CLOCK_PERIODS',
                'value': 101
            },
            {
                'documentation': {
                    'description': 'Specifies the pulse width in seconds.'
                },
                'name': 'NIFGEN_VAL_SECONDS',
                'value': 102
            }
        ]
    },
    'MarkerEventToggleInitialState': {
        'values': [
            {
                'documentation': {
                    'description': 'Sets the initial state of the Marker event to high.'
                },
                'name': 'NIFGEN_VAL_HIGH',
                'value': 101
            },
            {
                'documentation': {
                    'description': 'Sets the initial state of the Marker event to low.'
                },
                'name': 'NIFGEN_VAL_LOW',
                'value': 102
            }
        ]
    },
    'OperationMode': {
        'values': [
            {
                'documentation': {
                    'description': 'Continuous Operation'
                },
                'name': 'NIFGEN_VAL_OPERATE_CONTINUOUS',
                'value': 0
            }
        ]
    },
    'OspMode': {
        'values': [
            {
                'documentation': {
                    'description': 'The OSP block generates intermediate frequency (IF) data.'
                },
                'name': 'NIFGEN_VAL_OSP_IF',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'The OSP block generates baseband data.'
                },
                'name': 'NIFGEN_VAL_OSP_BASEBAND',
                'value': 1
            }
        ]
    },
    'OspOverflowErrorReporting': {
        'values': [
            {
                'documentation': {
                    'description': 'NI-FGEN returns errors whenever an overflow has occurred in the OSP block.'
                },
                'name': 'NIFGEN_VAL_ERROR_REPORTING_ERROR',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'NI-FGEN does not return errors when an overflow occurs in the OSP block.'
                },
                'name': 'NIFGEN_VAL_ERROR_REPORTING_DISABLED',
                'value': 2
            }
        ]
    },
    'OspOverflowStatus': {
        'values': [
            {
                'name': 'NIFGEN_VAL_OSP_OVERFLOW_NONE',
                'value': 0
            },
            {
                'name': 'NIFGEN_VAL_OSP_OVERFLOW_PRE_FILTER_GAIN_I',
                'value': 1
            },
            {
                'name': 'NIFGEN_VAL_OSP_OVERFLOW_PRE_FILTER_GAIN_Q',
                'value': 2
            },
            {
                'name': 'NIFGEN_VAL_OSP_OVERFLOW_PRE_FILTER_OFFSET_I',
                'value': 4
            },
            {
                'name': 'NIFGEN_VAL_OSP_OVERFLOW_PRE_FILTER_OFFSET_Q',
                'value': 8
            },
            {
                'name': 'NIFGEN_VAL_OSP_OVERFLOW_FIR_FILTER_I',
                'value': 16
            },
            {
                'name': 'NIFGEN_VAL_OSP_OVERFLOW_PFIR_FILTER_I',
                'value': 16
            },
            {
                'name': 'NIFGEN_VAL_OSP_OVERFLOW_FIR_FILTER_Q',
                'value': 32
            },
            {
                'name': 'NIFGEN_VAL_OSP_OVERFLOW_PFIR_FILTER_Q',
                'value': 32
            },
            {
                'name': 'NIFGEN_VAL_OSP_OVERFLOW_CIC_FILTER_I',
                'value': 64
            },
            {
                'name': 'NIFGEN_VAL_OSP_OVERFLOW_CIC_FILTER_Q',
                'value': 128
            },
            {
                'name': 'NIFGEN_VAL_OSP_OVERFLOW_COMPLEX_DATA',
                'value': 256
            },
            {
                'name': 'NIFGEN_VAL_OSP_OVERFLOW_CFIR_FILTER_I',
                'value': 512
            },
            {
                'name': 'NIFGEN_VAL_OSP_OVERFLOW_CFIR_FILTER_Q',
                'value': 1024
            },
            {
                'name': 'NIFGEN_VAL_OSP_OVERFLOW_EQUALIZER',
                'value': 2048
            }
        ]
    },
    'OutputImpedance': {
        'values': [
            {
                'name': 'NIFGEN_VAL_50_OHMS',
                'value': 50.0
            },
            {
                'name': 'NIFGEN_VAL_75_OHMS',
                'value': 75.0
            }
        ]
    },
    'OutputMode': {
        'values': [
            {
                'documentation': {
                    'description': 'Standard Function mode—  Generates standard function waveforms  such as sine, square, triangle, and so on.'
                },
                'name': 'NIFGEN_VAL_OUTPUT_FUNC',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Arbitrary waveform mode—Generates  waveforms from user-created/provided  waveform arrays of numeric data.'
                },
                'name': 'NIFGEN_VAL_OUTPUT_ARB',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Arbitrary sequence mode —  Generates downloaded waveforms  in an order your specify.'
                },
                'name': 'NIFGEN_VAL_OUTPUT_SEQ',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Frequency List mode—Generates a  standard function using a list of  frequencies you define.'
                },
                'name': 'NIFGEN_VAL_OUTPUT_FREQ_LIST',
                'value': 101
            },
            {
                'documentation': {
                    'description': '\n**Script mode—**\\ Allows you to use scripting to link and loop multiple\nwaveforms in complex combinations.\n'
                },
                'name': 'NIFGEN_VAL_OUTPUT_SCRIPT',
                'value': 102
            }
        ]
    },
    'P2PAddressType': {
        'values': [
            {
                'documentation': {
                    'description': 'Physical'
                },
                'name': 'NIFGEN_VAL_ADDR_PHYSICAL',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Physical'
                },
                'name': 'NIFGEN_VAL_ADDR_VIRTUAL',
                'value': 1
            }
        ]
    },
    'ReadyForStartEventActiveLevel': {
        'values': [
            {
                'documentation': {
                    'description': 'When the operation is ready to start, the Ready for Start  event level is high.'
                },
                'name': 'NIFGEN_VAL_ACTIVE_HIGH',
                'value': 101
            },
            {
                'documentation': {
                    'description': 'When the operation is ready to start, the Ready for Start  event level is low.'
                },
                'name': 'NIFGEN_VAL_ACTIVE_LOW',
                'value': 102
            }
        ]
    },
    'ReferenceClockSource': {
        'values': [
            {
                'documentation': {
                    'description': '\nSpecifies that the CLK IN input signal from the front panel connector is\nused as the Reference Clock source.\n'
                },
                'name': 'NIFGEN_VAL_CLOCK_IN_COLLISION_AVOIDANCE',
                'python_name': 'CLOCK_IN',
                'value': 'ClkIn'
            },
            {
                'documentation': {
                    'description': 'Specifies that a Reference Clock is not used.'
                },
                'name': 'NIFGEN_VAL_NONE_COLLISION_AVOIDANCE',
                'python_name': 'NONE',
                'value': 'None'
            },
            {
                'documentation': {
                    'description': '\nSpecifies that the onboard Reference Clock is used as the Reference\nClock source.\n'
                },
                'name': 'NIFGEN_VAL_ONBOARD_REFERENCE_CLOCK_COLLISION_AVOIDANCE',
                'python_name': 'ONBOARD_REFERENCE_CLOCK',
                'value': 'OnboardRefClk'
            },
            {
                'documentation': {
                    'description': 'Specifies the PXI Clock is used as the Reference Clock source.'
                },
                'name': 'NIFGEN_VAL_PXI_CLOCK_COLLISION_AVOIDANCE',
                'python_name': 'PXI_CLOCK',
                'value': 'PXI_Clk'
            },
            {
                'documentation': {
                    'description': 'Specifies that the RTSI line 7 is used as the Reference Clock source.'
                },
                'name': 'NIFGEN_VAL_RTSI_7_COLLISION_AVOIDANCE',
                'python_name': 'RTSI_7',
                'value': 'RTSI7'
            }
        ]
    },
    'RelativeTo': {
        'values': [
            {
                'name': 'NIFGEN_VAL_WAVEFORM_POSITION_START',
                'value': 0
            },
            {
                'name': 'NIFGEN_VAL_WAVEFORM_POSITION_CURRENT',
                'value': 1
            }
        ]
    },
    'RouteSignalFrom': {
        'values': [
            {
                'name': 'NIFGEN_VAL_MARKER',
                'value': 1001
            },
            {
                'name': 'NIFGEN_VAL_SYNC_OUT',
                'value': 1002
            },
            {
                'name': 'NIFGEN_VAL_OUT_START_TRIGGER',
                'value': 1004
            },
            {
                'name': 'NIFGEN_VAL_BOARD_CLOCK',
                'value': 1006
            },
            {
                'name': 'NIFGEN_VAL_SYNCHRONIZATION',
                'value': 1007
            },
            {
                'name': 'NIFGEN_VAL_SOFTWARE_TRIG',
                'value': 2
            },
            {
                'name': 'NIFGEN_VAL_REF_OUT',
                'value': 1008
            },
            {
                'name': 'NIFGEN_VAL_CLOCK_OUT',
                'value': 1009
            },
            {
                'name': 'NIFGEN_VAL_PXI_STAR',
                'value': 131
            },
            {
                'name': 'NIFGEN_VAL_PFI_0',
                'value': 1011
            },
            {
                'name': 'NIFGEN_VAL_RTSI_0',
                'value': 141
            },
            {
                'name': 'NIFGEN_VAL_RTSI_1',
                'value': 142
            },
            {
                'name': 'NIFGEN_VAL_RTSI_2',
                'value': 143
            },
            {
                'name': 'NIFGEN_VAL_RTSI_3',
                'value': 144
            },
            {
                'name': 'NIFGEN_VAL_RTSI_4',
                'value': 145
            },
            {
                'name': 'NIFGEN_VAL_RTSI_5',
                'value': 146
            },
            {
                'name': 'NIFGEN_VAL_RTSI_6',
                'value': 147
            },
            {
                'name': 'NIFGEN_VAL_RTSI_7',
                'value': 1010
            },
            {
                'name': 'NIFGEN_VAL_ONBOARD_REFERENCE_CLOCK',
                'value': 1019
            }
        ]
    },
    'RouteSignalTo': {
        'values': [
            {
                'name': 'NIFGEN_VAL_RTSI_0',
                'value': 141
            },
            {
                'name': 'NIFGEN_VAL_RTSI_1',
                'value': 142
            },
            {
                'name': 'NIFGEN_VAL_RTSI_2',
                'value': 143
            },
            {
                'name': 'NIFGEN_VAL_RTSI_3',
                'value': 144
            },
            {
                'name': 'NIFGEN_VAL_RTSI_4',
                'value': 145
            },
            {
                'name': 'NIFGEN_VAL_RTSI_5',
                'value': 146
            },
            {
                'name': 'NIFGEN_VAL_RTSI_6',
                'value': 147
            },
            {
                'name': 'NIFGEN_VAL_RTSI_7',
                'value': 1010
            },
            {
                'name': 'NIFGEN_VAL_REF_OUT',
                'value': 1008
            },
            {
                'name': 'NIFGEN_VAL_PFI_0',
                'value': 1011
            },
            {
                'name': 'NIFGEN_VAL_PFI_1',
                'value': 1012
            },
            {
                'name': 'NIFGEN_VAL_PXI_STAR',
                'value': 131
            }
        ]
    },
    'SampleClockSource': {
        'values': [
            {
                'documentation': {
                    'description': '\nSpecifies that the signal at the CLK IN front panel connector is used as\nthe Sample Clock source.\n'
                },
                'name': 'NIFGEN_VAL_CLOCK_IN',
                'value': 'ClkIn'
            },
            {
                'documentation': {
                    'description': '\nSpecifies that the Sample Clock from DDC connector is used as the Sample\nClock source.\n'
                },
                'name': 'NIFGEN_VAL_DDC_CLOCK_IN',
                'value': 'DDC_ClkIn'
            },
            {
                'documentation': {
                    'description': 'Specifies that the onboard clock is used as the Sample Clock source.'
                },
                'name': 'NIFGEN_VAL_ONBOARD_CLOCK',
                'value': 'OnboardClock'
            },
            {
                'documentation': {
                    'description': '\nSpecifies that the PXI\\_STAR trigger line is used as the Sample Clock\nsource.\n'
                },
                'name': 'NIFGEN_VAL_PXI_STAR_LINE',
                'value': 'PXI_Star'
            },
            {
                'documentation': {
                    'description': '\nSpecifies that the PXI or RTSI line 0 is used as the Sample Clock\nsource.\n'
                },
                'name': 'NIFGEN_VAL_PXI_TRIGGER_LINE_0_RTSI_0',
                'value': 'PXI_Trig0'
            },
            {
                'documentation': {
                    'description': '\nSpecifies that the PXI or RTSI line 1 is used as the Sample Clock\nsource.\n'
                },
                'name': 'NIFGEN_VAL_PXI_TRIGGER_LINE_1_RTSI_1',
                'value': 'PXI_Trig1'
            },
            {
                'documentation': {
                    'description': '\nSpecifies that the PXI or RTSI line 2 is used as the Sample Clock\nsource.\n'
                },
                'name': 'NIFGEN_VAL_PXI_TRIGGER_LINE_2_RTSI_2',
                'value': 'PXI_Trig2'
            },
            {
                'documentation': {
                    'description': '\nSpecifies that the PXI or RTSI line 3 is used as the Sample Clock\nsource.\n'
                },
                'name': 'NIFGEN_VAL_PXI_TRIGGER_LINE_3_RTSI_3',
                'value': 'PXI_Trig3'
            },
            {
                'documentation': {
                    'description': '\nSpecifies that the PXI or RTSI line 4 is used as the Sample Clock\nsource.\n'
                },
                'name': 'NIFGEN_VAL_PXI_TRIGGER_LINE_4_RTSI_4',
                'value': 'PXI_Trig4'
            },
            {
                'documentation': {
                    'description': '\nSpecifies that the PXI or RTSI line 5 is used as the Sample Clock\nsource.\n'
                },
                'name': 'NIFGEN_VAL_PXI_TRIGGER_LINE_5_RTSI_5',
                'value': 'PXI_Trig5'
            },
            {
                'documentation': {
                    'description': '\nSpecifies that the PXI or RTSI line 6 is used as the Sample Clock\nsource.\n'
                },
                'name': 'NIFGEN_VAL_PXI_TRIGGER_LINE_6_RTSI_6',
                'value': 'PXI_Trig6'
            },
            {
                'documentation': {
                    'description': '\nSpecifies that the PXI or RTSI line 7 is used as the Sample Clock\nsource.\n'
                },
                'name': 'NIFGEN_VAL_PXI_TRIGGER_LINE_7_RTSI_7',
                'value': 'PXI_Trig7'
            }
        ]
    },
    'SampleClockTimebaseSource': {
        'values': [
            {
                'documentation': {
                    'description': '\nSpecifies that the external signal on the CLK IN front panel connector\nis used as the source.\n'
                },
                'name': 'NIFGEN_VAL_CLOCK_IN',
                'value': 'ClkIn'
            },
            {
                'documentation': {
                    'description': 'Specifies that the onboard Sample Clock timebase is used as the source.'
                },
                'name': 'NIFGEN_VAL_ONBOARD_CLOCK',
                'value': 'OnboardClock'
            }
        ]
    },
    'SampleRate': {
        'values': [
            {
                'name': 'NIFGEN_VAL_EXTERNAL_SAMPLE_RATE',
                'value': -1.0
            }
        ]
    },
    'ScriptTriggerDigitalEdgeEdge': {
        'values': [
            {
                'documentation': {
                    'description': 'Rising Edge'
                },
                'name': 'NIFGEN_VAL_RISING_EDGE',
                'value': 101
            },
            {
                'documentation': {
                    'description': 'Falling Edge'
                },
                'name': 'NIFGEN_VAL_FALLING_EDGE',
                'value': 102
            }
        ]
    },
    'ScriptTriggerDigitalLevelActiveLevel': {
        'values': [
            {
                'documentation': {
                    'description': 'High Level'
                },
                'name': 'NIFGEN_VAL_ACTIVE_HIGH',
                'value': 101
            },
            {
                'documentation': {
                    'description': 'Low Level'
                },
                'name': 'NIFGEN_VAL_ACTIVE_LOW',
                'value': 102
            }
        ]
    },
    'ScriptTriggerType': {
        'values': [
            {
                'documentation': {
                    'description': 'No trigger is configured. Signal generation starts immediately.'
                },
                'name': 'NIFGEN_VAL_TRIG_NONE',
                'value': 101
            },
            {
                'documentation': {
                    'description': 'Trigger is asserted when a digital edge is detected.'
                },
                'name': 'NIFGEN_VAL_DIGITAL_EDGE',
                'value': 102
            },
            {
                'documentation': {
                    'description': 'Trigger is asserted when a digital level is detected.'
                },
                'name': 'NIFGEN_VAL_DIGITAL_LEVEL',
                'value': 103
            },
            {
                'documentation': {
                    'description': 'Trigger is asserted when a software edge is detected.'
                },
                'name': 'NIFGEN_VAL_SOFTWARE_EDGE',
                'value': 104
            }
        ]
    },
    'SequenceHandle': {
        'values': [
            {
                'name': 'NIFGEN_VAL_ALL_SEQUENCES',
                'value': -1
            }
        ]
    },
    'Signal': {
        'values': [
            {
                'name': 'NIFGEN_VAL_ONBOARD_REFERENCE_CLOCK',
                'value': 1019
            },
            {
                'name': 'NIFGEN_VAL_SYNC_OUT',
                'value': 1002
            },
            {
                'name': 'NIFGEN_VAL_START_TRIGGER',
                'value': 1004
            },
            {
                'name': 'NIFGEN_VAL_MARKER_EVENT',
                'value': 1001
            },
            {
                'name': 'NIFGEN_VAL_SAMPLE_CLOCK_TIMEBASE',
                'value': 1006
            },
            {
                'name': 'NIFGEN_VAL_SYNCHRONIZATION',
                'value': 1007
            },
            {
                'name': 'NIFGEN_VAL_SAMPLE_CLOCK',
                'value': 101
            },
            {
                'name': 'NIFGEN_VAL_REFERENCE_CLOCK',
                'value': 102
            },
            {
                'name': 'NIFGEN_VAL_SCRIPT_TRIGGER',
                'value': 103
            },
            {
                'name': 'NIFGEN_VAL_READY_FOR_START_EVENT',
                'value': 105
            },
            {
                'name': 'NIFGEN_VAL_STARTED_EVENT',
                'value': 106
            },
            {
                'name': 'NIFGEN_VAL_DONE_EVENT',
                'value': 107
            },
            {
                'name': 'NIFGEN_VAL_DATA_MARKER_EVENT',
                'value': 108
            }
        ]
    },
    'StartTriggerDigitalEdgeEdge': {
        'values': [
            {
                'documentation': {
                    'description': 'Rising Edge'
                },
                'name': 'NIFGEN_VAL_RISING_EDGE',
                'value': 101
            },
            {
                'documentation': {
                    'description': 'Falling Edge'
                },
                'name': 'NIFGEN_VAL_FALLING_EDGE',
                'value': 102
            }
        ]
    },
    'StartTriggerType': {
        'values': [
            {
                'documentation': {
                    'description': 'None'
                },
                'name': 'NIFGEN_VAL_TRIG_NONE',
                'value': 101
            },
            {
                'documentation': {
                    'description': 'Digital Edge'
                },
                'name': 'NIFGEN_VAL_DIGITAL_EDGE',
                'value': 102
            },
            {
                'documentation': {
                    'description': 'Software Edge'
                },
                'name': 'NIFGEN_VAL_SOFTWARE_EDGE',
                'value': 104
            },
            {
                'documentation': {
                    'description': 'P2P Endpoint Fullness'
                },
                'name': 'NIFGEN_VAL_P2P_ENDPOINT_FULLNESS',
                'value': 106
            }
        ]
    },
    'StartedEventActiveLevel': {
        'values': [
            {
                'documentation': {
                    'description': 'When the operation is ready to start, the Ready for Start  event level is high.'
                },
                'name': 'NIFGEN_VAL_ACTIVE_HIGH',
                'value': 101
            },
            {
                'documentation': {
                    'description': 'When the operation is ready to start, the Ready for Start  event level is low.'
                },
                'name': 'NIFGEN_VAL_ACTIVE_LOW',
                'value': 102
            }
        ]
    },
    'StartedEventDelayUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies the pulse width in Sample clock periods.'
                },
                'name': 'NIFGEN_VAL_SAMPLE_CLOCK_PERIODS',
                'value': 101
            },
            {
                'documentation': {
                    'description': 'Specifies the pulse width in seconds.'
                },
                'name': 'NIFGEN_VAL_SECONDS',
                'value': 102
            }
        ]
    },
    'StartedEventOutputBehavior': {
        'values': [
            {
                'documentation': {
                    'description': 'Triggers a pulse for a specified period of time.'
                },
                'name': 'NIFGEN_VAL_PULSE',
                'value': 101
            },
            {
                'documentation': {
                    'description': 'Shifts high or low while the event is active, depending  on the active state you specify.'
                },
                'name': 'NIFGEN_VAL_LEVEL',
                'value': 102
            }
        ]
    },
    'StartedEventPulsePolarity': {
        'values': [
            {
                'documentation': {
                    'description': 'When the operation is ready to start, the Ready for Start  event level is high.'
                },
                'name': 'NIFGEN_VAL_ACTIVE_HIGH',
                'value': 101
            },
            {
                'documentation': {
                    'description': 'When the operation is ready to start, the Ready for Start  event level is low.'
                },
                'name': 'NIFGEN_VAL_ACTIVE_LOW',
                'value': 102
            }
        ]
    },
    'StartedEventPulseWidthUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies the pulse width in Sample clock periods.'
                },
                'name': 'NIFGEN_VAL_SAMPLE_CLOCK_PERIODS',
                'value': 101
            },
            {
                'documentation': {
                    'description': 'Specifies the pulse width in seconds.'
                },
                'name': 'NIFGEN_VAL_SECONDS',
                'value': 102
            }
        ]
    },
    'SynchronizationSource': {
        'values': [
            {
                'documentation': {
                    'description': 'PXI TRIG0 or VXI TTL0'
                },
                'name': 'NIFGEN_VAL_TTL0',
                'value': 111
            },
            {
                'documentation': {
                    'description': 'PXI TRIG1 or VXI TTL1'
                },
                'name': 'NIFGEN_VAL_TTL1',
                'value': 112
            },
            {
                'documentation': {
                    'description': 'PXI TRIG2 or VXI TTL2'
                },
                'name': 'NIFGEN_VAL_TTL2',
                'value': 113
            },
            {
                'documentation': {
                    'description': 'PXI TRIG3 or VXI TTL3'
                },
                'name': 'NIFGEN_VAL_TTL3',
                'value': 114
            },
            {
                'documentation': {
                    'description': 'PXI TRIG4 or VXI TTL4'
                },
                'name': 'NIFGEN_VAL_TTL4',
                'value': 115
            },
            {
                'documentation': {
                    'description': 'PXI TRIG5 or VXI TTL5'
                },
                'name': 'NIFGEN_VAL_TTL5',
                'value': 116
            },
            {
                'documentation': {
                    'description': 'PXI TRIG6 or VXI TTL6'
                },
                'name': 'NIFGEN_VAL_TTL6',
                'value': 117
            },
            {
                'documentation': {
                    'description': 'RTSI 0'
                },
                'name': 'NIFGEN_VAL_RTSI_0',
                'value': 141
            },
            {
                'documentation': {
                    'description': 'RTSI 1'
                },
                'name': 'NIFGEN_VAL_RTSI_1',
                'value': 142
            },
            {
                'documentation': {
                    'description': 'RTSI 2'
                },
                'name': 'NIFGEN_VAL_RTSI_2',
                'value': 143
            },
            {
                'documentation': {
                    'description': 'RTSI 3'
                },
                'name': 'NIFGEN_VAL_RTSI_3',
                'value': 144
            },
            {
                'documentation': {
                    'description': 'RTSI 4'
                },
                'name': 'NIFGEN_VAL_RTSI_4',
                'value': 145
            },
            {
                'documentation': {
                    'description': 'RTSI 5'
                },
                'name': 'NIFGEN_VAL_RTSI_5',
                'value': 146
            },
            {
                'documentation': {
                    'description': 'RTSI 6'
                },
                'name': 'NIFGEN_VAL_RTSI_6',
                'value': 147
            },
            {
                'documentation': {
                    'description': 'No Synchronization Source'
                },
                'name': 'NIFGEN_VAL_NONE',
                'value': 1000
            }
        ]
    },
    'TerminalConfiguration': {
        'values': [
            {
                'documentation': {
                    'description': 'Single-ended operation'
                },
                'name': 'NIFGEN_VAL_SINGLE_ENDED',
                'value': 300
            },
            {
                'documentation': {
                    'description': 'Differential operation'
                },
                'name': 'NIFGEN_VAL_DIFFERENTIAL',
                'value': 301
            }
        ]
    },
    'Trigger': {
        'values': [
            {
                'name': 'NIFGEN_VAL_START_TRIGGER',
                'value': 1004
            },
            {
                'name': 'NIFGEN_VAL_SCRIPT_TRIGGER',
                'value': 103
            }
        ]
    },
    'TriggerMode': {
        'values': [
            {
                'documentation': {
                    'description': 'Single Trigger Mode - The waveform you describe in the sequence list is  generated only once by going through the entire staging list. Only one  trigger is required to start the waveform generation. You can use Single  trigger mode with the output mode in any mode. After a trigger is  received, the waveform generation starts from the first stage and  continues through to the last stage. Then, the last stage generates  repeatedly until you stop the waveform generation.'
                },
                'name': 'NIFGEN_VAL_SINGLE',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Continuous Trigger Mode - The waveform you describe in the staging list generates infinitely by repeatedly cycling through the staging list.  After a trigger is received, the waveform generation starts from the  first stage and continues through to the last stage. After the last stage  completes, the waveform generation loops back to the start of the  first stage and continues until it is stopped. Only one trigger is  required to start the waveform generation.'
                },
                'name': 'NIFGEN_VAL_CONTINUOUS',
                'value': 2
            },
            {
                'documentation': {
                    'description': '\nStepped Trigger Mode - After a start trigger is received, the waveform  described by the first stage generates. Then, the device waits for the  next trigger signal. On the next trigger, the waveform described by the  second stage generates, and so on. After the staging list completes,  the waveform generation returns to the first stage and continues in a  cyclic fashion. After any stage has generated completely, the first  eight samples of the next stage are repeated continuously until the next  trigger is received.\ntrigger mode.\n',
                    'note': 'In Frequency List mode, Stepped trigger mode is the same as Burst'
                },
                'name': 'NIFGEN_VAL_STEPPED',
                'value': 3
            },
            {
                'documentation': {
                    'description': '\nBurst Trigger Mode - After a start trigger is received, the waveform  described by the first stage generates until another trigger is  received. At the next trigger, the buffer of the previous stage completes, and then the waveform described by the second stage generates. After the staging list completes, the waveform generation  returns to the first stage and continues in a cyclic fashion. In  Frequency List mode, the duration instruction is ignored, and the trigger  switches the frequency to the next frequency in the list.\ntrigger mode.\n',
                    'note': 'In Frequency List mode, Stepped trigger mode is the same as Burst'
                },
                'name': 'NIFGEN_VAL_BURST',
                'value': 4
            }
        ]
    },
    'TriggerSource': {
        'values': [
            {
                'documentation': {
                    'description': 'Immediate-The signal generator does not wait for a trigger of any kind.'
                },
                'name': 'NIFGEN_VAL_IMMEDIATE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'External-The signal generator waits for a trigger on the external trigger input'
                },
                'name': 'NIFGEN_VAL_EXTERNAL',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Software Trigger-The signal generator waits until you call niFgen_SendSWTrigger.'
                },
                'name': 'NIFGEN_VAL_SOFTWARE_TRIG',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'PXI TRIG0 or VXI TTL0'
                },
                'name': 'NIFGEN_VAL_TTL0',
                'value': 111
            },
            {
                'documentation': {
                    'description': 'PXI TRIG1 or VXI TTL1'
                },
                'name': 'NIFGEN_VAL_TTL1',
                'value': 112
            },
            {
                'documentation': {
                    'description': 'PXI TRIG2 or VXI TTL2'
                },
                'name': 'NIFGEN_VAL_TTL2',
                'value': 113
            },
            {
                'documentation': {
                    'description': 'PXI TRIG3 or VXI TTL3'
                },
                'name': 'NIFGEN_VAL_TTL3',
                'value': 114
            },
            {
                'documentation': {
                    'description': 'PXI TRIG4 or VXI TTL4'
                },
                'name': 'NIFGEN_VAL_TTL4',
                'value': 115
            },
            {
                'documentation': {
                    'description': 'PXI TRIG5 or VXI TTL5'
                },
                'name': 'NIFGEN_VAL_TTL5',
                'value': 116
            },
            {
                'documentation': {
                    'description': 'PXI TRIG6 or VXI TTL6'
                },
                'name': 'NIFGEN_VAL_TTL6',
                'value': 117
            },
            {
                'documentation': {
                    'description': 'PXI star'
                },
                'name': 'NIFGEN_VAL_PXI_STAR',
                'value': 131
            },
            {
                'documentation': {
                    'description': 'RTSI line 0'
                },
                'name': 'NIFGEN_VAL_RTSI_0',
                'value': 141
            },
            {
                'documentation': {
                    'description': 'RTSI line 1'
                },
                'name': 'NIFGEN_VAL_RTSI_1',
                'value': 142
            },
            {
                'documentation': {
                    'description': 'RTSI line 2'
                },
                'name': 'NIFGEN_VAL_RTSI_2',
                'value': 143
            },
            {
                'documentation': {
                    'description': 'RTSI line 3'
                },
                'name': 'NIFGEN_VAL_RTSI_3',
                'value': 144
            },
            {
                'documentation': {
                    'description': 'RTSI line 4'
                },
                'name': 'NIFGEN_VAL_RTSI_4',
                'value': 145
            },
            {
                'documentation': {
                    'description': 'RTSI line 5'
                },
                'name': 'NIFGEN_VAL_RTSI_5',
                'value': 146
            },
            {
                'documentation': {
                    'description': 'RTSI line 6'
                },
                'name': 'NIFGEN_VAL_RTSI_6',
                'value': 147
            },
            {
                'documentation': {
                    'description': 'RTSI line 7'
                },
                'name': 'NIFGEN_VAL_RTSI_7',
                'value': 1010
            },
            {
                'documentation': {
                    'description': 'PFI 0'
                },
                'name': 'NIFGEN_VAL_PFI_0',
                'value': 1011
            },
            {
                'documentation': {
                    'description': 'PFI 1'
                },
                'name': 'NIFGEN_VAL_PFI_1',
                'value': 1012
            },
            {
                'documentation': {
                    'description': 'PFI 2'
                },
                'name': 'NIFGEN_VAL_PFI_2',
                'value': 1013
            },
            {
                'documentation': {
                    'description': 'PFI 3'
                },
                'name': 'NIFGEN_VAL_PFI_3',
                'value': 1014
            },
            {
                'documentation': {
                    'description': 'Specifies that another terminal is used.'
                },
                'name': 'NIFGEN_VAL_OTHER_TERMINAL',
                'value': 1018
            }
        ]
    },
    'TriggerWhen': {
        'values': [
            {
                'name': 'NIFGEN_VAL_ACTIVE_HIGH',
                'value': 101
            },
            {
                'name': 'NIFGEN_VAL_ACTIVE_LOW',
                'value': 102
            }
        ]
    },
    'UpdateClockSource': {
        'values': [
            {
                'documentation': {
                    'description': 'Internal Update Clock'
                },
                'name': 'NIFGEN_VAL_INTERNAL',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'External update clock given on the IO front panel connector'
                },
                'name': 'NIFGEN_VAL_EXTERNAL',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'TTL1'
                },
                'name': 'NIFGEN_VAL_TTL1',
                'value': 112
            },
            {
                'documentation': {
                    'description': 'TTL2'
                },
                'name': 'NIFGEN_VAL_TTL2',
                'value': 113
            },
            {
                'documentation': {
                    'description': 'TTL3'
                },
                'name': 'NIFGEN_VAL_TTL3',
                'value': 114
            },
            {
                'documentation': {
                    'description': 'TTL4'
                },
                'name': 'NIFGEN_VAL_TTL4',
                'value': 115
            },
            {
                'documentation': {
                    'description': 'TTL5'
                },
                'name': 'NIFGEN_VAL_TTL5',
                'value': 116
            },
            {
                'documentation': {
                    'description': 'TTL6'
                },
                'name': 'NIFGEN_VAL_TTL6',
                'value': 117
            },
            {
                'documentation': {
                    'description': 'PXI Star Trigger Line'
                },
                'name': 'NIFGEN_VAL_PXI_STAR',
                'value': 131
            },
            {
                'documentation': {
                    'description': 'RTSI 0'
                },
                'name': 'NIFGEN_VAL_RTSI_0',
                'value': 141
            },
            {
                'documentation': {
                    'description': 'RTSI 1'
                },
                'name': 'NIFGEN_VAL_RTSI_1',
                'value': 142
            },
            {
                'documentation': {
                    'description': 'RTSI 2'
                },
                'name': 'NIFGEN_VAL_RTSI_2',
                'value': 143
            },
            {
                'documentation': {
                    'description': 'RTSI 3'
                },
                'name': 'NIFGEN_VAL_RTSI_3',
                'value': 144
            },
            {
                'documentation': {
                    'description': 'RTSI 4'
                },
                'name': 'NIFGEN_VAL_RTSI_4',
                'value': 145
            },
            {
                'documentation': {
                    'description': 'RTSI 5'
                },
                'name': 'NIFGEN_VAL_RTSI_5',
                'value': 146
            },
            {
                'documentation': {
                    'description': 'RTSI 6'
                },
                'name': 'NIFGEN_VAL_RTSI_6',
                'value': 147
            },
            {
                'documentation': {
                    'description': 'RTSI 7'
                },
                'name': 'NIFGEN_VAL_RTSI_7',
                'value': 1010
            },
            {
                'documentation': {
                    'description': 'Uses another device terminal.'
                },
                'name': 'NIFGEN_VAL_OTHER_TERMINAL',
                'value': 1018
            },
            {
                'documentation': {
                    'description': 'CLK IN front panel connector'
                },
                'name': 'NIFGEN_VAL_CLK_IN',
                'value': 1202
            },
            {
                'documentation': {
                    'description': 'DDC CLK IN line of the Digital Data & Control front panel connector'
                },
                'name': 'NIFGEN_VAL_DDC_CLK_IN',
                'value': 1203
            }
        ]
    },
    'VideoWaveformType': {
        'values': [
            {
                'documentation': {
                    'description': 'PAL B Video Type'
                },
                'name': 'NIFGEN_VAL_PAL_B',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'PAL D Video Type'
                },
                'name': 'NIFGEN_VAL_PAL_D',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'PAL G Video Type'
                },
                'name': 'NIFGEN_VAL_PAL_G',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'PAL H Video Type'
                },
                'name': 'NIFGEN_VAL_PAL_H',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'PAL I Video Type'
                },
                'name': 'NIFGEN_VAL_PAL_I',
                'value': 4
            },
            {
                'documentation': {
                    'description': 'PAL M Video Type'
                },
                'name': 'NIFGEN_VAL_PAL_M',
                'value': 5
            },
            {
                'documentation': {
                    'description': 'PAL N Video Type'
                },
                'name': 'NIFGEN_VAL_PAL_N',
                'value': 6
            },
            {
                'documentation': {
                    'description': 'NTSC M Video Type'
                },
                'name': 'NIFGEN_VAL_NTSC_M',
                'value': 7
            }
        ]
    },
    'WaitBehavior': {
        'values': [
            {
                'documentation': {
                    'description': 'While in an Idle or Wait state, the output signal remains  at the last voltage generated prior to entering the state.'
                },
                'name': 'NIFGEN_VAL_HOLD_LAST_VALUE',
                'value': 400
            },
            {
                'documentation': {
                    'description': 'While in an Idle or Wait state, the output signal remains  at the value configured in the Idle or Wait value attribute.'
                },
                'name': 'NIFGEN_VAL_JUMP_TO_VALUE',
                'value': 401
            }
        ]
    },
    'Waveform': {
        'values': [
            {
                'documentation': {
                    'description': 'Sinusoid waveform'
                },
                'name': 'NIFGEN_VAL_WFM_SINE',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Square waveform'
                },
                'name': 'NIFGEN_VAL_WFM_SQUARE',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Triange waveform'
                },
                'name': 'NIFGEN_VAL_WFM_TRIANGLE',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'Positive ramp waveform'
                },
                'name': 'NIFGEN_VAL_WFM_RAMP_UP',
                'value': 4
            },
            {
                'documentation': {
                    'description': 'Negative ramp waveform'
                },
                'name': 'NIFGEN_VAL_WFM_RAMP_DOWN',
                'value': 5
            },
            {
                'documentation': {
                    'description': 'Constant voltage'
                },
                'name': 'NIFGEN_VAL_WFM_DC',
                'value': 6
            },
            {
                'documentation': {
                    'description': 'White noise'
                },
                'name': 'NIFGEN_VAL_WFM_NOISE',
                'value': 101
            },
            {
                'documentation': {
                    'description': 'User-defined waveform as defined by the niFgen_DefineUserStandardWaveform function.'
                },
                'name': 'NIFGEN_VAL_WFM_USER',
                'value': 102
            }
        ]
    },
    'WaveformHandle': {
        'values': [
            {
                'name': 'NIFGEN_VAL_ALL_WAVEFORMS',
                'value': -1
            }
        ]
    }
}
