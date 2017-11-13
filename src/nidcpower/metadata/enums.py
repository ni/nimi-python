
# -*- coding: utf-8 -*-
# This file is code generated, do not make changes here.
#  If the generated information is not correct for python
#  changes can be made in enums_addon.py and they will be
#  applied at build time.

enums = {
    'ApertureTimeUnits': {
        'values': [
            {
                'name': 'SECONDS',
                'value': 1028,
'documentation': {
'description': 'Specifies aperture time in seconds.',
},
            },
            {
                'name': 'POWER_LINE_CYCLES',
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
                'name': 'OFF',
                'value': 0,
'documentation': {
'description': 'Disables auto zero.',
},
            },
            {
                'name': 'ON',
                'value': 1,
'documentation': {
'description': 'Makes zero conversions for every measurement.',
},
            },
            {
                'name': 'ONCE',
                'value': 1024,
'documentation': {
'description': 'Makes zero conversions following the first measurement after initiating the device.  The device uses these zero conversions for the preceding measurement and future  measurements until the device is reinitiated.',
},
            },
        ],
    },
    'CurrentLevelAutorange': {
        'values': [
            {
                'name': 'OFF',
                'value': 0,
'documentation': {
'description': 'Autoranging is disabled.',
},
            },
            {
                'name': 'ON',
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
                'name': 'OFF',
                'value': 0,
'documentation': {
'description': 'Autoranging is disabled.',
},
            },
            {
                'name': 'ON',
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
                'name': 'SECOND_ORDER',
                'prefix': 'DC_NOISE_REJECTION_',
                'value': 1043,
'documentation': {
'description': 'Second-order rejection of DC noise.',
},
            },
            {
                'name': 'NORMAL',
                'prefix': 'DC_NOISE_REJECTION_',
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
                'name': 'RISING',
                'value': 1016,
'documentation': {
'description': 'Asserts the trigger on the rising edge of the digital signal.',
},
            },
            {
                'name': 'FALLING',
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
                'name': 'AUTOMATICALLY_AFTER_SOURCE_COMPLETE',
                'value': 1025,
'documentation': {
'description': 'Acquires a measurement after each Source Complete event completes.',
},
            },
            {
                'name': 'ON_DEMAND',
                'value': 1026,
'documentation': {
'description': 'Acquires a measurement when the niDCPower_Measure function or niDCPower_MeasureMultiple function is called.',
},
            },
            {
                'name': 'ON_MEASURE_TRIGGER',
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
                'name': 'LOW',
                'value': 1010,
'documentation': {
'description': 'Output Capacitance is low.',
},
            },
            {
                'name': 'HIGH',
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
                'name': 'DC_VOLTAGE',
                'value': 1006,
'documentation': {
'description': 'Sets the output function to DC voltage.',
},
            },
            {
                'name': 'DC_CURRENT',
                'value': 1007,
'documentation': {
'description': 'Sets the output function to DC current.',
},
            },
            {
                'name': 'PULSE_VOLTAGE',
                'value': 1049,
'documentation': {
'description': 'Sets the output function to pulse voltage.',
},
            },
            {
                'name': 'PULSE_CURRENT',
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
                'name': 'HIGH',
                'prefix': 'ACTIVE_',
                'value': 1018,
'documentation': {
'description': 'A high pulse occurs when the event is generated.  The exported signal is low level both before and after the event is generated.',
},
            },
            {
                'name': 'LOW',
                'prefix': 'ACTIVE_',
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
                'name': '_50',
                'suffix': '_HERTZ',
                'value': 50.0,
'documentation': {
'description': 'Specifies a power line frequency of 50 Hz.',
},
            },
            {
                'name': '_60',
                'suffix': '_HERTZ',
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
                'name': 'INTERNAL',
                'value': 1003,
'documentation': {
'description': 'Uses the PXI chassis power source.',
},
            },
            {
                'name': 'AUXILIARY',
                'value': 1004,
'documentation': {
'description': 'Uses the auxiliary power source connected to the device.',
},
            },
            {
                'name': 'AUTOMATIC',
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
                'name': 'INTERNAL',
                'value': 1003,
'documentation': {
'description': 'Uses the PXI chassis power source.',
},
            },
            {
                'name': 'AUXILIARY',
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
                'name': 'KEEP_IN_MEMORY',
                'value': 1045,
'documentation': {
'description': 'Keep new self calibration values in memory only.',
},
            },
            {
                'name': 'WRITE_TO_EEPROM',
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
                'name': 'LOCAL',
                'value': 1008,
'documentation': {
'description': 'Local sensing is selected.',
},
            },
            {
                'name': 'REMOTE',
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
                'name': 'SINGLE_POINT',
                'value': 1020,
'documentation': {
'description': 'The source unit applies a single source configuration.',
},
            },
            {
                'name': 'SEQUENCE',
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
                'name': 'NORMAL',
                'value': 1038,
'documentation': {
'description': 'The output responds to changes in load at a normal speed.',
},
            },
            {
                'name': 'FAST',
                'value': 1039,
'documentation': {
'description': 'The output responds to changes in load quickly.',
},
            },
            {
                'name': 'SLOW',
                'value': 1041,
'documentation': {
'description': 'The output responds to changes in load slowly.',
},
            },
            {
                'name': 'CUSTOM',
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
                'name': 'NONE',
                'value': 1012,
'documentation': {
'description': 'No trigger is configured.',
},
            },
            {
                'name': 'DIGITAL',
                'suffix': '_EDGE',
                'value': 1014,
'documentation': {
'description': 'The data operation starts when a digital edge is detected.',
},
            },
            {
                'name': 'SOFTWARE',
                'suffix': '_EDGE',
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
                'name': 'OFF',
                'value': 0,
'documentation': {
'description': 'Autoranging is disabled.',
},
            },
            {
                'name': 'ON',
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
                'name': 'OFF',
                'value': 0,
'documentation': {
'description': 'Autoranging is disabled.',
},
            },
            {
                'name': 'ON',
                'value': 1,
'documentation': {
'description': 'Autoranging is enabled.',
},
            },
        ],
    },
}
