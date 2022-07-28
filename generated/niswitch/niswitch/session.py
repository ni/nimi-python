# -*- coding: utf-8 -*-
# This file was generated
import array  # noqa: F401
import ctypes
# Used by @ivi_synchronized
from functools import wraps

import niswitch._attributes as _attributes
import niswitch._converters as _converters
import niswitch._library_singleton as _library_singleton
import niswitch._visatype as _visatype
import niswitch.enums as enums
import niswitch.errors as errors

import hightime

# Used for __repr__
import pprint
pp = pprint.PrettyPrinter(indent=4)


# Helper functions for creating ctypes needed for calling into the driver DLL
def get_ctypes_pointer_for_buffer(value=None, library_type=None, size=None):
    if isinstance(value, array.array):
        assert library_type is not None, 'library_type is required for array.array'
        addr, _ = value.buffer_info()
        return ctypes.cast(addr, ctypes.POINTER(library_type))
    elif str(type(value)).find("'numpy.ndarray'") != -1:
        import numpy
        return numpy.ctypeslib.as_ctypes(value)
    elif isinstance(value, bytes):
        return ctypes.cast(value, ctypes.POINTER(library_type))
    elif isinstance(value, list):
        assert library_type is not None, 'library_type is required for list'
        return (library_type * len(value))(*value)
    else:
        if library_type is not None and size is not None:
            return (library_type * size)()
        else:
            return None


