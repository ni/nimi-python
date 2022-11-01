# -*- coding: utf-8 -*-
# This file is generated from NI-SWITCH API metadata version 23.0.0d69
enums = {
    'CabledModuleScanAdvancedBus': {
        'values': [
            {
                'documentation': {
                    'description': ''
                },
                'name': 'NISWITCH_VAL_NONE',
                'value': 0
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the PXI\\_Trig0\nline before processing the next entry in the scan list.\n'
                },
                'name': 'NISWITCH_VAL_PXI_TRIG0',
                'value': 111
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the PXI\\_Trig1\nline before processing the next entry in the scan list.\n'
                },
                'name': 'NISWITCH_VAL_PXI_TRIG1',
                'value': 112
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the PXI\\_Trig2\nline before processing the next entry in the scan list.\n'
                },
                'name': 'NISWITCH_VAL_PXI_TRIG2',
                'value': 113
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the PXI\\_Trig3\nline before processing the next entry in the scan list.\n'
                },
                'name': 'NISWITCH_VAL_PXI_TRIG3',
                'value': 114
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the PXI\\_Trig4\nline before processing the next entry in the scan list.\n'
                },
                'name': 'NISWITCH_VAL_PXI_TRIG4',
                'value': 115
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the PXI\\_Trig5\nline before processing the next entry in the scan list.\n'
                },
                'name': 'NISWITCH_VAL_PXI_TRIG5',
                'value': 116
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the PXI\\_Trig6\nline before processing the next entry in the scan list.\n'
                },
                'name': 'NISWITCH_VAL_PXI_TRIG6',
                'value': 117
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the PXI\\_Trig7\nline before processing the next entry in the scan list.\n'
                },
                'name': 'NISWITCH_VAL_PXI_TRIG7',
                'value': 118
            }
        ]
    },
    'CabledModuleTriggerBus': {
        'values': [
            {
                'documentation': {
                    'description': ''
                },
                'name': 'NISWITCH_VAL_NONE',
                'value': 0
            },
            {
                'documentation': {
                    'description': ''
                },
                'name': 'NISWITCH_VAL_PXI_TRIG0',
                'value': 111
            },
            {
                'documentation': {
                    'description': ''
                },
                'name': 'NISWITCH_VAL_PXI_TRIG1',
                'value': 112
            },
            {
                'documentation': {
                    'description': ''
                },
                'name': 'NISWITCH_VAL_PXI_TRIG2',
                'value': 113
            },
            {
                'documentation': {
                    'description': ''
                },
                'name': 'NISWITCH_VAL_PXI_TRIG3',
                'value': 114
            },
            {
                'documentation': {
                    'description': ''
                },
                'name': 'NISWITCH_VAL_PXI_TRIG4',
                'value': 115
            },
            {
                'documentation': {
                    'description': ''
                },
                'name': 'NISWITCH_VAL_PXI_TRIG5',
                'value': 116
            },
            {
                'documentation': {
                    'description': ''
                },
                'name': 'NISWITCH_VAL_PXI_TRIG6',
                'value': 117
            },
            {
                'documentation': {
                    'description': ''
                },
                'name': 'NISWITCH_VAL_PXI_TRIG7',
                'value': 118
            }
        ]
    },
    'HandshakingInitiation': {
        'values': [
            {
                'documentation': {
                    'description': '\nThe `niSwitch Initiate\nScan <switchviref.chm::/niSwitch_Initiate_Scan.html>`__ VI does not\nreturn until the switch hardware is waiting for a trigger input. This\nensures that if you initiate the measurement device after calling the\n`niSwitch Initiate\nScan <switchviref.chm::/niSwitch_Initiate_Scan.html>`__ VI , the switch\nis sure to receive the first measurement complete (MC) signal sent by\nthe measurement device. The measurement device should be configured to\nfirst take a measurement, send MC, then wait for scanner advanced output\nsignal. Thus, the first MC of the measurement device initiates\nhandshaking.\n'
                },
                'name': 'NISWITCH_VAL_MEASUREMENT_DEVICE_INITIATED',
                'value': 0
            },
            {
                'documentation': {
                    'description': '\nThe `niSwitch Initiate\nScan <switchviref.chm::/niSwitch_Initiate_Scan.html>`__ VI returns\nimmediately after beginning scan list execution. It is assumed that the\nmeasurement device has already been configured and is waiting for the\nscanner advanced signal. The measurement should be configured to first\nwait for a trigger, then take a measurement. Thus, the first scanner\nadvanced output signal of the switch module initiates handshaking.\n'
                },
                'name': 'NISWITCH_VAL_SWITCH_INITIATED',
                'value': 1
            }
        ]
    },
    'MasterSlaveScanAdvancedBus': {
        'values': [
            {
                'documentation': {
                    'description': ''
                },
                'name': 'NISWITCH_VAL_NONE',
                'value': 0
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the PXI\\_Trig0\nline before processing the next entry in the scan list.\n'
                },
                'name': 'NISWITCH_VAL_PXI_TRIG0',
                'value': 111
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the PXI\\_Trig1\nline before processing the next entry in the scan list.\n'
                },
                'name': 'NISWITCH_VAL_PXI_TRIG1',
                'value': 112
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the PXI\\_Trig2\nline before processing the next entry in the scan list.\n'
                },
                'name': 'NISWITCH_VAL_PXI_TRIG2',
                'value': 113
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the PXI\\_Trig3\nline before processing the next entry in the scan list.\n'
                },
                'name': 'NISWITCH_VAL_PXI_TRIG3',
                'value': 114
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the PXI\\_Trig4\nline before processing the next entry in the scan list.\n'
                },
                'name': 'NISWITCH_VAL_PXI_TRIG4',
                'value': 115
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the PXI\\_Trig5\nline before processing the next entry in the scan list.\n'
                },
                'name': 'NISWITCH_VAL_PXI_TRIG5',
                'value': 116
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the PXI\\_Trig6\nline before processing the next entry in the scan list.\n'
                },
                'name': 'NISWITCH_VAL_PXI_TRIG6',
                'value': 117
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the PXI\\_Trig7\nline before processing the next entry in the scan list.\n'
                },
                'name': 'NISWITCH_VAL_PXI_TRIG7',
                'value': 118
            }
        ]
    },
    'MasterSlaveTriggerBus': {
        'values': [
            {
                'documentation': {
                    'description': ''
                },
                'name': 'NISWITCH_VAL_NONE',
                'value': 0
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the PXI\\_Trig0\nline before processing the next entry in the scan list.\n'
                },
                'name': 'NISWITCH_VAL_PXI_TRIG0',
                'value': 111
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the PXI\\_Trig1\nline before processing the next entry in the scan list.\n'
                },
                'name': 'NISWITCH_VAL_PXI_TRIG1',
                'value': 112
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the PXI\\_Trig2\nline before processing the next entry in the scan list.\n'
                },
                'name': 'NISWITCH_VAL_PXI_TRIG2',
                'value': 113
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the PXI\\_Trig3\nline before processing the next entry in the scan list.\n'
                },
                'name': 'NISWITCH_VAL_PXI_TRIG3',
                'value': 114
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the PXI\\_Trig4\nline before processing the next entry in the scan list.\n'
                },
                'name': 'NISWITCH_VAL_PXI_TRIG4',
                'value': 115
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the PXI\\_Trig5\nline before processing the next entry in the scan list.\n'
                },
                'name': 'NISWITCH_VAL_PXI_TRIG5',
                'value': 116
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the PXI\\_Trig6\nline before processing the next entry in the scan list.\n'
                },
                'name': 'NISWITCH_VAL_PXI_TRIG6',
                'value': 117
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the PXI\\_Trig7\nline before processing the next entry in the scan list.\n'
                },
                'name': 'NISWITCH_VAL_PXI_TRIG7',
                'value': 118
            }
        ]
    },
    'PathCapability': {
        'values': [
            {
                'documentation': {
                    'description': 'Path Available'
                },
                'name': 'NISWITCH_VAL_PATH_AVAILABLE',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Path Exists'
                },
                'name': 'NISWITCH_VAL_PATH_EXISTS',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Path Unsupported'
                },
                'name': 'NISWITCH_VAL_PATH_UNSUPPORTED',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'Resource in use'
                },
                'name': 'NISWITCH_VAL_RESOURCE_IN_USE',
                'value': 4
            },
            {
                'documentation': {
                    'description': 'Source conflict'
                },
                'name': 'NISWITCH_VAL_SOURCE_CONFLICT',
                'value': 5
            },
            {
                'documentation': {
                    'description': 'Channel not available'
                },
                'name': 'NISWITCH_VAL_CHANNEL_NOT_AVAILABLE',
                'value': 6
            }
        ]
    },
    'RelayAction': {
        'values': [
            {
                'documentation': {
                    'description': 'Open Relay'
                },
                'name': 'NISWITCH_VAL_OPEN_RELAY',
                'value': 20
            },
            {
                'documentation': {
                    'description': 'Close Relay'
                },
                'name': 'NISWITCH_VAL_CLOSE_RELAY',
                'value': 21
            }
        ]
    },
    'RelayPosition': {
        'values': [
            {
                'documentation': {
                    'description': 'Open'
                },
                'name': 'NISWITCH_VAL_OPEN',
                'value': 10
            },
            {
                'documentation': {
                    'description': 'Closed'
                },
                'name': 'NISWITCH_VAL_CLOSED',
                'value': 11
            }
        ]
    },
    'ScanAdvancedOutput': {
        'values': [
            {
                'documentation': {
                    'description': 'The switch device does not produce a Scan Advanced Output trigger.'
                },
                'name': 'NISWITCH_VAL_NONE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'External Trigger. The switch device produces the Scan Advanced Output  trigger on the external trigger output.'
                },
                'name': 'NISWITCH_VAL_EXTERNAL',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'The switch device produces the Scan Advanced Output on the PXI TRIG0 line.'
                },
                'name': 'NISWITCH_VAL_TTL0',
                'value': 111
            },
            {
                'documentation': {
                    'description': 'The switch device produces the Scan Advanced Output on the PXI TRIG1 line.'
                },
                'name': 'NISWITCH_VAL_TTL1',
                'value': 112
            },
            {
                'documentation': {
                    'description': 'The switch device produces the Scan Advanced Output on the PXI TRIG2 line.'
                },
                'name': 'NISWITCH_VAL_TTL2',
                'value': 113
            },
            {
                'documentation': {
                    'description': 'The switch device produces the Scan Advanced Output on the PXI TRIG3 line.'
                },
                'name': 'NISWITCH_VAL_TTL3',
                'value': 114
            },
            {
                'documentation': {
                    'description': 'The switch device produces the Scan Advanced Output on the PXI TRIG4 line.'
                },
                'name': 'NISWITCH_VAL_TTL4',
                'value': 115
            },
            {
                'documentation': {
                    'description': 'The switch device produces the Scan Advanced Output on the PXI TRIG5 line.'
                },
                'name': 'NISWITCH_VAL_TTL5',
                'value': 116
            },
            {
                'documentation': {
                    'description': 'The switch device produces the Scan Advanced Output on the PXI TRIG6 line.'
                },
                'name': 'NISWITCH_VAL_TTL6',
                'value': 117
            },
            {
                'documentation': {
                    'description': 'The switch device produces the Scan Advanced Output on the PXI TRIG7 line.'
                },
                'name': 'NISWITCH_VAL_TTL7',
                'value': 118
            },
            {
                'documentation': {
                    'description': '\nThe switch module produces the Scan Advanced Output Trigger on the PXI\nStar trigger bus before processing the next entry in the scan list.\n'
                },
                'name': 'NISWITCH_VAL_PXI_STAR',
                'value': 125
            },
            {
                'documentation': {
                    'description': 'The switch device produces the Scan Advanced Output  trigger on the rear connector.'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR',
                'value': 1000
            },
            {
                'documentation': {
                    'description': 'The switch device produces the Scan Advanced Output  trigger on the front connector.'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR',
                'value': 1001
            },
            {
                'documentation': {
                    'description': '\nThe switch module produces the Scan Advanced Output Trigger on the rear\nconnector module 1.\n'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE1',
                'value': 1021
            },
            {
                'documentation': {
                    'description': '\nThe switch module produces the Scan Advanced Output Trigger on the rear\nconnector module 2.\n'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE2',
                'value': 1022
            },
            {
                'documentation': {
                    'description': '\nThe switch module produces the Scan Advanced Output Trigger on the rear\nconnector module 3.\n'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE3',
                'value': 1023
            },
            {
                'documentation': {
                    'description': '\nThe switch module produces the Scan Advanced Output Trigger on the rear\nconnector module 4.\n'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE4',
                'value': 1024
            },
            {
                'documentation': {
                    'description': '\nThe switch module produces the Scan Advanced Output Trigger on the rear\nconnector module 5.\n'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE5',
                'value': 1025
            },
            {
                'documentation': {
                    'description': '\nThe switch module produces the Scan Advanced Output Trigger on the rear\nconnector module 6.\n'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE6',
                'value': 1026
            },
            {
                'documentation': {
                    'description': '\nThe switch module produces the Scan Advanced Output Trigger on the rear\nconnector module 7.\n'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE7',
                'value': 1027
            },
            {
                'documentation': {
                    'description': '\nThe switch module produces the Scan Advanced Output Trigger on the rear\nconnector module 8.\n'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE8',
                'value': 1028
            },
            {
                'documentation': {
                    'description': '\nThe switch module produces the Scan Advanced Ouptut Trigger on the rear\nconnector module 9.\n'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE9',
                'value': 1029
            },
            {
                'documentation': {
                    'description': '\nThe switch module produces the Scan Advanced Output Trigger on the rear\nconnector module 10.\n'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE10',
                'value': 1030
            },
            {
                'documentation': {
                    'description': '\nThe switch module produces the Scan Advanced Output Trigger on the rear\nconnector module 11.\n'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE11',
                'value': 1031
            },
            {
                'documentation': {
                    'description': '\nThe switch module produces the Scan Advanced Output Trigger on the rear\nconnector module 12.\n'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE12',
                'value': 1032
            },
            {
                'documentation': {
                    'description': '\nThe switch module produces the Scan Advanced Output Trigger on the front\nconnector module 1.\n'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE1',
                'value': 1041
            },
            {
                'documentation': {
                    'description': '\nThe switch module produces the Scan Advanced Output Trigger on the front\nconnector module 2.\n'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE2',
                'value': 1042
            },
            {
                'documentation': {
                    'description': '\nThe switch module produces the Scan Advanced Output Trigger on the front\nconnector module 3.\n'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE3',
                'value': 1043
            },
            {
                'documentation': {
                    'description': '\nThe switch module produces the Scan Advanced Output Trigger on the front\nconnector module 4.\n'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE4',
                'value': 1044
            },
            {
                'documentation': {
                    'description': '\nThe switch module produces the Scan Advanced Output Trigger on the front\nconnector module 5.\n'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE5',
                'value': 1045
            },
            {
                'documentation': {
                    'description': '\nThe switch module produces the Scan Advanced Output Trigger on the front\nconnector module 6.\n'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE6',
                'value': 1046
            },
            {
                'documentation': {
                    'description': '\nThe switch module produces the Scan Advanced Output Trigger on the front\nconnector module 7.\n'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE7',
                'value': 1047
            },
            {
                'documentation': {
                    'description': '\nThe switch module produces the Scan Advanced Output Trigger on the front\nconnector module 8.\n'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE8',
                'value': 1048
            },
            {
                'documentation': {
                    'description': '\nThe switch module produces the Scan Advanced Output Trigger on the front\nconnector module 9.\n'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE9',
                'value': 1049
            },
            {
                'documentation': {
                    'description': '\nThe switch module produces the Scan Advanced Output Trigger on the front\nconnector module 10.\n'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE10',
                'value': 1050
            },
            {
                'documentation': {
                    'description': '\nThe switch module produces the Scan Advanced Output Trigger on the front\nconnector module 11.\n'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE11',
                'value': 1051
            },
            {
                'documentation': {
                    'description': '\nThe switch module produces the Scan Advanced Output Trigger on the front\nconnector module 12.\n'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE12',
                'value': 1052
            }
        ]
    },
    'ScanAdvancedPolarity': {
        'values': [
            {
                'documentation': {
                    'description': 'The trigger occurs on the rising edge of the signal.'
                },
                'name': 'NISWITCH_VAL_RISING_EDGE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'The trigger occurs on the falling edge of the signal.'
                },
                'name': 'NISWITCH_VAL_FALLING_EDGE',
                'value': 1
            }
        ]
    },
    'ScanMode': {
        'values': [
            {
                'documentation': {
                    'description': 'No implicit action on connections when scanning.'
                },
                'name': 'NISWITCH_VAL_NONE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'When scanning, the switch device breaks existing connections before  making new connections.'
                },
                'name': 'NISWITCH_VAL_BREAK_BEFORE_MAKE',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'When scanning, the switch device breaks existing connections after making  new connections.'
                },
                'name': 'NISWITCH_VAL_BREAK_AFTER_MAKE',
                'value': 2
            }
        ]
    },
    'TriggerInput': {
        'values': [
            {
                'documentation': {
                    'description': 'Immediate Trigger. The switch device does not wait for a trigger before  processing the next entry in the scan list.'
                },
                'name': 'NISWITCH_VAL_IMMEDIATE',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'External Trigger. The switch device waits until it receives a trigger  from an external source through the external trigger input before  processing the next entry in the scan list.'
                },
                'name': 'NISWITCH_VAL_EXTERNAL',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'The switch device waits until you call the niSwitch_SendSoftwareTrigger  function before processing the next entry in the scan list.'
                },
                'name': 'NISWITCH_VAL_SOFTWARE_TRIG',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'The switch device waits until it receives a trigger on the PXI TRIG0 line before processing the next entry in the scan list.'
                },
                'name': 'NISWITCH_VAL_TTL0',
                'value': 111
            },
            {
                'documentation': {
                    'description': 'The switch device waits until it receives a trigger on the PXI TRIG1 line before processing the next entry in the scan list.'
                },
                'name': 'NISWITCH_VAL_TTL1',
                'value': 112
            },
            {
                'documentation': {
                    'description': 'The switch device waits until it receives a trigger on the PXI TRIG2 line before processing the next entry in the scan list.'
                },
                'name': 'NISWITCH_VAL_TTL2',
                'value': 113
            },
            {
                'documentation': {
                    'description': 'The switch device waits until it receives a trigger on the PXI TRIG3 line before processing the next entry in the scan list.'
                },
                'name': 'NISWITCH_VAL_TTL3',
                'value': 114
            },
            {
                'documentation': {
                    'description': 'The switch device waits until it receives a trigger on the PXI TRIG4 line before processing the next entry in the scan list.'
                },
                'name': 'NISWITCH_VAL_TTL4',
                'value': 115
            },
            {
                'documentation': {
                    'description': 'The switch device waits until it receives a trigger on the PXI TRIG5 line before processing the next entry in the scan list.'
                },
                'name': 'NISWITCH_VAL_TTL5',
                'value': 116
            },
            {
                'documentation': {
                    'description': 'The switch device waits until it receives a trigger on the PXI TRIG6 line before processing the next entry in the scan list.'
                },
                'name': 'NISWITCH_VAL_TTL6',
                'value': 117
            },
            {
                'documentation': {
                    'description': 'The switch device waits until it receives a trigger on the PXI TRIG7 line before processing the next entry in the scan list.'
                },
                'name': 'NISWITCH_VAL_TTL7',
                'value': 118
            },
            {
                'documentation': {
                    'description': 'The switch device waits until it receives a trigger on the PXI STAR  trigger bus before processing the next entry in the scan list.'
                },
                'name': 'NISWITCH_VAL_PXI_STAR',
                'value': 125
            },
            {
                'documentation': {
                    'description': 'The switch device waits until it receives a trigger on the  rear connector.'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR',
                'value': 1000
            },
            {
                'documentation': {
                    'description': 'The switch device waits until it receives a trigger on the  front connector.'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR',
                'value': 1001
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the rear\nconnector module 1.\n'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE1',
                'value': 1021
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the rear\nconnector module 2.\n'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE2',
                'value': 1022
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the rear\nconnector module 3.\n'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE3',
                'value': 1023
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the rear\nconnector module 4.\n'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE4',
                'value': 1024
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the rear\nconnector module 5.\n'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE5',
                'value': 1025
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the rear\nconnector module 6.\n'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE6',
                'value': 1026
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the rear\nconnector module 7.\n'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE7',
                'value': 1027
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the rear\nconnector module 8.\n'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE8',
                'value': 1028
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the rear\nconnector module 9.\n'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE9',
                'value': 1029
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the rear\nconnector module 10.\n'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE10',
                'value': 1030
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the rear\nconnector module 11.\n'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE11',
                'value': 1031
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the rear\nconnector module 12.\n'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE12',
                'value': 1032
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the front\nconnector module 1.\n'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE1',
                'value': 1041
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the front\nconnector module 2.\n'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE2',
                'value': 1042
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the front\nconnector module 3.\n'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE3',
                'value': 1043
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the front\nconnector module 4.\n'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE4',
                'value': 1044
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the front\nconnector module 5.\n'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE5',
                'value': 1045
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the front\nconnector module 6.\n'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE6',
                'value': 1046
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the front\nconnector module 7.\n'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE7',
                'value': 1047
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the front\nconnector module 8.\n'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE8',
                'value': 1048
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the front\nconnector module 9.\n'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE9',
                'value': 1049
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the front\nconnector module 10.\n'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE10',
                'value': 1050
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the front\nconnector module 11.\n'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE11',
                'value': 1051
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the front\nconnector module 12.\n'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE12',
                'value': 1052
            }
        ]
    },
    'TriggerInputPolarity': {
        'values': [
            {
                'documentation': {
                    'description': 'The trigger occurs on the rising edge of the signal.'
                },
                'name': 'NISWITCH_VAL_RISING_EDGE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'The trigger occurs on the falling edge of the signal.'
                },
                'name': 'NISWITCH_VAL_FALLING_EDGE',
                'value': 1
            }
        ]
    },
    'TriggerMode': {
        'values': [
            {
                'documentation': {
                    'description': ''
                },
                'name': 'NISWITCH_VAL_SINGLE',
                'value': 0
            },
            {
                'documentation': {
                    'description': ''
                },
                'name': 'NISWITCH_VAL_MASTER',
                'value': 1
            },
            {
                'documentation': {
                    'description': ''
                },
                'name': 'NISWITCH_VAL_SLAVE',
                'value': 2
            }
        ]
    },
    'WireMode': {
        'values': [
            {
                'name': 'NISWITCH_VAL_1_WIRE',
                'value': 1
            },
            {
                'name': 'NISWITCH_VAL_2_WIRE',
                'value': 2
            },
            {
                'name': 'NISWITCH_VAL_4_WIRE',
                'value': 4
            }
        ]
    }
}
