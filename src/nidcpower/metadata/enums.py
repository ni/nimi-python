
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
                'prefix': None,
                'value': 1028,
'documentation': {
'description': '''
Specifies aperture time in seconds.
''',
},
            },
            {
                'name': 'POWER_LINE_CYCLES',
                'prefix': None,
                'value': 1029,
'documentation': {
'description': '''
Specifies aperture time in power line cycles (PLCs).
''',
},
            },
        ],
    },
    'AutoZero': {
        'values': [
            {
                'name': 'OFF',
                'prefix': None,
                'value': 0,
'documentation': {
'description': '''
Disables auto zero.
''',
},
            },
            {
                'name': 'ON',
                'prefix': None,
                'value': 1,
'documentation': {
'description': '''
Makes zero conversions for every measurement.
''',
},
            },
            {
                'name': 'ONCE',
                'prefix': None,
                'value': 1024,
'documentation': {
'description': '''
Makes zero conversions following the first measurement after initiating the device.  The device uses these zero conversions for the preceding measurement and future  measurements until the device is reinitiated.
''',
},
            },
        ],
    },
    'CurrentLevelAutorange': {
        'values': [
            {
                'name': 'OFF',
                'prefix': None,
                'value': 0,
'documentation': {
'description': '''
Autoranging is disabled.
''',
},
            },
            {
                'name': 'ON',
                'prefix': None,
                'value': 1,
'documentation': {
'description': '''
Autoranging is enabled.
''',
},
            },
        ],
    },
    'CurrentLimitAutorange': {
        'values': [
            {
                'name': 'OFF',
                'prefix': None,
                'value': 0,
'documentation': {
'description': '''
Autoranging is disabled.
''',
},
            },
            {
                'name': 'ON',
                'prefix': None,
                'value': 1,
'documentation': {
'description': '''
Autoranging is enabled.
''',
},
            },
        ],
    },
    'CurrentLimitBehavior': {
        'values': [
            {
                'name': 'CURRENT_REGULATE',
                'prefix': None,
                'value': 13613,
'documentation': {
'description': '''

''',
},
            },
            {
                'name': 'CURRENT_TRIP',
                'prefix': None,
                'value': 13614,
'documentation': {
'description': '''

''',
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
'description': '''
Second-order rejection of DC noise.
''',
},
            },
            {
                'name': 'NORMAL',
                'prefix': 'DC_NOISE_REJECTION_',
                'value': 1044,
'documentation': {
'description': '''
Normal rejection of DC noise.
''',
},
            },
        ],
    },
    'DigitalEdge': {
        'values': [
            {
                'name': 'RISING',
                'prefix': None,
                'value': 1016,
'documentation': {
'description': '''
Asserts the trigger on the rising edge of the digital signal.
''',
},
            },
            {
                'name': 'FALLING',
                'prefix': None,
                'value': 1017,
'documentation': {
'description': '''
Asserts the trigger on the falling edge of the digital signal.
''',
},
            },
        ],
    },
    'MeasureWhen': {
        'values': [
            {
                'name': 'AUTOMATICALLY_AFTER_SOURCE_COMPLETE',
                'prefix': None,
                'value': 1025,
'documentation': {
'description': '''
Acquires a measurement after each Source Complete event completes.
''',
},
            },
            {
                'name': 'ON_DEMAND',
                'prefix': None,
                'value': 1026,
'documentation': {
'description': '''
Acquires a measurement when the niDCPower_Measure function or niDCPower_MeasureMultiple function is called.
''',
},
            },
            {
                'name': 'ON_MEASURE_TRIGGER',
                'prefix': None,
                'value': 1027,
'documentation': {
'description': '''
Acquires a measurement when a Measure trigger is received.
''',
},
            },
        ],
    },
    'OutputCapacitance': {
        'values': [
            {
                'name': 'LOW',
                'prefix': None,
                'value': 1010,
'documentation': {
'description': '''
Output Capacitance is low.
''',
},
            },
            {
                'name': 'HIGH',
                'prefix': None,
                'value': 1011,
'documentation': {
'description': '''
Output Capacitance is high.
''',
},
            },
        ],
    },
    'OutputFunction': {
        'values': [
            {
                'name': 'DC_VOLTAGE',
                'prefix': None,
                'value': 1006,
'documentation': {
'description': '''
Sets the output function to DC voltage.
''',
},
            },
            {
                'name': 'DC_CURRENT',
                'prefix': None,
                'value': 1007,
'documentation': {
'description': '''
Sets the output function to DC current.
''',
},
            },
            {
                'name': 'PULSE_VOLTAGE',
                'prefix': None,
                'value': 1049,
'documentation': {
'description': '''
Sets the output function to pulse voltage.
''',
},
            },
            {
                'name': 'PULSE_CURRENT',
                'prefix': None,
                'value': 1050,
'documentation': {
'description': '''
Sets the output function to pulse current.
''',
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
'description': '''
A high pulse occurs when the event is generated.  The exported signal is low level both before and after the event is generated.
''',
},
            },
            {
                'name': 'LOW',
                'prefix': 'ACTIVE_',
                'value': 1019,
'documentation': {
'description': '''
A low pulse occurs when the event is generated.  The exported signal is high level both before and after the event is generated.
''',
},
            },
        ],
    },
    'PowerLineFrequency': {
        'values': [
            {
                'name': '_50_HERTZ',
                'prefix': None,
                'value': 50.0,
'documentation': {
'description': '''
Specifies a power line frequency of 50 Hz.
''',
},
            },
            {
                'name': '_60_HERTZ',
                'prefix': None,
                'value': 60.0,
'documentation': {
'description': '''
Specifies a power line frequency of 60 Hz.
''',
},
            },
        ],
    },
    'PowerSource': {
        'values': [
            {
                'name': 'INTERNAL',
                'prefix': None,
                'value': 1003,
'documentation': {
'description': '''
Uses the PXI chassis power source.
''',
},
            },
            {
                'name': 'AUXILIARY',
                'prefix': None,
                'value': 1004,
'documentation': {
'description': '''
Uses the auxiliary power source connected to the device.
''',
},
            },
            {
                'name': 'AUTOMATIC',
                'prefix': None,
                'value': 1005,
'documentation': {
'description': '''
Uses the auxiliary power source if it is available; otherwise uses the PXI chassis power source.
''',
},
            },
        ],
    },
    'PowerSourceInUse': {
        'values': [
            {
                'name': 'INTERNAL',
                'prefix': None,
                'value': 1003,
'documentation': {
'description': '''
Uses the PXI chassis power source.
''',
},
            },
            {
                'name': 'AUXILIARY',
                'prefix': None,
                'value': 1004,
'documentation': {
'description': '''
Uses the auxiliary power source connected to the device. Only the NI PXI-4110,  NI PXIe-4112, NI PXIe-4113, and NI PXI-4130 support this value. This is the only supported value  for the NI PXIe-4112 and NI PXIe-4113.
''',
},
            },
        ],
    },
    'SelfCalibrationPersistence': {
        'values': [
            {
                'name': 'KEEP_IN_MEMORY',
                'prefix': None,
                'value': 1045,
'documentation': {
'description': '''
Keep new self calibration values in memory only.
''',
},
            },
            {
                'name': 'WRITE_TO_EEPROM',
                'prefix': None,
                'value': 1046,
'documentation': {
'description': '''
Write new self calibration values to hardware.
''',
},
            },
        ],
    },
    'Sense': {
        'values': [
            {
                'name': 'LOCAL',
                'prefix': None,
                'value': 1008,
'documentation': {
'description': '''
Local sensing is selected.
''',
},
            },
            {
                'name': 'REMOTE',
                'prefix': None,
                'value': 1009,
'documentation': {
'description': '''
Remote sensing is selected.
''',
},
            },
        ],
    },
    'SourceMode': {
        'values': [
            {
                'name': 'SINGLE_POINT',
                'prefix': None,
                'value': 1020,
'documentation': {
'description': '''
The source unit applies a single source configuration.
''',
},
            },
            {
                'name': 'SEQUENCE',
                'prefix': None,
                'value': 1021,
'documentation': {
'description': '''
The source unit applies a list of voltage or current configurations sequentially.
''',
},
            },
        ],
    },
    'TransientResponse': {
        'values': [
            {
                'name': 'NORMAL',
                'prefix': None,
                'value': 1038,
'documentation': {
'description': '''
The output responds to changes in load at a normal speed.
''',
},
            },
            {
                'name': 'FAST',
                'prefix': None,
                'value': 1039,
'documentation': {
'description': '''
The output responds to changes in load quickly.
''',
},
            },
            {
                'name': 'SLOW',
                'prefix': None,
                'value': 1041,
'documentation': {
'description': '''
The output responds to changes in load slowly.
''',
},
            },
            {
                'name': 'CUSTOM',
                'prefix': None,
                'value': 1042,
'documentation': {
'description': '''
The output responds to changes in load based on specified values.
''',
},
            },
        ],
    },
    'TriggerType': {
        'values': [
            {
                'name': 'NONE',
                'prefix': None,
                'value': 1012,
'documentation': {
'description': '''
No trigger is configured.
''',
},
            },
            {
                'name': 'DIGITAL_EDGE',
                'prefix': None,
                'value': 1014,
'documentation': {
'description': '''
The data operation starts when a digital edge is detected.
''',
},
            },
            {
                'name': 'SOFTWARE_EDGE',
                'prefix': None,
                'value': 1015,
'documentation': {
'description': '''
The data operation starts when a software trigger occurs.
''',
},
            },
        ],
    },
    'VoltageLevelAutorange': {
        'values': [
            {
                'name': 'OFF',
                'prefix': None,
                'value': 0,
'documentation': {
'description': '''
Autoranging is disabled.
''',
},
            },
            {
                'name': 'ON',
                'prefix': None,
                'value': 1,
'documentation': {
'description': '''
Autoranging is enabled.
''',
},
            },
        ],
    },
    'VoltageLimitAutorange': {
        'values': [
            {
                'name': 'OFF',
                'prefix': None,
                'value': 0,
'documentation': {
'description': '''
Autoranging is disabled.
''',
},
            },
            {
                'name': 'ON',
                'prefix': None,
                'value': 1,
'documentation': {
'description': '''
Autoranging is enabled.
''',
},
            },
        ],
    },
    'SendSoftwareEdgeTriggerType': {
        'values': [
            {
                'name': 'START',
                'value': 1034,
                'documentation': {'',},
            },
            {
                'name': 'SOURCE',
                'value': 1035,
                'documentation': {'',},
            },
            {
                'name': 'MEASURE',
                'value': 1036,
                'documentation': {'',},
            },
            {
                'name': 'SEQUENCE_ADVANCE',
                'value': 1037,
                'documentation': {'',},
            },
            {
                'name': 'PULSE',
                'value': 1053,
                'documentation': {'',},
            },
        ],
    },
    'Event': {
        'values': [
            {
                'name': 'SOURCE_COMPLETE',
                'value': 1030,
                'documentation': {'',},
            },
            {
                'name': 'MEASURE_COMPLETE',
                'value': 1031,
                'documentation': {'',},
            },
            {
                'name': 'SEQUENCE_ITERATION_COMPLETE',
                'value': 1032,
                'documentation': {'',},
            },
            {
                'name': 'SEQUENCE_ENGINE_DONE',
                'value': 1033,
                'documentation': {'',},
            },
            {
                'name': 'PULSE_COMPLETE',
                'value': 1051,
                'documentation': {'',},
            },
            {
                'name': 'READY_FOR_PULSE_TRIGGER',
                'value': 1052,
                'documentation': {'',},
            },
        ],
    },
}
