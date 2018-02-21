
# -*- coding: utf-8 -*-
# This file is code generated, do not make changes here
#  If the generated information is not correct for python
#  changes can be made in functions_addon.py and they will be
#  applied at build time


functions = {
    'AbortGeneration': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
        ],
'documentation': {
'description': '''
Aborts any previously initiated signal generation. Call the
nifgen_InitiateGeneration function to cause the signal generator to
produce a signal again.
''',
},
    },
    'AdjustSampleClockRelativeDelay': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'adjustmentTime',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the amount of time to adjust the Sample Clock delay.

**Units**: Seconds

**Default Value**: 0
''',
},
            },
        ],
'documentation': {
'description': '''
Delays (or phase shifts) the Sample Clock, which delays the generated
signal. Delaying the Sample Clock can be useful when synchronizing the
output of multiple modules or when intentionally phase shifting the
output relative to a fixed reference, such as the PLL Reference Clock.

Adjustment time can be positive or negative, but it must be less than or
equal to the Sample Clock period. The delay takes effect immediately
after this function is called. To delay an external Sample Clock, use
the NIFGEN_ATTR_SAMPLE_CLOCK_ABSOLUTE_DELAY attribute.
''',
},
    },
    'AllocateNamedWaveform': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the channel name for which you want to allocate the named
waveform.

**Default Value**: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'waveformName',
                'type': 'ViConstString',
'documentation': {
'description': 'Specifies the name to associate with the allocated waveform.',
},
            },
            {
                'direction': 'in',
                'name': 'waveformSize',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the size of the waveform to allocate in samples.

**Default Value**: "4096"
''',
},
            },
        ],
'documentation': {
'description': '''
Specifies the size of a named waveform up front so that it can be
allocated in onboard memory before loading the associated data. Data can
then be loaded in smaller blocks with the niFgen Write (Binary16)
Waveform functions.
''',
},
    },
    'AllocateWaveform': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the channel name for which you want to allocate the waveform.

**Default Value**: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'waveformSize',
                'type': 'ViInt32',
'documentation': {
'description': 'Specifies, in samples, the size of the waveform to allocate.',
},
            },
            {
                'direction': 'out',
                'name': 'waveformHandle',
                'type': 'ViInt32',
'documentation': {
'description': '''
The handle that identifies the new waveform. This handle is used later
when referring to this waveform.
''',
},
            },
        ],
'documentation': {
'description': '''
Specifies the size of a waveform so that it can be allocated in onboard
memory before loading the associated data. Data can then be loaded in
smaller blocks with the Write Binary 16 Waveform functions.
''',
'note': '''
The signal generator must not be in the Generating state when you call
this function.
''',
},
    },
    'CalAdjustADC': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the name of the channel being calibrated.

**Default Value**: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'Configuration',
                'type': 'ViInt32',
'documentation': {
'description': 'Specifies the main path configuration.',
},
            },
            {
                'direction': 'in',
                'name': 'voltagesMeasuredExternally',
                'type': 'ViReal64[]',
'documentation': {
'description': '''
Specifies an array of analog output voltages measured with an external
instrument.
''',
},
            },
            {
                'direction': 'in',
                'name': 'voltagesMeasuredWithCaladc',
                'type': 'ViReal64[]',
'documentation': {
'description': '''
Specifies an array of analog output voltages measured with the onboard
calibration ADC.
''',
},
            },
        ],
'documentation': {
'description': '''
Calculates calibration constants pertaining to the gain and offset of
the onboard calibration ADC. During external calibration, you can
generate voltages and measure them both externally and with the
calibration ADC. Pass the measured voltages to this function to allow
NI-FGEN to calculate the appropriate calibration constants and store
them in the onboard EEPROM when the calibration session is committed.
''',
},
    },
    'CalAdjustCalADC': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
nifgen_InitExtCal function and identifies a particular instrument
session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'voltagesMeasuredExternally',
                'type': 'ViReal64[]',
'documentation': {
'description': '''
Specifies an array of analog output voltages measured with an external
instrument.
''',
},
            },
            {
                'direction': 'in',
                'name': 'voltagesMeasuredWithCaladc',
                'type': 'ViReal64[]',
'documentation': {
'description': '''
Specifies an array of analog output voltages measured with the onboard
calibration ADC.
''',
},
            },
        ],
'documentation': {
'description': '''
Calculates calibration constants pertaining to the gain and offset of
the onboard calibration ADC. During external calibration, you can
generate voltages and measure them both externally and with the
calibration ADC. Pass the measured voltages to this function to allow
NI-FGEN to calculate the appropriate calibration constants and store
them in the onboard EEPROM when the calibration session is committed.
''',
},
    },
    'CalAdjustDirectPathGain': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
nifgen_InitExtCal function and identifies a particular instrument
session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the name of the channel being calibrated.

**Default Value**: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'mainDacValues',
                'type': 'ViInt32[]',
'documentation': {
'description': '''
Specifies an array of the values programmed to the main output DAC
during this calibration stage.
''',
},
            },
            {
                'direction': 'in',
                'name': 'gainDacValues',
                'type': 'ViInt32[]',
'documentation': {
'description': '''
Specifies an array of the values programmed to the gain calibration DAC
during this calibration stage.
''',
},
            },
            {
                'direction': 'in',
                'name': 'measuredOutputs',
                'type': 'ViReal64[]',
'documentation': {
'description': '''
Specifies an array of the analog output voltages measured during this
calibration stage.
''',
},
            },
        ],
'documentation': {
'description': '''
Calculates calibration constants pertaining to the gain of the direct
analog path. During external calibration, you can put the device in
different configurations; program different gain and main DAC values;
and take measurements of the resulting output voltage. Pass the
configuration data, as well as the measurements, to this function to
allow NI-FGEN to calculate the appropriate calibration constants and
store them in the onboard EEPROM when the calibration session is
committed.
''',
},
    },
    'CalAdjustDirectPathOutputImpedance': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
nifgen_InitExtCal function and identifies a particular instrument
session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the name of the channel being calibrated.

**Default Value**: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'Configuration',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the direct path output impedance configuration. Refer to the
nifgen_Related_Documentation for your device for information on what
configurations must be calibrated.
''',
},
            },
            {
                'direction': 'in',
                'name': 'loadImpedance',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the impedance of the load across which the measurement passed
in as **measuredVoltageAcrossLoad** is taken.
''',
},
            },
            {
                'direction': 'in',
                'name': 'measuredSourceVoltage',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the analog output voltage measured across a very
high-impedance load.
''',
},
            },
            {
                'direction': 'in',
                'name': 'measuredVoltageAcrossLoad',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the analog output voltage measured across the load impedance
specified in the **loadImpedance** parameter.
''',
},
            },
        ],
'documentation': {
'description': '''
Calculates calibration constants pertaining to direct analog path output
impedance. During external calibration, you can put the device in
different configurations and take measurements of the resulting output
voltage across different loads. Pass the configuration data, as well as
the measurements, to this function to allow NI-FGEN to calculate the
appropriate calibration constants and store them in the onboard EEPROM
when the calibration session is committed.
''',
},
    },
    'CalAdjustFlatness': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
nifgen_InitExtCal function and identifies a particular instrument
session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the name of the channel being calibrated.

**Default Value**: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'Configuration',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the analog path configuration of the device for this stage of
calibration. Refer to the nifgen_Related_Documentation for your device
for information on which configurations must be calibrated.
''',
},
            },
            {
                'direction': 'in',
                'name': 'requestedAmplitude',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the amplitude, in volts, that was used to configure NI-FGEN to
generate the sine tones at different frequencies.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Frequencies',
                'type': 'ViReal64[]',
'documentation': {
'description': 'Specifies the frequencies of the output waveform in hertz.',
},
            },
            {
                'direction': 'in',
                'name': 'measuredAmplitudes',
                'type': 'ViReal64[]',
'documentation': {
'description': '''
Specifies the actual (measured) amplitudes of the output waveform in
volts.
''',
},
            },
            {
                'direction': 'in',
                'name': 'numberOfMeasurements',
                'type': 'ViInt32',
'documentation': {
'description': 'Specifies the number of measurements to take.',
},
            },
        ],
'documentation': {
'description': '''
During external calibration, the device is configured with the different
analog settings. Measurements are taken of the resulting output voltage
across different frequencies. The configuration data, as well as the
measurements, are passed to this function so that NI-FGEN can calculate
the appropriate calibration constants and, when the calibration session
is committed, store them in the onboard EEPROM.
''',
},
    },
    'CalAdjustMainPathOutputImpedance': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
nifgen_InitExtCal function and identifies a particular instrument
session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the name of the channel being calibrated.

**Default Value**: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'Configuration',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the main path output impedance configuration. Refer to the
nifgen_Related_Documentation for your device for information on what
configurations must be calibrated.
''',
},
            },
            {
                'direction': 'in',
                'name': 'loadImpedance',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the impedance of the load across which the measurement passed
in as **measuredVoltageAcrossLoad** is taken.
''',
},
            },
            {
                'direction': 'in',
                'name': 'measuredSourceVoltage',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the analog output voltage measured across a very
high-impedance load.
''',
},
            },
            {
                'direction': 'in',
                'name': 'measuredVoltageAcrossLoad',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the analog output voltage measured across the load impedance
specified in the **loadImpedance** parameter.
''',
},
            },
        ],
'documentation': {
'description': '''
Calculates calibration constants pertaining to main analog path output
impedance. During external calibration, you can put the device in
different configurations and take measurements of the resulting output
voltage across different loads. Pass the configuration data, as well as
the measurements, to this function to allow NI-FGEN to calculate the
appropriate calibration constants and store them in the onboard EEPROM
when the calibration session is committed.
''',
},
    },
    'CalAdjustMainPathPostAmpGainAndOffset': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
nifgen_InitExtCal function and identifies a particular instrument
session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the name of the channel being calibrated.

**Default Value**: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'Configuration',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the postamplifier stage configuration. Refer to the
nifgen_Related_Documentation for your device for information on what
configurations must be calibrated.
''',
},
            },
            {
                'direction': 'in',
                'name': 'mainDacValues',
                'type': 'ViInt32[]',
'documentation': {
'description': '''
Specifies an array of the values programmed to the main output DAC
during this calibration stage.
''',
},
            },
            {
                'direction': 'in',
                'name': 'gainDacValues',
                'type': 'ViInt32[]',
'documentation': {
'description': '''
Specifies an array of the values programmed to the gain calibration DAC
during this calibration stage.
''',
},
            },
            {
                'direction': 'in',
                'name': 'offsetDacValues',
                'type': 'ViInt32[]',
'documentation': {
'description': '''
Specifies an array of the values programmed to the offset calibration
DAC during this calibration stage.
''',
},
            },
            {
                'direction': 'in',
                'name': 'measuredOutputs',
                'type': 'ViReal64[]',
'documentation': {
'description': '''
Specifies an array of the analog output voltages measured during this
calibration stage.
''',
},
            },
        ],
'documentation': {
'description': '''
Calculates calibration constants pertaining to the postamplifier gain
and offset of the main analog path. During external calibration, you can
put the device in different configurations; program different gain,
offset, and main DAC values; and take measurements of the resulting
output voltage. Pass the configuration data, as well as the measurements
to this function to allow NI-FGEN to calculate the appropriate
calibration constants and store them in the onboard EEPROM when the
calibration session is committed.
''',
},
    },
    'CalAdjustMainPathPreAmpGain': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
nifgen_InitExtCal function and identifies a particular instrument
session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the name of the channel being calibrated.

**Default Value**: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'Configuration',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the preamplifier stage configuration. Refer to the
nifgen_Related_Documentation for your device for information on what
configurations must be calibrated.
''',
},
            },
            {
                'direction': 'in',
                'name': 'mainDacValues',
                'type': 'ViInt32[]',
'documentation': {
'description': '''
Specifies an array of the values programmed to the main output DAC
during this calibration stage.
''',
},
            },
            {
                'direction': 'in',
                'name': 'gainDacValues',
                'type': 'ViInt32[]',
'documentation': {
'description': '''
Specifies an array of the values programmed to the gain calibration DAC
during this calibration stage.
''',
},
            },
            {
                'direction': 'in',
                'name': 'offsetDacValues',
                'type': 'ViInt32[]',
'documentation': {
'description': '''
Specifies an array of the values programmed to the offset calibration
DAC during this calibration stage.
''',
},
            },
            {
                'direction': 'in',
                'name': 'measuredOutputs',
                'type': 'ViReal64[]',
'documentation': {
'description': '''
Specifies an array of the analog output voltages measured during this
calibration stage.
''',
},
            },
        ],
'documentation': {
'description': '''
Calculates calibration constants pertaining to the preamplifier gain of
the main analog path. During external calibration, you can put the
device in different configurations; program different gain, offset, and
main DAC values; and take measurements of the resulting output voltage.
Pass the configuration data, as well as the measurements to this
function to allow NI-FGEN to calculate the appropriate calibration
constants and store them in the onboard EEPROM when the calibration
session is committed.
''',
},
    },
    'CalAdjustMainPathPreAmpOffset': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
nifgen_InitExtCal function and identifies a particular instrument
session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the name of the channel being calibrated.

**Default Value**: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'Configuration',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the preamplifier stage configuration. Refer to the
nifgen_Related_Documentation for your device for information about
what configurations must be calibrated.
''',
},
            },
            {
                'direction': 'in',
                'name': 'gainDacValues',
                'type': 'ViInt32[]',
'documentation': {
'description': '''
Specifies an array of the values programmed to the gain calibration DAC
during this calibration stage.
''',
},
            },
            {
                'direction': 'in',
                'name': 'offsetDacValues',
                'type': 'ViInt32[]',
'documentation': {
'description': '''
Specifies an array of the values programmed to the offset calibration
DAC during this calibration stage.
''',
},
            },
            {
                'direction': 'in',
                'name': 'measuredOutputs',
                'type': 'ViReal64[]',
'documentation': {
'description': '''
Specifies an array of the analog output voltages measured during this
calibration stage.
''',
},
            },
        ],
'documentation': {
'description': '''
Calculates calibration constants pertaining to the preamplifier offset
of the main analog path. During external calibration, you can put the
device in different configurations; program different gain, offset, and
main DAC values; and take measurements of the resulting output voltage.
Pass the configuration data, as well as the measurements, to this
function to allow NI-FGEN to calculate the appropriate calibration
constants and store them in the onboard EEPROM when the calibration
session is committed.
''',
},
    },
    'CalAdjustOscillatorFrequency': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
nifgen_InitExtCal function and identifies a particular instrument
session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'desiredFrequency',
                'type': 'ViReal64',
'documentation': {
'description': 'Specifies the expected frequency of the output waveform.',
},
            },
            {
                'direction': 'in',
                'name': 'measuredFrequency',
                'type': 'ViReal64',
'documentation': {
'description': 'Specifies the actual measured frequency of the output waveform.',
},
            },
        ],
'documentation': {
'description': '''
Calculates calibration constants pertaining to the VCXO. During external
calibration, you can generate sine waves and take measurements of the
resulting output frequency. Pass the desired and measured frequencies to
this function to allow NI-FGEN to calculate the appropriate calibration
constants and store them in the onboard EEPROM when the calibration
session is committed.
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
Identifies your instrument session. **vi** is obtained from the
nifgen_init or the nifgen_InitExtCal function and identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'oldPassword',
                'type': 'ViConstString',
'documentation': {
'description': 'Specifies the old (current) external calibration password.',
},
            },
            {
                'direction': 'in',
                'name': 'newPassword',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the new (desired) external calibration password. The password
may be up to four characters long.
''',
},
            },
        ],
'documentation': {
'description': '''
Changes the password that is required to initialize an external
calibration session. The password may be up to four characters long.
''',
},
    },
    'CheckAttributeViBoolean': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the name of the channel on which to check the attribute value
if the attribute is channel-based. If the attribute is not
channel-based, then pass VI_NULL or an empty string ("").

**Default Value**: "" (empty string)
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'Specifies the ID of an attribute.',
},
            },
            {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies the value to which you want to set the attribute. **Default
Value**: None
''',
'note': '''
Some of the values might not be valid depending on the current
settings of the instrument session.
''',
},
            },
        ],
'documentation': {
'description': 'Checks the validity of a value you specify for a ViBoolean attribute.',
},
    },
    'CheckAttributeViInt32': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the name of the channel on which to check the attribute value
if the attribute is channel-based. If the attribute is not
channel-based, then pass VI_NULL or an empty string ("").

**Default Value**: "" (empty string)
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'Specifies the ID of an attribute.',
},
            },
            {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the value to which you want to set the attribute. **Default
Value**: None
''',
'note': '''
Some of the values might not be valid depending on the current
settings of the instrument session.
''',
},
            },
        ],
'documentation': {
'description': 'Checks the validity of a value you specify for a ViInt32 attribute.',
},
    },
    'CheckAttributeViInt64': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the name of the channel on which to check the attribute value
if the attribute is channel-based. If the attribute is not
channel-based, then pass VI_NULL or an empty string ("").

**Default Value**: "" (empty string)
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'Specifies the ID of an attribute.',
},
            },
            {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViInt64',
'documentation': {
'description': '''
Specifies the value to which you want to set the attribute. **Default
Value**: None
''',
'note': '''
Some of the values might not be valid depending on the current
settings of the instrument session.
''',
},
            },
        ],
'documentation': {
'description': 'Checks the validity of a value you specify for a ViInt64 attribute.',
},
    },
    'CheckAttributeViReal64': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the name of the channel on which to check the attribute value
if the attribute is channel-based. If the attribute is not
channel-based, then pass VI_NULL or an empty string ("").

**Default Value**: "" (empty string)
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'Specifies the ID of an attribute.',
},
            },
            {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the value to which you want to set the attribute. **Default
Value**: None
''',
'note': '''
Some of the values might not be valid depending on the current
settings of the instrument session.
''',
},
            },
        ],
'documentation': {
'description': 'Checks the validity of a value you specify for a ViReal64 attribute.',
},
    },
    'CheckAttributeViSession': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the name of the channel on which to check the attribute value
if the attribute is channel-based. If the attribute is not
channel-based, then pass VI_NULL or an empty string ("").

**Default Value**: "" (empty string)
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'Specifies the ID of an attribute.',
},
            },
            {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViSession',
'documentation': {
'description': '''
Specifies the value to which you want to set the attribute. **Default
Value**: None
''',
'note': '''
Some of the values might not be valid depending on the current
settings of the instrument session.
''',
},
            },
        ],
'documentation': {
'description': 'Checks the validity of a value you specify for a ViSession attribute.',
},
    },
    'CheckAttributeViString': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the name of the channel on which to check the attribute value
if the attribute is channel-based. If the attribute is not
channel-based, then pass VI_NULL or an empty string ("").

**Default Value**: "" (empty string)
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'Specifies the ID of an attribute.',
},
            },
            {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the value which you want to verify as a valid value for the
attribute.

**Default Value**: None
''',
'note': '''
Some of the values might not be valid depending on the current
settings of the instrument session.
''',
},
            },
        ],
'documentation': {
'description': 'Checks the validity of a value you specify for a ViString attribute.',
},
    },
    'ClearArbMemory': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
        ],
'documentation': {
'description': '''
Removes all previously created arbitrary waveforms, sequences, and
scripts from the signal generator memory and invalidates all waveform
handles, sequence handles, and waveform names.
''',
'note': '''
The signal generator must not be in the Generating state when you
call this function.
''',
},
    },
    'ClearArbSequence': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'sequenceHandle',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the handle of the arbitrary sequence that you want the signal
generator to remove. You can create an arbitrary sequence using the
nifgen_CreateArbSequence or nifgen_CreateAdvancedArbSequence function.
These functions return a handle that you use to identify the sequence.

| **Defined Value**:
| NIFGEN_VAL_ALL_SEQUENCES—Remove all sequences from the signal
  generator

**Default Value**: None
''',
},
            },
        ],
'documentation': {
'description': '''
Removes a previously created arbitrary sequence from the signal
generator memory and invalidates the sequence handle.
''',
'note': '''
The signal generator must not be in the Generating state when you
call this function.
''',
},
    },
    'ClearArbWaveform': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'waveformHandle',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the handle of the arbitrary waveform that you want the signal
generator to remove.

You can create multiple arbitrary waveforms using one of the following
niFgen Create Waveform functions:

-  niFgen_CreateWaveformF64
-  niFgen_CreateWaveformI16
-  niFgen_CreateWaveformFromFileI16
-  niFgen_CreateWaveformFromFileF64
-  niFgen_CreateWaveformFromFileHWS

**Defined Value**:

NIFGEN_VAL_ALL_WAVEFORMS—Remove all waveforms from the signal
generator.

**Default Value**: None
''',
},
            },
        ],
'documentation': {
'description': '''
Removes a previously created arbitrary waveform from the signal
generator memory and invalidates the waveform handle.
''',
'note': '''
The signal generator must not be in the Generating state when you
call this function.
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
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
        ],
'documentation': {
'description': '''
Clears the error information for the current execution thread and the
IVI session you specify. If you pass VI_NULL for the **vi** parameter,
this function clears the error information only for the current
execution thread.

This function sets the error code to VI_SUCCESS (0), and sets the error
description string to "" (empty string).

The IVI Engine also maintains this error information separately for each
thread. This feature is useful if you do not have a session handle to
pass to the nifgen_ClearError or the nifgen_GetError function. This
situation occurs when a call to the nifgen_init or
nifgen_InitWithOptions function fails.
''',
},
    },
    'ClearFreqList': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'frequencyListHandle',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the handle of the frequency list you want the signal generator
to remove. You create multiple frequency lists using
niFgen_CreateFreqList. niFgen_CreateFreqList returns a handle that you
use to identify each list. Specify a value of -1 to clear all frequency
lists.

**Defined Value**

NIFGEN_VAL_ALL_FLISTS—Remove all frequency lists from the signal
generator.

**Default Value**: None
''',
},
            },
        ],
'documentation': {
'description': '''
Removes a previously created frequency list from the signal generator
memory and invalidates the frequency list handle.
''',
'note': '''
The signal generator must not be in the Generating state when you
call this function.
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
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
        ],
'documentation': {
'description': 'Clears the list of current interchange warnings.',
},
    },
    'ClearUserStandardWaveform': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the channel name from which you want to clear a user standard
waveform.

**Default Value**: "0"
''',
},
            },
        ],
'documentation': {
'description': '''
Clears the user-defined waveform created by the
nifgen_DefineUserStandardWaveform function.
''',
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
Identifies your instrument session. **vi** is obtained from the
nifgen_InitExtCal function and identifies a particular instrument
session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Action',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies he action to perform upon closing.

**Defined Values**

**Default Value**: NIFGEN_VAL_EXT_CAL_ABORT
''',
'table_body': [['NIFGEN_VAL_EXT_CAL_ABORT', 'No changes are made to the calibration constants and data in the EEPROM.'], ['NIFGEN_VAL_EXT_CAL_COMMIT', 'The new calibration constants and data determined during the external calibration session are stored in the onboard EEPROM.']],
},
            },
        ],
'documentation': {
'description': '''
Closes an NI-FGEN external calibration session and, if specified, stores
the new calibration constants and calibration data, such as time and
temperature, in the onboard EEPROM.
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
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
        ],
'documentation': {
'description': '''
Causes a transition to the Committed state. This function verifies
attribute values, reserves the device, and commits the attribute values
to the device. If the attribute values are all valid, NI-FGEN sets the
device hardware configuration to match the session configuration. This
function does not support the NI 5401/5404/5411/5431 signal generators.

In the Committed state, you can load waveforms, scripts, and sequences
into memory. If any attributes are changed, NI-FGEN implicitly
transitions back to the Idle state, where you can program all session
properties before applying them to the device. This function has no
effect if the device is already in the Committed or Generating state and
returns a successful status value.

Calling this VI before the niFgen Initiate Generation VI is optional but
has the following benefits:

-  Routes are committed, so signals are exported or imported.
-  Any Reference Clock and external clock circuits are phase-locked.
-  A subsequent niFgen_InitiateGeneration function can run faster
   because the device is already configured.
''',
},
    },
    'ConfigureAmplitude': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the channel name for which you want to configure a standard
waveform.

**Default Value**: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'Amplitude',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the amplitude of the standard waveform that you want the
signal generator to produce. This value is the amplitude at the output
terminal. NI-FGEN sets the NIFGEN_ATTR_FUNC_AMPLITUDE attribute to
this value.

