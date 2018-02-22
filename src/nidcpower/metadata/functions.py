
# -*- coding: utf-8 -*-
# This file is code generated, do not make changes here
#  If the generated information is not correct for python
#  changes can be made in functions_addon.py and they will be
#  applied at build time


functions = {
    'Abort': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
        ],
'documentation': {
'description': '''
Transitions the NI-DCPower session from the Running state to the
Committed state. If a sequence is running, it is stopped. Any
configuration functions called after this function are not applied until
the niDCPower_Initiate function is called. If power output is enabled
when you call the niDCPower_Abort function, the output channels remain
in their current state and continue providing power.

Use the niDCPower_ConfigureOutputEnabled function to disable power
output on a per channel basis. Use the niDCPower_reset function to
disable output on all channels.

Refer to the `Programming
States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic in
the *NI DC Power Supplies and SMUs Help* for information about the
specific NI-DCPower software states.

**Related Topics:**

`Programming
States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__
''',
},
    },
    'CalAdjustCurrentLimit': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument calibration session. **vi** is
obtained from the niDCPower_InitExtCal function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': 'Specifies the channel name to which these calibration settings apply.',
},
            },
            {
                'direction': 'in',
                'name': 'Range',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the range to calibrate with these settings. Only one channel
at a time may be calibrated.
''',
},
            },
            {
                'direction': 'in',
                'name': 'numberOfMeasurements',
                'type': 'ViUInt32',
'documentation': {
'description': '''
Specifies the number of elements in **requestedOutputs** and
**measuredOutputs**.
''',
},
            },
            {
                'direction': 'in',
                'name': 'requestedOutputs',
                'type': 'ViReal64[]',
'documentation': {
'description': '''
Specifies an array of the output values that were requested in the
niDCPower_ConfigureCurrentLimit function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'measuredOutputs',
                'type': 'ViReal64[]',
'documentation': {
'description': '''
Specifies an array of the output values measured by an external
precision digital multimeter.
''',
},
            },
        ],
'documentation': {
'description': '''
Calculates the calibration constants for the current limit for the
specified output channel and range. This function compares the array in
**requestedOutputs** to the array in **measuredOutputs** and calculates
the calibration constants for the current limit returned by the device.
Refer to the calibration procedure for the device you are calibrating
for detailed instructions on the appropriate use of this function. This
function can only be called from an external calibration session.
''',
'note': '''
This function is not supported on all devices. Refer to `Supported
Functions by
Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
for more information about supported devices.
''',
},
    },
    'CalAdjustCurrentMeasurement': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument calibration session. **vi** is
obtained from the niDCPower_InitExtCal function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel name to which these calibration settings
apply.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Range',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the range to calibrate with these settings. Only one channel
at a time may be calibrated.
''',
},
            },
            {
                'direction': 'in',
                'name': 'numberOfMeasurements',
                'type': 'ViUInt32',
'documentation': {
'description': '''
Specifies the number of elements in **reportedOutputs** and
**measuredOutputs**.
''',
},
            },
            {
                'direction': 'in',
                'name': 'reportedOutputs',
                'type': 'ViReal64[]',
'documentation': {
'description': '''
Specifies an array of the output values that were returned by the
niDCPower_Measure function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'measuredOutputs',
                'type': 'ViReal64[]',
'documentation': {
'description': '''
Specifies an array of the output values measured by an external
precision digital multimeter.
''',
},
            },
        ],
'documentation': {
'description': '''
Calibrates the current measurements returned by the niDCPower_Measure
function for the specified output channel. This function calculates new
calibration coefficients for the specified current measurement range
based on the **reportedOutputs** and **measuredOutputs**. Refer to the
calibration procedure for the device you are calibrating for detailed
instructions about the appropriate use of this function. This function
can only be called in an external calibration session.
''',
},
    },
    'CalAdjustInternalReference': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'internalReference',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the internal reference to be adjusted.
**Defined Values**:
''',
'table_body': [['NIDCPOWER_VAL_INTERNAL_REFERENCE_5V (1054)', 'Calibration pin connected to 5 V internal reference.'], ['NIDCPOWER_VAL_INTERNAL_REFERENCE_100KOHM (1055)', 'Calibration pin connected to 100 kΩ internal reference.']],
},
            },
            {
                'direction': 'in',
                'name': 'adjustedInternalReference',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the updated value of the internal reference that will be
programmed to the device.
''',
},
            },
        ],
'documentation': {
'description': '''
Programs the adjusted reference value to the device. Refer to the
calibration procedure for the device you are calibrating for detailed
instructions on the appropriate use of this function. This function can
only be called from an external calibration session.
''',
'note': '''
This function is not supported on all devices. Refer to `Supported
Functions by
Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
for more information about supported devices.
''',
},
    },
    'CalAdjustOutputResistance': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument calibration session. **vi** is
obtained from the niDCPower_InitExtCal function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel name to which these calibration settings
apply. Only one channel at a time can be calibrated.
''',
},
            },
            {
                'direction': 'in',
                'name': 'numberOfMeasurements',
                'type': 'ViUInt32',
'documentation': {
'description': '''
Specifies the number of elements in **requestedOutputs** and
**measuredOutputs**.
''',
},
            },
            {
                'direction': 'in',
                'name': 'requestedOutputs',
                'type': 'ViReal64[]',
'documentation': {
'description': '''
Specifies an array of the output values that were requested in the
niDCPower_ConfigureOutputResistance function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'measuredOutputs',
                'type': 'ViReal64[]',
'documentation': {
'description': '''
Specifies an array of the output values measured by an external
precision digital multimeter.
''',
},
            },
        ],
'documentation': {
'description': '''
Compares the array in **requestedOutputs** to the array in
**measuredOutputs** and calculates the calibration constants for the
output resistance of the specified channel. Refer to the calibration
procedure for the device you are calibrating for detailed instructions
on the appropriate use of this function. This function can only be
called from an external calibration session.
''',
'note': '''
This function is not supported on all devices. Refer to `Supported
Functions by
Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
for more information about supported devices.
''',
},
    },
    'CalAdjustResidualCurrentOffset': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel(s) to which this configuration value
applies. Specify multiple channels by using a channel list or a channel
range. A channel list is a comma (,) separated sequence of channel names
(for example, 0,2 specifies channels 0 and 2). A channel range is a
lower bound channel followed by a hyphen (-) or colon (:) followed by an
upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
In the Running state, multiple output channel configurations are
performed sequentially based on the order specified in this parameter.
''',
},
            },
        ],
'documentation': {
'description': '''
Calculates the calibration constants for the residual current offsets
for the specified output channel. Residual offsets account for minor
offset effects on the device that lie outside of the self-calibration
circuitry. These offsets can include multiplexer input offsets and
leakage effects from internal switching.

This function requires that the output be open prior to it being
invoked.

Refer to the calibration procedure for the device you are calibrating
for detailed instructions on the appropriate use of this function. This
function can be called only in an external calibration session.
''',
'note': '''
This function is not supported on all devices. Refer to `Supported
Functions by
Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
for more information about supported devices.
''',
},
    },
    'CalAdjustResidualVoltageOffset': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel(s) to which this configuration value
applies. Specify multiple channels by using a channel list or a channel
range. A channel list is a comma (,) separated sequence of channel names
(for example, 0,2 specifies channels 0 and 2). A channel range is a
lower bound channel followed by a hyphen (-) or colon (:) followed by an
upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
In the Running state, multiple output channel configurations are
performed sequentially based on the order specified in this parameter.
''',
},
            },
        ],
'documentation': {
'description': '''
Calculates the calibration constants for the residual voltage offsets
for the specified output channel. Residual offsets account for minor
offset effects on the device that lie outside of the self-calibration
circuitry. These offsets can include multiplexer input offsets and
leakage effects from internal switching.

This function requires that the output be shorted prior to it being
invoked.

Refer to the calibration procedure for the device you are calibrating
for detailed instructions on the appropriate use of this function. This
function can be called only in an external calibration session.
''',
'note': '''
This function is not supported on all devices. Refer to `Supported
Functions by
Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
for more information about supported devices.
''',
},
    },
    'CalAdjustVoltageLevel': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument calibration session. **vi** is
obtained from the niDCPower_InitExtCal function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': 'Specifies the output channel to which these calibration settings apply.',
},
            },
            {
                'direction': 'in',
                'name': 'Range',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the range to calibrate with these settings. Only one channel
at a time may be calibrated.
''',
},
            },
            {
                'direction': 'in',
                'name': 'numberOfMeasurements',
                'type': 'ViUInt32',
'documentation': {
'description': '''
Specifies the number of elements in **requestedOutputs** and
**measuredOutputs**.
''',
},
            },
            {
                'direction': 'in',
                'name': 'requestedOutputs',
                'type': 'ViReal64[]',
'documentation': {
'description': '''
Specifies an array of the output values requested in the
niDCPower_ConfigureVoltageLevel function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'measuredOutputs',
                'type': 'ViReal64[]',
'documentation': {
'description': '''
Specifies an array of the output values measured by an external
precision digital multimeter.
''',
},
            },
        ],
'documentation': {
'description': '''
Calculates the calibration constants for the voltage level for the
specified output channel. This function compares the array in
**requestedOutputs** to the array in **measuredOutputs** and calculates
the calibration constants for the voltage level of the output channel.
Refer to the calibration procedure of the device you are calibrating for
detailed instructions on the appropriate use of this function. This
function can be called only in an external calibration session.
''',
'note': '''
This function is not supported on all devices. Refer to `Supported
Functions by
Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
for more information about supported devices.
''',
},
    },
    'CalAdjustVoltageMeasurement': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument calibration session. **vi** is
obtained from the niDCPower_InitExtCal function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': 'Specifies the channel name to which these calibration settings apply.',
},
            },
            {
                'direction': 'in',
                'name': 'Range',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the range to calibrate with these settings. Only one channel
at a time may be calibrated.
''',
},
            },
            {
                'direction': 'in',
                'name': 'numberOfMeasurements',
                'type': 'ViUInt32',
'documentation': {
'description': '''
Specifies the number of elements in **reportedOutputs** and
**measuredOutputs**.
''',
},
            },
            {
                'direction': 'in',
                'name': 'reportedOutputs',
                'type': 'ViReal64[]',
'documentation': {
'description': '''
Specifies an array of the output values that were returned by the
niDCPower_Measure function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'measuredOutputs',
                'type': 'ViReal64[]',
'documentation': {
'description': '''
Specifies an array of the output values measured by an external
precision digital multimeter.
''',
},
            },
        ],
'documentation': {
'description': '''
Calculates the calibration constants for the voltage measurements
returned by the niDCPower_Measure function for the specified output
channel. This function compares the array in **reportedOutputs** to the
array in **measuredOutputs** and calculates the calibration constants
for the voltage measurements returned by the niDCPower_Measure
function. Refer to the calibration procedure for the device you are
calibrating for detailed instructions on the appropriate use of this
function. This function can only be called in an external calibration
session.
''',
},
    },
    'CalSelfCalibrate': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel(s) to which this configuration value
applies. Specify multiple channels by using a channel list or a channel
range. A channel list is a comma (,) separated sequence of channel names
(for example, 0,2 specifies channels 0 and 2). A channel range is a
lower bound channel followed by a hyphen (-) or colon (:) followed by an
upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
In the Running state, multiple output channel configurations are
performed sequentially based on the order specified in this parameter.
''',
},
            },
        ],
'documentation': {
'description': '''
Performs a self-calibration upon the specified channel(s).

This function disables the output, performs several internal
calculations, and updates calibration values. The updated calibration
values are written to the device hardware if the
NIDCPOWER_ATTR_SELF_CALIBRATION_PERSISTENCE attribute is set to
NIDCPOWER_VAL_WRITE_TO_EEPROM. Refer to the
NIDCPOWER_ATTR_SELF_CALIBRATION_PERSISTENCE attribute topic for more
information about the settings for this attribute.

When calling niDCPower_CalSelfCalibrate with the PXIe-4162/4163,
specify all channels of your PXIe-4162/4163 with the channelName input.
You cannot self-calibrate a subset of PXIe-4162/4163 channels.

Refer to the
`Self-Calibration <REPLACE_DRIVER_SPECIFIC_URL_1(selfcal)>`__ topic for
more information about this function.

**Related Topics:**

`Self-Calibration <REPLACE_DRIVER_SPECIFIC_URL_1(selfcal)>`__
''',
'note': '''
This function is not supported on all devices. Refer to `Supported
Functions by
Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
for more information about supported devices.
''',
},
    },
    'ChangeExtCalPassword': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitExtCal or niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'oldPassword',
                'type': 'ViChar[]',
'documentation': {
'description': 'Specifies the previous password used to protect the calibration values.',
},
            },
            {
                'direction': 'in',
                'name': 'newPassword',
                'type': 'ViChar[]',
'documentation': {
'description': 'Specifies the new password to use to protect the calibration values.',
},
            },
        ],
'documentation': {
'description': '''
Changes the **password** that is required to initialize an external
calibration session. The **password** can be a maximum of four
alphanumeric characters. If you call this function in a session,
**password** is changed immediately. If you call this function in an
external calibration session, **password** is changed only after you
close the session using the niDCPower_CloseExtCal function with
**action** set to NIDCPOWER_VAL_COMMIT.
''',
},
    },
    'ClearError': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
        ],
'documentation': {
'description': '''
| Clears the error code and error description for the IVI session. If
  the user specifies a valid IVI session for **vi**, this function
  clears the error information for the session. If the user passes
  VI_NULL for **vi**, this function clears the error information for
  the current execution thread. If the ViSession parameter is an invalid
  session, the function does nothing and returns an error.
| The function clears the error code by setting it to VI_SUCCESS. If
  the error description string is non-NULL, the function de-allocates
  the error description string and sets the address to VI_NULL.
| Maintaining the error information separately for each thread is useful
  if the user does not have a session handle to pass to the
  niDCPower_GetError function, which occurs when a call to
  niDCPower_InitializeWithChannels fails.
''',
},
    },
    'ClearInterchangeWarnings': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
        ],
'documentation': {
'description': 'Clears the list of current interchange warnings.',
},
    },
    'CloseExtCal': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument calibration session. **vi** is
obtained from the niDCPower_InitExtCal function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Action',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies how to use the calibration values from this session as the
session is closed.

**Defined Values**:
''',
'table_body': [['NIDCPOWER_VAL_COMMIT (1002)', 'The new calibration constants are stored in the EEPROM.'], ['NIDCPOWER_VAL_CANCEL (1001)', 'The old calibration constants are kept, and the new ones are discarded.']],
},
            },
        ],
'documentation': {
'description': '''
Closes the session specified in **vi** and deallocates the resources
that NI-DCPower reserved for calibration. Refer to the calibration
procedure for the device you are calibrating for detailed instructions
on the appropriate use of this function.
''',
},
    },
    'Commit': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
        ],
'documentation': {
'description': '''
Applies previously configured settings to the device. Calling this
function moves the NI-DCPower session from the Uncommitted state into
the Committed state. After calling this function, modifying any
attribute reverts the NI-DCPower session to the Uncommitted state. Use
the niDCPower_Initiate function to transition to the Running state.
Refer to the `Programming
States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic in
the *NI DC Power Supplies and SMUs Help* for details about the specific
NI-DCPower software states.

**Related Topics:**

`Programming
States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__
''',
},
    },
    'ConfigureApertureTime': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel(s) to which this configuration value
applies. Specify multiple channels by using a channel list or a channel
range. A channel list is a comma (,) separated sequence of channel names
(for example, 0,2 specifies channels 0 and 2). A channel range is a
lower bound channel followed by a hyphen (-) or colon (:) followed by an
upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
In the Running state, multiple output channel configurations are
performed sequentially based on the order specified in this parameter.
''',
},
            },
            {
                'direction': 'in',
                'name': 'apertureTime',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the aperture time. Refer to the *Aperture Time* topic for your
device in the *NI DC Power Supplies and SMUs Help* for more information.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Units',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the units for **apertureTime**.
**Defined Values**:
''',
'table_body': [['NIDCPOWER_VAL_SECONDS (1028)', 'Specifies seconds.'], ['NIDCPOWER_VAL_POWER_LINE_CYCLES (1029)', 'Specifies Power Line Cycles.']],
},
            },
        ],
'documentation': {
'description': '''
Configures the aperture time on the specified channel(s).

The supported values depend on the **units**. Refer to the *Aperture
Time* topic for your device in the *NI DC Power Supplies and SMUs Help*
for more information. In general, devices support discrete
**apertureTime** values, and if you configure **apertureTime** to some
unsupported value, NI-DCPower coerces it up to the next supported value.

Refer to the *Measurement Configuration and Timing* or *DC Noise
Rejection* topic for your device in the *NI DC Power Supplies and SMUs
Help* for more information about how to configure your measurements.

**Related Topics:**

`Aperture Time <REPLACE_DRIVER_SPECIFIC_URL_1(aperture)>`__
''',
'note': '''
This function is not supported on all devices. Refer to `Supported
Functions by
Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
for more information about supported devices.
''',
},
    },
    'ConfigureAutoZero': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel(s) to which this configuration value
applies. Specify multiple channels by using a channel list or a channel
range. A channel list is a comma (,) separated sequence of channel names
(for example, 0,2 specifies channels 0 and 2). A channel range is a
lower bound channel followed by a hyphen (-) or colon (:) followed by an
upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
In the Running state, multiple output channel configurations are
performed sequentially based on the order specified in this parameter.
''',
},
            },
            {
                'direction': 'in',
                'name': 'autoZero',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the auto-zero setting. Refer to the *Measurement Configuration
and Timing* topic and the *Auto Zero* topic for your device for more
information about how to configure your measurements.
**Defined Values:**
''',
'table_body': [['NIDCPOWER_VAL_OFF (0)', 'Disables auto-zero.'], ['NIDCPOWER_VAL_ONCE (1024)', 'Makes zero conversions following the first measurement after initiating the device. The device uses these zero conversions for the preceding measurement and future measurements until the device is reinitiated.'], ['NIDCPOWER_VAL_ON (1)', 'Makes zero conversions for every measurement.']],
},
            },
        ],
'documentation': {
'description': '''
Configures auto zero for the device.

Refer to the `NI PXI-4132 Auto
Zero <REPLACE_DRIVER_SPECIFIC_URL_1(4132_autozero)>`__ and `NI PXI-4132
Measurement Configuration and
Timing <REPLACE_DRIVER_SPECIFIC_URL_1(4132_measureconfigtiming)>`__
topics in the *NI DC Power Supplies and SMUs Help* for more information
about how to configure your measurements.

**Related Topics:**

`Auto Zero <REPLACE_DRIVER_SPECIFIC_URL_1(autozero)>`__
''',
'note': '''
This function is not supported on all devices. Refer to `Supported
Functions by
Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
for more information about supported devices.
''',
},
    },
    'ConfigureCurrentLevel': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel(s) to which this configuration value
