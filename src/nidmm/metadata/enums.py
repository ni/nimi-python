
# -*- coding: utf-8 -*-
# This file is code generated, do not make changes here.
#  If the generated information is not correct for python
#  changes can be made in enums_addon.py and they will be
#  applied at build time.

enums = {
    'ADCCalibration': {
        'values': [
            {
                'name': 'AUTO',
                'prefix': 'ADC_CALIBRATION_',
                'value': -1,
'documentation': {
'description': 'The DMM enables or disables ADC calibration for you.',
},
            },
            {
                'name': 'OFF',
                'prefix': 'ADC_CALIBRATION_',
                'value': 0,
'documentation': {
'description': 'The DMM does not compensate for changes to the gain.',
},
            },
            {
                'name': 'ON',
                'prefix': 'ADC_CALIBRATION_',
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
                'name': 'SECONDS',
                'value': 0,
'documentation': {
'description': 'Seconds',
},
            },
            {
                'name': 'POWER_LINE_CYCLES',
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
                'name': 'AUTO',
                'prefix': 'AUTO_ZERO_',
                'value': -1,
'documentation': {
'description': 'The drivers chooses the AutoZero setting based on the configured function  and resolution.',
},
            },
            {
                'name': 'OFF',
                'prefix': 'AUTO_ZERO_',
                'value': 0,
'documentation': {
'description': 'Disables AutoZero.',
},
            },
            {
                'name': 'ON',
                'prefix': 'AUTO_ZERO_',
                'value': 1,
'documentation': {
'description': 'The DMM internally disconnects the input signal following each measurement  and takes a zero reading. It then subtracts the zero reading from the  preceding reading.',
},
            },
            {
                'name': 'ONCE',
                'prefix': 'AUTO_ZERO_',
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
                'name': 'NONE',
                'prefix': 'CABLE_COMP_',
                'value': 0,
'documentation': {
'description': 'No Cable Compensation',
},
            },
            {
                'name': 'OPEN',
                'prefix': 'CABLE_COMP_',
                'value': 1,
'documentation': {
'description': 'Open Cable Compensation',
},
            },
            {
                'name': 'SHORT',
                'prefix': 'CABLE_COMP_',
                'value': 2,
'documentation': {
'description': 'Short Cable Compensation',
},
            },
            {
                'name': 'OPEN_AND_SHORT',
                'prefix': 'CABLE_COMP_',
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
                'name': '_1_MICROAMP',
                'value': 1e-06,
'documentation': {
'description': 'NI 4070/4071/4072 are supported.',
},
            },
            {
                'name': '_10_MICROAMP',
                'value': 1e-05,
'documentation': {
'description': 'NI 4080/4081/4082 and NI 4070/4071/4072 are supported.',
},
            },
            {
                'name': '_100_MICROAMP',
                'value': 0.0001,
'documentation': {
'description': 'NI 4080/4081/4082, NI 4070/4071/4072, and NI 4065 are supported.',
},
            },
            {
                'name': '_1_MILLIAMP',
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
                'name': 'OFF',
                'prefix': 'DC_BIAS_',
                'value': 0,
'documentation': {
'description': 'NI-DMM programs the device not to use the DC bias',
},
            },
            {
                'name': 'ON',
                'prefix': 'DC_BIAS_',
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
                'name': 'AUTO',
                'prefix': 'DCNR_',
                'value': -1,
'documentation': {
'description': 'The driver chooses the DC noise rejection setting based on the configured  function and resolution.',
},
            },
            {
                'name': 'NORMAL',
                'prefix': 'DCNR_',
                'value': 0,
'documentation': {
'description': 'NI-DMM weighs all samples equally.',
},
            },
            {
                'name': 'SECOND_ORDER',
                'prefix': 'DCNR_',
                'value': 1,
'documentation': {
'description': 'NI-DMM weighs the samples taken in the middle of the aperture time more than  samples taken at the beginning and the end of the measurement using a  triangular weighing function.',
},
            },
            {
                'name': 'HIGH_ORDER',
                'prefix': 'DCNR_',
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
                'name': 'DC_VOLTS',
                'value': 1,
'documentation': {
'description': 'DC Voltage',
},
            },
            {
                'name': 'AC_VOLTS',
                'value': 2,
'documentation': {
'description': 'AC Voltage',
},
            },
            {
                'name': 'DC_CURRENT',
                'value': 3,
'documentation': {
'description': 'DC Current',
},
            },
            {
                'name': 'AC_CURRENT',
                'value': 4,
'documentation': {
'description': 'AC Current',
},
            },
            {
                'name': '_2_WIRE_RES',
                'value': 5,
'documentation': {
'description': '2-Wire Resistance',
},
            },
            {
                'name': '_4_WIRE_RES',
                'value': 101,
'documentation': {
'description': '4-Wire Resistance',
},
            },
            {
                'name': 'FREQ',
                'value': 104,
'documentation': {
'description': 'Frequency',
},
            },
            {
                'name': 'PERIOD',
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
                'name': 'AC_VOLTS_DC_COUPLED',
                'value': 1001,
'documentation': {
'description': 'AC Voltage with DC Coupling',
},
            },
            {
                'name': 'DIODE',
                'value': 1002,
'documentation': {
'description': 'Diode',
},
            },
            {
                'name': 'WAVEFORM_VOLTAGE',
                'value': 1003,
'documentation': {
'description': 'Waveform voltage',
},
            },
            {
                'name': 'WAVEFORM_CURRENT',
                'value': 1004,
'documentation': {
'description': 'Waveform current',
},
            },
            {
                'name': 'CAPACITANCE',
                'value': 1005,
'documentation': {
'description': 'Capacitance',
},
            },
            {
                'name': 'INDUCTANCE',
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
                'name': '_1_MEGAOHM',
                'value': 1000000.0,
'documentation': {
'description': 'Input resistance of 1 M Ohm',
},
            },
            {
                'name': '_10_MEGAOHM',
                'value': 10000000.0,
'documentation': {
'description': 'Input resistance of 10 M Ohm',
},
            },
            {
                'name': 'GREATER_THAN_10_GIGAOHM',
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
                'name': 'AUTO',
                'prefix': 'CALC_MODEL_',
                'value': -1,
'documentation': {
'description': 'NI-DMM chooses the algorithm based on function and range',
},
            },
            {
                'name': 'SERIES',
                'prefix': 'CALC_MODEL_',
                'value': 0,
'documentation': {
'description': 'NI-DMM uses the series impedance model to calculate capacitance and inductance',
},
            },
            {
                'name': 'PARALLEL',
                'prefix': 'CALC_MODEL_',
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
                'name': 'NONE',
                'value': -1,
'documentation': {
'description': 'No Trigger',
},
            },
            {
                'name': 'EXTERNAL',
                'value': 2,
'documentation': {
'description': 'AUX I/O Connector',
},
            },
            {
                'name': 'PXI_TRIG0',
                'value': 111,
'documentation': {
'description': 'PXI Trigger Line 0',
},
            },
            {
                'name': 'PXI_TRIG1',
                'value': 112,
'documentation': {
'description': 'PXI Trigger Line 1',
},
            },
            {
                'name': 'PXI_TRIG2',
                'value': 113,
'documentation': {
'description': 'PXI Trigger Line 2',
},
            },
            {
                'name': 'PXI_TRIG3',
                'value': 114,
'documentation': {
'description': 'PXI Trigger Line 3',
},
            },
            {
                'name': 'PXI_TRIG4',
                'value': 115,
'documentation': {
'description': 'PXI Trigger Line 4',
},
            },
            {
                'name': 'PXI_TRIG5',
                'value': 116,
'documentation': {
'description': 'PXI Trigger Line 5',
},
            },
            {
                'name': 'PXI_TRIG6',
                'value': 117,
'documentation': {
'description': 'PXI Trigger Line 6',
},
            },
            {
                'name': 'PXI_TRIG7',
                'value': 118,
'documentation': {
'description': 'PXI Trigger Line 7',
},
            },
            {
                'name': 'LBR_TRIG0',
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
                'name': 'POSITIVE',
                'value': 0,
'documentation': {
'description': 'Rising Edgs',
},
            },
            {
                'name': 'NEGATIVE',
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
                'name': 'OFF',
                'prefix': 'OFFSET_COMP_OHMS_',
                'value': 0,
'documentation': {
'description': 'The DMM disables offset compensated ohms.',
},
            },
            {
                'name': 'ON',
                'prefix': 'OFFSET_COMP_OHMS_',
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
                'name': 'IVIDMM',
                'suffix': '_MODE',
                'value': 0,
'documentation': {
'description': 'IviDmm Mode',
},
            },
            {
                'name': 'WAVEFORM',
                'suffix': '_MODE',
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
                'name': '_50',
                'suffix': '_HERTZ',
                'value': 50.0,
'documentation': {
'description': 'Specifies the powerline frequency as 50 Hz.',
},
            },
            {
                'name': '_60',
                'suffix': '_HERTZ',
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
                'name': 'CUSTOM',
                'prefix': 'TEMP_RTD_',
                'value': 0,
'documentation': {
'description': '''
Performs Callendar-Van Dusen RTD scaling with the user-specified A, B,
and C coefficients.
''',
},
            },
            {
                'name': 'PT3750',
                'prefix': 'TEMP_RTD_',
                'value': 1,
'documentation': {
'description': 'Performs scaling for a Pt 3750 RTD.',
},
            },
            {
                'name': 'PT3851',
                'prefix': 'TEMP_RTD_',
                'value': 2,
'documentation': {
'description': 'Performs scaling for a Pt 3851 RTD.',
},
            },
            {
                'name': 'PT3911',
                'prefix': 'TEMP_RTD_',
                'value': 3,
'documentation': {
'description': 'Performs scaling for a Pt 3911 RTD.',
},
            },
            {
                'name': 'PT3916',
                'prefix': 'TEMP_RTD_',
                'value': 4,
'documentation': {
'description': 'Performs scaling for a Pt 3916 RTD.',
},
            },
            {
                'name': 'PT3920',
                'prefix': 'TEMP_RTD_',
                'value': 5,
'documentation': {
'description': 'Performs scaling for a Pt 3920 RTD.',
},
            },
            {
                'name': 'PT3928',
                'prefix': 'TEMP_RTD_',
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
                'name': 'POSITIVE',
                'value': 0,
'documentation': {
'description': 'Rising Edgs',
},
            },
            {
                'name': 'NEGATIVE',
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
                'name': 'IMMEDIATE',
                'value': 1,
'documentation': {
'description': 'No Trigger',
},
            },
            {
                'name': 'EXTERNAL',
                'value': 2,
'documentation': {
'description': 'AUX I/O Connector Trigger Line 0',
},
            },
            {
                'name': 'SOFTWARE_TRIG',
                'value': 3,
'documentation': {
'description': 'Software Trigger',
},
            },
            {
                'name': 'INTERVAL',
                'value': 10,
'documentation': {
'description': 'Interval Trigger',
},
            },
            {
                'name': 'PXI_TRIG0',
                'value': 111,
'documentation': {
'description': 'PXI Trigger Line 0',
},
            },
            {
                'name': 'PXI_TRIG1',
                'value': 112,
'documentation': {
'description': 'PXI Trigger Line 1',
},
            },
            {
                'name': 'PXI_TRIG2',
                'value': 113,
'documentation': {
'description': 'PXI Trigger Line 2',
},
            },
            {
                'name': 'PXI_TRIG3',
                'value': 114,
'documentation': {
'description': 'PXI Trigger Line 3',
},
            },
            {
                'name': 'PXI_TRIG4',
                'value': 115,
'documentation': {
'description': 'PXI Trigger Line 4',
},
            },
            {
                'name': 'PXI_TRIG5',
                'value': 116,
'documentation': {
'description': 'PXI Trigger Line 5',
},
            },
            {
                'name': 'PXI_TRIG6',
                'value': 117,
'documentation': {
'description': 'PXI Trigger Line 6',
},
            },
            {
                'name': 'PXI_TRIG7',
                'value': 118,
'documentation': {
'description': 'PXI Trigger Line 7',
},
            },
            {
                'name': 'PXI_STAR',
                'value': 131,
'documentation': {
'description': 'PXI Star Trigger Line',
},
            },
            {
                'name': 'AUX_TRIG1',
                'value': 1001,
'documentation': {
'description': 'AUX I/0 Connector Trigger Line 1',
},
            },
            {
                'name': 'LBR_TRIG1',
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
                'name': 'CUSTOM',
                'prefix': 'TEMP_THERMISTOR_',
                'value': 0,
'documentation': {
'description': 'Custom',
},
            },
            {
                'name': '_44004',
                'prefix': 'TEMP_THERMISTOR_',
                'value': 1,
'documentation': {
'description': '44004',
},
            },
            {
                'name': '_44006',
                'prefix': 'TEMP_THERMISTOR_',
                'value': 2,
'documentation': {
'description': '44006',
},
            },
            {
                'name': '_44007',
                'prefix': 'TEMP_THERMISTOR_',
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
                'name': 'B',
                'prefix': 'TEMP_TC_',
                'value': 1,
'documentation': {
'description': 'Thermocouple type B',
},
            },
            {
                'name': 'E',
                'prefix': 'TEMP_TC_',
                'value': 4,
'documentation': {
'description': 'Thermocouple type E',
},
            },
            {
                'name': 'J',
                'prefix': 'TEMP_TC_',
                'value': 6,
'documentation': {
'description': 'Thermocouple type J',
},
            },
            {
                'name': 'K',
                'prefix': 'TEMP_TC_',
                'value': 7,
'documentation': {
'description': 'Thermocouple type K',
},
            },
            {
                'name': 'N',
                'prefix': 'TEMP_TC_',
                'value': 8,
'documentation': {
'description': 'Thermocouple type N',
},
            },
            {
                'name': 'R',
                'prefix': 'TEMP_TC_',
                'value': 9,
'documentation': {
'description': 'Thermocouple type R',
},
            },
            {
                'name': 'S',
                'prefix': 'TEMP_TC_',
                'value': 10,
'documentation': {
'description': 'Thermocouple type S',
},
            },
            {
                'name': 'T',
                'prefix': 'TEMP_TC_',
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
                'name': 'THERMOCOUPLE',
                'value': 1,
'documentation': {
'description': 'Thermocouple',
},
            },
            {
                'name': 'THERMISTOR',
                'value': 2,
'documentation': {
'description': 'Thermistor',
},
            },
            {
                'name': '_2_WIRE_RTD',
                'value': 3,
'documentation': {
'description': '2-wire RTD',
},
            },
            {
                'name': '_4_WIRE_RTD',
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
                'name': 'POSITIVE',
                'value': 0,
'documentation': {
'description': 'Rising Edgs',
},
            },
            {
                'name': 'NEGATIVE',
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
                'name': 'IMMEDIATE',
                'value': 1,
'documentation': {
'description': 'No Trigger',
},
            },
            {
                'name': 'EXTERNAL',
                'value': 2,
'documentation': {
'description': 'AUX I/O Connector Trigger Line 0',
},
            },
            {
                'name': 'SOFTWARE_TRIG',
                'value': 3,
'documentation': {
'description': 'Software Trigger',
},
            },
            {
                'name': 'PXI_TRIG0',
                'value': 111,
'documentation': {
'description': 'PXI Trigger Line 0',
},
            },
            {
                'name': 'PXI_TRIG1',
                'value': 112,
'documentation': {
'description': 'PXI Trigger Line 1',
},
            },
            {
                'name': 'PXI_TRIG2',
                'value': 113,
'documentation': {
'description': 'PXI Trigger Line 2',
},
            },
            {
                'name': 'PXI_TRIG3',
                'value': 114,
'documentation': {
'description': 'PXI Trigger Line 3',
},
            },
            {
                'name': 'PXI_TRIG4',
                'value': 115,
'documentation': {
'description': 'PXI Trigger Line 4',
},
            },
            {
                'name': 'PXI_TRIG5',
                'value': 116,
'documentation': {
'description': 'PXI Trigger Line 5',
},
            },
            {
                'name': 'PXI_TRIG6',
                'value': 117,
'documentation': {
'description': 'PXI Trigger Line 6',
},
            },
            {
                'name': 'PXI_TRIG7',
                'value': 118,
'documentation': {
'description': 'PXI Trigger Line 7',
},
            },
            {
                'name': 'PXI_STAR',
                'value': 131,
'documentation': {
'description': 'PXI Star Trigger Line',
},
            },
            {
                'name': 'AUX_TRIG1',
                'value': 1001,
'documentation': {
'description': 'AUX I/O Connector Trigger Line 1',
},
            },
            {
                'name': 'LBR_TRIG1',
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
                'name': 'AC',
                'prefix': 'WAVEFORM_COUPLING_',
                'value': 0,
'documentation': {
'description': 'AC Coupled',
},
            },
            {
                'name': 'DC',
                'prefix': 'WAVEFORM_COUPLING_',
                'value': 1,
'documentation': {
'description': 'DC Coupled',
},
            },
        ],
    },
}
