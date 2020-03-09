
# -*- coding: utf-8 -*-
# This file is code generated, do not make changes here.
#  If the generated information is not correct for python
#  changes can be made in enums_addon.py and they will be
#  applied at build time.

enums = {
    'ApertureTimeUnits': {
        'values': [
            {
                'name': 'NIDCPOWER_VAL_SECONDS',
                'value': 1028,
'documentation': {
'description': 'Specifies aperture time in seconds.',
},
            },
            {
                'name': 'NIDCPOWER_VAL_POWER_LINE_CYCLES',
                'value': 1029,
'documentation': {
'description': 'Specifies aperture time in power line cycles (PLCs).',
},
            },
        ],
    },
    'AutoZero': {
        'values': [
            {
                'name': 'NIDCPOWER_VAL_OFF',
                'value': 0,
'documentation': {
'description': 'Disables auto zero.',
},
            },
            {
                'name': 'NIDCPOWER_VAL_ON',
                'value': 1,
'documentation': {
'description': 'Makes zero conversions for every measurement.',
},
            },
            {
                'name': 'NIDCPOWER_VAL_ONCE',
                'value': 1024,
'documentation': {
'description': 'Makes zero conversions following the first measurement after initiating the device.  The device uses these zero conversions for the preceding measurement and future  measurements until the device is reinitiated.',
},
            },
        ],
    },
    'ComplianceLimitSymmetry': {
        'values': [
            {
                'name': 'SYMMETRIC',
                'value': 0,
'documentation': {
'description': 'Compliance limits are specified symmetrically about 0.',
},
            },
            {
                'name': 'ASYMMETRIC',
                'value': 1,
'documentation': {
'description': 'Compliance limits can be specified asymmetrically with respect to 0.',
},
            },
        ],
    },
    'CurrentLevelAutorange': {
        'values': [
            {
                'name': 'NIDCPOWER_VAL_OFF',
                'value': 0,
'documentation': {
'description': 'Autoranging is disabled.',
},
            },
            {
                'name': 'NIDCPOWER_VAL_ON',
                'value': 1,
'documentation': {
'description': 'Autoranging is enabled.',
},
            },
        ],
    },
    'CurrentLimitAutorange': {
        'values': [
            {
                'name': 'NIDCPOWER_VAL_OFF',
                'value': 0,
'documentation': {
'description': 'Autoranging is disabled.',
},
            },
            {
                'name': 'NIDCPOWER_VAL_ON',
                'value': 1,
'documentation': {
'description': 'Autoranging is enabled.',
},
            },
        ],
    },
    'CurrentLimitBehavior': {
        'values': [
            {
                'name': 'CURRENT_REGULATE',
                'value': 13613,
'documentation': {
'description': '',
},
            },
            {
                'name': 'CURRENT_TRIP',
                'value': 13614,
'documentation': {
'description': '',
},
            },
        ],
    },
    'DCNoiseRejection': {
        'values': [
            {
                'name': 'NIDCPOWER_VAL_DC_NOISE_REJECTION_SECOND_ORDER',
                'value': 1043,
'documentation': {
'description': 'Second-order rejection of DC noise.',
},
            },
            {
                'name': 'NIDCPOWER_VAL_DC_NOISE_REJECTION_NORMAL',
                'value': 1044,
'documentation': {
'description': 'Normal rejection of DC noise.',
},
            },
        ],
    },
    'DigitalEdge': {
        'values': [
            {
                'name': 'NIDCPOWER_VAL_RISING',
                'value': 1016,
'documentation': {
'description': 'Asserts the trigger on the rising edge of the digital signal.',
},
            },
            {
                'name': 'NIDCPOWER_VAL_FALLING',
                'value': 1017,
'documentation': {
'description': 'Asserts the trigger on the falling edge of the digital signal.',
},
            },
        ],
    },
    'MeasureWhen': {
        'values': [
            {
                'name': 'NIDCPOWER_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE',
                'value': 1025,
'documentation': {
'description': 'Acquires a measurement after each Source Complete event completes.',
},
            },
            {
                'name': 'NIDCPOWER_VAL_ON_DEMAND',
                'value': 1026,
'documentation': {
'description': 'Acquires a measurement when the niDCPower_Measure function or niDCPower_MeasureMultiple function is called.',
},
            },
            {
                'name': 'NIDCPOWER_VAL_ON_MEASURE_TRIGGER',
                'value': 1027,
'documentation': {
'description': 'Acquires a measurement when a Measure trigger is received.',
},
            },
        ],
    },
    'OutputCapacitance': {
        'values': [
            {
                'name': 'NIDCPOWER_VAL_LOW',
                'value': 1010,
'documentation': {
'description': 'Output Capacitance is low.',
},
            },
            {
                'name': 'NIDCPOWER_VAL_HIGH',
                'value': 1011,
'documentation': {
'description': 'Output Capacitance is high.',
},
            },
        ],
    },
    'OutputFunction': {
        'values': [
            {
                'name': 'NIDCPOWER_VAL_DC_VOLTAGE',
                'value': 1006,
'documentation': {
'description': 'Sets the output function to DC voltage.',
},
            },
            {
                'name': 'NIDCPOWER_VAL_DC_CURRENT',
                'value': 1007,
'documentation': {
'description': 'Sets the output function to DC current.',
},
            },
            {
                'name': 'NIDCPOWER_VAL_PULSE_VOLTAGE',
                'value': 1049,
'documentation': {
'description': 'Sets the output function to pulse voltage.',
},
            },
            {
                'name': 'NIDCPOWER_VAL_PULSE_CURRENT',
                'value': 1050,
'documentation': {
'description': 'Sets the output function to pulse current.',
},
            },
        ],
    },
    'Polarity': {
        'values': [
            {
                'name': 'NIDCPOWER_VAL_ACTIVE_HIGH',
                'value': 1018,
'documentation': {
'description': 'A high pulse occurs when the event is generated.  The exported signal is low level both before and after the event is generated.',
},
            },
            {
                'name': 'NIDCPOWER_VAL_ACTIVE_LOW',
                'value': 1019,
'documentation': {
'description': 'A low pulse occurs when the event is generated.  The exported signal is high level both before and after the event is generated.',
},
            },
        ],
    },
    'PowerLineFrequency': {
        'values': [
            {
                'name': 'NIDCPOWER_VAL_50_HERTZ',
                'value': 50.0,
'documentation': {
'description': 'Specifies a power line frequency of 50 Hz.',
},
            },
            {
                'name': 'NIDCPOWER_VAL_60_HERTZ',
                'value': 60.0,
'documentation': {
'description': 'Specifies a power line frequency of 60 Hz.',
},
            },
        ],
    },
    'PowerSource': {
        'values': [
            {
                'name': 'NIDCPOWER_VAL_INTERNAL',
                'value': 1003,
'documentation': {
'description': 'Uses the PXI chassis power source.',
},
            },
            {
                'name': 'NIDCPOWER_VAL_AUXILIARY',
                'value': 1004,
'documentation': {
'description': 'Uses the auxiliary power source connected to the device.',
},
            },
            {
                'name': 'NIDCPOWER_VAL_AUTOMATIC',
                'value': 1005,
'documentation': {
'description': 'Uses the auxiliary power source if it is available; otherwise uses the PXI chassis power source.',
},
            },
        ],
    },
    'PowerSourceInUse': {
        'values': [
            {
                'name': 'NIDCPOWER_VAL_INTERNAL',
                'value': 1003,
'documentation': {
'description': 'Uses the PXI chassis power source.',
},
            },
            {
                'name': 'NIDCPOWER_VAL_AUXILIARY',
                'value': 1004,
'documentation': {
'description': 'Uses the auxiliary power source connected to the device. Only the NI PXI-4110,  NI PXIe-4112, NI PXIe-4113, and NI PXI-4130 support this value. This is the only supported value  for the NI PXIe-4112 and NI PXIe-4113.',
},
            },
        ],
    },
    'SelfCalibrationPersistence': {
        'values': [
            {
                'name': 'NIDCPOWER_VAL_KEEP_IN_MEMORY',
                'value': 1045,
'documentation': {
'description': 'Keep new self calibration values in memory only.',
},
            },
            {
                'name': 'NIDCPOWER_VAL_WRITE_TO_EEPROM',
                'value': 1046,
'documentation': {
'description': 'Write new self calibration values to hardware.',
},
            },
        ],
    },
    'Sense': {
        'values': [
            {
                'name': 'NIDCPOWER_VAL_LOCAL',
                'value': 1008,
'documentation': {
'description': 'Local sensing is selected.',
},
            },
            {
                'name': 'NIDCPOWER_VAL_REMOTE',
                'value': 1009,
'documentation': {
'description': 'Remote sensing is selected.',
},
            },
        ],
    },
    'SourceMode': {
        'values': [
            {
                'name': 'NIDCPOWER_VAL_SINGLE_POINT',
                'value': 1020,
'documentation': {
'description': 'The source unit applies a single source configuration.',
},
            },
            {
                'name': 'NIDCPOWER_VAL_SEQUENCE',
                'value': 1021,
'documentation': {
'description': 'The source unit applies a list of voltage or current configurations sequentially.',
},
            },
        ],
    },
    'TransientResponse': {
        'values': [
            {
                'name': 'NIDCPOWER_VAL_NORMAL',
                'value': 1038,
'documentation': {
'description': 'The output responds to changes in load at a normal speed.',
},
            },
            {
                'name': 'NIDCPOWER_VAL_FAST',
                'value': 1039,
'documentation': {
'description': 'The output responds to changes in load quickly.',
},
            },
            {
                'name': 'NIDCPOWER_VAL_SLOW',
                'value': 1041,
'documentation': {
'description': 'The output responds to changes in load slowly.',
},
            },
            {
                'name': 'NIDCPOWER_VAL_CUSTOM',
                'value': 1042,
'documentation': {
'description': 'The output responds to changes in load based on specified values.',
},
            },
        ],
    },
    'TriggerType': {
        'values': [
            {
                'name': 'NIDCPOWER_VAL_NONE',
                'value': 1012,
'documentation': {
'description': 'No trigger is configured.',
},
            },
            {
                'name': 'NIDCPOWER_VAL_DIGITAL_EDGE',
                'value': 1014,
'documentation': {
'description': 'The data operation starts when a digital edge is detected.',
},
            },
            {
                'name': 'NIDCPOWER_VAL_SOFTWARE_EDGE',
                'value': 1015,
'documentation': {
'description': 'The data operation starts when a software trigger occurs.',
},
            },
        ],
    },
    'VoltageLevelAutorange': {
        'values': [
            {
                'name': 'NIDCPOWER_VAL_OFF',
                'value': 0,
'documentation': {
'description': 'Autoranging is disabled.',
},
            },
            {
                'name': 'NIDCPOWER_VAL_ON',
                'value': 1,
'documentation': {
'description': 'Autoranging is enabled.',
},
            },
        ],
    },
    'VoltageLimitAutorange': {
        'values': [
            {
                'name': 'NIDCPOWER_VAL_OFF',
                'value': 0,
'documentation': {
'description': 'Autoranging is disabled.',
},
            },
            {
                'name': 'NIDCPOWER_VAL_ON',
                'value': 1,
'documentation': {
'description': 'Autoranging is enabled.',
},
            },
        ],
    },
    'tBoolean': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0,
'documentation': {
'description': '',
},
            },
            {
                'name': 'TRUE',
                'value': 1,
'documentation': {
'description': '',
},
            },
        ],
    },
}
