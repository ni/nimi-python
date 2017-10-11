
# -*- coding: utf-8 -*-
# This file is code generated, do not make changes here
#  If the generated information is not correct for python
#  changes can be made in functions_addon.py and they will be
#  applied at build time



functions = {
    'Abort': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
        ],
'documentation': {
'description': '''
Aborts a previously initiated measurement and returns the DMM to the
Idle state.
''',
},
    },
    'CalAdjustACFilter': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The session handle that you obtain from niDMM\_InitExtCal. The handle
identifies a particular instrument calibration session.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'Mode',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the calibration **mode** used to acquire the measurement.

For valid modes, refer to the calibration procedure for your device.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'Range',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the **range** to calibrate.

For valid ranges, refer to the calibration procedure for your device.
Auto-ranging is not supported for calibration operations.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'Frequency',
                'type': 'ViReal64',
'documentation': {
'description': 'Specifies the **frequency** of the input signal.',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'expectedValue',
                'type': 'ViReal64',
'documentation': {
'description': 'Specifies the **expected\_value** of the measurement.',
},
            },
        ],
'documentation': {
'description': '''
For the NI 4080/4081/4082 and the NI 4070/4071/4072, calibrates the
filter coefficients used for AC measurements of the supplied **Mode**
and **Range**.
''',
'note': '''
Refer to the calibration procedure for your device before using this
function.
''',
},
    },
    'CalAdjustGain': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The session handle that you obtain from niDMM\_InitExtCal. The handle
identifies a particular instrument calibration session.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'Mode',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the calibration **mode** used to acquire the measurement.

For valid modes, refer to the calibration procedure for your device.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'Range',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the **range** to calibrate.

For valid ranges, refer to the calibration procedure for your device.
Auto-ranging is not supported for calibration operations.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'inputResistance',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the **input\_resistance** that the device should use.
**input\_resistance** values are coerced up to the closest
**input\_resistance**.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'expectedValue',
                'type': 'ViReal64',
'documentation': {
'description': 'Specifies the **expected\_value** of the measurement.',
},
            },
        ],
'documentation': {
'description': '''
Calibrates the gain coefficient for the supplied **Mode**, **Range**,
and **Input\_Resistance**.
''',
'table_body': [['|image0|  .. |image0| image:: note.gif', '**Notes** The NI 4050 and NI 4060 are not supported. Refer to the calibration procedure for your device before using this function.']],
},
    },
    'CalAdjustLC': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The session handle that you obtain from niDMM\_InitExtCal. The handle
identifies a particular instrument calibration session.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'Type',
                'type': 'ViInt32',
'documentation': {
'description': 'Specifies which of the LC calibration steps to perform.',
'table_body': [['L & C Open (default)', 'Calibrates the open compensation.'], ['L & C Short', 'Calibrates the short compensation.'], ['L & C 25 Ω', 'Calibrates the 25 Ω resistance.'], ['L & C 1 kΩ', 'Calibrates the 1 kΩ resistance.'], ['L & C 5 kΩ', 'Calibrates the 5 kΩ resistance.'], ['L & C 100 kΩ', 'Calibrates the 100 kΩ resistance.']],
},
            },
        ],
'documentation': {
'description': '''
For the NI 4082 and NI 4072 only, performs a specialized LC calibration
step depending on the specified **Type**.
''',
'note': '''
Refer to the calibration procedure for your device before using this
function.
''',
},
    },
    'CalAdjustLinearization': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The session handle that you obtain from niDMM\_InitExtCal. The handle
identifies a particular instrument calibration session.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'Function',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the calibration **function** used to acquire the measurement.

For valid modes, refer to the *NI 4065 6½ Digit DMM Calibration
Procedure*.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'Range',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the **range** to calibrate. **range** values are coerced up to
the closest **range**.

For valid ranges, refer to the *NI 4065 6½ Digit DMM Calibration
Procedure*. Auto-ranging is not supported for calibration operations.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'inputResistance',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the **input\_resistance** that the device should use.
**input\_resistance** values are coerced up to the closest
**input\_resistance**.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'expectedValue',
                'type': 'ViReal64',
'documentation': {
'description': 'Specifies the **expected\_value** of the measurement.',
},
            },
        ],
'documentation': {
'description': 'For the NI 4065 only, compensates for any non-linearities.',
},
    },
    'CalAdjustMisc': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The session handle that you obtain from niDMM\_InitExtCal. The handle
identifies a particular instrument calibration session.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'Type',
                'type': 'ViInt32',
'documentation': {
'description': 'Specifies which of the miscellaneous calibration steps to perform.',
'table_body': [['NIDMM\\_EXTCAL\\_MISCCAL\\_VREF (default)', 'Calibrate the Voltage Reference.'], ['NIDMM\\_EXTCAL\\_MISCCAL\\_RREF', 'Calibrate the Resistance Reference.'], ['NIDMM\\_EXTCAL\\_MISCCAL\\_ZINT', 'Calibrate the Internal Impedance.'], ['NIDMM\\_EXTCAL\\_MISCCAL\\_2WIRELEAKAGE', 'Calibrate the 2-wire Leakage resistance.'], ['NIDMM\\_EXTCAL\\_MISCCAL\\_4WIRELEAKAGE', 'Calibrate the 4-wire Leakage resistance.'], ['NIDMM\\_EXTCAL\\_MISCCAL\\_SECTION', 'Update calibration information and verify calibration completeness.']],
},
            },
        ],
'documentation': {
'description': '''
Performs a specialized calibration step depending on the specified
**Type**.
''',
'note': '''
The NI 4050 and NI 4060 are not supported.
Refer to the calibration procedure for your device before using this
function.
''',
},
    },
    'CalAdjustOffset': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The session handle that you obtain from niDMM\_InitExtCal. The handle
identifies a particular instrument calibration session.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'Mode',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the calibration **mode** used to acquire the measurement.

For valid modes, refer to the calibration procedure for your device.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'Range',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the **range** to calibrate.

For valid ranges, refer to the calibration procedure for your device.
Auto-ranging is not supported for calibration operations.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'inputResistance',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the **input\_resistance** that the device should use.
**input\_resistance** values are coerced up to the closest
**input\_resistance**.
''',
},
            },
        ],
'documentation': {
'description': '''
Calibrates the offset and Auto Zero offset for the supplied **Mode**,
**Range**, and **Input\_Resistance**.
''',
'note': '''
The NI 4050 and NI 4060 are not supported.
Refer to the calibration procedure for your device before using this
function.
''',
},
    },
    'CheckAttributeViBoolean': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
This parameter is ignored. National Instruments DMMs do not support
channel names since they only have a single channel. This parameter is
included in order to support interchangeability and upgradability to
multiple channel DMMs.

The default value is " " (an empty string).
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'Pass the ID of an attribute.',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeValue',
                'type': 'ViBoolean',
'documentation': {
'description': 'Pass the value that you want to set the attribute to.',
},
            },
        ],
'documentation': {
'description': '''
This function checks the validity of a value you specify for a ViBoolean
attribute.
''',
},
    },
    'CheckAttributeViInt32': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
This parameter is ignored. National Instruments DMMs do not support
channel names since they only have a single channel. This parameter is
included in order to support interchangeability and upgradability to
multiple channel DMMs.

The default value is " " (an empty string).
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'Pass the ID of an attribute.',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeValue',
                'type': 'ViInt32',
'documentation': {
'description': 'Pass the value that you want to set the attribute to.',
},
            },
        ],
'documentation': {
'description': '''
This function checks the validity of a value you specify for a ViInt32
attribute.
''',
},
    },
    'CheckAttributeViReal64': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
This parameter is ignored. National Instruments DMMs do not support
channel names since they only have a single channel. This parameter is
included in order to support interchangeability and upgradability to
multiple channel DMMs.

The default value is " " (an empty string).
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'Pass the ID of an attribute.',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeValue',
                'type': 'ViReal64',
'documentation': {
'description': 'Pass the value that you want to set the attribute to.',
},
            },
        ],
'documentation': {
'description': '''
This function checks the validity of a value you specify for a ViReal64
attribute.
''',
},
    },
    'CheckAttributeViSession': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
This parameter is ignored. National Instruments DMMs do not support
channel names since they only have a single channel. This parameter is
included in order to support interchangeability and upgradability to
multiple channel DMMs.

The default value is " " (an empty string).
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'Pass the ID of an attribute.',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeValue',
                'type': 'ViSession',
'documentation': {
'description': 'Pass the value that you want to set the attribute to.',
},
            },
        ],
'documentation': {
'description': '''
This function checks the validity of a value you specify for a ViSession
attribute.
''',
},
    },
    'CheckAttributeViString': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
This parameter is ignored. National Instruments DMMs do not support
channel names since they only have a single channel. This parameter is
included in order to support interchangeability and upgradability to
multiple channel DMMs.

The default value is " " (an empty string).
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'Pass the ID of an attribute.',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeValue',
                'type': 'ViChar[ ]',
'documentation': {
'description': 'Pass the value that you want to set the attribute to.',
},
            },
        ],
'documentation': {
'description': '''
This function checks the validity of a value you specify for a ViString
attribute.
''',
},
    },
    'ClearError': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
        ],
'documentation': {
'description': '''
Clears the error information for the current execution thread and the
IVI session you specify. If you pass VI\_NULL for the
**Instrument\_Handle** parameter, this function clears the error
information only for the current execution thread.
''',
},
    },
    'ClearInterchangeWarnings': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
        ],
'documentation': {
'description': 'Clears the list of current interchange warnings.',
},
    },
    'CloseExtCal': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The session handle that you obtain from niDMM\_InitExtCal. The handle
identifies a particular instrument calibration session.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'Action',
                'type': 'ViInt32',
'documentation': {
'description': 'Specifies whether the driver saves the updated calibration constants.',
'table_body': [['NIDMM\\_EXTCAL\\_ACTION\\_ABORT (default)', 'Restores the calibration constants to what they were before starting the external calibration procedure.'], ['NIDMM\\_EXTCAL\\_ACTION\\_SAVE', 'Saves the new calibration constants to the device.']],
},
            },
        ],
'documentation': {
'description': '''
Performs the specified **Action**, closes the specified external
calibration session obtained from niDMM\_InitExtCal, and deallocates
resources that it reserved.
''',
'note': '''
The NI 4050 and NI 4060 are not supported.
Refer to the calibration procedure for your device before using this
function.
''',
},
    },
    'ConfigureACBandwidth': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'acMinimumFrequencyHz',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the minimum expected frequency component of the input signal
in hertz. This parameter affects the DMM only when you set the
NIDMM\_ATTR\_FUNCTION attribute to AC measurements. NI-DMM uses this
parameter to calculate the proper aperture for the measurement.
The driver sets the NIDMM\_ATTR\_AC\_MIN\_FREQ attribute to this value.
The valid range is 1 Hz–300 kHz for the NI 4080/4081/4082 and the NI
4070/4071/4072, 10 Hz–100 Hz for the NI 4065, and 20 Hz–25 kHz for the
NI 4050 and NI 4060.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'acMaximumFrequencyHz',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the maximum expected frequency component of the input signal
in hertz within the device limits. This parameter is used only for error
checking and verifies that the value of this parameter is less than the
maximum frequency of the device.

This parameter affects the DMM only when you set the
NIDMM\_ATTR\_FUNCTION attribute to AC measurements. The driver sets the
NIDMM\_ATTR\_AC\_MAX\_FREQ attribute to this value. The valid range is 1
Hz–300 kHz for the NI 4080/4081/4082 and the NI 4070/4071/4072, 10
Hz–100 Hz for the NI 4065, and 20 Hz–25 kHz for the NI 4050 and NI 4060.
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the NIDMM\_ATTR\_AC\_MIN\_FREQ and NIDMM\_ATTR\_AC\_MAX\_FREQ
attributes, which the DMM uses for AC measurements.
''',
},
    },
    'ConfigureADCCalibration': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'adcCalibration',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the **ADC\_Calibration** setting. The driver sets
NIDMM\_ATTR\_ADC\_CALIBRATION to this value.
NIDMM\_VAL\_ADC\_CALIBRATION\_ON enables **ADC\_Calibration**.
NIDMM\_VAL\_ADC\_CALIBRATION\_OFF disables **ADC\_Calibration**. If you
set the value to NIDMM\_VAL\_ADC\_CALIBRATION\_AUTO, the driver
determines whether to enable **ADC\_Calibration** based on the
measurement function and resolution that you configure. If you configure
the NI 4080/4081/4082 or NI 4070/4071/4072 for a 6½–digit and greater
resolution DC measurement, the driver enables ADC Calibration. For all
other measurement configurations, the driver disables
**ADC\_Calibration**.
''',
'table_body': [['NIDMM\\_VAL\\_ADC\\_CALIBRATION\\_AUTO (default)', '-1.0', 'The DMM enables or disables **ADC\\_Calibration** based on the configured function and resolution.'], ['NIDMM\\_VAL\\_ADC\\_CALIBRATION\\_OFF', '0', 'The DMM does not compensate for changes to the gain.'], ['NIDMM\\_VAL\\_ADC\\_CALIBRATION\\_ON', '1', 'The DMM measures an internal reference to calculate the correct gain for the measurement.']],
'table_header': ['Name', 'Value', 'Description'],
},
            },
        ],
'documentation': {
'description': '''
For the NI 4080/4081/4082 and NI 4070/4071/4072, allows the DMM to
compensate for gain drift since the last external calibration or
self-calibration. When **ADC\_Calibration** is ON, the DMM measures an
internal reference to calculate the correct gain for the measurement.
When **ADC\_Calibration** is OFF, the DMM does not compensate for
changes to the gain.
''',
},
    },
    'ConfigureAutoZeroMode': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'autoZeroMode',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the **auto\_zero\_mode**. NI-DMM sets the
NIDMM\_ATTR\_AUTO\_ZERO attribute to this value.

ON enables **auto\_zero\_mode** for each measurement. ONCE enables
**auto\_zero\_mode** before the next measurement. The
**auto\_zero\_mode** value is stored and used in subsequent measurements
until the device is reconfigured.

OFF disables **auto\_zero\_mode**. If you set this parameter to AUTO,
NI-DMM determines whether to enable Auto Zero based on the measurement
function that you configure. If you configure the NI 4080/4081/4082 or
the NI 4070/4071/4072 for a 6½–digit and greater resolution DC
measurement, NI-DMM sets **auto\_zero\_mode** to ON.

For all other DC measurement configurations on the NI 4080/4081/4082 or
the NI 4070/4071/4072, NI-DMM sets **auto\_zero\_mode** to ONCE. For all
AC measurements or waveform acquisitions on the NI 4080/4081/4082 or the
NI 4070/4071/4072, NI-DMM sets **auto\_zero\_mode** to OFF. For NI 4060,
**auto\_zero\_mode** is set to OFF when AUTO is selected.

For NI 4065 devices, **auto\_zero\_mode** is always ON.
**auto\_zero\_mode** is an integral part of the signal measurement phase
and adds no extra time to the overall measurement.
''',
'note': 'The NI 4060/4065 does *not* support this setting.',
'table_body': [['NIDMM\\_VAL\\_AUTO\\_ZERO\\_AUTO (default)', '-1', 'NI-DMM chooses the Auto Zero setting based on the configured function and resolution.'], ['NIDMM\\_VAL\\_AUTO\\_ZERO\\_OFF', '0', 'Disables Auto Zero.'], ['NIDMM\\_VAL\\_AUTO\\_ZERO\\_ON', '1', 'The DMM internally disconnects the input signal following each measurement and takes a zero reading. It then subtracts the zero reading from the preceding reading.'], ['NIDMM\\_VAL\\_AUTO\\_ZERO\\_ONCE', '2', 'The DMM internally disconnects the input signal following the first measurement and takes a zero reading. It then subtracts the zero reading from the preceding reading and each measurement that follows.']],
},
            },
        ],
