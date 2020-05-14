.. py:module:: niswitch

Session
=======

.. py:class:: Session(self, resource_name, topology="Configured Topology", simulate=False, reset_device=False)

    

    Returns a session handle used to identify the switch in all subsequent
    instrument driver calls and sets the topology of the switch.
    :py:meth:`niswitch.Session.__init__` creates a new IVI instrument driver session
    for the switch specified in the resourceName parameter. The driver uses
    the topology specified in the topology parameter and overrides the
    topology specified in MAX. Note: When initializing an NI SwitchBlock
    device with topology, you must specify the toplogy created when you
    configured the device in MAX, using either
    NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY or the toplogy string of the
    device. Refer to the Initializing with Toplogy for NI SwitchBlock
    Devices topic in the NI Switches Help for information about determining
    the topology string of an NI SwitchBlock device. By default, the switch
    is reset to a known state. Enable simulation by specifying the topology
    and setting the simulate parameter to True.

    



    :param resource_name:
        

        Resource name of the switch module to initialize. Default value: None
        Syntax: Optional fields are shown in square brackets ([]). Configured in
        MAX Under Valid Syntax Devices and Interfaces DeviceName Traditional
        NI-DAQ Devices SCXI[chassis ID]::slot number PXI System PXI[bus
        number]::device number TIP: IVI logical names are also valid for the
        resource name. Default values for optional fields: chassis ID = 1 bus
        number = 0 Example resource names: Resource Name Description SC1Mod3
        NI-DAQmx module in chassis "SC1" slot 3 MySwitch NI-DAQmx module renamed
        to "MySwitch" SCXI1::3 Traditional NI-DAQ module in chassis 1, slot 3
        SCXI::3 Traditional NI-DAQ module in chassis 1, slot 3 PXI0::16 PXI bus
        0, device number 16 PXI::16 PXI bus 0, device number 16

        


    :type resource_name: str

    :param topology:
        

        Pass the topology name you want to use for the switch you specify with
        Resource Name parameter. You can also pass
        NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY to use the last topology that
        was configured for the device in MAX. Default Value:
        NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY Valid Values:
        NISWITCH_TOPOLOGY_1127_1_WIRE_64X1_MUX
        NISWITCH_TOPOLOGY_1127_2_WIRE_32X1_MUX
        NISWITCH_TOPOLOGY_1127_2_WIRE_4X8_MATRIX
        NISWITCH_TOPOLOGY_1127_4_WIRE_16X1_MUX
        NISWITCH_TOPOLOGY_1127_INDEPENDENT
        NISWITCH_TOPOLOGY_1128_1_WIRE_64X1_MUX
        NISWITCH_TOPOLOGY_1128_2_WIRE_32X1_MUX
        NISWITCH_TOPOLOGY_1128_2_WIRE_4X8_MATRIX
        NISWITCH_TOPOLOGY_1128_4_WIRE_16X1_MUX
        NISWITCH_TOPOLOGY_1128_INDEPENDENT
        NISWITCH_TOPOLOGY_1129_2_WIRE_16X16_MATRIX
        NISWITCH_TOPOLOGY_1129_2_WIRE_8X32_MATRIX
        NISWITCH_TOPOLOGY_1129_2_WIRE_4X64_MATRIX
        NISWITCH_TOPOLOGY_1129_2_WIRE_DUAL_8X16_MATRIX
        NISWITCH_TOPOLOGY_1129_2_WIRE_DUAL_4X32_MATRIX
        NISWITCH_TOPOLOGY_1129_2_WIRE_QUAD_4X16_MATRIX
        NISWITCH_TOPOLOGY_1130_1_WIRE_256X1_MUX
        NISWITCH_TOPOLOGY_1130_1_WIRE_DUAL_128X1_MUX
        NISWITCH_TOPOLOGY_1130_1_WIRE_4X64_MATRIX
        NISWITCH_TOPOLOGY_1130_1_WIRE_8x32_MATRIX
        NISWITCH_TOPOLOGY_1130_1_WIRE_OCTAL_32X1_MUX
        NISWITCH_TOPOLOGY_1130_1_WIRE_QUAD_64X1_MUX
        NISWITCH_TOPOLOGY_1130_1_WIRE_SIXTEEN_16X1_MUX
        NISWITCH_TOPOLOGY_1130_2_WIRE_4X32_MATRIX
        NISWITCH_TOPOLOGY_1130_2_WIRE_128X1_MUX
        NISWITCH_TOPOLOGY_1130_2_WIRE_OCTAL_16X1_MUX
        NISWITCH_TOPOLOGY_1130_2_WIRE_QUAD_32X1_MUX
        NISWITCH_TOPOLOGY_1130_4_WIRE_64X1_MUX
        NISWITCH_TOPOLOGY_1130_4_WIRE_QUAD_16X1_MUX
        NISWITCH_TOPOLOGY_1130_INDEPENDENT NISWITCH_TOPOLOGY_1160_16_SPDT
        NISWITCH_TOPOLOGY_1161_8_SPDT
        NISWITCH_TOPOLOGY_1163R_OCTAL_4X1_MUX
        NISWITCH_TOPOLOGY_1166_16_DPDT NISWITCH_TOPOLOGY_1166_32_SPDT
        NISWITCH_TOPOLOGY_1167_INDEPENDENT
        NISWITCH_TOPOLOGY_1169_100_SPST NISWITCH_TOPOLOGY_1169_50_DPST
        NISWITCH_TOPOLOGY_1175_1_WIRE_196X1_MUX
        NISWITCH_TOPOLOGY_1175_2_WIRE_98X1_MUX
        NISWITCH_TOPOLOGY_1175_2_WIRE_95X1_MUX
        NISWITCH_TOPOLOGY_1190_QUAD_4X1_MUX
        NISWITCH_TOPOLOGY_1191_QUAD_4X1_MUX
        NISWITCH_TOPOLOGY_1192_8_SPDT NISWITCH_TOPOLOGY_1193_32X1_MUX
        NISWITCH_TOPOLOGY_1193_16X1_TERMINATED_MUX
        NISWITCH_TOPOLOGY_1193_DUAL_16X1_MUX
        NISWITCH_TOPOLOGY_1193_DUAL_8X1_TERMINATED_MUX
        NISWITCH_TOPOLOGY_1193_QUAD_8X1_MUX
        NISWITCH_TOPOLOGY_1193_QUAD_4X1_TERMINATED_MUX
        NISWITCH_TOPOLOGY_1193_INDEPENDENT
        NISWITCH_TOPOLOGY_1194_QUAD_4X1_MUX
        NISWITCH_TOPOLOGY_1195_QUAD_4X1_MUX
        NISWITCH_TOPOLOGY_2501_1_WIRE_48X1_MUX
        NISWITCH_TOPOLOGY_2501_1_WIRE_48X1_AMPLIFIED_MUX
        NISWITCH_TOPOLOGY_2501_2_WIRE_24X1_MUX
        NISWITCH_TOPOLOGY_2501_2_WIRE_24X1_AMPLIFIED_MUX
        NISWITCH_TOPOLOGY_2501_2_WIRE_DUAL_12X1_MUX
        NISWITCH_TOPOLOGY_2501_2_WIRE_QUAD_6X1_MUX
        NISWITCH_TOPOLOGY_2501_2_WIRE_4X6_MATRIX
        NISWITCH_TOPOLOGY_2501_4_WIRE_12X1_MUX
        NISWITCH_TOPOLOGY_2503_1_WIRE_48X1_MUX
        NISWITCH_TOPOLOGY_2503_2_WIRE_24X1_MUX
        NISWITCH_TOPOLOGY_2503_2_WIRE_DUAL_12X1_MUX
        NISWITCH_TOPOLOGY_2503_2_WIRE_QUAD_6X1_MUX
        NISWITCH_TOPOLOGY_2503_2_WIRE_4X6_MATRIX
        NISWITCH_TOPOLOGY_2503_4_WIRE_12X1_MUX
        NISWITCH_TOPOLOGY_2510_INDEPENDENT
        NISWITCH_TOPOLOGY_2512_INDEPENDENT
        NISWITCH_TOPOLOGY_2514_INDEPENDENT
        NISWITCH_TOPOLOGY_2515_INDEPENDENT NISWITCH_TOPOLOGY_2520_80_SPST
        NISWITCH_TOPOLOGY_2521_40_DPST NISWITCH_TOPOLOGY_2522_53_SPDT
        NISWITCH_TOPOLOGY_2523_26_DPDT
        NISWITCH_TOPOLOGY_2524_1_WIRE_128X1_MUX
        NISWITCH_TOPOLOGY_2524_1_WIRE_DUAL_64X1_MUX
        NISWITCH_TOPOLOGY_2524_1_WIRE_QUAD_32X1_MUX
        NISWITCH_TOPOLOGY_2524_1_WIRE_OCTAL_16X1_MUX
        NISWITCH_TOPOLOGY_2524_1_WIRE_SIXTEEN_8X1_MUX
        NISWITCH_TOPOLOGY_2525_2_WIRE_64X1_MUX
        NISWITCH_TOPOLOGY_2525_2_WIRE_DUAL_32X1_MUX
        NISWITCH_TOPOLOGY_2525_2_WIRE_QUAD_16X1_MUX
        NISWITCH_TOPOLOGY_2525_2_WIRE_OCTAL_8X1_MUX
        NISWITCH_TOPOLOGY_2525_2_WIRE_SIXTEEN_4X1_MUX
        NISWITCH_TOPOLOGY_2526_1_WIRE_158X1_MUX
        NISWITCH_TOPOLOGY_2526_2_WIRE_79X1_MUX
        NISWITCH_TOPOLOGY_2527_1_WIRE_64X1_MUX
        NISWITCH_TOPOLOGY_2527_1_WIRE_DUAL_32X1_MUX
        NISWITCH_TOPOLOGY_2527_2_WIRE_32X1_MUX
        NISWITCH_TOPOLOGY_2527_2_WIRE_DUAL_16X1_MUX
        NISWITCH_TOPOLOGY_2527_4_WIRE_16X1_MUX
        NISWITCH_TOPOLOGY_2527_INDEPENDENT
        NISWITCH_TOPOLOGY_2529_2_WIRE_DUAL_4X16_MATRIX
        NISWITCH_TOPOLOGY_2529_2_WIRE_8X16_MATRIX
        NISWITCH_TOPOLOGY_2529_2_WIRE_4X32_MATRIX
        NISWITCH_TOPOLOGY_2530_1_WIRE_128X1_MUX
        NISWITCH_TOPOLOGY_2530_1_WIRE_DUAL_64X1_MUX
        NISWITCH_TOPOLOGY_2530_1_WIRE_4x32_MATRIX
        NISWITCH_TOPOLOGY_2530_1_WIRE_8x16_MATRIX
        NISWITCH_TOPOLOGY_2530_1_WIRE_OCTAL_16X1_MUX
        NISWITCH_TOPOLOGY_2530_1_WIRE_QUAD_32X1_MUX
        NISWITCH_TOPOLOGY_2530_2_WIRE_4x16_MATRIX
        NISWITCH_TOPOLOGY_2530_2_WIRE_64X1_MUX
        NISWITCH_TOPOLOGY_2530_2_WIRE_DUAL_32X1_MUX
        NISWITCH_TOPOLOGY_2530_2_WIRE_QUAD_16X1_MUX
        NISWITCH_TOPOLOGY_2530_4_WIRE_32X1_MUX
        NISWITCH_TOPOLOGY_2530_4_WIRE_DUAL_16X1_MUX
        NISWITCH_TOPOLOGY_2530_INDEPENDENT
        NISWITCH_TOPOLOGY_2531_1_WIRE_4X128_MATRIX
        NISWITCH_TOPOLOGY_2531_1_WIRE_8X64_MATRIX
        NISWITCH_TOPOLOGY_2531_1_WIRE_DUAL_4X64_MATRIX
        NISWITCH_TOPOLOGY_2531_1_WIRE_DUAL_8X32_MATRIX
        NISWITCH_TOPOLOGY_2531_2_WIRE_4X64_MATRIX
        NISWITCH_TOPOLOGY_2531_2_WIRE_8X32_MATRIX
        NISWITCH_TOPOLOGY_2532_1_WIRE_16X32_MATRIX
        NISWITCH_TOPOLOGY_2532_1_WIRE_4X128_MATRIX
        NISWITCH_TOPOLOGY_2532_1_WIRE_8X64_MATRIX
        NISWITCH_TOPOLOGY_2532_1_WIRE_DUAL_16X16_MATRIX
        NISWITCH_TOPOLOGY_2532_1_WIRE_DUAL_4X64_MATRIX
        NISWITCH_TOPOLOGY_2532_1_WIRE_DUAL_8X32_MATRIX
        NISWITCH_TOPOLOGY_2532_1_WIRE_SIXTEEN_2X16_MATRIX
        NISWITCH_TOPOLOGY_2532_2_WIRE_16X16_MATRIX
        NISWITCH_TOPOLOGY_2532_2_WIRE_4X64_MATRIX
        NISWITCH_TOPOLOGY_2532_2_WIRE_8X32_MATRIX
        NISWITCH_TOPOLOGY_2532_2_WIRE_DUAL_4X32_MATRIX
        NISWITCH_TOPOLOGY_2533_1_WIRE_4X64_MATRIX
        NISWITCH_TOPOLOGY_2534_1_WIRE_8X32_MATRIX
        NISWITCH_TOPOLOGY_2535_1_WIRE_4X136_MATRIX
        NISWITCH_TOPOLOGY_2536_1_WIRE_8X68_MATRIX
        NISWITCH_TOPOLOGY_2540_1_WIRE_8X9_MATRIX
        NISWITCH_TOPOLOGY_2541_1_WIRE_8X12_MATRIX
        NISWITCH_TOPOLOGY_2542_QUAD_2X1_TERMINATED_MUX
        NISWITCH_TOPOLOGY_2543_DUAL_4X1_TERMINATED_MUX
        NISWITCH_TOPOLOGY_2544_8X1_TERMINATED_MUX
        NISWITCH_TOPOLOGY_2545_4X1_TERMINATED_MUX
        NISWITCH_TOPOLOGY_2546_DUAL_4X1_MUX
        NISWITCH_TOPOLOGY_2547_8X1_MUX NISWITCH_TOPOLOGY_2548_4_SPDT
        NISWITCH_TOPOLOGY_2549_TERMINATED_2_SPDT
        NISWITCH_TOPOLOGY_2554_4X1_MUX
        NISWITCH_TOPOLOGY_2555_4X1_TERMINATED_MUX
        NISWITCH_TOPOLOGY_2556_DUAL_4X1_MUX
        NISWITCH_TOPOLOGY_2557_8X1_MUX NISWITCH_TOPOLOGY_2558_4_SPDT
        NISWITCH_TOPOLOGY_2559_TERMINATED_2_SPDT
        NISWITCH_TOPOLOGY_2564_16_SPST NISWITCH_TOPOLOGY_2564_8_DPST
        NISWITCH_TOPOLOGY_2565_16_SPST NISWITCH_TOPOLOGY_2566_16_SPDT
        NISWITCH_TOPOLOGY_2566_8_DPDT NISWITCH_TOPOLOGY_2567_INDEPENDENT
        NISWITCH_TOPOLOGY_2568_15_DPST NISWITCH_TOPOLOGY_2568_31_SPST
        NISWITCH_TOPOLOGY_2569_100_SPST NISWITCH_TOPOLOGY_2569_50_DPST
        NISWITCH_TOPOLOGY_2570_20_DPDT NISWITCH_TOPOLOGY_2570_40_SPDT
        NISWITCH_TOPOLOGY_2571_66_SPDT
        NISWITCH_TOPOLOGY_2575_1_WIRE_196X1_MUX
        NISWITCH_TOPOLOGY_2575_2_WIRE_98X1_MUX
        NISWITCH_TOPOLOGY_2575_2_WIRE_95X1_MUX
        NISWITCH_TOPOLOGY_2576_2_WIRE_64X1_MUX
        NISWITCH_TOPOLOGY_2576_2_WIRE_DUAL_32X1_MUX
        NISWITCH_TOPOLOGY_2576_2_WIRE_OCTAL_8X1_MUX
        NISWITCH_TOPOLOGY_2576_2_WIRE_QUAD_16X1_MUX
        NISWITCH_TOPOLOGY_2576_2_WIRE_SIXTEEN_4X1_MUX
        NISWITCH_TOPOLOGY_2576_INDEPENDENT
        NISWITCH_TOPOLOGY_2584_1_WIRE_12X1_MUX
        NISWITCH_TOPOLOGY_2584_1_WIRE_DUAL_6X1_MUX
        NISWITCH_TOPOLOGY_2584_2_WIRE_6X1_MUX
        NISWITCH_TOPOLOGY_2584_INDEPENDENT
        NISWITCH_TOPOLOGY_2585_1_WIRE_10X1_MUX
        NISWITCH_TOPOLOGY_2586_10_SPST NISWITCH_TOPOLOGY_2586_5_DPST
        NISWITCH_TOPOLOGY_2590_4X1_MUX NISWITCH_TOPOLOGY_2591_4X1_MUX
        NISWITCH_TOPOLOGY_2593_16X1_MUX
        NISWITCH_TOPOLOGY_2593_8X1_TERMINATED_MUX
        NISWITCH_TOPOLOGY_2593_DUAL_8X1_MUX
        NISWITCH_TOPOLOGY_2593_DUAL_4X1_TERMINATED_MUX
        NISWITCH_TOPOLOGY_2593_INDEPENDENT NISWITCH_TOPOLOGY_2594_4X1_MUX
        NISWITCH_TOPOLOGY_2595_4X1_MUX
        NISWITCH_TOPOLOGY_2596_DUAL_6X1_MUX
        NISWITCH_TOPOLOGY_2597_6X1_TERMINATED_MUX
        NISWITCH_TOPOLOGY_2598_DUAL_TRANSFER
        NISWITCH_TOPOLOGY_2599_2_SPDT NISWITCH_TOPOLOGY_2720_INDEPENDENT
        NISWITCH_TOPOLOGY_2722_INDEPENDENT
        NISWITCH_TOPOLOGY_2725_INDEPENDENT
        NISWITCH_TOPOLOGY_2727_INDEPENDENT
        NISWITCH_TOPOLOGY_2737_2_WIRE_4X64_MATRIX
        NISWITCH_TOPOLOGY_2738_2_WIRE_8X32_MATRIX
        NISWITCH_TOPOLOGY_2739_2_WIRE_16X16_MATRIX
        NISWITCH_TOPOLOGY_2746_QUAD_4X1_MUX
        NISWITCH_TOPOLOGY_2747_DUAL_8X1_MUX
        NISWITCH_TOPOLOGY_2748_16X1_MUX
        NISWITCH_TOPOLOGY_2790_INDEPENDENT
        NISWITCH_TOPOLOGY_2796_DUAL_6X1_MUX
        NISWITCH_TOPOLOGY_2797_6X1_TERMINATED_MUX
        NISWITCH_TOPOLOGY_2798_DUAL_TRANSFER
        NISWITCH_TOPOLOGY_2799_2_SPDT

        


    :type topology: str

    :param simulate:
        

        Enables simulation of the switch module specified in the resource name
        parameter. Valid Values: True - simulate False - Don't simulate
        (Default Value)

        


    :type simulate: bool

    :param reset_device:
        

        Specifies whether to reset the switch module during the initialization
        process. Valid Values: True - Reset Device (Default Value) False
        - Currently unsupported. The device will not reset.

        


    :type reset_device: bool


