
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
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
        ],
'documentation': {
'description': '''
Aborts an acquisition and returns the digitizer to the Idle state. Call
this function if the digitizer times out waiting for a trigger.
''',
},
    },
    'AcquisitionStatus': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'out',
                'name': 'acquisitionStatus',
                'type': 'ViInt32',
'documentation': {
'description': '''
Returns whether the acquisition is complete, in progress, or unknown.

**Defined Values**

NISCOPE_VAL_ACQ_COMPLETE

NISCOPE_VAL_ACQ_IN_PROGRESS

NISCOPE_VAL_ACQ_STATUS_UNKNOWN
''',
},
            },
        ],
'documentation': {
'description': '''
Returns status information about the acquisition to the **status**
output parameter.
''',
},
    },
    'ActualMeasWfmSize': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'arrayMeasFunction',
                'type': 'ViInt32',
'documentation': {
'description': '''
The `array
measurement <REPLACE_DRIVER_SPECIFIC_URL_2(array_measurements_refs)>`__
to perform.
''',
},
            },
            {
                'direction': 'out',
                'name': 'measWaveformSize',
                'type': 'ViInt32',
'documentation': {
'description': '''
Returns the size (in number of samples) of the resulting analysis
waveform.
''',
},
            },
        ],
'documentation': {
'description': 'Returns the total available size of an array measurement acquisition.',
},
    },
    'ActualNumWfms': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The channel to configure. For more information, refer to `Channel String
Syntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.
''',
},
            },
            {
                'direction': 'out',
                'name': 'numWfms',
                'type': 'ViInt32',
'documentation': {
'description': '''
Returns the number of records times the number of channels; if you are
operating in DDC mode (NI 5620/5621 only), this value is multiplied by
two.
''',
},
            },
        ],
'documentation': {
'description': '''
Helps you to declare appropriately sized waveforms. NI-SCOPE handles the
channel list parsing for you.
''',
},
    },
    'ActualRecordLength': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'out',
                'name': 'recordLength',
                'type': 'ViInt32',
'documentation': {
'description': '''
Returns the actual number of points the digitizer acquires for each
channel; NI-SCOPE returns the value held in the
NISCOPE_ATTR_HORZ_RECORD_LENGTH attribute.
''',
},
            },
        ],
'documentation': {
'description': '''
Returns the actual number of points the digitizer acquires for each
channel. After configuring the digitizer for an acquisition, call this
function to determine the size of the waveforms that the digitizer
acquires. The value is equal to or greater than the minimum number of
points specified in any of the Configure Horizontal functions.
''',
},
    },
    'AddWaveformProcessing': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The channel to configure. For more information, refer to `Channel String
Syntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.
''',
},
            },
            {
                'direction': 'in',
                'name': 'measFunction',
                'type': 'ViInt32',
'documentation': {
'description': '''
The `array
measurement <REPLACE_DRIVER_SPECIFIC_URL_2(array_measurements_refs)>`__
to add.
''',
},
            },
        ],
'documentation': {
'description': '''
Adds one measurement to the list of processing steps that are completed
before the measurement. The processing is added on a per channel basis,
and the processing measurements are completed in the same order they are
registered. All measurement library parameters—the attributes starting
with NISCOPE_ATTR_MEAS—are cached at the time of registering the
processing, and this set of parameters is used during the processing
step. The processing measurements are streamed, so the result of the
first processing step is used as the input for the next step. The
processing is done before any other measurements.
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
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Delay',
                'type': 'ViReal64',
'documentation': {
'description': '''
How long the digitizer waits after receiving the trigger to start
acquiring data. Refer to NISCOPE_ATTR_TRIGGER_DELAY_TIME for more
information.
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the relative sample clock delay (in seconds) when using the
internal clock. Each time this function is called, the sample clock is
delayed from the reference clock by the specified amount of time.
''',
},
    },
    'AutoSetup': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
        ],
'documentation': {
'description': '''
Automatically configures the instrument. When you call this function,
the digitizer senses the input signal and automatically configures many
of the instrument settings. If a signal is detected on a channel, the
driver chooses the smallest available vertical range that is larger than
the signal range. For example, if the signal is a 1.2 V\ :sub:`pk-pk`
sine wave, and the device supports 1 V and 2 V vertical ranges, the
driver will choose the 2 V vertical range for that channel.

If no signal is found on any analog input channel, a warning is
returned, and all channels are enabled. A channel is considered to have
a signal present if the signal is at least 10% of the smallest vertical
range available for that channel.

The following settings are changed:
''',
'table_body': [['**General**'], ['Acquisition mode', 'Normal'], ['Reference clock', 'Internal'], ['**Vertical**'], ['Vertical coupling', 'AC (DC for NI 5621)'], ['Vertical bandwidth', 'Full'], ['Vertical range', 'Changed by auto setup'], ['Vertical offset', '0 V'], ['Probe attenuation', 'Unchanged by auto setup'], ['Input impedance', 'Unchanged by auto setup'], ['**Horizontal**'], ['Sample rate', 'Changed by auto setup'], ['Min record length', 'Changed by auto setup'], ['Enforce realtime', 'True'], ['Number of Records', 'Changed to 1'], ['**Triggering**'], ['Trigger type', 'Edge if signal present, otherwise immediate'], ['Trigger channel', 'Lowest numbered channel with a signal present'], ['Trigger slope', 'Positive'], ['Trigger coupling', 'DC'], ['Reference position', '50%'], ['Trigger level', '50% of signal on trigger channel'], ['Trigger delay', '0'], ['Trigger holdoff', '0'], ['Trigger output', 'None']],
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
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The channel to configure. For more information, refer to `Channel String
Syntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Option',
                'type': 'ViInt32',
'documentation': {
'description': '''
The calibration option. Use VI_NULL for a normal self-calibration
operation or NISCOPE_VAL_CAL_RESTORE_EXTERNAL_CALIBRATION to
restore the previous calibration.
''',
},
            },
        ],
'documentation': {
'description': '''
Self-calibrates most NI digitizers, including all SMC-based devices and
most Traditional NI-DAQ (Legacy) devices. To verify that your digitizer
supports self-calibration, refer to `Features Supported by
Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__.

For SMC-based digitizers, if the self-calibration is performed
successfully in a regular session, the calibration constants are
immediately stored in the self-calibration area of the EEPROM. If the
self-calibration is performed in an external calibration session, the
calibration constants take effect immediately for the duration of the
session. However, they are not stored in the EEPROM until
niScope_CalEnd is called with **action** set to
NISCOPE_VAL_ACTION_STORE and no errors occur.
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
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The channel to configure. For more information, refer to `Channel String
Syntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'The ID of an attribute',
},
            },
            {
                'direction': 'in',
                'name': 'Value',
                'type': 'ViBoolean',
'documentation': {
'description': '''
The value that you want to verify for the attribute. Some values might
not be valid depending on the current settings of the instrument
session.
''',
},
            },
        ],
'documentation': {
'description': 'Verifies the validity of a value you specify for a ViBoolean attribute.',
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
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The channel to configure. For more information, refer to `Channel String
Syntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'The ID of an attribute.',
},
            },
            {
                'direction': 'in',
                'name': 'Value',
                'type': 'ViInt32',
'documentation': {
'description': '''
The value that you want to verify for the attribute. Some values might
not be valid depending on the current settings of the instrument
session.
''',
},
            },
        ],
'documentation': {
'description': 'Verifies the validity of a value you specify for a ViInt32 attribute.',
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
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The channel to configure. For more information, refer to `Channel String
Syntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'The ID of an attribute.',
},
            },
            {
                'direction': 'in',
                'name': 'Value',
                'type': 'ViInt64',
'documentation': {
'description': '''
The value that you want to verify for the attribute. Some values might
not be valid depending on the current settings of the instrument
session.
''',
},
            },
        ],
'documentation': {
'description': 'Verifies the validity of a value you specify for a ViInt64 attribute.',
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
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The channel to configure. For more information, refer to `Channel String
Syntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'The ID of an attribute.',
},
            },
            {
                'direction': 'in',
                'name': 'Value',
                'type': 'ViReal64',
'documentation': {
'description': '''
The value that you want to verify for the attribute. Some values might
not be valid depending on the current settings of the instrument
session.
''',
},
            },
        ],
'documentation': {
'description': 'Verifies the validity of a value you specify for a ViReal64 attribute.',
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
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The channel to configure. For more information, refer to `Channel String
Syntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'The ID of an attribute.',
},
            },
            {
                'direction': 'in',
                'name': 'Value',
                'type': 'ViSession',
'documentation': {
'description': '''
The value that you want to verify for the attribute. Some values might
not be valid depending on the current settings of the instrument
session.
''',
},
            },
        ],
'documentation': {
'description': 'Verifies the validity of a value you specify for a ViSession attribute.',
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
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The channel to configure. For more information, refer to `Channel String
Syntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'The ID of an attribute.',
},
            },
            {
                'direction': 'in',
                'name': 'Value',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The value that you want to verify for the attribute. Some values might
not be valid depending on the current settings of the instrument
session.
''',
},
            },
        ],
'documentation': {
'description': 'Verifies the validity of a value you specify for a ViString attribute.',
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
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
        ],
'documentation': {
'description': '''
Clears the error information for the current execution thread and the
IVI session you specify. If you pass VI_NULL for the Instrument Handle
parameter, this function clears the error information only for the
current execution thread.
''',
'note': '''
This function is included for compliance with the IviScope Class
Specification.
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
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
        ],
'documentation': {
'description': 'Clears the list of current interchange warnings.',
'note': '''
This function is included for compliance with the IviScope Class
Specification.
''',
},
    },
    'ClearWaveformMeasurementStats': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The channel to configure. For more information, refer to `Channel String
Syntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.
''',
},
            },
            {
                'direction': 'in',
                'name': 'clearableMeasurementFunction',
                'type': 'ViInt32',
'documentation': {
'description': '''
The `scalar
measurement <REPLACE_DRIVER_SPECIFIC_URL_2(scalar_measurements_refs)>`__
or `array
measurement <REPLACE_DRIVER_SPECIFIC_URL_2(array_measurements_refs)>`__
to clear the stats for.
''',
},
            },
        ],
'documentation': {
'description': '''
Clears the waveform stats on the channel and measurement you specify. If
you want to clear all of the measurements, use
NISCOPE_VAL_ALL_MEASUREMENTS in the **clearableMeasurementFunction**
parameter.

Every time a measurement is called, the statistics information is
updated, including the min, max, mean, standard deviation, and number of
updates. This information is fetched with
niScope_FetchMeasurementStats. The multi-acquisition array measurements
are also cleared with this function.
''',
},
    },
    'ClearWaveformProcessing': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The channel to configure. For more information, refer to `Channel String
Syntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.
''',
},
            },
        ],
'documentation': {
'description': '''
Clears the list of processing steps assigned to the given channel. The
processing is added using the niScope_AddWaveformProcessing function,
where the processing steps are completed in the same order in which they
are registered. The processing measurements are streamed, so the result
of the first processing step is used as the input for the next step. The
processing is also done before any other measurements.
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
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
        ],
'documentation': {
'description': '''
Commits to hardware all the parameter settings associated with the task.
Use this function if you want a parameter change to be immediately
reflected in the hardware. This function is not supported for
Traditional NI-DAQ (Legacy) devices.
''',
},
    },
    'ConfigureAcquisition': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'acquisitionType',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the manner in which the digitizer acquires data and fills the
waveform record; NI-SCOPE sets NISCOPE_ATTR_ACQUISITION_TYPE to this
value.

**Defined Values**

NISCOPE_VAL_NORMAL

NISCOPE_VAL_FLEXRES

NISCOPE_VAL_DDC
''',
'note': '''
NISCOPE_VAL_DDC applies to the NI 5620/5621 only. To use DDC mode in
the NI 5142/5622, leave **acquisitionType** set to NISCOPE_VAL_NORMAL
and set NISCOPE_ATTR_DDC_ENABLED to True.
''',
},
            },
        ],
'documentation': {
'description': '''
Configures how the digitizer acquires data and fills the waveform
record.
''',
},
    },
    'ConfigureAcquisitionRecord': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'timePerRecord',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the time per record.

Units: Seconds.
''',
},
            },
            {
                'direction': 'in',
                'name': 'minNumPoints',
                'type': 'ViInt32',
'documentation': {
'description': '''
Pass the minimum number of points you require in the record for each
channel. Call niScope_ActualRecordLength to obtain the actual record
length used.

Valid Values: 1 – available onboard memory
''',
},
            },
            {
                'direction': 'in',
                'name': 'acquisitionStartTime',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the position of the first point in the waveform record
relative to the trigger event.
''',
},
            },
        ],
'documentation': {
'description': '''
This function is included for compliance with the IviScope Class
Specification.

Configures the most commonly configured attributes of the instrument
acquisition subsystem.
''',
},
    },
    'ConfigureChanCharacteristics': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The channel to configure. For more information, refer to `Channel String
Syntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.
''',
},
            },
            {
                'direction': 'in',
                'name': 'inputImpedance',
                'type': 'ViReal64',
'documentation': {
'description': '''
The input impedance for the channel; NI-SCOPE sets
NISCOPE_ATTR_INPUT_IMPEDANCE to this value.
''',
},
            },
            {
                'direction': 'in',
                'name': 'maxInputFrequency',
                'type': 'ViReal64',
'documentation': {
'description': '''
The bandwidth for the channel; NI-SCOPE sets
NISCOPE_ATTR_MAX_INPUT_FREQUENCY to this value. Pass 0 for this
value to use the hardware default bandwidth. Pass –1 for this value to
achieve full bandwidth.
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the attributes that control the electrical characteristics of
the channel—the input impedance and the bandwidth.
''',
},
    },
    'ConfigureChannel': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Channel',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The channel to configure. For more information, refer to `channel String
Syntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.

Default Value: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'Range',
                'type': 'ViReal64',
'documentation': {
'description': 'Specifies the voltage range for the specified channel(s).',
},
            },
            {
                'direction': 'in',
                'name': 'Offset',
                'type': 'ViReal64',
'documentation': {
'description': '''
Selects the DC offset added to the specified channel(s).

Default Value: 0
''',
},
            },
            {
                'direction': 'in',
                'name': 'Coupling',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specify how you want the digitizer to couple the input signal for the
channel.

Defined Values

NISCOPE_VAL_AC (0)

NISCOPE_VAL_DC (1)

NISCOPE_VAL_GND (2)

A certain amount of delay is required for the coupling capacitor to
charge after changing vertical coupling from DC to AC. This delay is
typically:

| Low Impedance Source—150 ms
| 10X Probe—1.5 s
| 100X Probe—15 s
''',
},
            },
            {
                'direction': 'in',
                'name': 'probeAttenuation',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the probe attenuation for the specified channel(s).

Default Value: 1.00

Valid Range: 1.00 – 100

If you have a probe with *y*\ X attenuation, set this parameter to *y*.
For example, enter a value of 10 for a 10X probe.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Enabled',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Specify whether to enable the digitizer to acquire data for the channel
when you call niScope_InitiateAcquisition or niScope_ReadWaveform.

| Default Value:
| NISCOPE_VAL_TRUE (1)

Defined Values

| NISCOPE_VAL_TRUE (1)—Acquire data on this channel
| NISCOPE_VAL_FALSE (0)—Do not acquire data on this channel
''',
},
            },
        ],
'documentation': {
'description': '''
This function is included for compliance with the IviScope Class
Specification.

Configures the most commonly configured attributes of the instrument's
channel subsystem.
''',
},
    },
    'ConfigureClock': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'inputClockSource',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the input source for the reference clock to which the 100 MHz
