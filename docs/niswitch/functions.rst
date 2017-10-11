niswitch.Session methods
========================

.. py:currentmodule:: niswitch

.. function:: can_connect(channel1, channel2)

    Verifies that a path between channel 1 and channel 2 can be created. If
    a path is possible in the switch module, the availability of that path
    is returned given the existing connections. If the path is possible but
    in use, a NISWITCH\_WARN\_IMPLICIT\_CONNECTION\_EXISTS warning is
    returned.

    



    :param channel1:


        Input one of the channel names of the desired path. Pass the other
        channel name as the channel 2 parameter. Refer to Devices Overview for
        valid channel names for the switch module. Examples of valid channel
        names: ch0, com0, ab0, r1, c2, cjtemp Default value: ""

        


    :type channel1: string
    :param channel2:


        Input one of the channel names of the desired path. Pass the other
        channel name as the channel 1 parameter. Refer to Devices Overview for
        valid channel names for the switch module. Examples of valid channel
        names: ch0, com0, ab0, r1, c2, cjtemp Default value: ""

        


    :type channel2: string

    :rtype: :py:data:`niswitch.PathCapability`
    :return:


            Indicates whether a path is valid. Possible values include:
            ------------------------------------ NISWITCH\_VAL\_PATH\_AVAILABLE 1
            NISWITCH\_VAL\_PATH\_EXISTS 2 NISWITCH\_VAL\_PATH\_UNSUPPORTED 3
            NISWITCH\_VAL\_RSRC\_IN\_USE 4 NISWITCH\_VAL\_SOURCE\_CONFLICT 5
            NISWITCH\_VAL\_CHANNEL\_NOT\_AVAILABLE 6 Notes: (1)
            NISWITCH\_VAL\_PATH\_AVAILABLE indicates that the driver can create the
            path at this time. (2) NISWITCH\_VAL\_PATH\_EXISTS indicates that the
            path already exists. (3) NISWITCH\_VAL\_PATH\_UNSUPPORTED indicates that
            the instrument is not capable of creating a path between the channels
            you specify. (4) NISWITCH\_VAL\_RSRC\_IN\_USE indicates that although
            the path is valid, the driver cannot create the path at this moment
            because the switch device is currently using one or more of the required
            channels to create another path. You must destroy the other path before
            creating this one. (5) NISWITCH\_VAL\_SOURCE\_CONFLICT indicates that
            the instrument cannot create a path because both channels are connected
            to a different source channel. (6)
            NISWITCH\_VAL\_CHANNEL\_NOT\_AVAILABLE indicates that the driver cannot
            create a path between the two channels because one of the channels is a
            configuration channel and thus unavailable for external connections.

            



.. function:: commit()

    Downloads the configured scan list and trigger settings to hardware.
    Calling :py:func:`niswitch.commit` optional as it is implicitly called during
    :py:func:`niswitch._initiate_scan`. Use :py:func:`niswitch.commit` to arm triggers in a given
    order or to control when expensive hardware operations are performed.

    



.. function:: configure_scan_list(scanlist, scan_mode=niswitch.ScanMode.BREAK_BEFORE_MAKE)

    Configures the scan list and scan mode used for scanning. Refer to
    Devices Overview to determine if the switch module supports scanning.
    The scan list is comprised of a list of channel connections separated by
    semi-colons. For example, the following scan list will scan the first
    three channels of a multiplexer: com0->ch0; com0->ch1; com0->ch2; Refer
    to Scan Lists for more information on scan list syntax To see the status
    of the scan, call either :py:func:`niswitch.is_scanning` or
    :py:func:`niswitch.wait_for_scan_complete`. Use the :py:func:`niswitch.configure_scan_trigger`
    function to configure the scan trigger. Use the :py:func:`niswitch._initiate_scan`
    function to start the scan.

    



    :param scanlist:


        The scan list to use. The driver uses this value to set the Scan List
        attribute. Default value: None

        


    :type scanlist: string
    :param scan_mode:


        Specifies how the switch module breaks existing connections when
        scanning. The driver uses this value to set the Scan Mode attribute.
        Refer to scan modes for more information. Default value: Break Before
        Make

        


    :type scan_mode: :py:data:`niswitch.ScanMode`

.. function:: configure_scan_trigger(trigger_input, scan_advanced_output, scan_delay=0.0)

    Configures the scan triggers for the scan list established with
    :py:func:`niswitch.configure_scan_list`. Refer to Devices Overview to determine if
    the switch module supports scanning. :py:func:`niswitch.configure_scan_trigger` sets
    the location that the switch expects to receive an input trigger to
    advance through the scan list. This function also sets the location
    where it outputs a scan advanced signal after it completes an entry in
    the scan list.

    



    :param scan_delay:


        The minimum length of time you want the switch device to wait after it
        creates a path until it asserts a trigger on the scan advanced output
        line. The driver uses this value to set the Scan Delay attribute. The
        scan delay is in addition to the settling time.The driver uses this
        value to set the :py:data:`niswitch.SCAN\_DELAY` attribute. Express this
        value in seconds. Default value: 0.0 s

        


    :type scan_delay: float
    :param trigger_input:


        Trigger source you want the switch module to use during scanning. The
        driver uses this value to set the :py:data:`niswitch.TRIGGER\_INPUT`
        attribute. The switch device waits for the trigger you specify when it
        encounters a semicolon in the scanlist. When the trigger occurs, the
        switch device advances to the next entry in the scanlist. Refer to the
        :py:data:`niswitch.TRIGGER\_INPUT` topic in the NI Switches Help for a list
        of valid values.

        


    :type trigger_input: :py:data:`niswitch.TriggerInput`
    :param scan_advanced_output:


        Output destination of the scan advanced trigger signal. The driver uses
        this value to set the :py:data:`niswitch.SCAN\_ADVANCED\_OUTPUT` attribute.
        After the switch processes each entry in the scan list, it waits the
        length of time you specify in the Scan Delay parameter and then asserts
        a trigger on the line you specify with this parameter. Refer to the
        :py:data:`niswitch.SCAN\_ADVANCED\_OUTPUT` topic in the NI Switches Help for
        a list of valid values.

        


    :type scan_advanced_output: :py:data:`niswitch.ScanAdvancedOutput`