applies. Specify multiple channels by using a channel list or a channel
range. A channel list is a comma (,) separated sequence of channel names
(for example, 0,2 specifies channels 0 and 2). A channel range is a
lower bound channel followed by a hyphen (-) or colon (:) followed by an
upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
In the Running state, multiple output channel configurations are
performed sequentially based on the order specified in this parameter.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Level',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the current level, in amps, to generate for the specified
channel(s).
**Valid Values:**
The valid values for this parameter are defined by the current level
range that is configured using the niDCPower_ConfigureCurrentlevelRange
function.
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the current level the device attempts to generate for the
specified channel(s). The channel must be enabled for the specified
current level to take effect. Refer to the
niDCPower_ConfigureOutputEnabled function for more information about
enabling the output channel.

The current level setting is applicable only if the output function of
the channel is set to NIDCPOWER_VAL_DC_CURRENT. Use
nidcpower_ConfigureOutputFunction to set the output function. The
device actively regulates the current at the specified level unless
doing so causes a voltage greater than the
niDCPower_ConfigureVoltageLimit across the channels' output terminals.

**Related Topics:**

`Constant Current
Mode <REPLACE_DRIVER_SPECIFIC_URL_1(constant_current)>`__
''',
},
    },
    'ConfigureCurrentLevelRange': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel(s) to which this configuration value
applies. Specify multiple channels by using a channel list or a channel
range. A channel list is a comma (,) separated sequence of channel names
(for example, 0,2 specifies channels 0 and 2). A channel range is a
lower bound channel followed by a hyphen (-) or colon (:) followed by an
upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
In the Running state, multiple output channel configurations are
performed sequentially based on the order specified in this parameter.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Range',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the current level range, in amps, for the specified channel.
For valid ranges, refer to the *ranges* topic for your device in the *NI
DC Power Supplies and SMUs Help*.
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the current level range for the specified channel(s). The
configured range defines the valid values the current level can be set
to using the niDCPower_ConfigureCurrentLevel function. The current
level range setting is applicable only if the output function of the
channel is set to NIDCPOWER_VAL_DC_CURRENT. Use
nidcpower_ConfigureOutputFunction to set the output function.

Use the NIDCPOWER_ATTR_CURRENT_LEVEL_AUTORANGE attribute to enable
automatic selection of the current level range.

**Related Topics:**

`Ranges <REPLACE_DRIVER_SPECIFIC_URL_1(ranges)>`__
''',
},
    },
    'ConfigureCurrentLimit': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel(s) to which this configuration value
applies. Specify multiple channels by using a channel list or a channel
range. A channel list is a comma (,) separated sequence of channel names
(for example, 0,2 specifies channels 0 and 2). A channel range is a
lower bound channel followed by a hyphen (-) or colon (:) followed by an
upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
In the Running state, multiple output channel configurations are
performed sequentially based on the order specified in this parameter.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Behavior',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies how the output should behave when the current limit is
reached.
**Defined Values:**
''',
'table_body': [['NIDCPOWER_VAL_CURRENT_REGULATE', 'Controls output current so that it does not exceed the current limit. Power continues to generate even if the current limit is reached.']],
},
            },
            {
                'direction': 'in',
                'name': 'Limit',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the current limit, in amps, on the specified channel(s). The
limit is specified as a positive value, but symmetric positive and
negative limits are enforced simultaneously.
**Valid Values:**
The valid values for this parameter are defined by the current limit
range that is configured using the niDCPower_ConfigureCurrentlimitRange
function.
''',
},
            },
        ],
'documentation': {
'description': '''
| Configures the current limit for the specified channel(s). The channel
  must be enabled for the specified current limit to take effect. Refer
  to the niDCPower_ConfigureOutputEnabled function for more information
  about enabling the output channel.
| The current limit is the current that the output should not exceed
  when generating the desired niDCPower_ConfigureVoltageLevel. The
  current limit setting is applicable only if the output function of the
  channel is set to NIDCPOWER_VAL_DC_VOLTAGE. Use
  nidcpower_ConfigureOutputFunction to set the output function.

**Related Topics:**

`Compliance <REPLACE_DRIVER_SPECIFIC_URL_1(compliance)>`__
''',
},
    },
    'ConfigureCurrentLimitRange': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel(s) to which this configuration value
applies. Specify multiple channels by using a channel list or a channel
range. A channel list is a comma (,) separated sequence of channel names
(for example, 0,2 specifies channels 0 and 2). A channel range is a
lower bound channel followed by a hyphen (-) or colon (:) followed by an
upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
In the Running state, multiple output channel configurations are
performed sequentially based on the order specified in this parameter.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Range',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the current limit range, in amps, for the specified channel.
For valid ranges, refer to the *ranges* topic for your device in the *NI
DC Power Supplies and SMUs Help*.
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the current limit range for the specified channel(s).The
configured range defines the valid values the current limit can be set
to using the niDCPower_ConfigureCurrentLimit function. The current
limit range setting is applicable only if the output function of the
channel is set to NIDCPOWER_VAL_DC_VOLTAGE. Use
nidcpower_ConfigureOutputFunction to set the output function.

Use the NIDCPOWER_ATTR_CURRENT_LIMIT_AUTORANGE attribute to enable
automatic selection of the current limit range.

**Related Topics:**

`Ranges <REPLACE_DRIVER_SPECIFIC_URL_1(ranges)>`__
''',
},
    },
    'ConfigureDigitalEdgeMeasureTrigger': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'inputTerminal',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the input terminal for the digital edge Measure trigger.

You can specify any valid input terminal for this function. Valid
terminals are listed in MAX under the **Device Routes** tab. For
PXIe-4162/4163, refer to the Signal Routing topic for the device to
determine which routes are available. This information is not available
on a Device Routes tab in MAX.

Input terminals can be specified in one of two ways. If the device is
named Dev1 and your terminal is PXI_Trig0, you can specify the terminal
with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the
shortened terminal name, PXI_Trig0. The input terminal can also be a
terminal from another device. For example, you can set the input
terminal on Dev1 to be /Dev2/SourceCompleteEvent.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Edge',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies whether to configure the Measure trigger to assert on the
rising or falling edge.
**Defined Values:**
''',
'table_body': [['NIDCPOWER_VAL_RISING (1016)', 'Asserts the trigger on the rising edge of the digital signal.'], ['NIDCPOWER_VAL_FALLING (1017)', 'Asserts the trigger on the falling edge of the digital signal.']],
},
            },
        ],
'documentation': {
'description': 'Configures the Measure trigger for digital edge triggering.',
'note': '''
This function is not supported on all devices. Refer to `Supported
Functions by
Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
for more information about supported devices.
''',
},
    },
    'ConfigureDigitalEdgePulseTrigger': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'inputTerminal',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the input terminal for the digital edge Pulse trigger.

You can specify any valid input terminal for this function. Valid
terminals are listed in MAX under the **Device Routes** tab.

Input terminals can be specified in one of two ways. If the device is
named Dev1 and your terminal is PXI_Trig0, you can specify the terminal
with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the
shortened terminal name, PXI_Trig0. The input terminal can also be a
terminal from another device. For example, you can set the input
terminal on Dev1 to be /Dev2/SourceCompleteEvent.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Edge',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies whether to configure the Pulse trigger to assert on the rising
or falling edge.
**Defined Values:**
''',
'table_body': [['NIDCPOWER_VAL_RISING (1016)', 'Asserts the trigger on the rising edge of the digital signal.'], ['NIDCPOWER_VAL_FALLING (1017)', 'Asserts the trigger on the falling edge of the digital signal.']],
},
            },
        ],
'documentation': {
'description': 'Configures the Pulse trigger for digital edge triggering.',
'note': '''
This function is not supported on all devices. Refer to `Supported
Functions by
Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
for more information about supported devices.
''',
},
    },
    'ConfigureDigitalEdgeSequenceAdvanceTrigger': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'inputTerminal',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the input terminal for the digital edge Sequence Advance
trigger.

You can specify any valid input terminal for this function. Valid
terminals are listed in MAX under the **Device Routes** tab. For
PXIe-4162/4163, refer to the Signal Routing topic for the device to
determine which routes are available. This information is not available
on a Device Routes tab in MAX.

Input terminals can be specified in one of two ways. If the device is
named Dev1 and your terminal is PXI_Trig0, you can specify the terminal
with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the
shortened terminal name, PXI_Trig0. The input terminal can also be a
terminal from another device. For example, you can set the input
terminal on Dev1 to be /Dev2/SourceCompleteEvent.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Edge',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies whether to configure the Sequence Advance trigger to assert on
the rising or falling edge.
**Defined Values:**
''',
'table_body': [['NIDCPOWER_VAL_RISING (1016)', 'Asserts the trigger on the rising edge of the digital signal.'], ['NIDCPOWER_VAL_FALLING (1017)', 'Asserts the trigger on the falling edge of the digital signal.']],
},
            },
        ],
'documentation': {
'description': 'Configures the Sequence Advance trigger for digital edge triggering.',
'note': '''
This function is not supported on all devices. Refer to `Supported
Functions by
Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
for more information about supported devices.
''',
},
    },
    'ConfigureDigitalEdgeSourceTrigger': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'inputTerminal',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the input terminal for the digital edge Source trigger.

You can specify any valid input terminal for this function. Valid
terminals are listed in MAX under the **Device Routes** tab. For
PXIe-4162/4163, refer to the Signal Routing topic for the device to
determine which routes are available. This information is not available
on a Device Routes tab in MAX.

Input terminals can be specified in one of two ways. If the device is
named Dev1 and your terminal is PXI_Trig0, you can specify the terminal
with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the
shortened terminal name, PXI_Trig0. The input terminal can also be a
terminal from another device. For example, you can set the input
terminal on Dev1 to be /Dev2/SourceCompleteEvent.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Edge',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies whether to configure the Source trigger to assert on the
rising or falling edge.
**Defined Values:**
''',
'table_body': [['NIDCPOWER_VAL_RISING (1016)', 'Asserts the trigger on the rising edge of the digital signal.'], ['NIDCPOWER_VAL_FALLING (1017)', 'Asserts the trigger on the falling edge of the digital signal.']],
},
            },
        ],
'documentation': {
'description': 'Configures the Source trigger for digital edge triggering.',
'note': '''
This function is not supported on all devices. Refer to `Supported
Functions by
Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
for more information about supported devices.
''',
},
    },
    'ConfigureDigitalEdgeStartTrigger': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'inputTerminal',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the input terminal for the digital edge Start trigger.

You can specify any valid input terminal for this function. Valid
terminals are listed in MAX under the **Device Routes** tab. For
PXIe-4162/4163, refer to the Signal Routing topic for the device to
determine which routes are available. This information is not available
on a Device Routes tab in MAX.

Input terminals can be specified in one of two ways. If the device is
named Dev1 and your terminal is PXI_Trig0, you can specify the terminal
with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the
shortened terminal name, PXI_Trig0. The input terminal can also be a
terminal from another device. For example, you can set the input
terminal on Dev1 to be /Dev2/SourceCompleteEvent.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Edge',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies whether to configure the Start trigger to assert on the rising
or falling edge.
**Defined Values:**
''',
'table_body': [['NIDCPOWER_VAL_RISING (1016)', 'Asserts the trigger on the rising edge of the digital signal.'], ['NIDCPOWER_VAL_FALLING (1017)', 'Asserts the trigger on the falling edge of the digital signal.']],
},
            },
        ],
'documentation': {
'description': 'Configures the Start trigger for digital edge triggering.',
'note': '''
This function is not supported on all devices. Refer to `Supported
Functions by
Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
for more information about supported devices.
''',
},
    },
    'ConfigureOutputEnabled': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel(s) to which this configuration value
applies. Specify multiple channels by using a channel list or a channel
range. A channel list is a comma (,) separated sequence of channel names
(for example, 0,2 specifies channels 0 and 2). A channel range is a
lower bound channel followed by a hyphen (-) or colon (:) followed by an
upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
In the Running state, multiple output channel configurations are
performed sequentially based on the order specified in this parameter.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Enabled',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether the output is enabled or disabled.
**Defined Values**:
''',
'table_body': [['VI_TRUE', 'Enables generation on the specified output channel(s).'], ['VI_FALSE', 'Disables generation on the specified output channel(s). This parameter has no effect on the output disconnect relay. To toggle the relay, use the NIDCPOWER_ATTR_OUTPUT_CONNECTED attribute.']],
},
            },
        ],
'documentation': {
'description': '''
Enables or disables generation on the specified channel(s). Depending on
the selected output function, the voltage level, current level,or output
resistance must be set in addition to enabling the output to generate
the desired level. For more information about configuring the output
level, refer to niDCPower_ConfigureOutputFunction.
''',
'note': '''
If the device is in the
`Uncommitted <javascript:LaunchHelp('NI_DC_Power_Supplies_Help.chm::/programmingStates.html#uncommitted')>`__
state, enabling the output does not take effect until you call the
niDCPower_Initiate function.
''',
},
    },
    'ConfigureOutputFunction': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel(s) to which this configuration value
applies. Specify multiple channels by using a channel list or a channel
range. A channel list is a comma (,) separated sequence of channel names
(for example, 0,2 specifies channels 0 and 2). A channel range is a
lower bound channel followed by a hyphen (-) or colon (:) followed by an
upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
In the Running state, multiple output channel configurations are
performed sequentially based on the order specified in this parameter.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Function',
                'type': 'ViInt32',
'documentation': {
'description': '''
Configures the function to generate for the specified channel(s).
**Defined Values**:
''',
'table_body': [['NIDCPOWER_VAL_DC_VOLTAGE (1006)', 'Sets the output function to DC voltage.'], ['NIDCPOWER_VAL_DC_CURRENT (1007)', 'Sets the output function to DC current.'], ['NIDCPOWER_VAL_PULSE_VOLTAGE (1049)', 'Sets the output function to pulse voltage.'], ['NIDCPOWER_VAL_PULSE_CURRENT (1050)', 'Sets the output function to pulse current.']],
},
            },
        ],
'documentation': {
'description': '''
Configures the function the device attempts to generate for the
specified channel(s).

When NIDCPOWER_VAL_DC_VOLTAGE is selected, the device generates the
desired voltage level on the output as long as the output current is
below the current limit. The following functions can be used to
configure the channel when NIDCPOWER_VAL_DC_VOLTAGE is selected:

-  niDCPower_ConfigureVoltageLevel
-  niDCPower_ConfigureCurrentLimit
-  niDCPower_ConfigureVoltageLevelRange
-  niDCPower_ConfigureCurrentLimitRange

When NIDCPOWER_VAL_DC_CURRENT is selected, the device generates the
desired current level on the output as long as the output voltage is
below the voltage limit. The following functions can be used to
configure the channel when NIDCPOWER_VAL_DC_CURRENT is selected:

-  niDCPower_ConfigureCurrentLevel
-  niDCPower_ConfigureVoltageLimit
-  niDCPower_ConfigureCurrentLevelRange
-  niDCPower_ConfigureVoltageLimitRange

When NIDCPOWER_VAL_PULSE_VOLTAGE is selected, the device generates
pulses at the desired voltage levels on the output as long as the output
current is below the current limit. The following VIs can be used to
configure the channel when NIDCPOWER_VAL_PULSE_VOLTAGE is selected:

-  niDCPower_ConfigurePulseVoltageLevel
-  niDCPower_ConfigurePulseBiasVoltageLevel
-  niDCPower_ConfigurePulseCurrentLimit
-  niDCPower_ConfigurePulseBiasCurrentLimit
-  niDCPower_ConfigurePulseVoltageLevelRange
-  niDCPower_ConfigurePulseCurrentLimitRange

When NIDCPOWER_VAL_PULSE_CURRENT is selected, the device generates
pulses at the desired current levels on the output as long as the output
voltage is below the voltage limit. The following VIs can be used to
configure the channel when NIDCPOWER_VAL_PULSE_CURRENT is selected:

-  niDCPower_ConfigurePulseCurrentLevel
-  niDCPower_ConfigurePulseBiasCurrentLevel
-  niDCPower_ConfigurePulseVoltageLimit
-  niDCPower_ConfigurePulseBiasVoltageLimit
-  niDCPower_ConfigurePulseCurrentLevelRange
-  niDCPower_ConfigurePulseVoltageLimitRange

**Related Topics:**

`Constant Voltage
Mode <REPLACE_DRIVER_SPECIFIC_URL_1(constant_voltage)>`__

`Constant Current
Mode <REPLACE_DRIVER_SPECIFIC_URL_1(constant_current)>`__
''',
},
    },
    'ConfigureOutputRange': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel(s) to which this configuration value
applies. Specify multiple channels by using a channel list or a channel
range. A channel list is a comma (,) separated sequence of channel names
(for example, 0,2 specifies channels 0 and 2). A channel range is a
lower bound channel followed by a hyphen (-) or colon (:) followed by an
upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
In the Running state, multiple output channel configurations are
performed sequentially based on the order specified in this parameter.
''',
},
            },
            {
                'direction': 'in',
                'name': 'rangeType',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the type of the range: voltage or current.
**Defined Values**:
''',
'table_body': [['NIDCPOWER_VAL_RANGE_CURRENT (0)', 'NI-DCPower configures the current range.'], ['NIDCPOWER_VAL_RANGE_VOLTAGE (1)', 'NI-DCPower configures the voltage range.']],
},
            },
            {
                'direction': 'in',
                'name': 'Range',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the range to calibrate with these settings. Only one channel
at a time may be calibrated.
''',
},
            },
        ],
'documentation': {
'description': '''
Configures either the voltage level range or the current limit range. If
**range type** is Voltage, the voltage level range is configured. If
**range type** is Current, the current limit range is configured.

This function does not configure any of the DC Current output function
settings. Refer to the niDCPower_ConfigureOutputFunction function for
more information.

This is a deprecated function. You must use the following functions
instead of theniDCPower_ConfigureOutputRange function:

-  niDCPower_ConfigureVoltageLevel
-  niDCPower_ConfigureVoltageLimit
-  niDCPower_ConfigureCurrentLevel
-  niDCPower_ConfigureCurrentLimit
''',
},
    },
    'ConfigureOutputResistance': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel(s) to which this configuration value
applies. Specify multiple channels by using a channel list or a channel
range. A channel list is a comma (,) separated sequence of channel names
(for example, 0,2 specifies channels 0 and 2). A channel range is a
lower bound channel followed by a hyphen (-) or colon (:) followed by an
upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
In the Running state, multiple output channel configurations are
performed sequentially based on the order specified in this parameter.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Resistance',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the output resistance, in ohms, for the specified channel.
Refer to the `NI PXIe-4141 Programmable Output
resistance <REPLACE_DRIVER_SPECIFIC_URL_1(4140_4141_progoutputresist)>`__,
`NI PXIe-4143 Programmable Output
resistance <REPLACE_DRIVER_SPECIFIC_URL_1(4142_4143_progoutputresist)>`__,
`NI PXIe-4145 Programmable Output
resistance <REPLACE_DRIVER_SPECIFIC_URL_1(4144_4145_progoutputresist)>`__,or
`NI PXIe-4154 Programmable Output
resistance <REPLACE_DRIVER_SPECIFIC_URL_1(4154_prog_output_resist)>`__
topic in the NI DC Power Supplies and SMUs Help for more information
about configuring output resistance.
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the output resistance that the device attempts to generate
for the specified channel or channels. The channel must be enabled for
the specified output resistance to take effect.

Refer to the nidcpower_ConfigureOutputEnabled function for more
information about enabling the output channel.

For NI PXIe-4141/4143/4145 devices, output resistance is only supported
if the output function of the channel is set to
NIDCPOWER_VAL_DC_VOLTAGE using the niDCPower_ConfigureOutputFunction
function.

For PXIe-4135, NI PXIe-4137, and NI PXIe-4139 devices, output resistance
is supported if the output function of the channel is set to
NIDCPOWER_VAL_DC_CURRENT or NIDCPOWER_VAL_DC_VOLTAGE using the
niDCPower_ConfigureOutputFunction function.

The device actively regulates the current and voltage to reach the
specified output resistance, although in DC Voltage output mode, the
voltage at the output experiences a "virtual drop" that is proportional
to its current. In DC Current output mode, the output experiences a
"virtual leakage current" that is proportional to the output voltage.
''',
'note': '''
This function is not supported on all devices. Refer to `Supported
Functions by
Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
for more information about supported devices.
''',
},
    },
    'ConfigurePowerLineFrequency': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'powerlineFrequency',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the power line frequency in hertz for specified channel(s).
NI-DCPower uses this value to select a timebase for the
NIDCPOWER_ATTR_APERTURE_TIME attribute. Refer to the *Measurement
Configuration and Timing* topic for your device for more information
about how to configure your measurements.
**Defined Values**:
''',
'note': 'Set this parameter to the frequency of the AC power line.',
'table_body': [['NIDCPOWER_VAL_50_HERTZ (50.0)', 'Specifies 50 Hz.'], ['NIDCPOWER_VAL_60_HERTZ (60.0)', 'Specifies 60 Hz.']],
},
            },
        ],