sample clock is phase-locked. Refer to
NISCOPE_ATTR_INPUT_CLOCK_SOURCE for more information.
''',
},
            },
            {
                'direction': 'in',
                'name': 'outputClockSource',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the output source for the reference clock to which another
scope's sample clock can be phased-locked. Refer to
NISCOPE_ATTR_OUTPUT_CLOCK_SOURCE for more information
''',
},
            },
            {
                'direction': 'in',
                'name': 'clockSyncPulseSource',
                'type': 'ViChar[]',
'documentation': {
'description': '''
For the NI 5102, specifies the line on which the sample clock is sent or
received. For the NI 5112/5620/5621/5911, specifies the line on which
the one time sync pulse is sent or received. This line should be the
same for all devices to be synchronized. Refer to
NISCOPE_ATTR_CLOCK_SYNC_PULSE_SOURCE for more information.
''',
},
            },
            {
                'direction': 'in',
                'name': 'masterEnabled',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether you want the device to be a master or a slave. The
master device is typically the originator of the trigger signal and
clock sync pulse. For a standalone device, set this attribute to
VI_FALSE.

Refer to NISCOPE_ATTR_MASTER_ENABLE for more information.
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the attributes for synchronizing the digitizer to a reference
or sending the digitizer's reference clock output to be used as a
synchronizing clock for other digitizers.
''',
'note': '''
Some features are not supported by all digitizers. Refer to `Features
Supported by
Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
more information.
''',
},
    },
    'ConfigureEdgeTriggerSource': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Source',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The voltage threshold for the trigger. Refer to
NISCOPE_ATTR_TRIGGER_LEVEL for more information.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Level',
                'type': 'ViReal64',
'documentation': {
'description': '''
The voltage threshold for the trigger. Refer to
NISCOPE_ATTR_TRIGGER_LEVEL for more information.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Slope',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies whether you want a rising edge or a falling edge to trigger
the digitizer. Refer to NISCOPE_ATTR_TRIGGER_SLOPE for more
information.
''',
},
            },
        ],
'documentation': {
'description': '''
Sets the edge triggering attributes. An edge trigger occurs when the
trigger signal specified with the source parameter passes through the
voltage threshold specified with the level parameter and has the slope
specified with the slope parameter.

This function affects instrument behavior only if the triggerType is
NISCOPE_VAL_EDGE. Set the trigger type and trigger coupling before
calling this function.

If the trigger source is one of the analog input channels, you must
configure the vertical range, vertical offset, vertical coupling, probe
attenuation, and the maximum input frequency before calling this
function.
''',
'note': '''
This function is included for compliance with the IviScope Class
Specification.
''',
},
    },
    'ConfigureEqualizationFilterCoefficients': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The channel to configure. For more information, refer to `Channel String
Syntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.
''',
},
            },
            {
                'direction': 'in',
                'name': 'numberOfCoefficients',
                'type': 'ViInt32',
'documentation': {
'description': 'The number of coefficients being passed in the **coefficients** array.',
},
            },
            {
                'direction': 'in',
                'name': 'Coefficients',
                'type': 'ViReal64[]',
'documentation': {
'description': '''
The custom coefficients for the equalization FIR filter on the device.
These coefficients should be between +1 and –1. You can obtain the
number of coefficients from the
`NISCOPE_ATTR_EQUALIZATION_NUM_COEFFICIENTS <cviNISCOPE_ATTR_EQUALIZATION_NUM_COEFFICIENTS.html>`__
attribute. The
`NISCOPE_ATTR_EQUALIZATION_FILTER_ENABLED <cviNISCOPE_ATTR_EQUALIZATION_FILTER_ENABLED.html>`__
attribute must be set to TRUE to enable the filter.
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the custom coefficients for the equalization FIR filter on
the device. This filter is designed to compensate the input signal for
artifacts introduced to the signal outside of the digitizer. Because
this filter is a generic FIR filter, any coefficients are valid.
Coefficient values should be between +1 and –1.
''',
},
    },
    'ConfigureHorizontalTiming': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'minSampleRate',
                'type': 'ViReal64',
'documentation': {
'description': '''
The sampling rate for the acquisition. Refer to
NISCOPE_ATTR_MIN_SAMPLE_RATE for more information.
''',
},
            },
            {
                'direction': 'in',
                'name': 'minNumPts',
                'type': 'ViInt32',
'documentation': {
'description': '''
The minimum number of points you need in the record for each channel;
call niScope_ActualRecordLength to obtain the actual record length
used.

Valid Values: Greater than 1; limited by available memory
''',
},
            },
            {
                'direction': 'in',
                'name': 'refPosition',
                'type': 'ViReal64',
'documentation': {
'description': '''
The position of the Reference Event in the waveform record specified as
a percentage.
''',
},
            },
            {
                'direction': 'in',
                'name': 'numRecords',
                'type': 'ViInt32',
'documentation': {
'description': 'The number of records to acquire',
},
            },
            {
                'direction': 'in',
                'name': 'enforceRealtime',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Indicates whether the digitizer enforces real-time measurements or
allows equivalent-time (RIS) measurements; not all digitizers support
RIS—refer to `Features Supported by
Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
more information.

Default value: VI_TRUE

**Defined Values**

VI_TRUE—Allow real-time acquisitions only

VI_FALSE—Allow real-time and equivalent-time acquisitions
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the common properties of the horizontal subsystem for a
multirecord acquisition in terms of minimum sample rate.
''',
},
    },
    'ConfigureRefLevels': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Low',
                'type': 'ViReal64',
'documentation': {
'description': '''
Pass the low reference you want the digitizer to use for waveform
measurements.

Units: Either a percentage or voltage based on
NISCOPE_ATTR_MEAS_REF_LEVEL_UNITS. A percentage is calculated with
the voltage low and voltage high measurements representing 0% and 100%,
respectively.

Default Value: 10.0
''',
},
            },
            {
                'direction': 'in',
                'name': 'Mid',
                'type': 'ViReal64',
'documentation': {
'description': '''
Pass the mid reference you want the digitizer to use for waveform
measurements.

Units: Either a percentage or voltage based on
NISCOPE_ATTR_MEAS_REF_LEVEL_UNITS. A percentage is calculated with
the voltage low and voltage high measurements representing 0% and 100%,
respectively.

Default Value: 50.0
''',
},
            },
            {
                'direction': 'in',
                'name': 'High',
                'type': 'ViReal64',
'documentation': {
'description': '''
Pass the high reference you want the digitizer to use for waveform
measurements.

Units: Either a percentage or voltage based on
NISCOPE_ATTR_MEAS_REF_LEVEL_UNITS. A percentage is calculated with
the voltage low and voltage high measurements representing 0% and 100%,
respectively.

Default Value: 90.0
''',
},
            },
        ],
'documentation': {
'description': '''
This function is included for compliance with the IviScope Class
Specification.

Configures the reference levels for all channels of the digitizer. The
levels may be set on a per channel basis by setting
NISCOPE_ATTR_MEAS_CHAN_HIGH_REF_LEVEL,
NISCOPE_ATTR_MEAS_CHAN_LOW_REF_LEVEL, and
NISCOPE_ATTR_MEAS_CHAN_MID_REF_LEVEL

This function configures the reference levels for waveform measurements.
Call this function before calling niScope_FetchMeasurement to take a
rise time, fall time, width negative, width positive, duty cycle
negative, or duty cycle positive measurement.
''',
},
    },
    'ConfigureTVTriggerLineNumber': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'lineNumber',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specify the line number of the signal you want to trigger off of. The
valid ranges of the attribute depend on the signal format configured.

Default Value: 1
''',
'table_body': [['M-NTSC, 480i, 480p', '1 to 525'], ['BG/PAL, SECAM, 576i, 576p', '1 to 625'], ['720p', '1 to 750'], ['1080i,1080p', '1 to 1,125']],
'table_header': ['Signal Format', 'Line Numbers'],
},
            },
        ],
'documentation': {
'description': '''
This function is included for compliance with the IviScope Class
Specification.

Configures the TV line upon which the instrument triggers. The line
number is absolute and not relative to the field of the TV signal.

This function affects instrument behavior only if the trigger type is
set to NISCOPE_VAL_TV_TRIGGER and the TV trigger event is set to
NISCOPE_VAL_TV_EVENT_LINE_NUMBER. Call
niScope_ConfigureTVTriggerSource to set the TV trigger event before
calling this function.
''',
},
    },
    'ConfigureTVTriggerSource': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Source',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Pass the source you want the digitizer to monitor for a trigger.

Defined Values

| "0"—Channel 0
| "1"—Channel 1
| NISCOPE_VAL_EXTERNAL—Analog External Trigger Input
''',
},
            },
            {
                'direction': 'in',
                'name': 'signalFormat',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the Video/TV signal format.

Defined Values

| NISCOPE_VAL_NTSC (1)
| NISCOPE_VAL_PAL (2)
| NISCOPE_VAL_SECAM (3)
''',
},
            },
            {
                'direction': 'in',
                'name': 'Event',
                'type': 'ViInt32',
'documentation': {
'description': '''
Video/TV event to trigger off of.

Defined Values

| NISCOPE_VAL_TV_EVENT_FIELD1 (1)—trigger on field 1 of the signal
| NISCOPE_VAL_TV_EVENT_FIELD2 (2)—trigger on field 2 of the signal
| NISCOPE_VAL_TV_EVENT_ANY_FIELD (3)—trigger on the first field
  acquired
| NISCOPE_VAL_TV_EVENT_ANY_LINE (4)—trigger on the first line
  acquired
| NISCOPE_VAL_TV_EVENT_LINE_NUMBER (5)—trigger on a specific line
  of a video signal. Valid values vary depending on the signal format
  configured.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Polarity',
                'type': 'ViInt32',
'documentation': {
'description': '''
| Specifies the polarity of the video signal to trigger off of.

Defined Values

| NISCOPE_VAL_TV_POSITIVE (1)
| NISCOPE_VAL_TV_NEGATIVE (2)
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the instrument for TV triggering. It configures the TV signal
format, the event, and the signal polarity.

This function affects instrument behavior only if the trigger type is
NISCOPE_VAL_TV_TRIGGER. Set the trigger type and trigger coupling
before calling this function.
''',
'note': '''
This function is included for compliance with the IviScope Class
Specification.
''',
},
    },
    'ConfigureTrigger': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'triggerType',
                'type': 'ViInt32',
'documentation': {
'description': 'Specifies the type of trigger for which the digitizer will wait.',
},
            },
            {
                'direction': 'in',
                'name': 'Holdoff',
                'type': 'ViReal64',
'documentation': {
'description': '''
The length of time the digitizer waits after detecting a trigger before
enabling NI-SCOPE to detect another trigger. Refer to
NISCOPE_ATTR_TRIGGER_HOLDOFF for more information.
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the common attributes of the trigger subsystem.

When you use niScope_ReadWaveform, the instrument waits for a trigger.
You specify the type of trigger for which the instrument waits with the
Trigger Type parameter.

If the instrument requires multiple waveform acquisitions to build a
complete waveform, it waits for the length of time you specify with the
**holdoff** parameter to elapse since the previous trigger. The
instrument then waits for the next trigger.
''',
'note': '''
This function is included for compliance with the IviScope Class
Specification.
''',
},
    },
    'ConfigureTriggerCoupling': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Coupling',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specify how you want the instrument to couple the trigger signal.

Defined Values

 NISCOPE_VAL_AC (0)

 NISCOPE_VAL_DC (1)

NISCOPE_VAL_HF_REJECT (2)

NISCOPE_VAL_LF_REJECT (3)

NISCOPE_VAL_AC_PLUS_HF_REJECT (1001)
''',
},
            },
        ],
'documentation': {
'description': 'Sets the trigger coupling attribute.',
'note': '''
This function is included for compliance with the IviScope Class
Specification.
''',
},
    },
    'ConfigureTriggerDigital': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'triggerSource',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the trigger source. Refer to NISCOPE_ATTR_TRIGGER_SOURCE
for defined values.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Slope',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies whether you want a rising edge or a falling edge to trigger
the digitizer. Refer to NISCOPE_ATTR_TRIGGER_SLOPE for more
information.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Holdoff',
                'type': 'ViReal64',
'documentation': {
'description': '''
The length of time the digitizer waits after detecting a trigger before
enabling NI-SCOPE to detect another trigger. Refer to
NISCOPE_ATTR_TRIGGER_HOLDOFF for more information.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Delay',
                'type': 'ViReal64',
'documentation': {
'description': '''
How long the digitizer waits after receiving the trigger to start
acquiring data. Refer to NISCOPE_ATTR_TRIGGER_DELAY_TIME for more
information.
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the common properties of a digital trigger.

When you initiate an acquisition, the digitizer waits for the start
trigger, which is configured through the NISCOPE_ATTR_ACQ_ARM_SOURCE
(Start Trigger Source) attribute. The default is immediate. Upon
receiving the start trigger the digitizer begins sampling pretrigger
points. After the digitizer finishes sampling pretrigger points, the
digitizer waits for a reference (stop) trigger that you specify with a
function such as this one. Upon receiving the reference trigger the
digitizer finishes the acquisition after completing posttrigger
sampling. With each Configure Trigger function, you specify
configuration parameters such as the trigger source and the amount of
trigger delay.
''',
'note': '''
For multirecord acquisitions, all records after the first record are
started by using the Advance Trigger Source. The default is immediate.

You can adjust the amount of pre-trigger and post-trigger samples using
the reference position parameter on the
niScope_ConfigureHorizontalTiming function. The default is half of the
record length.

Some features are not supported by all digitizers. Refer to `Features
Supported by
Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
more information.

Digital triggering is not supported in RIS mode.
''',
},
    },
    'ConfigureTriggerEdge': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'triggerSource',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the trigger source. Refer to NISCOPE_ATTR_TRIGGER_SOURCE
for defined values.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Level',
                'type': 'ViReal64',
'documentation': {
'description': '''
The voltage threshold for the trigger. Refer to
NISCOPE_ATTR_TRIGGER_LEVEL for more information.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Slope',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies whether you want a rising edge or a falling edge to trigger
the digitizer. Refer to NISCOPE_ATTR_TRIGGER_SLOPE for more
information.
''',
},
            },
            {
                'direction': 'in',
                'name': 'triggerCoupling',
                'type': 'ViInt32',
'documentation': {
'description': '''
Applies coupling and filtering options to the trigger signal. Refer to
NISCOPE_ATTR_TRIGGER_COUPLING for more information.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Holdoff',
                'type': 'ViReal64',
'documentation': {
'description': '''
The length of time the digitizer waits after detecting a trigger before
enabling NI-SCOPE to detect another trigger. Refer to
NISCOPE_ATTR_TRIGGER_HOLDOFF for more information.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Delay',
                'type': 'ViReal64',
'documentation': {
'description': '''
How long the digitizer waits after receiving the trigger to start
acquiring data. Refer to NISCOPE_ATTR_TRIGGER_DELAY_TIME for more
information.
''',
},
            },
        ],
'documentation': {
'description': '''
Configures common properties for analog edge triggering.

When you initiate an acquisition, the digitizer waits for the start
trigger, which is configured through the NISCOPE_ATTR_ACQ_ARM_SOURCE
(Start Trigger Source) attribute. The default is immediate. Upon
receiving the start trigger the digitizer begins sampling pretrigger
points. After the digitizer finishes sampling pretrigger points, the
digitizer waits for a reference (stop) trigger that you specify with a
function such as this one. Upon receiving the reference trigger the
digitizer finishes the acquisition after completing posttrigger
sampling. With each Configure Trigger function, you specify
configuration parameters such as the trigger source and the amount of
trigger delay.
''',
'note': '''
Some features are not supported by all digitizers. Refer to `Features
Supported by
Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
more information.
''',
},
    },
    'ConfigureTriggerHysteresis': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'triggerSource',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the trigger source. Refer to NISCOPE_ATTR_TRIGGER_SOURCE
for defined values.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Level',
                'type': 'ViReal64',