.. function:: connect(channel1, channel2)

    Creates a path between channel 1 and channel 2. The driver calculates
    and uses the shortest path between the two channels. Refer to Immediate
    Operations for information about Channel Usage types. If a path is not
    available, the function returns one of the following errors: -
    NISWITCH\_ERROR\_EXPLICIT\_CONNECTION\_EXISTS, if the two channels are
    already explicitly connected by calling either the :py:func:`niswitch.connect` or
    :py:func:`niswitch.set_path` function. -
    NISWITCH\_ERROR\_IS\_CONFIGURATION\_CHANNEL, if a channel is a
    configuration channel. Error elaboration contains information about
    which of the two channels is a configuration channel. -
    NISWITCH\_ERROR\_ATTEMPT\_TO\_CONNECT\_SOURCES, if both channels are
    connected to a different source. Error elaboration contains information
    about sources channel 1 and 2 connect to. -
    NISWITCH\_ERROR\_CANNOT\_CONNECT\_TO\_ITSELF, if channels 1 and 2 are
    one and the same channel. - NISWITCH\_ERROR\_PATH\_NOT\_FOUND, if the
    driver cannot find a path between the two channels. Note: Paths are
    bidirectional. For example, if a path exists between channels CH1 and
    CH2, then the path also exists between channels CH2 and CH1.

    



    :param channel1:


        Input one of the channel names of the desired path. Pass the other
        channel name as the channel 2 parameter. Refer to Devices Overview for
        valid channel names for the switch module. Examples of valid channel
        names: ch0, com0, ab0, r1, c2, cjtemp Default value: None

        


    :type channel1: string
    :param channel2:


        Input one of the channel names of the desired path. Pass the other
        channel name as the channel 1 parameter. Refer to Devices Overview for
        valid channel names for the switch module. Examples of valid channel
        names: ch0, com0, ab0, r1, c2, cjtemp Default value: None

        


    :type channel2: string

.. function:: connect_multiple(connection_list)

    Creates the connections between channels specified in Connection List.
    Specify connections with two endpoints only or the explicit path between
    two endpoints. NI-SWITCH calculates and uses the shortest path between
    the channels. Refer to Setting Source and Configuration Channels for
    information about channel usage types. In the event of an error,
    connecting stops at the point in the list where the error occurred. If a
    path is not available, the function returns one of the following errors:
    - NISWITCH\_ERROR\_EXPLICIT\_CONNECTION\_EXISTS, if the two channels are
    already explicitly connected. -
    NISWITCH\_ERROR\_IS\_CONFIGURATION\_CHANNEL, if a channel is a
    configuration channel. Error elaboration contains information about
    which of the two channels is a configuration channel. -
    NISWITCH\_ERROR\_ATTEMPT\_TO\_CONNECT\_SOURCES, if both channels are
    connected to a different source. Error elaboration contains information
    about sources channel 1 and 2 to connect. -
    NISWITCH\_ERROR\_CANNOT\_CONNECT\_TO\_ITSELF, if channels 1 and 2 are
    one and the same channel. - NISWITCH\_ERROR\_PATH\_NOT\_FOUND, if the
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

        


    :type connection_list: string

.. function:: disable()

    Places the switch module in a quiescent state where it has minimal or no
    impact on the system to which it is connected. All channels are
    disconnected and any scan in progress is aborted.

    



.. function:: disconnect(channel1, channel2)

    This function destroys the path between two channels that you create
    with the :py:func:`niswitch.connect` or :py:func:`niswitch.set_path` function. If a path is
    not connected or not available, the function returns the
    IVISWTCH\_ERROR\_NO\_SUCH\_PATH error.

    



    :param channel1:


        Input one of the channel names of the path to break. Pass the other
        channel name as the channel 2 parameter. Refer to Devices Overview for
        valid channel names for the switch module. Examples of valid channel
        names: ch0, com0, ab0, r1, c2, cjtemp Default value: None

        


    :type channel1: string
    :param channel2:


        Input one of the channel names of the path to break. Pass the other
        channel name as the channel 1 parameter. Refer to Devices Overview for
        valid channel names for the switch module. Examples of valid channel
        names: ch0, com0, ab0, r1, c2, cjtemp Default value: None

        


    :type channel2: string

.. function:: disconnect_all()

    Breaks all existing paths. If the switch module cannot break all paths,
    NISWITCH\_WARN\_PATH\_REMAINS warning is returned.

    



.. function:: disconnect_multiple(disconnection_list)

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

        


    :type disconnection_list: string

.. function:: get_channel_name(index)

    Returns the channel string that is in the channel table at the specified
    index. Use :py:func:`niswitch.get_channel_name` in a For Loop to get a complete list
    of valid channel names for the switch module. Use the Channel Count
    attribute to determine the number of channels.

    



    :param index:


        A 1-based index into the channel table. Default value: 1 Maximum value:
        Value of Channel Count attribute.

        


    :type index: int
    :param buffer_size:


        Pass the number of bytes in the ViChar array you specify for the Channel
        Name Buffer parameter. If the channel name string, including the
        terminating NUL byte, contains more bytes than you indicate in this
        parameter, the function copies Buffer Size - 1 bytes into the buffer,
        places an ASCII NUL byte at the end of the buffer, and returns the
        buffer size you must pass to get the entire value. For example, if the
        value is "123456" and the Buffer Size is 4, the function places "123"
        into the buffer and returns 7. If you pass a negative number, the
        function copies the value to the buffer regardless of the number of
        bytes in the value. If you pass 0, you can pass VI\_NULL for the
        Coercion Record buffer parameter. Default Value: None

        


    :type buffer_size: int