'documentation': {
'description': '''
Configures the DMM for **Auto\_Zero\_Mode**. When **Auto\_Zero\_Mode**
is ON, the DMM internally disconnects the input signal and takes a zero
reading. It then subtracts the zero reading from the measurement. This
prevents offset voltages present on the input circuitry of the DMM from
affecting measurement accuracy. When **Auto\_Zero\_Mode** is OFF, the
DMM does not compensate for zero reading offset.
''',
},
    },
    'ConfigureCableCompType': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'cableCompType',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the type of cable compensation that is used for the current
range.
''',
},
            },
        ],
'documentation': {
'description': '''
For the NI 4082 and NI 4072 only, sets the
NIDMM\_ATTR\_CABLE\_COMP\_TYPE attribute for the current
capacitance/inductance mode range.
''',
},
    },
    'ConfigureCurrentSource': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'currentSource',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the **current\_source** provided during diode measurements.
For valid ranges, refer to the device sections for your device. The
driver sets NIDMM\_ATTR\_CURRENT\_SOURCE to this value.
''',
'table_body': [['NIDMM\\_VAL\\_1\\_MICROAMP', '1 µA', 'NI 4080/4081/4082 and NI 4070/4071/4072'], ['NIDMM\\_VAL\\_10\\_MICROAMP', '10 µA', 'NI 4080/4081/4082 and NI 4070/4071/4072 only'], ['NIDMM\\_VAL\\_100\\_MICROAMP', '100 µA', 'NI 4080/4081/4082, NI 4070/4071/4072, and NI 4065'], ['NIDMM\\_VAL\\_1\\_MILLIAMP (default)', '1 mA', 'NI 4080/4081/4082, NI 4070/4071/4072, and NI 4065']],
},
            },
        ],
'documentation': {
'description': '''
The NI 4050 and NI 4060 are not supported. Configures the
**Current\_Source** for diode measurements.
''',
},
    },
    'ConfigureFixedRefJunction': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'fixedReferenceJunction',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the reference junction temperature when a fixed reference
junction is used to take a thermocouple measurement. The units are
degrees Celsius. NI-DMM uses this value to set the Fixed Reference
Junction property. The default is 25.00 (°C).
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the fixed reference junction temperature for a thermocouple
with a fixed reference junction type.
''',
},
    },
    'ConfigureFrequencyVoltageRange': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'voltageRange',
                'type': 'ViReal64',
'documentation': {
'description': '''
Sets the expected maximum amplitude of the input signal. Refer to the
`NI 4080 <REPLACE_DRIVER_SPECIFIC_URL_1(4080_functional_overview)>`__,
`NI 4081 <REPLACE_DRIVER_SPECIFIC_URL_1(4081_functional_overview)>`__,
`NI 4072 <REPLACE_DRIVER_SPECIFIC_URL_1(4082)>`__,
`NI 4070 <REPLACE_DRIVER_SPECIFIC_URL_1(4070_functional_overview)>`__,
`NI 4071 <REPLACE_DRIVER_SPECIFIC_URL_1(4071_functional_overview)>`__,
and `NI 4072 <REPLACE_DRIVER_SPECIFIC_URL_1(4072)>`__ sections for a
list of valid values. NI-DMM sets NIDMM\_ATTR\_FREQ\_VOLTAGE\_RANGE to
this value. The minimum peak-to-peak signal amplitude that can be
detected is 10% of the specified **voltage\_range**.
''',
'table_body': [['NIDMM\\_VAL\\_AUTO\\_RANGE\\_ON (default)', '-1.0', 'Configures the DMM to take an Auto Range measurement to calculate the voltage range before each frequency or period measurement.'], ['NIDMM\\_VAL\\_AUTO\\_RANGE\\_OFF', '-2.0', 'Disables Auto Ranging. The driver sets the voltage range to the last calculated voltage range.']],
'table_header': ['Name', 'Value', 'Description'],
},
            },
        ],
'documentation': {
'description': '''
For the NI 4080/4081/4082 and the NI 4070/4071/4072 only, specifies the
expected maximum amplitude of the input signal for frequency and period
measurements.
''',
},
    },
    'ConfigureMeasCompleteDest': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'measCompleteDestination',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the destination of the Measurement Complete signal. This
signal is issued when the DMM completes a single measurement. The driver
sets the NIDMM\_ATTR\_MEAS\_COMPLETE\_DEST attribute to this value. This
signal is commonly referred to as Voltmeter Complete.
''',
'note': '''
To determine which values are supported by each device, refer to the
`LabWindows/CVI Trigger
Routing <REPLACE_DRIVER_SPECIFIC_URL_1(cvitrigger_routing)>`__ section.
''',
},
            },
        ],
'documentation': {
'description': '''
Specifies the destination of the DMM Measurement Complete (MC) signal.
Refer to `Triggering <REPLACE_DRIVER_SPECIFIC_URL_1(trigger)>`__ for
more information.
''',
},
    },
    'ConfigureMeasCompleteSlope': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'measCompleteSlope',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the polarity of the signal that is generated. The driver sets
NIDMM\_ATTR\_MEAS\_DEST\_SLOPE to this value.
''',
'table_body': [['Rising Edge', '0', 'NIDMM\\_VAL\\_POSITIVE', 'The driver triggers on the rising edge of the trigger signal.'], ['Falling Edge (default)', '1', 'NIDMM\\_VAL\\_NEGATIVE', 'The driver triggers on the falling edge of the trigger signal.']],
},
            },
        ],
'documentation': {
'description': '''
Sets the Measurement Complete signal to either rising edge (positive) or
falling edge (negative) polarity.
''',
},
    },
    'ConfigureMeasurementAbsolute': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'measurementFunction',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the **measurement\_function** used to acquire the measurement.
The driver sets NIDMM\_ATTR\_FUNCTION to this value.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'Range',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the **range** for the function specified in the
**Measurement\_Function** parameter. When frequency is specified in the
**Measurement\_Function** parameter, you must supply the minimum
frequency expected in the **range** parameter. For example, you must
type in 100 Hz if you are measuring 101 Hz or higher.
For all other functions, you must supply a **range** that exceeds the
value that you are measuring. For example, you must type in 10 V if you
are measuring 9 V. **range** values are coerced up to the closest input
**range**. Refer to the `Devices
Overview <REPLACE_DRIVER_SPECIFIC_URL_1(devices)>`__ for a list of valid
ranges. The driver sets NIDMM\_ATTR\_RANGE to this value. The default is
0.02 V.
''',
'note': '''
The NI 4050, NI 4060, and NI 4065 only support Auto Range when the
trigger and sample trigger are set to IMMEDIATE.
''',
'table_body': [['NIDMM\\_VAL\\_AUTO\\_RANGE\\_ON', '-1.0', 'NI-DMM performs an Auto Range before acquiring the measurement.'], ['NIDMM\\_VAL\\_AUTO\\_RANGE\\_OFF', '-2.0', 'NI-DMM sets the Range to the current NIDMM\\_ATTR\\_AUTO\\_RANGE\\_VALUE and uses this range for all subsequent measurements until the measurement configuration is changed.'], ['NIDMM\\_VAL\\_AUTO\\_RANGE\\_ONCE', '-3.0', 'NI-DMM performs an Auto Range before acquiring the measurement. The NIDMM\\_ATTR\\_AUTO\\_RANGE\\_VALUE is stored and used for all subsequent measurements until the measurement configuration is changed.']],
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'resolutionAbsolute',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the absolute resolution for the measurement. NI-DMM sets
NIDMM\_ATTR\_RESOLUTION\_ABSOLUTE to this value. This parameter is
ignored when the **Range** parameter is set to
NIDMM\_VAL\_AUTO\_RANGE\_ON (-1.0) or NIDMM\_VAL\_AUTO\_RANGE\_ONCE
(-3.0). The default is 0.001 V.
''',
'note': '''
NI-DMM ignores this parameter for capacitance and inductance
measurements on the NI 4072. To achieve better resolution for such
measurements, use the NIDMM\_ATTR\_LC\_NUMBER\_MEAS\_TO\_AVERAGE
attribute.
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the common attributes of the measurement. These attributes
include NIDMM\_ATTR\_FUNCTION, NIDMM\_ATTR\_RANGE, and
NIDMM\_ATTR\_RESOLUTION\_ABSOLUTE.
''',
},
    },
    'ConfigureMeasurementDigits': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'measurementFunction',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the **measurement\_function** used to acquire the measurement.
The driver sets NIDMM\_ATTR\_FUNCTION to this value.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'Range',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the range for the function specified in the
**Measurement\_Function** parameter. When frequency is specified in the
**Measurement\_Function** parameter, you must supply the minimum
frequency expected in the **range** parameter. For example, you must
type in 100 Hz if you are measuring 101 Hz or higher.
For all other functions, you must supply a range that exceeds the value
that you are measuring. For example, you must type in 10 V if you are
measuring 9 V. range values are coerced up to the closest input range.
Refer to the `Devices
Overview <REPLACE_DRIVER_SPECIFIC_URL_1(devices)>`__ for a list of valid
ranges. The driver sets NIDMM\_ATTR\_RANGE to this value. The default is
0.02 V.
''',
'note': '''
The NI 4050, NI 4060, and NI 4065 only support Auto Range when the
trigger and sample trigger are set to IMMEDIATE.
''',
'table_body': [['NIDMM\\_VAL\\_AUTO\\_RANGE\\_ON', '-1.0', 'NI-DMM performs an Auto Range before acquiring the measurement.'], ['NIDMM\\_VAL\\_AUTO\\_RANGE\\_OFF', '-2.0', 'NI-DMM sets the Range to the current NIDMM\\_ATTR\\_AUTO\\_RANGE\\_VALUE and uses this range for all subsequent measurements until the measurement configuration is changed.'], ['NIDMM\\_VAL\\_AUTO\\_RANGE\\_ONCE', '-3.0', 'NI-DMM performs an Auto Range before acquiring the measurement. The NIDMM\\_ATTR\\_AUTO\\_RANGE\\_VALUE is stored and used for all subsequent measurements until the measurement configuration is changed.']],
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'resolutionDigits',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the resolution of the measurement in digits. The driver sets
the `Devices Overview <REPLACE_DRIVER_SPECIFIC_URL_1(devices)>`__ for a
list of valid ranges. The driver sets NIDMM\_ATTR\_RESOLUTION\_DIGITS
attribute to this value. This parameter is ignored when the **Range**
parameter is set to NIDMM\_VAL\_AUTO\_RANGE\_ON (-1.0) or
NIDMM\_VAL\_AUTO\_RANGE\_ONCE (-3.0). The default is 5½.
''',
'note': '''
NI-DMM ignores this parameter for capacitance and inductance
measurements on the NI 4072. To achieve better resolution for such
measurements, use the NIDMM\_ATTR\_LC\_NUMBER\_MEAS\_TO\_AVERAGE
attribute.
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the common attributes of the measurement. These attributes
include NIDMM\_ATTR\_FUNCTION, NIDMM\_ATTR\_RANGE, and
NIDMM\_ATTR\_RESOLUTION\_DIGITS.
''',
},
    },
    'ConfigureMultiPoint': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'triggerCount',
                'type': 'ViInt32',
'documentation': {
'description': '''
Sets the number of triggers you want the DMM to receive before returning
to the Idle state. The driver sets NIDMM\_ATTR\_TRIGGER\_COUNT to this
value. The default value is 1.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'sampleCount',
                'type': 'ViInt32',