'documentation': {
'description': '''
The voltage threshold for the trigger. Refer to
NISCOPE_ATTR_TRIGGER_LEVEL for more information.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Hysteresis',
                'type': 'ViReal64',
'documentation': {
'description': '''
The size of the hysteresis window on either side of the **level** in
volts; the digitizer triggers when the trigger signal passes through the
hysteresis value you specify with this parameter, has the slope you
specify with **slope**, and passes through the **level**. Refer to
NISCOPE_ATTR_TRIGGER_HYSTERESIS for defined values.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Slope',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies whether you want a rising edge or a falling edge to trigger
the digitizer. Refer to NISCOPE_ATTR_TRIGGER_SLOPE for more
information.
''',
},
            },
            {
                'direction': 'in',
                'name': 'triggerCoupling',
                'type': 'ViInt32',
'documentation': {
'description': '''
Applies coupling and filtering options to the trigger signal. Refer to
NISCOPE_ATTR_TRIGGER_COUPLING for more information.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Holdoff',
                'type': 'ViReal64',
'documentation': {
'description': '''
The length of time the digitizer waits after detecting a trigger before
enabling NI-SCOPE to detect another trigger. Refer to
NISCOPE_ATTR_TRIGGER_HOLDOFF for more information.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Delay',
                'type': 'ViReal64',
'documentation': {
'description': '''
How long the digitizer waits after receiving the trigger to start
acquiring data. Refer to NISCOPE_ATTR_TRIGGER_DELAY_TIME for more
information.
''',
},
            },
        ],
'documentation': {
'description': '''
Configures common properties for analog hysteresis triggering. This kind
of trigger specifies an additional value, specified in the
**hysteresis** parameter, that a signal must pass through before a
trigger can occur. This additional value acts as a kind of buffer zone
that keeps noise from triggering an acquisition.

When you initiate an acquisition, the digitizer waits for the start
trigger, which is configured through the
NISCOPE_ATTR_ACQ_ARM_SOURCE. The default is immediate. Upon
receiving the start trigger the digitizer begins sampling pretrigger
points. After the digitizer finishes sampling pretrigger points, the
digitizer waits for a reference (stop) trigger that you specify with a
function such as this one. Upon receiving the reference trigger the
digitizer finishes the acquisition after completing posttrigger
sampling. With each Configure Trigger function, you specify
configuration parameters such as the trigger source and the amount of
trigger delay.
''',
'note': '''
Some features are not supported by all digitizers. Refer to `Features
Supported by
Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
more information.
''',
},
    },
    'ConfigureTriggerImmediate': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
        ],
'documentation': {
'description': '''
Configures common properties for immediate triggering. Immediate
triggering means the digitizer triggers itself.

When you initiate an acquisition, the digitizer waits for a trigger. You
specify the type of trigger that the digitizer waits for with a
Configure Trigger function, such as niScope_ConfigureTriggerImmediate.
''',
},
    },
    'ConfigureTriggerOutput': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'triggerEvent',
                'type': 'ViInt32',
'documentation': {
'description': 'Specifies the condition in which this device generates a digital pulse.',
},
            },
            {
                'direction': 'in',
                'name': 'triggerOutput',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the hardware signal line on which the digital pulse is
generated.

**Valid Values**

| NISCOPE_VAL_NO_EVENT
| NISCOPE_VAL_STOP_TRIGGER_EVENT
| NISCOPE_VAL_START_TRIGGER_EVENT
| NISCOPE_VAL_END_OF_ACQUISITION_EVENT
| NISCOPE_VAL_END_OF_RECORD_EVENT
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the digitizer to generate a signal pulse that other
digitizers can detect when configured for digital triggering.

For Traditional NI-DAQ devices, exported signals are still present in
the route after the session is closed. You must clear the route before
closing the session, or call niScope_reset.

To clear the route, call this function again and route
NISCOPE_VAL_NONE to the line that you had exported. For example, if
you originally called this function with the trigger event
NISCOPE_VAL_STOP_TRIGGER_EVENT routed to the trigger output
NISCOPE_VAL_RTSI_0, you would call this function again with
NISCOPE_VAL_NONE routed to NISCOPE_VAL_RTSI_0 to clear the route.
''',
'note': '''
This function is obsolete. Consider using niScope_ExportSignal
instead.
''',
},
    },
    'ConfigureTriggerSoftware': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Holdoff',
                'type': 'ViReal64',
'documentation': {
'description': '''
The length of time the digitizer waits after detecting a trigger before
enabling NI-SCOPE to detect another trigger. Refer to
NISCOPE_ATTR_TRIGGER_HOLDOFF for more information.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Delay',
                'type': 'ViReal64',
'documentation': {
'description': '''
How long the digitizer waits after receiving the trigger to start
acquiring data. Refer to NISCOPE_ATTR_TRIGGER_DELAY_TIME for more
information.
''',
},
            },
        ],
'documentation': {
'description': '''
Configures common properties for software triggering.

When you initiate an acquisition, the digitizer waits for the start
trigger, which is configured through the NISCOPE_ATTR_ACQ_ARM_SOURCE
(Start Trigger Source) attribute. The default is immediate. Upon
receiving the start trigger the digitizer begins sampling pretrigger
points. After the digitizer finishes sampling pretrigger points, the
digitizer waits for a reference (stop) trigger that you specify with a
function such as this one. Upon receiving the reference trigger the
digitizer finishes the acquisition after completing posttrigger
sampling. With each Configure Trigger function, you specify
configuration parameters such as the trigger source and the amount of
trigger delay.

To trigger the acquisition, use niScope_SendSoftwareTriggerEdge.
''',
'note': '''
Some features are not supported by all digitizers. Refer to `Features
Supported by
Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
more information.
''',
},
    },
    'ConfigureTriggerVideo': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'triggerSource',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the trigger source. Refer to NISCOPE_ATTR_TRIGGER_SOURCE
for defined values.
''',
},
            },
            {
                'direction': 'in',
                'name': 'enableDcRestore',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Offsets each video line so the clamping level (the portion of the video
line between the end of the color burst and the beginning of the active
image) is moved to zero volt. Refer to
NISCOPE_ATTR_ENABLE_DC_RESTORE for defined values.
''',
},
            },
            {
                'direction': 'in',
                'name': 'signalFormat',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the type of video signal sync the digitizer should look for.
Refer to NISCOPE_ATTR_TV_TRIGGER_SIGNAL_FORMAT for more
information.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Event',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the TV event you want to trigger on. You can trigger on a
specific or on the next coming line or field of the signal.
''',
},
            },
            {
                'direction': 'in',
                'name': 'lineNumber',
                'type': 'ViInt32',
'documentation': {
'description': '''
Selects the line number to trigger on. The line number range covers an
entire frame and is referenced as shown on `Vertical Blanking and
Synchronization
Signal <REPLACE_DRIVER_SPECIFIC_URL_1(gray_scale_image)>`__. Refer to
NISCOPE_ATTR_TV_TRIGGER_LINE_NUMBER for more information.

Default value: 1
''',
},
            },
            {
                'direction': 'in',
                'name': 'Polarity',
                'type': 'ViInt32',
'documentation': {
'description': 'Specifies the polarity of the video signal sync.',
},
            },
            {
                'direction': 'in',
                'name': 'triggerCoupling',
                'type': 'ViInt32',
'documentation': {
'description': '''
Applies coupling and filtering options to the trigger signal. Refer to
NISCOPE_ATTR_TRIGGER_COUPLING for more information.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Holdoff',
                'type': 'ViReal64',
'documentation': {
'description': '''
The length of time the digitizer waits after detecting a trigger before
enabling NI-SCOPE to detect another trigger. Refer to
NISCOPE_ATTR_TRIGGER_HOLDOFF for more information.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Delay',
                'type': 'ViReal64',
'documentation': {
'description': '''
How long the digitizer waits after receiving the trigger to start
acquiring data. Refer to NISCOPE_ATTR_TRIGGER_DELAY_TIME for more
information.
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the common properties for video triggering, including the
signal format, TV event, line number, polarity, and enable DC restore. A
video trigger occurs when the digitizer finds a valid video signal sync.

When you initiate an acquisition, the digitizer waits for the start
trigger, which is configured through the NISCOPE_ATTR_ACQ_ARM_SOURCE
(Start Trigger Source) attribute. The default is immediate. Upon
receiving the start trigger the digitizer begins sampling pretrigger
points. After the digitizer finishes sampling pretrigger points, the
digitizer waits for a reference (stop) trigger that you specify with a
function such as this one. Upon receiving the reference trigger the
digitizer finishes the acquisition after completing posttrigger
sampling. With each Configure Trigger function, you specify
configuration parameters such as the trigger source and the amount of
trigger delay.
''',
'note': '''
Some features are not supported by all digitizers. Refer to `Features
Supported by
Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
more information.
''',
},
    },
    'ConfigureTriggerWindow': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'triggerSource',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the trigger source. Refer to NISCOPE_ATTR_TRIGGER_SOURCE
for defined values.
''',
},
            },
            {
                'direction': 'in',
                'name': 'lowLevel',
                'type': 'ViReal64',
'documentation': {
'description': '''
Passes the voltage threshold you want the digitizer to use for low
triggering.
''',
},
            },
            {
                'direction': 'in',
                'name': 'highLevel',
                'type': 'ViReal64',
'documentation': {
'description': '''
Passes the voltage threshold you want the digitizer to use for high
triggering.
''',
},
            },
            {
                'direction': 'in',
                'name': 'windowMode',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies whether you want the trigger to occur when the signal enters
or leaves a window.
''',
},
            },
            {
                'direction': 'in',
                'name': 'triggerCoupling',
                'type': 'ViInt32',
'documentation': {
'description': '''
Applies coupling and filtering options to the trigger signal. Refer to
NISCOPE_ATTR_TRIGGER_COUPLING for more information.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Holdoff',
                'type': 'ViReal64',
'documentation': {
'description': '''
The length of time the digitizer waits after detecting a trigger before
enabling NI-SCOPE to detect another trigger. Refer to
NISCOPE_ATTR_TRIGGER_HOLDOFF for more information.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Delay',
                'type': 'ViReal64',
'documentation': {
'description': '''
How long the digitizer waits after receiving the trigger to start
acquiring data. Refer to NISCOPE_ATTR_TRIGGER_DELAY_TIME for more
information.
''',
},
            },
        ],
'documentation': {
'description': '''
Configures common properties for analog window triggering. A window
trigger occurs when a signal enters or leaves a window you specify with
the **high level** or **low level** parameters.

When you initiate an acquisition, the digitizer waits for the start
trigger, which is configured through the NISCOPE_ATTR_ACQ_ARM_SOURCE
(Start Trigger Source) attribute. The default is immediate. Upon
receiving the start trigger the digitizer begins sampling pretrigger
points. After the digitizer finishes sampling pretrigger points, the
digitizer waits for a reference (stop) trigger that you specify with a
function such as this one. Upon receiving the reference trigger the
digitizer finishes the acquisition after completing posttrigger
sampling. With each Configure Trigger function, you specify
configuration parameters such as the trigger source and the amount of
trigger delay.

To trigger the acquisition, use niScope_SendSoftwareTriggerEdge.
''',
'note': '''
Some features are not supported by all digitizers. Refer to `Features
Supported by
Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
more information.
''',
},
    },
    'ConfigureVertical': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The channel to configure. For more information, refer to `Channel String
Syntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Range',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the vertical range Refer to NISCOPE_ATTR_VERTICAL_RANGE for
more information.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Offset',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the vertical offset. Refer to NISCOPE_ATTR_VERTICAL_OFFSET
for more information.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Coupling',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies how to couple the input signal. Refer to
NISCOPE_ATTR_VERTICAL_COUPLING for more information.
''',
},
            },
            {
                'direction': 'in',
                'name': 'probeAttenuation',
                'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the probe attenuation. Refer to
NISCOPE_ATTR_PROBE_ATTENUATION for valid values.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Enabled',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether the channel is enabled for acquisition. Refer to
NISCOPE_ATTR_CHANNEL_ENABLED for more information.
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the most commonly configured attributes of the digitizer
vertical subsystem, such as the range, offset, coupling, probe
attenuation, and the channel.
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
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
        ],
'documentation': {
'description': '''
Aborts any current operation, opens data channel relays, and releases
RTSI and PFI lines.
''',
},
    },
    'ExportAttributeConfigurationBuffer': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'sizeInBytes',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the size, in bytes, of the byte array to export. If you enter
0, this function returns the needed size.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Configuration',
                'type': 'ViAddr',
'documentation': {
'description': '''
Specifies the byte array buffer to be populated with the exported
attribute configuration.
''',
},
            },
        ],
'documentation': {
'description': '''
Exports the attribute configuration of the session to a configuration
buffer.

You can export and import session attribute configurations only between
devices with identical model numbers, channel counts, and onboard memory
sizes.

This function verifies that the attributes you have configured for the
session are valid. If the configuration is invalid, NI‑SCOPE returns an
error.

**Related Topics:**

`Attributes and Attribute
Functions <REPLACE_DRIVER_SPECIFIC_URL_1(attributes_and_attribute_functions)>`__

`Setting Attributes Before Reading
Attributes <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__
''',
},
    },
    'ExportAttributeConfigurationFile': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'filePath',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the absolute path to the file to contain the exported
attribute configuration. If you specify an empty or relative path, this
function returns an error.
**Default file extension:** .niscopeconfig
''',
},
            },
        ],
