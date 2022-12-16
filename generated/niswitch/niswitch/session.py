# -*- coding: utf-8 -*-
# This file was generated
import array  # noqa: F401
# Used by @ivi_synchronized
from functools import wraps

import niswitch._attributes as _attributes
import niswitch._converters as _converters
import niswitch._library_interpreter as _library_interpreter
import niswitch.enums as enums
import niswitch.errors as errors

import hightime

# Used for __repr__
import pprint
pp = pprint.PrettyPrinter(indent=4)


class _Scan(object):
    def __init__(self, session):
        self._session = session
        self._session._initiate_scan()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._session.abort()


# From https://stackoverflow.com/questions/5929107/decorators-with-parameters
def ivi_synchronized(f):
    @wraps(f)
    def aux(*xs, **kws):
        session = xs[0]  # parameter 0 is 'self' which is the session object
        with session.lock():
            return f(*xs, **kws)
    return aux


class _Lock(object):
    def __init__(self, session):
        self._session = session

    def __enter__(self):
        # _lock_session is called from the lock() function, not here
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._session.unlock()


class _RepeatedCapabilities(object):
    def __init__(self, session, prefix, current_repeated_capability_list):
        self._session = session
        self._prefix = prefix
        # We need at least one element. If we get an empty list, make the one element an empty string
        self._current_repeated_capability_list = current_repeated_capability_list if len(current_repeated_capability_list) > 0 else ['']
        # Now we know there is at lease one entry, so we look if it is an empty string or not
        self._separator = '/' if len(self._current_repeated_capability_list[0]) > 0 else ''

    def __getitem__(self, repeated_capability):
        '''Set/get properties or call methods with a repeated capability (i.e. channels)'''
        rep_caps_list = _converters.convert_repeated_capabilities(repeated_capability, self._prefix)
        complete_rep_cap_list = [current_rep_cap + self._separator + rep_cap for current_rep_cap in self._current_repeated_capability_list for rep_cap in rep_caps_list]

        return _SessionBase(
            repeated_capability_list=complete_rep_cap_list,
            all_channels_in_session=self._session._all_channels_in_session,
            interpreter=self._session._interpreter,
            freeze_it=True
        )


# This is a very simple context manager we can use when we need to set/get attributes
# or call functions from _SessionBase that require no channels. It is tied to the specific
# implementation of _SessionBase and how repeated capabilities are handled.
class _NoChannel(object):
    def __init__(self, session):
        self._session = session

    def __enter__(self):
        self._repeated_capability_cache = self._session._repeated_capability
        self._session._repeated_capability = ''

    def __exit__(self, exc_type, exc_value, traceback):
        self._session._repeated_capability = self._repeated_capability_cache