'documentation': {
'description': '''
Specifies the power line frequency for specified channel(s). NI-DCPower
uses this value to select a timebase for setting the
niDCPower_ConfigureApertureTime function in power line cycles (PLCs).

Refer to the *Measurement Configuration and Timing* topic for your
device in the *NI DC Power Supplies and SMUs Help* for more information
about how to configure your measurements.

**Related Topics:**

`Measurement Noise
Rejection <REPLACE_DRIVER_SPECIFIC_URL_1(noiserejectmeasure)>`__
''',
'note': '''
This function is not supported on all devices. Refer to `Supported
Functions by
Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
for more information about supported devices.
''',
},
    },
    'ConfigurePulseBiasCurrentLevel': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel(s) to which this configuration value
applies. Specify multiple channels by using a channel list or a channel
range. A channel list is a comma (,) separated sequence of channel names
(for example, 0,2 specifies channels 0 and 2). A channel range is a
lower bound channel followed by a hyphen (-) or colon (:) followed by an
upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
In the Running state, multiple output channel configurations are
performed sequentially based on the order specified in this parameter.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Level',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the pulse bias current level, in amps, on the specified
channel(s).
**Valid Values:**
The valid values for this parameter are defined by the pulse current
level range that is configured using the
niDCPower_ConfigurePulseCurrentlevelRange function.
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the pulse bias current level that the device attempts to
generate for the specified channel(s) during the off phase of a pulse.
The channel must be enabled for the specified current level to take
effect.

Refer to the niDCPower_ConfigureOutputEnabled function for more
information about enabling the output channel. The pulse current level
setting is applicable only if the channel is set to the
NIDCPOWER_VAL_PULSE_CURRENT output function using the
niDCPower_ConfigureOutputFunction function.

The device actively regulates the current at the specified level unless
doing so causes a voltage drop greater than the
NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT across the channels' output
terminals.
''',
'note': '''
This function is not supported on all devices. Refer to `Supported
Functions by
Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
for more information about supported devices.
''',
},
    },
    'ConfigurePulseBiasCurrentLimit': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel(s) to which this configuration value
applies. Specify multiple channels by using a channel list or a channel
range. A channel list is a comma (,) separated sequence of channel names
(for example, 0,2 specifies channels 0 and 2). A channel range is a
lower bound channel followed by a hyphen (-) or colon (:) followed by an
upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
In the Running state, multiple output channel configurations are
performed sequentially based on the order specified in this parameter.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Limit',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the pulse bias current limit, in amps, on the specified
channel(s). The limit is specified as a positive value, but symmetric
positive and negative limits are enforced simultaneously.
**Valid Values:**
The valid values for this parameter are defined by the pulse current
limit range that is configured using the
niDCPower_ConfigurePulseCurrentlimitRange function.
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the pulse bias current limit for the specified channel(s).
The channel must be enabled for the specified current limit to take
effect.

Refer to the niDCPower_ConfigureOutputEnabled function for more
information about enabling the output channel. The pulse bias current
limit is the current that the output must not exceed when generating the
desired NIDCPOWER_ATTR_pULSE_bIAS_vOLTAGE_lEVEL. The pulse bias
current limit setting is only applicable if the channel is set to the
NIDCPOWER_VAL_PULSE_VOLTAGE output function using the
niDCPower_ConfigureOutputFunction function.
''',
'note': '''
This function is not supported on all devices. Refer to `Supported
Functions by
Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
for more information about supported devices.
''',
},
    },
    'ConfigurePulseBiasVoltageLevel': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel(s) to which this configuration value
applies. Specify multiple channels by using a channel list or a channel
range. A channel list is a comma (,) separated sequence of channel names
(for example, 0,2 specifies channels 0 and 2). A channel range is a
lower bound channel followed by a hyphen (-) or colon (:) followed by an
upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
In the Running state, multiple output channel configurations are
performed sequentially based on the order specified in this parameter.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Level',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the pulse bias voltage level, in volts, for the output channel
generation.
**Valid Values**:
The valid values for this parameter are defined by the pulse voltage
level range that is selected using the
niDCPower_ConfigurePulseVoltagelevelRange function.
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the pulse bias voltage level that the device attempts to
generate for the specified channel(s) during the off phase of a pulse.
The channel must be enabled for the specified voltage level to take
effect.

Refer to the niDCPower_ConfigureOutputEnabled function for more
information about enabling the output channel. The pulse bias voltage
level setting is applicable only if the channel is set to the
NIDCPOWER_VAL_PULSE_VOLTAGE output function using the
niDCPower_ConfigureOutputFunction function.

The device actively regulates the voltage at the specified level unless
doing so causes a current greater than the
NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT through the channels'
output terminals.
''',
'note': '''
This function is not supported on all devices. Refer to `Supported
Functions by
Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
for more information about supported devices.
''',
},
    },
    'ConfigurePulseBiasVoltageLimit': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel(s) to which this configuration value
applies. Specify multiple channels by using a channel list or a channel
range. A channel list is a comma (,) separated sequence of channel names
(for example, 0,2 specifies channels 0 and 2). A channel range is a
lower bound channel followed by a hyphen (-) or colon (:) followed by an
upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
In the Running state, multiple output channel configurations are
performed sequentially based on the order specified in this parameter.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Limit',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the pulse bias voltage limit, in volts, on the specified
channel(s). The limit is specified as a positive value, but symmetric
positive and negative limits are enforced simultaneously.
**Valid Values:**
The valid values for this parameter are defined by the pulse voltage
limit range that is configured using the
niDCPower_ConfigurePulseVoltagelimitRange function.
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the pulse bias voltage limit for the specified channel(s).
The channel must be enabled for the specified voltage limit to take
effect.

Refer to the niDCPower_ConfigureOutputEnabled function for more
information about enabling the output channel. The pulse bias voltage
limit is the voltage that the output must not exceed when generating the
desired NIDCPOWER_ATTR_PULSE_bIAS_cURRENT_lEVEL. The pulse bias
voltage limit setting is only applicable if the channel is set to the
NIDCPOWER_VAL_PULSE_CURRENT output function using the
niDCPower_ConfigureOutputFunction function.
''',
'note': '''
This function is not supported on all devices. Refer to `Supported
Functions by
Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
for more information about supported devices.
''',
},
    },
    'ConfigurePulseCurrentLevel': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel(s) to which this configuration value
applies. Specify multiple channels by using a channel list or a channel
range. A channel list is a comma (,) separated sequence of channel names
(for example, 0,2 specifies channels 0 and 2). A channel range is a
lower bound channel followed by a hyphen (-) or colon (:) followed by an
upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
In the Running state, multiple output channel configurations are
performed sequentially based on the order specified in this parameter.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Level',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the pulse current level, in amps, on the specified channel(s).
**Valid Values:**
The valid values for this parameter are defined by the pulse current
level range that is configured using the
niDCPower_ConfigurePulseCurrentlevelRange function.
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the pulse current level that the device attempts to generate
for the specified channel(s) during the on phase of a pulse. The channel
must be enabled for the specified current level to take effect.

Refer to the niDCPower_ConfigureOutputEnabled function for more
information about enabling the output channel. The pulse current level
setting is applicable only if the channel is set to the
NIDCPOWER_VAL_PULSE_CURRENT output function using the
niDCPower_ConfigureOutputEnabled function.

The device actively regulates the current at the specified level unless
doing so causes a voltage drop greater than the
NIDCPOWER_ATTR_PULSE_VOLTAGE_lIMIT across the channels' output
terminals.
''',
'note': '''
This function is not supported on all devices. Refer to `Supported
Functions by
Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
for more information about supported devices.
''',
},
    },
    'ConfigurePulseCurrentLevelRange': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel(s) to which this configuration value
applies. Specify multiple channels by using a channel list or a channel
range. A channel list is a comma (,) separated sequence of channel names
(for example, 0,2 specifies channels 0 and 2). A channel range is a
lower bound channel followed by a hyphen (-) or colon (:) followed by an
upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
In the Running state, multiple output channel configurations are
performed sequentially based on the order specified in this parameter.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Range',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the pulse current level range, in amps, on the specified
channel(s).
For valid ranges, refer to the *ranges* topic for your device in the *NI
DC Power Supplies and SMUs Help*.
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the pulse current level range for the specified channel(s).

The configured range defines the valid values to which you can set the
pulse current level and pulse bias current level using the
niDCPower_ConfigurePulseCurrentLevel and
niDCPower_ConfigurePulseBiasCurrentLevel functions. The pulse current
level range setting is applicable only if the channel is set to the
NIDCPOWER_VAL_PULSE_CURRENT output function using the
niDCPower_ConfigureOutputFunction function.
''',
'note': '''
This function is not supported on all devices. Refer to `Supported
Functions by
Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
for more information about supported devices.
''',
},
    },
    'ConfigurePulseCurrentLimit': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel(s) to which this configuration value
applies. Specify multiple channels by using a channel list or a channel
range. A channel list is a comma (,) separated sequence of channel names
(for example, 0,2 specifies channels 0 and 2). A channel range is a
lower bound channel followed by a hyphen (-) or colon (:) followed by an
upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
In the Running state, multiple output channel configurations are
performed sequentially based on the order specified in this parameter.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Limit',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the pulse current limit, in amps, on the specified channel(s).
The limit is specified as a positive value, but symmetric positive and
negative limits are enforced simultaneously.
**Valid Values:**
The valid values for this parameter are defined by the pulse current
limit range that is configured using the
niDCPower_ConfigurePulseCurrentlimitRange function.
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the pulse current limit for the specified channel(s). The
channel must be enabled for the specified current limit to take effect.

Refer to the niDCPower_ConfigureOutputEnabled function for more
information about enabling the output channel. The pulse current limit
is the current that the output must not exceed when generating the
desired NIDCPOWER_ATTR_PULSE_vOLTAGE_lEVEL. The pulse current limit
setting is only applicable if the channel is set to the
NIDCPOWER_VAL_PULSE_VOLTAGE output function using the
niDCPower_ConfigureOutputFunction function.
''',
'note': '''
This function is not supported on all devices. Refer to `Supported
Functions by
Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
for more information about supported devices.
''',
},
    },
    'ConfigurePulseCurrentLimitRange': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel(s) to which this configuration value
applies. Specify multiple channels by using a channel list or a channel
range. A channel list is a comma (,) separated sequence of channel names
(for example, 0,2 specifies channels 0 and 2). A channel range is a
lower bound channel followed by a hyphen (-) or colon (:) followed by an
upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
In the Running state, multiple output channel configurations are
performed sequentially based on the order specified in this parameter.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Range',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the pulse current limit range, in amps, on the specified
channel(s).
For valid ranges, refer to the *ranges* topic for your device in the *NI
DC Power Supplies and SMUs Help*.
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the pulse current limit range for the specified channel(s).

The configured range defines the valid values to which you can set the
pulse current limit and pulse bias current limit using the
niDCPower_ConfigurePulseCurrentLimit and
niDCPower_ConfigurePulseBiasCurrentLimit functions. The pulse current
limit range setting is applicable only if the channel is set to the
NIDCPOWER_VAL_PULSE_VOLTAGE output function using the
niDCPower_ConfigureOutputFunction function.
''',
'note': '''
This function is not supported on all devices. Refer to `Supported
Functions by
Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
for more information about supported devices.
''',
},
    },
    'ConfigurePulseVoltageLevel': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel(s) to which this configuration value
applies. Specify multiple channels by using a channel list or a channel
range. A channel list is a comma (,) separated sequence of channel names
(for example, 0,2 specifies channels 0 and 2). A channel range is a
lower bound channel followed by a hyphen (-) or colon (:) followed by an
upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
In the Running state, multiple output channel configurations are
performed sequentially based on the order specified in this parameter.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Level',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the pulse voltage level, in volts, for the output channel
generation.
**Valid Values**:
The valid values for this parameter are defined by the voltage level
range that is selected using the
niDCPower_ConfigurePulseVoltagelevelRange function.
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the pulse voltage level that the device attempts to generate
for the specified channel(s) during the on phase of a pulse. The channel
must be enabled for the specified voltage level to take effect.

Refer to the niDCPower_ConfigureOutputEnabled function for more
information about enabling the output channel. The pulse voltage level
setting is applicable only if the channel is set to the
NIDCPOWER_VAL_PULSE_VOLTAGE output function using the
niDCPower_ConfigureOutputFunction function.

The device actively regulates the voltage at the specified level unless
doing so causes a current greater than the
NIDCPOWER_ATTR_PULSE_cURRENT_lIMIT through the channels' output
terminals.
''',
'note': '''
This function is not supported on all devices. Refer to `Supported
Functions by
Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
for more information about supported devices.
''',
},
    },
    'ConfigurePulseVoltageLevelRange': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel(s) to which this configuration value
applies. Specify multiple channels by using a channel list or a channel
range. A channel list is a comma (,) separated sequence of channel names
(for example, 0,2 specifies channels 0 and 2). A channel range is a
lower bound channel followed by a hyphen (-) or colon (:) followed by an
upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
In the Running state, multiple output channel configurations are
performed sequentially based on the order specified in this parameter.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Range',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the pulse voltage level range, in volts, on the specified
channel(s).
For valid ranges, refer to the *ranges* topic for your device in the *NI
DC Power Supplies and SMUs Help*.
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the pulse voltage level range for the specified channel(s).

The configured range defines the valid values to which you can set the
pulse voltage level and pulse bias voltage level using the
niDCPower_ConfigurePulseVoltageLevel and
niDCPower_ConfigurePulseBiasVoltageLevel functions. The pulse voltage
level range setting is applicable only if the channel is set to the
NIDCPOWER_VAL_PULSE_VOLTAGE output function using the
niDCPower_ConfigureOutputFunction function.
''',
'note': '''
This function is not supported on all devices. Refer to `Supported
Functions by
Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
for more information about supported devices.
''',
},
    },
    'ConfigurePulseVoltageLimit': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel(s) to which this configuration value
applies. Specify multiple channels by using a channel list or a channel
range. A channel list is a comma (,) separated sequence of channel names
(for example, 0,2 specifies channels 0 and 2). A channel range is a
lower bound channel followed by a hyphen (-) or colon (:) followed by an
upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
In the Running state, multiple output channel configurations are
performed sequentially based on the order specified in this parameter.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Limit',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the pulse voltage limit, in volts, on the specified output
channel(s). The limit is specified as a positive value, but symmetric
positive and negative limits are enforced simultaneously.
**Valid Values:**
The valid values for this parameter are defined by the pulse voltage
limit range that is configured using the
niDCPower_ConfigurePulseVoltagelimitRange function.
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the pulse voltage limit for the specified channel(s). The
channel must be enabled for the specified voltage limit to take effect.

Refer to the niDCPower_ConfigureOutputEnabled function for more
information about enabling the output channel. The pulse voltage limit
is the voltage that the output must not exceed when generating the
desired NIDCPOWER_ATTR_PULSE_cURRENT_lEVEL. The pulse voltage limit
setting is only applicable if the channel is set to the
NIDCPOWER_VAL_PULSE_CURRENT output function using the
niDCPower_ConfigureOutputFunction function.
''',
'note': '''
This function is not supported on all devices. Refer to `Supported
Functions by
Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
for more information about supported devices.
''',
},
    },
    'ConfigurePulseVoltageLimitRange': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel(s) to which this configuration value
applies. Specify multiple channels by using a channel list or a channel
range. A channel list is a comma (,) separated sequence of channel names
(for example, 0,2 specifies channels 0 and 2). A channel range is a
lower bound channel followed by a hyphen (-) or colon (:) followed by an
upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
In the Running state, multiple output channel configurations are
performed sequentially based on the order specified in this parameter.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Range',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the pulse voltage limit range, in volts, on the specified
channel(s).
For valid ranges, refer to the *ranges* topic for your device in the *NI
DC Power Supplies and SMUs Help*.
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the pulse voltage limit range for the specified channel(s).

The configured range defines the valid values to which you can set the
pulse voltage limit and pulse bias voltage limit using the
niDCPower_ConfigurePulseVoltageLimit and
niDCPower_ConfigurePulseBiasVoltageLimit functions. The pulse voltage
limit range setting is applicable only if the channel is set to the
NIDCPOWER_VAL_PULSE_CURRENT output function using the
niDCPower_ConfigureOutputFunction function.

.
''',
'note': '''
This function is not supported on all devices. Refer to `Supported
Functions by
Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
for more information about supported devices.
''',
},
    },
    'ConfigureSense': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel(s) to which this configuration value
