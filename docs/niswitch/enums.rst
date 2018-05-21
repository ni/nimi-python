Enums
=====

Enums used in NI-SWITCH

.. py:currentmodule:: niswitch


HandshakingInitiation
---------------------

.. py:class:: HandshakingInitiation

    .. py:attribute:: HandshakingInitiation.MEASUREMENT_DEVICE



        The `niSwitch Initiate
        Scan <switchviref.chm::/:py:meth:`niswitch.Session.Initiate_Scan`.html>`__ VI does not
        return until the switch hardware is waiting for a trigger input. This
        ensures that if you initiate the measurement device after calling the
        `niSwitch Initiate
        Scan <switchviref.chm::/:py:meth:`niswitch.Session.Initiate_Scan`.html>`__ VI , the switch
        is sure to receive the first measurement complete (MC) signal sent by
        the measurement device. The measurement device should be configured to
        first take a measurement, send MC, then wait for scanner advanced output
        signal. Thus, the first MC of the measurement device initiates
        handshaking.

        



    .. py:attribute:: HandshakingInitiation.SWITCH



        The `niSwitch Initiate
        Scan <switchviref.chm::/:py:meth:`niswitch.Session.Initiate_Scan`.html>`__ VI returns
        immediately after beginning scan list execution. It is assumed that the
        measurement device has already been configured and is waiting for the
        scanner advanced signal. The measurement should be configured to first
        wait for a trigger, then take a measurement. Thus, the first scanner
        advanced output signal of the switch module initiates handshaking.

        



PathCapability
--------------

.. py:class:: PathCapability

    .. py:attribute:: PathCapability.PATH_AVAILABLE



        Path Available

        



    .. py:attribute:: PathCapability.PATH_EXISTS



        Path Exists

        



    .. py:attribute:: PathCapability.PATH_UNSUPPORTED



        Path Unsupported

        



    .. py:attribute:: PathCapability.RESOURCE_IN_USE



        Resource in use

        



    .. py:attribute:: PathCapability.SOURCE_CONFLICT



        Source conflict

        



    .. py:attribute:: PathCapability.CHANNEL_NOT_AVAILABLE



        Channel not available

        



RelayAction
-----------

.. py:class:: RelayAction

    .. py:attribute:: RelayAction.OPEN



        Open Relay

        



    .. py:attribute:: RelayAction.CLOSE



        Close Relay

        



RelayPosition
-------------

.. py:class:: RelayPosition

    .. py:attribute:: RelayPosition.OPEN



        Open

        



    .. py:attribute:: RelayPosition.CLOSED



        Closed

        



ScanAdvancedOutput
------------------

