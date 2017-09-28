Enums
=====

Enums used in NI-SWITCH

.. py:currentmodule:: niswitch



.. py:data:: CabledModuleScanAdvancedBus

    .. py:attribute:: NONE



        

        


    .. py:attribute:: PXI_TRIG0



        The switch module waits until it receives a trigger on the PXI\_Trig0
        line before processing the next entry in the scan list.

        


    .. py:attribute:: PXI_TRIG1



        The switch module waits until it receives a trigger on the PXI\_Trig1
        line before processing the next entry in the scan list.

        


    .. py:attribute:: PXI_TRIG2



        The switch module waits until it receives a trigger on the PXI\_Trig2
        line before processing the next entry in the scan list.

        


    .. py:attribute:: PXI_TRIG3



        The switch module waits until it receives a trigger on the PXI\_Trig3
        line before processing the next entry in the scan list.

        


    .. py:attribute:: PXI_TRIG4



        The switch module waits until it receives a trigger on the PXI\_Trig4
        line before processing the next entry in the scan list.

        


    .. py:attribute:: PXI_TRIG5



        The switch module waits until it receives a trigger on the PXI\_Trig5
        line before processing the next entry in the scan list.

        


    .. py:attribute:: PXI_TRIG6



        The switch module waits until it receives a trigger on the PXI\_Trig6
        line before processing the next entry in the scan list.

        


    .. py:attribute:: PXI_TRIG7



        The switch module waits until it receives a trigger on the PXI\_Trig7
        line before processing the next entry in the scan list.

        



.. py:data:: CabledModuleTriggerBus

    .. py:attribute:: NONE



        

        


    .. py:attribute:: PXI_TRIG0



        

        


    .. py:attribute:: PXI_TRIG1



        

        


    .. py:attribute:: PXI_TRIG2



        

        


    .. py:attribute:: PXI_TRIG3



        

        


    .. py:attribute:: PXI_TRIG4



        

        


    .. py:attribute:: PXI_TRIG5



        

        


    .. py:attribute:: PXI_TRIG6



        

        


    .. py:attribute:: PXI_TRIG7



        

        



.. py:data:: HandshakingInitiation

    .. py:attribute:: MEASUREMENT_DEVICE_INITIATED



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

        


    .. py:attribute:: SWITCH_INITIATED



        The `niSwitch Initiate
        Scan <switchviref.chm::/niSwitch_Initiate_Scan.html>`__ VI returns
        immediately after beginning scan list execution. It is assumed that the
        measurement device has already been configured and is waiting for the
        scanner advanced signal. The measurement should be configured to first
        wait for a trigger, then take a measurement. Thus, the first scanner
        advanced output signal of the switch module initiates handshaking.

        



.. py:data:: MasterSlaveScanAdvancedBus

    .. py:attribute:: NONE



        

        


    .. py:attribute:: PXI_TRIG0



        The switch module waits until it receives a trigger on the PXI\_Trig0
        line before processing the next entry in the scan list.

        


    .. py:attribute:: PXI_TRIG1



        The switch module waits until it receives a trigger on the PXI\_Trig1
        line before processing the next entry in the scan list.

        


    .. py:attribute:: PXI_TRIG2



        The switch module waits until it receives a trigger on the PXI\_Trig2
        line before processing the next entry in the scan list.

        


    .. py:attribute:: PXI_TRIG3



        The switch module waits until it receives a trigger on the PXI\_Trig3
        line before processing the next entry in the scan list.

        


    .. py:attribute:: PXI_TRIG4



        The switch module waits until it receives a trigger on the PXI\_Trig4
        line before processing the next entry in the scan list.

        


    .. py:attribute:: PXI_TRIG5



        The switch module waits until it receives a trigger on the PXI\_Trig5
        line before processing the next entry in the scan list.

        


    .. py:attribute:: PXI_TRIG6



        The switch module waits until it receives a trigger on the PXI\_Trig6
        line before processing the next entry in the scan list.

        


    .. py:attribute:: PXI_TRIG7



        The switch module waits until it receives a trigger on the PXI\_Trig7
        line before processing the next entry in the scan list.

        



