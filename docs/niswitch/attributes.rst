niswitch.Session properties
===========================

.. py:currentmodule:: niswitch

.. py:attribute:: analog_bus_sharing_enable

    Enables or disables sharing of an analog bus line so that multiple
    NI SwitchBlock devices may connect to it simultaneously. To enable
    multiple NI SwitchBlock devices to share an analog bus line, set this
    property to TRUE for each device on the channel that corresponds with
    the shared analog bus line. The default value for all devices is FALSE,
    which disables sharing of the analog bus.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__ `Using the
    Analog Bus on an NI SwitchBlock
    Carrier <switch.chm::/SwitchBlock_analog_bus_reservation.html>`__




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        analog_bus_sharing_enable.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        analog_bus_sharing_enable.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].analog_bus_sharing_enable = var
            var = session['0,1'].analog_bus_sharing_enable

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | bool       |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Channel Configuration:Analog Bus Sharing Enable**
            - C Attribute: **NISWITCH_ATTR_ANALOG_BUS_SHARING_ENABLE**

.. py:attribute:: bandwidth

    Returns the bandwidth for the channel in hertz.

    **Related topics**

    `Bandwidth and Insertion Loss <SWITCH.chm::/bandwidth.html>`__ `niSwitch
    Properties <switchpropref.chm::/cniSwitch.html>`__ `RF Switching
    Considerations <SWITCH.chm::/rf.html>`__




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        bandwidth.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        bandwidth.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].bandwidth = var
            var = session['0,1'].bandwidth

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | float     |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | True      |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Module Characteristics:Bandwidth**
            - C Attribute: **NISWITCH_ATTR_BANDWIDTH**

.. py:attribute:: cabled_module_scan_advanced_bus

    This property has been deprecated and might be removed from a future
    release of NI-SWITCH. Use `niSwitch Route Scan Advanced
    Output <switchviref.chm::/niSwitch_Route_Scan_Advanced_Output.html>`__
    VI instead.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Obsolete Attributes:Cabled Module Scan Advanced Bus**
            - C Attribute: **NISWITCH_ATTR_CABLED_MODULE_SCAN_ADVANCED_BUS**

.. py:attribute:: cabled_module_trigger_bus

    This property has been deprecated and might be removed from a future
    release of NI-SWITCH. Use the `niSwitch Route Trigger
    Input <switchviref.chm::/niSwitch_Route_Trigger_Input.html>`__ VI
    instead.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Obsolete Attributes:Cabled Module Trigger Bus**
            - C Attribute: **NISWITCH_ATTR_CABLED_MODULE_TRIGGER_BUS**

.. py:attribute:: cache

    Specifies whether to cache the value of properties. The default value is
    TRUE. Use the `niSwitch Initialize With
    Options <switchviref.chm::/niSwitch_Initialize_With_Options.html>`__ VI
    to override the default value.

    Set this property to TRUE to ensure the instrument driver tracks the
    current instrument settings and avoid sending redundant commands to the
    instrument. The instrument driver can always cache or never cache
    regardless of the setting of this property.

    **Related topics**

    `niSwitch Initialize With
    Options <switchviref.chm::/niSwitch_Initialize_With_Options.html>`__
    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | bool       |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Inherent IVI Attributes:User Options:Cache**
            - C Attribute: **NISWITCH_ATTR_CACHE**

.. py:attribute:: channel_count

    Contains the number of channels that the instrument driver supports.

    **Related topics**

    `niSwitch Get Channel
    Name <switchviref.chm::/niSwitch_Get_Channel_Name.html>`__ `niSwitch
    Properties <switchpropref.chm::/cniSwitch.html>`__

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | int       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Inherent IVI Attributes:Driver Capabilities:Channel Count**
            - C Attribute: **NISWITCH_ATTR_CHANNEL_COUNT**

.. py:attribute:: characteristic_impedance

    Returns the characteristic impedance for the channel in ohms.

    **Related topics**

    `Characteristic
    Impedance <SWITCH.chm::/characteristic_impedance.html>`__ `niSwitch
    Properties <switchpropref.chm::/cniSwitch.html>`__ `RF Switching
    Considerations <SWITCH.chm::/rf.html>`__




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        characteristic_impedance.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        characteristic_impedance.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].characteristic_impedance = var
            var = session['0,1'].characteristic_impedance

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | float     |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | True      |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Module Characteristics:Characteristic Impedance**
            - C Attribute: **NISWITCH_ATTR_CHARACTERISTIC_IMPEDANCE**