.. py:class:: ScanAdvancedOutput

    .. py:attribute:: ScanAdvancedOutput.NONE



        The switch device does not produce a Scan Advanced Output trigger.

        



    .. py:attribute:: ScanAdvancedOutput.EXTERNAL



        External Trigger. The switch device produces the Scan Advanced Output  trigger on the external trigger output.

        



    .. py:attribute:: ScanAdvancedOutput.TTL0



        The switch device produces the Scan Advanced Output on the PXI TRIG0 line.

        



    .. py:attribute:: ScanAdvancedOutput.TTL1



        The switch device produces the Scan Advanced Output on the PXI TRIG1 line.

        



    .. py:attribute:: ScanAdvancedOutput.TTL2



        The switch device produces the Scan Advanced Output on the PXI TRIG2 line.

        



    .. py:attribute:: ScanAdvancedOutput.TTL3



        The switch device produces the Scan Advanced Output on the PXI TRIG3 line.

        



    .. py:attribute:: ScanAdvancedOutput.TTL4



        The switch device produces the Scan Advanced Output on the PXI TRIG4 line.

        



    .. py:attribute:: ScanAdvancedOutput.TTL5



        The switch device produces the Scan Advanced Output on the PXI TRIG5 line.

        



    .. py:attribute:: ScanAdvancedOutput.TTL6



        The switch device produces the Scan Advanced Output on the PXI TRIG6 line.

        



    .. py:attribute:: ScanAdvancedOutput.TTL7



        The switch device produces the Scan Advanced Output on the PXI TRIG7 line.

        



    .. py:attribute:: ScanAdvancedOutput.PXI_STAR



        The switch module produces the Scan Advanced Output Trigger on the PXI
        Star trigger bus before processing the next entry in the scan list.

        



    .. py:attribute:: ScanAdvancedOutput.REARCONNECTOR



        The switch device produces the Scan Advanced Output  trigger on the rear connector.

        



    .. py:attribute:: ScanAdvancedOutput.FRONTCONNECTOR



        The switch device produces the Scan Advanced Output  trigger on the front connector.

        



    .. py:attribute:: ScanAdvancedOutput.REARCONNECTOR_MODULE1



        The switch module produces the Scan Advanced Output Trigger on the rear
        connector module 1.

        



    .. py:attribute:: ScanAdvancedOutput.REARCONNECTOR_MODULE2



        The switch module produces the Scan Advanced Output Trigger on the rear
        connector module 2.

        



    .. py:attribute:: ScanAdvancedOutput.REARCONNECTOR_MODULE3



        The switch module produces the Scan Advanced Output Trigger on the rear
        connector module 3.

        



    .. py:attribute:: ScanAdvancedOutput.REARCONNECTOR_MODULE4



        The switch module produces the Scan Advanced Output Trigger on the rear
        connector module 4.

        



    .. py:attribute:: ScanAdvancedOutput.REARCONNECTOR_MODULE5



        The switch module produces the Scan Advanced Output Trigger on the rear
        connector module 5.

        



    .. py:attribute:: ScanAdvancedOutput.REARCONNECTOR_MODULE6



        The switch module produces the Scan Advanced Output Trigger on the rear
        connector module 6.

        



    .. py:attribute:: ScanAdvancedOutput.REARCONNECTOR_MODULE7



        The switch module produces the Scan Advanced Output Trigger on the rear
        connector module 7.

        



    .. py:attribute:: ScanAdvancedOutput.REARCONNECTOR_MODULE8



        The switch module produces the Scan Advanced Output Trigger on the rear
        connector module 8.

        



    .. py:attribute:: ScanAdvancedOutput.REARCONNECTOR_MODULE9



        The switch module produces the Scan Advanced Ouptut Trigger on the rear
        connector module 9.

        



    .. py:attribute:: ScanAdvancedOutput.REARCONNECTOR_MODULE10



        The switch module produces the Scan Advanced Output Trigger on the rear
        connector module 10.

        



    .. py:attribute:: ScanAdvancedOutput.REARCONNECTOR_MODULE11



        The switch module produces the Scan Advanced Output Trigger on the rear
        connector module 11.

        



    .. py:attribute:: ScanAdvancedOutput.REARCONNECTOR_MODULE12



        The switch module produces the Scan Advanced Output Trigger on the rear
        connector module 12.

        



    .. py:attribute:: ScanAdvancedOutput.FRONTCONNECTOR_MODULE1



        The switch module produces the Scan Advanced Output Trigger on the front
        connector module 1.

        



    .. py:attribute:: ScanAdvancedOutput.FRONTCONNECTOR_MODULE2



        The switch module produces the Scan Advanced Output Trigger on the front
        connector module 2.

        



    .. py:attribute:: ScanAdvancedOutput.FRONTCONNECTOR_MODULE3



        The switch module produces the Scan Advanced Output Trigger on the front
        connector module 3.

        



    .. py:attribute:: ScanAdvancedOutput.FRONTCONNECTOR_MODULE4



        The switch module produces the Scan Advanced Output Trigger on the front
        connector module 4.

        



    .. py:attribute:: ScanAdvancedOutput.FRONTCONNECTOR_MODULE5



        The switch module produces the Scan Advanced Output Trigger on the front
        connector module 5.

        



    .. py:attribute:: ScanAdvancedOutput.FRONTCONNECTOR_MODULE6



        The switch module produces the Scan Advanced Output Trigger on the front
        connector module 6.

        



    .. py:attribute:: ScanAdvancedOutput.FRONTCONNECTOR_MODULE7



        The switch module produces the Scan Advanced Output Trigger on the front
        connector module 7.

        



    .. py:attribute:: ScanAdvancedOutput.FRONTCONNECTOR_MODULE8



        The switch module produces the Scan Advanced Output Trigger on the front
        connector module 8.

        



    .. py:attribute:: ScanAdvancedOutput.FRONTCONNECTOR_MODULE9



        The switch module produces the Scan Advanced Output Trigger on the front
        connector module 9.

        



    .. py:attribute:: ScanAdvancedOutput.FRONTCONNECTOR_MODULE10



        The switch module produces the Scan Advanced Output Trigger on the front
        connector module 10.

        



    .. py:attribute:: ScanAdvancedOutput.FRONTCONNECTOR_MODULE11



        The switch module produces the Scan Advanced Output Trigger on the front
        connector module 11.

        



    .. py:attribute:: ScanAdvancedOutput.FRONTCONNECTOR_MODULE12



        The switch module produces the Scan Advanced Output Trigger on the front
        connector module 12.

        