Methods
=======

abort
-----

    .. py:currentmodule:: niswitch.Session

    .. py:method:: abort()

            Aborts the scan in progress. Initiate a scan with
            :py:meth:`niswitch.Session.initiate`. If the switch module is not scanning,
            NISWITCH_ERROR_NO_SCAN_IN_PROGRESS error is returned.

            



can_connect
-----------

    .. py:currentmodule:: niswitch.Session

    .. py:method:: can_connect(channel1, channel2)

            Verifies that a path between channel 1 and channel 2 can be created. If
            a path is possible in the switch module, the availability of that path
            is returned given the existing connections. If the path is possible but
            in use, a NISWITCH_WARN_IMPLICIT_CONNECTION_EXISTS warning is
            returned.

            



            :param channel1:


                Input one of the channel names of the desired path. Pass the other
                channel name as the channel 2 parameter. Refer to Devices Overview for
                valid channel names for the switch module. Examples of valid channel
                names: ch0, com0, ab0, r1, c2, cjtemp Default value: ""

                


            :type channel1: str
            :param channel2:


                Input one of the channel names of the desired path. Pass the other
                channel name as the channel 1 parameter. Refer to Devices Overview for
                valid channel names for the switch module. Examples of valid channel
                names: ch0, com0, ab0, r1, c2, cjtemp Default value: ""

                


            :type channel2: str

            :rtype: :py:data:`niswitch.PathCapability`
            :return:


                    Indicates whether a path is valid. Possible values include:

                    - :py:data:`~niswitch.PathCapability.PATH_AVAILABLE` 1
                    - :py:data:`~niswitch.PathCapability.PATH_EXISTS` 2
                    - :py:data:`~niswitch.PathCapability.PATH_UNSUPPORTED` 3
                    - :py:data:`~niswitch.PathCapability.RESOURCE_IN_USE` 4
                    - :py:data:`~niswitch.PathCapability.SOURCE_CONFLICT` 5
                    - :py:data:`~niswitch.PathCapability.CHANNEL_NOT_AVAILABLE` 6

                    Notes: (1)
                    :py:data:`~niswitch.PathCapability.PATH_AVAILABLE` indicates that the driver can create the
                    path at this time. (2) :py:data:`~niswitch.PathCapability.PATH_EXISTS` indicates that the
                    path already exists. (3) :py:data:`~niswitch.PathCapability.PATH_UNSUPPORTED` indicates that
                    the instrument is not capable of creating a path between the channels
                    you specify. (4) :py:data:`~niswitch.PathCapability.RESOURCE_IN_USE` indicates that although
                    the path is valid, the driver cannot create the path at this moment
                    because the switch device is currently using one or more of the required
                    channels to create another path. You must destroy the other path before
                    creating this one. (5) :py:data:`~niswitch.PathCapability.SOURCE_CONFLICT` indicates that
                    the instrument cannot create a path because both channels are connected
                    to a different source channel. (6)
                    :py:data:`~niswitch.PathCapability.CHANNEL_NOT_AVAILABLE` indicates that the driver cannot
                    create a path between the two channels because one of the channels is a
                    configuration channel and thus unavailable for external connections.

                    