.. py:attribute:: continuous_scan

    Specifies whether to continuously scan through a scan list. Set the
    property to FALSE to stop scanning after one pass through the scan list.
    Set this property to TRUE to loop continuously through the scan list.

    If you set the property to TRUE, the `niSwitch Wait For Scan To
    Complete <switchviref.chm::/niSwitch_Wait_For_Scan_To_Complete.html>`__
    VI times out, and you must call the `niSwitch Abort
    Scan <switchviref.chm::/niSwitch_Abort_Scan.html>`__ VI to stop the
    scan.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__
    `Scanning <SWITCH.chm::/scanning_fundamentals.html>`__

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | bool       |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Scanning Configuration:Continuous Scan**
            - C Attribute: **NISWITCH_ATTR_CONTINUOUS_SCAN**

.. py:attribute:: digital_filter_enable

    Specifies whether to apply the pulse width filter to the Trigger Input.
    Set the property to TRUE to prevent the switch module from being
    triggered by pulses that are less than 150 ns on PXI trigger lines 0-7.

    When this property is set to FALSE, noise on the PXI trigger lines might
    trigger the switch module. If the device triggering the switch module
    can send pulses greater than 150 ns, do not disable this property.

    **Related topics**

    `Disabling Digital Filtering <SWITCH.chm::/fast_pxi_triggering.html>`__
    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | bool       |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Scanning Configuration:Digital Filter Enable**
            - C Attribute: **NISWITCH_ATTR_DIGITAL_FILTER_ENABLE**

.. py:attribute:: driver_setup

    Contains the Driver Setup string that you specified when initializing
    the instrument driver.

    In some cases, you must specify instrument driver options at
    initialization time—for example, when specifying a particular instrument
    model from among a family of instruments that the instrument driver
    supports. This is useful when using simulation.

    You can specify instrument driver-specific options through the
    DriverSetup keyword in the **option string** parameter of the `niSwitch
    Initialize With
    Options <switchviref.chm::/niSwitch_Initialize_With_Options.html>`__ VI,
    or through the IVI Configuration Utility. If you did not specify a
    Driver Setup string, this property returns an empty string.

    **Related topics**

    `niSwitch Initialize With
    Options <switchviref.chm::/niSwitch_Initialize_With_Options.html>`__
    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | str       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Inherent IVI Attributes:Advanced Session Information:Driver Setup**
            - C Attribute: **NISWITCH_ATTR_DRIVER_SETUP**

.. py:attribute:: group_capabilities

    Contains a comma-separated (,) list of class-extension groups that the
    instrument driver implements.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | str       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Inherent IVI Attributes:Driver Capabilities:Class Group Capabilities**
            - C Attribute: **NISWITCH_ATTR_GROUP_CAPABILITIES**

.. py:attribute:: handshaking_initiation

    Specifies how to start handshaking with a measurement device.

    **Related topics**

    `Handshaking <SWITCH.chm::/handshakingg.html>`__ `niSwitch
    Properties <switchpropref.chm::/cniSwitch.html>`__
    `Scanning <SWITCH.chm::/scanning_fundamentals.html>`__

    The following table lists the characteristics of this property.

    +----------------+----------------------------------+
    | Characteristic | Value                            |
    +================+==================================+
    | Datatype       | :py:data:`HandshakingInitiation` |
    +----------------+----------------------------------+
    | Permissions    | read-write                       |
    +----------------+----------------------------------+
    | Channel Based  | False                            |
    +----------------+----------------------------------+
    | Resettable     | No                               |
    +----------------+----------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Scanning Configuration:Handshaking Initiation**
            - C Attribute: **NISWITCH_ATTR_HANDSHAKING_INITIATION**

.. py:attribute:: instrument_firmware_revision

    Contains the firmware revision information for the instrument currently
    in use.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__ `niSwitch
    Revision Query <switchviref.chm::/niSwitch_Revision_Query.html>`__

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | str       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Inherent IVI Attributes:Instrument Identification:Firmware Revision**
            - C Attribute: **NISWITCH_ATTR_INSTRUMENT_FIRMWARE_REVISION**

.. py:attribute:: instrument_manufacturer

    Contains the name of the manufacturer of the instrument currently in
    use.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | str       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Inherent IVI Attributes:Instrument Identification:Manufacturer**
            - C Attribute: **NISWITCH_ATTR_INSTRUMENT_MANUFACTURER**

.. py:attribute:: instrument_model

    Contains the model number or name of the instrument currently in use.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | str       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Inherent IVI Attributes:Instrument Identification:Model**
            - C Attribute: **NISWITCH_ATTR_INSTRUMENT_MODEL**