'documentation': {
'description': '''
Sets the number of measurements the DMM makes in each measurement
sequence initiated by a trigger. The driver sets
NIDMM\_ATTR\_SAMPLE\_COUNT to this value. The default value is 1.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'sampleTrigger',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the **sample\_trigger** source you want to use. The driver
sets NIDMM\_ATTR\_SAMPLE\_TRIGGER to this value. The default is
Immediate.
''',
'note': '''
To determine which values are supported by each device, refer to the
`LabWindows/CVI Trigger
Routing <REPLACE_DRIVER_SPECIFIC_URL_1(cvitrigger_routing)>`__ section.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'sampleInterval',
                'type': 'ViReal64',
'documentation': {
'description': '''
Sets the amount of time in seconds the DMM waits between measurement
cycles. The driver sets NIDMM\_ATTR\_SAMPLE\_INTERVAL to this value.
Specify a sample interval to add settling time between measurement
cycles or to decrease the measurement rate. **sample\_interval** only
applies when the **Sample\_Trigger** is set to INTERVAL.

On the NI 4060, the **sample\_interval** value is used as the settling
time. When sample interval is set to 0, the DMM does not settle between
measurement cycles. The NI 4065 and NI 4070/4071/4072 use the value
specified in **sample\_interval** as additional delay. The default value
(-1) ensures that the DMM settles for a recommended time. This is the
same as using an Immediate trigger.
''',
'note': 'This attribute is not used on the NI 4080/4081/4082 and the NI 4050.',
},
            },
        ],
'documentation': {
'description': '''
Configures the attributes for multipoint measurements. These attributes
include NIDMM\_ATTR\_TRIGGER\_COUNT, NIDMM\_ATTR\_SAMPLE\_COUNT,
NIDMM\_ATTR\_SAMPLE\_TRIGGER, and NIDMM\_ATTR\_SAMPLE\_INTERVAL.

For continuous acquisitions, set NIDMM\_ATTR\_TRIGGER\_COUNT or
NIDMM\_ATTR\_SAMPLE\_COUNT to zero. For more information, refer to
`Multiple Point
Acquisitions <REPLACE_DRIVER_SPECIFIC_URL_1(multi_point)>`__,
`Triggering <REPLACE_DRIVER_SPECIFIC_URL_1(trigger)>`__, and `Using
Switches <REPLACE_DRIVER_SPECIFIC_URL_1(switch_selection)>`__.
''',
},
    },
    'ConfigureOffsetCompOhms': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'offsetCompOhms',
                'type': 'ViInt32',
'documentation': {
'description': '''
Enables or disables **offset\_comp\_ohms**. The driver sets
NIDMM\_ATTR\_OFFSET\_COMP\_OHMS to this value.
''',
'table_body': [['NIDMM\\_VAL\\_OFFSET\\_COMP\\_OHMS\\_OFF (default)', '0', 'Off disables **Offset\\_Comp\\_Ohms**.'], ['NIDMM\\_VAL\\_OFFSET\\_COMP\\_OHMS\\_ON', '1', 'On enables **Offset\\_Comp\\_Ohms**.']],
'table_header': ['Name', 'Value', 'Description'],
},
            },
        ],
'documentation': {
'description': '''
For NI 4080/4081/4082 and NI 4070/4071/4072, allows the DMM to
compensate for voltage offsets in resistance measurements. When
**Offset\_Comp\_Ohms** is enabled, the DMM measures the resistance twice
(once with the current source on and again with it turned off). Any
voltage offset present in both measurements is cancelled out.
**Offset\_Comp\_Ohms** is useful when measuring resistance values less
than 10 KΩ.
''',
},
    },
    'ConfigureOpenCableCompValues': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'Conductance',
                'type': 'ViReal64',
'documentation': {
'description': 'Specifies the open cable compensation **conductance**.',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'Susceptance',
                'type': 'ViReal64',
'documentation': {
'description': 'Specifies the open cable compensation **susceptance**.',
},
            },
        ],
'documentation': {
'description': '''
For the NI 4082 and NI 4072 only, configures the
NIDMM\_ATTR\_OPEN\_CABLE\_COMP\_CONDUCTANCE and
NIDMM\_ATTR\_OPEN\_CABLE\_COMP\_SUSCEPTANCE attributes.
''',
},
    },
    'ConfigurePowerLineFrequency': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'powerLineFrequencyHz',
                'type': 'ViReal64',
'documentation': {
'description': '''
**Powerline Frequency** specifies the powerline frequency in hertz.
NI-DMM sets the Powerline Frequency property to this value.
''',
},
            },
        ],
'documentation': {
'description': 'Specifies the powerline frequency.',
},
    },
    'ConfigureRTDCustom': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'rtdA',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the Callendar-Van Dusen A coefficient for RTD scaling when RTD
Type parameter is set to Custom in the niDMM\_ConfigureRTDType function.
The default is 3.9083e-3 (Pt3851)
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'rtdB',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the Callendar-Van Dusen B coefficient for RTD scaling when RTD
Type parameter is set to Custom in the niDMM\_ConfigureRTDType function.
The default is -5.775e-7 (Pt3851).
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'rtdC',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the Callendar-Van Dusen C coefficient for RTD scaling when RTD
Type parameter is set to Custom in the niDMM\_ConfigureRTDType function.
The default is -4.183e-12 (Pt3851).
''',
},
            },
        ],
'documentation': {
'description': 'Configures the A, B, and C parameters for a custom RTD.',
},
    },
    'ConfigureRTDType': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'rtdType',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the type of RTD used to measure the temperature resistance.
NI-DMM uses this value to set the RTD Type property. The default is
NIDMM\_VAL\_TEMP\_RTD\_PT3851.
''',
'table_body': [['Callendar-Van Dusen Coefficient'], ['NIDMM\\_VAL\\_TEMP\\_RTD\\_PT3851', 'IEC-751 DIN 43760 BS 1904 ASTM-E1137 EN-60751', 'Platinum', '.003851', '100 Ω 1000 Ω', 'A = 3.9083 × 10\\ :sup:`–3` B = –5.775×10:sup:`–7` C = –4.183×10:sup:`–12`', 'Most common RTDs'], ['NIDMM\\_VAL\\_TEMP\\_RTD\\_PT3750', 'Low-cost vendor compliant RTD\\*', 'Platinum', '.003750', '1000 Ω', 'A = 3.81 × 10\\ :sup:`–3` B = –6.02×10:sup:`–7` C = –6.0×10:sup:`–12`', 'Low-cost RTD'], ['NIDMM\\_VAL\\_TEMP\\_RTD\\_PT3916', 'JISC 1604', 'Platinum', '.003916', '100 Ω', 'A = 3.9739 × 10\\ :sup:`–3` B = –5.870×10:sup:`–7` C = –4.4 ×10\\ :sup:`–12`', 'Used in primarily in Japan'], ['NIDMM\\_VAL\\_TEMP\\_RTD\\_PT3920', 'US Industrial Standard D-100 American', 'Platinum', '.003920', '100 Ω', 'A = 3.9787 × 10\\ :sup:`–3` B = –5.8686×10:sup:`–7` C = –4.167 ×10\\ :sup:`–12`', 'Low-cost RTD'], ['NIDMM\\_VAL\\_TEMP\\_RTD\\_PT3911', 'US Industrial Standard American', 'Platinum', '.003911', '100 Ω', 'A = 3.9692 × 10\\ :sup:`–3` B = –5.8495×10:sup:`–7` C = –4.233 ×10\\ :sup:`–12`', 'Low-cost RTD'], ['NIDMM\\_VAL\\_TEMP\\_RTD\\_PT3928', 'ITS-90', 'Platinum', '.003928', '100 Ω', 'A = 3.9888 × 10\\ :sup:`–3` B = –5.915×10:sup:`–7` C = –3.85 ×10\\ :sup:`–12`', 'The definition of temperature'], ['\\*No standard. Check the TCR.']],
'table_header': ['Enum', 'Standards', 'Material', 'TCR (α)', 'Typical R\\ :sub:`0` (Ω)', 'Notes'],
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'rtdResistance',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the RTD resistance in ohms at 0 °C. NI-DMM uses this value to
set the RTD Resistance property. The default is 100 (Ω).
''',
},
            },
        ],
'documentation': {
'description': 'Configures the RTD Type and RTD Resistance parameters for an RTD.',
},
    },
    'ConfigureSampleTriggerSlope': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'sampleTriggerSlope',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the polarity of the Trigger signal on which the measurement is
triggered for values of either NIDMM\_VAL\_POSITIVE or
NIDMM\_VAL\_NEGATIVE. The driver sets
NIDMM\_ATTR\_SAMPLE\_TRIGGER\_SLOPE to this value.
''',
'table_body': [['Rising Edge', '0', 'NIDMM\\_VAL\\_POSITIVE', 'The driver triggers on the rising edge of the trigger signal.'], ['Falling Edge (default)', '1', 'NIDMM\\_VAL\\_NEGATIVE', 'The driver triggers on the falling edge of the trigger signal.']],
},
            },
        ],
'documentation': {
'description': '''
Sets the NIDMM\_ATTR\_SAMPLE\_TRIGGER\_SLOPE to either rising edge
(positive) or falling edge (negative) polarity.
''',
},
    },
    'ConfigureShortCableCompValues': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'Resistance',
                'type': 'ViReal64',
'documentation': {
'description': 'Specifies the short cable compensation **resistance**.',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'Reactance',
                'type': 'ViReal64',
'documentation': {
'description': 'Specifies the short cable compensation **reactance**.',
},
            },
        ],
'documentation': {
'description': '''
For the NI 4082 and NI 4072 only, configures the
NIDMM\_ATTR\_SHORT\_CABLE\_COMP\_RESISTANCE and
NIDMM\_ATTR\_SHORT\_CABLE\_COMP\_REACTANCE attributes.
''',
},
    },
    'ConfigureThermistorCustom': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'thermistorA',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the Steinhart-Hart A coefficient for thermistor scaling when
Thermistor Type is set to Custom in the niDMM\_ConfigureThermistorType
function. The default is 1.0295e-3 (44006).
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'thermistorB',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the Steinhart-Hart B coefficient for thermistor scaling when
Thermistor Type is set to Custom in the niDMM\_ConfigureThermistorType
function. The default is 2.391e-4 (44006).
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'thermistorC',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the Steinhart-Hart C coefficient for thermistor scaling when
Thermistor Type is set to Custom in the niDMM\_ConfigureThermistorType
function. The default is 1.568e-7 (44006).
''',
},
            },
        ],
'documentation': {
'description': 'Configures the A, B, and C parameters for a custom thermistor.',
},
    },
    'ConfigureThermistorType': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'thermistorType',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the type of thermistor used to measure the temperature. NI-DMM
uses this value to set the Thermistor Type property. The default is
NIDMM\_VAL\_TEMP\_THERMISTOR\_44006.

+--------------------+--------------------+--------------------+--------------------+
| **Defined Values** | **Thermistor       | **Value**          | **25 °C            |
|                    | Type**             |                    | Resistance**       |
+--------------------+--------------------+--------------------+--------------------+
| NIDMM\_VAL\_TEMP\_ | Custom             | 0                  | —                  |
| THERMISTOR\_CUSTOM |                    |                    |                    |
+--------------------+--------------------+--------------------+--------------------+
| NIDMM\_VAL\_TEMP\_ | 44004              | 1                  | 2.25 kΩ            |
| THERMISTOR\_44004  |                    |                    |                    |
+--------------------+--------------------+--------------------+--------------------+
| NIDMM\_VAL\_TEMP\_ | 44006              | 2                  | 10 kΩ              |
| THERMISTOR\_44006  |                    |                    |                    |
+--------------------+--------------------+--------------------+--------------------+
| NIDMM\_VAL\_TEMP\_ | 44007              | 3                  | 5 kΩ               |
| THERMISTOR\_44007  |                    |                    |                    |
+--------------------+--------------------+--------------------+--------------------+
''',
},
            },
        ],
'documentation': {
'description': 'Configures the thermistor type.',
},
    },
    'ConfigureThermocouple': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'thermocoupleType',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the type of thermocouple used to measure the temperature.
NI-DMM uses this value to set the Thermocouple Type property. The
default is NIDMM\_VAL\_TEMP\_TC\_J.
''',
'table_body': [['NIDMM\\_VAL\\_TEMP\\_TC\\_B', 'Thermocouple type B'], ['NIDMM\\_VAL\\_TEMP\\_TC\\_E', 'Thermocouple type E'], ['NIDMM\\_VAL\\_TEMP\\_TC\\_J', 'Thermocouple type J'], ['NIDMM\\_VAL\\_TEMP\\_TC\\_K', 'Thermocouple type K'], ['NIDMM\\_VAL\\_TEMP\\_TC\\_N', 'Thermocouple type N'], ['NIDMM\\_VAL\\_TEMP\\_TC\\_R', 'Thermocouple type R'], ['NIDMM\\_VAL\\_TEMP\\_TC\\_S', 'Thermocouple type S'], ['NIDMM\\_VAL\\_TEMP\\_TC\\_T', 'Thermocouple type T']],
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'referenceJunctionType',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the type of reference junction to be used in the reference
junction compensation of a thermocouple measurement. NI-DMM uses this
value to set the Reference Junction Type property. The only supported
value is NIDMM\_VAL\_TEMP\_REF\_JUNC\_FIXED.
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the thermocouple type and reference junction type for a
chosen thermocouple.
''',
},
    },
    'ConfigureTransducerType': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'transducerType',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the type of device used to measure the temperature. NI-DMM
uses this value to set the Transducer Type property. The default is
NIDMM\_VAL\_THERMOCOUPLE.
''',
'table_body': [['NIDMM\\_VAL\\_2\\_WIRE\\_RTD', '2-wire RTD'], ['NIDMM\\_VAL\\_4\\_WIRE\\_RTD', '4-wire RTD'], ['NIDMM\\_VAL\\_THERMISTOR', 'Thermistor'], ['NIDMM\\_VAL\\_THERMOCOUPLE', 'Thermocouple']],
},
            },
        ],
'documentation': {
'description': 'Configures the transducer type.',
},
    },
    'ConfigureTrigger': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'triggerSource',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the **trigger\_source** that initiates the acquisition. The
