
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
                'name': 'NISWITCH_VAL_NONE',
                'value': 0,
'documentation': {
'description': 'The switch device does not produce a Scan Advanced Output trigger.',
},
            },
            {
                'name': 'NISWITCH_VAL_EXTERNAL',
                'value': 2,
'documentation': {
'description': 'External Trigger. The switch device produces the Scan Advanced Output  trigger on the external trigger output.',
},
            },
            {
                'name': 'NISWITCH_VAL_TTL0',
                'value': 111,
'documentation': {
'description': 'The switch device produces the Scan Advanced Output on the PXI TRIG0 line.',
},
            },
            {
                'name': 'NISWITCH_VAL_TTL1',
                'value': 112,
'documentation': {
'description': 'The switch device produces the Scan Advanced Output on the PXI TRIG1 line.',
},
            },
            {
                'name': 'NISWITCH_VAL_TTL2',
                'value': 113,
'documentation': {
'description': 'The switch device produces the Scan Advanced Output on the PXI TRIG2 line.',
},
            },
            {
                'name': 'NISWITCH_VAL_TTL3',
                'value': 114,
'documentation': {
'description': 'The switch device produces the Scan Advanced Output on the PXI TRIG3 line.',
},
            },
            {
                'name': 'NISWITCH_VAL_TTL4',
                'value': 115,
'documentation': {
'description': 'The switch device produces the Scan Advanced Output on the PXI TRIG4 line.',
},
            },
            {
                'name': 'NISWITCH_VAL_TTL5',
                'value': 116,
'documentation': {
'description': 'The switch device produces the Scan Advanced Output on the PXI TRIG5 line.',
},
            },
            {
                'name': 'NISWITCH_VAL_TTL6',
                'value': 117,
'documentation': {
'description': 'The switch device produces the Scan Advanced Output on the PXI TRIG6 line.',
},
            },
            {
                'name': 'NISWITCH_VAL_TTL7',
                'value': 118,
'documentation': {
'description': 'The switch device produces the Scan Advanced Output on the PXI TRIG7 line.',
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
                'name': 'NISWITCH_VAL_REARCONNECTOR',
                'value': 1000,
'documentation': {
'description': 'The switch device produces the Scan Advanced Output  trigger on the rear connector.',
},
            },
            {
                'name': 'NISWITCH_VAL_FRONTCONNECTOR',
                'value': 1001,
'documentation': {
'description': 'The switch device produces the Scan Advanced Output  trigger on the front connector.',
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
    'ScanAdvancedPolarity': {
        'values': [
            {
                'name': 'NISWITCH_VAL_RISING_EDGE',
                'value': 0,
'documentation': {
'description': 'The trigger occurs on the rising edge of the signal.',
},
            },
            {
                'name': 'NISWITCH_VAL_FALLING_EDGE',
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
                'name': 'NISWITCH_VAL_NONE',
                'value': 0,
'documentation': {
'description': 'No implicit action on connections when scanning.',
},
            },
            {
                'name': 'NISWITCH_VAL_BREAK_BEFORE_MAKE',
                'value': 1,
'documentation': {
'description': 'When scanning, the switch device breaks existing connections before  making new connections.',
},
            },
            {
                'name': 'NISWITCH_VAL_BREAK_AFTER_MAKE',
                'value': 2,
'documentation': {
'description': 'When scanning, the switch device breaks existing connections after making  new connections.',
},
            },
        ],
    },
    'TriggerInput': {
        'values': [
            {
                'name': 'NISWITCH_VAL_IMMEDIATE',
                'value': 1,
'documentation': {
'description': 'Immediate Trigger. The switch device does not wait for a trigger before  processing the next entry in the scan list.',
},
            },
            {
                'name': 'NISWITCH_VAL_EXTERNAL',
                'value': 2,
'documentation': {
'description': 'External Trigger. The switch device waits until it receives a trigger  from an external source through the external trigger input before  processing the next entry in the scan list.',
},
            },
            {
                'name': 'NISWITCH_VAL_SOFTWARE_TRIG',
                'value': 3,
'documentation': {
'description': 'The switch device waits until you call the niSwitch_SendSoftwareTrigger  function before processing the next entry in the scan list.',
},
            },
            {
                'name': 'NISWITCH_VAL_TTL0',
                'value': 111,
'documentation': {
'description': 'The switch device waits until it receives a trigger on the PXI TRIG0 line before processing the next entry in the scan list.',
},
            },
            {
                'name': 'NISWITCH_VAL_TTL1',
                'value': 112,
'documentation': {
'description': 'The switch device waits until it receives a trigger on the PXI TRIG1 line before processing the next entry in the scan list.',
},
            },
            {
                'name': 'NISWITCH_VAL_TTL2',
                'value': 113,
'documentation': {
'description': 'The switch device waits until it receives a trigger on the PXI TRIG2 line before processing the next entry in the scan list.',
},
            },
            {
                'name': 'NISWITCH_VAL_TTL3',
                'value': 114,
'documentation': {
'description': 'The switch device waits until it receives a trigger on the PXI TRIG3 line before processing the next entry in the scan list.',
},
            },
            {
                'name': 'NISWITCH_VAL_TTL4',
                'value': 115,
'documentation': {
'description': 'The switch device waits until it receives a trigger on the PXI TRIG4 line before processing the next entry in the scan list.',
},
            },
            {
                'name': 'NISWITCH_VAL_TTL5',
                'value': 116,
'documentation': {
'description': 'The switch device waits until it receives a trigger on the PXI TRIG5 line before processing the next entry in the scan list.',
},
            },
            {
                'name': 'NISWITCH_VAL_TTL6',
                'value': 117,
'documentation': {
'description': 'The switch device waits until it receives a trigger on the PXI TRIG6 line before processing the next entry in the scan list.',
},
            },
            {
                'name': 'NISWITCH_VAL_TTL7',
                'value': 118,
'documentation': {
'description': 'The switch device waits until it receives a trigger on the PXI TRIG7 line before processing the next entry in the scan list.',
},
            },
            {
                'name': 'NISWITCH_VAL_PXI_STAR',
                'value': 125,
'documentation': {
'description': 'The switch device waits until it receives a trigger on the PXI STAR  trigger bus before processing the next entry in the scan list.',
},
            },
            {
                'name': 'NISWITCH_VAL_REARCONNECTOR',
                'value': 1000,
'documentation': {
'description': 'The switch device waits until it receives a trigger on the  rear connector.',
},
            },
            {
                'name': 'NISWITCH_VAL_FRONTCONNECTOR',
                'value': 1001,
'documentation': {
'description': 'The switch device waits until it receives a trigger on the  front connector.',
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
    'TriggerInputPolarity': {
        'values': [
            {
                'name': 'NISWITCH_VAL_RISING_EDGE',
                'value': 0,
'documentation': {
'description': 'The trigger occurs on the rising edge of the signal.',
},
            },
            {
                'name': 'NISWITCH_VAL_FALLING_EDGE',
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