For example, to produce a waveform ranging from –5.00 V to +5.00 V, set
the amplitude to 10.00 V.

**Units**: peak-to-peak voltage

**Default Value**: None
''',
'note': '''
This parameter does not affect signal generator behavior when you set
the **waveform** parameter of the niFgen_ConfigureStandardWaveform
function to NIFGEN_VAL_WFM_DC.
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the amplitude of the standard waveform that you want the
signal generator to produce.
''',
},
    },
    'ConfigureArbSequence': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the channel name from which you want to configure an arbitrary
sequence.

**Default Value**: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'sequenceHandle',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the handle of the arbitrary sequence that you want the signal
generator to produce. NI-FGEN sets the
NIFGEN_ATTR_ARB_SEQUENCE_HANDLE attribute to this value. You can
create an arbitrary sequence using the niFgen_CreateArbSequence or
niFgen_CreateAdvancedArbSequence function. These functions return a
handle that you use to identify the sequence.

**Default Value**: None
''',
},
            },
            {
                'direction': 'in',
                'name': 'Gain',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the factor by which the signal generator scales the arbitrary
waveforms in the sequence. When you create an arbitrary waveform, you
must first normalize the data points to a range of –1.00 to +1.00. You
can use this parameter to scale the waveform to other ranges. The gain
is applied before the offset is added.

For example, to configure the output signal to range from –2.00 to
+2.00 V, set **gain** to 2.00.

**Units**: unitless

**Default Value**: None
''',
},
            },
            {
                'direction': 'in',
                'name': 'Offset',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the value the signal generator adds to the arbitrary waveform
data. When you create arbitrary waveforms, you must first normalize the
data points to a range of –1.00 to +1.00 V. You can use this parameter
to shift the range of the arbitrary waveform. NI-FGEN sets the
NIFGEN_ATTR_ARB_OFFSET attribute to this value.

For example, to configure the output signal to range from 0.00 to 2.00 V
instead of –1.00 to 1.00 V, set the offset to 1.00.

**Units**: volts

**Default Value**: None
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the signal generator attributes that affect arbitrary
sequence generation. Sets the NIFGEN_ATTR_ARB_SEQUENCE_HANDLE,
NIFGEN_ATTR_ARB_GAIN, and NIFGEN_ATTR_ARB_OFFSET attributes.
''',
'note': '''
The signal generator must not be in the Generating state when you call
this function.
''',
},
    },
    'ConfigureArbWaveform': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the channel name for which you want to configure an arbitrary
waveform.

**Default Value**: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'waveformHandle',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the handle of the arbitrary waveform you want the signal
generator to produce. NI-FGEN sets the
NIFGEN_ATTR_ARB_WAVEFORM_HANDLE attribute to this value. You can
create an arbitrary waveform using one of the following niFgen Create
Waveform functions:

-  niFgen_CreateWaveformF64
-  niFgen_CreateWaveformI16
-  niFgen_CreateWaveformFromFileI16
-  niFgen_CreateWaveformFromFileF64
-  niFgen_CreateWaveformFromFileHWS

These functions return a handle that you use to identify the waveform.

**Default Value**: None
''',
},
            },
            {
                'direction': 'in',
                'name': 'Gain',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the factor by which the signal generator scales the arbitrary
waveforms in the sequence. When you create an arbitrary waveform, you
must first normalize the data points to a range of –1.00 to +1.00. You
can use this parameter to scale the waveform to other ranges. The gain
is applied before the offset is added.

For example, to configure the output signal to range from –2.00 to
+2.00 V, set **gain** to 2.00.

**Units**: unitless

**Default Value**: None
''',
},
            },
            {
                'direction': 'in',
                'name': 'Offset',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the value the signal generator adds to the arbitrary waveform
data. When you create arbitrary waveforms, you must first normalize the
data points to a range of –1.00 to +1.00 V. You can use this parameter
to shift the range of the arbitrary waveform. NI-FGEN sets the
NIFGEN_ATTR_ARB_OFFSET attribute to this value.

For example, to configure the output signal to range from 0.00 to 2.00 V
instead of –1.00 to 1.00 V, set the offset to 1.00.

**Units**: volts

**Default Value**: None
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the attributes of the signal generator that affect arbitrary
waveform generation. Sets the NIFGEN_ATTR_ARB_WAVEFORM_HANDLE,
NIFGEN_ATTR_ARB_GAIN, and NIFGEN_ATTR_ARB_OFFSET attributes.
''',
'note': '''
The signal generator must not be in the Generating state when you call
this function.
''',
},
    },
    'ConfigureChannels': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Channels',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the channel on which all subsequent channel-based attributes
in the session are set. Valid values are non-negative integers. For
example, 0 is the only valid value on devices with one channel, while
devices with two channels support values of 0 and 1. You can specify
more than one channel by inserting commas between values (for example,
0,1).
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the channels to use with the instrument specified in the
**vi** parameter. If you call this function, you must call it
immediately after initializing your session and before configuring
attributes or writing data.
''',
},
    },
    'ConfigureClockMode': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'clockMode',
                'type': 'ViInt32',
'documentation': {
'description': '''
Sets the clock mode of the signal generator.

****Defined Values****

**Default Value**: NIFGEN_VAL_HIGH_RESOLUTION (NI 5450, NI 5451),
NIFGEN_VAL_DIVIDE_DOWN (all other devices)
''',
'table_body': [['NIFGEN_VAL_DIVIDE_DOWN', '**Divide down sampling**—Sample rates are generated by dividing the source frequency.'], ['NIFGEN_VAL_HIGH_RESOLUTION', '**High resolution sampling**—Sample rate is generated by a high-resolution clock source.'], ['NIFGEN_VAL_AUTOMATIC', '**Automatic Selection**—NI-FGEN selects between the divide-down and high-resolution clocking modes.']],
},
            },
        ],
'documentation': {
'description': '''
Selects the clock mode for the signal generator.

Some signal generators allow you to switch the Sample Clock to
High-Resolution or Automatic Sampling mode with this function.

When you select NIFGEN_VAL_DIVIDE_DOWN, NI-FGEN rounds the sample
rate to a frequency that can be achieved by dividing down the board
clock (Sample Clock timebase). However, if you select
NIFGEN_VAL_HIGH_RESOLUTION, you can set the sample rate to any value.
If you select NIFGEN_VAL_AUTOMATIC, NI-FGEN selects the clock mode
based on the sample rate, using divide-down sampling when possible.
''',
'note': '''
The signal generator must not be in the Generating state when you call
this function.
''',
},
    },
    'ConfigureCustomFIRFilterCoefficients': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the channel name for which you want to configure the operation
mode.

**Defined Value**: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'numberOfCoefficients',
                'type': 'ViInt32',
'documentation': {
'description': 'Specifies the number of coefficients. The NI 5441 requires 95.',
},
            },
            {
                'direction': 'in',
                'name': 'coefficientsArray',
                'type': 'ViReal64[]',
'documentation': {
'description': '''
Specifies the array of data the onboard signal processor uses for the
FIR filter coefficients. For the NI 5441, provide a symmetric array of
95 coefficients to this parameter. The array must have at least as many
elements as the value that you specify in the **numberOfCoefficients**
parameter in this function.
The coefficients should range between –1.00 and +1.00.
''',
},
            },
        ],
'documentation': {
'description': '''
Sets the FIR filter coefficients used by the onboard signal processing
block. The values are coerced to the closest settings achievable by the
signal generator.

Refer to the *FIR Filter* topic for your device in the *NI Signal
Generators Help* for more information about FIR filter coefficients.
This function is supported only for the NI 5441.
''',
'note': '''
The signal generator must not be in the Generating state when you call
this function.
''',
},
    },
    'ConfigureDigitalEdgeScriptTrigger': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'triggerId',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the Script Trigger used for triggering.

**Defined Values**

**Default Value**: "ScriptTrigger0"
''',
'table_body': [['"ScriptTrigger0"', 'Script Trigger 0'], ['"ScriptTrigger1"', 'Script Trigger 1'], ['"ScriptTrigger2"', 'Script Trigger 2'], ['"ScriptTrigger3"', 'Script Trigger 3']],
},
            },
            {
                'direction': 'in',
                'name': 'Source',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies which trigger source the signal generator uses.

**Defined Values**

**Default Value**: "PFI0"
''',
'table_body': [['"PFI0"', 'PFI 0'], ['"PFI1"', 'PFI 1'], ['"PFI2"', 'PFI 2'], ['"PFI3"', 'PFI 3'], ['"PFI4"', 'PFI 4'], ['"PFI5"', 'PFI 5'], ['"PFI6"', 'PFI 6'], ['"PFI7"', 'PFI 7'], ['"PXI_Trig0"', 'PXI trigger line 0 or RTSI line 0'], ['"PXI_Trig1"', 'PXI trigger line 1 or RTSI line 1'], ['"PXI_Trig2"', 'PXI trigger line 2 or RTSI line 2'], ['"PXI_Trig3"', 'PXI trigger line 3 or RTSI line 3'], ['"PXI_Trig4"', 'PXI trigger line 4 or RTSI line 4'], ['"PXI_Trig5"', 'PXI trigger line 5 or RTSI line 5'], ['"PXI_Trig6"', 'PXI trigger line 6 or RTSI line 6'], ['"PXI_Trig7"', 'PXI trigger line 7 or RTSI line 7'], ['"PXI_Star"', 'PXI star trigger line']],
},
            },
            {
                'direction': 'in',
                'name': 'Edge',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the edge to detect.

****Defined Values****

****Default Value**:** NIFGEN_VAL_RISING_EDGE
''',
'table_body': [['NIFGEN_VAL_RISING_EDGE', 'Occurs when the signal transitions from low level to high level.'], ['NIFGEN_VAL_FALLING_EDGE', 'Occurs when the signal transitions from high level to low level.']],
},
            },
        ],
'documentation': {
'description': 'Configures the specified Script Trigger for digital edge triggering.',
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
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Source',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies which trigger source the signal generator uses.

**Defined Values**

**Default Value**: "PFI0"
''',
'table_body': [['"PFI0"', 'PFI 0'], ['"PFI1"', 'PFI 1'], ['"PFI2"', 'PFI 2'], ['"PFI3"', 'PFI 3'], ['"PFI4"', 'PFI 4'], ['"PFI5"', 'PFI 5'], ['"PFI6"', 'PFI 6'], ['"PFI7"', 'PFI 7'], ['"PXI_Trig0"', 'PXI trigger line 0 or RTSI line 0'], ['"PXI_Trig1"', 'PXI trigger line 1 or RTSI line 1'], ['"PXI_Trig2"', 'PXI trigger line 2 or RTSI line 2'], ['"PXI_Trig3"', 'PXI trigger line 3 or RTSI line 3'], ['"PXI_Trig4"', 'PXI trigger line 4 or RTSI line 4'], ['"PXI_Trig5"', 'PXI trigger line 5 or RTSI line 5'], ['"PXI_Trig6"', 'PXI trigger line 6 or RTSI line 6'], ['"PXI_Trig7"', 'PXI trigger line 7 or RTSI line 7'], ['"PXI_Star"', 'PXI star trigger line']],
},
            },
            {
                'direction': 'in',
                'name': 'Edge',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the edge to detect.

****Defined Values****

****Default Value**:** NIFGEN_VAL_RISING_EDGE
''',
'table_body': [['NIFGEN_VAL_RISING_EDGE', 'Occurs when the signal transitions from low level to high level.'], ['NIFGEN_VAL_FALLING_EDGE', 'Occurs when the signal transitions from high level to low level.']],
},
            },
        ],
'documentation': {
'description': 'Configures the Start Trigger for digital edge triggering.',
},
    },
    'ConfigureDigitalLevelScriptTrigger': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'triggerId',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the Script Trigger used for triggering.

**Defined Values**

**Default Value**: "ScriptTrigger0"
''',
'table_body': [['"ScriptTrigger0"', 'Script Trigger 0'], ['"ScriptTrigger1"', 'Script Trigger 1'], ['"ScriptTrigger2"', 'Script Trigger 2'], ['"ScriptTrigger3"', 'Script Trigger 3']],
},
            },
            {
                'direction': 'in',
                'name': 'Source',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies which trigger source the signal generator uses.

**Defined Values**

**Default Value**: "PFI0"
''',
'table_body': [['"PFI0"', 'PFI 0'], ['"PFI1"', 'PFI 1'], ['"PFI2"', 'PFI 2'], ['"PFI3"', 'PFI 3'], ['"PFI4"', 'PFI 4'], ['"PFI5"', 'PFI 5'], ['"PFI6"', 'PFI 6'], ['"PFI7"', 'PFI 7'], ['"PXI_Trig0"', 'PXI trigger line 0 or RTSI line 0'], ['"PXI_Trig1"', 'PXI trigger line 1 or RTSI line 1'], ['"PXI_Trig2"', 'PXI trigger line 2 or RTSI line 2'], ['"PXI_Trig3"', 'PXI trigger line 3 or RTSI line 3'], ['"PXI_Trig4"', 'PXI trigger line 4 or RTSI line 4'], ['"PXI_Trig5"', 'PXI trigger line 5 or RTSI line 5'], ['"PXI_Trig6"', 'PXI trigger line 6 or RTSI line 6'], ['"PXI_Trig7"', 'PXI trigger line 7 or RTSI line 7'], ['"PXI_Star"', 'PXI star trigger line']],
},
            },
            {
                'direction': 'in',
                'name': 'triggerWhen',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies whether the Script Trigger asserts on a high or low digital
level.

**Defined Values**

**Default Value**: "HighLevel"
''',
'table_body': [['"HighLevel"', 'Script Trigger asserts on a high digital level.'], ['"LowLevel"', 'Script Trigger asserts on a low digital level.']],
},
            },
        ],
'documentation': {
'description': 'Configures the specified Script Trigger for digital level triggering.',
},
    },
    'ConfigureFreqList': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the channel name for which you want to configure the frequency
list.

**Default Value**: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'frequencyListHandle',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the handle of the frequency list that you want the signal
generator to produce. NI-FGEN sets the NIFGEN_ATTR_FREQ_LIST_HANDLE
attribute to this value. You can create a frequency list using the
niFgen_CreateFreqList function, which returns a handle that you use to
identify the list.
**Default Value**: None
''',
},
            },
            {
                'direction': 'in',
                'name': 'Amplitude',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the amplitude of the standard waveform that you want the
signal generator to produce. This value is the amplitude at the output
terminal. NI-FGEN sets the NIFGEN_ATTR_FUNC_AMPLITUDE attribute to
this value.

For example, to produce a waveform ranging from –5.00 V to +5.00 V, set
the amplitude to 10.00 V.

**Units**: peak-to-peak voltage

**Default Value**: None
''',
'note': '''
This parameter does not affect signal generator behavior when you set
the **waveform** parameter of the niFgen_ConfigureStandardWaveform
function to NIFGEN_VAL_WFM_DC.
''',
},
            },
            {
                'direction': 'in',
                'name': 'dcOffset',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the DC offset of the standard waveform that you want the
signal generator to produce. The value is the offset from ground to the
center of the waveform you specify with the **waveform** parameter,
observed at the output terminal. For example, to configure a waveform
with an amplitude of 10.00 V to range from 0.00 V to +10.00 V, set the
**dcOffset** to 5.00 V. NI-FGEN sets the NIFGEN_ATTR_FUNC_DC_OFFSET
attribute to this value.

**Units**: volts

**Default Value**: None
''',
},
            },
            {
                'direction': 'in',
                'name': 'startPhase',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the horizontal offset of the standard waveform you want the
signal generator to produce. Specify this attribute in degrees of one
waveform cycle. NI-FGEN sets the NIFGEN_ATTR_FUNC_START_PHASE
attribute to this value. A start phase of 180 degrees means output
generation begins halfway through the waveform. A start phase of 360
degrees offsets the output by an entire waveform cycle, which is
identical to a start phase of 0 degrees.

**Units**: degrees of one cycle

**Default Value**: None degrees
''',
'note': '''
This parameter does not affect signal generator behavior when you set
the **waveform** parameter to NIFGEN_VAL_WFM_DC.
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the attributes of the signal generator that affect frequency
list generation (the NIFGEN_ATTR_FREQ_LIST_HANDLE,
NIFGEN_ATTR_FUNC_AMPLITUDE, NIFGEN_ATTR_FUNC_DC_OFFSET, and
NIFGEN_ATTR_FUNC_START_PHASE attributes).
''',
'note': '''
The signal generator must not be in the Generating state when you call
this function.
''',
},
    },
    'ConfigureFrequency': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the channel name for which you want to configure a standard
waveform.

**Default Value**: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'Frequency',
                'type': 'ViReal64',
'documentation': {
'description': '''
| Specifies the frequency of the standard waveform that you want the
  signal generator to produce. NI-FGEN sets the
  NIFGEN_ATTR_FUNC_FREQUENCY attribute to this value.

**Units**: hertz

**Default Value**: None
''',
'note': '''
This parameter does not affect signal generator behavior when you set
the **waveform** parameter of the niFgen_ConfigureStandardWaveform
function to NIFGEN_VAL_WFM_DC.
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the frequency of the standard waveform that you want the
signal generator to produce.
''',
},
    },
    'ConfigureGain': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the channel name for which you want to configure the gain.

**Default Value**: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'Gain',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the factor by which the signal generator scales the arbitrary
waveforms in the sequence. When you create an arbitrary waveform, you
must first normalize the data points to a range of –1.00 to +1.00. You
can use this parameter to scale the waveform to other ranges. The gain
is applied before the offset is added.

For example, to configure the output signal to range from –2.00 to
+2.00 V, set **gain** to 2.00.

**Units**: unitless

**Default Value**: None
''',
},
            },
        ],
'documentation': {
'description': 'Configures the amount of gain to apply to the waveform.',
'note': '''
The signal generator must not be in the Generating state when you call
this function.
''',
},
    },
    'ConfigureOperationMode': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the channel name for which you want to configure the operation
mode.

**Defined Value**: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'operationMode',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the operation mode you want the signal generator to use.
NI-FGEN sets the NIFGEN_ATTR_OPERATION_MODE attribute to this value.
NI-FGEN supports only one value.

**Defined Value**: NIFGEN_VAL_OPERATE_CONTINUOUS
''',
},
            },
        ],
'documentation': {
'description': '''
Determines how the signal generator produces waveforms. NI signal
generators support only Continuous operation mode. To control trigger
mode, use the nifgen_ConfigureTriggerMode function.
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
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the channel name for which you want to enable the output.

**Default Value**: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'Enabled',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether you want to enable or disable the output. NI-FGEN uses
this value to set the NIFGEN_ATTR_OUTPUT_ENABLED attribute.

****Defined Values****

**Default Value**: VI_TRUE
''',
'table_body': [['VI_TRUE', 'Enable the output.'], ['VI_FALSE', 'Disable the output.']],
},
            },
        ],
'documentation': {
'description': '''
Configures the signal generator to generate a signal at the channel
output connector.
''',
},
    },
    'ConfigureOutputImpedance': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the channel name for which you want to set the output
impedance.

**Default Value**: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'Impedance',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the impedance value that you want the signal generator to use.
NI-FGEN sets the NIFGEN_ATTR_OUTPUT_IMPEDANCE attribute to this
value.

**Units**: Ω (ohms)

****Defined Values****:

**Default Value**: NIFGEN_VAL_50_OHMS
''',
'table_body': [['NIFGEN_VAL_50_OHMS', 'Specifies that 50 Ω of impedance is used'], ['NIFGEN_VAL_75_OHMS', 'Specifies that 75 Ω of impedance is used']],
},
            },
        ],
'documentation': {
'description': 'Configures the output impedance for the channel you specify.',
},
    },
    'ConfigureOutputMode': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'outputMode',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the output mode that you want the signal generator to use. The
value you specify determines which functions and attributes you can use
to configure the waveform the signal generator produces.
Refer to the NIFGEN_ATTR_OUTPUT_MODE attribute for more information
about setting this parameter.
****Defined Values****
**Default Value**: NIFGEN_VAL_OUTPUT_FUNC
''',
'table_body': [['NIFGEN_VAL_OUTPUT_FUNC', '**Standard Function mode**—Generates standard function waveforms such as sine, square, triangle, and so on.'], ['NIFGEN_VAL_OUTPUT_FREQ_LIST', '**Frequency List mode**—Generates a standard function using a list of frequencies you define.'], ['NIFGEN_VAL_OUTPUT_ARB', '**Arbitrary waveform mode**—Generates waveforms from user-created/provided waveform arrays of numeric data.'], ['NIFGEN_VAL_OUTPUT_SEQ', '**Arbitrary sequence mode**—Generates downloaded waveforms in an order your specify.'], ['NIFGEN_VAL_OUTPUT_SCRIPT', '**Script mode**—Allows you to use scripting to link and loop multiple waveforms in complex combinations.']],
},
            },
        ],
'documentation': {
'description': '''
Configures the output mode of the signal generator. The output mode
determines how the signal generator produces waveforms. For example, you
can select to generate a standard waveform, an arbitrary waveform, or a
sequence of arbitrary waveforms.
''',
'note': '''
The signal generator must not be in the Generating state when you
call this function.
''',
},
    },
    'ConfigureP2PEndpointFullnessStartTrigger': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'p2pEndpointFullnessLevel',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the quantity of data in the FIFO endpoint that asserts the
trigger. The value –1 specifies that NI-FGEN uses a default value based
on your endpoint configuration.

**Units**: samples per channel
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the Start Trigger for to detect peer-to-peer endpoint
fullness. Generation begins when the number of samples in the
peer-to-peer endpoint reaches the threshold indicated by the
**p2pEndpointFullnessLevel** parameter.
''',
'note': '''
Because there is an additional internal FIFO in the signal generator,
the writer peer must actually write 2,304 bytes more than the quantity
of data specified by this function to satisfy the trigger level.
''',
},
    },
    'ConfigureRefClockFrequency': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'referenceClockFrequency',
                'type': 'ViReal64',
'documentation': {
'description': '''
The reference clock frequency in Hz.

**Default Value**: 10000000
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the signal generator reference clock frequency. The signal
generator uses the reference clock to derive frequencies and sample
rates when generating waveforms.
''',
'note': '''
The signal generator must not be in the Generating state when you
call this function.
''',
},
    },
    'ConfigureRefClockSource': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'referenceClockSource',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the reference clock source that you want the signal generator
to use. NI-FGEN sets the NIFGEN_ATTR_REF_CLOCK_SOURCE attribute to
this value.

The signal generator derives the frequencies and sample rates that it
uses to generate waveforms from the source you specify.

For example, when you set this parameter to
NIFGEN_VAL_REF_CLOCK_EXTERNAL, the signal generator uses the signal
it receives at its external clock terminal as the reference clock.

****Defined Values****

**Default Value**: NIFGEN_VAL_REF_CLOCK_INTERNAL
''',
'table_body': [['NIFGEN_VAL_REF_CLOCK_INTERNAL', 'Internal clock source'], ['NIFGEN_VAL_REF_CLOCK_EXTERNAL', 'External clock source'], ['NIFGEN_VAL_REF_CLOCK_RTSI_CLOCK', 'RTSI clock'], ['NIFGEN_VAL_REF_CLOCK_TTL7', 'TTL 7'], ['NIFGEN_VAL_PXI_CLK10', 'PXI 10 MHz clock'], ['NIFGEN_VAL_REF_IN', 'External clock source'], ['NIFGEN_VAL_RTSI_0', 'RTSI 0'], ['NIFGEN_VAL_RTSI_1', 'RTSI 1'], ['NIFGEN_VAL_RTSI_2', 'RTSI 2'], ['NIFGEN_VAL_RTSI_3', 'RTSI 3'], ['NIFGEN_VAL_RTSI_4', 'RTSI 4'], ['NIFGEN_VAL_RTSI_5', 'RTSI 5'], ['NIFGEN_VAL_RTSI_6', 'RTSI 6'], ['NIFGEN_VAL_RTSI_7', 'RTSI 7'], ['NIFGEN_VAL_CLK_IN', 'CLK IN front panel connector']],
},
            },
        ],
'documentation': {
'description': '''
Configures the signal generator reference clock source. The signal
generator uses the reference clock to derive frequencies and sample
rates when generating waveforms.
''',
},
    },
    'ConfigureReferenceClock': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'referenceClockSource',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the source for the Reference Clock. For example, when you set
