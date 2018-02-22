# This file was generated

from enum import Enum


class HandshakingInitiation(Enum):
    MEASUREMENT_DEVICE = 0
    '''
    The `niSwitch Initiate
    Scan <switchviref.chm::/Initiate_Scan.html>`__ VI does not
    return until the switch hardware is waiting for a trigger input. This
    ensures that if you initiate the measurement device after calling the
    `niSwitch Initiate
    Scan <switchviref.chm::/Initiate_Scan.html>`__ VI , the switch
    is sure to receive the first measurement complete (MC) signal sent by
    the measurement device. The measurement device should be configured to
    first take a measurement, send MC, then wait for scanner advanced output
    signal. Thus, the first MC of the measurement device initiates
    handshaking.
    '''
    SWITCH = 1
    '''
    The `niSwitch Initiate
    Scan <switchviref.chm::/Initiate_Scan.html>`__ VI returns
    immediately after beginning scan list execution. It is assumed that the
    measurement device has already been configured and is waiting for the
    scanner advanced signal. The measurement should be configured to first
    wait for a trigger, then take a measurement. Thus, the first scanner
    advanced output signal of the switch module initiates handshaking.
    '''


class PathCapability(Enum):
    PATH_AVAILABLE = 1
    '''
    Path Available
    '''
    PATH_EXISTS = 2
    '''
    Path Exists
    '''
    PATH_UNSUPPORTED = 3
    '''
    Path Unsupported
    '''
    RESOURCE_IN_USE = 4
    '''
    Resource in use
    '''
    SOURCE_CONFLICT = 5
    '''
    Source conflict
    '''
    CHANNEL_NOT_AVAILABLE = 6
    '''
    Channel not available
    '''


class RelayAction(Enum):
    OPEN = 20
    '''
    Open Relay
    '''
    CLOSE = 21
    '''
    Close Relay
    '''


class RelayPosition(Enum):
    OPEN = 10
    '''
    Open
    '''
    CLOSED = 11
    '''
    Closed
    '''


