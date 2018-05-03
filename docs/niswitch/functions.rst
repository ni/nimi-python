niswitch.Session methods
========================

.. py:currentmodule:: niswitch.Session

.. py:method:: abort()

    Aborts the scan in progress. Initiate a scan with
    :py:meth:`niswitch.Session._initiate_scan`. If the switch module is not scanning,
    NISWITCH_ERROR_NO_SCAN_IN_PROGRESS error is returned.

    



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
            ------------------------------------ :py:data:`~niswitch.NISWITCH_VAL_PATH_AVAILABLE` 1
            :py:data:`~niswitch.NISWITCH_VAL_PATH_EXISTS` 2 :py:data:`~niswitch.NISWITCH_VAL_PATH_UNSUPPORTED` 3
            :py:data:`~niswitch.NISWITCH_VAL_RSRC_IN_USE` 4 :py:data:`~niswitch.NISWITCH_VAL_SOURCE_CONFLICT` 5
            :py:data:`~niswitch.NISWITCH_VAL_CHANNEL_NOT_AVAILABLE` 6 Notes: (1)
            :py:data:`~niswitch.NISWITCH_VAL_PATH_AVAILABLE` indicates that the driver can create the
            path at this time. (2) :py:data:`~niswitch.NISWITCH_VAL_PATH_EXISTS` indicates that the
            path already exists. (3) :py:data:`~niswitch.NISWITCH_VAL_PATH_UNSUPPORTED` indicates that
            the instrument is not capable of creating a path between the channels
            you specify. (4) :py:data:`~niswitch.NISWITCH_VAL_RSRC_IN_USE` indicates that although
            the path is valid, the driver cannot create the path at this moment
            because the switch device is currently using one or more of the required
            channels to create another path. You must destroy the other path before
            creating this one. (5) :py:data:`~niswitch.NISWITCH_VAL_SOURCE_CONFLICT` indicates that
            the instrument cannot create a path because both channels are connected
            to a different source channel. (6)
            :py:data:`~niswitch.NISWITCH_VAL_CHANNEL_NOT_AVAILABLE` indicates that the driver cannot
            create a path between the two channels because one of the channels is a
            configuration channel and thus unavailable for external connections.

            

            .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.



.. py:method:: commit()

    Downloads the configured scan list and trigger settings to hardware.
    Calling :py:meth:`niswitch.Session.commit` optional as it is implicitly called during
    :py:meth:`niswitch.Session._initiate_scan`. Use :py:meth:`niswitch.Session.commit` to arm triggers in a given
    order or to control when expensive hardware operations are performed.

    



.. py:method:: configure_scan_list(scanlist, scan_mode=niswitch.ScanMode.BREAK_BEFORE_MAKE)

    Configures the scan list and scan mode used for scanning. Refer to
    Devices Overview to determine if the switch module supports scanning.
    The scan list is comprised of a list of channel connections separated by
    semi-colons. For example, the following scan list will scan the first
    three channels of a multiplexer: com0->ch0; com0->ch1; com0->ch2; Refer
    to Scan Lists for more information on scan list syntax To see the status
    of the scan, call either :py:meth:`niswitch.Session.IsScanning` or
    :py:meth:`niswitch.Session.wait_for_scan_complete`. Use the :py:meth:`niswitch.Session.configure_scan_trigger`
    method to configure the scan trigger. Use the :py:meth:`niswitch.Session._initiate_scan`
    method to start the scan.

    

    .. note:: One or more of the referenced methods are not in the Python API for this driver.



    :param scanlist:


        The scan list to use. The driver uses this value to set the Scan List
        property. Default value: None

        


    :type scanlist: str
    :param scan_mode:


        Specifies how the switch module breaks existing connections when
        scanning. The driver uses this value to set the Scan Mode property.
        Refer to scan modes for more information. Default value: Break Before
        Make

        


    :type scan_mode: :py:data:`niswitch.ScanMode`