driver sets NIDMM\_ATTR\_TRIGGER\_SOURCE to this value. Software
configures the DMM to wait until niDMM\_SendSoftwareTrigger is called
before triggering the DMM.
''',
'note': '''
To determine which values are supported by each device, refer to the
`LabWindows/CVI Trigger
Routing <REPLACE_DRIVER_SPECIFIC_URL_1(cvitrigger_routing)>`__ section.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'triggerDelay',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the time that the DMM waits after it has received a trigger
before taking a measurement. The driver sets the
NIDMM\_ATTR\_TRIGGER\_DELAY attribute to this value. By default,
**trigger\_delay** is NIDMM\_VAL\_AUTO\_DELAY (-1), which means the DMM
waits an appropriate settling time before taking the measurement. On the
NI 4060, if you set **trigger\_delay** to 0, the DMM does not settle
before taking the measurement. The NI 4065 and NI 4070/4071/4072 use the
value specified in **trigger\_delay** as additional settling time.
''',
'note': '''
When using the NI 4050, **Trigger\_Delay** must be set to
NIDMM\_VAL\_AUTO\_DELAY (-1).
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the DMM **Trigger\_Source** and **Trigger\_Delay**. Refer to
`Triggering <REPLACE_DRIVER_SPECIFIC_URL_1(trigger)>`__ and `Using
Switches <REPLACE_DRIVER_SPECIFIC_URL_1(switch_selection)>`__ for more
information.
''',
},
    },
    'ConfigureTriggerSlope': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'triggerSlope',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the polarity of the trigger signal on which the measurement is
triggered for values of either NIDMM\_VAL\_POSITIVE or
NIDMM\_VAL\_NEGATIVE. The driver sets the NIDMM\_ATTR\_TRIGGER\_SLOPE
attribute to this value.
''',
'table_body': [['NIDMM\\_VAL\\_POSITIVE', '0', 'The driver triggers on the rising edge of the trigger signal.'], ['NIDMM\\_VAL\\_NEGATIVE (default)', '1', 'The driver triggers on the falling edge of the trigger signal.']],
},
            },
        ],
'documentation': {
'description': '''
Sets the NIDMM\_ATTR\_TRIGGER\_SLOPE attribute to either rising edge
(positive) or falling edge (negative) polarity.
''',
},
    },
    'ConfigureWaveformAcquisition': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'measurementFunction',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the **measurement\_function** used in a waveform acquisition.
The driver sets NIDMM\_ATTR\_FUNCTION to this value.
''',
'table_body': [['NIDMM\\_VAL\\_WAVEFORM\\_VOLTAGE (default)', '1003', 'Voltage Waveform'], ['NIDMM\\_VAL\\_WAVEFORM\\_CURRENT', '1004', 'Current Waveform']],
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'Range',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the expected maximum amplitude of the input signal and sets
the **range** for the **Measurement\_Function**. NI-DMM sets
NIDMM\_ATTR\_RANGE to this value. **range** values are coerced up to the
closest input **range**. The default is 10.0.

For valid ranges refer to the topics in
`Devices <REPLACE_DRIVER_SPECIFIC_URL_1(devices)>`__.

Auto-ranging is not supported during waveform acquisitions.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'Rate',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the **rate** of the acquisition in samples per second. NI-DMM
sets NIDMM\_ATTR\_WAVEFORM\_RATE to this value.

The valid **Range** is 10.0–1,800,000 S/s. **rate** values are coerced
to the closest integer divisor of 1,800,000. The default value is
1,800,000.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'waveformPoints',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the number of points to acquire before the waveform
acquisition completes. NI-DMM sets NIDMM\_ATTR\_WAVEFORM\_POINTS to this
value.

To calculate the maximum and minimum number of waveform points that you
can acquire in one acquisition, refer to the `Waveform Acquisition
Measurement Cycle <REPLACE_DRIVER_SPECIFIC_URL_1(waveform_cycle)>`__.

The default value is 500.
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the DMM for waveform acquisitions. This feature is supported
on the NI 4080/4081/4082 and the NI 4070/4071/4072.
''',
},
    },
    'ConfigureWaveformCoupling': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'waveformCoupling',
                'type': 'ViInt32',
'documentation': {
'description': '''
Selects DC or AC coupling. The driver sets
NIDMM\_ATTR\_WAVEFORM\_COUPLING to this value.
''',
'table_body': [['NIDMM\\_VAL\\_WAVEFORM\\_COUPLING\\_AC', '0', 'AC coupling'], ['NIDMM\\_VAL\\_WAVEFORM\\_COUPLING\\_DC (default)', '1', 'DC coupling']],
'table_header': ['Name', 'Value', 'Description'],
},
            },
        ],
'documentation': {
'description': '''
For the NI 4080/4081/4082 and the NI 4070/4071/4072, configures
instrument coupling for voltage waveforms.
''',
},
    },
    'Control': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'controlAction',
                'type': 'ViInt32',
'documentation': {
'description': '''
The action you want the driver to perform. Only
NIDMM\_VAL\_CONTROL\_COMMIT (0) is supported, which commits to hardware
all of the configured attributes associated with the session.
''',
},
            },
        ],
'documentation': {
'description': '''
Controls the DMM. Use this function if you want a parameter change to be
immediately reflected in the hardware. Use this function before calling
nidMM\_Initiate to make the initiate call as quickly as possible.
''',
'table_body': [['|image0|  .. |image0| image:: note.gif', '**Notes** The NI 4050 and NI 4060 are not supported. Calling this function while the DMM is taking measurements results in an error. After the DMM is finished taking measurements, calling this function will make any unfetched data points unavailable.']],
},
    },
    'Disable': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
        ],
'documentation': {
'description': '''
Places the instrument in a quiescent state where it has minimal or no
impact on the system to which it is connected. If a measurement is in
progress when this function is called, the measurement is aborted.
''',
},
    },
    'Fetch': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'maximumTime',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the **maximum\_time** allowed for this function to complete in
milliseconds. If the function does not complete within this time
interval, the function returns the NIDMM\_ERROR\_MAX\_TIME\_EXCEEDED
error code. This may happen if an external trigger has not been
received, or if the specified timeout is not long enough for the
acquisition to complete.

The valid range is 0–86400000. The default value is
NIDMM\_VAL\_TIME\_LIMIT\_AUTO (-1). The DMM calculates the timeout
automatically.
''',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'Reading',
                'type': 'ViReal64',
'documentation': {
'description': 'The measured value returned from the DMM.',
},
            },
        ],
'documentation': {
'description': '''
Returns the value from a previously initiated measurement. You must call
niDMM\_Initiate before calling this function.
''',
},
    },
    'FetchMultiPoint': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'maximumTime',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the **maximum\_time** allowed for this function to complete in
milliseconds. If the function does not complete within this time
interval, the function returns the NIDMM\_ERROR\_MAX\_TIME\_EXCEEDED
error code. This may happen if an external trigger has not been
received, or if the specified timeout is not long enough for the
acquisition to complete.

The valid range is 0–86400000. The default value is
NIDMM\_VAL\_TIME\_LIMIT\_AUTO (-1). The DMM calculates the timeout
automatically.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'arraySize',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the number of measurements to acquire. The maximum number of
measurements for a finite acquisition is the (**Trigger Count** x
**Sample Count**) parameters in niDMM\_ConfigureMultiPoint.

For continuous acquisitions, up to 100,000 points can be returned at
once. The number of measurements can be a subset. The valid range is any
positive ViInt32. The default value is 1.
''',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'readingArray',
                'type': 'ViReal64[ ]',
'documentation': {
'description': 'An array of measurement values.',
'note': '''
The size of the **Reading\_Array** must be at least the size that you
specify for the **Array\_Size** parameter.
''',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'actualNumberOfPoints',
                'type': 'ViInt32',
'documentation': {
'description': 'Indicates the number of measured values actually retrieved from the DMM.',
},
            },
        ],
'documentation': {
'description': '''
Returns an array of values from a previously initiated multipoint
measurement. The number of measurements the DMM makes is determined by
the values you specify for the **Trigger\_Count** and **Sample\_Count**
parameters of niDMM\_ConfigureMultiPoint. You must first call
niDMM\_Initiate to initiate a measurement before calling this function.
''',
},
    },
    'FetchWaveform': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'maximumTime',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the **maximum\_time** allowed for this function to complete in
milliseconds. If the function does not complete within this time
interval, the function returns the NIDMM\_ERROR\_MAX\_TIME\_EXCEEDED
error code. This may happen if an external trigger has not been
received, or if the specified timeout is not long enough for the
acquisition to complete.

The valid range is 0–86400000. The default value is
NIDMM\_VAL\_TIME\_LIMIT\_AUTO (-1). The DMM calculates the timeout
automatically.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'arraySize',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the number of waveform points to return. You specify the total
number of points that the DMM acquires in the **Waveform Points**
parameter of niDMM\_ConfigureWaveformAcquisition. The default value is
1.
''',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'waveformArray',
                'type': 'ViReal64[ ]',
'documentation': {
'description': '''
**Waveform Array** is an array of measurement values stored in waveform
data type.
''',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'actualNumberOfPoints',
                'type': 'ViInt32',
'documentation': {
'description': 'Indicates the number of measured values actually retrieved from the DMM.',
},
            },
        ],
'documentation': {
'description': '''
For the NI 4080/4081/4082 and the NI 4070/4071/4072, returns an array of
values from a previously initiated waveform acquisition. You must call
niDMM\_Initiate before calling this function.
''',
},
    },
    'FormatMeasAbsolute': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'measurementFunction',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the **measurement\_function** used to acquire the measurement.
The driver sets NIDMM\_ATTR\_FUNCTION to this value.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'Range',
                'type': 'ViReal64',
'documentation': {
'description': 'Specifies the NIDMM\_ATTR\_RANGE used to acquire the **Measurement**.',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'Resolution',
                'type': 'ViReal64',
'documentation': {
'description': 'Specifies the NIDMM\_ATTR\_RESOLUTION\_ABSOLUTE of the **Measurement**.',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'Measurement',
                'type': 'ViReal64',
'documentation': {
'description': 'Specifies the measured value returned from the DMM.',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'modeString',
                'type': 'ViChar[ ]',
'documentation': {
'description': 'Returns a string containing the units of the **Measurement** mode.',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'rangeString',
                'type': 'ViChar[ ]',
'documentation': {
'description': '''
Returns the NIDMM\_ATTR\_RANGE of the **Measurement**, formatted into a
string with the correct number of display digits.
''',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'dataString',
                'type': 'ViChar[ ]',
'documentation': {
'description': '''
Returns the **Measurement**, formatted according to the
NIDMM\_ATTR\_FUNCTION, NIDMM\_ATTR\_RANGE, and
NIDMM\_ATTR\_RESOLUTION\_ABSOLUTE.
''',
},
            },
        ],
'documentation': {
'description': '''
Formats the **Measurement** to the proper number of displayed digits
according to the **Measurement\_Function**, **Range**, and
**Resolution**. Returns the formatted data, range, and mode strings.
''',
},
    },
    'GetApertureTimeInfo': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'apertureTime',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the amount of time the DMM digitizes the input signal for a
single measurement. This parameter does not include settling time.
Returns the value of the NIDMM\_ATTR\_APERTURE\_TIME attribute. The
units of this attribute depend on the value of the
NIDMM\_ATTR\_APERTURE\_TIME\_UNITS attribute.
On the NI 4070/4071/4072, the minimum aperture time is 8.89 µs, and the
maximum aperture time is 149 s. Any number of powerline cycles (PLCs)
within the minimum and maximum ranges is allowed on the
NI 4070/4071/4072.
On the NI 4065 the minimum aperture time is 333 µs, and the maximum
aperture time is 78.2 s. If setting the number of averages directly, the
total measurement time is aperture time X the number of averages, which
must be less than 72.8 s. The aperture times allowed are 333 µs, 667 µs,
or multiples of 1.11 ms—for example 1.11 ms, 2.22 ms, 3.33 ms, and so
on. If you set an aperture time other than 333 µs, 667 µs, or multiples
of 1.11 ms, the value will be coerced up to the next supported aperture
time.
On the NI 4060, when the powerline frequency is 60, the PLCs allowed are
1 PLC, 6 PLC, 12 PLC, and 120 PLC. When the powerline frequency is 50,
the PLCs allowed are 1 PLC, 5 PLC, 10 PLC, and 100 PLC.
''',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'apertureTimeUnits',
                'type': 'ViInt32',
'documentation': {
'description': '''
Indicates the units of aperture time as powerline cycles (PLCs) or
seconds. Returns the value of the NIDMM\_ATTR\_APERTURE\_TIME\_UNITS
attribute.
''',
'table_body': [['NIDMM\\_VAL\\_SECONDS', '0', 'Seconds'], ['NIDMM\\_VAL\\_POWER\\_LINE\\_CYCLES', '1', 'Powerline Cycles']],
},
            },
        ],
'documentation': {
'description': 'Returns the DMM **Aperture\_Time** and **Aperture\_Time\_Units**.',
},
    },
    'GetAttributeViBoolean': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
This parameter is ignored. National Instruments DMMs do not support
channel names since they only have a single channel. This parameter is
included in order to support interchangeability and upgradability to
multiple channel DMMs.

The default value is " " (an empty string).
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'Pass the ID of an attribute.',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'attributeValue',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Returns the current value of the attribute. Pass the address of a
ViBoolean variable.
''',
},
            },
        ],
'documentation': {
'description': '''
Queries the value of a ViBoolean attribute. You can use this function to
get the values of instrument-specific attributes and inherent IVI
attributes.

If the attribute represents an instrument state, this function performs
instrument I/O in the following cases:

-  State caching is disabled for the entire session or for the
   particular attribute.
-  State caching is enabled, and the currently cached value is invalid.
''',
},
    },
    'GetAttributeViInt32': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
This parameter is ignored. National Instruments DMMs do not support
channel names since they only have a single channel. This parameter is
included in order to support interchangeability and upgradability to
multiple channel DMMs.

The default value is " " (an empty string).
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'Pass the ID of an attribute.',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'attributeValue',
                'type': 'ViInt32',
'documentation': {
'description': '''
Returns the current value of the attribute. Pass the address of a
ViInt32 variable.
''',
},
            },
        ],
'documentation': {
'description': '''
Queries the value of a ViInt32 attribute. You can use this function to
get the values of instrument-specific attributes and inherent IVI
attributes.