this parameter to "ClkIn," the signal generator uses the signal it
receives at its CLK IN front panel connector as the Reference Clock. The
Reference Clock phase-locks with the signal generator Sample Clock
timebase to allow the frequency stability and accuracy of the Sample
Clock timebase to match that of the Reference Clock.
****Defined Values****
**Default Value**: "None"
''',
'note': '''
The following **Defined Values** are examples of possible Reference
Clock sources. For a complete list of the Reference Clock sources
available on your device, refer to the Routes topic for your device or
the **Device Routes** tab in MAX.
''',
'table_body': [['"None"', 'No Reference Clock'], ['"PXI_Clk"', '10 MHz backplane Reference Clock'], ['"ClkIn"', 'CLK IN front panel connector'], ['"OnboardReferenceClock"', 'Onboard Reference Clock'], ['"RTSI7"', 'RTSI line 7'], ['"RefIn"', 'REF IN front panel connector']],
},
            },
            {
                'direction': 'in',
                'name': 'referenceClockFrequency',
                'type': 'ViReal64',
'documentation': {
'description': '''
The Reference Clock frequency in hertz.

**Default Value**: 10000000
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the signal generator Reference Clock source and frequency.
The signal generator uses the Reference Clock to tune the Sample Clock
timebase of the signal generator so that the frequency stability and
accuracy of the Sample Clock timebase matches that of the Reference
Clock.
''',
},
    },
    'ConfigureSampleClockSource': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'sampleClockSource',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the Sample Clock source the signal generator uses.
****Defined Values****
**Default Value**: "OnboardClock"
''',
'note': '''
The following **Defined Values** are examples of possible Sample
Clock sources. For a complete list of the Sample Clock sources available
on your device, refer to the Routes topic for your device or the
**Device Routes** tab in MAX.
''',
'table_body': [['"OnboardClock"', 'Onboard Clock'], ['"ClkIn"', 'CLK IN front panel connector'], ['"PXI_Star"', 'PXI star trigger line'], ['"PXI_Trig0"', 'PXI trigger line 0 or RTSI line 0'], ['"PXI_Trig1"', 'PXI trigger line 1 or RTSI line 1'], ['"PXI_Trig2"', 'PXI trigger line 2 or RTSI line 2'], ['"PXI_Trig3"', 'PXI trigger line 3 or RTSI line 3'], ['"PXI_Trig4"', 'PXI trigger line 4 or RTSI line 4'], ['"PXI_Trig5"', 'PXI trigger line 5 or RTSI line 5'], ['"PXI_Trig6"', 'PXI trigger line 6 or RTSI line 6'], ['"PXI_Trig7"', 'PXI trigger line 7 or RTSI line 7'], ['"DDC_ClkIn"', 'Sample Clock from DDC connector']],
},
            },
        ],
'documentation': {
'description': '''
Sets the source of the Sample Clock (Update Clock) of the signal
generator.
''',
},
    },
    'ConfigureSampleRate': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'sampleRate',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the sample rate at which you want the signal generator to
generate arbitrary waveforms. NI-FGEN sets the
NIFGEN_ATTR_ARB_SAMPLE_RATE attribute to this value.

**Units**: Samples/s

**Default Value**: None
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the NIFGEN_ATTR_ARB_SAMPLE_RATE attribute, which
determines the rate at which the signal generator produces arbitrary
waveforms. When you configure the signal generator to produce an
arbitrary sequence, this value is the sample rate for all arbitrary
waveforms in the sequence.
''',
'note': '''
The signal generator must not be in the Generating state when you call
this function.
''',
},
    },
    'ConfigureSoftwareEdgeScriptTrigger': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'triggerId',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the Script Trigger used for triggering.

**Defined Values**

**Default Value**: "ScriptTrigger0"
''',
'table_body': [['"ScriptTrigger0"', 'Script Trigger 0'], ['"ScriptTrigger1"', 'Script Trigger 1'], ['"ScriptTrigger2"', 'Script Trigger 2'], ['"ScriptTrigger3"', 'Script Trigger 3']],
},
            },
        ],
'documentation': {
'description': 'Configures the specified Script Trigger for software edge triggering.',
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
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
        ],
'documentation': {
'description': 'Configures the Start Trigger for software edge triggering.',
},
    },
    'ConfigureStandardWaveform': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the channel name for which you want to configure a standard
waveform.

**Default Value**: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'Waveform',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the standard waveform that you want the signal generator to
produce. NI-FGEN sets the NIFGEN_ATTR_FUNC_WAVEFORM attribute to this
value.

****Defined Values****

**Default Value**: NIFGEN_VAL_WFM_SINE
''',
'table_body': [['NIFGEN_VAL_WFM_SINE', 'Specifies that the signal generator produces a sinusoid waveform.'], ['NIFGEN_VAL_WFM_SQUARE', 'Specifies that the signal generator produces a square waveform.'], ['NIFGEN_VAL_WFM_TRIANGLE', 'Specifies that the signal generator produces a triangle waveform.'], ['NIFGEN_VAL_WFM_RAMP_UP', 'Specifies that the signal generator produces a positive ramp waveform.'], ['NIFGEN_VAL_WFM_RAMP_DOWN', 'Specifies that the signal generator produces a negative ramp waveform.'], ['NIFGEN_VAL_WFM_DC', 'Specifies that the signal generator produces a constant voltage.'], ['NIFGEN_VAL_WFM_NOISE', 'Specifies that the signal generator produces white noise.'], ['NIFGEN_VAL_WFM_USER', 'Specifies that the signal generator produces a user-defined waveform as defined with the nifgen_DefineUserStandardWaveform function.']],
},
            },
            {
                'direction': 'in',
                'name': 'Amplitude',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the amplitude of the standard waveform that you want the
signal generator to produce. This value is the amplitude at the output
terminal. NI-FGEN sets the NIFGEN_ATTR_FUNC_AMPLITUDE attribute to
this value.

For example, to produce a waveform ranging from –5.00 V to +5.00 V, set
the amplitude to 10.00 V.

**Units**: peak-to-peak voltage

**Default Value**: None
''',
'note': '''
This parameter does not affect signal generator behavior when you set
the **waveform** parameter of the niFgen_ConfigureStandardWaveform
function to NIFGEN_VAL_WFM_DC.
''',
},
            },
            {
                'direction': 'in',
                'name': 'dcOffset',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the DC offset of the standard waveform that you want the
signal generator to produce. The value is the offset from ground to the
center of the waveform you specify with the **waveform** parameter,
observed at the output terminal. For example, to configure a waveform
with an amplitude of 10.00 V to range from 0.00 V to +10.00 V, set the
**dcOffset** to 5.00 V. NI-FGEN sets the NIFGEN_ATTR_FUNC_DC_OFFSET
attribute to this value.

**Units**: volts

**Default Value**: None
''',
},
            },
            {
                'direction': 'in',
                'name': 'Frequency',
                'type': 'ViReal64',
'documentation': {
'description': '''
| Specifies the frequency of the standard waveform that you want the
  signal generator to produce. NI-FGEN sets the
  NIFGEN_ATTR_FUNC_FREQUENCY attribute to this value.

**Units**: hertz

**Default Value**: None
''',
'note': '''
This parameter does not affect signal generator behavior when you set
the **waveform** parameter of the niFgen_ConfigureStandardWaveform
function to NIFGEN_VAL_WFM_DC.
''',
},
            },
            {
                'direction': 'in',
                'name': 'startPhase',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the horizontal offset of the standard waveform that you want
the signal generator to produce. Specify this parameter in degrees of
one waveform cycle. NI-FGEN sets the NIFGEN_ATTR_FUNC_START_PHASE
attribute to this value. A start phase of 180 degrees means output
generation begins halfway through the waveform. A start phase of 360
degrees offsets the output by an entire waveform cycle, which is
identical to a start phase of 0 degrees.

**Units**: degrees of one cycle

**Default Value**: 0.00
''',
'note': '''
This parameter does not affect signal generator behavior when you set
the **waveform** parameter to NIFGEN_VAL_WFM_DC.
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the following attributes of the signal generator that affect
standard waveform generation:

-  NIFGEN_ATTR_FUNC_WAVEFORM
-  NIFGEN_ATTR_FUNC_AMPLITUDE
-  NIFGEN_ATTR_FUNC_DC_OFFSET
-  NIFGEN_ATTR_FUNC_FREQUENCY
-  NIFGEN_ATTR_FUNC_START_PHASE
''',
'note': '''
You must call the niFgen_ConfigureOutputMode function with the
**outputMode** parameter set to NIFGEN_VAL_OUTPUT_FUNC before calling
this function.
''',
},
    },
    'ConfigureSynchronization': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the channel name for which you want to configure the
synchronization signal.

**Default Value**: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'synchronizationSource',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specify the source of the synchronization signal you want to use.

****Defined Values****

**Default Value**: NIFGEN_VAL_NONE
''',
'table_body': [['NIFGEN_VAL_NONE', 'Specifies that no synchronization source is used.'], ['NIFGEN_VAL_RTSI_0', 'Specifies that RTSI 0 or PXI_Trig 0 is used as the synchronization source.'], ['NIFGEN_VAL_RTSI_1', 'Specifies that RTSI 1 or PXI_Trig 1 is used as the synchronization source.'], ['NIFGEN_VAL_RTSI_2', 'Specifies that RTSI 2 or PXI_Trig 2 is used as the synchronization source.'], ['NIFGEN_VAL_RTSI_3', 'Specifies that RTSI 3 or PXI_Trig 3 is used as the synchronization source.'], ['NIFGEN_VAL_RTSI_4', 'Specifies that RTSI 4 or PXI_Trig 4 is used as the synchronization source.'], ['NIFGEN_VAL_RTSI_5', 'Specifies that RTSI 5 or PXI_Trig 5 is used as the synchronization source.'], ['NIFGEN_VAL_RTSI_6', 'Specifies that RTSI 6 or PXI_Trig 6 is used as the synchronization source.'], ['NIFGEN_VAL_TTL0', 'Specifies that TTL 0 is used as the synchronization source.'], ['NIFGEN_VAL_TTL1', 'Specifies that TTL 1 is used as the synchronization source.'], ['NIFGEN_VAL_TTL2', 'Specifies that TTL 2 is used as the synchronization source.'], ['NIFGEN_VAL_TTL3', 'Specifies that TTL 3 is used as the synchronization source.'], ['NIFGEN_VAL_TTL4', 'Specifies that TTL 4 is used as the synchronization source.'], ['NIFGEN_VAL_TTL5', 'Specifies that TTL 5 is used as the synchronization source.'], ['NIFGEN_VAL_TTL6', 'Specifies that TTL 6 is used as the synchronization source.']],
},
            },
        ],
'documentation': {
'description': '''
Sets the signal generator to receive a synchronization signal to
synchronize two or more NI 5401/5411/5431 signal generators. One signal
generator should route a SYNC signal to a RTSI line by calling the
nifgen_ExportSignal function (use the nifgen_RouteSignalOut function
for the NI 5404), and other signal generators should receive the signal
by calling the niFgen_ConfigureSynchronization function.
''',
'note': '''
The signal generator must not be in the Generating state when you call
this function.
Only the NI 5401/5411/5431 signal generators require this function to be
called for proper synchronization.
''',
},
    },
    'ConfigureTriggerMode': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the channel name for which you want to configure the trigger
mode.

**Default Value**: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'triggerMode',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the trigger mode.

****Defined Values****

**Default Value**: NIFGEN_VAL_CONTINUOUS
''',
'table_body': [['NIFGEN_VAL_SINGLE', 'The waveform that you describe in the sequence list generates only once by going through the entire staging list. Only one trigger is required to start the waveform generation. You can use Single trigger mode in any output mode. After a trigger is received, the waveform generation starts from the first stage and continues through to the last stage.'], ['NIFGEN_VAL_CONTINUOUS', 'The waveform that you describe in the staging list generates infinitely by repeatedly cycling through the staging list. After a trigger is received, the waveform generation starts from the first stage and continues through to the last stage. After the last stage is completed, the waveform generation loops back to the start of the first stage and continues until it is stopped. Only one trigger is required to start the waveform generation.'], ['NIFGEN_VAL_STEPPED', 'After a Start Trigger is received, the waveform described by the first stage generates. Then, the device waits for the next trigger signal. On the next trigger, the waveform described by the second stage generates, and so on. After the staging list is exhausted, the waveform generation returns to the first stage and continues to repeat the cycle.'], ['NIFGEN_VAL_BURST', 'After a Start Trigger is received, the waveform described by the first stage generates until another trigger is received. At the next trigger, the buffer of the previous stage completes, then the waveform described by the second stage generates. After the staging list is exhausted, the waveform generation returns to the first stage and continues to repeat the cycle. In Frequency List mode, the duration instruction is ignored, and the trigger switches the frequency to the next frequency in the list.']],
},
            },
        ],
'documentation': {
'description': '''
Sets the trigger mode for your device. Refer to the *Trigger Modes*
topic for your device in the *NI Signal Generators Help* for
descriptions of the specific behavior for supported trigger modes.
''',
'note': '''
The signal generator must not be in the Generating state when you call
this function.
In Frequency List output mode, Stepped trigger mode is the same as Burst
trigger mode.
''',
},
    },
    'ConfigureTriggerSource': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the channel name for which you want to configure the trigger
source.

**Defined Value:**"0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'triggerSource',
                'type': 'ViInt32',
'documentation': {
'description': '''
Controls which trigger source the signal generator uses.

****Defined Values****

**Default Value**: NIFGEN_VAL_IMMEDIATE
''',
'table_body': [['NIFGEN_VAL_IMMEDIATE', 'Immediate'], ['NIFGEN_VAL_EXTERNAL', 'External (maps to PFI 0)'], ['NIFGEN_VAL_SOFTWARE_TRIG', 'Software trigger'], ['NIFGEN_VAL_PXI_STAR', 'PXI star'], ['NIFGEN_VAL_RTSI_0', 'RTSI 0 or PXI_Trig 0'], ['NIFGEN_VAL_RTSI_1', 'RTSI 1 or PXI_Trig 1'], ['NIFGEN_VAL_RTSI_2', 'RTSI 2 or PXI_Trig 2'], ['NIFGEN_VAL_RTSI_3', 'RTSI 3 or PXI_Trig 3'], ['NIFGEN_VAL_RTSI_4', 'RTSI 4 or PXI_Trig 4'], ['NIFGEN_VAL_RTSI_5', 'RTSI 5 or PXI_Trig 5'], ['NIFGEN_VAL_RTSI_6', 'RTSI 6 or PXI_Trig 6'], ['NIFGEN_VAL_RTSI_7', 'RTSI 7 or PXI_Trig 7'], ['NIFGEN_VAL_TTL0', 'TTL 0'], ['NIFGEN_VAL_TTL1', 'TTL 1'], ['NIFGEN_VAL_TTL2', 'TTL 2'], ['NIFGEN_VAL_TTL3', 'TTL 3'], ['NIFGEN_VAL_TTL4', 'TTL 4'], ['NIFGEN_VAL_TTL5', 'TTL 5'], ['NIFGEN_VAL_TTL6', 'TTL 6'], ['NIFGEN_VAL_PFI_0', 'PFI 0'], ['NIFGEN_VAL_PFI_1', 'PFI 1'], ['NIFGEN_VAL_PFI_2', 'PFI 2'], ['NIFGEN_VAL_PFI_3', 'PFI 3']],
},
            },
        ],
'documentation': {
'description': '''
Configures the trigger source. The signal generator responds to a
trigger depending on the operation mode in which the signal generator is
operating.
''',
'note': '''
The signal generator must not be in the Generating state when you
call this function.
''',
},
    },
    'ConfigureUpdateClockSource': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'updateClockSource',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the update clock source.

****Defined Values****

**Default Value**: NIFGEN_VAL_INTERNAL
''',
'table_body': [['NIFGEN_VAL_INTERNAL', 'Internal clock source'], ['NIFGEN_VAL_EXTERNAL', 'External clock source'], ['NIFGEN_VAL_PXI_STAR', 'PXI star'], ['NIFGEN_VAL_RTSI_0', 'RTSI 0 or PXI_Trig 0'], ['NIFGEN_VAL_RTSI_1', 'RTSI 1 or PXI_Trig 1'], ['NIFGEN_VAL_RTSI_2', 'RTSI 2 or PXI_Trig 2'], ['NIFGEN_VAL_RTSI_3', 'RTSI 3 or PXI_Trig 3'], ['NIFGEN_VAL_RTSI_4', 'RTSI 4 or PXI_Trig 4'], ['NIFGEN_VAL_RTSI_5', 'RTSI 5 or PXI_Trig 5'], ['NIFGEN_VAL_RTSI_6', 'RTSI 6 or PXI_Trig 6'], ['NIFGEN_VAL_RTSI_7', 'RTSI 7 or PXI_Trig 7'], ['NIFGEN_VAL_CLK_IN', 'CLK IN front panel connector'], ['NIFGEN_VAL_DDC_CLK_IN', 'Digital Data & Control clock in']],
},
            },
        ],
'documentation': {
'description': '''
Sets the source of the update clock of the signal generator. The source
can be internal or external.
''',
},
    },
    'CreateAdvancedArbSequence': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'sequenceLength',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the number of waveforms in the new arbitrary sequence that you
want to create. The value you pass must be between the minimum and
maximum sequence lengths that the signal generator allows. You can
obtain the minimum and maximum sequence lengths from
**minimumSequenceLength** and **maximumSequenceLength** in the
nifgen_QueryArbSeqCapabilities function.

**Default Value**: None
''',
},
            },
            {
                'direction': 'in',
                'name': 'waveformHandlesArray',
                'type': 'ViInt32[]',
'documentation': {
'description': '''
Specifies the array of waveform handles from which you want to create a
new arbitrary sequence. The array must have at least as many elements as
the value that you specify in **sequenceLength**. Each
**waveformHandlesArray** element has a corresponding **loopCountsArray**
element that indicates how many times that waveform is repeated. You
obtain waveform handles when you create arbitrary waveforms with the
nifgen_AllocateWaveform function or one of the following niFgen
CreateWaveform functions:

-  nifgen_CreateWaveformF64
-  nifgen_CreateWaveformI16
-  nifgen_CreateWaveformFromFileI16
-  nifgen_CreateWaveformFromFileF64
-  nifgen_CreateWaveformFromFileHWS

**Default Value**: None
''',
},
            },
            {
                'direction': 'in',
                'name': 'loopCountsArray',
                'type': 'ViInt32[]',
'documentation': {
'description': '''
Specifies the array of loop counts you want to use to create a new
arbitrary sequence. The array must have at least as many elements as the
value that you specify in the **sequenceLength** parameter. Each
**loopCountsArray** element corresponds to a **waveformHandlesArray**
element and indicates how many times to repeat that waveform. Each
element of the **loopCountsArray** must be less than or equal to the
maximum number of loop counts that the signal generator allows. You can
obtain the maximum loop count from **maximumLoopCount** in the
nifgen_QueryArbSeqCapabilities function.

**Default Value**: None
''',
},
            },
            {
                'direction': 'in',
                'name': 'sampleCountsArray',
                'type': 'ViInt32[]',
'documentation': {
'description': '''
Specifies the array of sample counts that you want to use to create a
new arbitrary sequence. The array must have at least as many elements as
the value you specify in the **sequenceLength** parameter. Each
**sampleCountsArray** element corresponds to a **waveformHandlesArray**
element and indicates the subset, in samples, of the given waveform to
generate. Each element of the **sampleCountsArray** must be larger than
the minimum waveform size, a multiple of the waveform quantum and no
larger than the number of samples in the corresponding waveform. You can
obtain these values by calling the nifgen_QueryArbWfmCapabilities
function.

**Default Value**: None
''',
},
            },
            {
                'direction': 'in',
                'name': 'markerLocationArray',
                'type': 'ViInt32[]',
'documentation': {
'description': '''
Specifies the array of marker locations to where you want a marker to be
generated in the sequence. The array must have at least as many elements
as the value you specify in the **sequenceLength** parameter. Each
**markerLocationArray** element corresponds to a
**waveformHandlesArray** element and indicates where in the waveform a
marker is to generate. The marker location must be less than the size of
the waveform the marker is in. The markers are coerced to the nearest
marker quantum and the coerced values are returned in the
**coercedMarkersArray** parameter.

If you do not want a marker generated for a particular sequence stage,
set this parameter to NIFGEN_VAL_NO_MARKER.

**Defined Value**: NIFGEN_VAL_NO_MARKER

**Default Value**: None
''',
},
            },
            {
                'direction': 'out',
                'name': 'coercedMarkersArray',
                'type': 'ViInt32[]',
'documentation': {
'description': '''
Returns an array of all given markers that are coerced (rounded) to the
nearest marker quantum. Not all devices coerce markers.

**Default Value**: None
''',
},
            },
            {
                'direction': 'out',
                'name': 'sequenceHandle',
                'type': 'ViInt32',
'documentation': {
'description': '''
Returns the handle that identifies the new arbitrary sequence. You can
pass this handle to nifgen_ConfigureArbSequence to generate the
arbitrary sequence.
''',
},
            },
        ],
'documentation': {
'description': '''
Creates an arbitrary sequence from an array of waveform handles and an
array of corresponding loop counts. This function returns a handle that
identifies the sequence. You pass this handle to the
niFgen_ConfigureArbSequence function to specify what arbitrary sequence
you want the signal generator to produce.

The niFgen_CreateAdvancedArbSequence function extends on the
niFgen_CreateArbSequence function by adding the ability to set the
number of samples in each sequence step and to set marker locations.

An arbitrary sequence consists of multiple waveforms. For each waveform,
you specify the number of times the signal generator produces the
waveform before proceeding to the next waveform. The number of times to
repeat a specific waveform is called the loop count.
''',
'note': '''
The signal generator must not be in the Generating state when you call
this function.
You must call the nifgen_ConfigureOutputMode function to set the
**outputMode** parameter to NIFGEN_VAL_OUTPUT_SEQ before calling this
function.
''',
},
    },
    'CreateArbSequence': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'sequenceLength',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the number of waveforms in the new arbitrary sequence that you
want to create. The value you pass must be between the minimum and
maximum sequence lengths that the signal generator allows. You can
obtain the minimum and maximum sequence lengths from
**minimumSequenceLength** and **maximumSequenceLength** in the
nifgen_QueryArbSeqCapabilities function.

**Default Value**: None
''',
},
            },
            {
                'direction': 'in',
                'name': 'waveformHandlesArray',
                'type': 'ViInt32[]',
'documentation': {
'description': '''
Specifies the array of waveform handles from which you want to create a
new arbitrary sequence. The array must have at least as many elements as
the value that you specify in **sequenceLength**. Each
**waveformHandlesArray** element has a corresponding **loopCountsArray**
element that indicates how many times that waveform is repeated. You
obtain waveform handles when you create arbitrary waveforms with the
nifgen_AllocateWaveform function or one of the following niFgen
CreateWaveform functions:

-  nifgen_CreateWaveformF64
-  nifgen_CreateWaveformI16
-  nifgen_CreateWaveformFromFileI16
-  nifgen_CreateWaveformFromFileF64
-  nifgen_CreateWaveformFromFileHWS

**Default Value**: None
''',
},
            },
            {
                'direction': 'in',
                'name': 'loopCountsArray',
                'type': 'ViInt32[]',
'documentation': {
'description': '''
Specifies the array of loop counts you want to use to create a new
arbitrary sequence. The array must have at least as many elements as the
value that you specify in the **sequenceLength** parameter. Each
**loopCountsArray** element corresponds to a **waveformHandlesArray**
element and indicates how many times to repeat that waveform. Each
element of the **loopCountsArray** must be less than or equal to the
maximum number of loop counts that the signal generator allows. You can
obtain the maximum loop count from **maximumLoopCount** in the
nifgen_QueryArbSeqCapabilities function.

**Default Value**: None
''',
},
            },
            {
                'direction': 'out',
                'name': 'sequenceHandle',
                'type': 'ViInt32',
'documentation': {
'description': '''
Returns the handle that identifies the new arbitrary sequence. You can
pass this handle to nifgen_ConfigureArbSequence to generate the
arbitrary sequence.
''',
},
            },
        ],
'documentation': {
'description': '''
Creates an arbitrary sequence from an array of waveform handles and an
array of corresponding loop counts. This function returns a handle that
identifies the sequence. You pass this handle to the
nifgen_ConfigureArbSequence function to specify what arbitrary sequence
you want the signal generator to produce.

