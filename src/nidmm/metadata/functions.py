# -*- coding: utf-8 -*-
functions = {
    'Abort': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
        },
    },
    'CalAdjustACFilter': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'mode',
                'type': 'ViInt32',
                'enum': None,
            },
            3: {
                'direction': 'in',
                'name': 'range',
                'type': 'ViReal64',
                'enum': None,
            },
            4: {
                'direction': 'in',
                'name': 'frequency',
                'type': 'ViReal64',
                'enum': None,
            },
            5: {
                'direction': 'in',
                'name': 'expectedValue',
                'type': 'ViReal64',
                'enum': None,
            },
        },
    },
    'CalAdjustGain': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'mode',
                'type': 'ViInt32',
                'enum': None,
            },
            3: {
                'direction': 'in',
                'name': 'range',
                'type': 'ViReal64',
                'enum': None,
            },
            4: {
                'direction': 'in',
                'name': 'inputResistance',
                'type': 'ViReal64',
                'enum': None,
            },
            5: {
                'direction': 'in',
                'name': 'expectedValue',
                'type': 'ViReal64',
                'enum': None,
            },
        },
    },
    'CalAdjustLC': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'type',
                'type': 'ViInt32',
                'enum': None,
            },
        },
    },
    'CalAdjustLinearization': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'function',
                'type': 'ViInt32',
                'enum': None,
            },
            3: {
                'direction': 'in',
                'name': 'range',
                'type': 'ViReal64',
                'enum': None,
            },
            4: {
                'direction': 'in',
                'name': 'inputResistance',
                'type': 'ViReal64',
                'enum': None,
            },
            5: {
                'direction': 'in',
                'name': 'expectedValue',
                'type': 'ViReal64',
                'enum': None,
            },
        },
    },
    'CalAdjustMisc': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'type',
                'type': 'ViInt32',
                'enum': None,
            },
        },
    },
    'CalAdjustOffset': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'mode',
                'type': 'ViInt32',
                'enum': None,
            },
            3: {
                'direction': 'in',
                'name': 'range',
                'type': 'ViReal64',
                'enum': None,
            },
            4: {
                'direction': 'in',
                'name': 'inputResistance',
                'type': 'ViReal64',
                'enum': None,
            },
        },
    },
    'CheckAttributeViBoolean': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
                'enum': None,
            },
            3: {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
                'enum': None,
            },
            4: {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViBoolean',
                'enum': None,
            },
        },
    },
    'CheckAttributeViInt32': {
        'returns': 'void',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
                'enum': None,
            },
            3: {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
                'enum': None,
            },
            4: {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViInt32',
                'enum': None,
            },
        },
    },
    'CheckAttributeViReal64': {
        'returns': 'void',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
                'enum': None,
            },
            3: {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
                'enum': None,
            },
            4: {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViReal64',
                'enum': None,
            },
        },
    },
    'CheckAttributeViSession': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
                'enum': None,
            },
            3: {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
                'enum': None,
            },
            4: {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViSession',
                'enum': None,
            },
        },
    },
    'CheckAttributeViString': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
                'enum': None,
            },
            3: {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
                'enum': None,
            },
            4: {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViChar',
                'enum': None,
            },
        },
    },
    'ClearError': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
        },
    },
    'ClearInterchangeWarnings': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
        },
    },
    'CloseExtCal': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'action',
                'type': 'ViInt32',
                'enum': None,
            },
        },
    },
    'ConfigureACBandwidth': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'acMinimumFrequencyHz',
                'type': 'ViReal64',
                'enum': None,
            },
            3: {
                'direction': 'in',
                'name': 'acMaximumFrequencyHz',
                'type': 'ViReal64',
                'enum': None,
            },
        },
    },
    'ConfigureADCCalibration': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'adcCalibration',
                'type': 'ViInt32',
                'enum': None,
            },
        },
    },
    'ConfigureAutoZeroMode': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'autoZeroMode',
                'type': 'ViInt32',
                'enum': None,
            },
        },
    },
    'ConfigureCableCompType': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'cableCompType',
                'type': 'ViInt32',
                'enum': None,
            },
        },
    },
    'ConfigureCurrentSource': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'currentSource',
                'type': 'ViReal64',
                'enum': None,
            },
        },
    },
    'ConfigureFixedRefJunction': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'fixedReferenceJunction',
                'type': 'ViReal64',
                'enum': None,
            },
        },
    },
    'ConfigureFrequencyVoltageRange': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'voltageRange',
                'type': 'ViReal64',
                'enum': None,
            },
        },
    },
    'ConfigureMeasCompleteDest': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'measCompleteDestination',
                'type': 'ViInt32',
                'enum': None,
            },
        },
    },
    'ConfigureMeasCompleteSlope': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'measCompleteSlope',
                'type': 'ViInt32',
                'enum': None,
            },
        },
    },
    'ConfigureMeasurementAbsolute': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'measurementFunction',
                'type': 'ViInt32',
                'enum': None,
            },
            3: {
                'direction': 'in',
                'name': 'range',
                'type': 'ViReal64',
                'enum': None,
            },
            4: {
                'direction': 'in',
                'name': 'resolutionAbsolute',
                'type': 'ViReal64',
                'enum': None,
            },
        },
    },
    'ConfigureMeasurementDigits': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'measurementFunction',
                'type': 'ViInt32',
                'enum': None,
            },
            3: {
                'direction': 'in',
                'name': 'range',
                'type': 'ViReal64',
                'enum': None,
            },
            4: {
                'direction': 'in',
                'name': 'resolutionDigits',
                'type': 'ViReal64',
                'enum': None,
            },
        },
    },
    'ConfigureMultiPoint': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'triggerCount',
                'type': 'ViInt32',
                'enum': None,
            },
            3: {
                'direction': 'in',
                'name': 'sampleCount',
                'type': 'ViInt32',
                'enum': None,
            },
            4: {
                'direction': 'in',
                'name': 'sampleTrigger',
                'type': 'ViInt32',
                'enum': None,
            },
            5: {
                'direction': 'in',
                'name': 'sampleInterval',
                'type': 'ViReal64',
                'enum': None,
            },
        },
    },
    'ConfigureOffsetCompOhms': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'offsetCompOhms',
                'type': 'ViInt32',
                'enum': None,
            },
        },
    },
    'ConfigureOpenCableCompValues': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'conductance',
                'type': 'ViReal64',
                'enum': None,
            },
            3: {
                'direction': 'in',
                'name': 'susceptance',
                'type': 'ViReal64',
                'enum': None,
            },
        },
    },
    'ConfigurePowerLineFrequency': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'powerLineFrequencyHz',
                'type': 'ViReal64',
                'enum': None,
            },
        },
    },
    'ConfigureRTDCustom': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'rtdA',
                'type': 'ViReal64',
                'enum': None,
            },
            3: {
                'direction': 'in',
                'name': 'rtdB',
                'type': 'ViReal64',
                'enum': None,
            },
            4: {
                'direction': 'in',
                'name': 'rtdC',
                'type': 'ViReal64',
                'enum': None,
            },
        },
    },
    'ConfigureRTDType': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'rtdType',
                'type': 'ViInt32',
                'enum': None,
            },
            3: {
                'direction': 'in',
                'name': 'rtdResistance',
                'type': 'ViReal64',
                'enum': None,
            },
        },
    },
    'ConfigureSampleTriggerSlope': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'sampleTriggerSlope',
                'type': 'ViInt32',
                'enum': None,
            },
        },
    },
    'ConfigureShortCableCompValues': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'resistance',
                'type': 'ViReal64',
                'enum': None,
            },
            3: {
                'direction': 'in',
                'name': 'reactance',
                'type': 'ViReal64',
                'enum': None,
            },
        },
    },
    'ConfigureThermistorCustom': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'thermistorA',
                'type': 'ViReal64',
                'enum': None,
            },
            3: {
                'direction': 'in',
                'name': 'thermistorB',
                'type': 'ViReal64',
                'enum': None,
            },
            4: {
                'direction': 'in',
                'name': 'thermistorC',
                'type': 'ViReal64',
                'enum': None,
            },
        },
    },
    'ConfigureThermistorType': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'thermistorType',
                'type': 'ViInt32',
                'enum': None,
            },
        },
    },
    'ConfigureThermocouple': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'thermocoupleType',
                'type': 'ViInt32',
                'enum': None,
            },
            3: {
                'direction': 'in',
                'name': 'referenceJunctionType',
                'type': 'ViInt32',
                'enum': None,
            },
        },
    },
    'ConfigureTransducerType': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'transducerType',
                'type': 'ViInt32',
                'enum': None,
            },
        },
    },
    'ConfigureTrigger': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'triggerSource',
                'type': 'ViInt32',
                'enum': None,
            },
            3: {
                'direction': 'in',
                'name': 'triggerDelay',
                'type': 'ViReal64',
                'enum': None,
            },
        },
    },
    'ConfigureTriggerSlope': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'triggerSlope',
                'type': 'ViInt32',
                'enum': None,
            },
        },
    },
    'ConfigureWaveformAcquisition': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'measurementFunction',
                'type': 'ViInt32',
                'enum': None,
            },
            3: {
                'direction': 'in',
                'name': 'range',
                'type': 'ViReal64',
                'enum': None,
            },
            4: {
                'direction': 'in',
                'name': 'rate',
                'type': 'ViReal64',
                'enum': None,
            },
            5: {
                'direction': 'in',
                'name': 'waveformPoints',
                'type': 'ViInt32',
                'enum': None,
            },
        },
    },
    'ConfigureWaveformCoupling': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'waveformCoupling',
                'type': 'ViInt32',
                'enum': None,
            },
        },
    },
    'Control': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'controlAction',
                'type': 'ViInt32',
                'enum': None,
            },
        },
    },
    'Disable': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
        },
    },
    'Fetch': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'maximumTime',
                'type': 'ViInt32',
                'enum': None,
            },
            3: {
                'direction': 'out',
                'name': 'reading',
                'type': 'ViReal64',
                'enum': None,
            },
        },
    },
    'FetchMultiPoint': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'maximumTime',
                'type': 'ViInt32',
                'enum': None,
            },
            3: {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'ViInt32',
                'enum': None,
            },
            4: {
                'direction': 'out',
                'name': 'readingArray',
                'type': 'ViReal64',
                'enum': None,
            },
            5: {
                'direction': 'out',
                'name': 'actualNumberOfPoints',
                'type': 'ViInt32',
                'enum': None,
            },
        },
    },
    'FetchWaveform': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'maximumTime',
                'type': 'ViInt32',
                'enum': None,
            },
            3: {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'ViInt32',
                'enum': None,
            },
            4: {
                'direction': 'out',
                'name': 'waveformArray',
                'type': 'ViReal64',
                'enum': None,
            },
            5: {
                'direction': 'out',
                'name': 'actualNumberOfPoints',
                'type': 'ViInt32',
                'enum': None,
            },
        },
    },
    'FormatMeasAbsolute': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'measurementFunction',
                'type': 'ViInt32',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'range',
                'type': 'ViReal64',
                'enum': None,
            },
            3: {
                'direction': 'in',
                'name': 'resolution',
                'type': 'ViReal64',
                'enum': None,
            },
            4: {
                'direction': 'in',
                'name': 'measurement',
                'type': 'ViReal64',
                'enum': None,
            },
            5: {
                'direction': 'out',
                'name': 'modeString',
                'type': 'ViChar',
                'enum': None,
            },
            6: {
                'direction': 'out',
                'name': 'rangeString',
                'type': 'ViChar',
                'enum': None,
            },
            7: {
                'direction': 'out',
                'name': 'dataString',
                'type': 'ViChar',
                'enum': None,
            },
        },
    },
    'GetApertureTimeInfo': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'out',
                'name': 'apertureTime',
                'type': 'ViReal64',
                'enum': None,
            },
            3: {
                'direction': 'out',
                'name': 'apertureTimeUnits',
                'type': 'ViInt32',
                'enum': None,
            },
        },
    },
    'GetAttributeViBoolean': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
                'enum': None,
            },
            3: {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
                'enum': None,
            },
            4: {
                'direction': 'out',
                'name': 'attributeValue',
                'type': 'ViBoolean',
                'enum': None,
            },
        },
    },
    'GetAttributeViInt32': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
                'enum': None,
            },
            3: {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
                'enum': None,
            },
            4: {
                'direction': 'out',
                'name': 'attributeValue',
                'type': 'ViInt32',
                'enum': None,
            },
        },
    },
    'GetAttributeViReal64': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
                'enum': None,
            },
            3: {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
                'enum': None,
            },
            4: {
                'direction': 'out',
                'name': 'attributeValue',
                'type': 'ViReal64',
                'enum': None,
            },
        },
    },
    'GetAttributeViSession': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
                'enum': None,
            },
            3: {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
                'enum': None,
            },
            4: {
                'direction': 'out',
                'name': 'attributeValue',
                'type': 'ViSession',
                'enum': None,
            },
        },
    },
    'GetAttributeViString': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
                'enum': None,
            },
            3: {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
                'enum': None,
            },
            4: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32',
                'enum': None,
            },
            5: {
                'direction': 'out',
                'name': 'attributeValue',
                'type': 'ViChar',
                'enum': None,
            },
        },
    },
    'GetAutoRangeValue': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'out',
                'name': 'actualRange',
                'type': 'ViReal64',
                'enum': None,
            },
        },
    },
    'GetCalCount': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'calType',
                'type': 'ViInt32',
                'enum': None,
            },
            3: {
                'direction': 'out',
                'name': 'count',
                'type': 'ViInt32',
                'enum': None,
            },
        },
    },
    'GetCalDateAndTime': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'calType',
                'type': 'ViInt32',
                'enum': None,
            },
            3: {
                'direction': 'out',
                'name': 'month',
                'type': 'ViInt32',
                'enum': None,
            },
            4: {
                'direction': 'out',
                'name': 'day',
                'type': 'ViInt32',
                'enum': None,
            },
            5: {
                'direction': 'out',
                'name': 'year',
                'type': 'ViInt32',
                'enum': None,
            },
            6: {
                'direction': 'out',
                'name': 'hour',
                'type': 'ViInt32',
                'enum': None,
            },
            7: {
                'direction': 'out',
                'name': 'minute',
                'type': 'ViInt32',
                'enum': None,
            },
        },
    },
    'GetCalUserDefinedInfo': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32',
                'enum': None,
            },
            3: {
                'direction': 'out',
                'name': 'info',
                'type': 'ViChar',
                'enum': None,
            },
        },
    },
    'GetCalUserDefinedInfoMaxSize': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'out',
                'name': 'infoSize',
                'type': 'ViInt32',
                'enum': None,
            },
        },
    },
    'GetChannelName': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'index',
                'type': 'ViInt32',
                'enum': None,
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32',
                'enum': None,
            },
            4: {
                'direction': 'out',
                'name': 'channelString',
                'type': 'ViChar',
                'enum': None,
            },
        },
    },
    'GetDevTemp': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'options',
                'type': 'ViString',
                'enum': None,
            },
            3: {
                'direction': 'out',
                'name': 'temperature',
                'type': 'ViReal64',
                'enum': None,
            },
        },
    },
    'GetError': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'out',
                'name': 'errorCode',
                'type': 'ViStatus',
                'enum': None,
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32',
                'enum': None,
            },
            4: {
                'direction': 'out',
                'name': 'description',
                'type': 'ViChar',
                'enum': None,
            },
        },
    },
    'GetErrorMessage': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'errorCode',
                'type': 'ViStatus',
                'enum': None,
            },
            3: {
                'direction': 'in',
                'name': 'buffer_size',
                'type': 'ViInt32',
                'enum': None,
            },
            4: {
                'direction': 'out',
                'name': 'errorMessage',
                'type': 'ViChar',
                'enum': None,
            },
        },
    },
    'GetExtCalRecommendedInterval': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'out',
                'name': 'months',
                'type': 'ViInt32',
                'enum': None,
            },
        },
    },
    'GetLastCalTemp': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'calType',
                'type': 'ViInt32',
                'enum': None,
            },
            3: {
                'direction': 'out',
                'name': 'temperature',
                'type': 'ViReal64',
                'enum': None,
            },
        },
    },
    'GetMeasurementPeriod': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'out',
                'name': 'period',
                'type': 'ViReal64',
                'enum': None,
            },
        },
    },
    'GetNextCoercionRecord': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32',
                'enum': None,
            },
            3: {
                'direction': 'out',
                'name': 'coercionRecord',
                'type': 'ViChar',
                'enum': None,
            },
        },
    },
    'GetNextInterchangeWarning': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32',
                'enum': None,
            },
            3: {
                'direction': 'out',
                'name': 'interchangeWarning',
                'type': 'ViChar',
                'enum': None,
            },
        },
    },
    'GetSelfCalSupported': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'out',
                'name': 'selfCalSupported',
                'type': 'ViBoolean',
                'enum': None,
            },
        },
    },
    'InitExtCal': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'resourceName',
                'type': 'ViString',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'calibrationPassword',
                'type': 'ViChar',
                'enum': None,
            },
            3: {
                'direction': 'out',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
        },
    },
    'InitWithOptions': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'resourceName',
                'type': 'ViString',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'idQuery',
                'type': 'ViBoolean',
                'enum': None,
            },
            3: {
                'direction': 'in',
                'name': 'resetDevice',
                'type': 'ViBoolean',
                'enum': None,
            },
            4: {
                'direction': 'in',
                'name': 'optionString',
                'type': 'ViString',
                'enum': None,
            },
            5: {
                'direction': 'out',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
        },
    },
    'Initiate': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
        },
    },
    'IsOverRange': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'measurementValue',
                'type': 'ViReal64',
                'enum': None,
            },
            3: {
                'direction': 'out',
                'name': 'isOverRange',
                'type': 'ViBoolean',
                'enum': None,
            },
        },
    },
    'IsUnderRange': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'measurementValue',
                'type': 'ViReal64',
                'enum': None,
            },
            3: {
                'direction': 'out',
                'name': 'isUnderRange',
                'type': 'ViBoolean',
                'enum': None,
            },
        },
    },
    'LockSession': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'out',
                'name': 'callerHasLock',
                'type': 'ViBoolean',
                'enum': None,
            },
        },
    },
    'PerformOpenCableComp': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'out',
                'name': 'conductance',
                'type': 'ViReal64',
                'enum': None,
            },
            3: {
                'direction': 'out',
                'name': 'susceptance',
                'type': 'ViReal64',
                'enum': None,
            },
        },
    },
    'PerformShortCableComp': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'out',
                'name': 'resistance',
                'type': 'ViReal64',
                'enum': None,
            },
            3: {
                'direction': 'out',
                'name': 'reactance',
                'type': 'ViReal64',
                'enum': None,
            },
        },
    },
    'Read': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'maximumTime',
                'type': 'ViInt32',
                'enum': None,
            },
            3: {
                'direction': 'out',
                'name': 'reading',
                'type': 'ViReal64',
                'enum': None,
            },
        },
    },
    'ReadMultiPoint': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'maximumTime',
                'type': 'ViInt32',
                'enum': None,
            },
            3: {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'ViInt32',
                'enum': None,
            },
            4: {
                'direction': 'out',
                'name': 'readingArray',
                'type': 'ViReal64',
                'enum': None,
            },
            5: {
                'direction': 'out',
                'name': 'actualNumberOfPoints',
                'type': 'ViInt32',
                'enum': None,
            },
        },
    },
    'ReadStatus': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'out',
                'name': 'acquisitionBacklog',
                'type': 'ViInt32',
                'enum': None,
            },
            3: {
                'direction': 'out',
                'name': 'acquisitionStatus',
                'type': 'ViInt16',
                'enum': None,
            },
        },
    },
    'ReadWaveform': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'maximumTime',
                'type': 'ViInt32',
                'enum': None,
            },
            3: {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'ViInt32',
                'enum': None,
            },
            4: {
                'direction': 'out',
                'name': 'waveformArray',
                'type': 'ViReal64',
                'enum': None,
            },
            5: {
                'direction': 'out',
                'name': 'actualNumberOfPoints',
                'type': 'ViInt32',
                'enum': None,
            },
        },
    },
    'ResetInterchangeCheck': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
        },
    },
    'ResetWithDefaults': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
        },
    },
    'RestoreLastExtCalConstants': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
        },
    },
    'SelfCal': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
        },
    },
    'SendSoftwareTrigger': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
        },
    },
    'SetAttributeViBoolean': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
                'enum': None,
            },
            3: {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
                'enum': None,
            },
            4: {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViBoolean',
                'enum': None,
            },
        },
    },
    'SetAttributeViInt32': {
        'returns': 'void',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
                'enum': None,
            },
            3: {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
                'enum': None,
            },
            4: {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViInt32',
                'enum': None,
            },
        },
    },
    'SetAttributeViReal64': {
        'returns': 'void',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
                'enum': None,
            },
            3: {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
                'enum': None,
            },
            4: {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViReal64',
                'enum': None,
            },
        },
    },
    'SetAttributeViSession': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
                'enum': None,
            },
            3: {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
                'enum': None,
            },
            4: {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViSession',
                'enum': None,
            },
        },
    },
    'SetAttributeViString': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
                'enum': None,
            },
            3: {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
                'enum': None,
            },
            4: {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViChar',
                'enum': None,
            },
        },
    },
    'SetCalPassword': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'oldPassword',
                'type': 'ViChar',
                'enum': None,
            },
            3: {
                'direction': 'in',
                'name': 'newPassword',
                'type': 'ViChar',
                'enum': None,
            },
        },
    },
    'SetCalUserDefinedInfo': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'info',
                'type': 'ViChar',
                'enum': None,
            },
        },
    },
    'UnlockSession': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'out',
                'name': 'callerHasLock',
                'type': 'ViBoolean',
                'enum': None,
            },
        },
    },
    'close': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
        },
    },
    'error_message': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'errorCode',
                'type': 'ViStatus',
                'enum': None,
            },
            3: {
                'direction': 'out',
                'name': 'errorMessage',
                'type': 'ViChar',
                'enum': None,
            },
        },
    },
    'error_query': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'out',
                'name': 'errorCode',
                'type': 'ViStatus',
                'enum': None,
            },
            3: {
                'direction': 'out',
                'name': 'errorMessage',
                'type': 'ViChar',
                'enum': None,
            },
        },
    },
    'init': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'resourceName',
                'type': 'ViString',
                'enum': None,
            },
            2: {
                'direction': 'in',
                'name': 'idQuery',
                'type': 'ViBoolean',
                'enum': None,
            },
            3: {
                'direction': 'in',
                'name': 'resetDevice',
                'type': 'ViBoolean',
                'enum': None,
            },
            4: {
                'direction': 'out',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
        },
    },
    'reset': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
        },
    },
    'revision_query': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'out',
                'name': 'instrumentDriverRevision',
                'type': 'ViChar',
                'enum': None,
            },
            3: {
                'direction': 'out',
                'name': 'firmwareRevision',
                'type': 'ViChar',
                'enum': None,
            },
        },
    },
    'self_test': {
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': {
            1: {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            2: {
                'direction': 'out',
                'name': 'selfTestResult',
                'type': 'ViInt16',
                'enum': None,
            },
            3: {
                'direction': 'out',
                'name': 'selfTestMessage',
                'type': 'ViChar',
                'enum': None,
            },
        },
    },
}