.. function:: get_path(channel1, channel2)

    Returns a string that identifies the explicit path created with
    :py:func:`niswitch.connect`. Pass this string to :py:func:`niswitch.set_path` to establish
    the exact same path in future connections. In some cases, multiple paths
    are available between two channels. When you call :py:func:`niswitch.connect`, the
    driver selects an available path. With :py:func:`niswitch.connect`, there is no
    guarantee that the driver selected path will always be the same path
    through the switch module. :py:func:`niswitch.get_path` only returns those paths
    explicitly created by niSwitch Connect Channels or :py:func:`niswitch.set_path`.
    For example, if you connect channels CH1 and CH3,and then channels CH2
    and CH3, an explicit path between channels CH1 and CH2 does not exist an
    error is returned

    



    :param channel1:


        Input one of the channel names of the desired path. Pass the other
        channel name as the channel 2 parameter. Refer to Devices Overview for
        valid channel names for the switch module. Examples of valid channel
        names: ch0, com0, ab0, r1, c2, cjtemp Default value: ""

        


    :type channel1: string
    :param channel2:


        Input one of the channel names of the desired path. Pass the other
        channel name as the channel 1 parameter. Refer to Devices Overview for
        valid channel names for the switch module. Examples of valid channel
        names: ch0, com0, ab0, r1, c2, cjtemp Default value: ""

        


    :type channel2: string
    :param buffer_size:


        Pass the number of bytes in the ViChar array you specify for the Path
        List parameter. If the current value of the attribute, including the
        terminating NULL byte, contains more bytes that you indicate in this
        parameter, the function copies Buffer Size - 1 bytes into the buffer,
        places an ASCII NULL byte at the end of the buffer, and returns the
        buffer size you must pass to get the entire value. For example, if the
        value is "R1->C1" and the Buffer Size is 4, the function places "R1-"
        into the buffer and returns 7. If you pass 0, you can pass VI\_NULL for
        the Path parameter. This enables you to find out the path size and to
        allocate the buffer of the appropriate size before calling this function
        again.

        


    :type buffer_size: int

.. function:: get_relay_count(relay_name)

    Returns the number of times the relay has changed from Closed to Open.
    Relay count is useful for tracking relay lifetime and usage. Call
    :py:func:`niswitch.wait_for_debounce` before :py:func:`niswitch.get_relay_count` to ensure an
    accurate count. Refer to the Relay Count topic in the NI Switches Help
    to determine if the switch module supports relay counting.

    



    :param relay_name:


        Name of the relay. Default value: None Examples of valid relay names:
        ch0, ab0, 1wire, hlselect Refer to Devices Overview for a list of valid
        relay names for the switch module.

        


    :type relay_name: string

    :rtype: int
    :return:


            The number of relay cycles.

            



.. function:: get_relay_name(index)

    Returns the relay name string that is in the relay list at the specified
    index. Use :py:func:`niswitch.get_relay_name` in a For Loop to get a complete list
    of valid relay names for the switch module. Use the Number of Relays
    attribute to determine the number of relays.

    



    :param index:


        A 1-based index into the channel table. Default value: 1 Maximum value:
        Value of Channel Count attribute.

        


    :type index: int
    :param relay_name_buffer_size:


        Pass the number of bytes in the ViChar array you specify for the Relay
        Name Buffer parameter. If the relay name string, including the
        terminating NUL byte, contains more bytes than you indicate in this
        parameter, the function copies Buffer Size - 1 bytes into the buffer,
        places an ASCII NUL byte at the end of the buffer, and returns the
        buffer size you must pass to get the entire value. For example, if the
        value is "123456" and the Buffer Size is 4, the function places "123"
        into the buffer and returns 7. If you pass a negative number, the
        function copies the value to the buffer regardless of the number of
        bytes in the value. If you pass 0, you can pass VI\_NULL for the
        Coercion Record buffer parameter. Default Value: None

        


    :type relay_name_buffer_size: int

.. function:: get_relay_position(relay_name)

    Returns the relay position for the relay specified in the Relay Name
    parameter.

    



    :param relay_name:


        Name of the relay. Default value: None Examples of valid relay names:
        ch0, ab0, 1wire, hlselect Refer to Devices Overview for a list of valid
        relay names for the switch module.

        


    :type relay_name: string

    :rtype: :py:data:`niswitch.RelayPosition`
    :return:


            Indicates whether the relay is open or closed. NISWITCH\_VAL\_OPEN 10
            NIWITCH\_VAL\_CLOSED 11

            



