Enums
=====

Enums used in NI-SWITCH

.. py:currentmodule:: niswitch



.. py:data:: CabledModuleScanAdvancedBus

    .. py:attribute:: niswitch.CabledModuleScanAdvancedBus.NONE



        

        



    .. py:attribute:: niswitch.CabledModuleScanAdvancedBus.PXI_TRIG0



        The switch module waits until it receives a trigger on the PXI\_Trig0
        line before processing the next entry in the scan list.

        



    .. py:attribute:: niswitch.CabledModuleScanAdvancedBus.PXI_TRIG1



        The switch module waits until it receives a trigger on the PXI\_Trig1
        line before processing the next entry in the scan list.

        



    .. py:attribute:: niswitch.CabledModuleScanAdvancedBus.PXI_TRIG2



        The switch module waits until it receives a trigger on the PXI\_Trig2
        line before processing the next entry in the scan list.

        



    .. py:attribute:: niswitch.CabledModuleScanAdvancedBus.PXI_TRIG3



        The switch module waits until it receives a trigger on the PXI\_Trig3
        line before processing the next entry in the scan list.

        



    .. py:attribute:: niswitch.CabledModuleScanAdvancedBus.PXI_TRIG4



        The switch module waits until it receives a trigger on the PXI\_Trig4
        line before processing the next entry in the scan list.

        



    .. py:attribute:: niswitch.CabledModuleScanAdvancedBus.PXI_TRIG5



        The switch module waits until it receives a trigger on the PXI\_Trig5
        line before processing the next entry in the scan list.

        



    .. py:attribute:: niswitch.CabledModuleScanAdvancedBus.PXI_TRIG6



        The switch module waits until it receives a trigger on the PXI\_Trig6
        line before processing the next entry in the scan list.

        



    .. py:attribute:: niswitch.CabledModuleScanAdvancedBus.PXI_TRIG7



        The switch module waits until it receives a trigger on the PXI\_Trig7
        line before processing the next entry in the scan list.

        




.. py:data:: CabledModuleTriggerBus

    .. py:attribute:: niswitch.CabledModuleTriggerBus.NONE



        

        



    .. py:attribute:: niswitch.CabledModuleTriggerBus.PXI_TRIG0



        

        



    .. py:attribute:: niswitch.CabledModuleTriggerBus.PXI_TRIG1



        

        



    .. py:attribute:: niswitch.CabledModuleTriggerBus.PXI_TRIG2



        

        



    .. py:attribute:: niswitch.CabledModuleTriggerBus.PXI_TRIG3



        

        



    .. py:attribute:: niswitch.CabledModuleTriggerBus.PXI_TRIG4



        

        



    .. py:attribute:: niswitch.CabledModuleTriggerBus.PXI_TRIG5



        

        



    .. py:attribute:: niswitch.CabledModuleTriggerBus.PXI_TRIG6



        

        



    .. py:attribute:: niswitch.CabledModuleTriggerBus.PXI_TRIG7



        

        




.. py:data:: HandshakingInitiation

    .. py:attribute:: niswitch.HandshakingInitiation.MEASUREMENT_DEVICE_INITIATED



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

        



    .. py:attribute:: niswitch.HandshakingInitiation.SWITCH_INITIATED



        The `niSwitch Initiate
        Scan <switchviref.chm::/niSwitch_Initiate_Scan.html>`__ VI returns
        immediately after beginning scan list execution. It is assumed that the
        measurement device has already been configured and is waiting for the
        scanner advanced signal. The measurement should be configured to first
        wait for a trigger, then take a measurement. Thus, the first scanner
        advanced output signal of the switch module initiates handshaking.

        