.. py:method:: configure_scan_trigger(trigger_input, scan_advanced_output, scan_delay=datetime.timedelta(seconds=0.0))

    Configures the scan triggers for the scan list established with
    :py:meth:`niswitch.Session.configure_scan_list`. Refer to Devices Overview to determine if
    the switch module supports scanning. :py:meth:`niswitch.Session.configure_scan_trigger` sets
    the location that the switch expects to receive an input trigger to
    advance through the scan list. This method also sets the location
    where it outputs a scan advanced signal after it completes an entry in
    the scan list.

    



    :param trigger_input:


        Trigger source you want the switch module to use during scanning. The
        driver uses this value to set the :py:data:`niswitch.Session.trigger_input`
        property. The switch device waits for the trigger you specify when it
        encounters a semicolon in the scanlist. When the trigger occurs, the
        switch device advances to the next entry in the scanlist. Refer to the
        :py:data:`niswitch.Session.trigger_input` topic in the NI Switches Help for a list
        of valid values.

        


    :type trigger_input: :py:data:`niswitch.TriggerInput`
    :param scan_advanced_output:


        Output destination of the scan advanced trigger signal. The driver uses
        this value to set the :py:data:`niswitch.Session.scan_advanced_output` property.
        After the switch processes each entry in the scan list, it waits the
        length of time you specify in the Scan Delay parameter and then asserts
        a trigger on the line you specify with this parameter. Refer to the
        :py:data:`niswitch.Session.scan_advanced_output` topic in the NI Switches Help for
        a list of valid values.

        


    :type scan_advanced_output: :py:data:`niswitch.ScanAdvancedOutput`
    :param scan_delay:


        The minimum length of time you want the switch device to wait after it
        creates a path until it asserts a trigger on the scan advanced output
        line. The driver uses this value to set the Scan Delay property. The
        scan delay is in addition to the settling time.The driver uses this
        value to set the :py:data:`niswitch.Session.scan_delay` property. Express this
        value in seconds. Default value: 0.0 s

        


    :type scan_delay: float in seconds or datetime.timedelta

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

.. py:method:: disable()

    Places the switch module in a quiescent state where it has minimal or no
    impact on the system to which it is connected. All channels are
    disconnected and any scan in progress is aborted.

    



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

.. py:method:: disconnect_all()

    Breaks all existing paths. If the switch module cannot break all paths,
    NISWITCH_WARN_PATH_REMAINS warning is returned.

    



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

.. py:method:: get_channel_name(index)

    Returns the channel string that is in the channel table at the specified
    index. Use :py:meth:`niswitch.Session.get_channel_name` in a For Loop to get a complete list
    of valid channel names for the switch module. Use the Channel Count
    property to determine the number of channels.

    



    :param index:


        A 1-based index into the channel table. Default value: 1 Maximum value:
        Value of Channel Count property.

        


    :type index: int

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

            



.. py:method:: get_relay_name(index)

    Returns the relay name string that is in the relay list at the specified
    index. Use :py:meth:`niswitch.Session.get_relay_name` in a For Loop to get a complete list
    of valid relay names for the switch module. Use the Number of Relays
    property to determine the number of relays.

    



    :param index:


        A 1-based index into the channel table. Default value: 1 Maximum value:
        Value of Channel Count property.

        


    :type index: int

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


            Indicates whether the relay is open or closed. :py:data:`~niswitch.NISWITCH_VAL_OPEN` 10
            NIWITCH_VAL_CLOSED 11

            

            .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.



.. py:method:: lock_session(caller_has_lock)

    | Obtains a multithread lock on the device session. Before doing so, the
      software waits until all other execution threads release their locks
      on the device session.
    | Other threads may have obtained a lock on this session for the
      following reasons:

    -  The application called the :py:meth:`nidcpower.Session.lock_session` method.
    -  A call to NI-DCPower locked the session.
    -  A call to the IVI engine locked the session.
    -  After a call to the :py:meth:`nidcpower.Session.lock_session` method returns
       successfully, no other threads can access the device session until
       you call the :py:meth:`nidcpower.Session.unlock_session` method.
    -  Use the :py:meth:`nidcpower.Session.lock_session` method and the
       :py:meth:`nidcpower.Session.unlock_session` method around a sequence of calls to
       instrument driver methods if you require that the device retain its
       settings through the end of the sequence.

    You can safely make nested calls to the :py:meth:`nidcpower.Session.lock_session` method
    within the same thread. To completely unlock the session, you must
    balance each call to the :py:meth:`nidcpower.Session.lock_session` method with a call to
    the :py:meth:`nidcpower.Session.unlock_session` method. If, however, you use
    **Caller_Has_Lock** in all calls to the :py:meth:`nidcpower.Session.lock_session` and
    :py:meth:`nidcpower.Session.unlock_session` method within a method, the IVI Library
    locks the session only once within the method regardless of the number
    of calls you make to the :py:meth:`nidcpower.Session.lock_session` method. This behavior
    allows you to call the :py:meth:`nidcpower.Session.unlock_session` method just once at
    the end of the method.





    :param caller_has_lock:


        This parameter is optional. If you do not want to use this parameter, pass None.

        Use this parameter in complex methods to keep track of whether you
        obtain a lock and therefore need to unlock the session. Pass False to the initial
        lock_session call and store the return value into a variable. Pass in the variable as well
        as putting the return value into the same variable for each call to lock_session or
        unlock_session.




    :type caller_has_lock: bool

    :rtype: bool
    :return:


            This parameter is optional. If you do not want to use this parameter, pass None.

            Use this parameter in complex methods to keep track of whether you
            obtain a lock and therefore need to unlock the session. Pass False to the initial
            lock_session call and store the return value into a variable. Pass in the variable as well
            as putting the return value into the same variable for each call to lock_session or
            unlock_session.




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
        Close Defined values: :py:data:`~niswitch.NISWITCH_VAL_OPEN_RELAY`
        :py:data:`~niswitch.NISWITCH_VAL_CLOSE_RELAY` (Default Value)

        

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


    :type relay_action: :py:data:`niswitch.RelayAction`