If the attribute represents an instrument state, this function performs
instrument I/O in the following cases:

-  State caching is disabled for the entire session or for the
   particular attribute.
-  State caching is enabled, and the currently cached value is invalid.
''',
},
    },
    'GetAttributeViReal64': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
This parameter is ignored. National Instruments DMMs do not support
channel names since they only have a single channel. This parameter is
included in order to support interchangeability and upgradability to
multiple channel DMMs.

The default value is " " (an empty string).
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'Pass the ID of an attribute.',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'attributeValue',
                'type': 'ViReal64',
'documentation': {
'description': '''
Returns the current value of the attribute. Pass the address of a
ViReal64 variable.
''',
},
            },
        ],
'documentation': {
'description': '''
Queries the value of a ViReal64 attribute. You can use this function to
get the values of instrument-specific attributes and inherent IVI
attributes.

If the attribute represents an instrument state, this function performs
instrument I/O in the following cases:

-  State caching is disabled for the entire session or for the
   particular attribute.
-  State caching is enabled, and the currently cached value is invalid.
''',
},
    },
    'GetAttributeViSession': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
This parameter is ignored. National Instruments DMMs do not support
channel names since they only have a single channel. This parameter is
included in order to support interchangeability and upgradability to
multiple channel DMMs.

The default value is " " (an empty string).
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'Pass the ID of an attribute.',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'attributeValue',
                'type': 'ViSession',
'documentation': {
'description': '''
Returns the current value of the attribute. Pass the address of a
ViSession variable.
''',
},
            },
        ],
'documentation': {
'description': '''
Queries the value of a ViSession attribute. You can use this function to
get the values of instrument-specific attributes and inherent IVI
attributes.

If the attribute represents an instrument state, this function performs
instrument I/O in the following cases:

-  State caching is disabled for the entire session or for the
   particular attribute.
-  State caching is enabled, and the currently cached value is invalid.
''',
},
    },
    'GetAttributeViString': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
This parameter is ignored. National Instruments DMMs do not support
channel names since they only have a single channel. This parameter is
included in order to support interchangeability and upgradability to
multiple channel DMMs.

The default value is " " (an empty string).
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'Pass the ID of an attribute.',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'bufferSize',
                'type': 'ViInt32',
'documentation': {
'description': '''
Pass the number of bytes in the ViChar array you specify for the
**Attribute\_Value** parameter.

If the current value of the attribute, including the terminating NULL
byte, contains more bytes that you indicate in this parameter, the
function copies **buffer\_size**—1 bytes into the buffer, places an
ASCII NUL byte at the end of the buffer, and returns the buffer size you
must pass to get the entire value. For example, if the value is "123456"
and the **buffer\_size** is 4, the function places "123" into the buffer
and returns 7.

If you pass a negative number, the function copies the value to the
buffer regardless of the number of bytes in the value. If you pass 0,
you can pass VI\_NULL for the **Attribute\_Value** buffer parameter.
''',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'attributeValue',
                'type': 'ViChar[ ]',
'documentation': {
'description': '''
The buffer in which the function returns the current value of the
attribute. The buffer must be of type ViChar and have at least as many
bytes as indicated in the **Buffer\_Size** parameter.

If you specify 0 for the **Buffer\_Size** parameter, you can pass
VI\_NULL for this parameter.
''',
},
            },
        ],
'documentation': {
'description': '''
Queries the value of a ViString attribute. You can use this function to
get the values of instrument-specific attributes and inherent IVI
attributes.

If the attribute represents an instrument state, this function performs
instrument I/O in the following cases:

-  State caching is disabled for the entire session or for the
   particular attribute.
-  State caching is enabled, and the currently cached value is invalid.
   You must provide a ViChar array to serve as a buffer for the value.
   You pass the number of bytes in the buffer as the Array Size
   parameter.
''',
},
    },
    'GetAutoRangeValue': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'actualRange',
                'type': 'ViReal64',
'documentation': {
'description': '''
Indicates the **actual\_range** the DMM is using. Returns the value of
the NIDMM\_ATTR\_AUTO\_RANGE\_VALUE attribute. The units of the returned
value depend on the function.
''',
},
            },
        ],
'documentation': {
'description': '''
Returns the **Actual\_Range** that the DMM is using, even when Auto
Range is off.
''',
},
    },
    'GetCalCount': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'calType',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the type of calibration performed (external or
self-calibration).
''',
'note': 'The NI 4065 does not support self-calibration.',
'table_body': [['NIDMM\\_VAL\\_INTERNAL\\_AREA (default)', '0', 'Self-Calibration'], ['NIDMM\\_VAL\\_EXTERNAL\\_AREA', '1', 'External Calibration']],
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'Count',
                'type': 'ViInt32',
'documentation': {
'description': 'The number of times calibration has been performed.',
},
            },
        ],
'documentation': {
'description': 'Returns the calibration **Count** for the specified type of calibration.',
'note': 'The NI 4050, NI 4060, and NI 4080/4081/4082 are not supported.',
},
    },
    'GetCalDateAndTime': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'calType',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the type of calibration performed (external or
self-calibration).
''',
'note': 'The NI 4065 does not support self-calibration.',
'table_body': [['NIDMM\\_VAL\\_INTERNAL\\_AREA (default)', '0', 'Self-Calibration'], ['NIDMM\\_VAL\\_EXTERNAL\\_AREA', '1', 'External Calibration']],
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'Month',
                'type': 'ViInt32',
'documentation': {
'description': 'Indicates the **month** of the last calibration.',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'Day',
                'type': 'ViInt32',
'documentation': {
'description': 'Indicates the **day** of the last calibration.',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'Year',
                'type': 'ViInt32',
'documentation': {
'description': 'Indicates the **year** of the last calibration.',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'Hour',
                'type': 'ViInt32',
'documentation': {
'description': 'Indicates the **hour** of the last calibration.',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'Minute',
                'type': 'ViInt32',
'documentation': {
'description': 'Indicates the **minute** of the last calibration.',
},
            },
        ],
'documentation': {
'description': 'Returns the date and time of the last calibration performed.',
'note': 'The NI 4050 and NI 4060 are not supported.',
},
    },
    'GetCalUserDefinedInfo': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'bufferSize',
                'type': 'ViInt32',
'documentation': {
'description': '''
Passes the number of bytes in the ViString you specify for the **Info**
parameter.

If zero is passed for this parameter, the **buffer\_size** needed to
store the information is returned. If the Info parameter, including the
terminating NULL byte, contains more bytes than you indicate in this
parameter, the function copies **buffer\_size** - 1 bytes into the
buffer, places an ASCII NULL byte at the end of the buffer, and returns
the **buffer\_size** you must pass to get the entire value.

For example, if the value is "123456" and the **buffer\_size** is 4, the
function places "123" into the buffer and returns 7. If you pass a
negative number, the function copies the value to the buffer regardless
of the number of bytes in the value.
''',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'Info',
                'type': 'ViChar[ ]',
'documentation': {
'description': '''
Returns the user-defined calibration information stored in the EEPROM.
If this is NULL, the **Buffer\_Size** needed to store the information is
returned.
''',
},
            },
        ],
'documentation': {
'description': 'Returns the user-defined calibration information stored in the EEPROM.',
'note': 'The NI 4050 and NI 4060 are not supported.',
},
    },
    'GetCalUserDefinedInfoMaxSize': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'infoSize',
                'type': 'ViInt32',
'documentation': {
'description': '''
Returns the value of maximum string length that can be stored in the
EEPROM using niDMM\_SetCalUserDefinedInfo. The **info\_size** value is
given in characters, but it does not include the termination character.
''',
},
            },
        ],
'documentation': {
'description': '''
Returns the maximum string length that can be stored in the EEPROM. Use
niDMM\_SetCalUserDefinedInfo to store user-defined information.
''',
'note': 'The NI 4050 and NI 4060 are not supported.',
},
    },
    'GetChannelName': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'Index',
                'type': 'ViInt32',
'documentation': {
'description': 'A 1–based **index** into the channel table.',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'bufferSize',
                'type': 'ViInt32',
'documentation': {
'description': '''
Passes the number of bytes in the ViChar array you specify for the
**Channel\_String** parameter. If the next **Channel\_String**,
including the terminating NULL byte, contains more bytes than you
indicate in this parameter, the function copies
**buffer\_size** –1 bytes into the buffer, places an ASCII NULL byte at
the end of the buffer, and returns the buffer size you must pass to get
the entire value.

For example, if the value is "123456" and the **buffer\_size** is 4, the
function places "123" into the buffer and returns 7. If you pass a
negative number, the function copies the value to the buffer regardless
of the number of bytes in the value. If you pass 0, you can pass
VI\_NULL for the **Channel\_String** buffer parameter. The default value
is None.
''',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'channelString',
                'type': 'ViChar[ ]',
'documentation': {
'description': '''
Returns the **channel\_string** that is in the channel table at the
**Index** you specify. Do not modify the contents of the
**channel\_string**.
''',
},
            },
        ],
'documentation': {
'description': '''
Returns the **Channel\_String** that is in the channel table at an
**Index** you specify. Not applicable to National Instruments DMMs.
Included for compliance with the *IviDmm Class Specification*.
''',
},
    },
    'GetDevTemp': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'Options',
                'type': 'ViString',
'documentation': {
'description': 'Reserved.',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'Temperature',
                'type': 'ViReal64',
'documentation': {
'description': 'Returns the current **temperature** of the device.',
},
            },
        ],
'documentation': {
'description': 'Returns the current **Temperature** of the device.',
'note': 'The NI 4050 and NI 4060 are not supported.',
},
    },
    'GetError': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'errorCode',
                'type': 'ViStatus',
'documentation': {
'description': '''
Returns the **error\_code** for the session or execution thread. If you
pass 0 for the **Buffer\_Size**, you can pass VI\_NULL for this
parameter.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'bufferSize',
                'type': 'ViInt32',
'documentation': {
'description': '''
Passes the number of bytes in the ViChar array you specify for the
**Description** parameter. If the error description, including the
terminating NULL byte, contains more bytes than you indicate in this
parameter, the function copies **buffer\_size** –1 bytes into the
buffer, places an ASCII NULL byte at the end of the buffer, and returns
the **buffer\_size** you must pass to get the entire value.

For example, if the value is "123456" and the **buffer\_size** is 4, the
function places "123" into the buffer and returns 7. If you pass a
negative number, the function copies the value to the buffer regardless
of the number of bytes in the value. If you pass 0, you can pass
VI\_NULL for the **Description** buffer parameter. The default value is
None.
''',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'Description',
                'type': 'ViChar[ ]',
'documentation': {
'description': '''
Returns the error **description** for the IVI session or execution
thread. If there is no **description**, the function returns an empty
string. The buffer must contain at least as many elements as the value
you specify with the **Buffer\_Size** parameter. If you pass 0 for the
**Buffer\_Size**, you can pass VI\_NULL for this parameter.
''',
},
            },
        ],
'documentation': {
'description': '''
Returns the error information associated with the
**Instrument\_Handle**. This function retrieves and then clears the
error information for the session. If you leave the
**Instrument\_Handle** unwired, this function retrieves and then clears
the error information for the process.
''',
},
    },
    'GetErrorMessage': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. You can also use
VI\_NULL if you do not have a valid **vi**.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'errorCode',
                'type': 'ViStatus',
'documentation': {
'description': '''
The error code returned from the instrument for which you want to get a
user-readable string.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'Buffer_Size',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the number of bytes allocated for the **Error\_Message**
ViChar array. If the error description that this function returns
(including terminating NULL byte) is larger than you indicated in
**buffer\_\_size**, the error description will be truncated to fit. If
you pass 0 for **buffer\_\_size**, the function returns the buffer size
needed for **Error\_Message**.
''',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'errorMessage',
                'type': 'ViChar[ ]',
'documentation': {
'description': '''
Contains the error information formatted into a user-readable string.
The buffer must contain at least as many elements as the value you
specify with the **Buffer\_Size** parameter. If you pass 0 for
**Buffer\_Size**, you can pass VI\_NULL for this parameter.
''',
},
            },
        ],
'documentation': {
'description': '''
Returns the **Error\_Message** as a user-readable string for the
provided **Error\_Code**. Calling this function with a **Buffer\_Size**
of 0 returns the size needed for the **Error\_Message**.
''',
},
    },
    'GetExtCalRecommendedInterval': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'Months',
                'type': 'ViInt32',
'documentation': {
'description': '''
Returns the recommended number of **months** between external
calibrations.
''',
},
            },
        ],
'documentation': {
'description': '''
Returns the recommended interval between external recalibration in
**Months**.
''',
'note': 'The NI 4050 and NI 4060 are not supported.',
},
    },
    'GetLastCalTemp': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'calType',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the type of calibration performed (external or
self-calibration).
''',
'note': 'The NI 4065 does not support self-calibration.',
'table_body': [['NIDMM\\_VAL\\_INTERNAL\\_AREA (default)', '0', 'Self-Calibration'], ['NIDMM\\_VAL\\_EXTERNAL\\_AREA', '1', 'External Calibration']],
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'Temperature',
                'type': 'ViReal64',
'documentation': {
'description': 'Returns the **temperature** during the last calibration.',
},
            },
        ],
'documentation': {
'description': 'Returns the **Temperature** during the last calibration procedure.',
'note': 'The NI 4050 and NI 4060 are not supported.',
},
    },
    'GetMeasurementPeriod': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'Period',
                'type': 'ViReal64',
'documentation': {
'description': '''
Returns the number of seconds it takes to make one measurement.