.. function:: init_with_topology(resource_name, topology='Configured Topology', simulate=False, reset_device=False)

    Returns a session handle used to identify the switch in all subsequent
    instrument driver calls and sets the topology of the switch.
    :py:func:`niswitch.init_with_topology` creates a new IVI instrument driver session
    for the switch specified in the resourceName parameter. The driver uses
    the topology specified in the topology parameter and overrides the
    topology specified in MAX. Note: When initializing an NI SwitchBlock
    device with topology, you must specify the toplogy created when you
    configured the device in MAX, using either
    NISWITCH\_TOPOLOGY\_CONFIGURED\_TOPOLOGY or the toplogy string of the
    device. Refer to the Initializing with Toplogy for NI SwitchBlock
    Devices topic in the NI Switches Help for information about determining
    the topology string of an NI SwitchBlock device. By default, the switch
    is reset to a known state. Enable simulation by specifying the topology
    and setting the simulate parameter to VI\_TRUE.

    



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

        


    :type resource_name: string
    :param topology:


        Pass the topology name you want to use for the switch you specify with
        Resource Name parameter. You can also pass
        NISWITCH\_TOPOLOGY\_CONFIGURED\_TOPOLOGY to use the last topology that
        was configured for the device in MAX. Default Value:
        NISWITCH\_TOPOLOGY\_CONFIGURED\_TOPOLOGY Valid Values:
        NISWITCH\_TOPOLOGY\_1127\_1\_WIRE\_64X1\_MUX
        NISWITCH\_TOPOLOGY\_1127\_2\_WIRE\_32X1\_MUX
        NISWITCH\_TOPOLOGY\_1127\_2\_WIRE\_4X8\_MATRIX
        NISWITCH\_TOPOLOGY\_1127\_4\_WIRE\_16X1\_MUX
        NISWITCH\_TOPOLOGY\_1127\_INDEPENDENT
        NISWITCH\_TOPOLOGY\_1128\_1\_WIRE\_64X1\_MUX
        NISWITCH\_TOPOLOGY\_1128\_2\_WIRE\_32X1\_MUX
        NISWITCH\_TOPOLOGY\_1128\_2\_WIRE\_4X8\_MATRIX
        NISWITCH\_TOPOLOGY\_1128\_4\_WIRE\_16X1\_MUX
        NISWITCH\_TOPOLOGY\_1128\_INDEPENDENT
        NISWITCH\_TOPOLOGY\_1129\_2\_WIRE\_16X16\_MATRIX
        NISWITCH\_TOPOLOGY\_1129\_2\_WIRE\_8X32\_MATRIX
        NISWITCH\_TOPOLOGY\_1129\_2\_WIRE\_4X64\_MATRIX
        NISWITCH\_TOPOLOGY\_1129\_2\_WIRE\_DUAL\_8X16\_MATRIX
        NISWITCH\_TOPOLOGY\_1129\_2\_WIRE\_DUAL\_4X32\_MATRIX
        NISWITCH\_TOPOLOGY\_1129\_2\_WIRE\_QUAD\_4X16\_MATRIX
        NISWITCH\_TOPOLOGY\_1130\_1\_WIRE\_256X1\_MUX
        NISWITCH\_TOPOLOGY\_1130\_1\_WIRE\_DUAL\_128X1\_MUX
        NISWITCH\_TOPOLOGY\_1130\_1\_WIRE\_4X64\_MATRIX
        NISWITCH\_TOPOLOGY\_1130\_1\_WIRE\_8x32\_MATRIX
        NISWITCH\_TOPOLOGY\_1130\_1\_WIRE\_OCTAL\_32X1\_MUX
        NISWITCH\_TOPOLOGY\_1130\_1\_WIRE\_QUAD\_64X1\_MUX
        NISWITCH\_TOPOLOGY\_1130\_1\_WIRE\_SIXTEEN\_16X1\_MUX
        NISWITCH\_TOPOLOGY\_1130\_2\_WIRE\_4X32\_MATRIX
        NISWITCH\_TOPOLOGY\_1130\_2\_WIRE\_128X1\_MUX
        NISWITCH\_TOPOLOGY\_1130\_2\_WIRE\_OCTAL\_16X1\_MUX
        NISWITCH\_TOPOLOGY\_1130\_2\_WIRE\_QUAD\_32X1\_MUX
        NISWITCH\_TOPOLOGY\_1130\_4\_WIRE\_64X1\_MUX
        NISWITCH\_TOPOLOGY\_1130\_4\_WIRE\_QUAD\_16X1\_MUX
        NISWITCH\_TOPOLOGY\_1130\_INDEPENDENT NISWITCH\_TOPOLOGY\_1160\_16\_SPDT
        NISWITCH\_TOPOLOGY\_1161\_8\_SPDT
        NISWITCH\_TOPOLOGY\_1163R\_OCTAL\_4X1\_MUX
        NISWITCH\_TOPOLOGY\_1166\_16\_DPDT NISWITCH\_TOPOLOGY\_1166\_32\_SPDT
        NISWITCH\_TOPOLOGY\_1167\_INDEPENDENT
        NISWITCH\_TOPOLOGY\_1169\_100\_SPST NISWITCH\_TOPOLOGY\_1169\_50\_DPST
        NISWITCH\_TOPOLOGY\_1175\_1\_WIRE\_196X1\_MUX
        NISWITCH\_TOPOLOGY\_1175\_2\_WIRE\_98X1\_MUX
        NISWITCH\_TOPOLOGY\_1175\_2\_WIRE\_95X1\_MUX
        NISWITCH\_TOPOLOGY\_1190\_QUAD\_4X1\_MUX
        NISWITCH\_TOPOLOGY\_1191\_QUAD\_4X1\_MUX
        NISWITCH\_TOPOLOGY\_1192\_8\_SPDT NISWITCH\_TOPOLOGY\_1193\_32X1\_MUX
        NISWITCH\_TOPOLOGY\_1193\_16X1\_TERMINATED\_MUX
        NISWITCH\_TOPOLOGY\_1193\_DUAL\_16X1\_MUX
        NISWITCH\_TOPOLOGY\_1193\_DUAL\_8X1\_TERMINATED\_MUX
        NISWITCH\_TOPOLOGY\_1193\_QUAD\_8X1\_MUX
        NISWITCH\_TOPOLOGY\_1193\_QUAD\_4X1\_TERMINATED\_MUX
        NISWITCH\_TOPOLOGY\_1193\_INDEPENDENT
        NISWITCH\_TOPOLOGY\_1194\_QUAD\_4X1\_MUX
        NISWITCH\_TOPOLOGY\_1195\_QUAD\_4X1\_MUX
        NISWITCH\_TOPOLOGY\_2501\_1\_WIRE\_48X1\_MUX
        NISWITCH\_TOPOLOGY\_2501\_1\_WIRE\_48X1\_AMPLIFIED\_MUX
        NISWITCH\_TOPOLOGY\_2501\_2\_WIRE\_24X1\_MUX
        NISWITCH\_TOPOLOGY\_2501\_2\_WIRE\_24X1\_AMPLIFIED\_MUX
        NISWITCH\_TOPOLOGY\_2501\_2\_WIRE\_DUAL\_12X1\_MUX
        NISWITCH\_TOPOLOGY\_2501\_2\_WIRE\_QUAD\_6X1\_MUX
        NISWITCH\_TOPOLOGY\_2501\_2\_WIRE\_4X6\_MATRIX
        NISWITCH\_TOPOLOGY\_2501\_4\_WIRE\_12X1\_MUX
        NISWITCH\_TOPOLOGY\_2503\_1\_WIRE\_48X1\_MUX
        NISWITCH\_TOPOLOGY\_2503\_2\_WIRE\_24X1\_MUX
        NISWITCH\_TOPOLOGY\_2503\_2\_WIRE\_DUAL\_12X1\_MUX
        NISWITCH\_TOPOLOGY\_2503\_2\_WIRE\_QUAD\_6X1\_MUX
        NISWITCH\_TOPOLOGY\_2503\_2\_WIRE\_4X6\_MATRIX
        NISWITCH\_TOPOLOGY\_2503\_4\_WIRE\_12X1\_MUX
        NISWITCH\_TOPOLOGY\_2510\_INDEPENDENT
        NISWITCH\_TOPOLOGY\_2512\_INDEPENDENT
        NISWITCH\_TOPOLOGY\_2514\_INDEPENDENT
        NISWITCH\_TOPOLOGY\_2515\_INDEPENDENT NISWITCH\_TOPOLOGY\_2520\_80\_SPST
        NISWITCH\_TOPOLOGY\_2521\_40\_DPST NISWITCH\_TOPOLOGY\_2522\_53\_SPDT
        NISWITCH\_TOPOLOGY\_2523\_26\_DPDT
        NISWITCH\_TOPOLOGY\_2524\_1\_WIRE\_128X1\_MUX
        NISWITCH\_TOPOLOGY\_2524\_1\_WIRE\_DUAL\_64X1\_MUX
        NISWITCH\_TOPOLOGY\_2524\_1\_WIRE\_QUAD\_32X1\_MUX
        NISWITCH\_TOPOLOGY\_2524\_1\_WIRE\_OCTAL\_16X1\_MUX
        NISWITCH\_TOPOLOGY\_2524\_1\_WIRE\_SIXTEEN\_8X1\_MUX
        NISWITCH\_TOPOLOGY\_2525\_2\_WIRE\_64X1\_MUX
        NISWITCH\_TOPOLOGY\_2525\_2\_WIRE\_DUAL\_32X1\_MUX
        NISWITCH\_TOPOLOGY\_2525\_2\_WIRE\_QUAD\_16X1\_MUX
        NISWITCH\_TOPOLOGY\_2525\_2\_WIRE\_OCTAL\_8X1\_MUX
        NISWITCH\_TOPOLOGY\_2525\_2\_WIRE\_SIXTEEN\_4X1\_MUX
        NISWITCH\_TOPOLOGY\_2526\_1\_WIRE\_158X1\_MUX
        NISWITCH\_TOPOLOGY\_2526\_2\_WIRE\_79X1\_MUX
        NISWITCH\_TOPOLOGY\_2527\_1\_WIRE\_64X1\_MUX
        NISWITCH\_TOPOLOGY\_2527\_1\_WIRE\_DUAL\_32X1\_MUX
        NISWITCH\_TOPOLOGY\_2527\_2\_WIRE\_32X1\_MUX
        NISWITCH\_TOPOLOGY\_2527\_2\_WIRE\_DUAL\_16X1\_MUX
        NISWITCH\_TOPOLOGY\_2527\_4\_WIRE\_16X1\_MUX
        NISWITCH\_TOPOLOGY\_2527\_INDEPENDENT
        NISWITCH\_TOPOLOGY\_2529\_2\_WIRE\_DUAL\_4X16\_MATRIX
        NISWITCH\_TOPOLOGY\_2529\_2\_WIRE\_8X16\_MATRIX
        NISWITCH\_TOPOLOGY\_2529\_2\_WIRE\_4X32\_MATRIX
        NISWITCH\_TOPOLOGY\_2530\_1\_WIRE\_128X1\_MUX
        NISWITCH\_TOPOLOGY\_2530\_1\_WIRE\_DUAL\_64X1\_MUX
        NISWITCH\_TOPOLOGY\_2530\_1\_WIRE\_4x32\_MATRIX
        NISWITCH\_TOPOLOGY\_2530\_1\_WIRE\_8x16\_MATRIX
        NISWITCH\_TOPOLOGY\_2530\_1\_WIRE\_OCTAL\_16X1\_MUX
        NISWITCH\_TOPOLOGY\_2530\_1\_WIRE\_QUAD\_32X1\_MUX
        NISWITCH\_TOPOLOGY\_2530\_2\_WIRE\_4x16\_MATRIX
        NISWITCH\_TOPOLOGY\_2530\_2\_WIRE\_64X1\_MUX
        NISWITCH\_TOPOLOGY\_2530\_2\_WIRE\_DUAL\_32X1\_MUX
        NISWITCH\_TOPOLOGY\_2530\_2\_WIRE\_QUAD\_16X1\_MUX
        NISWITCH\_TOPOLOGY\_2530\_4\_WIRE\_32X1\_MUX
        NISWITCH\_TOPOLOGY\_2530\_4\_WIRE\_DUAL\_16X1\_MUX
        NISWITCH\_TOPOLOGY\_2530\_INDEPENDENT
        NISWITCH\_TOPOLOGY\_2531\_1\_WIRE\_4X128\_MATRIX
        NISWITCH\_TOPOLOGY\_2531\_1\_WIRE\_8X64\_MATRIX
        NISWITCH\_TOPOLOGY\_2531\_1\_WIRE\_DUAL\_4X64\_MATRIX
        NISWITCH\_TOPOLOGY\_2531\_1\_WIRE\_DUAL\_8X32\_MATRIX
        NISWITCH\_TOPOLOGY\_2531\_2\_WIRE\_4X64\_MATRIX
        NISWITCH\_TOPOLOGY\_2531\_2\_WIRE\_8X32\_MATRIX
        NISWITCH\_TOPOLOGY\_2532\_1\_WIRE\_16X32\_MATRIX
        NISWITCH\_TOPOLOGY\_2532\_1\_WIRE\_4X128\_MATRIX
        NISWITCH\_TOPOLOGY\_2532\_1\_WIRE\_8X64\_MATRIX
        NISWITCH\_TOPOLOGY\_2532\_1\_WIRE\_DUAL\_16X16\_MATRIX
        NISWITCH\_TOPOLOGY\_2532\_1\_WIRE\_DUAL\_4X64\_MATRIX
        NISWITCH\_TOPOLOGY\_2532\_1\_WIRE\_DUAL\_8X32\_MATRIX
        NISWITCH\_TOPOLOGY\_2532\_1\_WIRE\_SIXTEEN\_2X16\_MATRIX
        NISWITCH\_TOPOLOGY\_2532\_2\_WIRE\_16X16\_MATRIX
        NISWITCH\_TOPOLOGY\_2532\_2\_WIRE\_4X64\_MATRIX
        NISWITCH\_TOPOLOGY\_2532\_2\_WIRE\_8X32\_MATRIX
        NISWITCH\_TOPOLOGY\_2532\_2\_WIRE\_DUAL\_4X32\_MATRIX
        NISWITCH\_TOPOLOGY\_2533\_1\_WIRE\_4X64\_MATRIX
        NISWITCH\_TOPOLOGY\_2534\_1\_WIRE\_8X32\_MATRIX
        NISWITCH\_TOPOLOGY\_2535\_1\_WIRE\_4X136\_MATRIX
        NISWITCH\_TOPOLOGY\_2536\_1\_WIRE\_8X68\_MATRIX
        NISWITCH\_TOPOLOGY\_2540\_1\_WIRE\_8X9\_MATRIX
        NISWITCH\_TOPOLOGY\_2541\_1\_WIRE\_8X12\_MATRIX
        NISWITCH\_TOPOLOGY\_2542\_QUAD\_2X1\_TERMINATED\_MUX
        NISWITCH\_TOPOLOGY\_2543\_DUAL\_4X1\_TERMINATED\_MUX
        NISWITCH\_TOPOLOGY\_2544\_8X1\_TERMINATED\_MUX
        NISWITCH\_TOPOLOGY\_2545\_4X1\_TERMINATED\_MUX
        NISWITCH\_TOPOLOGY\_2546\_DUAL\_4X1\_MUX
        NISWITCH\_TOPOLOGY\_2547\_8X1\_MUX NISWITCH\_TOPOLOGY\_2548\_4\_SPDT
        NISWITCH\_TOPOLOGY\_2549\_TERMINATED\_2\_SPDT
        NISWITCH\_TOPOLOGY\_2554\_4X1\_MUX
        NISWITCH\_TOPOLOGY\_2555\_4X1\_TERMINATED\_MUX
        NISWITCH\_TOPOLOGY\_2556\_DUAL\_4X1\_MUX
        NISWITCH\_TOPOLOGY\_2557\_8X1\_MUX NISWITCH\_TOPOLOGY\_2558\_4\_SPDT
        NISWITCH\_TOPOLOGY\_2559\_TERMINATED\_2\_SPDT
        NISWITCH\_TOPOLOGY\_2564\_16\_SPST NISWITCH\_TOPOLOGY\_2564\_8\_DPST
        NISWITCH\_TOPOLOGY\_2565\_16\_SPST NISWITCH\_TOPOLOGY\_2566\_16\_SPDT
        NISWITCH\_TOPOLOGY\_2566\_8\_DPDT NISWITCH\_TOPOLOGY\_2567\_INDEPENDENT
        NISWITCH\_TOPOLOGY\_2568\_15\_DPST NISWITCH\_TOPOLOGY\_2568\_31\_SPST
        NISWITCH\_TOPOLOGY\_2569\_100\_SPST NISWITCH\_TOPOLOGY\_2569\_50\_DPST
        NISWITCH\_TOPOLOGY\_2570\_20\_DPDT NISWITCH\_TOPOLOGY\_2570\_40\_SPDT
        NISWITCH\_TOPOLOGY\_2571\_66\_SPDT
        NISWITCH\_TOPOLOGY\_2575\_1\_WIRE\_196X1\_MUX
        NISWITCH\_TOPOLOGY\_2575\_2\_WIRE\_98X1\_MUX
        NISWITCH\_TOPOLOGY\_2575\_2\_WIRE\_95X1\_MUX
        NISWITCH\_TOPOLOGY\_2576\_2\_WIRE\_64X1\_MUX
        NISWITCH\_TOPOLOGY\_2576\_2\_WIRE\_DUAL\_32X1\_MUX
        NISWITCH\_TOPOLOGY\_2576\_2\_WIRE\_OCTAL\_8X1\_MUX
        NISWITCH\_TOPOLOGY\_2576\_2\_WIRE\_QUAD\_16X1\_MUX
        NISWITCH\_TOPOLOGY\_2576\_2\_WIRE\_SIXTEEN\_4X1\_MUX
        NISWITCH\_TOPOLOGY\_2576\_INDEPENDENT
        NISWITCH\_TOPOLOGY\_2584\_1\_WIRE\_12X1\_MUX
        NISWITCH\_TOPOLOGY\_2584\_1\_WIRE\_DUAL\_6X1\_MUX
        NISWITCH\_TOPOLOGY\_2584\_2\_WIRE\_6X1\_MUX
        NISWITCH\_TOPOLOGY\_2584\_INDEPENDENT
        NISWITCH\_TOPOLOGY\_2585\_1\_WIRE\_10X1\_MUX
        NISWITCH\_TOPOLOGY\_2586\_10\_SPST NISWITCH\_TOPOLOGY\_2586\_5\_DPST
        NISWITCH\_TOPOLOGY\_2590\_4X1\_MUX NISWITCH\_TOPOLOGY\_2591\_4X1\_MUX
        NISWITCH\_TOPOLOGY\_2593\_16X1\_MUX
        NISWITCH\_TOPOLOGY\_2593\_8X1\_TERMINATED\_MUX
        NISWITCH\_TOPOLOGY\_2593\_DUAL\_8X1\_MUX
        NISWITCH\_TOPOLOGY\_2593\_DUAL\_4X1\_TERMINATED\_MUX
        NISWITCH\_TOPOLOGY\_2593\_INDEPENDENT NISWITCH\_TOPOLOGY\_2594\_4X1\_MUX
        NISWITCH\_TOPOLOGY\_2595\_4X1\_MUX
        NISWITCH\_TOPOLOGY\_2596\_DUAL\_6X1\_MUX
        NISWITCH\_TOPOLOGY\_2597\_6X1\_TERMINATED\_MUX
        NISWITCH\_TOPOLOGY\_2598\_DUAL\_TRANSFER
        NISWITCH\_TOPOLOGY\_2599\_2\_SPDT NISWITCH\_TOPOLOGY\_2720\_INDEPENDENT
        NISWITCH\_TOPOLOGY\_2722\_INDEPENDENT
        NISWITCH\_TOPOLOGY\_2725\_INDEPENDENT
        NISWITCH\_TOPOLOGY\_2727\_INDEPENDENT
        NISWITCH\_TOPOLOGY\_2737\_2\_WIRE\_4X64\_MATRIX
        NISWITCH\_TOPOLOGY\_2738\_2\_WIRE\_8X32\_MATRIX
        NISWITCH\_TOPOLOGY\_2739\_2\_WIRE\_16X16\_MATRIX
        NISWITCH\_TOPOLOGY\_2746\_QUAD\_4X1\_MUX
        NISWITCH\_TOPOLOGY\_2747\_DUAL\_8X1\_MUX
        NISWITCH\_TOPOLOGY\_2748\_16X1\_MUX
        NISWITCH\_TOPOLOGY\_2790\_INDEPENDENT
        NISWITCH\_TOPOLOGY\_2796\_DUAL\_6X1\_MUX
        NISWITCH\_TOPOLOGY\_2797\_6X1\_TERMINATED\_MUX
        NISWITCH\_TOPOLOGY\_2798\_DUAL\_TRANSFER
        NISWITCH\_TOPOLOGY\_2799\_2\_SPDT

        


    :type topology: string
    :param simulate:


        Enables simulation of the switch module specified in the resource name
        parameter. Valid Values: VI\_TRUE - simulate VI\_FALSE - Don't simulate
        (Default Value)

        


    :type simulate: bool
    :param reset_device:


        Specifies whether to reset the switch module during the initialization
        process. Valid Values: VI\_TRUE - Reset Device (Default Value) VI\_FALSE
        - Currently unsupported. The device will not reset.

        


    :type reset_device: bool

    :rtype: int
    :return:


            A particular NI-SWITCH session established with
            :py:func:`niswitch.init_with_topology`, :py:func:`niswitch.init_with_options`, or :py:func:`niswitch.init`
            and used for all subsequent NI-SWITCH calls.

            



