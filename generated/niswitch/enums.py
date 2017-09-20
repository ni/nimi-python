# This file was generated

from enum import Enum


class CabledModuleScanAdvancedBus(Enum):
    NONE = 0
    PXI_TRIG0 = 111
    '''
    The switch module waits until it receives a trigger on the PXI_Trig0
    line before processing the next entry in the scan list.
    '''
    PXI_TRIG1 = 112
    '''
    The switch module waits until it receives a trigger on the PXI_Trig1
    line before processing the next entry in the scan list.
    '''
    PXI_TRIG2 = 113
    '''
    The switch module waits until it receives a trigger on the PXI_Trig2
    line before processing the next entry in the scan list.
    '''
    PXI_TRIG3 = 114
    '''
    The switch module waits until it receives a trigger on the PXI_Trig3
    line before processing the next entry in the scan list.
    '''
    PXI_TRIG4 = 115
    '''
    The switch module waits until it receives a trigger on the PXI_Trig4
    line before processing the next entry in the scan list.
    '''
    PXI_TRIG5 = 116
    '''
    The switch module waits until it receives a trigger on the PXI_Trig5
    line before processing the next entry in the scan list.
    '''
    PXI_TRIG6 = 117
    '''
    The switch module waits until it receives a trigger on the PXI_Trig6
    line before processing the next entry in the scan list.
    '''
    PXI_TRIG7 = 118
    '''
    The switch module waits until it receives a trigger on the PXI_Trig7
    line before processing the next entry in the scan list.
    '''


class CabledModuleTriggerBus(Enum):
    NONE = 0
    PXI_TRIG0 = 111
    PXI_TRIG1 = 112
    PXI_TRIG2 = 113
    PXI_TRIG3 = 114
    PXI_TRIG4 = 115
    PXI_TRIG5 = 116
    PXI_TRIG6 = 117
    PXI_TRIG7 = 118


class HandshakingInitiation(Enum):
    MEASUREMENT_DEVICE_INITIATED = 0
    '''
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
    '''
    SWITCH_INITIATED = 1
    '''
    The `niSwitch Initiate
    Scan <switchviref.chm::/niSwitch_Initiate_Scan.html>`__ VI returns
    immediately after beginning scan list execution. It is assumed that the
    measurement device has already been configured and is waiting for the
    scanner advanced signal. The measurement should be configured to first
    wait for a trigger, then take a measurement. Thus, the first scanner
    advanced output signal of the switch module initiates handshaking.
    '''


class MasterSlaveScanAdvancedBus(Enum):
    NONE = 0
    PXI_TRIG0 = 111
    '''
    The switch module waits until it receives a trigger on the PXI_Trig0
    line before processing the next entry in the scan list.
    '''
    PXI_TRIG1 = 112
    '''
    The switch module waits until it receives a trigger on the PXI_Trig1
    line before processing the next entry in the scan list.
    '''
    PXI_TRIG2 = 113
    '''
    The switch module waits until it receives a trigger on the PXI_Trig2
    line before processing the next entry in the scan list.
    '''
    PXI_TRIG3 = 114
    '''
    The switch module waits until it receives a trigger on the PXI_Trig3
    line before processing the next entry in the scan list.
    '''
    PXI_TRIG4 = 115
    '''
    The switch module waits until it receives a trigger on the PXI_Trig4
    line before processing the next entry in the scan list.
    '''
    PXI_TRIG5 = 116
    '''
    The switch module waits until it receives a trigger on the PXI_Trig5
    line before processing the next entry in the scan list.
    '''
    PXI_TRIG6 = 117
    '''
    The switch module waits until it receives a trigger on the PXI_Trig6
    line before processing the next entry in the scan list.
    '''
    PXI_TRIG7 = 118
    '''
    The switch module waits until it receives a trigger on the PXI_Trig7
    line before processing the next entry in the scan list.
    '''