applies. Specify multiple channels by using a channel list or a channel
range. A channel list is a comma (,) separated sequence of channel names
(for example, 0,2 specifies channels 0 and 2). A channel range is a
lower bound channel followed by a hyphen (-) or colon (:) followed by an
upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
In the Running state, multiple output channel configurations are
performed sequentially based on the order specified in this parameter.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Sense',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies local or remote sensing on the specified channel(s).
**Defined Values:**
''',
'table_body': [['NIDCPOWER_VAL_LOCAL (1008)', 'Local sensing'], ['NIDCPOWER_VAL_REMOTE (1009)', 'Remote sensing']],
},
            },
        ],
'documentation': {
'description': '''
Specifies whether to use
`local <REPLACE_DRIVER_SPECIFIC_URL_2(local_and_remote_sense)>`__ or
`remote <REPLACE_DRIVER_SPECIFIC_URL_2(local_and_remote_sense)>`__
sensing of the output voltage on the specified channel(s). Refer to the
*Devices* topic specific to your device in the *NI DC Power Supplies and
SMUs* Help for more information about sensing voltage on supported
channels.

**Related Topics:**

`Local and Remote
Sense <REPLACE_DRIVER_SPECIFIC_URL_1(4112_localandremotesense)>`__
''',
},
    },
    'ConfigureSoftwareEdgeMeasureTrigger': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the Measure trigger for software triggering. Use the
niDCPower_SendSoftwareEdgeTrigger function to assert the trigger
condition.
''',
'note': '''
This function is not supported on all devices. Refer to `Supported
Functions by
Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
for more information about supported devices.
''',
},
    },
    'ConfigureSoftwareEdgePulseTrigger': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the Pulse trigger for software triggering. Use the
niDCPower_SendSoftwareEdgeTrigger function to assert the trigger
condition.
''',
'note': '''
This function is not supported on all devices. Refer to `Supported
Functions by
Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
for more information about supported devices.
''',
},
    },
    'ConfigureSoftwareEdgeSequenceAdvanceTrigger': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the Sequence Advance trigger for software triggering. Use the
niDCPower_SendSoftwareEdgeTrigger function to assert the trigger
condition.
''',
'note': '''
This function is not supported on all devices. Refer to `Supported
Functions by
Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
for more information about supported devices.
''',
},
    },
    'ConfigureSoftwareEdgeSourceTrigger': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the Source trigger for software triggering. Use the
niDCPower_SendSoftwareEdgeTrigger function to assert the trigger
condition.
''',
'note': '''
This function is not supported on all devices. Refer to `Supported
Functions by
Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
for more information about supported devices.
''',
},
    },
    'ConfigureSoftwareEdgeStartTrigger': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the Start trigger for software triggering. Use the
niDCPower_SendSoftwareEdgeTrigger function to assert the trigger
condition.
''',
'note': '''
This function is not supported on all devices. Refer to `Supported
Functions by
Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
for more information about supported devices.
''',
},
    },
    'ConfigureSourceMode': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'sourceMode',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the source mode for the NI-DCPower session.
**Defined Values**:
''',
'table_body': [['NIDCPOWER_VAL_SINGLE_POINT (1020)', 'Applies a single source configuration.'], ['NIDCPOWER_VAL_SEQUENCE (1021)', 'Applies a list of voltage or current configurations sequentially.']],
},
            },
        ],
'documentation': {
'description': '''
Configures the NIDCPOWER_ATTR_SOURCE_MODE attribute. Specifies
whether to run a single output point or a sequence. Refer to the `Single
Point Source Mode <REPLACE_DRIVER_SPECIFIC_URL_1(singlept)>`__ and
`Sequence Source Mode <REPLACE_DRIVER_SPECIFIC_URL_1(sequencing)>`__
topics in the *NI DC Power Supplies and SMUs Help* for more information
about using this function.
''',
},
    },
    'ConfigureVoltageLevel': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel(s) to which this configuration value
applies. Specify multiple channels by using a channel list or a channel
range. A channel list is a comma (,) separated sequence of channel names
(for example, 0,2 specifies channels 0 and 2). A channel range is a
lower bound channel followed by a hyphen (-) or colon (:) followed by an
upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
In the Running state, multiple output channel configurations are
performed sequentially based on the order specified in this parameter.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Level',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the voltage level, in volts, for the output channel
generation.
**Valid Values**:
The valid values for this parameter are defined by the voltage level
range that is selected using the niDCPower_ConfigureVoltagelevelRange
function.
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the voltage level the device attempts to generate for the
specified channel(s). The channel must be enabled for the specified
voltage level to take effect. Refer to the
niDCPower_ConfigureOutputEnabled function for more information about
enabling the output channel.

The voltage level setting is applicable only if the output function of
the channel is set to NIDCPOWER_VAL_DC_VOLTAGE. Use
nidcpower_ConfigureOutputFunction to set the output function.

The device actively regulates the voltage at the specified level unless
doing so causes a current output greater than the
NIDCPOWER_ATTR_CURRENT_LIMIT across the channels' output terminals.

**Related Topics:**

`Constant Voltage
Mode <REPLACE_DRIVER_SPECIFIC_URL_1(constant_voltage)>`__
''',
},
    },
    'ConfigureVoltageLevelRange': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel(s) to which this configuration value
applies. Specify multiple channels by using a channel list or a channel
range. A channel list is a comma (,) separated sequence of channel names
(for example, 0,2 specifies channels 0 and 2). A channel range is a
lower bound channel followed by a hyphen (-) or colon (:) followed by an
upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
In the Running state, multiple output channel configurations are
performed sequentially based on the order specified in this parameter.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Range',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the voltage level range, in volts, on the specified
channel(s).
For valid ranges, refer to the *ranges* topic for your device in the *NI
DC Power Supplies and SMUs Help*.
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the voltage level range for the specified channel(s). The
configured range defines the valid values the voltage level can be set
to using the niDCPower_ConfigureVoltageLevel function. The voltage
level range setting is applicable only if the output function of the
channel is set to NIDCPOWER_VAL_DC_VOLTAGE. Use
nidcpower_ConfigureOutputFunction to set the output function.

Use the NIDCPOWER_ATTR_VOLTAGE_LEVEL_AUTORANGE attribute to enable
automatic selection of the voltage level range.

**Related Topics:**

`Ranges <REPLACE_DRIVER_SPECIFIC_URL_1(ranges)>`__
''',
},
    },
    'ConfigureVoltageLimit': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel(s) to which this configuration value
applies. Specify multiple channels by using a channel list or a channel
range. A channel list is a comma (,) separated sequence of channel names
(for example, 0,2 specifies channels 0 and 2). A channel range is a
lower bound channel followed by a hyphen (-) or colon (:) followed by an
upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
In the Running state, multiple output channel configurations are
performed sequentially based on the order specified in this parameter.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Limit',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the voltage limit, in volts, on the specified output
channel(s). The limit is specified as a positive value, but symmetric
positive and negative limits are enforced simultaneously.
**Valid Values:**
The valid values for this parameter are defined by the voltage limit
range that is configured using the niDCPower_ConfigureVoltagelimitRange
function.
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the voltage limit for the specified channel(s). The channel
must be enabled for the specified voltage limit to take effect. Refer to
the niDCPower_ConfigureOutputEnabled function for more information
about enabling the output channel.

The voltage limit is the voltage that the output should not exceed when
generating the desired niDCPower_ConfigureCurrentLevel. The voltage
limit setting is applicable only if the output function of the channel
is set to NIDCPOWER_VAL_DC_CURRENT. Use
nidcpower_ConfigureOutputFunction to set the output function.

**Related Topics:**

`Compliance <REPLACE_DRIVER_SPECIFIC_URL_1(compliance)>`__
''',
},
    },
    'ConfigureVoltageLimitRange': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel(s) to which this configuration value
applies. Specify multiple channels by using a channel list or a channel
range. A channel list is a comma (,) separated sequence of channel names
(for example, 0,2 specifies channels 0 and 2). A channel range is a
lower bound channel followed by a hyphen (-) or colon (:) followed by an
upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
In the Running state, multiple output channel configurations are
performed sequentially based on the order specified in this parameter.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Range',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the voltage limit range, in volts, on the specified
channel(s).
For valid ranges, refer to the *ranges* topic for your device in the *NI
DC Power Supplies and SMUs Help*.
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the voltage limit range for the specified channel(s). The
configured range defines the valid values the voltage limit can be set
to using the niDCPower_ConfigureVoltageLimit function. The voltage
limit range setting is applicable only if the output function of the
channel is set to NIDCPOWER_VAL_DC_CURRENT. Use
nidcpower_ConfigureOutputFunction to set the output function.

Use the NIDCPOWER_ATTR_VOLTAGE_LIMIT_AUTORANGE attribute to enable
automatic selection of the voltage limit range.

**Related Topics:**

`Ranges <REPLACE_DRIVER_SPECIFIC_URL_1(ranges)>`__
''',
},
    },
    'ConnectInternalReference': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'internalReference',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the internal reference to be connected to the calibration pin.
**Defined Values**:
''',
'table_body': [['NIDCPOWER_VAL_INTERNAL_REFERENCE_5V (1054)', 'Calibration pin connected to 5 V internal reference.'], ['NIDCPOWER_VAL_INTERNAL_REFERENCE_100KOHM (1055)', 'Calibration pin connected to 100 kΩ internal reference.'], ['NIDCPOWER_VAL_INTERNAL_REFERENCE_GROUND (1056)', 'Calibration pin connected to ground reference.'], ['NIDCPOWER_VAL_INTERNAL_REFERENCE_NONE (1057)', 'Calibration pin disconnected from internal reference.']],
},
            },
        ],
'documentation': {
'description': '''
Routes the internal reference to the calibration pin in preparation for
adjustment. Refer to the calibration procedure for the device you are
calibrating for detailed instructions on the appropriate use of this
function. This function can only be called from an external calibration
session.
''',
'note': '''
This function is not supported on all devices. Refer to `Supported
Functions by
Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
for more information about supported devices.
''',
},
    },
    'CreateAdvancedSequence': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'sequenceName',
                'type': 'ViConstString',
'documentation': {
'description': 'Specifies the name of the sequence to create.',
},
            },
            {
                'direction': 'in',
                'name': 'attributeIdCount',
                'type': 'ViInt32',
'documentation': {
'description': 'Specifies the number of attributes in the attributeIDs array.',
},
            },
            {
                'direction': 'in',
                'name': 'attributeIds',
                'type': 'ViInt32[]',
'documentation': {
'description': '''
Specifies the attributes you reconfigure per step in the advanced
sequence. The following table lists which attributes can be configured
in an advanced sequence for each NI-DCPower device that supports
advanced sequencing. A ✓ indicates that the attribute can be configured
in advanced sequencing. An ✕ indicates that the attribute cannot be
configured in advanced sequencing.
''',
'table_body': [['NIDCPOWER_ATTR_DC_NOISE_REJECTION', '✓', '✕', '✓', '✕', '✓', '✕', '✕', '✓'], ['NIDCPOWER_ATTR_APERTURE_TIME', '✓', '✓', '✓', '✓', '✓', '✓', '✓', '✓'], ['NIDCPOWER_ATTR_MEASURE_RECORD_LENGTH', '✓', '✓', '✓', '✓', '✓', '✓', '✓', '✓'], ['NIDCPOWER_ATTR_SENSE', '✓', '✓', '✓', '✓', '✓', '✓', '✓', '✓'], ['NIDCPOWER_ATTR_OVP_ENABLED', '✓', '✓', '✓', '✕', '✕', '✕', '✕', '✕'], ['NIDCPOWER_ATTR_OVP_LIMIT', '✓', '✓', '✓', '✕', '✕', '✕', '✕', '✕'], ['NIDCPOWER_ATTR_PULSE_BIAS_DELAY', '✓', '✓', '✓', '✓', '✓', '✕', '✕', '✕'], ['NIDCPOWER_ATTR_PULSE_OFF_TIME', '✓', '✓', '✓', '✓', '✓', '✕', '✕', '✕'], ['NIDCPOWER_ATTR_PULSE_ON_TIME', '✓', '✓', '✓', '✓', '✓', '✕', '✕', '✕'], ['NIDCPOWER_ATTR_SOURCE_DELAY', '✓', '✓', '✓', '✓', '✓', '✓', '✓', '✓'], ['NIDCPOWER_ATTR_CURRENT_COMPENSATION_FREQUENCY', '✓', '✕', '✓', '✕', '✓', '✕', '✓', '✓'], ['NIDCPOWER_ATTR_CURRENT_GAIN_BANDWIDTH', '✓', '✕', '✓', '✕', '✓', '✕', '✓', '✓'], ['NIDCPOWER_ATTR_CURRENT_POLE_ZERO_RATIO', '✓', '✕', '✓', '✕', '✓', '✕', '✓', '✓'], ['NIDCPOWER_ATTR_VOLTAGE_COMPENSATION_FREQUENCY', '✓', '✕', '✓', '✕', '✓', '✕', '✓', '✓'], ['NIDCPOWER_ATTR_VOLTAGE_GAIN_BANDWIDTH', '✓', '✕', '✓', '✕', '✓', '✕', '✓', '✓'], ['NIDCPOWER_ATTR_VOLTAGE_POLE_ZERO_RATIO', '✓', '✕', '✓', '✕', '✓', '✕', '✓', '✓'], ['NIDCPOWER_ATTR_CURRENT_LEVEL', '✓', '✓', '✓', '✓', '✓', '✓', '✓', '✓'], ['NIDCPOWER_ATTR_CURRENT_LEVEL_RANGE', '✓', '✓', '✓', '✓', '✓', '✓', '✓', '✓'], ['NIDCPOWER_ATTR_VOLTAGE_LIMIT', '✓', '✓', '✓', '✓', '✓', '✓', '✓', '✓'], ['NIDCPOWER_ATTR_VOLTAGE_LIMIT_RANGE', '✓', '✓', '✓', '✓', '✓', '✓', '✓', '✓'], ['NIDCPOWER_ATTR_CURRENT_LIMIT', '✓', '✓', '✓', '✓', '✓', '✓', '✓', '✓'], ['NIDCPOWER_ATTR_CURRENT_LIMIT_RANGE', '✓', '✓', '✓', '✓', '✓', '✓', '✓', '✓'], ['NIDCPOWER_ATTR_VOLTAGE_LEVEL', '✓', '✓', '✓', '✓', '✓', '✓', '✓', '✓'], ['NIDCPOWER_ATTR_VOLTAGE_LEVEL_RANGE', '✓', '✓', '✓', '✓', '✓', '✓', '✓', '✓'], ['NIDCPOWER_ATTR_OUTPUT_ENABLED', '✓', '✓', '✓', '✓', '✓', '✓', '✓', '✓'], ['NIDCPOWER_ATTR_OUTPUT_FUNCTION', '✓', '✓', '✓', '✓', '✓', '✓', '✓', '✓'], ['NIDCPOWER_ATTR_OUTPUT_RESISTANCE', '✓', '✕', '✓', '✕', '✓', '✕', '✓', '✕'], ['NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LEVEL', '✓', '✓', '✓', '✓', '✓', '✕', '✕', '✕'], ['NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT', '✓', '✓', '✓', '✓', '✓', '✕', '✕', '✕'], ['NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL', '✓', '✓', '✓', '✓', '✓', '✕', '✕', '✕'], ['NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL_RANGE', '✓', '✓', '✓', '✓', '✓', '✕', '✕', '✕'], ['NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT', '✓', '✓', '✓', '✓', '✓', '✕', '✕', '✕'], ['NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_RANGE', '✓', '✓', '✓', '✓', '✓', '✕', '✕', '✕'], ['NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT', '✓', '✓', '✓', '✓', '✓', '✕', '✕', '✕'], ['NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LEVEL', '✓', '✓', '✓', '✓', '✓', '✕', '✕', '✕'], ['NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT', '✓', '✓', '✓', '✓', '✓', '✕', '✕', '✕'], ['NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_RANGE', '✓', '✓', '✓', '✓', '✓', '✕', '✕', '✕'], ['NIDCPOWER_ATTR_PULSE_VOLTAGE_LEVEL', '✓', '✓', '✓', '✓', '✓', '✕', '✕', '✕'], ['NIDCPOWER_ATTR_PULSE_VOLTAGE_LEVEL_RANGE', '✓', '✓', '✓', '✓', '✓', '✕', '✕', '✕'], ['NIDCPOWER_ATTR_TRANSIENT_RESPONSE', '✓', '✓', '✓', '✓', '✓', '✓', '✓', '✓']],
'table_header': ['Attribute', 'PXIe-4135', 'NI 4136', 'NI 4137', 'NI 4138', 'NI 4139', 'NI 4140/4142/4144', 'NI 4141/4143/4145', 'PXIe-4162/4163'],
},
            },
            {
                'direction': 'in',
                'name': 'setAsActiveSequence',
                'type': 'ViBoolean',
'documentation': {
'description': 'Specifies that this current sequence is active.',
},
            },
        ],
'documentation': {
'description': '''
Creates an empty advanced sequence. Call the
niDCPower_CreateAdvancedSequenceStep function to add steps to the
active advanced sequence.

**Support for this function**

You must set the source mode to Sequence to use this function.

Using the niDCPower_SetSequence function with Advanced Sequence
functions is unsupported.

Use this function in the Uncommitted or Committed programming states.
Refer to the `Programming
States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic in
the *NI DC Power Supplies and SMUs Help* for more information about
NI-DCPower programming states.

**Related Topics**:

`Advanced Sequence
Mode <REPLACE_DRIVER_SPECIFIC_URL_1(advancedsequencemode)>`__

`Programming
States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

niDCPower_CreateAdvancedSequenceStep
''',
'note': '''
This function is not supported on all devices. Refer to `Supported
Functions by
Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
for more information about supported devices.
''',
},
    },
    'CreateAdvancedSequenceStep': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'setAsActiveStep',
                'type': 'ViBoolean',
'documentation': {
'description': 'Specifies that this current step in the active sequence is active.',
},
            },
        ],
'documentation': {
'description': '''
Creates a new advanced sequence step in the advanced sequence specified
by the Active advanced sequence. When you create an advanced sequence
step, each attribute you passed to the niDCPower_CreateAdvancedSequence
function is reset to its default value for that step unless otherwise
specified.

**Support for this Function**

You must set the source mode to Sequence to use this function.

Using the niDCPower_SetSequence function with Advanced Sequence
functions is unsupported.

**Related Topics**:

`Advanced Sequence
Mode <REPLACE_DRIVER_SPECIFIC_URL_1(advancedsequencemode)>`__

`Programming
States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