close
-----

    .. py:currentmodule:: niswitch.Session

    .. py:method:: close()

            Terminates the NI-SWITCH session and all of its properties and
            deallocates any memory resources the driver uses. Notes: (1) You must
            unlock the session before calling :py:meth:`niswitch.Session._close`. (2) After calling
            :py:meth:`niswitch.Session._close`, you cannot use the instrument driver again until you
            call :py:meth:`niswitch.Session.init` or :py:meth:`niswitch.Session.InitWithOptions`.

            

            .. note:: One or more of the referenced methods are not in the Python API for this driver.

            .. note:: This method is not needed when using the session context manager



commit
------

    .. py:currentmodule:: niswitch.Session

    .. py:method:: commit()

            Downloads the configured scan list and trigger settings to hardware.
            Calling :py:meth:`niswitch.Session.commit` optional as it is implicitly called during
            :py:meth:`niswitch.Session.initiate`. Use :py:meth:`niswitch.Session.commit` to arm triggers in a given
            order or to control when expensive hardware operations are performed.

            



connect
-------

    .. py:currentmodule:: niswitch.Session

    .. py:method:: connect(channel1, channel2)

            Creates a path between channel 1 and channel 2. The driver calculates
            and uses the shortest path between the two channels. Refer to Immediate
            Operations for information about Channel Usage types. If a path is not
            available, the method returns one of the following errors: -
            NISWITCH_ERROR_EXPLICIT_CONNECTION_EXISTS, if the two channels are
            already explicitly connected by calling either the :py:meth:`niswitch.Session.connect` or
            :py:meth:`niswitch.Session.set_path` method. -
            NISWITCH_ERROR_IS_CONFIGURATION_CHANNEL, if a channel is a
            configuration channel. Error elaboration contains information about
            which of the two channels is a configuration channel. -
            NISWITCH_ERROR_ATTEMPT_TO_CONNECT_SOURCES, if both channels are
            connected to a different source. Error elaboration contains information
            about sources channel 1 and 2 connect to. -
            NISWITCH_ERROR_CANNOT_CONNECT_TO_ITSELF, if channels 1 and 2 are
            one and the same channel. - NISWITCH_ERROR_PATH_NOT_FOUND, if the
            driver cannot find a path between the two channels. Note: Paths are
            bidirectional. For example, if a path exists between channels CH1 and
            CH2, then the path also exists between channels CH2 and CH1.

            



            :param channel1:


                Input one of the channel names of the desired path. Pass the other
                channel name as the channel 2 parameter. Refer to Devices Overview for
                valid channel names for the switch module. Examples of valid channel
                names: ch0, com0, ab0, r1, c2, cjtemp Default value: None

                


            :type channel1: str
            :param channel2:


                Input one of the channel names of the desired path. Pass the other
                channel name as the channel 1 parameter. Refer to Devices Overview for
                valid channel names for the switch module. Examples of valid channel
                names: ch0, com0, ab0, r1, c2, cjtemp Default value: None

                


            :type channel2: str

connect_multiple
----------------

    .. py:currentmodule:: niswitch.Session

    .. py:method:: connect_multiple(connection_list)

            Creates the connections between channels specified in Connection List.
            Specify connections with two endpoints only or the explicit path between
            two endpoints. NI-SWITCH calculates and uses the shortest path between
            the channels. Refer to Setting Source and Configuration Channels for
            information about channel usage types. In the event of an error,
            connecting stops at the point in the list where the error occurred. If a
            path is not available, the method returns one of the following errors:
            - NISWITCH_ERROR_EXPLICIT_CONNECTION_EXISTS, if the two channels are
            already explicitly connected. -
            NISWITCH_ERROR_IS_CONFIGURATION_CHANNEL, if a channel is a
            configuration channel. Error elaboration contains information about
            which of the two channels is a configuration channel. -
            NISWITCH_ERROR_ATTEMPT_TO_CONNECT_SOURCES, if both channels are
            connected to a different source. Error elaboration contains information
            about sources channel 1 and 2 to connect. -
            NISWITCH_ERROR_CANNOT_CONNECT_TO_ITSELF, if channels 1 and 2 are
            one and the same channel. - NISWITCH_ERROR_PATH_NOT_FOUND, if the
            driver cannot find a path between the two channels. Note: Paths are
            bidirectional. For example, if a path exists between channels ch1 and
            ch2, then the path also exists between channels ch1 and ch2.

            



            :param connection_list:


                Connection List specifies a list of connections between channels to
                make. NI-SWITCH validates the connection list, and aborts execution of
                the list if errors are returned. Refer to Connection and Disconnection
                List Syntax for valid connection list syntax and examples. Refer to
                Devices Overview for valid channel names for the switch module. Example
                of a valid connection list: c0 -> r1, [c2 -> r2 -> c3] In this example,
                r2 is a configuration channel. Default value: None

                


            :type connection_list: str