.. function:: is_debounced()

    Indicates if all created paths have settled by returning the value of
    the :py:data:`niswitch.IS\_DEBOUNCED` attribute.

    



    :rtype: bool
    :return:


            VI\_TRUE indicates that all created paths have settled. VI\_FALSE
            indicates that all created paths have not settled.

            



.. function:: is_scanning()

    Indicates the status of the scan.

    



    :rtype: bool
    :return:


            The driver returns the value of :py:data:`niswitch.IS\_SCANNING` attribute.
            VI\_TRUE indicates that the switch device is scanning. VI\_FALSE
            indicates that the switch device is idle.

            



.. function:: relay_control(relay_name, relay_action)

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

        


    :type relay_name: string
    :param relay_action:


        Specifies whether to open or close a given relay. Default value: Relay
        Close Defined values: NISWITCH\_VAL\_OPEN\_RELAY
        NISWITCH\_VAL\_CLOSE\_RELAY (Default Value)

        


    :type relay_action: :py:data:`niswitch.RelayAction`

.. function:: reset_with_defaults()

    Resets the switch module and applies initial user specified settings
    from the logical name used to initialize the session. If the session was
    created without a logical name, this function is equivalent to
    :py:func:`niswitch.reset`.

    



.. function:: route_scan_advanced_output(scan_advanced_output_connector, scan_advanced_output_bus_line, invert=False)

    Routes the scan advanced output trigger from a trigger bus line (TTLx)
    to the front or rear connector.

    



    :param scan_advanced_output_connector:


        The scan advanced trigger destination. Valid locations are the
        NISWITCH\_VAL\_FRONTCONNECTOR and NISWITCH\_VAL\_REARCONNECTOR. Default
        value: NISWITCH\_VAL\_FRONTCONNECTOR

        


    :type scan_advanced_output_connector: :py:data:`niswitch.ScanAdvancedOutput`
    :param scan_advanced_output_bus_line:


        The trigger line to route the scan advanced output trigger from the
        front or rear connector. Select NISWITCH\_VAL\_NONE to break an existing
        route. Default value: None Valid Values: NISWITCH\_VAL\_NONE
        NISWITCH\_VAL\_TTL0 NISWITCH\_VAL\_TTL1 NISWITCH\_VAL\_TTL2
        NISWITCH\_VAL\_TTL3 NISWITCH\_VAL\_TTL4 NISWITCH\_VAL\_TTL5
        NISWITCH\_VAL\_TTL6 NISWITCH\_VAL\_TTL7

        


    :type scan_advanced_output_bus_line: :py:data:`niswitch.ScanAdvancedOutput`
    :param invert:


        If VI\_TRUE, inverts the input trigger signal from falling to rising or
        vice versa. Default value: VI\_FALSE

        


    :type invert: bool