.. py:attribute:: interchange_check

    Specifies whether to perform interchangeability checking and retrieve
    interchangeability warnings when you call the `niSwitch Connect
    Channels <switchviref.chm::/niSwitch_Connect_Channels.html>`__,
    `niSwitch Set Path <switchviref.chm::/niSwitch_Set_Path.html>`__ and
    `niSwitch Initiate
    Scan <switchviref.chm::/niSwitch_Initiate_Scan.html>`__ VIs. The default
    value is FALSE.

    Interchangeability checking examines the properties in a capability
    group only if you specify a value for at least one property within that
    group. Interchangeability warnings can occur when a property that you
    have not set or that has been invalidated affects the behavior of the
    instrument.

    Interchangeability warnings indicate that using your application with a
    different instrument might cause different behavior. Call `niSwitch Get
    Next Interchange
    Warning <switchviref.chm::/niSwitch_Get_Next_Interchange_Warning.html>`__
    VI to extract interchange warnings. Call the `niSwitch Clear Interchange
    Warnings <switchviref.chm::/niSwitch_Clear_Interchange_Warnings.html>`__
    VI to clear the list of interchangeability warnings without reading
    them.

    **Related topics**

    `niSwitch Get Next Interchange
    Warning <switchviref.chm::/niSwitch_Get_Next_Interchange_Warning.html>`__
    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__ `niSwitch
    Reset Interchange
    Check <switchviref.chm::/niSwitch_Reset_Interchange_Check.html>`__

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | bool       |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Inherent IVI Attributes:User Options:Interchange Check**
            - C Attribute: **NISWITCH_ATTR_INTERCHANGE_CHECK**

.. py:attribute:: is_configuration_channel

    Specifies whether to designate the channel as a configuration channel—a
    channel reserved for internal path creation. The instrument driver uses
    configuration channels to create paths between the channels you specify
    in the `niSwitch Connect
    Channels <switchviref.chm::/niSwitch_Connect_Channels.html>`__ VI.

    Set this property to TRUE to designate the channel as a configuration
    channel. Set this property to FALSE to designate the channel as
    available for external connections. Because you cannot use a
    configuration channel for external connections, the `niSwitch Connect
    Channels <switchviref.chm::/niSwitch_Connect_Channels.html>`__ VI
    returns the Is Configuration Channel error when you attempt to establish
    a connection between a configuration channel and any other channel.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__ `Setting
    Source and Configuration Channels <SWITCH.chm::/configchannels.html>`__




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        is_configuration_channel.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        is_configuration_channel.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].is_configuration_channel = var
            var = session['0,1'].is_configuration_channel

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | bool       |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Channel Configuration:Is Configuration Channel**
            - C Attribute: **NISWITCH_ATTR_IS_CONFIGURATION_CHANNEL**

.. py:attribute:: is_debounced

    Indicates whether the entire switch module has settled since the last
    switching command. A value of TRUE indicates that all signals going
    through the switch module are valid.

    **Related topics**

    `Electromechanical Relays <SWITCH.chm::/electromechanical_relay.html>`__
    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__ `Settling
    Time <SWITCH.chm::/settling_time.html>`__

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | bool      |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Module Characteristics:Is Debounced**
            - C Attribute: **NISWITCH_ATTR_IS_DEBOUNCED**

.. py:attribute:: is_scanning

    Indicates whether the switch module has completed the scan operation.
    TRUE indicates that the scan has completed.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__
    `Scanning <SWITCH.chm::/scanning_fundamentals.html>`__

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | bool      |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Scanning Configuration:Is Scanning**
            - C Attribute: **NISWITCH_ATTR_IS_SCANNING**

.. py:attribute:: is_source_channel

    Specifies whether to designate the channel as a source channel.

    Set this property to TRUE when you connect the channel to a power
    supply, a function generator, or an active measurement point on the unit
    under test, and you do not want to connect the channel to another
    source. The instrument driver prevents source channels from connecting
    to each other: when you attempt to connect two source channels, the
    `niSwitch Connect
    Channels <switchviref.chm::/niSwitch_Connect_Channels.html>`__ VI
    returns the Attempt To Connect Sources error.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__ `Setting
    Source and Configuration Channels <SWITCH.chm::/configchannels.html>`__




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        is_source_channel.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        is_source_channel.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].is_source_channel = var
            var = session['0,1'].is_source_channel

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | bool       |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Channel Configuration:Is Source Channel**
            - C Attribute: **NISWITCH_ATTR_IS_SOURCE_CHANNEL**

.. py:attribute:: is_waiting_for_trig

    Indicates with a semi-colon (;) that at that point in the scan list, the
    scan engine should pause until a trigger is received from the trigger
    input. If you generate that trigger through either a hardware pulse or
    the `niSwitch Send Software
    Trigger <switchviref.chm::/niSwitch_Send_Software_Trigger.html>`__ VI,
    you must know when the scan engine has reached such a state.

    **Related topics**

    `niSwitch Configure Scan
    Trigger <switchviref.chm::/niSwitch_Configure_Scan_List.html>`__
    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__
    `Scanning <SWITCH.chm::/scanning_fundamentals.html>`__

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | bool      |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Scanning Configuration:Is Waiting for Trigger?**
            - C Attribute: **NISWITCH_ATTR_IS_WAITING_FOR_TRIG**