niDCPower_CreateAdvancedSequence
''',
'note': '''
This function is not supported on all devices. Refer to `Supported
Functions by
Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
for more information about supported devices.
''',
},
    },
    'DeleteAdvancedSequence': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'sequenceName',
                'type': 'ViConstString',
'documentation': {
'description': 'specifies the name of the sequence to delete.',
},
            },
        ],
'documentation': {
'description': '''
Deletes a previously created advanced sequence and all the advanced
sequence steps in the advanced sequence.

**Support for this Function**

You must set the source mode to Sequence to use this function.

Using the niDCPower_SetSequence function with Advanced Sequence
functions is unsupported.

**Related Topics**:

`Advanced Sequence
Mode <REPLACE_DRIVER_SPECIFIC_URL_1(advancedsequencemode)>`__

`Programming
States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__
''',
'note': '''
This function is not supported on all devices. Refer to `Supported
Functions by
Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
for more information about supported devices.
''',
},
    },
    'Disable': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
        ],
'documentation': {
'description': '''
This function performs the same actions as the niDCPower_reset
function, except that this function also immediately sets the
NIDCPOWER_ATTR_OUTPUT_ENABLED attribute to VI_FALSE.

This function opens the output relay on devices that have an output
relay.
''',
},
    },
    'DisablePulseTrigger': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
        ],
'documentation': {
'description': '''
Disables the Pulse trigger. The device does not wait for a pulse trigger
before performing a pulse operation. Refer to `Pulse
Mode <REPLACE_DRIVER_SPECIFIC_URL_1(pulsemode)>`__ and `Sequence Source
Mode <REPLACE_DRIVER_SPECIFIC_URL_1(sequencing)>`__ for more information
about the Pulse trigger.

This function is necessary only if you configured a Pulse trigger in the
past and now want to disable it.
''',
'note': '''
This function is not supported on all devices. Refer to `Supported
Functions by
Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
for more information about supported devices.
''',
},
    },
    'DisableSequenceAdvanceTrigger': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
        ],
'documentation': {
'description': '''
Disables the Sequence Advance trigger. The device does not wait for a
Sequence Advance trigger before advancing to the next iteration of the
sequence. Refer to the `Sequence Source
Mode <REPLACE_DRIVER_SPECIFIC_URL_1(sequencing)>`__ topic for more
information about the Sequence Advance trigger.
''',
'note': '''
This function is not supported on all devices. Refer to `Supported
Functions by
Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
for more information about supported devices.
''',
},
    },
    'DisableSourceTrigger': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
        ],
'documentation': {
'description': '''
Disables the Source trigger. The device does not wait for a source
trigger before performing a source operation. Refer to the `Single Point
Source Mode <REPLACE_DRIVER_SPECIFIC_URL_1(singlept)>`__ and `Sequence
Source Mode <REPLACE_DRIVER_SPECIFIC_URL_1(sequencing)>`__ topics for
more information about the Source trigger.
''',
'note': '''
This function is not supported on all devices. Refer to `Supported
Functions by
Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
for more information about supported devices.
''',
},
    },
    'DisableStartTrigger': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
        ],
'documentation': {
'description': '''
Disables the Start trigger. The device does not wait for a Start trigger
when starting generation or acquisition.
''',
'note': '''
This function is not supported on all devices. Refer to `Supported
Functions by
Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
for more information about supported devices.
''',
},
    },
    'ExportSignal': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Signal',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies which trigger or event to export.
**Defined Values:**
''',
'table_body': [['NIDCPOWER_VAL_SOURCE_COMPLETE_EVENT (1030)', 'Exports the Source Complete event.'], ['NIDCPOWER_VAL_MEASURE_COMPLETE_EVENT (1031)', 'Exports the Measure Complete event.'], ['NIDCPOWER_VAL_SEQUENCE_ITERATION_COMPLETE_EVENT (1032)', 'Exports the Sequence Iteration Complete event.'], ['NIDCPOWER_VAL_SEQUENCE_ENGINE_DONE_EVENT (1033)', 'Exports the Sequence Engine Done event.'], ['NIDCPOWER_VAL_PULSE_COMPLETE_EVENT (1051)', 'Exports the Pulse Complete event.'], ['NIDCPOWER_VAL_READY_FOR_PULSE_TRIGGER_EVENT (1052)', 'Exports the Ready Pulse Trigger event.'], ['NIDCPOWER_VAL_START_TRIGGER (1034)', 'Exports the Start trigger.'], ['NIDCPOWER_VAL_SOURCE_TRIGGER (1035)', 'Exports the Source trigger.'], ['NIDCPOWER_VAL_MEASURE_TRIGGER (1036)', 'Exports the Measure trigger.'], ['NIDCPOWER_VAL_SEQUENCE_ADVANCE_TRIGGER (1037)', 'Exports the Sequence Advance trigger.'], ['NIDCPOWER_VAL_PULSE_TRIGGER (1053)', 'Exports the Pulse trigger.']],
},
            },
            {
                'direction': 'in',
                'name': 'signalIdentifier',
                'type': 'ViChar[]',
'documentation': {
'description': 'Reserved for future use. Pass in an empty string for this parameter.',
},
            },
            {
                'direction': 'in',
                'name': 'outputTerminal',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies where to export the selected signal.
**Relative Terminals**:
''',
'table_body': [['""', 'Do not export signal'], ['"PXI_Trig0"', 'PXI trigger line 0'], ['"PXI_Trig1"', 'PXI trigger line 1'], ['"PXI_Trig2"', 'PXI trigger line 2'], ['"PXI_Trig3"', 'PXI trigger line 3'], ['"PXI_Trig4"', 'PXI trigger line 4'], ['"PXI_Trig5"', 'PXI trigger line 5'], ['"PXI_Trig6"', 'PXI trigger line 6'], ['"PXI_Trig7"', 'PXI trigger line 7']],
},
            },
        ],
'documentation': {
'description': '''
Routes signals (triggers and events) to the output terminal you specify.
The route is created when the session is niDCPower_Commit.

**Related Topics:**

`Triggers <REPLACE_DRIVER_SPECIFIC_URL_1(trigger)>`__
''',
'note': '''
This function is not supported on all devices. Refer to `Supported
Functions by
Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
for more information about supported devices.
''',
},
    },
    'FetchMultiple': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel(s) to which this configuration value
applies. Specify multiple channels by using a channel list or a channel
range. A channel list is a comma (,) separated sequence of channel names
(for example, 0,2 specifies channels 0 and 2). A channel range is a
lower bound channel followed by a hyphen (-) or colon (:) followed by an
upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
In the Running state, multiple output channel configurations are
performed sequentially based on the order specified in this parameter.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the maximum time allowed for this function to complete, in
seconds. If the function does not complete within this time interval,
NI-DCPower returns an error.
''',
'note': '''
When setting the timeout interval, ensure you take into account any
triggers so that the timeout interval is long enough for your
application.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Count',
                'type': 'ViInt32',
'documentation': {
'description': 'Specifies the number of measurements to fetch.',
},
            },
            {
                'direction': 'out',
                'name': 'voltageMeasurements',
                'type': 'ViReal64[]',
'documentation': {
'description': '''
Returns an array of voltage measurements. Ensure that sufficient space
has been allocated for the returned array.
''',
},
            },
            {
                'direction': 'out',
                'name': 'currentMeasurements',
                'type': 'ViReal64[]',
'documentation': {
'description': '''
Returns an array of current measurements. Ensure that sufficient space
has been allocated for the returned array.
''',
},
            },
            {
                'direction': 'out',
                'name': 'inCompliance',
                'type': 'ViBoolean[]',
'documentation': {
'description': '''
Returns an array of Boolean values indicating whether the output was in
compliance at the time the measurement was taken. Ensure that sufficient
space has been allocated for the returned array.
''',
},
            },
            {
                'direction': 'out',
                'name': 'actualCount',
                'type': 'ViInt32',
'documentation': {
'description': '''
Indicates the number of measured values actually retrieved from the
device.
''',
},
            },
        ],
'documentation': {
'description': '''
Returns an array of voltage measurements, an array of current
measurements, and an array of compliance measurements that were
previously taken and are stored in the NI-DCPower buffer. This function
should not be used when the NIDCPOWER_ATTR_MEASURE_WHEN attribute is
set to NIDCPOWER_VAL_ON_DEMAND. You must first call
niDCPower_Initiate before calling this function.