.. function:: route_trigger_input(trigger_input_connector, trigger_input_bus_line, invert=False)

    Routes the input trigger from the front or rear connector to a trigger
    bus line (TTLx). To disconnect the route, call this function again and
    specify None for trigger bus line parameter.

    



    :param trigger_input_connector:


        The location of the input trigger source on the switch module. Valid
        locations are the NISWITCH\_VAL\_FRONTCONNECTOR and
        NISWITCH\_VAL\_REARCONNECTOR. Default value:
        NISWITCH\_VAL\_FRONTCONNECTOR

        


    :type trigger_input_connector: :py:data:`niswitch.TriggerInput`
    :param trigger_input_bus_line:


        The trigger line to route the input trigger. Select NISWITCH\_VAL\_NONE
        to break an existing route. Default value: None Valid Values:
        NISWITCH\_VAL\_NONE NISWITCH\_VAL\_TTL0 NISWITCH\_VAL\_TTL1
        NISWITCH\_VAL\_TTL2 NISWITCH\_VAL\_TTL3 NISWITCH\_VAL\_TTL4
        NISWITCH\_VAL\_TTL5 NISWITCH\_VAL\_TTL6 NISWITCH\_VAL\_TTL7

        


    :type trigger_input_bus_line: :py:data:`niswitch.TriggerInput`
    :param invert:


        If VI\_TRUE, inverts the input trigger signal from falling to rising or
        vice versa. Default value: VI\_FALSE

        


    :type invert: bool

