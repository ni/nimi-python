
# -*- coding: utf-8 -*-
# This file is code generated, do not make changes here.
#  If the generated information is not correct for python
#  changes can be made in enums_addon.py and they will be
#  applied at build time.

enums = {
    'CabledModuleScanAdvancedBus': {
        'values': [
            {
                'name': 'NONE',
                'value': 0,
'documentation': {
'description': '',
},
            },
            {
                'name': 'PXI_TRIG0',
                'value': 111,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the PXI\_Trig0
line before processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'PXI_TRIG1',
                'value': 112,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the PXI\_Trig1
line before processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'PXI_TRIG2',
                'value': 113,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the PXI\_Trig2
line before processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'PXI_TRIG3',
                'value': 114,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the PXI\_Trig3
line before processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'PXI_TRIG4',
                'value': 115,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the PXI\_Trig4
line before processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'PXI_TRIG5',
                'value': 116,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the PXI\_Trig5
line before processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'PXI_TRIG6',
                'value': 117,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the PXI\_Trig6
line before processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'PXI_TRIG7',
                'value': 118,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the PXI\_Trig7
line before processing the next entry in the scan list.
''',
},
            },
        ],
    },
    'CabledModuleTriggerBus': {
        'values': [
            {
                'name': 'NONE',
                'value': 0,
'documentation': {
'description': '',
},
            },
            {
                'name': 'PXI_TRIG0',
                'value': 111,
'documentation': {
'description': '',
},
            },
            {
                'name': 'PXI_TRIG1',
                'value': 112,
'documentation': {
'description': '',
},
            },
            {
                'name': 'PXI_TRIG2',
                'value': 113,
'documentation': {
'description': '',
},
            },
            {
                'name': 'PXI_TRIG3',
                'value': 114,
'documentation': {
'description': '',
},
            },
            {
                'name': 'PXI_TRIG4',
                'value': 115,
'documentation': {
'description': '',
},
            },
            {
                'name': 'PXI_TRIG5',
                'value': 116,
'documentation': {
'description': '',
},
            },
            {
                'name': 'PXI_TRIG6',
                'value': 117,
'documentation': {
'description': '',
},
            },
            {
                'name': 'PXI_TRIG7',
                'value': 118,
'documentation': {
'description': '',
},
            },
        ],
    },
    'HandshakingInitiation': {
        'values': [
            {
                'name': 'MEASUREMENT_DEVICE_INITIATED',
                'value': 0,
'documentation': {
'description': '''
The `niSwitch Initiate
Scan <switchviref.chm::/niSwitch_Initiate_Scan.html>`__ VI does not
return until the switch hardware is waiting for a trigger input. This
ensures that if you initiate the measurement device after calling the
`niSwitch Initiate
Scan <switchviref.chm::/niSwitch_Initiate_Scan.html>`__ VI , the switch
is sure to receive the first measurement complete (MC) signal sent by
the measurement device. The measurement device should be configured to
first take a measurement, send MC, then wait for scanner advanced output
signal. Thus, the first MC of the measurement device initiates
handshaking.
''',
},
            },
            {
                'name': 'SWITCH_INITIATED',
                'value': 1,
'documentation': {
'description': '''
The `niSwitch Initiate
Scan <switchviref.chm::/niSwitch_Initiate_Scan.html>`__ VI returns
immediately after beginning scan list execution. It is assumed that the
measurement device has already been configured and is waiting for the
scanner advanced signal. The measurement should be configured to first
wait for a trigger, then take a measurement. Thus, the first scanner
advanced output signal of the switch module initiates handshaking.
''',
},
            },
        ],
    },
    'MasterSlaveScanAdvancedBus': {
        'values': [
            {
                'name': 'NONE',
                'value': 0,
'documentation': {
'description': '',
},
            },
            {
                'name': 'PXI_TRIG0',
                'value': 111,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the PXI\_Trig0
line before processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'PXI_TRIG1',
                'value': 112,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the PXI\_Trig1
line before processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'PXI_TRIG2',
                'value': 113,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the PXI\_Trig2
line before processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'PXI_TRIG3',
                'value': 114,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the PXI\_Trig3
line before processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'PXI_TRIG4',
                'value': 115,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the PXI\_Trig4
line before processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'PXI_TRIG5',
                'value': 116,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the PXI\_Trig5
line before processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'PXI_TRIG6',
                'value': 117,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the PXI\_Trig6
line before processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'PXI_TRIG7',
                'value': 118,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the PXI\_Trig7
line before processing the next entry in the scan list.
''',
},
            },
        ],
    },
    'MasterSlaveTriggerBus': {
        'values': [
            {
                'name': 'NONE',
                'value': 0,
'documentation': {
'description': '',
},
            },
            {
                'name': 'PXI_TRIG0',
                'value': 111,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the PXI\_Trig0
line before processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'PXI_TRIG1',
                'value': 112,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the PXI\_Trig1
line before processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'PXI_TRIG2',
                'value': 113,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the PXI\_Trig2
line before processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'PXI_TRIG3',
                'value': 114,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the PXI\_Trig3
line before processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'PXI_TRIG4',
                'value': 115,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the PXI\_Trig4
line before processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'PXI_TRIG5',
                'value': 116,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the PXI\_Trig5
line before processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'PXI_TRIG6',
                'value': 117,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the PXI\_Trig6
line before processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'PXI_TRIG7',
                'value': 118,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the PXI\_Trig7
line before processing the next entry in the scan list.
''',
},
            },
        ],
    },
    'PathCapability': {
        'values': [
            {
                'name': 'PATH_AVAILABLE',
                'value': 1,
'documentation': {
'description': 'Path Available',
},
            },
            {
                'name': 'PATH_EXISTS',
                'value': 2,
'documentation': {
'description': 'Path Exists',
},
            },
            {
                'name': 'PATH_UNSUPPORTED',
                'value': 3,
'documentation': {
'description': 'Path Unsupported',
},
            },
            {
                'name': 'RESOURCE_IN_USE',
                'value': 4,
'documentation': {
'description': 'Resource in use',
},
            },
            {
                'name': 'SOURCE_CONFLICT',
                'value': 5,
'documentation': {
'description': 'Source conflict',
},
            },
            {
                'name': 'CHANNEL_NOT_AVAILABLE',
                'value': 6,
'documentation': {
'description': 'Channel not available',
},
            },
        ],
    },
    'RelayAction': {
        'values': [
            {
                'name': 'OPEN_RELAY',
                'value': 20,
'documentation': {
'description': 'Open Relay',
},
            },
            {
                'name': 'CLOSE_RELAY',
                'value': 21,
'documentation': {
'description': 'Close Relay',
},
            },
        ],
    },
    'RelayPosition': {
        'values': [
            {
                'name': 'OPEN',
                'value': 10,
'documentation': {
'description': 'Open',
},
            },
            {
                'name': 'CLOSED',
                'value': 11,
'documentation': {
'description': 'Closed',
},
            },
        ],
    },
    'ScanAdvancedOutput': {
        'values': [
            {
                'name': 'NONE',
                'value': 0,
'documentation': {
'description': 'The switch module does not produce a Scan Advanced Output trigger.',
},
            },
            {
                'name': 'EXTERNAL',
                'value': 2,
'documentation': {
'description': '''
The switch module produces the Scan Advanced Output trigger on the
external trigger output.
''',
},
            },
            {
                'name': 'PXI_TRIG0',
                'value': 111,
'documentation': {
'description': '''
The switch module produces the Scan Advanced Output Trigger on the
PXI\_Trig0 line before processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'PXI_TRIG1',
                'value': 112,
'documentation': {
'description': '''
The switch module produces the Scan Advanced Output Trigger on the
PXI\_Trig1 line before processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'PXI_TRIG2',
                'value': 113,
'documentation': {
'description': '''
The switch module produces the Scan Advanced Output Trigger on the
PXI\_Trig2 line before processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'PXI_TRIG3',
                'value': 114,
'documentation': {
'description': '''
The switch module produces the Scan Advanced Output Trigger on the
PXI\_Trig3 line before processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'PXI_TRIG4',
                'value': 115,
'documentation': {
'description': '''
The switch module produces the Scan Advanced Output Trigger on the
PXI\_Trig4 line before processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'PXI_TRIG5',
                'value': 116,
'documentation': {
'description': '''
The switch module produces the Scan Advanced Output Trigger on the
PXI\_Trig5 line before processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'PXI_TRIG6',
                'value': 117,
'documentation': {
'description': '''
The switch module produces the Scan Advanced Output Trigger on the
PXI\_Trig6 line before processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'PXI_TRIG7',
                'value': 118,
'documentation': {
'description': '''
The switch module produces the Scan Advanced Output Trigger on the
PXI\_Trig7 line before processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'PXI_STAR',
                'value': 125,
'documentation': {
'description': '''
The switch module produces the Scan Advanced Output Trigger on the PXI
Star trigger bus before processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'REARCONNECTOR',
                'value': 1000,
'documentation': {
'description': '''
The switch module produces the Scan Advanced Output Trigger on the rear
connector.
''',
},
            },
            {
                'name': 'FRONTCONNECTOR',
                'value': 1001,
'documentation': {
'description': '''
The switch module produces the Scan Advanced Output Trigger on the front
connector.
''',
},
            },
            {
                'name': 'REARCONNECTOR_MODULE1',
                'value': 1021,
'documentation': {
'description': '''
The switch module produces the Scan Advanced Output Trigger on the rear
connector module 1.
''',
},
            },
            {
                'name': 'REARCONNECTOR_MODULE2',
                'value': 1022,
'documentation': {
'description': '''
The switch module produces the Scan Advanced Output Trigger on the rear
connector module 2.
''',
},
            },
            {
                'name': 'REARCONNECTOR_MODULE3',
                'value': 1023,
'documentation': {
'description': '''
The switch module produces the Scan Advanced Output Trigger on the rear
connector module 3.
''',
},
            },
            {
                'name': 'REARCONNECTOR_MODULE4',
                'value': 1024,
'documentation': {
'description': '''
The switch module produces the Scan Advanced Output Trigger on the rear
connector module 4.
''',
},
            },
            {
                'name': 'REARCONNECTOR_MODULE5',
                'value': 1025,
'documentation': {
'description': '''
The switch module produces the Scan Advanced Output Trigger on the rear
connector module 5.
''',
},
            },
            {
                'name': 'REARCONNECTOR_MODULE6',
                'value': 1026,
'documentation': {
'description': '''
The switch module produces the Scan Advanced Output Trigger on the rear
connector module 6.
''',
},
            },
            {
                'name': 'REARCONNECTOR_MODULE7',
                'value': 1027,
'documentation': {
'description': '''
The switch module produces the Scan Advanced Output Trigger on the rear
connector module 7.
''',
},
            },
            {
                'name': 'REARCONNECTOR_MODULE8',
                'value': 1028,
'documentation': {
'description': '''
The switch module produces the Scan Advanced Output Trigger on the rear
connector module 8.
''',
},
            },
            {
                'name': 'REARCONNECTOR_MODULE9',
                'value': 1029,
'documentation': {
'description': '''
The switch module produces the Scan Advanced Ouptut Trigger on the rear
connector module 9.
''',
},
            },
            {
                'name': 'REARCONNECTOR_MODULE10',
                'value': 1030,
'documentation': {
'description': '''
The switch module produces the Scan Advanced Output Trigger on the rear
connector module 10.
''',
},
            },
            {
                'name': 'REARCONNECTOR_MODULE11',
                'value': 1031,
'documentation': {
'description': '''
The switch module produces the Scan Advanced Output Trigger on the rear
connector module 11.
''',
},
            },
            {
                'name': 'REARCONNECTOR_MODULE12',
                'value': 1032,
'documentation': {
'description': '''
The switch module produces the Scan Advanced Output Trigger on the rear
connector module 12.
''',
},
            },
            {
                'name': 'FRONTCONNECTOR_MODULE1',
                'value': 1041,
'documentation': {
'description': '''
The switch module produces the Scan Advanced Output Trigger on the front
connector module 1.
''',
},
            },
            {
                'name': 'FRONTCONNECTOR_MODULE2',
                'value': 1042,
'documentation': {
'description': '''
The switch module produces the Scan Advanced Output Trigger on the front
connector module 2.
''',
},
            },
            {
                'name': 'FRONTCONNECTOR_MODULE3',
                'value': 1043,
'documentation': {
'description': '''
The switch module produces the Scan Advanced Output Trigger on the front
connector module 3.
''',
},
            },
            {
                'name': 'FRONTCONNECTOR_MODULE4',
                'value': 1044,
'documentation': {
'description': '''
The switch module produces the Scan Advanced Output Trigger on the front
connector module 4.
''',
},
            },
            {
                'name': 'FRONTCONNECTOR_MODULE5',
                'value': 1045,
'documentation': {
'description': '''
The switch module produces the Scan Advanced Output Trigger on the front
connector module 5.
''',
},
            },
            {
                'name': 'FRONTCONNECTOR_MODULE6',
                'value': 1046,
'documentation': {
'description': '''
The switch module produces the Scan Advanced Output Trigger on the front
connector module 6.
''',
},
            },
            {
                'name': 'FRONTCONNECTOR_MODULE7',
                'value': 1047,
'documentation': {
'description': '''
The switch module produces the Scan Advanced Output Trigger on the front
connector module 7.
''',
},
            },
            {
                'name': 'FRONTCONNECTOR_MODULE8',
                'value': 1048,
'documentation': {
'description': '''
The switch module produces the Scan Advanced Output Trigger on the front
connector module 8.
''',
},
            },
            {
                'name': 'FRONTCONNECTOR_MODULE9',
                'value': 1049,
'documentation': {
'description': '''
The switch module produces the Scan Advanced Output Trigger on the front
connector module 9.
''',
},
            },
            {
                'name': 'FRONTCONNECTOR_MODULE10',
                'value': 1050,
'documentation': {
'description': '''
The switch module produces the Scan Advanced Output Trigger on the front
connector module 10.
''',
},
            },
            {
                'name': 'FRONTCONNECTOR_MODULE11',
                'value': 1051,
'documentation': {
'description': '''
The switch module produces the Scan Advanced Output Trigger on the front
connector module 11.
''',
},
            },
            {
                'name': 'FRONTCONNECTOR_MODULE12',
                'value': 1052,
'documentation': {
'description': '''
The switch module produces the Scan Advanced Output Trigger on the front
connector module 12.
''',
},
            },
        ],
    },
    'ScanAdvancedOutputConfigureScanTrigger': {
        'values': [
            {
                'name': 'NONE',
                'value': 0,
'documentation': {
'description': 'None',
},
            },
            {
                'name': 'EXTERNAL',
                'value': 1,
'documentation': {
'description': 'External',
},
            },
            {
                'name': 'TTL0',
                'value': 2,
'documentation': {
'description': 'TTL0',
},
            },
            {
                'name': 'TTL1',
                'value': 3,
'documentation': {
'description': 'TTL1',
},
            },
            {
                'name': 'TTL2',
                'value': 4,
'documentation': {
'description': 'TTL2',
},
            },
            {
                'name': 'TTL3',
                'value': 5,
'documentation': {
'description': 'TTL3',
},
            },
            {
                'name': 'TTL4',
                'value': 6,
'documentation': {
'description': 'TTL4',
},
            },
            {
                'name': 'TTL5',
                'value': 7,
'documentation': {
'description': 'TTL5',
},
            },
            {
                'name': 'TTL6',
                'value': 8,
'documentation': {
'description': 'TTL6',
},
            },
            {
                'name': 'TTL7',
                'value': 9,
'documentation': {
'description': 'TTL7',
},
            },
            {
                'name': 'ECL0',
                'value': 10,
'documentation': {
'description': 'ECL0',
},
            },
            {
                'name': 'ECL1',
                'value': 11,
'documentation': {
'description': 'ECL1',
},
            },
            {
                'name': 'PXI_STAR',
                'value': 12,
'documentation': {
'description': 'PXI Star',
},
            },
            {
                'name': 'REAR_CONNECTOR',
                'value': 13,
'documentation': {
'description': 'Rear Connector',
},
            },
            {
                'name': 'FRONT_CONNECTOR',
                'value': 14,
'documentation': {
'description': 'Front Connector',
},
            },
            {
                'name': 'REAR_CONNECTOR_MODULE_1',
                'value': 15,
'documentation': {
'description': 'Rear Connector Module 1',
},
            },
            {
                'name': 'REAR_CONNECTOR_MODULE_2',
                'value': 16,
'documentation': {
'description': 'Rear Connector Module 2',
},
            },
            {
                'name': 'REAR_CONNECTOR_MODULE_3',
                'value': 17,
'documentation': {
'description': 'Rear Connector Module 3',
},
            },
            {
                'name': 'REAR_CONNECTOR_MODULE_4',
                'value': 18,
'documentation': {
'description': 'Rear Connector Module 4',
},
            },
            {
                'name': 'REAR_CONNECTOR_MODULE_5',
                'value': 19,
'documentation': {
'description': 'Rear Connector Module 5',
},
            },
            {
                'name': 'REAR_CONNECTOR_MODULE_6',
                'value': 20,
'documentation': {
'description': 'Rear Connector Module 6',
},
            },
            {
                'name': 'REAR_CONNECTOR_MODULE_7',
                'value': 21,
'documentation': {
'description': 'Rear Connector Module 7',
},
            },
            {
                'name': 'REAR_CONNECTOR_MODULE_8',
                'value': 22,
'documentation': {
'description': 'Rear Connector Module 8',
},
            },
            {
                'name': 'REAR_CONNECTOR_MODULE_9',
                'value': 23,
'documentation': {
'description': 'Rear Connector Module 9',
},
            },
            {
                'name': 'REAR_CONNECTOR_MODULE_10',
                'value': 24,
'documentation': {
'description': 'Rear Connector Module 10',
},
            },
            {
                'name': 'REAR_CONNECTOR_MODULE_11',
                'value': 25,
'documentation': {
'description': 'Rear Connector Module 11',
},
            },
            {
                'name': 'REAR_CONNECTOR_MODULE_12',
                'value': 26,
'documentation': {
'description': 'Rear Connector Module 12',
},
            },
            {
                'name': 'FRONT_CONNECTOR_MODULE_1',
                'value': 27,
'documentation': {
'description': 'Front Connector Module 1',
},
            },
            {
                'name': 'FRONT_CONNECTOR_MODULE_2',
                'value': 28,
'documentation': {
'description': 'Front Connector Module 2',
},
            },
            {
                'name': 'FRONT_CONNECTOR_MODULE_3',
                'value': 29,
'documentation': {
'description': 'Front Connector Module 3',
},
            },
            {
                'name': 'FRONT_CONNECTOR_MODULE_4',
                'value': 30,
'documentation': {
'description': 'Front Connector Module 4',
},
            },
            {
                'name': 'FRONT_CONNECTOR_MODULE_5',
                'value': 31,
'documentation': {
'description': 'Front Connector Module 5',
},
            },
            {
                'name': 'FRONT_CONNECTOR_MODULE_6',
                'value': 32,
'documentation': {
'description': 'Front Connector Module 6',
},
            },
            {
                'name': 'FRONT_CONNECTOR_MODULE_7',
                'value': 33,
'documentation': {
'description': 'Front Connector Module 7',
},
            },
            {
                'name': 'FRONT_CONNECTOR_MODULE_8',
                'value': 34,
'documentation': {
'description': 'Front Connector Module 8',
},
            },
            {
                'name': 'FRONT_CONNECTOR_MODULE_9',
                'value': 35,
'documentation': {
'description': 'Front Connector Module 9',
},
            },
            {
                'name': 'FRONT_CONNECTOR_MODULE_10',
                'value': 36,
'documentation': {
'description': 'Front Connector Module 10',
},
            },
            {
                'name': 'FRONT_CONNECTOR_MODULE_11',
                'value': 37,
'documentation': {
'description': 'Front Connector Module 11',
},
            },
            {
                'name': 'FRONT_CONNECTOR_MODULE_12',
                'value': 38,
'documentation': {
'description': 'Front Connector Module 12',
},
            },
        ],
    },
    'ScanAdvancedPolarity': {
        'values': [
            {
                'name': 'RISING_EDGE',
                'value': 0,
'documentation': {
'description': 'The trigger occurs on the rising edge of the signal.',
},
            },
            {
                'name': 'FALLING_EDGE',
                'value': 1,
'documentation': {
'description': 'The trigger occurs on the falling edge of the signal.',
},
            },
        ],
    },
    'ScanMode': {
        'values': [
            {
                'name': 'NONE',
                'value': 0,
'documentation': {
'description': 'No implicit action on connections when scanning.',
},
            },
            {
                'name': 'BREAK_BEFORE_MAKE',
                'value': 1,
'documentation': {
'description': '''
When scanning, the switch module breaks existing connections before
making new connections.
''',
},
            },
            {
                'name': 'BREAK_AFTER_MAKE',
                'value': 2,
'documentation': {
'description': '''
When scanning, the switch module breaks existing connections after
making new connections.
''',
},
            },
        ],
    },
    'TriggerInput': {
        'values': [
            {
                'name': 'IMMEDIATE',
                'value': 1,
'documentation': {
'description': '''
The switch module does not wait for a trigger before processing the next
entry in the scan list.
''',
},
            },
            {
                'name': 'EXTERNAL',
                'value': 2,
'documentation': {
'description': '''
The switch module waits until it receives a trigger from an external
source through the external trigger input before processing the next
entry in the scan list.
''',
},
            },
            {
                'name': 'SW_TRIG_FUNC',
                'value': 3,
'documentation': {
'description': '''
The switch module waits until you call the `niSwitch Send Software
Trigger <switchviref.chm::/niSwitch_Send_Software_Trigger.html>`__ VI
before processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'PXI_TRIG0',
                'value': 111,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the PXI\_Trig0
line before processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'PXI_TRIG1',
                'value': 112,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the PXI\_Trig1
line before processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'PXI_TRIG2',
                'value': 113,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the PXI\_Trig2
line before processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'PXI_TRIG3',
                'value': 114,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the PXI\_Trig3
line before processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'PXI_TRIG4',
                'value': 115,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the PXI\_Trig4
line before processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'PXI_TRIG5',
                'value': 116,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the PXI\_Trig5
line before processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'PXI_TRIG6',
                'value': 117,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the PXI\_Trig6
line before processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'PXI_TRIG7',
                'value': 118,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the PXI\_Trig7
line before processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'PXI_STAR',
                'value': 125,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the PXI star
trigger bus before processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'REARCONNECTOR',
                'value': 1000,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the rear
connector.
''',
},
            },
            {
                'name': 'FRONTCONNECTOR',
                'value': 1001,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the front
connector.
''',
},
            },
            {
                'name': 'REARCONNECTOR_MODULE1',
                'value': 1021,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the rear
connector module 1.
''',
},
            },
            {
                'name': 'REARCONNECTOR_MODULE2',
                'value': 1022,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the rear
connector module 2.
''',
},
            },
            {
                'name': 'REARCONNECTOR_MODULE3',
                'value': 1023,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the rear
connector module 3.
''',
},
            },
            {
                'name': 'REARCONNECTOR_MODULE4',
                'value': 1024,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the rear
connector module 4.
''',
},
            },
            {
                'name': 'REARCONNECTOR_MODULE5',
                'value': 1025,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the rear
connector module 5.
''',
},
            },
            {
                'name': 'REARCONNECTOR_MODULE6',
                'value': 1026,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the rear
connector module 6.
''',
},
            },
            {
                'name': 'REARCONNECTOR_MODULE7',
                'value': 1027,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the rear
connector module 7.
''',
},
            },
            {
                'name': 'REARCONNECTOR_MODULE8',
                'value': 1028,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the rear
connector module 8.
''',
},
            },
            {
                'name': 'REARCONNECTOR_MODULE9',
                'value': 1029,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the rear
connector module 9.
''',
},
            },
            {
                'name': 'REARCONNECTOR_MODULE10',
                'value': 1030,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the rear
connector module 10.
''',
},
            },
            {
                'name': 'REARCONNECTOR_MODULE11',
                'value': 1031,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the rear
connector module 11.
''',
},
            },
            {
                'name': 'REARCONNECTOR_MODULE12',
                'value': 1032,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the rear
connector module 12.
''',
},
            },
            {
                'name': 'FRONTCONNECTOR_MODULE1',
                'value': 1041,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the front
connector module 1.
''',
},
            },
            {
                'name': 'FRONTCONNECTOR_MODULE2',
                'value': 1042,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the front
connector module 2.
''',
},
            },
            {
                'name': 'FRONTCONNECTOR_MODULE3',
                'value': 1043,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the front
connector module 3.
''',
},
            },
            {
                'name': 'FRONTCONNECTOR_MODULE4',
                'value': 1044,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the front
connector module 4.
''',
},
            },
            {
                'name': 'FRONTCONNECTOR_MODULE5',
                'value': 1045,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the front
connector module 5.
''',
},
            },
            {
                'name': 'FRONTCONNECTOR_MODULE6',
                'value': 1046,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the front
connector module 6.
''',
},
            },
            {
                'name': 'FRONTCONNECTOR_MODULE7',
                'value': 1047,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the front
connector module 7.
''',
},
            },
            {
                'name': 'FRONTCONNECTOR_MODULE8',
                'value': 1048,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the front
connector module 8.
''',
},
            },
            {
                'name': 'FRONTCONNECTOR_MODULE9',
                'value': 1049,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the front
connector module 9.
''',
},
            },
            {
                'name': 'FRONTCONNECTOR_MODULE10',
                'value': 1050,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the front
connector module 10.
''',
},
            },
            {
                'name': 'FRONTCONNECTOR_MODULE11',
                'value': 1051,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the front
connector module 11.
''',
},
            },
            {
                'name': 'FRONTCONNECTOR_MODULE12',
                'value': 1052,
'documentation': {
'description': '''
The switch module waits until it receives a trigger on the front
connector module 12.
''',
},
            },
        ],
    },
    'TriggerInputBusLine': {
        'values': [
            {
                'name': 'NONE',
                'value': 0,
'documentation': {
'description': 'None',
},
            },
            {
                'name': 'TTL0',
                'value': 2,
'documentation': {
'description': 'TTL0',
},
            },
            {
                'name': 'TTL1',
                'value': 3,
'documentation': {
'description': 'TTL1',
},
            },
            {
                'name': 'TTL2',
                'value': 4,
'documentation': {
'description': 'TTL2',
},
            },
            {
                'name': 'TTL3',
                'value': 5,
'documentation': {
'description': 'TTL3',
},
            },
            {
                'name': 'TTL4',
                'value': 6,
'documentation': {
'description': 'TTL4',
},
            },
            {
                'name': 'TTL5',
                'value': 7,
'documentation': {
'description': 'TTL5',
},
            },
            {
                'name': 'TTL6',
                'value': 8,
'documentation': {
'description': 'TTL6',
},
            },
            {
                'name': 'TTL7',
                'value': 9,
'documentation': {
'description': 'TTL7',
},
            },
        ],
    },
    'TriggerInputConfigureScanTrigger': {
        'values': [
            {
                'name': 'IMMEDIATE',
                'value': 0,
'documentation': {
'description': 'Immediate',
},
            },
            {
                'name': 'EXTERNAL',
                'value': 1,
'documentation': {
'description': 'External',
},
            },
            {
                'name': 'TTL0',
                'value': 2,
'documentation': {
'description': 'TTL0',
},
            },
            {
                'name': 'TTL1',
                'value': 3,
'documentation': {
'description': 'TTL1',
},
            },
            {
                'name': 'TTL2',
                'value': 4,
'documentation': {
'description': 'TTL2',
},
            },
            {
                'name': 'TTL3',
                'value': 5,
'documentation': {
'description': 'TTL3',
},
            },
            {
                'name': 'TTL4',
                'value': 6,
'documentation': {
'description': 'TTL4',
},
            },
            {
                'name': 'TTL5',
                'value': 7,
'documentation': {
'description': 'TTL5',
},
            },
            {
                'name': 'TTL6',
                'value': 8,
'documentation': {
'description': 'TTL6',
},
            },
            {
                'name': 'TTL7',
                'value': 9,
'documentation': {
'description': 'TTL7',
},
            },
            {
                'name': 'ECL0',
                'value': 10,
'documentation': {
'description': 'ECL0',
},
            },
            {
                'name': 'ECL1',
                'value': 11,
'documentation': {
'description': 'ECL1',
},
            },
            {
                'name': 'PXI_STAR',
                'value': 12,
'documentation': {
'description': 'PXI Star',
},
            },
            {
                'name': 'SOFTWARE_TRIGGER_FUNCTION',
                'value': 13,
'documentation': {
'description': 'Software Trigger Function',
},
            },
            {
                'name': 'REAR_CONNECTOR',
                'value': 14,
'documentation': {
'description': 'Rear Connector',
},
            },
            {
                'name': 'FRONT_CONNECTOR',
                'value': 15,
'documentation': {
'description': 'Front Connector',
},
            },
            {
                'name': 'REAR_CONNECTOR_OF_MODULE_1',
                'value': 16,
'documentation': {
'description': 'Rear Connector of Module 1',
},
            },
            {
                'name': 'REAR_CONNECTOR_OF_MODULE_2',
                'value': 17,
'documentation': {
'description': 'Rear Connector of Module 2',
},
            },
            {
                'name': 'REAR_CONNECTOR_OF_MODULE_3',
                'value': 18,
'documentation': {
'description': 'Rear Connector of Module 3',
},
            },
            {
                'name': 'REAR_CONNECTOR_OF_MODULE_4',
                'value': 19,
'documentation': {
'description': 'Rear Connector of Module 4',
},
            },
            {
                'name': 'REAR_CONNECTOR_OF_MODULE_5',
                'value': 20,
'documentation': {
'description': 'Rear Connector of Module 5',
},
            },
            {
                'name': 'REAR_CONNECTOR_OF_MODULE_6',
                'value': 21,
'documentation': {
'description': 'Rear Connector of Module 6',
},
            },
            {
                'name': 'REAR_CONNECTOR_OF_MODULE_7',
                'value': 22,
'documentation': {
'description': 'Rear Connector of Module 7',
},
            },
            {
                'name': 'REAR_CONNECTOR_OF_MODULE_8',
                'value': 23,
'documentation': {
'description': 'Rear Connector of Module 8',
},
            },
            {
                'name': 'REAR_CONNECTOR_OF_MODULE_9',
                'value': 24,
'documentation': {
'description': 'Rear Connector of Module 9',
},
            },
            {
                'name': 'REAR_CONNECTOR_OF_MODULE_10',
                'value': 25,
'documentation': {
'description': 'Rear Connector of Module 10',
},
            },
            {
                'name': 'REAR_CONNECTOR_OF_MODULE_11',
                'value': 26,
'documentation': {
'description': 'Rear Connector of Module 11',
},
            },
            {
                'name': 'REAR_CONNECTOR_OF_MODULE_12',
                'value': 27,
'documentation': {
'description': 'Rear Connector of Module 12',
},
            },
            {
                'name': 'FRONT_CONNECTOR_OF_MODULE_1',
                'value': 28,
'documentation': {
'description': 'Front Connector of Module 1',
},
            },
            {
                'name': 'FRONT_CONNECTOR_OF_MODULE_2',
                'value': 29,
'documentation': {
'description': 'Front Connector of Module 2',
},
            },
            {
                'name': 'FRONT_CONNECTOR_OF_MODULE_3',
                'value': 30,
'documentation': {
'description': 'Front Connector of Module 3',
},
            },
            {
                'name': 'FRONT_CONNECTOR_OF_MODULE_4',
                'value': 31,
'documentation': {
'description': 'Front Connector of Module 4',
},
            },
            {
                'name': 'FRONT_CONNECTOR_OF_MODULE_5',
                'value': 32,
'documentation': {
'description': 'Front Connector of Module 5',
},
            },
            {
                'name': 'FRONT_CONNECTOR_OF_MODULE_6',
                'value': 33,
'documentation': {
'description': 'Front Connector of Module 6',
},
            },
            {
                'name': 'FRONT_CONNECTOR_OF_MODULE_7',
                'value': 34,
'documentation': {
'description': 'Front Connector of Module 7',
},
            },
            {
                'name': 'FRONT_CONNECTOR_OF_MODULE_8',
                'value': 35,
'documentation': {
'description': 'Front Connector of Module 8',
},
            },
            {
                'name': 'FRONT_CONNECTOR_OF_MODULE_9',
                'value': 36,
'documentation': {
'description': 'Front Connector of Module 9',
},
            },
            {
                'name': 'FRONT_CONNECTOR_OF_MODULE_10',
                'value': 37,
'documentation': {
'description': 'Front Connector of Module 10',
},
            },
            {
                'name': 'FRONT_CONNECTOR_OF_MODULE_11',
                'value': 38,
'documentation': {
'description': 'Front Connector of Module 11',
},
            },
            {
                'name': 'FRONT_CONNECTOR_OF_MODULE_12',
                'value': 39,
'documentation': {
'description': 'Front Connector of Module 12',
},
            },
        ],
    },
    'TriggerInputConnector': {
        'values': [
            {
                'name': 'REAR_CONNECTOR',
                'value': 1000,
'documentation': {
'description': 'Rear Connector',
},
            },
            {
                'name': 'FRONT_CONNECTOR',
                'value': 1001,
'documentation': {
'description': 'Front Connector',
},
            },
        ],
    },
    'TriggerInputPolarity': {
        'values': [
            {
                'name': 'RISING_EDGE',
                'value': 0,
'documentation': {
'description': 'The trigger occurs on the rising edge of the signal.',
},
            },
            {
                'name': 'FALLING_EDGE',
                'value': 1,
'documentation': {
'description': 'The trigger occurs on the falling edge of the signal.',
},
            },
        ],
    },
    'TriggerMode': {
        'values': [
            {
                'name': 'SINGLE',
                'value': 0,
'documentation': {
'description': '',
},
            },
            {
                'name': 'MASTER',
                'value': 1,
'documentation': {
'description': '',
},
            },
            {
                'name': 'SLAVE',
                'value': 2,
'documentation': {
'description': '',
},
            },
        ],
    },
}