Refer to the `Acquiring
Measurements <REPLACE_DRIVER_SPECIFIC_URL_1(acquiringmeasurements)>`__
and `Compliance <REPLACE_DRIVER_SPECIFIC_URL_1(compliance)>`__ topics in
the *NI DC Power Supplies and SMUs Help* for more information about
configuring this function.
''',
'note': '''
This function is not supported on all devices. Refer to `Supported
Functions by
Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
for more information about supported devices.
''',
},
    },
    'GetAttributeViBoolean': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel(s) to which this configuration value
applies. Specify multiple channels by using a channel list or a channel
range. A channel list is a comma (,) separated sequence of channel names
(for example, 0,2 specifies channels 0 and 2). A channel range is a
lower bound channel followed by a hyphen (-) or colon (:) followed by an
upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
In the Running state, multiple output channel configurations are
performed sequentially based on the order specified in this parameter.
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': '''
Specifies the ID of an attribute. From the function panel window, you
can use this control as follows.

-  In the function panel window, click on the control or press **Enter**
   or the spacebar to display a dialog box containing hierarchical list
   of the available attributes. Help text is shown for each attribute.
   Select an attribute by double-clicking on it or by selecting it and
   then pressing **Enter**.
-  A ring control at the top of the dialog box allows you to see all IVI
   attributes or only the attributes of type ViBoolean. If you choose to
   see all IVI attributes, the data types appear to the right of the
   attribute names in the list box. Attributes with data types other
   than ViBoolean are dim. If you select an attribute data type that is
   dim, LabWindows/CVI transfers you to the function panel for the
   corresponding function that is consistent with the data type.
-  If you want to enter a variable name, press **Ctrl**\ +\ **T** to
   change this ring control to a manual input box. If the attribute in
   this ring control has named constants as valid values, you can view
   the constants by moving to the value control and pressing **Enter**.
''',
},
            },
            {
                'direction': 'out',
                'name': 'attributeValue',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Returns the current value of the attribute. Passes the address of a
ViBoolean variable.
If the attribute currently showing in the attribute ring control has
constants as valid values, you can view a list of the constants by
pressing **Enter** on this control. Select a value by double-clicking on
it or by selecting it and then pressing **Enter**.
''',
},
            },
        ],
'documentation': {
'description': '''
| Queries the value of a ViBoolean attribute.
| You can use this function to get the values of device-specific
  attributes and inherent IVI attributes.
''',
},
    },
    'GetAttributeViInt32': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel(s) to which this configuration value
applies. Specify multiple channels by using a channel list or a channel
range. A channel list is a comma (,) separated sequence of channel names
(for example, 0,2 specifies channels 0 and 2). A channel range is a
lower bound channel followed by a hyphen (-) or colon (:) followed by an
upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
In the Running state, multiple output channel configurations are
performed sequentially based on the order specified in this parameter.
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': '''
Specifies the ID of an attribute. From the function panel window, you
can use this control as follows.

-  In the function panel window, click on the control or press **Enter**
   or the spacebar to display a dialog box containing hierarchical list
   of the available attributes. Help text is shown for each attribute.
   Select an attribute by double-clicking on it or by selecting it and
   then pressing **Enter**.
-  A ring control at the top of the dialog box allows you to see all IVI
   attributes or only the attributes of type ViInt32. If you choose to
   see all IVI attributes, the data types appear to the right of the
   attribute names in the list box. Attributes with data types other
   than ViInt32 are dim. If you select an attribute data type that is
   dim, LabWindows/CVI transfers you to the function panel for the
   corresponding function that is consistent with the data type.
-  If you want to enter a variable name, press **Ctrl**\ +\ **T** to
   change this ring control to a manual input box. If the attribute in
   this ring control has named constants as valid values, you can view
   the constants by moving to the value control and pressing **Enter**.
''',
},
            },
            {
                'direction': 'out',
                'name': 'attributeValue',
                'type': 'ViInt32',
'documentation': {
'description': '''
Returns the current value of the attribute. Passes the address of a
ViInt32 variable.
If the attribute currently showing in the attribute ring control has
constants as valid values, you can view a list of the constants by
pressing **Enter** on this control. Select a value by double-clicking on
it or by selecting it and then pressing **Enter**.
''',
},
            },
        ],
'documentation': {
'description': '''
| Queries the value of a ViInt32 attribute.
| You can use this function to get the values of device-specific
  attributes and inherent IVI attributes.
''',
},
    },
    'GetAttributeViInt64': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel(s) to which this configuration value
applies. Specify multiple channels by using a channel list or a channel
range. A channel list is a comma (,) separated sequence of channel names
(for example, 0,2 specifies channels 0 and 2). A channel range is a
lower bound channel followed by a hyphen (-) or colon (:) followed by an
upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
In the Running state, multiple output channel configurations are
performed sequentially based on the order specified in this parameter.
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': '''
Specifies the ID of an attribute. From the function panel window, you
can use this control as follows.

-  In the function panel window, click on the control or press **Enter**
   or the spacebar to display a dialog box containing hierarchical list
   of the available attributes. Help text is shown for each attribute.
   Select an attribute by double-clicking on it or by selecting it and
   then pressing **Enter**.
-  A ring control at the top of the dialog box allows you to see all IVI
   attributes or only the attributes of type ViReal64. If you choose to
   see all IVI attributes, the data types appear to the right of the
   attribute names in the list box. Attributes with data types other
   than ViReal64 are dim. If you select an attribute data type that is
   dim, LabWindows/CVI transfers you to the function panel for the
   corresponding function that is consistent with the data type.
-  If you want to enter a variable name, press **Ctrl**\ +\ **T** to
   change this ring control to a manual input box. If the attribute in
   this ring control has named constants as valid values, you can view
   the constants by moving to the value control and pressing **Enter**.
''',
},
            },
            {
                'direction': 'out',
                'name': 'attributeValue',
                'type': 'ViInt64',
'documentation': {
'description': '''
Returns the current value of the attribute. Passes the address of a
ViReal64 variable.
If the attribute currently showing in the attribute ring control has
constants as valid values, you can view a list of the constants by
pressing **Enter** on this control. Select a value by double-clicking on
it or by selecting it and then pressing **Enter**.
''',
},
            },
        ],
'documentation': {
'description': '''
| Queries the value of a ViInt64 attribute.
| You can use this function to get the values of device-specific
  attributes and inherent IVI attributes.
''',
},
    },
    'GetAttributeViReal64': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel(s) to which this configuration value
applies. Specify multiple channels by using a channel list or a channel
range. A channel list is a comma (,) separated sequence of channel names
(for example, 0,2 specifies channels 0 and 2). A channel range is a
lower bound channel followed by a hyphen (-) or colon (:) followed by an
upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
In the Running state, multiple output channel configurations are
performed sequentially based on the order specified in this parameter.
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': '''
Specifies the ID of an attribute. From the function panel window, you
can use this control as follows.

-  In the function panel window, click on the control or press **Enter**
   or the spacebar to display a dialog box containing hierarchical list
   of the available attributes. Help text is shown for each attribute.
   Select an attribute by double-clicking on it or by selecting it and
   then pressing **Enter**.
-  A ring control at the top of the dialog box allows you to see all IVI
   attributes or only the attributes of type ViReal64. If you choose to
   see all IVI attributes, the data types appear to the right of the
   attribute names in the list box. Attributes with data types other
   than ViReal64 are dim. If you select an attribute data type that is
   dim, LabWindows/CVI transfers you to the function panel for the
   corresponding function that is consistent with the data type.
-  If you want to enter a variable name, press **Ctrl**\ +\ **T** to
   change this ring control to a manual input box. If the attribute in
   this ring control has named constants as valid values, you can view
   the constants by moving to the value control and pressing **Enter**.
''',
},
            },
            {
                'direction': 'out',
                'name': 'attributeValue',
                'type': 'ViReal64',
'documentation': {
'description': '''
Returns the current value of the attribute. Passes the address of a
ViReal64 variable.
If the attribute currently showing in the attribute ring control has
constants as valid values, you can view a list of the constants by
pressing **Enter** on this control. Select a value by double-clicking on
it or by selecting it and then pressing **Enter**.
''',
},
            },
        ],
'documentation': {
'description': '''
| Queries the value of a ViReal64 attribute.
| You can use this function to get the values of device-specific
  attributes and inherent IVI attributes.
''',
},
    },
    'GetAttributeViSession': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel(s) to which this configuration value
applies. Specify multiple channels by using a channel list or a channel
range. A channel list is a comma (,) separated sequence of channel names
(for example, 0,2 specifies channels 0 and 2). A channel range is a
lower bound channel followed by a hyphen (-) or colon (:) followed by an
upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
In the Running state, multiple output channel configurations are
performed sequentially based on the order specified in this parameter.
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': '''
Specifies the ID of an attribute. From the function panel window, you
can use this control as follows.

-  In the function panel window, click on the control or press **Enter**
   or the spacebar to display a dialog box containing hierarchical list
   of the available attributes. Help text is shown for each attribute.
   Select an attribute by double-clicking on it or by selecting it and
   then pressing **Enter**.
-  A ring control at the top of the dialog box allows you to see all IVI
   attributes or only the attributes of type ViSession. If you choose to
   see all IVI attributes, the data types appear to the right of the
   attribute names in the list box. Attributes with data types other
   than ViSession are dim. If you select an attribute data type that is
   dim, LabWindows/CVI transfers you to the function panel for the
   corresponding function that is consistent with the data type.
-  If you want to enter a variable name, press **Ctrl**\ +\ **T** to
   change this ring control to a manual input box. If the attribute in
   this ring control has named constants as valid values, you can view
   the constants by moving to the value control and pressing **Enter**.
''',
},
            },
            {
                'direction': 'out',
                'name': 'attributeValue',
                'type': 'ViSession',
'documentation': {
'description': '''
Returns the current value of the attribute. Passes the address of a
ViSession variable.
If the attribute currently showing in the attribute ring control has
constants as valid values, you can view a list of the constants by
pressing **Enter** on this control. Select a value by double-clicking on
it or by selecting it and then pressing **Enter**.
''',
},
            },
        ],
'documentation': {
'description': '''
| Queries the value of a ViSession attribute.
| You can use this function to get the values of device-specific
  attributes and inherent IVI attributes.
''',
},
    },
    'GetAttributeViString': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel(s) to which this configuration value
applies. Specify multiple channels by using a channel list or a channel
range. A channel list is a comma (,) separated sequence of channel names
(for example, 0,2 specifies channels 0 and 2). A channel range is a
lower bound channel followed by a hyphen (-) or colon (:) followed by an
upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
In the Running state, multiple output channel configurations are
performed sequentially based on the order specified in this parameter.
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': '''
Specifies the ID of an attribute. From the function panel window, you
can use this control as follows.

-  In the function panel window, click on the control or press or the
   spacebar to display a dialog box containing hierarchical list of the
   available attributes. Help text is shown for each attribute. Select
   an attribute by double-clicking on it or by selecting it and then
   pressing .
-  A ring control at the top of the dialog box allows you to see all IVI
   attributes or only the attributes of type ViString. If you choose to
   see all IVI attributes, the data types appear to the right of the
   attribute names in the list box. Attributes with data types other
   than ViString are dimmed. If you select an attribute data type that
   is dimmed, LabWindows/CVI transfers you to the function panel for the
   corresponding function that is consistent with the data type.
-  If you want to enter a variable name, press to change this ring
   control to a manual input control. If the attribute in this ring
   control has named constants as valid values, you can view the
   constants by moving to the value control and pressing .
''',
},
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32',
'documentation': {
'description': '''
Passes the number of bytes in the buffer and specifies the number of
bytes in the ViChar array you specify for **value**. If the current
value of **value**, including the terminating NUL byte, is larger than
the size you indicate in this parameter, the function copies (buffer
size - 1) bytes into the buffer, places an ASCII NUL byte at the end of
the buffer, and returns the buffer size you must pass to get the entire
value. For example, if the value is 123456 and the buffer size is 4, the
function places 123 into the buffer and returns 7.
To obtain the required buffer size, you can pass 0 for this attribute
and VI_NULL for **value**. If you want the function to fill in the
buffer regardless of the number of bytes in the value, pass a negative
number for this attribute.
''',
},
            },
            {
                'direction': 'out',
                'name': 'attributeValue',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The buffer in which the function returns the current value of the
attribute. The buffer must be of type ViChar and have at least as many
bytes as indicated in **bufSize**.
If the current value of the attribute, including the terminating NUL
byte, contains more bytes that you indicate in this attribute, the
function copies (buffer size -1) bytes into the buffer, places an ASCII
NUL byte at the end of the buffer, and returns the buffer size you must
pass to get the entire value. For example, if the value is 123456 and
the buffer size is 4, the function places 123 into the buffer and
returns 7.
If you specify 0 for **bufSize**, you can pass VI_NULL for this
attribute.
If the attribute currently showing in the attribute ring control has
constants as valid values, you can view a list of the constants by
pressing on this control. Select a value by double-clicking on it or by
selecting it and then pressing .
''',
},
            },
        ],
'documentation': {
'description': '''
| Queries the value of a ViString attribute.
| You can use this function to get the values of device-specific
  attributes and inherent IVI attributes.
''',
},
    },
    'GetCalUserDefinedInfo': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitExtCal or niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'out',
                'name': 'Info',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Returns the user-defined information stored in the device onboard
EEPROM.
''',
},
            },
        ],
'documentation': {
'description': 'Returns the user-defined information in the device onboard EEPROM.',
},
    },
    'GetCalUserDefinedInfoMaxSize': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitExtCal or niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'out',
                'name': 'infoSize',
                'type': 'ViInt32',
'documentation': {
'description': '''
Returns the number of characters that can be stored in the device
onboard EEPROM.
''',
},
            },
        ],
'documentation': {
'description': '''
Returns the maximum number of characters that can be used to store
user-defined information in the device onboard EEPROM.
''',
},
    },
    'GetChannelName': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Index',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies which output channel name to return. The index values begin at
1.
''',
},
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the number of bytes in the ViChar array you specify for
**channelName**. If the **channelName**, including the terminating NUL
byte, contains more bytes than you indicate in this attribute, the
function copies (buffer size - 1) bytes into the buffer, places an ASCII
NUL byte at the end of the buffer, and returns the buffer size you must
pass to get the entire value. For example, if the value is 123456 and
the buffer size is 4, the function places 123 into the buffer and
returns 7.
If you pass 0, you can pass VI_NULL for **channelName**.
''',
},
            },
            {
                'direction': 'out',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': 'Returns the output channel name that corresponds to **index**.',
},
            },
        ],
'documentation': {
'description': '''
Retrieves the output **channelName** that corresponds to the requested
**index**. Use the NIDCPOWER_ATTR_CHANNEL_COUNT attribute to
determine the upper bound of valid values for **index**.
''',
},
    },
    'GetError': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'out',
                'name': 'Code',
                'type': 'ViStatus',
'documentation': {
'description': 'Returns the error code for the session or execution thread.',
},
            },
            {
                'direction': 'in',
                'name': 'BufferSize',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the number of bytes in the ViChar array you specify for
**description**.
If the error description, including the terminating NUL byte, contains
more bytes than you indicate in this attribute, the function copies
(buffer size - 1) bytes into the buffer, places an ASCII NUL byte at the
end of the buffer, and returns the buffer size you must pass to get the
entire value. For example, if the value is 123456 and the buffer size is
4, the function places 123 into the buffer and returns 7.
If you pass 0 for this attribute, you can pass VI_NULL for
**description**.
''',
},
            },
            {
                'direction': 'out',
                'name': 'Description',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Returns the error description for the IVI session or execution thread.
If there is no description, the function returns an empty string.
The buffer must contain at least as many elements as the value you
specify with **bufferSize**. If the error description, including the
terminating NUL byte, contains more bytes than you indicate with
**bufferSize**, the function copies (buffer size - 1) bytes into the
buffer, places an ASCII NUL byte at the end of the buffer, and returns
the buffer size you must pass to get the entire value. For example, if
the value is 123456 and the buffer size is 4, the function places 123
into the buffer and returns 7.
If you pass 0 for **bufferSize**, you can pass VI_NULL for this
attribute.
''',
},
            },
        ],
'documentation': {
'description': '''
| Retrieves and then clears the IVI error information for the session or
  the current execution thread unless **bufferSize** is 0, in which case
  the function does not clear the error information. By passing 0 for
  the buffer size, you can ascertain the buffer size required to get the
  entire error description string and then call the function again with
  a sufficiently large buffer size.
| If the user specifies a valid IVI session for **vi**, this function
  retrieves and then clears the error information for the session. If
  the user passes VI_NULL for **vi**, this function retrieves and then
  clears the error information for the current execution thread. If
  **vi** is an invalid session, the function does nothing and returns an
  error. Normally, the error information describes the first error that
  occurred since the user last called niDCPower_GetError or
  niDCPower_ClearError.
''',
},
    },
    'GetExtCalLastDateAndTime': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitExtCal or niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'out',
                'name': 'Year',
                'type': 'ViInt32',
'documentation': {
'description': 'Returns the **year** the device was last calibrated.',
},
            },
            {
                'direction': 'out',
                'name': 'Month',
                'type': 'ViInt32',
'documentation': {
'description': 'Returns the **month** in which the device was last calibrated.',
},
            },
            {
                'direction': 'out',
                'name': 'Day',
                'type': 'ViInt32',
'documentation': {
'description': 'Returns the **day** on which the device was last calibrated.',
},
            },
            {
                'direction': 'out',
                'name': 'Hour',
                'type': 'ViInt32',
'documentation': {
'description': '''
Returns the **hour** (in 24-hour time) in which the device was last
calibrated.
''',
},
            },
            {
                'direction': 'out',
                'name': 'Minute',
                'type': 'ViInt32',
'documentation': {
'description': 'Returns the **minute** in which the device was last calibrated.',
},
            },
        ],
'documentation': {
'description': '''
Returns the date and time of the last successful calibration. The time
returned is 24-hour (military) local time; for example, if the device
was calibrated at 2:30 PM, this function returns 14 for **hours** and 30
for **minutes**.
''',
},
    },
    'GetExtCalLastTemp': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitExtCal or niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'out',
                'name': 'Temperature',
                'type': 'ViReal64',
'documentation': {
'description': '''
Returns the onboard **temperature** of the device, in degrees Celsius,
during the last successful external calibration.
''',
},
            },
        ],
'documentation': {
'description': '''
Returns the onboard **temperature** of the device, in degrees Celsius,
during the last successful external calibration.
''',
},
    },
    'GetExtCalRecommendedInterval': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitExtCal or niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'out',
                'name': 'Months',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the recommended maximum interval, in **months**, between
external calibrations.
''',
},
            },
        ],
'documentation': {
'description': '''
Returns the recommended maximum interval, in **months**, between
external calibrations.
''',
},
    },
    'GetNextCoercionRecord': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the number of bytes in the ViChar array you specify for
**coercionRecord**. If the next coercion record string, including the
terminating NUL byte, contains more bytes than you indicate in this
attribute, the function copies (buffer size - 1) bytes into the buffer,
places an ASCII NUL byte at the end of the buffer, and returns the
buffer size you must pass to get the entire value. For example, if the
value is 123456 and the buffer size is 4, the function places 123 into
the buffer and returns 7.
If you pass 0, you can pass VI_NULL for **coercionRecord**.
''',
},
            },
            {
                'direction': 'out',
                'name': 'coercionRecord',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Returns the next **coercionRecord** for the IVI session. If there are no
**coercionRecords**, the function returns an empty string.
''',
},
            },
        ],
'documentation': {
'description': '''
Returns the coercion information associated with the IVI session and
clears the earliest instance in which NI-DCPower coerced a value you
specified.
''',
},
    },
    'GetNextInterchangeWarning': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the number of bytes in the ViChar array you specify for
**interchangeWarning**. If the next interchangeability warning string,
including the terminating NUL byte, contains more bytes than you
indicate in this attribute, the function copies (buffer size - 1) bytes
into the buffer, places an ASCII NUL byte at the end of the buffer, and
returns the buffer size you must pass to get the entire value. For
example, if the value is 123456 and the buffer size is 4, the function
places 123 into the buffer and returns 7.
If you pass 0, you can pass VI_NULL for **interchangeWarning**.
''',
},
            },
            {
                'direction': 'out',
                'name': 'interchangeWarning',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Returns the next interchange warning for the IVI session. If there are
no interchange warnings, the function returns an empty string.
''',
},
            },
        ],
'documentation': {
'description': '''
This function returns the interchangeability warning associated with the
IVI session. It retrieves and clears the earliest instance in which the
class driver recorded an interchangeability warning. Interchangeability
warnings indicate that using your application with a different device
may cause a different behavior.

NI-DCPower performs interchangeability checking when the
NIDCPOWER_ATTR_INTERCHANGE_CHECK attribute is set to VI_TRUE. This
function returns an empty string in warning if no interchangeability
warnings remain for the session. In general, NI-DCPower generates
interchangeability warnings when an attribute that affects the behavior
of the device is in a state that you did not specify.
''',
},
    },
    'GetSelfCalLastDateAndTime': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitExtCal or niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'out',
                'name': 'Year',
                'type': 'ViInt32',
'documentation': {
'description': 'Returns the **year** the device was last calibrated.',
},
            },
            {
                'direction': 'out',
                'name': 'Month',
                'type': 'ViInt32',
'documentation': {
'description': 'Returns the **month** in which the device was last calibrated.',
},
            },
            {
                'direction': 'out',
                'name': 'Day',
                'type': 'ViInt32',
'documentation': {
'description': 'Returns the **day** on which the device was last calibrated.',
},
            },
            {
                'direction': 'out',
                'name': 'Hour',
                'type': 'ViInt32',
'documentation': {
'description': '''
Returns the **hour** (in 24-hour time) in which the device was last
calibrated.
''',
},
            },
            {
                'direction': 'out',
                'name': 'Minute',
                'type': 'ViInt32',
'documentation': {
'description': 'Returns the **minute** in which the device was last calibrated.',
},
            },
        ],
'documentation': {
'description': '''
Returns the date and time of the oldest successful self-calibration from
among the channels in the session.

The time returned is 24-hour (military) local time; for example, if you
have a session using channels 1 and 2, and a self-calibration was
performed on channel 1 at 2:30 PM, and a self-calibration was performed
on channel 2 at 3:00 PM on the same day, this function returns 14 for
**hours** and 30 for **minutes**.
''',
'note': '''
This function is not supported on all devices. Refer to `Supported
Functions by
Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
for more information about supported devices.
''',
},
    },
    'GetSelfCalLastTemp': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitExtCal or niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'out',
                'name': 'Temperature',
                'type': 'ViReal64',
'documentation': {
'description': '''
Returns the onboard **temperature** of the device, in degrees Celsius,
during the oldest successful calibration.
''',
},
            },
        ],
'documentation': {
'description': '''
Returns the onboard temperature of the device, in degrees Celsius,
during the oldest successful self-calibration from among the channels in
the session.

For example, if you have a session using channels 1 and 2, and you
perform a self-calibration on channel 1 with a device temperature of 25
degrees Celsius at 2:00, and a self-calibration was performed on channel
2 at 27 degrees Celsius at 3:00 on the same day, this function returns
25 for the **temperature** parameter.
''',
'note': '''
This function is not supported on all devices. Refer to `Supported
Functions by
Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
for more information about supported devices.
''',
},
    },
    'InitExtCal': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'resourceName',
                'type': 'ViRsrc',
'documentation': {
'description': '''
Specifies the **resourceName** assigned by Measurement & Automation
Explorer (MAX), for example "PXI1Slot3" where "PXI1Slot3" is an
instrument's **resourceName**. **resourceName** can also be a logical
IVI name.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Password',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the **password** for opening a calibration session. The
initial password is factory configured to "NI". **password** can be a
maximum of four alphanumeric characters.
''',
},
            },
            {
                'direction': 'out',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Returns a handle that you use to identify the session in all subsequent
NI-DCPower function calls.
''',
},
            },
        ],
'documentation': {
'description': '''
If **password** is valid, this function creates a new IVI instrument
driver session to the device specified in **resourceName** and returns
an instrument handle you use to identify the device in all subsequent
NI-DCPower function calls. This function also sends initialization
commands to set the device to the state necessary for the operation of
NI-DCPower.

Opening a calibration session always performs a reset. Refer to the
calibration procedure for the device you are calibrating for detailed
instructions on the appropriate use of this function. This function uses
the `deprecated programming state
model <REPLACE_DRIVER_SPECIFIC_URL_1(initializedeprecatedmodel)>`__.
''',
},
    },
    'InitWithOptions': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'resourceName',
                'type': 'ViRsrc',
'documentation': {
'description': '''
Specifies the **resourceName** assigned by Measurement & Automation
Explorer (MAX), for example "PXI1Slot3" where "PXI1Slot3" is an
instrument's **resourceName**. **resourceName** can also be a logical
IVI name.
''',
},
            },
            {
                'direction': 'in',
                'name': 'idQuery',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether the device is queried to determine if the device is a
valid instrument for NI-DCPower.
''',
},
            },
            {
                'direction': 'in',
                'name': 'resetDevice',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether to reset the device during the initialization
procedure.
''',
},
            },
            {
                'direction': 'in',
                'name': 'optionString',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the initial value of certain attributes for the session. The
syntax for **optionString** is a list of attributes with an assigned
value where 1 is VI_TRUE and 0 is VI_FALSE. Each attribute/value
combination is delimited with a comma, as shown in the following
example:

"Simulate=0,RangeCheck=1,QueryInstrStatus=0,Cache=1"

If you do not wire this input or pass an empty string, the session
assigns the default values, shown in the example, for these attributes.
You do not have to specify a value for all the attributes. If you do not
specify a value for an attribute, the default value is used.

For more information about simulating a device, refer to `Simulating a
Power Supply or SMU <REPLACE_DRIVER_SPECIFIC_URL_1(simulate)>`__.
''',
},
            },
            {
                'direction': 'out',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Returns a handle that you use to identify the device in all subsequent
NI-DCPower function calls.
''',
},
            },
        ],
'documentation': {
'description': '''
This function is deprecated. Use niDCPower_InitializeWithChannels
instead.

Creates a new IVI instrument driver session to the device specified in
**resourceName** and returns a session handle you use to identify the
device in all subsequent NI-DCPower function calls. With this function,
you can optionally set the initial state of the following session
attributes:

-  NIDCPOWER_ATTR_SIMULATE
-  NIDCPOWER_ATTR_DRIVER_SETUP
-  NIDCPOWER_ATTR_RANGE_CHECK
-  NIDCPOWER_ATTR_QUERY_INSTRUMENT_STATUS
-  NIDCPOWER_ATTR_CACHE
-  NIDCPOWER_ATTR_RECORD_COERCIONS

This function also sends initialization commands to set the device to
the state necessary for NI-DCPower to operate.

To place the device in a known start-up state when creating a new
session, set **resetDevice** to VI_TRUE. This action is equivalent to
using the niDCPower_reset function.

To open a session and leave the device in its existing configuration
without passing through a transitional output state, set **resetDevice**
to VI_FALSE, and immediately call the niDCPower_Abort function. Then
configure the device as in the previous session changing only the
desired settings, and then call the niDCPower_Initiate function.

Refer to the `deprecated programming state
model <REPLACE_DRIVER_SPECIFIC_URL_1(initializedeprecatedmodel)>`__ for
information about the specific software states.
''',
},
    },
    'InitializeWithChannels': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'resourceName',
                'type': 'ViRsrc',
'documentation': {
'description': '''
Specifies the **resourceName** assigned by Measurement & Automation
Explorer (MAX), for example "PXI1Slot3" where "PXI1Slot3" is an
instrument's **resourceName**. **resourceName** can also be a logical
IVI name.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Channels',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies which output channel(s) to include in a new session. Specify
multiple channels by using a channel list or a channel range. A channel
list is a comma (,) separated sequence of channel names (for example,
0,2 specifies channels 0 and 2). A channel range is a lower bound
channel followed by a hyphen (-) or colon (:) followed by an upper bound
channel (for example, 0-2 specifies channels 0, 1, and 2). In the
Running state, multiple output channel configurations are performed
sequentially based on the order specified in this parameter. If you do
not specify any channels, by default all channels on the device are
included in the session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Reset',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether to reset the device during the initialization
procedure.
''',
},
            },
            {
                'direction': 'in',
                'name': 'optionString',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the initial value of certain attributes for the session. The
syntax for **optionString** is a list of attributes with an assigned
value where 1 is VI_TRUE and 0 is VI_FALSE. For example:

"Simulate=0"

You do not have to specify a value for all the attributes. If you do not
specify a value for an attribute, the default value is used.

For more information about simulating a device, refer to `Simulating a
Power Supply or SMU <REPLACE_DRIVER_SPECIFIC_URL_1(simulate)>`__.
''',
},
            },
            {
                'direction': 'out',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Returns a session handle that you use to identify the device in all
subsequent NI-DCPower function calls.
''',
},
            },
        ],
'documentation': {
'description': '''
Creates and returns a new NI-DCPower session to the power supply or SMU
specified in **resource name** to be used in all subsequent NI-DCPower
function calls. With this function, you can optionally set the initial
state of the following session attributes:

-  NIDCPOWER_ATTR_SIMULATE
-  NIDCPOWER_ATTR_DRIVER_SETUP

After calling this function, the session will be in the Uncommitted
state. Refer to the `Programming
States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic for
details about specific software states.

To place the device in a known start-up state when creating a new
session, set **reset** to VI_TRUE. This action is equivalent to using
the niDCPower_reset function immediately after initializing the
session.