.. function:: send_software_trigger()

    Sends a software trigger to the switch module specified in the NI-SWITCH
    session. When the trigger input is set to NISWITCH\_VAL\_SOFTWARE\_TRIG
    through either the :py:func:`niswitch.configure_scan_trigger` or the
    :py:data:`niswitch.TRIGGER\_INPUT` attribute, the scan does not proceed from
    a semi-colon (wait for trigger) until :py:func:`niswitch.send_software_trigger` is
    called.

    



.. function:: set_continuous_scan(continuous_scan)

    Sets the to loop continuously through the scan list or to stop scanning
    after one pass through the scan list.

    



    :param continuous_scan:


        If VI\_TRUE, loops continuously through the scan list during scanning.
        If VI\_FALSE, the scan stops after one pass through the scan list.
        Default value: VI\_FALSE

        


    :type continuous_scan: bool

.. function:: set_path(path_list)

    Connects two channels by specifying an explicit path in the path list
    parameter. :py:func:`niswitch.set_path` is particularly useful where path
    repeatability is important, such as in calibrated signal paths. If this
    is not necessary, use :py:func:`niswitch.connect`.

    



    :param path_list:


        A string composed of comma-separated paths between channel 1 and channel
        2. The first and last names in the path are the endpoints of the path.
        Every other channel in the path are configuration channels. Example of a
        valid path list string: ch0->com0, com0->ab0. In this example, com0 is a
        configuration channel. Default value: None Obtain the path list for a
        previously created path with :py:func:`niswitch.get_path`.

        


    :type path_list: string

