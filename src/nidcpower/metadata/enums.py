# -*- coding: utf-8 -*-
# This file is generated from NI-DCPower API metadata version 23.0.0d225
enums = {
    'ApertureTimeAutoMode': {
        'values': [
            {
                'documentation': {
                    'description': 'Disables automatic aperture time scaling. The NIDCPOWER_ATTR_APERTURE_TIME attribute specifies the aperture time for all ranges.'
                },
                'name': 'NIDCPOWER_VAL_APERTURE_TIME_AUTO_MODE_OFF',
                'value': 1135
            },
            {
                'documentation': {
                    'description': 'Prioritizes measurement speed over measurement accuracy by quickly scaling down aperture time in larger current ranges. The NIDCPOWER_ATTR_APERTURE_TIME attribute specifies the aperture time for the minimum range.'
                },
                'name': 'NIDCPOWER_VAL_APERTURE_TIME_AUTO_MODE_SHORT',
                'value': 1136
            },
            {
                'documentation': {
                    'description': 'Balances measurement accuracy and speed by scaling down aperture time in larger current ranges. The NIDCPOWER_ATTR_APERTURE_TIME attribute specifies the aperture time for the minimum range.'
                },
                'name': 'NIDCPOWER_VAL_APERTURE_TIME_AUTO_MODE_NORMAL',
                'value': 1137
            },
            {
                'documentation': {
                    'description': 'Prioritizes accuracy while still decreasing measurement time by slowly scaling down aperture time in larger current ranges. The NIDCPOWER_ATTR_APERTURE_TIME attribute specifies the aperture time for the minimum range.'
                },
                'name': 'NIDCPOWER_VAL_APERTURE_TIME_AUTO_MODE_LONG',
                'value': 1138
            }
        ]
    },
    'ApertureTimeUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies aperture time in seconds.'
                },
                'name': 'NIDCPOWER_VAL_SECONDS',
                'value': 1028
            },
            {
                'documentation': {
                    'description': 'Specifies aperture time in power line cycles (PLCs).'
                },
                'name': 'NIDCPOWER_VAL_POWER_LINE_CYCLES',
                'value': 1029
            }
        ]
    },
    'AutoZero': {
        'values': [
            {
                'documentation': {
                    'description': 'Disables auto zero.'
                },
                'name': 'NIDCPOWER_VAL_OFF',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Makes zero conversions for every measurement.'
                },
                'name': 'NIDCPOWER_VAL_ON',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Makes zero conversions following the first measurement after initiating the device.  The device uses these zero conversions for the preceding measurement and future  measurements until the device is reinitiated.'
                },
                'name': 'NIDCPOWER_VAL_ONCE',
                'value': 1024
            }
        ]
    },
    'AutorangeApertureTimeMode': {
        'values': [
            {
                'documentation': {
                    'description': 'NI-DCPower optimizes the aperture time for the autorange algorithm based on the module range.'
                },
                'name': 'NIDCPOWER_VAL_APERTURE_TIME_AUTO',
                'value': 1110
            },
            {
                'documentation': {
                    'description': 'The user specifies a minimum aperture time for the algorithm using the NIDCPOWER_ATTR_AUTORANGE_MINIMUM_APERTURE_TIME property and the corresponding NIDCPOWER_ATTR_AUTORANGE_MINIMUM_APERTURE_TIME_UNITS property.'
                },
                'name': 'NIDCPOWER_VAL_APERTURE_TIME_CUSTOM',
                'value': 1111
            }
        ]
    },
    'AutorangeBehavior': {
        'values': [
            {
                'documentation': {
                    'description': 'Go to limit range then range down as needed until measured value is within thresholds.'
                },
                'name': 'NIDCPOWER_VAL_RANGE_UP_TO_LIMIT_THEN_DOWN',
                'value': 1107
            },
            {
                'documentation': {
                    'description': 'go up one range when the upper threshold is reached.'
                },
                'name': 'NIDCPOWER_VAL_RANGE_UP',
                'value': 1108
            },
            {
                'documentation': {
                    'description': 'go up or down one range when the upper/lower threshold is reached.'
                },
                'name': 'NIDCPOWER_VAL_RANGE_UP_AND_DOWN',
                'value': 1109
            }
        ]
    },
    'AutorangeThresholdMode': {
        'values': [
            {
                'documentation': {
                    'description': 'Thresholds are selected based on a balance between accuracy and hysteresis.'
                },
                'name': 'NIDCPOWER_VAL_THRESHOLD_MODE_NORMAL',
                'value': 1112
            },
            {
                'documentation': {
                    'description': 'Optimized for faster changes in the measured signal. Thresholds are configured to be a smaller percentage of the range.'
                },
                'name': 'NIDCPOWER_VAL_THRESHOLD_MODE_FAST_STEP',
                'value': 1113
            },
            {
                'documentation': {
                    'description': 'Optimized for noisy signals to minimize frequent and unpredictable range changes. Thresholds are configured to be a larger percentage of the range.'
                },
                'name': 'NIDCPOWER_VAL_THRESHOLD_MODE_HIGH_HYSTERESIS',
                'value': 1114
            },
            {
                'documentation': {
                    'description': 'Optimized for noisy signals to minimize frequent and unpredictable range changes. Thresholds are configured to be a medium percentage of the range.'
                },
                'name': 'NIDCPOWER_VAL_THRESHOLD_MODE_MEDIUM_HYSTERESIS',
                'value': 1115
            },
            {
                'documentation': {
                    'description': 'Attempt to maintain the active range. Thresholds will favor the active range.'
                },
                'name': 'NIDCPOWER_VAL_THRESHOLD_MODE_HOLD',
                'value': 1116
            }
        ]
    },
    'CableLength': {
        'values': [
            {
                'documentation': {
                    'description': 'Uses predefined cable compensation data for a 0m cable (direct connection).'
                },
                'name': 'NIDCPOWER_VAL_ZERO_M',
                'value': 1121
            },
            {
                'documentation': {
                    'description': 'Uses predefined cable compensation data for an NI standard 1m coaxial cable.'
                },
                'name': 'NIDCPOWER_VAL_NI_STANDARD_1M',
                'value': 1122
            },
            {
                'documentation': {
                    'description': 'Uses predefined cable compensation data for an NI standard 2m coaxial cable.'
                },
                'name': 'NIDCPOWER_VAL_NI_STANDARD_2M',
                'value': 1123
            },
            {
                'documentation': {
                    'description': 'Uses predefined cable compensation data for an NI standard 4m coaxial cable.'
                },
                'name': 'NIDCPOWER_VAL_NI_STANDARD_4M',
                'value': 1124
            },
            {
                'documentation': {
                    'description': 'Uses previously generated custom cable compensation data from onboard storage. Only the most recently performed compensation data for each custom cable compensation type (open, short) is stored.'
                },
                'name': 'NIDCPOWER_VAL_CUSTOM_ONBOARD_STORAGE',
                'value': 1125
            },
            {
                'documentation': {
                    'description': 'Uses the custom cable compensation data supplied to niDCPower_ConfigureLCRCustomCableCompensation. Use this option to manage multiple sets of custom cable compensation data.'
                },
                'name': 'NIDCPOWER_VAL_CUSTOM_AS_CONFIGURED',
                'value': 1126
            },
            {
                'documentation': {
                    'description': 'Uses predefined cable compensation data for an NI standard 1m triaxial cable.'
                },
                'name': 'NIDCPOWER_VAL_NI_STANDARD_TRIAXIAL_1M',
                'value': 1139
            },
            {
                'documentation': {
                    'description': 'Uses predefined cable compensation data for an NI standard 2m triaxial cable.'
                },
                'name': 'NIDCPOWER_VAL_NI_STANDARD_TRIAXIAL_2M',
                'value': 1140
            },
            {
                'documentation': {
                    'description': 'Uses predefined cable compensation data for an NI standard 4m triaxial cable.'
                },
                'name': 'NIDCPOWER_VAL_NI_STANDARD_TRIAXIAL_4M',
                'value': 1141
            }
        ]
    },
    'ComplianceLimitSymmetry': {
        'values': [
            {
                'documentation': {
                    'description': 'Compliance limits are specified symmetrically about 0.'
                },
                'name': 'NIDCPOWER_VAL_SYMMETRIC',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Compliance limits can be specified asymmetrically with respect to 0.'
                },
                'name': 'NIDCPOWER_VAL_ASYMMETRIC',
                'value': 1
            }
        ]
    },
    'CurrentLimitBehavior': {
        'values': [
            {
                'documentation': {
                    'description': 'The channel acts to restrict the output current to the value of the Current Limit property when the actual output on the channel reaches or exceeds that value.'
                },
                'name': 'NIDCPOWER_VAL_CURRENT_REGULATE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'The channel disables the output when the actual output current on the channel reaches or exceeds the value of the Current Limit property.'
                },
                'name': 'NIDCPOWER_VAL_CURRENT_TRIP',
                'value': 1
            }
        ]
    },
    'DCNoiseRejection': {
        'values': [
            {
                'documentation': {
                    'description': 'Second-order rejection of DC noise.'
                },
                'name': 'NIDCPOWER_VAL_DC_NOISE_REJECTION_SECOND_ORDER',
                'value': 1043
            },
            {
                'documentation': {
                    'description': 'Normal rejection of DC noise.'
                },
                'name': 'NIDCPOWER_VAL_DC_NOISE_REJECTION_NORMAL',
                'value': 1044
            }
        ]
    },
    'DigitalEdge': {
        'values': [
            {
                'documentation': {
                    'description': 'Asserts the trigger on the rising edge of the digital signal.'
                },
                'name': 'NIDCPOWER_VAL_RISING',
                'value': 1016
            },
            {
                'documentation': {
                    'description': 'Asserts the trigger on the falling edge of the digital signal.'
                },
                'name': 'NIDCPOWER_VAL_FALLING',
                'value': 1017
            }
        ]
    },
    'Event': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies the Source Complete event.'
                },
                'name': 'NIDCPOWER_VAL_SOURCE_COMPLETE_EVENT',
                'python_name': 'NIDCPOWER_VAL_SOURCE_COMPLETE',
                'value': 1030
            },
            {
                'documentation': {
                    'description': 'Specifies the Measure Complete event.'
                },
                'name': 'NIDCPOWER_VAL_MEASURE_COMPLETE_EVENT',
                'python_name': 'NIDCPOWER_VAL_MEASURE_COMPLETE',
                'value': 1031
            },
            {
                'documentation': {
                    'description': 'Specifies the Sequence Iteration Complete event.'
                },
                'name': 'NIDCPOWER_VAL_SEQUENCE_ITERATION_COMPLETE_EVENT',
                'python_name': 'NIDCPOWER_VAL_SEQUENCE_ITERATION_COMPLETE',
                'value': 1032
            },
            {
                'documentation': {
                    'description': 'Specifies the Sequence Engine Done event.'
                },
                'name': 'NIDCPOWER_VAL_SEQUENCE_ENGINE_DONE_EVENT',
                'python_name': 'NIDCPOWER_VAL_SEQUENCE_ENGINE_DONE',
                'value': 1033
            },
            {
                'documentation': {
                    'description': 'Specifies the Pulse Complete event.'
                },
                'name': 'NIDCPOWER_VAL_PULSE_COMPLETE_EVENT',
                'python_name': 'NIDCPOWER_VAL_PULSE_COMPLETE',
                'value': 1051
            },
            {
                'documentation': {
                    'description': 'Specifies the Ready for Pulse Trigger event.'
                },
                'name': 'NIDCPOWER_VAL_READY_FOR_PULSE_TRIGGER_EVENT',
                'python_name': 'NIDCPOWER_VAL_READY_FOR_PULSE_TRIGGER',
                'value': 1052
            }
        ]
    },
    'ExportSignal': {
        'values': [
            {
                'documentation': {
                    'description': 'Exports the Source Complete event.'
                },
                'name': 'NIDCPOWER_VAL_SOURCE_COMPLETE_EVENT',
                'value': 1030
            },
            {
                'documentation': {
                    'description': 'Exports the Measure Complete event.'
                },
                'name': 'NIDCPOWER_VAL_MEASURE_COMPLETE_EVENT',
                'value': 1031
            },
            {
                'documentation': {
                    'description': 'Exports the Sequence Iteration Complete event.'
                },
                'name': 'NIDCPOWER_VAL_SEQUENCE_ITERATION_COMPLETE_EVENT',
                'value': 1032
            },
            {
                'documentation': {
                    'description': 'Exports the Sequence Engine Done event.'
                },
                'name': 'NIDCPOWER_VAL_SEQUENCE_ENGINE_DONE_EVENT',
                'value': 1033
            },
            {
                'documentation': {
                    'description': 'Exports the Pulse Complete event.'
                },
                'name': 'NIDCPOWER_VAL_PULSE_COMPLETE_EVENT',
                'value': 1051
            },
            {
                'documentation': {
                    'description': 'Exports the Ready Pulse Trigger event.'
                },
                'name': 'NIDCPOWER_VAL_READY_FOR_PULSE_TRIGGER_EVENT',
                'value': 1052
            },
            {
                'documentation': {
                    'description': 'Exports the Start trigger.'
                },
                'name': 'NIDCPOWER_VAL_START_TRIGGER',
                'value': 1034
            },
            {
                'documentation': {
                    'description': 'Exports the Source trigger.'
                },
                'name': 'NIDCPOWER_VAL_SOURCE_TRIGGER',
                'value': 1035
            },
            {
                'documentation': {
                    'description': 'Exports the Measure trigger.'
                },
                'name': 'NIDCPOWER_VAL_MEASURE_TRIGGER',
                'value': 1036
            },
            {
                'documentation': {
                    'description': 'Exports the Sequence Advance trigger.'
                },
                'name': 'NIDCPOWER_VAL_SEQUENCE_ADVANCE_TRIGGER',
                'value': 1037
            },
            {
                'documentation': {
                    'description': 'Exports the Pulse trigger.'
                },
                'name': 'NIDCPOWER_VAL_PULSE_TRIGGER',
                'value': 1053
            },
            {
                'documentation': {
                    'description': 'Exports the Shutdown trigger.'
                },
                'name': 'NIDCPOWER_VAL_SHUTDOWN_TRIGGER',
                'value': 1118
            }
        ]
    },
    'InstrumentMode': {
        'values': [
            {
                'documentation': {
                    'description': 'The channel operates as an SMU/power supply.'
                },
                'name': 'NIDCPOWER_VAL_SMU_PS',
                'value': 1061
            },
            {
                'documentation': {
                    'description': 'The channel operates as an LCR meter.'
                },
                'name': 'NIDCPOWER_VAL_LCR',
                'value': 1062
            }
        ]
    },
    'IsolationState': {
        'codegen_method': 'private',
        'converted_value_to_enum_function_name': 'convert_to_isolation_state_enum',
        'enum_to_converted_value_function_name': 'convert_from_isolation_state_enum',
        'values': [
            {
                'converts_to_value': True,
                'documentation': {
                    'description': 'The channel is disconnected from chassis ground.'
                },
                'name': 'NIDCPOWER_VAL_ISOLATED',
                'value': 1128
            },
            {
                'converts_to_value': False,
                'documentation': {
                    'description': 'The channel is connected to chassis ground.'
                },
                'name': 'NIDCPOWER_VAL_NON_ISOLATED',
                'value': 1129
            }
        ]
    },
    'LCRCompensationType': {
        'values': [
            {
                'documentation': {
                    'description': 'Open LCR compensation.'
                },
                'name': 'NIDCPOWER_VAL_OPEN_COMPENSATION',
                'value': 1130
            },
            {
                'documentation': {
                    'description': 'Short LCR compensation.'
                },
                'name': 'NIDCPOWER_VAL_SHORT_COMPENSATION',
                'value': 1131
            },
            {
                'documentation': {
                    'description': 'Load LCR compensation.'
                },
                'name': 'NIDCPOWER_VAL_LOAD_COMPENSATION',
                'value': 1132
            },
            {
                'documentation': {
                    'description': 'Open custom cable compensation.'
                },
                'name': 'NIDCPOWER_VAL_OPEN_CUSTOM_CABLE_COMPENSATION',
                'value': 1133
            },
            {
                'documentation': {
                    'description': 'Short custom cable compensation.'
                },
                'name': 'NIDCPOWER_VAL_SHORT_CUSTOM_CABLE_COMPENSATION',
                'value': 1134
            }
        ]
    },
    'LCRDCBiasSource': {
        'values': [
            {
                'documentation': {
                    'description': 'Disables DC bias in LCR mode.'
                },
                'name': 'NIDCPOWER_VAL_DC_BIAS_OFF',
                'value': 1065
            },
            {
                'documentation': {
                    'description': 'Applies a constant voltage bias, as defined by the NIDCPOWER_ATTR_LCR_DC_BIAS_VOLTAGE_LEVEL property.'
                },
                'name': 'NIDCPOWER_VAL_DC_BIAS_VOLTAGE',
                'value': 1066
            },
            {
                'documentation': {
                    'description': 'Applies a constant current bias, as defined by the NIDCPOWER_ATTR_LCR_DC_BIAS_CURRENT_LEVEL property.'
                },
                'name': 'NIDCPOWER_VAL_DC_BIAS_CURRENT',
                'value': 1067
            }
        ]
    },
    'LCRImpedanceAutoRange': {
        'codegen_method': 'private',
        'converted_value_to_enum_function_name': 'convert_to_lcr_impedance_auto_range_enum',
        'enum_to_converted_value_function_name': 'convert_from_lcr_impedance_auto_range_enum',
        'values': [
            {
                'converts_to_value': False,
                'name': 'NIDCPOWER_VAL_AUTO_RANGE_OFF',
                'value': 1068
            },
            {
                'converts_to_value': True,
                'name': 'NIDCPOWER_VAL_AUTO_RANGE_ON',
                'value': 1070
            }
        ]
    },
    'LCRImpedanceRangeSource': {
        'values': [
            {
                'documentation': {
                    'description': 'Uses the impedance range you specify with the NIDCPOWER_ATTR_LCR_IMPEDANCE_RANGE property.'
                },
                'name': 'NIDCPOWER_VAL_LCR_IMPEDANCE_RANGE',
                'value': 1142
            },
            {
                'documentation': {
                    'description': 'Computes the impedance range to select based on the values you supply to the NIDCPOWER_ATTR_LCR_LOAD_RESISTANCE, NIDCPOWER_ATTR_LCR_LOAD_INDUCTANCE, and NIDCPOWER_ATTR_LCR_LOAD_CAPACITANCE properties. NI-DCPower uses a series model of load resistance, load inductance, and load capacitance to compute the impedance range.'
                },
                'name': 'NIDCPOWER_VAL_LCR_LOAD_CONFIGURATION',
                'value': 1143
            }
        ]
    },
    'LCRMeasurementTime': {
        'values': [
            {
                'documentation': {
                    'description': 'Uses a short aperture time for LCR measurements.'
                },
                'name': 'NIDCPOWER_VAL_MEASUREMENT_TIME_SHORT',
                'value': 1071
            },
            {
                'documentation': {
                    'description': 'Uses a medium aperture time for LCR measurements.'
                },
                'name': 'NIDCPOWER_VAL_MEASUREMENT_TIME_MEDIUM',
                'value': 1072
            },
            {
                'documentation': {
                    'description': 'Uses a long aperture time for LCR measurements.'
                },
                'name': 'NIDCPOWER_VAL_MEASUREMENT_TIME_LONG',
                'value': 1073
            },
            {
                'documentation': {
                    'description': 'Uses a custom aperture time for LCR measurements as specified by the NIDCPOWER_ATTR_LCR_CUSTOM_MEASUREMENT_TIME property.'
                },
                'name': 'NIDCPOWER_VAL_MEASUREMENT_TIME_CUSTOM',
                'value': 1117
            }
        ]
    },
    'LCROpenShortLoadCompensationDataSource': {
        'values': [
            {
                'documentation': {
                    'description': 'Uses previously generated LCR compensation data. Only the most recently performed compensation data for each LCR compensation type (open, short, and load) is stored.'
                },
                'name': 'NIDCPOWER_VAL_ONBOARD_STORAGE',
                'value': 1074
            },
            {
                'documentation': {
                    'description': 'Uses the LCR compensation data represented by the relevant LCR compensation attributes as generated by niDCPower_PerformLCROpenCompensation, niDCPower_PerformLCRShortCompensation, and niDCPower_PerformLCRLoadCompensation. Use this option to manage multiple sets of LCR compensation data. This option applies compensation data from the following attributes: NIDCPOWER_ATTR_LCR_OPEN_CONDUCTANCE, NIDCPOWER_ATTR_LCR_OPEN_SUSCEPTANCE, NIDCPOWER_ATTR_LCR_SHORT_RESISTANCE, NIDCPOWER_ATTR_LCR_SHORT_REACTANCE, NIDCPOWER_ATTR_LCR_MEASURED_LOAD_RESISTANCE, NIDCPOWER_ATTR_LCR_MEASURED_LOAD_REACTANCE, NIDCPOWER_ATTR_LCR_ACTUAL_LOAD_RESISTANCE, NIDCPOWER_ATTR_LCR_ACTUAL_LOAD_REACTANCE.'
                },
                'name': 'NIDCPOWER_VAL_AS_DEFINED',
                'value': 1075
            }
        ]
    },
    'LCRReferenceValueType': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'The actual impedance, comprising real resistance and imaginary reactance, of your DUT. Supply resistance, in ohms, to reference value A; supply reactance, in ohms, to reference value B.'
                },
                'name': 'NIDCPOWER_VAL_IMPEDANCE',
                'value': 1076
            },
            {
                'documentation': {
                    'description': 'The ideal capacitance of your DUT. Supply capacitance, in farads, to reference value A.'
                },
                'name': 'NIDCPOWER_VAL_IDEAL_CAPACITANCE',
                'value': 1077
            },
            {
                'documentation': {
                    'description': 'The ideal inductance of your DUT. Supply inductance, in henrys, to reference value A.'
                },
                'name': 'NIDCPOWER_VAL_IDEAL_INDUCTANCE',
                'value': 1078
            },
            {
                'documentation': {
                    'description': 'The ideal resistance of your DUT. Supply resistance, in ohms, to reference value A.'
                },
                'name': 'NIDCPOWER_VAL_IDEAL_RESISTANCE',
                'value': 1079
            }
        ]
    },
    'LCRSourceDelayMode': {
        'values': [
            {
                'documentation': {
                    'description': 'NI-DCPower automatically applies source delay of sufficient duration to account for settling time.'
                },
                'name': 'NIDCPOWER_VAL_LCR_SOURCE_DELAY_MODE_AUTOMATIC',
                'value': 1144
            },
            {
                'documentation': {
                    'description': 'NI-DCPower applies the source delay that you set manually with NIDCPOWER_ATTR_SOURCE_DELAY. You can use this option to set a shorter delay to reduce measurement time at the possible expense of measurement accuracy.'
                },
                'name': 'NIDCPOWER_VAL_LCR_SOURCE_DELAY_MODE_MANUAL',
                'value': 1145
            }
        ]
    },
    'LCRStimulusFunction': {
        'values': [
            {
                'documentation': {
                    'description': 'Applies an AC voltage for LCR stimulus.'
                },
                'name': 'NIDCPOWER_VAL_AC_VOLTAGE',
                'value': 1063
            },
            {
                'documentation': {
                    'description': 'Applies an AC current for LCR stimulus.'
                },
                'name': 'NIDCPOWER_VAL_AC_CURRENT',
                'value': 1064
            }
        ]
    },
    'MeasureWhen': {
        'values': [
            {
                'documentation': {
                    'description': 'Acquires a measurement after each Source Complete event completes.'
                },
                'name': 'NIDCPOWER_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE',
                'value': 1025
            },
            {
                'documentation': {
                    'description': 'Acquires a measurement when the niDCPower_Measure function or niDCPower_MeasureMultiple function is called.'
                },
                'name': 'NIDCPOWER_VAL_ON_DEMAND',
                'value': 1026
            },
            {
                'documentation': {
                    'description': 'Acquires a measurement when a Measure trigger is received.'
                },
                'name': 'NIDCPOWER_VAL_ON_MEASURE_TRIGGER',
                'value': 1027
            }
        ]
    },
    'MeasurementTypes': {
        'values': [
            {
                'documentation': {
                    'description': 'The device measures current.'
                },
                'name': 'NIDCPOWER_VAL_MEASURE_CURRENT',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'The device measures voltage.'
                },
                'name': 'NIDCPOWER_VAL_MEASURE_VOLTAGE',
                'value': 1
            }
        ]
    },
    'OutputCapacitance': {
        'values': [
            {
                'documentation': {
                    'description': 'Output Capacitance is low.'
                },
                'name': 'NIDCPOWER_VAL_LOW',
                'value': 1010
            },
            {
                'documentation': {
                    'description': 'Output Capacitance is high.'
                },
                'name': 'NIDCPOWER_VAL_HIGH',
                'value': 1011
            }
        ]
    },
    'OutputCutoffReason': {
        'values': [
            {
                'documentation': {
                    'description': 'Queries any output cutoff condition; clears all output cutoff conditions.'
                },
                'name': 'NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_ALL',
                'value': -1
            },
            {
                'documentation': {
                    'description': 'Queries or clears cutoff conditions when the output exceeded the high cutoff limit for voltage output.'
                },
                'name': 'NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_VOLTAGE_OUTPUT_HIGH',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Queries or clears cutoff conditions when the output fell below the low cutoff limit for voltage output.'
                },
                'name': 'NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_VOLTAGE_OUTPUT_LOW',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Queries or clears cutoff conditions when the measured current exceeded the high cutoff limit for current output.'
                },
                'name': 'NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_CURRENT_MEASURE_HIGH',
                'value': 4
            },
            {
                'documentation': {
                    'description': 'Queries or clears cutoff conditions when the measured current fell below the low cutoff limit for current output.'
                },
                'name': 'NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_CURRENT_MEASURE_LOW',
                'value': 8
            },
            {
                'documentation': {
                    'description': 'Queries or clears cutoff conditions when the voltage slew rate increased beyond the positive change cutoff for voltage output.'
                },
                'name': 'NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_VOLTAGE_CHANGE_HIGH',
                'value': 16
            },
            {
                'documentation': {
                    'description': 'Queries or clears cutoff conditions when the voltage slew rate decreased beyond the negative change cutoff for voltage output.'
                },
                'name': 'NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_VOLTAGE_CHANGE_LOW',
                'value': 32
            },
            {
                'documentation': {
                    'description': 'Queries or clears cutoff conditions when the current slew rate increased beyond the positive change cutoff for current output.'
                },
                'name': 'NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_CURRENT_CHANGE_HIGH',
                'value': 64
            },
            {
                'documentation': {
                    'description': 'Queries or clears cutoff conditions when the current slew rate decreased beyond the negative change cutoff for current output.'
                },
                'name': 'NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_CURRENT_CHANGE_LOW',
                'value': 128
            }
        ]
    },
    'OutputFunction': {
        'values': [
            {
                'documentation': {
                    'description': 'Sets the output function to DC voltage.'
                },
                'name': 'NIDCPOWER_VAL_DC_VOLTAGE',
                'value': 1006
            },
            {
                'documentation': {
                    'description': 'Sets the output function to DC current.'
                },
                'name': 'NIDCPOWER_VAL_DC_CURRENT',
                'value': 1007
            },
            {
                'documentation': {
                    'description': 'Sets the output function to pulse voltage.'
                },
                'name': 'NIDCPOWER_VAL_PULSE_VOLTAGE',
                'value': 1049
            },
            {
                'documentation': {
                    'description': 'Sets the output function to pulse current.'
                },
                'name': 'NIDCPOWER_VAL_PULSE_CURRENT',
                'value': 1050
            }
        ]
    },
    'OutputStates': {
        'values': [
            {
                'documentation': {
                    'description': 'The channel maintains a constant voltage by adjusting the current.'
                },
                'name': 'NIDCPOWER_VAL_OUTPUT_CONSTANT_VOLTAGE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'The channel maintains a constant current by adjusting the voltage.'
                },
                'name': 'NIDCPOWER_VAL_OUTPUT_CONSTANT_CURRENT',
                'value': 1
            }
        ]
    },
    'Polarity': {
        'values': [
            {
                'documentation': {
                    'description': 'A high pulse occurs when the event is generated.  The exported signal is low level both before and after the event is generated.'
                },
                'name': 'NIDCPOWER_VAL_ACTIVE_HIGH',
                'value': 1018
            },
            {
                'documentation': {
                    'description': 'A low pulse occurs when the event is generated.  The exported signal is high level both before and after the event is generated.'
                },
                'name': 'NIDCPOWER_VAL_ACTIVE_LOW',
                'value': 1019
            }
        ]
    },
    'PowerAllocationMode': {
        'values': [
            {
                'documentation': {
                    'description': 'The device attempts to source, on each active channel, the power that the present source configuration requires; NI-DCPower does not perform a sourcing power check. If the required power is greater than the maximum sourcing power, the device attempts to source the required amount and may shut down to prevent damage.'
                },
                'name': 'NIDCPOWER_VAL_POWER_ALLOCATION_MODE_DISABLED',
                'value': 1058
            },
            {
                'documentation': {
                    'description': 'The device attempts to source, on each active channel, the power that the present source configuration requires; NI-DCPower performs a sourcing power check. If the required power is greater than the maximum sourcing power, the device does not exceed the maximum power, and NI-DCPower returns an error.'
                },
                'name': 'NIDCPOWER_VAL_POWER_ALLOCATION_MODE_AUTOMATIC',
                'value': 1059
            },
            {
                'documentation': {
                    'description': 'The device attempts to source, on each active channel, the power you request with the NIDCPOWER_ATTR_REQUESTED_POWER_ALLOCATION attribute; NI-DCPower performs a sourcing power check. If the requested power is either less than the required power for the present source configuration or greater than the maximum sourcing power, the device does not exceed the requested or allowed power, respectively, and NI-DCPower returns an error.'
                },
                'name': 'NIDCPOWER_VAL_POWER_ALLOCATION_MODE_MANUAL',
                'value': 1060
            }
        ]
    },
    'PowerSource': {
        'values': [
            {
                'documentation': {
                    'description': 'Uses the PXI chassis power source.'
                },
                'name': 'NIDCPOWER_VAL_INTERNAL',
                'value': 1003
            },
            {
                'documentation': {
                    'description': 'Uses the auxiliary power source connected to the device.'
                },
                'name': 'NIDCPOWER_VAL_AUXILIARY',
                'value': 1004
            },
            {
                'documentation': {
                    'description': 'Uses the auxiliary power source if it is available; otherwise uses the PXI chassis power source.'
                },
                'name': 'NIDCPOWER_VAL_AUTOMATIC',
                'value': 1005
            }
        ]
    },
    'PowerSourceInUse': {
        'values': [
            {
                'documentation': {
                    'description': 'Uses the PXI chassis power source.'
                },
                'name': 'NIDCPOWER_VAL_INTERNAL',
                'value': 1003
            },
            {
                'documentation': {
                    'description': 'Uses the auxiliary power source connected to the device. Only the NI PXI-4110,  NI PXIe-4112, NI PXIe-4113, and NI PXI-4130 support this value. This is the only supported value  for the NI PXIe-4112 and NI PXIe-4113.'
                },
                'name': 'NIDCPOWER_VAL_AUXILIARY',
                'value': 1004
            }
        ]
    },
    'SelfCalibrationPersistence': {
        'values': [
            {
                'documentation': {
                    'description': 'Keep new self calibration values in memory only.'
                },
                'name': 'NIDCPOWER_VAL_KEEP_IN_MEMORY',
                'value': 1045
            },
            {
                'documentation': {
                    'description': 'Write new self calibration values to hardware.'
                },
                'name': 'NIDCPOWER_VAL_WRITE_TO_EEPROM',
                'value': 1046
            }
        ]
    },
    'SendSoftwareEdgeTriggerType': {
        'values': [
            {
                'documentation': {
                    'description': 'Asserts the Start trigger.'
                },
                'name': 'NIDCPOWER_VAL_START_TRIGGER',
                'python_name': 'NIDCPOWER_VAL_START',
                'value': 1034
            },
            {
                'documentation': {
                    'description': 'Asserts the Source trigger.'
                },
                'name': 'NIDCPOWER_VAL_SOURCE_TRIGGER',
                'python_name': 'NIDCPOWER_VAL_SOURCE',
                'value': 1035
            },
            {
                'documentation': {
                    'description': 'Asserts the Measure trigger.'
                },
                'name': 'NIDCPOWER_VAL_MEASURE_TRIGGER',
                'python_name': 'NIDCPOWER_VAL_MEASURE',
                'value': 1036
            },
            {
                'documentation': {
                    'description': 'Asserts the Sequence Advance trigger.'
                },
                'name': 'NIDCPOWER_VAL_SEQUENCE_ADVANCE_TRIGGER',
                'python_name': 'NIDCPOWER_VAL_SEQUENCE_ADVANCE',
                'value': 1037
            },
            {
                'documentation': {
                    'description': 'Asserts the Pulse trigger.'
                },
                'name': 'NIDCPOWER_VAL_PULSE_TRIGGER',
                'python_name': 'NIDCPOWER_VAL_PULSE',
                'value': 1053
            },
            {
                'documentation': {
                    'description': 'Asserts the Shutdown trigger.'
                },
                'name': 'NIDCPOWER_VAL_SHUTDOWN_TRIGGER',
                'python_name': 'NIDCPOWER_VAL_SHUTDOWN',
                'value': 1118
            }
        ]
    },
    'Sense': {
        'values': [
            {
                'documentation': {
                    'description': 'Local sensing is selected.'
                },
                'name': 'NIDCPOWER_VAL_LOCAL',
                'value': 1008
            },
            {
                'documentation': {
                    'description': 'Remote sensing is selected.'
                },
                'name': 'NIDCPOWER_VAL_REMOTE',
                'value': 1009
            }
        ]
    },
    'SessionState': {
        'values': [
            {
                'name': 'NIDCPOWER_VAL_IDLE',
                'value': 1
            },
            {
                'name': 'NIDCPOWER_VAL_VERIFIED',
                'value': 2
            },
            {
                'name': 'NIDCPOWER_VAL_COMMITTED',
                'value': 4
            },
            {
                'name': 'NIDCPOWER_VAL_RUNNING',
                'value': 8
            }
        ]
    },
    'SourceMode': {
        'values': [
            {
                'documentation': {
                    'description': 'The source unit applies a single source configuration.'
                },
                'name': 'NIDCPOWER_VAL_SINGLE_POINT',
                'value': 1020
            },
            {
                'documentation': {
                    'description': 'The source unit applies a list of voltage or current configurations sequentially.'
                },
                'name': 'NIDCPOWER_VAL_SEQUENCE',
                'value': 1021
            }
        ]
    },
    'TransientResponse': {
        'values': [
            {
                'documentation': {
                    'description': 'The output responds to changes in load at a normal speed.'
                },
                'name': 'NIDCPOWER_VAL_NORMAL',
                'value': 1038
            },
            {
                'documentation': {
                    'description': 'The output responds to changes in load quickly.'
                },
                'name': 'NIDCPOWER_VAL_FAST',
                'value': 1039
            },
            {
                'documentation': {
                    'description': 'The output responds to changes in load slowly.'
                },
                'name': 'NIDCPOWER_VAL_SLOW',
                'value': 1041
            },
            {
                'documentation': {
                    'description': 'The output responds to changes in load based on specified values.'
                },
                'name': 'NIDCPOWER_VAL_CUSTOM',
                'value': 1042
            }
        ]
    },
    'TriggerType': {
        'values': [
            {
                'documentation': {
                    'description': 'No trigger is configured.'
                },
                'name': 'NIDCPOWER_VAL_NONE',
                'value': 1012
            },
            {
                'documentation': {
                    'description': 'The data operation starts when a digital edge is detected.'
                },
                'name': 'NIDCPOWER_VAL_DIGITAL_EDGE',
                'value': 1014
            },
            {
                'documentation': {
                    'description': 'The data operation starts when a software trigger occurs.'
                },
                'name': 'NIDCPOWER_VAL_SOFTWARE_EDGE',
                'value': 1015
            }
        ]
    }
}
