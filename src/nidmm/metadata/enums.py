
# -*- coding: utf-8 -*-
# This file is code generated, do not make changes here.
#  If the generated information is not correct for python
#  changes can be made in enums_addon.py and they will be
#  applied at build time.

enums = {
    'ADCCalibration': {
        'values': [
            {
                'name': 'NIDMM_VAL_ADC_CALIBRATION_AUTO',
                'value': -1,
'documentation': {
'description': 'The DMM enables or disables ADC calibration for you.',
},
            },
            {
                'name': 'NIDMM_VAL_ADC_CALIBRATION_OFF',
                'value': 0,
'documentation': {
'description': 'The DMM does not compensate for changes to the gain.',
},
            },
            {
                'name': 'NIDMM_VAL_ADC_CALIBRATION_ON',
                'value': 1,
'documentation': {
'description': 'The DMM measures an internal reference to calculate the correct gain for the  measurement.',
},
            },
        ],
    },
    'AcquisitionStatus': {
        'values': [
            {
                'name': 'RUNNING',
                'value': 0,
'documentation': {
'description': 'Running',
},
            },
            {
                'name': 'FINISHED_WITH_BACKLOG',
                'value': 1,
'documentation': {
'description': 'Finished with **Backlog**',
},
            },
            {
                'name': 'FINISHED_WITH_NO_BACKLOG',
                'value': 2,
'documentation': {
'description': 'Finished with no **Backlog**',
},
            },
            {
                'name': 'PAUSED',
                'value': 3,
'documentation': {
'description': 'Paused',
},
            },
            {
                'name': 'NO_ACQUISITION_IN_PROGRESS',
                'value': 4,
'documentation': {
'description': 'No acquisition in progress',
},
            },
        ],
    },
    'ApertureTimeUnits': {
        'values': [
            {
                'name': 'NIDMM_VAL_SECONDS',
                'value': 0,
'documentation': {
'description': 'Seconds',
},
            },
            {
                'name': 'NIDMM_VAL_POWER_LINE_CYCLES',
                'value': 1,
'documentation': {
'description': 'Powerline Cycles',
},
            },
        ],
    },
    'AutoZero': {
        'values': [
            {
                'name': 'NIDMM_VAL_AUTO_ZERO_AUTO',
                'value': -1,
'documentation': {
'description': 'The drivers chooses the AutoZero setting based on the configured function  and resolution.',
},
            },
            {
                'name': 'NIDMM_VAL_AUTO_ZERO_OFF',
                'value': 0,
'documentation': {
'description': 'Disables AutoZero.',
},
            },
            {
                'name': 'NIDMM_VAL_AUTO_ZERO_ON',
                'value': 1,
'documentation': {
'description': 'The DMM internally disconnects the input signal following each measurement  and takes a zero reading. It then subtracts the zero reading from the  preceding reading.',
},
            },
            {
                'name': 'NIDMM_VAL_AUTO_ZERO_ONCE',
                'value': 2,
'documentation': {
'description': 'The DMM internally disconnects the input signal for the first measurement  and takes a zero reading. It then subtracts the zero reading from the first  reading and the following readings.',
},
            },
        ],
    },
    'CableCompensationType': {
        'values': [
            {
                'name': 'NIDMM_VAL_CABLE_COMP_NONE',
                'value': 0,
'documentation': {
'description': 'No Cable Compensation',
},
            },
            {
                'name': 'NIDMM_VAL_CABLE_COMP_OPEN',
                'value': 1,
'documentation': {
'description': 'Open Cable Compensation',
},
            },
            {
                'name': 'NIDMM_VAL_CABLE_COMP_SHORT',
                'value': 2,
'documentation': {
'description': 'Short Cable Compensation',
},
            },
            {
                'name': 'NIDMM_VAL_CABLE_COMP_OPEN_AND_SHORT',
                'value': 3,
'documentation': {
'description': 'Open and Short Cable Compensation',
},
            },
        ],
    },
    'CurrentSource': {
        'values': [
            {
                'name': 'NIDMM_VAL_1_MICROAMP',
                'value': 1e-06,
'documentation': {
'description': 'NI 4070/4071/4072 are supported.',
},
            },
            {
                'name': 'NIDMM_VAL_10_MICROAMP',
                'value': 1e-05,
'documentation': {
'description': 'NI 4080/4081/4082 and NI 4070/4071/4072 are supported.',
},
            },
            {
                'name': 'NIDMM_VAL_100_MICROAMP',
                'value': 0.0001,
'documentation': {
'description': 'NI 4080/4081/4082, NI 4070/4071/4072, and NI 4065 are supported.',
},
            },
            {
                'name': 'NIDMM_VAL_1_MILLIAMP',
                'value': 0.001,
'documentation': {
'description': 'NI 4080/4081/4082, NI 4070/4071/4072, and NI 4065 are supported.',
},
            },
        ],
    },
    'DCBias': {
        'values': [
            {
                'name': 'NIDMM_VAL_DC_BIAS_OFF',
                'value': 0,
'documentation': {
'description': 'NI-DMM programs the device not to use the DC bias',
},
            },
            {
                'name': 'NIDMM_VAL_DC_BIAS_ON',
                'value': 1,
'documentation': {
'description': 'NI-DMM programs the device to use the DC bias',
},
            },
        ],
    },
    'DCNoiseRejection': {
        'values': [
            {
                'name': 'NIDMM_VAL_DCNR_AUTO',
                'value': -1,
'documentation': {
'description': 'The driver chooses the DC noise rejection setting based on the configured  function and resolution.',
},
            },
            {
                'name': 'NIDMM_VAL_DCNR_NORMAL',
                'value': 0,
'documentation': {
'description': 'NI-DMM weighs all samples equally.',
},
            },
            {
                'name': 'NIDMM_VAL_DCNR_SECOND_ORDER',
                'value': 1,
'documentation': {
'description': 'NI-DMM weighs the samples taken in the middle of the aperture time more than  samples taken at the beginning and the end of the measurement using a  triangular weighing function.',
},
            },
            {
                'name': 'NIDMM_VAL_DCNR_HIGH_ORDER',
                'value': 2,
'documentation': {
'description': 'NI-DMM weighs the samples taken in the middle of the aperture time more than  samples taken at the beginning and the end of the measurement using a  bell-curve weighing function.',
},
            },
        ],
    },
    'DigitsResolution': {
        'values': [
            {
                'name': '_3_5',
                'value': 3.5,
'documentation': {
'description': 'Specifies 3.5 digits resolution.',
},
            },
            {
                'name': '_4_5',
                'value': 4.5,
'documentation': {
'description': 'Specifies 4.5 digits resolution.',
},
            },
            {
                'name': '_5_5',
                'value': 5.5,
'documentation': {
'description': 'Specifies 5.5 digits resolution.',
},
            },
            {
                'name': '_6_5',
                'value': 6.5,
'documentation': {
'description': 'Specifies 6.5 digits resolution.',
},
            },
            {
                'name': '_7_5',
                'value': 7.5,
'documentation': {
'description': 'Specifies 7.5 digits resolution.',
},
            },
        ],
    },
    'Function': {
        'values': [
            {
                'name': 'NIDMM_VAL_DC_VOLTS',
                'value': 1,
'documentation': {
'description': 'DC Voltage',
},
            },
            {
                'name': 'NIDMM_VAL_AC_VOLTS',
                'value': 2,
'documentation': {
'description': 'AC Voltage',
},
            },
            {
                'name': 'NIDMM_VAL_DC_CURRENT',
                'value': 3,
'documentation': {
'description': 'DC Current',
},
            },
            {
                'name': 'NIDMM_VAL_AC_CURRENT',
                'value': 4,
'documentation': {
'description': 'AC Current',
},
            },
            {
                'name': 'NIDMM_VAL_2_WIRE_RES',
                'value': 5,
'documentation': {
'description': '2-Wire Resistance',
},
            },
            {
                'name': 'NIDMM_VAL_4_WIRE_RES',
                'value': 101,
'documentation': {
'description': '4-Wire Resistance',
},
            },
            {
                'name': 'NIDMM_VAL_FREQ',
                'value': 104,
'documentation': {
'description': 'Frequency',
},
            },
            {
                'name': 'NIDMM_VAL_PERIOD',
                'value': 105,
'documentation': {
'description': 'Period',
},
            },
            {
                'name': 'TEMPERATURE',
                'value': 108,
'documentation': {
'description': 'NI 4065, and NI 4070/4071/4072 supported.',
},
            },
            {
                'name': 'NIDMM_VAL_AC_VOLTS_DC_COUPLED',
                'value': 1001,
'documentation': {
'description': 'AC Voltage with DC Coupling',
},
            },
            {
                'name': 'NIDMM_VAL_DIODE',
                'value': 1002,
'documentation': {
'description': 'Diode',
},
            },
            {
                'name': 'NIDMM_VAL_WAVEFORM_VOLTAGE',
                'value': 1003,
'documentation': {
'description': 'Waveform voltage',
},
            },
            {
                'name': 'NIDMM_VAL_WAVEFORM_CURRENT',
                'value': 1004,
'documentation': {
'description': 'Waveform current',
},
            },
            {
                'name': 'NIDMM_VAL_CAPACITANCE',
                'value': 1005,
'documentation': {
'description': 'Capacitance',
},
            },
            {
                'name': 'NIDMM_VAL_INDUCTANCE',
                'value': 1006,
'documentation': {
'description': 'Inductance',
},
            },
        ],
    },
    'InputResistance': {
        'values': [
            {
                'name': 'NIDMM_VAL_1_MEGAOHM',
                'value': 1000000.0,
'documentation': {
'description': 'Input resistance of 1 M Ohm',
},
            },
            {
                'name': 'NIDMM_VAL_10_MEGAOHM',
                'value': 10000000.0,
'documentation': {
'description': 'Input resistance of 10 M Ohm',
},
            },
            {
                'name': 'NIDMM_VAL_GREATER_THAN_10_GIGAOHM',
                'value': 10000000000.0,
'documentation': {
'description': 'Input resistance greater than 10 G Ohm',
},
            },
        ],
    },
    'LCCalculationModel': {
        'values': [
            {
                'name': 'NIDMM_VAL_CALC_MODEL_AUTO',
                'value': -1,
'documentation': {
'description': 'NI-DMM chooses the algorithm based on function and range',
},
            },
            {
                'name': 'NIDMM_VAL_CALC_MODEL_SERIES',
                'value': 0,
'documentation': {
'description': 'NI-DMM uses the series impedance model to calculate capacitance and inductance',
},
            },
            {
                'name': 'NIDMM_VAL_CALC_MODEL_PARALLEL',
                'value': 1,
'documentation': {
'description': 'NI-DMM uses the parallel admittance model to calculate capacitance and inductance',
},
            },
        ],
    },
    'MeasurementCompleteDest': {
        'values': [
            {
                'name': 'NIDMM_VAL_NONE',
                'value': -1,
'documentation': {
'description': 'No Trigger',
},
            },
            {
                'name': 'NIDMM_VAL_EXTERNAL',
                'value': 2,
'documentation': {
'description': 'AUX I/O Connector',
},
            },
            {
                'name': 'NIDMM_VAL_PXI_TRIG0',
                'value': 111,
'documentation': {
'description': 'PXI Trigger Line 0',
},
            },
            {
                'name': 'NIDMM_VAL_PXI_TRIG1',
                'value': 112,
'documentation': {
'description': 'PXI Trigger Line 1',
},
            },
            {
                'name': 'NIDMM_VAL_PXI_TRIG2',
                'value': 113,
'documentation': {
'description': 'PXI Trigger Line 2',
},
            },
            {
                'name': 'NIDMM_VAL_PXI_TRIG3',
                'value': 114,
'documentation': {
'description': 'PXI Trigger Line 3',
},
            },
            {
                'name': 'NIDMM_VAL_PXI_TRIG4',
                'value': 115,
'documentation': {
'description': 'PXI Trigger Line 4',
},
            },
            {
                'name': 'NIDMM_VAL_PXI_TRIG5',
                'value': 116,
'documentation': {
'description': 'PXI Trigger Line 5',
},
            },
            {
                'name': 'NIDMM_VAL_PXI_TRIG6',
                'value': 117,
'documentation': {
'description': 'PXI Trigger Line 6',
},
            },
            {
                'name': 'NIDMM_VAL_PXI_TRIG7',
                'value': 118,
'documentation': {
'description': 'PXI Trigger Line 7',
},
            },
            {
                'name': 'NIDMM_VAL_LBR_TRIG0',
                'value': 1003,
'documentation': {
'description': 'Internal Trigger Line of a PXI/SCXI Combination Chassis',
},
            },
        ],
    },
    'MeasurementDestinationSlope': {
        'values': [
            {
                'name': 'NIDMM_VAL_POSITIVE',
                'value': 0,
'documentation': {
'description': 'Rising Edgs',
},
            },
            {
                'name': 'NIDMM_VAL_NEGATIVE',
                'value': 1,
'documentation': {
'description': 'Falling Edge',
},
            },
        ],
    },
    'OffsetCompensatedOhms': {
        'values': [
            {
                'name': 'NIDMM_VAL_OFFSET_COMP_OHMS_OFF',
                'value': 0,
'documentation': {
'description': 'The DMM disables offset compensated ohms.',
},
            },
            {
                'name': 'NIDMM_VAL_OFFSET_COMP_OHMS_ON',
                'value': 1,
'documentation': {
'description': 'The DMM enables offset compensated ohms.',
},
            },
        ],
    },
    'OperationMode': {
        'values': [
            {
                'name': 'NIDMM_VAL_IVIDMM_MODE',
                'value': 0,
'documentation': {
'description': 'IviDmm Mode',
},
            },
            {
                'name': 'NIDMM_VAL_WAVEFORM_MODE',
                'value': 1,
'documentation': {
'description': 'Waveform acquisition mode',
},
            },
        ],
    },
    'PowerlineFrequency': {
        'values': [
            {
                'name': 'NIDMM_VAL_50_HERTZ',
                'value': 50.0,
'documentation': {
'description': 'Specifies the powerline frequency as 50 Hz.',
},
            },
            {
                'name': 'NIDMM_VAL_60_HERTZ',
                'value': 60.0,
'documentation': {
'description': 'Specifies the powerline frequency as 60 Hz.',
},
            },
        ],
    },
    'RTDType': {
        'values': [
            {
                'name': 'NIDMM_VAL_TEMP_RTD_CUSTOM',
                'value': 0,
'documentation': {
'description': '''
Performs Callendar-Van Dusen RTD scaling with the user-specified A, B,
and C coefficients.
''',
},
            },
            {
                'name': 'NIDMM_VAL_TEMP_RTD_PT3750',
                'value': 1,
'documentation': {
'description': 'Performs scaling for a Pt 3750 RTD.',
},
            },
            {
                'name': 'NIDMM_VAL_TEMP_RTD_PT3851',
                'value': 2,
'documentation': {
'description': 'Performs scaling for a Pt 3851 RTD.',
},
            },
            {
                'name': 'NIDMM_VAL_TEMP_RTD_PT3911',
                'value': 3,
'documentation': {
'description': 'Performs scaling for a Pt 3911 RTD.',
},
            },
            {
                'name': 'NIDMM_VAL_TEMP_RTD_PT3916',
                'value': 4,
'documentation': {
'description': 'Performs scaling for a Pt 3916 RTD.',
},
            },
            {
                'name': 'NIDMM_VAL_TEMP_RTD_PT3920',
                'value': 5,
'documentation': {
'description': 'Performs scaling for a Pt 3920 RTD.',
},
            },
            {
                'name': 'NIDMM_VAL_TEMP_RTD_PT3928',
                'value': 6,
'documentation': {
'description': 'Performs scaling for a Pt 3928 RTD.',
},
            },
        ],
    },
    'SampleTrigSlope': {
        'values': [
            {
                'name': 'NIDMM_VAL_POSITIVE',
                'value': 0,
'documentation': {
'description': 'Rising Edgs',
},
            },
            {
                'name': 'NIDMM_VAL_NEGATIVE',
                'value': 1,
'documentation': {
'description': 'Falling Edge',
},
            },
        ],
    },
    'SampleTrigger': {
        'values': [
            {
                'name': 'NIDMM_VAL_IMMEDIATE',
                'value': 1,
'documentation': {
'description': 'No Trigger',
},
            },
            {
                'name': 'NIDMM_VAL_EXTERNAL',
                'value': 2,
'documentation': {
'description': 'AUX I/O Connector Trigger Line 0',
},
            },
            {
                'name': 'NIDMM_VAL_SOFTWARE_TRIG',
                'value': 3,
'documentation': {
'description': 'Software Trigger',
},
            },
            {
                'name': 'NIDMM_VAL_INTERVAL',
                'value': 10,
'documentation': {
'description': 'Interval Trigger',
},
            },
            {
                'name': 'NIDMM_VAL_PXI_TRIG0',
                'value': 111,
'documentation': {
'description': 'PXI Trigger Line 0',
},
            },
            {
                'name': 'NIDMM_VAL_PXI_TRIG1',
                'value': 112,
'documentation': {
'description': 'PXI Trigger Line 1',
},
            },
            {
                'name': 'NIDMM_VAL_PXI_TRIG2',
                'value': 113,
'documentation': {
'description': 'PXI Trigger Line 2',
},
            },
            {
                'name': 'NIDMM_VAL_PXI_TRIG3',
                'value': 114,
'documentation': {
'description': 'PXI Trigger Line 3',
},
            },
            {
                'name': 'NIDMM_VAL_PXI_TRIG4',
                'value': 115,
'documentation': {
'description': 'PXI Trigger Line 4',
},
            },
            {
                'name': 'NIDMM_VAL_PXI_TRIG5',
                'value': 116,
'documentation': {
'description': 'PXI Trigger Line 5',
},
            },
            {
                'name': 'NIDMM_VAL_PXI_TRIG6',
                'value': 117,
'documentation': {
'description': 'PXI Trigger Line 6',
},
            },
            {
                'name': 'NIDMM_VAL_PXI_TRIG7',
                'value': 118,
'documentation': {
'description': 'PXI Trigger Line 7',
},
            },
            {
                'name': 'NIDMM_VAL_PXI_STAR',
                'value': 131,
'documentation': {
'description': 'PXI Star Trigger Line',
},
            },
            {
                'name': 'NIDMM_VAL_AUX_TRIG1',
                'value': 1001,
'documentation': {
'description': 'AUX I/0 Connector Trigger Line 1',
},
            },
            {
                'name': 'NIDMM_VAL_LBR_TRIG1',
                'value': 1004,
'documentation': {
'description': 'Internal Trigger Line of a PXI/SCXI Combination Chassis',
},
            },
        ],
    },
    'ThermistorType': {
        'values': [
            {
                'name': 'NIDMM_VAL_TEMP_THERMISTOR_CUSTOM',
                'value': 0,
'documentation': {
'description': 'Custom',
},
            },
            {
                'name': 'NIDMM_VAL_TEMP_THERMISTOR_44004',
                'value': 1,
'documentation': {
'description': '44004',
},
            },
            {
                'name': 'NIDMM_VAL_TEMP_THERMISTOR_44006',
                'value': 2,
'documentation': {
'description': '44006',
},
            },
            {
                'name': 'NIDMM_VAL_TEMP_THERMISTOR_44007',
                'value': 3,
'documentation': {
'description': '44007',
},
            },
        ],
    },
    'ThermocoupleReferenceJunctionType': {
        'values': [
            {
                'name': 'FIXED',
                'value': 2,
'documentation': {
'description': '''
Thermocouple reference juction is fixed at the user-specified
temperature.
''',
},
            },
        ],
    },
    'ThermocoupleType': {
        'values': [
            {
                'name': 'NIDMM_VAL_TEMP_TC_B',
                'value': 1,
'documentation': {
'description': 'Thermocouple type B',
},
            },
            {
                'name': 'NIDMM_VAL_TEMP_TC_E',
                'value': 4,
'documentation': {
'description': 'Thermocouple type E',
},
            },
            {
                'name': 'NIDMM_VAL_TEMP_TC_J',
                'value': 6,
'documentation': {
'description': 'Thermocouple type J',
},
            },
            {
                'name': 'NIDMM_VAL_TEMP_TC_K',
                'value': 7,
'documentation': {
'description': 'Thermocouple type K',
},
            },
            {
                'name': 'NIDMM_VAL_TEMP_TC_N',
                'value': 8,
'documentation': {
'description': 'Thermocouple type N',
},
            },
            {
                'name': 'NIDMM_VAL_TEMP_TC_R',
                'value': 9,
'documentation': {
'description': 'Thermocouple type R',
},
            },
            {
                'name': 'NIDMM_VAL_TEMP_TC_S',
                'value': 10,
'documentation': {
'description': 'Thermocouple type S',
},
            },
            {
                'name': 'NIDMM_VAL_TEMP_TC_T',
                'value': 11,
'documentation': {
'description': 'Thermocouple type T',
},
            },
        ],
    },
    'TransducerType': {
        'values': [
            {
                'name': 'NIDMM_VAL_THERMOCOUPLE',
                'value': 1,
'documentation': {
'description': 'Thermocouple',
},
            },
            {
                'name': 'NIDMM_VAL_THERMISTOR',
                'value': 2,
'documentation': {
'description': 'Thermistor',
},
            },
            {
                'name': 'NIDMM_VAL_2_WIRE_RTD',
                'value': 3,
'documentation': {
'description': '2-wire RTD',
},
            },
            {
                'name': 'NIDMM_VAL_4_WIRE_RTD',
                'value': 4,
'documentation': {
'description': '4-wire RTD',
},
            },
        ],
    },
    'TriggerSlope': {
        'values': [
            {
                'name': 'NIDMM_VAL_POSITIVE',
                'value': 0,
'documentation': {
'description': 'Rising Edgs',
},
            },
            {
                'name': 'NIDMM_VAL_NEGATIVE',
                'value': 1,
'documentation': {
'description': 'Falling Edge',
},
            },
        ],
    },
    'TriggerSource': {
        'values': [
            {
                'name': 'NIDMM_VAL_IMMEDIATE',
                'value': 1,
'documentation': {
'description': 'No Trigger',
},
            },
            {
                'name': 'NIDMM_VAL_EXTERNAL',
                'value': 2,
'documentation': {
'description': 'AUX I/O Connector Trigger Line 0',
},
            },
            {
                'name': 'NIDMM_VAL_SOFTWARE_TRIG',
                'value': 3,
'documentation': {
'description': 'Software Trigger',
},
            },
            {
                'name': 'NIDMM_VAL_PXI_TRIG0',
                'value': 111,
'documentation': {
'description': 'PXI Trigger Line 0',
},
            },
            {
                'name': 'NIDMM_VAL_PXI_TRIG1',
                'value': 112,
'documentation': {
'description': 'PXI Trigger Line 1',
},
            },
            {
                'name': 'NIDMM_VAL_PXI_TRIG2',
                'value': 113,
'documentation': {
'description': 'PXI Trigger Line 2',
},
            },
            {
                'name': 'NIDMM_VAL_PXI_TRIG3',
                'value': 114,
'documentation': {
'description': 'PXI Trigger Line 3',
},
            },
            {
                'name': 'NIDMM_VAL_PXI_TRIG4',
                'value': 115,
'documentation': {
'description': 'PXI Trigger Line 4',
},
            },
            {
                'name': 'NIDMM_VAL_PXI_TRIG5',
                'value': 116,
'documentation': {
'description': 'PXI Trigger Line 5',
},
            },
            {
                'name': 'NIDMM_VAL_PXI_TRIG6',
                'value': 117,
'documentation': {
'description': 'PXI Trigger Line 6',
},
            },
            {
                'name': 'NIDMM_VAL_PXI_TRIG7',
                'value': 118,
'documentation': {
'description': 'PXI Trigger Line 7',
},
            },
            {
                'name': 'NIDMM_VAL_PXI_STAR',
                'value': 131,
'documentation': {
'description': 'PXI Star Trigger Line',
},
            },
            {
                'name': 'NIDMM_VAL_AUX_TRIG1',
                'value': 1001,
'documentation': {
'description': 'AUX I/O Connector Trigger Line 1',
},
            },
            {
                'name': 'NIDMM_VAL_LBR_TRIG1',
                'value': 1004,
'documentation': {
'description': 'Internal Trigger Line of a PXI/SCXI Combination Chassis',
},
            },
        ],
    },
    'WaveformCoupling': {
        'values': [
            {
                'name': 'NIDMM_VAL_WAVEFORM_COUPLING_AC',
                'value': 0,
'documentation': {
'description': 'AC Coupled',
},
            },
            {
                'name': 'NIDMM_VAL_WAVEFORM_COUPLING_DC',
                'value': 1,
'documentation': {
'description': 'DC Coupled',
},
            },
        ],
    },
}