The first measurement in a multipoint acquisition requires additional
settling time. This function does not include this additional time or
any NIDMM\_ATTR\_TRIGGER\_DELAY associated with the first measurement.
Time required for internal measurements, such as
NIDMM\_ATTR\_AUTO\_ZERO, is included.
''',
},
            },
        ],
'documentation': {
'description': '''
Returns the measurement **Period**, which is the amount of time it takes
to complete one measurement with the current configuration. Use this
function right before you begin acquiring data—after you have completely
configured the measurement and after all configuration functions have
been called.
''',
},
    },
    'GetNextCoercionRecord': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'bufferSize',
                'type': 'ViInt32',
'documentation': {
'description': '''
Passes the number of bytes in the ViChar array you specify for the
**Coercion\_Record** parameter. If the next coercion record string,
including the terminating NULL byte, contains more bytes than you
indicate in this parameter, the function copies **buffer\_size** – 1
bytes into the buffer, places an ASCII NULL byte at the end of the
buffer, and returns the buffer size you must pass to get the entire
value.

For example, if the value is "123456" and the **buffer\_size** is 4, the
function places "123" into the buffer and returns 7. If you pass a
negative number, the function copies the value to the buffer regardless
of the number of bytes in the value.

If you pass 0, you can pass VI\_NULL for the **Coercion\_Record** buffer
parameter.

The default value is None.
''',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'coercionRecord',
                'type': 'ViChar[ ]',
'documentation': {
'description': '''
Returns the next **coercion\_record** for the IVI session.

If there are no coercions records, the function returns an empty string.
The buffer must contain at least as many elements as the value you
specify with the **Buffer\_Size** parameter.
''',
},
            },
        ],
'documentation': {
'description': '''
This function returns the coercion information associated with the IVI
session, and it retrieves and clears the oldest instance in which NI-DMM
coerced a value you specified to another value.

If you set NIDMM\_ATTR\_RECORD\_COERCIONS to VI\_TRUE (1), NI-DMM keeps
a list of all coercions it makes on ViInt32 or ViReal64 values that you
pass to NI-DMM functions. Use this function to retrieve information from
that list.
''',
},
    },
    'GetNextInterchangeWarning': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'bufferSize',
                'type': 'ViInt32',
'documentation': {
'description': '''
Passes the number of bytes in the ViChar array you specify for the
**Interchange\_Warning** parameter. If the next interchangeability
warning string, including the terminating NULL byte, contains more bytes
than you indicate in this parameter, the function copies
**buffer\_size** –1 bytes into the buffer, places an ASCII NULL byte at
the end of the buffer, and returns the buffer size you must pass to get
the entire value.

For example, if the value is "123456" and the **buffer\_size** is 4, the
function places "123" into the buffer and returns 7. If you pass a
negative number, the function copies the value to the buffer regardless
of the number of bytes in the value. If you pass 0, you can pass
VI\_NULL for the **Interchange\_Warning** buffer parameter. The default
value is None.
''',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'interchangeWarning',
                'type': 'ViChar[ ]',
'documentation': {
'description': '''
Returns the next interchange warning for the IVI session. If there are
no interchange warnings, the function returns an empty string. The
buffer must contain at least as many elements as the value you specify
with the **Buffer\_Size** parameter.
''',
},
            },
        ],
'documentation': {
'description': '''
This function returns the interchangeability warnings associated with
the IVI session. It retrieves and clears the oldest instance in which
the class driver recorded an interchangeability warning.
Interchangeability warnings indicate that using your application with a
different instrument might cause different behavior.

The driver performs interchangeability checking when
NIDMM\_ATTR\_INTERCHANGE\_CHECK is set to VI\_TRUE (1). The function
returns an empty string in the **Interchange\_Warning** parameter if no
interchangeability warnings remain for the session. In general, the
instrument driver generates interchangeability warnings when an
attribute that affects the behavior of the instrument is in a state that
you did not specify.
''',
},
    },
    'GetSelfCalSupported': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'selfCalSupported',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Returns whether Self Cal is supported for the device specified by the
given session.
''',
'table_body': [['VI\\_TRUE', '1', 'The DMM that you are using can perform self-calibration.'], ['VI\\_FALSE', '0', 'The DMM that you are using cannot perform self-calibration.']],
},
            },
        ],
'documentation': {
'description': '''
Returns a Boolean value that expresses whether or not the DMM that you
are using can perform self-calibration.
''',
},
    },
    'InitExtCal': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'resourceName',
                'type': 'ViString',
'documentation': {
'caution': '''
All IVI names for the **Resource\_Name**, such as logical names or
virtual names, are case-sensitive. If you use logical names, driver
session names, or virtual names in your program, you must make sure that
the name you use matches the name in the IVI Configuration Store file
exactly, without any variations in the case of the characters in the
name.
''',
'description': '''
| Contains the **resource\_name** of the device to initialize. The
  **resource\_name** is assigned in Measurement & Automation Explorer
  (MAX). Refer to `Related
  Documentation <REPLACE_DRIVER_SPECIFIC_URL_1(related_documentation)>`__
  for the *NI Digital Multimeters Getting Started Guide* for more
  information about configuring and testing the DMM in MAX.
| Valid Syntax:

-  NI-DAQmx name
-  DAQ::NI-DAQmx name[::INSTR]
-  DAQ::Traditional NI-DAQ device number[::INSTR]
-  IVI logical name
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'calibrationPassword',
                'type': 'ViChar[ ]',
'documentation': {
'description': '''
Specifies the password required to enable external calibration
functionality.

The maximum password string length is eight characters, excluding the
termination character. "NI" is the factory-default password.
''',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The session handle that you obtain from niDMM\_InitExtCal. The handle
identifies a particular instrument calibration session.
''',
},
            },
        ],
'documentation': {
'description': '''
The following operations are performed if the **Calibration\_Password**
is valid:

-  Creates a new session for external calibration to the device you
   specify for the **Resource\_Name** parameter.
-  Resets the device and prepares the EEPROM for new calibration
   coefficients.
-  Returns a ViSession handle that you use to identify the instrument in
   all calibration adjustments and post-adjustment verification steps.

After opening a calibration session, the device cannot take valid
measurements using this session until the device has been properly
adjusted. Once the adjustment phase is complete, you can use this
session to verify the new calibration constants. After verification, you
have the option of saving the new calibration constants or reverting to
the previous calibration constants by specifying the **Action**
parameter in niDMM\_CloseExtCal.

If you encounter a fatal error such as a power failure or system crash
while performing an external calibration, you can call
niDMM\_RestoreLastExtCalConstants to return the device to a usable
state.
''',
'table_body': [['|image0|  .. |image0| image:: note.gif', '**Notes**', 'The NI 4050 and NI 4060 are not supported. Refer to the *NI 4065 6½ Digit DMM Calibration Procedure*, the *NI 4070/4072 6½ Digit FlexDMM Calibration Procedure*, or the *NI 4071 7½–Digit FlexDMM Calibration Procedure* before using this function. This function creates a new session the first time you invoke it for a device. If you call this function on the same resource, an error is returned. You should use niDMM\\_CloseExtCal to close a session obtained using this function.']],
},
    },
    'InitWithOptions': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'resourceName',
                'type': 'ViString',
'documentation': {
'caution': '''
All IVI names for the **Resource\_Name**, such as logical names or
virtual names, are case-sensitive. If you use logical names, driver
session names, or virtual names in your program, you must make sure that
the name you use matches the name in the IVI Configuration Store file
exactly, without any variations in the case of the characters in the
name.
''',
'description': '''
| Contains the **resource\_name** of the device to initialize. The
  **resource\_name** is assigned in Measurement & Automation Explorer
  (MAX). Refer to `Related
  Documentation <REPLACE_DRIVER_SPECIFIC_URL_1(related_documentation)>`__
  for the *NI Digital Multimeters Getting Started Guide* for more
  information about configuring and testing the DMM in MAX.
| Valid Syntax:

-  NI-DAQmx name
-  DAQ::NI-DAQmx name[::INSTR]
-  DAQ::Traditional NI-DAQ device number[::INSTR]
-  IVI logical name
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'idQuery',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Verifies that the device you initialize is one that the driver supports.
NI-DMM automatically performs this query, so setting this parameter is
not necessary.
Defined Values:
''',
'table_body': [['VI\\_TRUE (default)', '1', 'Perform ID Query'], ['VI\\_FALSE', '0', 'Skip ID Query']],
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'resetDevice',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether to reset the instrument during the initialization
procedure.
Defined Values:
''',
'table_body': [['VI\\_TRUE (default)', '1', 'Reset Device'], ['VI\\_FALSE', '0', "Don't Reset"]],
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'optionString',
                'type': 'ViString',
'documentation': {
'description': '''
| Sets the initial value of certain attributes for the session. The
  following table specifies the attribute name, attribute constant, and
  default value for each attribute that you can use in this parameter:

The format of this string is, "AttributeName=Value." To set multiple
attributes, separate their assignments with a comma.

If you pass NULL or an empty string for this parameter, the session uses
the default values for the attributes. You can override the default
values by assigning a value explicitly in an **option\_string**
parameter. You do not have to specify all of the attributes and may
leave any of them out (those left out use the default value).

Refer to `Simulating NI Digital
Multimeters <REPLACE_DRIVER_SPECIFIC_URL_1(simulation)>`__ for more
information.
''',
'table_body': [['Check', 'NIDMM\\_ATTR\\_RANGE\\_CHECK', 'VI\\_TRUE', '1'], ['QueryInstrStatus', 'NIDMM\\_ATTR\\_QUERY\\_INSTR\\_STATUS', 'VI\\_FALSE', '0'], ['Cache', 'NIDMM\\_ATTR\\_CACHE', 'VI\\_TRUE', '1'], ['Simulate', 'NIDMM\\_ATTR\\_SIMULATE', 'VI\\_FALSE', '0'], ['RecordCoercions', 'NIDMM\\_ATTR\\_RECORD\\_COERCIONS', 'VI\\_FALSE', '0'], ['DriverSetup', 'NIDMM\\_ATTR\\_DRIVER\\_SETUP', '"" (empty string)', '""']],
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Returns a ViSession handle that you use to identify the instrument in
all subsequent instrument driver function calls.
''',
},
            },
        ],
'documentation': {
'description': '''
This function completes the following tasks:

-  Creates a new IVI instrument driver session and, optionally, sets the
   initial state of the following session attributes:
   NIDMM\_ATTR\_RANGE\_CHECK, NIDMM\_ATTR\_QUERY\_INSTR\_STATUS,
   NIDMM\_ATTR\_CACHE, NIDMM\_ATTR\_SIMULATE,
   NIDMM\_ATTR\_RECORD\_COERCIONS.
-  Opens a session to the device you specify for the **Resource\_Name**
   parameter. If the **ID\_Query** parameter is set to VI\_TRUE, this
   function queries the instrument ID and checks that it is valid for
   this instrument driver.
-  If the **Reset\_Device** parameter is set to VI\_TRUE, this function
   resets the instrument to a known state. Sends initialization commands
   to set the instrument to the state necessary for the operation of the
   instrument driver.
-  Returns a ViSession handle that you use to identify the instrument in
   all subsequent instrument driver function calls.
''',
},
    },
    'Initiate': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
        ],
'documentation': {
'description': '''
Initiates an acquisition. After you call this function, the DMM leaves
the Idle state and enters the Wait-for-Trigger state. If trigger is set
to Immediate mode, the DMM begins acquiring measurement data. Use
niDMM\_Fetch, niDMM\_FetchMultiPoint, or niDMM\_FetchWaveform to
retrieve the measurement data.
''',
},
    },
    'IsOverRange': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'measurementValue',
                'type': 'ViReal64',
'documentation': {
'description': 'The measured value returned from the DMM.',
'note': '''
If an overrange condition occurs, the **Measurement\_Value** contains
an IEEE-defined NaN (Not a Number) value.
''',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'isOverRange',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Returns whether the measurement value is a valid measurement or an
overrange condition.
''',
'table_body': [['VI\\_TRUE', '1', 'The value indicates that an overrange condition occurred.'], ['VI\\_FALSE', '0', 'The value is a valid measurement.']],
},
            },
        ],
'documentation': {
'description': '''
Takes a **Measurement\_Value** and determines if the value is a valid
measurement or a value indicating that an overrange condition occurred.
''',
},
    },
    'IsUnderRange': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'measurementValue',
                'type': 'ViReal64',
'documentation': {
'description': 'The measured value returned from the DMM.',
'note': '''
If an overrange condition occurs, the **Measurement\_Value** contains
an IEEE-defined NaN (Not a Number) value.
''',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'isUnderRange',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Returns whether the **Measurement\_Value** is a valid measurement or an
underrange condition.
''',
'table_body': [['VI\\_TRUE', '1', 'The value indicates that an underrange condition occurred.'], ['VI\\_FALSE', '0', 'The value is a valid measurement.']],
},
            },
        ],
'documentation': {
'description': '''
Takes a **Measurement\_Value** and determines if the value is a valid
measurement or a value indicating that an underrange condition occurred.
''',
},
    },
    'LockSession': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'callerHasLock',
                'type': 'ViBoolean',
'documentation': {
'description': '''
This parameter serves as a convenience. If you do not want to use this
parameter, pass VI\_NULL. Use this parameter in complex functions to
keep track of whether you obtain a lock and, therefore, need to unlock
the session. To use this parameter, complete the following steps:

#. Pass the address of a local ViBoolean variable.
#. In the declaration of the local variable, initialize it to VI\_FALSE
   (0).
#. Pass the address of the same local variable to any other calls you
   make to this function or niDMM\_UnlockSession in the same function.

The parameter is an input/output parameter. This function and
niDMM\_UnlockSession each inspect the current value and take the
following actions:

If the value is VI\_TRUE (1), this function does not lock the session
again. If the value is VI\_FALSE, this function obtains the lock and
sets the value of the parameter to VI\_TRUE.

If the value is VI\_FALSE, niDMM\_UnlockSession does not attempt to
unlock the session. If the value is VI\_TRUE, niDMM\_UnlockSession
releases the lock and sets the value of the parameter to VI\_FALSE.
Thus, you can, call niDMM\_UnlockSession at the end of your function
without worrying about whether you actually have the lock.

**Example**

ViStatus TestFunc (ViSession vi, ViInt32 flags)

{

| ViStatus error = VI\_SUCCESS;
| ViBoolean haveLock = VI\_FALSE;
| if (flags & BIT\_1)

| {
| viCheckErr( NIDMM\_LockSession(vi, &haveLock;));
| viCheckErr( TakeAction1(vi));
| if (flags & BIT\_2)

{

viCheckErr( NIDMM\_UnlockSession(vi, &haveLock;));

viCheckErr( TakeAction2(vi));

viCheckErr( NIDMM\_LockSession(vi, &haveLock;);

}

if (flags & BIT\_3)

viCheckErr( TakeAction3(vi));

}

Error:

/\*

At this point, you cannot really be sure that you have the lock.
Fortunately, the haveLock variable takes care of that for you.

\*/

niDMM\_UnlockSession(vi, &haveLock;);

return error;

}
''',
},
            },
        ],