.. py:attribute:: logical_name

    Contains the logical name you specified when opening the current IVI
    session.

    You can wire a logical name to the `niSwitch
    Initialize <switchviref.chm::/niSwitch_Initialize.html>`__ or the
    `niSwitch Initialize With
    Options <switchviref.chm::/niSwitch_Initialize_With_Options.html>`__
    VIs. The IVI Configuration Utility must contain an entry for the logical
    name. The logical name entry refers to a virtual instrument section,
    which specifies a physical device and initial user options, in the IVI
    Configuration file.

    **Related topics**

    `Initialization <SWITCH.chm::/flow_init.html>`__ `niSwitch
    Properties <switchpropref.chm::/cniSwitch.html>`__ `Using NI Switches in
    IVI <SWITCH.chm::/switches_in_ivi.html>`__

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | str       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Inherent IVI Attributes:Advanced Session Information:Logical Name**
            - C Attribute: **NISWITCH_ATTR_LOGICAL_NAME**

.. py:attribute:: master_slave_scan_advanced_bus

    This property has been deprecated and might be removed from a future
    release of NI-SWITCH. Use `niSwitch Route Scan Advanced
    Output <switchviref.chm::/niSwitch_Route_Scan_Advanced_Output.html>`__
    VI instead.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Obsolete Attributes:Master Slave Scan Advanced Bus**
            - C Attribute: **NISWITCH_ATTR_MASTER_SLAVE_SCAN_ADVANCED_BUS**

.. py:attribute:: master_slave_trigger_bus

    This property has been deprecated and might be removed from a future
    release of NI-SWITCH. Use the `niSwitch Route Trigger
    Input <switchviref.chm::/niSwitch_Route_Trigger_Input.html>`__ VI
    instead.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Obsolete Attributes:Master Slave Trigger Bus**
            - C Attribute: **NISWITCH_ATTR_MASTER_SLAVE_TRIGGER_BUS**

.. py:attribute:: max_ac_voltage

    Returns the maximum AC voltage the channel can switch in volts RMS.

    **Related topics**

    `General Switching Considerations <SWITCH.chm::/considerations.html>`__
    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        max_ac_voltage.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        max_ac_voltage.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].max_ac_voltage = var
            var = session['0,1'].max_ac_voltage

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | float     |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | True      |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Module Characteristics:Maximum AC Voltage**
            - C Attribute: **NISWITCH_ATTR_MAX_AC_VOLTAGE**

.. py:attribute:: max_carry_ac_current

    Returns the maximum AC current the channel can carry in amperes RMS.

    **Related topics**

    `General Switching Considerations <SWITCH.chm::/considerations.html>`__
    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        max_carry_ac_current.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        max_carry_ac_current.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].max_carry_ac_current = var
            var = session['0,1'].max_carry_ac_current

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | float     |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | True      |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Module Characteristics:Maximum Carry AC Current**
            - C Attribute: **NISWITCH_ATTR_MAX_CARRY_AC_CURRENT**

.. py:attribute:: max_carry_ac_power

    Returns the maximum AC power the channel can carry in volt-amperes.

    **Related topics**

    `General Switching Considerations <SWITCH.chm::/considerations.html>`__
    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        max_carry_ac_power.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        max_carry_ac_power.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].max_carry_ac_power = var
            var = session['0,1'].max_carry_ac_power

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | float     |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | True      |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Module Characteristics:Maximum Carry AC Power**
            - C Attribute: **NISWITCH_ATTR_MAX_CARRY_AC_POWER**

.. py:attribute:: max_carry_dc_current

    Returns the maximum DC current the channel can carry in amperes.

    **Related topics**

    `General Switching Considerations <SWITCH.chm::/considerations.html>`__
    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        max_carry_dc_current.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        max_carry_dc_current.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].max_carry_dc_current = var
            var = session['0,1'].max_carry_dc_current

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | float     |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | True      |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Module Characteristics:Maximum Carry DC Current**
            - C Attribute: **NISWITCH_ATTR_MAX_CARRY_DC_CURRENT**

.. py:attribute:: max_carry_dc_power

    Returns the maximum DC power the channel can carry in watts.

    **Related topics**

    `General Switching Considerations <SWITCH.chm::/considerations.html>`__
    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        max_carry_dc_power.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        max_carry_dc_power.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].max_carry_dc_power = var
            var = session['0,1'].max_carry_dc_power

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | float     |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | True      |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Module Characteristics:Maximum Carry DC Power**
            - C Attribute: **NISWITCH_ATTR_MAX_CARRY_DC_POWER**