.. py:method:: reset()

    Disconnects all created paths and returns the switch module to the state
    at initialization. Configuration channel and source channel settings
    remain unchanged.

    



.. py:method:: reset_with_defaults()

    Resets the switch module and applies initial user specified settings
    from the logical name used to initialize the session. If the session was
    created without a logical name, this method is equivalent to
    :py:meth:`niswitch.Session.reset`.

    



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



.. py:method:: send_software_trigger()

    Sends a software trigger to the switch module specified in the NI-SWITCH
    session. When the trigger input is set to :py:data:`~niswitch.TriggerInput.SOFTWARE_TRIG`
    through either the :py:meth:`niswitch.Session.configure_scan_trigger` or the
    :py:data:`niswitch.Session.trigger_input` property, the scan does not proceed from
    a semi-colon (wait for trigger) until :py:meth:`niswitch.Session.send_software_trigger` is
    called.

    



.. py:method:: set_continuous_scan(continuous_scan)

    Sets the to loop continuously through the scan list or to stop scanning
    after one pass through the scan list.

    



    :param continuous_scan:


        If True, loops continuously through the scan list during scanning.
        If False, the scan stops after one pass through the scan list.
        Default value: False

        


    :type continuous_scan: bool

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

.. py:method:: unlock_session(caller_has_lock)

    Releases a lock that you acquired on an device session using
    :py:meth:`nidcpower.Session.lock_session`. Refer to :py:meth:`nidcpower.Session.lock_session` for additional
    information on session locks.





    :param caller_has_lock:


        This parameter is optional. If you do not want to use this parameter, pass None.

        Use this parameter in complex methods to keep track of whether you
        obtain a lock and therefore need to unlock the session. Pass False to the initial
        lock_session call and store the return value into a variable. Pass in the variable as well
        as putting the return value into the same variable for each call to lock_session or
        unlock_session.




    :type caller_has_lock: bool

    :rtype: bool
    :return:


            This parameter is optional. If you do not want to use this parameter, pass None.

            Use this parameter in complex methods to keep track of whether you
            obtain a lock and therefore need to unlock the session. Pass False to the initial
            lock_session call and store the return value into a variable. Pass in the variable as well
            as putting the return value into the same variable for each call to lock_session or
            unlock_session.



.. py:method:: wait_for_debounce(maximum_time_ms=datetime.timedelta(milliseconds=5000))

    Pauses until all created paths have settled. If the time you specify
    with the Maximum Time (ms) parameter elapsed before the switch paths
    have settled, this method returns the
    NISWITCH_ERROR_MAX_TIME_EXCEEDED error.

    



    :param maximum_time_ms:


        Specifies the maximum length of time to wait for all relays in the
        switch module to activate or deactivate. If the specified time elapses
        before all relays active or deactivate, a timeout error is returned.
        Default Value:5000 ms

        


    :type maximum_time_ms: float in seconds or datetime.timedelta

.. py:method:: wait_for_scan_complete(maximum_time_ms=datetime.timedelta(milliseconds=5000))

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

        


    :type maximum_time_ms: float in seconds or datetime.timedelta