An arbitrary sequence consists of multiple waveforms. For each waveform,
you can specify the number of times that the signal generator produces
the waveform before proceeding to the next waveform. The number of times
to repeat a specific waveform is called the loop count.
''',
'note': '''
You must call the nifgen_ConfigureOutputMode function to set the
**outputMode** parameter to NIFGEN_VAL_OUTPUT_SEQ before calling this
function.
''',
},
    },
    'CreateArbWaveform': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'waveformSize',
                'type': 'ViInt32',
'documentation': {
'description': '''
| Specifies the size of the arbitrary waveform that you want created.
| The size must meet the following restrictions:

-  The size must be less than or equal to the maximum waveform size that
   the device allows.
-  The size must be greater than or equal to the minimum waveform size
   that the device allows.
-  The size must be an integer multiple of the device waveform quantum.

| 
| You can obtain these values from the **maximumWaveformSize**,
  **minimumWaveformSize**, and **waveformQuantum** parameters in the
  nifgen_QueryArbWfmCapabilities function.
| ****Default Value**:** None
''',
},
            },
            {
                'direction': 'in',
                'name': 'waveformDataArray',
                'type': 'ViReal64[]',
'documentation': {
'description': '''
Specifies the array of data you want to use for the new arbitrary
waveform. The array must have at least as many elements as the value
that you specify in **waveformSize**.

You must normalize the data points in the array to be between –1.00 and
+1.00.

**Default Value**: None
''',
},
            },
            {
                'direction': 'out',
                'name': 'waveformHandle',
                'type': 'ViInt32',
'documentation': {
'description': '''
The handle that identifies the new waveform. This handle is used later
when referring to this waveform.
''',
},
            },
        ],
'documentation': {
'description': '''
[OBSOLETE] This function is obsolete. Use the nifgen_CreateWaveformF64,
nifgen_CreateWaveformI16, or nifgen_CreateWaveformComplexF64 function
instead of this function.

Creates an arbitrary waveform and returns a handle that identifies that
waveform. You can pass this handle to the nifgen_ConfigureArbWaveform
function to produce that waveform. You can also use the handles this
function returns to specify a sequence of arbitrary waveforms with the
nifgen_CreateArbSequence function.
''',
'note': '''
You must scale the data between –1.00 and +1.00. Use the **arbGain**
parameter to generate different output voltages.
''',
},
    },
    'CreateBinary16ArbWaveform': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'waveformSize',
                'type': 'ViInt32',
'documentation': {
'description': '''
| Specifies the size of the arbitrary waveform that you want created.
| The size must meet the following restrictions:

-  The size must be less than or equal to the maximum waveform size that
   the device allows.
-  The size must be greater than or equal to the minimum waveform size
   that the device allows.
-  The size must be an integer multiple of the device waveform quantum.

| 
| You can obtain these values from the **maximumWaveformSize**,
  **minimumWaveformSize**, and **waveformQuantum** parameters in
  nifgen_QueryArbWfmCapabilities.
| ****Default Value**:** None
''',
},
            },
            {
                'direction': 'in',
                'name': 'waveformDataArray',
                'type': 'ViInt16[]',
'documentation': {
'description': '''
Specifies the array of data you want to use for the new arbitrary
waveform. The array must have at least as many elements as the value
that you specify in **waveformSize**.

You must normalize the data points in the array to be between –32768 and
32767.

**Default Value**: None
''',
},
            },
            {
                'direction': 'out',
                'name': 'waveformHandle',
                'type': 'ViInt32',
'documentation': {
'description': '''
The handle that identifies the new waveform. This handle is used later
when referring to this waveform.
''',
},
            },
        ],
'documentation': {
'description': '''
[OBSOLETE] This function is obsolete. Use the nifgen_CreateWaveformI16
function instead of this function.

Creates an arbitrary waveform from binary data and returns a handle that
identifies that waveform. You can pass this handle to the
nifgen_ConfigureArbWaveform function to produce that waveform. You can
also use the handles this function returns to specify a sequence of
arbitrary waveforms with the nifgen_CreateArbSequence function.
''',
'note': '''
You must set the output mode to NIFGEN_VAL_OUTPUT_ARB or
NIFGEN_VAL_OUTPUT_SEQ before calling this function.
''',
},
    },
    'CreateFreqList': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Waveform',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the standard waveform that you want the signal generator to
produce. NI-FGEN sets the NIFGEN_ATTR_FUNC_WAVEFORM attribute to this
value.

****Defined Values****

**Default Value**: NIFGEN_VAL_WFM_SINE
''',
'table_body': [['NIFGEN_VAL_WFM_SINE', 'Specifies that the signal generator produces a sinusoid waveform.'], ['NIFGEN_VAL_WFM_SQUARE', 'Specifies that the signal generator produces a square waveform.'], ['NIFGEN_VAL_WFM_TRIANGLE', 'Specifies that the signal generator produces a triangle waveform.'], ['NIFGEN_VAL_WFM_RAMP_UP', 'Specifies that the signal generator produces a positive ramp waveform.'], ['NIFGEN_VAL_WFM_RAMP_DOWN', 'Specifies that the signal generator produces a negative ramp waveform.'], ['NIFGEN_VAL_WFM_DC', 'Specifies that the signal generator produces a constant voltage.'], ['NIFGEN_VAL_WFM_NOISE', 'Specifies that the signal generator produces white noise.'], ['NIFGEN_VAL_WFM_USER', 'Specifies that the signal generator produces a user-defined waveform as defined with the nifgen_DefineUserStandardWaveform function.']],
},
            },
            {
                'direction': 'in',
                'name': 'frequencyListLength',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the number of steps in the frequency list you want to create.
The value must be between the minimum and maximum frequency list lengths
that the signal generator allows. You can obtain the minimum and maximum
frequency list lengths from the **minimumFrequencyListLength** and
**maximumFrequencyListLength** parameters in the
nifgen_QueryFreqListCapabilities function.

**frequency** and **duration** must each be at least as long as this
frequency list length.

**Default Value**: None
''',
},
            },
            {
                'direction': 'in',
                'name': 'frequencyArray',
                'type': 'ViReal64[]',
'documentation': {
'description': '''
Specifies the array of frequencies to form the frequency list. The array
must have at least as many elements as the value you specify in
**frequencyListLength**. Each **frequencyArray** element has a
corresponding **durationArray** element that indicates how long that
frequency is repeated.

**Units**: hertz

**Default Value**: None
''',
},
            },
            {
                'direction': 'in',
                'name': 'durationArray',
                'type': 'ViReal64[]',
'documentation': {
'description': '''
Specifies the array of durations to form the frequency list. The array
must have at least as many elements as the value that you specify in
**frequencyListLength**. Each **durationArray** element has a
corresponding **frequencyArray** element and indicates how long in
seconds to generate the corresponding frequency.

**Units**: seconds

**Default Value**: None
''',
},
            },
            {
                'direction': 'out',
                'name': 'frequencyListHandle',
                'type': 'ViInt32',
'documentation': {
'description': '''
Returns the handle that identifies the new frequency list. You can pass
this handle to nifgen_ConfigureFreqList to generate the arbitrary
sequence.
''',
},
            },
        ],
'documentation': {
'description': '''
Creates a frequency list from an array of frequencies
(**frequencyArray**) and an array of durations (**durationArray**). The
two arrays should have the same number of elements, and this value must
also be the size of the **frequencyListLength**. The function returns a
handle that identifies the frequency list (the **frequencyListHandle**).
You can pass this handle to nifgen_ConfigureFreqList to specify what
frequency list you want the signal generator to produce.

A frequency list consists of a list of frequencies and durations. The
signal generator generates each frequency for the given amount of time
and then proceeds to the next frequency. When the end of the list is
reached, the signal generator starts over at the beginning of the list.
''',
'note': '''
The signal generator must not be in the Generating state when you call
this function.
''',
},
    },
    'CreateWaveformComplexF64': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the channel name for which you want to create the waveform.

**Default Value**: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'numberOfSamples',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the size of the arbitrary waveform that you want to create.

The size must meet the following restrictions:

-  The size must be less than or equal to the maximum waveform size that
   the device allows.
-  The size must be greater than or equal to the minimum waveform size
   that the device allows.
-  The size must be an integer multiple of the device waveform quantum.

You can obtain these values from the **maximumWaveformSize**,
**minimumWaveformSize**, and **waveformQuantum** parameters of the
niFgen_QueryArbWfmCapabilities function.

| 
| **Default Value**: None
''',
},
            },
            {
                'direction': 'in',
                'name': 'waveformDataArray',
                'type': 'NIComplexNumber[]',
'documentation': {
'description': '''
Specifies the array of data you want to use for the new arbitrary
waveform. The array must have at least as many elements as the value
that you specify in **waveformSize**.

You must normalize the data points in the array to be between –1.00 and
+1.00.

**Default Value**: None
''',
},
            },
            {
                'direction': 'out',
                'name': 'waveformHandle',
                'type': 'ViInt32',
'documentation': {
'description': '''
The handle that identifies the new waveform. This handle is used later
when referring to this waveform.
''',
},
            },
        ],
'documentation': {
'description': '''
Creates an onboard waveform from complex double-precision floating-point
(F64) data for use with the NIFGEN_ATTR_OUTPUT_MODE attribute set to
Arbitrary Waveform or Arbitrary Sequence output mode on devices with the
NIFGEN_ATTR_OUTPUT_ENABLED attribute set to VI_TRUE and the
NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE attribute set to
NIFGEN_VAL_OSP_COMPLEX. The **waveformHandle** returned by the
function can be used later for setting the active waveform, changing the
data in the waveform, building sequences of waveforms, or deleting the
waveform when it is no longer needed.
''',
'note': '''
You must call the nifgen_ConfigureOutputMode function to set the
**outputMode** parameter to NIFGEN_VAL_OUTPUT_ARB or
NIFGEN_VAL_OUTPUT_SEQ before calling this function.
''',
},
    },
    'CreateWaveformF64': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the channel name for which you want to create the waveform.

**Default Value**: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'waveformSize',
                'type': 'ViInt32',
'documentation': {
'description': '''
| Specifies the size of the arbitrary waveform that you want to create.
| The size must meet the following restrictions:

-  The size must be less than or equal to the maximum waveform size that
   the device allows.
-  The size must be greater than or equal to the minimum waveform size
   that the device allows.
-  The size must be an integer multiple of the device waveform quantum.

You can obtain these values from the **maximumWaveformSize**,
**minimumWaveformSize**, and **waveformQuantum** parameters of the
nifgen_QueryArbWfmCapabilities function.

| ****Default Value**:** None
''',
},
            },
            {
                'direction': 'in',
                'name': 'waveformDataArray',
                'type': 'ViReal64[]',
'documentation': {
'description': '''
Specifies the array of data you want to use for the new arbitrary
waveform. The array must have at least as many elements as the value
that you specify in **waveformSize**.

You must normalize the data points in the array to be between –1.00 and
+1.00.

**Default Value**: None
''',
},
            },
            {
                'direction': 'out',
                'name': 'waveformHandle',
                'type': 'ViInt32',
'documentation': {
'description': '''
The handle that identifies the new waveform. This handle is used later
when referring to this waveform.
''',
},
            },
        ],
'documentation': {
'description': '''
Creates an onboard waveform from binary F64 (floating point double) data
for use in Arbitrary Waveform output mode or Arbitrary Sequence output
mode. The **waveformHandle** returned can later be used for setting the
active waveform, changing the data in the waveform, building sequences
of waveforms, or deleting the waveform when it is no longer needed.
''',
'note': '''
You must call the nifgen_ConfigureOutputMode function to set the
**outputMode** parameter to NIFGEN_VAL_OUTPUT_ARB or
NIFGEN_VAL_OUTPUT_SEQ before calling this function.
''',
},
    },
    'CreateWaveformFromFileF64': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the channel name for which you want to create the waveform.

**Defined Value**: "0"

**Default Value**: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'FileName',
                'type': 'ViConstString',
'documentation': {
'description': 'The full path and name of the file where the waveform data resides.',
},
            },
            {
                'direction': 'in',
                'name': 'byteOrder',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the byte order of the data in the file.

****Defined Values****

| 
| ****Default Value**:** NIFGEN_VAL_LITTLE_ENDIAN
''',
'note': '''
Data written by most applications in Windows (including
LabWindows™/CVI™) is in Little Endian format. Data written to a file
from LabVIEW is in Big Endian format by default on all platforms. Big
Endian and Little Endian refer to the way data is stored in memory,
which can differ on different processors.
''',
'table_body': [['NIFGEN_VAL_LITTLE_ENDIAN', 'Little Endian Data—The least significant bit is stored at the lowest address, followed by the other bits, in order of increasing significance.'], ['NIFGEN_VAL_BIG_ENDIAN', 'Big Endian Data—The most significant bit is stored at the lowest address, followed by the other bits, in order of decreasing significance.']],
},
            },
            {
                'direction': 'out',
                'name': 'waveformHandle',
                'type': 'ViInt32',
'documentation': {
'description': '''
The handle that identifies the new waveform. This handle is used later
when referring to this waveform.
''',
},
            },
        ],
'documentation': {
'description': '''
This function takes the floating point double (F64) data from the
specified file and creates an onboard waveform for use in Arbitrary
Waveform or Arbitrary Sequence output mode. The **waveformHandle**
returned by this function can later be used for setting the active
waveform, changing the data in the waveform, building sequences of
waveforms, or deleting the waveform when it is no longer needed.
''',
'note': '''
The F64 data must be between –1.0 and +1.0 V. Use the
NIFGEN_ATTR_DIGITAL_GAIN attribute to generate different voltage
outputs.
''',
},
    },
    'CreateWaveformFromFileHWS': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the channel name for which you want to create the waveform.

**Defined Value**: "0"

**Default Value**: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'FileName',
                'type': 'ViConstString',
'documentation': {
'description': 'The full path and name of the file where the waveform data resides.',
},
            },
            {
                'direction': 'in',
                'name': 'useRateFromWaveform',
                'type': 'ViBoolean',
'documentation': {
'description': '''
| If you set this parameter input to VI_TRUE and if onboard signal
  processing (OSP) is enabled, the rate from the waveform is interpreted
  as the data rate, and FGEN sets the data rate attribute for you. In
  all other cases, it is interpreted as the sample rate, and FGEN sets
  the sample rate attribute for you.

****Defined Values****

| 
| ****Default Value**:** VI_TRUE
''',
'table_body': [['VI_TRUE', 'Use rate from waveform.'], ['VI_FALSE', 'Do not use rate from waveform.']],
},
            },
            {
                'direction': 'in',
                'name': 'useGainAndOffsetFromWaveform',
                'type': 'ViBoolean',
'documentation': {
'description': '''
| If this input is set to VI_TRUE, NI-FGEN retrieves the gain and
  offset values from the specified HWS file and applies them to the
  NI-FGEN driver.

****Defined Values****

| 
| ****Default Value**:** VI_TRUE
''',
'table_body': [['VI_TRUE', 'Use gain and offset from waveform.'], ['VI_FALSE', 'Do not use gain and offset from waveform.']],
},
            },
            {
                'direction': 'out',
                'name': 'waveformHandle',
                'type': 'ViInt32',
'documentation': {
'description': '''
The handle that identifies the new waveform. This handle is used later
when referring to this waveform.
''',
},
            },
        ],
'documentation': {
'description': '''
| Takes the waveform data from the specified HWS (Hierarchical Waveform
  Storage) file and creates an onboard waveform for use in Arbitrary
  Waveform or Arbitrary Sequence output mode. The **waveformHandle**
  returned by this function can be used later for setting the active
  waveform, changing the data in the waveform, building sequences of
  waveforms, or deleting the waveform when it is no longer needed.
| When the Analog Waveform Editor saves data in an HWS file, it also
  stores the rate, gain, and offset with the data. If the
  **useRateFromWaveform** and **useGain&OffsetFromWaveform;** parameters
  are set to VI_TRUE, this function also sets those properties.

|
''',
'note': '''
If you choose to have this function set the gain and offset properties
for you, you should **not** use the niFgen_ConfigureArbWaveform or
niFgen_ConfigureArbSequence functions, as they also set the gain and
offset, thereby overriding the values set by this function. Instead, use
the NIFGEN_ATTR_ARB_WAVEFORM_HANDLE or
NIFGEN_ATTR_ARB_SEQUENCE_HANDLE attributes.
''',
},
    },
    'CreateWaveformFromFileI16': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the channel name for which you want to create the waveform.

**Default Value**: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'FileName',
                'type': 'ViConstString',
'documentation': {
'description': 'The full path and name of the file where the waveform data resides.',
},
            },
            {
                'direction': 'in',
                'name': 'byteOrder',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the byte order of the data in the file.

****Defined Values****

| 
| ****Default Value**:** NIFGEN_VAL_LITTLE_ENDIAN
''',
'note': '''
Data written by most applications in Windows (including
LabWindows™/CVI™) is in Little Endian format. Data written to a file
from LabVIEW is in Big Endian format by default on all platforms. Big
Endian and Little Endian refer to the way data is stored in memory,
which can differ on different processors.
''',
'table_body': [['NIFGEN_VAL_LITTLE_ENDIAN', 'Little Endian Data—The least significant bit is stored at the lowest address, followed by the other bits, in order of increasing significance.'], ['NIFGEN_VAL_BIG_ENDIAN', 'Big Endian Data—The most significant bit is stored at the lowest address, followed by the other bits, in order of decreasing significance.']],
},
            },
            {
                'direction': 'out',
                'name': 'waveformHandle',
                'type': 'ViInt32',
'documentation': {
'description': '''
The handle that identifies the new waveform. This handle is used later
when referring to this waveform.
''',
},
            },
        ],
'documentation': {
'description': '''
Takes the binary 16-bit signed integer (I16) data from the specified
file and creates an onboard waveform for use in Arbitrary Waveform or
Arbitrary Sequence output mode. The **waveformHandle** returned by this
function can later be used for setting the active waveform, changing the
data in the waveform, building sequences of waveforms, or deleting the
waveform when it is no longer needed.
''',
'note': '''
The I16 data (values between –32768 and +32767) is assumed to
represent –1 to +1 V. Use the NIFGEN_ATTR_DIGITAL_GAIN attribute to
generate different voltage outputs.
''',
},
    },
    'CreateWaveformI16': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the channel name for which you want to create the waveform.

**Default Value**: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'waveformSize',
                'type': 'ViInt32',
'documentation': {
'description': '''
| Specifies the size of the arbitrary waveform that you want to create.
| The size must meet the following restrictions:

-  The size must be less than or equal to the maximum waveform size that
   the device allows.
-  The size must be greater than or equal to the minimum waveform size
   that the device allows.
-  The size must be an integer multiple of the device waveform quantum.

You can obtain these values from the **maximumWaveformSize**,
**minimumWaveformSize**, and **waveformQuantum** parameters of the
nifgen_QueryArbWfmCapabilities function.

| 
| ****Default Value**:** None
''',
},
            },
            {
                'direction': 'in',
                'name': 'waveformDataArray',
                'type': 'ViInt16[]',
'documentation': {
'description': '''
Specify the array of data that you want to use for the new arbitrary
waveform. The array must have at least as many elements as the value
that you specify in the Waveform Size parameter.
You must normalize the data points in the array to be between -32768 and
+32767.
****Default Value**:** None
''',
},
            },
            {
                'direction': 'out',
                'name': 'waveformHandle',
                'type': 'ViInt32',
'documentation': {
'description': '''
The handle that identifies the new waveform. This handle is used later
when referring to this waveform.
''',
},
            },
        ],
'documentation': {
'description': '''
Creates an onboard waveform from binary 16-bit signed integer (I16) data
for use in Arbitrary Waveform or Arbitrary Sequence output mode. The
**waveformHandle** returned can later be used for setting the active
waveform, changing the data in the waveform, building sequences of
waveforms, or deleting the waveform when it is no longer needed.
''',
'note': '''
You must call the nifgen_ConfigureOutputMode function to set the
**outputMode** parameter to NIFGEN_VAL_OUTPUT_ARB or
NIFGEN_VAL_OUTPUT_SEQ before calling this function.
''',
},
    },
    'DefineUserStandardWaveform': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the channel name for which you want to define a user standard
waveform.

**Default Value**: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'waveformSize',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the size of the waveform in samples.
**Default Value**: 16384
''',
},
            },
            {
                'direction': 'in',
                'name': 'waveformDataArray',
                'type': 'ViReal64[]',
'documentation': {
'description': '''
Specifies the array of data you want to use for the new arbitrary
waveform. The array must have at least as many elements as the value
that you specify in **waveformSize**.

You must normalize the data points in the array to be between –1.00 and
+1.00.

**Default Value**: None
''',
},
            },
        ],
'documentation': {
'description': '''
Defines a user waveform for use in either Standard Function or Frequency
List output mode.

To select the waveform, set the **waveform** parameter to
NIFGEN_VAL_WFM_USER with either the nifgen_ConfigureStandardWaveform
or the nifgen_CreateFreqList function.

The waveform data must be scaled between –1.0 and 1.0. Use the
**amplitude** parameter in the niFgen_ConfigureStandardWaveform
function to generate different output voltages.
''',
'note': '''
You must call the nifgen_ConfigureOutputMode function to set the
**outputMode** parameter to NIFGEN_VAL_OUTPUT_FUNC or
NIFGEN_VAL_OUTPUT_FREQ_LIST before calling this function.
''',
},
    },
    'DeleteNamedWaveform': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the channel onto which the named waveform is loaded.

**Default Value**: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'waveformName',
                'type': 'ViConstString',
'documentation': {
'description': 'Specifies the name to associate with the allocated waveform.',
},
            },
        ],
'documentation': {
'description': '''
Removes a previously created arbitrary waveform from the signal
generator memory and invalidates the waveform handle.
''',
'note': '''
The signal generator must not be in the Generating state when you call
this function.
''',
},
    },
    'DeleteScript': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the channel onto which the script is loaded.

**Default Value**: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'scriptName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the name of the script you want to delete. The script name
appears in the text of the script following the script keyword.
''',
},
            },
        ],
'documentation': {
'description': 'Deletes the specified script from onboard memory.',
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
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
        ],
'documentation': {
'description': '''
Places the instrument in a quiescent state where it has minimal or no
impact on the system to which it is connected. The analog output and all
exported signals are disabled.
''',
},
    },
    'DisableAnalogFilter': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the channel name for which you want to disable the analog
filter.

**Default Value**: "0"
''',
},
            },
        ],
'documentation': {
'description': '''
Disables the analog filter. This function sets the
NIFGEN_ATTR_ANALOG_FILTER_ENABLED attribute to VI_FALSE. This
setting can be applied in Arbitrary Waveform, Arbitrary Sequence, or
Script output modes. You also can use this setting in Standard Function
and Frequency List output modes for user-defined waveforms.
''',
},
    },
    'DisableDigitalFilter': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the channel name for which you want to disable the digital
filter.

**Default Value**: "0"
''',
},
            },
        ],
'documentation': {
'description': '''
Disables the digital filter. This function sets the
NIFGEN_ATTR_DIGITAL_FILTER_ENABLED attribute to VI_FALSE. This
setting can be applied in Arbitrary Waveform, Arbitrary Sequence, or
Script output modes. You also can use this setting in Standard Function
and Frequency List output modes for user-defined waveforms.
''',
},
    },
    'DisableDigitalPatterning': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the channel name for which you want to disable digital pattern
output.

**Default Value**: "0"
''',
},
            },
        ],
'documentation': {
'description': '''
Disables digital pattern output on the signal generator. This function
sets the NIFGEN_ATTR_DIGITAL_PATTERN_ENABLED attribute to VI_FALSE.
''',
},
    },
    'DisableScriptTrigger': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'triggerId',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the Script Trigger used for triggering.

**Defined Values**

**Default Value**: "ScriptTrigger0"
''',
'table_body': [['"ScriptTrigger0"', 'Script Trigger 0'], ['"ScriptTrigger1"', 'Script Trigger 1'], ['"ScriptTrigger2"', 'Script Trigger 2'], ['"ScriptTrigger3"', 'Script Trigger 3']],
},
            },
        ],
'documentation': {
'description': 'Disables the specified Script Trigger.',
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
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
        ],
'documentation': {
'description': 'Disables the Start Trigger.',
},
    },
    'EnableAnalogFilter': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the channel name for which you want to enable the analog
filter.

**Default Value**: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'filterCorrectionFrequency',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the filter correction frequency of the analog filter. On the
NI 5411 and NI 5431, NI-FGEN adjusts signal amplitude to compensate for
the filter attenuation at that frequency. To disable amplitude
correction, set **filterCorrectionFrequency** to 0. For Standard
Function output mode, **filterCorrectionFrequency** typically should be
set to the same value as the frequency of the standard waveform.