To open a session and leave the device in its existing configuration
without passing through a transitional output state, set **reset** to
VI_FALSE. Then configure the device as in the previous session,
changing only the desired settings, and then call the
niDCPower_Initiate function.

**Related Topics:**

`Programming
States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__
''',
},
    },
    'Initiate': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
        ],
'documentation': {
'description': '''
Starts generation or acquisition, causing the NI-DCPower session to
leave the Uncommitted state or Committed state and enter the Running
state. To return to the Committed state call the niDCPower_Abort
function. Refer to the `Programming
States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic in
the *NI DC Power Supplies and SMUs Help* for information about the
specific NI-DCPower software states.

**Related Topics:**

`Programming
States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__
''',
},
    },
    'LockSession': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'out',
                'name': 'callerHasLock',
                'type': 'ViBoolean',
'documentation': {
'description': '''
| This parameter is optional. If you do not want to use this parameter,
  pass VI_NULL.
| Use this parameter in complex functions to keep track of whether you
  obtain a lock and therefore need to unlock the session. Pass the
  address of a local ViBoolean variable. In the declaration of the local
  variable, initialize it to VI_FALSE. Pass the address of the same
  local variable to any other calls you make to the
  niDCPower_LockSession function or the niDCPower_UnlockSession
  function in the same function.
| The parameter is an input/output parameter. The niDCPower_LockSession
  and niDCPower_UnlockSession functions each inspect the current value
  and take the following actions.

-  If the value is VI_TRUE, the niDCPower_LockSession function does
   not lock the session again.
-  If the value is VI_FALSE, the niDCPower_LockSession function
   obtains the lock and sets the value of the parameter to VI_TRUE.
-  If the value is VI_FALSE, the niDCPower_UnlockSession function does
   not attempt to unlock the session.
-  If the value is VI_TRUE, the niDCPower_UnlockSession function
   releases the lock and sets the value of the parameter to VI_FALSE.

| Thus, you can, call the niDCPower_UnlockSession function at the end
  of your function without worrying about whether you actually have the
  lock, as shown in the following example.
| ViStatus TestFunc (ViSession vi, ViInt32 flags)
  {
  ViStatus error = VI_SUCCESS;
  ViBoolean haveLock = VI_FALSE;
  if (flags & BIT_1)
  {
  viCheckErr( niDCPower_LockSession(vi, &haveLock;));
  viCheckErr( TakeAction1(vi));
  if (flags & BIT_2)
  {
  viCheckErr( niDCPower_UnlockSession(vi, &haveLock;));
  viCheckErr( TakeAction2(vi));
  viCheckErr( niDCPower_LockSession(vi, &haveLock;);
  }
  if (flags & BIT_3)
  viCheckErr( TakeAction3(vi));
  }
  Error:
  /\*At this point, you cannot really be sure that you have the lock.
  Fortunately, the haveLock variable takes care of that for you.\*/
  niDCPower_UnlockSession(vi, &haveLock;);
  return error;
| }
''',
},
            },
        ],
'documentation': {
'description': '''
| Obtains a multithread lock on the device session. Before doing so, the
  software waits until all other execution threads release their locks
  on the device session.
| Other threads may have obtained a lock on this session for the
  following reasons:

-  The application called the niDCPower_LockSession function.
-  A call to NI-DCPower locked the session.
-  A call to the IVI engine locked the session.
-  After a call to the niDCPower_LockSession function returns
   successfully, no other threads can access the device session until
   you call the niDCPower_UnlockSession function.
-  Use the niDCPower_LockSession function and the
   niDCPower_UnlockSession function around a sequence of calls to
   instrument driver functions if you require that the device retain its
   settings through the end of the sequence.

You can safely make nested calls to the niDCPower_LockSession function
within the same thread. To completely unlock the session, you must
balance each call to the niDCPower_LockSession function with a call to
the niDCPower_UnlockSession function. If, however, you use
**Caller_Has_Lock** in all calls to the niDCPower_LockSession and
niDCPower_UnlockSession function within a function, the IVI Library
locks the session only once within the function regardless of the number
of calls you make to the niDCPower_LockSession function. This behavior
allows you to call the niDCPower_UnlockSession function just once at
the end of the function.
''',
},
    },
    'Measure': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel to measure. Only one measurement at a time
may be made with the niDCPower_Measure function. Use the
niDCPower_MeasureMultiple function to measure multiple channels.
''',
},
            },
            {
                'direction': 'in',
                'name': 'measurementType',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies whether a voltage or current value is measured.
**Defined Values**:
''',
'table_body': [['NIDCPOWER_VAL_MEASURE_VOLTAGE (1)', 'The device measures voltage.'], ['NIDCPOWER_VAL_MEASURE_CURRENT (0)', 'The device measures current.']],
},
            },
            {
                'direction': 'out',
                'name': 'Measurement',
                'type': 'ViReal64',
'documentation': {
'description': '''
Returns the value of the measurement, either in volts for voltage or
amps for current.
''',
},
            },
        ],
'documentation': {
'description': '''
Returns the measured value of either the voltage or current on the
specified output channel. Each call to this function blocks other
function calls until the hardware returns the **measurement**. To
measure multiple output channels, use the niDCPower_MeasureMultiple
function.
''',
},
    },
    'MeasureMultiple': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channels to measure. You can specify multiple
channels by using a channel list or a channel range. A channel list is a
comma (,) separated sequence of channel names (e.g. 0,2 specifies
channels 0 and 2). A channel range is a lower bound channel followed by
a hyphen (-) or colon (:) followed by an upper bound channel (e.g. 0-2
specifies channels 0, 1, and 2). If you do not specify a channel name,
the function uses all channels in the session.
''',
},
            },
            {
                'direction': 'out',
                'name': 'voltageMeasurements',
                'type': 'ViReal64[]',
'documentation': {
'description': '''
Returns an array of voltage measurements. The measurements in the array
are returned in the same order as the channels specified in
**channelName**. Ensure that sufficient space has been allocated for the
returned array.
''',
},
            },
            {
                'direction': 'out',
                'name': 'currentMeasurements',
                'type': 'ViReal64[]',
'documentation': {
'description': '''
Returns an array of current measurements. The measurements in the array
are returned in the same order as the channels specified in
**channelName**. Ensure that sufficient space has been allocated for the
returned array.
''',
},
            },
        ],
'documentation': {
'description': '''
Returns arrays of the measured voltage and current values on the
specified output channel(s). Each call to this function blocks other
function calls until the measurements are returned from the device. The
order of the measurements returned in the array corresponds to the order
on the specified output channel(s).
''',
},
    },
    'QueryInCompliance': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel to query. Compliance status can only be
queried for one channel at a time.
''',
},
            },
            {
                'direction': 'out',
                'name': 'inCompliance',
                'type': 'ViBoolean',
'documentation': {
'description': 'Returns whether the device output channel is in compliance.',
},
            },
        ],
'documentation': {
'description': '''
Queries the specified output device to determine if it is operating at
the `compliance <REPLACE_DRIVER_SPECIFIC_URL_2(compliance)>`__ limit.

The compliance limit is the current limit when the output function is
set to NIDCPOWER_VAL_DC_VOLTAGE. If the output is operating at the
compliance limit, the output reaches the current limit before the
desired voltage level. Refer to the niDCPower_ConfigureOutputFunction
function and the niDCPower_ConfigureCurrentLimit function for more
information about output function and current limit, respectively.

The compliance limit is the voltage limit when the output function is
set to NIDCPOWER_VAL_DC_CURRENT. If the output is operating at the
compliance limit, the output reaches the voltage limit before the
desired current level. Refer to the niDCPower_ConfigureOutputFunction
function and the niDCPower_ConfigureVoltageLimit function for more
information about output function and voltage limit, respectively.

**Related Topics:**

`Compliance <REPLACE_DRIVER_SPECIFIC_URL_1(compliance)>`__
''',
},
    },
    'QueryMaxCurrentLimit': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel to query. The maximum current limit may
only be queried for one channel at a time.
''',
},
            },
            {
                'direction': 'in',
                'name': 'voltageLevel',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the voltage level to use when calculating the
**maxCurrentLimit**.
''',
},
            },
            {
                'direction': 'out',
                'name': 'maxCurrentLimit',
                'type': 'ViReal64',
'documentation': {
'description': '''
Returns the maximum current limit that can be set with the specified
**voltageLevel**.
''',
},
            },
        ],
'documentation': {
'description': '''
Queries the maximum current limit on an output channel if the output
channel is set to the specified **voltageLevel**.
''',
},
    },
    'QueryMaxVoltageLevel': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel to query. The maximum voltage level may
only be queried for one channel at a time.
''',
},
            },
            {
                'direction': 'in',
                'name': 'currentLimit',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the current limit to use when calculating the
**maxVoltageLevel**.
''',
},
            },
            {
                'direction': 'out',
                'name': 'maxVoltageLevel',
                'type': 'ViReal64',
'documentation': {
'description': '''
Returns the maximum voltage level that can be set on an output channel
with the specified **currentLimit**.
''',
},
            },
        ],
'documentation': {
'description': '''
Queries the maximum voltage level on an output channel if the output
channel is set to the specified **currentLimit**.
''',
},
    },
    'QueryMinCurrentLimit': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel to query. The minimum current limit may
only be queried for one channel at a time.
''',
},
            },
            {
                'direction': 'in',
                'name': 'voltageLevel',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the voltage level to use when calculating the
**minCurrentLimit**.
''',
},
            },
            {
                'direction': 'out',
                'name': 'minCurrentLimit',
                'type': 'ViReal64',
'documentation': {
'description': '''
Returns the minimum current limit that can be set on an output channel
with the specified **voltageLevel**.
''',
},
            },
        ],
'documentation': {
'description': '''
Queries the minimum current limit on an output channel if the output
channel is set to the specified **voltageLevel**.
''',
},
    },
    'QueryOutputState': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel to query. The output state may only be
queried for one channel at a time.
''',
},
            },
            {
                'direction': 'in',
                'name': 'outputState',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the output state of the output channel that is being queried.
**Defined Values**:
''',
'table_body': [['NIDCPOWER_VAL_OUTPUT_CONSTANT_VOLTAGE (0)', 'The device maintains a constant voltage by adjusting the current.'], ['NIDCPOWER_VAL_OUTPUT_CONSTANT_CURRENT (1)', 'The device maintains a constant current by adjusting the voltage.']],
},
            },
            {
                'direction': 'out',
                'name': 'inState',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Returns whether the device output channel is in the specified output
state.
''',
},
            },
        ],
'documentation': {
'description': '''
Queries the specified output channel to determine if the output channel
is currently in the state specified by **outputState**.

**Related Topics:**

`Compliance <REPLACE_DRIVER_SPECIFIC_URL_1(compliance)>`__
''',
},
    },
    'ReadCurrentTemperature': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitExtCal or niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'out',
                'name': 'Temperature',
                'type': 'ViReal64',
'documentation': {
'description': 'Returns the onboard **temperature**, in degrees Celsius, of the device.',
},
            },
        ],
'documentation': {
'description': '''
Returns the current onboard **temperature**, in degrees Celsius, of the
device.
''',
},
    },
    'ResetDevice': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
        ],
'documentation': {
'description': '''
Resets the device to a known state. The function disables power
generation, resets session attributes to their default values, clears
errors such as overtemperature and unexpected loss of auxiliary power,
commits the session attributes, and leaves the session in the
Uncommitted state. This function also performs a hard reset on the
device and driver software. This function has the same functionality as
using reset in Measurement & Automation Explorer. Refer to the
`Programming
States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic for
more information about NI-DCPower software states.

This will also open the output relay on devices that have an output
relay.
''',
},
    },
    'ResetInterchangeCheck': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
        ],
'documentation': {
'description': '''
When developing a complex test system that consists of multiple test
modules, it is generally a good idea to design the test modules so that
they can run in any order. To do so requires ensuring that each test
module completely configures the state of each instrument it uses. If a
particular test module does not completely configure the state of an
instrument, the state of the instrument depends on the configuration
from a previously executed test module. If you execute the test modules
in a different order, the behavior of the instrument and therefore the
entire test module is likely to change. This change in behavior is
generally instrument specific and represents an interchangeability
problem.

You can use this function to test for such cases. After you call this
function, the interchangeability checking algorithms in the specific
driver ignore all previous configuration operations. By calling this
function at the beginning of a test module, you can determine whether
the test module has dependencies on the operation of previously executed
test modules.

This function does not clear the interchangeability warnings from the
list of previously recorded interchangeability warnings. If you want to
guarantee that the niDCPower_GetNextInterchangeWarning function only
returns those interchangeability warnings that are generated after
calling this function, you must clear the list of interchangeability
warnings. You can clear the interchangeability warnings list by
repeatedly calling the niDCPower_GetNextInterchangeWarning function
until no more interchangeability warnings are returned. If you are not
interested in the content of those warnings, you can call the
niDCPower_ClearInterchangeWarnings function.
''',
'note': '''
niDCPower_GetNextInterchangeWarning does not mark any attributes for
an interchange check.
''',
},
    },
    'ResetWithDefaults': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
        ],
'documentation': {
'description': '''
Resets the device to a known state. This function disables power
generation, resets session attributes to their default values, commits
the session attributes, and leaves the session in the
`Running <javascript:LaunchHelp('NI_DC_Power_Supplies_Help.chm::/programmingStates.html#running')>`__
state. In addition to exhibiting the behavior of the niDCPower_reset
function, this function can assign user-defined default values for
configurable attributes from the IVI configuration.
''',
},
    },
    'SendSoftwareEdgeTrigger': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Trigger',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies which trigger to assert.
**Defined Values:**
''',
'table_body': [['NIDCPOWER_VAL_START_TRIGGER (1034)', 'Asserts the Start trigger.'], ['NIDCPOWER_VAL_SOURCE_TRIGGER (1035)', 'Asserts the Source trigger.'], ['NIDCPOWER_VAL_MEASURE_TRIGGER (1036)', 'Asserts the Measure trigger.'], ['NIDCPOWER_VAL_SEQUENCE_ADVANCE_TRIGGER (1037)', 'Asserts the Sequence Advance trigger.'], ['NIDCPOWER_VAL_PULSE_TRIGGER (1053', 'Asserts the Pulse trigger.']],
},
            },
        ],
'documentation': {
'description': '''
Asserts the specified trigger. This function can override an external
edge trigger.

**Related Topics:**

`Triggers <REPLACE_DRIVER_SPECIFIC_URL_1(trigger)>`__
''',
'note': '''
This function is not supported on all devices. Refer to `Supported
Functions by
Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
for more information about supported devices.
''',
},
    },
    'SetAttributeViBoolean': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel(s) to which this configuration value
applies. Specify multiple channels by using a channel list or a channel
range. A channel list is a comma (,) separated sequence of channel names
(for example, 0,2 specifies channels 0 and 2). A channel range is a
lower bound channel followed by a hyphen (-) or colon (:) followed by an
upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
In the Running state, multiple output channel configurations are
performed sequentially based on the order specified in this parameter.
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': '''
Specifies the ID of an attribute. From the function panel window, you
can use this control as follows.

-  In the function panel window, click on the control or press **Enter**
   or the spacebar to display a dialog box containing hierarchical list
   of the available attributes. Attributes whose value cannot be set are
   dim. Help text is shown for each attribute. Select an attribute by
   double-clicking on it or by selecting it and then pressing **Enter**.
-  Read-only attributes appear dim in the list box. If you select a
   read-only attribute, an error message appears. A ring control at the
   top of the dialog box allows you to see all IVI attributes or only
   the attributes of type ViBoolean. If you choose to see all IVI
   attributes, the data types appear to the right of the attribute names
   in the list box. Attributes with data types other than ViBoolean are
   dim. If you select an attribute data type that is dim, LabWindows/CVI
   transfers you to the function panel for the corresponding function
   that is consistent with the data type.
-  If you want to enter a variable name, press **Ctrl**\ +\ **T** to
   change this ring control to a manual input box. If the attribute in
   this ring control has named constants as valid values, you can view
   the constants by moving to the value control and pressing **Enter**.
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies the value to which you want to set the attribute. If the
attribute currently showing in the attribute ring control has constants
as valid values, you can view a list of the constants by pressing
**Enter** on this control. Select a value by double-clicking on it or by
selecting it and then pressing **Enter**.
''',
'note': '''
Some of the values might not be valid depending upon the current
settings of the device session.
''',
},
            },
        ],
'documentation': {
'description': '''
| Sets the value of a ViBoolean attribute.
| This is a low-level function that you can use to set the values of
  device-specific attributes and inherent IVI attributes.
''',
},
    },
    'SetAttributeViInt32': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel(s) to which this configuration value
applies. Specify multiple channels by using a channel list or a channel
range. A channel list is a comma (,) separated sequence of channel names
(for example, 0,2 specifies channels 0 and 2). A channel range is a
lower bound channel followed by a hyphen (-) or colon (:) followed by an
upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
In the Running state, multiple output channel configurations are
performed sequentially based on the order specified in this parameter.
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': '''
Specifies the ID of an attribute. From the function panel window, you
can use this control as follows.

-  In the function panel window, click on the control or press **Enter**
   or the spacebar to display a dialog box containing hierarchical list
   of the available attributes. Attributes whose value cannot be set are
   dim. Help text is shown for each attribute. Select an attribute by
   double-clicking on it or by selecting it and then pressing **Enter**.
-  Read-only attributes appear dim in the list box. If you select a
   read-only attribute, an error message appears. A ring control at the
   top of the dialog box allows you to see all IVI attributes or only
   the attributes of type ViInt32. If you choose to see all IVI
   attributes, the data types appear to the right of the attribute names
   in the list box. Attributes with data types other than ViInt32 are
   dim. If you select an attribute data type that is dim, LabWindows/CVI
   transfers you to the function panel for the corresponding function
   that is consistent with the data type.
-  If you want to enter a variable name, press **Ctrl**\ +\ **T** to
   change this ring control to a manual input box. If the attribute in
   this ring control has named constants as valid values, you can view
   the constants by moving to the value control and pressing **Enter**.
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the value to which you want to set the attribute. If the
attribute currently showing in the attribute ring control has constants
as valid values, you can view a list of the constants by pressing
**Enter** on this control. Select a value by double-clicking on it or by
selecting it and then pressing **Enter**.
''',
'note': '''
Some of the values might not be valid depending upon the current
settings of the device session.
''',
},
            },
        ],
'documentation': {
'description': '''
| Sets the value of a ViInt32 attribute.
| This is a low-level function that you can use to set the values of
  device-specific attributes and inherent IVI attributes.
''',
},
    },
    'SetAttributeViInt64': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel(s) to which this configuration value
applies. Specify multiple channels by using a channel list or a channel
range. A channel list is a comma (,) separated sequence of channel names
(for example, 0,2 specifies channels 0 and 2). A channel range is a
lower bound channel followed by a hyphen (-) or colon (:) followed by an
upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
In the Running state, multiple output channel configurations are
performed sequentially based on the order specified in this parameter.
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': '''
Specifies the ID of an attribute. From the function panel window, you
can use this control as follows.