.. py:attribute:: max_dc_voltage

    Returns the maximum DC voltage the channel can switch in volts.

    **Related topics**

    `General Switching Considerations <SWITCH.chm::/considerations.html>`__
    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        max_dc_voltage.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        max_dc_voltage.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].max_dc_voltage = var
            var = session['0,1'].max_dc_voltage

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | float     |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | True      |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Module Characteristics:Maximum DC Voltage**
            - C Attribute: **NISWITCH_ATTR_MAX_DC_VOLTAGE**

.. py:attribute:: max_switching_ac_current

    Returns the maximum AC current the channel can switch in amperes RMS.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__ `Switching
    Current <SWITCH.chm::/switching_current.html>`__




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        max_switching_ac_current.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        max_switching_ac_current.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].max_switching_ac_current = var
            var = session['0,1'].max_switching_ac_current

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | float     |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | True      |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Module Characteristics:Maximum Switching AC Current**
            - C Attribute: **NISWITCH_ATTR_MAX_SWITCHING_AC_CURRENT**

.. py:attribute:: max_switching_ac_power

    Returns the maximum AC power the channel can switch in volt-amperes.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__ `Switching
    Power <SWITCH.chm::/switching_power.html>`__




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        max_switching_ac_power.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        max_switching_ac_power.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].max_switching_ac_power = var
            var = session['0,1'].max_switching_ac_power

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | float     |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | True      |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Module Characteristics:Maximum Switching AC Power**
            - C Attribute: **NISWITCH_ATTR_MAX_SWITCHING_AC_POWER**

.. py:attribute:: max_switching_dc_current

    Returns the maximum DC current the channel can switch in amperes.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__ `Switching
    Current <SWITCH.chm::/switching_current.html>`__




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        max_switching_dc_current.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        max_switching_dc_current.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].max_switching_dc_current = var
            var = session['0,1'].max_switching_dc_current

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | float     |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | True      |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Module Characteristics:Maximum Switching DC Current**
            - C Attribute: **NISWITCH_ATTR_MAX_SWITCHING_DC_CURRENT**

.. py:attribute:: max_switching_dc_power

    Returns the maximum DC power the channel can switch in watts.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__ `Switching
    Power <SWITCH.chm::/switching_power.html>`__




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        max_switching_dc_power.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        max_switching_dc_power.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].max_switching_dc_power = var
            var = session['0,1'].max_switching_dc_power

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | float     |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | True      |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Module Characteristics:Maximum Switching DC Power**
            - C Attribute: **NISWITCH_ATTR_MAX_SWITCHING_DC_POWER**

.. py:attribute:: number_of_relays

    Returns the number of relays that the instrument driver supports.

    **Related topics**

    `niSwitch Get Relay
    Name <switchviref.chm::/niSwitch_Get_Relay_Name.html>`__ `niSwitch
    Properties <switchpropref.chm::/cniSwitch.html>`__

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | int       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Module Characteristics:Number of Relays**
            - C Attribute: **NISWITCH_ATTR_NUMBER_OF_RELAYS**

.. py:attribute:: num_of_columns

    Returns the number of channels on the column of a matrix or scanner. If
    the switch module is a scanner, this property returns the number of
    input channels.

    The `Wire mode <pniSwitch_Wiremode.html>`__ property affects the number
    of available columns. For example, if your switch module has eight input
    lines and you use the 4-wire mode, then the number of columns available
    is two.

    **Related topics**

    `Matrix <SWITCH.chm::/matrix.html>`__ `niSwitch
    Properties <switchpropref.chm::/cniSwitch.html>`__

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | int       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Matrix Configuration:Number of Columns**
            - C Attribute: **NISWITCH_ATTR_NUM_OF_COLUMNS**

.. py:attribute:: num_of_rows

    Returns the number of channels on the row of a matrix or scanner. If the
    switch module is a scanner, this property returns the number of output
    channels.

    The `Wire mode <pniSwitch_Wiremode.html>`__ property affects the number
    of available rows. For example, if your switch module has eight input
    lines and you use the 2-wire mode, then the number of columns you have
    available is four.

    **Related topics**

    `Matrix <SWITCH.chm::/matrix.html>`__ `niSwitch
    Properties <switchpropref.chm::/cniSwitch.html>`__

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | int       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Matrix Configuration:Number of Rows**
            - C Attribute: **NISWITCH_ATTR_NUM_OF_ROWS**

.. py:attribute:: parsed_scan_list

    This property has been deprecated and might be removed from a future
    release of NI-SWITCH.

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | str       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Obsolete Attributes:Parsed Scan List**
            - C Attribute: **NISWITCH_ATTR_PARSED_SCAN_LIST**