disable
-------

    .. py:currentmodule:: niswitch.Session

    .. py:method:: disable()

            Places the switch module in a quiescent state where it has minimal or no
            impact on the system to which it is connected. All channels are
            disconnected and any scan in progress is aborted.

            



disconnect
----------

    .. py:currentmodule:: niswitch.Session

    .. py:method:: disconnect(channel1, channel2)

            This method destroys the path between two channels that you create
            with the :py:meth:`niswitch.Session.connect` or :py:meth:`niswitch.Session.set_path` method. If a path is
            not connected or not available, the method returns the
            IVISWTCH_ERROR_NO_SUCH_PATH error.

            



            :param channel1:


                Input one of the channel names of the path to break. Pass the other
                channel name as the channel 2 parameter. Refer to Devices Overview for
                valid channel names for the switch module. Examples of valid channel
                names: ch0, com0, ab0, r1, c2, cjtemp Default value: None

                


            :type channel1: str
            :param channel2:


                Input one of the channel names of the path to break. Pass the other
                channel name as the channel 1 parameter. Refer to Devices Overview for
                valid channel names for the switch module. Examples of valid channel
                names: ch0, com0, ab0, r1, c2, cjtemp Default value: None

                


            :type channel2: str

disconnect_all
--------------

    .. py:currentmodule:: niswitch.Session

    .. py:method:: disconnect_all()

            Breaks all existing paths. If the switch module cannot break all paths,
            NISWITCH_WARN_PATH_REMAINS warning is returned.

            



disconnect_multiple
-------------------

    .. py:currentmodule:: niswitch.Session

    .. py:method:: disconnect_multiple(disconnection_list)

            Breaks the connections between channels specified in Disconnection List.
            If no connections exist between channels, NI-SWITCH returns an error. In
            the event of an error, the VI stops at the point in the list where the
            error occurred.

            



            :param disconnection_list:


                Disconnection List specifies a list of connections between channels to
                break. NI-SWITCH validates the disconnection list, and aborts execution
                of the list if errors are returned. Refer to Connection and
                Disconnection List Syntax for valid disconnection list syntax and
                examples. Refer to Devices Overview for valid channel names for the
                switch module. Example of a valid disconnection list: c0 -> r1, [c2 ->
                r2 -> c3] In this example, r2 is a configuration channel. Default value:
                None

                


            :type disconnection_list: str

get_channel_name
----------------

    .. py:currentmodule:: niswitch.Session

    .. py:method:: get_channel_name(index)

            Returns the channel string that is in the channel table at the specified
            index. Use :py:meth:`niswitch.Session.get_channel_name` in a For Loop to get a complete list
            of valid channel names for the switch module. Use the Channel Count
            property to determine the number of channels.

            



            :param index:


                A 1-based index into the channel table. Default value: 1 Maximum value:
                Value of Channel Count property.

                


            :type index: int

            :rtype: str
            :return:


                    Returns the channel name that is in the channel table at the index you
                    specify.

                    



get_path
--------

    .. py:currentmodule:: niswitch.Session

    .. py:method:: get_path(channel1, channel2)

            Returns a string that identifies the explicit path created with
            :py:meth:`niswitch.Session.connect`. Pass this string to :py:meth:`niswitch.Session.set_path` to establish
            the exact same path in future connections. In some cases, multiple paths
            are available between two channels. When you call :py:meth:`niswitch.Session.connect`, the
            driver selects an available path. With :py:meth:`niswitch.Session.connect`, there is no
            guarantee that the driver selected path will always be the same path
            through the switch module. :py:meth:`niswitch.Session.get_path` only returns those paths
            explicitly created by niSwitch Connect Channels or :py:meth:`niswitch.Session.set_path`.
            For example, if you connect channels CH1 and CH3,and then channels CH2
            and CH3, an explicit path between channels CH1 and CH2 does not exist an
            error is returned

            



            :param channel1:


                Input one of the channel names of the desired path. Pass the other
                channel name as the channel 2 parameter. Refer to Devices Overview for
                valid channel names for the switch module. Examples of valid channel
                names: ch0, com0, ab0, r1, c2, cjtemp Default value: ""

                


            :type channel1: str
            :param channel2:


                Input one of the channel names of the desired path. Pass the other
                channel name as the channel 1 parameter. Refer to Devices Overview for
                valid channel names for the switch module. Examples of valid channel
                names: ch0, com0, ab0, r1, c2, cjtemp Default value: ""

                


            :type channel2: str

            :rtype: str
            :return:


                    A string composed of comma-separated paths between channel 1 and channel
                    2. The first and last names in the path are the endpoints of the path.
                    All other channels in the path are configuration channels. Examples of
                    returned paths: ch0->com0, com0->ab0

                    



get_relay_count
---------------

    .. py:currentmodule:: niswitch.Session

    .. py:method:: get_relay_count(relay_name)

            Returns the number of times the relay has changed from Closed to Open.
            Relay count is useful for tracking relay lifetime and usage. Call
            :py:meth:`niswitch.Session.wait_for_debounce` before :py:meth:`niswitch.Session.get_relay_count` to ensure an
            accurate count. Refer to the Relay Count topic in the NI Switches Help
            to determine if the switch module supports relay counting.

            



            :param relay_name:


                Name of the relay. Default value: None Examples of valid relay names:
                ch0, ab0, 1wire, hlselect Refer to Devices Overview for a list of valid
                relay names for the switch module.

                


            :type relay_name: str

            :rtype: int
            :return:


                    The number of relay cycles.

                    



get_relay_name
--------------

    .. py:currentmodule:: niswitch.Session

    .. py:method:: get_relay_name(index)

            Returns the relay name string that is in the relay list at the specified
            index. Use :py:meth:`niswitch.Session.get_relay_name` in a For Loop to get a complete list
            of valid relay names for the switch module. Use the Number of Relays
            property to determine the number of relays.

            



            :param index:


                A 1-based index into the channel table. Default value: 1 Maximum value:
                Value of Channel Count property.

                


            :type index: int

            :rtype: str
            :return:


                    Returns the relay name for the index you specify.

                    



get_relay_position
------------------

    .. py:currentmodule:: niswitch.Session

    .. py:method:: get_relay_position(relay_name)

            Returns the relay position for the relay specified in the Relay Name
            parameter.

            



            :param relay_name:


                Name of the relay. Default value: None Examples of valid relay names:
                ch0, ab0, 1wire, hlselect Refer to Devices Overview for a list of valid
                relay names for the switch module.

                


            :type relay_name: str

            :rtype: :py:data:`niswitch.RelayPosition`
            :return:


                    Indicates whether the relay is open or closed. :py:data:`~niswitch.RelayPosition.OPEN` 10
                    :py:data:`~niswitch.RelayPosition.CLOSED` 11

                    



initiate
--------

    .. py:currentmodule:: niswitch.Session

    .. py:method:: initiate()

            Commits the configured scan list and trigger settings to hardware and
            initiates the scan. If niSwitch Commit was called earlier, niSwitch
            Initiate Scan only initiates the scan and returns immediately. Once the
            scanning operation begins, you cannot perform any other operation other
            than GetAttribute, AbortScan, or SendSoftwareTrigger. All other
            methods return NISWITCH_ERROR_SCAN_IN_PROGRESS. To stop the
            scanning operation, To stop the scanning operation, call
            :py:meth:`niswitch.Session.abort`.

            

            .. note:: This method will return a Python context manager that will initiate on entering and abort on exit.



lock
----

    .. py:currentmodule:: niswitch.Session

.. py:method:: lock()

    Obtains a multithread lock on the device session. Before doing so, the
    software waits until all other execution threads release their locks
    on the device session.

    Other threads may have obtained a lock on this session for the
    following reasons:

        -  The application called the :py:meth:`niswitch.Session.lock` method.
        -  A call to NI-SWITCH locked the session.
        -  After a call to the :py:meth:`niswitch.Session.lock` method returns
           successfully, no other threads can access the device session until
           you call the :py:meth:`niswitch.Session.unlock` method or exit out of the with block when using
           lock context manager.
        -  Use the :py:meth:`niswitch.Session.lock` method and the
           :py:meth:`niswitch.Session.unlock` method around a sequence of calls to
           instrument driver methods if you require that the device retain its
           settings through the end of the sequence.

    You can safely make nested calls to the :py:meth:`niswitch.Session.lock` method
    within the same thread. To completely unlock the session, you must
    balance each call to the :py:meth:`niswitch.Session.lock` method with a call to
    the :py:meth:`niswitch.Session.unlock` method.

    One method for ensuring there are the same number of unlock method calls as there is lock calls
    is to use lock as a context manager

        .. code:: python

            with niswitch.Session('dev1') as session:
                with session.lock():
                    # Calls to session within a single lock context

        The first `with` block ensures the session is closed regardless of any exceptions raised

        The second `with` block ensures that unlock is called regardless of any exceptions raised

    :rtype: context manager
    :return:
        When used in a `with` statement, :py:meth:`niswitch.Session.lock` acts as
        a context manager and unlock will be called when the `with` block is exited