**Units**: hertz

**Default Value**: 0
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the analog filter for the device. This function sets the
NIFGEN_ATTR_ANALOG_FILTER_ENABLED attribute to VI_TRUE. This
setting can be applied in Arbitrary Waveform, Arbitrary Sequence, or
Script output modes. You also can use this setting in Standard Function
and Frequency List output modes for user-defined waveforms.
''',
},
    },
    'EnableDigitalFilter': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the channel name for which you want to enable the digital
filter.

**Default Value**: "0"
''',
},
            },
        ],
'documentation': {
'description': '''
Enables the digital filter by setting the
NIFGEN_ATTR_DIGITAL_FILTER_ENABLED attribute to VI_TRUE. This
setting can be applied in Arbitrary Waveform, Arbitrary Sequence, or
Script output modes. You also can use this setting in Standard Function
and Frequency List output modes for user-defined waveforms.
''',
},
    },
    'EnableDigitalPatterning': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the channel name for which you want to enable the digital
pattern output.

**Default Value**: "0"
''',
},
            },
        ],
'documentation': {
'description': '''
Enables digital pattern output on the signal generator. This function
sets the NIFGEN_ATTR_DIGITAL_PATTERN_ENABLED attribute to VI_TRUE.
''',
},
    },
    'ErrorHandler': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init or the niFgen_InitWithOptions functions and identifies a
particular instrument session.

You can pass VI_NULL for this parameter. Passing VI_NULL is useful
when one of the initialize functions fails.

**Default Value**: VI_NULL
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
NI-FGEN functions.

**Default Value**: 0 (VI_SUCCESS)
''',
},
            },
            {
                'direction': 'out',
                'name': 'errorMessage',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Returns the error message string read from the instrument error message
queue.

You must pass a ViChar array with at least 256 bytes.
''',
},
            },
        ],
'documentation': {
'description': '''
Converts a status code returned by an NI-FGEN function into a
user-readable string and returns any error elaborations.
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
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Signal',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the source of the signal to route.
****Defined Values****
''',
'table_body': [['NIFGEN_VAL_ONBOARD_REFERENCE_CLOCK', 'Onboard 10 MHz synchronization clock (PCI only)'], ['NIFGEN_VAL_SYNC_OUT', 'SYNC OUT signal The SYNC OUT signal is normally generated on the SYNC OUT front panel connector.'], ['NIFGEN_VAL_START_TRIGGER', 'Start Trigger'], ['NIFGEN_VAL_MARKER_EVENT', 'Marker Event'], ['NIFGEN_VAL_SAMPLE_CLOCK_TIMEBASE', 'The clock from which the Sample Clock is derived'], ['NIFGEN_VAL_SYNCHRONIZATION', 'Synchronization strobe (NI 5404/5411/5431 only) A synchronization strobe is used to guarantee absolute synchronization between two or more signal generators.'], ['NIFGEN_VAL_SAMPLE_CLOCK', 'Sample Clock'], ['NIFGEN_VAL_REFERENCE_CLOCK', 'PLL Reference Clock'], ['NIFGEN_VAL_SCRIPT_TRIGGER', 'Script Trigger'], ['NIFGEN_VAL_READY_FOR_START_EVENT', 'Ready For Start Event'], ['NIFGEN_VAL_STARTED_EVENT', 'Started Event'], ['NIFGEN_VAL_DONE_EVENT', 'Done Event'], ['NIFGEN_VAL_DATA_MARKER_EVENT', 'Data Marker Event']],
},
            },
            {
                'direction': 'in',
                'name': 'signalIdentifier',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies which instance of the selected signal to export.
****Defined Values****
''',
'table_body': [['"" (empty string)', 'Default (for non instance-based signals)'], ['"ScriptTrigger0"', 'Script Trigger 0'], ['"ScriptTrigger1"', 'Script Trigger 1'], ['"ScriptTrigger2"', 'Script Trigger 2'], ['"ScriptTrigger3"', 'Script Trigger 3'], ['"Marker0"', 'Marker 0'], ['"Marker1"', 'Marker 1'], ['"Marker2"', 'Marker 2'], ['"Marker3"', 'Marker 3'], ['"DataMarker0"', 'Data Marker 0\\*'], ['"DataMarker1"', 'Data Marker 1\\*'], ['"DataMarker2"', 'Data Marker 2\\*'], ['"DataMarker3"', 'Data Marker 3\\*'], ['\\* These Data Marker values apply only to single-channel devices or to multichannel devices that are configured for single-channel operation. When using a device that is configured for multichannel operation, specify the channel number along with the signal identifier. For example, to export Data Marker 0 on channel 1 of a device configured for multichannel operation, use the value "1/ DataMarker0." If you do not specify a channel when using a device configured for multichannel generation, DataMarker0 generates on all channels.']],
},
            },
            {
                'direction': 'in',
                'name': 'outputTerminal',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the output terminal to export the signal.
****Defined Values****
''',
'note': '''
The following **Defined Values** are examples of possible output
terminals. For a complete list of the output terminals available on your
device, refer to the Routes topic for your device or the **Device
Routes** tab in MAX.
''',
'table_body': [['"" (empty string)', 'Do not export signal'], ['"PFI0"', 'PFI line 0'], ['"PFI1"', 'PFI line 1'], ['"PFI4"', 'PFI line 4'], ['"PFI5"', 'PFI line 5'], ['"PXI_Trig0"', 'PXI or RTSI line 0'], ['"PXI_Trig1"', 'PXI or RTSI line 1'], ['"PXI_Trig2"', 'PXI or RTSI line 2'], ['"PXI_Trig3"', 'PXI or RTSI line 3'], ['"PXI_Trig4"', 'PXI or RTSI line 4'], ['"PXI_Trig5"', 'PXI or RTSI line 5'], ['"PXI_Trig6"', 'PXI or RTSI line 6'], ['"PXI_Trig7"', 'PXI or RTSI line 7'], ['"DDC_ClkOut"', 'Clock out from DDC connector'], ['"PXI_Star"', 'PXI star trigger line']],
},
            },
        ],
'documentation': {
'description': '''
Routes signals (clocks, triggers, and events) to the output terminal you
specify.

Any routes created within a session persist after the session closes to
prevent signal glitching. To unconfigure signal routes created in
previous sessions, set **resetDevice** in the niFgen_init function to
VI_TRUE or use the niFgen_ResetDevice function.

If you export a signal with this function and commit the session, the
signal is routed to the output terminal you specify.
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
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the name of the channel on which to check the attribute value
if the attribute is channel-based. If the attribute is not
channel-based, then pass VI_NULL or an empty string ("").

**Default Value**: "" (empty string)
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'Specifies the ID of an attribute.',
},
            },
            {
                'direction': 'out',
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
Queries the value of a ViBoolean attribute.

You can use this function to get the values of instrument-specific
attributes and inherent IVI attributes. If the attribute represents an
instrument state, this function performs instrument I/O in the following
cases:

-  State caching is disabled for the entire session or for the
   particular attribute.
-  State caching is enabled and the currently cached value is invalid.
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
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the name of the channel on which to check the attribute value
if the attribute is channel-based. If the attribute is not
channel-based, then pass VI_NULL or an empty string ("").

**Default Value**: "" (empty string)
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'Specifies the ID of an attribute.',
},
            },
            {
                'direction': 'out',
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
attributes. If the attribute represents an instrument state, this
function performs instrument I/O in the following cases:

-  State caching is disabled for the entire session or for the
   particular attribute.
-  State caching is enabled and the currently cached value is invalid.
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
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the name of the channel on which to check the attribute value
if the attribute is channel-based. If the attribute is not
channel-based, then pass VI_NULL or an empty string ("").

**Default Value**: "" (empty string)
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'Specifies the ID of an attribute.',
},
            },
            {
                'direction': 'out',
                'name': 'attributeValue',
                'type': 'ViInt64',
'documentation': {
'description': '''
Returns the current value of the attribute. Pass the address of a
ViInt64 variable.
''',
},
            },
        ],
'documentation': {
'description': '''
Queries the value of a ViInt64 attribute. You can use this function to
get the values of instrument-specific attributes and inherent IVI
attributes. If the attribute represents an instrument state, this
function performs instrument I/O in the following cases:

-  State caching is disabled for the entire session or for the
   particular attribute.
-  State caching is enabled and the currently cached value is invalid.
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
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the name of the channel on which to check the attribute value
if the attribute is channel-based. If the attribute is not
channel-based, then pass VI_NULL or an empty string ("").

**Default Value**: "" (empty string)
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'Specifies the ID of an attribute.',
},
            },
            {
                'direction': 'out',
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
Queries the value of a ViReal64 attribute.

You can use this function to get the values of instrument-specific
attributes and inherent IVI attributes. If the attribute represents an
instrument state, this function performs instrument I/O in the following
cases:

-  State caching is disabled for the entire session or for the
   particular attribute.
-  State caching is enabled and the currently cached value is invalid.
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
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the name of the channel on which to check the attribute value
if the attribute is channel-based. If the attribute is not
channel-based, then pass VI_NULL or an empty string ("").

**Default Value**: "" (empty string)
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'Specifies the ID of an attribute.',
},
            },
            {
                'direction': 'out',
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
Queries the value of a ViSession attribute.

You can use this function to get the values of instrument-specific
attributes and inherent IVI attributes. If the attribute represents an
instrument state, this function performs instrument I/O in the following
cases:

-  State caching is disabled for the entire session or for the
   particular attribute.
-  State caching is enabled and the currently cached value is invalid.
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
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the name of the channel on which to check the attribute value
if the attribute is channel-based. If the attribute is not
channel-based, then pass VI_NULL or an empty string ("").

**Default Value**: "" (empty string)
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'Specifies the ID of an attribute.',
},
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the number of bytes in the ViChar array you specify for the
**attributeValue** parameter.

If the current value of the attribute, including the terminating NUL
byte, contains more bytes than you indicate in this parameter, the
function copies **arraySize** – 1 bytes into the buffer, places an ASCII
NUL byte at the end of the buffer, and returns the array size you must
pass to get the entire value. For example, if the value is 123456 and
**arraySize** is 4, the function places 123 into the buffer and returns
7.

If you pass a negative number, the function copies the value to the
buffer regardless of the number of bytes in the value.

If you pass 0, you can pass VI_NULL for the **attributeValue** buffer
parameter.
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
attribute. The buffer must be a ViChar data type and have at least as
many bytes as indicated in the **arraySize** parameter.

If the current value of the attribute, including the terminating NUL
byte, contains more bytes than you indicate in this parameter, the
function copies **arraySize** – 1 bytes into the buffer, places an ASCII
NUL byte at the end of the buffer, and returns the array size you must
pass to get the entire value. For example, if the value is 123456 and
**arraySize** is 4, the function places 123 into the buffer and returns
7.

If you specify 0 for the **arraySize** parameter, you can pass VI_NULL
for this parameter.
''',
},
            },
        ],
'documentation': {
'description': '''
Queries the value of a ViString attribute.

You can use this function to get the values of instrument-specific
attributes and inherent IVI attributes. If the attribute represents an
instrument state, this function performs instrument I/O in the following
cases:

-  State caching is disabled for the entire session or for the
   particular attribute.
-  State caching is enabled and the currently cached value is invalid.

You must provide a ViChar array to serve as a buffer for the value. You
pass the number of bytes in the buffer as the **arraySize** parameter.
If the current value of the attribute, including the terminating NUL
byte, is larger than the size you indicate in the **arraySize**
parameter, the function copies **arraySize** – 1 bytes into the buffer,
places an ASCII NUL byte at the end of the buffer, and returns the array
size you must pass to get the entire value. For example, if the value is
123456 and **arraySize** is 4, the function places 123 into the buffer
and returns 7.

If you want to call this function just to get the required array size,
you can pass 0 for **arraySize** and VI_NULL for the **attributeValue**
buffer.

If you want the function to fill in the buffer regardless of the number
of bytes in the value, pass a negative number for the **arraySize**
parameter.
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
Identifies your instrument session. **vi** is obtained from the
nifgen_init or the nifgen_InitExtCal function and identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Info',
                'type': 'ViString',
'documentation': {
'description': '''
Specifies a string into which the user information is copied. This
parameter must point to a character buffer large enough to hold the
information string.
''',
},
            },
        ],
'documentation': {
'description': '''
Retrieves user-defined information from the onboard EEPROM. Call the
nifgen_GetCalUserDefinedInfoMaxSize function to determine the number of
characters that can be retrieved. The buffer you provide should be the
size of the maximum number of characters stored plus one termination
character.
''',
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
Identifies your instrument session. **vi** is obtained from the
nifgen_init or the nifgen_InitExtCal function and identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'out',
                'name': 'infoSize',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the maximum number of characters of user defined info that can
be stored in the onboard EEPROM.
''',
},
            },
        ],
'documentation': {
'description': '''
Returns the maximum number of characters, excluding the termination
character, of user-defined information that can be stored in the onboard
EEPROM.
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
Identifies your instrument session. **vi** is obtained from the
niFgen_init or the nifgen_InitWithOptions functions and identifies a
particular instrument session.

You can pass VI_NULL for this parameter. Passing VI_NULL is useful
when one of the initialize functions fail.

**Default Value**: VI_NULL
''',
},
            },
            {
                'direction': 'out',
                'name': 'errorCode',
                'type': 'ViStatus',
'documentation': {
'description': '''
The error code for the session or execution thread.

A value of VI_SUCCESS (0) indicates that no error occurred. A positive
value indicates a warning. A negative value indicates an error.

You can call nifgen_error_message to get a text description of the
value.

If you are not interested in this value, you can pass VI_NULL.
''',
},
            },
            {
                'direction': 'in',
                'name': 'errorDescriptionBufferSize',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the size of the **errorDescription** array.

You can determine the array size needed to store the entire error
description by setting this parameter to 0. The function then ignores
the **errorDescription** buffer, which may be set to VI_NULL, and gives
as its return value the required buffer size. You can then call the
function a second time using the correct buffer size.
''',
},
            },
            {
                'direction': 'out',
                'name': 'errorDescription',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The error description string for the session or execution thread. If the
error code is nonzero, the description string can further describe the
error or warning condition.

If you are not interested in this value, you can pass VI_NULL.
Otherwise, you must pass a ViChar array of a size specified with the
**errorDescriptionBufferSize** parameter.
''',
},
            },
        ],
'documentation': {
'description': '''
Returns the error information associated with an IVI session or with the
current execution thread. If you specify a valid IVI session for the
**vi** parameter, this function retrieves and then clears the error
information for the session. If you pass VI_NULL for the **vi**
parameter, this function retrieves and then clears the error information
for the current execution thread.

The IVI Engine also maintains this error information separately for each
thread. This feature is useful if you do not have a session handle to
pass to the niFgen_GetError or nifgen_ClearError functions. This
situation occurs when a call to the nifgen_init or
nifgen_InitWithOptions function fails.
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
Identifies your instrument session. **vi** is obtained from the
nifgen_init or the nifgen_InitExtCal function and identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'out',
                'name': 'Year',
                'type': 'ViInt32',
'documentation': {
'description': 'Specifies the year of the last successful calibration.',
},
            },
            {
                'direction': 'out',
                'name': 'Month',
                'type': 'ViInt32',
'documentation': {
'description': 'Specifies the month of the last successful calibration.',
},
            },
            {
                'direction': 'out',
                'name': 'Day',
                'type': 'ViInt32',
'documentation': {
'description': 'Specifies the day of the last successful calibration.',
},
            },
            {
                'direction': 'out',
                'name': 'Hour',
                'type': 'ViInt32',
'documentation': {
'description': 'Specifies the hour of the last successful calibration.',
},
            },
            {
                'direction': 'out',
                'name': 'Minute',
                'type': 'ViInt32',
'documentation': {
'description': 'Specifies the minute of the last successful calibration.',
},
            },
        ],
'documentation': {
'description': '''
Returns the date and time of the last successful external calibration.
The time returned is 24-hour (military) local time; for example, if the
device was calibrated at 2:30 PM, this function returns 14 for the
**hour** parameter and 30 for the **minute** parameter.
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
Identifies your instrument session. **vi** is obtained from the
nifgen_init or the nifgen_InitExtCal function and identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'out',
                'name': 'Temperature',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the temperature at the last successful calibration in degrees
Celsius.
''',
},
            },
        ],
'documentation': {
'description': '''
Returns the temperature at the last successful external calibration. The
temperature is returned in degrees Celsius.
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
Identifies your instrument session. **vi** is obtained from the
nifgen_init or the nifgen_InitExtCal function and identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'out',
                'name': 'Months',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the recommended interval between external calibrations in
months.
''',
},
            },
        ],
'documentation': {
'description': '''
Returns the recommended interval between external calibrations in
months.
''',
},
    },
    'GetFIRFilterCoefficients': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the channel name for which you want to configure the operation
mode.

**Defined Value**: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'ViInt32',
'documentation': {
'description': 'Specifies the size of the coefficient array',
},
            },
            {
                'direction': 'in',
                'name': 'coefficientsArray',
                'type': 'ViReal64[]',
'documentation': {
'description': '''
Specifies the array of data the onboard signal processor uses for the
FIR filter coefficients. For the NI 5441, provide a symmetric array of
95 coefficients to this parameter. The array must have at least as many
elements as the value that you specify in the **numberOfCoefficients**
parameter in this function.
The coefficients should range between –1.00 and +1.00.
''',
},
            },
            {
                'direction': 'in',
                'name': 'numberOfCoefficientsRead',
                'type': 'ViInt32[]',
'documentation': {
'description': '''
Specifies the array of data containing the number of coefficients you
want to read.
''',
},
            },
        ],
'documentation': {
'description': '''
| Returns the FIR filter coefficients used by the onboard signal
  processing block. These coefficients are determined by NI-FGEN and
  based on the FIR filter type and corresponding attribute (Alpha,
  Passband, BT) unless you are using the custom filter. If you are using
  a custom filter, the coefficients returned are those set with the
  nifgen_ConfigureCustomFIRFilterCoefficients function coerced to the
  quantized values used by the device.
| To use this function, first call an instance of the
  niFgen_GetFIRFilterCoefficients function with the
  **coefficientsArray** parameter set to VI_NULL. Calling the function
  in this state returns the current size of the **coefficientsArray** as
  the value of the **numberOfCoefficientsRead** parameter. Create an
  array of this size, and call the niFgen_GetFIRFilterCoefficients
  function a second time, passing the new array as the
  **coefficientsArray** parameter and the size as the **arraySize**
  parameter. This second function call populates the array with the FIR
  filter coefficients.
| Refer to the FIR Filter topic for your device in the *NI Signal
  Generators Help* for more information about FIR filter coefficients.
  This function is supported only for the NI 5441.
| **Default Value**: None
''',
},
    },
    'GetHardwareState': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'out',
                'name': 'state',
                'type': 'ViInt32',
'documentation': {
'description': '''
Returns the hardware state of the signal generator.

**Defined Values**
''',
'table_body': [['NIFGEN_VAL_IDLE', 'The device is in the Idle state.'], ['NIFGEN_VAL_WAITING_FOR_START_TRIGGER', 'The device is waiting for Start Trigger.'], ['NIFGEN_VAL_RUNNING', 'The device is in the Running state.'], ['NIFGEN_VAL_DONE', 'The generation has completed successfully.'], ['NIFGEN_VAL_HARDWARE_ERROR', 'There is a hardware error.']],
},
            },
        ],
'documentation': {
'description': '''
Returns the current hardware state of the device and, if the device is
in the hardware error state, the current hardware error.
''',
'note': 'Hardware states do not necessarily correspond to NI-FGEN states.',
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
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the number of bytes in the ViChar array you specify for the
**coercionRecord** parameter.

If the next coercion record string, including the terminating NUL byte,
contains more bytes than you indicate in this parameter, the function
copies **bufferSize** – 1 bytes into the buffer, places an ASCII NUL
byte at the end of the buffer, and returns the buffer size that you must
pass to get the entire value. For example, if the value is 123456 and
the buffer size is 4, the function places 123 into the buffer and
returns 7.

If you pass a negative number, the function copies the value to the
buffer regardless of the number of bytes in the value.

If you pass 0, you can pass VI_NULL for the **coercionRecord** buffer
parameter.

**Default Value**: None
''',
},
            },
            {
                'direction': 'out',
                'name': 'coercionRecord',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Returns the next coercion record for the IVI session. If there are no
coercion records, the function returns an empty string.

The buffer must contain at least as many elements as the value you
specify with the **bufferSize** parameter. If the next coercion record
string, including the terminating NUL byte, contains more bytes than you
indicate with the **bufferSize** parameter, the function copies
**bufferSize** – 1 bytes into the buffer, places an ASCII NUL byte at
the end of the buffer, and returns the buffer size that you must pass to
get the entire value. For example, if the value is "123456" and
**bufferSize** is 4, the function places "123" into the buffer and
returns 7.

This parameter returns an empty string if no coercion records remain for
the session.
''',
},
            },
        ],
'documentation': {
'description': '''
Returns the coercion information associated with the IVI session. This
function retrieves and clears the oldest instance in which the NI-FGEN
coerced a value you specified to another value.

If you set the NIFGEN_ATTR_RECORD_COERCIONS attribute to VI_TRUE,
NI-FGEN keeps a list of all coercions it makes on ViInt32 or ViReal64
values that you pass to NI-FGEN functions. You use this function to
retrieve information from that list.

If the next coercion record string, including the terminating NUL byte,
contains more bytes than you indicate in this parameter, the function
copies **bufferSize** – 1 bytes into the buffer, places an ASCII NUL
byte at the end of the buffer, and returns the buffer size you must pass
to get the entire value. For example, if the value is 123456 and
**bufferSize** is 4, the function places 123 into the buffer and returns
7.

If you pass a negative number, the function copies the value to the
buffer regardless of the number of bytes in the value.

If you pass 0, you can pass VI_NULL for the **coercionRecord** buffer
parameter.

The function returns an empty string in the **coercionRecord** parameter
if no coercion records remain for the session.
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
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the number of bytes in the ViChar array you specify for the
**interchangeWarning** parameter.

If the next interchangeability warning string, including the terminating
NUL byte, contains more bytes than you indicate in this parameter, the
function copies **bufferSize** – 1 bytes into the buffer, places an
ASCII NUL byte at the end of the buffer, and returns the buffer size
that you must pass to get the entire value. For example, if the value is
123456 and **bufferSize** is 4, the function places 123 into the buffer
and returns 7.

If you pass a negative number, the function copies the value to the
buffer regardless of the number of bytes in the value.

If you pass 0, you can pass VI_NULL for the **interchangeWarning**
buffer parameter.

**Default Value**: None
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

The buffer must contain at least as many elements as the value you
specify with the **bufferSize** parameter. If the next
interchangeability warning string, including the terminating NUL byte,
contains more bytes than you indicate with the **bufferSize** parameter,
the function copies **bufferSize** – 1 bytes into the buffer, places an
ASCII NUL byte at the end of the buffer, and returns the buffer size
that you must pass to get the entire value. For example, if the value is
123456 and **bufferSize** is 4, the function places 123 into the buffer
and returns 7.

This parameter returns an empty string if no interchangeability warnings
remain for the session.
''',
},
            },
        ],
'documentation': {
'description': '''
Returns the interchangeability warnings associated with the IVI session.
It retrieves and clears the oldest instance in which the class driver
recorded an interchangeability warning. Interchangeability warnings
indicate that using your application with a different instrument might
cause different behavior. Use this function to retrieve
interchangeability warnings.

NI-FGEN performs interchangeability checking when the
NIFGEN_ATTR_INTERCHANGE_CHECK attribute is set to VI_TRUE.

The function returns an empty string in the **interchangeWarning**
parameter if no interchangeability warnings remain for the session.

In general, NI-FGEN generates interchangeability warnings when an
attribute that affects the behavior of the instrument is in a state that
you did not specify.
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
Identifies your instrument session. **vi** is obtained from the
nifgen_init or the nifgen_InitExtCal function and identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'out',
                'name': 'Year',
                'type': 'ViInt32',
'documentation': {
'description': 'Specifies the year of the last successful calibration.',
},
            },
            {
                'direction': 'out',
                'name': 'Month',
                'type': 'ViInt32',
'documentation': {
'description': 'Specifies the month of the last successful calibration.',
},
            },
            {
                'direction': 'out',
                'name': 'Day',
                'type': 'ViInt32',
'documentation': {
'description': 'Specifies the day of the last successful calibration.',
},
            },
            {
                'direction': 'out',
                'name': 'Hour',
                'type': 'ViInt32',
'documentation': {
'description': 'Specifies the hour of the last successful calibration.',
},
            },
            {
                'direction': 'out',
                'name': 'Minute',
                'type': 'ViInt32',
'documentation': {
'description': 'Specifies the minute of the last successful calibration.',
},
            },
        ],