'documentation': {
'description': '''
Exports the attribute configuration of the session to the specified
file.

You can export and import session attribute configurations only between
devices with identical model numbers, channel counts, and onboard memory
sizes.

This function verifies that the attributes you have configured for the
session are valid. If the configuration is invalid, NI‑SCOPE returns an
error.

**Related Topics:**

`Attributes and Attribute
Functions <REPLACE_DRIVER_SPECIFIC_URL_1(attributes_and_attribute_functions)>`__

`Setting Attributes Before Reading
Attributes <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__
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
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Signal',
                'type': 'ViInt32',
'documentation': {
'description': '''
signal (clock, trigger, or event) to export.

**Defined Values**
''',
'table_body': [['NISCOPE_VAL_REF_TRIGGER', '(1)', 'Generate a pulse when detecting the Stop/Reference trigger.'], ['NISCOPE_VAL_START_TRIGGER', '(2)', 'Generate a pulse when detecting a Start trigger.'], ['NISCOPE_VAL_END_OF_ACQUISITION_EVENT', '(3)', 'Generate a pulse when the acquisition finishes.'], ['NISCOPE_VAL_END_OF_RECORD_EVENT', '(4)', 'Generate a pulse at the end of the record.'], ['NISCOPE_VAL_ADVANCE_TRIGGER', '(5)', 'Generate a pulse when detecting an Advance trigger.'], ['NISCOPE_VAL_READY_FOR_ADVANCE_EVENT', '(6)', 'Asserts when the digitizer is ready to advance to the next record.'], ['NISCOPE_VAL_READY_FOR_START_EVENT', '(7)', 'Asserts when the digitizer is initiated and ready to accept a Start trigger and begin sampling.'], ['NISCOPE_VAL_READY_FOR_REF_EVENT', '(10)', 'Asserts when the digitizer is ready to accept a Reference trigger.'], ['NISCOPE_VAL_REF_CLOCK', '(100)', 'Export the Reference clock for the digitizer to the specified terminal.'], ['NISCOPE_VAL_SAMPLE_CLOCK', '(101)', 'Export the Sample clock for the digitizer to the specified terminal.'], ['NISCOPE_VAL_5V_OUT', '(13)', 'Exports a 5 V power supply.']],
},
            },
            {
                'direction': 'in',
                'name': 'signalIdentifier',
                'type': 'ViConstString',
'documentation': {
'description': 'Describes the signal being exported.',
},
            },
            {
                'direction': 'in',
                'name': 'outputTerminal',
                'type': 'ViConstString',
'documentation': {
'description': '''
Identifies the hardware signal line on which the digital pulse is
generated.

**Defined Values**
''',
'table_body': [['NISCOPE_VAL_RTSI_0', '("VAL_RTSI_0")'], ['NISCOPE_VAL_RTSI_1', '("VAL_RTSI_1")'], ['NISCOPE_VAL_RTSI_2', '("VAL_RTSI_2")'], ['NISCOPE_VAL_RTSI_3', '("VAL_RTSI_3")'], ['NISCOPE_VAL_RTSI_4', '("VAL_RTSI_4")'], ['NISCOPE_VAL_RTSI_5', '("VAL_RTSI_5")'], ['NISCOPE_VAL_RTSI_6', '("VAL_RTSI_6")'], ['NISCOPE_VAL_RTSI_7', '("VAL_RTSI_7")'], ['NISCOPE_VAL_PXI_STAR', '("VAL_PXI_STAR")'], ['NISCOPE_VAL_PFI_0', '("VAL_PFI_0")'], ['NISCOPE_VAL_PFI_1', '("VAL_PFI_1")'], ['NISCOPE_VAL_PFI_2', '("VAL_PFI_2")'], ['NISCOPE_VAL_CLK_OUT', '("VAL_CLK_OUT")']],
},
            },
        ],
'documentation': {
'description': '''
Configures the digitizer to generate a signal that other devices can
detect when configured for digital triggering or sharing clocks. The
**signal** parameter specifies what condition causes the digitizer to
generate the signal. The **outputTerminal** parameter specifies where to
send the signal on the hardware (such as a PFI connector or RTSI line).

In cases where multiple instances of a particular signal exist, use the
**signalIdentifier** input to specify which instance to control. For
normal signals, only one instance exists and you should leave this
parameter set to the empty string. You can call this function multiple
times and set each available line to a different signal.

To unprogram a specific line on device, call this function with the
signal you no longer want to export and set **outputTerminal** to
NISCOPE_VAL_NONE.
''',
'note': 'This function replaces niScope_ConfigureTriggerOutput.',
},
    },
    'Fetch': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The channel to configure. For more information, refer to `Channel String
Syntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'ViReal64',
'documentation': {
'description': '''
The time to wait in seconds for data to be acquired; using 0 for this
parameter tells NI-SCOPE to fetch whatever is currently available. Using
-1 for this parameter implies infinite timeout.
''',
},
            },
            {
                'direction': 'in',
                'name': 'numSamples',
                'type': 'ViInt32',
'documentation': {
'description': '''
The maximum number of samples to fetch for each waveform. If the
acquisition finishes with fewer points than requested, some devices
return partial data if the acquisition finished, was aborted, or a
timeout of 0 was used. If it fails to complete within the timeout
period, the function returns an error.
''',
},
            },
            {
                'direction': 'out',
                'name': 'Wfm',
                'type': 'ViReal64[]',
'documentation': {
'description': '''
Returns an array whose length is the **numSamples** times number of
waveforms. Call niScope_ActualNumwfms to determine the number of
waveforms.

NI-SCOPE returns this data sequentially, so all record 0 waveforms are
first. For example, with a channel list of 0,1, you would have the
following index values:

index 0 = record 0, channel 0

index *x* = record 0, channel 1

index 2\ *x* = record 1, channel 0

index 3\ *x* = record 1, channel 1

Where *x* = the record length
''',
},
            },
            {
                'direction': 'out',
                'name': 'wfmInfo',
                'type': 'struct niScope_wfmInfo[]',
'documentation': {
'description': '''
Returns an array of structures with the following timing and scaling
information about each waveform:

-  **relativeInitialX**—the time (in seconds) from the trigger to the
   first sample in the fetched waveform
-  **absoluteInitialX**—timestamp (in seconds) of the first fetched
   sample. This timestamp is comparable between records and
   acquisitions; devices that do not support this parameter use 0 for
   this output.
-  **xIncrement**—the time between points in the acquired waveform in
   seconds
-  **actualSamples**—the actual number of samples fetched and placed in
   the waveform array
-  **gain**—the gain factor of the given channel; useful for scaling
   binary data with the following formula:

voltage = binary data × gain factor + offset

-  **offset**—the offset factor of the given channel; useful for scaling
   binary data with the following formula:

voltage = binary data × gain factor + offset

Call niScope_ActualNumWfms to determine the size of this array.
''',
},
            },
        ],
'documentation': {
'description': '''
Returns the waveform from a previously initiated acquisition that the
digitizer acquires for the specified channel. This function returns
scaled voltage waveforms.

This function may return multiple waveforms depending on the number of
channels, the acquisition type, and the number of records you specify.
''',
'note': '''
You can use niScope_Read instead of this function. niScope_Read
starts an acquisition on all enabled channels, waits for the acquisition
to complete, and returns the waveform for the specified channel.

Some functionality, such as time stamping, is not supported in all
digitizers. Refer to `Features Supported by
Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
more information.
''',
},
    },
    'FetchArrayMeasurement': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The channel to configure. For more information, refer to `Channel String
Syntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'ViReal64',
'documentation': {
'description': '''
The time to wait in seconds for data to be acquired; using 0 for this
parameter tells NI-SCOPE to fetch whatever is currently available. Using
-1 for this parameter implies infinite timeout.
''',
},
            },
            {
                'direction': 'in',
                'name': 'arrayMeasFunction',
                'type': 'ViInt32',
'documentation': {
'description': '''
The `array
measurement <REPLACE_DRIVER_SPECIFIC_URL_2(array_measurements_refs)>`__
to perform.
''',
},
            },
            {
                'direction': 'in',
                'name': 'measWfmSize',
                'type': 'ViInt32',
'documentation': {
'description': '''
The maximum number of samples returned in the measurement waveform array
for each waveform measurement. Use niScope_ActualMeasWfmSize to
determine the number of available samples.
''',
'note': '''
Use the attribute NISCOPE_ATTR_FETCH_MEAS_NUM_SAMPLES to set the
number of samples to fetch when performing a measurement. For more
information about when to use this attribute, refer to the `NI
KnowledgeBase <javascript:WWW(WWW_KB_MEAS)>`__.
''',
},
            },
            {
                'direction': 'out',
                'name': 'measWfm',
                'type': 'ViReal64[]',
'documentation': {
'description': '''
Returns an array whose length is the number of waveforms times
**measWfmSize**; call niScope_ActualNumWfms to determine the number of
waveforms; call niScope_ActualMeasWfmSize to determine the size of each
waveform.

NI-SCOPE returns this data sequentially, so all record 0 waveforms are
first. For example, with channel list of 0, 1, you would have the
following index values:

index 0 = record 0, channel 0

index *x* = record 0, channel 1

index 2\ *x* = record 1, channel 0

index 3\ *x* = record 1, channel 1

Where *x* = the record length
''',
},
            },
            {
                'direction': 'out',
                'name': 'wfmInfo',
                'type': 'struct niScope_wfmInfo[]',
'documentation': {
'description': '''
Returns an array of structures with the following timing and scaling
information about each waveform:

-  **relativeInitialX**—the time (in seconds) from the trigger to the
   first sample in the fetched waveform
-  **absoluteInitialX**—timestamp (in seconds) of the first fetched
   sample. This timestamp is comparable between records and
   acquisitions; devices that do not support this parameter use 0 for
   this output.
-  **xIncrement**—the time between points in the acquired waveform in
   seconds
-  **actualSamples**—the actual number of samples fetched and placed in
   the waveform array
-  **gain**—the gain factor of the given channel; useful for scaling
   binary data with the following formula:

voltage = binary data × gain factor + offset

-  **offset**—the offset factor of the given channel; useful for scaling
   binary data with the following formula:

voltage = binary data × gain factor + offset

Call niScope_ActualNumWfms to determine the size of this array.
''',
},
            },
        ],
'documentation': {
'description': '''
Obtains a waveform from the digitizer and returns the specified
measurement array. This function may return multiple waveforms depending
on the number of channels, the acquisition type, and the number of
records you specify.
''',
'note': '''
Some functionality, such as time stamping, is not supported in all
digitizers. Refer to `Features Supported by
Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
more information.
''',
},
    },
    'FetchBinary16': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The channel to configure. For more information, refer to `Channel String
Syntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'ViReal64',
'documentation': {
'description': '''
The time to wait in seconds for data to be acquired; using 0 for this
parameter tells NI-SCOPE to fetch whatever is currently available. Using
-1 for this parameter implies infinite timeout.
''',
},
            },
            {
                'direction': 'in',
                'name': 'numSamples',
                'type': 'ViInt32',
'documentation': {
'description': '''
The maximum number of samples to fetch for each waveform. If the
acquisition finishes with fewer points than requested, some devices
return partial data if the acquisition finished, was aborted, or a
timeout of 0 was used. If it fails to complete within the timeout
period, the function returns an error.
''',
},
            },
            {
                'direction': 'out',
                'name': 'Wfm',
                'type': 'ViInt16[]',
'documentation': {
'description': '''
Returns an array whose length is the **numSamples** times number of
waveforms. Call niScope_ActualNumwfms to determine the number of
waveforms.

NI-SCOPE returns this data sequentially, so all record 0 waveforms are
first. For example, with a channel list of 0,1, you would have the
following index values:

index 0 = record 0, channel 0

index *x* = record 0, channel 1

index 2\ *x* = record 1, channel 0

index 3\ *x* = record 1, channel 1

Where *x* = the record length
''',
},
            },
            {
                'direction': 'out',
                'name': 'wfmInfo',
                'type': 'struct niScope_wfmInfo[]',
'documentation': {
'description': '''
Returns an array of structures with the following timing and scaling
information about each waveform:

-  **relativeInitialX**—the time (in seconds) from the trigger to the
   first sample in the fetched waveform
-  **absoluteInitialX**—timestamp (in seconds) of the first fetched
   sample. This timestamp is comparable between records and
   acquisitions; devices that do not support this parameter use 0 for
   this output.
-  **xIncrement**—the time between points in the acquired waveform in
   seconds
-  **actualSamples**—the actual number of samples fetched and placed in
   the waveform array
-  **gain**—the gain factor of the given channel; useful for scaling
   binary data with the following formula:

voltage = binary data × gain factor + offset

-  **offset**—the offset factor of the given channel; useful for scaling
   binary data with the following formula:

voltage = binary data × gain factor + offset

Call niScope_ActualNumWfms to determine the size of this array.
''',
},
            },
        ],
'documentation': {
'description': '''
Retrieves data from a previously initiated acquisition and returns
binary 16-bit waveforms. This function may return multiple waveforms
depending on the number of channels, the acquisition type, and the
number of records you specify.

Refer to `Using Fetch
Functions <REPLACE_DRIVER_SPECIFIC_URL_1(using_fetch_functions)>`__ for
more information on using this function.
''',
'note': '''
Some functionality, such as time stamping, is not supported in all
digitizers. Refer to `Features Supported by
Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
more information.
''',
},
    },
    'FetchBinary32': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The channel to configure. For more information, refer to `Channel String
Syntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'ViReal64',
'documentation': {
'description': '''
The time to wait in seconds for data to be acquired; using 0 for this
parameter tells NI-SCOPE to fetch whatever is currently available. Using
-1 for this parameter implies infinite timeout.
''',
},
            },
            {
                'direction': 'in',
                'name': 'numSamples',
                'type': 'ViInt32',
'documentation': {
'description': '''
The maximum number of samples to fetch for each waveform. If the
acquisition finishes with fewer points than requested, some devices
return partial data if the acquisition finished, was aborted, or a
timeout of 0 was used. If it fails to complete within the timeout
period, the function returns an error.
''',
},
            },
            {
                'direction': 'out',
                'name': 'Wfm',
                'type': 'ViInt32[]',
'documentation': {
'description': '''
Returns an array whose length is the **numSamples** times number of
waveforms. Call niScope_ActualNumwfms to determine the number of
waveforms.

NI-SCOPE returns this data sequentially, so all record 0 waveforms are
first. For example, with a channel list of 0,1, you would have the
following index values:

index 0 = record 0, channel 0

index *x* = record 0, channel 1

index 2\ *x* = record 1, channel 0

index 3\ *x* = record 1, channel 1

Where *x* = the record length
''',
},
            },
            {
                'direction': 'out',
                'name': 'wfmInfo',
                'type': 'struct niScope_wfmInfo[]',
'documentation': {
'description': '''
Returns an array of structures with the following timing and scaling
information about each waveform:

-  **relativeInitialX**—the time (in seconds) from the trigger to the
   first sample in the fetched waveform
-  **absoluteInitialX**—timestamp (in seconds) of the first fetched
   sample. This timestamp is comparable between records and
   acquisitions; devices that do not support this parameter use 0 for
   this output.
-  **xIncrement**—the time between points in the acquired waveform in
   seconds
-  **actualSamples**—the actual number of samples fetched and placed in
   the waveform array
-  **gain**—the gain factor of the given channel; useful for scaling
   binary data with the following formula:

voltage = binary data × gain factor + offset

-  **offset**—the offset factor of the given channel; useful for scaling
   binary data with the following formula:

voltage = binary data × gain factor + offset

Call niScope_ActualNumWfms to determine the size of this array.
''',
},
            },
        ],
'documentation': {
'description': '''
Retrieves data from a previously initiated acquisition and returns
binary 32-bit waveforms. This function may return multiple waveforms
depending on the number of channels, the acquisition type, and the
number of records you specify.

Refer to `Using Fetch
Functions <REPLACE_DRIVER_SPECIFIC_URL_1(using_fetch_functions)>`__ for
more information on using this function.
''',
'note': '''
Some functionality, such as time stamping, is not supported in all
digitizers. Refer to `Features Supported by
Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
more information.
''',
},
    },
    'FetchBinary8': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The channel to configure. For more information, refer to `Channel String
Syntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'ViReal64',
'documentation': {
'description': '''
The time to wait in seconds for data to be acquired; using 0 for this
parameter tells NI-SCOPE to fetch whatever is currently available. Using
-1 for this parameter implies infinite timeout.
''',
},
            },
            {
                'direction': 'in',
                'name': 'numSamples',
                'type': 'ViInt32',
'documentation': {
'description': '''
The maximum number of samples to fetch for each waveform. If the
acquisition finishes with fewer points than requested, some devices
return partial data if the acquisition finished, was aborted, or a
timeout of 0 was used. If it fails to complete within the timeout
period, the function returns an error.
''',
},
            },
            {
                'direction': 'out',
                'name': 'Wfm',
                'type': 'ViInt8[]',
'documentation': {
'description': '''
Returns an array whose length is the **numSamples** times number of
waveforms. Call niScope_ActualNumwfms to determine the number of
waveforms.

NI-SCOPE returns this data sequentially, so all record 0 waveforms are
first. For example, with a channel list of 0,1, you would have the
following index values:

index 0 = record 0, channel 0

index *x* = record 0, channel 1

index 2\ *x* = record 1, channel 0

index 3\ *x* = record 1, channel 1

Where *x* = the record length
''',
},
            },
            {
                'direction': 'out',
                'name': 'wfmInfo',
                'type': 'struct niScope_wfmInfo[]',
'documentation': {
'description': '''
Returns an array of structures with the following timing and scaling
information about each waveform:

-  **relativeInitialX**—the time (in seconds) from the trigger to the
   first sample in the fetched waveform
-  **absoluteInitialX**—timestamp (in seconds) of the first fetched
   sample. This timestamp is comparable between records and
   acquisitions; devices that do not support this parameter use 0 for
   this output.
-  **xIncrement**—the time between points in the acquired waveform in
   seconds
-  **actualSamples**—the actual number of samples fetched and placed in
   the waveform array
-  **gain**—the gain factor of the given channel; useful for scaling
   binary data with the following formula:

voltage = binary data × gain factor + offset

-  **offset**—the offset factor of the given channel; useful for scaling
   binary data with the following formula:

voltage = binary data × gain factor + offset

Call niScope_ActualNumWfms to determine the size of this array.
''',
},
            },
        ],
'documentation': {
'description': '''
Retrieves data from a previously initiated acquisition and returns
binary 8-bit waveforms. This function may return multiple waveforms
depending on the number of channels, the acquisition type, and the
number of records you specify.

Refer to `Using Fetch
Functions <REPLACE_DRIVER_SPECIFIC_URL_1(using_fetch_functions)>`__ for
more information on using this function.
''',
'note': '''
Some functionality, such as time stamping, is not supported in all
digitizers. Refer to `Features Supported by
Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
more information.
''',
},
    },
    'FetchComplex': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViConstString',