class _SessionBase(object):
    '''Base class for all NI-SWITCH sessions.'''

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

    analog_bus_sharing_enable = _attributes.AttributeViBoolean(1150018)
    '''Type: bool

    Enables or disables sharing of an analog bus line so that multiple  NI SwitchBlock devices may connect to it simultaneously. To enable  multiple NI SwitchBlock devices to share an analog bus line, set this  property to True for each device on the channel that corresponds  with the shared analog bus line. The default value for all devices is  False, which disables sharing of the analog bus.
    Refer to the Using the Analog Bus on an NI SwitchBlock Carrier topic  in the NI Switches Help for more information about sharing the analog bus.

    Tip:
    This property can be set/get on specific channels within your :py:class:`niswitch.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].analog_bus_sharing_enable`

    To set/get on all channels, you can call the property directly on the :py:class:`niswitch.Session`.

    Example: :py:attr:`my_session.analog_bus_sharing_enable`
    '''
    bandwidth = _attributes.AttributeViReal64(1250005)
    '''Type: float

    This channel-based property returns the bandwidth for the channel.
    The units are hertz.

    Tip:
    This property can be set/get on specific channels within your :py:class:`niswitch.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].bandwidth`

    To set/get on all channels, you can call the property directly on the :py:class:`niswitch.Session`.

    Example: :py:attr:`my_session.bandwidth`
    '''
    channel_count = _attributes.AttributeViInt32(1050203)
    '''Type: int

    Indicates the number of channels that the specific instrument  driver supports.
    '''
    characteristic_impedance = _attributes.AttributeViReal64(1250016)
    '''Type: float

    This channel-based property returns the characteristic impedance for the  channel.
    The units are ohms.

    Tip:
    This property can be set/get on specific channels within your :py:class:`niswitch.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].characteristic_impedance`

    To set/get on all channels, you can call the property directly on the :py:class:`niswitch.Session`.

    Example: :py:attr:`my_session.characteristic_impedance`
    '''
    continuous_scan = _attributes.AttributeViBoolean(1250026)
    '''Type: bool

    When a switch device is scanning, the swich can either stop scanning when  the end of the scan (False) or continue scanning from the top of the  scan list again (True).
    Notice that if you set the scan to continuous (True), the Wait For Scan  Complete operation will always time out and you must call Abort to stop  the scan.
    '''
    digital_filter_enable = _attributes.AttributeViBoolean(1150016)
    '''Type: bool

    This property specifies whether to apply the pulse width filter to the  Trigger Input. Enabling the Digital Filter (True) prevents the switch  module from being triggered by pulses that are less than 150 ns on PXI  trigger lines 0–7.
    When Digital Filter is disabled (False), it is possible for the switch  module to be triggered by noise on the PXI trigger lines. If the device  triggering the switch is capable of sending pulses greater than 150 ns, you should not disable the Digital Filter.
    '''
    driver_setup = _attributes.AttributeViString(1050007)
    '''Type: str

    This property indicates the Driver Setup string that the user  specified when initializing the driver.
    Some cases exist where the end-user must specify instrument driver  options at initialization time.  An example of this is specifying  a particular instrument model from among a family of instruments  that the driver supports.  This is useful when using simulation.   The end-user can specify driver-specific options through  the DriverSetup keyword in the optionsString parameter to the  InitWithOptions method, or through the IVI Configuration Utility.
    If the user does not specify a Driver Setup string, this property returns an empty string.

    Note:
    One or more of the referenced methods are not in the Python API for this driver.
    '''
    handshaking_initiation = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.HandshakingInitiation, 1150013)
    instrument_firmware_revision = _attributes.AttributeViString(1050510)
    '''Type: str

    A string that contains the firmware revision information  for the instrument you are currently using.
    '''
    instrument_manufacturer = _attributes.AttributeViString(1050511)
    '''Type: str

    A string that contains the name of the instrument manufacturer you are currently  using.
    '''
    instrument_model = _attributes.AttributeViString(1050512)
    '''Type: str

    A string that contains the model number or name of the instrument that you  are currently using.
    '''
    io_resource_descriptor = _attributes.AttributeViString(1050304)
    '''Type: str

    Indicates the resource descriptor the driver  uses to identify the physical device.
    If you initialize the driver with a logical name, this  property contains the resource descriptor that corresponds  to the entry in the IVI Configuration utility.
    If you initialize the instrument driver with the resource  descriptor, this property contains that value.
    '''
    is_configuration_channel = _attributes.AttributeViBoolean(1250003)
    '''Type: bool

    This channel-based property specifies whether to reserve the channel for  internal path creation.  A channel that is available for internal path  creation is called a configuration channel.  The driver may use  configuration channels to create paths between two channels you specify in  the connect method.  Configuration channels are not available  for external connections.
    Set this property to True to mark the channel as a configuration  channel.  Set this property to False to mark the channel as available  for external connections.
    After you identify a channel as a configuration channel, you cannot  use that channel for external connections.  The connect method  returns the NISWITCH_ERROR_IS_CONFIGURATION_CHANNEL error when you attempt  to establish a connection between a configuration channel and any other  channel.

    Tip:
    This property can be set/get on specific channels within your :py:class:`niswitch.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].is_configuration_channel`

    To set/get on all channels, you can call the property directly on the :py:class:`niswitch.Session`.

    Example: :py:attr:`my_session.is_configuration_channel`
    '''
    is_debounced = _attributes.AttributeViBoolean(1250002)
    '''Type: bool

    This property indicates whether the entire switch device has settled  since the last switching command.  A value of True indicates that all  signals going through the switch device are valid.
    '''
    is_scanning = _attributes.AttributeViBoolean(1250024)
    '''Type: bool

    If True, the switch module is currently scanning through the scan list  (i.e. it is not in the Idle state). If False, the switch module is not  currently scanning through the scan list (i.e. it is in the Idle state).
    '''
    is_source_channel = _attributes.AttributeViBoolean(1250001)
    '''Type: bool

    This channel-based property specifies whether you want to identify the  channel as a source channel.  Typically, you set this property to True  when you attach the channel to a power supply, a method generator, or an  active measurement point on the unit under test, and you do not want to  connect the channel to another source.  The driver prevents source  channels from connecting to each other.  The connect method  returns the NISWITCH_ERROR_ATTEMPT_TO_CONNECT_SOURCES when you attempt to  connect two channels that you identify as source channels.

    Tip:
    This property can be set/get on specific channels within your :py:class:`niswitch.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].is_source_channel`

    To set/get on all channels, you can call the property directly on the :py:class:`niswitch.Session`.

    Example: :py:attr:`my_session.is_source_channel`
    '''
    is_waiting_for_trig = _attributes.AttributeViBoolean(1150004)
    '''Type: bool

    In a scan list, a semi-colon (;) is used to indicate that at that point in  the scan list, the scan engine should pause until a trigger is received  from the trigger input.  If that trigger is user generated through either  a hardware pulse or the Send SW Trigger operation, it is necessary for the  user to know  when the scan engine has reached such a state.
    '''
    logical_name = _attributes.AttributeViString(1050305)
    '''Type: str

    A string containing the logical name you specified when opening the  current IVI session.
    You may pass a logical name to the init or  InitWithOptions methods.   The IVI Configuration utility must contain an entry for the logical name.   The logical name entry refers to a virtual instrument section in the  IVI Configuration file.  The virtual instrument section specifies a physical  device and initial user options.

    Note:
    One or more of the referenced methods are not in the Python API for this driver.
    '''
    max_ac_voltage = _attributes.AttributeViReal64(1250007)
    '''Type: float

    This channel-based property returns the maximum AC voltage the channel  can switch.
    The units are volts RMS.

    Tip:
    This property can be set/get on specific channels within your :py:class:`niswitch.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].max_ac_voltage`

    To set/get on all channels, you can call the property directly on the :py:class:`niswitch.Session`.

    Example: :py:attr:`my_session.max_ac_voltage`
    '''
    max_carry_ac_current = _attributes.AttributeViReal64(1250011)
    '''Type: float

    This channel-based property returns the maximum AC current the channel  can carry.
    The units are amperes RMS.

    Tip:
    This property can be set/get on specific channels within your :py:class:`niswitch.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].max_carry_ac_current`

    To set/get on all channels, you can call the property directly on the :py:class:`niswitch.Session`.

    Example: :py:attr:`my_session.max_carry_ac_current`
    '''
    max_carry_ac_power = _attributes.AttributeViReal64(1250015)
    '''Type: float

    This channel-based property returns the maximum AC power the channel can  carry.
    The units are volt-amperes.

    Tip:
    This property can be set/get on specific channels within your :py:class:`niswitch.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].max_carry_ac_power`

    To set/get on all channels, you can call the property directly on the :py:class:`niswitch.Session`.

    Example: :py:attr:`my_session.max_carry_ac_power`
    '''
    max_carry_dc_current = _attributes.AttributeViReal64(1250010)
    '''Type: float

    This channel-based property returns the maximum DC current the channel  can carry.
    The units are amperes.

    Tip:
    This property can be set/get on specific channels within your :py:class:`niswitch.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].max_carry_dc_current`

    To set/get on all channels, you can call the property directly on the :py:class:`niswitch.Session`.

    Example: :py:attr:`my_session.max_carry_dc_current`
    '''
    max_carry_dc_power = _attributes.AttributeViReal64(1250014)
    '''Type: float

    This channel-based property returns the maximum DC power the channel can  carry.
    The units are watts.

    Tip:
    This property can be set/get on specific channels within your :py:class:`niswitch.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].max_carry_dc_power`

    To set/get on all channels, you can call the property directly on the :py:class:`niswitch.Session`.

    Example: :py:attr:`my_session.max_carry_dc_power`
    '''
    max_dc_voltage = _attributes.AttributeViReal64(1250006)
    '''Type: float

    This channel-based property returns the maximum DC voltage the channel  can switch.
    The units are volts.

    Tip:
    This property can be set/get on specific channels within your :py:class:`niswitch.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].max_dc_voltage`

    To set/get on all channels, you can call the property directly on the :py:class:`niswitch.Session`.

    Example: :py:attr:`my_session.max_dc_voltage`
    '''
    max_switching_ac_current = _attributes.AttributeViReal64(1250009)
    '''Type: float

    This channel-based property returns the maximum AC current the channel  can switch.
    The units are amperes RMS.

    Tip:
    This property can be set/get on specific channels within your :py:class:`niswitch.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].max_switching_ac_current`

    To set/get on all channels, you can call the property directly on the :py:class:`niswitch.Session`.

    Example: :py:attr:`my_session.max_switching_ac_current`
    '''
    max_switching_ac_power = _attributes.AttributeViReal64(1250013)
    '''Type: float

    This channel-based property returns the maximum AC power the channel can  switch.
    The units are volt-amperes.

    Tip:
    This property can be set/get on specific channels within your :py:class:`niswitch.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].max_switching_ac_power`

    To set/get on all channels, you can call the property directly on the :py:class:`niswitch.Session`.

    Example: :py:attr:`my_session.max_switching_ac_power`
    '''
    max_switching_dc_current = _attributes.AttributeViReal64(1250008)
    '''Type: float

    This channel-based property returns the maximum DC current the channel  can switch.
    The units are amperes.

    Tip:
    This property can be set/get on specific channels within your :py:class:`niswitch.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].max_switching_dc_current`

    To set/get on all channels, you can call the property directly on the :py:class:`niswitch.Session`.

    Example: :py:attr:`my_session.max_switching_dc_current`
    '''
    max_switching_dc_power = _attributes.AttributeViReal64(1250012)
    '''Type: float

    This channel-based property returns the maximum DC power the channel can  switch.
    The units are watts.

    Tip:
    This property can be set/get on specific channels within your :py:class:`niswitch.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].max_switching_dc_power`

    To set/get on all channels, you can call the property directly on the :py:class:`niswitch.Session`.

    Example: :py:attr:`my_session.max_switching_dc_power`
    '''
    number_of_relays = _attributes.AttributeViInt32(1150014)
    '''Type: int

    This property returns the number of relays.
    '''
    num_of_columns = _attributes.AttributeViInt32(1250019)
    '''Type: int

    This property returns the number of channels on the column of a matrix or  scanner.  If the switch device is a scanner, this value is the number of  input channels.
    The wire_mode property affects the number of available  columns.  For example, if your device has 8 input lines and you use the  four-wire mode, then the number of columns you have available is 2.
    '''
    num_of_rows = _attributes.AttributeViInt32(1250018)
    '''Type: int

    This property returns the number of channels on the row of a matrix or  scanner.  If the switch device is a scanner, this value is the number of  output channels.
    The wire_mode property affects the number of available  rows.  For example, if your device has 8 input lines and you use the  two-wire mode, then the number of columns you have available is 4.
    '''
    power_down_latching_relays_after_debounce = _attributes.AttributeViBoolean(1150017)
    '''Type: bool

    This property specifies whether to power down latching relays after  calling Wait For Debounce.
    When Power Down Latching Relays After Debounce is enabled (True),  a call to Wait For Debounce ensures that the relays are settled  and the latching relays are powered down.
    '''
    scan_advanced_output = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.ScanAdvancedOutput, 1250023)
    '''Type: enums.ScanAdvancedOutput

    This property specifies the method you want to use to notify another  instrument that all signals going through the switch device have settled  following the processing of one entry in the scan list.
    '''
    scan_advanced_polarity = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.ScanAdvancedPolarity, 1150011)
    scan_delay = _attributes.AttributeViReal64TimeDeltaSeconds(1250025)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    This property specifies the minimum amount of time the switch device  waits before it asserts the scan advanced output trigger after opening or  closing the switch.  The switch device always waits for debounce before  asserting the trigger. The units are seconds.
    the greater value of the settling time and the value you specify as the  scan delay.

    Note: NI PXI-2501/2503/2565/2590/2591 Users--the actual delay will always be
    '''
    scan_list = _attributes.AttributeViString(1250020)
    '''Type: str

    This property contains a scan list, which is a string that specifies  channel connections and trigger conditions.  The initiate  method makes or breaks connections and waits for triggers according to  the instructions in the scan list.
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
    '''
    scan_mode = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.ScanMode, 1250021)
    '''Type: enums.ScanMode

    This property specifies what happens to existing connections that  conflict with the connections you make in a scan list.  For example, if  CH1 is already connected to CH2 and the scan list instructs the switch  device to connect CH1 to CH3, this property specifies what happens to the  connection between CH1 and CH2.
    If the value of this property is ScanMode.NONE, the switch device  takes no action on existing paths.  If the value is  ScanMode.BREAK_BEFORE_MAKE, the switch device breaks conflicting paths  before making new ones.  If the value is ScanMode.BREAK_AFTER_MAKE,  the switch device breaks conflicting paths after making new ones.
    Most switch devices support only one of the possible values.  In such  cases, this property serves as an indicator of the device's behavior.

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    serial_number = _attributes.AttributeViString(1150015)
    '''Type: str

    This read-only property returns the serial number for the switch device  controlled by this instrument driver.  If the device does not return a  serial number, the driver returns the IVI_ERROR_ATTRIBUTE_NOT_SUPPORTED error.
    '''
    settling_time = _attributes.AttributeViReal64TimeDeltaSeconds(1250004)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    This channel-based property returns the maximum length of time from after  you make a connection until the signal flowing through the channel  settles. The units are seconds.
    the greater value of the settling time and the value you specify as the  scan delay.

    Note: NI PXI-2501/2503/2565/2590/2591 Users--the actual delay will always be

    Tip:
    This property can be set/get on specific channels within your :py:class:`niswitch.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].settling_time`

    To set/get on all channels, you can call the property directly on the :py:class:`niswitch.Session`.

    Example: :py:attr:`my_session.settling_time`
    '''
    simulate = _attributes.AttributeViBoolean(1050005)
    '''Type: bool

    Specifies whether or not to simulate instrument driver I/O operations.  If  simulation is enabled, instrument driver methods perform range checking  and call Ivi_GetAttribute and Ivi_SetAttribute methods, but they do not  perform instrument I/O.  For output parameters that represent instrument  data, the instrument driver methods return calculated values.
    The default value is False.   Use the InitWithOptions  method to override this value.

    Note:
    One or more of the referenced methods are not in the Python API for this driver.
    '''
    specific_driver_description = _attributes.AttributeViString(1050514)
    '''Type: str

    A string that contains a brief description of the specific  driver.
    '''
    specific_driver_revision = _attributes.AttributeViString(1050551)
    '''Type: str

    A string that contains additional version information about this  instrument driver.
    '''
    specific_driver_vendor = _attributes.AttributeViString(1050513)
    '''Type: str

    A string that contains the name of the vendor that supplies this driver.
    '''
    supported_instrument_models = _attributes.AttributeViString(1050327)
    '''Type: str

    Contains a comma-separated list of supported instrument models.
    '''
    temperature = _attributes.AttributeViReal64(1150019)
    '''Type: float

    This property returns the temperature as read by the Switch module.     The units are degrees Celsius.
    '''
    trigger_input = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.TriggerInput, 1250022)
    '''Type: enums.TriggerInput

    This property specifies the source of the trigger for which the switch  device can wait when processing a scan list.  The switch device waits for  a trigger when it encounters a semi-colon in a scan list.  When the trigger  occurs, the switch device advances to the next entry in the scan list.
    '''
    trigger_input_polarity = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.TriggerInputPolarity, 1150010)
    '''Type: enums.TriggerInputPolarity

    Determines the behavior of the trigger Input.
    '''
    wire_mode = _attributes.AttributeViInt32(1250017)
    '''Type: int

    This property returns the wire mode of the switch device.
    This property affects the values of the num_of_rows and  num_of_columns properties.   The actual number of input and  output lines on the switch device is fixed, but the number of channels  depends on how many lines constitute each channel.

    Tip:
    This property can be set/get on specific channels within your :py:class:`niswitch.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].wire_mode`

    To set/get on all channels, you can call the property directly on the :py:class:`niswitch.Session`.

    Example: :py:attr:`my_session.wire_mode`
    '''

    def __init__(self, repeated_capability_list, all_channels_in_session, interpreter, freeze_it=False):
        self._repeated_capability_list = repeated_capability_list
        self._repeated_capability = ','.join(repeated_capability_list)
        self._all_channels_in_session = all_channels_in_session
        self._interpreter = interpreter

        # Store the parameter list for later printing in __repr__
        param_list = []
        param_list.append("repeated_capability_list=" + pp.pformat(repeated_capability_list))
        param_list.append("interpreter=" + pp.pformat(interpreter))
        self._param_list = ', '.join(param_list)

        # Instantiate any repeated capability objects
        self.channels = _RepeatedCapabilities(self, '', repeated_capability_list)

        # Finally, set _is_frozen to True which is used to prevent clients from accidentally adding
        # members when trying to set a property with a typo.
        self._is_frozen = freeze_it

    def __repr__(self):
        return '{0}.{1}({2})'.format('niswitch', self.__class__.__name__, self._param_list)

    def __setattr__(self, key, value):
        if self._is_frozen and key not in dir(self):
            raise AttributeError("'{0}' object has no attribute '{1}'".format(type(self).__name__, key))
        object.__setattr__(self, key, value)

    ''' These are code-generated '''

    @ivi_synchronized
    def _get_attribute_vi_boolean(self, attribute_id):
        r'''_get_attribute_vi_boolean

        This method queries the value of a ViBoolean property. You can use
        this method to get the values of instrument specific properties and
        inherent IVI properties. If the property represents an instrument
        state, this method performs instrument I/O in the following cases: -
        State caching is disabled for the entire session or for the particular
        property. - State caching is enabled and the currently cached value is
        invalid.

        Tip:
        This method can be called on specific channels within your :py:class:`niswitch.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_boolean`

        To call the method on all channels, you can call it directly on the :py:class:`niswitch.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_boolean`

        Args:
            attribute_id (int): Pass the ID of a property. From the method panel window, you can use
                this control as follows. - Click on the control or press , , or , to
                display a dialog box containing a hierarchical list of the available
                properties. Properties whose value cannot be set are dim. Help text is
                shown for each property. Select a property by double-clicking on it
                or by selecting it and then pressing . A ring control at the top of the
                dialog box allows you to see all IVI properties or only the properties
                of the ViInt32 type. If you choose to see all IVI properties, the data
                types appear to the right of the property names in the list box. The
                data types that are not consistent with this method are dim. If you
                select a property data type that is dim, LabWindows/CVI transfers you
                to the method panel for the corresponding method that is consistent
                with the data type. - If you want to enter a variable name, press to
                change this ring control to a manual input box. - If the property in
                this ring control has constants as valid values, you can view the
                constants by moving to the Property Value control and pressing .


        Returns:
            attribute_value (bool): Returns the current value of the property. Pass the address of a
                ViBoolean variable. From the method panel window, you can use this
                control as follows. - If the property currently showing in the
                Property ID ring control has constants as valid values, you can view a
                list of the constants by pressing on this control. Select a value by
                double-clicking on it or by selecting it and then pressing .

        '''
        attribute_value = self._interpreter.get_attribute_vi_boolean(self._repeated_capability, attribute_id)
        return attribute_value

    @ivi_synchronized
    def _get_attribute_vi_int32(self, attribute_id):
        r'''_get_attribute_vi_int32

        This method queries the value of a ViInt32 property. You can use this
        method to get the values of instrument specific properties and
        inherent IVI properties. If the property represents an instrument
        state, this method performs instrument I/O in the following cases: -
        State caching is disabled for the entire session or for the particular
        property. - State caching is enabled and the currently cached value is
        invalid.

        Tip:
        This method can be called on specific channels within your :py:class:`niswitch.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_int32`

        To call the method on all channels, you can call it directly on the :py:class:`niswitch.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_int32`

        Args:
            attribute_id (int): Pass the ID of a property. From the method panel window, you can use
                this control as follows. - Click on the control or press , , or , to
                display a dialog box containing a hierarchical list of the available
                properties. Properties whose value cannot be set are dim. Help text is
                shown for each property. Select a property by double-clicking on it
                or by selecting it and then pressing . A ring control at the top of the
                dialog box allows you to see all IVI properties or only the properties
                of the ViInt32 type. If you choose to see all IVI properties, the data
                types appear to the right of the property names in the list box. The
                data types that are not consistent with this method are dim. If you
                select a property data type that is dim, LabWindows/CVI transfers you
                to the method panel for the corresponding method that is consistent
                with the data type. - If you want to enter a variable name, press to
                change this ring control to a manual input box. - If the property in
                this ring control has constants as valid values, you can view the
                constants by moving to the Property Value control and pressing .


        Returns:
            attribute_value (int): Returns the current value of the property. Pass the address of a
                ViInt32 variable. From the method panel window, you can use this
                control as follows. - If the property currently showing in the
                Property ID ring control has constants as valid values, you can view a
                list of the constants by pressing on this control. Select a value by
                double-clicking on it or by selecting it and then pressing .

        '''
        attribute_value = self._interpreter.get_attribute_vi_int32(self._repeated_capability, attribute_id)
        return attribute_value

    @ivi_synchronized
    def _get_attribute_vi_real64(self, attribute_id):
        r'''_get_attribute_vi_real64

        This method queries the value of a ViReal64 property. You can use
        this method to get the values of instrument specific properties and
        inherent IVI properties. If the property represents an instrument
        state, this method performs instrument I/O in the following cases: -
        State caching is disabled for the entire session or for the particular
        property. - State caching is enabled and the currently cached value is
        invalid.

        Tip:
        This method can be called on specific channels within your :py:class:`niswitch.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_real64`

        To call the method on all channels, you can call it directly on the :py:class:`niswitch.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_real64`

        Args:
            attribute_id (int): Pass the ID of a property. From the method panel window, you can use
                this control as follows. - Click on the control or press , , or , to
                display a dialog box containing a hierarchical list of the available
                properties. Properties whose value cannot be set are dim. Help text is
                shown for each property. Select a property by double-clicking on it
                or by selecting it and then pressing . A ring control at the top of the
                dialog box allows you to see all IVI properties or only the properties
                of the ViInt32 type. If you choose to see all IVI properties, the data
                types appear to the right of the property names in the list box. The
                data types that are not consistent with this method are dim. If you
                select a property data type that is dim, LabWindows/CVI transfers you
                to the method panel for the corresponding method that is consistent
                with the data type. - If you want to enter a variable name, press to
                change this ring control to a manual input box. - If the property in
                this ring control has constants as valid values, you can view the
                constants by moving to the Property Value control and pressing .


        Returns:
            attribute_value (float): Returns the current value of the property. Pass the address of a
                ViReal64 variable. From the method panel window, you can use this
                control as follows. - If the property currently showing in the
                Property ID ring control has constants as valid values, you can view a
                list of the constants by pressing on this control. Select a value by
                double-clicking on it or by selecting it and then pressing .

        '''
        attribute_value = self._interpreter.get_attribute_vi_real64(self._repeated_capability, attribute_id)
        return attribute_value

    @ivi_synchronized
    def _get_attribute_vi_string(self, attribute_id):
        r'''_get_attribute_vi_string

        This method queries the value of a ViString property. You can use
        this method to get the values of instrument specific properties and
        inherent IVI properties. If the property represents an instrument
        state, this method performs instrument I/O in the following cases: -
        State caching is disabled for the entire session or for the particular
        property. - State caching is enabled and the currently cached value is
        invalid. You must provide a ViChar array to serve as a buffer for the
        value. You pass the number of bytes in the buffer as the Array Size
        parameter. If the current value of the property, including the
        terminating NULL byte, is larger than the size you indicate in the Array
        Size parameter, the method copies Array Size-1 bytes into the buffer,
        places an ASCII NULL byte at the end of the buffer, and returns the
        array size you must pass to get the entire value. For example, if the
        value is "123456" and the Array Size is 4, the method places "123"
        into the buffer and returns 7. If you want to call this method just to
        get the required array size, you can pass 0 for the Array Size and
        VI_NULL for the Property Value buffer. If you want the method to
        fill in the buffer regardless of the number of bytes in the value, pass
        a negative number for the Array Size parameter.

        Tip:
        This method can be called on specific channels within your :py:class:`niswitch.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_string`

        To call the method on all channels, you can call it directly on the :py:class:`niswitch.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_string`

        Args:
            attribute_id (int): Pass the ID of a property. From the method panel window, you can use
                this control as follows. - Click on the control or press , , or , to
                display a dialog box containing a hierarchical list of the available
                properties. Properties whose value cannot be set are dim. Help text is
                shown for each property. Select a property by double-clicking on it
                or by selecting it and then pressing . A ring control at the top of the
                dialog box allows you to see all IVI properties or only the properties
                of the ViInt32 type. If you choose to see all IVI properties, the data
                types appear to the right of the property names in the list box. The
                data types that are not consistent with this method are dim. If you
                select a property data type that is dim, LabWindows/CVI transfers you
                to the method panel for the corresponding method that is consistent
                with the data type. - If you want to enter a variable name, press to
                change this ring control to a manual input box. - If the property in
                this ring control has constants as valid values, you can view the
                constants by moving to the Property Value control and pressing .


        Returns:
            attribute_value (str): The buffer in which the method returns the current value of the
                property. The buffer must be of type ViChar and have at least as many
                bytes as indicated in the Array Size parameter. If the current value of
                the property, including the terminating NUL byte, contains more bytes
                that you indicate in this parameter, the method copies Array Size-1
                bytes into the buffer, places an ASCII NUL byte at the end of the
                buffer, and returns the array size you must pass to get the entire
                value. For example, if the value is "123456" and the Array Size is 4,
                the method places "123" into the buffer and returns 7. If you specify
                0 for the Array Size parameter, you can pass VI_NULL for this
                parameter. From the method panel window, you can use this control as
                follows. - If the property currently showing in the Property ID ring
                control has constants as valid values, you can view a list of the
                constants by pressing on this control. Select a value by double-clicking
                on it or by selecting it and then pressing .

        '''
        attribute_value = self._interpreter.get_attribute_vi_string(self._repeated_capability, attribute_id)
        return attribute_value

    def lock(self):
        '''lock

        Obtains a multithread lock on the device session. Before doing so, the
        software waits until all other execution threads release their locks
        on the device session.

        Other threads may have obtained a lock on this session for the
        following reasons:

            -  The application called the lock method.
            -  A call to NI-SWITCH locked the session.
            -  After a call to the lock method returns
               successfully, no other threads can access the device session until
               you call the unlock method or exit out of the with block when using
               lock context manager.
            -  Use the lock method and the
               unlock method around a sequence of calls to
               instrument driver methods if you require that the device retain its
               settings through the end of the sequence.

        You can safely make nested calls to the lock method
        within the same thread. To completely unlock the session, you must
        balance each call to the lock method with a call to
        the unlock method.

        Returns:
            lock (context manager): When used in a with statement, niswitch.Session.lock acts as
            a context manager and unlock will be called when the with block is exited
        '''
        self._interpreter.lock()  # We do not call this in the context manager so that this function can
        # act standalone as well and let the client call unlock() explicitly. If they do use the context manager,
        # that will handle the unlock for them
        return _Lock(self)

    @ivi_synchronized
    def _set_attribute_vi_boolean(self, attribute_id, attribute_value):
        r'''_set_attribute_vi_boolean

        This method sets the value of a ViBoolean property. This is a
        low-level method that you can use to set the values of
        instrument-specific properties and inherent IVI properties. If the
        property represents an instrument state, this method performs
        instrument I/O in the following cases: - State caching is disabled for
        the entire session or for the particular property. - State caching is
        enabled and the currently cached value is invalid or is different than
        the value you specify. This instrument driver contains high-level
        methods that set most of the instrument properties. It is best to use
        the high-level driver methods as much as possible. They handle order
        dependencies and multithread locking for you. In addition, they perform
        status checking only after setting all of the properties. In contrast,
        when you set multiple properties using the SetAttribute methods, the
        methods check the instrument status after each call. Also, when state
        caching is enabled, the high-level methods that configure multiple
        properties perform instrument I/O only for the properties whose value
        you change. Thus, you can safely call the high-level methods without
        the penalty of redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`niswitch.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_boolean`

        To call the method on all channels, you can call it directly on the :py:class:`niswitch.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_boolean`

        Args:
            attribute_id (int): Pass the ID of a property. From the method panel window, you can use
                this control as follows. - Click on the control or press , , or , to
                display a dialog box containing a hierarchical list of the available
                properties. Properties whose value cannot be set are dim. Help text is
                shown for each property. Select a property by double-clicking on it
                or by selecting it and then pressing . Read-only properties appear dim
                in the list box. If you select a read-only property, an error message
                appears. A ring control at the top of the dialog box allows you to see
                all IVI properties or only the properties of the ViInt32 type. If you
                choose to see all IVI properties, the data types appear to the right of
                the property names in the list box. The data types that are not
                consistent with this method are dim. If you select a property data
                type that is dim, LabWindows/CVI transfers you to the method panel for
                the corresponding method that is consistent with the data type. - If
                you want to enter a variable name, press to change this ring control to
                a manual input box. - If the property in this ring control has
                constants as valid values, you can view the constants by moving to the
                Property Value control and pressing .

            attribute_value (bool): Pass the value to which you want to set the property. From the method
                panel window, you can use this control as follows. - If the property
                currently showing in the Property ID ring control has constants as
                valid values, you can view a list of the constants by pressing on this
                control. Select a value by double-clicking on it or by selecting it and
                then pressing . Note: Some of the values might not be valid depending on
                the current settings of the instrument session. Default Value: none

        '''
        self._interpreter.set_attribute_vi_boolean(self._repeated_capability, attribute_id, attribute_value)

    @ivi_synchronized
    def _set_attribute_vi_int32(self, attribute_id, attribute_value):
        r'''_set_attribute_vi_int32

        This method sets the value of a ViInt32 property. This is a low-level
        method that you can use to set the values of instrument-specific
        properties and inherent IVI properties. If the property represents an
        instrument state, this method performs instrument I/O in the following
        cases: - State caching is disabled for the entire session or for the
        particular property. - State caching is enabled and the currently
        cached value is invalid or is different than the value you specify. This
        instrument driver contains high-level methods that set most of the
        instrument properties. It is best to use the high-level driver methods
        as much as possible. They handle order dependencies and multithread
        locking for you. In addition, they perform status checking only after
        setting all of the properties. In contrast, when you set multiple
        properties using the SetAttribute methods, the methods check the
        instrument status after each call. Also, when state caching is enabled,
        the high-level methods that configure multiple properties perform
        instrument I/O only for the properties whose value you change. Thus, you
        can safely call the high-level methods without the penalty of
        redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`niswitch.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_int32`

        To call the method on all channels, you can call it directly on the :py:class:`niswitch.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_int32`

        Args:
            attribute_id (int): Pass the ID of a property. From the method panel window, you can use
                this control as follows. - Click on the control or press , , or , to
                display a dialog box containing a hierarchical list of the available
                properties. Properties whose value cannot be set are dim. Help text is
                shown for each property. Select a property by double-clicking on it
                or by selecting it and then pressing . Read-only properties appear dim
                in the list box. If you select a read-only property, an error message
                appears. A ring control at the top of the dialog box allows you to see
                all IVI properties or only the properties of the ViInt32 type. If you
                choose to see all IVI properties, the data types appear to the right of
                the property names in the list box. The data types that are not
                consistent with this method are dim. If you select a property data
                type that is dim, LabWindows/CVI transfers you to the method panel for
                the corresponding method that is consistent with the data type. - If
                you want to enter a variable name, press to change this ring control to
                a manual input box. - If the property in this ring control has
                constants as valid values, you can view the constants by moving to the
                Property Value control and pressing .

            attribute_value (int): Pass the value to which you want to set the property. From the method
                panel window, you can use this control as follows. - If the property
                currently showing in the Property ID ring control has constants as
                valid values, you can view a list of the constants by pressing on this
                control. Select a value by double-clicking on it or by selecting it and
                then pressing . Note: Some of the values might not be valid depending on
                the current settings of the instrument session. Default Value: none

        '''
        self._interpreter.set_attribute_vi_int32(self._repeated_capability, attribute_id, attribute_value)

    @ivi_synchronized
    def _set_attribute_vi_real64(self, attribute_id, attribute_value):
        r'''_set_attribute_vi_real64

        This method sets the value of a ViReal64 property. This is a
        low-level method that you can use to set the values of
        instrument-specific properties and inherent IVI properties. If the
        property represents an instrument state, this method performs
        instrument I/O in the following cases: - State caching is disabled for
        the entire session or for the particular property. - State caching is
        enabled and the currently cached value is invalid or is different than
        the value you specify. This instrument driver contains high-level
        methods that set most of the instrument properties. It is best to use
        the high-level driver methods as much as possible. They handle order
        dependencies and multithread locking for you. In addition, they perform
        status checking only after setting all of the properties. In contrast,
        when you set multiple properties using the SetAttribute methods, the
        methods check the instrument status after each call. Also, when state
        caching is enabled, the high-level methods that configure multiple
        properties perform instrument I/O only for the properties whose value
        you change. Thus, you can safely call the high-level methods without
        the penalty of redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`niswitch.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_real64`

        To call the method on all channels, you can call it directly on the :py:class:`niswitch.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_real64`

        Args:
            attribute_id (int): Pass the ID of a property. From the method panel window, you can use
                this control as follows. - Click on the control or press , , or , to
                display a dialog box containing a hierarchical list of the available
                properties. Properties whose value cannot be set are dim. Help text is
                shown for each property. Select a property by double-clicking on it
                or by selecting it and then pressing . Read-only properties appear dim
                in the list box. If you select a read-only property, an error message
                appears. A ring control at the top of the dialog box allows you to see
                all IVI properties or only the properties of the ViInt32 type. If you
                choose to see all IVI properties, the data types appear to the right of
                the property names in the list box. The data types that are not
                consistent with this method are dim. If you select a property data
                type that is dim, LabWindows/CVI transfers you to the method panel for
                the corresponding method that is consistent with the data type. - If
                you want to enter a variable name, press to change this ring control to
                a manual input box. - If the property in this ring control has
                constants as valid values, you can view the constants by moving to the
                Property Value control and pressing .

            attribute_value (float): Pass the value to which you want to set the property. From the method
                panel window, you can use this control as follows. - If the property
                currently showing in the Property ID ring control has constants as
                valid values, you can view a list of the constants by pressing on this
                control. Select a value by double-clicking on it or by selecting it and
                then pressing . Note: Some of the values might not be valid depending on
                the current settings of the instrument session. Default Value: none

        '''
        self._interpreter.set_attribute_vi_real64(self._repeated_capability, attribute_id, attribute_value)

    @ivi_synchronized
    def _set_attribute_vi_string(self, attribute_id, attribute_value):
        r'''_set_attribute_vi_string

        This method sets the value of a ViString property. This is a
        low-level method that you can use to set the values of
        instrument-specific properties and inherent IVI properties. If the
        property represents an instrument state, this method performs
        instrument I/O in the following cases: - State caching is disabled for
        the entire session or for the particular property. - State caching is
        enabled and the currently cached value is invalid or is different than
        the value you specify. This instrument driver contains high-level
        methods that set most of the instrument properties. It is best to use
        the high-level driver methods as much as possible. They handle order
        dependencies and multithread locking for you. In addition, they perform
        status checking only after setting all of the properties. In contrast,
        when you set multiple properties using the SetAttribute methods, the
        methods check the instrument status after each call. Also, when state
        caching is enabled, the high-level methods that configure multiple
        properties perform instrument I/O only for the properties whose value
        you change. Thus, you can safely call the high-level methods without
        the penalty of redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`niswitch.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_string`

        To call the method on all channels, you can call it directly on the :py:class:`niswitch.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_string`

        Args:
            attribute_id (int): Pass the ID of a property. From the method panel window, you can use
                this control as follows. - Click on the control or press , , or , to
                display a dialog box containing a hierarchical list of the available
                properties. Properties whose value cannot be set are dim. Help text is
                shown for each property. Select a property by double-clicking on it
                or by selecting it and then pressing . Read-only properties appear dim
                in the list box. If you select a read-only property, an error message
                appears. A ring control at the top of the dialog box allows you to see
                all IVI properties or only the properties of the ViInt32 type. If you
                choose to see all IVI properties, the data types appear to the right of
                the property names in the list box. The data types that are not
                consistent with this method are dim. If you select a property data
                type that is dim, LabWindows/CVI transfers you to the method panel for
                the corresponding method that is consistent with the data type. - If
                you want to enter a variable name, press to change this ring control to
                a manual input box. - If the property in this ring control has
                constants as valid values, you can view the constants by moving to the
                Property Value control and pressing .

            attribute_value (str): Pass the value to which you want to set the property. From the method
                panel window, you can use this control as follows. - If the property
                currently showing in the Property ID ring control has constants as
                valid values, you can view a list of the constants by pressing on this
                control. Select a value by double-clicking on it or by selecting it and
                then pressing . Note: Some of the values might not be valid depending on
                the current settings of the instrument session. Default Value: none

        '''
        self._interpreter.set_attribute_vi_string(self._repeated_capability, attribute_id, attribute_value)

    def unlock(self):
        '''unlock

        Releases a lock that you acquired on an device session using
        lock. Refer to lock for additional
        information on session locks.
        '''
        self._interpreter.unlock()

    def _error_message(self, error_code):
        r'''_error_message

        Converts an error code returned by NI-SWITCH into a user-readable
        string. Generally this information is supplied in error out of any
        NI-SWITCH VI. Use _error_message for a static lookup of an
        error code description.

        Args:
            error_code (int): Status code returned by any NI-SWITCH method. Default Value: 0
                (VI_SUCCESS)


        Returns:
            error_message (str): The error information formatted into a string. You must pass a ViChar
                array with at least 256 bytes.

        '''
        error_message = self._interpreter.error_message(error_code)
        return error_message


class Session(_SessionBase):
    '''An NI-SWITCH session to an NI switch module.'''

    def __init__(self, resource_name, topology="Configured Topology", simulate=False, reset_device=False, *, grpc_options=None):
        r'''An NI-SWITCH session to an NI switch module.

        Returns a session handle used to identify the switch in all subsequent
        instrument driver calls and sets the topology of the switch.
        __init__ creates a new IVI instrument driver session
        for the switch specified in the resourceName parameter. The driver uses
        the topology specified in the topology parameter and overrides the
        topology specified in MAX. Note: When initializing an NI SwitchBlock
        device with topology, you must specify the topology created when you
        configured the device in MAX, using either
        "Configured Topology" or the topology string of the
        device. Refer to the Initializing with Topology for NI SwitchBlock
        Devices topic in the NI Switches Help for information about determining
        the topology string of an NI SwitchBlock device. By default, the switch
        is reset to a known state. Enable simulation by specifying the topology
        and setting the simulate parameter to True.

        Args:
            resource_name (str): Resource name of the switch module to initialize. Default value: None
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

            topology (str): Pass the topology name you want to use for the switch you specify with
                Resource Name parameter. You can also pass
                "Configured Topology" to use the last topology that
                was configured for the device in MAX.
                Default Value:
                "Configured Topology"
                Valid Values:
                "Configured Topology"
                "2501/1-Wire 48x1 Mux"
                "2501/1-Wire 48x1 Amplified Mux"
                "2501/2-Wire 24x1 Mux"
                "2501/2-Wire 24x1 Amplified Mux"
                "2501/2-Wire Dual 12x1 Mux"
                "2501/2-Wire Quad 6x1 Mux"
                "2501/2-Wire 4x6 Matrix"
                "2501/4-Wire 12x1 Mux"
                "2503/1-Wire 48x1 Mux"
                "2503/2-Wire 24x1 Mux"
                "2503/2-Wire Dual 12x1 Mux"
                "2503/2-Wire Quad 6x1 Mux"
                "2503/2-Wire 4x6 Matrix"
                "2503/4-Wire 12x1 Mux"
                "2510/Independent"
                "2512/Independent"
                "2514/Independent"
                "2515/Independent"
                "2520/80-SPST"
                "2521/40-DPST"
                "2522/53-SPDT"
                "2523/26-DPDT"
                "2524/1-Wire 128x1 Mux"
                "2524/1-Wire Dual 64x1 Mux"
                "2524/1-Wire Quad 32x1 Mux"
                "2524/1-Wire Octal 16x1 Mux"
                "2524/1-Wire Sixteen 8x1 Mux"
                "2525/2-Wire 64x1 Mux"
                "2525/2-Wire Dual 32x1 Mux"
                "2525/2-Wire Quad 16x1 Mux"
                "2525/2-Wire Octal 8x1 Mux"
                "2525/2-Wire Sixteen 4x1 Mux"
                "2526/1-Wire 158x1 Mux"
                "2526/2-Wire 79x1 Mux"
                "2527/1-Wire 64x1 Mux"
                "2527/1-Wire Dual 32x1 Mux"
                "2527/2-Wire 32x1 Mux"
                "2527/2-Wire Dual 16x1 Mux"
                "2527/4-Wire 16x1 Mux"
                "2527/Independent"
                "2529/2-Wire Dual 4x16 Matrix"
                "2529/2-Wire 8x16 Matrix"
                "2529/2-Wire 4x32 Matrix"
                "2530/1-Wire 128x1 Mux"
                "2530/1-Wire Dual 64x1 Mux"
                "2530/1-Wire 4x32 Matrix"
                "2530/1-Wire 8x16 Matrix"
                "2530/1-Wire Octal 16x1 Mux"
                "2530/1-Wire Quad 32x1 Mux"
                "2530/2-Wire 4x16 Matrix"
                "2530/2-Wire 64x1 Mux"
                "2530/2-Wire Dual 32x1 Mux"
                "2530/2-Wire Quad 16x1 Mux"
                "2530/4-Wire 32x1 Mux"
                "2530/4-Wire Dual 16x1 Mux"
                "2530/Independent"
                "2531/1-Wire 4x128 Matrix"
                "2531/1-Wire 8x64 Matrix"
                "2531/1-Wire Dual 4x64 Matrix"
                "2531/1-Wire Dual 8x32 Matrix"
                "2531/2-Wire 4x64 Matrix"
                "2531/2-Wire 8x32 Matrix"
                "2532/1-Wire 16x32 Matrix"
                "2532/1-Wire 4x128 Matrix"
                "2532/1-Wire 8x64 Matrix"
                "2532/1-Wire Dual 16x16 Matrix"
                "2532/1-Wire Dual 4x64 Matrix"
                "2532/1-Wire Dual 8x32 Matrix"
                "2532/1-Wire Quad 4x32 Matrix"
                "2532/1-Wire Sixteen 2x16 Matrix"
                "2532/2-Wire 16x16 Matrix"
                "2532/2-Wire 4x64 Matrix"
                "2532/2-Wire 8x32 Matrix"
                "2532/2-Wire Dual 4x32 Matrix"
                "2533/1-Wire 4x64 Matrix"
                "2534/1-Wire 8x32 Matrix"
                "2535/1-Wire 4x136 Matrix"
                "2536/1-Wire 8x68 Matrix"
                "2540/1-Wire 8x9 Matrix"
                "2541/1-Wire 8x12 Matrix"
                "2542/Quad 2x1 Terminated Mux"
                "2543/Dual 4x1 Terminated Mux"
                "2544/8x1 Terminated Mux"
                "2545/4x1 Terminated Mux"
                "2546/Dual 4x1 Mux"
                "2547/8x1 Mux"
                "2548/4-SPDT"
                "2549/Terminated 2-SPDT"
                "2554/4x1 Mux"
                "2555/4x1 Terminated Mux"
                "2556/Dual 4x1 Mux"
                "2557/8x1 Mux"
                "2558/4-SPDT"
                "2559/Terminated 2-SPDT"
                "2564/16-SPST"
                "2564/8-DPST"
                "2565/16-SPST"
                "2566/16-SPDT"
                "2566/8-DPDT"
                "2567/Independent"
                "2568/15-DPST"
                "2568/31-SPST"
                "2569/100-SPST"
                "2569/50-DPST"
                "2570/20-DPDT"
                "2570/40-SPDT"
                "2571/66-SPDT"
                "2575/1-Wire 196x1 Mux"
                "2575/2-Wire 98x1 Mux"
                "2575/2-Wire 95x1 Mux"
                "2576/2-Wire 64x1 Mux"
                "2576/2-Wire Dual 32x1 Mux"
                "2576/2-Wire Octal 8x1 Mux"
                "2576/2-Wire Quad 16x1 Mux"
                "2576/2-Wire Sixteen 4x1 Mux"
                "2576/Independent"
                "2584/1-Wire 12x1 Mux"
                "2584/1-Wire Dual 6x1 Mux"
                "2584/2-Wire 6x1 Mux"
                "2584/Independent"
                "2585/1-Wire 10x1 Mux"
                "2586/10-SPST"
                "2586/5-DPST"
                "2590/4x1 Mux"
                "2591/4x1 Mux"
                "2593/16x1 Mux"
                "2593/8x1 Terminated Mux"
                "2593/Dual 8x1 Mux"
                "2593/Dual 4x1 Terminated Mux"
                "2593/Independent"
                "2594/4x1 Mux"
                "2595/4x1 Mux"
                "2596/Dual 6x1 Mux"
                "2597/6x1 Terminated Mux"
                "2598/Dual Transfer"
                "2599/2-SPDT"
                "2720/Independent"
                "2722/Independent"
                "2725/Independent"
                "2727/Independent"
                "2737/2-Wire 4x64 Matrix"
                "2738/2-Wire 8x32 Matrix"
                "2739/2-Wire 16x16 Matrix"
                "2746/Quad 4x1 Mux"
                "2747/Dual 8x1 Mux"
                "2748/16x1 Mux"
                "2790/Independent"
                "2796/Dual 6x1 Mux"
                "2797/6x1 Terminated Mux"
                "2798/Dual Transfer"
                "2799/2-SPDT"

            simulate (bool): Enables simulation of the switch module specified in the resource name
                parameter. Valid Values: True - simulate False - Don't simulate
                (Default Value)

            reset_device (bool): Specifies whether to reset the switch module during the initialization
                process. Valid Values: True - Reset Device (Default Value) False
                - Currently unsupported. The device will not reset.

            grpc_options (niswitch.grpc_session_options.GrpcSessionOptions): MeasurementLink gRPC session options


        Returns:
            session (niswitch.Session): A session object representing the device.

        '''
        if grpc_options:
            import niswitch._grpc_stub_interpreter as _grpc_stub_interpreter
            interpreter = _grpc_stub_interpreter.GrpcStubInterpreter(grpc_options)
        else:
            interpreter = _library_interpreter.LibraryInterpreter(encoding='windows-1251')

        # Initialize the superclass with default values first, populate them later
        super(Session, self).__init__(
            repeated_capability_list=[],
            interpreter=interpreter,
            freeze_it=False,
            all_channels_in_session=None
        )

        # Call specified init function
        # Note that _interpreter default-initializes the session handle in its constructor, so that
        # if _init_with_topology fails, the error handler can reference it.
        # And then here, once _init_with_topology succeeds, we call set_session_handle
        # with the actual session handle.
        self._interpreter.set_session_handle(self._init_with_topology(resource_name, topology, simulate, reset_device))

        # Store the parameter list for later printing in __repr__
        param_list = []
        param_list.append("resource_name=" + pp.pformat(resource_name))
        param_list.append("topology=" + pp.pformat(topology))
        param_list.append("simulate=" + pp.pformat(simulate))
        param_list.append("reset_device=" + pp.pformat(reset_device))
        self._param_list = ', '.join(param_list)

        # Store the list of channels in the Session which is needed by some nimi-python modules.
        # Use try/except because not all the modules support channels.
        # self.get_channel_names() and self.channel_count can only be called after the session
        # handle is set
        try:
            self._all_channels_in_session = self.get_channel_names(range(self.channel_count))
        except AttributeError:
            self._all_channels_in_session = None

        # Finally, set _is_frozen to True which is used to prevent clients from accidentally adding
        # members when trying to set a property with a typo.
        self._is_frozen = True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self._interpreter._close_on_exit:
            self.close()

    def initiate(self):
        '''initiate

        Commits the configured scan list and trigger settings to hardware and
        initiates the scan. If niSwitch Commit was called earlier, niSwitch
        Initiate Scan only initiates the scan and returns immediately. Once the
        scanning operation begins, you cannot perform any other operation other
        than GetAttribute, AbortScan, or SendSoftwareTrigger. All other
        methods return NISWITCH_ERROR_SCAN_IN_PROGRESS. To stop the
        scanning operation, To stop the scanning operation, call
        abort.

        Note:
        This method will return a Python context manager that will initiate on entering and abort on exit.
        '''
        return _Scan(self)

    def close(self):
        '''close

        Terminates the NI-SWITCH session and all of its properties and
        deallocates any memory resources the driver uses. Notes: (1) You must
        unlock the session before calling _close. (2) After calling
        _close, you cannot use the instrument driver again until you
        call init or InitWithOptions.

        Note:
        One or more of the referenced methods are not in the Python API for this driver.

        Note:
        This method is not needed when using the session context manager
        '''
        try:
            self._close()
        except errors.DriverError:
            self._interpreter.set_session_handle()
            raise
        self._interpreter.set_session_handle()

    ''' These are code-generated '''

    @ivi_synchronized
    def abort(self):
        r'''abort

        Aborts the scan in progress. Initiate a scan with
        initiate. If the switch module is not scanning,
        NISWITCH_ERROR_NO_SCAN_IN_PROGRESS error is returned.
        '''
        self._interpreter.abort()

    @ivi_synchronized
    def can_connect(self, channel1, channel2):
        r'''can_connect

        Verifies that a path between channel 1 and channel 2 can be created. If
        a path is possible in the switch module, the availability of that path
        is returned given the existing connections. If the path is possible but
        in use, a NISWITCH_WARN_IMPLICIT_CONNECTION_EXISTS warning is
        returned.

        Args:
            channel1 (str): Input one of the channel names of the desired path. Pass the other
                channel name as the channel 2 parameter. Refer to Devices Overview for
                valid channel names for the switch module. Examples of valid channel
                names: ch0, com0, ab0, r1, c2, cjtemp Default value: ""

            channel2 (str): Input one of the channel names of the desired path. Pass the other
                channel name as the channel 1 parameter. Refer to Devices Overview for
                valid channel names for the switch module. Examples of valid channel
                names: ch0, com0, ab0, r1, c2, cjtemp Default value: ""


        Returns:
            path_capability (enums.PathCapability): Indicates whether a path is valid. Possible values include:

                - PathCapability.PATH_AVAILABLE 1
                - PathCapability.PATH_EXISTS 2
                - PathCapability.PATH_UNSUPPORTED 3
                - PathCapability.RESOURCE_IN_USE 4
                - PathCapability.SOURCE_CONFLICT 5
                - PathCapability.CHANNEL_NOT_AVAILABLE 6

                Notes: (1)
                PathCapability.PATH_AVAILABLE indicates that the driver can create the
                path at this time. (2) PathCapability.PATH_EXISTS indicates that the
                path already exists. (3) PathCapability.PATH_UNSUPPORTED indicates that
                the instrument is not capable of creating a path between the channels
                you specify. (4) PathCapability.RESOURCE_IN_USE indicates that although
                the path is valid, the driver cannot create the path at this moment
                because the switch device is currently using one or more of the required
                channels to create another path. You must destroy the other path before
                creating this one. (5) PathCapability.SOURCE_CONFLICT indicates that
                the instrument cannot create a path because both channels are connected
                to a different source channel. (6)
                PathCapability.CHANNEL_NOT_AVAILABLE indicates that the driver cannot
                create a path between the two channels because one of the channels is a
                configuration channel and thus unavailable for external connections.

        '''
        path_capability = self._interpreter.can_connect(channel1, channel2)
        return path_capability

    @ivi_synchronized
    def commit(self):
        r'''commit

        Downloads the configured scan list and trigger settings to hardware.
        Calling commit optional as it is implicitly called during
        initiate. Use commit to arm triggers in a given
        order or to control when expensive hardware operations are performed.
        '''
        self._interpreter.commit()

    @ivi_synchronized
    def connect(self, channel1, channel2):
        r'''connect

        Creates a path between channel 1 and channel 2. The driver calculates
        and uses the shortest path between the two channels. Refer to Immediate
        Operations for information about Channel Usage types. If a path is not
        available, the method returns one of the following errors: -
        NISWITCH_ERROR_EXPLICIT_CONNECTION_EXISTS, if the two channels are
        already explicitly connected by calling either the connect or
        set_path method. -
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

        Args:
            channel1 (str): Input one of the channel names of the desired path. Pass the other
                channel name as the channel 2 parameter. Refer to Devices Overview for
                valid channel names for the switch module. Examples of valid channel
                names: ch0, com0, ab0, r1, c2, cjtemp Default value: None

            channel2 (str): Input one of the channel names of the desired path. Pass the other
                channel name as the channel 1 parameter. Refer to Devices Overview for
                valid channel names for the switch module. Examples of valid channel
                names: ch0, com0, ab0, r1, c2, cjtemp Default value: None

        '''
        self._interpreter.connect(channel1, channel2)

    @ivi_synchronized
    def connect_multiple(self, connection_list):
        r'''connect_multiple

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

        Args:
            connection_list (str): Connection List specifies a list of connections between channels to
                make. NI-SWITCH validates the connection list, and aborts execution of
                the list if errors are returned. Refer to Connection and Disconnection
                List Syntax for valid connection list syntax and examples. Refer to
                Devices Overview for valid channel names for the switch module. Example
                of a valid connection list: c0 -> r1, [c2 -> r2 -> c3] In this example,
                r2 is a configuration channel. Default value: None

        '''
        self._interpreter.connect_multiple(connection_list)

    @ivi_synchronized
    def disable(self):
        r'''disable

        Places the switch module in a quiescent state where it has minimal or no
        impact on the system to which it is connected. All channels are
        disconnected and any scan in progress is aborted.
        '''
        self._interpreter.disable()

    @ivi_synchronized
    def disconnect(self, channel1, channel2):
        r'''disconnect

        This method destroys the path between two channels that you create
        with the connect or set_path method. If a path is
        not connected or not available, the method returns the
        IVISWTCH_ERROR_NO_SUCH_PATH error.

        Args:
            channel1 (str): Input one of the channel names of the path to break. Pass the other
                channel name as the channel 2 parameter. Refer to Devices Overview for
                valid channel names for the switch module. Examples of valid channel
                names: ch0, com0, ab0, r1, c2, cjtemp Default value: None

            channel2 (str): Input one of the channel names of the path to break. Pass the other
                channel name as the channel 1 parameter. Refer to Devices Overview for
                valid channel names for the switch module. Examples of valid channel
                names: ch0, com0, ab0, r1, c2, cjtemp Default value: None

        '''
        self._interpreter.disconnect(channel1, channel2)

    @ivi_synchronized
    def disconnect_all(self):
        r'''disconnect_all

        Breaks all existing paths. If the switch module cannot break all paths,
        NISWITCH_WARN_PATH_REMAINS warning is returned.
        '''
        self._interpreter.disconnect_all()

    @ivi_synchronized
    def disconnect_multiple(self, disconnection_list):
        r'''disconnect_multiple

        Breaks the connections between channels specified in Disconnection List.
        If no connections exist between channels, NI-SWITCH returns an error. In
        the event of an error, the VI stops at the point in the list where the
        error occurred.

        Args:
            disconnection_list (str): Disconnection List specifies a list of connections between channels to
                break. NI-SWITCH validates the disconnection list, and aborts execution
                of the list if errors are returned. Refer to Connection and
                Disconnection List Syntax for valid disconnection list syntax and
                examples. Refer to Devices Overview for valid channel names for the
                switch module. Example of a valid disconnection list: c0 -> r1, [c2 ->
                r2 -> c3] In this example, r2 is a configuration channel. Default value:
                None

        '''
        self._interpreter.disconnect_multiple(disconnection_list)

    @ivi_synchronized
    def get_channel_name(self, index):
        r'''get_channel_name

        Returns the channel string that is in the channel table at the specified
        index. Use get_channel_name in a For Loop to get a complete list
        of valid channel names for the switch module. Use the Channel Count
        property to determine the number of channels.

        Args:
            index (int): A 1-based index into the channel table. Default value: 1 Maximum value:
                Value of Channel Count property.


        Returns:
            channel_name_buffer (str): Returns the channel name that is in the channel table at the index you
                specify.

        '''
        channel_name_buffer = self._interpreter.get_channel_name(index)
        return channel_name_buffer

    @ivi_synchronized
    def get_path(self, channel1, channel2):
        r'''get_path

        Returns a string that identifies the explicit path created with
        connect. Pass this string to set_path to establish
        the exact same path in future connections. In some cases, multiple paths
        are available between two channels. When you call connect, the
        driver selects an available path. With connect, there is no
        guarantee that the driver selected path will always be the same path
        through the switch module. get_path only returns those paths
        explicitly created by niSwitch Connect Channels or set_path.
        For example, if you connect channels CH1 and CH3,and then channels CH2
        and CH3, an explicit path between channels CH1 and CH2 does not exist an
        error is returned

        Args:
            channel1 (str): Input one of the channel names of the desired path. Pass the other
                channel name as the channel 2 parameter. Refer to Devices Overview for
                valid channel names for the switch module. Examples of valid channel
                names: ch0, com0, ab0, r1, c2, cjtemp Default value: ""

            channel2 (str): Input one of the channel names of the desired path. Pass the other
                channel name as the channel 1 parameter. Refer to Devices Overview for
                valid channel names for the switch module. Examples of valid channel
                names: ch0, com0, ab0, r1, c2, cjtemp Default value: ""


        Returns:
            path (str): A string composed of comma-separated paths between channel 1 and channel
                2. The first and last names in the path are the endpoints of the path.
                All other channels in the path are configuration channels. Examples of
                returned paths: ch0->com0, com0->ab0

        '''
        path = self._interpreter.get_path(channel1, channel2)
        return path

    @ivi_synchronized
    def get_relay_count(self, relay_name):
        r'''get_relay_count

        Returns the number of times the relay has changed from Closed to Open.
        Relay count is useful for tracking relay lifetime and usage. Call
        wait_for_debounce before get_relay_count to ensure an
        accurate count. Refer to the Relay Count topic in the NI Switches Help
        to determine if the switch module supports relay counting.

        Args:
            relay_name (str): Name of the relay. Default value: None Examples of valid relay names:
                ch0, ab0, 1wire, hlselect Refer to Devices Overview for a list of valid
                relay names for the switch module.


        Returns:
            relay_count (int): The number of relay cycles.

        '''
        relay_count = self._interpreter.get_relay_count(relay_name)
        return relay_count

    @ivi_synchronized
    def get_relay_name(self, index):
        r'''get_relay_name

        Returns the relay name string that is in the relay list at the specified
        index. Use get_relay_name in a For Loop to get a complete list
        of valid relay names for the switch module. Use the Number of Relays
        property to determine the number of relays.

        Args:
            index (int): A 1-based index into the channel table. Default value: 1 Maximum value:
                Value of Channel Count property.


        Returns:
            relay_name_buffer (str): Returns the relay name for the index you specify.

        '''
        relay_name_buffer = self._interpreter.get_relay_name(index)
        return relay_name_buffer

    @ivi_synchronized
    def get_relay_position(self, relay_name):
        r'''get_relay_position

        Returns the relay position for the relay specified in the Relay Name
        parameter.

        Args:
            relay_name (str): Name of the relay. Default value: None Examples of valid relay names:
                ch0, ab0, 1wire, hlselect Refer to Devices Overview for a list of valid
                relay names for the switch module.


        Returns:
            relay_position (enums.RelayPosition): Indicates whether the relay is open or closed. RelayPosition.OPEN 10
                RelayPosition.CLOSED 11

        '''
        relay_position = self._interpreter.get_relay_position(relay_name)
        return relay_position

    def _init_with_topology(self, resource_name, topology="Configured Topology", simulate=False, reset_device=False):
        r'''_init_with_topology

        Returns a session handle used to identify the switch in all subsequent
        instrument driver calls and sets the topology of the switch.
        __init__ creates a new IVI instrument driver session
        for the switch specified in the resourceName parameter. The driver uses
        the topology specified in the topology parameter and overrides the
        topology specified in MAX. Note: When initializing an NI SwitchBlock
        device with topology, you must specify the topology created when you
        configured the device in MAX, using either
        "Configured Topology" or the topology string of the
        device. Refer to the Initializing with Topology for NI SwitchBlock
        Devices topic in the NI Switches Help for information about determining
        the topology string of an NI SwitchBlock device. By default, the switch
        is reset to a known state. Enable simulation by specifying the topology
        and setting the simulate parameter to True.

        Args:
            resource_name (str): Resource name of the switch module to initialize. Default value: None
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

            topology (str): Pass the topology name you want to use for the switch you specify with
                Resource Name parameter. You can also pass
                "Configured Topology" to use the last topology that
                was configured for the device in MAX.
                Default Value:
                "Configured Topology"
                Valid Values:
                "Configured Topology"
                "2501/1-Wire 48x1 Mux"
                "2501/1-Wire 48x1 Amplified Mux"
                "2501/2-Wire 24x1 Mux"
                "2501/2-Wire 24x1 Amplified Mux"
                "2501/2-Wire Dual 12x1 Mux"
                "2501/2-Wire Quad 6x1 Mux"
                "2501/2-Wire 4x6 Matrix"
                "2501/4-Wire 12x1 Mux"
                "2503/1-Wire 48x1 Mux"
                "2503/2-Wire 24x1 Mux"
                "2503/2-Wire Dual 12x1 Mux"
                "2503/2-Wire Quad 6x1 Mux"
                "2503/2-Wire 4x6 Matrix"
                "2503/4-Wire 12x1 Mux"
                "2510/Independent"
                "2512/Independent"
                "2514/Independent"
                "2515/Independent"
                "2520/80-SPST"
                "2521/40-DPST"
                "2522/53-SPDT"
                "2523/26-DPDT"
                "2524/1-Wire 128x1 Mux"
                "2524/1-Wire Dual 64x1 Mux"
                "2524/1-Wire Quad 32x1 Mux"
                "2524/1-Wire Octal 16x1 Mux"
                "2524/1-Wire Sixteen 8x1 Mux"
                "2525/2-Wire 64x1 Mux"
                "2525/2-Wire Dual 32x1 Mux"
                "2525/2-Wire Quad 16x1 Mux"
                "2525/2-Wire Octal 8x1 Mux"
                "2525/2-Wire Sixteen 4x1 Mux"
                "2526/1-Wire 158x1 Mux"
                "2526/2-Wire 79x1 Mux"
                "2527/1-Wire 64x1 Mux"
                "2527/1-Wire Dual 32x1 Mux"
                "2527/2-Wire 32x1 Mux"
                "2527/2-Wire Dual 16x1 Mux"
                "2527/4-Wire 16x1 Mux"
                "2527/Independent"
                "2529/2-Wire Dual 4x16 Matrix"
                "2529/2-Wire 8x16 Matrix"
                "2529/2-Wire 4x32 Matrix"
                "2530/1-Wire 128x1 Mux"
                "2530/1-Wire Dual 64x1 Mux"
                "2530/1-Wire 4x32 Matrix"
                "2530/1-Wire 8x16 Matrix"
                "2530/1-Wire Octal 16x1 Mux"
                "2530/1-Wire Quad 32x1 Mux"
                "2530/2-Wire 4x16 Matrix"
                "2530/2-Wire 64x1 Mux"
                "2530/2-Wire Dual 32x1 Mux"
                "2530/2-Wire Quad 16x1 Mux"
                "2530/4-Wire 32x1 Mux"
                "2530/4-Wire Dual 16x1 Mux"
                "2530/Independent"
                "2531/1-Wire 4x128 Matrix"
                "2531/1-Wire 8x64 Matrix"
                "2531/1-Wire Dual 4x64 Matrix"
                "2531/1-Wire Dual 8x32 Matrix"
                "2531/2-Wire 4x64 Matrix"
                "2531/2-Wire 8x32 Matrix"
                "2532/1-Wire 16x32 Matrix"
                "2532/1-Wire 4x128 Matrix"
                "2532/1-Wire 8x64 Matrix"
                "2532/1-Wire Dual 16x16 Matrix"
                "2532/1-Wire Dual 4x64 Matrix"
                "2532/1-Wire Dual 8x32 Matrix"
                "2532/1-Wire Quad 4x32 Matrix"
                "2532/1-Wire Sixteen 2x16 Matrix"
                "2532/2-Wire 16x16 Matrix"
                "2532/2-Wire 4x64 Matrix"
                "2532/2-Wire 8x32 Matrix"
                "2532/2-Wire Dual 4x32 Matrix"
                "2533/1-Wire 4x64 Matrix"
                "2534/1-Wire 8x32 Matrix"
                "2535/1-Wire 4x136 Matrix"
                "2536/1-Wire 8x68 Matrix"
                "2540/1-Wire 8x9 Matrix"
                "2541/1-Wire 8x12 Matrix"
                "2542/Quad 2x1 Terminated Mux"
                "2543/Dual 4x1 Terminated Mux"
                "2544/8x1 Terminated Mux"
                "2545/4x1 Terminated Mux"
                "2546/Dual 4x1 Mux"
                "2547/8x1 Mux"
                "2548/4-SPDT"
                "2549/Terminated 2-SPDT"
                "2554/4x1 Mux"
                "2555/4x1 Terminated Mux"
                "2556/Dual 4x1 Mux"
                "2557/8x1 Mux"
                "2558/4-SPDT"
                "2559/Terminated 2-SPDT"
                "2564/16-SPST"
                "2564/8-DPST"
                "2565/16-SPST"
                "2566/16-SPDT"
                "2566/8-DPDT"
                "2567/Independent"
                "2568/15-DPST"
                "2568/31-SPST"
                "2569/100-SPST"
                "2569/50-DPST"
                "2570/20-DPDT"
                "2570/40-SPDT"
                "2571/66-SPDT"
                "2575/1-Wire 196x1 Mux"
                "2575/2-Wire 98x1 Mux"
                "2575/2-Wire 95x1 Mux"
                "2576/2-Wire 64x1 Mux"
                "2576/2-Wire Dual 32x1 Mux"
                "2576/2-Wire Octal 8x1 Mux"
                "2576/2-Wire Quad 16x1 Mux"
                "2576/2-Wire Sixteen 4x1 Mux"
                "2576/Independent"
                "2584/1-Wire 12x1 Mux"
                "2584/1-Wire Dual 6x1 Mux"
                "2584/2-Wire 6x1 Mux"
                "2584/Independent"
                "2585/1-Wire 10x1 Mux"
                "2586/10-SPST"
                "2586/5-DPST"
                "2590/4x1 Mux"
                "2591/4x1 Mux"
                "2593/16x1 Mux"
                "2593/8x1 Terminated Mux"
                "2593/Dual 8x1 Mux"
                "2593/Dual 4x1 Terminated Mux"
                "2593/Independent"
                "2594/4x1 Mux"
                "2595/4x1 Mux"
                "2596/Dual 6x1 Mux"
                "2597/6x1 Terminated Mux"
                "2598/Dual Transfer"
                "2599/2-SPDT"
                "2720/Independent"
                "2722/Independent"
                "2725/Independent"
                "2727/Independent"
                "2737/2-Wire 4x64 Matrix"
                "2738/2-Wire 8x32 Matrix"
                "2739/2-Wire 16x16 Matrix"
                "2746/Quad 4x1 Mux"
                "2747/Dual 8x1 Mux"
                "2748/16x1 Mux"
                "2790/Independent"
                "2796/Dual 6x1 Mux"
                "2797/6x1 Terminated Mux"
                "2798/Dual Transfer"
                "2799/2-SPDT"

            simulate (bool): Enables simulation of the switch module specified in the resource name
                parameter. Valid Values: True - simulate False - Don't simulate
                (Default Value)

            reset_device (bool): Specifies whether to reset the switch module during the initialization
                process. Valid Values: True - Reset Device (Default Value) False
                - Currently unsupported. The device will not reset.


        Returns:
            vi (int): A particular NI-SWITCH session established with
                __init__, InitWithOptions, or init
                and used for all subsequent NI-SWITCH calls.

                Note:
                One or more of the referenced methods are not in the Python API for this driver.

        '''
        vi = self._interpreter.init_with_topology(resource_name, topology, simulate, reset_device)
        return vi

    @ivi_synchronized
    def _initiate_scan(self):
        r'''_initiate_scan

        Commits the configured scan list and trigger settings to hardware and
        initiates the scan. If niSwitch Commit was called earlier, niSwitch
        Initiate Scan only initiates the scan and returns immediately. Once the
        scanning operation begins, you cannot perform any other operation other
        than GetAttribute, AbortScan, or SendSoftwareTrigger. All other
        methods return NISWITCH_ERROR_SCAN_IN_PROGRESS. To stop the
        scanning operation, To stop the scanning operation, call
        abort.
        '''
        self._interpreter.initiate_scan()

    @ivi_synchronized
    def relay_control(self, relay_name, relay_action):
        r'''relay_control

        Controls individual relays of the switch. When controlling individual
        relays, the protection offered by setting the usage of source channels
        and configuration channels, and by enabling or disabling analog bus
        sharing on the NI SwitchBlock, does not apply. Refer to the device book
        for your switch in the NI Switches Help to determine if the switch
        supports individual relay control.

        Args:
            relay_name (str): Name of the relay. Default value: None Examples of valid relay names:
                ch0, ab0, 1wire, hlselect Refer to Devices Overview for a list of valid
                relay names for the switch module.

            relay_action (enums.RelayAction): Specifies whether to open or close a given relay. Default value: Relay
                Close Defined values: RelayAction.OPEN
                RelayAction.CLOSE (Default Value)

        '''
        if type(relay_action) is not enums.RelayAction:
            raise TypeError('Parameter relay_action must be of type ' + str(enums.RelayAction))
        self._interpreter.relay_control(relay_name, relay_action)

    @ivi_synchronized
    def reset_with_defaults(self):
        r'''reset_with_defaults

        Resets the switch module and applies initial user specified settings
        from the logical name used to initialize the session. If the session was
        created without a logical name, this method is equivalent to
        reset.
        '''
        self._interpreter.reset_with_defaults()

    @ivi_synchronized
    def route_scan_advanced_output(self, scan_advanced_output_connector, scan_advanced_output_bus_line, invert=False):
        r'''route_scan_advanced_output

        Routes the scan advanced output trigger from a trigger bus line (TTLx)
        to the front or rear connector.

        Args:
            scan_advanced_output_connector (enums.ScanAdvancedOutput): The scan advanced trigger destination. Valid locations are the
                ScanAdvancedOutput.FRONTCONNECTOR and ScanAdvancedOutput.REARCONNECTOR. Default
                value: ScanAdvancedOutput.FRONTCONNECTOR

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            scan_advanced_output_bus_line (enums.ScanAdvancedOutput): The trigger line to route the scan advanced output trigger from the
                front or rear connector. Select ScanAdvancedOutput.NONE to break an existing
                route. Default value: None Valid Values: ScanAdvancedOutput.NONE
                ScanAdvancedOutput.TTL0 ScanAdvancedOutput.TTL1 ScanAdvancedOutput.TTL2
                ScanAdvancedOutput.TTL3 ScanAdvancedOutput.TTL4 ScanAdvancedOutput.TTL5
                ScanAdvancedOutput.TTL6 ScanAdvancedOutput.TTL7

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            invert (bool): If True, inverts the input trigger signal from falling to rising or
                vice versa. Default value: False

        '''
        if type(scan_advanced_output_connector) is not enums.ScanAdvancedOutput:
            raise TypeError('Parameter scan_advanced_output_connector must be of type ' + str(enums.ScanAdvancedOutput))
        if type(scan_advanced_output_bus_line) is not enums.ScanAdvancedOutput:
            raise TypeError('Parameter scan_advanced_output_bus_line must be of type ' + str(enums.ScanAdvancedOutput))
        self._interpreter.route_scan_advanced_output(scan_advanced_output_connector, scan_advanced_output_bus_line, invert)

    @ivi_synchronized
    def route_trigger_input(self, trigger_input_connector, trigger_input_bus_line, invert=False):
        r'''route_trigger_input

        Routes the input trigger from the front or rear connector to a trigger
        bus line (TTLx). To disconnect the route, call this method again and
        specify None for trigger bus line parameter.

        Args:
            trigger_input_connector (enums.TriggerInput): The location of the input trigger source on the switch module. Valid
                locations are the TriggerInput.FRONTCONNECTOR and
                TriggerInput.REARCONNECTOR. Default value:
                TriggerInput.FRONTCONNECTOR

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            trigger_input_bus_line (enums.TriggerInput): The trigger line to route the input trigger. Select NISWITCH_VAL_NONE
                to break an existing route. Default value: None Valid Values:
                NISWITCH_VAL_NONE TriggerInput.TTL0 TriggerInput.TTL1
                TriggerInput.TTL2 TriggerInput.TTL3 TriggerInput.TTL4
                TriggerInput.TTL5 TriggerInput.TTL6 TriggerInput.TTL7

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            invert (bool): If True, inverts the input trigger signal from falling to rising or
                vice versa. Default value: False

        '''
        if type(trigger_input_connector) is not enums.TriggerInput:
            raise TypeError('Parameter trigger_input_connector must be of type ' + str(enums.TriggerInput))
        if type(trigger_input_bus_line) is not enums.TriggerInput:
            raise TypeError('Parameter trigger_input_bus_line must be of type ' + str(enums.TriggerInput))
        self._interpreter.route_trigger_input(trigger_input_connector, trigger_input_bus_line, invert)

    @ivi_synchronized
    def send_software_trigger(self):
        r'''send_software_trigger

        Sends a software trigger to the switch module specified in the NI-SWITCH
        session. When the trigger input is set to TriggerInput.SOFTWARE_TRIG
        through either the ConfigureScanTrigger or the
        trigger_input property, the scan does not proceed from
        a semi-colon (wait for trigger) until send_software_trigger is
        called.

        Note:
        One or more of the referenced methods are not in the Python API for this driver.
        '''
        self._interpreter.send_software_trigger()

    @ivi_synchronized
    def set_path(self, path_list):
        r'''set_path

        Connects two channels by specifying an explicit path in the path list
        parameter. set_path is particularly useful where path
        repeatability is important, such as in calibrated signal paths. If this
        is not necessary, use connect.

        Args:
            path_list (str): A string composed of comma-separated paths between channel 1 and channel
                2. The first and last names in the path are the endpoints of the path.
                Every other channel in the path are configuration channels. Example of a
                valid path list string: ch0->com0, com0->ab0. In this example, com0 is a
                configuration channel. Default value: None Obtain the path list for a
                previously created path with get_path.

        '''
        self._interpreter.set_path(path_list)

    @ivi_synchronized
    def wait_for_debounce(self, maximum_time_ms=hightime.timedelta(milliseconds=5000)):
        r'''wait_for_debounce

        Pauses until all created paths have settled. If the time you specify
        with the Maximum Time (ms) parameter elapsed before the switch paths
        have settled, this method returns the
        NISWITCH_ERROR_MAX_TIME_EXCEEDED error.

        Args:
            maximum_time_ms (hightime.timedelta, datetime.timedelta, or int in milliseconds): Specifies the maximum length of time to wait for all relays in the
                switch module to activate or deactivate. If the specified time elapses
                before all relays active or deactivate, a timeout error is returned.
                Default Value:5000 ms

        '''
        maximum_time_ms = _converters.convert_timedelta_to_milliseconds_int32(maximum_time_ms)
        self._interpreter.wait_for_debounce(maximum_time_ms)

    @ivi_synchronized
    def wait_for_scan_complete(self, maximum_time_ms=hightime.timedelta(milliseconds=5000)):
        r'''wait_for_scan_complete

        Pauses until the switch module stops scanning or the maximum time has
        elapsed and returns a timeout error. If the time you specify with the
        Maximum Time (ms) parameter elapsed before the scanning operation has
        finished, this method returns the NISWITCH_ERROR_MAX_TIME_EXCEEDED
        error.

        Args:
            maximum_time_ms (hightime.timedelta, datetime.timedelta, or int in milliseconds): Specifies the maximum length of time to wait for the switch module to
                stop scanning. If the specified time elapses before the scan ends,
                NISWITCH_ERROR_MAX_TIME_EXCEEDED error is returned. Default
                Value:5000 ms

        '''
        maximum_time_ms = _converters.convert_timedelta_to_milliseconds_int32(maximum_time_ms)
        self._interpreter.wait_for_scan_complete(maximum_time_ms)

    def _close(self):
        r'''_close

        Terminates the NI-SWITCH session and all of its properties and
        deallocates any memory resources the driver uses. Notes: (1) You must
        unlock the session before calling _close. (2) After calling
        _close, you cannot use the instrument driver again until you
        call init or InitWithOptions.

        Note:
        One or more of the referenced methods are not in the Python API for this driver.
        '''
        self._interpreter.close()

    @ivi_synchronized
    def self_test(self):
        '''self_test

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
        '''
        code, msg = self._self_test()
        if code:
            raise errors.SelfTestError(code, msg)
        return None

    @ivi_synchronized
    def reset(self):
        r'''reset

        Disconnects all created paths and returns the switch module to the state
        at initialization. Configuration channel and source channel settings
        remain unchanged.
        '''
        self._interpreter.reset()

    @ivi_synchronized
    def _self_test(self):
        r'''_self_test

        Verifies that the driver can communicate with the switch module.

        Returns:
            self_test_result (int): Value returned from the switch device self-test. Passed 0 Failed 1

            self_test_message (str): Self-test response string from the switch device. You must pass a ViChar
                array with at least 256 bytes.

        '''
        self_test_result, self_test_message = self._interpreter.self_test()
        return self_test_result, self_test_message
