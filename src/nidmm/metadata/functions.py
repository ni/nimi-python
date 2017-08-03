# -*- coding: utf-8 -*-
# This file is code generated, do not make changes here
#  If the generated information is not correct for python
#  changes can be made in functions_addon.py and they will be 
#  applied at build time

functions = {
    'Abort': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
        ],
    },
    'CalAdjustACFilter': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'mode',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'range',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'frequency',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'expectedValue',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'CalAdjustGain': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'mode',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'range',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'inputResistance',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'expectedValue',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'CalAdjustLC': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'type',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'CalAdjustLinearization': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'function',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'range',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'inputResistance',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'expectedValue',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'CalAdjustMisc': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'type',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'CalAdjustOffset': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'mode',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'range',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'inputResistance',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'CheckAttributeViBoolean': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViBoolean',
                'enum': None,
            },
        ],
    },
    'CheckAttributeViInt32': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'CheckAttributeViReal64': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'CheckAttributeViSession': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViSession',
                'enum': None,
            },
        ],
    },
    'CheckAttributeViString': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
                'enum': None,
            },
            {
                'direction': 'in',
                'is_buffer': True,
                'name': 'attributeValue',
                'type': 'ViChar',
                'enum': None,
            },
        ],
    },
    'ClearError': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
        ],
    },
    'ClearInterchangeWarnings': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
        ],
    },
    'CloseExtCal': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'action',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'ConfigureACBandwidth': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'acMinimumFrequencyHz',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'acMaximumFrequencyHz',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'ConfigureADCCalibration': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'adcCalibration',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'ConfigureAutoZeroMode': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'autoZeroMode',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'ConfigureCableCompType': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'cableCompType',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'ConfigureCurrentSource': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'currentSource',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'ConfigureFixedRefJunction': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'fixedReferenceJunction',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'ConfigureFrequencyVoltageRange': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'voltageRange',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'ConfigureMeasCompleteDest': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'measCompleteDestination',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'ConfigureMeasCompleteSlope': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'measCompleteSlope',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'ConfigureMeasurementAbsolute': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'measurementFunction',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'range',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'resolutionAbsolute',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'ConfigureMeasurementDigits': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'measurementFunction',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'range',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'resolutionDigits',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'ConfigureMultiPoint': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'triggerCount',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'sampleCount',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'sampleTrigger',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'sampleInterval',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'ConfigureOffsetCompOhms': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'offsetCompOhms',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'ConfigureOpenCableCompValues': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'conductance',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'susceptance',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'ConfigurePowerLineFrequency': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'powerLineFrequencyHz',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'ConfigureRTDCustom': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'rtdA',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'rtdB',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'rtdC',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'ConfigureRTDType': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'rtdType',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'rtdResistance',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'ConfigureSampleTriggerSlope': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'sampleTriggerSlope',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'ConfigureShortCableCompValues': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'resistance',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'reactance',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'ConfigureThermistorCustom': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'thermistorA',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'thermistorB',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'thermistorC',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'ConfigureThermistorType': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'thermistorType',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'ConfigureThermocouple': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'thermocoupleType',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'referenceJunctionType',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'ConfigureTransducerType': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'transducerType',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'ConfigureTrigger': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'triggerSource',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'triggerDelay',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'ConfigureTriggerSlope': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'triggerSlope',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'ConfigureWaveformAcquisition': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'measurementFunction',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'range',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'rate',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'waveformPoints',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'ConfigureWaveformCoupling': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'waveformCoupling',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'Control': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'controlAction',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'Disable': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
        ],
    },
    'Fetch': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'maximumTime',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'out',
                'name': 'reading',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'FetchMultiPoint': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'maximumTime',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'out',
                'is_buffer': True,
                'name': 'readingArray',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'out',
                'name': 'actualNumberOfPoints',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'FetchWaveform': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'maximumTime',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'out',
                'is_buffer': True,
                'name': 'waveformArray',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'out',
                'name': 'actualNumberOfPoints',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'FormatMeasAbsolute': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'measurementFunction',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'range',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'resolution',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'measurement',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'out',
                'is_buffer': True,
                'name': 'modeString',
                'type': 'ViChar',
                'enum': None,
            },
            {
                'direction': 'out',
                'is_buffer': True,
                'name': 'rangeString',
                'type': 'ViChar',
                'enum': None,
            },
            {
                'direction': 'out',
                'is_buffer': True,
                'name': 'dataString',
                'type': 'ViChar',
                'enum': None,
            },
        ],
    },
    'GetApertureTimeInfo': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'out',
                'name': 'apertureTime',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'out',
                'name': 'apertureTimeUnits',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'GetAttributeViBoolean': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
                'enum': None,
            },
            {
                'direction': 'out',
                'name': 'attributeValue',
                'type': 'ViBoolean',
                'enum': None,
            },
        ],
    },
    'GetAttributeViInt32': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
                'enum': None,
            },
            {
                'direction': 'out',
                'name': 'attributeValue',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'GetAttributeViReal64': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
                'enum': None,
            },
            {
                'direction': 'out',
                'name': 'attributeValue',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'GetAttributeViSession': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
                'enum': None,
            },
            {
                'direction': 'out',
                'name': 'attributeValue',
                'type': 'ViSession',
                'enum': None,
            },
        ],
    },
    'GetAttributeViString': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'out',
                'is_buffer': True,
                'name': 'attributeValue',
                'type': 'ViChar',
                'enum': None,
            },
        ],
    },
    'GetAutoRangeValue': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'out',
                'name': 'actualRange',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'GetCalCount': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'calType',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'out',
                'name': 'count',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'GetCalDateAndTime': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'calType',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'out',
                'name': 'month',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'out',
                'name': 'day',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'out',
                'name': 'year',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'out',
                'name': 'hour',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'out',
                'name': 'minute',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'GetCalUserDefinedInfo': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'out',
                'is_buffer': True,
                'name': 'info',
                'type': 'ViChar',
                'enum': None,
            },
        ],
    },
    'GetCalUserDefinedInfoMaxSize': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'out',
                'name': 'infoSize',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'GetChannelName': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'index',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'out',
                'is_buffer': True,
                'name': 'channelString',
                'type': 'ViChar',
                'enum': None,
            },
        ],
    },
    'GetDevTemp': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'options',
                'type': 'ViString',
                'enum': None,
            },
            {
                'direction': 'out',
                'name': 'temperature',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'GetError': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'out',
                'name': 'errorCode',
                'type': 'ViStatus',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'out',
                'is_buffer': True,
                'name': 'description',
                'type': 'ViChar',
                'enum': None,
            },
        ],
    },
    'GetErrorMessage': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'errorCode',
                'type': 'ViStatus',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'buffer_size',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'out',
                'is_buffer': True,
                'name': 'errorMessage',
                'type': 'ViChar',
                'enum': None,
            },
        ],
    },
    'GetExtCalRecommendedInterval': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'out',
                'name': 'months',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'GetLastCalTemp': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'calType',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'out',
                'name': 'temperature',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'GetMeasurementPeriod': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'out',
                'name': 'period',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'GetNextCoercionRecord': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'out',
                'is_buffer': True,
                'name': 'coercionRecord',
                'type': 'ViChar',
                'enum': None,
            },
        ],
    },
    'GetNextInterchangeWarning': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'out',
                'is_buffer': True,
                'name': 'interchangeWarning',
                'type': 'ViChar',
                'enum': None,
            },
        ],
    },
    'GetSelfCalSupported': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'out',
                'name': 'selfCalSupported',
                'type': 'ViBoolean',
                'enum': None,
            },
        ],
    },
    'InitExtCal': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'resourceName',
                'type': 'ViString',
                'enum': None,
            },
            {
                'direction': 'in',
                'is_buffer': True,
                'name': 'calibrationPassword',
                'type': 'ViChar',
                'enum': None,
            },
            {
                'direction': 'out',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
        ],
    },
    'InitWithOptions': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'resourceName',
                'type': 'ViString',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'idQuery',
                'type': 'ViBoolean',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'resetDevice',
                'type': 'ViBoolean',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'optionString',
                'type': 'ViString',
                'enum': None,
            },
            {
                'direction': 'out',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
        ],
    },
    'Initiate': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
        ],
    },
    'IsOverRange': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'measurementValue',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'out',
                'name': 'isOverRange',
                'type': 'ViBoolean',
                'enum': None,
            },
        ],
    },
    'IsUnderRange': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'measurementValue',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'out',
                'name': 'isUnderRange',
                'type': 'ViBoolean',
                'enum': None,
            },
        ],
    },
    'LockSession': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'out',
                'name': 'callerHasLock',
                'type': 'ViBoolean',
                'enum': None,
            },
        ],
    },
    'PerformOpenCableComp': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'out',
                'name': 'conductance',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'out',
                'name': 'susceptance',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'PerformShortCableComp': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'out',
                'name': 'resistance',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'out',
                'name': 'reactance',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'Read': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'maximumTime',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'out',
                'name': 'reading',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'ReadMultiPoint': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'maximumTime',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'out',
                'is_buffer': True,
                'name': 'readingArray',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'out',
                'name': 'actualNumberOfPoints',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'ReadStatus': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'out',
                'name': 'acquisitionBacklog',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'out',
                'name': 'acquisitionStatus',
                'type': 'ViInt16',
                'enum': None,
            },
        ],
    },
    'ReadWaveform': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'maximumTime',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'out',
                'is_buffer': True,
                'name': 'waveformArray',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'out',
                'name': 'actualNumberOfPoints',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'ResetInterchangeCheck': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
        ],
    },
    'ResetWithDefaults': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
        ],
    },
    'RestoreLastExtCalConstants': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
        ],
    },
    'SelfCal': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
        ],
    },
    'SendSoftwareTrigger': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
        ],
    },
    'SetAttributeViBoolean': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViBoolean',
                'enum': None,
            },
        ],
    },
    'SetAttributeViInt32': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'SetAttributeViReal64': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'SetAttributeViSession': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViSession',
                'enum': None,
            },
        ],
    },
    'SetAttributeViString': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
                'enum': None,
            },
            {
                'direction': 'in',
                'is_buffer': True,
                'name': 'attributeValue',
                'type': 'ViChar',
                'enum': None,
            },
        ],
    },
    'SetCalPassword': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'is_buffer': True,
                'name': 'oldPassword',
                'type': 'ViChar',
                'enum': None,
            },
            {
                'direction': 'in',
                'is_buffer': True,
                'name': 'newPassword',
                'type': 'ViChar',
                'enum': None,
            },
        ],
    },
    'SetCalUserDefinedInfo': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'is_buffer': True,
                'name': 'info',
                'type': 'ViChar',
                'enum': None,
            },
        ],
    },
    'UnlockSession': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'out',
                'name': 'callerHasLock',
                'type': 'ViBoolean',
                'enum': None,
            },
        ],
    },
    'close': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
        ],
    },
    'error_message': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'errorCode',
                'type': 'ViStatus',
                'enum': None,
            },
            {
                'direction': 'out',
                'is_buffer': True,
                'name': 'errorMessage',
                'type': 'ViChar',
                'enum': None,
            },
        ],
    },
    'error_query': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'out',
                'name': 'errorCode',
                'type': 'ViStatus',
                'enum': None,
            },
            {
                'direction': 'out',
                'is_buffer': True,
                'name': 'errorMessage',
                'type': 'ViChar',
                'enum': None,
            },
        ],
    },
    'init': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'resourceName',
                'type': 'ViString',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'idQuery',
                'type': 'ViBoolean',
                'enum': None,
            },
            {
                'direction': 'in',
                'name': 'resetDevice',
                'type': 'ViBoolean',
                'enum': None,
            },
            {
                'direction': 'out',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
        ],
    },
    'reset': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
        ],
    },
    'revision_query': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'out',
                'is_buffer': True,
                'name': 'instrumentDriverRevision',
                'type': 'ViChar',
                'enum': None,
            },
            {
                'direction': 'out',
                'is_buffer': True,
                'name': 'firmwareRevision',
                'type': 'ViChar',
                'enum': None,
            },
        ],
    },
    'self_test': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'out',
                'name': 'selfTestResult',
                'type': 'ViInt16',
                'enum': None,
            },
            {
                'direction': 'out',
                'is_buffer': True,
                'name': 'selfTestMessage',
                'type': 'ViChar',
                'enum': None,
            },
        ],
    },
}