.. py:attribute:: power_down_latching_relays_after_debounce

    Specifies whether to power down latching relays after calling the
    `niSwitch Wait For
    Debounce <switchviref.chm::/niSwitch_Wait_For_Debounce.html>`__ VI. Set
    this property to TRUE to ensure that the relays settle and the latching
    relays power down after you call the `niSwitch Wait for
    Debounce <switchviref.chm::/niSwitch_Wait_For_Debounce.html>`__ VI.

    **Related topics**

    `Armature Relays <SWITCH.chm::/armature_relay.html>`__ `niSwitch
    Properties <switchpropref.chm::/cniSwitch.html>`__

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | bool       |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Module Characteristics:Power Down Latching Relays After Debounce**
            - C Attribute: **NISWITCH_ATTR_POWER_DOWN_LATCHING_RELAYS_AFTER_DEBOUNCE**

.. py:attribute:: range_check

    Specifies whether to validate property values and VI parameters. The
    default value is TRUE. Use the `niSwitch Initialize With
    Options <switchviref.chm::/niSwitch_Initialize_With_Options.html>`__ VI
    to override the default value.

    Set this property to TRUE to validate the parameter values that you pass
    to instrument driver VIs. Range checking parameters is useful for
    debugging. After validating your program, set this property to FALSE to
    disable range checking and maximize performance.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | bool       |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Inherent IVI Attributes:User Options:Range Check**
            - C Attribute: **NISWITCH_ATTR_RANGE_CHECK**

.. py:attribute:: record_coercions

    Specifies whether the IVI engine keeps a list of the value coercions it
    makes for properties with ViInt32 and ViReal64 datatypes. The default
    value is FALSE. Use the `niSwitch Initialize With
    Options <switchviref.chm::/niSwitch_Initialize_With_Options.html>`__ VI
    to override the default value.

    Call `niSwitch Get Next Coercion
    Record <switchviref.chm::/niSwitch_Get_Next_Coercion_Record.html>`__ VI
    to extract and delete the oldest coercion record from the list.

    **Related topics**

    `niSwitch Get Next Coercion
    Record <switchviref.chm::/niSwitch_Get_Next_Coercion_Record.html>`__
    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | bool       |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Inherent IVI Attributes:User Options:Record Value Coercions**
            - C Attribute: **NISWITCH_ATTR_RECORD_COERCIONS**

.. py:attribute:: scan_advanced_output

    Specifies the method to use to notify another instrument that all
    signals through the switch module have settled following the processing
    of one entry in the scan list.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__
    `Scanning <SWITCH.chm::/scanning_fundamentals.html>`__

    The following table lists the characteristics of this property.

    +----------------+-------------------------------+
    | Characteristic | Value                         |
    +================+===============================+
    | Datatype       | :py:data:`ScanAdvancedOutput` |
    +----------------+-------------------------------+
    | Permissions    | read-write                    |
    +----------------+-------------------------------+
    | Channel Based  | False                         |
    +----------------+-------------------------------+
    | Resettable     | No                            |
    +----------------+-------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Scanning Configuration:Scan Advanced Output**
            - C Attribute: **NISWITCH_ATTR_SCAN_ADVANCED_OUTPUT**

.. py:attribute:: scan_advanced_polarity

    Specifies the driving level for the Scan Advanced Output signal sent
    from the switch module through either the external (PXI/PXIe) or front
    connector (SCXI) lines. When the Scan Advanced Output signal is sent to
    one of the PXI\_Trig lines, the driven level is always low and this
    property is ignored. Between each Scan Advanced Output signal, the line
    is not driven and is in a high-impedance state.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__
    `Scanning <SWITCH.chm::/scanning_fundamentals.html>`__

    The following table lists the characteristics of this property.

    +----------------+---------------------------------+
    | Characteristic | Value                           |
    +================+=================================+
    | Datatype       | :py:data:`ScanAdvancedPolarity` |
    +----------------+---------------------------------+
    | Permissions    | read-write                      |
    +----------------+---------------------------------+
    | Channel Based  | False                           |
    +----------------+---------------------------------+
    | Resettable     | No                              |
    +----------------+---------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Scanning Configuration:Scan Advanced Polarity**
            - C Attribute: **NISWITCH_ATTR_SCAN_ADVANCED_POLARITY**

.. py:attribute:: scan_delay

    Specifies the minimum amount of time the switch module waits before it
    asserts the scan advanced output trigger after opening or closing the
    switch. The switch module always waits for debounce before asserting the
    trigger. Thus, the actual delay will always be the greater value of the
    settling time and the value you specify as the switch delay, measured in
    seconds. Settling time can vary depending on the switch module.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__
    `Scanning <SWITCH.chm::/scanning_fundamentals.html>`__

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Scanning Configuration:Scan Delay**
            - C Attribute: **NISWITCH_ATTR_SCAN_DELAY**