.. py:data:: MasterSlaveScanAdvancedBus

    .. py:attribute:: niswitch.MasterSlaveScanAdvancedBus.NONE



        

        



    .. py:attribute:: niswitch.MasterSlaveScanAdvancedBus.PXI_TRIG0



        The switch module waits until it receives a trigger on the PXI\_Trig0
        line before processing the next entry in the scan list.

        



    .. py:attribute:: niswitch.MasterSlaveScanAdvancedBus.PXI_TRIG1



        The switch module waits until it receives a trigger on the PXI\_Trig1
        line before processing the next entry in the scan list.

        



    .. py:attribute:: niswitch.MasterSlaveScanAdvancedBus.PXI_TRIG2



        The switch module waits until it receives a trigger on the PXI\_Trig2
        line before processing the next entry in the scan list.

        



    .. py:attribute:: niswitch.MasterSlaveScanAdvancedBus.PXI_TRIG3



        The switch module waits until it receives a trigger on the PXI\_Trig3
        line before processing the next entry in the scan list.

        



    .. py:attribute:: niswitch.MasterSlaveScanAdvancedBus.PXI_TRIG4



        The switch module waits until it receives a trigger on the PXI\_Trig4
        line before processing the next entry in the scan list.

        



    .. py:attribute:: niswitch.MasterSlaveScanAdvancedBus.PXI_TRIG5



        The switch module waits until it receives a trigger on the PXI\_Trig5
        line before processing the next entry in the scan list.

        



    .. py:attribute:: niswitch.MasterSlaveScanAdvancedBus.PXI_TRIG6



        The switch module waits until it receives a trigger on the PXI\_Trig6
        line before processing the next entry in the scan list.

        



    .. py:attribute:: niswitch.MasterSlaveScanAdvancedBus.PXI_TRIG7



        The switch module waits until it receives a trigger on the PXI\_Trig7
        line before processing the next entry in the scan list.

        




.. py:data:: MasterSlaveTriggerBus

    .. py:attribute:: niswitch.MasterSlaveTriggerBus.NONE



        

        



    .. py:attribute:: niswitch.MasterSlaveTriggerBus.PXI_TRIG0



        The switch module waits until it receives a trigger on the PXI\_Trig0
        line before processing the next entry in the scan list.

        



    .. py:attribute:: niswitch.MasterSlaveTriggerBus.PXI_TRIG1



        The switch module waits until it receives a trigger on the PXI\_Trig1
        line before processing the next entry in the scan list.

        



    .. py:attribute:: niswitch.MasterSlaveTriggerBus.PXI_TRIG2



        The switch module waits until it receives a trigger on the PXI\_Trig2
        line before processing the next entry in the scan list.

        



    .. py:attribute:: niswitch.MasterSlaveTriggerBus.PXI_TRIG3



        The switch module waits until it receives a trigger on the PXI\_Trig3
        line before processing the next entry in the scan list.

        



    .. py:attribute:: niswitch.MasterSlaveTriggerBus.PXI_TRIG4



        The switch module waits until it receives a trigger on the PXI\_Trig4
        line before processing the next entry in the scan list.

        



    .. py:attribute:: niswitch.MasterSlaveTriggerBus.PXI_TRIG5



        The switch module waits until it receives a trigger on the PXI\_Trig5
        line before processing the next entry in the scan list.

        



    .. py:attribute:: niswitch.MasterSlaveTriggerBus.PXI_TRIG6



        The switch module waits until it receives a trigger on the PXI\_Trig6
        line before processing the next entry in the scan list.

        



    .. py:attribute:: niswitch.MasterSlaveTriggerBus.PXI_TRIG7



        The switch module waits until it receives a trigger on the PXI\_Trig7
        line before processing the next entry in the scan list.

        




.. py:data:: PathCapability

    .. py:attribute:: niswitch.PathCapability.PATH_AVAILABLE



        Path Available

        



    .. py:attribute:: niswitch.PathCapability.PATH_EXISTS



        Path Exists

        



    .. py:attribute:: niswitch.PathCapability.PATH_UNSUPPORTED



        Path Unsupported

        



    .. py:attribute:: niswitch.PathCapability.RESOURCE_IN_USE



        Resource in use

        



    .. py:attribute:: niswitch.PathCapability.SOURCE_CONFLICT



        Source conflict

        



    .. py:attribute:: niswitch.PathCapability.CHANNEL_NOT_AVAILABLE



        Channel not available

        