'documentation': {
'description': '''
The channel to configure. For more information, refer to `Channel String
Syntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'ViReal64',
'documentation': {
'description': '''
The time to wait in seconds for data to be acquired; using 0 for this
parameter tells NI-SCOPE to fetch whatever is currently available. Using
-1 for this parameter implies infinite timeout.
''',
},
            },
            {
                'direction': 'in',
                'name': 'numSamples',
                'type': 'ViInt32',
'documentation': {
'description': '''
The maximum number of samples to fetch for each waveform. If the
acquisition finishes with fewer points than requested, some devices
return partial data if the acquisition finished, was aborted, or a
timeout of 0 was used. If it fails to complete within the timeout
period, the function returns an error.
''',
},
            },
            {
                'direction': 'out',
                'name': 'Wfm',
                'type': 'struct NIComplexNumber[]',
'documentation': {
'description': '''
Returns an array whose length is the **numSamples** times number of
waveforms. Call niScope_ActualNumwfms to determine the number of
waveforms.
''',
},
            },
            {
                'direction': 'out',
                'name': 'wfmInfo',
                'type': 'struct niScope_wfmInfo[]',
'documentation': {
'description': '''
Returns an array of structures with the following timing and scaling
information about each waveform:

-  **relativeInitialX**—the time (in seconds) from the trigger to the
   first sample in the fetched waveform
-  **absoluteInitialX**—timestamp (in seconds) of the first fetched
   sample. This timestamp is comparable between records and
   acquisitions; devices that do not support this parameter use 0 for
   this output.
-  **xIncrement**—the time between points in the acquired waveform in
   seconds
-  **actualSamples**—the actual number of samples fetched and placed in
   the waveform array
-  **gain**—the gain factor of the given channel; useful for scaling
   binary data with the following formula:

voltage = binary data × gain factor + offset

-  **offset**—the offset factor of the given channel; useful for scaling
   binary data with the following formula:

voltage = binary data × gain factor + offset

Call niScope_ActualNumWfms to determine the size of this array.
''',
},
            },
        ],
'documentation': {
'description': '''
Retrieves data that the digitizer has acquired from a previously
initiated acquisition and returns a one-dimensional array of complex,
scaled waveforms.
''',
},
    },
    'FetchComplexBinary16': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViConstString',
'documentation': {
'description': '''
The channel to configure. For more information, refer to `Channel String
Syntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'ViReal64',
'documentation': {
'description': '''
The time to wait in seconds for data to be acquired; using 0 for this
parameter tells NI-SCOPE to fetch whatever is currently available. Using
-1 for this parameter implies infinite timeout.
''',
},
            },
            {
                'direction': 'in',
                'name': 'numSamples',
                'type': 'ViInt32',
'documentation': {
'description': '''
The maximum number of samples to fetch for each waveform. If the
acquisition finishes with fewer points than requested, some devices
return partial data if the acquisition finished, was aborted, or a
timeout of 0 was used. If it fails to complete within the timeout
period, the function returns an error.
''',
},
            },
            {
                'direction': 'out',
                'name': 'Wfm',
                'type': 'struct NIComplexI16[]',
'documentation': {
'description': '''
Returns an array whose length is the **numSamples** times number of
waveforms. Call niScope_ActualNumwfms to determine the number of
waveforms.
''',
},
            },
            {
                'direction': 'out',
                'name': 'wfmInfo',
                'type': 'struct niScope_wfmInfo[]',
'documentation': {
'description': '''
Returns an array of structures with the following timing and scaling
information about each waveform:

-  **relativeInitialX**—the time (in seconds) from the trigger to the
   first sample in the fetched waveform
-  **absoluteInitialX**—timestamp (in seconds) of the first fetched
   sample. This timestamp is comparable between records and
   acquisitions; devices that do not support this parameter use 0 for
   this output.
-  **xIncrement**—the time between points in the acquired waveform in
   seconds
-  **actualSamples**—the actual number of samples fetched and placed in
   the waveform array
-  **gain**—the gain factor of the given channel; useful for scaling
   binary data with the following formula:

voltage = binary data × gain factor + offset

-  **offset**—the offset factor of the given channel; useful for scaling
   binary data with the following formula:

voltage = binary data × gain factor + offset

Call niScope_ActualNumWfms to determine the size of this array.
''',
},
            },
        ],
'documentation': {
'description': '''
Retrieves data from single channels and records. Returns a
one-dimensional array of complex binary 16-bit waveforms.
''',
},
    },
    'FetchMeasurement': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The channel to configure. For more information, refer to `Channel String
Syntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'ViReal64',
'documentation': {
'description': '''
The time to wait in seconds for data to be acquired; using 0 for this
parameter tells NI-SCOPE to fetch whatever is currently available. Using
-1 for this parameter implies infinite timeout.
''',
},
            },
            {
                'direction': 'in',
                'name': 'scalarMeasFunction',
                'type': 'ViInt32',
'documentation': {
'description': '''
The `scalar
measurement <REPLACE_DRIVER_SPECIFIC_URL_2(scalar_measurements_refs)>`__
to be performed.
''',
},
            },
            {
                'direction': 'out',
                'name': 'Result',
                'type': 'ViReal64[]',
'documentation': {
'description': '''
Contains an array of all measurements acquired; call
niScope_ActualNumWfms to determine the array length.
''',
},
            },
        ],
'documentation': {
'description': '''
Fetches a waveform from the digitizer and performs the specified
waveform measurement. Refer to `Using Fetch
Functions <REPLACE_DRIVER_SPECIFIC_URL_1(using_fetch_functions)>`__ for
more information.

Many of the measurements use the low, mid, and high reference levels.
You configure the low, mid, and high references by using
NISCOPE_ATTR_MEAS_CHAN_LOW_REF_LEVEL,
NISCOPE_ATTR_MEAS_CHAN_MID_REF_LEVEL, and
NISCOPE_ATTR_MEAS_CHAN_HIGH_REF_LEVEL to set each channel
differently.
''',
},
    },
    'FetchMeasurementStats': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The channel to configure. For more information, refer to `Channel String
Syntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'ViReal64',
'documentation': {
'description': '''
The time to wait in seconds for data to be acquired; using 0 for this
parameter tells NI-SCOPE to fetch whatever is currently available. Using
-1 for this parameter implies infinite timeout.
''',
},
            },
            {
                'direction': 'in',
                'name': 'scalarMeasFunction',
                'type': 'ViInt32',
'documentation': {
'description': '''
The `scalar
measurement <REPLACE_DRIVER_SPECIFIC_URL_2(scalar_measurements_refs)>`__
to be performed on each fetched waveform.
''',
},
            },
            {
                'direction': 'out',
                'name': 'Result',
                'type': 'ViReal64[]',
'documentation': {
'description': 'Returns the resulting measurement',
},
            },
            {
                'direction': 'out',
                'name': 'Mean',
                'type': 'ViReal64[]',
'documentation': {
'description': '''
Returns the mean scalar value, which is obtained by averaging each
niScope_FetchMeasurementStats call.
''',
},
            },
            {
                'direction': 'out',
                'name': 'Stdev',
                'type': 'ViReal64[]',
'documentation': {
'description': '''
Returns the standard deviation of the most recent **numInStats**
measurements.
''',
},
            },
            {
                'direction': 'out',
                'name': 'Min',
                'type': 'ViReal64[]',
'documentation': {
'description': '''
Returns the smallest scalar value acquired (the minimum of the
**numInStats** measurements).
''',
},
            },
            {
                'direction': 'out',
                'name': 'Max',
                'type': 'ViReal64[]',
'documentation': {
'description': '''
Returns the largest scalar value acquired (the maximum of the
**numInStats** measurements).
''',
},
            },
            {
                'direction': 'out',
                'name': 'numInStats',
                'type': 'ViInt32[]',
'documentation': {
'description': '''
Returns the number of times niScope_FetchMeasurementStats has been
called.
''',
},
            },
        ],
'documentation': {
'description': '''
Obtains a waveform measurement and returns the measurement value. This
function may return multiple statistical results depending on the number
of channels, the acquisition type, and the number of records you
specify.

You specify a particular measurement type, such as rise time, frequency,
or voltage peak-to-peak. The waveform on which the digitizer calculates
the waveform measurement is from an acquisition that you previously
initiated. The statistics for the specified measurement function are
returned, where the statistics are updated once every acquisition when
the specified measurement is fetched by any of the Fetch Measurement
functions. If a Fetch Measurement function has not been called, this
function fetches the data on which to perform the measurement. The
statistics are cleared by calling
niScope_ClearWaveformMeasurementStats. Refer to `Using Fetch
Functions <REPLACE_DRIVER_SPECIFIC_URL_1(using_fetch_functions)>`__ for
more information on incorporating fetch functions in your application.

Many of the measurements use the low, mid, and high reference levels.
You configure the low, mid, and high references with
NISCOPE_ATTR_MEAS_CHAN_LOW_REF_LEVEL,
NISCOPE_ATTR_MEAS_CHAN_MID_REF_LEVEL, and
NISCOPE_ATTR_MEAS_CHAN_HIGH_REF_LEVEL to set each channel
differently.
''',
},
    },
    'FetchWaveform': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Channel',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The channel to configure. For more information, refer to `channel String
Syntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.

Default Value: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'waveformSize',
                'type': 'ViInt32',
'documentation': {
'description': 'The number of elements to insert into the **waveform** array.',
},
            },
            {
                'direction': 'out',
                'name': 'Waveform',
                'type': 'ViReal64[]',
'documentation': {
'description': '''
Returns the waveform that the digitizer acquires.

Units: volts

| Notes:
| If the digitizer cannot sample a point in the waveform, this function
  returns an error.
''',
},
            },
            {
                'direction': 'out',
                'name': 'actualPoints',
                'type': 'ViInt32',
'documentation': {
'description': '''
Indicates the actual number of points the function placed in the
**waveform** array.
''',
},
            },
            {
                'direction': 'out',
                'name': 'initialX',
                'type': 'ViReal64',
'documentation': {
'description': '''
Indicates the time of the first point in the **waveform** array relative
to the Reference Position.

Units: seconds

For example, if the digitizer acquires the first point in the
**waveform** array 1 second before the trigger, this parameter returns
the value –1.0. If the acquisition of the first point occurs at the same
time as the trigger, this parameter returns the value 0.0.
''',
},
            },
            {
                'direction': 'out',
                'name': 'xIncrement',
                'type': 'ViReal64',
'documentation': {
'description': '''
Indicates the length of time between points in the **waveform** array.

Units: seconds
''',
},
            },
        ],
'documentation': {
'description': '''
Returns the waveform from a previously initiated acquisition that the
digitizer acquires for the channel you specify.

niScope_InitiateAcquisition starts an acquisition on the channels that
you enable with niScope_ConfigureVertical. The digitizer acquires
waveforms for the enabled channels concurrently. You use
niScope_AcquisitionStatus to determine when the acquisition is
complete. You must call this function separately for each enabled
channel to obtain the waveforms.

You can call niScope_ReadWaveform instead of
niScope_InitiateAcquisition. niScope_ReadWaveform starts an
acquisition on all enabled channels, waits for the acquisition to
complete, and returns the waveform for the channel you specify. Call
this function to obtain the waveforms for each of the remaining
channels.
''',
'note': '''
This function is included for compliance with the IviScope Class
Specification.
''',
},
    },
    'FetchWaveformMeasurement': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Channel',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The channel to configure. For more information, refer to `channel String
Syntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.

Default Value: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'measFunction',
                'type': 'ViInt32',
'documentation': {
'description': 'Characteristic of the acquired waveform to be measured.',
},
            },
            {
                'direction': 'out',
                'name': 'Measurement',
                'type': 'ViReal64',
'documentation': {
'description': 'The measured value.',
},
            },
        ],
'documentation': {
'description': '''
Configure the appropriate reference levels before calling this function.
You can configure the low, mid, and high references by setting the
following attributes:

| NISCOPE_ATTR_MEAS_HIGH_REF
| NISCOPE_ATTR_MEAS_LOW_REF
| NISCOPE_ATTR_MEAS_MID_REF
''',
'note': '''
This function is included for compliance with the IviScope Class
Specification.

You can use niScope_ReadWaveformMeasurement instead of this function.
niScope_ReadWaveformMeasurement starts an acquisition on all enabled
channels, waits for the acquisition to complete, obtains a waveform
measurement on the specified channel, and returns the waveform for the
specified channel. Call this function separately to obtain any other
waveform measurements on a specific channel.
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
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The channel to configure. For more information, refer to `Channel String
Syntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'The ID of an attribute.',
},
            },
            {
                'direction': 'out',
                'name': 'Value',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Returns the current value of the attribute; pass the address of a
ViBoolean variable.
''',
},
            },
        ],
'documentation': {
'description': '''
Queries the value of a ViBoolean attribute. You can use this function to
get the values of instrument-specific attributes and inherent IVI
attributes. If the attribute represents an instrument state, this
function performs instrument I/O in the following cases:

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
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The channel to configure. For more information, refer to `Channel String
Syntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'The ID of an attribute.',
},
            },
            {
                'direction': 'out',
                'name': 'Value',
                'type': 'ViInt32',
'documentation': {
'description': 'Returns the current value of the attribute.',
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
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The channel to configure. For more information, refer to `Channel String
Syntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'The ID of an attribute.',
},
            },
            {
                'direction': 'out',
                'name': 'Value',
                'type': 'ViInt64',
'documentation': {
'description': 'Returns the current value of the attribute.',
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
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The channel to configure. For more information, refer to `Channel String
Syntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'The ID of an attribute.',
},
            },
            {
                'direction': 'out',
                'name': 'Value',
                'type': 'ViReal64',
'documentation': {
'description': '''
Returns the current value of the attribute; pass the address of a
ViReal64 variable.
''',
},
            },
        ],
'documentation': {
'description': '''
Queries the value of a ViReal64 attribute. You can use this function to
get the values of instrument-specific attributes and inherent IVI
attributes. If the attribute represents an instrument state, this
function performs instrument I/O in the following cases:

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
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The channel to configure. For more information, refer to `Channel String
Syntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'The ID of an attribute.',
},
            },
            {
                'direction': 'out',
                'name': 'Value',
                'type': 'ViSession',
'documentation': {
'description': '''
Returns the current value of the attribute; pass the address of a
ViSession variable.
''',
},
            },
        ],
'documentation': {
'description': '''
Queries the value of a ViSession attribute. You can use this function to
get the values of instrument-specific attributes and inherent IVI
attributes. If the attribute represents an instrument state, this
function performs instrument I/O in the following cases:

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
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The channel to configure. For more information, refer to `Channel String
Syntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'The ID of an attribute.',
},
            },
            {
                'direction': 'in',
                'name': 'bufSize',
                'type': 'ViInt32',
'documentation': {
'description': 'The number of bytes in the ViChar array you specify for **value**.',
},
            },
            {
                'direction': 'out',
                'name': 'Value',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The buffer in which the function returns the current value of the
attribute; the buffer must be of type ViChar and have at least as many
bytes as indicated in the **bufSize**.
''',
},
            },
        ],
'documentation': {
'description': '''
Queries the value of a ViString attribute. You can use this function to
get the values of instrument-specific attributes and inherent IVI
attributes. If the attribute represents an instrument state, this
function performs instrument I/O in the following cases:

-  State caching is disabled for the entire session or for the
   particular attribute.
-  State caching is enabled and the currently cached value is invalid.

You must provide a ViChar array to serve as a buffer for the value. You
pass the number of bytes in the buffer as the **bufSize**. If the
current value of the attribute, including the terminating NUL byte, is
larger than the size you indicate in the **bufSize**, the function
copies (**bufSize** – 1) bytes into the buffer, places an ASCII NUL byte
at the end of the buffer, and returns the **bufSize** you must pass to
get the entire value. For example, if the value is 123456 and the
**bufSize** is 4, the function places 123 into the buffer and returns 7.
If you want to call this function just to get the required buffer size,
you can pass 0 for the **bufSize** and VI_NULL for the **value**.
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
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Index',
                'type': 'ViInt32',
'documentation': {
'description': 'A 1-based index into the channel table.',
},
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32',
'documentation': {
'description': '''
Passes the number of bytes in the ViChar array you specify for the
**description** parameter.

If the error description, including the terminating NULL byte, contains
more bytes than you indicate in this parameter, the function copies
BufferSize - 1 bytes into the buffer, places an ASCII NULL byte at the
end of the buffer, and returns the buffer size you must pass to get the
entire value. For example, if the value is "123456" and the Buffer Size
is 4, the function places "123" into the buffer and returns 7.

If you pass a negative number, the function copies the value to the
buffer regardless of the number of bytes in the value.
''',
},
            },
            {
                'direction': 'out',
                'name': 'channelString',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Returns the channel string that is in the channel table at the index you
specify. Do not modify the contents of the channel string.
''',
},
            },
        ],
'documentation': {
'description': '''
Returns the channel string that is in the channel table at an index you
specify. Not applicable to National Instruments digitizers.
''',
'note': '''
This function is included for compliance with the IviScope Class
Specification.
''',
},
    },
    'GetEqualizationFilterCoefficients': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channel',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The channel to configure. For more information, refer to `Channel String
Syntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.
''',
},
            },
            {
                'direction': 'in',
                'name': 'numberOfCoefficients',
                'type': 'ViInt32',
'documentation': {
'description': 'The number of coefficients being passed in the **coefficients** array.',
},
            },
            {
                'direction': 'out',
                'name': 'Coefficients',
                'type': 'ViReal64[]',
'documentation': {
'description': '''
The custom coefficients for the equalization FIR filter on the device.
These coefficients should be between +1 and –1. You can obtain the
number of coefficients from the
`NISCOPE_ATTR_EQUALIZATION_NUM_COEFFICIENTS <cviNISCOPE_ATTR_EQUALIZATION_NUM_COEFFICIENTS.html>`__
attribute.
''',
},
            },
        ],