.. py:attribute:: scan_list

    Contains a scan list (a string that specifies channel connections and
    trigger conditions). The `niSwitch Initiate
    Scan <switchviref.chm::/niSwitch_Initiate_Scan.html>`__ VI makes or
    breaks connections and waits for triggers according to the instructions
    in the scan list. The scan list is comprised of channel names separated
    by special characters that determine the operations the scanner performs
    on the channels when it executes the scan list.

    To create a path between two channels, use the following character
    between the two channel names: -> (a dash followed by a '>' sign)
    Example: 'CH1->CH2' tells the switch to make a path from channel CH1 to
    channel CH2.

    To break or clear a path, use the following character as a prefix before
    the path: ~ (tilde) Example: '~CH1->CH2' tells the switch to break the
    path from channel CH1 to channel CH2.

    To tell the switch module to wait for a trigger event, use the following
    character as a separator between paths: ; (semi-colon) Example:
    'CH1->CH2;CH3->CH4' tells the switch to make the path from channel CH1
    to channel CH2, wait for a trigger, and then make the path from CH3 to
    CH4.

    To tell the switch module to create multiple paths as quickly as
    possible, use the & (ampersand) or && (double ampersand) as a separator
    between the paths. The & in 'CH0->CH1;CH2->CH3&CH4->CH5' instructs the
    scanner to make the path between channels CH0 and CH1, wait for a
    trigger, and then make the paths between channels CH2 and CH3 and
    between channels CH4 and CH5 in no particular order without waiting for
    settling or waiting for a trigger. If wait for settling is desired,
    replace & with &&. The && in 'CH0->CH1;CH2->CH3&&CH4->CH5' instructs the
    scanner to make the path between channels CH0 and CH1, wait for a
    trigger, and then make the path between channels CH2 and CH3, wait for
    settling, then make the path between channels CH4 and CH5.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__ `Scan
    Lists <SWITCH.chm::/scan_list.html>`__
    `Scanning <SWITCH.chm::/scanning_fundamentals.html>`__

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | str        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Scanning Configuration:Scan List**
            - C Attribute: **NISWITCH_ATTR_SCAN_LIST**

.. py:attribute:: scan_mode

    Specifies how to handle existing connections that conflict with the
    connections you make in a scan list. For example, if CH1 is already
    connected to CH2 and the scan list instructs the switch module to
    connect CH1 to CH3, this property specifies what happens to the
    connection between CH1 and CH2.

    Set the property value to **None** to make the switch module take no
    action on existing paths. Set the value to **Break Before Make** to make
    the switch module break conflicting paths before making new ones. Set
    the value to **Break After Make** to make the switch module break
    conflicting paths after making new ones. Most switch modules support
    only one of the possible values: in such cases, this property serves as
    an indicator of the module's behavior.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__
    `Scanning <SWITCH.chm::/scanning_fundamentals.html>`__

    The following table lists the characteristics of this property.

    +----------------+---------------------+
    | Characteristic | Value               |
    +================+=====================+
    | Datatype       | :py:data:`ScanMode` |
    +----------------+---------------------+
    | Permissions    | read-write          |
    +----------------+---------------------+
    | Channel Based  | False               |
    +----------------+---------------------+
    | Resettable     | No                  |
    +----------------+---------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Scanning Configuration:Scan Mode**
            - C Attribute: **NISWITCH_ATTR_SCAN_MODE**

.. py:attribute:: serial_number

    Returns the serial number for the switch module controlled by the
    instrument driver. If the switch module does not return a serial number,
    the instrument driver returns the Invalid Attribute error.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | str       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Module Characteristics:Serial Number**
            - C Attribute: **NISWITCH_ATTR_SERIAL_NUMBER**

.. py:attribute:: settling_time

    Returns the maximum length of time in seconds from after you make a
    connection until the signal flowing through the channel settles.
    Settling time can vary depending on the switch module.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__ `Settling
    Time <SWITCH.chm::/settling_time.html>`__




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        settling_time.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        settling_time.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].settling_time = var
            var = session['0,1'].settling_time

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Module Characteristics:Settling Time**
            - C Attribute: **NISWITCH_ATTR_SETTLING_TIME**

.. py:attribute:: simulate

    Specifies whether to simulate instrument driver I/O operations. The
    default value is FALSE. Use the `niSwitch Initialize With
    Options <switchviref.chm::/niSwitch_Initialize_With_Options.html>`__ VI
    to override the default value.

    Set this property to TRUE to perform range checking and call
    Ivi\_GetAttribute and Ivi\_SetAttribute functions without performing
    instrument I/O. For output parameters that represent instrument data,
    the instrument driver VIs return calculated values.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__ `Simulating
    a Switch <SWITCH.chm::/simulate.html>`__

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | bool       |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Inherent IVI Attributes:User Options:Simulate**
            - C Attribute: **NISWITCH_ATTR_SIMULATE**

