
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
'description': 'Disables auto-zero.',
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
'description': '''
Makes zero conversions following the first measurement after initiating
the device. The device uses these zero conversions for the preceding
measurement and future measurements until the device is reinitiated.
''',
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
'description': 'NI-DCPower does not automatically select the current level range.',
},
            },
            {
                'name': 'ON',
                'value': 1,
'documentation': {
'description': 'NI-DCPower automatically selects the current level range.',
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
'description': 'NI-DCPower does not automatically select the current limit range.',
},
            },
            {
                'name': 'ON',
                'value': 1,
'documentation': {
'description': 'NI-DCPower automatically selects the current limit range.',
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
                'value': 1043,
'documentation': {
'description': '''
Second-order DC noise rejection. Refer to `Configuring the Measure
Unit <NI_DC_Power_Supplies_Help.chm::/ConfiguringTheMeasureUnit.html>`__
for supported devices.
''',
},
            },
            {
                'name': 'NORMAL',
                'value': 1044,
'documentation': {
'description': 'Normal DC noise rejection.',
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
'description': '''
Acquires a measurement after each Source Complete event completes. Use
the `niDCPower Fetch
Multiple <NIDCPowerVIRef.chm::/niDCPower_Fetch_Multiple.html>`__ VI to
retrieve the measurements.
''',
},
            },
            {
                'name': 'ON_DEMAND',
                'value': 1026,
'documentation': {
'description': '''
Acquires a measurement when the `niDCPower
Measure <NIDCPowerVIRef.chm::/niDCPower_Measure.html>`__ VI or
`niDCPower Measure
Multiple <NIDCPowerVIRef.chm::/niDCPower_Measure_Multiple.html>`__ VI is
called.
''',
},
            },
            {
                'name': 'ON_MEASURE_TRIGGER',
                'value': 1027,
'documentation': {
'description': '''
Acquires a measurement when a Measure trigger is received. Use the
`niDCPower Fetch
Multiple <NIDCPowerVIRef.chm::/niDCPower_Fetch_Multiple.html>`__ VI to
retrieve the measurements.
''',
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
'description': 'Output capacitance is low.',
},
            },
            {
                'name': 'HIGH',
                'value': 1011,
'documentation': {
'description': 'Output capacitance is high.',
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
                'name': 'ACTIVE_HIGH',
                'value': 1018,
'documentation': {
'description': '''
A high pulse occurs when the event is generated. The exported signal is
low level both before and after the event is generated.
''',
},
            },
            {
                'name': 'ACTIVE_LOW',
                'value': 1019,
'documentation': {
'description': '''
A low pulse occurs when the event is generated. The exported signal is
high level both before and after the event is generated.
''',
},
            },
        ],
    },
    'PowerLineFrequency': {
        'values': [
            {
                'name': '_50_HERTZ',
                'value': 50.0,
'documentation': {
'description': 'Specifies a power line frequency of 50 Hz.',
},
            },
            {
                'name': '_60_HERTZ',
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
'description': '''
Uses the auxiliary power source if it is available; otherwise, use the
PXI chassis power source.
''',
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
'description': '''
Uses the auxiliary power source connected to the device. Only the NI
PXI-4110, NI PXIe-4112, NI PXIe-4113, and NI PXI-4130 support this
value. This is the only supported value for the NI PXIe-4112 and NI
PXIe-4113.
''',
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
'description': 'Keep new self-calibration values in memory only.',
},
            },
            {
                'name': 'WRITE_TO_EEPROM',
                'value': 1046,
'documentation': {
'description': '''
Write new self-calibration values to hardware. Refer to your device
documentation for more information about the implications of frequent
writes to the EEPROM.
''',
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
'description': '''
The source unit sequentially applies a list of voltage or current
configurations.
''',
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
'description': 'Normal transient response time.',
},
            },
            {
                'name': 'FAST',
                'value': 1039,
'documentation': {
'description': 'Fast transient response time.',
},
            },
            {
                'name': 'SLOW',
                'value': 1041,
'documentation': {
'description': '''
Slow transient response time. Refer to `Configuring Transient
Response <NI_DC_Power_Supplies_Help.chm::/CompensatingforLoad.html>`__
for supported devices.
''',
},
            },
            {
                'name': 'CUSTOM',
                'value': 1042,
'documentation': {
'description': '''
Custom transient response time. If you select this value, you can then
specify values for the `Voltage Gain
Bandwidth <pniDCPower_VoltageGainBandwidth.html>`__, `Voltage
Compensation
Frequency <pniDCPower_VoltageCompensationFrequency.html>`__, `Voltage
Pole-Zero Frequency <pniDCPower_VoltagePoleZeroRatio.html>`__, `Current
Gain Bandwidth <pniDCPower_CurrentGainBandwidth.html>`__, `Current
Compensation
Frequency <pniDCPower_CurrentCompensationFrequency.html>`__, and
`Current Pole-Zero Ratio <pniDCPower_CurrentPoleZeroRatio.html>`__
properties. Refer to `Configuring Transient
Response <NI_DC_Power_Supplies_Help.chm::/CompensatingforLoad.html>`__
for supported devices.
''',
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
                'name': 'DIGITAL_EDGE',
                'value': 1014,
'documentation': {
'description': 'The data operation starts when a digital edge is detected.',
},
            },
            {
                'name': 'SOFTWARE_EDGE',
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
'description': 'NI-DCPower does not automatically select the voltage level range.',
},
            },
            {
                'name': 'ON',
                'value': 1,
'documentation': {
'description': 'NI-DCPower automatically selects the voltage level range.',
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
'description': 'NI-DCPower does not automatically select the voltage limit range.',
},
            },
            {
                'name': 'ON',
                'value': 1,
'documentation': {
'description': 'NI-DCPower automatically selects the voltage limit range.',
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
    'Signals': {
        'values': [
            {
                'name': 'SOURCE_COMPLETE_EVENT',
                'value': 1030,
                'documentation': {
                    'description': 'Exports the Source Complete event.',
                },
            },
            {
                'name': 'MEASURE_COMPLETE_EVENT',
                'value': 1031,
                'documentation': {
                    'description': 'Exports the Measure Complete event.',
                },
            },
            {
                'name': 'SEQUENCE_ITERATION_COMPLETE_EVENT',
                'value': 1032,
                'documentation': {
                    'description': 'Exports the Sequence Iteration Complete event.',
                },
            },  
            {
                'name': 'SEQUENCE_ENGINE_DONE_EVENT',
                'value': 1033,
                'documentation': {
                    'description': 'Exports the Sequence Engine Done event.',
                },
            },
            {
                'name': 'PULSE_COMPLETE_EVENT',
                'value': 1051,
                'documentation': {
                    'description': 'Exports the Pulse Complete event.',
                },
            },
            {
                'name': 'READY_FOR_PULSE_TRIGGER_EVENT',
                'value': 1052,
                'documentation': {
                    'description': 'Exports the Ready Pulse Trigger event.',
                },
            },
            {
                'name': 'START_TRIGGER',
                'value': 1034,
                'documentation': {
                    'description': 'Exports the Start trigger.',
                },
            },
            {
                'name': 'SOURCE_TRIGGER',
                'value': 1035,
                'documentation': {
                    'description': 'Exports the Source trigger.',
                },
            },
            {
                'name': 'MEASURE_TRIGGER',
                'value': 1036,
                'documentation': {
                    'description': 'Exports the Measure trigger.',
                },
            },
            {
                'name': 'SEQUENCE_ADVANCE_TRIGGER',
                'value': 1037,
                'documentation': {
                    'description': 'Exports the Sequence Advance trigger.',
                },
            },
            {
                'name': 'PULSE_TRIGGER',
                'value': 1053,
                'documentation': {
                    'description': 'Exports the Pulse trigger.',
                },
            },
    'MeasurementTypes': {
        'values': [
            {
                'name': 'MEASURE_CURRENT',
                'value': 0,
                'documentation': {
                    'description': 'The device measures current.',
                },
            },
            {
                'name': 'MEASURE_VOLTAGE',
                'value': 1,
                'documentation': {
                    'description': 'The device measures voltage.',
                },
            }
        ],
    },
    'OutputStates': {
        'values': [
            {
                'name': 'OUTPUT_CONSTANT_VOLTAGE',
                'value': 0,
                'documentation': {
                    'description': 'The device maintains a constant voltage by adjusting the current ',
                },
            },
            {
                'name': 'OUTPUT_CONSTANT_CURRENT',
                'value': 1,
                'documentation': {
                    'description': 'The device maintains a constant current by adjusting the voltage.',
                },
            }
        ],
    },  
}