'documentation': {
'description': '''
This function obtains a multithread lock on the instrument session.
Before it does so, it waits until all other execution threads have
released their locks on the instrument session.

Other threads might have obtained a lock on this session in the
following ways:

-  The user application called this function.
-  A call to the instrument driver locked the session.
-  A call to the IVI Library locked the session.

After your call to this function returns successfully, no other threads
can access the instrument session until you call niDMM\_UnlockSession.

Use this function and niDMM\_UnlockSession around a sequence of calls to
instrument driver functions if you require that the instrument retain
its settings through the end of the sequence. You can safely make nested
calls to this function within the same thread.

To completely unlock the session, you must balance each call to this
function with a call to niDMM\_UnlockSession. If, however, you use the
**Caller\_Has\_Lock** parameter in all calls to this function and
niDMM\_UnlockSession within a function, the IVI Library locks the
session only once within the function regardless of the number of calls
you make to this function. This feature allows you to call
niDMM\_UnlockSession just once at the end of the function.
''',
},
    },
    'PerformOpenCableComp': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'Conductance',
                'type': 'ViReal64',
'documentation': {
'description': '''
**conductance** is the measured value of open cable compensation
**conductance**.
''',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'Susceptance',
                'type': 'ViReal64',
'documentation': {
'description': '''
**susceptance** is the measured value of open cable compensation
**susceptance**.
''',
},
            },
        ],
'documentation': {
'description': '''
For the NI 4082 and NI 4072 only, performs the open cable compensation
measurements for the current capacitance/inductance range, and returns
open cable compensation **Conductance** and **Susceptance** values. You
can use the return values of this function as inputs to
niDMM\_ConfigureOpenCableCompValues.

This function returns an error if the value of the NIDMM\_ATTR\_FUNCTION
attribute is not set to NIDMM\_VAL\_CAPACITANCE (1005) or
NIDMM\_VAL\_INDUCTANCE (1006).
''',
},
    },
    'PerformShortCableComp': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'Resistance',
                'type': 'ViReal64',
'documentation': {
'description': '''
**resistance** is the measured value of short cable compensation
**resistance**.
''',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'Reactance',
                'type': 'ViReal64',
'documentation': {
'description': '''
**reactance** is the measured value of short cable compensation
**reactance**.
''',
},
            },
        ],
'documentation': {
'description': '''
Performs the short cable compensation measurements for the current
capacitance/inductance range, and returns short cable compensation
**Resistance** and **Reactance** values. You can use the return values
of this function as inputs to niDMM\_ConfigureShortCableCompValues.

This function returns an error if the value of the NIDMM\_ATTR\_FUNCTION
attribute is not set to NIDMM\_VAL\_CAPACITANCE (1005) or
NIDMM\_VAL\_INDUCTANCE (1006).
''',
},
    },
    'Read': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'maximumTime',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the **maximum\_time** allowed for this function to complete in
milliseconds. If the function does not complete within this time
interval, the function returns the NIDMM\_ERROR\_MAX\_TIME\_EXCEEDED
error code. This may happen if an external trigger has not been
received, or if the specified timeout is not long enough for the
acquisition to complete.

The valid range is 0–86400000. The default value is
NIDMM\_VAL\_TIME\_LIMIT\_AUTO (-1). The DMM calculates the timeout
automatically.
''',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'Reading',
                'type': 'ViReal64',
'documentation': {
'description': 'The measured value returned from the DMM.',
},
            },
        ],
'documentation': {
'description': 'Acquires a single measurement and returns the measured value.',
},
    },
    'ReadMultiPoint': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'maximumTime',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the **maximum\_time** allowed for this function to complete in
milliseconds. If the function does not complete within this time
interval, the function returns the NIDMM\_ERROR\_MAX\_TIME\_EXCEEDED
error code. This may happen if an external trigger has not been
received, or if the specified timeout is not long enough for the
acquisition to complete.

The valid range is 0–86400000. The default value is
NIDMM\_VAL\_TIME\_LIMIT\_AUTO (-1). The DMM calculates the timeout
automatically.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'arraySize',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the number of measurements to acquire. The maximum number of
measurements for a finite acquisition is the (**Trigger Count** x
**Sample Count**) parameters in niDMM\_ConfigureMultiPoint.

For continuous acquisitions, up to 100,000 points can be returned at
once. The number of measurements can be a subset. The valid range is any
positive ViInt32. The default value is 1.
''',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'readingArray',
                'type': 'ViReal64[ ]',
'documentation': {
'description': 'An array of measurement values.',
'note': '''
The size of the **Reading\_Array** must be at least the size that you
specify for the **Array\_Size** parameter.
''',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'actualNumberOfPoints',
                'type': 'ViInt32',
'documentation': {
'description': 'Indicates the number of measured values actually retrieved from the DMM.',
},
            },
        ],
'documentation': {
'description': '''
Acquires multiple measurements and returns an array of measured values.
The number of measurements the DMM makes is determined by the values you
specify for the **Trigger\_Count** and **Sample\_Count** parameters in
niDMM\_ConfigureMultiPoint.
''',
},
    },
    'ReadStatus': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'acquisitionBacklog',
                'type': 'ViInt32',
'documentation': {
'description': '''
The number of measurements available to be read. If the backlog
continues to increase, data is eventually overwritten, resulting in an
error.
''',
'note': '''
On the NI 4060, the **Backlog** does not increase when autoranging. On
the NI 4065, the **Backlog** does not increase when Range is set to AUTO
RANGE ON (-1), or before the first point is fetched when Range is set to
AUTO RANGE ONCE (-3). These behaviors are due to the autorange model of
the devices.
''',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'acquisitionStatus',
                'type': 'ViInt16',
'documentation': {
'description': '''
Indicates status of the acquisition. The following table shows the
acquisition states:
''',
'table_body': [['0', 'Running'], ['1', 'Finished with backlog'], ['2', 'Finished with no backlog'], ['3', 'Paused'], ['4', 'No acquisition in progress']],
},
            },
        ],
'documentation': {
'description': '''
Returns measurement backlog and acquisition status. Use this function to
determine how many measurements are available before calling
niDMM\_Fetch, niDMM\_FetchMultiPoint, or niDMM\_FetchWaveform.
''',
'note': 'The NI 4050 is not supported.',
},
    },
    'ReadWaveform': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'maximumTime',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the **maximum\_time** allowed for this function to complete in
milliseconds. If the function does not complete within this time
interval, the function returns the NIDMM\_ERROR\_MAX\_TIME\_EXCEEDED
error code. This may happen if an external trigger has not been
received, or if the specified timeout is not long enough for the
acquisition to complete.

The valid range is 0–86400000. The default value is
NIDMM\_VAL\_TIME\_LIMIT\_AUTO (-1). The DMM calculates the timeout
automatically.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'arraySize',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the number of waveform points to return. You specify the total
number of points that the DMM acquires in the **Waveform Points**
parameter of niDMM\_ConfigureWaveformAcquisition. The default value is
1.
''',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'waveformArray',
                'type': 'ViReal64[ ]',
'documentation': {
'description': 'An array of measurement values.',
'note': '''
The size of the **Waveform\_Array** must be at least the size that you
specify for the **Array\_Size** parameter.
''',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'actualNumberOfPoints',
                'type': 'ViInt32',
'documentation': {
'description': 'Indicates the number of measured values actually retrieved from the DMM.',
},
            },
        ],
'documentation': {
'description': '''
For the NI 4080/4081/4082 and the NI 4070/4071/4072, acquires a waveform
and returns data as an array of values or as a waveform data type. The
number of elements in the **Waveform\_Array** is determined by the
values you specify for the **Waveform\_Points** parameter in
niDMM\_ConfigureWaveformAcquisition.
''',
},
    },
    'ResetInterchangeCheck': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
        ],
'documentation': {
'description': '''
When developing a complex test system that consists of multiple test
modules, it is generally a good idea to design the test modules so that
they can run in any order. To do so requires ensuring that each test
module completely configures the state of each instrument it uses.

If a particular test module does not completely configure the state of
an instrument, the state of the instrument depends on the configuration
from a previously executed test module. If you execute the test modules
in a different order, the behavior of the instrument and therefore the
entire test module is likely to change. This change in behavior is
generally instrument specific and represents an interchangeability
problem. You can use this function to test for such cases. After you
call this function, the interchangeability checking algorithms in NI-DMM
ignore all previous configuration operations. By calling this function
at the beginning of a test module, you can determine whether the test
module has dependencies on the operation of previously executed test
modules.

This function does not clear the interchangeability warnings from the
list of previously recorded interchangeability warnings. If you want to
guarantee that niDMM\_GetNextInterchangeWarning only returns those
interchangeability warnings that are generated after calling this
function, you must clear the list of interchangeability warnings. You
can clear the interchangeability warnings list by repeatedly calling
niDMM\_GetNextInterchangeWarning until no more interchangeability
warnings are returned. If you are not interested in the content of those
warnings, you can call niDMM\_ClearInterchangeWarnings.
''',
},
    },
    'ResetWithDefaults': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
        ],
'documentation': {
'description': '''
Resets the instrument to a known state and sends initialization commands
to the DMM. The initialization commands set the DMM settings to the
state necessary for the operation of NI-DMM. All user-defined default
values associated with a logical name are applied after setting the DMM.
''',
},
    },
    'RestoreLastExtCalConstants': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
        ],
'documentation': {
'description': '''
Reverts the device to the calibration constants from the last complete
external calibration. This function recovers the hardware if a fatal
system error should occur during an external or self-calibration
procedure.

After calling this function, you should call niDMM\_SelfCal before
taking measurements with the device to adjust the device for any
temperature drifts since the last external calibration.
''',
'note': 'The NI 4050, NI 4060, and NI 4080/4081/4082 are not supported.',
},
    },
    'SelfCal': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
        ],
'documentation': {
'description': '''
For the NI 4080/4081/4082 and the NI 4070/4071/4072, executes the
self-calibration routine to maintain measurement accuracy.
''',
'note': '''
This function calls niDMM\_reset, and any configurations previous to
the call will be lost. All attributes will be set to their default
values after the call returns.
''',
},
    },
    'SendSoftwareTrigger': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
        ],
'documentation': {
'description': '''
Sends a command to trigger the DMM. Call this function if you have
configured either the NIDMM\_ATTR\_TRIGGER\_SOURCE or
NIDMM\_ATTR\_SAMPLE\_TRIGGER attributes. If the
NIDMM\_ATTR\_TRIGGER\_SOURCE and/or NIDMM\_ATTR\_SAMPLE\_TRIGGER
attributes are set to NIDMM\_VAL\_EXTERNAL or NIDMM\_VAL\_TTL\ *n*, you
can use this function to override the trigger source that you configured
and trigger the device. The NI 4050 and NI 4060 are not supported.
''',
},
    },
    'SetAttributeViBoolean': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
This parameter is ignored. National Instruments DMMs do not support
channel names since they only have a single channel. This parameter is
included in order to support interchangeability and upgradability to
multiple channel DMMs.

The default value is " " (an empty string).
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'Pass the ID of an attribute.',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeValue',
                'type': 'ViBoolean',
'documentation': {
'description': 'Pass the value that you want to set the attribute to.',
},
            },
        ],
'documentation': {
'description': '''
This function sets the value of a ViBoolean attribute.

This is a low-level function that you can use to set the values of
instrument-specific attributes and inherent IVI attributes.

If the attribute represents an instrument state, this function performs
instrument I/O in the following cases:

-  State caching is disabled for the entire session or for the
   particular attribute.
-  State caching is enabled, and the currently cached value is invalid
   or is different than the value you specify.

This instrument driver contains high-level functions that set most of
the instrument attributes. It is best to use the high-level driver
functions as much as possible. They handle order dependencies and
multithread locking for you. In addition, they perform status checking
only after setting all of the attributes.

In contrast, when you set multiple attributes using the SetAttribute
functions, the functions check the instrument status after each call.
Also, when state caching is enabled, the high-level functions that
configure multiple attributes perform instrument I/O only for the
attributes whose value you change. Thus, you can safely call the
high-level functions without the penalty of redundant instrument I/O.
''',
},
    },
    'SetAttributeViInt32': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
This parameter is ignored. National Instruments DMMs do not support
channel names since they only have a single channel. This parameter is
included in order to support interchangeability and upgradability to
multiple channel DMMs.

The default value is " " (an empty string).
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'Pass the ID of an attribute.',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeValue',
                'type': 'ViInt32',
'documentation': {
'description': 'Pass the value that you want to set the attribute to.',
},
            },
        ],
'documentation': {
'description': '''
This function sets the value of a ViInt32 attribute.

This is a low-level function that you can use to set the values of
instrument-specific attributes and inherent IVI attributes.

If the attribute represents an instrument state, this function performs
instrument I/O in the following cases:

-  State caching is disabled for the entire session or for the
   particular attribute.
-  State caching is enabled, and the currently cached value is invalid
   or is different than the value you specify.

This instrument driver contains high-level functions that set most of
the instrument attributes. It is best to use the high-level driver
functions as much as possible. They handle order dependencies and
multithread locking for you. In addition, they perform status checking
only after setting all of the attributes.