ScanAdvancedPolarity
--------------------

.. py:class:: ScanAdvancedPolarity

    .. py:attribute:: ScanAdvancedPolarity.RISING



        The trigger occurs on the rising edge of the signal.

        



    .. py:attribute:: ScanAdvancedPolarity.FALLING



        The trigger occurs on the falling edge of the signal.

        



ScanMode
--------

.. py:class:: ScanMode

    .. py:attribute:: ScanMode.NONE



        No implicit action on connections when scanning.

        



    .. py:attribute:: ScanMode.BREAK_BEFORE_MAKE



        When scanning, the switch device breaks existing connections before  making new connections.

        



    .. py:attribute:: ScanMode.BREAK_AFTER_MAKE



        When scanning, the switch device breaks existing connections after making  new connections.

        



TriggerInput
------------

.. py:class:: TriggerInput

    .. py:attribute:: TriggerInput.IMMEDIATE



        Immediate Trigger. The switch device does not wait for a trigger before  processing the next entry in the scan list.

        



    .. py:attribute:: TriggerInput.EXTERNAL



        External Trigger. The switch device waits until it receives a trigger  from an external source through the external trigger input before  processing the next entry in the scan list.

        



    .. py:attribute:: TriggerInput.SOFTWARE_TRIG



        The switch device waits until you call the :py:meth:`niswitch.Session.send_software_trigger`  method before processing the next entry in the scan list.

        



    .. py:attribute:: TriggerInput.TTL0



        The switch device waits until it receives a trigger on the PXI TRIG0 line before processing the next entry in the scan list.

        



    .. py:attribute:: TriggerInput.TTL1



        The switch device waits until it receives a trigger on the PXI TRIG1 line before processing the next entry in the scan list.

        



    .. py:attribute:: TriggerInput.TTL2



        The switch device waits until it receives a trigger on the PXI TRIG2 line before processing the next entry in the scan list.

        



    .. py:attribute:: TriggerInput.TTL3



        The switch device waits until it receives a trigger on the PXI TRIG3 line before processing the next entry in the scan list.

        



    .. py:attribute:: TriggerInput.TTL4



        The switch device waits until it receives a trigger on the PXI TRIG4 line before processing the next entry in the scan list.

        



    .. py:attribute:: TriggerInput.TTL5



        The switch device waits until it receives a trigger on the PXI TRIG5 line before processing the next entry in the scan list.

        



    .. py:attribute:: TriggerInput.TTL6



        The switch device waits until it receives a trigger on the PXI TRIG6 line before processing the next entry in the scan list.

        



    .. py:attribute:: TriggerInput.TTL7



        The switch device waits until it receives a trigger on the PXI TRIG7 line before processing the next entry in the scan list.

        



    .. py:attribute:: TriggerInput.PXI_STAR



        The switch device waits until it receives a trigger on the PXI STAR  trigger bus before processing the next entry in the scan list.

        



    .. py:attribute:: TriggerInput.REARCONNECTOR



        The switch device waits until it receives a trigger on the  rear connector.

        



    .. py:attribute:: TriggerInput.FRONTCONNECTOR



        The switch device waits until it receives a trigger on the  front connector.

        



    .. py:attribute:: TriggerInput.REARCONNECTOR_MODULE1



        The switch module waits until it receives a trigger on the rear
        connector module 1.

        



    .. py:attribute:: TriggerInput.REARCONNECTOR_MODULE2



        The switch module waits until it receives a trigger on the rear
        connector module 2.

        



    .. py:attribute:: TriggerInput.REARCONNECTOR_MODULE3



        The switch module waits until it receives a trigger on the rear
        connector module 3.

        



    .. py:attribute:: TriggerInput.REARCONNECTOR_MODULE4



        The switch module waits until it receives a trigger on the rear
        connector module 4.

        



    .. py:attribute:: TriggerInput.REARCONNECTOR_MODULE5



        The switch module waits until it receives a trigger on the rear
        connector module 5.

        



    .. py:attribute:: TriggerInput.REARCONNECTOR_MODULE6



        The switch module waits until it receives a trigger on the rear
        connector module 6.

        



    .. py:attribute:: TriggerInput.REARCONNECTOR_MODULE7



        The switch module waits until it receives a trigger on the rear
        connector module 7.

        



    .. py:attribute:: TriggerInput.REARCONNECTOR_MODULE8



        The switch module waits until it receives a trigger on the rear
        connector module 8.

        



    .. py:attribute:: TriggerInput.REARCONNECTOR_MODULE9



        The switch module waits until it receives a trigger on the rear
        connector module 9.

        



    .. py:attribute:: TriggerInput.REARCONNECTOR_MODULE10



        The switch module waits until it receives a trigger on the rear
        connector module 10.

        



    .. py:attribute:: TriggerInput.REARCONNECTOR_MODULE11



        The switch module waits until it receives a trigger on the rear
        connector module 11.

        



    .. py:attribute:: TriggerInput.REARCONNECTOR_MODULE12



        The switch module waits until it receives a trigger on the rear
        connector module 12.

        



    .. py:attribute:: TriggerInput.FRONTCONNECTOR_MODULE1



        The switch module waits until it receives a trigger on the front
        connector module 1.

        



    .. py:attribute:: TriggerInput.FRONTCONNECTOR_MODULE2



        The switch module waits until it receives a trigger on the front
        connector module 2.

        



    .. py:attribute:: TriggerInput.FRONTCONNECTOR_MODULE3



        The switch module waits until it receives a trigger on the front
        connector module 3.

        



    .. py:attribute:: TriggerInput.FRONTCONNECTOR_MODULE4



        The switch module waits until it receives a trigger on the front
        connector module 4.

        



    .. py:attribute:: TriggerInput.FRONTCONNECTOR_MODULE5



        The switch module waits until it receives a trigger on the front
        connector module 5.

        



    .. py:attribute:: TriggerInput.FRONTCONNECTOR_MODULE6



        The switch module waits until it receives a trigger on the front
        connector module 6.

        



    .. py:attribute:: TriggerInput.FRONTCONNECTOR_MODULE7



        The switch module waits until it receives a trigger on the front
        connector module 7.

        



    .. py:attribute:: TriggerInput.FRONTCONNECTOR_MODULE8



        The switch module waits until it receives a trigger on the front
        connector module 8.

        



    .. py:attribute:: TriggerInput.FRONTCONNECTOR_MODULE9



        The switch module waits until it receives a trigger on the front
        connector module 9.

        



    .. py:attribute:: TriggerInput.FRONTCONNECTOR_MODULE10



        The switch module waits until it receives a trigger on the front
        connector module 10.

        



    .. py:attribute:: TriggerInput.FRONTCONNECTOR_MODULE11



        The switch module waits until it receives a trigger on the front
        connector module 11.

        



    .. py:attribute:: TriggerInput.FRONTCONNECTOR_MODULE12



        The switch module waits until it receives a trigger on the front
        connector module 12.

        



TriggerInputPolarity
--------------------

.. py:class:: TriggerInputPolarity

    .. py:attribute:: TriggerInputPolarity.RISING



        The trigger occurs on the rising edge of the signal.

        



    .. py:attribute:: TriggerInputPolarity.FALLING



        The trigger occurs on the falling edge of the signal.

        