class MasterSlaveTriggerBus(Enum):
    NONE = 0
    PXI_TRIG0 = 111
    '''
    The switch module waits until it receives a trigger on the PXI_Trig0
    line before processing the next entry in the scan list.
    '''
    PXI_TRIG1 = 112
    '''
    The switch module waits until it receives a trigger on the PXI_Trig1
    line before processing the next entry in the scan list.
    '''
    PXI_TRIG2 = 113
    '''
    The switch module waits until it receives a trigger on the PXI_Trig2
    line before processing the next entry in the scan list.
    '''
    PXI_TRIG3 = 114
    '''
    The switch module waits until it receives a trigger on the PXI_Trig3
    line before processing the next entry in the scan list.
    '''
    PXI_TRIG4 = 115
    '''
    The switch module waits until it receives a trigger on the PXI_Trig4
    line before processing the next entry in the scan list.
    '''
    PXI_TRIG5 = 116
    '''
    The switch module waits until it receives a trigger on the PXI_Trig5
    line before processing the next entry in the scan list.
    '''
    PXI_TRIG6 = 117
    '''
    The switch module waits until it receives a trigger on the PXI_Trig6
    line before processing the next entry in the scan list.
    '''
    PXI_TRIG7 = 118
    '''
    The switch module waits until it receives a trigger on the PXI_Trig7
    line before processing the next entry in the scan list.
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
    OPEN_RELAY = 20
    '''
    Open Relay
    '''
    CLOSE_RELAY = 21
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
    The switch module does not produce a Scan Advanced Output trigger.
    '''
    EXTERNAL = 2
    '''
    The switch module produces the Scan Advanced Output trigger on the
    external trigger output.
    '''
    PXI_TRIG0 = 111
    '''
    The switch module produces the Scan Advanced Output Trigger on the
    PXI_Trig0 line before processing the next entry in the scan list.
    '''
    PXI_TRIG1 = 112
    '''
    The switch module produces the Scan Advanced Output Trigger on the
    PXI_Trig1 line before processing the next entry in the scan list.
    '''
    PXI_TRIG2 = 113
    '''
    The switch module produces the Scan Advanced Output Trigger on the
    PXI_Trig2 line before processing the next entry in the scan list.
    '''
    PXI_TRIG3 = 114
    '''
    The switch module produces the Scan Advanced Output Trigger on the
    PXI_Trig3 line before processing the next entry in the scan list.
    '''
    PXI_TRIG4 = 115
    '''
    The switch module produces the Scan Advanced Output Trigger on the
    PXI_Trig4 line before processing the next entry in the scan list.
    '''
    PXI_TRIG5 = 116
    '''
    The switch module produces the Scan Advanced Output Trigger on the
    PXI_Trig5 line before processing the next entry in the scan list.
    '''
    PXI_TRIG6 = 117
    '''
    The switch module produces the Scan Advanced Output Trigger on the
    PXI_Trig6 line before processing the next entry in the scan list.
    '''
    PXI_TRIG7 = 118
    '''
    The switch module produces the Scan Advanced Output Trigger on the
    PXI_Trig7 line before processing the next entry in the scan list.
    '''
    PXI_STAR = 125
    '''
    The switch module produces the Scan Advanced Output Trigger on the PXI
    Star trigger bus before processing the next entry in the scan list.
    '''
    REARCONNECTOR = 1000
    '''
    The switch module produces the Scan Advanced Output Trigger on the rear
    connector.
    '''
    FRONTCONNECTOR = 1001
    '''
    The switch module produces the Scan Advanced Output Trigger on the front
    connector.
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
    RISING_EDGE = 0
    '''
    The trigger occurs on the rising edge of the signal.
    '''
    FALLING_EDGE = 1
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
    When scanning, the switch module breaks existing connections before
    making new connections.
    '''
    BREAK_AFTER_MAKE = 2
    '''
    When scanning, the switch module breaks existing connections after
    making new connections.
    '''


class TriggerInput(Enum):
    IMMEDIATE = 1
    '''
    The switch module does not wait for a trigger before processing the next
    entry in the scan list.
    '''
    EXTERNAL = 2
    '''
    The switch module waits until it receives a trigger from an external
    source through the external trigger input before processing the next
    entry in the scan list.
    '''
    SW_TRIG_FUNC = 3
    '''
    The switch module waits until you call the `niSwitch Send Software
    Trigger <switchviref.chm::/niSwitch_Send_Software_Trigger.html>`__ VI
    before processing the next entry in the scan list.
    '''
    PXI_TRIG0 = 111
    '''
    The switch module waits until it receives a trigger on the PXI_Trig0
    line before processing the next entry in the scan list.
    '''
    PXI_TRIG1 = 112
    '''
    The switch module waits until it receives a trigger on the PXI_Trig1
    line before processing the next entry in the scan list.
    '''
    PXI_TRIG2 = 113
    '''
    The switch module waits until it receives a trigger on the PXI_Trig2
    line before processing the next entry in the scan list.
    '''
    PXI_TRIG3 = 114
    '''
    The switch module waits until it receives a trigger on the PXI_Trig3
    line before processing the next entry in the scan list.
    '''
    PXI_TRIG4 = 115
    '''
    The switch module waits until it receives a trigger on the PXI_Trig4
    line before processing the next entry in the scan list.
    '''
    PXI_TRIG5 = 116
    '''
    The switch module waits until it receives a trigger on the PXI_Trig5
    line before processing the next entry in the scan list.
    '''
    PXI_TRIG6 = 117
    '''
    The switch module waits until it receives a trigger on the PXI_Trig6
    line before processing the next entry in the scan list.
    '''
    PXI_TRIG7 = 118
    '''
    The switch module waits until it receives a trigger on the PXI_Trig7
    line before processing the next entry in the scan list.
    '''
    PXI_STAR = 125
    '''
    The switch module waits until it receives a trigger on the PXI star
    trigger bus before processing the next entry in the scan list.
    '''
    REARCONNECTOR = 1000
    '''
    The switch module waits until it receives a trigger on the rear
    connector.
    '''
    FRONTCONNECTOR = 1001
    '''
    The switch module waits until it receives a trigger on the front
    connector.
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
    RISING_EDGE = 0
    '''
    The trigger occurs on the rising edge of the signal.
    '''
    FALLING_EDGE = 1
    '''
    The trigger occurs on the falling edge of the signal.
    '''


class TriggerMode(Enum):
    SINGLE = 0
    MASTER = 1
    SLAVE = 2