.. py:data:: MasterSlaveTriggerBus

    .. py:attribute:: NONE



        

        


    .. py:attribute:: PXI_TRIG0



        The switch module waits until it receives a trigger on the PXI\_Trig0
        line before processing the next entry in the scan list.

        


    .. py:attribute:: PXI_TRIG1



        The switch module waits until it receives a trigger on the PXI\_Trig1
        line before processing the next entry in the scan list.

        


    .. py:attribute:: PXI_TRIG2



        The switch module waits until it receives a trigger on the PXI\_Trig2
        line before processing the next entry in the scan list.

        


    .. py:attribute:: PXI_TRIG3



        The switch module waits until it receives a trigger on the PXI\_Trig3
        line before processing the next entry in the scan list.

        


    .. py:attribute:: PXI_TRIG4



        The switch module waits until it receives a trigger on the PXI\_Trig4
        line before processing the next entry in the scan list.

        


    .. py:attribute:: PXI_TRIG5



        The switch module waits until it receives a trigger on the PXI\_Trig5
        line before processing the next entry in the scan list.

        


    .. py:attribute:: PXI_TRIG6



        The switch module waits until it receives a trigger on the PXI\_Trig6
        line before processing the next entry in the scan list.

        


    .. py:attribute:: PXI_TRIG7



        The switch module waits until it receives a trigger on the PXI\_Trig7
        line before processing the next entry in the scan list.

        



.. py:data:: PathCapability

    .. py:attribute:: PATH_AVAILABLE



        Path Available

        


    .. py:attribute:: PATH_EXISTS



        Path Exists

        


    .. py:attribute:: PATH_UNSUPPORTED



        Path Unsupported

        


    .. py:attribute:: RESOURCE_IN_USE



        Resource in use

        


    .. py:attribute:: SOURCE_CONFLICT



        Source conflict

        


    .. py:attribute:: CHANNEL_NOT_AVAILABLE



        Channel not available

        



.. py:data:: RelayAction

    .. py:attribute:: OPEN_RELAY



        Open Relay

        


    .. py:attribute:: CLOSE_RELAY



        Close Relay

        



.. py:data:: RelayPosition

    .. py:attribute:: OPEN



        Open

        


    .. py:attribute:: CLOSED



        Closed

        



.. py:data:: ScanAdvancedOutput

    .. py:attribute:: NONE



        The switch module does not produce a Scan Advanced Output trigger.

        


    .. py:attribute:: EXTERNAL



        The switch module produces the Scan Advanced Output trigger on the
        external trigger output.

        


    .. py:attribute:: PXI_TRIG0



        The switch module produces the Scan Advanced Output Trigger on the
        PXI\_Trig0 line before processing the next entry in the scan list.

        


    .. py:attribute:: PXI_TRIG1



        The switch module produces the Scan Advanced Output Trigger on the
        PXI\_Trig1 line before processing the next entry in the scan list.

        


    .. py:attribute:: PXI_TRIG2



        The switch module produces the Scan Advanced Output Trigger on the
        PXI\_Trig2 line before processing the next entry in the scan list.

        


    .. py:attribute:: PXI_TRIG3



        The switch module produces the Scan Advanced Output Trigger on the
        PXI\_Trig3 line before processing the next entry in the scan list.

        


    .. py:attribute:: PXI_TRIG4



        The switch module produces the Scan Advanced Output Trigger on the
        PXI\_Trig4 line before processing the next entry in the scan list.

        


    .. py:attribute:: PXI_TRIG5



        The switch module produces the Scan Advanced Output Trigger on the
        PXI\_Trig5 line before processing the next entry in the scan list.

        


    .. py:attribute:: PXI_TRIG6



        The switch module produces the Scan Advanced Output Trigger on the
        PXI\_Trig6 line before processing the next entry in the scan list.

        


    .. py:attribute:: PXI_TRIG7



        The switch module produces the Scan Advanced Output Trigger on the
        PXI\_Trig7 line before processing the next entry in the scan list.

        


    .. py:attribute:: PXI_STAR



        The switch module produces the Scan Advanced Output Trigger on the PXI
        Star trigger bus before processing the next entry in the scan list.

        


    .. py:attribute:: REARCONNECTOR



        The switch module produces the Scan Advanced Output Trigger on the rear
        connector.

        


    .. py:attribute:: FRONTCONNECTOR



        The switch module produces the Scan Advanced Output Trigger on the front
        connector.

        


    .. py:attribute:: REARCONNECTOR_MODULE1



        The switch module produces the Scan Advanced Output Trigger on the rear
        connector module 1.

        


    .. py:attribute:: REARCONNECTOR_MODULE2



        The switch module produces the Scan Advanced Output Trigger on the rear
        connector module 2.

        


    .. py:attribute:: REARCONNECTOR_MODULE3



        The switch module produces the Scan Advanced Output Trigger on the rear
        connector module 3.

        


    .. py:attribute:: REARCONNECTOR_MODULE4



        The switch module produces the Scan Advanced Output Trigger on the rear
        connector module 4.

        


    .. py:attribute:: REARCONNECTOR_MODULE5



        The switch module produces the Scan Advanced Output Trigger on the rear
        connector module 5.

        


    .. py:attribute:: REARCONNECTOR_MODULE6



        The switch module produces the Scan Advanced Output Trigger on the rear
        connector module 6.

        


    .. py:attribute:: REARCONNECTOR_MODULE7



        The switch module produces the Scan Advanced Output Trigger on the rear
        connector module 7.

        


    .. py:attribute:: REARCONNECTOR_MODULE8



        The switch module produces the Scan Advanced Output Trigger on the rear
        connector module 8.

        


    .. py:attribute:: REARCONNECTOR_MODULE9



        The switch module produces the Scan Advanced Ouptut Trigger on the rear
        connector module 9.

        


    .. py:attribute:: REARCONNECTOR_MODULE10



        The switch module produces the Scan Advanced Output Trigger on the rear
        connector module 10.

        


    .. py:attribute:: REARCONNECTOR_MODULE11



        The switch module produces the Scan Advanced Output Trigger on the rear
        connector module 11.

        


    .. py:attribute:: REARCONNECTOR_MODULE12



        The switch module produces the Scan Advanced Output Trigger on the rear
        connector module 12.

        


    .. py:attribute:: FRONTCONNECTOR_MODULE1



        The switch module produces the Scan Advanced Output Trigger on the front
        connector module 1.

        


    .. py:attribute:: FRONTCONNECTOR_MODULE2



        The switch module produces the Scan Advanced Output Trigger on the front
        connector module 2.

        


    .. py:attribute:: FRONTCONNECTOR_MODULE3



        The switch module produces the Scan Advanced Output Trigger on the front
        connector module 3.

        


    .. py:attribute:: FRONTCONNECTOR_MODULE4



        The switch module produces the Scan Advanced Output Trigger on the front
        connector module 4.

        


    .. py:attribute:: FRONTCONNECTOR_MODULE5



        The switch module produces the Scan Advanced Output Trigger on the front
        connector module 5.

        


    .. py:attribute:: FRONTCONNECTOR_MODULE6



        The switch module produces the Scan Advanced Output Trigger on the front
        connector module 6.

        


    .. py:attribute:: FRONTCONNECTOR_MODULE7



        The switch module produces the Scan Advanced Output Trigger on the front
        connector module 7.

        


    .. py:attribute:: FRONTCONNECTOR_MODULE8



        The switch module produces the Scan Advanced Output Trigger on the front
        connector module 8.

        


    .. py:attribute:: FRONTCONNECTOR_MODULE9



        The switch module produces the Scan Advanced Output Trigger on the front
        connector module 9.

        


    .. py:attribute:: FRONTCONNECTOR_MODULE10



        The switch module produces the Scan Advanced Output Trigger on the front
        connector module 10.

        


    .. py:attribute:: FRONTCONNECTOR_MODULE11



        The switch module produces the Scan Advanced Output Trigger on the front
        connector module 11.

        


    .. py:attribute:: FRONTCONNECTOR_MODULE12



        The switch module produces the Scan Advanced Output Trigger on the front
        connector module 12.

        



