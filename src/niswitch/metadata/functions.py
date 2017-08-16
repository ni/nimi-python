
# -*- coding: utf-8 -*-
# This file is code generated, do not make changes here
#  If the generated information is not correct for python
#  changes can be made in functions_addon.py and they will be
#  applied at build time



functions = {
    'AbortScan': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',

            },
        ],

    },
    'CanConnect': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'channel1',
                'type': 'ViConstString',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'channel2',
                'type': 'ViConstString',

            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'pathCapability',
                'type': 'ViInt32',

            },
        ],

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

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'channelName',
                'type': 'ViConstString',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeId',
                'type': 'ViAttr',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeValue',
                'type': 'ViBoolean',

            },
        ],

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

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'channelName',
                'type': 'ViConstString',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeId',
                'type': 'ViAttr',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeValue',
                'type': 'ViInt32',

            },
        ],

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

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'channelName',
                'type': 'ViConstString',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeId',
                'type': 'ViAttr',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeValue',
                'type': 'ViReal64',

            },
        ],

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

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'channelName',
                'type': 'ViConstString',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeId',
                'type': 'ViAttr',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeValue',
                'type': 'ViSession',

            },
        ],

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

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'channelName',
                'type': 'ViConstString',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeId',
                'type': 'ViAttr',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeValue',
                'type': 'ViChar',

            },
        ],

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

            },
        ],

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

            },
        ],

    },
    'Commit': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',

            },
        ],

    },
    'ConfigureScanList': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'scanlist',
                'type': 'ViConstString',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'scanMode',
                'type': 'ViInt32',

            },
        ],

    },
    'ConfigureScanTrigger': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'scanDelay',
                'type': 'ViReal64',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'triggerInput',
                'type': 'ViInt32',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'scanAdvancedOutput',
                'type': 'ViInt32',

            },
        ],

    },
    'Connect': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'channel1',
                'type': 'ViConstString',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'channel2',
                'type': 'ViConstString',

            },
        ],

    },
    'ConnectMultiple': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'connectionList',
                'type': 'ViConstString',

            },
        ],

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

            },
        ],

    },
    'Disconnect': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'channel1',
                'type': 'ViConstString',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'channel2',
                'type': 'ViConstString',

            },
        ],

    },
    'DisconnectAll': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',

            },
        ],

    },
    'DisconnectMultiple': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'disconnectionList',
                'type': 'ViConstString',

            },
        ],

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

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'channelName',
                'type': 'ViConstString',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeId',
                'type': 'ViAttr',

            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'attributeValue',
                'type': 'ViBoolean',

            },
        ],

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

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'channelName',
                'type': 'ViConstString',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeId',
                'type': 'ViAttr',

            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'attributeValue',
                'type': 'ViInt32',

            },
        ],

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

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'channelName',
                'type': 'ViConstString',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeId',
                'type': 'ViAttr',

            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'attributeValue',
                'type': 'ViReal64',

            },
        ],

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

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'channelName',
                'type': 'ViConstString',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeId',
                'type': 'ViAttr',

            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'attributeValue',
                'type': 'ViSession',

            },
        ],

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

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'channelName',
                'type': 'ViConstString',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeId',
                'type': 'ViAttr',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'arraySize',
                'type': 'ViInt32',

            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'attributeValue',
                'type': 'ViChar',

            },
        ],

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

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'index',
                'type': 'ViInt32',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'bufferSize',
                'type': 'ViInt32',

            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'channelNameBuffer',
                'type': 'ViChar',

            },
        ],

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

            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'code',
                'type': 'ViStatus',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'buffersize',
                'type': 'ViInt32',

            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'description',
                'type': 'ViChar',

            },
        ],

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

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'bufferSize',
                'type': 'ViInt32',

            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'coercionRecord',
                'type': 'ViChar',

            },
        ],

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

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'bufferSize',
                'type': 'ViInt32',

            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'interchangeWarning',
                'type': 'ViChar',

            },
        ],

    },
    'GetPath': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'channel1',
                'type': 'ViConstString',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'channel2',
                'type': 'ViConstString',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'bufferSize',
                'type': 'ViInt32',

            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'path',
                'type': 'ViChar',

            },
        ],

    },
    'GetRelayCount': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'relayName',
                'type': 'ViConstString',

            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'relayCount',
                'type': 'ViInt32',

            },
        ],

    },
    'GetRelayName': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'index',
                'type': 'ViInt32',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'relayNameBufferSize',
                'type': 'ViInt32',

            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'relayNameBuffer',
                'type': 'ViChar',

            },
        ],

    },
    'GetRelayPosition': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'relayName',
                'type': 'ViConstString',

            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'relayPosition',
                'type': 'ViInt32',

            },
        ],

    },
    'InitWithOptions': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'resourceName',
                'type': 'ViRsrc',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'idQuery',
                'type': 'ViBoolean',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'resetDevice',
                'type': 'ViBoolean',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'optionsString',
                'type': 'ViConstString',

            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',

            },
        ],

    },
    'InitWithTopology': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'resourceName',
                'type': 'ViRsrc',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'topology',
                'type': 'ViConstString',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'simulate',
                'type': 'ViBoolean',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'resetDevice',
                'type': 'ViBoolean',

            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',

            },
        ],

    },
    'InitiateScan': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',

            },
        ],

    },
    'IsDebounced': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',

            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'isDebounced',
                'type': 'ViBoolean',

            },
        ],

    },
    'IsScanning': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',

            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'isScanning',
                'type': 'ViBoolean',

            },
        ],

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

            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'callerHasLock',
                'type': 'ViBoolean',

            },
        ],

    },
    'RelayControl': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'relayName',
                'type': 'ViConstString',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'relayAction',
                'type': 'ViInt32',

            },
        ],

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

            },
        ],

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

            },
        ],

    },
    'RouteScanAdvancedOutput': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'scanAdvancedOutputConnector',
                'type': 'ViInt32',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'scanAdvancedOutputBusLine',
                'type': 'ViInt32',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'invert',
                'type': 'ViBoolean',

            },
        ],

    },
    'RouteTriggerInput': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'triggerInputConnector',
                'type': 'ViInt32',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'triggerInputBusLine',
                'type': 'ViInt32',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'invert',
                'type': 'ViBoolean',

            },
        ],

    },
    'Scan': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'scanlist',
                'type': 'ViConstString',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'initiation',
                'type': 'ViInt16',

            },
        ],

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

            },
        ],

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

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'channelName',
                'type': 'ViConstString',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeId',
                'type': 'ViAttr',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeValue',
                'type': 'ViBoolean',

            },
        ],

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

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'channelName',
                'type': 'ViConstString',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeId',
                'type': 'ViAttr',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeValue',
                'type': 'ViInt32',

            },
        ],

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

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'channelName',
                'type': 'ViConstString',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeId',
                'type': 'ViAttr',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeValue',
                'type': 'ViReal64',

            },
        ],

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

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'channelName',
                'type': 'ViConstString',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeId',
                'type': 'ViAttr',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeValue',
                'type': 'ViSession',

            },
        ],

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

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'channelName',
                'type': 'ViConstString',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeId',
                'type': 'ViAttr',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeValue',
                'type': 'ViChar',

            },
        ],

    },
    'SetContinuousScan': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'continuousScan',
                'type': 'ViBoolean',

            },
        ],

    },
    'SetPath': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'pathList',
                'type': 'ViConstString',

            },
        ],

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

            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'callerHasLock',
                'type': 'ViBoolean',

            },
        ],

    },
    'WaitForDebounce': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'maximumTimeMs',
                'type': 'ViInt32',

            },
        ],

    },
    'WaitForScanComplete': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'maximumTimeMs',
                'type': 'ViInt32',

            },
        ],

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

            },
        ],

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

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'errorCode',
                'type': 'ViStatus',

            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'errorMessage',
                'type': 'ViChar',

            },
        ],

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

            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'errorCode',
                'type': 'ViInt32',

            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'errorMessage',
                'type': 'ViChar',

            },
        ],

    },
    'init': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'resourceName',
                'type': 'ViRsrc',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'idQuery',
                'type': 'ViBoolean',

            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'resetDevice',
                'type': 'ViBoolean',

            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',

            },
        ],

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

            },
        ],

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

            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'instrumentDriverRevision',
                'type': 'ViChar',

            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'firmwareRevision',
                'type': 'ViChar',

            },
        ],

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

            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'selfTestResult',
                'type': 'ViInt16',

            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'selfTestMessage',
                'type': 'ViChar',

            },
        ],

    },
}