-  In the function panel window, click on the control or press **Enter**
   or the spacebar to display a dialog box containing hierarchical list
   of the available attributes. Attributes whose value cannot be set are
   dim. Help text is shown for each attribute. Select an attribute by
   double-clicking on it or by selecting it and then pressing **Enter**.
-  Read-only attributes appear dim in the list box. If you select a
   read-only attribute, an error message appears. A ring control at the
   top of the dialog box allows you to see all IVI attributes or only
   the attributes of type ViReal64. If you choose to see all IVI
   attributes, the data types appear to the right of the attribute names
   in the list box. Attributes with data types other than ViReal64 are
   dim. If you select an attribute data type that is dim, LabWindows/CVI
   transfers you to the function panel for the corresponding function
   that is consistent with the data type.
-  If you want to enter a variable name, press **Ctrl**\ +\ **T** to
   change this ring control to a manual input box. If the attribute in
   this ring control has named constants as valid values, you can view
   the constants by moving to the value control and pressing **Enter**.
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViInt64',
'documentation': {
'description': '''
Specifies the value to which you want to set the attribute. If the
attribute currently showing in the attribute ring control has constants
as valid values, you can view a list of the constants by pressing
**Enter** on this control. Select a value by double-clicking on it or by
selecting it and then pressing **Enter**.
''',
'note': '''
Some of the values might not be valid depending upon the current
settings of the device session.
''',
},
            },
        ],
'documentation': {
'description': '''
| Sets the value of a ViInt64 attribute.
| This is a low-level function that you can use to set the values of
  device-specific attributes and inherent IVI attributes.
''',
},
    },
    'SetAttributeViReal64': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel(s) to which this configuration value
applies. Specify multiple channels by using a channel list or a channel
range. A channel list is a comma (,) separated sequence of channel names
(for example, 0,2 specifies channels 0 and 2). A channel range is a
lower bound channel followed by a hyphen (-) or colon (:) followed by an
upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
In the Running state, multiple output channel configurations are
performed sequentially based on the order specified in this parameter.
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': '''
Specifies the ID of an attribute. From the function panel window, you
can use this control as follows.

-  In the function panel window, click on the control or press **Enter**
   or the spacebar to display a dialog box containing hierarchical list
   of the available attributes. Attributes whose value cannot be set are
   dim. Help text is shown for each attribute. Select an attribute by
   double-clicking on it or by selecting it and then pressing **Enter**.
-  Read-only attributes appear dim in the list box. If you select a
   read-only attribute, an error message appears. A ring control at the
   top of the dialog box allows you to see all IVI attributes or only
   the attributes of type ViReal64. If you choose to see all IVI
   attributes, the data types appear to the right of the attribute names
   in the list box. Attributes with data types other than ViReal64 are
   dim. If you select an attribute data type that is dim, LabWindows/CVI
   transfers you to the function panel for the corresponding function
   that is consistent with the data type.
-  If you want to enter a variable name, press **Ctrl**\ +\ **T** to
   change this ring control to a manual input box. If the attribute in
   this ring control has named constants as valid values, you can view
   the constants by moving to the value control and pressing **Enter**.
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the value to which you want to set the attribute. If the
attribute currently showing in the attribute ring control has constants
as valid values, you can view a list of the constants by pressing
**Enter** on this control. Select a value by double-clicking on it or by
selecting it and then pressing **Enter**.
''',
'note': '''
Some of the values might not be valid depending upon the current
settings of the device session.
''',
},
            },
        ],
'documentation': {
'description': '''
| Sets the value of a ViReal64 attribute.
| This is a low-level function that you can use to set the values of
  device-specific attributes and inherent IVI attributes.
''',
},
    },
    'SetAttributeViSession': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel(s) to which this configuration value
applies. Specify multiple channels by using a channel list or a channel
range. A channel list is a comma (,) separated sequence of channel names
(for example, 0,2 specifies channels 0 and 2). A channel range is a
lower bound channel followed by a hyphen (-) or colon (:) followed by an
upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
In the Running state, multiple output channel configurations are
performed sequentially based on the order specified in this parameter.
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': '''
Specifies the ID of an attribute. From the function panel window, you
can use this control as follows.

-  In the function panel window, click on the control or press **Enter**
   or the spacebar to display a dialog box containing hierarchical list
   of the available attributes. Attributes whose value cannot be set are
   dim. Help text is shown for each attribute. Select an attribute by
   double-clicking on it or by selecting it and then pressing **Enter**.
-  Read-only attributes appear dim in the list box. If you select a
   read-only attribute, an error message appears. A ring control at the
   top of the dialog box allows you to see all IVI attributes or only
   the attributes of type ViSession. If you choose to see all IVI
   attributes, the data types appear to the right of the attribute names
   in the list box. Attributes with data types other than ViSession are
   dim. If you select an attribute data type that is dim, LabWindows/CVI
   transfers you to the function panel for the corresponding function
   that is consistent with the data type.
-  If you want to enter a variable name, press **Ctrl**\ +\ **T** to
   change this ring control to a manual input box. If the attribute in
   this ring control has named constants as valid values, you can view
   the constants by moving to the value control and pressing **Enter**.
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViSession',
'documentation': {
'description': '''
Specifies the value to which you want to set the attribute. If the
attribute currently showing in the attribute ring control has constants
as valid values, you can view a list of the constants by pressing
**Enter** on this control. Select a value by double-clicking on it or by
selecting it and then pressing **Enter**.
''',
'note': '''
Some of the values might not be valid depending upon the current
settings of the device session.
''',
},
            },
        ],
'documentation': {
'description': '''
| Sets the value of a ViSession attribute.
| This is a low-level function that you can use to set the values of
  device-specific attributes and inherent IVI attributes.
''',
},
    },
    'SetAttributeViString': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel(s) to which this configuration value
applies. Specify multiple channels by using a channel list or a channel
range. A channel list is a comma (,) separated sequence of channel names
(for example, 0,2 specifies channels 0 and 2). A channel range is a
lower bound channel followed by a hyphen (-) or colon (:) followed by an
upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
In the Running state, multiple output channel configurations are
performed sequentially based on the order specified in this parameter.
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': '''
Specifies the ID of an attribute. From the function panel window, you
can use this control as follows.

-  In the function panel window, click on the control or press **Enter**
   or the spacebar to display a dialog box containing hierarchical list
   of the available attributes. Attributes whose value cannot be set are
   dim. Help text is shown for each attribute. Select an attribute by
   double-clicking on it or by selecting it and then pressing **Enter**.
-  Read-only attributes appear dim in the list box. If you select a
   read-only attribute, an error message appears. A ring control at the
   top of the dialog box allows you to see all IVI attributes or only
   the attributes of type ViString. If you choose to see all IVI
   attributes, the data types appear to the right of the attribute names
   in the list box. Attributes with data types other than ViString are
   dim. If you select an attribute data type that is dim, LabWindows/CVI
   transfers you to the function panel for the corresponding function
   that is consistent with the data type.
-  If you want to enter a variable name, press **Ctrl**\ +\ **T** to
   change this ring control to a manual input box. If the attribute in
   this ring control has named constants as valid values, you can view
   the constants by moving to the value control and pressing **Enter**.
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the value to which you want to set the attribute. If the
attribute currently showing in the attribute ring control has constants
as valid values, you can view a list of the constants by pressing
**Enter** on this control. Select a value by double-clicking on it or by
selecting it and then pressing **Enter**.
''',
'note': '''
Some of the values might not be valid depending upon the current
settings of the device session.
''',
},
            },
        ],
'documentation': {
'description': '''
| Sets the value of a ViString attribute.
| This is a low-level function that you can use to set the values of
  device-specific attributes and inherent IVI attributes.
''',
},
    },
    'SetCalUserDefinedInfo': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitExtCal or niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Info',
                'type': 'ViChar[]',
'documentation': {
'description': 'Specifies the string to store in the device onboard EEPROM.',
},
            },
        ],
'documentation': {
'description': '''
Stores a user-defined string of characters in the device onboard EEPROM.
If the string is longer than the maximum allowable size, it is
truncated. This function overwrites any existing user-defined
information.

If you call this function in a session, **info** is immediately changed.
If you call this function in an external calibration session, **info**
is changed only after you close the session using the
niDCPower_CloseExtCal function with **action** set to
NIDCPOWER_VAL_COMMIT.
''',
},
    },
    'SetSequence': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output channel to which this configuration value applies.
You can only set a sequence for one channel at a time.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Values',
                'type': 'ViReal64[]',
'documentation': {
'description': '''
Specifies the series of voltage levels or current levels, depending on
the configured `output
function <REPLACE_DRIVER_SPECIFIC_URL_1(programming_output)>`__.
**Valid values**:
The valid values for this parameter are defined by the voltage level
range or current level range.
''',
},
            },
            {
                'direction': 'in',
                'name': 'sourceDelays',
                'type': 'ViReal64[]',
'documentation': {
'description': '''
Specifies the source delay that follows the configuration of each value
in the sequence.
**Valid Values**:
The valid values are between 0 and 167 seconds.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Size',
                'type': 'ViUInt32',
'documentation': {
'description': '''
The number of elements in the Values and the Source Delays arrays. The
Values and Source Delays arrays should have the same size.
''',
},
            },
        ],
'documentation': {
'description': '''
Configures a series of voltage or current outputs and corresponding
source delays. The source mode must be set to
`Sequence <REPLACE_DRIVER_SPECIFIC_URL_1(sequencing)>`__ for this
function to take effect.

Refer to the `Configuring the Source
Unit <REPLACE_DRIVER_SPECIFIC_URL_1(configuringthesourceunit)>`__ topic
in the *NI DC Power Supplies and SMUs Help* for more information about
how to configure your device.

Use this function in the Uncommitted or Committed programming states.
Refer to the `Programming
States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic in
the *NI DC Power Supplies and SMUs Help* for more information about
NI-DCPower programming states.
''',
'note': '''
This function is not supported on all devices. Refer to `Supported
Functions by
Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
for more information about supported devices.
''',
},
    },
    'UnlockSession': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'out',
                'name': 'callerHasLock',
                'type': 'ViBoolean',
'documentation': {
'description': '''
| This attribute is optional. If you do not want to use this attribute,
  pass VI_NULL.
| Use this attribute in complex functions to keep track of whether you
  obtain a lock and therefore need to unlock the session.
| Pass the address of a local ViBoolean variable. In the declaration of
  the local variable, initialize it to VI_FALSE. Pass the address of
  the same local variable to any other calls you make to
  niDCPower_LockSession or niDCPower_UnlockSessionin the same
  function.
| The parameter is an input/output parameter. niDCPower_LockSession and
  niDCPower_UnlockSessioneach inspect the current value and take the
  following actions.

-  If the value is VI_TRUE, niDCPower_LockSession does not lock the
   session again.
-  If the value is VI_FALSE, niDCPower_LockSession obtains the lock
   and sets the value of the parameter to VI_TRUE.
-  If the value is VI_FALSE, niDCPower_UnlockSessiondoes not attempt
   to unlock the session.
-  If the value is VI_TRUE, niDCPower_UnlockSessionreleases the lock
   and sets the value of the parameter to VI_FALSE.

| Thus, you can, call niDCPower_UnlockSession at the end of your
  function without worrying about whether you actually have the lock, as
  the following example shows.
| ViStatus TestFunc (ViSession vi, ViInt32 flags)
  {
  ViStatus error = VI_SUCCESS;
  ViBoolean haveLock = VI_FALSE;
  if (flags & BIT_1)
  {
  viCheckErr( niDCPower_LockSession(vi, &haveLock;));
  viCheckErr( TakeAction1(vi));
  if (flags & BIT_2)
  {
  viCheckErr( niDCPower_UnlockSession(vi, &haveLock;));
  viCheckErr( TakeAction2(vi));
  viCheckErr( niDCPower_LockSession(vi, &haveLock;);
  }
  if (flags & BIT_3)
  viCheckErr( TakeAction3(vi));
  }
  Error:
  /\*At this point, you cannot really be sure that you have the lock.
  Fortunately, the haveLock variable takes care of that for you.\*/
  niDCPower_UnlockSession(vi, &haveLock;);
  return error;
  }
''',
},
            },
        ],
'documentation': {
'description': '''
Releases a lock that you acquired on an device session using
niDCPower_LockSession. Refer to niDCPower_LockSession for additional
information on session locks.
''',
},
    },
    'WaitForEvent': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'eventId',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies which event to wait for.
**Defined Values:**
''',
'table_body': [['NIDCPOWER_VAL_SOURCE_COMPLETE_EVENT (1030)', 'Waits for the Source Complete event.'], ['NIDCPOWER_VAL_MEASURE_COMPLETE_EVENT (1031)', 'Waits for the Measure Complete event.'], ['NIDCPOWER_VAL_SEQUENCE_ITERATION_COMPLETE_EVENT (1032)', 'Waits for the Sequence Iteration Complete event.'], ['NIDCPOWER_VAL_SEQUENCE_ENGINE_DONE_EVENT (1033)', 'Waits for the Sequence Engine Done event.'], ['NIDCPOWER_VAL_PULSE_COMPLETE_EVENT (1051 )', 'Waits for the Pulse Complete event.'], ['NIDCPOWER_VAL_READY_FOR_PULSE_TRIGGER_EVENT (1052)', 'Waits for the Ready for Pulse Trigger event.']],
},
            },
            {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the maximum time allowed for this function to complete, in
seconds. If the function does not complete within this time interval,
NI-DCPower returns an error.
''',
'note': '''
When setting the timeout interval, ensure you take into account any
triggers so that the timeout interval is long enough for your
application.
''',
},
            },
        ],
'documentation': {
'description': '''
Waits until the device has generated the specified event.

The session monitors whether each type of event has occurred at least
once since the last time this function or the niDCPower_Initiate
function were called. If an event has only been generated once and you
call this function successively, the function times out. Individual
events must be generated between separate calls of this function.
''',
'note': '''
Refer to `Supported Functions by
Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
for more information about supported devices.
''',
},
    },
    'close': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
        ],
'documentation': {
'description': '''
Closes the session specified in **vi** and deallocates the resources
that NI-DCPower reserves. If power output is enabled when you call this
function, the output channels remain in their existing state and
continue providing power. Use the niDCPower_ConfigureOutputEnabled
function to disable power output on a per channel basis. Use the
niDCPower_reset function to disable power output on all channel(s).

**Related Topics:**

`Programming
States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__
''',
},
    },
    'error_message': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'errorCode',
                'type': 'ViStatus',
'documentation': {
'description': '''
Specifies the **status** parameter that is returned from any of the
NI-DCPower functions.
''',
},
            },
            {
                'direction': 'out',
                'name': 'errorMessage',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Returns the user-readable message string that corresponds to the status
code you specify.
You must pass a ViChar array with at least 256 bytes.
''',
},
            },
        ],
'documentation': {
'description': '''
Converts a status code returned by an instrument driver function into a
user-readable string.
''',
},
    },
    'init': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'resourceName',
                'type': 'ViRsrc',
'documentation': {
'description': '''
Specifies the **resourceName** assigned by Measurement & Automation
Explorer (MAX), for example "PXI1Slot3" where "PXI1Slot3" is an
instrument's **resourceName**. **resourceName** can also be a logical
IVI name.
''',
},
            },
            {
                'direction': 'in',
                'name': 'idQuery',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether the device is queried to determine if the device is a
valid instrument for NI-DCPower.
**Defined Values**:
''',
'table_body': [['VI_TRUE (1)', 'Perform ID query.'], ['VI_FALSE (0)', 'Do not perform ID query.']],
},
            },
            {
                'direction': 'in',
                'name': 'resetDevice',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether to reset the device during the initialization
procedure.
**Defined Values**:
''',
'table_body': [['VI_TRUE (1)', 'Reset the device.'], ['VI_FALSE (0)', 'Do not reset the device.']],
},
            },
            {
                'direction': 'out',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Returns a session handle that you use to identify the session in all
subsequent NI-DCPower function calls.
''',
},
            },
        ],
'documentation': {
'description': '''
This function is deprecated. Use niDCPower_InitializeWithChannels
instead.

Creates a new IVI instrument driver session to the device specified in
**resourceName** and returns a session handle you use to identify the
device in all subsequent NI-DCPower function calls. This function also
sends initialization commands to set the device to the state necessary
for the operation of NI-DCPower.

To place the device in a known start-up state when creating a new
session, set **resetDevice** to VI_TRUE. This action is equivalent to
using the niDCPower_reset function.

To open a session and leave the device in its existing configuration
without passing through a transitional output state, set **resetDevice**
to VI_FALSE, and immediately call the niDCPower_Abort function. Then
configure the device as in the previous session, changing only the
desired settings, and then call the niDCPower_Initiate function. Refer
to the `deprecated programming state
model <REPLACE_DRIVER_SPECIFIC_URL_1(initializedeprecatedmodel)>`__ for
information about the specific software states.
''',
},
    },
    'reset': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
        ],
'documentation': {
'description': '''
Resets the device to a known state. This function disables power
generation, resets session attributes to their default values, commits
the session attributes, and leaves the session in the Uncommitted state.
Refer to the `Programming
States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic for
more information about NI-DCPower software states.
''',
},
    },
    'revision_query': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'out',
                'name': 'instrumentDriverRevision',
                'type': 'ViChar[]',
'documentation': {
'description': 'Returns the driver revision information for NI-DCPower.',
},
            },
            {
                'direction': 'out',
                'name': 'firmwareRevision',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Returns firmware revision information for the device you are using. The
size of this array must be at least 256 bytes.
''',
},
            },
        ],
'documentation': {
'description': 'Returns the revision information of NI-DCPower and the device firmware.',
},
    },
    'self_test': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies a particular instrument session. **vi** is obtained from the
niDCPower_InitializeWithChannels function.
''',
},
            },
            {
                'direction': 'out',
                'name': 'selfTestResult',
                'type': 'ViInt16',
'documentation': {
'description': 'Returns the value result from the device self-test.',
'table_body': [['0', 'Self test passed.'], ['1', 'Self test failed.']],
'table_header': ['Self-Test Code', 'Description'],
},
            },
            {
                'direction': 'out',
                'name': 'selfTestMessage',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Returns the self-test result message. The size of this array must be at
least 256 bytes.
''',
},
            },
        ],
'documentation': {
'description': '''
Performs the device self-test routine and returns the test result(s).
Calling this function implicitly calls the niDCPower_reset function.

When calling niDCPower_self_test with the PXIe-4162/4163, specify all
channels of your PXIe-4162/4163 with the channels input of
niDCPower_InitializeWithChannels. You cannot self test a subset of
PXIe-4162/4163 channels.
''',
},
    },
}
