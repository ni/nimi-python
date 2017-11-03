niswitch.Session properties
===========================

.. py:currentmodule:: niswitch

.. py:attribute:: analog_bus_sharing_enable

    Enables or disables sharing of an analog bus line so that multiple  NI SwitchBlock devices may connect to it simultaneously. To enable  multiple NI SwitchBlock devices to share an analog bus line, set this  attribute to VI_TRUE for each device on the channel that corresponds  with the shared analog bus line. The default value for all devices is  VI_FALSE, which disables sharing of the analog bus.
    Refer to the Using the Analog Bus on an NI SwitchBlock Carrier topic  in the NI Switches Help for more information about sharing the analog bus.




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

    This channel-based attribute returns the bandwidth for the channel.
    The units are hertz.




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

    This attribute has been deprecated and may be removed from a future release of  NI-SWITCH.  Use the niSwitch_RouteScanAdvancedOutput function instead.

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

    This attribute has been deprecated and may be removed from a future release of  NI-SWITCH.  Use the niSwitch_RouteTriggerInput function instead.

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

    Specifies whether to cache the value of attributes.  When caching is  enabled, the instrument driver keeps track of the current instrument  settings and avoids sending redundant commands to the instrument.
    The instrument driver can choose always to cache or never to cache  particular attributes regardless of the setting of this attribute.
    The default value is VI_TRUE.   Use the niSwitch_InitWithOptions  function to override this value.

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

    Indicates the number of channels that the specific instrument  driver supports.

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

    This channel-based attribute returns the characteristic impedance for the  channel.
    The units are ohms.




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

    When a switch device is scanning, the swich can either stop scanning when  the end of the scan (VI_FALSE) or continue scanning from the top of the  scan list again (VI_TRUE).
    Notice that if you set the scan to continuous (VI_TRUE), the Wait For Scan  Complete operation will always time out and you must call Abort to stop  the scan.

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

    This property specifies whether to apply the pulse width filter to the  Trigger Input. Enabling the Digital Filter (VI_TRUE) prevents the switch  module from being triggered by pulses that are less than 150 ns on PXI  trigger lines 0–7.
    When Digital Filter is disabled (VI_FALSE), it is possible for the switch  module to be triggered by noise on the PXI trigger lines. If the device  triggering the switch is capable of sending pulses greater than 150 ns, you should not disable the Digital Filter.

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

    This attribute indicates the Driver Setup string that the user  specified when initializing the driver.
    Some cases exist where the end-user must specify instrument driver  options at initialization time.  An example of this is specifying  a particular instrument model from among a family of instruments  that the driver supports.  This is useful when using simulation.   The end-user can specify driver-specific options through  the DriverSetup keyword in the optionsString parameter to the  niSwitch_InitWithOptions function, or through the IVI Configuration Utility.
    If the user does not specify a Driver Setup string, this attribute returns an empty string.

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

    A string that contains a comma-separated list of class-extention groups that  this driver implements.

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

    A string that contains the firmware revision information  for the instrument you are currently using.

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

    A string that contains the name of the instrument manufacturer you are currently  using.

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

    A string that contains the model number or name of the instrument that you  are currently using.

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

    Specifies whether to perform interchangeability checking and retrieve  interchangeability warnings when you call  niSwitch_Connect, niSwitch_SetPath and niSwitch_InitiateScan functions.
    The default value is VI_FALSE.
    Interchangeability warnings indicate that using your application with a  different instrument might cause different behavior.   You call niSwitch_GetNextInterchangeWarning to extract interchange warnings.   Call the niSwitch_ClearInterchangeWarnings function to clear the list  of interchangeability warnings without reading them.
    Interchangeability checking examines the attributes in a  capability group only if you specify a value for at least one  attribute within that group.  Interchangeability warnings can  occur when an attribute affects the behavior of the instrument and you  have not set that attribute, or the attribute has been invalidated since you set it.

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

    This channel-based attribute specifies whether to reserve the channel for  internal path creation.  A channel that is available for internal path  creation is called a configuration channel.  The driver may use  configuration channels to create paths between two channels you specify in  the niSwitch_Connect function.  Configuration channels are not available  for external connections.
    Set this attribute to VI_TRUE to mark the channel as a configuration  channel.  Set this attribute to VI_FALSE to mark the channel as available  for external connections.
    After you identify a channel as a configuration channel, you cannot  use that channel for external connections.  The niSwitch_Connect function  returns the NISWITCH_ERROR_IS_CONFIGURATION_CHANNEL error when you attempt  to establish a connection between a configuration channel and any other  channel.




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

    This attribute indicates whether the entire switch device has settled  since the last switching command.  A value of VI_TRUE indicates that all  signals going through the switch device are valid.

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

    If VI_TRUE, the switch module is currently scanning through the scan list  (i.e. it is not in the Idle state). If VI_FALSE, the switch module is not  currently scanning through the scan list (i.e. it is in the Idle state).

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

    This channel-based attribute specifies whether you want to identify the  channel as a source channel.  Typically, you set this attribute to VI_TRUE  when you attach the channel to a power supply, a function generator, or an  active measurement point on the unit under test, and you do not want to  connect the channel to another source.  The driver prevents source  channels from connecting to each other.  The niSwitch_Connect function  returns the NISWITCH_ERROR_ATTEMPT_TO_CONNECT_SOURCES when you attempt to  connect two channels that you identify as source channels.




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

    In a scan list, a semi-colon (;) is used to indicate that at that point in  the scan list, the scan engine should pause until a trigger is received  from the trigger input.  If that trigger is user generated through either  a hardware pulse or the Send SW Trigger operation, it is necessary for the  user to know  when the scan engine has reached such a state.

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

    A string containing the logical name you specified when opening the  current IVI session.
    You may pass a logical name to the niSwitch_init or  niSwitch_InitWithOptions functions.   The IVI Configuration utility must contain an entry for the logical name.   The logical name entry refers to a virtual instrument section in the  IVI Configuration file.  The virtual instrument section specifies a physical  device and initial user options.

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

    This attribute has been deprecated and may be removed from a future release of  NI-SWITCH.  Use the niSwitch_RouteScanAdvancedOutput function instead.

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

    This attribute has been deprecated and may be removed from a future release of  NI-SWITCH.  Use the niSwitch_RouteTriggerInput function instead.

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

    This channel-based attribute returns the maximum AC voltage the channel  can switch.
    The units are volts RMS.




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

    This channel-based attribute returns the maximum AC current the channel  can carry.
    The units are amperes RMS.




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

    This channel-based attribute returns the maximum AC power the channel can  carry.
    The units are volt-amperes.




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

    This channel-based attribute returns the maximum DC current the channel  can carry.
    The units are amperes.




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

    This channel-based attribute returns the maximum DC power the channel can  carry.
    The units are watts.




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

    This channel-based attribute returns the maximum DC voltage the channel  can switch.
    The units are volts.




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

    This channel-based attribute returns the maximum AC current the channel  can switch.
    The units are amperes RMS.




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

    This channel-based attribute returns the maximum AC power the channel can  switch.
    The units are volt-amperes.




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

    This channel-based attribute returns the maximum DC current the channel  can switch.
    The units are amperes.




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

    This channel-based attribute returns the maximum DC power the channel can  switch.
    The units are watts.




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

    This attribute returns the number of relays.

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

    This attribute returns the number of channels on the column of a matrix or  scanner.  If the switch device is a scanner, this value is the number of  input channels.
    The NISWITCH_ATTR_WIRE_MODE attribute affects the number of available  columns.  For example, if your device has 8 input lines and you use the  four-wire mode, then the number of columns you have available is 2.

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

    This attribute returns the number of channels on the row of a matrix or  scanner.  If the switch device is a scanner, this value is the number of  output channels.
    The NISWITCH_ATTR_WIRE_MODE attribute affects the number of available  rows.  For example, if your device has 8 input lines and you use the  two-wire mode, then the number of columns you have available is 4.

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

    This attribute has been deprecated and may be removed from a future release of  NI-SWITCH.

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

    This property specifies whether to power down latching relays after  calling Wait For Debounce.
    When Power Down Latching Relays After Debounce is enabled (VI_TRUE),  a call to Wait For Debounce ensures that the relays are settled  and the latching relays are powered down.

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

    Specifies whether to validate attribute values and function parameters.   If enabled, the instrument driver validates the parameter values that  you pass to driver functions.  Range checking  parameters is very useful for debugging.  After you validate your program,  you can set this attribute to VI_FALSE to disable range checking and  maximize performance.
    The default value is VI_TRUE.   Use the niSwitch_InitWithOptions  function to override this value.

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

    Specifies whether the IVI engine keeps a list of  the value coercions it makes for ViInt32 and ViReal64 attributes.   You call niSwitch_GetNextCoercionRecord to extract and delete the oldest  coercion record from the list.
    The default value is VI_FALSE.   Use the  niSwitch_InitWithOptions function to override this value.

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

    This attribute specifies the method you want to use to notify another  instrument that all signals going through the switch device have settled  following the processing of one entry in the scan list.

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

    This attribute specifies the minimum amount of time the switch device  waits before it asserts the scan advanced output trigger after opening or  closing the switch.  The switch device always waits for debounce before  asserting the trigger. The units are seconds.
    the greater value of the settling time and the value you specify as the  scan delay.



    .. note:: NI PXI-2501/2503/2565/2590/2591 Users--the actual delay will always be

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

    This attribute contains a scan list, which is a string that specifies  channel connections and trigger conditions.  The niSwitch_InitiateScan  function makes or breaks connections and waits for triggers according to  the instructions in the scan list.
    The scan list is comprised of channel names that you separate with  special characters.  These special characters determine the operations the  scanner performs on the channels when it executes this scan list.
    To create a path between two channels, use the following character between  the two channel names:
    -> (a dash followed by a '>' sign)
    Example:  \CH1->CH2\ tells the switch to make a path from channel CH1 to channel  CH2.
    To break or clear a path, use the following character as a prefix before  the path:
    ~ (tilde)
    Example:  \~CH1->CH2\ tells the switch to break the path from channel CH1 to  channel CH2.
    To tell the switch device to wait for a trigger event, use the following  character as a separator between paths:
    ; (semi-colon)
    Example:  \CH1->CH2;CH3->CH4\ tells the switch to make the path from channel CH1  to channel CH2, wait for a trigger, and then make the path from CH3 to  CH4.

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

    This attribute specifies what happens to existing connections that  conflict with the connections you make in a scan list.  For example, if  CH1 is already connected to CH2 and the scan list instructs the switch  device to connect CH1 to CH3, this attribute specifies what happens to the  connection between CH1 and CH2.
    If the value of this attribute is NISWITCH_VAL_NONE, the switch device  takes no action on existing paths.  If the value is  NISWITCH_VAL_BREAK_BEFORE_MAKE, the switch device breaks conflicting paths  before making new ones.  If the value is NISWITCH_VAL_BREAK_AFTER_MAKE,  the switch device breaks conflicting paths after making new ones.
    Most switch devices support only one of the possible values.  In such  cases, this attribute serves as an indicator of the device's behavior.

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

    This read-only attribute returns the serial number for the switch device  controlled by this instrument driver.  If the device does not return a  serial number, the driver returns the IVI_ERROR_ATTRIBUTE_NOT_SUPPORTED error.

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

    This channel-based attribute returns the maximum length of time from after  you make a connection until the signal flowing through the channel  settles. The units are seconds.
    the greater value of the settling time and the value you specify as the  scan delay.



    .. note:: NI PXI-2501/2503/2565/2590/2591 Users--the actual delay will always be


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

    Specifies whether or not to simulate instrument driver I/O operations.  If  simulation is enabled, instrument driver functions perform range checking  and call Ivi_GetAttribute and Ivi_SetAttribute functions, but they do not  perform instrument I/O.  For output parameters that represent instrument  data, the instrument driver functions return calculated values.
    The default value is VI_FALSE.   Use the niSwitch_InitWithOptions  function to override this value.

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

    The major version number of the IviSwtch class specification.

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

    The minor version number of the class specification with which this driver is compliant.

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

    A string that contains a brief description of the specific  driver.

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

    A string that contains the name of the vendor that supplies this driver.

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

    Contains a comma-separated list of supported instrument models.

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

    This attribute returns the temperature as read by the Switch module.     The units are degrees Celsius.

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

    This attribute specifies the source of the trigger for which the switch  device can wait when processing a scan list.  The switch device waits for  a trigger when it encounters a semi-colon in a scan list.  When the trigger  occurs, the switch device advances to the next entry in the scan list.

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

    Determines the behavior of the trigger Input.

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

    This attribute has been deprecated and may be removed from a future release of  NI-SWITCH.  Use the niSwitch_RouteTriggerInput and/or niSwitch_RouteScanAdvancedOutput  functions instead.

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

    This attribute returns the wire mode of the switch device.
    This attribute affects the values of the NISWITCH_ATTR_NUM_OF_ROWS and  NISWITCH_ATTR_NUM_OF_COLUMNS attributes.   The actual number of input and  output lines on the switch device is fixed, but the number of channels  depends on how many lines constitute each channel.




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


