
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
                'value': -1,
'documentation': {
'description': '''
The DMM enables or disables ADC calibration based on the configured
function and resolution.
''',
},
            },
            {
                'name': 'OFF',
                'value': 0,
'documentation': {
'description': 'The DMM does not compensate for changes to the gain.',
},
            },
            {
                'name': 'ON',
                'value': 1,
'documentation': {
'description': '''
The DMM measures an internal reference to calculate the correct gain for
the measurement.
''',
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
'description': 'Units are seconds.',
},
            },
            {
                'name': 'POWER_LINE_CYCLES',
                'value': 1,
'documentation': {
'description': 'Units are powerline cycles (PLCs).',
},
            },
        ],
    },
    'AutoZero': {
        'values': [
            {
                'name': 'AUTO',
                'value': -1,
'documentation': {
'description': '''
NI-DMM chooses the Auto Zero setting based on the configured function
and resolution.
''',
},
            },
            {
                'name': 'OFF',
                'value': 0,
'documentation': {
'description': 'Disables AutoZero.',
},
            },
            {
                'name': 'ON',
                'value': 1,
'documentation': {
'description': '''
The DMM internally disconnects the input signal following each
measurement and takes a zero reading. It then subtracts the zero reading
from the preceding reading. For NI 4065 devices, Auto Zero is always ON.
Auto Zero is an integral part of the signal measurement phase and adds
no extra time to the overall measurement.
''',
},
            },
            {
                'name': 'ONCE',
                'value': 2,
'documentation': {
'description': '''
The DMM internally disconnects the input signal for the first
measurement and takes a zero reading. It then subtracts the zero reading
from the first reading and the following readings. The NI 4060/4065 does
not support this setting.
''',
},
            },
        ],
    },
    'CableCompensationType': {
        'values': [
            {
                'name': 'NONE',
                'value': 0,
'documentation': {
'description': 'No cable compensation.',
},
            },
            {
                'name': 'OPEN',
                'value': 1,
'documentation': {
'description': 'Open cable compensation.',
},
            },
            {
                'name': 'SHORT',
                'value': 2,
'documentation': {
'description': 'Short cable compensation.',
},
            },
            {
                'name': 'OPEN_AND_SHORT',
                'value': 3,
'documentation': {
'description': 'Open and short cable compensation.',
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
                'name': 'DC_BIAS_OFF',
                'value': 0,
'documentation': {
'description': 'NI-DMM programs the device not to use the DC bias.',
},
            },
            {
                'name': 'DC_BIAS_ON',
                'value': 1,
'documentation': {
'description': 'NI-DMM programs the device to use the DC bias.',
},
            },
        ],
    },
    'DCNoiseRejection': {
        'values': [
            {
                'name': 'AUTO',
                'value': -1,
'documentation': {
'description': '''
The driver chooses the DC noise rejection setting based on the
configured function and resolution.
''',
},
            },
            {
                'name': 'NORMAL',
                'value': 0,
'documentation': {
'description': 'NI-DMM weighs all samples equally.',
},
            },
            {
                'name': 'SECOND_ORDER',
                'value': 1,
'documentation': {
'description': '''
NI-DMM weighs the samples taken in the middle of the aperture time more
than samples taken at the beginning and the end of the measurement using
a triangular weighing function.
''',
},
            },
            {
                'name': 'HIGH_ORDER',
                'value': 2,
'documentation': {
'description': '''
NI-DMM weighs the samples taken in the middle of the aperture time more
than samples taken at the beginning and the end of the measurement using
a bell-curve weighing function.
''',
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
'description': 'All devices supported.',
},
            },
            {
                'name': 'AC_VOLTS',
                'value': 2,
'documentation': {
'description': 'All devices supported.',
},
            },
            {
                'name': 'DC_CURRENT',
                'value': 3,
'documentation': {
'description': 'All devices supported.',
},
            },
            {
                'name': 'AC_CURRENT',
                'value': 4,
'documentation': {
'description': 'All devices supported.',
},
            },
            {
                'name': '_2_WIRE_RESISTANCE',
                'value': 5,
'documentation': {
'description': 'All devices supported.',
},
            },
            {
                'name': '_4_WIRE_RESISTANCE',
                'value': 101,
'documentation': {
'description': 'NI 4065, and NI 4070/4071/4072 supported.',
},
            },
            {
                'name': 'FREQUENCY',
                'value': 104,
'documentation': {
'description': 'NI 4070/4071/4072 supported.',
},
            },
            {
                'name': 'PERIOD',
                'value': 105,
'documentation': {
'description': 'NI 4070/4071/4072 supported.',
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
                'name': '_AC_VOLTS_DC_COUPLED',
                'value': 1001,
'documentation': {
'description': 'NI 4070/4071/4072 supported.',
},
            },
            {
                'name': 'DIODE',
                'value': 1002,
'documentation': {
'description': 'All devices supported.',
},
            },
            {
                'name': 'WAVEFORM_VOLTAGE',
                'value': 1003,
'documentation': {
'description': 'NI 4070/4071/4072 supported.',
},
            },
            {
                'name': '_WAVEFORM_CURRENT',
                'value': 1004,
'documentation': {
'description': 'NI 4070/4071/4072 supported.',
},
            },
            {
                'name': 'CAPACITANCE',
                'value': 1005,
'documentation': {
'description': 'NI 4072 supported.',
},
            },
            {
                'name': 'INDUCTANCE',
                'value': 1006,
'documentation': {
'description': 'NI 4072 supported.',
},
            },
        ],
    },
    'InputResistance': {
        'values': [
            {
                'name': '_1_M_OHM',
                'value': 1000000.0,
'documentation': {
'description': 'Input resistance of 1 M Ohm',
},
            },
            {
                'name': '_10_M_OHM',
                'value': 10000000.0,
'documentation': {
'description': 'Input resistance of 10 M Ohm',
},
            },
            {
                'name': 'GREATER_THAN_10_G_OHM',
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
                'value': -1,
'documentation': {
'description': 'NI-DMM chooses the algorithm based on function and range.',
},
            },
            {
                'name': 'SERIES',
                'value': 0,
'documentation': {
'description': '''
NI-DMM uses the series impedance model to calculate capacitance and
inductance.
''',
},
            },
            {
                'name': 'PARALLEL',
                'value': 1,
'documentation': {
'description': '''
NI-DMM uses the parallel admittance model to calculate capacitance and
inductance.
''',
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
'description': 'No destination specified.',
},
            },
            {
                'name': 'EXTERNAL',
                'value': 2,
'documentation': {
'description': 'Pin 6 on the AUX Connector',
},
            },
            {
                'name': 'TTL_0',
                'value': 111,
'documentation': {
'description': 'PXI Trigger Line 0',
},
            },
            {
                'name': 'TTL_1',
                'value': 112,
'documentation': {
'description': 'PXI Trigger Line 1',
},
            },
            {
                'name': 'TL_2',
                'value': 113,
'documentation': {
'description': 'PXI Trigger Line 2',
},
            },
            {
                'name': 'TTL_3',
                'value': 114,
'documentation': {
'description': 'PXI Trigger Line 3',
},
            },
            {
                'name': 'TL_4',
                'value': 115,
'documentation': {
'description': 'PXI Trigger Line 4',
},
            },
            {
                'name': 'TTL_5',
                'value': 116,
'documentation': {
'description': 'PXI Trigger Line 5',
},
            },
            {
                'name': 'TTL_6',
                'value': 117,
'documentation': {
'description': 'PXI Trigger Line 6',
},
            },
            {
                'name': 'TTL_7',
                'value': 118,
'documentation': {
'description': 'PXI Trigger Line 7',
},
            },
            {
                'name': '_LBR_TRIG_0',
                'value': 1003,
'documentation': {
'description': 'Local Bus Right Trigger Line 0 of PXI/SCXI combination chassis',
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
'description': 'The driver triggers on the rising edge of the trigger signal.',
},
            },
            {
                'name': 'NEGATIVE',
                'value': 1,
'documentation': {
'description': 'The driver triggers on the falling edge of the trigger signal.',
},
            },
        ],
    },
    'OffsetCompensatedOhms': {
        'values': [
            {
                'name': 'OFF',
                'value': 0,
'documentation': {
'description': 'Disables Offset Compensated Ohms.',
},
            },
            {
                'name': 'ON',
                'value': 1,
'documentation': {
'description': 'Enables Offset Compensated Ohms.',
},
            },
        ],
    },
    'OperationMode': {
        'values': [
            {
                'name': '_IVIDMM_MODE',
                'value': 0,
'documentation': {
'description': '''
Single or multipoint measurements: When the Trigger Count and Sample
Count properties are both set to 1, the NI 4065, NI 4070/4071/4072, and
NI 4080/4081/4082 take a single-point measurement; otherwise, NI-DMM
takes multipoint measurements.
''',
},
            },
            {
                'name': 'WAVEFORM_MODE',
                'value': 1,
'documentation': {
'description': '''
Configures the NI 4080/4081/4082 and NI 4070/4071/4072 to take waveform
measurements.
''',
},
            },
        ],
    },
    'PowerlineFrequency': {
        'values': [
            {
                'name': '_50_HZ',
                'value': 50.0,
'documentation': {
'description': 'Specifies the powerline frequency as 50 Hz.',
},
            },
            {
                'name': '_60_HZ',
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
                'value': 0,
'documentation': {
'description': '''
Performs Callendar-Van Dusen RTD scaling with the user-specified A, B,
and C coefficients.
''',
},
            },
            {
                'name': 'PT_3750',
                'value': 1,
'documentation': {
'description': 'Performs scaling for a Pt 3750 RTD.',
},
            },
            {
                'name': 'PT_3851',
                'value': 2,
'documentation': {
'description': 'Performs scaling for a Pt 3851 RTD.',
},
            },
            {
                'name': 'PT_3911',
                'value': 3,
'documentation': {
'description': 'Performs scaling for a Pt 3911 RTD.',
},
            },
            {
                'name': 'PT_3916',
                'value': 4,
'documentation': {
'description': 'Performs scaling for a Pt 3916 RTD.',
},
            },
            {
                'name': 'PT_3920',
                'value': 5,
'documentation': {
'description': 'Performs scaling for a Pt 3920 RTD.',
},
            },
            {
                'name': 'PT_3928',
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
'description': 'The driver triggers on the rising edge of the trigger signal.',
},
            },
            {
                'name': 'NEGATIVE',
                'value': 1,
'documentation': {
'description': 'The driver triggers on the falling edge of the trigger signal.',
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
'description': 'No trigger specified',
},
            },
            {
                'name': '_EXTERNAL',
                'value': 2,
'documentation': {
'description': 'Pin 9 on the AUX Connector',
},
            },
            {
                'name': 'SOFTWARE_TRIG',
                'value': 3,
'documentation': {
'description': '''
Configures the DMM to wait until `niDMM Send Software
Trigger <dmmviref.chm::/niDMM_Send_Software_Trigger.html>`__ is called.
''',
},
            },
            {
                'name': 'INTERVAL',
                'value': 10,
'documentation': {
'description': 'Interval trigger',
},
            },
            {
                'name': 'TTL_0',
                'value': 111,
'documentation': {
'description': 'PXI Trigger Line 0',
},
            },
            {
                'name': 'TTL_1',
                'value': 112,
'documentation': {
'description': 'PXI Trigger Line 1',
},
            },
            {
                'name': 'TTL_2',
                'value': 113,
'documentation': {
'description': 'PXI Trigger Line 2',
},
            },
            {
                'name': '_TTL_3',
                'value': 114,
'documentation': {
'description': 'PXI Trigger Line 3',
},
            },
            {
                'name': 'TTL_4',
                'value': 115,
'documentation': {
'description': 'PXI Trigger Line 4',
},
            },
            {
                'name': 'TTL_5',
                'value': 116,
'documentation': {
'description': 'PXI Trigger Line 5',
},
            },
            {
                'name': 'TTL_6',
                'value': 117,
'documentation': {
'description': 'PXI Trigger Line 6',
},
            },
            {
                'name': 'TTL_7',
                'value': 118,
'documentation': {
'description': 'PXI Trigger Line 7',
},
            },
            {
                'name': 'PXI_STAR',
                'value': 131,
'documentation': {
'description': 'PXI Star trigger line',
},
            },
            {
                'name': 'AUX_TRIG_1',
                'value': 1001,
'documentation': {
'description': 'Pin 3 on the AUX connector',
},
            },
            {
                'name': 'LBR_TRIG_1',
                'value': 1004,
'documentation': {
'description': 'Local Bus Right Trigger Line 1 of PXI/SCXI combination chassis',
},
            },
        ],
    },
    'ThermistorType': {
        'values': [
            {
                'name': 'CUSTOM',
                'value': 0,
'documentation': {
'description': '''
Performs Steinhart-Hart thermistor scaling with the user-specified A, B,
and C coefficients.
''',
},
            },
            {
                'name': '_44004',
                'value': 1,
'documentation': {
'description': 'Performs scaling for an Omega Series 44004 thermistor.',
},
            },
            {
                'name': '_44006',
                'value': 2,
'documentation': {
'description': 'Performs scaling for an Omega Series 44006 thermistor.',
},
            },
            {
                'name': '_44007',
                'value': 3,
'documentation': {
'description': 'Performs scaling for an Omega Series 44007 thermistor.',
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
                'value': 1,
'documentation': {
'description': 'Thermocouple type B',
},
            },
            {
                'name': 'E',
                'value': 4,
'documentation': {
'description': 'Thermocouple type E',
},
            },
            {
                'name': 'J',
                'value': 6,
'documentation': {
'description': 'Thermocouple type J',
},
            },
            {
                'name': 'K',
                'value': 7,
'documentation': {
'description': 'Thermocouple type K',
},
            },
            {
                'name': 'N',
                'value': 8,
'documentation': {
'description': 'Thermocouple type N',
},
            },
            {
                'name': 'R',
                'value': 9,
'documentation': {
'description': 'Thermocouple type R',
},
            },
            {
                'name': 'S',
                'value': 10,
'documentation': {
'description': 'Thermocouple type S',
},
            },
            {
                'name': 'T',
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
'description': 'Use for thermocouple measurements.',
},
            },
            {
                'name': 'THERMISTOR',
                'value': 2,
'documentation': {
'description': 'Use for thermistor measurements.',
},
            },
            {
                'name': '_2_WIRE_RTD',
                'value': 3,
'documentation': {
'description': 'Use for 2-wire RTD measurements.',
},
            },
            {
                'name': '_4_WIRE_RTD',
                'value': 4,
'documentation': {
'description': 'Use for 4-wire RTD measurements.',
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
'description': 'The driver triggers on the rising edge of the trigger signal.',
},
            },
            {
                'name': 'NEGATIVE',
                'value': 1,
'documentation': {
'description': 'The driver triggers on the falling edge of the trigger signal.',
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
'description': 'No trigger specified.',
},
            },
            {
                'name': 'EXTERNAL',
                'value': 2,
'documentation': {
'description': 'Pin 9 on the AUX Connector',
},
            },
            {
                'name': 'SOFTWARE_TRIG',
                'value': 3,
'documentation': {
'description': '''
Waits until `niDMM Send Software
Trigger <dmmviref.chm::/niDMM_Send_Software_Trigger.html>`__ is called.
''',
},
            },
            {
                'name': '_TTL_0',
                'value': 111,
'documentation': {
'description': 'PXI Trigger Line 0',
},
            },
            {
                'name': 'TTL_1',
                'value': 112,
'documentation': {
'description': 'PXI Trigger Line 1',
},
            },
            {
                'name': 'TTL_2',
                'value': 113,
'documentation': {
'description': 'PXI Trigger Line 2',
},
            },
            {
                'name': '_TTL_3',
                'value': 114,
'documentation': {
'description': 'PXI Trigger Line 3',
},
            },
            {
                'name': 'TTL_4',
                'value': 115,
'documentation': {
'description': 'PXI Trigger Line 4',
},
            },
            {
                'name': 'TTL_5',
                'value': 116,
'documentation': {
'description': 'PXI Trigger Line 5',
},
            },
            {
                'name': 'TTL_6',
                'value': 117,
'documentation': {
'description': 'PXI Trigger Line 6',
},
            },
            {
                'name': '_TTL_7',
                'value': 118,
'documentation': {
'description': 'PXI Trigger Line 7',
},
            },
            {
                'name': '_PXI_STAR',
                'value': 131,
'documentation': {
'description': 'PXI Star Trigger Line',
},
            },
            {
                'name': 'AUX_TRIG_1',
                'value': 1001,
'documentation': {
'description': 'Pin 3 on the AUX connector',
},
            },
            {
                'name': 'LBR_TRIG_1',
                'value': 1004,
'documentation': {
'description': 'Local Bus Right Trigger Line 1 of PXI/SCXI combination chassis',
},
            },
        ],
    },
    'WaveformCoupling': {
        'values': [
            {
                'name': 'AC',
                'value': 0,
'documentation': {
'description': 'Specifies AC coupling.',
},
            },
            {
                'name': 'DC',
                'value': 1,
'documentation': {
'description': 'Specifies DC coupling.',
},
            },
        ],
    },
}