'documentation': {
'description': '''
Retrieves the custom coefficients for the equalization FIR filter on the
device. This filter is designed to compensate the input signal for
artifacts introduced to the signal outside of the digitizer. Because
this filter is a generic FIR filter, any coefficients are valid.
Coefficient values should be between +1 and –1.
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
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'out',
                'name': 'errorCode',
                'type': 'ViStatus',
'documentation': {
'description': '''
Passes the number of bytes in the ViChar array you specify for the
Description parameter.

If the error description, including the terminating NULL byte, contains
more bytes than you indicate in this parameter, the function copies
**bufferSize** – 1 bytes into the buffer, places an ASCII NULL byte at
the end of the buffer, and returns the buffer size you must pass to get
the entire value. For example, if the value is "123456" and the Buffer
Size is 4, the function places "123" into the buffer and returns 7.

If you pass a negative number, the function copies the value to the
buffer regardless of the number of bytes in the value.

If you pass 0, you can pass VI_NULL for the **description** parameter.
''',
},
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32',
'documentation': {
'description': '''
Pass the Error Code that is returned from any of the instrument driver
functions.
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

If there is no description, the function returns an empty string. The
buffer must contain at least as many elements as the value you specify
with the Buffer Size parameter.

If you pass 0 for the **bufferSize**, you can pass VI_NULL for this
parameter.
''',
},
            },
        ],
'documentation': {
'description': '''
Reads an error code and message from the error queue. National
Instruments digitizers do not contain an error queue. Errors are
reported as they occur. Therefore, this function does not detect errors.
''',
'note': '''
This function is included for compliance with the IviScope Class
Specification.
''',
},
    },
    'GetErrorMessage': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'errorCode',
                'type': 'ViStatus',
'documentation': {
'description': '''
The error code that is returned from any of the instrument driver
functions.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Buffer_Size',
                'type': 'ViInt32',
'documentation': {
'description': 'The number of characters you specify for the **errorMessage** parameter.',
},
            },
            {
                'direction': 'out',
                'name': 'errorMessage',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Returns a char buffer that will be populated with the error message. It
should be at least as large as the buffer size.
''',
},
            },
        ],
'documentation': {
'description': '''
Returns the error code from an NI-SCOPE function as a user-readable
string. Use VI_NULL as the default instrument handle.

You must call this function twice. For the first call, set
**bufferSize** to 0 to prevent the function from populating the error
message. Instead, the function returns the size of the error string. Use
the returned size to create a buffer, then call the function again,
passing in the new buffer and setting **bufferSize** equal to the size
that was returned in the first function call.
''',
},
    },
    'GetFrequencyResponse': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channel',
                'type': 'ViConstString',
'documentation': {
'description': '''
The channel to configure. For more information, refer to `Channel String
Syntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.
''',
},
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32',
'documentation': {
'description': '''
The array size for the frequencies, amplitudes, and phases arrays that
you pass in to the other parameters.

To determine the sizes of the buffers to allocate for the frequencies,
amplitudes, and phases arrays, pass a value of 0 to the **buffer_size**
parameter and a value of NULL to the **frequencies** parameter. In this
case, the value returned by the **numberOfFrequencies** parameter is the
size of the arrays necessary to hold the frequencies, amplitudes, and
phases. Allocate three arrays of this size, then call this function
again (with correct **buffer_size** parameter) to retrieve the actual
values.
''',
},
            },
            {
                'direction': 'in',
                'name': 'frequencies',
                'type': 'ViReal64[]',
'documentation': {
'description': '''
The array of frequencies that corresponds with the amplitude and phase
response of the device.
''',
},
            },
            {
                'direction': 'in',
                'name': 'amplitudes',
                'type': 'ViReal64[]',
'documentation': {
'description': '''
The array of amplitudes that correspond with the magnitude response of
the device.
''',
},
            },
            {
                'direction': 'in',
                'name': 'phases',
                'type': 'ViReal64[]',
'documentation': {
'description': '''
The array of phases that correspond with the phase response of the
device.
''',
},
            },
            {
                'direction': 'out',
                'name': 'numberOfFrequencies',
                'type': 'ViInt32',
'documentation': {
'description': 'Returns the number of frequencies in the returned spectrum.',
},
            },
        ],
'documentation': {
'description': '''
Gets the frequency response of the digitizer for the current
configurations of the channel attributes. Not all digitizers support
this function.
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
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32',
'documentation': {
'description': '''
Passes the number of bytes in the ViChar array you specify for the
Description parameter.

If the error description, including the terminating NULL byte, contains
more bytes than you indicate in this parameter, the function copies
**bufferSize** – 1 bytes into the buffer, places an ASCII NULL byte at
the end of the buffer, and returns the buffer size you must pass to get
the entire value. For example, if the value is "123456" and the
**bufferSize** is 4, the function places "123" into the buffer and
returns 7.

If you pass a negative number, the function copies the value to the
buffer regardless of the number of bytes in the value.

If you pass 0, you can pass VI_NULL for the Description buffer
parameter.
''',
},
            },
            {
                'direction': 'out',
                'name': 'Record',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Returns the next coercion record for the IVI session. If there are no
coercions records, the function returns an empty string. The buffer must
contain at least as many elements as the value you specify with the
**bufferSize** parameter.
''',
},
            },
        ],
'documentation': {
'description': '''
Returns the coercion information associated with the IVI session. This
function retrieves and clears the oldest instance in which the
instrument driver coerced a value you specified to another value.

If you set NISCOPE_ATTR_RECORD_COERCIONS to VI_TRUE, NI-SCOPE keeps
a list of all coercions it makes on ViInt32 or ViReal64 values that you
pass to instrument driver functions. Use this function to retrieve
information from that list.
''',
'note': '''
This function is included for compliance with the IviScope Class
Specification.
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
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32',
'documentation': {
'description': '''
Passes the number of bytes in the ViChar array you specify for the
**Description** parameter.

If the error description, including the terminating NULL byte, contains
more bytes than you indicate in this parameter, the function copies
**bufferSize**; – 1 bytes into the buffer, places an ASCII NULL byte at
the end of the buffer, and returns the buffer size you must pass to get
the entire value. For example, if the value is "123456" and the Buffer
Size is 4, the function places "123" into the buffer and returns 7.

If you pass a negative number, the function copies the value to the
buffer regardless of the number of bytes in the value.

If you pass 0, you can pass VI_NULL for the Description buffer
parameter.
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
no interchange warnings, the function returns an empty string. The
buffer must contain at least as many elements as the value you specify
with the **bufferSize** parameter.
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
cause different behavior.

Use this function to retrieve interchangeability warnings. The driver
performs interchangeability checking when
NISCOPE_ATTR_INTERCHANGE_CHECK is set to VI_TRUE. The function
returns an empty string in the **interchangeWarning** parameter if no
interchangeability warnings remain for the session.

In general, the instrument driver generates interchangeability warnings
when an attribute that affects the behavior of the instrument is in a
state that you did not specify.
''',
'note': '''
This function is included for compliance with the IviScope Class
Specification.
''',
},
    },
    'GetNormalizationCoefficients': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViConstString',
'documentation': {
'description': '''
The channel to configure. For more information, refer to `Channel String
Syntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.
''',
},
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'ViInt32',
'documentation': {
'description': '''
The array size for the **coefficentInfo** parameter.

To determine the size of the buffer to allocate for **coefficientInfo**,
pass a value of 0 to the **buffersize** parameter and a value of NULL to
the **coefficientInfo** parameter. In this case, the return value of the
**numberOfCoefficientSets** parameter is the size of the array necessary
to hold the coefficient structures. Allocate an array of
niScope_coefficientInfo structures of this size, then call this
function again (with the correct **bufferSize** parameter) to retrieve
the actual values.
''',
},
            },
            {
                'direction': 'in',
                'name': 'coefficientInfo',
                'type': 'void',
'documentation': {
'description': '''
An array of structures containing gain and offset coefficients for a
given channel.
''',
},
            },
            {
                'direction': 'out',
                'name': 'numberOfCoefficientSets',
                'type': 'ViInt32',
'documentation': {
'description': '''
Returns the number of coefficient sets returned in the
**coefficientInfo** array.
''',
},
            },
        ],
'documentation': {
'description': '''
Returns coefficients that can be used to convert binary data to
normalized and calibrated data.

Refer to `Scaling and Normalization of Binary
Data <Digitizers.chm::/scaling_and_norm_binary_data.html>`__ for more
information about how to use this function.
''',
},
    },
    'GetScalingCoefficients': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViConstString',
'documentation': {
'description': '''
The channel to configure. For more information, refer to `Channel String
Syntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.
''',
},
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'ViInt32',
'documentation': {
'description': '''
The array size for the **coefficentInfo** parameter.

To determine the size of the buffer to allocate for **coefficientInfo**,
pass a value of 0 to the **buffersize** parameter and a value of NULL to
the **coefficientInfo** parameter. In this case, the return value of the
**numberOfCoefficientSets** parameter is the size of the array necessary
to hold the coefficient structures. Allocate an array of
niScope_coefficientInfo structures of this size, then call this
function again (with the correct **bufferSize** parameter) to retrieve
the actual values.
''',
},
            },
            {
                'direction': 'in',
                'name': 'coefficientInfo',
                'type': 'void',
'documentation': {
'description': '''
An array of structures containing gain and offset coefficients for a
given channel.
''',
},
            },
            {
                'direction': 'out',
                'name': 'numberOfCoefficientSets',
                'type': 'ViInt32',
'documentation': {
'description': '''
Returns the number of coefficient sets returned in the
**coefficientInfo** array.
''',
},
            },
        ],
'documentation': {
'description': '''
Returns coefficients that can be used to scale binary data to volts.

Refer to `Scaling and Normalization of Binary
Data <Digitizers.chm::/scaling_and_norm_binary_data.html>`__ for more
information about how to use this function.
''',
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
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'streamName',
                'type': 'ViConstString',
'documentation': {
'description': '''
The stream endpoint FIFO to configure. Refer to the device-specific
documentation for peer-to-peer streaming in the *High-Speed Digitizers
Help* for more information.
''',
},
            },
            {
                'direction': 'out',
                'name': 'writerHandle',
                'type': 'ViUInt32',
'documentation': {
'description': '''
Returns a reference to a peer-to-peer writer FIFO that can be used to
create a peer-to-peer streaming session.
''',
},
            },
        ],
'documentation': {
'description': '''
Returns a writer endpoint that can be used with NI-P2P to configure a
peer-to-peer stream with a digitizer endpoint.

-  `Peer-to-Peer Streaming <digitizers.chm::/5160_P2P.html>`__
''',
},
    },
    'ImportAttributeConfigurationBuffer': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'sizeInBytes',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the size, in bytes, of the byte array to import. If you enter
0, this function returns the needed size.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Configuration',
                'type': 'ViAddr',
'documentation': {
'description': '''
Specifies the byte array buffer that contains the attribute
configuration to import.
''',
},
            },
        ],
'documentation': {
'description': '''
Imports an attribute configuration to the session from the specified
configuration buffer.

You can export and import session attribute configurations only between
devices with identical model numbers, channel counts, and onboard memory
sizes.

**Related Topics:**

`Attributes and Attribute
Functions <REPLACE_DRIVER_SPECIFIC_URL_1(attributes_and_attribute_functions)>`__

`Setting Attributes Before Reading
Attributes <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__
''',
'note': '''
You cannot call this function while the session is in a running state,
such as while acquiring a signal.
''',
},
    },
    'ImportAttributeConfigurationFile': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'filePath',
                'type': 'ViConstString',
'documentation': {
'description': '''
Specifies the absolute path to the file containing the attribute
configuration to import. If you specify an empty or relative path, this
function returns an error.
**Default File Extension:** .niscopeconfig
''',
},
            },
        ],
'documentation': {
'description': '''
Imports an attribute configuration to the session from the specified
file.

You can export and import session attribute configurations only between
devices with identical model numbers, channel counts, and onboard memory
sizes.

**Related Topics:**

`Attributes and Attribute
Functions <REPLACE_DRIVER_SPECIFIC_URL_1(attributes_and_attribute_functions)>`__

`Setting Attributes Before Reading
Attributes <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__
''',
'note': '''
You cannot call this function while the session is in a running state,
such as while acquiring a signal.
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
program, you must make sure that the name you use matches the name in
the IVI Configuration Store file exactly, without any variations in the
case of the characters.
''',
'description': '''
| Specifies the resource name of the device to initialize

For Traditional NI-DAQ devices, the syntax is DAQ::\ *n*, where *n* is
the device number assigned by MAX, as shown in Example 1.

For NI-DAQmx devices, the syntax is just the device name specified in
MAX, as shown in Example 2. Typical default names for NI-DAQmx devices
in MAX are Dev1 or PXI1Slot1. You can rename an NI-DAQmx device by
right-clicking on the name in MAX and entering a new name.

An alternate syntax for NI-DAQmx devices consists of DAQ::NI-DAQmx
device name, as shown in Example 3. This naming convention allows for
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
'table_body': [['1', 'Traditional NI-DAQ device', 'DAQ::1 (1 = device number)'], ['2', 'NI-DAQmx device', 'myDAQmxDevice (myDAQmxDevice = device name)'], ['3', 'NI-DAQmx device', 'DAQ::myDAQmxDevice (myDAQmxDevice = device name)'], ['4', 'NI-DAQmx device', 'DAQ::2 (2 = device name)'], ['5', 'IVI logical name or IVI virtual name', 'myLogicalName (myLogicalName = name)']],
'table_header': ['Example', 'Device Type', 'Syntax'],
},
            },
            {
                'direction': 'in',
                'name': 'idQuery',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Specify whether to perform an ID query.

When you set this parameter to VI_TRUE, NI-SCOPE verifies that the
device you initialize is a type that it supports.

When you set this parameter to VI_FALSE, the function initializes the
device without performing an ID query.

**Defined Values**

| VI_TRUE—Perform ID query
| VI_FALSE—Skip ID query

**Default Value**: VI_TRUE
''',
},
            },
            {
                'direction': 'in',
                'name': 'resetDevice',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Specify whether to reset the device during the initialization process.

Default Value: VI_TRUE

**Defined Values**

VI_TRUE (1)—Reset device

VI_FALSE (0)—Do not reset device
''',
'note': '''
For the NI 5112, repeatedly resetting the device may cause excessive
wear on the electromechanical relays. Refer to `NI 5112
Electromechanical Relays <REPLACE_DRIVER_SPECIFIC_URL_1(5112_relays)>`__
for recommended programming practices.
''',
},
            },
            {
                'direction': 'in',
                'name': 'optionString',
                'type': 'ViString',
'documentation': {
'description': '''
| Specifies initialization commands. The following table lists the
  attributes and the name you use in the **optionString** to identify
  the attribute.

Default Values: "Simulate=0,RangeCheck=1,QueryInstrStatus=1,Cache=1"

You can use the option string to simulate a device. The DriverSetup flag
specifies the model that is to be simulated and the type of the model.
One example to simulate an NI PXI-5102 would be as follows:

Option String: Simulate = 1, DriverSetup = Model:5102; BoardType:PXI

Refer to the example niScope EX Simulated Acquisition for more
information on simulation.

You can also use the option string to attach an accessory such as the
NI 5900 to your digitizer session to allow the seamless use of the
accessory:

Option String: DriverSetup = Accessory:Dev1

Refer to the example niScope EX External Amplifier for more information.
''',
'table_body': [],
},
            },
            {
                'direction': 'out',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
Returns a session handle that you can use to identify the device in all
subsequent NI-SCOPE function calls.
''',
},
            },
        ],
'documentation': {
'description': '''
Performs the following initialization actions:

-  Creates a new IVI instrument driver and optionally sets the initial
   state of the following session properties: Range Check, Cache,
   Simulate, Record Value Coercions
-  Opens a session to the specified device using the interface and
   address you specify for the **resourceName**
-  Resets the digitizer to a known state if **resetDevice** is set to
   VI_TRUE
-  Queries the instrument ID and verifies that it is valid for this
   instrument driver if the **IDQuery** is set to VI_TRUE
-  Returns an instrument handle that you use to identify the instrument
   in all subsequent instrument driver function calls
''',
},
    },
    'InitiateAcquisition': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
        ],
'documentation': {
'description': '''
Initiates a waveform acquisition.

After calling this function, the digitizer leaves the Idle state and
waits for a trigger. The digitizer acquires a waveform for each channel
you enable with niScope_ConfigureVertical.
''',
},
    },
    'IsDeviceReady': {
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
program, you must make sure that the name you use matches the name in
the IVI Configuration Store file exactly, without any variations in the
case of the characters.
''',
'description': '''
**resourceName** specifies the resource name of the device to
initialize.

resourceName Examples

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
'table_body': [['1', 'Traditional NI-DAQ device', 'DAQ::\\ *1*', '(*1* = device number)'], ['2', 'NI-DAQmx device', '*myDAQmxDevice*', '(*myDAQmxDevice* = device name)'], ['3', 'NI-DAQmx device', 'DAQ::\\ *myDAQmxDevice*', '(*myDAQmxDevice* = device name)'], ['4', 'NI-DAQmx device', 'DAQ::\\ *2*', '(*2* = device name)']],
'table_header': ['Example #', 'Device Type', 'Syntax', 'Variable'],
},
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Use only "" or a null pointer. If you specify a channel, NI-SCOPE will
return an error.
''',
},
            },
            {
                'direction': 'out',
                'name': 'deviceReady',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Returns True if the device is ready to use, or False if the device is
still initializing.
''',
},
            },
        ],
'documentation': {
'description': '''
Call this function to determine whether the device is ready for use or
the device is still undergoing initialization.
''',
},
    },
    'IsInvalidWfmElement': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'elementValue',
                'type': 'ViReal64',
'documentation': {
'description': '''
Pass one of the values from the waveform array returned by the read and
fetch waveform functions.
''',
},
            },
            {
                'direction': 'out',
                'name': 'isInvalid',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Returns whether the element value is a valid voltage or a value
indicating that the digitizer could not sample a voltage.

Return values:

| VI_TRUE—The element value indicates that the instrument could not
  sample the voltage.
| VI_FALSE—The element value is a valid voltage.
''',
},
            },
        ],
'documentation': {
'description': '''
Determines whether a value you pass from the waveform array is invalid.
After the read and fetch waveform functions execute, each element in the
waveform array contains either a voltage or a value indicating that the
instrument could not sample a voltage.
''',
'note': '''
This function is included for compliance with the IviScope Class
Specification.
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
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'out',
                'name': 'callerHasLock',
                'type': 'ViBoolean',
'documentation': {
'description': '''
This parameter serves as a convenience. If you do not want to use this
parameter, pass VI_NULL.

Use this parameter in complex functions to keep track of whether you
have obtained a lock and therefore need to unlock the session. Pass the
address of a local ViBoolean variable. In the declaration of the local
variable, initialize it to VI_FALSE. Pass the address of the same local
variable to any other calls you make to niScope_LockSession or
niScope_UnlockSession in the same function.
''',
},
            },
        ],
'documentation': {
'description': '''
Obtains a multithread lock on the instrument session. Before doing so,
it waits until all other execution threads have released their locks on
the instrument session. Other threads might have obtained a lock on this
session in the following ways:

-  Your application called niScope_LockSession
-  A call to the instrument driver locked the session
-  A call to the IVI engine locked the session

After your call to niScope_LockSession returns successfully, no other
threads can access the instrument session until you call
niScope_UnlockSession. Use niScope_LockSession and
niScope_UnlockSession around a sequence of calls to instrument driver
functions if you require that the instrument retain its settings through
the end of the sequence.

You can safely make nested calls to niScope_LockSession within the same
thread. To completely unlock the session, you must balance each call to
niScope_LockSession with a call to niScope_UnlockSession. If, however,
you use the **callerHasLock** in all calls to niScope_LockSession and
niScope_UnlockSession within a function, the IVI Library locks the
session only once within the function regardless of the number of calls
you make to niScope_LockSession. This allows you to call
niScope_UnlockSession just once at the end of the function.
''',
},
    },
    'ProbeCompensationSignalStart': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
        ],
'documentation': {
'description': 'Starts the 1 kHz square wave output on PFI 1 for probe compensation.',
},
    },
    'ProbeCompensationSignalStop': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
        ],
'documentation': {
'description': 'Stops the 1 kHz square wave output on PFI 1 for probe compensation.',
},
    },
    'Read': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The channel to configure. For more information, refer to `Channel String
Syntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'ViReal64',
'documentation': {
'description': '''
The time to wait in seconds for data to be acquired; using 0 for this
parameter tells NI-SCOPE to fetch whatever is currently available. Using
-1 for this parameter implies infinite timeout.
''',
},
            },
            {
                'direction': 'in',
                'name': 'numSamples',
                'type': 'ViInt32',
'documentation': {
'description': '''
The maximum number of samples to fetch for each waveform. If the
acquisition finishes with fewer points than requested, some devices
return partial data if the acquisition finished, was aborted, or a
timeout of 0 was used. If it fails to complete within the timeout
period, the function returns an error.
''',
},
            },
            {
                'direction': 'out',
                'name': 'Wfm',
                'type': 'ViReal64[]',
'documentation': {
'description': '''
Returns an array whose length is the **numSamples** times number of
waveforms. Call niScope_ActualNumwfms to determine the number of
waveforms.

NI-SCOPE returns this data sequentially, so all record 0 waveforms are
first. For example, with a channel list of 0,1, you would have the
following index values:

index 0 = record 0, channel 0

index *x* = record 0, channel 1

index 2\ *x* = record 1, channel 0

index 3\ *x* = record 1, channel 1

Where *x* = the record length
''',
},
            },
            {
                'direction': 'out',
                'name': 'wfmInfo',
                'type': 'struct niScope_wfmInfo[]',
'documentation': {
'description': '''
Returns an array of structures with the following timing and scaling
information about each waveform:

-  **relativeInitialX**—the time (in seconds) from the trigger to the
   first sample in the fetched waveform
-  **absoluteInitialX**—timestamp (in seconds) of the first fetched
   sample. This timestamp is comparable between records and
   acquisitions; devices that do not support this parameter use 0 for
   this output.
-  **xIncrement**—the time between points in the acquired waveform in
   seconds
-  **actualSamples**—the actual number of samples fetched and placed in
   the waveform array
-  **gain**—the gain factor of the given channel; useful for scaling
   binary data with the following formula:

voltage = binary data × gain factor + offset

-  **offset**—the offset factor of the given channel; useful for scaling
   binary data with the following formula:

voltage = binary data × gain factor + offset

Call niScope_ActualNumWfms to determine the size of this array.
''',
},
            },
        ],