'documentation': {
'description': '''
Returns the date and time of the last successful self-calibration.

All values are returned as separate parameters. Each parameter is
returned as an integer, including the year, month, day, hour, minute,
and second. For example, if the device is calibrated in September 2013,
this function returns 9 for the **month** parameter and 2013 for the
**year** parameter.

The time returned is 24-hour (military) local time. For example, if the
device was calibrated at 2:30 PM, this function returns 14 for the
**hours** parameter and 30 for the **minutes** parameter.
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
Identifies your instrument session. **vi** is obtained from the
nifgen_init or the nifgen_InitExtCal function and identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'out',
                'name': 'Temperature',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the temperature at the last successful calibration in degrees
Celsius.
''',
},
            },
        ],
'documentation': {
'description': '''
Returns the temperature at the last successful self-calibration. The
temperature is returned in degrees Celsius.
''',
},
    },
    'GetSelfCalSupported': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
nifgen_init or the nifgen_InitWithOptions function and identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'out',
                'name': 'selfCalSupported',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Returns whether the device supports self-calibration.

****Defined Values****
''',
'table_body': [['VI_TRUE', 'Self–calibration is supported.'], ['VI_FALSE', 'Self–calibration is not supported.']],
},
            },
        ],
'documentation': {
'description': 'Returns whether the device supports self–calibration.',
},
    },
    'GetStreamEndpointHandle': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'streamEndpoint',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the stream endpoint FIFO to configure. Refer to the
device-specific documentation for peer-to-peer streaming in the *NI
Signal Generators Help* for more information.
''',
},
            },
            {
                'direction': 'out',
                'name': 'readerHandle',
                'type': 'void',
'documentation': {
'description': '''
Specifies the reader endpoint handle that is used with NI-P2P to create
a stream with the signal generator as an endpoint.
''',
},
            },
        ],
'documentation': {
'description': '''
Returns a reader endpoint handle that can be used with NI-P2P to
configure a peer-to-peer stream with a signal generator endpoint.
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
'caution': '''
Traditional NI-DAQ and NI-DAQmx device names are not case-sensitive.
However, all IVI names, such as logical names, are case-sensitive. If
you use logical names, driver session names, or virtual names in your
program, you must ensure that the name you use matches the name in the
IVI Configuration Store file exactly, without any variations in the case
of the characters.
''',
'description': '''
| Specifies the resource name of the device to initialize.

For Traditional NI-DAQ devices, the syntax is DAQ::\ *n*, where *n* is
the device number assigned by MAX, as shown in Example 1.

For NI-DAQmx devices, the syntax is just the device name specified in
MAX, as shown in Example 2. Typical default names for NI-DAQmx devices
in MAX are Dev1 or PXI1Slot1. You can rename an NI-DAQmx device by
right-clicking on the name in MAX and entering a new name.

An alternate syntax for NI-DAQmx devices consists of DAQ::\ *NI-DAQmx
device name*, as shown in Example 3. This naming convention allows for
the use of an NI-DAQmx device in an application that was originally
designed for a Traditional NI-DAQ device. For example, if the
application expects DAQ::1, you can rename the NI-DAQmx device to 1 in
MAX and pass in DAQ::1 for the resource name, as shown in Example 4.

If you use the DAQ::\ *n* syntax and an NI-DAQmx device name already
exists with that same name, the NI-DAQmx device is matched first.

You can also pass in the name of an IVI logical name or an IVI virtual
name configured with the IVI Configuration utility, as shown in Example
5. A logical name identifies a particular virtual instrument. A virtual
name identifies a specific device and specifies the initial settings for
the session.
''',
'table_body': [['1', 'Traditional NI-DAQ device', 'DAQ::\\ *1*', '(*1* = device number)'], ['2', 'NI-DAQmx device', '*myDAQmxDevice*', '(*myDAQmxDevice* = device name)'], ['3', 'NI-DAQmx device', 'DAQ::\\ *myDAQmxDevice*', '(*myDAQmxDevice* = device name)'], ['4', 'NI-DAQmx device', 'DAQ::\\ *2*', '(*2* = device name)'], ['5', 'IVI logical name or IVI virtual name', '*myLogicalName*', '(*myLogicalName* = name)']],
'table_header': ['Example #', 'Device Type', 'Syntax', 'Variable'],
},
            },
            {
                'direction': 'in',
                'name': 'Password',
                'type': 'ViConstString',
'documentation': {
'description': '''
The calibration password required to open an external calibration
session to the device.
''',
},
            },
            {
                'direction': 'out',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Returns a session handle that you can use to identify the device in all
subsequent NI-FGEN function calls.
''',
},
            },
        ],
'documentation': {
'description': '''
Creates and initializes a special NI-FGEN external calibration session.
The ViSession returned is an NI-FGEN session that can be used to
configure the device using normal attributes and functions. However,
flags have been set that allow you to program an external calibration
procedure using the special calibration attributes and functions. The
NI 5401/5404/5411/5431 have different calibration functions. Refer to
the nifgen_Related_Documentation for the signal generator for more
information.
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
'caution': '''
Traditional NI-DAQ and NI-DAQmx device names are not case-sensitive.
However, all IVI names, such as logical names, are case-sensitive. If
you use logical names, driver session names, or virtual names in your
program, you must ensure that the name you use matches the name in the
IVI Configuration Store file exactly, without any variations in the case
of the characters.
''',
'description': '''
| Specifies the resource name of the device to initialize.

For Traditional NI-DAQ devices, the syntax is DAQ::\ *n*, where *n* is
the device number assigned by MAX, as shown in Example 1.

For NI-DAQmx devices, the syntax is just the device name specified in
MAX, as shown in Example 2. Typical default names for NI-DAQmx devices
in MAX are Dev1 or PXI1Slot1. You can rename an NI-DAQmx device by
right-clicking on the name in MAX and entering a new name.

An alternate syntax for NI-DAQmx devices consists of DAQ::\ *NI-DAQmx
device name*, as shown in Example 3. This naming convention allows for
the use of an NI-DAQmx device in an application that was originally
designed for a Traditional NI-DAQ device. For example, if the
application expects DAQ::1, you can rename the NI-DAQmx device to 1 in
MAX and pass in DAQ::1 for the resource name, as shown in Example 4.

If you use the DAQ::\ *n* syntax and an NI-DAQmx device name already
exists with that same name, the NI-DAQmx device is matched first.

You can also pass in the name of an IVI logical name or an IVI virtual
name configured with the IVI Configuration utility, as shown in Example
5. A logical name identifies a particular virtual instrument. A virtual
name identifies a specific device and specifies the initial settings for
the session.
''',
'table_body': [['1', 'Traditional NI-DAQ device', 'DAQ::\\ *1*', '(*1* = device number)'], ['2', 'NI-DAQmx device', '*myDAQmxDevice*', '(*myDAQmxDevice* = device name)'], ['3', 'NI-DAQmx device', 'DAQ::\\ *myDAQmxDevice*', '(*myDAQmxDevice* = device name)'], ['4', 'NI-DAQmx device', 'DAQ::\\ *2*', '(*2* = device name)'], ['5', 'IVI logical name or IVI virtual name', '*myLogicalName*', '(*myLogicalName* = name)']],
'table_header': ['Example #', 'Device Type', 'Syntax', 'Variable'],
},
            },
            {
                'direction': 'in',
                'name': 'idQuery',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether you want NI-FGEN to perform an ID query.

When you set this parameter to VI_TRUE, NI-FGEN verifies that the
device that you initialize is a type that it supports.

Circumstances can arise where sending an ID query to the device is
undesirable. When you set this parameter to VI_FALSE, the function
initializes the device without performing an ID query.

****Defined Values****

**Default Value**: VI_TRUE
''',
'table_body': [['VI_TRUE', 'Perform ID query'], ['VI_FALSE', 'Skip ID query']],
},
            },
            {
                'direction': 'in',
                'name': 'resetDevice',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether you want to reset the device during the initialization
procedure. VI_TRUE specifies that the device is reset and performs the
same function as the nifgen_Reset function.

****Defined Values****

**Default Value**: VI_TRUE
''',
'table_body': [['VI_TRUE', 'Reset device'], ['VI_FALSE', 'Do not reset device']],
},
            },
            {
                'direction': 'in',
                'name': 'optionString',
                'type': 'ViString',
'documentation': {
'description': '''
Sets the initial value of certain session attributes.

The syntax for **optionString** is

<*attributeName*> = <*value*>

where

*attributeName* is the name of the attribute and *value* is the value to
which the attribute is set

To set multiple attributes, separate them with a comma.

If you pass NULL or an empty string for this parameter, the session uses
the default values for these attributes. You can override the default
values by assigning a value explicitly in a string that you pass for
this parameter.

You do not have to specify all of the attributes and may leave any of
them out. However, if you do not specify one of the attributes, its
default value is used.

If simulation is enabled (Simulate=1), you may specify the device that
you want to simulate. To specify a device, enter the following syntax in
**optionString**.

DriverSetup=Model:<*driver model number*>;Channels:<*channel
names*>;BoardType:<*module type*>;MemorySize:<*size of onboard memory in
bytes*>

**Syntax Examples**

**Attributes and **Defined Values****

**Default Values**: "Simulate=0,RangeCheck=1,QueryInstrStatus=1,Cache=1"
''',
'table_body': [['RangeCheck', 'NIFGEN_ATTR_RANGE_CHECK', 'VI_TRUE, VI_FALSE'], ['QueryInstrStatus', 'NIFGEN_ATTR_QUERY_INSTRUMENT_STATUS', 'VI_TRUE, VI_FALSE'], ['Cache', 'NIFGEN_ATTR_CACHE', 'VI_TRUE, VI_FALSE'], ['Simulate', 'NIFGEN_ATTR_SIMULATE', 'VI_TRUE, VI_FALSE']],
'table_header': ['Attribute Name', 'Attribute', 'Values'],
},
            },
            {
                'direction': 'out',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Returns a session handle that you can use to identify the device in all
subsequent NI-FGEN function calls.
''',
},
            },
        ],
'documentation': {
'description': '''
Performs the following initialization actions:

-  Creates a new IVI instrument session and optionally sets the initial
   state of the following session attributes:
   NIFGEN_ATTR_RANGE_CHECK, NIFGEN_ATTR_QUERY_INSTRUMENT_STATUS,
   NIFGEN_ATTR_CACHE, NIFGEN_ATTR_SIMULATE, and
   NIFGEN_ATTR_RECORD_COERCIONS.
-  Opens a session to the specified device using the interface and
   address that you specify for **resourceName**.
-  If **IDQuery** is set to VI_TRUE, this function queries the device
   ID and checks that it is valid for NI-FGEN.
-  If **resetDevice** is set to VI_TRUE, this function resets the
   device to a known state.
-  Sends initialization commands to set the instrument to the state
   necessary for NI-FGEN operation.
-  Returns a session handle that you can use to identify the device in
   all subsequent NI-FGEN function calls.
''',
},
    },
    'InitializeAnalogOutputCalibration': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
nifgen_InitExtCal function and identifies a particular instrument
session.
''',
},
            },
        ],
'documentation': {
'description': 'Sets up the device to start the analog output calibration.',
},
    },
    'InitializeCalADCCalibration': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
nifgen_InitExtCal function and identifies a particular instrument
session.
''',
},
            },
        ],
'documentation': {
'description': '''
Initializes an external calibration session for ADC calibration. For the
NI 5421/5422/5441, ADC calibration involves characterizing the gain and
offset of the onboard ADC.
''',
},
    },
    'InitializeFlatnessCalibration': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
nifgen_InitExtCal function and identifies a particular instrument
session.
''',
},
            },
        ],
'documentation': {
'description': 'Initializes an external calibration session to calibrate flatness.',
},
    },
    'InitializeOscillatorFrequencyCalibration': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
nifgen_InitExtCal function and identifies a particular instrument
session.
''',
},
            },
        ],
'documentation': {
'description': '''
Sets up the device to start the VCXO calibration.

The session handle should be the handle returned by the
nifgen_InitExtCal function.
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
'caution': '''
Traditional NI-DAQ and NI-DAQmx device names are not case-sensitive.
However, all IVI names, such as logical names, are case-sensitive. If
you use logical names, driver session names, or virtual names in your
program, you must ensure that the name you use matches the name in the
IVI Configuration Store file exactly, without any variations in the case
of the characters.
''',
'description': '''
| Specifies the resource name of the device to initialize.

For Traditional NI-DAQ devices, the syntax is DAQ::\ *n*, where *n* is
the device number assigned by MAX, as shown in Example 1.

For NI-DAQmx devices, the syntax is just the device name specified in
MAX, as shown in Example 2. Typical default names for NI-DAQmx devices
in MAX are Dev1 or PXI1Slot1. You can rename an NI-DAQmx device by
right-clicking on the name in MAX and entering a new name.

An alternate syntax for NI-DAQmx devices consists of DAQ::\ *NI-DAQmx
device name*, as shown in Example 3. This naming convention allows for
the use of an NI-DAQmx device in an application that was originally
designed for a Traditional NI-DAQ device. For example, if the
application expects DAQ::1, you can rename the NI-DAQmx device to 1 in
MAX and pass in DAQ::1 for the resource name, as shown in Example 4.

If you use the DAQ::\ *n* syntax and an NI-DAQmx device name already
exists with that same name, the NI-DAQmx device is matched first.

You can also pass in the name of an IVI logical name or an IVI virtual
name configured with the IVI Configuration utility, as shown in Example
5. A logical name identifies a particular virtual instrument. A virtual
name identifies a specific device and specifies the initial settings for
the session.
''',
'table_body': [['1', 'Traditional NI-DAQ device', 'DAQ::\\ *1*', '(*1* = device number)'], ['2', 'NI-DAQmx device', '*myDAQmxDevice*', '(*myDAQmxDevice* = device name)'], ['3', 'NI-DAQmx device', 'DAQ::\\ *myDAQmxDevice*', '(*myDAQmxDevice* = device name)'], ['4', 'NI-DAQmx device', 'DAQ::\\ *2*', '(*2* = device name)'], ['5', 'IVI logical name or IVI virtual name', '*myLogicalName*', '(*myLogicalName* = name)']],
'table_header': ['Example #', 'Device Type', 'Syntax', 'Variable'],
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViString',
'documentation': {
'description': '''
Specifies the channel that this VI uses.

**Default Value**: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'resetDevice',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether you want to reset the device during the initialization
procedure. VI_TRUE specifies that the device is reset and performs the
same function as the nifgen_Reset function.

****Defined Values****

**Default Value**: VI_FALSE
''',
'table_body': [['VI_TRUE', 'Reset device'], ['VI_FALSE', 'Do not reset device']],
},
            },
            {
                'direction': 'in',
                'name': 'optionString',
                'type': 'ViString',
'documentation': {
'description': '''
Sets the initial value of certain session attributes.

The syntax for **optionString** is

<*attributeName*> = <*value*>

where

*attributeName* is the name of the attribute and *value* is the value to
which the attribute is set

To set multiple attributes, separate them with a comma.

If you pass NULL or an empty string for this parameter, the session uses
the default values for these attributes. You can override the default
values by assigning a value explicitly in a string that you pass for
this parameter.

You do not have to specify all of the attributes and may leave any of
them out. However, if you do not specify one of the attributes, its
default value is used.

If simulation is enabled (Simulate=1), you may specify the device that
you want to simulate. To specify a device, enter the following syntax in
**optionString**.

DriverSetup=Model:<*driver model number*>;Channels:<*channel
names*>;BoardType:<*module type*>;MemorySize:<*size of onboard memory in
bytes*>

**Syntax Examples**

**Attributes and **Defined Values****

**Default Values**: "Simulate=0,RangeCheck=1,QueryInstrStatus=1,Cache=1"
''',
'table_body': [['RangeCheck', 'NIFGEN_ATTR_RANGE_CHECK', 'VI_TRUE, VI_FALSE'], ['QueryInstrStatus', 'NIFGEN_ATTR_QUERY_INSTRUMENT_STATUS', 'VI_TRUE, VI_FALSE'], ['Cache', 'NIFGEN_ATTR_CACHE', 'VI_TRUE, VI_FALSE'], ['Simulate', 'NIFGEN_ATTR_SIMULATE', 'VI_TRUE, VI_FALSE']],
'table_header': ['Attribute Name', 'Attribute', 'Values'],
},
            },
            {
                'direction': 'out',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Returns a session handle that you can use to identify the device in all
subsequent NI-FGEN function calls.
''',
},
            },
        ],
'documentation': {
'description': '''
Creates and returns a new NI-FGEN session to the specified channel of a
waveform generator that is used in all subsequent NI-FGEN function
calls.
''',
},
    },
    'InitiateGeneration': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
        ],
'documentation': {
'description': '''
Initiates signal generation. If you want to abort signal generation,
call the nifgen_AbortGeneration function. After the signal generation
is aborted, you can call the niFgen_InitiateGeneration function to
cause the signal generator to produce a signal again.
''',
},
    },
    'IsDone': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'out',
                'name': 'Done',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Returns information about the completion of waveform generation.

**Defined Values**
''',
'table_body': [['VI_TRUE', 'Generation is complete.'], ['VI_FALSE', 'Generation is not complete.']],
},
            },
        ],
'documentation': {
'description': '''
Determines whether the current generation is complete. This function
sets the **done** parameter to VI_TRUE if the session is in the Idle or
Committed states.
''',
'note': '''
NI-FGEN only reports the **done** parameter as VI_TRUE after the
current generation is complete in Single trigger mode.
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
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'out',
                'name': 'callerHasLock',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Keeps track of whether you obtained a lock and therefore need to unlock
the session. Pass the address of a local ViBoolean variable. In the
declaration of the local variable, initialize it to VI_FALSE. Pass the
address of the same local variable to any other calls you make to the
niFgen_LockSession function or the nifgen_UnlockSession function in
the same function.

This parameter serves as a convenience. If you do not want to use this
parameter, pass VI_NULL.

This parameter is an input/output parameter. The niFgen_LockSession
function and the niFgen_UnlockSession function each inspect the current
value and take the following actions:

-  If the value is VI_TRUE, the niFgen_LockSession function does not
   lock the session again. If the value is VI_FALSE, the
   niFgen_LockSession function obtains the lock and sets the value of
   the parameter to VI_TRUE.
-  If the value is VI_FALSE, the niFgen_UnlockSession function does
   not attempt to unlock the session. If the value is VI_TRUE, the
   niFgen_UnlockSession function releases the lock and sets the value
   of the parameter to VI_FALSE.

Thus, you can call the niFgen_UnlockSession function at the end of your
function without worrying about whether you actually have the lock.

Example:

ViStatus TestFunc (ViSession vi, ViInt32 flags)
{

ViStatus error = VI_SUCCESS;
ViBoolean haveLock = VI_FALSE;
if (flags & BIT_1)
{

viCheckErr( niFgen_LockSession(vi, &haveLock;));
viCheckErr( TakeAction1(vi));
if (flags & BIT_2)
{

 viCheckErr( niFgen_UnlockSession(vi, &haveLock;));
viCheckErr( TakeAction2(vi));
viCheckErr( niFgen_LockSession(vi, &haveLock;);

}
if (flags & BIT_3)

 viCheckErr( TakeAction3(vi));

}

Error:

| 

/\*
At this point, you cannot really be sure that
you have the lock. Fortunately, the haveLock
variable takes care of that for you.
\*/
niFgen_UnlockSession(vi, &haveLock;);
return error;

| }
''',
},
            },
        ],
'documentation': {
'description': '''
Obtains a multithread lock on the instrument session. Before it does so,
this function waits until all other execution threads have released
their locks on the instrument session.

Other threads might have obtained a lock on this session in the
following ways:

-  Your application called the niFgen_LockSession function.
-  A call to the NI-FGEN locked the session.
-  A call to the IVI Engine locked the session.

After your call to the niFgen_LockSession function returns
successfully, no other threads can access the instrument session until
you call the nifgen_UnlockSession function.

Use the niFgen_LockSession function and the niFgen_UnlockSession
function around a sequence of calls to NI-FGEN functions if you require
that the instrument retain its settings through the end of the sequence.

You can safely make nested calls to the niFgen_LockSession function
within the same thread. To completely unlock the session, you must
balance each call to the niFgen_LockSession function with a call to the
niFgen_UnlockSession function. If, however, you use the
**callerHasLock** parameter in all calls to the niFgen_LockSession
function and the niFgen_UnlockSession function within a function, the
IVI Engine locks the session only once within the function regardless of
the number of calls you make to the niFgen_LockSession function. This
configuration allows you to call the niFgen_UnlockSession function just
once at the end of the function.
''',
},
    },
    'ManualEnableP2PStream': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'endpointName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the stream endpoint FIFO to configure. Refer to the
`Peer-to-Peer Data
Streaming <REPLACE_DRIVER_SPECIFIC_URL_2(p2p_streaming)>`__
documentation in the *NI Signal Generators Help* for more information.
''',
},
            },
        ],
'documentation': {
'description': 'Enables a peer-to-peer data stream using manual flow control.',
},
    },
    'QueryArbSeqCapabilities': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'out',
                'name': 'maximumNumberOfSequences',
                'type': 'ViInt32',
'documentation': {
'description': '''
Returns the maximum number of arbitrary waveform sequences that the
signal generator allows. NI-FGEN obtains this value from the
NIFGEN_ATTR_MAX_NUM_SEQUENCES attribute.
''',
},
            },
            {
                'direction': 'out',
                'name': 'minimumSequenceLength',
                'type': 'ViInt32',
'documentation': {
'description': '''
Returns the minimum number of arbitrary waveforms the signal generator
allows in a sequence. NI-FGEN obtains this value from the
NIFGEN_ATTR_MIN_SEQUENCE_LENGTH attribute.
''',
},
            },
            {
                'direction': 'out',
                'name': 'maximumSequenceLength',
                'type': 'ViInt32',
'documentation': {
'description': '''
Returns the maximum number of arbitrary waveforms the signal generator
allows in a sequence. NI-FGEN obtains this value from the
NIFGEN_ATTR_MAX_SEQUENCE_LENGTH attribute.
''',
},
            },
            {
                'direction': 'out',
                'name': 'maximumLoopCount',
                'type': 'ViInt32',
'documentation': {
'description': '''
Returns the maximum number of times the signal generator can repeat an
arbitrary waveform in a sequence. NI-FGEN obtains this value from the
NIFGEN_ATTR_MAX_LOOP_COUNT attribute.
''',
},
            },
        ],
'documentation': {
'description': '''
Returns the attributes of the signal generator that are related to
creating arbitrary sequences (the NIFGEN_ATTR_MAX_NUM_SEQUENCES,
NIFGEN_ATTR_MIN_SEQUENCE_LENGTH,
NIFGEN_ATTR_MAX_SEQUENCE_LENGTH, and NIFGEN_ATTR_MAX_LOOP_COUNT
attributes).
''',
},
    },
    'QueryArbWfmCapabilities': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'out',
                'name': 'maximumNumberOfWaveforms',
                'type': 'ViInt32',
'documentation': {
'description': '''
Returns the maximum number of arbitrary waveforms that the signal
generator allows. NI-FGEN obtains this value from the
NIFGEN_ATTR_MAX_NUM_WAVEFORMS attribute.
''',
},
            },
            {
                'direction': 'out',
                'name': 'waveformQuantum',
                'type': 'ViInt32',
'documentation': {
'description': '''
The size (number of points) of each waveform must be a multiple of a
constant quantum value. This parameter obtains the quantum value that
the signal generator uses. NI-FGEN returns this value from the
NIFGEN_ATTR_WAVEFORM_QUANTUM attribute.

For example, when this attribute returns a value of 8, all waveform
sizes must be a multiple of 8.
''',
},
            },
            {
                'direction': 'out',
                'name': 'minimumWaveformSize',
                'type': 'ViInt32',
'documentation': {
'description': '''
Returns the minimum number of points that the signal generator allows in
a waveform. NI-FGEN obtains this value from the
NIFGEN_ATTR_MIN_WAVEFORM_SIZE attribute.
''',
},
            },
            {
                'direction': 'out',
                'name': 'maximumWaveformSize',
                'type': 'ViInt32',
'documentation': {
'description': '''
Returns the maximum number of points that the signal generator allows in
a waveform. NI-FGEN obtains this value from the
NIFGEN_ATTR_MAX_WAVEFORM_SIZE attribute.
''',
},
            },
        ],