.. py:attribute:: specific_driver_class_spec_major_version

    Contains the major version number of the IviSwtch class specification.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | int       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Inherent IVI Attributes:Driver Identification:Class Specification Major Version**
            - C Attribute: **NISWITCH_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION**

.. py:attribute:: specific_driver_class_spec_minor_version

    Contains the minor version number of the class specification with which
    the instrument driver is compliant.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | int       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Inherent IVI Attributes:Driver Identification:Class Specification Minor Version**
            - C Attribute: **NISWITCH_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION**

.. py:attribute:: specific_driver_description

    Contains a brief description of the instrument driver.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | str       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Inherent IVI Attributes:Driver Identification:Description**
            - C Attribute: **NISWITCH_ATTR_SPECIFIC_DRIVER_DESCRIPTION**

.. py:attribute:: specific_driver_vendor

    Contains the name of the vendor that supplies the instrument driver.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | str       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Inherent IVI Attributes:Driver Identification:Driver Vendor**
            - C Attribute: **NISWITCH_ATTR_SPECIFIC_DRIVER_VENDOR**

.. py:attribute:: supported_instrument_models

    Contains a comma-separated (,) list of supported instrument models.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | str       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models**
            - C Attribute: **NISWITCH_ATTR_SUPPORTED_INSTRUMENT_MODELS**

.. py:attribute:: temperature

    Returns the temperature as read by the Switch module in degrees Celsius.
    Refer to the device documentation for more information.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | float     |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Module Characteristics:Temperature**
            - C Attribute: **NISWITCH_ATTR_TEMPERATURE**

.. py:attribute:: trigger_input

    Specifies the source of the trigger for which the switch module can wait
    upon encountering a semi-colon (;) when processing a scan list. When the
    trigger occurs, the switch module advances to the next entry in the scan
    list.

    **Related topics**

    `niSwitch Configure Scan
    List <switchviref.chm::/niSwitch_Configure_Scan_List.html>`__ `niSwitch
    Properties <switchpropref.chm::/cniSwitch.html>`__
    `Scanning <SWITCH.chm::/scanning_fundamentals.html>`__

    The following table lists the characteristics of this property.

    +----------------+-------------------------+
    | Characteristic | Value                   |
    +================+=========================+
    | Datatype       | :py:data:`TriggerInput` |
    +----------------+-------------------------+
    | Permissions    | read-write              |
    +----------------+-------------------------+
    | Channel Based  | False                   |
    +----------------+-------------------------+
    | Resettable     | No                      |
    +----------------+-------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Scanning Configuration:Trigger Input**
            - C Attribute: **NISWITCH_ATTR_TRIGGER_INPUT**

.. py:attribute:: trigger_input_polarity

    Determines the behavior of the trigger input.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__
    `Scanning <SWITCH.chm::/scanning_fundamentals.html>`__

    The following table lists the characteristics of this property.

    +----------------+---------------------------------+
    | Characteristic | Value                           |
    +================+=================================+
    | Datatype       | :py:data:`TriggerInputPolarity` |
    +----------------+---------------------------------+
    | Permissions    | read-write                      |
    +----------------+---------------------------------+
    | Channel Based  | False                           |
    +----------------+---------------------------------+
    | Resettable     | No                              |
    +----------------+---------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Scanning Configuration:Trigger Input Polarity**
            - C Attribute: **NISWITCH_ATTR_TRIGGER_INPUT_POLARITY**

.. py:attribute:: trigger_mode

    This property has been deprecated and might be removed from a future
    release of NI-SWITCH. Use the `niSwitch Route Trigger
    Input <switchviref.chm::/niSwitch_Route_Trigger_Input.html>`__ and/or
    `niSwitch Route Scan Advanced
    Output <switchviref.chm::/niSwitch_Route_Scan_Advanced_Output.html>`__
    VIs instead.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Obsolete Attributes:Trigger Mode**
            - C Attribute: **NISWITCH_ATTR_TRIGGER_MODE**

.. py:attribute:: wire_mode

    Returns the wire mode of the switch module. This property affects the
    values of the `Number of Rows <pniSwitch_NumberofRows.html>`__ and
    `Number of Columns <pniSwitch_NumberofColumns.html>`__ properties. The
    actual number of input and output lines on the switch module does not
    change, but the number of channels depends on how many lines constitute
    each channel.

    **Related topics**

    `N-Wire Switching Modes <SWITCH.chm::/xwire.html>`__ `niSwitch
    Properties <switchpropref.chm::/cniSwitch.html>`__




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        wire_mode.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        wire_mode.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].wire_mode = var
            var = session['0,1'].wire_mode

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | int       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | True      |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Module Characteristics:Wire mode**
            - C Attribute: **NISWITCH_ATTR_WIRE_MODE**


