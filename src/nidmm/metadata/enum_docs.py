enum_docs = {
    'ADCCalibration': {
        '-1': {
            'name': 'Auto',
            'description': '''
The DMM enables or disables ADC calibration based on the configured
function and resolution.
''',
        },
        '0': {
            'name': 'Off',
            'description': '''
The DMM does not compensate for changes to the gain.
''',
        },
        '1': {
            'name': 'On',
            'description': '''
The DMM measures an internal reference to calculate the correct gain for
the measurement.
''',
        },
    },
    'ApertureTimeUnits': {
        '0': {
            'name': 'Seconds',
            'description': '''
Units are seconds.
''',
        },
        '1': {
            'name': 'Power Line Cycles',
            'description': '''
Units are powerline cycles (PLCs).
''',
        },
    },
    'AutoZero': {
        '-1': {
            'name': 'Auto',
            'description': '''
NI-DMM chooses the Auto Zero setting based on the configured function
and resolution.
''',
        },
        '0': {
            'name': 'Off',
            'description': '''
Disables AutoZero.
''',
        },
        '1': {
            'name': 'On',
            'description': '''
The DMM internally disconnects the input signal following each
measurement and takes a zero reading. It then subtracts the zero reading
from the preceding reading. For NI 4065 devices, Auto Zero is always ON.
Auto Zero is an integral part of the signal measurement phase and adds
no extra time to the overall measurement.
''',
        },
        '2': {
            'name': 'Once',
            'description': '''
The DMM internally disconnects the input signal for the first
measurement and takes a zero reading. It then subtracts the zero reading
from the first reading and the following readings. The NI 4060/4065 does
not support this setting.
''',
        },
    },
    'CableCompensationType': {
        '0': {
            'name': 'None',
            'description': '''
No cable compensation.
''',
        },
        '1': {
            'name': 'Open',
            'description': '''
Open cable compensation.
''',
        },
        '2': {
            'name': 'Short',
            'description': '''
Short cable compensation.
''',
        },
        '3': {
            'name': 'Open_and_Short',
            'description': '''
Open and short cable compensation.
''',
        },
    },
    'CurrentSource': {
        '1.000000E-3': {
            'name': '1 Milliamp',
            'description': '''
NI 4080/4081/4082, NI 4070/4071/4072, and NI 4065 are supported.
''',
        },
        '1.000000E-4': {
            'name': '100 Microamp',
            'description': '''
NI 4080/4081/4082, NI 4070/4071/4072, and NI 4065 are supported.
''',
        },
        '1.000000E-5': {
            'name': '10 Microamp',
            'description': '''
NI 4080/4081/4082 and NI 4070/4071/4072 are supported.
''',
        },
        '1.000000E-6': {
            'name': '1 Microamp',
            'description': '''
NI 4070/4071/4072 are supported.
''',
        },
    },
    'DCBias': {
        '0': {
            'name': 'DC Bias Off',
            'description': '''
NI-DMM programs the device not to use the DC bias.
''',
        },
        '1': {
            'name': 'DC Bias On',
            'description': '''
NI-DMM programs the device to use the DC bias.
''',
        },
    },
    'DCNoiseRejection': {
        '-1': {
            'name': 'Auto',
            'description': '''
The driver chooses the DC noise rejection setting based on the
configured function and resolution.
''',
        },
        '0': {
            'name': 'Normal',
            'description': '''
NI-DMM weighs all samples equally.
''',
        },
        '1': {
            'name': 'Second Order',
            'description': '''
NI-DMM weighs the samples taken in the middle of the aperture time more
than samples taken at the beginning and the end of the measurement using
a triangular weighing function.
''',
        },
        '2': {
            'name': 'High Order',
            'description': '''
NI-DMM weighs the samples taken in the middle of the aperture time more
than samples taken at the beginning and the end of the measurement using
a bell-curve weighing function.
''',
        },
    },
    'DigitsResolution': {
        '3.5000000E+0': {
            'name': '3.5',
            'description': '''
Specifies 3.5 digits resolution.
''',
        },
        '4.500000E+0': {
            'name': '4.5',
            'description': '''
Specifies 4.5 digits resolution.
''',
        },
        '5.500000E+0': {
            'name': '5.5',
            'description': '''
Specifies 5.5 digits resolution.
''',
        },
        '6.500000E+0': {
            'name': '6.5',
            'description': '''
Specifies 6.5 digits resolution.
''',
        },
        '7.500000E+0': {
            'name': '7.5',
            'description': '''
Specifies 7.5 digits resolution.
''',
        },
    },
    'Function': {
        '1': {
            'name': 'DC Volts',
            'description': '''
All devices supported.
''',
        },
        '1001': {
            'name': 'AC Volts DC Coupled',
            'description': '''
NI 4070/4071/4072 supported.
''',
        },
        '1002': {
            'name': 'Diode',
            'description': '''
All devices supported.
''',
        },
        '1003': {
            'name': 'Waveform Voltage',
            'description': '''
NI 4070/4071/4072 supported.
''',
        },
        '1004': {
            'name': 'Waveform Current',
            'description': '''
NI 4070/4071/4072 supported.
''',
        },
        '1005': {
            'name': 'Capacitance',
            'description': '''
NI 4072 supported.
''',
        },
        '1006': {
            'name': 'Inductance',
            'description': '''
NI 4072 supported.
''',
        },
        '101': {
            'name': '4-Wire Resistance',
            'description': '''
NI 4065, and NI 4070/4071/4072 supported.
''',
        },
        '104': {
            'name': 'Frequency',
            'description': '''
NI 4070/4071/4072 supported.
''',
        },
        '105': {
            'name': 'Period',
            'description': '''
NI 4070/4071/4072 supported.
''',
        },
        '108': {
            'name': 'Temperature',
            'description': '''
NI 4065, and NI 4070/4071/4072 supported.
''',
        },
        '2': {
            'name': 'AC Volts',
            'description': '''
All devices supported.
''',
        },
        '3': {
            'name': 'DC Current',
            'description': '''
All devices supported.
''',
        },
        '4': {
            'name': 'AC Current',
            'description': '''
All devices supported.
''',
        },
        '5': {
            'name': '2-Wire Resistance',
            'description': '''
All devices supported.
''',
        },
    },
    'InputResistance': {
        '1.000000E+10': {
            'name': 'Greater Than 10 G Ohm',
            'description': '''
Input resistance greater than 10 G Ohm
''',
        },
        '1.000000E+6': {
            'name': '1 M Ohm',
            'description': '''
Input resistance of 1 M Ohm
''',
        },
        '1.000000E+7': {
            'name': '10 M Ohm',
            'description': '''
Input resistance of 10 M Ohm
''',
        },
    },
    'LCCalculationModel': {
        '-1': {
            'name': 'Auto',
            'description': '''
NI-DMM chooses the algorithm based on function and range.
''',
        },
        '0': {
            'name': 'Series',
            'description': '''
NI-DMM uses the series impedance model to calculate capacitance and
inductance.
''',
        },
        '1': {
            'name': 'Parallel',
            'description': '''
NI-DMM uses the parallel admittance model to calculate capacitance and
inductance.
''',
        },
    },
    'MeasurementCompleteDest': {
        '-1': {
            'name': 'None',
            'description': '''
No destination specified.
''',
        },
        '1003': {
            'name': 'LBR Trig 0',
            'description': '''
Local Bus Right Trigger Line 0 of PXI/SCXI combination chassis
''',
        },
        '111': {
            'name': 'TTL 0',
            'description': '''
PXI Trigger Line 0
''',
        },
        '112': {
            'name': 'TTL 1',
            'description': '''
PXI Trigger Line 1
''',
        },
        '113': {
            'name': 'TL 2',
            'description': '''
PXI Trigger Line 2
''',
        },
        '114': {
            'name': 'TTL 3',
            'description': '''
PXI Trigger Line 3
''',
        },
        '115': {
            'name': 'TL 4',
            'description': '''
PXI Trigger Line 4
''',
        },
        '116': {
            'name': 'TTL 5',
            'description': '''
PXI Trigger Line 5
''',
        },
        '117': {
            'name': 'TTL 6',
            'description': '''
PXI Trigger Line 6
''',
        },
        '118': {
            'name': 'TTL 7',
            'description': '''
PXI Trigger Line 7
''',
        },
        '2': {
            'name': 'External',
            'description': '''
Pin 6 on the AUX Connector
''',
        },
    },
    'MeasurementDestinationSlope': {
        '0': {
            'name': 'Positive',
            'description': '''
The driver triggers on the rising edge of the trigger signal.
''',
        },
        '1': {
            'name': 'Negative',
            'description': '''
The driver triggers on the falling edge of the trigger signal.
''',
        },
    },
    'OffsetCompensatedOhms': {
        '0': {
            'name': 'Off',
            'description': '''
Disables Offset Compensated Ohms.
''',
        },
        '1': {
            'name': 'On',
            'description': '''
Enables Offset Compensated Ohms.
''',
        },
    },
    'OperationMode': {
        '0': {
            'name': 'IVIDMM Mode',
            'description': '''
Single or multipoint measurements: When the Trigger Count and Sample
Count properties are both set to 1, the NI 4065, NI 4070/4071/4072, and
NI 4080/4081/4082 take a single-point measurement; otherwise, NI-DMM
takes multipoint measurements.
''',
        },
        '1': {
            'name': 'Waveform Mode',
            'description': '''
Configures the NI 4080/4081/4082 and NI 4070/4071/4072 to take waveform
measurements.
''',
        },
    },
    'PowerlineFrequency': {
        '5.000000E+1': {
            'name': '50 Hz',
            'description': '''
Specifies the powerline frequency as 50 Hz.
''',
        },
        '6.000000E+1': {
            'name': '60 Hz',
            'description': '''
Specifies the powerline frequency as 60 Hz.
''',
        },
    },
    'RTDType': {
        '0': {
            'name': 'Custom',
            'description': '''
Performs Callendar-Van Dusen RTD scaling with the user-specified A, B,
and C coefficients.
''',
        },
        '1': {
            'name': 'Pt 3750',
            'description': '''
Performs scaling for a Pt 3750 RTD.
''',
        },
        '2': {
            'name': 'Pt 3851',
            'description': '''
Performs scaling for a Pt 3851 RTD.
''',
        },
        '3': {
            'name': 'Pt 3911',
            'description': '''
Performs scaling for a Pt 3911 RTD.
''',
        },
        '4': {
            'name': 'Pt 3916',
            'description': '''
Performs scaling for a Pt 3916 RTD.
''',
        },
        '5': {
            'name': 'Pt 3920',
            'description': '''
Performs scaling for a Pt 3920 RTD.
''',
        },
        '6': {
            'name': 'Pt 3928',
            'description': '''
Performs scaling for a Pt 3928 RTD.
''',
        },
    },
    'SampleTrigSlope': {
        '0': {
            'name': 'Positive',
            'description': '''
The driver triggers on the rising edge of the trigger signal.
''',
        },
        '1': {
            'name': 'Negative',
            'description': '''
The driver triggers on the falling edge of the trigger signal.
''',
        },
    },
    'SampleTrigger': {
        '1': {
            'name': 'Immediate',
            'description': '''
No trigger specified
''',
        },
        '10': {
            'name': 'Interval',
            'description': '''
Interval trigger
''',
        },
        '1001': {
            'name': 'AUX Trig 1',
            'description': '''
Pin 3 on the AUX connector
''',
        },
        '1004': {
            'name': 'LBR Trig 1',
            'description': '''
Local Bus Right Trigger Line 1 of PXI/SCXI combination chassis
''',
        },
        '111': {
            'name': 'TTL 0',
            'description': '''
PXI Trigger Line 0
''',
        },
        '112': {
            'name': 'TTL 1',
            'description': '''
PXI Trigger Line 1
''',
        },
        '113': {
            'name': 'TTL 2',
            'description': '''
PXI Trigger Line 2
''',
        },
        '114': {
            'name': 'TTL 3',
            'description': '''
PXI Trigger Line 3
''',
        },
        '115': {
            'name': 'TTL 4',
            'description': '''
PXI Trigger Line 4
''',
        },
        '116': {
            'name': 'TTL 5',
            'description': '''
PXI Trigger Line 5
''',
        },
        '117': {
            'name': 'TTL 6',
            'description': '''
PXI Trigger Line 6
''',
        },
        '118': {
            'name': 'TTL 7',
            'description': '''
PXI Trigger Line 7
''',
        },
        '131': {
            'name': 'PXI Star',
            'description': '''
PXI Star trigger line
''',
        },
        '2': {
            'name': 'External',
            'description': '''
Pin 9 on the AUX Connector
''',
        },
        '3': {
            'name': 'Software Trig',
            'description': '''
Configures the DMM to wait until niDMM Send Software Trigger is called.
''',
        },
    },
    'ThermistorType': {
        '0': {
            'name': 'Custom',
            'description': '''
Performs Steinhart-Hart thermistor scaling with the user-specified A, B,
and C coefficients.
''',
        },
        '1': {
            'name': '44004',
            'description': '''
Performs scaling for an Omega Series 44004 thermistor.
''',
        },
        '2': {
            'name': '44006',
            'description': '''
Performs scaling for an Omega Series 44006 thermistor.
''',
        },
        '3': {
            'name': '44007',
            'description': '''
Performs scaling for an Omega Series 44007 thermistor.
''',
        },
    },
    'ThermocoupleReferenceJunctionType': {
        '2': {
            'name': 'Fixed',
            'description': '''
Thermocouple reference juction is fixed at the user-specified
temperature.
''',
        },
    },
    'ThermocoupleType': {
        '1': {
            'name': 'B',
            'description': '''
Thermocouple type B
''',
        },
        '10': {
            'name': 'S',
            'description': '''
Thermocouple type S
''',
        },
        '11': {
            'name': 'T',
            'description': '''
Thermocouple type T
''',
        },
        '4': {
            'name': 'E',
            'description': '''
Thermocouple type E
''',
        },
        '6': {
            'name': 'J',
            'description': '''
Thermocouple type J
''',
        },
        '7': {
            'name': 'K',
            'description': '''
Thermocouple type K
''',
        },
        '8': {
            'name': 'N',
            'description': '''
Thermocouple type N
''',
        },
        '9': {
            'name': 'R',
            'description': '''
Thermocouple type R
''',
        },
    },
    'TransducerType': {
        '1': {
            'name': 'Thermocouple',
            'description': '''
Use for thermocouple measurements.
''',
        },
        '2': {
            'name': 'Thermistor',
            'description': '''
Use for thermistor measurements.
''',
        },
        '3': {
            'name': '2-Wire RTD',
            'description': '''
Use for 2-wire RTD measurements.
''',
        },
        '4': {
            'name': '4-Wire RTD',
            'description': '''
Use for 4-wire RTD measurements.
''',
        },
    },
    'TriggerSlope': {
        '0': {
            'name': 'Positive',
            'description': '''
The driver triggers on the rising edge of the trigger signal.
''',
        },
        '1': {
            'name': 'Negative',
            'description': '''
The driver triggers on the falling edge of the trigger signal.
''',
        },
    },
    'TriggerSource': {
        '1': {
            'name': 'Immediate',
            'description': '''
No trigger specified.
''',
        },
        '1001': {
            'name': 'AUX_Trig 1',
            'description': '''
Pin 3 on the AUX connector
''',
        },
        '1004': {
            'name': 'LBR Trig 1',
            'description': '''
Local Bus Right Trigger Line 1 of PXI/SCXI combination chassis
''',
        },
        '111': {
            'name': 'TTL 0',
            'description': '''
PXI Trigger Line 0
''',
        },
        '112': {
            'name': 'TTL 1',
            'description': '''
PXI Trigger Line 1
''',
        },
        '113': {
            'name': 'TTL 2',
            'description': '''
PXI Trigger Line 2
''',
        },
        '114': {
            'name': 'TTL 3',
            'description': '''
PXI Trigger Line 3
''',
        },
        '115': {
            'name': 'TTL 4',
            'description': '''
PXI Trigger Line 4
''',
        },
        '116': {
            'name': 'TTL 5',
            'description': '''
PXI Trigger Line 5
''',
        },
        '117': {
            'name': 'TTL 6',
            'description': '''
PXI Trigger Line 6
''',
        },
        '118': {
            'name': 'TTL 7',
            'description': '''
PXI Trigger Line 7
''',
        },
        '131': {
            'name': 'PXI Star',
            'description': '''
PXI Star Trigger Line
''',
        },
        '2': {
            'name': 'External',
            'description': '''
Pin 9 on the AUX Connector
''',
        },
        '3': {
            'name': 'Software Trig',
            'description': '''
Waits until niDMM Send Software Trigger is called.
''',
        },
    },
    'WaveformCoupling': {
        '0': {
            'name': 'AC',
            'description': '''
Specifies AC coupling.
''',
        },
        '1': {
            'name': 'DC',
            'description': '''
Specifies DC coupling.
''',
        },
    },
}
