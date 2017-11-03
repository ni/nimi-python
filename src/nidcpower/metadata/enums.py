
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
'description': '''
Specifies aperture time in seconds. NIDCPOWER_VAL_POWER_LINE_CYCLES (1029) Specifies aperture time in power line cycles (PLCs).
''',
},
            },
            {
                'name': 'POWER_LINE_CYCLES',
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
                'value': 0,
'documentation': {
'description': '''
Disables auto zero. NIDCPOWER_VAL_ONCE (1024) Makes zero conversions following the first measurement after initiating the device.  The device uses these zero conversions for the preceding measurement and future  measurements until the device is reinitiated.
''',
},
            },
            {
                'name': 'ON',
                'value': 1,
'documentation': {
'description': '''
Makes zero conversions for every measurement.
''',
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
'description': '''
Autoranging is disabled.
''',
},
            },
            {
                'name': 'ON',
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
                'value': 0,
'documentation': {
'description': '''
Autoranging is disabled.
''',
},
            },
            {
                'name': 'ON',
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
                'value': 13613,
'documentation': {
'description': '''

''',
},
            },
            {
                'name': 'CURRENT_TRIP',
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
                'name': 'DC_NOISE_REJECTION_NORMAL',
                'value': 1044,
'documentation': {
'description': '''
Normal rejection of DC noise. NIDCPOWER_VAL_DC_NOISE_REJECTION_SECOND_ORDER (1043) Second-order rejection of DC noise.
''',
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
'description': '''
Asserts the trigger on the rising edge of the digital signal. NIDCPOWER_VAL_FALLING (1017) Asserts the trigger on the falling edge of the digital signal.
''',
},
            },
            {
                'name': 'FALLING',
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
                'value': 1025,
'documentation': {
'description': '''
Acquires a measurement after each Source Complete event completes. NIDCPOWER_VAL_ON_DEMAND (1026) Acquires a measurement when the niDCPower_Measure function or niDCPower_MeasureMultiple function is called. NIDCPOWER_VAL_ON_MEASURE_TRIGGER (1027) Acquires a measurement when a Measure trigger is received.
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
'description': '''
Output Capacitance is low. NIDCPOWER_VAL_HIGH (1011) Output Capacitance is high.
''',
},
            },
            {
                'name': 'HIGH',
                'value': 1011,
'documentation': {
'description': '''
Output capacitance is high.
''',
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
'description': '''
Sets the output function to DC voltage. NIDCPOWER_VAL_DC_CURRENT (1007) Sets the output function to DC current. NIDCPOWER_VAL_PULSE_VOLTAGE (1049)   NIDCPOWER_VAL_PULSE_CURRENT (1050)
''',
},
            },
            {
                'name': 'DC_CURRENT',
                'value': 1007,
'documentation': {
'description': '''
Sets the output function to DC current.
''',
},
            },
            {
                'name': 'PULSE_VOLTAGE',
                'value': 1049,
'documentation': {
'description': '''
Sets the output function to pulse voltage.
''',
},
            },
            {
                'name': 'PULSE_CURRENT',
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
                'name': 'ACTIVE_HIGH',
                'value': 1018,
'documentation': {
'description': '''
A high pulse occurs when the event is generated.  The exported signal is low level both before and after the event is generated. NIDCPOWER_VAL_ACTIVE_LOW (1019) A low pulse occurs when the event is generated.  The exported signal is high level both before and after the event is generated.
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
'description': '''
Specifies a power line frequency of 50 Hz. NIDCPOWER_VAL_60_HERTZ (60.0) Specifies a power line frequency of 60 Hz.
''',
},
            },
            {
                'name': '_60_HERTZ',
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
                'value': 1003,
'documentation': {
'description': '''
Uses the PXI chassis power source.
''',
},
            },
            {
                'name': 'AUXILIARY',
                'value': 1004,
'documentation': {
'description': '''
Uses the auxiliary power source connected to the device.
''',
},
            },
            {
                'name': 'AUTOMATIC',
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
                'value': 1003,
'documentation': {
'description': '''
Uses the PXI chassis power source.
''',
},
            },
            {
                'name': 'AUXILIARY',
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
                'value': 1045,
'documentation': {
'description': '''
Keep new self calibration values in memory only.
''',
},
            },
            {
                'name': 'WRITE_TO_EEPROM',
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
                'value': 1008,
'documentation': {
'description': '''
Local sensing is selected. NIDCPOWER_VAL_REMOTE (1009) Remote sensing is selected.
''',
},
            },
            {
                'name': 'REMOTE',
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
                'value': 1020,
'documentation': {
'description': '''
The source unit applies a single source configuration. NIDCPOWER_VAL_SEQUENCE (1021) The source unit applies a list of voltage or current configurations sequentially.
''',
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
'description': '''
The output responds to changes in load at a normal speed. NIDCPOWER_VAL_FAST (1039) The output responds to changes in load quickly. NIDCPOWER_VAL_SLOW (1041) The output responds to changes in load slowly. NIDCPOWER_VAL_CUSTOM (1042) The output responds to changes in load based on specified values.
''',
},
            },
            {
                'name': 'FAST',
                'value': 1039,
'documentation': {
'description': '''
Fast transient response time.
''',
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
'description': '''
No trigger is configured. NIDCPOWER_VAL_DIGITAL_EDGE (1014) The data operation starts when a digital edge is detected. NIDCPOWER_VAL_SOFTWARE_EDGE (1015) The data operation starts when a software trigger occurs.
''',
},
            },
            {
                'name': 'DIGITAL_EDGE',
                'value': 1014,
'documentation': {
'description': '''
The data operation starts when a digital edge is detected. NIDCPOWER_VAL_SOFTWARE_EDGE (1015) The data operation starts when a software trigger occurs.
''',
},
            },
            {
                'name': 'SOFTWARE_EDGE',
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
                'value': 0,
'documentation': {
'description': '''
Autoranging is disabled.
''',
},
            },
            {
                'name': 'ON',
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
                'value': 0,
'documentation': {
'description': '''
Autoranging is disabled.
''',
},
            },
            {
                'name': 'ON',
                'value': 1,
'documentation': {
'description': '''
Autoranging is enabled.
''',
},
            },
        ],
    },
}
