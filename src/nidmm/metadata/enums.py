# -*- coding: utf-8 -*-
# This file is generated from NI-DMM API metadata version 23.0.0d85
enums = {
    'ADCCalibration': {
        'values': [
            {
                'documentation': {
                    'description': 'The DMM enables or disables ADC calibration for you.'
                },
                'name': 'NIDMM_VAL_ADC_CALIBRATION_AUTO',
                'value': -1
            },
            {
                'documentation': {
                    'description': 'The DMM does not compensate for changes to the gain.'
                },
                'name': 'NIDMM_VAL_ADC_CALIBRATION_OFF',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'The DMM measures an internal reference to calculate the correct gain for the  measurement.'
                },
                'name': 'NIDMM_VAL_ADC_CALIBRATION_ON',
                'value': 1
            }
        ]
    },
    'AcquisitionStatus': {
        'values': [
            {
                'documentation': {
                    'description': 'Running'
                },
                'name': 'NIDMM_VAL_ACQUISITION_STATUS_RUNNING',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Finished with **Backlog**'
                },
                'name': 'NIDMM_VAL_ACQUISITION_STATUS_FINISHED_WITH_BACKLOG',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Finished with no **Backlog**'
                },
                'name': 'NIDMM_VAL_ACQUISITION_STATUS_FINISHED_WITH_NO_BACKLOG',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Paused'
                },
                'name': 'NIDMM_VAL_ACQUISITION_STATUS_PAUSED',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'No acquisition in progress'
                },
                'name': 'NIDMM_VAL_ACQUISITION_STATUS_NO_ACQUISITION_IN_PROGRESS',
                'value': 4
            }
        ]
    },
    'ApertureTimeUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'Seconds'
                },
                'name': 'NIDMM_VAL_SECONDS',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Powerline Cycles'
                },
                'name': 'NIDMM_VAL_POWER_LINE_CYCLES',
                'value': 1
            }
        ]
    },
    'AutoZero': {
        'values': [
            {
                'documentation': {
                    'description': 'The drivers chooses the AutoZero setting based on the configured function  and resolution.'
                },
                'name': 'NIDMM_VAL_AUTO_ZERO_AUTO',
                'value': -1
            },
            {
                'documentation': {
                    'description': 'Disables AutoZero.'
                },
                'name': 'NIDMM_VAL_AUTO_ZERO_OFF',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'The DMM internally disconnects the input signal following each measurement  and takes a zero reading. It then subtracts the zero reading from the  preceding reading.'
                },
                'name': 'NIDMM_VAL_AUTO_ZERO_ON',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'The DMM internally disconnects the input signal for the first measurement  and takes a zero reading. It then subtracts the zero reading from the first  reading and the following readings.'
                },
                'name': 'NIDMM_VAL_AUTO_ZERO_ONCE',
                'value': 2
            }
        ]
    },
    'CableCompensationType': {
        'values': [
            {
                'documentation': {
                    'description': 'No Cable Compensation'
                },
                'name': 'NIDMM_VAL_CABLE_COMP_NONE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Open Cable Compensation'
                },
                'name': 'NIDMM_VAL_CABLE_COMP_OPEN',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Short Cable Compensation'
                },
                'name': 'NIDMM_VAL_CABLE_COMP_SHORT',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Open and Short Cable Compensation'
                },
                'name': 'NIDMM_VAL_CABLE_COMP_OPEN_AND_SHORT',
                'value': 3
            }
        ]
    },
    'DCNoiseRejection': {
        'values': [
            {
                'documentation': {
                    'description': 'The driver chooses the DC noise rejection setting based on the configured  function and resolution.'
                },
                'name': 'NIDMM_VAL_DCNR_AUTO',
                'value': -1
            },
            {
                'documentation': {
                    'description': 'NI-DMM weighs all samples equally.'
                },
                'name': 'NIDMM_VAL_DCNR_NORMAL',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'NI-DMM weighs the samples taken in the middle of the aperture time more than  samples taken at the beginning and the end of the measurement using a  triangular weighing function.'
                },
                'name': 'NIDMM_VAL_DCNR_SECOND_ORDER',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'NI-DMM weighs the samples taken in the middle of the aperture time more than  samples taken at the beginning and the end of the measurement using a  bell-curve weighing function.'
                },
                'name': 'NIDMM_VAL_DCNR_HIGH_ORDER',
                'value': 2
            }
        ]
    },
    'Function': {
        'values': [
            {
                'documentation': {
                    'description': 'DC Voltage'
                },
                'name': 'NIDMM_VAL_DC_VOLTS',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'AC Voltage'
                },
                'name': 'NIDMM_VAL_AC_VOLTS',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'DC Current'
                },
                'name': 'NIDMM_VAL_DC_CURRENT',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'AC Current'
                },
                'name': 'NIDMM_VAL_AC_CURRENT',
                'value': 4
            },
            {
                'documentation': {
                    'description': '2-Wire Resistance'
                },
                'name': 'NIDMM_VAL_2_WIRE_RES',
                'python_name': 'TWO_WIRE_RES',
                'value': 5
            },
            {
                'documentation': {
                    'description': '4-Wire Resistance'
                },
                'name': 'NIDMM_VAL_4_WIRE_RES',
                'python_name': 'FOUR_WIRE_RES',
                'value': 101
            },
            {
                'documentation': {
                    'description': 'Frequency'
                },
                'name': 'NIDMM_VAL_FREQ',
                'value': 104
            },
            {
                'documentation': {
                    'description': 'Period'
                },
                'name': 'NIDMM_VAL_PERIOD',
                'value': 105
            },
            {
                'documentation': {
                    'description': 'NI 4065, NI 4070/4071/4072, and NI 4080/4081/4182 supported.'
                },
                'name': 'NIDMM_VAL_TEMPERATURE',
                'value': 108
            },
            {
                'documentation': {
                    'description': 'AC Voltage with DC Coupling'
                },
                'name': 'NIDMM_VAL_AC_VOLTS_DC_COUPLED',
                'value': 1001
            },
            {
                'documentation': {
                    'description': 'Diode'
                },
                'name': 'NIDMM_VAL_DIODE',
                'value': 1002
            },
            {
                'documentation': {
                    'description': 'Waveform voltage'
                },
                'name': 'NIDMM_VAL_WAVEFORM_VOLTAGE',
                'value': 1003
            },
            {
                'documentation': {
                    'description': 'Waveform current'
                },
                'name': 'NIDMM_VAL_WAVEFORM_CURRENT',
                'value': 1004
            },
            {
                'documentation': {
                    'description': 'Capacitance'
                },
                'name': 'NIDMM_VAL_CAPACITANCE',
                'value': 1005
            },
            {
                'documentation': {
                    'description': 'Inductance'
                },
                'name': 'NIDMM_VAL_INDUCTANCE',
                'value': 1006
            }
        ]
    },
    'LCCalculationModel': {
        'values': [
            {
                'documentation': {
                    'description': 'NI-DMM chooses the algorithm based on function and range'
                },
                'name': 'NIDMM_VAL_CALC_MODEL_AUTO',
                'value': -1
            },
            {
                'documentation': {
                    'description': 'NI-DMM uses the series impedance model to calculate capacitance and inductance'
                },
                'name': 'NIDMM_VAL_CALC_MODEL_SERIES',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'NI-DMM uses the parallel admittance model to calculate capacitance and inductance'
                },
                'name': 'NIDMM_VAL_CALC_MODEL_PARALLEL',
                'value': 1
            }
        ]
    },
    'MeasurementCompleteDest': {
        'values': [
            {
                'documentation': {
                    'description': 'No Trigger'
                },
                'name': 'NIDMM_VAL_NONE',
                'value': -1
            },
            {
                'documentation': {
                    'description': 'AUX I/O Connector'
                },
                'name': 'NIDMM_VAL_EXTERNAL',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'PXI Trigger Line 0'
                },
                'name': 'NIDMM_VAL_PXI_TRIG0',
                'value': 111
            },
            {
                'documentation': {
                    'description': 'PXI Trigger Line 1'
                },
                'name': 'NIDMM_VAL_PXI_TRIG1',
                'value': 112
            },
            {
                'documentation': {
                    'description': 'PXI Trigger Line 2'
                },
                'name': 'NIDMM_VAL_PXI_TRIG2',
                'value': 113
            },
            {
                'documentation': {
                    'description': 'PXI Trigger Line 3'
                },
                'name': 'NIDMM_VAL_PXI_TRIG3',
                'value': 114
            },
            {
                'documentation': {
                    'description': 'PXI Trigger Line 4'
                },
                'name': 'NIDMM_VAL_PXI_TRIG4',
                'value': 115
            },
            {
                'documentation': {
                    'description': 'PXI Trigger Line 5'
                },
                'name': 'NIDMM_VAL_PXI_TRIG5',
                'value': 116
            },
            {
                'documentation': {
                    'description': 'PXI Trigger Line 6'
                },
                'name': 'NIDMM_VAL_PXI_TRIG6',
                'value': 117
            },
            {
                'documentation': {
                    'description': 'PXI Trigger Line 7'
                },
                'name': 'NIDMM_VAL_PXI_TRIG7',
                'value': 118
            },
            {
                'documentation': {
                    'description': 'Internal Trigger Line of a PXI/SCXI Combination Chassis'
                },
                'name': 'NIDMM_VAL_LBR_TRIG0',
                'value': 1003
            }
        ]
    },
    'MeasurementDestinationSlope': {
        'values': [
            {
                'documentation': {
                    'description': 'Rising Edgs'
                },
                'name': 'NIDMM_VAL_POSITIVE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Falling Edge'
                },
                'name': 'NIDMM_VAL_NEGATIVE',
                'value': 1
            }
        ]
    },
    'OperationMode': {
        'values': [
            {
                'documentation': {
                    'description': 'IviDmm Mode'
                },
                'name': 'NIDMM_VAL_IVIDMM_MODE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Waveform acquisition mode'
                },
                'name': 'NIDMM_VAL_WAVEFORM_MODE',
                'value': 1
            }
        ]
    },
    'RTDType': {
        'values': [
            {
                'documentation': {
                    'description': '\nPerforms Callendar-Van Dusen RTD scaling with the user-specified A, B,\nand C coefficients.\n'
                },
                'name': 'NIDMM_VAL_TEMP_RTD_CUSTOM',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Performs scaling for a Pt 3750 RTD.'
                },
                'name': 'NIDMM_VAL_TEMP_RTD_PT3750',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Performs scaling for a Pt 3851 RTD.'
                },
                'name': 'NIDMM_VAL_TEMP_RTD_PT3851',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Performs scaling for a Pt 3911 RTD.'
                },
                'name': 'NIDMM_VAL_TEMP_RTD_PT3911',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'Performs scaling for a Pt 3916 RTD.'
                },
                'name': 'NIDMM_VAL_TEMP_RTD_PT3916',
                'value': 4
            },
            {
                'documentation': {
                    'description': 'Performs scaling for a Pt 3920 RTD.'
                },
                'name': 'NIDMM_VAL_TEMP_RTD_PT3920',
                'value': 5
            },
            {
                'documentation': {
                    'description': 'Performs scaling for a Pt 3928 RTD.'
                },
                'name': 'NIDMM_VAL_TEMP_RTD_PT3928',
                'value': 6
            }
        ]
    },
    'SampleTrigSlope': {
        'values': [
            {
                'documentation': {
                    'description': 'Rising Edgs'
                },
                'name': 'NIDMM_VAL_POSITIVE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Falling Edge'
                },
                'name': 'NIDMM_VAL_NEGATIVE',
                'value': 1
            }
        ]
    },
    'SampleTrigger': {
        'values': [
            {
                'documentation': {
                    'description': 'No Trigger'
                },
                'name': 'NIDMM_VAL_IMMEDIATE',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'AUX I/O Connector Trigger Line 0'
                },
                'name': 'NIDMM_VAL_EXTERNAL',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Software Trigger'
                },
                'name': 'NIDMM_VAL_SOFTWARE_TRIG',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'Interval Trigger'
                },
                'name': 'NIDMM_VAL_INTERVAL',
                'value': 10
            },
            {
                'documentation': {
                    'description': 'PXI Trigger Line 0'
                },
                'name': 'NIDMM_VAL_PXI_TRIG0',
                'value': 111
            },
            {
                'documentation': {
                    'description': 'PXI Trigger Line 1'
                },
                'name': 'NIDMM_VAL_PXI_TRIG1',
                'value': 112
            },
            {
                'documentation': {
                    'description': 'PXI Trigger Line 2'
                },
                'name': 'NIDMM_VAL_PXI_TRIG2',
                'value': 113
            },
            {
                'documentation': {
                    'description': 'PXI Trigger Line 3'
                },
                'name': 'NIDMM_VAL_PXI_TRIG3',
                'value': 114
            },
            {
                'documentation': {
                    'description': 'PXI Trigger Line 4'
                },
                'name': 'NIDMM_VAL_PXI_TRIG4',
                'value': 115
            },
            {
                'documentation': {
                    'description': 'PXI Trigger Line 5'
                },
                'name': 'NIDMM_VAL_PXI_TRIG5',
                'value': 116
            },
            {
                'documentation': {
                    'description': 'PXI Trigger Line 6'
                },
                'name': 'NIDMM_VAL_PXI_TRIG6',
                'value': 117
            },
            {
                'documentation': {
                    'description': 'PXI Trigger Line 7'
                },
                'name': 'NIDMM_VAL_PXI_TRIG7',
                'value': 118
            },
            {
                'documentation': {
                    'description': 'PXI Star Trigger Line'
                },
                'name': 'NIDMM_VAL_PXI_STAR',
                'value': 131
            },
            {
                'documentation': {
                    'description': 'AUX I/0 Connector Trigger Line 1'
                },
                'name': 'NIDMM_VAL_AUX_TRIG1',
                'value': 1001
            },
            {
                'documentation': {
                    'description': 'Internal Trigger Line of a PXI/SCXI Combination Chassis'
                },
                'name': 'NIDMM_VAL_LBR_TRIG1',
                'value': 1004
            }
        ]
    },
    'ThermistorType': {
        'values': [
            {
                'documentation': {
                    'description': 'Custom'
                },
                'name': 'NIDMM_VAL_TEMP_THERMISTOR_CUSTOM',
                'value': 0
            },
            {
                'documentation': {
                    'description': '44004'
                },
                'name': 'NIDMM_VAL_TEMP_THERMISTOR_44004',
                'python_name': 'TEMP_THERMISTOR_THERMISTOR_44004',
                'value': 1
            },
            {
                'documentation': {
                    'description': '44006'
                },
                'name': 'NIDMM_VAL_TEMP_THERMISTOR_44006',
                'python_name': 'TEMP_THERMISTOR_THERMISTOR_44006',
                'value': 2
            },
            {
                'documentation': {
                    'description': '44007'
                },
                'name': 'NIDMM_VAL_TEMP_THERMISTOR_44007',
                'python_name': 'TEMP_THERMISTOR_THERMISTOR_44007',
                'value': 3
            }
        ]
    },
    'ThermocoupleReferenceJunctionType': {
        'values': [
            {
                'documentation': {
                    'description': '\nThermocouple reference juction is fixed at the user-specified\ntemperature.\n'
                },
                'name': 'NIDMM_VAL_TEMP_REF_JUNC_FIXED',
                'value': 2
            }
        ]
    },
    'ThermocoupleType': {
        'values': [
            {
                'documentation': {
                    'description': 'Thermocouple type B'
                },
                'name': 'NIDMM_VAL_TEMP_TC_B',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Thermocouple type E'
                },
                'name': 'NIDMM_VAL_TEMP_TC_E',
                'value': 4
            },
            {
                'documentation': {
                    'description': 'Thermocouple type J'
                },
                'name': 'NIDMM_VAL_TEMP_TC_J',
                'value': 6
            },
            {
                'documentation': {
                    'description': 'Thermocouple type K'
                },
                'name': 'NIDMM_VAL_TEMP_TC_K',
                'value': 7
            },
            {
                'documentation': {
                    'description': 'Thermocouple type N'
                },
                'name': 'NIDMM_VAL_TEMP_TC_N',
                'value': 8
            },
            {
                'documentation': {
                    'description': 'Thermocouple type R'
                },
                'name': 'NIDMM_VAL_TEMP_TC_R',
                'value': 9
            },
            {
                'documentation': {
                    'description': 'Thermocouple type S'
                },
                'name': 'NIDMM_VAL_TEMP_TC_S',
                'value': 10
            },
            {
                'documentation': {
                    'description': 'Thermocouple type T'
                },
                'name': 'NIDMM_VAL_TEMP_TC_T',
                'value': 11
            }
        ]
    },
    'TransducerType': {
        'values': [
            {
                'documentation': {
                    'description': 'Thermocouple'
                },
                'name': 'NIDMM_VAL_THERMOCOUPLE',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Thermistor'
                },
                'name': 'NIDMM_VAL_THERMISTOR',
                'value': 2
            },
            {
                'documentation': {
                    'description': '2-wire RTD'
                },
                'name': 'NIDMM_VAL_2_WIRE_RTD',
                'python_name': 'TWO_WIRE_RTD',
                'value': 3
            },
            {
                'documentation': {
                    'description': '4-wire RTD'
                },
                'name': 'NIDMM_VAL_4_WIRE_RTD',
                'python_name': 'FOUR_WIRE_RTD',
                'value': 4
            }
        ]
    },
    'TriggerSlope': {
        'values': [
            {
                'documentation': {
                    'description': 'Rising Edgs'
                },
                'name': 'NIDMM_VAL_POSITIVE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Falling Edge'
                },
                'name': 'NIDMM_VAL_NEGATIVE',
                'value': 1
            }
        ]
    },
    'TriggerSource': {
        'values': [
            {
                'documentation': {
                    'description': 'No Trigger'
                },
                'name': 'NIDMM_VAL_IMMEDIATE',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'AUX I/O Connector Trigger Line 0'
                },
                'name': 'NIDMM_VAL_EXTERNAL',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Software Trigger'
                },
                'name': 'NIDMM_VAL_SOFTWARE_TRIG',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'PXI Trigger Line 0'
                },
                'name': 'NIDMM_VAL_PXI_TRIG0',
                'value': 111
            },
            {
                'documentation': {
                    'description': 'PXI Trigger Line 1'
                },
                'name': 'NIDMM_VAL_PXI_TRIG1',
                'value': 112
            },
            {
                'documentation': {
                    'description': 'PXI Trigger Line 2'
                },
                'name': 'NIDMM_VAL_PXI_TRIG2',
                'value': 113
            },
            {
                'documentation': {
                    'description': 'PXI Trigger Line 3'
                },
                'name': 'NIDMM_VAL_PXI_TRIG3',
                'value': 114
            },
            {
                'documentation': {
                    'description': 'PXI Trigger Line 4'
                },
                'name': 'NIDMM_VAL_PXI_TRIG4',
                'value': 115
            },
            {
                'documentation': {
                    'description': 'PXI Trigger Line 5'
                },
                'name': 'NIDMM_VAL_PXI_TRIG5',
                'value': 116
            },
            {
                'documentation': {
                    'description': 'PXI Trigger Line 6'
                },
                'name': 'NIDMM_VAL_PXI_TRIG6',
                'value': 117
            },
            {
                'documentation': {
                    'description': 'PXI Trigger Line 7'
                },
                'name': 'NIDMM_VAL_PXI_TRIG7',
                'value': 118
            },
            {
                'documentation': {
                    'description': 'PXI Star Trigger Line'
                },
                'name': 'NIDMM_VAL_PXI_STAR',
                'value': 131
            },
            {
                'documentation': {
                    'description': 'AUX I/O Connector Trigger Line 1'
                },
                'name': 'NIDMM_VAL_AUX_TRIG1',
                'value': 1001
            },
            {
                'documentation': {
                    'description': 'Internal Trigger Line of a PXI/SCXI Combination Chassis'
                },
                'name': 'NIDMM_VAL_LBR_TRIG1',
                'value': 1004
            }
        ]
    },
    'WaveformCoupling': {
        'values': [
            {
                'documentation': {
                    'description': 'AC Coupled'
                },
                'name': 'NIDMM_VAL_WAVEFORM_COUPLING_AC',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'DC Coupled'
                },
                'name': 'NIDMM_VAL_WAVEFORM_COUPLING_DC',
                'value': 1
            }
        ]
    }
}