relay_control
-------------

    .. py:currentmodule:: niswitch.Session

    .. py:method:: relay_control(relay_name, relay_action)

            Controls individual relays of the switch. When controlling individual
            relays, the protection offered by setting the usage of source channels
            and configuration channels, and by enabling or disabling analog bus
            sharing on the NI SwitchBlock, does not apply. Refer to the device book
            for your switch in the NI Switches Help to determine if the switch
            supports individual relay control.

            



            :param relay_name:


                Name of the relay. Default value: None Examples of valid relay names:
                ch0, ab0, 1wire, hlselect Refer to Devices Overview for a list of valid
                relay names for the switch module.

                


            :type relay_name: str
            :param relay_action:


                Specifies whether to open or close a given relay. Default value: Relay
                Close Defined values: :py:data:`~niswitch.RelayAction.OPEN`
                :py:data:`~niswitch.RelayAction.CLOSE` (Default Value)

                


            :type relay_action: :py:data:`niswitch.RelayAction`

reset
-----

    .. py:currentmodule:: niswitch.Session

    .. py:method:: reset()

            Disconnects all created paths and returns the switch module to the state
            at initialization. Configuration channel and source channel settings
            remain unchanged.

            



reset_with_defaults
-------------------

    .. py:currentmodule:: niswitch.Session

    .. py:method:: reset_with_defaults()

            Resets the switch module and applies initial user specified settings
            from the logical name used to initialize the session. If the session was
            created without a logical name, this method is equivalent to
            :py:meth:`niswitch.Session.reset`.

            



route_scan_advanced_output
--------------------------

    .. py:currentmodule:: niswitch.Session

    .. py:method:: route_scan_advanced_output(scan_advanced_output_connector, scan_advanced_output_bus_line, invert=False)

            Routes the scan advanced output trigger from a trigger bus line (TTLx)
            to the front or rear connector.

            



            :param scan_advanced_output_connector:


                The scan advanced trigger destination. Valid locations are the
                :py:data:`~niswitch.ScanAdvancedOutput.FRONTCONNECTOR` and :py:data:`~niswitch.ScanAdvancedOutput.REARCONNECTOR`. Default
                value: :py:data:`~niswitch.ScanAdvancedOutput.FRONTCONNECTOR`

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type scan_advanced_output_connector: :py:data:`niswitch.ScanAdvancedOutput`
            :param scan_advanced_output_bus_line:


                The trigger line to route the scan advanced output trigger from the
                front or rear connector. Select :py:data:`~niswitch.ScanAdvancedOutput.NONE` to break an existing
                route. Default value: None Valid Values: :py:data:`~niswitch.ScanAdvancedOutput.NONE`
                :py:data:`~niswitch.ScanAdvancedOutput.TTL0` :py:data:`~niswitch.ScanAdvancedOutput.TTL1` :py:data:`~niswitch.ScanAdvancedOutput.TTL2`
                :py:data:`~niswitch.ScanAdvancedOutput.TTL3` :py:data:`~niswitch.ScanAdvancedOutput.TTL4` :py:data:`~niswitch.ScanAdvancedOutput.TTL5`
                :py:data:`~niswitch.ScanAdvancedOutput.TTL6` :py:data:`~niswitch.ScanAdvancedOutput.TTL7`

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type scan_advanced_output_bus_line: :py:data:`niswitch.ScanAdvancedOutput`
            :param invert:


                If True, inverts the input trigger signal from falling to rising or
                vice versa. Default value: False

                


            :type invert: bool

route_trigger_input
-------------------

    .. py:currentmodule:: niswitch.Session

    .. py:method:: route_trigger_input(trigger_input_connector, trigger_input_bus_line, invert=False)

            Routes the input trigger from the front or rear connector to a trigger
            bus line (TTLx). To disconnect the route, call this method again and
            specify None for trigger bus line parameter.

            



            :param trigger_input_connector:


                The location of the input trigger source on the switch module. Valid
                locations are the :py:data:`~niswitch.TriggerInput.FRONTCONNECTOR` and
                :py:data:`~niswitch.TriggerInput.REARCONNECTOR`. Default value:
                :py:data:`~niswitch.TriggerInput.FRONTCONNECTOR`

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type trigger_input_connector: :py:data:`niswitch.TriggerInput`
            :param trigger_input_bus_line:


                The trigger line to route the input trigger. Select :py:data:`~niswitch.NISWITCH_VAL_NONE`
                to break an existing route. Default value: None Valid Values:
                :py:data:`~niswitch.NISWITCH_VAL_NONE` :py:data:`~niswitch.TriggerInput.TTL0` :py:data:`~niswitch.TriggerInput.TTL1`
                :py:data:`~niswitch.TriggerInput.TTL2` :py:data:`~niswitch.TriggerInput.TTL3` :py:data:`~niswitch.TriggerInput.TTL4`
                :py:data:`~niswitch.TriggerInput.TTL5` :py:data:`~niswitch.TriggerInput.TTL6` :py:data:`~niswitch.TriggerInput.TTL7`

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type trigger_input_bus_line: :py:data:`niswitch.TriggerInput`
            :param invert:


                If True, inverts the input trigger signal from falling to rising or
                vice versa. Default value: False

                


            :type invert: bool

self_test
---------

    .. py:currentmodule:: niswitch.Session

    .. py:method:: self_test()

            Verifies that the driver can communicate with the switch module.

            Raises `SelfTestError` on self test failure. Properties on exception object:

            - code - failure code from driver
            - message - status message from driver

            +----------------+------------------+
            | Self-Test Code | Description      |
            +================+==================+
            | 0              | Passed self-test |
            +----------------+------------------+
            | 1              | Self-test failed |
            +----------------+------------------+



send_software_trigger
---------------------

    .. py:currentmodule:: niswitch.Session

    .. py:method:: send_software_trigger()

            Sends a software trigger to the switch module specified in the NI-SWITCH
            session. When the trigger input is set to :py:data:`~niswitch.TriggerInput.SOFTWARE_TRIG`
            through either the :py:meth:`niswitch.Session.ConfigureScanTrigger` or the
            :py:attr:`niswitch.Session.trigger_input` property, the scan does not proceed from
            a semi-colon (wait for trigger) until :py:meth:`niswitch.Session.send_software_trigger` is
            called.

            

            .. note:: One or more of the referenced methods are not in the Python API for this driver.



set_path
--------

    .. py:currentmodule:: niswitch.Session

    .. py:method:: set_path(path_list)

            Connects two channels by specifying an explicit path in the path list
            parameter. :py:meth:`niswitch.Session.set_path` is particularly useful where path
            repeatability is important, such as in calibrated signal paths. If this
            is not necessary, use :py:meth:`niswitch.Session.connect`.

            



            :param path_list:


                A string composed of comma-separated paths between channel 1 and channel
                2. The first and last names in the path are the endpoints of the path.
                Every other channel in the path are configuration channels. Example of a
                valid path list string: ch0->com0, com0->ab0. In this example, com0 is a
                configuration channel. Default value: None Obtain the path list for a
                previously created path with :py:meth:`niswitch.Session.get_path`.

                


            :type path_list: str

unlock
------

    .. py:currentmodule:: niswitch.Session

.. py:method:: unlock()

    Releases a lock that you acquired on an device session using
    :py:meth:`niswitch.Session.lock`. Refer to :py:meth:`niswitch.Session.unlock` for additional
    information on session locks.



wait_for_debounce
-----------------

    .. py:currentmodule:: niswitch.Session

    .. py:method:: wait_for_debounce(maximum_time_ms=hightime.timedelta(milliseconds=5000))

            Pauses until all created paths have settled. If the time you specify
            with the Maximum Time (ms) parameter elapsed before the switch paths
            have settled, this method returns the
            NISWITCH_ERROR_MAX_TIME_EXCEEDED error.

            



            :param maximum_time_ms:


                Specifies the maximum length of time to wait for all relays in the
                switch module to activate or deactivate. If the specified time elapses
                before all relays active or deactivate, a timeout error is returned.
                Default Value:5000 ms

                


            :type maximum_time_ms: int in milliseconds or hightime.timedelta

wait_for_scan_complete
----------------------

    .. py:currentmodule:: niswitch.Session

    .. py:method:: wait_for_scan_complete(maximum_time_ms=hightime.timedelta(milliseconds=5000))

            Pauses until the switch module stops scanning or the maximum time has
            elapsed and returns a timeout error. If the time you specify with the
            Maximum Time (ms) parameter elapsed before the scanning operation has
            finished, this method returns the NISWITCH_ERROR_MAX_TIME_EXCEEDED
            error.

            



            :param maximum_time_ms:


                Specifies the maximum length of time to wait for the switch module to
                stop scanning. If the specified time elapses before the scan ends,
                NISWITCH_ERROR_MAX_TIME_EXCEEDED error is returned. Default
                Value:5000 ms

                


            :type maximum_time_ms: int in milliseconds or hightime.timedelta