.. function:: wait_for_debounce(maximum_time_ms=5000)

    Pauses until all created paths have settled. If the time you specify
    with the Maximum Time (ms) parameter elapsed before the switch paths
    have settled, this function returns the
    NISWITCH\_ERROR\_MAX\_TIME\_EXCEEDED error.

    



    :param maximum_time_ms:


        Specifies the maximum length of time to wait for all relays in the
        switch module to activate or deactivate. If the specified time elapses
        before all relays active or deactivate, a timeout error is returned.
        Default Value:5000 ms

        


    :type maximum_time_ms: int

.. function:: wait_for_scan_complete(maximum_time_ms=5000)

    Pauses until the switch module stops scanning or the maximum time has
    elapsed and returns a timeout error. If the time you specify with the
    Maximum Time (ms) parameter elapsed before the scanning operation has
    finished, this function returns the NISWITCH\_ERROR\_MAX\_TIME\_EXCEEDED
    error.

    



    :param maximum_time_ms:


        Specifies the maximum length of time to wait for the switch module to
        stop scanning. If the specified time elapses before the scan ends,
        NISWITCH\_ERROR\_MAX\_TIME\_EXCEEDED error is returned. Default
        Value:5000 ms

        


    :type maximum_time_ms: int

.. function:: reset()

    Disconnects all created paths and returns the switch module to the state
    at initialization. Configuration channel and source channel settings
    remain unchanged.

    



.. function:: self_test()

    Verifies that the driver can communicate with the switch module.

    



    :rtype: tuple (self_test_result, self_test_message)

        WHERE

        self_test_result (int): 


            Value returned from the switch device self-test. Passed 0 Failed 1

            


        self_test_message (string): 


            Self-test response string from the switch device. You must pass a ViChar
            array with at least 256 bytes.

            