.. py:data:: RelayAction

    .. py:attribute:: niswitch.RelayAction.OPEN_RELAY



        Open Relay

        



    .. py:attribute:: niswitch.RelayAction.CLOSE_RELAY



        Close Relay

        




.. py:data:: RelayPosition

    .. py:attribute:: niswitch.RelayPosition.OPEN



        Open

        



    .. py:attribute:: niswitch.RelayPosition.CLOSED



        Closed

        




.. py:data:: ScanAdvancedOutput

    .. py:attribute:: niswitch.ScanAdvancedOutput.NONE



        The switch module does not produce a Scan Advanced Output trigger.

        



    .. py:attribute:: niswitch.ScanAdvancedOutput.EXTERNAL



        The switch module produces the Scan Advanced Output trigger on the
        external trigger output.

        



    .. py:attribute:: niswitch.ScanAdvancedOutput.PXI_TRIG0



        The switch module produces the Scan Advanced Output Trigger on the
        PXI\_Trig0 line before processing the next entry in the scan list.

        



    .. py:attribute:: niswitch.ScanAdvancedOutput.PXI_TRIG1



        The switch module produces the Scan Advanced Output Trigger on the
        PXI\_Trig1 line before processing the next entry in the scan list.

        



    .. py:attribute:: niswitch.ScanAdvancedOutput.PXI_TRIG2



        The switch module produces the Scan Advanced Output Trigger on the
        PXI\_Trig2 line before processing the next entry in the scan list.

        



    .. py:attribute:: niswitch.ScanAdvancedOutput.PXI_TRIG3



        The switch module produces the Scan Advanced Output Trigger on the
        PXI\_Trig3 line before processing the next entry in the scan list.

        



    .. py:attribute:: niswitch.ScanAdvancedOutput.PXI_TRIG4



        The switch module produces the Scan Advanced Output Trigger on the
        PXI\_Trig4 line before processing the next entry in the scan list.

        



    .. py:attribute:: niswitch.ScanAdvancedOutput.PXI_TRIG5



        The switch module produces the Scan Advanced Output Trigger on the
        PXI\_Trig5 line before processing the next entry in the scan list.

        



    .. py:attribute:: niswitch.ScanAdvancedOutput.PXI_TRIG6



        The switch module produces the Scan Advanced Output Trigger on the
        PXI\_Trig6 line before processing the next entry in the scan list.

        



    .. py:attribute:: niswitch.ScanAdvancedOutput.PXI_TRIG7



        The switch module produces the Scan Advanced Output Trigger on the
        PXI\_Trig7 line before processing the next entry in the scan list.

        



    .. py:attribute:: niswitch.ScanAdvancedOutput.PXI_STAR



        The switch module produces the Scan Advanced Output Trigger on the PXI
        Star trigger bus before processing the next entry in the scan list.

        



    .. py:attribute:: niswitch.ScanAdvancedOutput.REARCONNECTOR



        The switch module produces the Scan Advanced Output Trigger on the rear
        connector.

        



    .. py:attribute:: niswitch.ScanAdvancedOutput.FRONTCONNECTOR



        The switch module produces the Scan Advanced Output Trigger on the front
        connector.

        



    .. py:attribute:: niswitch.ScanAdvancedOutput.REARCONNECTOR_MODULE1



        The switch module produces the Scan Advanced Output Trigger on the rear
        connector module 1.

        



    .. py:attribute:: niswitch.ScanAdvancedOutput.REARCONNECTOR_MODULE2



        The switch module produces the Scan Advanced Output Trigger on the rear
        connector module 2.

        



    .. py:attribute:: niswitch.ScanAdvancedOutput.REARCONNECTOR_MODULE3



        The switch module produces the Scan Advanced Output Trigger on the rear
        connector module 3.

        



    .. py:attribute:: niswitch.ScanAdvancedOutput.REARCONNECTOR_MODULE4



        The switch module produces the Scan Advanced Output Trigger on the rear
        connector module 4.

        



    .. py:attribute:: niswitch.ScanAdvancedOutput.REARCONNECTOR_MODULE5



        The switch module produces the Scan Advanced Output Trigger on the rear
        connector module 5.

        



    .. py:attribute:: niswitch.ScanAdvancedOutput.REARCONNECTOR_MODULE6



        The switch module produces the Scan Advanced Output Trigger on the rear
        connector module 6.

        



    .. py:attribute:: niswitch.ScanAdvancedOutput.REARCONNECTOR_MODULE7



        The switch module produces the Scan Advanced Output Trigger on the rear
        connector module 7.

        



    .. py:attribute:: niswitch.ScanAdvancedOutput.REARCONNECTOR_MODULE8



        The switch module produces the Scan Advanced Output Trigger on the rear
        connector module 8.

        



    .. py:attribute:: niswitch.ScanAdvancedOutput.REARCONNECTOR_MODULE9



        The switch module produces the Scan Advanced Ouptut Trigger on the rear
        connector module 9.

        



    .. py:attribute:: niswitch.ScanAdvancedOutput.REARCONNECTOR_MODULE10



        The switch module produces the Scan Advanced Output Trigger on the rear
        connector module 10.

        



    .. py:attribute:: niswitch.ScanAdvancedOutput.REARCONNECTOR_MODULE11



        The switch module produces the Scan Advanced Output Trigger on the rear
        connector module 11.

        



    .. py:attribute:: niswitch.ScanAdvancedOutput.REARCONNECTOR_MODULE12



        The switch module produces the Scan Advanced Output Trigger on the rear
        connector module 12.

        



    .. py:attribute:: niswitch.ScanAdvancedOutput.FRONTCONNECTOR_MODULE1



        The switch module produces the Scan Advanced Output Trigger on the front
        connector module 1.

        



    .. py:attribute:: niswitch.ScanAdvancedOutput.FRONTCONNECTOR_MODULE2



        The switch module produces the Scan Advanced Output Trigger on the front
        connector module 2.

        



    .. py:attribute:: niswitch.ScanAdvancedOutput.FRONTCONNECTOR_MODULE3



        The switch module produces the Scan Advanced Output Trigger on the front
        connector module 3.

        



    .. py:attribute:: niswitch.ScanAdvancedOutput.FRONTCONNECTOR_MODULE4



        The switch module produces the Scan Advanced Output Trigger on the front
        connector module 4.

        



    .. py:attribute:: niswitch.ScanAdvancedOutput.FRONTCONNECTOR_MODULE5



        The switch module produces the Scan Advanced Output Trigger on the front
        connector module 5.

        



    .. py:attribute:: niswitch.ScanAdvancedOutput.FRONTCONNECTOR_MODULE6



        The switch module produces the Scan Advanced Output Trigger on the front
        connector module 6.

        



    .. py:attribute:: niswitch.ScanAdvancedOutput.FRONTCONNECTOR_MODULE7



        The switch module produces the Scan Advanced Output Trigger on the front
        connector module 7.

        



    .. py:attribute:: niswitch.ScanAdvancedOutput.FRONTCONNECTOR_MODULE8



        The switch module produces the Scan Advanced Output Trigger on the front
        connector module 8.

        



    .. py:attribute:: niswitch.ScanAdvancedOutput.FRONTCONNECTOR_MODULE9



        The switch module produces the Scan Advanced Output Trigger on the front
        connector module 9.

        



    .. py:attribute:: niswitch.ScanAdvancedOutput.FRONTCONNECTOR_MODULE10



        The switch module produces the Scan Advanced Output Trigger on the front
        connector module 10.

        



    .. py:attribute:: niswitch.ScanAdvancedOutput.FRONTCONNECTOR_MODULE11



        The switch module produces the Scan Advanced Output Trigger on the front
        connector module 11.

        



    .. py:attribute:: niswitch.ScanAdvancedOutput.FRONTCONNECTOR_MODULE12



        The switch module produces the Scan Advanced Output Trigger on the front
        connector module 12.

        