Properties
==========

analog_bus_sharing_enable
-------------------------

    .. py:attribute:: analog_bus_sharing_enable

        Enables or disables sharing of an analog bus line so that multiple  NI SwitchBlock devices may connect to it simultaneously. To enable  multiple NI SwitchBlock devices to share an analog bus line, set this  property to True for each device on the channel that corresponds  with the shared analog bus line. The default value for all devices is  False, which disables sharing of the analog bus.
        Refer to the Using the Analog Bus on an NI SwitchBlock Carrier topic  in the NI Switches Help for more information about sharing the analog bus.




        .. tip:: This property can use repeated capabilities. If set or get directly on the
            niswitch.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            niswitch.Session repeated capabilities container, and calling set/get value on the result.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | Yes        |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Channel Configuration:Analog Bus Sharing Enable**
                - C Attribute: **NISWITCH_ATTR_ANALOG_BUS_SHARING_ENABLE**

bandwidth
---------

    .. py:attribute:: bandwidth

        This channel-based property returns the bandwidth for the channel.
        The units are hertz.




        .. tip:: This property can use repeated capabilities. If set or get directly on the
            niswitch.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            niswitch.Session repeated capabilities container, and calling set/get value on the result.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | float     |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | Yes       |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Module Characteristics:Bandwidth**
                - C Attribute: **NISWITCH_ATTR_BANDWIDTH**

channel_count
-------------

    .. py:attribute:: channel_count

        Indicates the number of channels that the specific instrument  driver supports.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Driver Capabilities:Channel Count**
                - C Attribute: **NISWITCH_ATTR_CHANNEL_COUNT**

characteristic_impedance
------------------------

    .. py:attribute:: characteristic_impedance

        This channel-based property returns the characteristic impedance for the  channel.
        The units are ohms.




        .. tip:: This property can use repeated capabilities. If set or get directly on the
            niswitch.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            niswitch.Session repeated capabilities container, and calling set/get value on the result.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | float     |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | Yes       |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Module Characteristics:Characteristic Impedance**
                - C Attribute: **NISWITCH_ATTR_CHARACTERISTIC_IMPEDANCE**

continuous_scan
---------------

    .. py:attribute:: continuous_scan

        When a switch device is scanning, the swich can either stop scanning when  the end of the scan (False) or continue scanning from the top of the  scan list again (True).
        Notice that if you set the scan to continuous (True), the Wait For Scan  Complete operation will always time out and you must call Abort to stop  the scan.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Scanning Configuration:Continuous Scan**
                - C Attribute: **NISWITCH_ATTR_CONTINUOUS_SCAN**

digital_filter_enable
---------------------

    .. py:attribute:: digital_filter_enable

        This property specifies whether to apply the pulse width filter to the  Trigger Input. Enabling the Digital Filter (True) prevents the switch  module from being triggered by pulses that are less than 150 ns on PXI  trigger lines 0–7.
        When Digital Filter is disabled (False), it is possible for the switch  module to be triggered by noise on the PXI trigger lines. If the device  triggering the switch is capable of sending pulses greater than 150 ns, you should not disable the Digital Filter.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Scanning Configuration:Digital Filter Enable**
                - C Attribute: **NISWITCH_ATTR_DIGITAL_FILTER_ENABLE**

driver_setup
------------

    .. py:attribute:: driver_setup

        This property indicates the Driver Setup string that the user  specified when initializing the driver.
        Some cases exist where the end-user must specify instrument driver  options at initialization time.  An example of this is specifying  a particular instrument model from among a family of instruments  that the driver supports.  This is useful when using simulation.   The end-user can specify driver-specific options through  the DriverSetup keyword in the optionsString parameter to the  :py:meth:`niswitch.Session.InitWithOptions` method, or through the IVI Configuration Utility.
        If the user does not specify a Driver Setup string, this property returns an empty string.



        .. note:: One or more of the referenced methods are not in the Python API for this driver.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Advanced Session Information:Driver Setup**
                - C Attribute: **NISWITCH_ATTR_DRIVER_SETUP**

handshaking_initiation
----------------------

    .. py:attribute:: handshaking_initiation

        

        The following table lists the characteristics of this property.

            +----------------+-----------------------------+
            | Characteristic | Value                       |
            +================+=============================+
            | Datatype       | enums.HandshakingInitiation |
            +----------------+-----------------------------+
            | Permissions    | read-write                  |
            +----------------+-----------------------------+
            | Channel Based  | No                          |
            +----------------+-----------------------------+
            | Resettable     | No                          |
            +----------------+-----------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Scanning Configuration:Handshaking Initiation**
                - C Attribute: **NISWITCH_ATTR_HANDSHAKING_INITIATION**

instrument_firmware_revision
----------------------------

    .. py:attribute:: instrument_firmware_revision

        A string that contains the firmware revision information  for the instrument you are currently using.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Instrument Identification:Firmware Revision**
                - C Attribute: **NISWITCH_ATTR_INSTRUMENT_FIRMWARE_REVISION**

instrument_manufacturer
-----------------------

    .. py:attribute:: instrument_manufacturer

        A string that contains the name of the instrument manufacturer you are currently  using.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Instrument Identification:Manufacturer**
                - C Attribute: **NISWITCH_ATTR_INSTRUMENT_MANUFACTURER**

instrument_model
----------------

    .. py:attribute:: instrument_model

        A string that contains the model number or name of the instrument that you  are currently using.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Instrument Identification:Model**
                - C Attribute: **NISWITCH_ATTR_INSTRUMENT_MODEL**

io_resource_descriptor
----------------------

    .. py:attribute:: io_resource_descriptor

        Indicates the resource descriptor the driver  uses to identify the physical device.
        If you initialize the driver with a logical name, this  property contains the resource descriptor that corresponds  to the entry in the IVI Configuration utility.
        If you initialize the instrument driver with the resource  descriptor, this property contains that value.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Advanced Session Information:IO Resource Descriptor**
                - C Attribute: **NISWITCH_ATTR_IO_RESOURCE_DESCRIPTOR**

is_configuration_channel
------------------------

    .. py:attribute:: is_configuration_channel

        This channel-based property specifies whether to reserve the channel for  internal path creation.  A channel that is available for internal path  creation is called a configuration channel.  The driver may use  configuration channels to create paths between two channels you specify in  the :py:meth:`niswitch.Session.connect` method.  Configuration channels are not available  for external connections.
        Set this property to True to mark the channel as a configuration  channel.  Set this property to False to mark the channel as available  for external connections.
        After you identify a channel as a configuration channel, you cannot  use that channel for external connections.  The :py:meth:`niswitch.Session.connect` method  returns the NISWITCH_ERROR_IS_CONFIGURATION_CHANNEL error when you attempt  to establish a connection between a configuration channel and any other  channel.




        .. tip:: This property can use repeated capabilities. If set or get directly on the
            niswitch.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            niswitch.Session repeated capabilities container, and calling set/get value on the result.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | Yes        |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Channel Configuration:Is Configuration Channel**
                - C Attribute: **NISWITCH_ATTR_IS_CONFIGURATION_CHANNEL**

is_debounced
------------

    .. py:attribute:: is_debounced

        This property indicates whether the entire switch device has settled  since the last switching command.  A value of True indicates that all  signals going through the switch device are valid.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | bool      |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Module Characteristics:Is Debounced**
                - C Attribute: **NISWITCH_ATTR_IS_DEBOUNCED**

is_scanning
-----------

    .. py:attribute:: is_scanning

        If True, the switch module is currently scanning through the scan list  (i.e. it is not in the Idle state). If False, the switch module is not  currently scanning through the scan list (i.e. it is in the Idle state).

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | bool      |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Scanning Configuration:Is Scanning**
                - C Attribute: **NISWITCH_ATTR_IS_SCANNING**

is_source_channel
-----------------

    .. py:attribute:: is_source_channel

        This channel-based property specifies whether you want to identify the  channel as a source channel.  Typically, you set this property to True  when you attach the channel to a power supply, a method generator, or an  active measurement point on the unit under test, and you do not want to  connect the channel to another source.  The driver prevents source  channels from connecting to each other.  The :py:meth:`niswitch.Session.connect` method  returns the NISWITCH_ERROR_ATTEMPT_TO_CONNECT_SOURCES when you attempt to  connect two channels that you identify as source channels.




        .. tip:: This property can use repeated capabilities. If set or get directly on the
            niswitch.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            niswitch.Session repeated capabilities container, and calling set/get value on the result.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | Yes        |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Channel Configuration:Is Source Channel**
                - C Attribute: **NISWITCH_ATTR_IS_SOURCE_CHANNEL**

