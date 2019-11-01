# -*- coding: utf-8 -*-
# This file is generated from NI-Sync API metadata version 20.0.0d0
enums = {
    '1588ClockState': {
        'python_name': '1588ClockState',
        'values': [
            {
                'documentation': {
                    'description': 'Not Defined'
                },
                'name': 'NISYNC_VAL_1588_CLK_STATE_NOT_DEFINED',
                'python_name': 'NISYNC_VAL_1588_CLK_STATE_NOT_DEFINED',
                'value': -1
            },
            {
                'documentation': {
                    'description': 'Initializing'
                },
                'name': 'NISYNC_VAL_1588_CLK_STATE_INIT',
                'python_name': 'NISYNC_VAL_1588_CLK_STATE_INIT',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Faulty'
                },
                'name': 'NISYNC_VAL_1588_CLK_STATE_FAULT',
                'python_name': 'NISYNC_VAL_1588_CLK_STATE_FAULT',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Disabled'
                },
                'name': 'NISYNC_VAL_1588_CLK_STATE_DISABLE',
                'python_name': 'NISYNC_VAL_1588_CLK_STATE_DISABLE',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Listening'
                },
                'name': 'NISYNC_VAL_1588_CLK_STATE_LISTENING',
                'python_name': 'NISYNC_VAL_1588_CLK_STATE_LISTENING',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'PreMaster'
                },
                'name': 'NISYNC_VAL_1588_CLK_STATE_PREMASTER',
                'python_name': 'NISYNC_VAL_1588_CLK_STATE_PREMASTER',
                'value': 4
            },
            {
                'documentation': {
                    'description': 'Master'
                },
                'name': 'NISYNC_VAL_1588_CLK_STATE_MASTER',
                'python_name': 'NISYNC_VAL_1588_CLK_STATE_MASTER',
                'value': 5
            },
            {
                'documentation': {
                    'description': 'Passive'
                },
                'name': 'NISYNC_VAL_1588_CLK_STATE_PASSIVE',
                'python_name': 'NISYNC_VAL_1588_CLK_STATE_PASSIVE',
                'value': 6
            },
            {
                'documentation': {
                    'description': 'Uncalibrated'
                },
                'name': 'NISYNC_VAL_1588_CLK_STATE_UNCALIBRATED',
                'python_name': 'NISYNC_VAL_1588_CLK_STATE_UNCALIBRATED',
                'value': 7
            },
            {
                'documentation': {
                    'description': 'Slave'
                },
                'name': 'NISYNC_VAL_1588_CLK_STATE_SLAVE',
                'python_name': 'NISYNC_VAL_1588_CLK_STATE_SLAVE',
                'value': 8
            },
            {
                'documentation': {
                    'description': 'Stopped'
                },
                'name': 'NISYNC_VAL_1588_CLK_STATE_STOPPED',
                'python_name': 'NISYNC_VAL_1588_CLK_STATE_STOPPED',
                'value': 9
            }
        ]
    },
    '8021AsClockAccuracy': {
        'python_name': '8021AsClockAccuracy',
        'values': [
            {
                'documentation': {
                    'description': 'Within25nsec'
                },
                'name': 'NISYNC_VAL_8021AS_CLK_ACCURACY_WITHIN_25_NSEC',
                'python_name': 'NISYNC_VAL_8021AS_CLK_ACCURACY_WITHIN_25_NSEC',
                'value': 32
            },
            {
                'documentation': {
                    'description': 'Within100nsec'
                },
                'name': 'NISYNC_VAL_8021AS_CLK_ACCURACY_WITHIN_100_NSEC',
                'python_name': 'NISYNC_VAL_8021AS_CLK_ACCURACY_WITHIN_100_NSEC',
                'value': 33
            },
            {
                'documentation': {
                    'description': 'Within250nsec'
                },
                'name': 'NISYNC_VAL_8021AS_CLK_ACCURACY_WITHIN_250_NSEC',
                'python_name': 'NISYNC_VAL_8021AS_CLK_ACCURACY_WITHIN_250_NSEC',
                'value': 34
            },
            {
                'documentation': {
                    'description': 'Within1usec'
                },
                'name': 'NISYNC_VAL_8021AS_CLK_ACCURACY_WITHIN_1_USEC',
                'python_name': 'NISYNC_VAL_8021AS_CLK_ACCURACY_WITHIN_1_USEC',
                'value': 35
            },
            {
                'documentation': {
                    'description': 'Within2500nsec'
                },
                'name': 'NISYNC_VAL_8021AS_CLK_ACCURACY_WITHIN_2500_NSEC',
                'python_name': 'NISYNC_VAL_8021AS_CLK_ACCURACY_WITHIN_2500_NSEC',
                'value': 36
            },
            {
                'documentation': {
                    'description': 'Within10usec'
                },
                'name': 'NISYNC_VAL_8021AS_CLK_ACCURACY_WITHIN_10_USEC',
                'python_name': 'NISYNC_VAL_8021AS_CLK_ACCURACY_WITHIN_10_USEC',
                'value': 37
            },
            {
                'documentation': {
                    'description': 'Within25usec'
                },
                'name': 'NISYNC_VAL_8021AS_CLK_ACCURACY_WITHIN_25_USEC',
                'python_name': 'NISYNC_VAL_8021AS_CLK_ACCURACY_WITHIN_25_USEC',
                'value': 38
            },
            {
                'documentation': {
                    'description': 'Within100usec'
                },
                'name': 'NISYNC_VAL_8021AS_CLK_ACCURACY_WITHIN_100_USEC',
                'python_name': 'NISYNC_VAL_8021AS_CLK_ACCURACY_WITHIN_100_USEC',
                'value': 39
            },
            {
                'documentation': {
                    'description': 'Within250usec'
                },
                'name': 'NISYNC_VAL_8021AS_CLK_ACCURACY_WITHIN_250_USEC',
                'python_name': 'NISYNC_VAL_8021AS_CLK_ACCURACY_WITHIN_250_USEC',
                'value': 40
            },
            {
                'documentation': {
                    'description': 'Within1msec'
                },
                'name': 'NISYNC_VAL_8021AS_CLK_ACCURACY_WITHIN_1_MSEC',
                'python_name': 'NISYNC_VAL_8021AS_CLK_ACCURACY_WITHIN_1_MSEC',
                'value': 41
            },
            {
                'documentation': {
                    'description': 'Within2500usec'
                },
                'name': 'NISYNC_VAL_8021AS_CLK_ACCURACY_WITHIN_2500_USEC',
                'python_name': 'NISYNC_VAL_8021AS_CLK_ACCURACY_WITHIN_2500_USEC',
                'value': 42
            },
            {
                'documentation': {
                    'description': 'Within10msec'
                },
                'name': 'NISYNC_VAL_8021AS_CLK_ACCURACY_WITHIN_10_MSEC',
                'python_name': 'NISYNC_VAL_8021AS_CLK_ACCURACY_WITHIN_10_MSEC',
                'value': 43
            },
            {
                'documentation': {
                    'description': 'Within25msec'
                },
                'name': 'NISYNC_VAL_8021AS_CLK_ACCURACY_WITHIN_25_MSEC',
                'python_name': 'NISYNC_VAL_8021AS_CLK_ACCURACY_WITHIN_25_MSEC',
                'value': 44
            },
            {
                'documentation': {
                    'description': 'Within100msec'
                },
                'name': 'NISYNC_VAL_8021AS_CLK_ACCURACY_WITHIN_100_MSEC',
                'python_name': 'NISYNC_VAL_8021AS_CLK_ACCURACY_WITHIN_100_MSEC',
                'value': 45
            },
            {
                'documentation': {
                    'description': 'Within250msec'
                },
                'name': 'NISYNC_VAL_8021AS_CLK_ACCURACY_WITHIN_250_MSEC',
                'python_name': 'NISYNC_VAL_8021AS_CLK_ACCURACY_WITHIN_250_MSEC',
                'value': 46
            },
            {
                'documentation': {
                    'description': 'Within1sec'
                },
                'name': 'NISYNC_VAL_8021AS_CLK_ACCURACY_WITHIN_1_SEC',
                'python_name': 'NISYNC_VAL_8021AS_CLK_ACCURACY_WITHIN_1_SEC',
                'value': 47
            },
            {
                'documentation': {
                    'description': 'Within10sec'
                },
                'name': 'NISYNC_VAL_8021AS_CLK_ACCURACY_WITHIN_10_SEC',
                'python_name': 'NISYNC_VAL_8021AS_CLK_ACCURACY_WITHIN_10_SEC',
                'value': 48
            },
            {
                'documentation': {
                    'description': 'GreaterThan10sec'
                },
                'name': 'NISYNC_VAL_8021AS_CLK_ACCURACY_GREATER_THAN_10_SEC',
                'python_name': 'NISYNC_VAL_8021AS_CLK_ACCURACY_GREATER_THAN_10_SEC',
                'value': 49
            },
            {
                'documentation': {
                    'description': 'Unknown'
                },
                'name': 'NISYNC_VAL_8021AS_CLK_ACCURACY_UNKNOWN',
                'python_name': 'NISYNC_VAL_8021AS_CLK_ACCURACY_UNKNOWN',
                'value': 254
            }
        ]
    },
    '8021AsSyncInterval': {
        'python_name': '8021AsSyncInterval',
        'values': [
            {
                'documentation': {
                    'description': '125 Milliseconds'
                },
                'name': 'NISYNC_VAL_SYNC_INTERVAL_125_MSEC',
                'python_name': 'NISYNC_VAL_SYNC_INTERVAL_125_MSEC',
                'value': -3
            },
            {
                'documentation': {
                    'description': '250 Milliseconds'
                },
                'name': 'NISYNC_VAL_SYNC_INTERVAL_250_MSEC',
                'python_name': 'NISYNC_VAL_SYNC_INTERVAL_250_MSEC',
                'value': -2
            },
            {
                'documentation': {
                    'description': '0.5 Seconds'
                },
                'name': 'NISYNC_VAL_SYNC_INTERVAL_HALF_SEC',
                'python_name': 'NISYNC_VAL_SYNC_INTERVAL_HALF_SEC',
                'value': -1
            },
            {
                'documentation': {
                    'description': '1 Second'
                },
                'name': 'NISYNC_VAL_SYNC_INTERVAL_ONE_SEC',
                'python_name': 'NISYNC_VAL_SYNC_INTERVAL_ONE_SEC',
                'value': 0
            },
            {
                'documentation': {
                    'description': '2 Seconds'
                },
                'name': 'NISYNC_VAL_SYNC_INTERVAL_TWO_SEC',
                'python_name': 'NISYNC_VAL_SYNC_INTERVAL_TWO_SEC',
                'value': 1
            }
        ]
    },
    'AnnounceInterval': {
        'python_name': 'AnnounceInterval',
        'values': [
            {
                'documentation': {
                    'description': '0.5 Seconds'
                },
                'name': 'NISYNC_VAL_SYNC_INTERVAL_HALF_SEC',
                'python_name': 'NISYNC_VAL_SYNC_INTERVAL_HALF_SEC',
                'value': -1
            },
            {
                'documentation': {
                    'description': '1 Second'
                },
                'name': 'NISYNC_VAL_SYNC_INTERVAL_ONE_SEC',
                'python_name': 'NISYNC_VAL_SYNC_INTERVAL_ONE_SEC',
                'value': 0
            },
            {
                'documentation': {
                    'description': '2 Seconds'
                },
                'name': 'NISYNC_VAL_SYNC_INTERVAL_TWO_SEC',
                'python_name': 'NISYNC_VAL_SYNC_INTERVAL_TWO_SEC',
                'value': 1
            }
        ]
    },
    'BmcaMode': {
        'python_name': 'BmcaMode',
        'values': [
            {
                'documentation': {
                    'description': 'SlaveOnly'
                },
                'name': 'NISYNC_VAL_BMCA_MODE_SLAVE_ONLY',
                'python_name': 'NISYNC_VAL_BMCA_MODE_SLAVE_ONLY',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'MasterSlave'
                },
                'name': 'NISYNC_VAL_BMCA_MODE_MASTER_SLAVE',
                'python_name': 'NISYNC_VAL_BMCA_MODE_MASTER_SLAVE',
                'value': 1
            }
        ]
    },
    'ClockAccuracy': {
        'python_name': 'ClockAccuracy',
        'values': [
            {
                'documentation': {
                    'description': 'Unknown'
                },
                'name': 'NISYNC_VAL_1588_CLK_ACCURACY_UNKNOWN',
                'python_name': 'NISYNC_VAL_1588_CLK_ACCURACY_UNKNOWN',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Within25nsec'
                },
                'name': 'NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_25_NSEC',
                'python_name': 'NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_25_NSEC',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Within100nsec'
                },
                'name': 'NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_100_NSEC',
                'python_name': 'NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_100_NSEC',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Within250nsec'
                },
                'name': 'NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_250_NSEC',
                'python_name': 'NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_250_NSEC',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'Within1usec'
                },
                'name': 'NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_1_USEC',
                'python_name': 'NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_1_USEC',
                'value': 4
            },
            {
                'documentation': {
                    'description': 'Within2500nsec'
                },
                'name': 'NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_2500_NSEC',
                'python_name': 'NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_2500_NSEC',
                'value': 5
            },
            {
                'documentation': {
                    'description': 'Within10usec'
                },
                'name': 'NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_10_USEC',
                'python_name': 'NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_10_USEC',
                'value': 6
            },
            {
                'documentation': {
                    'description': 'Within25usec'
                },
                'name': 'NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_25_USEC',
                'python_name': 'NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_25_USEC',
                'value': 7
            },
            {
                'documentation': {
                    'description': 'Within100usec'
                },
                'name': 'NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_100_USEC',
                'python_name': 'NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_100_USEC',
                'value': 8
            },
            {
                'documentation': {
                    'description': 'Within250usec'
                },
                'name': 'NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_250_USEC',
                'python_name': 'NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_250_USEC',
                'value': 9
            },
            {
                'documentation': {
                    'description': 'Within1msec'
                },
                'name': 'NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_1_MSEC',
                'python_name': 'NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_1_MSEC',
                'value': 10
            },
            {
                'documentation': {
                    'description': 'Within2500usec'
                },
                'name': 'NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_2500_USEC',
                'python_name': 'NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_2500_USEC',
                'value': 11
            },
            {
                'documentation': {
                    'description': 'Within10msec'
                },
                'name': 'NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_10_MSEC',
                'python_name': 'NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_10_MSEC',
                'value': 12
            },
            {
                'documentation': {
                    'description': 'Within25msec'
                },
                'name': 'NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_25_MSEC',
                'python_name': 'NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_25_MSEC',
                'value': 13
            },
            {
                'documentation': {
                    'description': 'Within100msec'
                },
                'name': 'NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_100_MSEC',
                'python_name': 'NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_100_MSEC',
                'value': 14
            },
            {
                'documentation': {
                    'description': 'Within250msec'
                },
                'name': 'NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_250_MSEC',
                'python_name': 'NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_250_MSEC',
                'value': 15
            },
            {
                'documentation': {
                    'description': 'Within1sec'
                },
                'name': 'NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_1_SEC',
                'python_name': 'NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_1_SEC',
                'value': 16
            },
            {
                'documentation': {
                    'description': 'Within10sec'
                },
                'name': 'NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_10_SEC',
                'python_name': 'NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_10_SEC',
                'value': 17
            },
            {
                'documentation': {
                    'description': 'GreaterThan10sec'
                },
                'name': 'NISYNC_VAL_1588_CLK_ACCURACY_GREATER_THAN_10_SEC',
                'python_name': 'NISYNC_VAL_1588_CLK_ACCURACY_GREATER_THAN_10_SEC',
                'value': 18
            }
        ]
    },
    'GpsStatus': {
        'python_name': 'GpsStatus',
        'values': [
            {
                'documentation': {
                    'description': 'Uninitialized'
                },
                'name': 'NISYNC_VAL_GPS_UNINITIALIZED',
                'python_name': 'NISYNC_VAL_GPS_UNINITIALIZED',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Antenna Error'
                },
                'name': 'NISYNC_VAL_GPS_ANTENNA_ERROR',
                'python_name': 'NISYNC_VAL_GPS_ANTENNA_ERROR',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'No Useable Satellites'
                },
                'name': 'NISYNC_VAL_GPS_NO_USEABLE_SATELLITE',
                'python_name': 'NISYNC_VAL_GPS_NO_USEABLE_SATELLITE',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'One Useable Satellite'
                },
                'name': 'NISYNC_VAL_GPS_ONE_USEABLE_SATELLITE',
                'python_name': 'NISYNC_VAL_GPS_ONE_USEABLE_SATELLITE',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'Two Useable Satellites'
                },
                'name': 'NISYNC_VAL_GPS_TWO_USEABLE_SATELLITES',
                'python_name': 'NISYNC_VAL_GPS_TWO_USEABLE_SATELLITES',
                'value': 4
            },
            {
                'documentation': {
                    'description': 'Three Useable Satellites'
                },
                'name': 'NISYNC_VAL_GPS_THREE_USEABLE_SATELLITES',
                'python_name': 'NISYNC_VAL_GPS_THREE_USEABLE_SATELLITES',
                'value': 5
            },
            {
                'documentation': {
                    'description': 'No GPS Time'
                },
                'name': 'NISYNC_VAL_GPS_NO_GPS_TIME',
                'python_name': 'NISYNC_VAL_GPS_NO_GPS_TIME',
                'value': 6
            },
            {
                'documentation': {
                    'description': 'PDOP Too High'
                },
                'name': 'NISYNC_VAL_GPS_PDOP_TOO_HIGH',
                'python_name': 'NISYNC_VAL_GPS_PDOP_TOO_HIGH',
                'value': 7
            },
            {
                'documentation': {
                    'description': 'Unuseable Satellite'
                },
                'name': 'NISYNC_VAL_GPS_UNUSEABLE_SATELLITE',
                'python_name': 'NISYNC_VAL_GPS_UNUSEABLE_SATELLITE',
                'value': 8
            },
            {
                'documentation': {
                    'description': 'Fix Rejected'
                },
                'name': 'NISYNC_VAL_GPS_FIX_REJECTED',
                'python_name': 'NISYNC_VAL_GPS_FIX_REJECTED',
                'value': 9
            },
            {
                'documentation': {
                    'description': 'Self Survey Complete'
                },
                'name': 'NISYNC_VAL_GPS_SELF_SURVEY_COMPLETE',
                'python_name': 'NISYNC_VAL_GPS_SELF_SURVEY_COMPLETE',
                'value': 10
            },
            {
                'documentation': {
                    'description': 'Self Survey Not Complete'
                },
                'name': 'NISYNC_VAL_GPS_SELF_SURVEY_NOT_COMPLETE',
                'python_name': 'NISYNC_VAL_GPS_SELF_SURVEY_NOT_COMPLETE',
                'value': 11
            }
        ]
    },
    'PortState': {
        'python_name': 'PortState',
        'values': [
            {
                'documentation': {
                    'description': 'Disabled'
                },
                'name': 'NISYNC_VAL_8021AS_PORT_STATE_DISABLED',
                'python_name': 'NISYNC_VAL_8021AS_PORT_STATE_DISABLED',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'Master'
                },
                'name': 'NISYNC_VAL_8021AS_PORT_STATE_MASTER',
                'python_name': 'NISYNC_VAL_8021AS_PORT_STATE_MASTER',
                'value': 6
            },
            {
                'documentation': {
                    'description': 'Passive'
                },
                'name': 'NISYNC_VAL_8021AS_PORT_STATE_PASSIVE',
                'python_name': 'NISYNC_VAL_8021AS_PORT_STATE_PASSIVE',
                'value': 7
            },
            {
                'documentation': {
                    'description': 'Slave'
                },
                'name': 'NISYNC_VAL_8021AS_PORT_STATE_SLAVE',
                'python_name': 'NISYNC_VAL_8021AS_PORT_STATE_SLAVE',
                'value': 9
            }
        ]
    },
    'SyncInterval': {
        'python_name': 'SyncInterval',
        'values': [
            {
                'documentation': {
                    'description': '0.5 Seconds'
                },
                'name': 'NISYNC_VAL_SYNC_INTERVAL_HALF_SEC',
                'python_name': 'NISYNC_VAL_SYNC_INTERVAL_HALF_SEC',
                'value': -1
            },
            {
                'documentation': {
                    'description': '1 Second'
                },
                'name': 'NISYNC_VAL_SYNC_INTERVAL_ONE_SEC',
                'python_name': 'NISYNC_VAL_SYNC_INTERVAL_ONE_SEC',
                'value': 0
            },
            {
                'documentation': {
                    'description': '2 Seconds'
                },
                'name': 'NISYNC_VAL_SYNC_INTERVAL_TWO_SEC',
                'python_name': 'NISYNC_VAL_SYNC_INTERVAL_TWO_SEC',
                'value': 1
            }
        ]
    }
}