In contrast, when you set multiple attributes using the SetAttribute
functions, the functions check the instrument status after each call.
Also, when state caching is enabled, the high-level functions that
configure multiple attributes perform instrument I/O only for the
attributes whose value you change. Thus, you can safely call the
high-level functions without the penalty of redundant instrument I/O.
''',
},
    },
    'SetAttributeViReal64': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
This parameter is ignored. National Instruments DMMs do not support
channel names since they only have a single channel. This parameter is
included in order to support interchangeability and upgradability to
multiple channel DMMs.

The default value is " " (an empty string).
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'Pass the ID of an attribute.',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeValue',
                'type': 'ViReal64',
'documentation': {
'description': 'Pass the value that you want to set the attribute to.',
},
            },
        ],
'documentation': {
'description': '''
This function sets the value of a ViReal64 attribute.

This is a low-level function that you can use to set the values of
instrument-specific attributes and inherent IVI attributes.

If the attribute represents an instrument state, this function performs
instrument I/O in the following cases:

-  State caching is disabled for the entire session or for the
   particular attribute.
-  State caching is enabled, and the currently cached value is invalid
   or is different than the value you specify.

This instrument driver contains high-level functions that set most of
the instrument attributes. It is best to use the high-level driver
functions as much as possible. They handle order dependencies and
multithread locking for you. In addition, they perform status checking
only after setting all of the attributes.

In contrast, when you set multiple attributes using the SetAttribute
functions, the functions check the instrument status after each call.
Also, when state caching is enabled, the high-level functions that
configure multiple attributes perform instrument I/O only for the
attributes whose value you change. Thus, you can safely call the
high-level functions without the penalty of redundant instrument I/O.
''',
},
    },
    'SetAttributeViSession': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
This parameter is ignored. National Instruments DMMs do not support
channel names since they only have a single channel. This parameter is
included in order to support interchangeability and upgradability to
multiple channel DMMs.

The default value is " " (an empty string).
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'Pass the ID of an attribute.',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeValue',
                'type': 'ViSession',
'documentation': {
'description': 'Pass the value that you want to set the attribute to.',
},
            },
        ],
'documentation': {
'description': '''
This function sets the value of a ViSession attribute.

This is a low-level function that you can use to set the values of
instrument-specific attributes and inherent IVI attributes.

If the attribute represents an instrument state, this function performs
instrument I/O in the following cases:

-  State caching is disabled for the entire session or for the
   particular attribute.
-  State caching is enabled, and the currently cached value is invalid
   or is different than the value you specify.
''',
},
    },
    'SetAttributeViString': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
This parameter is ignored. National Instruments DMMs do not support
channel names since they only have a single channel. This parameter is
included in order to support interchangeability and upgradability to
multiple channel DMMs.

The default value is " " (an empty string).
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'Pass the ID of an attribute.',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeValue',
                'type': 'ViChar[ ]',
'documentation': {
'description': 'Pass the value that you want to set the attribute to.',
},
            },
        ],
'documentation': {
'description': '''
This function sets the value of a ViString attribute.

This is a low-level function that you can use to set the values of
instrument-specific attributes and inherent IVI attributes.

If the attribute represents an instrument state, this function performs
instrument I/O in the following cases:

-  State caching is disabled for the entire session or for the
   particular attribute.
-  State caching is enabled, and the currently cached value is invalid
   or is different than the value you specify.

This instrument driver contains high-level functions that set most of
the instrument attributes. It is best to use the high-level driver
functions as much as possible. They handle order dependencies and
multithread locking for you. In addition, they perform status checking
only after setting all of the attributes.

In contrast, when you set multiple attributes using the SetAttribute
functions, the functions check the instrument status after each call.
Also, when state caching is enabled, the high-level functions that
configure multiple attributes perform instrument I/O only for the
attributes whose value you change. Thus, you can safely call the
high-level functions without the penalty of redundant instrument I/O.
''',
},
    },
    'SetCalPassword': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'oldPassword',
                'type': 'ViChar[ ]',
'documentation': {
'description': '''
Specifies the current password required to enable external calibration
functionality. The maximum password string length is eight characters,
excluding the termination character.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'newPassword',
                'type': 'ViChar[ ]',
'documentation': {
'description': '''
Specifies the **new\_password** required to enable external calibration
functionality. The maximum password string length is eight characters,
excluding the termination character.
''',
},
            },
        ],
'documentation': {
'description': '''
Changes the password required to enable external calibration
functionality for the specified instrument. The maximum password string
length is eight characters, excluding the termination character. "NI" is
the default password.
''',
'table_body': [['|image0|  .. |image0| image:: note.gif', '**Notes**', 'The NI 4050 and NI 4060 are not supported. A password is required for external calibration. Be sure to record the password in a secure location.']],
},
    },
    'SetCalUserDefinedInfo': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'Info',
                'type': 'ViChar[ ]',
'documentation': {
'description': '''
Specifies the user-defined information to be stored in the EEPROM such
as the operator who performed the calibration operation or system
information. Use niDMM\_GetCalUserDefinedinfoMaxSize to learn the
maximum string size that is allowed. If the **info** string size is
larger than the maximum string size, NI-DMM stores as much of the
information as possible, truncates the remainder, and return a warning.
''',
},
            },
        ],
'documentation': {
'description': '''
Stores the user-defined information in the EEPROM. Use
niDMM\_GetCalUserDefinedInfoMaxSize to learn the maximum string size
that is allowed. If the **Info** string size is larger than the maximum
string size, NI-DMM stores as much of the information as possible,
truncates the remainder, and returns a warning.
''',
'note': 'The NI 4050 and NI 4060 are not supported.',
},
    },
    'UnlockSession': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'callerHasLock',
                'type': 'ViBoolean',
'documentation': {
'description': '''
This parameter serves as a convenience. If you do not want to use this
parameter, pass VI\_NULL.

Use this parameter in complex functions to keep track of whether you
obtain a lock and, therefore, need to unlock the session.

To use this parameter, complete the following steps:

#. Pass the address of a local ViBoolean variable.
#. In the declaration of the local variable, initialize it to VI\_FALSE
   (0).
#. Pass the address of the same local variable to any other calls you
   make to niDMM\_LockSession or this function in the same function.

The parameter is an input/output parameter. niDMM\_LockSession and this
function each inspect the current value and take the following actions:

If the value is VI\_TRUE (1), niDMM\_LockSession does not lock the
session again. If the value is VI\_FALSE, niDMM\_LockSession obtains the
lock and sets the value of the parameter to VI\_TRUE.

If the value is VI\_FALSE, this function does not attempt to unlock the
session. If the value is VI\_TRUE, this function releases the lock and
sets the value of the parameter to VI\_FALSE. Thus, you can, call this
function at the end of your function without worrying about whether you
actually have the lock.

**Example**

ViStatus TestFunc (ViSession vi, ViInt32 flags)

{

ViStatus error = VI\_SUCCESS;

ViBoolean haveLock = VI\_FALSE;

if (flags & BIT\_1)

{

viCheckErr( NIDMM\_LockSession(vi, &haveLock;));

viCheckErr( TakeAction1(vi));

if (flags & BIT\_2)

{

viCheckErr( NIDMM\_UnlockSession(vi, &haveLock;));

viCheckErr( TakeAction2(vi));

viCheckErr( NIDMM\_LockSession(vi, &haveLock;);

}

if (flags & BIT\_3)

viCheckErr( TakeAction3(vi));

}

Error:

/\*

At this point, you cannot really be sure that you have the lock.
Fortunately, the haveLock variable takes care of that for you.

\*/

niDMM\_UnlockSession(vi, &haveLock;);

return error;

}
''',
},
            },
        ],
'documentation': {
'description': '''
This function releases a lock that you acquired on an instrument session
using niDMM\_LockSession. Refer to niDMM\_LockSession for additional
information on session locks.
''',
},
    },
    'close': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
        ],
'documentation': {
'description': 'Closes the specified session and deallocates resources that it reserved.',
},
    },
    'error_message': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'errorCode',
                'type': 'ViStatus',
'documentation': {
'description': '''
The **error\_code** returned from the instrument. The default is 0,
indicating VI\_SUCCESS.
''',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'errorMessage',
                'type': 'ViChar[ ]',
'documentation': {
'description': 'The error information formatted into a string.',
},
            },
        ],
'documentation': {
'description': '''
Takes the **Error\_Code** returned by the instrument driver functions,
interprets it, and returns it as a user-readable string.
''',
},
    },
    'error_query': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'errorCode',
                'type': 'ViStatus',
'documentation': {
'description': '''
The **error\_code** returned from the instrument.

The default value is VI\_SUCCESS (0).
''',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'errorMessage',
                'type': 'ViChar[ ]',
'documentation': {
'description': 'Formats the **Error\_Code** into a user-readable message string.',
'note': 'The array must contain at least 256 elements ViChar[256].',
},
            },
        ],
'documentation': {
'description': '''
Reads an **Error\_Code** and message from the DMM error queue. National
Instruments DMMs do not contain an error queue. Errors are reported as
they occur. Therefore, this function does not detect errors; it is
included for compliance with the *IviDmm Class Specification*.
''',
},
    },
    'init': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'resourceName',
                'type': 'ViString',
'documentation': {
'caution': '''
All IVI names for the **Resource\_Name**, such as logical names or
virtual names, are case-sensitive. If you use logical names, driver
session names, or virtual names in your program, you must make sure that
the name you use matches the name in the IVI Configuration Store file
exactly, without any variations in the case of the characters in the
name.
''',
'description': '''
| Contains the **resource\_name** of the device to initialize. The
  **resource\_name** is assigned in Measurement & Automation Explorer
  (MAX). Refer to `Related
  Documentation <REPLACE_DRIVER_SPECIFIC_URL_1(related_documentation)>`__
  for the *NI Digital Multimeters Getting Started Guide* for more
  information about configuring and testing the DMM in MAX.
| Valid Syntax:

-  NI-DAQmx name
-  DAQ::NI-DAQmx name[::INSTR]
-  DAQ::Traditional NI-DAQ device number[::INSTR]
-  IVI logical name
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'idQuery',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Verifies that the device you initialize is one that the driver supports.
NI-DMM automatically performs this query, so setting this parameter is
not necessary.
Defined Values:
''',
'table_body': [['VI\\_TRUE (default)', '1', 'Perform ID Query'], ['VI\\_FALSE', '0', 'Skip ID Query']],
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'resetDevice',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether to reset the instrument during the initialization
procedure.
Defined Values:
''',
'table_body': [['VI\\_TRUE (default)', '1', 'Reset Device'], ['VI\\_FALSE', '0', "Don't Reset"]],
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Returns a ViSession handle that you use to identify the instrument in
all subsequent instrument driver function calls.
''',
},
            },
        ],
'documentation': {
'description': '''
This function completes the following tasks:

-  Creates a new IVI instrument driver session.
-  Opens a session to the device you specify for the **Resource\_Name**
   parameter.

-  If the **ID\_Query** parameter is set to VI\_TRUE (1), this function
   queries the instrument ID and checks that it is valid for this
   instrument driver.

-  If the **Reset\_Device** parameter is set to VI\_TRUE (1), this
   function resets the instrument to a known state. Sends initialization
   commands to set the instrument to the state necessary for the
   operation of the instrument driver.

-  Returns a ViSession handle that you use to identify the instrument in
   all subsequent instrument driver function calls.
''',
},
    },
    'reset': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
        ],
'documentation': {
'description': '''
Resets the instrument to a known state and sends initialization commands
to the instrument. The initialization commands set instrument settings
to the state necessary for the operation of the instrument driver.
''',
},
    },
    'revision_query': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'instrumentDriverRevision',
                'type': 'ViChar[ ]',
'documentation': {
'description': '''
Returns a string containing the instrument driver software revision
numbers.
''',
'note': 'The array must contain at least 256 elements ViChar[256].',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'firmwareRevision',
                'type': 'ViChar[ ]',
'documentation': {
'description': '''
Returns a string containing the instrument **firmware\_revision**
numbers.
''',
'note': 'The array must contain at least 256 elements ViChar[256].',
},
            },
        ],
'documentation': {
'description': '''
Returns the revision numbers of the instrument driver and instrument
firmware.
''',
},
    },
    'self_test': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from niDMM\_init or niDMM\_InitWithOptions. The default is
None.
''',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'selfTestResult',
                'type': 'ViInt16',
'documentation': {
'description': '''
Contains the value returned from the instrument self-test. Zero
indicates success.

On the NI 4080/4082 and NI 4070/4072, the error code 1013 indicates that
you should check the fuse and replace it, if necessary.
''',
'note': '''
Self-test does not check the fuse on the NI 4065, NI 4071, and
NI 4081. Hence, even if the fuse is blown on the device, self-test does
not return error code 1013.
''',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'selfTestMessage',
                'type': 'ViChar[ ]',
'documentation': {
'description': '''
This parameter contains the string returned from the instrument
self-test. The array must contain at least 256 elements.

For the NI 4050 and NI 4060, the error codes returned for self-test
failures include the following:

-  NIDMM\_ERROR\_AC\_TEST\_FAILURE
-  NIDMM\_ERROR\_DC\_TEST\_FAILURE
-  NIDMM\_ERROR\_RESISTANCE\_TEST\_FAILURE

These error codes indicate that the DMM should be repaired.

For the NI 4080/4081/4082 and the NI 4070/4071/4072, the error code
returned for a self-test failure is NIDMM\_ERROR\_SELF\_TEST\_FAILURE.
This error code indicates that the DMM should be repaired.
''',
},
            },
        ],
'documentation': {
'description': '''
Performs a self-test on the DMM to ensure that the DMM is functioning
properly. Self-test does not calibrate the DMM.
''',
'note': '''
This function calls niDMM\_reset, and any configurations previous to
the call will be lost. All attributes will be set to their default
values after the call returns.
''',
},
    },
}