is_waiting_for_trig
-------------------

    .. py:attribute:: is_waiting_for_trig

        In a scan list, a semi-colon (;) is used to indicate that at that point in  the scan list, the scan engine should pause until a trigger is received  from the trigger input.  If that trigger is user generated through either  a hardware pulse or the Send SW Trigger operation, it is necessary for the  user to know  when the scan engine has reached such a state.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | bool      |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Scanning Configuration:Is Waiting for Trigger?**
                - C Attribute: **NISWITCH_ATTR_IS_WAITING_FOR_TRIG**

logical_name
------------

    .. py:attribute:: logical_name

        A string containing the logical name you specified when opening the  current IVI session.
        You may pass a logical name to the :py:meth:`niswitch.Session.init` or  :py:meth:`niswitch.Session.InitWithOptions` methods.   The IVI Configuration utility must contain an entry for the logical name.   The logical name entry refers to a virtual instrument section in the  IVI Configuration file.  The virtual instrument section specifies a physical  device and initial user options.



        .. note:: One or more of the referenced methods are not in the Python API for this driver.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Advanced Session Information:Logical Name**
                - C Attribute: **NISWITCH_ATTR_LOGICAL_NAME**

max_ac_voltage
--------------

    .. py:attribute:: max_ac_voltage

        This channel-based property returns the maximum AC voltage the channel  can switch.
        The units are volts RMS.




        .. tip:: This property can use repeated capabilities. If set or get directly on the
            niswitch.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            niswitch.Session repeated capabilities container, and calling set/get value on the result.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | float     |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | Yes       |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Module Characteristics:Maximum AC Voltage**
                - C Attribute: **NISWITCH_ATTR_MAX_AC_VOLTAGE**

max_carry_ac_current
--------------------

    .. py:attribute:: max_carry_ac_current

        This channel-based property returns the maximum AC current the channel  can carry.
        The units are amperes RMS.




        .. tip:: This property can use repeated capabilities. If set or get directly on the
            niswitch.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            niswitch.Session repeated capabilities container, and calling set/get value on the result.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | float     |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | Yes       |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Module Characteristics:Maximum Carry AC Current**
                - C Attribute: **NISWITCH_ATTR_MAX_CARRY_AC_CURRENT**

max_carry_ac_power
------------------

    .. py:attribute:: max_carry_ac_power

        This channel-based property returns the maximum AC power the channel can  carry.
        The units are volt-amperes.




        .. tip:: This property can use repeated capabilities. If set or get directly on the
            niswitch.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            niswitch.Session repeated capabilities container, and calling set/get value on the result.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | float     |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | Yes       |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Module Characteristics:Maximum Carry AC Power**
                - C Attribute: **NISWITCH_ATTR_MAX_CARRY_AC_POWER**

max_carry_dc_current
--------------------

    .. py:attribute:: max_carry_dc_current

        This channel-based property returns the maximum DC current the channel  can carry.
        The units are amperes.




        .. tip:: This property can use repeated capabilities. If set or get directly on the
            niswitch.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            niswitch.Session repeated capabilities container, and calling set/get value on the result.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | float     |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | Yes       |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Module Characteristics:Maximum Carry DC Current**
                - C Attribute: **NISWITCH_ATTR_MAX_CARRY_DC_CURRENT**

max_carry_dc_power
------------------

    .. py:attribute:: max_carry_dc_power

        This channel-based property returns the maximum DC power the channel can  carry.
        The units are watts.




        .. tip:: This property can use repeated capabilities. If set or get directly on the
            niswitch.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            niswitch.Session repeated capabilities container, and calling set/get value on the result.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | float     |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | Yes       |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Module Characteristics:Maximum Carry DC Power**
                - C Attribute: **NISWITCH_ATTR_MAX_CARRY_DC_POWER**

max_dc_voltage
--------------

    .. py:attribute:: max_dc_voltage

        This channel-based property returns the maximum DC voltage the channel  can switch.
        The units are volts.




        .. tip:: This property can use repeated capabilities. If set or get directly on the
            niswitch.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            niswitch.Session repeated capabilities container, and calling set/get value on the result.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | float     |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | Yes       |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Module Characteristics:Maximum DC Voltage**
                - C Attribute: **NISWITCH_ATTR_MAX_DC_VOLTAGE**

max_switching_ac_current
------------------------

    .. py:attribute:: max_switching_ac_current

        This channel-based property returns the maximum AC current the channel  can switch.
        The units are amperes RMS.




        .. tip:: This property can use repeated capabilities. If set or get directly on the
            niswitch.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            niswitch.Session repeated capabilities container, and calling set/get value on the result.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | float     |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | Yes       |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Module Characteristics:Maximum Switching AC Current**
                - C Attribute: **NISWITCH_ATTR_MAX_SWITCHING_AC_CURRENT**

max_switching_ac_power
----------------------

    .. py:attribute:: max_switching_ac_power

        This channel-based property returns the maximum AC power the channel can  switch.
        The units are volt-amperes.




        .. tip:: This property can use repeated capabilities. If set or get directly on the
            niswitch.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            niswitch.Session repeated capabilities container, and calling set/get value on the result.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | float     |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | Yes       |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Module Characteristics:Maximum Switching AC Power**
                - C Attribute: **NISWITCH_ATTR_MAX_SWITCHING_AC_POWER**

max_switching_dc_current
------------------------

    .. py:attribute:: max_switching_dc_current

        This channel-based property returns the maximum DC current the channel  can switch.
        The units are amperes.




        .. tip:: This property can use repeated capabilities. If set or get directly on the
            niswitch.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            niswitch.Session repeated capabilities container, and calling set/get value on the result.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | float     |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | Yes       |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Module Characteristics:Maximum Switching DC Current**
                - C Attribute: **NISWITCH_ATTR_MAX_SWITCHING_DC_CURRENT**

max_switching_dc_power
----------------------

    .. py:attribute:: max_switching_dc_power

        This channel-based property returns the maximum DC power the channel can  switch.
        The units are watts.




        .. tip:: This property can use repeated capabilities. If set or get directly on the
            niswitch.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            niswitch.Session repeated capabilities container, and calling set/get value on the result.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | float     |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | Yes       |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Module Characteristics:Maximum Switching DC Power**
                - C Attribute: **NISWITCH_ATTR_MAX_SWITCHING_DC_POWER**

number_of_relays
----------------

    .. py:attribute:: number_of_relays

        This property returns the number of relays.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Module Characteristics:Number of Relays**
                - C Attribute: **NISWITCH_ATTR_NUMBER_OF_RELAYS**

num_of_columns
--------------

    .. py:attribute:: num_of_columns

        This property returns the number of channels on the column of a matrix or  scanner.  If the switch device is a scanner, this value is the number of  input channels.
        The :py:attr:`niswitch.Session.wire_mode` property affects the number of available  columns.  For example, if your device has 8 input lines and you use the  four-wire mode, then the number of columns you have available is 2.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Matrix Configuration:Number of Columns**
                - C Attribute: **NISWITCH_ATTR_NUM_OF_COLUMNS**

num_of_rows
-----------

    .. py:attribute:: num_of_rows

        This property returns the number of channels on the row of a matrix or  scanner.  If the switch device is a scanner, this value is the number of  output channels.
        The :py:attr:`niswitch.Session.wire_mode` property affects the number of available  rows.  For example, if your device has 8 input lines and you use the  two-wire mode, then the number of columns you have available is 4.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Matrix Configuration:Number of Rows**
                - C Attribute: **NISWITCH_ATTR_NUM_OF_ROWS**

power_down_latching_relays_after_debounce
-----------------------------------------

    .. py:attribute:: power_down_latching_relays_after_debounce

        This property specifies whether to power down latching relays after  calling Wait For Debounce.
        When Power Down Latching Relays After Debounce is enabled (True),  a call to Wait For Debounce ensures that the relays are settled  and the latching relays are powered down.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Module Characteristics:Power Down Latching Relays After Debounce**
                - C Attribute: **NISWITCH_ATTR_POWER_DOWN_LATCHING_RELAYS_AFTER_DEBOUNCE**

scan_advanced_output
--------------------

    .. py:attribute:: scan_advanced_output

        This property specifies the method you want to use to notify another  instrument that all signals going through the switch device have settled  following the processing of one entry in the scan list.

        The following table lists the characteristics of this property.

            +----------------+--------------------------+
            | Characteristic | Value                    |
            +================+==========================+
            | Datatype       | enums.ScanAdvancedOutput |
            +----------------+--------------------------+
            | Permissions    | read-write               |
            +----------------+--------------------------+
            | Channel Based  | No                       |
            +----------------+--------------------------+
            | Resettable     | No                       |
            +----------------+--------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Scanning Configuration:Scan Advanced Output**
                - C Attribute: **NISWITCH_ATTR_SCAN_ADVANCED_OUTPUT**

scan_advanced_polarity
----------------------

    .. py:attribute:: scan_advanced_polarity

        

        The following table lists the characteristics of this property.

            +----------------+----------------------------+
            | Characteristic | Value                      |
            +================+============================+
            | Datatype       | enums.ScanAdvancedPolarity |
            +----------------+----------------------------+
            | Permissions    | read-write                 |
            +----------------+----------------------------+
            | Channel Based  | No                         |
            +----------------+----------------------------+
            | Resettable     | No                         |
            +----------------+----------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Scanning Configuration:Scan Advanced Polarity**
                - C Attribute: **NISWITCH_ATTR_SCAN_ADVANCED_POLARITY**

