
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
                'prefix': None,
                'value': 0,
'documentation': {
'description': '''

''',
},
            },
            {
                'name': 'PXI_TRIG0',
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
                'value': 0,
'documentation': {
'description': '''

''',
},
            },
            {
                'name': 'PXI_TRIG0',
                'prefix': None,
                'value': 111,
'documentation': {
'description': '''

''',
},
            },
            {
                'name': 'PXI_TRIG1',
                'prefix': None,
                'value': 112,
'documentation': {
'description': '''

''',
},
            },
            {
                'name': 'PXI_TRIG2',
                'prefix': None,
                'value': 113,
'documentation': {
'description': '''

''',
},
            },
            {
                'name': 'PXI_TRIG3',
                'prefix': None,
                'value': 114,
'documentation': {
'description': '''

''',
},
            },
            {
                'name': 'PXI_TRIG4',
                'prefix': None,
                'value': 115,
'documentation': {
'description': '''

''',
},
            },
            {
                'name': 'PXI_TRIG5',
                'prefix': None,
                'value': 116,
'documentation': {
'description': '''

''',
},
            },
            {
                'name': 'PXI_TRIG6',
                'prefix': None,
                'value': 117,
'documentation': {
'description': '''

''',
},
            },
            {
                'name': 'PXI_TRIG7',
                'prefix': None,
                'value': 118,
'documentation': {
'description': '''

''',
},
            },
        ],
    },
    'HandshakingInitiation': {
        'values': [
            {
                'name': 'MEASUREMENT_DEVICE_INITIATED',
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
                'value': 0,
'documentation': {
'description': '''

''',
},
            },
            {
                'name': 'PXI_TRIG0',
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
                'value': 0,
'documentation': {
'description': '''

''',
},
            },
            {
                'name': 'PXI_TRIG0',
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
                'value': 1,
'documentation': {
'description': '''
Path Available
''',
},
            },
            {
                'name': 'PATH_EXISTS',
                'prefix': None,
                'value': 2,
'documentation': {
'description': '''
Path Exists
''',
},
            },
            {
                'name': 'PATH_UNSUPPORTED',
                'prefix': None,
                'value': 3,
'documentation': {
'description': '''
Path Unsupported
''',
},
            },
            {
                'name': 'RESOURCE_IN_USE',
                'prefix': None,
                'value': 4,
'documentation': {
'description': '''
Resource in use
''',
},
            },
            {
                'name': 'SOURCE_CONFLICT',
                'prefix': None,
                'value': 5,
'documentation': {
'description': '''
Source conflict
''',
},
            },
            {
                'name': 'CHANNEL_NOT_AVAILABLE',
                'prefix': None,
                'value': 6,
'documentation': {
'description': '''
Channel not available
''',
},
            },
        ],
    },
    'RelayAction': {
        'values': [
            {
                'name': 'OPEN_RELAY',
                'prefix': None,
                'value': 20,
'documentation': {
'description': '''
Open Relay
''',
},
            },
            {
                'name': 'CLOSE_RELAY',
                'prefix': None,
                'value': 21,
'documentation': {
'description': '''
Close Relay
''',
},
            },
        ],
    },
    'RelayPosition': {
        'values': [
            {
                'name': 'OPEN',
                'prefix': None,
                'value': 10,
'documentation': {
'description': '''
Open
''',
},
            },
            {
                'name': 'CLOSED',
                'prefix': None,
                'value': 11,
'documentation': {
'description': '''
Closed
''',
},
            },
        ],
    },
    'ScanAdvancedOutput': {
        'values': [
            {
                'name': 'NONE',
                'prefix': None,
                'value': 0,
'documentation': {
'description': '''
The switch device does not produce a Scan Advanced Output trigger.
''',
},
            },
            {
                'name': 'EXTERNAL',
                'prefix': None,
                'value': 2,
'documentation': {
'description': '''
External Trigger. The switch device produces the Scan Advanced Output  trigger on the external trigger output.
''',
},
            },
            {
                'name': 'TTL0',
                'prefix': None,
                'value': 111,
'documentation': {
'description': '''
The switch device produces the Scan Advanced Output on the PXI TRIG0 line.
''',
},
            },
            {
                'name': 'TTL1',
                'prefix': None,
                'value': 112,
'documentation': {
'description': '''
The switch device produces the Scan Advanced Output on the PXI TRIG1 line.
''',
},
            },
            {
                'name': 'TTL2',
                'prefix': None,
                'value': 113,
'documentation': {
'description': '''
The switch device produces the Scan Advanced Output on the PXI TRIG2 line.
''',
},
            },
            {
                'name': 'TTL3',
                'prefix': None,
                'value': 114,
'documentation': {
'description': '''
The switch device produces the Scan Advanced Output on the PXI TRIG3 line.
''',
},
            },
            {
                'name': 'TTL4',
                'prefix': None,
                'value': 115,
'documentation': {
'description': '''
The switch device produces the Scan Advanced Output on the PXI TRIG4 line.
''',
},
            },
            {
                'name': 'TTL5',
                'prefix': None,
                'value': 116,
'documentation': {
'description': '''
The switch device produces the Scan Advanced Output on the PXI TRIG5 line.
''',
},
            },
            {
                'name': 'TTL6',
                'prefix': None,
                'value': 117,
'documentation': {
'description': '''
The switch device produces the Scan Advanced Output on the PXI TRIG6 line.
''',
},
            },
            {
                'name': 'TTL7',
                'prefix': None,
                'value': 118,
'documentation': {
'description': '''
The switch device produces the Scan Advanced Output on the PXI TRIG7 line.
''',
},
            },
            {
                'name': 'PXI_STAR',
                'prefix': None,
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
                'prefix': None,
                'value': 1000,
'documentation': {
'description': '''
The switch device produces the Scan Advanced Output  trigger on the rear connector.
''',
},
            },
            {
                'name': 'FRONTCONNECTOR',
                'prefix': None,
                'value': 1001,
'documentation': {
'description': '''
The switch device produces the Scan Advanced Output  trigger on the front connector.
''',
},
            },
            {
                'name': 'REARCONNECTOR_MODULE1',
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'name': 'RISING_EDGE',
                'prefix': None,
                'value': 0,
'documentation': {
'description': '''
The trigger occurs on the rising edge of the signal.
''',
},
            },
            {
                'name': 'FALLING_EDGE',
                'prefix': None,
                'value': 1,
'documentation': {
'description': '''
The trigger occurs on the falling edge of the signal.
''',
},
            },
        ],
    },
    'ScanMode': {
        'values': [
            {
                'name': 'NONE',
                'prefix': None,
                'value': 0,
'documentation': {
'description': '''
No implicit action on connections when scanning.
''',
},
            },
            {
                'name': 'BREAK_BEFORE_MAKE',
                'prefix': None,
                'value': 1,
'documentation': {
'description': '''
When scanning, the switch device breaks existing connections before  making new connections.
''',
},
            },
            {
                'name': 'BREAK_AFTER_MAKE',
                'prefix': None,
                'value': 2,
'documentation': {
'description': '''
When scanning, the switch device breaks existing connections after making  new connections.
''',
},
            },
        ],
    },
    'TriggerInput': {
        'values': [
            {
                'name': 'IMMEDIATE',
                'prefix': None,
                'value': 1,
'documentation': {
'description': '''
Immediate Trigger. The switch device does not wait for a trigger before  processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'EXTERNAL',
                'prefix': None,
                'value': 2,
'documentation': {
'description': '''
External Trigger. The switch device waits until it receives a trigger  from an external source through the external trigger input before  processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'SOFTWARE_TRIG',
                'prefix': None,
                'value': 3,
'documentation': {
'description': '''
The switch device waits until you call the niSwitch_SendSoftwareTrigger  function before processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'TTL0',
                'prefix': None,
                'value': 111,
'documentation': {
'description': '''
The switch device waits until it receives a trigger on the PXI TRIG0 line before processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'TTL1',
                'prefix': None,
                'value': 112,
'documentation': {
'description': '''
The switch device waits until it receives a trigger on the PXI TRIG1 line before processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'TTL2',
                'prefix': None,
                'value': 113,
'documentation': {
'description': '''
The switch device waits until it receives a trigger on the PXI TRIG2 line before processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'TTL3',
                'prefix': None,
                'value': 114,
'documentation': {
'description': '''
The switch device waits until it receives a trigger on the PXI TRIG3 line before processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'TTL4',
                'prefix': None,
                'value': 115,
'documentation': {
'description': '''
The switch device waits until it receives a trigger on the PXI TRIG4 line before processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'TTL5',
                'prefix': None,
                'value': 116,
'documentation': {
'description': '''
The switch device waits until it receives a trigger on the PXI TRIG5 line before processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'TTL6',
                'prefix': None,
                'value': 117,
'documentation': {
'description': '''
The switch device waits until it receives a trigger on the PXI TRIG6 line before processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'TTL7',
                'prefix': None,
                'value': 118,
'documentation': {
'description': '''
The switch device waits until it receives a trigger on the PXI TRIG7 line before processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'PXI_STAR',
                'prefix': None,
                'value': 125,
'documentation': {
'description': '''
The switch device waits until it receives a trigger on the PXI STAR  trigger bus before processing the next entry in the scan list.
''',
},
            },
            {
                'name': 'REARCONNECTOR',
                'prefix': None,
                'value': 1000,
'documentation': {
'description': '''
The switch device waits until it receives a trigger on the  rear connector.
''',
},
            },
            {
                'name': 'FRONTCONNECTOR',
                'prefix': None,
                'value': 1001,
'documentation': {
'description': '''
The switch device waits until it receives a trigger on the  front connector.
''',
},
            },
            {
                'name': 'REARCONNECTOR_MODULE1',
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'prefix': None,
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
                'name': 'RISING_EDGE',
                'prefix': None,
                'value': 0,
'documentation': {
'description': '''
The trigger occurs on the rising edge of the signal.
''',
},
            },
            {
                'name': 'FALLING_EDGE',
                'prefix': None,
                'value': 1,
'documentation': {
'description': '''
The trigger occurs on the falling edge of the signal.
''',
},
            },
        ],
    },
    'TriggerMode': {
        'values': [
            {
                'name': 'SINGLE',
                'prefix': None,
                'value': 0,
'documentation': {
'description': '''

''',
},
            },
            {
                'name': 'MASTER',
                'prefix': None,
                'value': 1,
'documentation': {
'description': '''

''',
},
            },
            {
                'name': 'SLAVE',
                'prefix': None,
                'value': 2,
'documentation': {
'description': '''

''',
},
            },
        ],
    },
}