class ScanAdvancedOutput(Enum):
    NONE = 0
    '''
    The switch device does not produce a Scan Advanced Output trigger.
    '''
    EXTERNAL = 2
    '''
    External Trigger. The switch device produces the Scan Advanced Output  trigger on the external trigger output.
    '''
    TTL0 = 111
    '''
    The switch device produces the Scan Advanced Output on the PXI TRIG0 line.
    '''
    TTL1 = 112
    '''
    The switch device produces the Scan Advanced Output on the PXI TRIG1 line.
    '''
    TTL2 = 113
    '''
    The switch device produces the Scan Advanced Output on the PXI TRIG2 line.
    '''
    TTL3 = 114
    '''
    The switch device produces the Scan Advanced Output on the PXI TRIG3 line.
    '''
    TTL4 = 115
    '''
    The switch device produces the Scan Advanced Output on the PXI TRIG4 line.
    '''
    TTL5 = 116
    '''
    The switch device produces the Scan Advanced Output on the PXI TRIG5 line.
    '''
    TTL6 = 117
    '''
    The switch device produces the Scan Advanced Output on the PXI TRIG6 line.
    '''
    TTL7 = 118
    '''
    The switch device produces the Scan Advanced Output on the PXI TRIG7 line.
    '''
    PXI_STAR = 125
    '''
    The switch module produces the Scan Advanced Output Trigger on the PXI
    Star trigger bus before processing the next entry in the scan list.
    '''
    REARCONNECTOR = 1000
    '''
    The switch device produces the Scan Advanced Output  trigger on the rear connector.
    '''
    FRONTCONNECTOR = 1001
    '''
    The switch device produces the Scan Advanced Output  trigger on the front connector.
    '''
    REARCONNECTOR_MODULE1 = 1021
    '''
    The switch module produces the Scan Advanced Output Trigger on the rear
    connector module 1.
    '''
    REARCONNECTOR_MODULE2 = 1022
    '''
    The switch module produces the Scan Advanced Output Trigger on the rear
    connector module 2.
    '''
    REARCONNECTOR_MODULE3 = 1023
    '''
    The switch module produces the Scan Advanced Output Trigger on the rear
    connector module 3.
    '''
    REARCONNECTOR_MODULE4 = 1024
    '''
    The switch module produces the Scan Advanced Output Trigger on the rear
    connector module 4.
    '''
    REARCONNECTOR_MODULE5 = 1025
    '''
    The switch module produces the Scan Advanced Output Trigger on the rear
    connector module 5.
    '''
    REARCONNECTOR_MODULE6 = 1026
    '''
    The switch module produces the Scan Advanced Output Trigger on the rear
    connector module 6.
    '''
    REARCONNECTOR_MODULE7 = 1027
    '''
    The switch module produces the Scan Advanced Output Trigger on the rear
    connector module 7.
    '''
    REARCONNECTOR_MODULE8 = 1028
    '''
    The switch module produces the Scan Advanced Output Trigger on the rear
    connector module 8.
    '''
    REARCONNECTOR_MODULE9 = 1029
    '''
    The switch module produces the Scan Advanced Ouptut Trigger on the rear
    connector module 9.
    '''
    REARCONNECTOR_MODULE10 = 1030
    '''
    The switch module produces the Scan Advanced Output Trigger on the rear
    connector module 10.
    '''
    REARCONNECTOR_MODULE11 = 1031
    '''
    The switch module produces the Scan Advanced Output Trigger on the rear
    connector module 11.
    '''
    REARCONNECTOR_MODULE12 = 1032
    '''
    The switch module produces the Scan Advanced Output Trigger on the rear
    connector module 12.
    '''
    FRONTCONNECTOR_MODULE1 = 1041
    '''
    The switch module produces the Scan Advanced Output Trigger on the front
    connector module 1.
    '''
    FRONTCONNECTOR_MODULE2 = 1042
    '''
    The switch module produces the Scan Advanced Output Trigger on the front
    connector module 2.
    '''
    FRONTCONNECTOR_MODULE3 = 1043
    '''
    The switch module produces the Scan Advanced Output Trigger on the front
    connector module 3.
    '''
    FRONTCONNECTOR_MODULE4 = 1044
    '''
    The switch module produces the Scan Advanced Output Trigger on the front
    connector module 4.
    '''
    FRONTCONNECTOR_MODULE5 = 1045
    '''
    The switch module produces the Scan Advanced Output Trigger on the front
    connector module 5.
    '''
    FRONTCONNECTOR_MODULE6 = 1046
    '''
    The switch module produces the Scan Advanced Output Trigger on the front
    connector module 6.
    '''
    FRONTCONNECTOR_MODULE7 = 1047
    '''
    The switch module produces the Scan Advanced Output Trigger on the front
    connector module 7.
    '''
    FRONTCONNECTOR_MODULE8 = 1048
    '''
    The switch module produces the Scan Advanced Output Trigger on the front
    connector module 8.
    '''
    FRONTCONNECTOR_MODULE9 = 1049
    '''
    The switch module produces the Scan Advanced Output Trigger on the front
    connector module 9.
    '''
    FRONTCONNECTOR_MODULE10 = 1050
    '''
    The switch module produces the Scan Advanced Output Trigger on the front
    connector module 10.
    '''
    FRONTCONNECTOR_MODULE11 = 1051
    '''
    The switch module produces the Scan Advanced Output Trigger on the front
    connector module 11.
    '''
    FRONTCONNECTOR_MODULE12 = 1052
    '''
    The switch module produces the Scan Advanced Output Trigger on the front
    connector module 12.
    '''


class ScanAdvancedPolarity(Enum):
    RISING = 0
    '''
    The trigger occurs on the rising edge of the signal.
    '''
    FALLING = 1
    '''
    The trigger occurs on the falling edge of the signal.
    '''


class ScanMode(Enum):
    NONE = 0
    '''
    No implicit action on connections when scanning.
    '''
    BREAK_BEFORE_MAKE = 1
    '''
    When scanning, the switch device breaks existing connections before  making new connections.
    '''
    BREAK_AFTER_MAKE = 2
    '''
    When scanning, the switch device breaks existing connections after making  new connections.
    '''