scan_delay
----------

    .. py:attribute:: scan_delay

        This property specifies the minimum amount of time the switch device  waits before it asserts the scan advanced output trigger after opening or  closing the switch.  The switch device always waits for debounce before  asserting the trigger. The units are seconds.
        the greater value of the settling time and the value you specify as the  scan delay.



        .. note:: NI PXI-2501/2503/2565/2590/2591 Users--the actual delay will always be

        The following table lists the characteristics of this property.

            +----------------+----------------------------------------+
            | Characteristic | Value                                  |
            +================+========================================+
            | Datatype       | float in seconds or hightime.timedelta |
            +----------------+----------------------------------------+
            | Permissions    | read-write                             |
            +----------------+----------------------------------------+
            | Channel Based  | No                                     |
            +----------------+----------------------------------------+
            | Resettable     | No                                     |
            +----------------+----------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Scanning Configuration:Scan Delay**
                - C Attribute: **NISWITCH_ATTR_SCAN_DELAY**

scan_list
---------

    .. py:attribute:: scan_list

        This property contains a scan list, which is a string that specifies  channel connections and trigger conditions.  The :py:meth:`niswitch.Session.initiate`  method makes or breaks connections and waits for triggers according to  the instructions in the scan list.
        The scan list is comprised of channel names that you separate with  special characters.  These special characters determine the operations the  scanner performs on the channels when it executes this scan list.
        To create a path between two channels, use the following character between  the two channel names:
        -> (a dash followed by a '>' sign)
        Example:  'CH1->CH2' tells the switch to make a path from channel CH1 to channel  CH2.
        To break or clear a path, use the following character as a prefix before  the path:
        ~ (tilde)
        Example:  '~CH1->CH2' tells the switch to break the path from channel CH1 to  channel CH2.
        To tell the switch device to wait for a trigger event, use the following  character as a separator between paths:
        ; (semi-colon)
        Example:  'CH1->CH2;CH3->CH4' tells the switch to make the path from channel CH1  to channel CH2, wait for a trigger, and then make the path from CH3 to  CH4.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Scanning Configuration:Scan List**
                - C Attribute: **NISWITCH_ATTR_SCAN_LIST**

scan_mode
---------

    .. py:attribute:: scan_mode

        This property specifies what happens to existing connections that  conflict with the connections you make in a scan list.  For example, if  CH1 is already connected to CH2 and the scan list instructs the switch  device to connect CH1 to CH3, this property specifies what happens to the  connection between CH1 and CH2.
        If the value of this property is :py:data:`~niswitch.ScanMode.NONE`, the switch device  takes no action on existing paths.  If the value is  :py:data:`~niswitch.ScanMode.BREAK_BEFORE_MAKE`, the switch device breaks conflicting paths  before making new ones.  If the value is :py:data:`~niswitch.ScanMode.BREAK_AFTER_MAKE`,  the switch device breaks conflicting paths after making new ones.
        Most switch devices support only one of the possible values.  In such  cases, this property serves as an indicator of the device's behavior.



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +----------------+----------------+
            | Characteristic | Value          |
            +================+================+
            | Datatype       | enums.ScanMode |
            +----------------+----------------+
            | Permissions    | read-write     |
            +----------------+----------------+
            | Channel Based  | No             |
            +----------------+----------------+
            | Resettable     | No             |
            +----------------+----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Scanning Configuration:Scan Mode**
                - C Attribute: **NISWITCH_ATTR_SCAN_MODE**

serial_number
-------------

    .. py:attribute:: serial_number

        This read-only property returns the serial number for the switch device  controlled by this instrument driver.  If the device does not return a  serial number, the driver returns the IVI_ERROR_ATTRIBUTE_NOT_SUPPORTED error.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Module Characteristics:Serial Number**
                - C Attribute: **NISWITCH_ATTR_SERIAL_NUMBER**

settling_time
-------------

    .. py:attribute:: settling_time

        This channel-based property returns the maximum length of time from after  you make a connection until the signal flowing through the channel  settles. The units are seconds.
        the greater value of the settling time and the value you specify as the  scan delay.



        .. note:: NI PXI-2501/2503/2565/2590/2591 Users--the actual delay will always be


        .. tip:: This property can use repeated capabilities. If set or get directly on the
            niswitch.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            niswitch.Session repeated capabilities container, and calling set/get value on the result.

        The following table lists the characteristics of this property.

            +----------------+----------------------------------------+
            | Characteristic | Value                                  |
            +================+========================================+
            | Datatype       | float in seconds or hightime.timedelta |
            +----------------+----------------------------------------+
            | Permissions    | read-write                             |
            +----------------+----------------------------------------+
            | Channel Based  | Yes                                    |
            +----------------+----------------------------------------+
            | Resettable     | No                                     |
            +----------------+----------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Module Characteristics:Settling Time**
                - C Attribute: **NISWITCH_ATTR_SETTLING_TIME**

simulate
--------

    .. py:attribute:: simulate

        Specifies whether or not to simulate instrument driver I/O operations.  If  simulation is enabled, instrument driver methods perform range checking  and call Ivi_GetAttribute and Ivi_SetAttribute methods, but they do not  perform instrument I/O.  For output parameters that represent instrument  data, the instrument driver methods return calculated values.
        The default value is False.   Use the :py:meth:`niswitch.Session.InitWithOptions`  method to override this value.



        .. note:: One or more of the referenced methods are not in the Python API for this driver.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:User Options:Simulate**
                - C Attribute: **NISWITCH_ATTR_SIMULATE**

specific_driver_description
---------------------------

    .. py:attribute:: specific_driver_description

        A string that contains a brief description of the specific  driver.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Driver Identification:Description**
                - C Attribute: **NISWITCH_ATTR_SPECIFIC_DRIVER_DESCRIPTION**

specific_driver_revision
------------------------

    .. py:attribute:: specific_driver_revision

        A string that contains additional version information about this  instrument driver.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Driver Identification:Revision**
                - C Attribute: **NISWITCH_ATTR_SPECIFIC_DRIVER_REVISION**

specific_driver_vendor
----------------------

    .. py:attribute:: specific_driver_vendor

        A string that contains the name of the vendor that supplies this driver.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Driver Identification:Driver Vendor**
                - C Attribute: **NISWITCH_ATTR_SPECIFIC_DRIVER_VENDOR**

supported_instrument_models
---------------------------

    .. py:attribute:: supported_instrument_models

        Contains a comma-separated list of supported instrument models.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models**
                - C Attribute: **NISWITCH_ATTR_SUPPORTED_INSTRUMENT_MODELS**

temperature
-----------

    .. py:attribute:: temperature

        This property returns the temperature as read by the Switch module.     The units are degrees Celsius.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | float     |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Module Characteristics:Temperature**
                - C Attribute: **NISWITCH_ATTR_TEMPERATURE**

trigger_input
-------------

    .. py:attribute:: trigger_input

        This property specifies the source of the trigger for which the switch  device can wait when processing a scan list.  The switch device waits for  a trigger when it encounters a semi-colon in a scan list.  When the trigger  occurs, the switch device advances to the next entry in the scan list.

        The following table lists the characteristics of this property.

            +----------------+--------------------+
            | Characteristic | Value              |
            +================+====================+
            | Datatype       | enums.TriggerInput |
            +----------------+--------------------+
            | Permissions    | read-write         |
            +----------------+--------------------+
            | Channel Based  | No                 |
            +----------------+--------------------+
            | Resettable     | No                 |
            +----------------+--------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Scanning Configuration:Trigger Input**
                - C Attribute: **NISWITCH_ATTR_TRIGGER_INPUT**

trigger_input_polarity
----------------------

    .. py:attribute:: trigger_input_polarity

        Determines the behavior of the trigger Input.

        The following table lists the characteristics of this property.

            +----------------+----------------------------+
            | Characteristic | Value                      |
            +================+============================+
            | Datatype       | enums.TriggerInputPolarity |
            +----------------+----------------------------+
            | Permissions    | read-write                 |
            +----------------+----------------------------+
            | Channel Based  | No                         |
            +----------------+----------------------------+
            | Resettable     | No                         |
            +----------------+----------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Scanning Configuration:Trigger Input Polarity**
                - C Attribute: **NISWITCH_ATTR_TRIGGER_INPUT_POLARITY**

wire_mode
---------

    .. py:attribute:: wire_mode

        This property returns the wire mode of the switch device.
        This property affects the values of the :py:attr:`niswitch.Session.num_of_rows` and  :py:attr:`niswitch.Session.num_of_columns` properties.   The actual number of input and  output lines on the switch device is fixed, but the number of channels  depends on how many lines constitute each channel.




        .. tip:: This property can use repeated capabilities. If set or get directly on the
            niswitch.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            niswitch.Session repeated capabilities container, and calling set/get value on the result.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | Yes       |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Module Characteristics:Wire mode**
                - C Attribute: **NISWITCH_ATTR_WIRE_MODE**


.. contents:: Session