.. py:data:: ScanAdvancedPolarity

    .. py:attribute:: RISING_EDGE



        The trigger occurs on the rising edge of the signal.

        


    .. py:attribute:: FALLING_EDGE



        The trigger occurs on the falling edge of the signal.

        



.. py:data:: ScanMode

    .. py:attribute:: NONE



        No implicit action on connections when scanning.

        


    .. py:attribute:: BREAK_BEFORE_MAKE



        When scanning, the switch module breaks existing connections before
        making new connections.

        


    .. py:attribute:: BREAK_AFTER_MAKE



        When scanning, the switch module breaks existing connections after
        making new connections.

        



.. py:data:: TriggerInput

    .. py:attribute:: IMMEDIATE



        The switch module does not wait for a trigger before processing the next
        entry in the scan list.

        


    .. py:attribute:: EXTERNAL



        The switch module waits until it receives a trigger from an external
        source through the external trigger input before processing the next
        entry in the scan list.

        


    .. py:attribute:: SW_TRIG_FUNC



        The switch module waits until you call the `niSwitch Send Software
        Trigger <switchviref.chm::/niSwitch_Send_Software_Trigger.html>`__ VI
        before processing the next entry in the scan list.

        


    .. py:attribute:: PXI_TRIG0



        The switch module waits until it receives a trigger on the PXI\_Trig0
        line before processing the next entry in the scan list.

        


    .. py:attribute:: PXI_TRIG1



        The switch module waits until it receives a trigger on the PXI\_Trig1
        line before processing the next entry in the scan list.

        


    .. py:attribute:: PXI_TRIG2



        The switch module waits until it receives a trigger on the PXI\_Trig2
        line before processing the next entry in the scan list.

        


    .. py:attribute:: PXI_TRIG3



        The switch module waits until it receives a trigger on the PXI\_Trig3
        line before processing the next entry in the scan list.

        


    .. py:attribute:: PXI_TRIG4



        The switch module waits until it receives a trigger on the PXI\_Trig4
        line before processing the next entry in the scan list.

        


    .. py:attribute:: PXI_TRIG5



        The switch module waits until it receives a trigger on the PXI\_Trig5
        line before processing the next entry in the scan list.

        


    .. py:attribute:: PXI_TRIG6



        The switch module waits until it receives a trigger on the PXI\_Trig6
        line before processing the next entry in the scan list.

        


    .. py:attribute:: PXI_TRIG7



        The switch module waits until it receives a trigger on the PXI\_Trig7
        line before processing the next entry in the scan list.

        


    .. py:attribute:: PXI_STAR



        The switch module waits until it receives a trigger on the PXI star
        trigger bus before processing the next entry in the scan list.

        


    .. py:attribute:: REARCONNECTOR



        The switch module waits until it receives a trigger on the rear
        connector.

        


    .. py:attribute:: FRONTCONNECTOR



        The switch module waits until it receives a trigger on the front
        connector.

        


    .. py:attribute:: REARCONNECTOR_MODULE1



        The switch module waits until it receives a trigger on the rear
        connector module 1.

        


    .. py:attribute:: REARCONNECTOR_MODULE2



        The switch module waits until it receives a trigger on the rear
        connector module 2.

        


    .. py:attribute:: REARCONNECTOR_MODULE3



        The switch module waits until it receives a trigger on the rear
        connector module 3.

        


    .. py:attribute:: REARCONNECTOR_MODULE4



        The switch module waits until it receives a trigger on the rear
        connector module 4.

        


    .. py:attribute:: REARCONNECTOR_MODULE5



        The switch module waits until it receives a trigger on the rear
        connector module 5.

        


    .. py:attribute:: REARCONNECTOR_MODULE6



        The switch module waits until it receives a trigger on the rear
        connector module 6.

        


    .. py:attribute:: REARCONNECTOR_MODULE7



        The switch module waits until it receives a trigger on the rear
        connector module 7.

        


    .. py:attribute:: REARCONNECTOR_MODULE8



        The switch module waits until it receives a trigger on the rear
        connector module 8.

        


    .. py:attribute:: REARCONNECTOR_MODULE9



        The switch module waits until it receives a trigger on the rear
        connector module 9.

        


    .. py:attribute:: REARCONNECTOR_MODULE10



        The switch module waits until it receives a trigger on the rear
        connector module 10.

        


    .. py:attribute:: REARCONNECTOR_MODULE11



        The switch module waits until it receives a trigger on the rear
        connector module 11.

        


    .. py:attribute:: REARCONNECTOR_MODULE12



        The switch module waits until it receives a trigger on the rear
        connector module 12.

        


    .. py:attribute:: FRONTCONNECTOR_MODULE1



        The switch module waits until it receives a trigger on the front
        connector module 1.

        


    .. py:attribute:: FRONTCONNECTOR_MODULE2



        The switch module waits until it receives a trigger on the front
        connector module 2.

        


    .. py:attribute:: FRONTCONNECTOR_MODULE3



        The switch module waits until it receives a trigger on the front
        connector module 3.

        


    .. py:attribute:: FRONTCONNECTOR_MODULE4



        The switch module waits until it receives a trigger on the front
        connector module 4.

        


    .. py:attribute:: FRONTCONNECTOR_MODULE5



        The switch module waits until it receives a trigger on the front
        connector module 5.

        


    .. py:attribute:: FRONTCONNECTOR_MODULE6



        The switch module waits until it receives a trigger on the front
        connector module 6.

        


    .. py:attribute:: FRONTCONNECTOR_MODULE7



        The switch module waits until it receives a trigger on the front
        connector module 7.

        


    .. py:attribute:: FRONTCONNECTOR_MODULE8



        The switch module waits until it receives a trigger on the front
        connector module 8.

        


    .. py:attribute:: FRONTCONNECTOR_MODULE9



        The switch module waits until it receives a trigger on the front
        connector module 9.

        


    .. py:attribute:: FRONTCONNECTOR_MODULE10



        The switch module waits until it receives a trigger on the front
        connector module 10.

        


    .. py:attribute:: FRONTCONNECTOR_MODULE11



        The switch module waits until it receives a trigger on the front
        connector module 11.

        


    .. py:attribute:: FRONTCONNECTOR_MODULE12



        The switch module waits until it receives a trigger on the front
        connector module 12.

        



.. py:data:: TriggerInputPolarity

    .. py:attribute:: RISING_EDGE



        The trigger occurs on the rising edge of the signal.

        


    .. py:attribute:: FALLING_EDGE



        The trigger occurs on the falling edge of the signal.

        



.. py:data:: TriggerMode

    .. py:attribute:: SINGLE



        

        


    .. py:attribute:: MASTER



        

        


    .. py:attribute:: SLAVE



        

        