'documentation': {
'description': '''
Initiates an acquisition, waits for it to complete, and retrieves the
data. The process is similar to calling niScope_InitiateAcquisition,
niScope_AcquisitionStatus, and niScope_Fetch. The only difference is
that with niScope_Read, you enable all channels specified with
**channelList** before the acquisition; in the other method, you enable
the channels with niScope_ConfigureVertical.

This function may return multiple waveforms depending on the number of
channels, the acquisition type, and the number of records you specify.
''',
'note': '''
Some functionality is not supported in all digitizers. Refer to
`Features Supported by
Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
more information.
''',
},
    },
    'ReadMeasurement': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The channel to configure. For more information, refer to `Channel String
Syntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'ViReal64',
'documentation': {
'description': '''
The time to wait in seconds for data to be acquired; using 0 for this
parameter tells NI-SCOPE to fetch whatever is currently available. Using
-1 for this parameter implies infinite timeout.
''',
},
            },
            {
                'direction': 'in',
                'name': 'scalarMeasFunction',
                'type': 'ViInt32',
'documentation': {
'description': '''
The `scalar
measurement <REPLACE_DRIVER_SPECIFIC_URL_2(scalar_measurements_refs)>`__
to be performed
''',
},
            },
            {
                'direction': 'out',
                'name': 'Result',
                'type': 'ViReal64[]',
'documentation': {
'description': '''
Contains an array of all measurements acquired. Call
niScope_ActualNumWfms to determine the array length.
''',
},
            },
        ],
'documentation': {
'description': '''
Initiates an acquisition, waits for it to complete, and performs the
specified waveform measurement for a single channel and record or for
multiple channels and records.

Refer to `Using Fetch
Functions <REPLACE_DRIVER_SPECIFIC_URL_1(using_fetch_functions)>`__ for
more information.

Many of the measurements use the low, mid, and high reference levels.
You configure the low, mid, and high references by using
NISCOPE_ATTR_MEAS_CHAN_LOW_REF_LEVEL,
NISCOPE_ATTR_MEAS_CHAN_MID_REF_LEVEL, and
NISCOPE_ATTR_MEAS_CHAN_HIGH_REF_LEVEL to set each channel
differently.
''',
},
    },
    'ReadWaveform': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Channel',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The channel to configure. For more information, refer to `channel String
Syntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.

Default Value: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'waveformSize',
                'type': 'ViInt32',
'documentation': {
'description': 'The number of elements to insert into the **waveform** array.',
},
            },
            {
                'direction': 'in',
                'name': 'MaxTime',
                'type': 'ViInt32',
'documentation': {
'description': '''
Pass the maximum length of time in which to allow the read waveform
operation to complete.

If the operation does not complete within this time interval, the
function returns the NISCOPE_ERROR_MAX_TIME_EXCEEDED error code.
When this occurs, you can call niScope_Abort to cancel the read
waveform operation and return the digitizer to the idle state.

Units: milliseconds

| Other Defined Values
| NISCOPE_VAL_MAX_TIME_NONE
| NISCOPE_VAL_MAX_TIME_INFINITE
''',
},
            },
            {
                'direction': 'out',
                'name': 'Waveform',
                'type': 'ViReal64[]',
'documentation': {
'description': '''
Returns the waveform that the digitizer acquires.
Units: volts
''',
},
            },
            {
                'direction': 'out',
                'name': 'actualPoints',
                'type': 'ViInt32',
'documentation': {
'description': '''
Indicates the actual number of points the function placed in the
**waveform** array.
''',
},
            },
            {
                'direction': 'out',
                'name': 'initialX',
                'type': 'ViReal64',
'documentation': {
'description': '''
Indicates the time of the first point in the **waveform** array relative
to the Reference Position.

Units: seconds

For example, if the digitizer acquires the first point in the
**waveform** array 1 second before the trigger, this parameter returns
the value –1.0. If the acquisition of the first point occurs at the same
time as the trigger, this parameter returns the value 0.0.
''',
},
            },
            {
                'direction': 'out',
                'name': 'xIncrement',
                'type': 'ViReal64',
'documentation': {
'description': '''
Indicates the length of time between points in the **waveform** array.

Units: seconds
''',
},
            },
        ],
'documentation': {
'description': '''
Initiates an acquisition on the channels that you enable with
niScope_ConfigureVertical. This function then waits for the acquisition
to complete and returns the waveform for the channel you specify. Call
niScope_FetchWaveform to obtain the waveforms for each of the remaining
enabled channels without initiating another acquisition.

Use niScope_ActualRecordLength to determine the required size for the
**waveform** array.
''',
'note': '''
This function is included for compliance with the IviScope Class
Specification.
''',
},
    },
    'ReadWaveformMeasurement': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Channel',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The channel to configure. For more information, refer to `channel String
Syntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.

Default Value: "0"
''',
},
            },
            {
                'direction': 'in',
                'name': 'measFunction',
                'type': 'ViInt32',
'documentation': {
'description': 'The scalar measurement to perform.',
},
            },
            {
                'direction': 'in',
                'name': 'maxTime',
                'type': 'ViInt32',
'documentation': {
'description': '''
Pass the maximum length of time in which to allow the read waveform
operation to complete.

If the operation does not complete within this time interval, the
function returns the NISCOPE_ERROR_MAX_TIME_EXCEEDED error code.
When this occurs, you can call niScope_Abort to cancel the read
waveform operation and return the digitizer to the idle state.

Units: milliseconds
''',
},
            },
            {
                'direction': 'out',
                'name': 'Measurement',
                'type': 'ViReal64',
'documentation': {
'description': 'The measured value.',
},
            },
        ],
'documentation': {
'description': '''
Initiates a new waveform acquisition and returns a specified waveform
measurement from a specific channel.

This function initiates an acquisition on the channels that you enable
with the niScope_ConfigureVertical function. It then waits for the
acquisition to complete, obtains a waveform measurement on the channel
you specify, and returns the measurement value. You specify a particular
measurement type, such as rise time, frequency, or voltage peak-to-peak.

You can call the niScope_FetchWaveformMeasurement function separately
to obtain any other waveform measurement on a specific channel without
initiating another acquisition.

You must configure the appropriate reference levels before calling this
function. Configure the low, mid, and high references by calling
niScope_ConfigureRefLevels or by setting the following attributes:

| NISCOPE_ATTR_MEAS_HIGH_REF
| NISCOPE_ATTR_MEAS_LOW_REF
| NISCOPE_ATTR_MEAS_MID_REF
''',
'note': '''
This function is included for compliance with the IviScope Class
Specification.
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
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
        ],