.. py:data:: ScanAdvancedPolarity

    .. py:attribute:: niswitch.ScanAdvancedPolarity.RISING_EDGE



        The trigger occurs on the rising edge of the signal.

        



    .. py:attribute:: niswitch.ScanAdvancedPolarity.FALLING_EDGE



        The trigger occurs on the falling edge of the signal.

        




.. py:data:: ScanMode

    .. py:attribute:: niswitch.ScanMode.NONE



        No implicit action on connections when scanning.

        



    .. py:attribute:: niswitch.ScanMode.BREAK_BEFORE_MAKE



        When scanning, the switch module breaks existing connections before
        making new connections.

        



    .. py:attribute:: niswitch.ScanMode.BREAK_AFTER_MAKE



        When scanning, the switch module breaks existing connections after
        making new connections.

        




.. py:data:: TriggerInput

    .. py:attribute:: niswitch.TriggerInput.IMMEDIATE



        The switch module does not wait for a trigger before processing the next
        entry in the scan list.

        



    .. py:attribute:: niswitch.TriggerInput.EXTERNAL



        The switch module waits until it receives a trigger from an external
        source through the external trigger input before processing the next
        entry in the scan list.

        



    .. py:attribute:: niswitch.TriggerInput.SW_TRIG_FUNC



        The switch module waits until you call the `niSwitch Send Software
        Trigger <switchviref.chm::/niSwitch_Send_Software_Trigger.html>`__ VI
        before processing the next entry in the scan list.

        



    .. py:attribute:: niswitch.TriggerInput.PXI_TRIG0



        The switch module waits until it receives a trigger on the PXI\_Trig0
        line before processing the next entry in the scan list.

        



    .. py:attribute:: niswitch.TriggerInput.PXI_TRIG1



        The switch module waits until it receives a trigger on the PXI\_Trig1
        line before processing the next entry in the scan list.

        



    .. py:attribute:: niswitch.TriggerInput.PXI_TRIG2



        The switch module waits until it receives a trigger on the PXI\_Trig2
        line before processing the next entry in the scan list.

        



    .. py:attribute:: niswitch.TriggerInput.PXI_TRIG3



        The switch module waits until it receives a trigger on the PXI\_Trig3
        line before processing the next entry in the scan list.

        



    .. py:attribute:: niswitch.TriggerInput.PXI_TRIG4



        The switch module waits until it receives a trigger on the PXI\_Trig4
        line before processing the next entry in the scan list.

        



    .. py:attribute:: niswitch.TriggerInput.PXI_TRIG5



        The switch module waits until it receives a trigger on the PXI\_Trig5
        line before processing the next entry in the scan list.

        



    .. py:attribute:: niswitch.TriggerInput.PXI_TRIG6



        The switch module waits until it receives a trigger on the PXI\_Trig6
        line before processing the next entry in the scan list.

        



    .. py:attribute:: niswitch.TriggerInput.PXI_TRIG7



        The switch module waits until it receives a trigger on the PXI\_Trig7
        line before processing the next entry in the scan list.

        



    .. py:attribute:: niswitch.TriggerInput.PXI_STAR



        The switch module waits until it receives a trigger on the PXI star
        trigger bus before processing the next entry in the scan list.

        



    .. py:attribute:: niswitch.TriggerInput.REARCONNECTOR



        The switch module waits until it receives a trigger on the rear
        connector.

        



    .. py:attribute:: niswitch.TriggerInput.FRONTCONNECTOR



        The switch module waits until it receives a trigger on the front
        connector.

        



    .. py:attribute:: niswitch.TriggerInput.REARCONNECTOR_MODULE1



        The switch module waits until it receives a trigger on the rear
        connector module 1.

        



    .. py:attribute:: niswitch.TriggerInput.REARCONNECTOR_MODULE2



        The switch module waits until it receives a trigger on the rear
        connector module 2.

        



    .. py:attribute:: niswitch.TriggerInput.REARCONNECTOR_MODULE3



        The switch module waits until it receives a trigger on the rear
        connector module 3.

        



    .. py:attribute:: niswitch.TriggerInput.REARCONNECTOR_MODULE4



        The switch module waits until it receives a trigger on the rear
        connector module 4.

        



    .. py:attribute:: niswitch.TriggerInput.REARCONNECTOR_MODULE5



        The switch module waits until it receives a trigger on the rear
        connector module 5.

        



    .. py:attribute:: niswitch.TriggerInput.REARCONNECTOR_MODULE6



        The switch module waits until it receives a trigger on the rear
        connector module 6.

        



    .. py:attribute:: niswitch.TriggerInput.REARCONNECTOR_MODULE7



        The switch module waits until it receives a trigger on the rear
        connector module 7.

        



    .. py:attribute:: niswitch.TriggerInput.REARCONNECTOR_MODULE8



        The switch module waits until it receives a trigger on the rear
        connector module 8.

        



    .. py:attribute:: niswitch.TriggerInput.REARCONNECTOR_MODULE9



        The switch module waits until it receives a trigger on the rear
        connector module 9.

        



    .. py:attribute:: niswitch.TriggerInput.REARCONNECTOR_MODULE10



        The switch module waits until it receives a trigger on the rear
        connector module 10.

        



    .. py:attribute:: niswitch.TriggerInput.REARCONNECTOR_MODULE11



        The switch module waits until it receives a trigger on the rear
        connector module 11.

        



    .. py:attribute:: niswitch.TriggerInput.REARCONNECTOR_MODULE12



        The switch module waits until it receives a trigger on the rear
        connector module 12.

        



    .. py:attribute:: niswitch.TriggerInput.FRONTCONNECTOR_MODULE1



        The switch module waits until it receives a trigger on the front
        connector module 1.

        



    .. py:attribute:: niswitch.TriggerInput.FRONTCONNECTOR_MODULE2



        The switch module waits until it receives a trigger on the front
        connector module 2.

        



    .. py:attribute:: niswitch.TriggerInput.FRONTCONNECTOR_MODULE3



        The switch module waits until it receives a trigger on the front
        connector module 3.

        



    .. py:attribute:: niswitch.TriggerInput.FRONTCONNECTOR_MODULE4



        The switch module waits until it receives a trigger on the front
        connector module 4.

        



    .. py:attribute:: niswitch.TriggerInput.FRONTCONNECTOR_MODULE5



        The switch module waits until it receives a trigger on the front
        connector module 5.

        



    .. py:attribute:: niswitch.TriggerInput.FRONTCONNECTOR_MODULE6



        The switch module waits until it receives a trigger on the front
        connector module 6.

        



    .. py:attribute:: niswitch.TriggerInput.FRONTCONNECTOR_MODULE7



        The switch module waits until it receives a trigger on the front
        connector module 7.

        



    .. py:attribute:: niswitch.TriggerInput.FRONTCONNECTOR_MODULE8



        The switch module waits until it receives a trigger on the front
        connector module 8.

        



    .. py:attribute:: niswitch.TriggerInput.FRONTCONNECTOR_MODULE9



        The switch module waits until it receives a trigger on the front
        connector module 9.

        



    .. py:attribute:: niswitch.TriggerInput.FRONTCONNECTOR_MODULE10



        The switch module waits until it receives a trigger on the front
        connector module 10.

        



    .. py:attribute:: niswitch.TriggerInput.FRONTCONNECTOR_MODULE11



        The switch module waits until it receives a trigger on the front
        connector module 11.

        



    .. py:attribute:: niswitch.TriggerInput.FRONTCONNECTOR_MODULE12



        The switch module waits until it receives a trigger on the front
        connector module 12.

        




.. py:data:: TriggerInputPolarity

    .. py:attribute:: niswitch.TriggerInputPolarity.RISING_EDGE



        The trigger occurs on the rising edge of the signal.

        



    .. py:attribute:: niswitch.TriggerInputPolarity.FALLING_EDGE



        The trigger occurs on the falling edge of the signal.

        




.. py:data:: TriggerMode

    .. py:attribute:: niswitch.TriggerMode.SINGLE



        

        



    .. py:attribute:: niswitch.TriggerMode.MASTER



        

        



    .. py:attribute:: niswitch.TriggerMode.SLAVE



        

        