'documentation': {
'description': '''
Returns the attributes of the signal generator that are related to
creating arbitrary waveforms. These attributes are the maximum number of
waveforms, waveform quantum, minimum waveform size, and maximum waveform
size.
''',
'note': '''
If you do not want to obtain the waveform quantum, pass a value of
VI_NULL for this parameter.
''',
},
    },
    'QueryFreqListCapabilities': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'out',
                'name': 'maximumNumberOfFreqLists',
                'type': 'ViInt32',
'documentation': {
'description': '''
Returns the maximum number of frequency lists that the signal generator
allows. NI-FGEN obtains this value from the
NIFGEN_ATTR_MAX_NUM_FREQ_LISTS attribute.
''',
},
            },
            {
                'direction': 'out',
                'name': 'minimumFrequencyListLength',
                'type': 'ViInt32',
'documentation': {
'description': '''
Returns the minimum number of steps that the signal generator allows in
a frequency list. NI-FGEN obtains this value from the
NIFGEN_ATTR_MIN_FREQ_LIST_LENGTH attribute.
''',
},
            },
            {
                'direction': 'out',
                'name': 'maximumFrequencyListLength',
                'type': 'ViInt32',
'documentation': {
'description': '''
Returns the maximum number of steps that the signal generator allows in
a frequency list. NI-FGEN obtains this value from the
NIFGEN_ATTR_MAX_FREQ_LIST_LENGTH attribute.
''',
},
            },
            {
                'direction': 'out',
                'name': 'minimumFrequencyListDuration',
                'type': 'ViReal64',
'documentation': {
'description': '''
Returns the minimum duration that the signal generator allows in a step
of a frequency list. NI-FGEN obtains this value from the
NIFGEN_ATTR_MIN_FREQ_LIST_DURATION attribute.
''',
},
            },
            {
                'direction': 'out',
                'name': 'maximumFrequencyListDuration',
                'type': 'ViReal64',
'documentation': {
'description': '''
Returns the maximum duration that the signal generator allows in a step
of a frequency list. NI-FGEN obtains this value from the
NIFGEN_ATTR_MAX_FREQ_LIST_DURATION attribute.
''',
},
            },
            {
                'direction': 'out',
                'name': 'frequencyListDurationQuantum',
                'type': 'ViReal64',
'documentation': {
'description': '''
Returns the quantum of which all durations must be a multiple in a
frequency list. NI-FGEN obtains this value from the
NIFGEN_ATTR_FREQ_LIST_DURATION_QUANTUM attribute.
''',
},
            },
        ],
'documentation': {
'description': '''
Returns the attributes of the signal generator that are related to
creating frequency lists. These attributes are
NIFGEN_ATTR_MAX_NUM_FREQ_LISTS,
NIFGEN_ATTR_MIN_FREQ_LIST_LENGTH,
NIFGEN_ATTR_MAX_FREQ_LIST_LENGTH,
NIFGEN_ATTR_MIN_FREQ_LIST_DURATION,
NIFGEN_ATTR_MAX_FREQ_LIST_DURATION, and
NIFGEN_ATTR_FREQ_LIST_DURATION_QUANTUM.
''',
},
    },
    'ReadCalADC': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
nifgen_init or the nifgen_InitExtCal function and identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'numberOfReadsToAverage',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the number of measurements to be taken and averaged to
determine the return value.
''',
},
            },
            {
                'direction': 'in',
                'name': 'returnCalibratedValue',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether the voltage returned from the ADC should be adjusted
to account for the gain and offset of the ADC.
''',
},
            },
            {
                'direction': 'out',
                'name': 'calAdcValue',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the average of the voltage measurements taken from the onboard
calibration ADC.
''',
},
            },
        ],
'documentation': {
'description': '''
Takes one or more voltage measurements from the onboard calibration ADC
and returns the value or the average value. The signal that the ADC
actually measures can be specified using the
NIFGEN_ATTR_CAL_ADC_INPUT attribute. The ADC has some inherent gain
and offset. These values can be determined during an external
calibration session and stored in the calibration EEPROM.

If the **returnCalibratedValue** parameter is VI_TRUE, NI-FGEN adjusts
the value that is returned to account for the gain and offset of the
ADC. Otherwise, the raw voltage value reported by the ADC is returned.
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
Identifies your instrument session. **vi** is obtained from the
nifgen_init or the nifgen_InitExtCal function and identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'out',
                'name': 'Temperature',
                'type': 'ViReal64',
'documentation': {
'description': '''
Returns the current temperature read from onboard temperature sensors,
in degrees Celsius.
''',
},
            },
        ],
'documentation': {
'description': '''
Reads the current onboard temperature of the device. The temperature is
returned in degrees Celsius.
''',
},
    },
    'ResetAttribute': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the name of the channel on which to check the attribute value
if the attribute is channel-based. If the attribute is not
channel-based, then pass VI_NULL or an empty string ("").

**Default Value**: "" (empty string)
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'Specifies the ID of an attribute.',
},
            },
        ],
'documentation': {
'description': 'Resets the attribute to its default value.',
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
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
        ],
'documentation': {
'description': '''
Performs a hard reset on the device. Generation is stopped, all routes
are released, external bidirectional terminals are tristated, FPGAs are
reset, hardware is configured to its default state, and all session
attributes are reset to their default states.
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
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
        ],
'documentation': {
'description': '''
This function tests the current test module for dependencies on the
operation of previously executed test modules. If your module depends on
the operation of previous modules, your test system has less
flexibility.

When developing a complex test system that consists of multiple test
modules, NI recommends that you design the test modules so that they can
run in any order. To do so, ensure that each test module completely
configures the state of each instrument it uses. If a particular test
module does not completely configure the state of an instrument, the
state of the instrument depends on the configuration from a previously
executed test module. If you execute the test modules in a different
order, the behavior of the instrument and the test module may change.
This change in behavior is generally instrument specific and represents
an interchangeability problem.

After you call this function, the interchangeability checking algorithms
in the specific driver ignore all previous configuration operations. By
calling this function at the beginning of a test module, you can
determine whether the test module has dependencies on the operation of
previously executed test modules.

This function does not clear the interchangeability warnings from the
list of previously recorded interchangeability warnings. If you want to
guarantee that the nifgen_GetNextInterchangeWarning function only
returns those interchangeability warnings that are generated after
calling this function, you must clear the list of interchangeability
warnings. You can clear the interchangeability warnings list by
repeatedly calling the niFgen_GetNextInterchangeWarning function until
no more interchangeability warnings are returned. If you are not
interested in the content of those warnings, you can call the
nifgen_ClearInterchangeWarnings function.
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
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
        ],
'documentation': {
'description': '''
Resets the instrument and reapplies initial user–specified settings from
the logical name that was used to initialize the session. If the session
was created without a logical name, this function is equivalent to the
nifgen_reset function.
''',
},
    },
    'RestoreLastExtCalConstants': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
nifgen_InitExtCal function and identifies a particular instrument
session.
''',
},
            },
        ],
'documentation': {
'description': '''
Overwrites the current calibration constants with those from the last
successful external calibration. This action effectively undoes any
self-calibrations performed since the last time an external calibration
was performed. This function should be used if a self-calibration
produced invalid calibration constants.
''',
},
    },
    'RouteSignalOut': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the channel name for which you want to route a signal.

**Default Value**: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'routeSignalFrom',
                'type': 'ViInt32',
'documentation': {
'description': '''
Various signals can be routed out the RTSI lines.

****Defined Values****
''',
'table_body': [['NIFGEN_VAL_NONE', 'Nothing Sending this value clears the line.'], ['NIFGEN_VAL_MARKER', 'Marker Event'], ['NIFGEN_VAL_SYNC_OUT', 'SYNC signal This signal normally appears on the SYNC OUT front panel connector.'], ['NIFGEN_VAL_OUT_START_TRIGGER', 'Start Trigger The Start Trigger is normally generated at the start of the sequence. Call the nifgen_ConfigureTriggerSource function to receive this trigger.'], ['NIFGEN_VAL_BOARD_CLOCK', 'Signal generator board clock The signal generator board clock is 20 MHz for the NI PCI-5401/5411/5431. The NI PXI-5404 has a 20 MHz board clock, and the NI PXI-5421 has integer divisors of 100 MHz. The NI PXI-5401/5411/5431 does not support routing a Board Clock to RTSI lines or front panel connectors.'], ['NIFGEN_VAL_SYNCHRONIZATION', 'Synchronization strobe A synchronization strobe is used to guarantee absolute synchronization between two or more signal generators. Call the nifgen_ConfigureSynchronization function to receive the strobe.'], ['NIFGEN_VAL_SOFTWARE_TRIG', 'Software trigger'], ['NIFGEN_VAL_OUT_UPDATE', '—'], ['NIFGEN_VAL_REF_OUT', 'Reference Clock out front panel connector'], ['NIFGEN_VAL_PXI_CLK10', 'PXI 10 MHz backplane Reference Clock'], ['NIFGEN_VAL_PXI_STAR', 'PXI star trigger line'], ['NIFGEN_VAL_PFI_0', 'PFI 0'], ['NIFGEN_VAL_RTSI_0', 'RTSI 0 or PXI_Trig 0'], ['NIFGEN_VAL_RTSI_1', 'RTSI 1 or PXI_Trig 1'], ['NIFGEN_VAL_RTSI_2', 'RTSI 2 or PXI_Trig 2'], ['NIFGEN_VAL_RTSI_3', 'RTSI 3 or PXI_Trig 3'], ['NIFGEN_VAL_RTSI_4', 'RTSI 4 or PXI_Trig 4'], ['NIFGEN_VAL_RTSI_5', 'RTSI 5 or PXI_Trig 5'], ['NIFGEN_VAL_RTSI_6', 'RTSI 6 or PXI_Trig 6'], ['NIFGEN_VAL_RTSI_7', 'RTSI 7 or PXI_Trig 7'], ['NIFGEN_VAL_REF_CLOCK_RTSI_CLOCK', 'RTSI clock'], ['NIFGEN_VAL_ONBOARD_REFERENCE_CLOCK', 'Onboard Reference Clock'], ['NIFGEN_VAL_UPDATE_CLOCK', 'Sample Clock'], ['NIFGEN_VAL_PLL_REF_SOURCE', 'PLL Reference Clock']],
},
            },
            {
                'direction': 'in',
                'name': 'routeSignalTo',
                'type': 'ViInt32',
'documentation': {
'description': '''
The possible RTSI lines to which you can route a signal.

****Defined Values****
''',
'table_body': [['NIFGEN_VAL_RTSI_0', 'RTSI 0 or PXI_Trig 0'], ['NIFGEN_VAL_RTSI_1', 'RTSI 1 or PXI_Trig 1'], ['NIFGEN_VAL_RTSI_2', 'RTSI 2 or PXI_Trig 2'], ['NIFGEN_VAL_RTSI_3', 'RTSI 3 or PXI_Trig 3'], ['NIFGEN_VAL_RTSI_4', 'RTSI 4 or PXI_Trig 4'], ['NIFGEN_VAL_RTSI_5', 'RTSI 5 or PXI_Trig 5'], ['NIFGEN_VAL_RTSI_6', 'RTSI 6 or PXI_Trig 6'], ['NIFGEN_VAL_RTSI_7', 'RTSI 7 or PXI_Trig 7'], ['NIFGEN_VAL_REF_CLOCK_RTSI_CLOCK', 'RTSI clock'], ['NIFGEN_VAL_REF_OUT', 'Reference Clock out front panel connector'], ['NIFGEN_VAL_PFI_0', 'PFI 0'], ['NIFGEN_VAL_PFI_1', 'PFI 1'], ['NIFGEN_VAL_PFI_4', 'PFI 4'], ['NIFGEN_VAL_PFI_5', 'PFI 5'], ['NIFGEN_VAL_PXI_STAR', 'PXI star trigger line'], ['NIFGEN_VAL_PXI_CLK10', 'PXI 10 MHz backplane Reference Clock']],
},
            },
        ],
'documentation': {
'description': '''
Routes various signals in the signal generator to the RTSI lines and
front panel terminals.
''',
'note': '''
The signal generator must not be in the Generating state when you call
this function.
''',
'table_body': [[' ', 'You can clear a previously routed signal by routing NIFGEN_VAL_NONE to the destination terminal.']],
},
    },
    'SelfCal': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init or the nifgen_InitWithOptions functions and identifies a
particular instrument session.
''',
},
            },
        ],
'documentation': {
'description': '''
Performs a full internal self-calibration on the device. If the
calibration is successful, new calibration data and constants are stored
in the onboard EEPROM.
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
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Trigger',
                'type': 'ViInt32',
'documentation': {
'description': '''
Sets the clock mode of the signal generator.

****Defined Values****
''',
'table_body': [['NIFGEN_VAL_DIVIDE_DOWN'], ['NIFGEN_VAL_HIGH_RESOLUTION'], ['NIFGEN_VAL_AUTOMATIC']],
},
            },
            {
                'direction': 'in',
                'name': 'triggerId',
                'type': 'ViString',

            },
        ],
'documentation': {
'description': '''
Sends a command to trigger the signal generator. This VI can act as an
override for an external edge trigger.
''',
'note': '''
This VI does not override external digital edge triggers of the
NI 5401/5411/5431.
''',
},
    },
    'SendSoftwareTrigger': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
        ],
'documentation': {
'description': 'Sends a command to trigger the signal generator.',
'note': '''
This function can act as an override for an external edge trigger.
However, the NI 5401/5411/5431 do not support overriding an external
digital edge trigger.
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
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the name of the channel on which to check the attribute value
if the attribute is channel-based. If the attribute is not
channel-based, then pass VI_NULL or "" (empty string).

**Default Value**: "" (empty string)
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'Specifies the ID of an attribute.',
},
            },
            {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies the value to which you want to set the attribute. **Default
Value**: None
''',
'note': '''
Some of the values might not be valid depending on the current
settings of the instrument session.
''',
},
            },
        ],
'documentation': {
'description': '''
Sets the value of a ViBoolean attribute.

This is a low-level function that you can use to set the values of
instrument-specific attributes and inherent IVI attributes. If the
attribute represents an instrument state, this function performs
instrument I/O in the following cases:

-  State caching is disabled for the entire session or for the
   particular attribute.
-  State caching is enabled and the currently cached value is invalid or
   is different than the value you specify.

NI-FGEN contains high-level functions that set most of the instrument
attributes. NI recommends that you use the high-level driver functions
as much as possible. They handle order dependencies and multithread
locking for you. In addition, they perform status checking only after
setting all of the attributes. In contrast, when you set multiple
attributes using the Set Attribute functions, the functions check the
instrument status after each call.

Also, when state caching is enabled, the high-level functions that
configure multiple attributes perform instrument I/O only for the
attributes whose value you change. Thus, you can safely call the
high-level functions without the penalty of redundant instrument I/O.
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
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the name of the channel on which to check the attribute value
if the attribute is channel-based. If the attribute is not
channel-based, then pass VI_NULL or "" (empty string).

**Default Value**: "" (empty string)
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'Specifies the ID of an attribute.',
},
            },
            {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the value to which you want to set the attribute. **Default
Value**: None
''',
'note': '''
Some of the values might not be valid depending on the current
settings of the instrument session.
''',
},
            },
        ],
'documentation': {
'description': '''
Sets the value of a ViInt32 attribute.

This is a low-level function that you can use to set the values of
instrument-specific attributes and inherent IVI attributes. If the
attribute represents an instrument state, this function performs
instrument I/O in the following cases:

-  State caching is disabled for the entire session or for the
   particular attribute.
-  State caching is enabled and the currently cached value is invalid or
   is different than the value you specify.

NI-FGEN contains high-level functions that set most of the instrument
attributes. NI recommends that you use the high-level driver functions
as much as possible. They handle order dependencies and multithread
locking for you. In addition, they perform status checking only after
setting all of the attributes. In contrast, when you set multiple
attributes using the Set Attribute functions, the functions check the
instrument status after each call.

Also, when state caching is enabled, the high-level functions that
configure multiple attributes perform instrument I/O only for the
attributes whose value you change. Thus, you can safely call the
high-level functions without the penalty of redundant instrument I/O.
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
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the name of the channel on which to check the attribute value
if the attribute is channel-based. If the attribute is not
channel-based, then pass VI_NULL or "" (empty string).

**Default Value**: "" (empty string)
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'Specifies the ID of an attribute.',
},
            },
            {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViInt64',
'documentation': {
'description': '''
Specifies the value to which you want to set the attribute. **Default
Value**: None
''',
'note': '''
Some of the values might not be valid depending on the current
settings of the instrument session.
''',
},
            },
        ],
'documentation': {
'description': '''
Sets the value of a ViInt64 attribute.

This is a low-level function that you can use to set the values of
instrument-specific attributes and inherent IVI attributes. If the
attribute represents an instrument state, this function performs
instrument I/O in the following cases:

-  State caching is disabled for the entire session or for the
   particular attribute.
-  State caching is enabled and the currently cached value is invalid or
   is different than the value you specify.

NI-FGEN contains high-level functions that set most of the instrument
attributes. NI recommends that you use the high-level driver functions
as much as possible. They handle order dependencies and multithread
locking for you. In addition, they perform status checking only after
setting all of the attributes. In contrast, when you set multiple
attributes using the Set Attribute functions, the functions check the
instrument status after each call.

Also, when state caching is enabled, the high-level functions that
configure multiple attributes perform instrument I/O only for the
attributes whose value you change. Thus, you can safely call the
high-level functions without the penalty of redundant instrument I/O.
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
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the name of the channel on which to check the attribute value
if the attribute is channel-based. If the attribute is not
channel-based, then pass VI_NULL or "" (empty string).

**Default Value**: "" (empty string)
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'Specifies the ID of an attribute.',
},
            },
            {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the value to which you want to set the attribute. **Default
Value**: None
''',
'note': '''
Some of the values might not be valid depending on the current
settings of the instrument session.
''',
},
            },
        ],
'documentation': {
'description': '''
Sets the value of a ViReal64 attribute.

This is a low-level function that you can use to set the values of
instrument-specific attributes and inherent IVI attributes. If the
attribute represents an instrument state, this function performs
instrument I/O in the following cases:

-  State caching is disabled for the entire session or for the
   particular attribute.
-  State caching is enabled and the currently cached value is invalid or
   is different than the value you specify.

NI-FGEN contains high-level functions that set most of the instrument
attributes. NI recommends that you use the high-level driver functions
as much as possible. They handle order dependencies and multithread
locking for you. In addition, they perform status checking only after
setting all of the attributes. In contrast, when you set multiple
attributes using the Set Attribute functions, the functions check the
instrument status after each call.

Also, when state caching is enabled, the high-level functions that
configure multiple attributes perform instrument I/O only for the
attributes whose value you change. Thus, you can safely call the
high-level functions without the penalty of redundant instrument I/O.
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
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the name of the channel on which to check the attribute value
if the attribute is channel-based. If the attribute is not
channel-based, then pass VI_NULL or an empty string ("").

**Default Value**: "" (empty string)
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'Specifies the ID of an attribute.',
},
            },
            {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViSession',
'documentation': {
'description': '''
Specifies the value to which you want to set the attribute. **Default
Value**: None
''',
'note': '''
Some of the values might not be valid depending on the current
settings of the instrument session.
''',
},
            },
        ],
'documentation': {
'description': '''
Sets the value of a ViSession attribute.

This is a low-level function that you can use to set the values of
instrument-specific attributes and inherent IVI attributes. If the
attribute represents an instrument state, this function performs
instrument I/O in the following cases:

-  State caching is disabled for the entire session or for the
   particular attribute.
-  State caching is enabled and the currently cached value is invalid or
   is different than the value you specify.

NI-FGEN contains high-level functions that set most of the instrument
attributes. It is best to use the high-level driver functions as much as
possible. They handle order dependencies and multithread locking for
you. In addition, they perform status checking only after setting all of
the attributes. In contrast, when you set multiple attributes using the
Set Attribute functions, the functions check the instrument status after
each call.

Also, when state caching is enabled, the high-level functions that
configure multiple attributes perform instrument I/O only for the
attributes whose value you change. Thus, you can safely call the
high-level functions without the penalty of redundant instrument I/O.
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
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the name of the channel on which to check the attribute value
if the attribute is channel-based. If the attribute is not
channel-based, then pass VI_NULL or "" (empty string).

**Default Value**: "" (empty string)
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'Specifies the ID of an attribute.',
},
            },
            {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the value to which you want to set the attribute. **Default
Value**: None
''',
'note': '''
Some of the values might not be valid depending on the current
settings of the instrument session.
''',
},
            },
        ],
'documentation': {
'description': '''
Sets the value of a ViString attribute.

This is a low-level function that you can use to set the values of
instrument-specific attributes and inherent IVI attributes. If the
attribute represents an instrument state, this function performs
instrument I/O in the following cases:

-  State caching is disabled for the entire session or for the
   particular attribute.
-  State caching is enabled and the currently cached value is invalid or
   is different than the value you specify.

NI-FGEN contains high-level functions that set most of the instrument
attributes. NI recommends that you use the high-level driver functions
as much as possible. They handle order dependencies and multithread
locking for you. In addition, they perform status checking only after
setting all of the attributes. In contrast, when you set multiple
attributes using the Set Attribute functions, the functions check the
instrument status after each call.

Also, when state caching is enabled, the high-level functions that
configure multiple attributes perform instrument I/O only for the
attributes whose value you change. Thus, you can safely call the
high-level functions without the penalty of redundant instrument I/O.
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
Identifies your instrument session. **vi** is obtained from the
nifgen_init or the nifgen_InitExtCal function and identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Info',
                'type': 'ViConstString',
'documentation': {
'description': 'Specifies the information string that should be stored in the EEPROM.',
},
            },
        ],
'documentation': {
'description': '''
Stores user-defined information in the onboard EEPROM. Call the
nifgen_GetCalUserDefinedInfoMaxSize function to determine the maximum
number of characters that can be stored.
''',
},
    },
    'SetNamedWaveformNextWritePosition': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the channel onto which the waveform data should be loaded.

**Default Value**: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'waveformName',
                'type': 'ViConstString',
'documentation': {
'description': 'Specifies the name to associate with the allocated waveform.',
},
            },
            {
                'direction': 'in',
                'name': 'relativeTo',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the reference position in the waveform. This position and
**offset** together determine where to start loading data into the
waveform.

****Defined Values****
''',
'table_body': [['NIFGEN_VAL_WAVEFORM_POSITION_START (0)', 'Use the start of the waveform as the reference position.'], ['NIFGEN_VAL_WAVEFORM_POSITION_CURRENT (1)', 'Use the current position within the waveform as the reference position.']],
},
            },
            {
                'direction': 'in',
                'name': 'offset',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the offset from the **relativeTo** parameter at which to start
loading the data into the waveform.
''',
},
            },
        ],
'documentation': {
'description': '''
Sets the position in the waveform to which data is written at the next
write. This function allows you to write to arbitrary locations within
the waveform. These settings apply only to the next write to the
waveform specified by the **waveformHandle** parameter. Subsequent
writes to that waveform begin where the last write left off, unless this
function is called again. The **waveformHandle** passed in must have
been created with a call to one of the following functions:

-  nifgen_AllocateWaveform
-  nifgen_CreateWaveformF64
-  nifgen_CreateWaveformI16
-  nifgen_CreateWaveformFromFileI16
-  nifgen_CreateWaveformFromFileF64
-  nifgen_CreateWaveformFromFileHWS
''',
},
    },
    'SetWaveformNextWritePosition': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the channel on which to the waveform data should be loaded.

**Default Value**: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'waveformHandle',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the handle of the arbitrary waveform previously allocated with
the nifgen_AllocateWaveform function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'relativeTo',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the reference position in the waveform. This position and
**offset** together determine where to start loading data into the
waveform.