'documentation': {
'description': '''
Performs a hard reset of the device. Acquisition stops, all routes are
released, RTSI and PFI lines are tristated, hardware is configured to
its default state, and all session attributes are reset to their default
state.

-  `Thermal Shutdown <digitizers.chm::/Thermal_Shutdown.html>`__
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
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
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

| If a particular test module does not completely configure the state of
  an instrument, the state of the instrument depends on the
  configuration from a previously executed test module.
| If you execute the test modules in a different order, the behavior of
  the instrument and therefore the entire test module is likely to
  change.

| This change in behavior is generally instrument-specific and
  represents an interchangeability problem. You can use this function to
  test for such cases. After you call this function, the
  interchangeability checking algorithms in the specific driver ignore
  all previous configuration operations.
| By calling this function at the beginning of a test module, you can
  determine whether the test module has dependencies on the operation of
  previously executed test modules.

This function does not clear the interchangeability warnings from the
list of previously recorded interchangeability warnings. If you want to
guarantee that niScope_GetNextInterchangeWarning only returns those
interchangeability warnings that are generated after calling this
function, you must clear the list of interchangeability warnings.

You can clear the interchangeability warnings list by repeatedly calling
niScope_GetNextInterchangeWarning until no more interchangeability
warnings are returned. If you are not interested in the content of those
warnings, you can call niScope_ClearInterchangeWarnings.
''',
'note': '''
This function is included for compliance with the IviScope Class
Specification.
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
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
        ],
'documentation': {
'description': '''
Performs a software reset of the device, returning it to the default
state and applying any initial default settings from the IVI
Configuration Store.
''',
},
    },
    'SampleMode': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'out',
                'name': 'sampleMode',
                'type': 'ViInt32',
'documentation': {
'description': '''
Returns the sample mode the digitizer is currently using; NI-SCOPE
returns the value of the NISCOPE_ATTR_SAMPLE_MODE attribute.
''',
},
            },
        ],
'documentation': {
'description': 'Returns the sample mode the digitizer is currently using.',
},
    },
    'SampleRate': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'out',
                'name': 'sampleRate',
                'type': 'ViReal64',
'documentation': {
'description': '''
Returns the effective sample rate of the acquired waveform the digitizer
acquires for each channel; the driver returns the value held in the
NISCOPE_ATTR_HORZ_SAMPLE_RATE attribute.
''',
},
            },
        ],
'documentation': {
'description': '''
Returns the effective sample rate, in samples per second, of the
acquired waveform using the current configuration. Refer to `Coercions
of Horizontal
Parameters <REPLACE_DRIVER_SPECIFIC_URL_1(horizontal_parameters)>`__ for
more information about sample rate coercion.
''',
},
    },
    'SendSWTrigger': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
        ],
'documentation': {
'description': '''
Sends a command to trigger the digitizer. Call this function after you
call niScope_ConfigureTriggerSoftware.
''',
'note': '''
This function is included for compliance with the IviScope Class
Specification. Consider using niScope_SendSoftwareTriggerEdge instead.
''',
},
    },
    'SendSoftwareTriggerEdge': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'whichTrigger',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the type of trigger to send to the digitizer.

**Defined Values**

| NISCOPE_VAL_SOFTWARE_TRIGGER_START (0L)
|  NISCOPE_VAL_SOFTWARE_TRIGGER_ARM_REFERENCE (1L)
| NISCOPE_VAL_SOFTWARE_TRIGGER_REFERENCE (2L)
| NISCOPE_VAL_SOFTWARE_TRIGGER_ADVANCE (3L)
''',
},
            },
        ],
'documentation': {
'description': '''
Sends the selected trigger to the digitizer. Call this function if you
called niScope_ConfigureTriggerSoftware when you want the Reference
trigger to occur. You can also call this function to override a misused
edge, digital, or hysteresis trigger. If you have configured
NISCOPE_ATTR_ACQ_ARM_SOURCE, NISCOPE_ATTR_ARM_REF_TRIG_SRC, or
NISCOPE_ATTR_ADV_TRIG_SRC, call this function when you want to send
the corresponding trigger to the digitizer.
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
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The channel to configure. For more information, refer to `Channel String
Syntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'The ID of an attribute.',
},
            },
            {
                'direction': 'in',
                'name': 'Value',
                'type': 'ViBoolean',
'documentation': {
'description': '''
The value that you want to set the attribute to. Some values might not
be valid depending on the current settings of the instrument session.
''',
},
            },
        ],
'documentation': {
'description': '''
Sets the value of a ViBoolean attribute. This is a low-level function
that you can use to set the values of instrument-specific attributes and
inherent IVI attributes. If the attribute represents an instrument
state, this function performs instrument I/O in the following cases:

-  State caching is disabled for the entire session or for the
   particular attribute.
-  State caching is enabled and the currently cached value is invalid or
   is different than the value you specify.
''',
'note': '''
NI-SCOPE contains high-level functions that set most of the instrument
attributes. Use the high-level driver functions as much as possible
because they handle order dependencies and multithread locking for you.
In addition, the high-level functions perform status checking only after
setting all of the attributes. In contrast, when you set multiple
attributes using the SetAttribute functions, the functions check the
instrument status after each call. Also, when state caching is enabled,
the high-level functions that configure multiple attributes perform
instrument I/O only for the attributes whose value you change. Thus, you
can safely call the high-level functions without the penalty of
redundant instrument I/O.
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
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The channel to configure. For more information, refer to `Channel String
Syntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'The ID of an attribute.',
},
            },
            {
                'direction': 'in',
                'name': 'Value',
                'type': 'ViInt32',
'documentation': {
'description': '''
The value that you want to set the attribute. Some values might not be
valid depending on the current settings of the instrument session.
''',
},
            },
        ],
'documentation': {
'description': '''
Sets the value of a ViInt32 attribute. This is a low-level function that
you can use to set the values of instrument-specific attributes and
inherent IVI attributes. If the attribute represents an instrument
state, this function performs instrument I/O in the following cases:

-  State caching is disabled for the entire session or for the
   particular attribute.
-  State caching is enabled and the currently cached value is invalid or
   is different than the value you specify.
''',
'note': '''
NI-SCOPE contains high-level functions that set most of the instrument
attributes. Use the high-level functions as much as possible because
they handle order dependencies and multithread locking for you. In
addition, high-level functions perform status checking only after
setting all of the attributes. In contrast, when you set multiple
attributes using the Set Attribute functions, the functions check the
instrument status after each call. Also, when state caching is enabled,
the high-level functions that configure multiple attributes perform
instrument I/O only for the attributes whose value you change. Thus, you
can safely call the high-level functions without the penalty of
redundant instrument I/O.
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
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The channel to configure. For more information, refer to `Channel String
Syntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'The ID of an attribute.',
},
            },
            {
                'direction': 'in',
                'name': 'Value',
                'type': 'ViInt64',
'documentation': {
'description': '''
The value that you want to set the attribute. Some values might not be
valid depending on the current settings of the instrument session.
''',
},
            },
        ],
'documentation': {
'description': '''
Sets the value of a ViInt64 attribute. This is a low-level function that
you can use to set the values of instrument-specific attributes and
inherent IVI attributes. If the attribute represents an instrument
state, this function performs instrument I/O in the following cases:

-  State caching is disabled for the entire session or for the
   particular attribute.
-  State caching is enabled and the currently cached value is invalid or
   is different than the value you specify.
''',
'note': '''
NI-SCOPE contains high-level functions that set most of the instrument
attributes. Use the high-level functions as much as possible because
they handle order dependencies and multithread locking for you. In
addition, high-level functions perform status checking only after
setting all of the attributes. In contrast, when you set multiple
attributes using the Set Attribute functions, the functions check the
instrument status after each call. Also, when state caching is enabled,
the high-level functions that configure multiple attributes perform
instrument I/O only for the attributes whose value you change. Thus, you
can safely call the high-level functions without the penalty of
redundant instrument I/O.
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
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The channel to configure. For more information, refer to `Channel String
Syntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'The ID of an attribute.',
},
            },
            {
                'direction': 'in',
                'name': 'Value',
                'type': 'ViReal64',
'documentation': {
'description': '''
The value that you want to set the attribute to. Some values might not
be valid depending on the current settings of the instrument session.
''',
},
            },
        ],
'documentation': {
'description': '''
Sets the value of a ViReal64 attribute. This is a low-level function
that you can use to set the values of instrument-specific attributes and
inherent IVI attributes. If the attribute represents an instrument
state, this function performs instrument I/O in the following cases:

-  State caching is disabled for the entire session or for the
   particular attribute.
-  State caching is enabled and the currently cached value is invalid or
   is different than the value you specify.
''',
'note': '''
NI-SCOPE contains high-level functions that set most of the instrument
attributes. Use the high-level driver functions as much as possible
because they handle order dependencies and multithread locking for you.
In addition, the high-level functions perform status checking only after
setting all of the attributes. In contrast, when you set multiple
attributes using the Set Attribute functions, the functions check the
instrument status after each call. Also, when state caching is enabled,
the high-level functions that configure multiple attributes perform
instrument I/O only for the attributes whose value you change. Thus, you
can safely call the high-level functions without the penalty of
redundant instrument I/O.
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
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The channel to configure. For more information, refer to `Channel String
Syntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'The ID of an attribute.',
},
            },
            {
                'direction': 'in',
                'name': 'Value',
                'type': 'ViSession',
'documentation': {
'description': '''
The value that you want to set the attribute to. Some values might not
be valid depending on the current settings of the instrument session.
''',
},
            },
        ],
'documentation': {
'description': '''
Sets the value of a ViSession attribute. This is a low-level function
that you can use to set the values of instrument-specific attributes and
inherent IVI attributes. If the attribute represents an instrument
state, this function performs instrument I/O in the following cases:

-  State caching is disabled for the entire session or for the
   particular attribute.
-  State caching is enabled and the currently cached value is invalid or
   is different than the value you specify.
''',
'note': '''
NI-SCOPE contains high-level functions that set most of the instrument
attributes. Use the high-level driver functions as much as possible
because they handle order dependencies and multithread locking for you.
In addition, the high-level functions perform status checking only after
setting all of the attributes. In contrast, when you set multiple
attributes using the Set Attribute functions, the functions check the
instrument status after each call. Also, when state caching is enabled,
the high-level functions that configure multiple attributes perform
instrument I/O only for the attributes whose value you change. Thus, you
can safely call the high-level functions without the penalty of
redundant instrument I/O.
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
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The channel to configure. For more information, refer to `Channel String
Syntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': 'The ID of an attribute.',
},
            },
            {
                'direction': 'in',
                'name': 'Value',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The value that you want to set the attribute to. Some values might not
be valid depending on the current settings of the instrument session.
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
''',
'note': '''
NI-SCOPE contains high-level functions that set most of the instrument
attributes. Use the high-level driver functions as much as possible
because they handle order dependencies and multithread locking for you.
In addition, the high-level functions perform status checking only after
setting all of the attributes. In contrast, when you set multiple
attributes using the SetAttribute functions, the functions check the
instrument status after each call. Also, when state caching is enabled,
the high-level functions that configure multiple attributes perform
instrument I/O only for the attributes whose value you change. Thus, you
can safely call the high-level functions without the penalty of
redundant instrument I/O.
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
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'out',
                'name': 'callerHasLock',
                'type': 'ViBoolean',
'documentation': {
'description': '''
This parameter serves as a convenience; if you do not want to use this
parameter, pass VI_NULL.

Use this parameter in complex functions to keep track of whether you
have obtained a lock and therefore need to unlock the session; pass the
address of a local ViBoolean variable; in the declaration of the local
variable, initialize it to VI_FALSE; pass the address of the same local
variable to any other calls you make to niScope_LockSession or
niScope_UnlockSession in the same function.
''',
},
            },
        ],
'documentation': {
'description': '''
Releases a lock that you acquired on an instrument session using
niScope_LockSession.
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
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
        ],
'documentation': {
'description': '''
When you are finished using an instrument driver session, you must call
this function to perform the following actions:

-  Closes the instrument I/O session.
-  Destroys the IVI session and all of its attributes.
-  Deallocates any memory resources used by the IVI session.
''',
},
    },
    'errorHandler': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'in',
                'name': 'errorCode',
                'type': 'ViInt32',
'documentation': {
'description': '''
The error code that is returned from any of the instrument driver
functions.
''',
},
            },
            {
                'direction': 'out',
                'name': 'errorSource',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Specifies the function in which the error occurred. You can pass in a
string no longer than MAX_FUNCTION_NAME_SIZE. If you pass in a valid
string, this source is included in the **errorDescription** string. For
example:

"Error <**errorCode**> at <**errorSource**>"

If you pass in NULL or an empty string, this parameter is ignored.
''',
},
            },
            {
                'direction': 'out',
                'name': 'errorDescription',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Returns the interpreted error code as a user readable message string;
you must pass a ViChar array at least MAX_ERROR_DESCRIPTION bytes in
length.
''',
},
            },
        ],
'documentation': {
'description': '''
Takes the error code returned by NI-SCOPE functions and returns the
interpretation as a user-readable string.
''',
'note': '''
You can pass VI_NULL as the instrument handle, which is useful to
interpret errors after niScope_init has failed.
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
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'out',
                'name': 'errCode',
                'type': 'ViInt32',
'documentation': {
'description': '''
Returns the error code for the session or execution thread. If you pass
0 for the Buffer Size, you can pass VI_NULL for this parameter.
''',
},
            },
            {
                'direction': 'out',
                'name': 'errMessage',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Formats the error code into a user-readable message string. The array
must contain at least 256 elements (ViChar[256]).
''',
},
            },
        ],
'documentation': {
'description': '''
Reads an error code and message from the error queue. National
Instruments digitizers do not contain an error queue. Errors are
reported as they occur. Therefore, this function does not detect errors.
''',
'note': '''
This function is included for compliance with the IviScope Class
Specification.
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
'caution': '''
Traditional NI-DAQ and NI-DAQmx device names are not case-sensitive.
However, all IVI names, such as logical names, are case-sensitive. If
you use logical names, driver session names, or virtual names in your
program, you must make sure that the name you use matches the name in
the IVI Configuration Store file exactly, without any variations in the
case of the characters.
''',
'description': '''
**resourceName** specifies the resource name of the device to
initialize.

resourceName Examples

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
Specify whether to perform an ID query.

When you set this parameter to VI_TRUE, NI-SCOPE verifies that the
device you initialize is a type that it supports.

When you set this parameter to VI_FALSE, the function initializes the
device without performing an ID query.

**Defined Values**

| VI_TRUE—Perform ID query
| VI_FALSE—Skip ID query

**Default Value**: VI_TRUE
''',
},
            },
            {
                'direction': 'in',
                'name': 'resetDevice',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Specify whether to reset the device during the initialization process.

**Defined Values**

| VI_TRUE—Reset device
| VI_FALSE—Do not reset device

**Default Value**: VI_TRUE
''',
'note': '''
For the NI 5112, repeatedly resetting the device may cause excessive
wear on the electromechanical relays. Refer to `NI 5112
Electromechanical Relays <REPLACE_DRIVER_SPECIFIC_URL_1(5112_relays)>`__
for recommended programming practices.
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
subsequent NI-SCOPE function calls.
''',
},
            },
        ],
'documentation': {
'description': '''
Performs the following initialization actions:

-  Creates a new IVI instrument driver session
-  Opens a session to the specific driver using the interface and
   address you specify in the **resourceName**
-  Queries the instrument ID and checks that it is valid for NI-SCOPE,
   if the **IDQuery** is set to VI_TRUE
-  Resets the digitizer to a known state, if **resetDevice** is set to
   VI_TRUE
-  Sends initialization commands to set the instrument to the state
   necessary for the operation of the instrument driver
-  Returns an instrument handle that you use to identify the instrument
   in all subsequent instrument driver function calls
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
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
        ],
'documentation': {
'description': '''
Stops the acquisition, releases routes, and all session attributes are
reset to their `default
states <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cviattribute_defaults)>`__.
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
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'out',
                'name': 'driverRevision',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Returns the instrument driver software revision numbers in the form of a
string; you must pass a ViChar array at least
IVI_MAX_MESSAGE_BUF_SIZE bytes in length.
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
string; you must pass a ViChar array at least
IVI_MAX_MESSAGE_BUF_SIZE bytes in length.
''',
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
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The instrument handle you obtain from niScope_init that identifies a
particular instrument session.
''',
},
            },
            {
                'direction': 'out',
                'name': 'selfTestResult',
                'type': 'ViInt16',
'documentation': {
'description': '''
This control contains the value returned from the instrument self-test.

**Self-Test Code Description**

0—Self-test passed

1—Self-test failed
''',
},
            },
            {
                'direction': 'out',
                'name': 'selfTestMessage',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Returns the self-test response string from the instrument. Refer to the
device-specific help topics for an explanation of the string contents;
you must pass a ViChar array at least IVI_MAX_MESSAGE_BUF_SIZE bytes
in length.
''',
},
            },
        ],
'documentation': {
'description': 'Runs the instrument self-test routine and returns the test result(s).',
},
    },
}
