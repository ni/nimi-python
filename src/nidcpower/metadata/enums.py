# -*- coding: utf-8 -*-
# This file is generated from NI-DCPower API metadata version 21.0.0d48
enums = {
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
                    'description': ''
                },
                'name': 'NIDCPOWER_VAL_CURRENT_REGULATE',
                'value': 0
            },
            {
                'documentation': {
                    'description': ''
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
                'name': 'NIDCPOWER_VAL_SOURCE_COMPLETE',
                'value': 1030
            },
            {
                'name': 'NIDCPOWER_VAL_MEASURE_COMPLETE',
                'value': 1031
            },
            {
                'name': 'NIDCPOWER_VAL_SEQUENCE_ITERATION_COMPLETE',
                'value': 1032
            },
            {
                'name': 'NIDCPOWER_VAL_SEQUENCE_ENGINE_DONE',
                'value': 1033
            },
            {
                'name': 'NIDCPOWER_VAL_PULSE_COMPLETE',
                'value': 1051
            },
            {
                'name': 'NIDCPOWER_VAL_READY_FOR_PULSE_TRIGGER',
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
                    'description': 'The device maintains a constant voltage by adjusting the current '
                },
                'name': 'NIDCPOWER_VAL_OUTPUT_CONSTANT_VOLTAGE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'The device maintains a constant current by adjusting the voltage.'
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
                'name': 'NIDCPOWER_VAL_START',
                'value': 1034
            },
            {
                'name': 'NIDCPOWER_VAL_SOURCE',
                'value': 1035
            },
            {
                'name': 'NIDCPOWER_VAL_MEASURE',
                'value': 1036
            },
            {
                'name': 'NIDCPOWER_VAL_SEQUENCE_ADVANCE',
                'value': 1037
            },
            {
                'name': 'NIDCPOWER_VAL_PULSE',
                'value': 1053
            },
            {
                'name': 'NIDCPOWER_VAL_SHUTDOWN',
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