class TriggerInput(Enum):
    IMMEDIATE = 1
    '''
    Immediate Trigger. The switch device does not wait for a trigger before  processing the next entry in the scan list.
    '''
    EXTERNAL = 2
    '''
    External Trigger. The switch device waits until it receives a trigger  from an external source through the external trigger input before  processing the next entry in the scan list.
    '''
    SOFTWARE_TRIG = 3
    '''
    The switch device waits until you call the send_software_trigger  method before processing the next entry in the scan list.
    '''
    TTL0 = 111
    '''
    The switch device waits until it receives a trigger on the PXI TRIG0 line before processing the next entry in the scan list.
    '''
    TTL1 = 112
    '''
    The switch device waits until it receives a trigger on the PXI TRIG1 line before processing the next entry in the scan list.
    '''
    TTL2 = 113
    '''
    The switch device waits until it receives a trigger on the PXI TRIG2 line before processing the next entry in the scan list.
    '''
    TTL3 = 114
    '''
    The switch device waits until it receives a trigger on the PXI TRIG3 line before processing the next entry in the scan list.
    '''
    TTL4 = 115
    '''
    The switch device waits until it receives a trigger on the PXI TRIG4 line before processing the next entry in the scan list.
    '''
    TTL5 = 116
    '''
    The switch device waits until it receives a trigger on the PXI TRIG5 line before processing the next entry in the scan list.
    '''
    TTL6 = 117
    '''
    The switch device waits until it receives a trigger on the PXI TRIG6 line before processing the next entry in the scan list.
    '''
    TTL7 = 118
    '''
    The switch device waits until it receives a trigger on the PXI TRIG7 line before processing the next entry in the scan list.
    '''
    PXI_STAR = 125
    '''
    The switch device waits until it receives a trigger on the PXI STAR  trigger bus before processing the next entry in the scan list.
    '''
    REARCONNECTOR = 1000
    '''
    The switch device waits until it receives a trigger on the  rear connector.
    '''
    FRONTCONNECTOR = 1001
    '''
    The switch device waits until it receives a trigger on the  front connector.
    '''
    REARCONNECTOR_MODULE1 = 1021
    '''
    The switch module waits until it receives a trigger on the rear
    connector module 1.
    '''
    REARCONNECTOR_MODULE2 = 1022
    '''
    The switch module waits until it receives a trigger on the rear
    connector module 2.
    '''
    REARCONNECTOR_MODULE3 = 1023
    '''
    The switch module waits until it receives a trigger on the rear
    connector module 3.
    '''
    REARCONNECTOR_MODULE4 = 1024
    '''
    The switch module waits until it receives a trigger on the rear
    connector module 4.
    '''
    REARCONNECTOR_MODULE5 = 1025
    '''
    The switch module waits until it receives a trigger on the rear
    connector module 5.
    '''
    REARCONNECTOR_MODULE6 = 1026
    '''
    The switch module waits until it receives a trigger on the rear
    connector module 6.
    '''
    REARCONNECTOR_MODULE7 = 1027
    '''
    The switch module waits until it receives a trigger on the rear
    connector module 7.
    '''
    REARCONNECTOR_MODULE8 = 1028
    '''
    The switch module waits until it receives a trigger on the rear
    connector module 8.
    '''
    REARCONNECTOR_MODULE9 = 1029
    '''
    The switch module waits until it receives a trigger on the rear
    connector module 9.
    '''
    REARCONNECTOR_MODULE10 = 1030
    '''
    The switch module waits until it receives a trigger on the rear
    connector module 10.
    '''
    REARCONNECTOR_MODULE11 = 1031
    '''
    The switch module waits until it receives a trigger on the rear
    connector module 11.
    '''
    REARCONNECTOR_MODULE12 = 1032
    '''
    The switch module waits until it receives a trigger on the rear
    connector module 12.
    '''
    FRONTCONNECTOR_MODULE1 = 1041
    '''
    The switch module waits until it receives a trigger on the front
    connector module 1.
    '''
    FRONTCONNECTOR_MODULE2 = 1042
    '''
    The switch module waits until it receives a trigger on the front
    connector module 2.
    '''
    FRONTCONNECTOR_MODULE3 = 1043
    '''
    The switch module waits until it receives a trigger on the front
    connector module 3.
    '''
    FRONTCONNECTOR_MODULE4 = 1044
    '''
    The switch module waits until it receives a trigger on the front
    connector module 4.
    '''
    FRONTCONNECTOR_MODULE5 = 1045
    '''
    The switch module waits until it receives a trigger on the front
    connector module 5.
    '''
    FRONTCONNECTOR_MODULE6 = 1046
    '''
    The switch module waits until it receives a trigger on the front
    connector module 6.
    '''
    FRONTCONNECTOR_MODULE7 = 1047
    '''
    The switch module waits until it receives a trigger on the front
    connector module 7.
    '''
    FRONTCONNECTOR_MODULE8 = 1048
    '''
    The switch module waits until it receives a trigger on the front
    connector module 8.
    '''
    FRONTCONNECTOR_MODULE9 = 1049
    '''
    The switch module waits until it receives a trigger on the front
    connector module 9.
    '''
    FRONTCONNECTOR_MODULE10 = 1050
    '''
    The switch module waits until it receives a trigger on the front
    connector module 10.
    '''
    FRONTCONNECTOR_MODULE11 = 1051
    '''
    The switch module waits until it receives a trigger on the front
    connector module 11.
    '''
    FRONTCONNECTOR_MODULE12 = 1052
    '''
    The switch module waits until it receives a trigger on the front
    connector module 12.
    '''


class TriggerInputPolarity(Enum):
    RISING = 0
    '''
    The trigger occurs on the rising edge of the signal.
    '''
    FALLING = 1
    '''
    The trigger occurs on the falling edge of the signal.
    '''