****Defined Values****
''',
'table_body': [['NIFGEN_VAL_WAVEFORM_POSITION_START (0)', 'Use the start of the waveform as the reference position.'], ['NIFGEN_VAL_WAVEFORM_POSITION_CURRENT (1)', 'Use the current position within the waveform as the reference position.']],
},
            },
            {
                'direction': 'in',
                'name': 'offset',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the offset from **relativeTo** at which to start loading the
data into the waveform.
''',
},
            },
        ],
'documentation': {
'description': '''
Sets the position in the waveform at which the next waveform data is
written. This function allows you to write to arbitrary locations within
the waveform. These settings apply only to the next write to the
waveform specified by the waveformHandle parameter. Subsequent writes to
that waveform begin where the last write left off, unless this function
is called again. The waveformHandle passed in must have been created by
a call to the nifgen_AllocateWaveform function or one of the following
niFgen CreateWaveform functions:

-  nifgen_CreateWaveformF64
-  nifgen_CreateWaveformI16
-  nifgen_CreateWaveformFromFileI16
-  nifgen_CreateWaveformFromFileF64
-  nifgen_CreateWaveformFromFileHWS
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
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'out',
                'name': 'callerHasLock',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Keeps track of whether you obtain a lock and therefore need to unlock
the session.

This parameter serves as a convenience. If you do not want to use this
parameter, pass VI_NULL.

Pass the address of a local ViBoolean variable. In the declaration of
the local variable, initialize it to VI_FALSE. Pass the address of the
same local variable to any other calls you make to the
niFgen_LockSession function or the niFgen_UnlockSession function in
the same function.

The parameter is an input/output parameter. The niFgen_LockSession
function and the niFgen_UnlockSession function each inspect the current
value and take the following actions:

-  If the value is VI_TRUE, the niFgen_LockSession function does not
   lock the session again. If the value is VI_FALSE, the
   niFgen_LockSession function obtains the lock and sets the value of
   the parameter to VI_TRUE.
-  If the value is VI_FALSE, the niFgen_UnlockSession function does
   not attempt to unlock the session. If the value is VI_TRUE, the
   niFgen_UnlockSession function releases the lock and sets the value
   of the parameter to VI_FALSE.

Thus, you can, call the niFgen_UnlockSession function at the end of
your function without worrying about whether you actually have the lock.

Example:

ViStatus TestFunc (ViSession vi, ViInt32 flags)
{

ViStatus error = VI_SUCCESS;
ViBoolean haveLock = VI_FALSE;
if (flags & BIT_1)
{

viCheckErr(niFgen_LockSession(vi, &haveLock;));
viCheckErr( TakeAction1(vi));
if (flags & BIT_2)
{

viCheckErr( niFgen_UnlockSession(vi, &haveLock;));
viCheckErr( TakeAction2(vi));
viCheckErr( niFgen_LockSession(vi, &haveLock;);

}
if (flags & BIT_3)

 viCheckErr( TakeAction3(vi));

}

Error:

| 

/\*
At this point, you cannot really be sure that
you have the lock. Fortunately, the haveLock
variable takes care of that for you.
\*/
niFgen_UnlockSession(vi, &haveLock;);
return error;

}
''',
},
            },
        ],
'documentation': {
'description': '''
Releases a lock that you acquired on an instrument session using the
nifgen_LockSession function.
''',
},
    },
    'WaitUntilDone': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'maxTime',
                'type': 'ViInt32',
'documentation': {
'description': 'Specifies the timeout value in milliseconds.',
},
            },
        ],
'documentation': {
'description': '''
Waits until the device is done generating or until the maximum time has
expired.
''',
},
    },
    'WriteBinary16AnalogStaticValue': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
nifgen_InitExtCal function and identifies a particular instrument
session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the channel name for which you want to write the value.

**Default Value**: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'Value',
                'type': 'ViInt16',
'documentation': {
'description': 'The value to write.',
},
            },
        ],
'documentation': {
'description': '''
| Writes the 16-bit value to the DAC, which could be output as a DC
  Voltage.
| This function writes to the DAC only when in an external calibration
  session.
''',
},
    },
    'WriteBinary16Waveform': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the channel on which to the waveform data should be loaded.

**Default Value**: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'waveformHandle',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the handle of the arbitrary waveform previously allocated with
the nifgen_AllocateWaveform function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Size',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the number of samples to load into the waveform.

**Default Value**: 0
''',
},
            },
            {
                'direction': 'in',
                'name': 'Data',
                'type': 'ViInt16[]',
'documentation': {
'description': '''
Specifies the array of data to load into the waveform. The array must
have at least as many elements as the value in **size**. The binary data
is left-justified.
''',
},
            },
        ],
'documentation': {
'description': '''
Writes binary data to the waveform in onboard memory. The waveform
handle passed must have been created by a call to the
nifgen_AllocateWaveform or the nifgen_CreateWaveformI16 function.

By default, the subsequent call to the niFgen_WriteBinary16Waveform
function continues writing data from the position of the last sample
written. You can set the write position and offset by calling the
nifgen_SetWaveformNextWritePosition function. If streaming is enabled,
you can write more data than the allocated waveform size in onboard
memory. Refer to the
`Streaming <REPLACE_DRIVER_SPECIFIC_URL_2(streaming)>`__ topic for more
information about streaming data.
''',
},
    },
    'WriteComplexBinary16Waveform': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies channel on which to the waveform data should be loaded.

**Default Value**: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'waveformHandle',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the handle of the arbitrary waveform previously allocated with
the nifgen_AllocateWaveform function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Size',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the number of samples to load into the waveform.

**Default Value**: 0
''',
},
            },
            {
                'direction': 'in',
                'name': 'Data',
                'type': 'NIComplexI16[]',
'documentation': {
'description': '''
Specifies the array of data to load into the waveform. The array must
have at least as many elements as the value in **size**. The binary data
is left-justified.
''',
},
            },
        ],
'documentation': {
'description': '''
Writes binary data to the waveform in onboard memory. The waveform
handle passed in must have been created by a call to the
nifgen_AllocateWaveform or the nifgen_CreateWaveformI16 function.

By default, the subsequent call to the
niFgen_WriteComplexBinary16Waveform function continues writing data
from the position of the last sample written. You can set the write
position and offset by calling the nifgen_SetWaveformNextWritePosition
function. If streaming is enabled, you can write more data than the
allocated waveform size in onboard memory. Refer to the
`Streaming <REPLACE_DRIVER_SPECIFIC_URL_2(streaming)>`__ topic for more
information about streaming data.
''',
},
    },
    'WriteNamedWaveformComplexF64': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the channel onto which the waveform data should be loaded.

**Default Value**: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'waveformName',
                'type': 'ViConstString',
'documentation': {
'description': 'Specifies the name to associate with the allocated waveform.',
},
            },
            {
                'direction': 'in',
                'name': 'Size',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the number of samples to load into the waveform.

**Default Value**: 0
''',
},
            },
            {
                'direction': 'in',
                'name': 'Data',
                'type': 'NIComplexNumber[]',
'documentation': {
'description': '''
Specifies the array of data to load into the waveform. The array must
have at least as many elements as the value in **size**.
''',
},
            },
        ],
'documentation': {
'description': '''
Writes complex floating–point data to the named waveform in onboard
memory on devices with the NIFGEN_ATTR_OSP_ENABLED attribute set to
VI_TRUE and the NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE attribute set
to NIFGEN_VAL_OSP_COMPLEX. The waveform handle passed in must have
been created by a call to the nifgen_AllocateWaveform function or to
one of the following niFgen Create Waveform functions:

-  nifgen_CreateWaveformF64
-  nifgen_CreateWaveformI16
-  nifgen_CreateWaveformFromFileI16
-  nifgen_CreateWaveformFromFileF64
-  nifgen_CreateWaveformFromFileHWS

By default, the subsequent call to the
niFgen_WriteNamedWaveformComplexF64 function continues writing data
from the position of the last sample written. You can set the write
position and offset by calling the
nifgen_SetNamedWaveformNextWritePosition function. If streaming is
enabled, you can write more data than the allocated waveform size in
onboard memory. Refer to the
`Streaming <REPLACE_DRIVER_SPECIFIC_URL_2(streaming)>`__ topic for more
information about streaming data.
''',
},
    },
    'WriteNamedWaveformComplexI16': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the channel onto which the waveform data should be loaded.

**Default Value**: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'waveformName',
                'type': 'ViConstString',
'documentation': {
'description': 'Specifies the name to associate with the allocated waveform.',
},
            },
            {
                'direction': 'in',
                'name': 'Size',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the number of samples to load into the waveform.

**Default Value**: 0
''',
},
            },
            {
                'direction': 'in',
                'name': 'Data',
                'type': 'NIComplexI16[]',
'documentation': {
'description': '''
Specifies the array of data to load into the waveform. The array must
have at least as many elements as the value in **size**.
''',
},
            },
        ],
'documentation': {
'description': '''
Writes complex binary data to the named waveform in onboard memory on
devices with the NIFGEN_ATTR_OSP_ENABLED attribute set to VI_TRUE
and the NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE attribute set to
NIFGEN_VAL_OSP_COMPLEX. The waveform handle passed in must have been
created by a call to the nifgen_AllocateWaveform function or to one of
the following niFgen Create Waveform functions:

-  nifgen_CreateWaveformF64
-  nifgen_CreateWaveformI16
-  nifgen_CreateWaveformFromFileI16
-  nifgen_CreateWaveformFromFileF64
-  nifgen_CreateWaveformFromFileHWS

By default, the subsequent call to the
niFgen_WriteNamedWaveformComplexi16 function continues writing data
from the position of the last sample written. You can set the write
position and offset by calling the
nifgen_SetNamedWaveformNextWritePosition function. If streaming is
enabled, you can write more data than the allocated waveform size in
onboard memory. Refer to the
`Streaming <REPLACE_DRIVER_SPECIFIC_URL_2(streaming)>`__ topic for more
information about streaming data.
''',
},
    },
    'WriteNamedWaveformF64': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the channel onto which the waveform data should be loaded.

**Default Value**: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'waveformName',
                'type': 'ViConstString',
'documentation': {
'description': 'Specifies the name to associate with the allocated waveform.',
},
            },
            {
                'direction': 'in',
                'name': 'Size',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the number of samples to load into the waveform.

**Default Value**: 0
''',
},
            },
            {
                'direction': 'in',
                'name': 'Data',
                'type': 'ViReal64[]',
'documentation': {
'description': '''
Specifies the array of data to load into the waveform. The array must
have at least as many elements as the value in **size**.
''',
},
            },
        ],
'documentation': {
'description': '''
Writes floating-point data to the waveform in onboard memory. The
waveform handle passed in must have been created by a call to the
nifgen_AllocateWaveform function or to one of the following niFgen
Create Waveform functions:

-  nifgen_CreateWaveformF64
-  nifgen_CreateWaveformI16
-  nifgen_CreateWaveformFromFileI16
-  nifgen_CreateWaveformFromFileF64
-  nifgen_CreateWaveformFromFileHWS

By default, the subsequent call to the niFgen_WriteNamedWaveformF64
function continues writing data from the position of the last sample
written. You can set the write position and offset by calling the
nifgen_SetNamedWaveformNextWritePosition function. If streaming is
enabled, you can write more data than the allocated waveform size in
onboard memory. Refer to the
`Streaming <REPLACE_DRIVER_SPECIFIC_URL_2(streaming)>`__ topic for more
information about streaming data.
''',
},
    },
    'WriteNamedWaveformI16': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the channel onto which the waveform data should be loaded.

**Default Value**: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'waveformName',
                'type': 'ViConstString',
'documentation': {
'description': 'Specifies the name to associate with the allocated waveform.',
},
            },
            {
                'direction': 'in',
                'name': 'Size',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the number of samples to load into the waveform.

**Default Value**: 0
''',
},
            },
            {
                'direction': 'in',
                'name': 'Data',
                'type': 'ViInt16[]',
'documentation': {
'description': '''
Specifies the array of data to load into the waveform. The array must
have at least as many elements as the value in **size**.
''',
},
            },
        ],
'documentation': {
'description': '''
Writes binary data to the named waveform in onboard memory.

By default, the subsequent call to the niFgen_WriteNamedWaveformI16
function continues writing data from the position of the last sample
written. You can set the write position and offset by calling the
nifgen_SetNamedWaveformNextWritePosition function. If streaming is
enabled, you can write more data than the allocated waveform size in
onboard memory. Refer to the
`Streaming <REPLACE_DRIVER_SPECIFIC_URL_2(streaming)>`__ topic for more
information about streaming data.
''',
},
    },
    'WriteP2PEndpointI16': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'endpointName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the name of the FIFO endpoint. Data is written to the endpoint
FIFO.
''',
},
            },
            {
                'direction': 'in',
                'name': 'numberOfSamples',
                'type': 'ViInt32',
'documentation': {
'description': 'Specifies the number of samples to write into the endpoint FIFO.',
},
            },
            {
                'direction': 'in',
                'name': 'endpointData',
                'type': 'ViInt16[]',
'documentation': {
'description': '''
Specifies the array of data to write into the endpoint FIFO. The binary
data is left-justified.
''',
},
            },
        ],
'documentation': {
'description': '''
Writes I16 data to the peer-to-peer endpoint. Use this function to write
initial data from the host to the endpoint before starting generation to
avoid an underflow at start.
''',
},
    },
    'WriteScript': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the channel on which the script is loaded.

**Default Value**: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'Script',
                'type': 'ViConstString',
'documentation': {
'description': '''
Contains the text of the script you want to use for your generation
operation. Refer to `scripting
Instructions <REPLACE_DRIVER_SPECIFIC_URL_2(niscripted.chm',%20'scripting_instructions)>`__
for more information about writing scripts.
''',
},
            },
        ],
'documentation': {
'description': '''
Writes a string containing one or more scripts that govern the
generation of waveforms.
''',
},
    },
    'WriteWaveform': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
The channel onto which the waveform data should be loaded.

**Default Value**: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'waveformHandle',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the handle of the arbitrary waveform previously allocated with
the nifgen_AllocateWaveform function.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Size',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the number of samples to load into the waveform.

**Default Value**: 0
''',
},
            },
            {
                'direction': 'in',
                'name': 'Data',
                'type': 'ViReal64[]',
'documentation': {
'description': '''
Specifies the array of data to load into the waveform. The array must
have at least as many elements as the value in **size**.
''',
},
            },
        ],
'documentation': {
'description': '''
Writes floating-point data to the waveform in onboard memory. The
waveform handle passed in must have been created by a call to the
nifgen_AllocateWaveform function or one of the following niFgen
CreateWaveform functions:

-  nifgen_CreateWaveformF64
-  nifgen_CreateWaveformI16
-  nifgen_CreateWaveformFromFileI16
-  nifgen_CreateWaveformFromFileF64
-  nifgen_CreateWaveformFromFileHWS

By default, the subsequent call to the niFgen_WriteWaveform function
continues writing data from the position of the last sample written. You
can set the write position and offset by calling the
nifgen_SetWaveformNextWritePosition function. If streaming is enabled,
you can write more data than the allocated waveform size in onboard
memory. Refer to the
`Streaming <REPLACE_DRIVER_SPECIFIC_URL_2(streaming)>`__ topic for more
information about streaming data.
''',
},
    },
    'WriteWaveformComplexF64': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the channel onto which the waveform data should be loaded.

**Default Value**: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'numberOfSamples',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the number of samples to load into the waveform.
**Default Value**: 0
''',
},
            },
            {
                'direction': 'in',
                'name': 'Data',
                'type': 'NIComplexNumber[]',
'documentation': {
'description': '''
Specifies the array of data to load into the waveform. You must
normalize the data points in the array to be between –1.00 and +1.00.
The array must have at least as many elements as the value in the
**numberOfSamples** parameter.
''',
},
            },
            {
                'direction': 'in',
                'name': 'waveformHandle',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the handle of the arbitrary waveform previously allocated with
the niFgen_AllocateWaveform function.
''',
},
            },
        ],
'documentation': {
'description': '''
Writes complex data to the waveform in onboard memory on devices with
the NIFGEN_ATTR_OUTPUT_ENABLED attribute set to VI_TRUE and the
NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE attribute set to
NIFGEN_VAL_OSP_COMPLEX. The waveform handle passed in must have been
created by a call to the nifgen_AllocateWaveform function or to one of
the following niFgen Create Waveform functions:

-  nifgen_CreateWaveformF64
-  nifgen_CreateWaveformI16
-  nifgen_CreateWaveformFromFileI16
-  nifgen_CreateWaveformFromFileF64
-  nifgen_CreateWaveformFromFileHWS

By default, the subsequent call to the niFgen_WriteWaveformComplexF64
function continues writing data from the position of the last sample
written. You can set the write position and offset by calling the
nifgen_SetWaveformNextWritePosition function. If streaming is enabled,
you can write more data than the allocated waveform size in onboard
memory. Refer to the
`Streaming <REPLACE_DRIVER_SPECIFIC_URL_2(streaming)>`__ topic for more
information about streaming data.
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
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
        ],
'documentation': {
'description': '''
Performs the following operations:

-  Closes the instrument I/O session.
-  Destroys the NI-FGEN session and all of its attributes.
-  Deallocates any memory resources NI-FGEN uses.

Not all signal routes established by calling the nifgen_ExportSignal
and nifgen_RouteSignalOut functions are released when the NI-FGEN
session is closed. The following table shows what happens to a signal
route on your device when you call the niFgen_close function.
''',
'note': '''
After calling niFgen_close, you cannot use NI-FGEN again until you
call the nifgen_init or nifgen_InitWithOptions functions.
''',
'table_body': [['Front Panel', 'Remain connected', 'Remain connected'], ['RTSI/PXI Backplane', 'Remain connected', 'Disconnected']],
'table_header': ['Routes To', 'NI 5401/5411/5431', 'Other Devices'],
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
Identifies your instrument session. **vi** is obtained from the
niFgen_init or the niFgen_InitWithOptions functions and identifies a
particular instrument session.

You can pass VI_NULL for this parameter. Passing VI_NULL is useful
when one of the initialize functions fails.

**Default Value**: VI_NULL
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
NI-FGEN functions.

**Default Value**: 0 (VI_SUCCESS)
''',
},
            },
            {
                'direction': 'out',
                'name': 'errorMessage',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Returns the error message string read from the instrument error message
queue.

You must pass a ViChar array with at least 256 bytes.
''',
},
            },
        ],
'documentation': {
'description': '''
Converts a status code returned by an NI-FGEN function into a
user-readable string.
''',
},
    },
    'error_query': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'out',
                'name': 'errorCode',
                'type': 'ViInt32',
'documentation': {
'description': 'Returns the error code read from the instrument error queue.',
},
            },
            {
                'direction': 'out',
                'name': 'errorMessage',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Returns the error message string read from the instrument error message
queue.

You must pass a ViChar array with at least 256 bytes.
''',
},
            },
        ],
'documentation': {
'description': 'Reads an error code and a message from the instrument error queue.',
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
'caution': '''
Traditional NI-DAQ and NI-DAQmx device names are not case-sensitive.
However, all IVI names, such as logical names, are case-sensitive. If
you use logical names, driver session names, or virtual names in your
program, you must ensure that the name you use matches the name in the
IVI Configuration Store file exactly, without any variations in the case
of the characters.
''',
'description': '''
| Specifies the resource name of the device to initialize.

For Traditional NI-DAQ devices, the syntax is DAQ::\ *n*, where *n* is
the device number assigned by MAX, as shown in Example 1.

For NI-DAQmx devices, the syntax is just the device name specified in
MAX, as shown in Example 2. Typical default names for NI-DAQmx devices
in MAX are Dev1 or PXI1Slot1. You can rename an NI-DAQmx device by
right-clicking on the name in MAX and entering a new name.

An alternate syntax for NI-DAQmx devices consists of DAQ::\ *NI-DAQmx
device name*, as shown in Example 3. This naming convention allows for
the use of an NI-DAQmx device in an application that was originally
designed for a Traditional NI-DAQ device. For example, if the
application expects DAQ::1, you can rename the NI-DAQmx device to 1 in
MAX and pass in DAQ::1 for the resource name, as shown in Example 4.

If you use the DAQ::\ *n* syntax and an NI-DAQmx device name already
exists with that same name, the NI-DAQmx device is matched first.

You can also pass in the name of an IVI logical name or an IVI virtual
name configured with the IVI Configuration utility, as shown in Example
5. A logical name identifies a particular virtual instrument. A virtual
name identifies a specific device and specifies the initial settings for
the session.
''',
'table_body': [['1', 'Traditional NI-DAQ device', 'DAQ::\\ *1*', '(*1* = device number)'], ['2', 'NI-DAQmx device', '*myDAQmxDevice*', '(*myDAQmxDevice* = device name)'], ['3', 'NI-DAQmx device', 'DAQ::\\ *myDAQmxDevice*', '(*myDAQmxDevice* = device name)'], ['4', 'NI-DAQmx device', 'DAQ::\\ *2*', '(*2* = device name)'], ['5', 'IVI logical name or IVI virtual name', '*myLogicalName*', '(*myLogicalName* = name)']],
'table_header': ['Example #', 'Device Type', 'Syntax', 'Variable'],
},
            },
            {
                'direction': 'in',
                'name': 'idQuery',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether you want NI-FGEN to perform an ID query.

When you set this parameter to VI_TRUE, NI-FGEN verifies that the
device that you initialize is supported.

Circumstances can arise where sending an ID query to the device is
undesirable. When you set this parameter to VI_FALSE, the function
initializes the device without performing an ID query.

****Defined Values****

**Default Value**: VI_TRUE
''',
'table_body': [['VI_TRUE', 'Perform ID query'], ['VI_FALSE', 'Skip ID query']],
},
            },
            {
                'direction': 'in',
                'name': 'resetDevice',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether you want to reset the device during the initialization
procedure. VI_TRUE specifies that the device is reset and performs the
same function as the nifgen_Reset function.

****Defined Values****

**Default Value**: VI_TRUE
''',
'table_body': [['VI_TRUE', 'Reset device'], ['VI_FALSE', 'Do not reset device']],
},
            },
            {
                'direction': 'out',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Returns a session handle that you can use to identify the device in all
subsequent NI-FGEN function calls.
''',
},
            },
        ],
'documentation': {
'description': '''
Performs the following initialization actions:

-  Creates a new IVI instrument driver session.
-  Opens a session to the specified device using the interface and
   address that you specify for the **resourceName** parameter.
-  If the **IDQuery** parameter is set to VI_TRUE, this function
   queries the device ID and checks that the ID is valid for NI-FGEN.
-  If the **resetDevice** parameter is set to VI_TRUE, this function
   resets the device to a known state.
-  Sends initialization commands to set the device to the state
   necessary for the operation of NI-FGEN.
-  Returns a session handle that you can use to identify the device in
   all subsequent NI-FGEN function calls.
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
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
        ],
'documentation': {
'description': '''
Resets the instrument to a known state. This function aborts the
generation, clears all routes, and resets session attributes to the
default values. This function does not, however, commit the session
properties or configure the device hardware to its default state.
''',
'note': '''
For the NI 5401/5404/5411/5431, this function exhibits the same
behavior as the nifgen_ResetDevice function.
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
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'out',
                'name': 'instrumentDriverRevision',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Returns the NI-FGEN software revision numbers in the form of a string.

You must pass a ViChar array with at least 256 bytes.
''',
},
            },
            {
                'direction': 'out',
                'name': 'firmwareRevision',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Returns the instrument firmware revision numbers in the form of a
string.

You must pass a ViChar array with at least 256 bytes.
''',
},
            },
        ],
'documentation': {
'description': 'Returns the revision numbers of the NI-FGEN and instrument firmware.',
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
Identifies your instrument session. **vi** is obtained from the
niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels
functions and identifies a particular instrument session.
''',
},
            },
            {
                'direction': 'out',
                'name': 'selfTestResult',
                'type': 'ViInt16',
'documentation': {
'description': '''
Contains the value returned from the instrument self-test. A value of 0
indicates success.
''',
'table_body': [['0', 'Passed self-test'], ['1', 'Self-test failed']],
'table_header': ['Self-Test Code', 'Description'],
},
            },
            {
                'direction': 'out',
                'name': 'selfTestMessage',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Returns the self-test response string from the instrument.

You must pass a ViChar array with at least 256 bytes.
''',
},
            },
        ],
'documentation': {
'description': 'Runs the instrument self-test routine and returns the test result(s).',
'note': '''
When used on some signal generators, the device is reset after the
niFgen_self_test function runs. If you use the niFgen_self_test
function, your device may not be in its previously configured state
after the function runs.
''',
},
    },
}