def get_ctypes_and_array(value, array_type):
    if value is not None:
        if isinstance(value, array.array):
            value_array = value
        else:
            value_array = array.array(array_type, value)
    else:
        value_array = None

    return value_array


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
            vi=self._session._vi,
            repeated_capability_list=complete_rep_cap_list,
            all_channels_in_session=self._session._all_channels_in_session,
            library=self._session._library,
            encoding=self._session._encoding,
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

    def __init__(self, repeated_capability_list, all_channels_in_session, vi, library, encoding, freeze_it=False):
        self._repeated_capability_list = repeated_capability_list
        self._repeated_capability = ','.join(repeated_capability_list)
        self._all_channels_in_session = all_channels_in_session
        self._vi = vi
        self._library = library
        self._encoding = encoding

        # Store the parameter list for later printing in __repr__
        param_list = []
        param_list.append("repeated_capability_list=" + pp.pformat(repeated_capability_list))
        param_list.append("vi=" + pp.pformat(vi))
        param_list.append("library=" + pp.pformat(library))
        param_list.append("encoding=" + pp.pformat(encoding))
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

    def _get_error_description(self, error_code):
        '''_get_error_description

        Returns the error description.
        '''
        try:
            _, error_string = self._get_error()
            return error_string
        except errors.Error:
            pass

        try:
            '''
            It is expected for _get_error to raise when the session is invalid
            (IVI spec requires GetError to fail).
            Use _error_message instead. It doesn't require a session.
            '''
            error_string = self._error_message(error_code)
            return error_string
        except errors.Error:
            return "Failed to retrieve error description."

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niSwitch_GetAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(attribute_value_ctype.value)

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niSwitch_GetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(attribute_value_ctype.value)

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niSwitch_GetAttributeViReal64(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(attribute_value_ctype.value)

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        array_size_ctype = _visatype.ViInt32()  # case S170
        attribute_value_ctype = None  # case C050
        error_code = self._library.niSwitch_GetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, array_size_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        array_size_ctype = _visatype.ViInt32(error_code)  # case S180
        attribute_value_ctype = (_visatype.ViChar * array_size_ctype.value)()  # case C060
        error_code = self._library.niSwitch_GetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, array_size_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return attribute_value_ctype.value.decode(self._encoding)

    def _get_error(self):
        r'''_get_error

        This method retrieves and then clears the IVI error information for
        the session or the current execution thread. One exception exists: If
        the buffer_size parameter is 0, the method does not clear the error
        information. By passing 0 for the buffer size, the caller can ascertain
        the buffer size required to get the entire error description string and
        then call the method again with a sufficiently large buffer. If the
        user specifies a valid IVI session for the InstrumentHandle parameter,
        Get Error retrieves and then clears the error information for the
        session. If the user passes VI_NULL for the InstrumentHandle parameter,
        this method retrieves and then clears the error information for the
        current execution thread. If the InstrumentHandle parameter is an
        invalid session, the method does nothing and returns an error.
        Normally, the error information describes the first error that occurred
        since the user last called _get_error or ClearError.

        Note:
        One or more of the referenced methods are not in the Python API for this driver.

        Returns:
            code (int): Returns the error code for the session or execution thread. If you pass
                0 for the Buffer Size, you can pass VI_NULL for this parameter.

            description (str): Returns the error description for the IVI session or execution thread.
                If there is no description, the method returns an empty string. The
                buffer must contain at least as many elements as the value you specify
                with the Buffer Size parameter. If the error description, including the
                terminating NUL byte, contains more bytes than you indicate with the
                Buffer Size parameter, the method copies Buffer Size - 1 bytes into
                the buffer, places an ASCII NUL byte at the end of the buffer, and
                returns the buffer size you must pass to get the entire value. For
                example, if the value is "123456" and the Buffer Size is 4, the method
                places "123" into the buffer and returns 7. If you pass 0 for the Buffer
                Size, you can pass VI_NULL for this parameter.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        code_ctype = _visatype.ViStatus()  # case S220
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        description_ctype = None  # case C050
        error_code = self._library.niSwitch_GetError(vi_ctype, None if code_ctype is None else (ctypes.pointer(code_ctype)), buffer_size_ctype, description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=True)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        description_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.niSwitch_GetError(vi_ctype, None if code_ctype is None else (ctypes.pointer(code_ctype)), buffer_size_ctype, description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return int(code_ctype.value), description_ctype.value.decode(self._encoding)

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
        self._lock_session()  # We do not call _lock_session() in the context manager so that this function can
        # act standalone as well and let the client call unlock() explicitly. If they do use the context manager,
        # that will handle the unlock for them
        return _Lock(self)

    def _lock_session(self):
        '''_lock_session

        Actual call to driver
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niSwitch_LockSession(vi_ctype, None)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViBoolean(attribute_value)  # case S150
        error_code = self._library.niSwitch_SetAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt32(attribute_value)  # case S150
        error_code = self._library.niSwitch_SetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViReal64(attribute_value)  # case S150
        error_code = self._library.niSwitch_SetAttributeViReal64(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = ctypes.create_string_buffer(attribute_value.encode(self._encoding))  # case C020
        error_code = self._library.niSwitch_SetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def unlock(self):
        '''unlock

        Releases a lock that you acquired on an device session using
        lock. Refer to lock for additional
        information on session locks.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niSwitch_UnlockSession(vi_ctype, None)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code_ctype = _visatype.ViStatus(error_code)  # case S150
        error_message_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library.niSwitch_error_message(vi_ctype, error_code_ctype, error_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return error_message_ctype.value.decode(self._encoding)


class Session(_SessionBase):
    '''An NI-SWITCH session to an NI switch module.'''

    def __init__(self, resource_name, topology="Configured Topology", simulate=False, reset_device=False):
        r'''An NI-SWITCH session to an NI switch module.

        Returns a session handle used to identify the switch in all subsequent
        instrument driver calls and sets the topology of the switch.
        __init__ creates a new IVI instrument driver session
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

            simulate (bool): Enables simulation of the switch module specified in the resource name
                parameter. Valid Values: True - simulate False - Don't simulate
                (Default Value)

            reset_device (bool): Specifies whether to reset the switch module during the initialization
                process. Valid Values: True - Reset Device (Default Value) False
                - Currently unsupported. The device will not reset.


        Returns:
            session (niswitch.Session): A session object representing the device.

        '''
        # Initialize the superclass with default values first, populate them later
        super(Session, self).__init__(
            repeated_capability_list=[],
            vi=None,
            library=None,
            encoding=None,
            freeze_it=False,
            all_channels_in_session=None
        )
        self._library = _library_singleton.get()
        self._encoding = 'windows-1251'

        # Call specified init function
        self._vi = 0  # This must be set before calling _init_with_topology().
        self._vi = self._init_with_topology(resource_name, topology, simulate, reset_device)

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
        # handle `self._vi` is set
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
            self._vi = 0
            raise
        self._vi = 0

    ''' These are code-generated '''

    @ivi_synchronized
    def abort(self):
        r'''abort

        Aborts the scan in progress. Initiate a scan with
        initiate. If the switch module is not scanning,
        NISWITCH_ERROR_NO_SCAN_IN_PROGRESS error is returned.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niSwitch_AbortScan(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel1_ctype = ctypes.create_string_buffer(channel1.encode(self._encoding))  # case C020
        channel2_ctype = ctypes.create_string_buffer(channel2.encode(self._encoding))  # case C020
        path_capability_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niSwitch_CanConnect(vi_ctype, channel1_ctype, channel2_ctype, None if path_capability_ctype is None else (ctypes.pointer(path_capability_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return enums.PathCapability(path_capability_ctype.value)

    @ivi_synchronized
    def commit(self):
        r'''commit

        Downloads the configured scan list and trigger settings to hardware.
        Calling commit optional as it is implicitly called during
        initiate. Use commit to arm triggers in a given
        order or to control when expensive hardware operations are performed.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niSwitch_Commit(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel1_ctype = ctypes.create_string_buffer(channel1.encode(self._encoding))  # case C020
        channel2_ctype = ctypes.create_string_buffer(channel2.encode(self._encoding))  # case C020
        error_code = self._library.niSwitch_Connect(vi_ctype, channel1_ctype, channel2_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        connection_list_ctype = ctypes.create_string_buffer(connection_list.encode(self._encoding))  # case C020
        error_code = self._library.niSwitch_ConnectMultiple(vi_ctype, connection_list_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def disable(self):
        r'''disable

        Places the switch module in a quiescent state where it has minimal or no
        impact on the system to which it is connected. All channels are
        disconnected and any scan in progress is aborted.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niSwitch_Disable(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel1_ctype = ctypes.create_string_buffer(channel1.encode(self._encoding))  # case C020
        channel2_ctype = ctypes.create_string_buffer(channel2.encode(self._encoding))  # case C020
        error_code = self._library.niSwitch_Disconnect(vi_ctype, channel1_ctype, channel2_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def disconnect_all(self):
        r'''disconnect_all

        Breaks all existing paths. If the switch module cannot break all paths,
        NISWITCH_WARN_PATH_REMAINS warning is returned.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niSwitch_DisconnectAll(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        disconnection_list_ctype = ctypes.create_string_buffer(disconnection_list.encode(self._encoding))  # case C020
        error_code = self._library.niSwitch_DisconnectMultiple(vi_ctype, disconnection_list_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        index_ctype = _visatype.ViInt32(index)  # case S150
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        channel_name_buffer_ctype = None  # case C050
        error_code = self._library.niSwitch_GetChannelName(vi_ctype, index_ctype, buffer_size_ctype, channel_name_buffer_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        channel_name_buffer_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.niSwitch_GetChannelName(vi_ctype, index_ctype, buffer_size_ctype, channel_name_buffer_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return channel_name_buffer_ctype.value.decode(self._encoding)

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel1_ctype = ctypes.create_string_buffer(channel1.encode(self._encoding))  # case C020
        channel2_ctype = ctypes.create_string_buffer(channel2.encode(self._encoding))  # case C020
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        path_ctype = None  # case C050
        error_code = self._library.niSwitch_GetPath(vi_ctype, channel1_ctype, channel2_ctype, buffer_size_ctype, path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        path_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.niSwitch_GetPath(vi_ctype, channel1_ctype, channel2_ctype, buffer_size_ctype, path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return path_ctype.value.decode(self._encoding)

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        relay_name_ctype = ctypes.create_string_buffer(relay_name.encode(self._encoding))  # case C020
        relay_count_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niSwitch_GetRelayCount(vi_ctype, relay_name_ctype, None if relay_count_ctype is None else (ctypes.pointer(relay_count_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(relay_count_ctype.value)

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        index_ctype = _visatype.ViInt32(index)  # case S150
        relay_name_buffer_size_ctype = _visatype.ViInt32()  # case S170
        relay_name_buffer_ctype = None  # case C050
        error_code = self._library.niSwitch_GetRelayName(vi_ctype, index_ctype, relay_name_buffer_size_ctype, relay_name_buffer_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        relay_name_buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        relay_name_buffer_ctype = (_visatype.ViChar * relay_name_buffer_size_ctype.value)()  # case C060
        error_code = self._library.niSwitch_GetRelayName(vi_ctype, index_ctype, relay_name_buffer_size_ctype, relay_name_buffer_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return relay_name_buffer_ctype.value.decode(self._encoding)

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        relay_name_ctype = ctypes.create_string_buffer(relay_name.encode(self._encoding))  # case C020
        relay_position_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niSwitch_GetRelayPosition(vi_ctype, relay_name_ctype, None if relay_position_ctype is None else (ctypes.pointer(relay_position_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return enums.RelayPosition(relay_position_ctype.value)

    def _init_with_topology(self, resource_name, topology="Configured Topology", simulate=False, reset_device=False):
        r'''_init_with_topology

        Returns a session handle used to identify the switch in all subsequent
        instrument driver calls and sets the topology of the switch.
        __init__ creates a new IVI instrument driver session
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
        resource_name_ctype = ctypes.create_string_buffer(resource_name.encode(self._encoding))  # case C020
        topology_ctype = ctypes.create_string_buffer(topology.encode(self._encoding))  # case C020
        simulate_ctype = _visatype.ViBoolean(simulate)  # case S150
        reset_device_ctype = _visatype.ViBoolean(reset_device)  # case S150
        vi_ctype = _visatype.ViSession()  # case S220
        error_code = self._library.niSwitch_InitWithTopology(resource_name_ctype, topology_ctype, simulate_ctype, reset_device_ctype, None if vi_ctype is None else (ctypes.pointer(vi_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(vi_ctype.value)

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niSwitch_InitiateScan(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        relay_name_ctype = ctypes.create_string_buffer(relay_name.encode(self._encoding))  # case C020
        relay_action_ctype = _visatype.ViInt32(relay_action.value)  # case S130
        error_code = self._library.niSwitch_RelayControl(vi_ctype, relay_name_ctype, relay_action_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def reset_with_defaults(self):
        r'''reset_with_defaults

        Resets the switch module and applies initial user specified settings
        from the logical name used to initialize the session. If the session was
        created without a logical name, this method is equivalent to
        reset.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niSwitch_ResetWithDefaults(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        scan_advanced_output_connector_ctype = _visatype.ViInt32(scan_advanced_output_connector.value)  # case S130
        scan_advanced_output_bus_line_ctype = _visatype.ViInt32(scan_advanced_output_bus_line.value)  # case S130
        invert_ctype = _visatype.ViBoolean(invert)  # case S150
        error_code = self._library.niSwitch_RouteScanAdvancedOutput(vi_ctype, scan_advanced_output_connector_ctype, scan_advanced_output_bus_line_ctype, invert_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        trigger_input_connector_ctype = _visatype.ViInt32(trigger_input_connector.value)  # case S130
        trigger_input_bus_line_ctype = _visatype.ViInt32(trigger_input_bus_line.value)  # case S130
        invert_ctype = _visatype.ViBoolean(invert)  # case S150
        error_code = self._library.niSwitch_RouteTriggerInput(vi_ctype, trigger_input_connector_ctype, trigger_input_bus_line_ctype, invert_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niSwitch_SendSoftwareTrigger(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        path_list_ctype = ctypes.create_string_buffer(path_list.encode(self._encoding))  # case C020
        error_code = self._library.niSwitch_SetPath(vi_ctype, path_list_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        maximum_time_ms_ctype = _converters.convert_timedelta_to_milliseconds_int32(maximum_time_ms)  # case S140
        error_code = self._library.niSwitch_WaitForDebounce(vi_ctype, maximum_time_ms_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        maximum_time_ms_ctype = _converters.convert_timedelta_to_milliseconds_int32(maximum_time_ms)  # case S140
        error_code = self._library.niSwitch_WaitForScanComplete(vi_ctype, maximum_time_ms_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niSwitch_close(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niSwitch_reset(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def _self_test(self):
        r'''_self_test

        Verifies that the driver can communicate with the switch module.

        Returns:
            self_test_result (int): Value returned from the switch device self-test. Passed 0 Failed 1

            self_test_message (str): Self-test response string from the switch device. You must pass a ViChar
                array with at least 256 bytes.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        self_test_result_ctype = _visatype.ViInt16()  # case S220
        self_test_message_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library.niSwitch_self_test(vi_ctype, None if self_test_result_ctype is None else (ctypes.pointer(self_test_result_ctype)), self_test_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(self_test_result_ctype.value), self_test_message_ctype.value.decode(self._encoding)



