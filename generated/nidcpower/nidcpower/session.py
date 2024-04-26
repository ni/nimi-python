# -*- coding: utf-8 -*-
# This file was generated
import array  # noqa: F401
# Used by @ivi_synchronized
from functools import wraps

import nidcpower._attributes as _attributes
import nidcpower._converters as _converters
import nidcpower._library_interpreter as _library_interpreter
import nidcpower.enums as enums
import nidcpower.errors as errors

import nidcpower.lcr_measurement as lcr_measurement  # noqa: F401

import nidcpower.lcr_load_compensation_spot as lcr_load_compensation_spot  # noqa: F401

import hightime

# Used for __repr__
import pprint
pp = pprint.PrettyPrinter(indent=4)


class _Acquisition(object):
    def __init__(self, session):
        self._session = session
        self._session._initiate_with_channels()

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
    '''Base class for all NI-DCPower sessions.'''

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

    active_advanced_sequence = _attributes.AttributeViString(1150074)
    '''Type: str

    Specifies the advanced sequence to configure or generate.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].active_advanced_sequence`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.active_advanced_sequence`
    '''
    active_advanced_sequence_step = _attributes.AttributeViInt64(1150075)
    '''Type: int

    Specifies the advanced sequence step to configure.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].active_advanced_sequence_step`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.active_advanced_sequence_step`
    '''
    actual_power_allocation = _attributes.AttributeViReal64(1150205)
    '''Type: float

    Returns the power, in watts, the device is sourcing on each active channel if the power_allocation_mode property is set to PowerAllocationMode.AUTOMATIC or PowerAllocationMode.MANUAL.

     Valid Values: [0, device per-channel maximum power]

     Default Value: Refer to the Supported Properties by Device topic for the default value by device.

    Note:
    NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

     This property returns -1 when the power_allocation_mode property is set to PowerAllocationMode.DISABLED.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].actual_power_allocation`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.actual_power_allocation`
    '''
    aperture_time = _attributes.AttributeViReal64(1150058)
    '''Type: float

    Specifies the measurement aperture time for the channel configuration. Aperture time is specified in the units set by the aperture_time_units property.
    Refer to the Aperture Time topic in the NI DC Power Supplies and SMUs Help for more information about how to configure your measurements and for information about valid values.
    Default Value: 0.01666666 seconds

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].aperture_time`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.aperture_time`
    '''
    aperture_time_auto_mode = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.ApertureTimeAutoMode, 1150314)
    '''Type: enums.ApertureTimeAutoMode

    Automatically optimizes the measurement aperture time according to the actual current range when measurement autorange is enabled.
    Optimization accounts for power line frequency when the aperture_time_units property is set to ApertureTimeUnits.POWER_LINE_CYCLES.

    This property is applicable only if the output_function property is set to OutputFunction.DC_VOLTAGE and the autorange property is enabled.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].aperture_time_auto_mode`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.aperture_time_auto_mode`
    '''
    aperture_time_units = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.ApertureTimeUnits, 1150059)
    '''Type: enums.ApertureTimeUnits

    Specifies the units of the aperture_time property for the channel configuration.
    Refer to the Aperture Time topic in the NI DC Power Supplies and SMUs Help for more information about how to configure your measurements and for information about valid values.
    Default Value: ApertureTimeUnits.SECONDS

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].aperture_time_units`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.aperture_time_units`
    '''
    autorange = _attributes.AttributeViInt32(1150244)
    '''Type: bool

    Specifies whether the hardware automatically selects the best range to measure the signal. Note the highest range the algorithm uses is dependent on the corresponding limit range property. The algorithm the hardware uses can be controlled using the autorange_aperture_time_mode property.

    Note:
    Autoranging begins at module startup and remains active until the module is reconfigured or reset. This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].autorange`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.autorange`
    '''
    autorange_aperture_time_mode = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.AutorangeApertureTimeMode, 1150246)
    '''Type: enums.AutorangeApertureTimeMode

    Specifies whether the aperture time used for the measurement autorange algorithm is determined automatically or customized using the autorange_minimum_aperture_time property.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].autorange_aperture_time_mode`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.autorange_aperture_time_mode`
    '''
    autorange_behavior = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.AutorangeBehavior, 1150245)
    '''Type: enums.AutorangeBehavior

    Specifies the algorithm the hardware uses for measurement autoranging.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].autorange_behavior`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.autorange_behavior`
    '''
    autorange_maximum_delay_after_range_change = _attributes.AttributeViReal64TimeDeltaSeconds(1150322)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    Balances between settling time and maximum measurement time by specifying the maximum time delay between when a range change occurs and when measurements resume.
    **Valid Values:** The minimum and maximum values of this property are hardware-dependent.
    PXIe-4135/4136/4137: 0 to 9 seconds
    PXIe-4138/4139: 0 to 9 seconds
    PXIe-4147: 0 to 9 seconds
    PXIe-4162/4163: 0 to 0.1 seconds.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].autorange_maximum_delay_after_range_change`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.autorange_maximum_delay_after_range_change`
    '''
    autorange_minimum_aperture_time = _attributes.AttributeViReal64(1150247)
    '''Type: float

    Specifies the measurement autorange aperture time used for the measurement autorange algorithm. The aperture time is specified in the units set by the autorange_minimum_aperture_time_units property. This value will typically be smaller than the aperture time used for measurements.

    Note: For smaller ranges, the value is scaled up to account for noise. The factor used to scale the value is derived from the module capabilities. This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].autorange_minimum_aperture_time`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.autorange_minimum_aperture_time`
    '''
    autorange_minimum_aperture_time_units = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.ApertureTimeUnits, 1150248)
    '''Type: enums.ApertureTimeUnits

    Specifies the units of the autorange_minimum_aperture_time property.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].autorange_minimum_aperture_time_units`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.autorange_minimum_aperture_time_units`
    '''
    autorange_minimum_current_range = _attributes.AttributeViReal64(1150255)
    '''Type: float

    Specifies the lowest range used during measurement autoranging. Limiting the lowest range used during autoranging can improve the speed of the autoranging algorithm and minimize frequent and unpredictable range changes for noisy signals.

    Note: The maximum range used is the range that includes the value specified in the compliance limit property, voltage_limit_range property or current_limit_range property, depending on the selected output_function. This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].autorange_minimum_current_range`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.autorange_minimum_current_range`
    '''
    autorange_minimum_voltage_range = _attributes.AttributeViReal64(1150256)
    '''Type: float

    Specifies the lowest range used during measurement autoranging. The maximum range used is range that includes the value specified in the compliance limit property. Limiting the lowest range used during autoranging can improve the speed of the autoranging algorithm and/or minimize thrashing between ranges for noisy signals.

    Note: The maximum range used is the range that includes the value specified in the compliance limit property, voltage_limit_range property or current_limit_range property, depending on the selected output_function. This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].autorange_minimum_voltage_range`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.autorange_minimum_voltage_range`
    '''
    autorange_threshold_mode = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.AutorangeThresholdMode, 1150257)
    '''Type: enums.AutorangeThresholdMode

    Specifies thresholds used during autoranging to determine when range changing occurs.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].autorange_threshold_mode`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.autorange_threshold_mode`
    '''
    auto_zero = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.AutoZero, 1150055)
    '''Type: enums.AutoZero

    Specifies the auto-zero method to use on the device.
    Refer to the NI PXI-4132 Measurement Configuration and Timing and Auto Zero topics for more information about how to configure your measurements.
    Default Value: The default value for the NI PXI-4132 is AutoZero.ON. The default value for all other devices is AutoZero.OFF, which is the only supported value for these devices.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].auto_zero`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.auto_zero`
    '''
    auxiliary_power_source_available = _attributes.AttributeViBoolean(1150002)
    '''Type: bool

    Indicates whether an auxiliary power source is connected to the device.
    A value of False may indicate that the auxiliary input fuse has blown. Refer to the Detecting Internal/Auxiliary Power topic in the NI DC Power Supplies and SMUs Help for more information about internal and auxiliary power.
    power source to generate power. Use the power_source_in_use property to retrieve this information.

    Note: This property does not necessarily indicate if the device is using the auxiliary
    '''
    cable_length = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.CableLength, 1150278)
    '''Type: enums.CableLength

    Specifies how to apply cable compensation data for instruments that support LCR functionality.
    Supported instruments use cable compensation for the following operations:

    SMU mode: to stabilize DC current sourcing in the two smallest current ranges.
    LCR mode: to compensate for the effects of cabling on LCR measurements.

    For NI standard options, select the length of your NI cable to apply compensation data for a typical cable of that type.
    For custom options, choose the source of the custom cable compensation data. You must then generate the custom cable compensation data.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].cable_length`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.cable_length`
    '''
    channel_count = _attributes.AttributeViInt32(1050203)
    '''Type: int

    Indicates the number of channels that NI-DCPower supports for the instrument that was chosen when the current session was opened. For channel-based properties, the IVI engine maintains a separate cache value for each channel.
    '''
    compliance_limit_symmetry = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.ComplianceLimitSymmetry, 1150184)
    '''Type: enums.ComplianceLimitSymmetry

    Specifies whether compliance limits for current generation and voltage
    generation for the device are applied symmetrically about 0 V and 0 A or
    asymmetrically with respect to 0 V and 0 A.
    When set to ComplianceLimitSymmetry.SYMMETRIC, voltage limits and current limits are set
    using a single property with a positive value. The resulting range is
    bounded by this positive value and its opposite.
    When set to ComplianceLimitSymmetry.ASYMMETRIC, you must separately set a limit high and a
    limit low using distinct properties.
    For asymmetric limits, the range bounded by the limit high and limit low
    must include zero.
    **Default Value:** Symmetric
    **Related Topics:**
    Compliance;
    Ranges;
    Changing Ranges;
    Overranging

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].compliance_limit_symmetry`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.compliance_limit_symmetry`
    '''
    conduction_voltage_mode = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.ConductionVoltageMode, 1150350)
    '''Type: enums.ConductionVoltageMode

    Specifies whether the conduction voltage feature is enabled on the specified channel(s).

    When the conduction voltage feature is enabled,
     - The instrument will not begin sinking on the specified channel(s) until the voltage at the input of the specified channel(s) rises above conduction_voltage_on_threshold
     - The instrument will stop sinking if the voltage at the input of the specified channel(s) falls below conduction_voltage_off_threshold.

    When the conduction voltage feature is disabled,
     - The instrument will start sinking regardless of the voltage at the input of the specified channel(s).

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].conduction_voltage_mode`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.conduction_voltage_mode`
    '''
    conduction_voltage_off_threshold = _attributes.AttributeViReal64(1150352)
    '''Type: float

    Specifies the minimum voltage, in volts, at the input of the specified channel(s) below which the instrument stops sinking on the specified channel(s) when the conduction voltage feature is enabled.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].conduction_voltage_off_threshold`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.conduction_voltage_off_threshold`
    '''
    conduction_voltage_on_threshold = _attributes.AttributeViReal64(1150351)
    '''Type: float

    Specifies the required minimum voltage, in volts, at the input of the specified channel(s) before the instrument starts sinking on the specified channel(s) when the conduction voltage feature is enabled.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].conduction_voltage_on_threshold`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.conduction_voltage_on_threshold`
    '''
    current_compensation_frequency = _attributes.AttributeViReal64(1150071)
    '''Type: float

    The frequency at which a pole-zero pair is added to the system when the channel is in Constant Current mode.
    Default Value: Determined by the value of the TransientResponse.NORMAL setting of the transient_response property.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].current_compensation_frequency`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.current_compensation_frequency`
    '''
    current_gain_bandwidth = _attributes.AttributeViReal64(1150070)
    '''Type: float

    The frequency at which the unloaded loop gain extrapolates to 0 dB in the absence of additional poles and zeroes. This property takes effect when the channel is in Constant Current mode.
    Default Value: Determined by the value of the TransientResponse.NORMAL setting of the transient_response property.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].current_gain_bandwidth`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.current_gain_bandwidth`
    '''
    current_level = _attributes.AttributeViReal64(1150009)
    '''Type: float

    Specifies the current level, in amps, that the device attempts to generate on the specified channel(s).
    This property is applicable only if the output_function property is set to OutputFunction.DC_CURRENT.

    Valid Values: The valid values for this property are defined by the values to which the current_level_range property is set.

    Note: The channel must be enabled for the specified current level to take effect. Refer to the output_enabled property for more information about enabling the channel.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].current_level`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.current_level`
    '''
    current_level_autorange = _attributes.AttributeViInt32(1150017)
    '''Type: bool

    Specifies whether NI-DCPower automatically selects the current level range based on the desired current level for the specified channels.
    If you set this property to AutoZero.ON, NI-DCPower ignores any changes you make to the current_level_range property. If you change the current_level_autorange property from AutoZero.ON to AutoZero.OFF, NI-DCPower retains the last value the current_level_range property was set to (or the default value if the property was never set) and uses that value as the current level range.
    Query the current_level_range property by using the _get_attribute_vi_int32 method for information about which range NI-DCPower automatically selects.
    The current_level_autorange property is applicable only if the output_function property is set to OutputFunction.DC_CURRENT.
    Default Value: AutoZero.OFF

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].current_level_autorange`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.current_level_autorange`
    '''
    current_level_falling_slew_rate = _attributes.AttributeViReal64(1150344)
    '''Type: float

    Specifies the rate of decrease, in amps per microsecond, to apply to the absolute magnitude of the current level of the specified channel(s).
    This property is applicable only if you set the output_function property to OutputFunction.DC_CURRENT.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].current_level_falling_slew_rate`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.current_level_falling_slew_rate`
    '''
    current_level_range = _attributes.AttributeViReal64(1150011)
    '''Type: float

    Specifies the current level range, in amps, for the specified channel(s).
    The range defines the valid values to which you can set the current level. Use the current_level_autorange property to enable automatic selection of the current level range.
    The current_level_range property is applicable only if the output_function property is set to OutputFunction.DC_CURRENT.

    For valid ranges, refer to the specifications for your instrument.

    Note: The channel must be enabled for the specified current level range to take effect. Refer to the output_enabled property for more information about enabling the channel.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].current_level_range`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.current_level_range`
    '''
    current_level_rising_slew_rate = _attributes.AttributeViReal64(1150343)
    '''Type: float

    Specifies the rate of increase, in amps per microsecond, to apply to the absolute magnitude of the current level of the specified channel(s).
    This property is applicable only if you set the output_function property to OutputFunction.DC_CURRENT.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].current_level_rising_slew_rate`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.current_level_rising_slew_rate`
    '''
    current_limit = _attributes.AttributeViReal64(1250005)
    '''Type: float

    Specifies the current limit, in amps, that the output cannot exceed when generating the desired voltage level on the specified channel(s).
    This property is applicable only if the output_function property is set to OutputFunction.DC_VOLTAGE and the compliance_limit_symmetry property is set to ComplianceLimitSymmetry.SYMMETRIC.

    Valid Values: The valid values for this property are defined by the values to which current_limit_range property is set.

    Note:
    The channel must be enabled for the specified current limit to take effect. Refer to the output_enabled property for more information about enabling the channel.

    NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].current_limit`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.current_limit`
    '''
    current_limit_autorange = _attributes.AttributeViInt32(1150016)
    '''Type: bool

    Specifies whether NI-DCPower automatically selects the current limit range based on the desired current limit for the specified channel(s).
    If you set this property to AutoZero.ON, NI-DCPower ignores any changes you make to the current_limit_range property. If you change this property from AutoZero.ON to AutoZero.OFF, NI-DCPower retains the last value the current_limit_range property was set to (or the default value if the property was never set) and uses that value as the current limit range.
    Query the current_limit_range property by using the _get_attribute_vi_int32 method for information about which range NI-DCPower automatically selects.
    The current_limit_autorange property is applicable only if the output_function property is set to OutputFunction.DC_VOLTAGE.
    Default Value: AutoZero.OFF

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].current_limit_autorange`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.current_limit_autorange`
    '''
    current_limit_behavior = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.CurrentLimitBehavior, 1250004)
    '''Type: enums.CurrentLimitBehavior

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].current_limit_behavior`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.current_limit_behavior`
    '''
    current_limit_high = _attributes.AttributeViReal64(1150187)
    '''Type: float

    Specifies the maximum current, in amps, that the output can produce when
    generating the desired voltage on the specified channel(s).
    This property is applicable only if the compliance_limit_symmetry property is set to
    ComplianceLimitSymmetry.ASYMMETRIC and the output_function property is set to OutputFunction.DC_VOLTAGE.
    You must also specify a current_limit_low to complete the asymmetric
    range.
    **Valid Values:** [1% of current_limit_range, current_limit_range]
    The range bounded by the limit high and limit low must include zero.
    **Default Value:** Search ni.com for Supported Properties by Device for the default value by device.
    **Related Topics:**
    Ranges;
    Changing Ranges;
    Overranging

    Note:
    The limit may be extended beyond the selected limit range if the
    overranging_enabled property is
    set to True.

    NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].current_limit_high`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.current_limit_high`
    '''
    current_limit_low = _attributes.AttributeViReal64(1150188)
    '''Type: float

    Specifies the minimum current, in amps, that the output can produce when
    generating the desired voltage on the specified channel(s).
    This property is applicable only if the compliance_limit_symmetry property is set to
    ComplianceLimitSymmetry.ASYMMETRIC and the output_function property is set to OutputFunction.DC_VOLTAGE.
    You must also specify a current_limit_high to complete the asymmetric
    range.
    **Valid Values:** [-current_limit_range, -1% of current_limit_range]
    The range bounded by the limit high and limit low must include zero.
    **Default Value:** Search ni.com for Supported Properties by Device for the default value by device.
    **Related Topics:**
    Ranges;
    Changing Ranges;
    Overranging

    Note:
    The limit may be extended beyond the selected limit range if the
    overranging_enabled property is
    set to True.

    NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].current_limit_low`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.current_limit_low`
    '''
    current_limit_range = _attributes.AttributeViReal64(1150004)
    '''Type: float

    Specifies the current limit range, in amps, for the specified channel(s).
    The range defines the valid values to which you can set the current limit. Use the current_limit_autorange property to enable automatic selection of the current limit range.
    The current_limit_range property is applicable only if the output_function property is set to OutputFunction.DC_VOLTAGE.

    For valid ranges, refer to the specifications for your instrument.

    Note: The channel must be enabled for the specified current limit to take effect. Refer to the output_enabled property for more information about enabling the channel.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].current_limit_range`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.current_limit_range`
    '''
    current_pole_zero_ratio = _attributes.AttributeViReal64(1150072)
    '''Type: float

    The ratio of the pole frequency to the zero frequency when the channel is in Constant Current mode.
    Default Value: Determined by the value of the TransientResponse.NORMAL setting of the transient_response property.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].current_pole_zero_ratio`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.current_pole_zero_ratio`
    '''
    dc_noise_rejection = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.DCNoiseRejection, 1150066)
    '''Type: enums.DCNoiseRejection

    Determines the relative weighting of samples in a measurement. Refer to the NI PXIe-4140/4141 DC Noise Rejection, NI PXIe-4142/4143 DC Noise Rejection, or NI PXIe-4144/4145 DC Noise Rejection topic in the NI DC Power Supplies and SMUs Help for more information about noise rejection.
    Default Value: TransientResponse.NORMAL

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].dc_noise_rejection`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.dc_noise_rejection`
    '''
    digital_edge_measure_trigger_input_terminal = _attributes.AttributeViString(1150036)
    '''Type: str

    Specifies the input terminal for the Measure trigger. This property is used only when the measure_trigger_type property is set to TriggerType.DIGITAL_EDGE.
    for this property.
    You can specify any valid input terminal for this property. Valid terminals are listed in Measurement & Automation Explorer under the Device Routes tab.
    Input terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0. The input terminal can also be a terminal from another device. For example, you can set the input terminal on Dev1 to be /Dev2/SourceCompleteEvent.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].digital_edge_measure_trigger_input_terminal`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.digital_edge_measure_trigger_input_terminal`
    '''
    digital_edge_pulse_trigger_input_terminal = _attributes.AttributeViString(1150097)
    '''Type: str

    Specifies the input terminal for the Pulse trigger. This property is used only when the pulse_trigger_type property is set to digital edge.
    You can specify any valid input terminal for this property. Valid terminals are listed in Measurement & Automation Explorer under the Device Routes tab.
    Input terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0. The input terminal can also be a terminal from another device. For example, you can set the input terminal on Dev1 to be /Dev2/SourceCompleteEvent.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].digital_edge_pulse_trigger_input_terminal`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.digital_edge_pulse_trigger_input_terminal`
    '''
    digital_edge_sequence_advance_trigger_input_terminal = _attributes.AttributeViString(1150028)
    '''Type: str

    Specifies the input terminal for the Sequence Advance trigger. Use this property only when the sequence_advance_trigger_type property is set to TriggerType.DIGITAL_EDGE.
    the NI DC Power Supplies and SMUs Help for information about supported devices.
    You can specify any valid input terminal for this property. Valid terminals are listed in Measurement & Automation Explorer under the Device Routes tab.
    Input terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0. The input terminal can also be a terminal from another device. For example, you can set the input terminal on Dev1 to be /Dev2/SourceCompleteEvent.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].digital_edge_sequence_advance_trigger_input_terminal`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.digital_edge_sequence_advance_trigger_input_terminal`
    '''
    digital_edge_shutdown_trigger_input_terminal = _attributes.AttributeViString(1150277)
    '''Type: str

    Specifies the input terminal for the Shutdown trigger. This property is used only when the shutdown_trigger_type property is set to digital edge.
    You can specify any valid input terminal for this property. Valid terminals are listed in Measurement & Automation Explorer under the Device Routes tab.
    Input terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0. The input terminal can also be a terminal from another device. For example, you can set the input terminal on Dev1 to be /Dev2/SourceCompleteEvent.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].digital_edge_shutdown_trigger_input_terminal`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.digital_edge_shutdown_trigger_input_terminal`
    '''
    digital_edge_source_trigger_input_terminal = _attributes.AttributeViString(1150032)
    '''Type: str

    Specifies the input terminal for the Source trigger. Use this property only when the source_trigger_type property is set to TriggerType.DIGITAL_EDGE.
    You can specify any valid input terminal for this property. Valid terminals are listed in Measurement & Automation Explorer under the Device Routes tab.
    Input terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0. The input terminal can also be a terminal from another device. For example, you can set the input terminal on Dev1 to be /Dev2/SourceCompleteEvent.

    Note:
    NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].digital_edge_source_trigger_input_terminal`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.digital_edge_source_trigger_input_terminal`
    '''
    digital_edge_start_trigger_input_terminal = _attributes.AttributeViString(1150023)
    '''Type: str

    Specifies the input terminal for the Start trigger. Use this property only when the start_trigger_type property is set to TriggerType.DIGITAL_EDGE.
    You can specify any valid input terminal for this property. Valid terminals are listed in Measurement & Automation Explorer under the Device Routes tab.
    Input terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name,  PXI_Trig0. The input terminal can also be a terminal from another device. For example, you can set the input terminal on Dev1 to be /Dev2/SourceCompleteEvent.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].digital_edge_start_trigger_input_terminal`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.digital_edge_start_trigger_input_terminal`
    '''
    driver_setup = _attributes.AttributeViString(1050007)
    '''Type: str

    Indicates the Driver Setup string that you specified when initializing the driver.
    Some cases exist where you must specify the instrument driver options at initialization time. An example of this case is specifying a particular device model from among a family of devices that the driver supports. This property is useful when simulating a device. You can specify the driver-specific options through the DriverSetup keyword in the optionsString parameter in the __init__ method or through the IVI Configuration Utility.
    You can specify driver-specific options through the DriverSetup keyword in the optionsString parameter in the __init__ method. If you do not specify a Driver Setup string, this property returns an empty string.
    '''
    exported_measure_trigger_output_terminal = _attributes.AttributeViString(1150037)
    '''Type: str

    Specifies the output terminal for exporting the Measure trigger.
    Refer to the Device Routes tab in Measurement & Automation Explorer for a list of the terminals available on your device.
    Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].exported_measure_trigger_output_terminal`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.exported_measure_trigger_output_terminal`
    '''
    exported_pulse_trigger_output_terminal = _attributes.AttributeViString(1150098)
    '''Type: str

    Specifies the output terminal for exporting the Pulse trigger.
    Refer to the Device Routes tab in Measurement & Automation Explorer for a list of the terminals available on your device.
    Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].exported_pulse_trigger_output_terminal`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.exported_pulse_trigger_output_terminal`
    '''
    exported_sequence_advance_trigger_output_terminal = _attributes.AttributeViString(1150029)
    '''Type: str

    Specifies the output terminal for exporting the Sequence Advance trigger.
    Refer to the Device Routes tab in Measurement & Automation Explorer for a list of the terminals available on your device.
    Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].exported_sequence_advance_trigger_output_terminal`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.exported_sequence_advance_trigger_output_terminal`
    '''
    exported_source_trigger_output_terminal = _attributes.AttributeViString(1150033)
    '''Type: str

    Specifies the output terminal for exporting the Source trigger.
    Refer to the Device Routes tab in MAX for a list of the terminals available on your device.
    Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].exported_source_trigger_output_terminal`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.exported_source_trigger_output_terminal`
    '''
    exported_start_trigger_output_terminal = _attributes.AttributeViString(1150024)
    '''Type: str

    Specifies the output terminal for exporting the Start trigger.
    Refer to the Device Routes tab in Measurement & Automation Explorer (MAX) for a list of the terminals available on your device.
    Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name,  PXI_Trig0.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].exported_start_trigger_output_terminal`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.exported_start_trigger_output_terminal`
    '''
    fetch_backlog = _attributes.AttributeViInt32(1150056)
    '''Type: int

    Returns the number of measurements acquired that have not been fetched yet.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].fetch_backlog`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.fetch_backlog`
    '''
    instrument_firmware_revision = _attributes.AttributeViString(1050510)
    '''Type: str

    Contains the firmware revision information for the device you are currently using.

    Tip:
    This property can be set/get on specific instruments within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container instruments to specify a subset.

    Example: :py:attr:`my_session.instruments[ ... ].instrument_firmware_revision`

    To set/get on all instruments, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.instrument_firmware_revision`
    '''
    instrument_manufacturer = _attributes.AttributeViString(1050511)
    '''Type: str

    Contains the name of the manufacturer for the device you are currently using.

    Tip:
    This property can be set/get on specific instruments within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container instruments to specify a subset.

    Example: :py:attr:`my_session.instruments[ ... ].instrument_manufacturer`

    To set/get on all instruments, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.instrument_manufacturer`
    '''
    instrument_mode = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.InstrumentMode, 1150208)
    '''Type: enums.InstrumentMode

    Specifies the mode of operation for an instrument channel for instruments that support multiple modes.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].instrument_mode`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.instrument_mode`
    '''
    instrument_model = _attributes.AttributeViString(1050512)
    '''Type: str

    Contains the model number or name of the device that you are currently using.

    Tip:
    This property can be set/get on specific instruments within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container instruments to specify a subset.

    Example: :py:attr:`my_session.instruments[ ... ].instrument_model`

    To set/get on all instruments, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.instrument_model`
    '''
    interlock_input_open = _attributes.AttributeViBoolean(1150105)
    '''Type: bool

    Indicates whether the safety interlock circuit is open.
    Refer to the Safety Interlock topic in the NI DC Power Supplies and SMUs Help for more information about the safety interlock circuit.
    about supported devices.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific instruments within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container instruments to specify a subset.

    Example: :py:attr:`my_session.instruments[ ... ].interlock_input_open`

    To set/get on all instruments, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.interlock_input_open`
    '''
    io_resource_descriptor = _attributes.AttributeViString(1050304)
    '''Type: str

    Indicates the resource descriptor NI-DCPower uses to identify the physical device.
    If you initialize NI-DCPower with a logical name, this property contains the resource descriptor that corresponds to the entry in the IVI Configuration utility.
    If you initialize NI-DCPower with the resource descriptor, this property contains that value.
    '''
    isolation_state = _attributes.AttributeEnumWithConverter(_attributes.AttributeEnum(_attributes.AttributeViInt32, enums._IsolationState, 1150302), _converters.convert_from_isolation_state_enum, _converters.convert_to_isolation_state_enum)
    '''Type: bool

    Defines whether the channel is isolated.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].isolation_state`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.isolation_state`
    '''
    lcr_actual_load_reactance = _attributes.AttributeViReal64(1150271)
    '''Type: float

    Specifies the actual reactance, in ohms, of the load used for load LCR compensation.
    This property applies when lcr_open_short_load_compensation_data_source is set to LCROpenShortLoadCompensationDataSource.AS_DEFINED.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].lcr_actual_load_reactance`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.lcr_actual_load_reactance`
    '''
    lcr_actual_load_resistance = _attributes.AttributeViReal64(1150270)
    '''Type: float

    Specifies the actual resistance, in ohms, of the load used for load LCR compensation.
    This property applies when lcr_open_short_load_compensation_data_source is set to LCROpenShortLoadCompensationDataSource.AS_DEFINED.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].lcr_actual_load_resistance`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.lcr_actual_load_resistance`
    '''
    lcr_ac_dither_enabled = _attributes.AttributeViBoolean(1150348)
    '''Type: bool

    Specifies whether dithering is enabled during LCR measurements.
    Dithering adds out-of-band noise to improve measurements of small voltage and current signals.

    Note:
    Hardware is only warranted to meet its accuracy specs with dither enabled. You can disable dither if the added noise interferes with your device-under-test.

    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].lcr_ac_dither_enabled`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.lcr_ac_dither_enabled`
    '''
    lcr_ac_electrical_cable_length_delay = _attributes.AttributeViReal64(1150309)
    '''Type: float

    Specifies the one-way electrical length delay of the cable, in seconds.
    The default value depends on cable_length.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].lcr_ac_electrical_cable_length_delay`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.lcr_ac_electrical_cable_length_delay`
    '''
    lcr_automatic_level_control = _attributes.AttributeViInt32(1150290)
    '''Type: bool

    Specifies whether the channel actively attempts to maintain a constant test voltage or current across the DUT for LCR measurements.
    The use of voltage or current depends on the test signal you configure with the lcr_stimulus_function property.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].lcr_automatic_level_control`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.lcr_automatic_level_control`
    '''
    lcr_current_amplitude = _attributes.AttributeViReal64(1150212)
    '''Type: float

    Specifies the amplitude, in amps RMS, of the AC current test signal applied to the DUT for LCR measurements.
    This property applies when the lcr_stimulus_function property is set to LCRStimulusFunction.CURRENT.

    Valid Values: 7.08e-9 A RMS to 0.707 A RMS

    Instrument specifications affect the valid values you can program. Refer to the specifications for your instrument for more information.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].lcr_current_amplitude`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.lcr_current_amplitude`
    '''
    lcr_current_range = _attributes.AttributeViReal64(1150267)
    '''Type: float

    Specifies the current range, in amps RMS, for the specified channel(s).
    The range defines the valid values to which you can set the lcr_current_amplitude.
    For valid ranges, refer to the specifications for your instrument.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].lcr_current_range`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.lcr_current_range`
    '''
    lcr_custom_measurement_time = _attributes.AttributeViReal64TimeDeltaSeconds(1150258)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    Specifies the LCR measurement aperture time for a channel, in seconds,
    when the lcr_measurement_time property is set to LCRMeasurementTime.CUSTOM.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].lcr_custom_measurement_time`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.lcr_custom_measurement_time`
    '''
    lcr_dc_bias_automatic_level_control = _attributes.AttributeViInt32(1150291)
    '''Type: bool

    Specifies whether the channel actively maintains a constant DC bias voltage or current across the DUT for LCR measurements.
    To use this property, you must configure a DC bias by 1) selecting an lcr_dc_bias_source and 2) depending on the DC bias source you choose, setting either the lcr_dc_bias_voltage_level or lcr_dc_bias_current_level.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].lcr_dc_bias_automatic_level_control`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.lcr_dc_bias_automatic_level_control`
    '''
    lcr_dc_bias_current_level = _attributes.AttributeViReal64(1150215)
    '''Type: float

    Specifies the DC bias current level, in amps, when the lcr_dc_bias_source property is set to LCRDCBiasSource.CURRENT.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].lcr_dc_bias_current_level`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.lcr_dc_bias_current_level`
    '''
    lcr_dc_bias_current_range = _attributes.AttributeViReal64(1150274)
    '''Type: float

    Specifies the DC Bias current range, in amps, for the specified channel(s).
    The range defines the valid values to which you can set the lcr_dc_bias_current_level.
    For valid ranges, refer to the specifications for your instrument.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].lcr_dc_bias_current_range`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.lcr_dc_bias_current_range`
    '''
    lcr_dc_bias_source = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.LCRDCBiasSource, 1150213)
    '''Type: enums.LCRDCBiasSource

    Specifies how to apply DC bias for LCR measurements.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].lcr_dc_bias_source`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.lcr_dc_bias_source`
    '''
    lcr_dc_bias_transient_response = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.LCRDCBiasTransientResponse, 1150347)
    '''Type: enums.LCRDCBiasTransientResponse

    For instruments in LCR mode, determines whether NI-DCPower automatically calculates and applies the transient response values for DC bias or applies the transient response you set manually.

    Default Value: Search ni.com for Supported Properties by Device for the default value by instrument.

    Related Topics: Transient Response

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].lcr_dc_bias_transient_response`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.lcr_dc_bias_transient_response`
    '''
    lcr_dc_bias_voltage_level = _attributes.AttributeViReal64(1150214)
    '''Type: float

    Specifies the DC bias voltage level, in volts, when the lcr_dc_bias_source property is set to LCRDCBiasSource.VOLTAGE.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].lcr_dc_bias_voltage_level`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.lcr_dc_bias_voltage_level`
    '''
    lcr_dc_bias_voltage_range = _attributes.AttributeViReal64(1150266)
    '''Type: float

    Specifies the DC Bias voltage range, in volts, for the specified channel(s).
    The range defines the valid values to which you can set the lcr_dc_bias_voltage_level.
    For valid ranges, refer to the specifications for your instrument.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].lcr_dc_bias_voltage_range`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.lcr_dc_bias_voltage_range`
    '''
    lcr_frequency = _attributes.AttributeViReal64(1150210)
    '''Type: float

    Specifies the frequency of the AC test signal applied to the DUT for LCR measurements.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].lcr_frequency`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.lcr_frequency`
    '''
    lcr_impedance_auto_range = _attributes.AttributeEnumWithConverter(_attributes.AttributeEnum(_attributes.AttributeViInt32, enums._LCRImpedanceAutoRange, 1150216), _converters.convert_from_lcr_impedance_auto_range_enum, _converters.convert_to_lcr_impedance_auto_range_enum)
    '''Type: bool

    Defines whether an instrument in LCR mode automatically selects the best impedance range for each given LCR measurement.

    Impedance autoranging may be enabled only when both:

    - The source_mode property is set to SourceMode.SINGLE_POINT
    - measure_when is set to a value other than MeasureWhen.ON_MEASURE_TRIGGER

    You can read lcr_impedance_range back after a measurement to determine the actual range used.

    When enabled, impedance autoranging overrides impedance range settings you configure manually with any other properties.

    When using a load with unknown impedance, you can set this property to _LCRImpedanceAutoRange.ON to determine the correct impedance range for the load. When you know the load impedance, you can achieve faster performance by setting this property to _LCRImpedanceAutoRange.OFF and setting lcr_impedance_range_source to LCRImpedanceRangeSource.LOAD_CONFIGURATION.

    Default Value: Search ni.com for Supported Properties by Device for the default value by instrument.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].lcr_impedance_auto_range`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.lcr_impedance_auto_range`
    '''
    lcr_impedance_range = _attributes.AttributeViReal64(1150217)
    '''Type: float

    Specifies the impedance range the channel uses for LCR measurements.

    Valid Values: 0 ohms to +inf ohms

    Default Value: Search ni.com for Supported Properties by Device for the default value by instrument.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].lcr_impedance_range`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.lcr_impedance_range`
    '''
    lcr_impedance_range_source = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.LCRImpedanceRangeSource, 1150321)
    '''Type: enums.LCRImpedanceRangeSource

    Specifies how the impedance range for LCR measurements is determined.

    "LCR_IMPEDANCE_AUTORANGE overrides any impedance range determined by this property.

    "

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Note:
    One or more of the referenced properties are not in the Python API for this driver.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].lcr_impedance_range_source`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.lcr_impedance_range_source`
    '''
    lcr_load_capacitance = _attributes.AttributeViReal64(1150320)
    '''Type: float

    Specifies the load capacitance, in farads and assuming a series model, of the DUT in order to compute the impedance range when the lcr_impedance_range_source property is set to LCRImpedanceRangeSource.LOAD_CONFIGURATION.

    Valid values: (0 farads, +inf farads)
    0 is a special value that signifies +inf farads.

    Default Value: Search ni.com for Supported Properties by Device for the default value by instrument

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].lcr_load_capacitance`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.lcr_load_capacitance`
    '''
    lcr_load_compensation_enabled = _attributes.AttributeViBoolean(1150222)
    '''Type: bool

    Specifies whether to apply load LCR compensation data to LCR measurements.
    Both the lcr_open_compensation_enabled and lcr_short_compensation_enabled properties must be set to True in order to set this property to True.

    Use the lcr_open_short_load_compensation_data_source property to define where the load compensation data that is applied to LCR measurements comes from.

    Note:
    Load compensation data are applied only for those specific frequencies you define with perform_lcr_load_compensation;
    load compensation is not interpolated from the specific frequencies you define and applied to other frequencies.

    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].lcr_load_compensation_enabled`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.lcr_load_compensation_enabled`
    '''
    lcr_load_inductance = _attributes.AttributeViReal64(1150319)
    '''Type: float

    Specifies the load inductance, in henrys and assuming a series model, of the DUT in order to compute the impedance range when the lcr_impedance_range_source property is set to LCRImpedanceRangeSource.LOAD_CONFIGURATION.

    Valid values: [0 henrys, +inf henrys)

    Default Value: Search ni.com for Supported Properties by Device for the default value by instrument

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].lcr_load_inductance`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.lcr_load_inductance`
    '''
    lcr_load_resistance = _attributes.AttributeViReal64(1150318)
    '''Type: float

    Specifies the load resistance, in ohms and assuming a series model, of the DUT in order to compute the impedance range when the lcr_impedance_range_source property is set to LCRImpedanceRangeSource.LOAD_CONFIGURATION.

    Valid values: [0 ohms, +inf ohms)

    Default Value: Search ni.com for Supported Properties by Device for the default value by instrument

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].lcr_load_resistance`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.lcr_load_resistance`
    '''
    lcr_measured_load_reactance = _attributes.AttributeViReal64(1150269)
    '''Type: float

    Specifies the reactance, in ohms, of the load used for load LCR compensation as measured by the instrument.
    This property applies when lcr_open_short_load_compensation_data_source is set to LCROpenShortLoadCompensationDataSource.AS_DEFINED.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].lcr_measured_load_reactance`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.lcr_measured_load_reactance`
    '''
    lcr_measured_load_resistance = _attributes.AttributeViReal64(1150268)
    '''Type: float

    Specifies the resistance, in ohms, of the load used for load LCR compensation as measured by the instrument.
    This property applies when lcr_open_short_load_compensation_data_source is set to LCROpenShortLoadCompensationDataSource.AS_DEFINED.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].lcr_measured_load_resistance`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.lcr_measured_load_resistance`
    '''
    lcr_measurement_time = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.LCRMeasurementTime, 1150218)
    '''Type: enums.LCRMeasurementTime

    Selects a general aperture time profile for LCR measurements. The actual duration of each profile depends on the frequency of the LCR test signal.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].lcr_measurement_time`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.lcr_measurement_time`
    '''
    lcr_open_compensation_enabled = _attributes.AttributeViBoolean(1150220)
    '''Type: bool

    Specifies whether to apply open LCR compensation data to LCR measurements.
    Use the lcr_open_short_load_compensation_data_source property to define where the open compensation data that is applied to LCR measurements comes from.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].lcr_open_compensation_enabled`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.lcr_open_compensation_enabled`
    '''
    lcr_open_conductance = _attributes.AttributeViReal64(1150261)
    '''Type: float

    Specifies the conductance, in siemens, of the circuit used for open LCR compensation.
    This property applies when lcr_open_short_load_compensation_data_source is set to LCROpenShortLoadCompensationDataSource.AS_DEFINED.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].lcr_open_conductance`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.lcr_open_conductance`
    '''
    lcr_open_short_load_compensation_data_source = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.LCROpenShortLoadCompensationDataSource, 1150223)
    '''Type: enums.LCROpenShortLoadCompensationDataSource

    Specifies the source of the LCR compensation data NI-DCPower applies to LCR measurements.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].lcr_open_short_load_compensation_data_source`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.lcr_open_short_load_compensation_data_source`
    '''
    lcr_open_susceptance = _attributes.AttributeViReal64(1150262)
    '''Type: float

    Specifies the susceptance, in siemens, of the circuit used for open LCR compensation.
    This property applies when lcr_open_short_load_compensation_data_source is set to LCROpenShortLoadCompensationDataSource.AS_DEFINED.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].lcr_open_susceptance`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.lcr_open_susceptance`
    '''
    lcr_short_compensation_enabled = _attributes.AttributeViBoolean(1150221)
    '''Type: bool

    Specifies whether to apply short LCR compensation data to LCR measurements.
    Use the lcr_open_short_load_compensation_data_source property to define where the short compensation data that is applied to LCR measurements comes from.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].lcr_short_compensation_enabled`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.lcr_short_compensation_enabled`
    '''
    lcr_short_custom_cable_compensation_enabled = _attributes.AttributeViBoolean(1150299)
    '''Type: bool

    Defines how to apply short custom cable compensation in LCR mode when cable_length property is set to CableLength.CUSTOM_ONBOARD_STORAGE or CableLength.CUSTOM_AS_CONFIGURED.

    LCR custom cable compensation uses compensation data for both an open and short configuration.
    For open custom cable compensation, you must supply your own data from a call to perform_lcr_open_custom_cable_compensation.
    For short custom cable compensation, you can supply your own data from a call to perform_lcr_short_custom_cable_compensation or NI-DCPower can apply a default set of short compensation data.

    +-------+-----------------------------------------------------------------------------------------------------+
    | False | Uses default short compensation data.                                                               |
    +-------+-----------------------------------------------------------------------------------------------------+
    | True  | Uses short custom cable compensation data generated by perform_lcr_short_custom_cable_compensation. |
    +-------+-----------------------------------------------------------------------------------------------------+

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].lcr_short_custom_cable_compensation_enabled`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.lcr_short_custom_cable_compensation_enabled`
    '''
    lcr_short_reactance = _attributes.AttributeViReal64(1150264)
    '''Type: float

    Specifies the reactance, in ohms, of the circuit used for short LCR compensation.
    This property applies when lcr_open_short_load_compensation_data_source is set to LCROpenShortLoadCompensationDataSource.AS_DEFINED.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].lcr_short_reactance`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.lcr_short_reactance`
    '''
    lcr_short_resistance = _attributes.AttributeViReal64(1150263)
    '''Type: float

    Specifies the resistance, in ohms, of the circuit used for short LCR compensation.
    This property applies when lcr_open_short_load_compensation_data_source is set to LCROpenShortLoadCompensationDataSource.AS_DEFINED.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].lcr_short_resistance`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.lcr_short_resistance`
    '''
    lcr_source_aperture_time = _attributes.AttributeViReal64(1150349)
    '''Type: float

    Specifies the LCR source aperture time for a channel, in seconds.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].lcr_source_aperture_time`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.lcr_source_aperture_time`
    '''
    lcr_source_delay_mode = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.LCRSourceDelayMode, 1150315)
    '''Type: enums.LCRSourceDelayMode

    For instruments in LCR mode, determines whether NI-DCPower automatically calculates and applies the source delay or applies a source delay you set manually.

    You can return the source delay duration for either option by reading source_delay.

    When you use this property to manually set the source delay, it is possible to set source delays short enough to unbalance the bridge and affect measurement accuracy. LCR measurement methods report whether the bridge is unbalanced.

    Default Value: LCRSourceDelayMode.AUTOMATIC

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].lcr_source_delay_mode`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.lcr_source_delay_mode`
    '''
    lcr_stimulus_function = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.LCRStimulusFunction, 1150209)
    '''Type: enums.LCRStimulusFunction

    Specifies the type of test signal to apply to the DUT for LCR measurements.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].lcr_stimulus_function`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.lcr_stimulus_function`
    '''
    lcr_voltage_amplitude = _attributes.AttributeViReal64(1150211)
    '''Type: float

    Specifies the amplitude, in volts RMS, of the AC voltage test signal applied to the DUT for LCR measurements.
    This property applies when the lcr_stimulus_function property is set to LCRStimulusFunction.VOLTAGE.

    Valid Values: 7.08e-4 V RMS to 7.07 V RMS

    Instrument specifications affect the valid values you can program. Refer to the specifications for your instrument for more information.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].lcr_voltage_amplitude`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.lcr_voltage_amplitude`
    '''
    lcr_voltage_range = _attributes.AttributeViReal64(1150265)
    '''Type: float

    Specifies the voltage range, in volts RMS, for the specified channel(s).
    The range defines the valid values to which you can set the lcr_voltage_amplitude.
    For valid ranges, refer to the specifications for your instrument.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].lcr_voltage_range`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.lcr_voltage_range`
    '''
    logical_name = _attributes.AttributeViString(1050305)
    '''Type: str

    Contains the logical name you specified when opening the current IVI session.
    You can pass a logical name to the __init__ method. The IVI Configuration utility must contain an entry for the logical name. The logical name entry refers to a method section in the IVI Configuration file. The method section specifies a physical device and initial user options.
    '''
    measure_buffer_size = _attributes.AttributeViInt32(1150077)
    '''Type: int

    Specifies the number of samples that the active channel measurement buffer can hold.
    The default value is the maximum number of samples that a device is capable of recording in one second.
    Valid Values: The PXIe-4051, PXIe-4147, and PXIe-4151 support values from 170 to 18000110.
    The PXIe-4162/4163 supports values from  256 to 1000192.
    The PXIe-4190 supports values from 102 to 6000048.
    The PXIe-4112, PXIe-4113, and PXIe-4154 support values from 1000 to 178956970.
    All other supported instruments support values from 1000 to 268435455.
    Default Value: Varies by device. Refer to Supported Properties by Device topic in the NI DC Power Supplies and SMUs Help for more information about default values.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].measure_buffer_size`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.measure_buffer_size`
    '''
    measure_complete_event_delay = _attributes.AttributeViReal64TimeDeltaSeconds(1150046)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    Specifies the amount of time to delay the generation of the Measure Complete event, in seconds.
    Valid Values: The PXIe-4051 supports values from 0 seconds to 39 seconds.
    The PXIe-4147 supports values from 0 seconds to 26.5 seconds.
    The PXIe-4151 supports values from 0 seconds to 42 seconds.
    The PXIe-4162/4163 and PXIe-4190 support values from 0 seconds to 23 seconds.
    All other supported instruments support values from 0 to 167 seconds.
    Default Value: Varies by device. Refer to Supported Properties by Device topic in the NI DC Power Supplies and SMUs Help for more information about default values.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].measure_complete_event_delay`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.measure_complete_event_delay`
    '''
    measure_complete_event_output_behavior = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.EventOutputBehavior, 1150333)
    '''Type: enums.EventOutputBehavior

    Determines the event type's behavior when a corresponding trigger is received. If you set the Measure Complete event output behavior to EventOutputBehavior.PULSE, a single pulse is transmitted. If you set the Measure Complete event output behavior to EventOutputBehavior.TOGGLE, the output level toggles between low and high. The default value is EventOutputBehavior.PULSE.

    Note:
    This property is not supported by all output terminals.
    This property is not supported on all devices. For more information about supported devices and terminals, search Supported Properties by Device on ni.com.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].measure_complete_event_output_behavior`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.measure_complete_event_output_behavior`
    '''
    measure_complete_event_output_terminal = _attributes.AttributeViString(1150047)
    '''Type: str

    Specifies the output terminal for exporting the Measure Complete event.
    Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].measure_complete_event_output_terminal`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.measure_complete_event_output_terminal`
    '''
    measure_complete_event_pulse_polarity = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.Polarity, 1150044)
    '''Type: enums.Polarity

    Specifies the behavior of the Measure Complete event.
    Default Value: Polarity.HIGH

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].measure_complete_event_pulse_polarity`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.measure_complete_event_pulse_polarity`
    '''
    measure_complete_event_pulse_width = _attributes.AttributeViReal64(1150045)
    '''Type: float

    Specifies the width of the Measure Complete event, in seconds.
    The minimum event pulse width value for PXI devices is 150 ns, and the minimum event pulse width value for PXI Express devices is 250 ns.
    The maximum event pulse width value for all devices is 1.6 microseconds.
    Valid Values: 1.5e-7 to 1.6e-6
    Default Value: The default value for PXI devices is 150 ns. The default value for PXI Express devices is 250 ns.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].measure_complete_event_pulse_width`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.measure_complete_event_pulse_width`
    '''
    measure_complete_event_toggle_initial_state = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.EventToggleInitialState, 1150334)
    '''Type: enums.EventToggleInitialState

    Specifies the initial state of the Measure Complete event when you set the measure_complete_event_output_behavior property to EventOutputBehavior.TOGGLE.
    For a Single Point mode acquisition, if you set the initial state to NIDCPOWER_VAL_LOW_STATE, the output is set to low at session commit.
    The output switches to high when the event occurs during the acquisition. If you set the initial state to NIDCPOWER_VAL_HIGH_STATE, the output is set to a high state at session commit.
    The output switches to low when the event occurs during the acquisition.
    For a Sequence mode operation, if you set the initial state to NIDCPOWER_VAL_LOW_STATE, the output is set to low at session commit. The output switches to high the first time an event occurs during the acquisition.
    The second time an event occurs, the output switches to low. This pattern repeats for any subsequent event occurrences.
    If you set the initial state to NIDCPOWER_VAL_HIGH_STATE, the output is set to high at session commit.
    The output switches to low on the first time the event occurs during the acquisition. The second time the event occurs, the output switches to high.
    This pattern repeats for any subsequent event occurrences.
    The default value is NIDCPOWER_VAL_LOW_STATE.

    Note:
    This property is not supported on all devices. For more information about supported devices and terminals, search Supported Properties by Device on ni.com

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].measure_complete_event_toggle_initial_state`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.measure_complete_event_toggle_initial_state`
    '''
    measure_record_delta_time = _attributes.AttributeViReal64TimeDeltaSeconds(1150065)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    Queries the amount of time, in seconds, between between the start of two consecutive measurements in a measure record. Only query this property after the desired measurement settings are committed.
    two measurements and the rest would differ.

    Note: This property is not available when Auto Zero is configured to Once because the amount of time between the first

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].measure_record_delta_time`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.measure_record_delta_time`
    '''
    measure_record_length = _attributes.AttributeViInt32(1150063)
    '''Type: int

    Specifies how many measurements compose a measure record. When this property is set to a value greater than 1, the measure_when property must be set to MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE or MeasureWhen.ON_MEASURE_TRIGGER.
    Valid Values: 1 to 16,777,216
    Default Value: 1

    Note:
    This property is not available in a session involving multiple channels.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].measure_record_length`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.measure_record_length`
    '''
    measure_record_length_is_finite = _attributes.AttributeViBoolean(1150064)
    '''Type: bool

    Specifies whether to take continuous measurements. Call the abort method to stop continuous measurements. When this property is set to False and the source_mode property is set to SourceMode.SINGLE_POINT, the measure_when property must be set to MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE or MeasureWhen.ON_MEASURE_TRIGGER. When this property is set to False and the source_mode property is set to SourceMode.SEQUENCE, the measure_when property must be set to MeasureWhen.ON_MEASURE_TRIGGER.
    Default Value: True

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device. This property is not available in a session involving multiple channels.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].measure_record_length_is_finite`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.measure_record_length_is_finite`
    '''
    measure_trigger_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.TriggerType, 1150034)
    '''Type: enums.TriggerType

    Specifies the behavior of the Measure trigger.
    Default Value: TriggerType.DIGITAL_EDGE

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].measure_trigger_type`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.measure_trigger_type`
    '''
    measure_when = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.MeasureWhen, 1150057)
    '''Type: enums.MeasureWhen

    Specifies when the measure unit should acquire measurements. Unless this property is configured to MeasureWhen.ON_MEASURE_TRIGGER, the measure_trigger_type property is ignored.
    Refer to the Acquiring Measurements topic in the NI DC Power Supplies and SMUs Help for more information about how to configure your measurements.
    Default Value: If the source_mode property is set to SourceMode.SINGLE_POINT, the default value is MeasureWhen.ON_DEMAND. This value supports only the measure method and measure_multiple method. If the source_mode property is set to SourceMode.SEQUENCE, the default value is MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE. This value supports only the fetch_multiple method.

    Note:
    NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].measure_when`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.measure_when`
    '''
    merged_channels = _attributes.AttributeViStringRepeatedCapability(1150249)
    '''Type: str

    Specifies the channel(s) to merge with a designated primary channel of an instrument in order to increase the maximum current you can source from the instrument.
    This property designates the merge channels to combine with a primary channel. To designate the primary channel, initialize the session to the primary channel only.
    Note: You cannot change the merge configuration with this property when the session is in the Running state.
    For complete information on using merged channels with this property, refer to Merged Channels in the NI DC Power Supplies and SMUs Help.

    Note:
    NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device. Devices that do not support this property behave as if no channels were merged.
    Default Value: Refer to the Supported Properties by Device topic for the default value by device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].merged_channels`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.merged_channels`
    '''
    output_capacitance = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.OutputCapacitance, 1150014)
    '''Type: enums.OutputCapacitance

    Specifies whether to use a low or high capacitance on the output for the specified channel(s).
    Refer to the NI PXI-4130 Output Capacitance Selection topic in the NI DC Power Supplies and SMUs Help for more information about capacitance.

    Note:
    NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].output_capacitance`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.output_capacitance`
    '''
    output_connected = _attributes.AttributeViBoolean(1150060)
    '''Type: bool

    Specifies whether the output relay is connected (closed) or disconnected (open). The output_enabled property does not change based on this property; they are independent of each other.

    Set this property to False to disconnect the output terminal from the output.

    Default Value: True

    Note:
    Only disconnect the output when disconnecting is necessary for your application. For example, a battery connected to the output terminal might discharge unless the relay is disconnected. Excessive connecting and disconnecting of the output can cause premature wear on electromechanical relays, such as those used by the PXIe-4147, PXI-4132, or PXIe-4138/39.

    The PXIe-4051 does not have an output relay. For the PXIe-4051, this property specifies whether the input MOSFETs are connected (ON) or disconnected (OFF).

    NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].output_connected`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.output_connected`
    '''
    output_cutoff_current_change_limit_high = _attributes.AttributeViReal64(1150295)
    '''Type: float

    Specifies a limit for positive current slew rate, in amps per microsecond, for output cutoff.
    If the current increases at a rate that exceeds this limit, the output is disconnected.

    To find out whether an output has exceeded this limit, call the query_latched_output_cutoff_state method with OutputCutoffReason.CURRENT_CHANGE_HIGH as the output cutoff reason.

    Note:
    NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].output_cutoff_current_change_limit_high`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.output_cutoff_current_change_limit_high`
    '''
    output_cutoff_current_change_limit_low = _attributes.AttributeViReal64(1150239)
    '''Type: float

    Specifies a limit for negative current slew rate, in amps per microsecond, for output cutoff.
    If the current decreases at a rate that exceeds this limit, the output is disconnected.

    To find out whether an output has exceeded this limit, call the query_latched_output_cutoff_state method with OutputCutoffReason.CURRENT_CHANGE_LOW as the output cutoff reason.

    Note:
    NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].output_cutoff_current_change_limit_low`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.output_cutoff_current_change_limit_low`
    '''
    output_cutoff_current_measure_limit_high = _attributes.AttributeViReal64(1150237)
    '''Type: float

    Specifies a high limit current value, in amps, for output cutoff.
    If the measured current exceeds this limit, the output is disconnected.

    To find out whether an output has exceeded this limit, call the query_latched_output_cutoff_state method with OutputCutoffReason.CURRENT_MEASURE_HIGH as the output cutoff reason.

    Note:
    NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].output_cutoff_current_measure_limit_high`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.output_cutoff_current_measure_limit_high`
    '''
    output_cutoff_current_measure_limit_low = _attributes.AttributeViReal64(1150293)
    '''Type: float

    Specifies a low limit current value, in amps, for output cutoff.
    If the measured current falls below this limit, the output is disconnected.

    To find out whether an output has fallen below this limit, call the query_latched_output_cutoff_state method with OutputCutoffReason.CURRENT_MEASURE_LOW as the output cutoff reason.

    Note:
    NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].output_cutoff_current_measure_limit_low`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.output_cutoff_current_measure_limit_low`
    '''
    output_cutoff_current_overrange_enabled = _attributes.AttributeViBoolean(1150240)
    '''Type: bool

    Enables or disables current overrange functionality for output cutoff. If enabled, the output is disconnected when the measured current saturates the current range.

    To find out whether an output has exceeded this limit, call the query_latched_output_cutoff_state method with OutputCutoffReason.CURRENT_SATURATED as the output cutoff reason.

    Note:
    NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].output_cutoff_current_overrange_enabled`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.output_cutoff_current_overrange_enabled`
    '''
    output_cutoff_delay = _attributes.AttributeViReal64TimeDeltaSeconds(1150300)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    Delays disconnecting the output by the time you specify, in seconds, when a limit is exceeded.

    Note:
    NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].output_cutoff_delay`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.output_cutoff_delay`
    '''
    output_cutoff_enabled = _attributes.AttributeViBoolean(1150235)
    '''Type: bool

    Enables or disables output cutoff functionality. If enabled, you can define output cutoffs that, if exceeded, cause the output of the specified channel(s) to be disconnected.
    When this property is disabled, all other output cutoff properties are ignored.

    Note:
    NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.
     Instruments that do not support this property behave as if this property were set to False.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].output_cutoff_enabled`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.output_cutoff_enabled`
    '''
    output_cutoff_voltage_change_limit_high = _attributes.AttributeViReal64(1150294)
    '''Type: float

    Specifies a limit for positive voltage slew rate, in volts per microsecond, for output cutoff.
    If the voltage increases at a rate that exceeds this limit, the output is disconnected.

    To find out whether an output has exceeded this limit, call the query_latched_output_cutoff_state with OutputCutoffReason.VOLTAGE_CHANGE_HIGH as the output cutoff reason.

    Note:
    NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].output_cutoff_voltage_change_limit_high`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.output_cutoff_voltage_change_limit_high`
    '''
    output_cutoff_voltage_change_limit_low = _attributes.AttributeViReal64(1150238)
    '''Type: float

    Specifies a limit for negative voltage slew rate, in volts per microsecond, for output cutoff.
    If the voltage decreases at a rate that exceeds this limit, the output is disconnected.

    To find out whether an output has exceeded this limit, call the query_latched_output_cutoff_state with OutputCutoffReason.VOLTAGE_CHANGE_LOW as the output cutoff reason.

    Note:
    NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].output_cutoff_voltage_change_limit_low`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.output_cutoff_voltage_change_limit_low`
    '''
    output_cutoff_voltage_measure_limit_high = _attributes.AttributeViReal64(1150357)
    '''Type: float

    Specifies a high limit voltage value, in volts, for output cutoff.
    If the measured voltage exceeds this limit, the output is disconnected.

    To find out whether an output has exceeded this limit, call the query_latched_output_cutoff_state method with OutputCutoffReason.VOLTAGE_MEASURE_HIGH as the output cutoff reason.

    Note:
    NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].output_cutoff_voltage_measure_limit_high`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.output_cutoff_voltage_measure_limit_high`
    '''
    output_cutoff_voltage_measure_limit_low = _attributes.AttributeViReal64(1150358)
    '''Type: float

    Specifies a low limit voltage value, in volts, for output cutoff.
    If the measured voltage falls below this limit, the output is disconnected.

    To find out whether an output has fallen below this limit, call the query_latched_output_cutoff_state method with OutputCutoffReason.VOLTAGE_MEASURE_LOW as the output cutoff reason.

    Note:
    NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].output_cutoff_voltage_measure_limit_low`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.output_cutoff_voltage_measure_limit_low`
    '''
    output_cutoff_voltage_output_limit_high = _attributes.AttributeViReal64(1150236)
    '''Type: float

    Specifies a high limit voltage value, in volts, for output cutoff.
    If the voltage output exceeds this limit, the output is disconnected.

    To find out whether an output has exceeded this limit, call the query_latched_output_cutoff_state method with OutputCutoffReason.VOLTAGE_OUTPUT_HIGH as the output cutoff reason.

    Note:
    NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].output_cutoff_voltage_output_limit_high`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.output_cutoff_voltage_output_limit_high`
    '''
    output_cutoff_voltage_output_limit_low = _attributes.AttributeViReal64(1150292)
    '''Type: float

    Specifies a low limit voltage value, in volts, for output cutoff.
    If the voltage output falls below this limit, the output is disconnected.

    To find out whether an output has fallen below this limit, call the query_latched_output_cutoff_state method with OutputCutoffReason.VOLTAGE_OUTPUT_LOW as the output cutoff reason.

    Note:
    NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].output_cutoff_voltage_output_limit_low`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.output_cutoff_voltage_output_limit_low`
    '''
    output_enabled = _attributes.AttributeViBoolean(1250006)
    '''Type: bool

    Specifies whether the output is enabled (True) or disabled (False).
    Depending on the value you specify for the output_function property, you also must set the voltage level or current level in addition to enabling the output

    Default Value: The default value is True if you use the __init__ method to open the session. Otherwise the default value is False, including when you use a calibration session or the deprecated programming model.

    Note:
    If the session is in the Committed or Uncommitted states, enabling the output does not take effect until you call the initiate method. Refer to the Programming States topic in the NI DC Power Supplies and SMUs Help for more information about NI-DCPower programming states.

    NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].output_enabled`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.output_enabled`
    '''
    output_function = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.OutputFunction, 1150008)
    '''Type: enums.OutputFunction

    Configures the method to generate on the specified channel(s).
    When OutputFunction.DC_VOLTAGE is selected, the device generates the desired voltage level on the output as long as the output current is below the current limit. You can use the following properties to configure the channel when OutputFunction.DC_VOLTAGE is selected:
    voltage_level
    current_limit
    current_limit_high
    current_limit_low
    voltage_level_range
    current_limit_range
    compliance_limit_symmetry
    When OutputFunction.DC_CURRENT is selected, the device generates the desired current level on the output as long as the output voltage is below the voltage limit. You can use the following properties to configure the channel when OutputFunction.DC_CURRENT is selected:
    current_level
    voltage_limit
    voltage_limit_high
    voltage_limit_low
    current_level_range
    voltage_limit_range
    compliance_limit_symmetry

    Note:
    NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].output_function`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.output_function`
    '''
    output_resistance = _attributes.AttributeViReal64(1150061)
    '''Type: float

    Specifies the output resistance that the device attempts to generate for the specified channel(s). This property is available only when you set the output_function property on a support device. Refer to a supported device's topic about output resistance for more information about selecting an output resistance.
    about supported devices.
    Default Value: 0.0

    Note:
    NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].output_resistance`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.output_resistance`
    '''
    overranging_enabled = _attributes.AttributeViBoolean(1150007)
    '''Type: bool

    Specifies whether NI-DCPower allows setting the voltage level, current level, voltage limit and current limit outside the device specification limits. True means that overranging is enabled.
    Refer to the Ranges topic in the NI DC Power Supplies and SMUs Help for more information about overranging.
    Default Value: False

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].overranging_enabled`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.overranging_enabled`
    '''
    ovp_enabled = _attributes.AttributeViBoolean(1250002)
    '''Type: bool

    Enables (True) or disables (False) overvoltage protection (OVP).
    Refer to the Output Overvoltage Protection topic in the NI DC Power Supplies and SMUs Help for more information about overvoltage protection.
    Default Value: False

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].ovp_enabled`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.ovp_enabled`
    '''
    ovp_limit = _attributes.AttributeViReal64(1250003)
    '''Type: float

    Determines the voltage limit, in volts, beyond which overvoltage protection (OVP) engages.
    The limit is specified as a positive value, but symmetric positive and negative limits are enforced simultaneously.
    For example, setting the OVP Limit to 65 will configure the OVP feature to trigger an OVP error if the output exceeds ±65 V.

    Valid Values: 2 V to 210 V
    Default Value: 210 V

    Note:
    NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].ovp_limit`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.ovp_limit`
    '''
    power_allocation_mode = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.PowerAllocationMode, 1150207)
    '''Type: enums.PowerAllocationMode

    Determines whether the device sources the power its source configuration requires or a specific wattage you request; determines whether NI-DCPower proactively checks that this sourcing power is within the maximum per-channel and overall sourcing power of the device.

     When this property configures NI-DCPower to perform a sourcing power check, a device is not permitted to source power in excess of its maximum per-channel or overall sourcing power. If the check determines a source configuration or power request would require the device to do so, NI-DCPower returns an error.

     When this property does not configure NI-DCPower to perform a sourcing power check, a device can attempt to fulfill source configurations that would require it to source power in excess of its maximum per-channel or overall sourcing power and may shut down to prevent damage.

     Default Value: Refer to the Supported Properties by Device topic for the default value by device.

    Note:
    NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device. Devices that do not support this property behave as if this property were set to PowerAllocationMode.DISABLED.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].power_allocation_mode`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.power_allocation_mode`
    '''
    power_line_frequency = _attributes.AttributeViReal64(1150020)
    '''Type: float

    Specifies the power line frequency for specified channel(s). NI-DCPower uses this value to select a timebase for setting the aperture_time property in power line cycles (PLCs).
    in the NI DC Power Supplies and SMUs Help for information about supported devices.
    Default Value: NIDCPOWER_VAL_60_HERTZ

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].power_line_frequency`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.power_line_frequency`
    '''
    power_source = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.PowerSource, 1150000)
    '''Type: enums.PowerSource

    Specifies the power source to use. NI-DCPower switches the power source used by the device to the specified value.
    Default Value: PowerSource.AUTOMATIC
    is set to PowerSource.AUTOMATIC. However, if the session is in the Committed or Uncommitted state when you set this property, the power source selection only occurs after you call the initiate method.

    Note: Automatic selection is not persistent and occurs only at the time this property
    '''
    power_source_in_use = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.PowerSourceInUse, 1150001)
    '''Type: enums.PowerSourceInUse

    Indicates whether the device is using the internal or auxiliary power source to generate power.
    '''
    pulse_bias_current_level = _attributes.AttributeViReal64(1150088)
    '''Type: float

    Specifies the pulse bias current level, in amps, that the device attempts to generate on the specified channel(s) during the off phase of a pulse.
    This property is applicable only if the output_function property is set to OutputFunction.PULSE_CURRENT.
    Valid Values: The valid values for this property are defined by the values you specify for the pulse_current_level_range property.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].pulse_bias_current_level`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.pulse_bias_current_level`
    '''
    pulse_bias_current_limit = _attributes.AttributeViReal64(1150083)
    '''Type: float

    Specifies the pulse bias current limit, in amps, that the output cannot exceed when generating the desired pulse bias voltage on the specified channel(s) during the off phase of a pulse.
    This property is applicable only if the output_function property is set to OutputFunction.PULSE_VOLTAGE.
    Valid Values: The valid values for this property are defined by the values you specify for the pulse_current_limit_range property.

    Note:
    NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].pulse_bias_current_limit`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.pulse_bias_current_limit`
    '''
    pulse_bias_current_limit_high = _attributes.AttributeViReal64(1150195)
    '''Type: float

    Specifies the maximum current, in amps, that the output can produce when
    generating the desired pulse voltage on the specified channel(s) during
    the *off* phase of a pulse.
    This property is applicable only if the compliance_limit_symmetry property is set to
    ComplianceLimitSymmetry.ASYMMETRIC and the output_function property is set to OutputFunction.PULSE_VOLTAGE.
    You must also specify a pulse_bias_current_limit_low to complete the
    asymmetric range.
    **Valid Values:** [1% of pulse_current_limit_range, pulse_current_limit_range]
    The range bounded by the limit high and limit low must include zero.
    **Default Value:** Search ni.com for Supported Properties by Device for the default value by device.
    **Related Topics:**
    Ranges;
    Changing Ranges;
    Overranging

    Note:
    The limit may be extended beyond the selected limit range if the
    overranging_enabled property is
    set to True or if the output_function property is set to a
    pulsing method.

    NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].pulse_bias_current_limit_high`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.pulse_bias_current_limit_high`
    '''
    pulse_bias_current_limit_low = _attributes.AttributeViReal64(1150196)
    '''Type: float

    Specifies the minimum current, in amps, that the output can produce when
    generating the desired pulse voltage on the specified channel(s) during
    the *off* phase of a pulse.
    This property is applicable only if the compliance_limit_symmetry property is set to
    ComplianceLimitSymmetry.ASYMMETRIC and the output_function property is set to OutputFunction.PULSE_VOLTAGE.
    You must also specify a pulse_bias_current_limit_high to complete the
    asymmetric range.
    **Valid Values:** [-pulse_current_limit_range, -1% of pulse_current_limit_range]
    The range bounded by the limit high and limit low must include zero.
    **Default Value:** Search ni.com for Supported Properties by Device for the default value by device.
    **Related Topics:**
    Ranges;
    Changing Ranges;
    Overranging

    Note:
    The limit may be extended beyond the selected limit range if the
    overranging_enabled property is
    set to True or if the output_function property is set to a
    pulsing method.

    NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].pulse_bias_current_limit_low`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.pulse_bias_current_limit_low`
    '''
    pulse_bias_delay = _attributes.AttributeViReal64(1150092)
    '''Type: float

    Determines when, in seconds, the device generates the Pulse Complete event after generating the off level of a pulse.
    Valid Values: 0 to 167 seconds
    Default Value: 16.67 milliseconds

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].pulse_bias_delay`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.pulse_bias_delay`
    '''
    pulse_bias_voltage_level = _attributes.AttributeViReal64(1150082)
    '''Type: float

    Specifies the pulse bias voltage level, in volts, that the device attempts to generate on the specified channel(s) during the off phase of a pulse.
    This property is applicable only if the output_function property is set to OutputFunction.PULSE_VOLTAGE.
    Valid Values: The valid values for this property are defined by the values you specify for the pulse_voltage_level_range property.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].pulse_bias_voltage_level`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.pulse_bias_voltage_level`
    '''
    pulse_bias_voltage_limit = _attributes.AttributeViReal64(1150089)
    '''Type: float

    Specifies the pulse voltage limit, in volts, that the output cannot exceed when generating the desired current on the specified channel(s) during the off phase of a pulse.
    This property is applicable only if the output_function property is set to OutputFunction.PULSE_CURRENT.
    Valid Values: The valid values for this property are defined by the values you specify for the pulse_voltage_limit_range property.

    Note:
    NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].pulse_bias_voltage_limit`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.pulse_bias_voltage_limit`
    '''
    pulse_bias_voltage_limit_high = _attributes.AttributeViReal64(1150191)
    '''Type: float

    Specifies the maximum voltage, in volts, that the output can produce
    when generating the desired pulse current on the specified channel(s)
    during the *off* phase of a pulse.
    This property is applicable only if the compliance_limit_symmetry property is set to
    ComplianceLimitSymmetry.ASYMMETRIC and the output_function property is set to OutputFunction.PULSE_CURRENT.
    You must also specify a pulse_bias_voltage_limit_low to complete the
    asymmetric range.
    **Valid Values:** [1% of pulse_voltage_limit_range, pulse_voltage_limit_range]
    The range bounded by the limit high and limit low must include zero.
    **Default Value:** Search ni.com for Supported Properties by Device for the default value by device.
    **Related Topics:**
    Ranges;
    Changing Ranges;
    Overranging

    Note:
    The limit may be extended beyond the selected limit range if the
    overranging_enabled property is
    set to True or if the output_function property is set to a
    pulsing method.

    NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].pulse_bias_voltage_limit_high`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.pulse_bias_voltage_limit_high`
    '''
    pulse_bias_voltage_limit_low = _attributes.AttributeViReal64(1150192)
    '''Type: float

    Specifies the minimum voltage, in volts, that the output can produce
    when generating the desired pulse current on the specified channel(s)
    during the *off* phase of a pulse.
    This property is applicable only if the compliance_limit_symmetry property is set to
    ComplianceLimitSymmetry.ASYMMETRIC and the output_function property is set to OutputFunction.PULSE_CURRENT.
    You must also specify a pulse_bias_voltage_limit_high to complete the
    asymmetric range.
    **Valid Values:** [-pulse_voltage_limit_range, -1% of pulse_voltage_limit_range]
    The range bounded by the limit high and limit low must include zero.
    **Default Value:** Search ni.com for Supported Properties by Device for the default value by device.
    **Related Topics:**
    Ranges;
    Changing Ranges;
    Overranging

    Note:
    The limit may be extended beyond the selected limit range if the
    overranging_enabled property is
    set to True or if the output_function property is set to a
    pulsing method.

    NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].pulse_bias_voltage_limit_low`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.pulse_bias_voltage_limit_low`
    '''
    pulse_complete_event_output_terminal = _attributes.AttributeViString(1150099)
    '''Type: str

    Specifies the output terminal for exporting the Pulse Complete event.
    Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.
    Default Value:The default value for PXI Express devices is 250 ns.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].pulse_complete_event_output_terminal`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.pulse_complete_event_output_terminal`
    '''
    pulse_complete_event_pulse_polarity = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.Polarity, 1150100)
    '''Type: enums.Polarity

    Specifies the behavior of the Pulse Complete event.
    Default Value: Polarity.HIGH

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].pulse_complete_event_pulse_polarity`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.pulse_complete_event_pulse_polarity`
    '''
    pulse_complete_event_pulse_width = _attributes.AttributeViReal64(1150101)
    '''Type: float

    Specifies the width of the Pulse Complete event, in seconds.
    The minimum event pulse width value for PXI Express devices is 250 ns.
    The maximum event pulse width value for PXI Express devices is 1.6 microseconds.
    Default Value: The default value for PXI Express devices is 250 ns.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].pulse_complete_event_pulse_width`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.pulse_complete_event_pulse_width`
    '''
    pulse_current_level = _attributes.AttributeViReal64(1150086)
    '''Type: float

    Specifies the pulse current level, in amps, that the device attempts to generate on the specified channel(s) during the on phase of a pulse.
    This property is applicable only if the output_function property is set to OutputFunction.PULSE_CURRENT.
    Valid Values: The valid values for this property are defined by the values you specify for the pulse_current_level_range property.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].pulse_current_level`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.pulse_current_level`
    '''
    pulse_current_level_range = _attributes.AttributeViReal64(1150090)
    '''Type: float

    Specifies the pulse current level range, in amps, for the specified channel(s).
    The range defines the valid values to which you can set the pulse current level and pulse bias current level.
    This property is applicable only if the output_function property is set to OutputFunction.PULSE_CURRENT.
    For valid ranges, refer to the specifications for your instrument.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].pulse_current_level_range`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.pulse_current_level_range`
    '''
    pulse_current_limit = _attributes.AttributeViReal64(1150081)
    '''Type: float

    Specifies the pulse current limit, in amps, that the output cannot exceed when generating the desired pulse voltage on the specified channel(s) during the on phase of a pulse.
    This property is applicable only if the output_function property is set to OutputFunction.PULSE_VOLTAGE and the compliance_limit_symmetry property is set to ComplianceLimitSymmetry.SYMMETRIC.
    Valid Values: The valid values for this property are defined by the values you specify for the pulse_current_limit_range property.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].pulse_current_limit`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.pulse_current_limit`
    '''
    pulse_current_limit_high = _attributes.AttributeViReal64(1150193)
    '''Type: float

    Specifies the maximum current, in amps, that the output can produce when
    generating the desired pulse voltage on the specified channel(s) during
    the *on* phase of a pulse.
    This property is applicable only if the compliance_limit_symmetry property is set to
    ComplianceLimitSymmetry.ASYMMETRIC and the output_function property is set to OutputFunction.PULSE_VOLTAGE.
    You must also specify a pulse_current_limit_low to complete the asymmetric
    range.
    **Valid Values:** [1% of pulse_current_limit_range, pulse_current_limit_range]
    The range bounded by the limit high and limit low must include zero.
    **Default Value:** Search ni.com for Supported Properties by Device for the default value by device.
    **Related Topics:**
    Ranges;
    Changing Ranges;
    Overranging

    Note:
    The limit may be extended beyond the selected limit range if the
    overranging_enabled property is
    set to True or if the output_function property is set to a
    pulsing method.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].pulse_current_limit_high`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.pulse_current_limit_high`
    '''
    pulse_current_limit_low = _attributes.AttributeViReal64(1150194)
    '''Type: float

    Specifies the minimum current, in amps, that the output can produce when
    generating the desired pulse voltage on the specified channel(s) during
    the *on* phase of a pulse.
    This property is applicable only if the compliance_limit_symmetry property is set to
    ComplianceLimitSymmetry.ASYMMETRIC and the output_function property is set to OutputFunction.PULSE_VOLTAGE.
    You must also specify a pulse_current_limit_high to complete the
    asymmetric range.
    **Valid Values:** [-pulse_current_limit_range, -1% of pulse_current_limit_range]
    The range bounded by the limit high and limit low must include zero.
    **Default Value:** Search ni.com for Supported Properties by Device for the default value by device.
    **Related Topics:**
    Ranges;
    Changing Ranges;
    Overranging

    Note:
    The limit may be extended beyond the selected limit range if the
    overranging_enabled property is
    set to True or if the output_function property is set to a
    pulsing method.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].pulse_current_limit_low`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.pulse_current_limit_low`
    '''
    pulse_current_limit_range = _attributes.AttributeViReal64(1150085)
    '''Type: float

    Specifies the pulse current limit range, in amps, for the specified channel(s).
    The range defines the valid values to which you can set the pulse current limit and pulse bias current limit.
    This property is applicable only if the output_function property is set to OutputFunction.PULSE_VOLTAGE.
    For valid ranges, refer to the specifications for your instrument.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].pulse_current_limit_range`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.pulse_current_limit_range`
    '''
    pulse_off_time = _attributes.AttributeViReal64TimeDeltaSeconds(1150094)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    Determines the length, in seconds, of the off phase of a pulse.
    Valid Values: 10 microseconds to 167 seconds
    Default Value: 34 milliseconds

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].pulse_off_time`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.pulse_off_time`
    '''
    pulse_on_time = _attributes.AttributeViReal64TimeDeltaSeconds(1150093)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    Determines the length, in seconds, of the on phase of a pulse.
    Valid Values: 10 microseconds to 167 seconds
    Default Value: 34 milliseconds

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].pulse_on_time`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.pulse_on_time`
    '''
    pulse_trigger_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.TriggerType, 1150095)
    '''Type: enums.TriggerType

    Specifies the behavior of the Pulse trigger.
    Default Value: TriggerType.NONE

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].pulse_trigger_type`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.pulse_trigger_type`
    '''
    pulse_voltage_level = _attributes.AttributeViReal64(1150080)
    '''Type: float

    Specifies the pulse current limit, in amps, that the output cannot exceed when generating the desired pulse voltage on the specified channel(s) during the on phase of a pulse.
    This property is applicable only if the output_function property is set to OutputFunction.PULSE_VOLTAGE.
    Valid Values: The valid values for this property are defined by the values you specify for the pulse_current_limit_range property.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].pulse_voltage_level`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.pulse_voltage_level`
    '''
    pulse_voltage_level_range = _attributes.AttributeViReal64(1150084)
    '''Type: float

    Specifies the pulse voltage level range, in volts, for the specified channel(s).
    The range defines the valid values at which you can set the pulse voltage level and pulse bias voltage level.
    This property is applicable only if the output_function property is set to OutputFunction.PULSE_VOLTAGE.
    For valid ranges, refer to the specifications for your instrument.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].pulse_voltage_level_range`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.pulse_voltage_level_range`
    '''
    pulse_voltage_limit = _attributes.AttributeViReal64(1150087)
    '''Type: float

    Specifies the pulse voltage limit, in volts, that the output cannot exceed when generating the desired pulse current on the specified channel(s) during the on phase of a pulse.
    This property is applicable only if the output_function property is set to OutputFunction.PULSE_CURRENT and the compliance_limit_symmetry property is set to ComplianceLimitSymmetry.SYMMETRIC.
    Valid Values: The valid values for this property are defined by the values you specify for the pulse_voltage_limit_range property.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].pulse_voltage_limit`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.pulse_voltage_limit`
    '''
    pulse_voltage_limit_high = _attributes.AttributeViReal64(1150189)
    '''Type: float

    Specifies the maximum voltage, in volts, that the output can produce
    when generating the desired pulse current on the specified channel(s)
    during the *on* phase of a pulse.
    This property is applicable only if the compliance_limit_symmetry property is set to
    ComplianceLimitSymmetry.ASYMMETRIC and the output_function property is set to OutputFunction.PULSE_CURRENT.
    You must also specify a pulse_voltage_limit_low to complete the asymmetric
    range.
    **Valid Values:** [1% of pulse_voltage_limit_range, pulse_voltage_limit_range]
    The range bounded by the limit high and limit low must include zero.
    **Default Value:** Search ni.com for Supported Properties by Device for the default value by device.
    **Related Topics:**
    Ranges;
    Changing Ranges;
    Overranging

    Note:
    The limit may be extended beyond the selected limit range if the
    overranging_enabled property is
    set to True or if the output_function property is set to a
    pulsing method.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].pulse_voltage_limit_high`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.pulse_voltage_limit_high`
    '''
    pulse_voltage_limit_low = _attributes.AttributeViReal64(1150190)
    '''Type: float

    Specifies the minimum voltage, in volts, that the output can produce
    when generating the desired pulse current on the specified channel(s)
    during the *on* phase of a pulse.
    This property is applicable only if the compliance_limit_symmetry property is set to
    ComplianceLimitSymmetry.ASYMMETRIC and the output_function property is set to OutputFunction.PULSE_CURRENT.
    You must also specify a pulse_voltage_limit_high to complete the
    asymmetric range.
    **Valid Values:** [-pulse_voltage_limit_range, -1% of pulse_voltage_limit_range]
    The range bounded by the limit high and limit low must include zero.
    **Default Value:** Search ni.com for Supported Properties by Device for the default value by device.
    **Related Topics:**
    Ranges;
    Changing Ranges;
    Overranging

    Note:
    The limit may be extended beyond the selected limit range if the
    overranging_enabled property is
    set to True or if the output_function property is set to a
    pulsing method.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].pulse_voltage_limit_low`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.pulse_voltage_limit_low`
    '''
    pulse_voltage_limit_range = _attributes.AttributeViReal64(1150091)
    '''Type: float

    Specifies the pulse voltage limit range, in volts, for the specified channel(s).
    The range defines the valid values to which you can set the pulse voltage limit and pulse bias voltage limit.
    This property is applicable only if the output_function property is set to OutputFunction.PULSE_CURRENT.
    For valid ranges, refer to the specifications for your instrument.

    Note: The channel must be enabled for the specified current limit to take effect. Refer to the output_enabled property for more information about enabling the channel.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].pulse_voltage_limit_range`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.pulse_voltage_limit_range`
    '''
    query_instrument_status = _attributes.AttributeViBoolean(1050003)
    '''Type: bool

    Specifies whether NI-DCPower queries the device status after each operation.
    Querying the device status is useful for debugging. After you validate your program, you can set this property to False to disable status checking and maximize performance.
    NI-DCPower ignores status checking for particular properties regardless of the setting of this property.
    Use the __init__ method to override this value.
    Default Value: True
    '''
    ready_for_pulse_trigger_event_output_terminal = _attributes.AttributeViString(1150102)
    '''Type: str

    Specifies the output terminal for exporting the Ready For Pulse Trigger event.
    Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].ready_for_pulse_trigger_event_output_terminal`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.ready_for_pulse_trigger_event_output_terminal`
    '''
    ready_for_pulse_trigger_event_pulse_polarity = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.Polarity, 1150103)
    '''Type: enums.Polarity

    Specifies the behavior of the Ready For Pulse Trigger event.
    Default Value: Polarity.HIGH

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].ready_for_pulse_trigger_event_pulse_polarity`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.ready_for_pulse_trigger_event_pulse_polarity`
    '''
    ready_for_pulse_trigger_event_pulse_width = _attributes.AttributeViReal64(1150104)
    '''Type: float

    Specifies the width of the Ready For Pulse Trigger event, in seconds.
    The minimum event pulse width value for PXI Express devices is 250 ns.
    The maximum event pulse width value for all devices is 1.6 microseconds.
    Default Value: The default value for PXI Express devices is 250 ns

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].ready_for_pulse_trigger_event_pulse_width`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.ready_for_pulse_trigger_event_pulse_width`
    '''
    requested_power_allocation = _attributes.AttributeViReal64(1150206)
    '''Type: float

    Specifies the power, in watts, to request the device to source from each active channel.
     This property defines the power to source from the device only if the power_allocation_mode property is set to PowerAllocationMode.MANUAL.

     The power you request with this property may be incompatible with the power a given source configuration requires or the power the device can provide:
     If the requested power is less than the power required for the source configuration, the device does not exceed the requested power, and NI-DCPower returns an error.
     If the requested power is greater than the maximum per-channel or overall sourcing power, the device does not exceed the allowed power, and NI-DCPower returns an error.

    Valid Values: [0, device per-channel maximum power]
     Default Value: Refer to the Supported Properties by Device topic for the default value by device.

    Note:
    NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].requested_power_allocation`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.requested_power_allocation`
    '''
    reset_average_before_measurement = _attributes.AttributeViBoolean(1150006)
    '''Type: bool

    Specifies whether the measurement returned from any measurement call starts with a new measurement call (True) or returns a measurement that has already begun or completed(False).
    When you set the samples_to_average property in the Running state, the channel measurements might move out of synchronization. While NI-DCPower automatically synchronizes measurements upon the initialization of a session, you can force a synchronization in the running state before you run the measure_multiple method. To force a synchronization in the running state, set this property to True, and then run the measure_multiple method, specifying all channels in the channel name parameter. You can set the reset_average_before_measurement property to False after the measure_multiple method completes.
    Default Value: True

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].reset_average_before_measurement`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.reset_average_before_measurement`
    '''
    samples_to_average = _attributes.AttributeViInt32(1150003)
    '''Type: int

    Specifies the number of samples to average when you take a measurement.
    Increasing the number of samples to average decreases measurement noise but increases the time required to take a measurement. Refer to the NI PXI-4110, NI PXI-4130, NI PXI-4132, or NI PXIe-4154 Averaging topic for optional property settings to improve immunity to certain noise types, or refer to the NI PXIe-4140/4141  DC Noise Rejection, NI PXIe-4142/4143 DC Noise Rejection, or NI PXIe-4144/4145 DC Noise Rejection topic for information about improving noise immunity for those devices.
    Default Value:
    NI PXI-4110 or NI PXI-4130—10
    NI PXI-4132—1
    NI PXIe-4112—1
    NI PXIe-4113—1
    NI PXIe-4140/4141—1
    NI PXIe-4142/4143—1
    NI PXIe-4144/4145—1
    NI PXIe-4154—500

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].samples_to_average`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.samples_to_average`
    '''
    self_calibration_persistence = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.SelfCalibrationPersistence, 1150073)
    '''Type: enums.SelfCalibrationPersistence

    Specifies whether the values calculated during self-calibration should be written to hardware to be used until the next self-calibration or only used until the reset_device method is called or the machine is powered down.
    This property affects the behavior of the self_cal method. When set to SelfCalibrationPersistence.KEEP_IN_MEMORY, the values calculated by the self_cal method are used in the existing session, as well as in all further sessions until you call the reset_device method or restart the machine. When you set this property to SelfCalibrationPersistence.WRITE_TO_EEPROM, the values calculated by the self_cal method are written to hardware and used in the existing session and in all subsequent sessions until another call to the self_cal method is made.
    about supported devices.
    Default Value: SelfCalibrationPersistence.KEEP_IN_MEMORY

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific instruments within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container instruments to specify a subset.

    Example: :py:attr:`my_session.instruments[ ... ].self_calibration_persistence`

    To set/get on all instruments, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.self_calibration_persistence`
    '''
    sense = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.Sense, 1150013)
    '''Type: enums.Sense

    Selects either local or remote sensing of the output voltage for the specified channel(s).
    Refer to the Local and Remote Sense topic in the NI DC Power Supplies and SMUs Help for more information about sensing voltage on supported channels and about devices that support local and/or remote sensing.
    Default Value: The default value is Sense.LOCAL if the device supports local sense. Otherwise, the default and only supported value is Sense.REMOTE.

    Note:
    NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].sense`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.sense`
    '''
    sequence_advance_trigger_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.TriggerType, 1150026)
    '''Type: enums.TriggerType

    Specifies the behavior of the Sequence Advance trigger.
    Default Value: TriggerType.NONE

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].sequence_advance_trigger_type`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.sequence_advance_trigger_type`
    '''
    sequence_engine_done_event_output_behavior = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.EventOutputBehavior, 1150345)
    '''Type: enums.EventOutputBehavior

    Determines the event type's behavior when a corresponding trigger is received. If you set the Sequence Engine Done event output behavior to EventOutputBehavior.PULSE, a single pulse is transmitted. If you set the Sequence Engine Done event output behavior to EventOutputBehavior.TOGGLE, the output level toggles between low and high. The default value is EventOutputBehavior.PULSE.

    Note:
    This property is not supported by all output terminals.
    This property is not supported on all devices. For more information about supported devices and terminals, search Supported Properties by Device on ni.com.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].sequence_engine_done_event_output_behavior`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.sequence_engine_done_event_output_behavior`
    '''
    sequence_engine_done_event_output_terminal = _attributes.AttributeViString(1150050)
    '''Type: str

    Specifies the output terminal for exporting the Sequence Engine Done Complete event.
    Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].sequence_engine_done_event_output_terminal`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.sequence_engine_done_event_output_terminal`
    '''
    sequence_engine_done_event_pulse_polarity = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.Polarity, 1150048)
    '''Type: enums.Polarity

    Specifies the behavior of the Sequence Engine Done event.
    Default Value: Polarity.HIGH

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].sequence_engine_done_event_pulse_polarity`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.sequence_engine_done_event_pulse_polarity`
    '''
    sequence_engine_done_event_pulse_width = _attributes.AttributeViReal64(1150049)
    '''Type: float

    Specifies the width of the Sequence Engine Done event, in seconds.
    The minimum event pulse width value for PXI devices is 150 ns, and the minimum event pulse width value for PXI Express devices is 250 ns.
    The maximum event pulse width value for all devices is 1.6 microseconds.
    Valid Values: 1.5e-7 to 1.6e-6 seconds
    Default Value: The default value for PXI devices is 150 ns. The default value for PXI Express devices is 250 ns.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].sequence_engine_done_event_pulse_width`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.sequence_engine_done_event_pulse_width`
    '''
    sequence_engine_done_event_toggle_initial_state = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.EventToggleInitialState, 1150346)
    '''Type: enums.EventToggleInitialState

    Specifies the initial state of the Sequence Engine Done event when you set the sequence_engine_done_event_output_behavior property to EventOutputBehavior.TOGGLE.
    For a Single Point mode acquisition, if you set the initial state to NIDCPOWER_VAL_LOW_STATE, the output is set to low at session commit.
    The output switches to high when the event occurs during the acquisition. If you set the initial state to NIDCPOWER_VAL_HIGH_STATE, the output is set to a high state at session commit.
    The output switches to low when the event occurs during the acquisition.
    For a Sequence mode operation, if you set the initial state to NIDCPOWER_VAL_LOW_STATE, the output is set to low at session commit. The output switches to high the first time an event occurs during the acquisition.
    The second time an event occurs, the output switches to low. This pattern repeats for any subsequent event occurrences.
    If you set the initial state to NIDCPOWER_VAL_HIGH_STATE, the output is set to high at session commit.
    The output switches to low on the first time the event occurs during the acquisition. The second time the event occurs, the output switches to high.
    This pattern repeats for any subsequent event occurrences.
    The default value is NIDCPOWER_VAL_LOW_STATE.

    Note:
    This property is not supported on all devices. For more information about supported devices and terminals, search Supported Properties by Device on ni.com

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].sequence_engine_done_event_toggle_initial_state`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.sequence_engine_done_event_toggle_initial_state`
    '''
    sequence_iteration_complete_event_output_behavior = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.EventOutputBehavior, 1150335)
    '''Type: enums.EventOutputBehavior

    Determines the event type's behavior when a corresponding trigger is received. If you set the Sequence Iteration Complete event output behavior to EventOutputBehavior.PULSE, a single pulse is transmitted. If you set the Sequence Iteration Complete event output behavior to EventOutputBehavior.TOGGLE, the output level toggles between low and high. The default value is EventOutputBehavior.PULSE.

    Note:
    This property is not supported by all output terminals.
    This property is not supported on all devices. For more information about supported devices and terminals, search Supported Properties by Device on ni.com.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].sequence_iteration_complete_event_output_behavior`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.sequence_iteration_complete_event_output_behavior`
    '''
    sequence_iteration_complete_event_output_terminal = _attributes.AttributeViString(1150040)
    '''Type: str

    Specifies the output terminal for exporting the Sequence Iteration Complete event.
    Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].sequence_iteration_complete_event_output_terminal`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.sequence_iteration_complete_event_output_terminal`
    '''
    sequence_iteration_complete_event_pulse_polarity = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.Polarity, 1150038)
    '''Type: enums.Polarity

    Specifies the behavior of the Sequence Iteration Complete event.
    Default Value: Polarity.HIGH

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].sequence_iteration_complete_event_pulse_polarity`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.sequence_iteration_complete_event_pulse_polarity`
    '''
    sequence_iteration_complete_event_pulse_width = _attributes.AttributeViReal64(1150039)
    '''Type: float

    Specifies the width of the Sequence Iteration Complete event, in seconds.
    The minimum event pulse width value for PXI devices is 150 ns, and the minimum event pulse width value for PXI Express devices is 250 ns.
    The maximum event pulse width value for all devices is 1.6 microseconds.
    the NI DC Power Supplies and SMUs Help for information about supported devices.
    Valid Values: 1.5e-7 to 1.6e-6 seconds
    Default Value: The default value for PXI devices is 150 ns. The default value for PXI Express devices is 250 ns.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].sequence_iteration_complete_event_pulse_width`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.sequence_iteration_complete_event_pulse_width`
    '''
    sequence_iteration_complete_event_toggle_initial_state = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.EventToggleInitialState, 1150336)
    '''Type: enums.EventToggleInitialState

    Specifies the initial state of the Sequence Iteration Complete event when you set the sequence_iteration_complete_event_output_behavior property to EventOutputBehavior.TOGGLE.
    For a Single Point mode acquisition, if you set the initial state to NIDCPOWER_VAL_LOW_STATE, the output is set to low at session commit.
    The output switches to high when the event occurs during the acquisition. If you set the initial state to NIDCPOWER_VAL_HIGH_STATE, the output is set to a high state at session commit.
    The output switches to low when the event occurs during the acquisition.
    For a Sequence mode operation, if you set the initial state to NIDCPOWER_VAL_LOW_STATE, the output is set to low at session commit. The output switches to high the first time an event occurs during the acquisition.
    The second time an event occurs, the output switches to low. This pattern repeats for any subsequent event occurrences.
    If you set the initial state to NIDCPOWER_VAL_HIGH_STATE, the output is set to high at session commit.
    The output switches to low on the first time the event occurs during the acquisition. The second time the event occurs, the output switches to high.
    This pattern repeats for any subsequent event occurrences.
    The default value is NIDCPOWER_VAL_LOW_STATE.

    Note:
    This property is not supported on all devices. For more information about supported devices and terminals, search Supported Properties by Device on ni.com

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].sequence_iteration_complete_event_toggle_initial_state`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.sequence_iteration_complete_event_toggle_initial_state`
    '''
    sequence_loop_count = _attributes.AttributeViInt32(1150025)
    '''Type: int

    Specifies the number of times a sequence is run after initiation.
    Refer to the Sequence Source Mode topic in the NI DC Power Supplies and SMUs Help for more information about the sequence loop count.
    When the sequence_loop_count_is_finite property is set to False, the sequence_loop_count property is ignored.
    Valid Range: 1 to 2147483647
    Default Value: 1

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].sequence_loop_count`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.sequence_loop_count`
    '''
    sequence_loop_count_is_finite = _attributes.AttributeViBoolean(1150078)
    '''Type: bool

    Specifies whether a sequence should repeat indefinitely.
    Refer to the Sequence Source Mode topic in the NI DC Power Supplies and SMUs Help for more information about infinite sequencing.
    When the sequence_loop_count_is_finite property is set to False, the sequence_loop_count property is ignored.
    Default Value: True

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].sequence_loop_count_is_finite`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.sequence_loop_count_is_finite`
    '''
    sequence_step_delta_time = _attributes.AttributeViReal64(1150198)
    '''Type: float

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].sequence_step_delta_time`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.sequence_step_delta_time`
    '''
    sequence_step_delta_time_enabled = _attributes.AttributeViBoolean(1150199)
    '''Type: bool

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].sequence_step_delta_time_enabled`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.sequence_step_delta_time_enabled`
    '''
    serial_number = _attributes.AttributeViString(1150152)
    '''Type: str

    Contains the serial number for the device you are currently using.

    Tip:
    This property can be set/get on specific instruments within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container instruments to specify a subset.

    Example: :py:attr:`my_session.instruments[ ... ].serial_number`

    To set/get on all instruments, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.serial_number`
    '''
    shutdown_trigger_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.TriggerType, 1150275)
    '''Type: enums.TriggerType

    Specifies the behavior of the Shutdown trigger.
    Default Value: TriggerType.NONE

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].shutdown_trigger_type`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.shutdown_trigger_type`
    '''
    simulate = _attributes.AttributeViBoolean(1050005)
    '''Type: bool

    Specifies whether to simulate NI-DCPower I/O operations. True specifies that operation is simulated.
    Default Value: False
    '''
    source_complete_event_output_behavior = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.EventOutputBehavior, 1150331)
    '''Type: enums.EventOutputBehavior

    Determines the event type's behavior when a corresponding trigger is received. If you set the Source Complete event output behavior to EventOutputBehavior.PULSE, a single pulse is transmitted. If you set the Source Complete event output behavior to EventOutputBehavior.TOGGLE, the output level toggles between low and high. The default value is EventOutputBehavior.PULSE.

    Note:
    This property is not supported by all output terminals.
    This property is not supported on all devices. For more information about supported devices and terminals, search Supported Properties by Device on ni.com.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].source_complete_event_output_behavior`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.source_complete_event_output_behavior`
    '''
    source_complete_event_output_terminal = _attributes.AttributeViString(1150043)
    '''Type: str

    Specifies the output terminal for exporting the Source Complete event.
    Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].source_complete_event_output_terminal`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.source_complete_event_output_terminal`
    '''
    source_complete_event_pulse_polarity = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.Polarity, 1150041)
    '''Type: enums.Polarity

    Specifies the behavior of the Source Complete event.
    Default Value: Polarity.HIGH

    Note:
    NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].source_complete_event_pulse_polarity`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.source_complete_event_pulse_polarity`
    '''
    source_complete_event_pulse_width = _attributes.AttributeViReal64(1150042)
    '''Type: float

    Specifies the width of the Source Complete event, in seconds.
    The minimum event pulse width value for PXI devices is 150 ns, and the minimum event pulse width value for PXI Express devices is 250 ns.
    The maximum event pulse width value for all devices is 1.6 microseconds
    Valid Values: 1.5e-7 to 1.6e-6 seconds
    Default Value: The default value for PXI devices is 150 ns. The default value for PXI Express devices is 250 ns.

    Note:
    NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].source_complete_event_pulse_width`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.source_complete_event_pulse_width`
    '''
    source_complete_event_toggle_initial_state = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.EventToggleInitialState, 1150332)
    '''Type: enums.EventToggleInitialState

    Specifies the initial state of the Source Complete event when you set the source_complete_event_output_behavior property to EventOutputBehavior.TOGGLE.
    For a Single Point mode acquisition, if you set the initial state to NIDCPOWER_VAL_LOW_STATE, the output is set to low at session commit.
    The output switches to high when the event occurs during the acquisition. If you set the initial state to NIDCPOWER_VAL_HIGH_STATE, the output is set to a high state at session commit.
    The output switches to low when the event occurs during the acquisition.
    For a Sequence mode operation, if you set the initial state to NIDCPOWER_VAL_LOW_STATE, the output is set to low at session commit. The output switches to high the first time an event occurs during the acquisition.
    The second time an event occurs, the output switches to low. This pattern repeats for any subsequent event occurrences.
    If you set the initial state to NIDCPOWER_VAL_HIGH_STATE, the output is set to high at session commit.
    The output switches to low on the first time the event occurs during the acquisition. The second time the event occurs, the output switches to high.
    This pattern repeats for any subsequent event occurrences.
    The default value is NIDCPOWER_VAL_LOW_STATE.

    Note:
    NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

    This property is not supported on all devices. For more information about supported devices and terminals, search Supported Properties by Device on ni.com

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].source_complete_event_toggle_initial_state`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.source_complete_event_toggle_initial_state`
    '''
    source_delay = _attributes.AttributeViReal64TimeDeltaSeconds(1150051)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    Determines when, in seconds, the device generates the Source Complete event, potentially starting a measurement if the measure_when property is set to MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE.
    Refer to the Single Point Source Mode and Sequence Source Mode topics for more information.
    Valid Values: The PXIe-4051 supports values from 0 to 39 seconds.
    The PXIe-4147 supports values from 0 to 26.5 seconds.
    The PXIe-4151 supports values from 0 to 42 seconds.
    The PXIe-4162/4163 and PXIe-4190 support values from 0 to 23 seconds.
    All other supported instruments support values from 0 to 167 seconds.
    Default Value: 0.01667 seconds

    Note:
    NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].source_delay`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.source_delay`
    '''
    source_mode = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.SourceMode, 1150054)
    '''Type: enums.SourceMode

    Specifies whether to run a single output point or a sequence. Refer to the Single Point Source Mode and Sequence Source Mode topics in the NI DC Power Supplies and SMUs Help for more information about source modes.
    Default value: SourceMode.SINGLE_POINT

    Note:
    NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].source_mode`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.source_mode`
    '''
    source_trigger_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.TriggerType, 1150030)
    '''Type: enums.TriggerType

    Specifies the behavior of the Source trigger.
    Default Value: TriggerType.NONE

    Note:
    NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].source_trigger_type`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.source_trigger_type`
    '''
    specific_driver_description = _attributes.AttributeViString(1050514)
    '''Type: str

    Contains a brief description of the specific driver.
    '''
    specific_driver_prefix = _attributes.AttributeViString(1050302)
    '''Type: str

    Contains the prefix for NI-DCPower. The name of each user-callable method in NI-DCPower begins with this prefix.
    '''
    specific_driver_revision = _attributes.AttributeViString(1050551)
    '''Type: str

    Contains additional version information about NI-DCPower.
    '''
    specific_driver_vendor = _attributes.AttributeViString(1050513)
    '''Type: str

    Contains the name of the vendor that supplies NI-DCPower.
    '''
    start_trigger_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.TriggerType, 1150021)
    '''Type: enums.TriggerType

    Specifies the behavior of the Start trigger.
    Default Value: TriggerType.NONE

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].start_trigger_type`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.start_trigger_type`
    '''
    supported_instrument_models = _attributes.AttributeViString(1050327)
    '''Type: str

    Contains a comma-separated (,) list of supported NI-DCPower device models.
    '''
    transient_response = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.TransientResponse, 1150062)
    '''Type: enums.TransientResponse

    Specifies the transient response. Refer to the Transient Response topic in the NI DC Power Supplies and SMUs Help for more information about transient response.
    Default Value: TransientResponse.NORMAL

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].transient_response`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.transient_response`
    '''
    voltage_compensation_frequency = _attributes.AttributeViReal64(1150068)
    '''Type: float

    The frequency at which a pole-zero pair is added to the system when the channel is in Constant Voltage mode.
    Default value: Determined by the value of the TransientResponse.NORMAL setting of the transient_response property.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].voltage_compensation_frequency`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.voltage_compensation_frequency`
    '''
    voltage_gain_bandwidth = _attributes.AttributeViReal64(1150067)
    '''Type: float

    The frequency at which the unloaded loop gain extrapolates to 0 dB in the absence of additional poles and zeroes. This property takes effect when the channel is in Constant Voltage mode.
    Default Value: Determined by the value of the TransientResponse.NORMAL setting of the transient_response property.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].voltage_gain_bandwidth`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.voltage_gain_bandwidth`
    '''
    voltage_level = _attributes.AttributeViReal64(1250001)
    '''Type: float

    Specifies the voltage level, in volts, that the device attempts to generate on the specified channel(s).
    This property is applicable only if the output_function property is set to OutputFunction.DC_VOLTAGE.

    Valid Values: The valid values for this property are defined by the values you specify for the voltage_level_range property.

    Note: The channel must be enabled for the specified voltage level to take effect. Refer to the output_enabled property for more information about enabling the channel.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].voltage_level`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.voltage_level`
    '''
    voltage_level_autorange = _attributes.AttributeViInt32(1150015)
    '''Type: bool

    Specifies whether NI-DCPower automatically selects the voltage level range based on the desired voltage level for the specified channel(s).
    If you set this property to AutoZero.ON, NI-DCPower ignores any changes you make to the voltage_level_range property. If you change the voltage_level_autorange property from AutoZero.ON to AutoZero.OFF, NI-DCPower retains the last value the voltage_level_range property was set to (or the default value if the property was never set) and uses that value as the voltage level range.
    Query the voltage_level_range property by using the _get_attribute_vi_int32 method for information about which range NI-DCPower automatically selects.
    The voltage_level_autorange property is applicable only if the output_function property is set to OutputFunction.DC_VOLTAGE.
    Default Value: AutoZero.OFF

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].voltage_level_autorange`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.voltage_level_autorange`
    '''
    voltage_level_range = _attributes.AttributeViReal64(1150005)
    '''Type: float

    Specifies the voltage level range, in volts, for the specified channel(s).
    The range defines the valid values to which the voltage level can be set. Use the voltage_level_autorange property to enable automatic selection of the voltage level range.
    The voltage_level_range property is applicable only if the output_function property is set to OutputFunction.DC_VOLTAGE.

    For valid ranges, refer to the specifications for your instrument.

    Note: The channel must be enabled for the specified voltage level range to take effect. Refer to the output_enabled property for more information about enabling the channel.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].voltage_level_range`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.voltage_level_range`
    '''
    voltage_limit = _attributes.AttributeViReal64(1150010)
    '''Type: float

    Specifies the voltage limit, in volts, that the output cannot exceed when generating the desired current level on the specified channels.
    This property is applicable only if the output_function property is set to OutputFunction.DC_CURRENT and the compliance_limit_symmetry property is set to ComplianceLimitSymmetry.SYMMETRIC.

    Valid Values: The valid values for this property are defined by the values to which the voltage_limit_range property is set.

    Note: The channel must be enabled for the specified current level to take effect. Refer to the output_enabled property for more information about enabling the channel.

    NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].voltage_limit`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.voltage_limit`
    '''
    voltage_limit_autorange = _attributes.AttributeViInt32(1150018)
    '''Type: bool

    Specifies whether NI-DCPower automatically selects the voltage limit range based on the desired voltage limit for the specified channel(s).
    If this property is set to AutoZero.ON, NI-DCPower ignores any changes you make to the voltage_limit_range property. If you change the voltage_limit_autorange property from AutoZero.ON to AutoZero.OFF, NI-DCPower retains the last value the voltage_limit_range property was set to (or the default value if the property was never set) and uses that value as the voltage limit range.
    Query the voltage_limit_range property by using the _get_attribute_vi_int32 method to find out which range NI-DCPower automatically selects.
    The voltage_limit_autorange property is applicable only if the output_function property is set to OutputFunction.DC_CURRENT.
    Default Value: AutoZero.OFF

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].voltage_limit_autorange`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.voltage_limit_autorange`
    '''
    voltage_limit_high = _attributes.AttributeViReal64(1150185)
    '''Type: float

    Specifies the maximum voltage, in volts, that the output can produce
    when generating the desired current on the specified channel(s).
    This property is applicable only if the compliance_limit_symmetry property is set to
    ComplianceLimitSymmetry.ASYMMETRIC and the output_function property is set to OutputFunction.DC_CURRENT.
    You must also specify a voltage_limit_low to complete the asymmetric
    range.
    **Valid Values:** [1% of voltage_limit_range, voltage_limit_range]
    The range bounded by the limit high and limit low must include zero.
    **Default Value:** Search ni.com for Supported Properties by Device for the default value by device.
    **Related Topics:**
    Ranges;
    Changing Ranges;
    Overranging

    Note:
    The limit may be extended beyond the selected limit range if the
    overranging_enabled property is
    set to True.

    NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].voltage_limit_high`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.voltage_limit_high`
    '''
    voltage_limit_low = _attributes.AttributeViReal64(1150186)
    '''Type: float

    Specifies the minimum voltage, in volts, that the output can produce
    when generating the desired current on the specified channel(s).
    This property is applicable only if the compliance_limit_symmetry property is set to
    ComplianceLimitSymmetry.ASYMMETRIC and the output_function property is set to OutputFunction.DC_CURRENT.
    You must also specify a voltage_limit_high to complete the asymmetric
    range.
    **Valid Values:** [-voltage_limit_range, -1% of voltage_limit_range]
    The range bounded by the limit high and limit low must include zero.
    **Default Value:** Search ni.com for Supported Properties by Device for the default value by device.
    **Related Topics:**
    Ranges;
    Changing Ranges;
    Overranging

    Note:
    The limit may be extended beyond the selected limit range if the
    overranging_enabled property is
    set to True.

    NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].voltage_limit_low`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.voltage_limit_low`
    '''
    voltage_limit_range = _attributes.AttributeViReal64(1150012)
    '''Type: float

    Specifies the voltage limit range, in volts, for the specified channel(s).
    The range defines the valid values to which the voltage limit can be set. Use the voltage_limit_autorange property to enable automatic selection of the voltage limit range.
    The voltage_limit_range property is applicable only if the output_function property is set to OutputFunction.DC_CURRENT.

    For valid ranges, refer to the specifications for your instrument.

    Note: The channel must be enabled for the specified voltage limit range to take effect. Refer to the output_enabled property for more information about enabling the channel.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].voltage_limit_range`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.voltage_limit_range`
    '''
    voltage_pole_zero_ratio = _attributes.AttributeViReal64(1150069)
    '''Type: float

    The ratio of the pole frequency to the zero frequency when the channel is in Constant Voltage mode.
    Default value: Determined by the value of the TransientResponse.NORMAL setting of the transient_response property.

    Note:
    This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].voltage_pole_zero_ratio`

    To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

    Example: :py:attr:`my_session.voltage_pole_zero_ratio`
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
        self.instruments = _RepeatedCapabilities(self, '', repeated_capability_list)

        # Finally, set _is_frozen to True which is used to prevent clients from accidentally adding
        # members when trying to set a property with a typo.
        self._is_frozen = freeze_it

    def __repr__(self):
        return '{0}.{1}({2})'.format('nidcpower', self.__class__.__name__, self._param_list)

    def __setattr__(self, key, value):
        if self._is_frozen and key not in dir(self):
            raise AttributeError("'{0}' object has no attribute '{1}'".format(type(self).__name__, key))
        object.__setattr__(self, key, value)

    def initiate(self):
        '''initiate

        Starts generation or acquisition, causing the specified channel(s) to
        leave the Uncommitted state or Committed state and enter the Running
        state. To return to the Uncommitted state call the abort
        method. Refer to the `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic in
        the *NI DC Power Supplies and SMUs Help* for information about the
        specific NI-DCPower software states.

        **Related Topics:**

        `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

        Note:
        This method will return a Python context manager that will initiate on entering and abort on exit.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].initiate`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.initiate`
        '''
        return _Acquisition(self)

    ''' These are code-generated '''

    @ivi_synchronized
    def abort(self):
        r'''abort

        Transitions the specified channel(s) from the Running state to the
        Uncommitted state. If a sequence is running, it is stopped. Any
        configuration methods called after this method are not applied until
        the initiate method is called. If power output is enabled
        when you call the abort method, the channels remain
        in their current state and continue providing power.

        Use the ConfigureOutputEnabled method to disable power
        output on a per channel basis. Use the reset method to
        disable output on all channels.

        Refer to the `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic in
        the *NI DC Power Supplies and SMUs Help* for information about the
        specific NI-DCPower software states.

        **Related Topics:**

        `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

        Note:
        NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

        Note:
        One or more of the referenced methods are not in the Python API for this driver.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].abort`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.abort`
        '''
        self._interpreter.abort(self._repeated_capability)

    @ivi_synchronized
    def self_cal(self):
        r'''self_cal

        Performs a self-calibration upon the specified channel(s).

        This method disables the output, performs several internal
        calculations, and updates calibration values. The updated calibration
        values are written to the device hardware if the
        self_calibration_persistence property is set to
        SelfCalibrationPersistence.WRITE_TO_EEPROM. Refer to the
        self_calibration_persistence property topic for more
        information about the settings for this property.

        When calling self_cal with the PXIe-4162/4163,
        specify all channels of your PXIe-4162/4163 with the channelName input.
        You cannot self-calibrate a subset of PXIe-4162/4163 channels.

        Refer to the
        `Self-Calibration <REPLACE_DRIVER_SPECIFIC_URL_1(selfcal)>`__ topic for
        more information about this method.

        **Related Topics:**

        `Self-Calibration <REPLACE_DRIVER_SPECIFIC_URL_1(selfcal)>`__

        Note:
        NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].self_cal`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.self_cal`
        '''
        self._interpreter.self_cal(self._repeated_capability)

    @ivi_synchronized
    def clear_latched_output_cutoff_state(self, output_cutoff_reason):
        r'''clear_latched_output_cutoff_state

        Clears the state of an output cutoff that was engaged.
        To clear the state for all output cutoff reasons, use OutputCutoffReason.ALL.

        Note:
        NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].clear_latched_output_cutoff_state`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.clear_latched_output_cutoff_state`

        Args:
            output_cutoff_reason (enums.OutputCutoffReason): Specifies the reasons for which to clear the output cutoff state.

                +-----------------------------------------+-----------------------------------------------------------------------------------------------------------------+
                | OutputCutoffReason.ALL                  | Clears all output cutoff conditions                                                                             |
                +-----------------------------------------+-----------------------------------------------------------------------------------------------------------------+
                | OutputCutoffReason.VOLTAGE_OUTPUT_HIGH  | Clears cutoffs caused when the output exceeded the high cutoff limit for voltage output                         |
                +-----------------------------------------+-----------------------------------------------------------------------------------------------------------------+
                | OutputCutoffReason.VOLTAGE_OUTPUT_LOW   | Clears cutoffs caused when the output fell below the low cutoff limit for voltage output                        |
                +-----------------------------------------+-----------------------------------------------------------------------------------------------------------------+
                | OutputCutoffReason.VOLTAGE_MEASURE_HIGH | Clears cutoffs caused when the measured voltage exceeded the high cutoff limit for voltage output               |
                +-----------------------------------------+-----------------------------------------------------------------------------------------------------------------+
                | OutputCutoffReason.VOLTAGE_MEASURE_LOW  | Clears cutoffs caused when the measured voltage fell below the low cutoff limit for voltage output              |
                +-----------------------------------------+-----------------------------------------------------------------------------------------------------------------+
                | OutputCutoffReason.CURRENT_MEASURE_HIGH | Clears cutoffs caused when the measured current exceeded the high cutoff limit for current output               |
                +-----------------------------------------+-----------------------------------------------------------------------------------------------------------------+
                | OutputCutoffReason.CURRENT_MEASURE_LOW  | Clears cutoffs caused when the measured current fell below the low cutoff limit for current output              |
                +-----------------------------------------+-----------------------------------------------------------------------------------------------------------------+
                | OutputCutoffReason.VOLTAGE_CHANGE_HIGH  | Clears cutoffs caused when the voltage slew rate increased beyond the positive change cutoff for voltage output |
                +-----------------------------------------+-----------------------------------------------------------------------------------------------------------------+
                | OutputCutoffReason.VOLTAGE_CHANGE_LOW   | Clears cutoffs caused when the voltage slew rate decreased beyond the negative change cutoff for voltage output |
                +-----------------------------------------+-----------------------------------------------------------------------------------------------------------------+
                | OutputCutoffReason.CURRENT_CHANGE_HIGH  | Clears cutoffs caused when the current slew rate increased beyond the positive change cutoff for current output |
                +-----------------------------------------+-----------------------------------------------------------------------------------------------------------------+
                | OutputCutoffReason.CURRENT_CHANGE_LOW   | Clears cutoffs caused when the voltage slew rate decreased beyond the negative change cutoff for current output |
                +-----------------------------------------+-----------------------------------------------------------------------------------------------------------------+
                | OutputCutoffReason.CURRENT_SATURATED    | Clears cutoffs caused when the measured current saturates the current range                                     |
                +-----------------------------------------+-----------------------------------------------------------------------------------------------------------------+

        '''
        if type(output_cutoff_reason) is not enums.OutputCutoffReason:
            raise TypeError('Parameter output_cutoff_reason must be of type ' + str(enums.OutputCutoffReason))
        self._interpreter.clear_latched_output_cutoff_state(self._repeated_capability, output_cutoff_reason)

    @ivi_synchronized
    def commit(self):
        r'''commit

        Applies previously configured settings to the specified channel(s). Calling this
        method moves the NI-DCPower session from the Uncommitted state into
        the Committed state. After calling this method, modifying any
        property reverts the NI-DCPower session to the Uncommitted state. Use
        the initiate method to transition to the Running state.
        Refer to the `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic in
        the *NI DC Power Supplies and SMUs Help* for details about the specific
        NI-DCPower software states.

        **Related Topics:**

        `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].commit`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.commit`
        '''
        self._interpreter.commit(self._repeated_capability)

    @ivi_synchronized
    def configure_aperture_time(self, aperture_time, units=enums.ApertureTimeUnits.SECONDS):
        r'''configure_aperture_time

        Configures the aperture time on the specified channel(s).

        The supported values depend on the **units**. Refer to the *Aperture
        Time* topic for your device in the *NI DC Power Supplies and SMUs Help*
        for more information. In general, devices support discrete
        **apertureTime** values, and if you configure **apertureTime** to some
        unsupported value, NI-DCPower coerces it up to the next supported value.

        Refer to the *Measurement Configuration and Timing* or *DC Noise
        Rejection* topic for your device in the *NI DC Power Supplies and SMUs
        Help* for more information about how to configure your measurements.

        **Related Topics:**

        `Aperture Time <REPLACE_DRIVER_SPECIFIC_URL_1(aperture)>`__

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].configure_aperture_time`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.configure_aperture_time`

        Args:
            aperture_time (float): Specifies the aperture time. Refer to the *Aperture Time* topic for your
                device in the *NI DC Power Supplies and SMUs Help* for more information.

            units (enums.ApertureTimeUnits): Specifies the units for **apertureTime**.
                **Defined Values**:

                +-------------------------------------+------------------------------+
                | ApertureTimeUnits.SECONDS           | Specifies seconds.           |
                +-------------------------------------+------------------------------+
                | ApertureTimeUnits.POWER_LINE_CYCLES | Specifies Power Line Cycles. |
                +-------------------------------------+------------------------------+

        '''
        if type(units) is not enums.ApertureTimeUnits:
            raise TypeError('Parameter units must be of type ' + str(enums.ApertureTimeUnits))
        self._interpreter.configure_aperture_time(self._repeated_capability, aperture_time, units)

    @ivi_synchronized
    def configure_lcr_compensation(self, compensation_data):
        r'''configure_lcr_compensation

        Applies previously generated open, short, load, as well as open and short custom cable compensation data to LCR measurements.

        This method applies open, short and load compensation data when you have set the lcr_open_short_load_compensation_data_source property to LCROpenShortLoadCompensationDataSource.AS_CONFIGURED, and it also applies custom cable compensation data when you have set the cable_length property to CableLength.CUSTOM_AS_CONFIGURED.

        Call this method after you have obtained LCR compensation data.

        If the lcr_short_custom_cable_compensation_enabled property is set to True, you must generate data with both perform_lcr_open_custom_cable_compensation and perform_lcr_short_custom_cable_compensation; if False, you must only use perform_lcr_open_custom_cable_compensation, and NI-DCPower uses default short data.

        Call get_lcr_compensation_data and pass the **compensation data** to this method.

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].configure_lcr_compensation`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.configure_lcr_compensation`

        Args:
            compensation_data (bytes): The open, short and load compensation data to apply.

        '''
        compensation_data = _converters.convert_to_bytes(compensation_data)
        self._interpreter.configure_lcr_compensation(self._repeated_capability, compensation_data)

    @ivi_synchronized
    def configure_lcr_custom_cable_compensation(self, custom_cable_compensation_data):
        r'''configure_lcr_custom_cable_compensation

        This method is deprecated. Use configure_lcr_compensation
        instead.

        Applies previously generated open and short custom cable compensation data to LCR measurements.

        This method applies custom cable compensation data when you have set cable_length property to CableLength.CUSTOM_AS_CONFIGURED.

        Call this method after you have obtained custom cable compensation data.

        If lcr_short_custom_cable_compensation_enabled property is set to True, you must generate data with both perform_lcr_open_custom_cable_compensation and perform_lcr_short_custom_cable_compensation;
        if False, you must only use perform_lcr_open_custom_cable_compensation, and NI-DCPower uses default short data.

        Call get_lcr_custom_cable_compensation_data and pass the **custom cable compensation data** to this method.

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].configure_lcr_custom_cable_compensation`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.configure_lcr_custom_cable_compensation`

        Args:
            custom_cable_compensation_data (bytes): The open and short custom cable compensation data to apply.

        '''
        custom_cable_compensation_data = _converters.convert_to_bytes(custom_cable_compensation_data)
        self._interpreter.configure_lcr_custom_cable_compensation(self._repeated_capability, custom_cable_compensation_data)

    @ivi_synchronized
    def create_advanced_sequence_commit_step(self, set_as_active_step=True):
        r'''create_advanced_sequence_commit_step

        Creates a Commit step in the Active advanced sequence. A Commit step
        configures channels to a user-defined known state before starting the advanced sequence.
        When a Commit step exists in the Active advanced sequence, you cannot
        set the output method to Pulse Voltage or Pulse Current in either
        the Commit step (-1) or step 0. When you create an advanced sequence
        step, each property you passed to the create_advanced_sequence
        method is reset to its default value for that step unless otherwise specified.

        **Support for this Method**

        You must set the source mode to Sequence to use this method.

        Using the set_sequence method with Advanced Sequence
        methods is unsupported.

        **Related Topics**:

        `Advanced Sequence
        Mode <REPLACE_DRIVER_SPECIFIC_URL_1(advancedsequencemode)>`__

        `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

        create_advanced_sequence

        Note:
        NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].create_advanced_sequence_commit_step`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.create_advanced_sequence_commit_step`

        Args:
            set_as_active_step (bool): Specifies whether the step created with this method is active in the Active advanced sequence.

        '''
        self._interpreter.create_advanced_sequence_commit_step(self._repeated_capability, set_as_active_step)

    @ivi_synchronized
    def create_advanced_sequence_step(self, set_as_active_step=True):
        r'''create_advanced_sequence_step

        Creates a new advanced sequence step in the advanced sequence specified
        by the Active advanced sequence. When you create an advanced sequence
        step, each property you passed to the create_advanced_sequence
        method is reset to its default value for that step unless otherwise
        specified.

        **Support for this Method**

        You must set the source mode to Sequence to use this method.

        Using the set_sequence method with Advanced Sequence
        methods is unsupported.

        **Related Topics**:

        `Advanced Sequence
        Mode <REPLACE_DRIVER_SPECIFIC_URL_1(advancedsequencemode)>`__

        `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

        create_advanced_sequence

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].create_advanced_sequence_step`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.create_advanced_sequence_step`

        Args:
            set_as_active_step (bool): Specifies whether the step created with this method is active in the Active advanced sequence.

        '''
        self._interpreter.create_advanced_sequence_step(self._repeated_capability, set_as_active_step)

    @ivi_synchronized
    def _create_advanced_sequence_with_channels(self, sequence_name, attribute_ids, set_as_active_sequence):
        r'''_create_advanced_sequence_with_channels

        Creates an empty advanced sequence. Call the
        create_advanced_sequence_step method to add steps to the
        active advanced sequence.

        You can create multiple advanced sequences for a channel.

        **Support for this method**

        You must set the source mode to Sequence to use this method.

        Using the set_sequence method with Advanced Sequence
        methods is unsupported.

        Use this method in the Uncommitted or Committed programming states.
        Refer to the `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic in
        the *NI DC Power Supplies and SMUs Help* for more information about
        NI-DCPower programming states.

        **Related Topics**:

        `Advanced Sequence
        Mode <REPLACE_DRIVER_SPECIFIC_URL_1(advancedsequencemode)>`__

        `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

        create_advanced_sequence_step

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._create_advanced_sequence_with_channels`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session._create_advanced_sequence_with_channels`

        Args:
            sequence_name (str): Specifies the name of the sequence to create.

            attribute_ids (list of int): Specifies the properties you reconfigure per step in the advanced
                sequence. For more information about which properties can be configured
                in an advanced sequence for each NI-DCPower device that supports advanced
                sequencing, search ni.com for Supported Properties by Device.

            set_as_active_sequence (bool): Specifies that this current sequence is active.

        '''
        self._interpreter.create_advanced_sequence_with_channels(self._repeated_capability, sequence_name, attribute_ids, set_as_active_sequence)

    @ivi_synchronized
    def delete_advanced_sequence(self, sequence_name):
        r'''delete_advanced_sequence

        Deletes a previously created advanced sequence and all the advanced
        sequence steps in the advanced sequence.

        **Support for this Method**

        You must set the source mode to Sequence to use this method.

        Using the set_sequence method with Advanced Sequence
        methods is unsupported.

        **Related Topics**:

        `Advanced Sequence
        Mode <REPLACE_DRIVER_SPECIFIC_URL_1(advancedsequencemode)>`__

        `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].delete_advanced_sequence`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.delete_advanced_sequence`

        Args:
            sequence_name (str): specifies the name of the sequence to delete.

        '''
        self._interpreter.delete_advanced_sequence(self._repeated_capability, sequence_name)

    @ivi_synchronized
    def create_advanced_sequence(self, sequence_name, property_names, set_as_active_sequence=True):
        '''create_advanced_sequence

        Creates an empty advanced sequence. Call the
        create_advanced_sequence_step method to add steps to the
        active advanced sequence.

        You can create multiple advanced sequences in a session.

        **Support for this method**

        You must set the source mode to Sequence to use this method.

        Using the set_sequence method with Advanced Sequence
        methods is unsupported.

        Use this method in the Uncommitted or Committed programming states.
        Refer to the `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic in
        the *NI DC Power Supplies and SMUs Help* for more information about
        NI-DCPower programming states.

        **Related Topics**:

        `Advanced Sequence
        Mode <REPLACE_DRIVER_SPECIFIC_URL_1(advancedsequencemode)>`__

        `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

        create_advanced_sequence_step

        Note:
        This method is not supported on all devices. Refer to `Supported
        Methods by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].create_advanced_sequence`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.create_advanced_sequence`

        Args:
            sequence_name (str): Specifies the name of the sequence to create.

            property_names (list of str): Specifies the names of the properties you reconfigure per step in the advanced sequence. The following table lists which properties can be configured in an advanced sequence for each NI-DCPower device that supports advanced sequencing. A Yes indicates that the property can be configured in advanced sequencing. An No indicates that the property cannot be configured in advanced sequencing.

                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | Property                       | PXIe-4135 | PXIe-4136 | PXIe-4137 | PXIe-4138 | PXIe-4139 | PXIe-4140/4142/4144 | PXIe-4141/4143/4145 | PXIe-4147 | PXIe-4162/4163 | PXIe-4190 |
                +================================+===========+===========+===========+===========+===========+=====================+=====================+===========+================+===========+
                | aperture_time                  | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes       | Yes            | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | dc_noise_rejection             | Yes       | No        | Yes       | No        | Yes       | No                  | No                  | Yes       | Yes            | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | instrument_mode                | No        | No        | No        | No        | No        | No                  | No                  | No        | No             | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | lcr_actual_load_reactance      | No        | No        | No        | No        | No        | No                  | No                  | No        | No             | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | lcr_actual_load_resistance     | No        | No        | No        | No        | No        | No                  | No                  | No        | No             | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | lcr_current_amplitude          | No        | No        | No        | No        | No        | No                  | No                  | No        | No             | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | lcr_current_range              | No        | No        | No        | No        | No        | No                  | No                  | No        | No             | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | lcr_custom_measurement_time    | No        | No        | No        | No        | No        | No                  | No                  | No        | No             | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | lcr_dc_bias_current_level      | No        | No        | No        | No        | No        | No                  | No                  | No        | No             | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | lcr_dc_bias_current_range      | No        | No        | No        | No        | No        | No                  | No                  | No        | No             | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | lcr_dc_bias_source             | No        | No        | No        | No        | No        | No                  | No                  | No        | No             | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | lcr_dc_bias_voltage_level      | No        | No        | No        | No        | No        | No                  | No                  | No        | No             | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | lcr_dc_bias_voltage_range      | No        | No        | No        | No        | No        | No                  | No                  | No        | No             | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | lcr_frequency                  | No        | No        | No        | No        | No        | No                  | No                  | No        | No             | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | lcr_impedance_auto_range       | No        | No        | No        | No        | No        | No                  | No                  | No        | No             | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | lcr_impedance_range            | No        | No        | No        | No        | No        | No                  | No                  | No        | No             | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | lcr_load_compensation_enabled  | No        | No        | No        | No        | No        | No                  | No                  | No        | No             | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | lcr_measured_load_reactance    | No        | No        | No        | No        | No        | No                  | No                  | No        | No             | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | lcr_measured_load_resistance   | No        | No        | No        | No        | No        | No                  | No                  | No        | No             | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | lcr_measurement_time           | No        | No        | No        | No        | No        | No                  | No                  | No        | No             | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | lcr_open_compensation_enabled  | No        | No        | No        | No        | No        | No                  | No                  | No        | No             | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | lcr_open_conductance           | No        | No        | No        | No        | No        | No                  | No                  | No        | No             | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | lcr_open_susceptance           | No        | No        | No        | No        | No        | No                  | No                  | No        | No             | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | lcr_short_compensation_enabled | No        | No        | No        | No        | No        | No                  | No                  | No        | No             | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | lcr_short_reactance            | No        | No        | No        | No        | No        | No                  | No                  | No        | No             | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | lcr_short_resistance           | No        | No        | No        | No        | No        | No                  | No                  | No        | No             | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | lcr_source_delay_mode          | No        | No        | No        | No        | No        | No                  | No                  | No        | No             | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | lcr_stimulus_function          | No        | No        | No        | No        | No        | No                  | No                  | No        | No             | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | lcr_voltage_amplitude          | No        | No        | No        | No        | No        | No                  | No                  | No        | No             | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | lcr_voltage_range              | No        | No        | No        | No        | No        | No                  | No                  | No        | No             | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | measure_record_length          | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes       | Yes            | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | sense                          | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes       | Yes            | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | ovp_enabled                    | Yes       | Yes       | Yes       | No        | No        | No                  | No                  | No        | No             | No        |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | ovp_limit                      | Yes       | Yes       | Yes       | No        | No        | No                  | No                  | No        | No             | No        |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | pulse_bias_delay               | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No        | No             | No        |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | pulse_off_time                 | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No        | No             | No        |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | pulse_on_time                  | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No        | No             | No        |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | source_delay                   | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes       | Yes            | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | current_compensation_frequency | Yes       | No        | Yes       | No        | Yes       | No                  | Yes                 | Yes       | Yes            | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | current_gain_bandwidth         | Yes       | No        | Yes       | No        | Yes       | No                  | Yes                 | Yes       | Yes            | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | current_pole_zero_ratio        | Yes       | No        | Yes       | No        | Yes       | No                  | Yes                 | Yes       | Yes            | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | voltage_compensation_frequency | Yes       | No        | Yes       | No        | Yes       | No                  | Yes                 | Yes       | Yes            | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | voltage_gain_bandwidth         | Yes       | No        | Yes       | No        | Yes       | No                  | Yes                 | Yes       | Yes            | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | voltage_pole_zero_ratio        | Yes       | No        | Yes       | No        | Yes       | No                  | Yes                 | Yes       | Yes            | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | current_level                  | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes       | Yes            | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | current_level_range            | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes       | Yes            | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | voltage_limit                  | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes       | Yes            | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | voltage_limit_high             | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes       | No             | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | voltage_limit_low              | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes       | No             | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | voltage_limit_range            | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes       | Yes            | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | current_limit                  | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes       | Yes            | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | current_limit_high             | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes       | No             | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | current_limit_low              | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes       | No             | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | current_limit_range            | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes       | Yes            | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | voltage_level                  | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes       | Yes            | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | voltage_level_range            | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes       | Yes            | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | output_enabled                 | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes       | Yes            | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | output_function                | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes       | Yes            | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | output_resistance              | Yes       | No        | Yes       | No        | Yes       | No                  | Yes                 | Yes       | No             | No        |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | pulse_bias_current_level       | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No        | No             | No        |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | pulse_bias_voltage_limit       | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No        | No             | No        |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | pulse_bias_voltage_limit_high  | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No        | No             | No        |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | pulse_bias_voltage_limit_low   | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No        | No             | No        |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | pulse_current_level            | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No        | No             | No        |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | pulse_current_level_range      | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No        | No             | No        |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | pulse_voltage_limit            | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No        | No             | No        |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | pulse_voltage_limit_high       | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No        | No             | No        |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | pulse_voltage_limit_low        | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No        | No             | No        |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | pulse_voltage_limit_range      | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No        | No             | No        |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | pulse_bias_current_limit       | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No        | No             | No        |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | pulse_bias_current_limit_high  | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No        | No             | No        |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | pulse_bias_current_limit_low   | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No        | No             | No        |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | pulse_bias_voltage_level       | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No        | No             | No        |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | pulse_current_limit            | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No        | No             | No        |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | pulse_current_limit_high       | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No        | No             | No        |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | pulse_current_limit_low        | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No        | No             | No        |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | pulse_current_limit_range      | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No        | No             | No        |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | pulse_voltage_level            | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No        | No             | No        |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | pulse_voltage_level_range      | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No        | No             | No        |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+
                | transient_response             | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes       | Yes            | Yes       |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+-----------+----------------+-----------+

            set_as_active_sequence (bool): Specifies that this current sequence is active.

        '''
        # The way the NI-DCPower C API is designed, we need to know all the attribute ID's upfront in order to call
        # `niDCPower_CreateAdvancedSequence`. In order to find the attribute ID of each property, we look at the
        # member Attribute objects of Session. We use a set since we don't have to worry about is it already there.
        attribute_ids_used = set()
        for prop in property_names:
            if prop not in Session.__base__.__dict__:
                raise KeyError('{} is not an property on the nidcpower.Session'.format(prop))
            if not isinstance(Session.__base__.__dict__[prop], _attributes.Attribute):
                raise TypeError('{} is not a valid property: {}'.format(prop, type(Session.__base__.__dict__[prop])))
            attribute_ids_used.add(Session.__base__.__dict__[prop]._attribute_id)

        self._create_advanced_sequence_with_channels(sequence_name, list(attribute_ids_used), set_as_active_sequence)

    @ivi_synchronized
    def fetch_multiple(self, count, timeout=hightime.timedelta(seconds=1.0)):
        '''fetch_multiple

        Returns a list of named tuples (Measurement) that were
        previously taken and are stored in the NI-DCPower buffer. This method
        should not be used when the measure_when property is
        set to MeasureWhen.ON_DEMAND. You must first call
        initiate before calling this method.

        Fields in Measurement:

        - **voltage** (float)
        - **current** (float)
        - **in_compliance** (bool)
        - **channel** (str)

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].fetch_multiple`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.fetch_multiple`

        Args:
            count (int): Specifies the number of measurements to fetch.

            timeout (hightime.timedelta, datetime.timedelta, or float in seconds): Specifies the maximum time allowed for this method to complete. If the method does not complete within this time interval, NI-DCPower returns an error.
                Default value: 1.0 second

                Note: When setting the timeout interval, ensure you take into account any triggers so that the timeout interval is long enough for your application.


        Returns:
            measurements (list of Measurement): List of named tuples with fields:

                - **voltage** (float)
                - **current** (float)
                - **in_compliance** (bool)
                - **channel** (str)

        '''
        import collections
        Measurement = collections.namedtuple('Measurement', ['voltage', 'current', 'in_compliance', 'channel'])

        voltage_measurements, current_measurements, in_compliances = self._fetch_multiple(timeout, count)

        channel_names = _converters.expand_channel_string(
            self._repeated_capability,
            self._all_channels_in_session
        )
        assert len(channel_names) == 1, "fetch_multiple only supports one channel at a time"
        return [
            Measurement(
                voltage=voltage,
                current=current,
                in_compliance=in_compliance,
                channel=channel_names[0]
            ) for voltage, current, in_compliance in zip(
                voltage_measurements, current_measurements, in_compliances
            )
        ]

    @ivi_synchronized
    def fetch_multiple_lcr(self, count, timeout=hightime.timedelta(seconds=1.0)):
        '''fetch_multiple_lcr

        Returns a list of previously measured LCRMeasurement instances on the specified channel that have been taken and stored in a buffer.

        To use this method:

        -  Set measure_when property to MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE or MeasureWhen.ON_MEASURE_TRIGGER
        -  Put the channel in the Running state (call initiate)

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].fetch_multiple_lcr`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.fetch_multiple_lcr`

        Args:
            count (int): Specifies the number of measurements to fetch.

            timeout (hightime.timedelta, datetime.timedelta, or float in seconds): Specifies the maximum time allowed for this method to complete, in seconds.
                If the method does not complete within this time interval, NI-DCPower returns an error.
                Default value: 1.0 second

                Note:
                When setting the timeout interval, ensure you take into account any triggers so that the timeout interval is long enough for your application.


        Returns:
            measurements (list of LCRMeasurement): A list of LCRMeasurement instances.

                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | channel               |                      | The channel name associated with this LCR measurement.                                                                                                                                                |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | vdc                   | float                | The measured DC voltage, in volts.                                                                                                                                                                    |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | idc                   | float                | The measured DC current, in amps.                                                                                                                                                                     |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | stimulus_frequency    | float                | The frequency of the LCR test signal, in Hz.                                                                                                                                                          |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | ac_voltage            | complex              | The measured AC voltage, in volts RMS.                                                                                                                                                                |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | ac_current            | complex              | The measured AC current, in amps RMS.                                                                                                                                                                 |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | z                     | complex              | The complex impedance.                                                                                                                                                                                |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | z_magnitude_and_phase | tuple of float       | The magnitude, in ohms, and phase angle, in degrees, of the complex impedance.                                                                                                                        |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | y                     | complex              | The complex admittance.                                                                                                                                                                               |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | y_magnitude_and_phase | tuple of float       | The magnitude, in siemens, and phase angle, in degrees, of the complex admittance.                                                                                                                    |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | series_lcr            | LCR                  | The inductance, in henrys, the capacitance, in farads, and the resistance, in ohms, as measured using a series circuit model.                                                                         |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | parallel_lcr          | LCR                  | The inductance, in henrys, the capacitance, in farads, and the resistance, in ohms, as measured using a parallel circuit model.                                                                       |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | d                     | float                | The dissipation factor of the circuit. The dimensionless dissipation factor is directly proportional to how quickly an oscillating system loses energy. D is the reciprocal of Q, the quality factor. |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | q                     | float                | The quality factor of the circuit. The dimensionless quality factor is inversely proportional to the degree of damping in a system. Q is the reciprocal of D, the dissipation factor.                 |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | measurement_mode      | enums.InstrumentMode | The measurement mode: **SMU** - The channel(s) are operating as a power supply/SMU. **LCR** - The channel(s) are operating as an LCR meter.                                                           |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | dc_in_compliance      | bool                 | Indicates whether the output was in DC compliance at the time the measurement was taken.                                                                                                              |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | ac_in_compliance      | bool                 | Indicates whether the output was in AC compliance at the time the measurement was taken.                                                                                                              |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | unbalanced            | bool                 | Indicates whether the output was unbalanced at the time the measurement was taken.                                                                                                                    |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        '''
        lcr_measurements = self._fetch_multiple_lcr(count, timeout)

        channel_names = _converters.expand_channel_string(
            self._repeated_capability,
            self._all_channels_in_session
        )
        assert len(channel_names) == 1, "fetch_multiple_lcr only supports one channel at a time"
        for lcr_measurement_object, in zip(lcr_measurements):
            lcr_measurement_object.channel = channel_names[0]
        return lcr_measurements

    @ivi_synchronized
    def measure_multiple(self):
        '''measure_multiple

        Returns a list of named tuples (Measurement) containing the measured voltage
        and current values on the specified channel(s). Each call to this method
        blocks other method calls until the measurements are returned from the device.
        The order of the measurements returned in the array corresponds to the order
        on the specified channel(s).

        Fields in Measurement:

        - **voltage** (float)
        - **current** (float)
        - **in_compliance** (bool) - Always None
        - **channel** (str)

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].measure_multiple`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.measure_multiple`

        Returns:
            measurements (list of Measurement): List of named tuples with fields:

                - **voltage** (float)
                - **current** (float)
                - **in_compliance** (bool) - Always None
                - **channel** (str)

        '''
        import collections
        Measurement = collections.namedtuple('Measurement', ['voltage', 'current', 'in_compliance', 'channel'])

        voltage_measurements, current_measurements = self._measure_multiple()

        channel_names = _converters.expand_channel_string(
            self._repeated_capability,
            self._all_channels_in_session
        )
        assert (
            len(channel_names) == len(voltage_measurements) and len(channel_names) == len(current_measurements)
        ), "measure_multiple should return as many voltage and current measurements as the number of channels specified through the channel string"
        return [
            Measurement(
                voltage=voltage,
                current=current,
                in_compliance=None,
                channel=channel_name
            ) for voltage, current, channel_name in zip(
                voltage_measurements, current_measurements, channel_names
            )
        ]

    @ivi_synchronized
    def measure_multiple_lcr(self):
        '''measure_multiple_lcr

        Measures and returns a list of LCRMeasurement instances on the specified channel(s).

        To use this method:

        -  Set instrument_mode property to InstrumentMode.LCR
        -  Set measure_when property to MeasureWhen.ON_DEMAND
        -  Put the channel(s) in the Running state (call initiate)

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].measure_multiple_lcr`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.measure_multiple_lcr`

        Returns:
            measurements (list of LCRMeasurement): A list of LCRMeasurement instances.

                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | channel               |                      | The channel name associated with this LCR measurement.                                                                                                                                                |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | vdc                   | float                | The measured DC voltage, in volts.                                                                                                                                                                    |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | idc                   | float                | The measured DC current, in amps.                                                                                                                                                                     |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | stimulus_frequency    | float                | The frequency of the LCR test signal, in Hz.                                                                                                                                                          |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | ac_voltage            | complex              | The measured AC voltage, in volts RMS.                                                                                                                                                                |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | ac_current            | complex              | The measured AC current, in amps RMS.                                                                                                                                                                 |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | z                     | complex              | The complex impedance.                                                                                                                                                                                |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | z_magnitude_and_phase | tuple of float       | The magnitude, in ohms, and phase angle, in degrees, of the complex impedance.                                                                                                                        |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | y                     | complex              | The complex admittance.                                                                                                                                                                               |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | y_magnitude_and_phase | tuple of float       | The magnitude, in siemens, and phase angle, in degrees, of the complex admittance.                                                                                                                    |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | series_lcr            | LCR                  | The inductance, in henrys, the capacitance, in farads, and the resistance, in ohms, as measured using a series circuit model.                                                                         |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | parallel_lcr          | LCR                  | The inductance, in henrys, the capacitance, in farads, and the resistance, in ohms, as measured using a parallel circuit model.                                                                       |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | d                     | float                | The dissipation factor of the circuit. The dimensionless dissipation factor is directly proportional to how quickly an oscillating system loses energy. D is the reciprocal of Q, the quality factor. |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | q                     | float                | The quality factor of the circuit. The dimensionless quality factor is inversely proportional to the degree of damping in a system. Q is the reciprocal of D, the dissipation factor.                 |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | measurement_mode      | enums.InstrumentMode | The measurement mode: **SMU** - The channel(s) are operating as a power supply/SMU. **LCR** - The channel(s) are operating as an LCR meter.                                                           |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | dc_in_compliance      | bool                 | Indicates whether the output was in DC compliance at the time the measurement was taken.                                                                                                              |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | ac_in_compliance      | bool                 | Indicates whether the output was in AC compliance at the time the measurement was taken.                                                                                                              |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | unbalanced            | bool                 | Indicates whether the output was unbalanced at the time the measurement was taken.                                                                                                                    |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        '''
        lcr_measurements = self._measure_multiple_lcr()

        channel_names = _converters.expand_channel_string(
            self._repeated_capability,
            self._all_channels_in_session
        )
        assert len(channel_names) == len(lcr_measurements), (
            "measure_multiple_lcr should return as many LCR measurements as the number of channels specified through the channel string"
        )
        for lcr_measurement_object, channel_name in zip(lcr_measurements, channel_names):
            lcr_measurement_object.channel = channel_name
        return lcr_measurements

    @ivi_synchronized
    def _fetch_multiple(self, timeout, count):
        r'''_fetch_multiple

        Returns an array of voltage measurements, an array of current
        measurements, and an array of compliance measurements that were
        previously taken and are stored in the NI-DCPower buffer. This method
        should not be used when the measure_when property is
        set to MeasureWhen.ON_DEMAND. You must first call
        initiate before calling this method.

        Refer to the `Acquiring
        Measurements <REPLACE_DRIVER_SPECIFIC_URL_1(acquiringmeasurements)>`__
        and `Compliance <REPLACE_DRIVER_SPECIFIC_URL_1(compliance)>`__ topics in
        the *NI DC Power Supplies and SMUs Help* for more information about
        configuring this method.

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._fetch_multiple`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session._fetch_multiple`

        Args:
            timeout (hightime.timedelta, datetime.timedelta, or float in seconds): Specifies the maximum time allowed for this method to complete, in
                seconds. If the method does not complete within this time interval,
                NI-DCPower returns an error.

                Note:
                When setting the timeout interval, ensure you take into account any
                triggers so that the timeout interval is long enough for your
                application.

            count (int): Specifies the number of measurements to fetch.


        Returns:
            voltage_measurements (array.array("d")): Returns an array of voltage measurements. Ensure that sufficient space
                has been allocated for the returned array.

            current_measurements (array.array("d")): Returns an array of current measurements. Ensure that sufficient space
                has been allocated for the returned array.

            in_compliance (list of bool): Returns an array of Boolean values indicating whether the output was in
                compliance at the time the measurement was taken. Ensure that sufficient
                space has been allocated for the returned array.

        '''
        timeout = _converters.convert_timedelta_to_seconds_real64(timeout)
        voltage_measurements, current_measurements, in_compliance = self._interpreter.fetch_multiple(self._repeated_capability, timeout, count)
        return voltage_measurements, current_measurements, in_compliance

    @ivi_synchronized
    def _fetch_multiple_lcr(self, count, timeout=hightime.timedelta(seconds=1.0)):
        r'''_fetch_multiple_lcr

        Returns a list of previously measured LCRMeasurement instances on the specified channel that have been taken and stored in a buffer.

        To use this method:

        -  Set measure_when property to MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE or MeasureWhen.ON_MEASURE_TRIGGER
        -  Put the channel in the Running state (call initiate)

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._fetch_multiple_lcr`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session._fetch_multiple_lcr`

        Args:
            count (int): Specifies the number of measurements to fetch.

            timeout (hightime.timedelta, datetime.timedelta, or float in seconds): Specifies the maximum time allowed for this method to complete, in seconds.
                If the method does not complete within this time interval, NI-DCPower returns an error.

                Note:
                When setting the timeout interval, ensure you take into account any triggers so that the timeout interval is long enough for your application.


        Returns:
            measurements (list of LCRMeasurement): A list of LCRMeasurement instances.

                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | vdc                   | float                | The measured DC voltage, in volts.                                                                                                                                                                    |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | idc                   | float                | The measured DC current, in amps.                                                                                                                                                                     |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | stimulus_frequency    | float                | The frequency of the LCR test signal, in Hz.                                                                                                                                                          |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | ac_voltage            | complex              | The measured AC voltage, in volts RMS.                                                                                                                                                                |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | ac_current            | complex              | The measured AC current, in amps RMS.                                                                                                                                                                 |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | z                     | complex              | The complex impedance.                                                                                                                                                                                |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | z_magnitude_and_phase | tuple of float       | The magnitude, in ohms, and phase angle, in degrees, of the complex impedance.                                                                                                                        |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | y                     | complex              | The complex admittance.                                                                                                                                                                               |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | y_magnitude_and_phase | tuple of float       | The magnitude, in siemens, and phase angle, in degrees, of the complex admittance.                                                                                                                    |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | series_lcr            | LCR                  | The inductance, in henrys, the capacitance, in farads, and the resistance, in ohms, as measured using a series circuit model.                                                                         |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | parallel_lcr          | LCR                  | The inductance, in henrys, the capacitance, in farads, and the resistance, in ohms, as measured using a parallel circuit model.                                                                       |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | d                     | float                | The dissipation factor of the circuit. The dimensionless dissipation factor is directly proportional to how quickly an oscillating system loses energy. D is the reciprocal of Q, the quality factor. |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | q                     | float                | The quality factor of the circuit. The dimensionless quality factor is inversely proportional to the degree of damping in a system. Q is the reciprocal of D, the dissipation factor.                 |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | measurement_mode      | enums.InstrumentMode | The measurement mode: **SMU** - The channel(s) are operating as a power supply/SMU. **LCR** - The channel(s) are operating as an LCR meter.                                                           |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | dc_in_compliance      | bool                 | Indicates whether the output was in DC compliance at the time the measurement was taken.                                                                                                              |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | ac_in_compliance      | bool                 | Indicates whether the output was in AC compliance at the time the measurement was taken.                                                                                                              |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | unbalanced            | bool                 | Indicates whether the output was unbalanced at the time the measurement was taken.                                                                                                                    |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        '''
        timeout = _converters.convert_timedelta_to_seconds_real64(timeout)
        measurements = self._interpreter.fetch_multiple_lcr(self._repeated_capability, timeout, count)
        return measurements

    @ivi_synchronized
    def _get_attribute_vi_boolean(self, attribute_id):
        r'''_get_attribute_vi_boolean

        | Queries the value of a ViBoolean property.
        | You can use this method to get the values of device-specific
          properties and inherent IVI properties.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_boolean`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_boolean`

        Args:
            attribute_id (int): Specifies the ID of a property. From the method panel window, you
                can use this control as follows.

                -  In the method panel window, click on the control or press **Enter**
                   or the spacebar to display a dialog box containing hierarchical list
                   of the available properties. Help text is shown for each property.
                   Select a property by double-clicking on it or by selecting it and
                   then pressing **Enter**.
                -  A ring control at the top of the dialog box allows you to see all IVI
                   properties or only the properties of type ViBoolean. If you choose to
                   see all IVI properties, the data types appear to the right of the
                   property names in the list box. Properties with data types other
                   than ViBoolean are dim. If you select a property data type that is
                   dim, LabWindows/CVI transfers you to the method panel for the
                   corresponding method that is consistent with the data type.
                -  If you want to enter a variable name, press **Ctrl**\ +\ **T** to
                   change this ring control to a manual input box. If the property in
                   this ring control has named constants as valid values, you can view
                   the constants by moving to the value control and pressing **Enter**.


        Returns:
            attribute_value (bool): Returns the current value of the property. Passes the address of a
                ViBoolean variable.
                If the property currently showing in the property ring control has
                constants as valid values, you can view a list of the constants by
                pressing **Enter** on this control. Select a value by double-clicking on
                it or by selecting it and then pressing **Enter**.

        '''
        attribute_value = self._interpreter.get_attribute_vi_boolean(self._repeated_capability, attribute_id)
        return attribute_value

    @ivi_synchronized
    def _get_attribute_vi_int32(self, attribute_id):
        r'''_get_attribute_vi_int32

        | Queries the value of a ViInt32 property.
        | You can use this method to get the values of device-specific
          properties and inherent IVI properties.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_int32`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_int32`

        Args:
            attribute_id (int): Specifies the ID of a property. From the method panel window, you
                can use this control as follows.

                -  In the method panel window, click on the control or press **Enter**
                   or the spacebar to display a dialog box containing hierarchical list
                   of the available properties. Help text is shown for each property.
                   Select a property by double-clicking on it or by selecting it and
                   then pressing **Enter**.
                -  A ring control at the top of the dialog box allows you to see all IVI
                   properties or only the properties of type ViInt32. If you choose to
                   see all IVI properties, the data types appear to the right of the
                   property names in the list box. Properties with data types other
                   than ViInt32 are dim. If you select a property data type that is
                   dim, LabWindows/CVI transfers you to the method panel for the
                   corresponding method that is consistent with the data type.
                -  If you want to enter a variable name, press **Ctrl**\ +\ **T** to
                   change this ring control to a manual input box. If the property in
                   this ring control has named constants as valid values, you can view
                   the constants by moving to the value control and pressing **Enter**.


        Returns:
            attribute_value (int): Returns the current value of the property. Passes the address of a
                ViInt32 variable.
                If the property currently showing in the property ring control has
                constants as valid values, you can view a list of the constants by
                pressing **Enter** on this control. Select a value by double-clicking on
                it or by selecting it and then pressing **Enter**.

        '''
        attribute_value = self._interpreter.get_attribute_vi_int32(self._repeated_capability, attribute_id)
        return attribute_value

    @ivi_synchronized
    def _get_attribute_vi_int64(self, attribute_id):
        r'''_get_attribute_vi_int64

        | Queries the value of a ViInt64 property.
        | You can use this method to get the values of device-specific
          properties and inherent IVI properties.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_int64`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_int64`

        Args:
            attribute_id (int): Specifies the ID of a property. From the method panel window, you
                can use this control as follows.

                -  In the method panel window, click on the control or press **Enter**
                   or the spacebar to display a dialog box containing hierarchical list
                   of the available properties. Help text is shown for each property.
                   Select a property by double-clicking on it or by selecting it and
                   then pressing **Enter**.
                -  A ring control at the top of the dialog box allows you to see all IVI
                   properties or only the properties of type ViReal64. If you choose to
                   see all IVI properties, the data types appear to the right of the
                   property names in the list box. Properties with data types other
                   than ViReal64 are dim. If you select a property data type that is
                   dim, LabWindows/CVI transfers you to the method panel for the
                   corresponding method that is consistent with the data type.
                -  If you want to enter a variable name, press **Ctrl**\ +\ **T** to
                   change this ring control to a manual input box. If the property in
                   this ring control has named constants as valid values, you can view
                   the constants by moving to the value control and pressing **Enter**.


        Returns:
            attribute_value (int): Returns the current value of the property. Passes the address of a
                ViReal64 variable.
                If the property currently showing in the property ring control has
                constants as valid values, you can view a list of the constants by
                pressing **Enter** on this control. Select a value by double-clicking on
                it or by selecting it and then pressing **Enter**.

        '''
        attribute_value = self._interpreter.get_attribute_vi_int64(self._repeated_capability, attribute_id)
        return attribute_value

    @ivi_synchronized
    def _get_attribute_vi_real64(self, attribute_id):
        r'''_get_attribute_vi_real64

        | Queries the value of a ViReal64 property.
        | You can use this method to get the values of device-specific
          properties and inherent IVI properties.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_real64`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_real64`

        Args:
            attribute_id (int): Specifies the ID of a property. From the method panel window, you
                can use this control as follows.

                -  In the method panel window, click on the control or press **Enter**
                   or the spacebar to display a dialog box containing hierarchical list
                   of the available properties. Help text is shown for each property.
                   Select a property by double-clicking on it or by selecting it and
                   then pressing **Enter**.
                -  A ring control at the top of the dialog box allows you to see all IVI
                   properties or only the properties of type ViReal64. If you choose to
                   see all IVI properties, the data types appear to the right of the
                   property names in the list box. Properties with data types other
                   than ViReal64 are dim. If you select a property data type that is
                   dim, LabWindows/CVI transfers you to the method panel for the
                   corresponding method that is consistent with the data type.
                -  If you want to enter a variable name, press **Ctrl**\ +\ **T** to
                   change this ring control to a manual input box. If the property in
                   this ring control has named constants as valid values, you can view
                   the constants by moving to the value control and pressing **Enter**.


        Returns:
            attribute_value (float): Returns the current value of the property. Passes the address of a
                ViReal64 variable.
                If the property currently showing in the property ring control has
                constants as valid values, you can view a list of the constants by
                pressing **Enter** on this control. Select a value by double-clicking on
                it or by selecting it and then pressing **Enter**.

        '''
        attribute_value = self._interpreter.get_attribute_vi_real64(self._repeated_capability, attribute_id)
        return attribute_value

    @ivi_synchronized
    def _get_attribute_vi_string(self, attribute_id):
        r'''_get_attribute_vi_string

        | Queries the value of a ViString property.
        | You can use this method to get the values of device-specific
          properties and inherent IVI properties.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_string`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_string`

        Args:
            attribute_id (int): Specifies the ID of a property. From the method panel window, you
                can use this control as follows.

                -  In the method panel window, click on the control or press or the
                   spacebar to display a dialog box containing hierarchical list of the
                   available properties. Help text is shown for each property. Select
                   a property by double-clicking on it or by selecting it and then
                   pressing .
                -  A ring control at the top of the dialog box allows you to see all IVI
                   properties or only the properties of type ViString. If you choose to
                   see all IVI properties, the data types appear to the right of the
                   property names in the list box. Properties with data types other
                   than ViString are dimmed. If you select a property data type that
                   is dimmed, LabWindows/CVI transfers you to the method panel for the
                   corresponding method that is consistent with the data type.
                -  If you want to enter a variable name, press to change this ring
                   control to a manual input control. If the property in this ring
                   control has named constants as valid values, you can view the
                   constants by moving to the value control and pressing .


        Returns:
            attribute_value (str): The buffer in which the method returns the current value of the
                property. The buffer must be of type ViChar and have at least as many
                bytes as indicated in **bufSize**.
                If the current value of the property, including the terminating NUL
                byte, contains more bytes that you indicate in this property, the
                method copies (buffer size -1) bytes into the buffer, places an ASCII
                NUL byte at the end of the buffer, and returns the buffer size you must
                pass to get the entire value. For example, if the value is 123456 and
                the buffer size is 4, the method places 123 into the buffer and
                returns 7.
                If you specify 0 for **bufSize**, you can pass VI_NULL for this
                property.
                If the property currently showing in the property ring control has
                constants as valid values, you can view a list of the constants by
                pressing on this control. Select a value by double-clicking on it or by
                selecting it and then pressing .

        '''
        attribute_value = self._interpreter.get_attribute_vi_string(self._repeated_capability, attribute_id)
        return attribute_value

    @ivi_synchronized
    def _get_channel_names(self, indices):
        r'''_get_channel_names

        Returns a list of channel names for the given channel indices.

        Args:
            indices (basic sequence types, str, or int): Index list for the channels in the session. Valid values are from zero to the total number of channels in the session minus one. The index string can be one of the following formats:

                -   A comma-separated list—for example, "0,2,3,1"
                -   A range using a hyphen—for example, "0-3"
                -   A range using a colon—for example, "0:3 "

                You can combine comma-separated lists and ranges that use a hyphen or colon. Both out-of-order and repeated indices are supported ("2,3,0", "1,2,2,3"). White space characters, including spaces, tabs, feeds, and carriage returns, are allowed between characters. Ranges can be incrementing or decrementing.


        Returns:
            names (list of str): The channel name(s) at the specified indices.

        '''
        indices = _converters.convert_repeated_capabilities_without_prefix(indices)
        names = self._interpreter.get_channel_names(indices)
        return _converters.convert_comma_separated_string_to_list(names)

    @ivi_synchronized
    def get_lcr_compensation_data(self):
        r'''get_lcr_compensation_data

        Collects previously generated open, short, load, and custom cable compensation data so you can then apply it to LCR measurements with configure_lcr_compensation.

        Call this method after you have obtained the compensation data of all types (open, short, load, open custom cable compensation, and short custom cable compensation) you want to apply to your measurements. Pass the **compensation data** to configure_lcr_compensation

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].get_lcr_compensation_data`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.get_lcr_compensation_data`

        Returns:
            compensation_data (bytes): The open, short, load, and custom cable compensation data to retrieve.

        '''
        compensation_data = self._interpreter.get_lcr_compensation_data(self._repeated_capability)
        return _converters.convert_to_bytes(compensation_data)

    @ivi_synchronized
    def _get_lcr_compensation_last_date_and_time(self, compensation_type):
        r'''_get_lcr_compensation_last_date_and_time

        Returns the date and time the specified type of compensation data for LCR measurements was most recently generated.
        The time returned is 24-hour (military) local time; for example, if the selected type of compensation data was generated at 2:30 PM, this method returns 14 for **hours** and 30 for **minutes**.

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_lcr_compensation_last_date_and_time`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session._get_lcr_compensation_last_date_and_time`

        Args:
            compensation_type (enums.LCRCompensationType): Specifies the type of compensation for LCR measurements.


        Returns:
            year (int): Returns the year of the relevant operation.

            month (int): Returns the month of the relevant operation.

            day (int): Returns the day of the relevant operation.

            hour (int): Returns the hour (in 24-hour time) of the relevant operation.

            minute (int): Returns the minute of the relevant operation.

        '''
        if type(compensation_type) is not enums.LCRCompensationType:
            raise TypeError('Parameter compensation_type must be of type ' + str(enums.LCRCompensationType))
        year, month, day, hour, minute = self._interpreter.get_lcr_compensation_last_date_and_time(self._repeated_capability, compensation_type)
        return year, month, day, hour, minute

    @ivi_synchronized
    def get_lcr_custom_cable_compensation_data(self):
        r'''get_lcr_custom_cable_compensation_data

        This method is deprecated. Use get_lcr_compensation_data
        instead.

        Collects previously generated open and short custom cable compensation data so you can then apply it to LCR measurements with configure_lcr_custom_cable_compensation.

        Call this method after you have obtained open and short custom cable compensation data. Pass the **custom cable compensation data** to configure_lcr_custom_cable_compensation

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].get_lcr_custom_cable_compensation_data`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.get_lcr_custom_cable_compensation_data`

        Returns:
            custom_cable_compensation_data (bytes): The open and short custom cable compensation data to retrieve.

        '''
        custom_cable_compensation_data = self._interpreter.get_lcr_custom_cable_compensation_data(self._repeated_capability)
        return _converters.convert_to_bytes(custom_cable_compensation_data)

    @ivi_synchronized
    def get_lcr_compensation_last_date_and_time(self, compensation_type):
        '''get_lcr_compensation_last_date_and_time

        Returns the date and time the specified type of compensation data for LCR measurements was most recently generated.

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].get_lcr_compensation_last_date_and_time`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.get_lcr_compensation_last_date_and_time`

        Args:
            compensation_type (enums.LCRCompensationType): Specifies the type of compensation for LCR measurements.


        Returns:
            last_comp_datetime (hightime.datetime): Returns the date and time the specified type of compensation data for LCR measurements was most recently generated.

        '''
        year, month, day, hour, minute = self._get_lcr_compensation_last_date_and_time(compensation_type)
        return hightime.datetime(year, month, day, hour, minute)

    @ivi_synchronized
    def _initiate_with_channels(self):
        r'''_initiate_with_channels

        Starts generation or acquisition, causing the specified channel(s) to
        leave the Uncommitted state or Committed state and enter the Running
        state. To return to the Uncommitted state call the abort
        method. Refer to the `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic in
        the *NI DC Power Supplies and SMUs Help* for information about the
        specific NI-DCPower software states.

        **Related Topics:**

        `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._initiate_with_channels`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session._initiate_with_channels`
        '''
        self._interpreter.initiate_with_channels(self._repeated_capability)

    def lock(self):
        '''lock

        Obtains a multithread lock on the device session. Before doing so, the
        software waits until all other execution threads release their locks
        on the device session.

        Other threads may have obtained a lock on this session for the
        following reasons:

            -  The application called the lock method.
            -  A call to NI-DCPower locked the session.
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
            lock (context manager): When used in a with statement, nidcpower.Session.lock acts as
            a context manager and unlock will be called when the with block is exited
        '''
        self._interpreter.lock()  # We do not call this in the context manager so that this function can
        # act standalone as well and let the client call unlock() explicitly. If they do use the context manager,
        # that will handle the unlock for them
        return _Lock(self)

    @ivi_synchronized
    def measure(self, measurement_type):
        r'''measure

        Returns the measured value of either the voltage or current on the
        specified channel. Each call to this method blocks other
        method calls until the hardware returns the **measurement**. To
        measure multiple channels, use the measure_multiple
        method.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].measure`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.measure`

        Args:
            measurement_type (enums.MeasurementTypes): Specifies whether a voltage or current value is measured.
                **Defined Values**:

                +--------------------------+------------------------------+
                | MeasurementTypes.VOLTAGE | The device measures voltage. |
                +--------------------------+------------------------------+
                | MeasurementTypes.CURRENT | The device measures current. |
                +--------------------------+------------------------------+


        Returns:
            measurement (float): Returns the value of the measurement, either in volts for voltage or
                amps for current.

        '''
        if type(measurement_type) is not enums.MeasurementTypes:
            raise TypeError('Parameter measurement_type must be of type ' + str(enums.MeasurementTypes))
        measurement = self._interpreter.measure(self._repeated_capability, measurement_type)
        return measurement

    @ivi_synchronized
    def _measure_multiple(self):
        r'''_measure_multiple

        Returns arrays of the measured voltage and current values on the
        specified channel(s). Each call to this method blocks other
        method calls until the measurements are returned from the device. The
        order of the measurements returned in the array corresponds to the order
        on the specified channel(s).

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._measure_multiple`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session._measure_multiple`

        Returns:
            voltage_measurements (array.array("d")): Returns an array of voltage measurements. The measurements in the array
                are returned in the same order as the channels specified in
                **channelName**. Ensure that sufficient space has been allocated for the
                returned array.

            current_measurements (array.array("d")): Returns an array of current measurements. The measurements in the array
                are returned in the same order as the channels specified in
                **channelName**. Ensure that sufficient space has been allocated for the
                returned array.

        '''
        voltage_measurements, current_measurements = self._interpreter.measure_multiple(self._repeated_capability)
        return voltage_measurements, current_measurements

    @ivi_synchronized
    def _measure_multiple_lcr(self):
        r'''_measure_multiple_lcr

        Measures and returns a list of LCRMeasurement instances on the specified channel(s).

        To use this method:

        -  Set instrument_mode property to InstrumentMode.LCR
        -  Set measure_when property to MeasureWhen.ON_DEMAND
        -  Put the channel(s) in the Running state (call initiate)

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._measure_multiple_lcr`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session._measure_multiple_lcr`

        Returns:
            measurements (list of LCRMeasurement): A list of LCRMeasurement instances.

                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | vdc                   | float                | The measured DC voltage, in volts.                                                                                                                                                                    |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | idc                   | float                | The measured DC current, in amps.                                                                                                                                                                     |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | stimulus_frequency    | float                | The frequency of the LCR test signal, in Hz.                                                                                                                                                          |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | ac_voltage            | complex              | The measured AC voltage, in volts RMS.                                                                                                                                                                |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | ac_current            | complex              | The measured AC current, in amps RMS.                                                                                                                                                                 |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | z                     | complex              | The complex impedance.                                                                                                                                                                                |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | z_magnitude_and_phase | tuple of float       | The magnitude, in ohms, and phase angle, in degrees, of the complex impedance.                                                                                                                        |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | y                     | complex              | The complex admittance.                                                                                                                                                                               |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | y_magnitude_and_phase | tuple of float       | The magnitude, in siemens, and phase angle, in degrees, of the complex admittance.                                                                                                                    |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | series_lcr            | LCR                  | The inductance, in henrys, the capacitance, in farads, and the resistance, in ohms, as measured using a series circuit model.                                                                         |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | parallel_lcr          | LCR                  | The inductance, in henrys, the capacitance, in farads, and the resistance, in ohms, as measured using a parallel circuit model.                                                                       |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | d                     | float                | The dissipation factor of the circuit. The dimensionless dissipation factor is directly proportional to how quickly an oscillating system loses energy. D is the reciprocal of Q, the quality factor. |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | q                     | float                | The quality factor of the circuit. The dimensionless quality factor is inversely proportional to the degree of damping in a system. Q is the reciprocal of D, the dissipation factor.                 |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | measurement_mode      | enums.InstrumentMode | The measurement mode: **SMU** - The channel(s) are operating as a power supply/SMU. **LCR** - The channel(s) are operating as an LCR meter.                                                           |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | dc_in_compliance      | bool                 | Indicates whether the output was in DC compliance at the time the measurement was taken.                                                                                                              |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | ac_in_compliance      | bool                 | Indicates whether the output was in AC compliance at the time the measurement was taken.                                                                                                              |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | unbalanced            | bool                 | Indicates whether the output was unbalanced at the time the measurement was taken.                                                                                                                    |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        '''
        measurements = self._interpreter.measure_multiple_lcr(self._repeated_capability)
        return measurements

    @ivi_synchronized
    def _parse_channel_count(self):
        r'''_parse_channel_count

        Returns the number of channels.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._parse_channel_count`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session._parse_channel_count`

        Returns:
            number_of_channels (int):

        '''
        number_of_channels = self._interpreter.parse_channel_count(self._repeated_capability)
        return number_of_channels

    @ivi_synchronized
    def perform_lcr_load_compensation(self, compensation_spots):
        r'''perform_lcr_load_compensation

        Generates load compensation data for LCR measurements for the test spots you specify.

        You must physically configure your LCR circuit with an appropriate reference load to use this method to generate valid load compensation data.

        When you call this method:

        -  The load compensation data is written to the onboard storage of the instrument. Onboard storage can contain only the most recent set of data.
        -  Most NI-DCPower properties in the session are reset to their default values. Rewrite the values of any properties you want to maintain.

        To apply the load compensation data you generate with this method to your LCR measurements, set the lcr_load_compensation_enabled property to True.

        Load compensation data are generated only for those specific frequencies you define with this method; load compensation is not interpolated from the specific frequencies you define and applied to other frequencies.

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].perform_lcr_load_compensation`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.perform_lcr_load_compensation`

        Args:
            compensation_spots (list of LCRLoadCompensationSpot): Defines the frequencies and DUT specifications to use for LCR load compensation.

                You can specify <=1000 spot frequencies.

                +----------------------+----------------------------------------------------------------------------------------------------------------------------------------+
                | frequency            | The spot frequency, in Hz.                                                                                                             |
                +----------------------+----------------------------------------------------------------------------------------------------------------------------------------+
                | reference_value_type | A known specification value of your DUT to use as the basis for load compensation.                                                     |
                +----------------------+----------------------------------------------------------------------------------------------------------------------------------------+
                | reference_value      | A value that describes the **reference_value_type** specification. Use as indicated by the **reference_value_type** option you choose. |
                +----------------------+----------------------------------------------------------------------------------------------------------------------------------------+

        '''
        self._interpreter.perform_lcr_load_compensation(self._repeated_capability, compensation_spots)

    @ivi_synchronized
    def perform_lcr_open_compensation(self, additional_frequencies=None):
        r'''perform_lcr_open_compensation

        Generates open compensation data for LCR measurements based on a default set of test frequencies and, optionally, additional frequencies you can specify.

        You must physically configure an open LCR circuit to use this method to generate valid open compensation data.

        When you call this method:

        -  The open compensation data is written to the onboard storage of the instrument. Onboard storage can contain only the most recent set of data.
        -  Most NI-DCPower properties in the session are reset to their default values. Rewrite the values of any properties you want to maintain.

        To apply the open compensation data you generate with this method to your LCR measurements, set the lcr_open_compensation_enabled property to True.

        Corrections for frequencies other than the default frequencies or any additional frequencies you specify are interpolated.

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Note:
        Default Open Compensation Frequencies:
        By default, NI-DCPower uses the following frequencies for LCR open compensation:

        -  10 logarithmic steps at 1 kHz frequency decade
        -  10 logarithmic steps at 10 kHz frequency decade
        -  100 logarithmic steps at 100 kHz frequency decade
        -  100 logarithmic steps at 1 MHz frequency decade

        The actual frequencies used depend on the bandwidth of your instrument.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].perform_lcr_open_compensation`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.perform_lcr_open_compensation`

        Args:
            additional_frequencies (list of float): Defines a further set of frequencies, in addition to the default frequencies, to perform the compensation for. You can specify <=200 additional frequencies.

        '''
        self._interpreter.perform_lcr_open_compensation(self._repeated_capability, additional_frequencies)

    @ivi_synchronized
    def perform_lcr_open_custom_cable_compensation(self):
        r'''perform_lcr_open_custom_cable_compensation

        Generates open custom cable compensation data for LCR measurements.

        To use this method, you must physically configure an open LCR circuit to generate valid open custom cable compensation data.

        When you call this method:

        -  The open compensation data is written to the onboard storage of the instrument. Onboard storage can contain only the most recent set of data.
        -  Most NI-DCPower properties in the session are reset to their default values. Rewrite the values of any properties you want to maintain.

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].perform_lcr_open_custom_cable_compensation`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.perform_lcr_open_custom_cable_compensation`
        '''
        self._interpreter.perform_lcr_open_custom_cable_compensation(self._repeated_capability)

    @ivi_synchronized
    def perform_lcr_short_compensation(self, additional_frequencies=None):
        r'''perform_lcr_short_compensation

        Generates short compensation data for LCR measurements based on a default set of test frequencies and, optionally, additional frequencies you can specify.

        You must physically configure your LCR circuit with a short to use this method to generate valid short compensation data.

        When you call this method:

        -  The short compensation data is written to the onboard storage of the instrument. Onboard storage can contain only the most recent set of data.
        - Most NI-DCPower properties in the session are reset to their default values. Rewrite the values of any properties you want to maintain.

        To apply the short compensation data you generate with this method to your LCR measurements, set the lcr_short_compensation_enabled property to True.

        Corrections for frequencies other than the default frequencies or any additional frequencies you specify are interpolated.

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Note:
        Default Short Compensation Frequencies:
        By default, NI-DCPower uses the following frequencies for LCR short compensation:

        -  10 logarithmic steps at 1 kHz frequency decade
        -  10 logarithmic steps at 10 kHz frequency decade
        -  100 logarithmic steps at 100 kHz frequency decade
        -  100 logarithmic steps at 1 MHz frequency decade

        The actual frequencies used depend on the bandwidth of your instrument.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].perform_lcr_short_compensation`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.perform_lcr_short_compensation`

        Args:
            additional_frequencies (list of float): Defines a further set of frequencies, in addition to the default frequencies, to perform the compensation for. You can specify <=200 additional frequencies.

        '''
        self._interpreter.perform_lcr_short_compensation(self._repeated_capability, additional_frequencies)

    @ivi_synchronized
    def perform_lcr_short_custom_cable_compensation(self):
        r'''perform_lcr_short_custom_cable_compensation

        Generates short custom cable compensation data for LCR measurements.

        To use this method:

        -  You must physically configure your LCR circuit with a short to generate valid short custom cable compensation data.
        -  Set lcr_short_custom_cable_compensation_enabled property to True

        When you call this method:

        -  The short compensation data is written to the onboard storage of the instrument. Onboard storage can contain only the most recent set of data.
        -  Most NI-DCPower properties in the session are reset to their default values. Rewrite the values of any properties you want to maintain.

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].perform_lcr_short_custom_cable_compensation`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.perform_lcr_short_custom_cable_compensation`
        '''
        self._interpreter.perform_lcr_short_custom_cable_compensation(self._repeated_capability)

    @ivi_synchronized
    def query_in_compliance(self):
        r'''query_in_compliance

        Queries the specified output device to determine if it is operating at
        the `compliance <REPLACE_DRIVER_SPECIFIC_URL_2(compliance)>`__ limit.

        The compliance limit is the current limit when the output method is
        set to OutputFunction.DC_VOLTAGE. If the output is operating at the
        compliance limit, the output reaches the current limit before the
        desired voltage level. Refer to the ConfigureOutputFunction
        method and the ConfigureCurrentLimit method for more
        information about output method and current limit, respectively.

        The compliance limit is the voltage limit when the output method is
        set to OutputFunction.DC_CURRENT. If the output is operating at the
        compliance limit, the output reaches the voltage limit before the
        desired current level. Refer to the ConfigureOutputFunction
        method and the ConfigureVoltageLimit method for more
        information about output method and voltage limit, respectively.

        **Related Topics:**

        `Compliance <REPLACE_DRIVER_SPECIFIC_URL_1(compliance)>`__

        Note:
        NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

        Note:
        One or more of the referenced methods are not in the Python API for this driver.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].query_in_compliance`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.query_in_compliance`

        Returns:
            in_compliance (bool): Returns whether the device channel is in compliance.

        '''
        in_compliance = self._interpreter.query_in_compliance(self._repeated_capability)
        return in_compliance

    @ivi_synchronized
    def query_latched_output_cutoff_state(self, output_cutoff_reason):
        r'''query_latched_output_cutoff_state

        Discovers if an output cutoff limit was exceeded for the specified reason. When an output cutoff is engaged, the output of the channel(s) is disconnected.
        If a limit was exceeded, the state is latched until you clear it with the clear_latched_output_cutoff_state method or the reset method.

        outputCutoffReason specifies the conditions for which an output is disconnected.

        Note:
        NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].query_latched_output_cutoff_state`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.query_latched_output_cutoff_state`

        Args:
            output_cutoff_reason (enums.OutputCutoffReason): Specifies which output cutoff conditions to query.

                +-----------------------------------------+--------------------------------------------------------------------------------------+
                | OutputCutoffReason.ALL                  | Any output cutoff condition was met                                                  |
                +-----------------------------------------+--------------------------------------------------------------------------------------+
                | OutputCutoffReason.VOLTAGE_OUTPUT_HIGH  | The output exceeded the high cutoff limit for voltage output                         |
                +-----------------------------------------+--------------------------------------------------------------------------------------+
                | OutputCutoffReason.VOLTAGE_OUTPUT_LOW   | The output fell below the low cutoff limit for voltage output                        |
                +-----------------------------------------+--------------------------------------------------------------------------------------+
                | OutputCutoffReason.VOLTAGE_MEASURE_HIGH | The measured voltage exceeded the high cutoff limit for voltage output               |
                +-----------------------------------------+--------------------------------------------------------------------------------------+
                | OutputCutoffReason.VOLTAGE_MEASURE_LOW  | The measured voltage fell below the low cutoff limit for voltage output              |
                +-----------------------------------------+--------------------------------------------------------------------------------------+
                | OutputCutoffReason.CURRENT_MEASURE_HIGH | The measured current exceeded the high cutoff limit for current output               |
                +-----------------------------------------+--------------------------------------------------------------------------------------+
                | OutputCutoffReason.CURRENT_MEASURE_LOW  | The measured current fell below the low cutoff limit for current output              |
                +-----------------------------------------+--------------------------------------------------------------------------------------+
                | OutputCutoffReason.VOLTAGE_CHANGE_HIGH  | The voltage slew rate increased beyond the positive change cutoff for voltage output |
                +-----------------------------------------+--------------------------------------------------------------------------------------+
                | OutputCutoffReason.VOLTAGE_CHANGE_LOW   | The voltage slew rate decreased beyond the negative change cutoff for voltage output |
                +-----------------------------------------+--------------------------------------------------------------------------------------+
                | OutputCutoffReason.CURRENT_CHANGE_HIGH  | The current slew rate increased beyond the positive change cutoff for current output |
                +-----------------------------------------+--------------------------------------------------------------------------------------+
                | OutputCutoffReason.CURRENT_CHANGE_LOW   | The current slew rate decreased beyond the negative change cutoff for current output |
                +-----------------------------------------+--------------------------------------------------------------------------------------+
                | OutputCutoffReason.CURRENT_SATURATED    | The measured current saturates the current range                                     |
                +-----------------------------------------+--------------------------------------------------------------------------------------+


        Returns:
            output_cutoff_state (bool): Specifies whether an output cutoff has engaged.

                +-------+------------------------------------------------------------------------------+
                | True  | An output cutoff has engaged for the conditions in **output cutoff reason**. |
                +-------+------------------------------------------------------------------------------+
                | False | No output cutoff has engaged.                                                |
                +-------+------------------------------------------------------------------------------+

        '''
        if type(output_cutoff_reason) is not enums.OutputCutoffReason:
            raise TypeError('Parameter output_cutoff_reason must be of type ' + str(enums.OutputCutoffReason))
        output_cutoff_state = self._interpreter.query_latched_output_cutoff_state(self._repeated_capability, output_cutoff_reason)
        return output_cutoff_state

    @ivi_synchronized
    def query_max_current_limit(self, voltage_level):
        r'''query_max_current_limit

        Queries the maximum current limit on a channel if the channel is set to the specified **voltageLevel**.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].query_max_current_limit`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.query_max_current_limit`

        Args:
            voltage_level (float): Specifies the voltage level to use when calculating the
                **maxCurrentLimit**.


        Returns:
            max_current_limit (float): Returns the maximum current limit that can be set with the specified
                **voltageLevel**.

        '''
        max_current_limit = self._interpreter.query_max_current_limit(self._repeated_capability, voltage_level)
        return max_current_limit

    @ivi_synchronized
    def query_max_voltage_level(self, current_limit):
        r'''query_max_voltage_level

        Queries the maximum voltage level on a channel if the channel is set to the specified **currentLimit**.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].query_max_voltage_level`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.query_max_voltage_level`

        Args:
            current_limit (float): Specifies the current limit to use when calculating the
                **maxVoltageLevel**.


        Returns:
            max_voltage_level (float): Returns the maximum voltage level that can be set on a channel
                with the specified **currentLimit**.

        '''
        max_voltage_level = self._interpreter.query_max_voltage_level(self._repeated_capability, current_limit)
        return max_voltage_level

    @ivi_synchronized
    def query_min_current_limit(self, voltage_level):
        r'''query_min_current_limit

        Queries the minimum current limit on a channel if the channel is set to the specified **voltageLevel**.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].query_min_current_limit`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.query_min_current_limit`

        Args:
            voltage_level (float): Specifies the voltage level to use when calculating the
                **minCurrentLimit**.


        Returns:
            min_current_limit (float): Returns the minimum current limit that can be set on a channel
                with the specified **voltageLevel**.

        '''
        min_current_limit = self._interpreter.query_min_current_limit(self._repeated_capability, voltage_level)
        return min_current_limit

    @ivi_synchronized
    def query_output_state(self, output_state):
        r'''query_output_state

        Queries the specified channel to determine if the channel
        is currently in the state specified by **outputState**.

        **Related Topics:**

        `Compliance <REPLACE_DRIVER_SPECIFIC_URL_1(compliance)>`__

        Note:
        NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].query_output_state`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.query_output_state`

        Args:
            output_state (enums.OutputStates): Specifies the output state of the channel that is being queried.
                **Defined Values**:

                +----------------------+-------------------------------------------------------------------+
                | OutputStates.VOLTAGE | The device maintains a constant voltage by adjusting the current. |
                +----------------------+-------------------------------------------------------------------+
                | OutputStates.CURRENT | The device maintains a constant current by adjusting the voltage. |
                +----------------------+-------------------------------------------------------------------+


        Returns:
            in_state (bool): Returns whether the device channel is in the specified output
                state.

        '''
        if type(output_state) is not enums.OutputStates:
            raise TypeError('Parameter output_state must be of type ' + str(enums.OutputStates))
        in_state = self._interpreter.query_output_state(self._repeated_capability, output_state)
        return in_state

    @ivi_synchronized
    def reset(self):
        r'''reset

        Resets the specified channel(s) to a known state. This method disables power
        generation, resets session properties to their default values, commits
        the session properties, and leaves the session in the Uncommitted state.
        Refer to the `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic for
        more information about NI-DCPower software states.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].reset`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.reset`
        '''
        self._interpreter.reset(self._repeated_capability)

    @ivi_synchronized
    def send_software_edge_trigger(self, trigger):
        r'''send_software_edge_trigger

        Asserts the specified trigger. This method can override an external
        edge trigger.

        **Related Topics:**

        `Triggers <REPLACE_DRIVER_SPECIFIC_URL_1(trigger)>`__

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].send_software_edge_trigger`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.send_software_edge_trigger`

        Args:
            trigger (enums.SendSoftwareEdgeTriggerType): Specifies which trigger to assert.
                **Defined Values:**

                +----------------------------------------------+---------------------------------------+
                | SendSoftwareEdgeTriggerType.START            | Asserts the Start trigger.            |
                +----------------------------------------------+---------------------------------------+
                | SendSoftwareEdgeTriggerType.SOURCE           | Asserts the Source trigger.           |
                +----------------------------------------------+---------------------------------------+
                | SendSoftwareEdgeTriggerType.MEASURE          | Asserts the Measure trigger.          |
                +----------------------------------------------+---------------------------------------+
                | SendSoftwareEdgeTriggerType.SEQUENCE_ADVANCE | Asserts the Sequence Advance trigger. |
                +----------------------------------------------+---------------------------------------+
                | SendSoftwareEdgeTriggerType.PULSE            | Asserts the Pulse trigger.            |
                +----------------------------------------------+---------------------------------------+
                | SendSoftwareEdgeTriggerType.SHUTDOWN         | Asserts the Shutdown trigger.         |
                +----------------------------------------------+---------------------------------------+

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        '''
        if type(trigger) is not enums.SendSoftwareEdgeTriggerType:
            raise TypeError('Parameter trigger must be of type ' + str(enums.SendSoftwareEdgeTriggerType))
        self._interpreter.send_software_edge_trigger(self._repeated_capability, trigger)

    @ivi_synchronized
    def _set_attribute_vi_boolean(self, attribute_id, attribute_value):
        r'''_set_attribute_vi_boolean

        | Sets the value of a ViBoolean property.
        | This is a low-level method that you can use to set the values of
          device-specific properties and inherent IVI properties.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_boolean`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_boolean`

        Args:
            attribute_id (int): Specifies the ID of a property. From the method panel window, you
                can use this control as follows.

                -  In the method panel window, click on the control or press **Enter**
                   or the spacebar to display a dialog box containing hierarchical list
                   of the available properties. Properties whose value cannot be set are
                   dim. Help text is shown for each property. Select a property by
                   double-clicking on it or by selecting it and then pressing **Enter**.
                -  Read-only properties appear dim in the list box. If you select a
                   read-only property, an error message appears. A ring control at the
                   top of the dialog box allows you to see all IVI properties or only
                   the properties of type ViBoolean. If you choose to see all IVI
                   properties, the data types appear to the right of the property names
                   in the list box. Properties with data types other than ViBoolean are
                   dim. If you select a property data type that is dim, LabWindows/CVI
                   transfers you to the method panel for the corresponding method
                   that is consistent with the data type.
                -  If you want to enter a variable name, press **Ctrl**\ +\ **T** to
                   change this ring control to a manual input box. If the property in
                   this ring control has named constants as valid values, you can view
                   the constants by moving to the value control and pressing **Enter**.

            attribute_value (bool): Specifies the value to which you want to set the property. If the
                property currently showing in the property ring control has constants
                as valid values, you can view a list of the constants by pressing
                **Enter** on this control. Select a value by double-clicking on it or by
                selecting it and then pressing **Enter**.

                Note:
                Some of the values might not be valid depending upon the current
                settings of the device session.

        '''
        self._interpreter.set_attribute_vi_boolean(self._repeated_capability, attribute_id, attribute_value)

    @ivi_synchronized
    def _set_attribute_vi_int32(self, attribute_id, attribute_value):
        r'''_set_attribute_vi_int32

        | Sets the value of a ViInt32 property.
        | This is a low-level method that you can use to set the values of
          device-specific properties and inherent IVI properties.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_int32`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_int32`

        Args:
            attribute_id (int): Specifies the ID of a property. From the method panel window, you
                can use this control as follows.

                -  In the method panel window, click on the control or press **Enter**
                   or the spacebar to display a dialog box containing hierarchical list
                   of the available properties. Properties whose value cannot be set are
                   dim. Help text is shown for each property. Select a property by
                   double-clicking on it or by selecting it and then pressing **Enter**.
                -  Read-only properties appear dim in the list box. If you select a
                   read-only property, an error message appears. A ring control at the
                   top of the dialog box allows you to see all IVI properties or only
                   the properties of type ViInt32. If you choose to see all IVI
                   properties, the data types appear to the right of the property names
                   in the list box. Properties with data types other than ViInt32 are
                   dim. If you select a property data type that is dim, LabWindows/CVI
                   transfers you to the method panel for the corresponding method
                   that is consistent with the data type.
                -  If you want to enter a variable name, press **Ctrl**\ +\ **T** to
                   change this ring control to a manual input box. If the property in
                   this ring control has named constants as valid values, you can view
                   the constants by moving to the value control and pressing **Enter**.

            attribute_value (int): Specifies the value to which you want to set the property. If the
                property currently showing in the property ring control has constants
                as valid values, you can view a list of the constants by pressing
                **Enter** on this control. Select a value by double-clicking on it or by
                selecting it and then pressing **Enter**.

                Note:
                Some of the values might not be valid depending upon the current
                settings of the device session.

        '''
        self._interpreter.set_attribute_vi_int32(self._repeated_capability, attribute_id, attribute_value)

    @ivi_synchronized
    def _set_attribute_vi_int64(self, attribute_id, attribute_value):
        r'''_set_attribute_vi_int64

        | Sets the value of a ViInt64 property.
        | This is a low-level method that you can use to set the values of
          device-specific properties and inherent IVI properties.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_int64`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_int64`

        Args:
            attribute_id (int): Specifies the ID of a property. From the method panel window, you
                can use this control as follows.

                -  In the method panel window, click on the control or press **Enter**
                   or the spacebar to display a dialog box containing hierarchical list
                   of the available properties. Properties whose value cannot be set are
                   dim. Help text is shown for each property. Select a property by
                   double-clicking on it or by selecting it and then pressing **Enter**.
                -  Read-only properties appear dim in the list box. If you select a
                   read-only property, an error message appears. A ring control at the
                   top of the dialog box allows you to see all IVI properties or only
                   the properties of type ViReal64. If you choose to see all IVI
                   properties, the data types appear to the right of the property names
                   in the list box. Properties with data types other than ViReal64 are
                   dim. If you select a property data type that is dim, LabWindows/CVI
                   transfers you to the method panel for the corresponding method
                   that is consistent with the data type.
                -  If you want to enter a variable name, press **Ctrl**\ +\ **T** to
                   change this ring control to a manual input box. If the property in
                   this ring control has named constants as valid values, you can view
                   the constants by moving to the value control and pressing **Enter**.

            attribute_value (int): Specifies the value to which you want to set the property. If the
                property currently showing in the property ring control has constants
                as valid values, you can view a list of the constants by pressing
                **Enter** on this control. Select a value by double-clicking on it or by
                selecting it and then pressing **Enter**.

                Note:
                Some of the values might not be valid depending upon the current
                settings of the device session.

        '''
        self._interpreter.set_attribute_vi_int64(self._repeated_capability, attribute_id, attribute_value)

    @ivi_synchronized
    def _set_attribute_vi_real64(self, attribute_id, attribute_value):
        r'''_set_attribute_vi_real64

        | Sets the value of a ViReal64 property.
        | This is a low-level method that you can use to set the values of
          device-specific properties and inherent IVI properties.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_real64`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_real64`

        Args:
            attribute_id (int): Specifies the ID of a property. From the method panel window, you
                can use this control as follows.

                -  In the method panel window, click on the control or press **Enter**
                   or the spacebar to display a dialog box containing hierarchical list
                   of the available properties. Properties whose value cannot be set are
                   dim. Help text is shown for each property. Select a property by
                   double-clicking on it or by selecting it and then pressing **Enter**.
                -  Read-only properties appear dim in the list box. If you select a
                   read-only property, an error message appears. A ring control at the
                   top of the dialog box allows you to see all IVI properties or only
                   the properties of type ViReal64. If you choose to see all IVI
                   properties, the data types appear to the right of the property names
                   in the list box. Properties with data types other than ViReal64 are
                   dim. If you select a property data type that is dim, LabWindows/CVI
                   transfers you to the method panel for the corresponding method
                   that is consistent with the data type.
                -  If you want to enter a variable name, press **Ctrl**\ +\ **T** to
                   change this ring control to a manual input box. If the property in
                   this ring control has named constants as valid values, you can view
                   the constants by moving to the value control and pressing **Enter**.

            attribute_value (float): Specifies the value to which you want to set the property. If the
                property currently showing in the property ring control has constants
                as valid values, you can view a list of the constants by pressing
                **Enter** on this control. Select a value by double-clicking on it or by
                selecting it and then pressing **Enter**.

                Note:
                Some of the values might not be valid depending upon the current
                settings of the device session.

        '''
        self._interpreter.set_attribute_vi_real64(self._repeated_capability, attribute_id, attribute_value)

    @ivi_synchronized
    def _set_attribute_vi_string(self, attribute_id, attribute_value):
        r'''_set_attribute_vi_string

        | Sets the value of a ViString property.
        | This is a low-level method that you can use to set the values of
          device-specific properties and inherent IVI properties.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_string`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_string`

        Args:
            attribute_id (int): Specifies the ID of a property. From the method panel window, you
                can use this control as follows.

                -  In the method panel window, click on the control or press **Enter**
                   or the spacebar to display a dialog box containing hierarchical list
                   of the available properties. Properties whose value cannot be set are
                   dim. Help text is shown for each property. Select a property by
                   double-clicking on it or by selecting it and then pressing **Enter**.
                -  Read-only properties appear dim in the list box. If you select a
                   read-only property, an error message appears. A ring control at the
                   top of the dialog box allows you to see all IVI properties or only
                   the properties of type ViString. If you choose to see all IVI
                   properties, the data types appear to the right of the property names
                   in the list box. Properties with data types other than ViString are
                   dim. If you select a property data type that is dim, LabWindows/CVI
                   transfers you to the method panel for the corresponding method
                   that is consistent with the data type.
                -  If you want to enter a variable name, press **Ctrl**\ +\ **T** to
                   change this ring control to a manual input box. If the property in
                   this ring control has named constants as valid values, you can view
                   the constants by moving to the value control and pressing **Enter**.

            attribute_value (str): Specifies the value to which you want to set the property. If the
                property currently showing in the property ring control has constants
                as valid values, you can view a list of the constants by pressing
                **Enter** on this control. Select a value by double-clicking on it or by
                selecting it and then pressing **Enter**.

                Note:
                Some of the values might not be valid depending upon the current
                settings of the device session.

        '''
        self._interpreter.set_attribute_vi_string(self._repeated_capability, attribute_id, attribute_value)

    @ivi_synchronized
    def set_sequence(self, values, source_delays):
        r'''set_sequence

        Configures a series of voltage or current outputs and corresponding
        source delays. The source mode must be set to
        `Sequence <REPLACE_DRIVER_SPECIFIC_URL_1(sequencing)>`__ for this
        method to take effect.

        Refer to the `Configuring the Source
        Unit <REPLACE_DRIVER_SPECIFIC_URL_1(configuringthesourceunit)>`__ topic
        in the *NI DC Power Supplies and SMUs Help* for more information about
        how to configure your device.

        Use this method in the Uncommitted or Committed programming states.
        Refer to the `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic in
        the *NI DC Power Supplies and SMUs Help* for more information about
        NI-DCPower programming states.

        Note:
        NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].set_sequence`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.set_sequence`

        Args:
            values (list of float): Specifies the series of voltage levels or current levels, depending on
                the configured `output
                method <REPLACE_DRIVER_SPECIFIC_URL_1(programming_output)>`__.
                **Valid values**:
                The valid values for this parameter are defined by the voltage level
                range or current level range.

            source_delays (list of float): Specifies the source delay that follows the configuration of each value
                in the sequence.
                **Valid Values**:
                The valid values are between 0 and 167 seconds.

        '''
        if source_delays is not None and len(source_delays) != len(values):  # case S160
            raise ValueError("Length of source_delays and values parameters do not match.")  # case S160
        self._interpreter.set_sequence(self._repeated_capability, values, source_delays)

    def unlock(self):
        '''unlock

        Releases a lock that you acquired on an device session using
        lock. Refer to lock for additional
        information on session locks.
        '''
        self._interpreter.unlock()

    @ivi_synchronized
    def wait_for_event(self, event_id, timeout=hightime.timedelta(seconds=10.0)):
        r'''wait_for_event

        Waits until the specified channel(s) have generated the specified event.

        The session monitors whether each type of event has occurred at least
        once since the last time this method or the initiate
        method were called. If an event has only been generated once and you
        call this method successively, the method times out. Individual
        events must be generated between separate calls of this method.

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].wait_for_event`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.wait_for_event`

        Args:
            event_id (enums.Event): Specifies which event to wait for.
                **Defined Values:**

                +-----------------------------------+--------------------------------------------------+
                | Event.SOURCE_COMPLETE             | Waits for the Source Complete event.             |
                +-----------------------------------+--------------------------------------------------+
                | Event.MEASURE_COMPLETE            | Waits for the Measure Complete event.            |
                +-----------------------------------+--------------------------------------------------+
                | Event.SEQUENCE_ITERATION_COMPLETE | Waits for the Sequence Iteration Complete event. |
                +-----------------------------------+--------------------------------------------------+
                | Event.SEQUENCE_ENGINE_DONE        | Waits for the Sequence Engine Done event.        |
                +-----------------------------------+--------------------------------------------------+
                | Event.PULSE_COMPLETE              | Waits for the Pulse Complete event.              |
                +-----------------------------------+--------------------------------------------------+
                | Event.READY_FOR_PULSE_TRIGGER     | Waits for the Ready for Pulse Trigger event.     |
                +-----------------------------------+--------------------------------------------------+

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            timeout (hightime.timedelta, datetime.timedelta, or float in seconds): Specifies the maximum time allowed for this method to complete, in
                seconds. If the method does not complete within this time interval,
                NI-DCPower returns an error.

                Note:
                When setting the timeout interval, ensure you take into account any
                triggers so that the timeout interval is long enough for your
                application.

        '''
        if type(event_id) is not enums.Event:
            raise TypeError('Parameter event_id must be of type ' + str(enums.Event))
        timeout = _converters.convert_timedelta_to_seconds_real64(timeout)
        self._interpreter.wait_for_event(self._repeated_capability, event_id, timeout)

    def _error_message(self, error_code):
        r'''_error_message

        Converts a status code returned by an instrument driver method into a
        user-readable string.

        Args:
            error_code (int): Specifies the **status** parameter that is returned from any of the
                NI-DCPower methods.


        Returns:
            error_message (str): Returns the user-readable message string that corresponds to the status
                code you specify.
                You must pass a ViChar array with at least 256 bytes.

        '''
        error_message = self._interpreter.error_message(error_code)
        return error_message


class Session(_SessionBase):
    '''An NI-DCPower session to an NI programmable power supply or source measure unit.'''

    def __init__(self, resource_name, channels=None, reset=False, options={}, independent_channels=True, *, grpc_options=None):
        r'''An NI-DCPower session to an NI programmable power supply or source measure unit.

        Creates and returns a new NI-DCPower session to the instrument(s) and channel(s) specified
        in **resource name** to be used in all subsequent NI-DCPower method calls. With this method,
        you can optionally set the initial state of the following session properties:

        -  simulate
        -  driver_setup

        After calling this method, the specified channel or channels will be in the Uncommitted
        state.

        To place channel(s) in a known start-up state when creating a new session, set **reset** to
        True. This action is equivalent to using the reset method immediately after initializing the
        session.

        To open a session and leave the channel(s) in an existing configuration without passing
        through a transitional output state, set **reset** to False. Next, configure the channel(s)
        as in the previous session, change the desired settings, and then call the initiate method
        to write both settings.

        **Details of Independent Channel Operation**

        With this method and channel-based NI-DCPower methods and properties, you can use any
        channels in the session independently. For example, you can initiate a subset of channels in
        the session with initiate, and the other channels in the session remain in the Uncommitted
        state.

        When you initialize with independent channels, each channel steps through the NI-DCPower
        programming state model independently of all other channels, and you can specify a subset of
        channels for most operations.

        **Note** You can make concurrent calls to a session from multiple threads, but the session
        executes the calls one at a time. If you specify multiple channels for a method or property,
        the session may perform the operation on multiple channels in parallel, though this is not
        guaranteed, and some operations may execute sequentially.

        Args:
            resource_name (str, list, tuple): Specifies the **resource name** as seen in Measurement
                & Automation Explorer (MAX) or lsni, for example "PXI1Slot3" where "PXI1Slot3" is an
                instrument's **resource name**. If independent_channels is False, **resource name**
                can also be a logical IVI name.

                If independent_channels is True, **resource name** can be names of the instrument(s)
                and the channel(s) to initialize. Specify the instrument(s) and channel(s) using the
                form "PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or
                PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3", where "PXI1Slot3" and "PXI1Slot4" are
                instrument resource names followed by channels. If you exclude a channels string
                after an instrument resource name, all channels of the instrument(s) are included in
                the session.

            channels (str, list, range, tuple): For new applications, use the default value of None
                and specify the channels in **resource name**.

                Specifies which channel(s) to include in a new session. Specify multiple
                channels by using a channel list or a channel range. A channel list is a comma (,)
                separated sequence of channel names (for example, 0,2 specifies channels 0 and 2).
                A channel range is a lower bound channel followed by a hyphen (-) or colon (:)
                followed by an upper bound channel (for example, 0-2 specifies channels 0, 1,
                and 2).

                If independent_channels is False, this argument specifies which channels to include
                in a legacy synchronized channels session. If you do not specify any channels, by
                default all channels on the device are included in the session.

                If independent_channels is True, this argument combines with **resource name** to
                specify which channels to include in an independent channels session. Initializing
                an independent channels session with a channels argument is deprecated.

            reset (bool): Specifies whether to reset channel(s) during the initialization procedure.

            options (dict): Specifies the initial value of certain properties for the session. The
                syntax for **options** is a dictionary of properties with an assigned
                value. For example:

                { 'simulate': False }

                You do not have to specify a value for all the properties. If you do not
                specify a value for a property, the default value is used.

                Advanced Example:
                { 'simulate': True, 'driver_setup': { 'Model': '<model number>',  'BoardType': '<type>' } }

                +-------------------------+---------+
                | Property                | Default |
                +=========================+=========+
                | range_check             | True    |
                +-------------------------+---------+
                | query_instrument_status | False   |
                +-------------------------+---------+
                | cache                   | True    |
                +-------------------------+---------+
                | simulate                | False   |
                +-------------------------+---------+
                | record_value_coersions  | False   |
                +-------------------------+---------+
                | driver_setup            | {}      |
                +-------------------------+---------+

            independent_channels (bool): Specifies whether to initialize the session with
                independent channels. Set this argument to False on legacy applications or if you
                are unable to upgrade your NI-DCPower driver runtime to 20.6 or higher.

            grpc_options (nidcpower.grpc_session_options.GrpcSessionOptions): MeasurementLink gRPC session options


        Returns:
            session (nidcpower.Session): A session object representing the device.

        '''
        if grpc_options:
            import nidcpower._grpc_stub_interpreter as _grpc_stub_interpreter
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
        resource_name = _converters.convert_repeated_capabilities_without_prefix(resource_name)
        channels = _converters.convert_repeated_capabilities_without_prefix(channels)
        options = _converters.convert_init_with_options_dictionary(options)

        # Call specified init function
        # Note that _interpreter default-initializes the session handle in its constructor, so that
        # if _fancy_initialize fails, the error handler can reference it.
        # And then here, once _fancy_initialize succeeds, we call set_session_handle
        # with the actual session handle.
        self._interpreter.set_session_handle(self._fancy_initialize(resource_name, channels, reset, options, independent_channels))

        # Store the parameter list for later printing in __repr__
        param_list = []
        param_list.append("resource_name=" + pp.pformat(resource_name))
        param_list.append("channels=" + pp.pformat(channels))
        param_list.append("reset=" + pp.pformat(reset))
        param_list.append("options=" + pp.pformat(options))
        param_list.append("independent_channels=" + pp.pformat(independent_channels))
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

    def close(self):
        '''close

        Closes the session specified in **vi** and deallocates the resources
        that NI-DCPower reserves. If power output is enabled when you call this
        method, the channels remain in their existing state and
        continue providing power. Use the ConfigureOutputEnabled
        method to disable power output on a per channel basis. Use the
        reset method to disable power output on all channel(s).

        **Related Topics:**

        `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

        Note:
        NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

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
    def disable(self):
        r'''disable

        This method performs the same actions as the reset
        method, except that this method also immediately sets the
        output_enabled property to False.

        This method opens the output relay on devices that have an output
        relay.

        Note:
        NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.
        '''
        self._interpreter.disable()

    @ivi_synchronized
    def export_attribute_configuration_buffer(self):
        r'''export_attribute_configuration_buffer

        Exports the property configuration of the session to the specified
        configuration buffer.

        You can export and import session property configurations only between
        devices with identical model numbers and the same number of configured
        channels.

        This method verifies that the properties you have configured for the
        session are valid. If the configuration is invalid, NI‑DCPower returns
        an error.

        **Support for this Method**

        Calling this method in `Sequence Source
        Mode <REPLACE_DRIVER_SPECIFIC_URL_1(sequencing)>`__ is unsupported.

        **Channel Mapping Behavior for Multichannel Sessions**

        When importing and exporting session property configurations between
        NI‑DCPower sessions that were initialized with different channels, the
        configurations of the exporting channels are mapped to the importing
        channels in the order you specify in the **channelName** input to the
        __init__ method.

        For example, if your entry for **channelName** is 0,1 for the exporting
        session and 1,2 for the importing session:

        -  The configuration exported from channel 0 is imported into channel 1.
        -  The configuration exported from channel 1 is imported into channel 2.

        **Related Topics:**

        `Using Properties and
        Properties <REPLACE_DRIVER_SPECIFIC_URL_1(using_properties_and_attributes)>`__

        `Setting Properties and Properties Before Reading
        Them <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__

        Note:
        This method will return an error if the total number of channels
        initialized for the exporting session is not equal to the total number
        of channels initialized for the importing session.

        Returns:
            configuration (bytes): Specifies the byte array buffer to be populated with the exported
                property configuration.

        '''
        configuration = self._interpreter.export_attribute_configuration_buffer()
        return _converters.convert_to_bytes(configuration)

    @ivi_synchronized
    def export_attribute_configuration_file(self, file_path):
        r'''export_attribute_configuration_file

        Exports the property configuration of the session to the specified
        file.

        You can export and import session property configurations only between
        devices with identical model numbers and the same number of configured
        channels.

        This method verifies that the properties you have configured for the
        session are valid. If the configuration is invalid, NI‑DCPower returns
        an error.

        **Support for this Method**

        Calling this method in `Sequence Source
        Mode <REPLACE_DRIVER_SPECIFIC_URL_1(sequencing)>`__ is unsupported.

        **Channel Mapping Behavior for Multichannel Sessions**

        When importing and exporting session property configurations between
        NI‑DCPower sessions that were initialized with different channels, the
        configurations of the exporting channels are mapped to the importing
        channels in the order you specify in the **channelName** input to the
        __init__ method.

        For example, if your entry for **channelName** is 0,1 for the exporting
        session and 1,2 for the importing session:

        -  The configuration exported from channel 0 is imported into channel 1.
        -  The configuration exported from channel 1 is imported into channel 2.

        **Related Topics:**

        `Using Properties and
        Properties <REPLACE_DRIVER_SPECIFIC_URL_1(using_properties_and_attributes)>`__

        `Setting Properties and Properties Before Reading
        Them <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__

        Note:
        This method will return an error if the total number of channels
        initialized for the exporting session is not equal to the total number
        of channels initialized for the importing session.

        Args:
            file_path (str): Specifies the absolute path to the file to contain the exported
                property configuration. If you specify an empty or relative path, this
                method returns an error.
                **Default file extension:** .nidcpowerconfig

        '''
        self._interpreter.export_attribute_configuration_file(file_path)

    def _fancy_initialize(self, resource_name, channels=None, reset=False, option_string="", independent_channels=True):
        '''_fancy_initialize

        Creates and returns a new NI-DCPower session to the instrument(s) and channel(s) specified
        in **resource name** to be used in all subsequent NI-DCPower method calls. With this method,
        you can optionally set the initial state of the following session properties:

        -  simulate
        -  driver_setup

        After calling this method, the specified channel or channels will be in the Uncommitted
        state.

        To place channel(s) in a known start-up state when creating a new session, set **reset** to
        True. This action is equivalent to using the reset method immediately after initializing the
        session.

        To open a session and leave the channel(s) in an existing configuration without passing
        through a transitional output state, set **reset** to False. Next, configure the channel(s)
        as in the previous session, change the desired settings, and then call the initiate method
        to write both settings.

        **Details of Independent Channel Operation**

        With this method and channel-based NI-DCPower methods and properties, you can use any
        channels in the session independently. For example, you can initiate a subset of channels in
        the session with initiate, and the other channels in the session remain in the Uncommitted
        state.

        When you initialize with independent channels, each channel steps through the NI-DCPower
        programming state model independently of all other channels, and you can specify a subset of
        channels for most operations.

        **Note** You can make concurrent calls to a session from multiple threads, but the session
        executes the calls one at a time. If you specify multiple channels for a method or property,
        the session may perform the operation on multiple channels in parallel, though this is not
        guaranteed, and some operations may execute sequentially.

        Args:
            resource_name (str, list, tuple): Specifies the **resource name** as seen in Measurement
                & Automation Explorer (MAX) or lsni, for example "PXI1Slot3" where "PXI1Slot3" is an
                instrument's **resource name**. If independent_channels is False, **resource name**
                can also be a logical IVI name.

                If independent_channels is True, **resource name** can be names of the instrument(s)
                and the channel(s) to initialize. Specify the instrument(s) and channel(s) using the
                form "PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or
                PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3", where "PXI1Slot3" and "PXI1Slot4" are
                instrument resource names followed by channels. If you exclude a channels string
                after an instrument resource name, all channels of the instrument(s) are included in
                the session.

            channels (str, list, range, tuple): For new applications, use the default value of None
                and specify the channels in **resource name**.

                Specifies which channel(s) to include in a new session. Specify multiple
                channels by using a channel list or a channel range. A channel list is a comma (,)
                separated sequence of channel names (for example, 0,2 specifies channels 0 and 2).
                A channel range is a lower bound channel followed by a hyphen (-) or colon (:)
                followed by an upper bound channel (for example, 0-2 specifies channels 0, 1,
                and 2).

                If independent_channels is False, this argument specifies which channels to include
                in a legacy synchronized channels session. If you do not specify any channels, by
                default all channels on the device are included in the session.

                If independent_channels is True, this argument combines with **resource name** to
                specify which channels to include in an independent channels session. Initializing
                an independent channels session with a channels argument is deprecated.

            reset (bool): Specifies whether to reset channel(s) during the initialization procedure.

            option_string (dict): Specifies the initial value of certain properties for the session.
                The syntax for **optionString** is a list of properties with an assigned value where
                1 is True and 0 is False. For example:

                Simulate=0, DriverSetup=Model:<model number>; BoardType:<bus connector>

                To simulate a multi-instrument session when independent_channels is True, set
                Simulate to 1 and list multiple instruments for DriverSetup. For example:

                Simulate=1, DriverSetup=ResourceName:<instrument name>; Model:<model number>;
                BoardType:<bus connector> & ResourceName:<resource name>; Model:<model number>;
                BoardType:<bus connector>

                You do not have to specify a value for all the properties. If you do not specify a
                value for a property, the default value is used.

            independent_channels (bool): Specifies whether to initialize the session with
                independent channels. Set this argument to False on legacy applications or if you
                are unable to upgrade your NI-DCPower driver runtime to 20.6 or higher.


        Returns:
            vi (int): Returns a session handle that you use to identify the device in all
                subsequent NI-DCPower method calls.

        '''
        if independent_channels:
            resource_string = resource_name  # store potential modifications to resource_name in a separate variable

            if channels:
                # if we have a channels arg, we need to try and combine it with the resource name
                # before calling into initialize with independent channels
                channel_list = (resource_name + "/" + channel for channel in channels.split(","))
                resource_string = ",".join(channel_list)

                import warnings
                warnings.warn(
                    "Attempting to initialize an independent channels session with a channels argument. The resource "
                    "name '" + resource_name + "' will be combined with the channels '" + channels + "' to form the "
                    "fully-qualified channel list '" + resource_string + "'. To avoid this warning, use a "
                    "fully-qualified channel list as the resource name instead of providing a channels argument.",
                    DeprecationWarning
                )

                if "," in resource_name:
                    raise ValueError(
                        "Channels cannot be combined with multiple instruments in the resource name '" + resource_name + "'. "
                        "Specify a list of fully-qualified channels as the resource name instead of supplying a "
                        "channels argument."
                    )

            return self._initialize_with_independent_channels(resource_string, reset, option_string)

        else:
            import warnings
            warnings.warn("Initializing session without independent channels enabled.", DeprecationWarning)

            return self._initialize_with_channels(resource_name, channels, reset, option_string)

    @ivi_synchronized
    def get_channel_name(self, index):
        r'''get_channel_name

        Retrieves the output **channelName** that corresponds to the requested
        **index**. Use the channel_count property to
        determine the upper bound of valid values for **index**.

        Args:
            index (int): Specifies which channel name to return. The index values begin at
                1.


        Returns:
            channel_name (str): Returns the channel name that corresponds to **index**.

        '''
        channel_name = self._interpreter.get_channel_name(index)
        return channel_name

    @ivi_synchronized
    def _get_ext_cal_last_date_and_time(self):
        r'''_get_ext_cal_last_date_and_time

        Returns the date and time of the last successful calibration. The time
        returned is 24-hour (military) local time; for example, if the device
        was calibrated at 2:30 PM, this method returns 14 for **hours** and 30
        for **minutes**.

        Returns:
            year (int): Returns the **year** the device was last calibrated.

            month (int): Returns the **month** in which the device was last calibrated.

            day (int): Returns the **day** on which the device was last calibrated.

            hour (int): Returns the **hour** (in 24-hour time) in which the device was last
                calibrated.

            minute (int): Returns the **minute** in which the device was last calibrated.

        '''
        year, month, day, hour, minute = self._interpreter.get_ext_cal_last_date_and_time()
        return year, month, day, hour, minute

    @ivi_synchronized
    def get_ext_cal_last_temp(self):
        r'''get_ext_cal_last_temp

        Returns the onboard **temperature** of the device, in degrees Celsius,
        during the last successful external calibration.

        Returns:
            temperature (float): Returns the onboard **temperature** of the device, in degrees Celsius,
                during the last successful external calibration.

        '''
        temperature = self._interpreter.get_ext_cal_last_temp()
        return temperature

    @ivi_synchronized
    def get_ext_cal_recommended_interval(self):
        r'''get_ext_cal_recommended_interval

        Returns the recommended maximum interval, in **months**, between
        external calibrations.

        Returns:
            months (hightime.timedelta): Specifies the recommended maximum interval, in **months**, between
                external calibrations.

        '''
        months = self._interpreter.get_ext_cal_recommended_interval()
        return _converters.convert_month_to_timedelta(months)

    @ivi_synchronized
    def get_ext_cal_last_date_and_time(self):
        '''get_ext_cal_last_date_and_time

        Returns the date and time of the last successful calibration.

        Returns:
            last_cal_datetime (hightime.datetime): Indicates date and time of the last calibration.

        '''
        year, month, day, hour, minute = self._get_ext_cal_last_date_and_time()
        return hightime.datetime(year, month, day, hour, minute)

    @ivi_synchronized
    def get_self_cal_last_date_and_time(self):
        '''get_self_cal_last_date_and_time

        Returns the date and time of the oldest successful self-calibration from among the channels in the session.

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Returns:
            last_cal_datetime (hightime.datetime): Returns the date and time the device was last calibrated.

        '''
        year, month, day, hour, minute = self._get_self_cal_last_date_and_time()
        return hightime.datetime(year, month, day, hour, minute)

    @ivi_synchronized
    def _get_self_cal_last_date_and_time(self):
        r'''_get_self_cal_last_date_and_time

        Returns the date and time of the oldest successful self-calibration from
        among the channels in the session.

        The time returned is 24-hour (military) local time; for example, if you
        have a session using channels 1 and 2, and a self-calibration was
        performed on channel 1 at 2:30 PM, and a self-calibration was performed
        on channel 2 at 3:00 PM on the same day, this method returns 14 for
        **hours** and 30 for **minutes**.

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Returns:
            year (int): Returns the **year** the device was last calibrated.

            month (int): Returns the **month** in which the device was last calibrated.

            day (int): Returns the **day** on which the device was last calibrated.

            hour (int): Returns the **hour** (in 24-hour time) in which the device was last
                calibrated.

            minute (int): Returns the **minute** in which the device was last calibrated.

        '''
        year, month, day, hour, minute = self._interpreter.get_self_cal_last_date_and_time()
        return year, month, day, hour, minute

    @ivi_synchronized
    def get_self_cal_last_temp(self):
        r'''get_self_cal_last_temp

        Returns the onboard temperature of the device, in degrees Celsius,
        during the oldest successful self-calibration from among the channels in
        the session.

        For example, if you have a session using channels 1 and 2, and you
        perform a self-calibration on channel 1 with a device temperature of 25
        degrees Celsius at 2:00, and a self-calibration was performed on channel
        2 at 27 degrees Celsius at 3:00 on the same day, this method returns
        25 for the **temperature** parameter.

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Returns:
            temperature (float): Returns the onboard **temperature** of the device, in degrees Celsius,
                during the oldest successful calibration.

        '''
        temperature = self._interpreter.get_self_cal_last_temp()
        return temperature

    @ivi_synchronized
    def import_attribute_configuration_buffer(self, configuration):
        r'''import_attribute_configuration_buffer

        Imports a property configuration to the session from the specified
        configuration buffer.

        You can export and import session property configurations only between
        devices with identical model numbers and the same number of configured
        channels.

        **Support for this Method**

        Calling this method in `Sequence Source
        Mode <REPLACE_DRIVER_SPECIFIC_URL_1(sequencing)>`__ is unsupported.

        **Channel Mapping Behavior for Multichannel Sessions**

        When importing and exporting session property configurations between
        NI‑DCPower sessions that were initialized with different channels, the
        configurations of the exporting channels are mapped to the importing
        channels in the order you specify in the **channelName** input to the
        __init__ method.

        For example, if your entry for **channelName** is 0,1 for the exporting
        session and 1,2 for the importing session:

        -  The configuration exported from channel 0 is imported into channel 1.
        -  The configuration exported from channel 1 is imported into channel 2.

        **Related Topics:**

        `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

        `Using Properties and
        Properties <REPLACE_DRIVER_SPECIFIC_URL_1(using_properties_and_attributes)>`__

        `Setting Properties and Properties Before Reading
        Them <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__

        Note:
        This method will return an error if the total number of channels
        initialized for the exporting session is not equal to the total number
        of channels initialized for the importing session.

        Args:
            configuration (bytes): Specifies the byte array buffer that contains the property
                configuration to import.

        '''
        configuration = _converters.convert_to_bytes(configuration)
        self._interpreter.import_attribute_configuration_buffer(configuration)

    @ivi_synchronized
    def import_attribute_configuration_file(self, file_path):
        r'''import_attribute_configuration_file

        Imports a property configuration to the session from the specified
        file.

        You can export and import session property configurations only between
        devices with identical model numbers and the same number of configured
        channels.

        **Support for this Method**

        Calling this method in `Sequence Source
        Mode <REPLACE_DRIVER_SPECIFIC_URL_1(sequencing)>`__ is unsupported.

        **Channel Mapping Behavior for Multichannel Sessions**

        When importing and exporting session property configurations between
        NI‑DCPower sessions that were initialized with different channels, the
        configurations of the exporting channels are mapped to the importing
        channels in the order you specify in the **channelName** input to the
        __init__ method.

        For example, if your entry for **channelName** is 0,1 for the exporting
        session and 1,2 for the importing session:

        -  The configuration exported from channel 0 is imported into channel 1.
        -  The configuration exported from channel 1 is imported into channel 2.

        **Related Topics:**

        `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

        `Using Properties and
        Properties <REPLACE_DRIVER_SPECIFIC_URL_1(using_properties_and_attributes)>`__

        `Setting Properties and Properties Before Reading
        Them <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__

        Note:
        This method will return an error if the total number of channels
        initialized for the exporting session is not equal to the total number
        of channels initialized for the importing session.

        Args:
            file_path (str): Specifies the absolute path to the file containing the property
                configuration to import. If you specify an empty or relative path, this
                method returns an error.
                **Default File Extension:** .nidcpowerconfig

        '''
        self._interpreter.import_attribute_configuration_file(file_path)

    def _initialize_with_channels(self, resource_name, channels, reset, option_string):
        r'''_initialize_with_channels

        Creates and returns a new NI-DCPower session to the instrument
        specified in **resource name** to be used in all subsequent NI-DCPower
        method calls. With this method, you can optionally set the initial
        state of the following session properties:

        -  simulate
        -  driver_setup

        After calling this method, the session will be in the Uncommitted
        state. Refer to the `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic for
        details about specific software states.

        To place the device in a known start-up state when creating a new
        session, set **reset** to True. This action is equivalent to using
        the reset method immediately after initializing the
        session.

        To open a session and leave the device in its existing configuration
        without passing through a transitional output state, set **reset** to
        False. Then configure the device as in the previous session,
        changing only the desired settings, and then call the
        initiate method.

        **Related Topics:**

        `Programming States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

        Args:
            resource_name (str): Specifies the **resourceName** assigned by Measurement & Automation
                Explorer (MAX), for example "PXI1Slot3" where "PXI1Slot3" is an
                instrument's **resourceName**. **resourceName** can also be a logical
                IVI name.

            channels (str): Specifies which channel(s) to include in a new session. Specify
                multiple channels by using a channel list or a channel range. A channel
                list is a comma (,) separated sequence of channel names (for example,
                0,2 specifies channels 0 and 2). A channel range is a lower bound
                channel followed by a hyphen (-) or colon (:) followed by an upper bound
                channel (for example, 0-2 specifies channels 0, 1, and 2). In the
                Running state, multiple channel configurations are performed
                sequentially based on the order specified in this parameter. If you do
                not specify any channels, by default all channels on the device are
                included in the session.

            reset (bool): Specifies whether to reset the device during the initialization
                procedure.

            option_string (str): Specifies the initial value of certain properties for the session.
                The syntax for **optionString** is a list of properties with an assigned
                value where 1 is True and 0 is False. For example:

                "Simulate=0"

                You do not have to specify a value for all the properties. If you do not
                specify a value for a property, the default value is used.

                For more information about simulating a device, refer to `Simulating an
                Instrument <REPLACE_DRIVER_SPECIFIC_URL_1(simulate)>`__.


        Returns:
            vi (int): Returns a session handle that you use to identify the device in all
                subsequent NI-DCPower method calls.

        '''
        vi = self._interpreter.initialize_with_channels(resource_name, channels, reset, option_string)
        return vi

    def _initialize_with_independent_channels(self, resource_name, reset, option_string):
        r'''_initialize_with_independent_channels

        Creates a new NI-DCPower session to the specified instrument(s) and channel(s) and returns a
        session handle to be used in all subsequent NI-DCPower method calls.

        After calling this method, the specified channel or channels will be in the Uncommitted
        state.

        With this method and channel-based NI-DCPower methods and properties, you can use any
        channels in the session independently. For example, you can initiate a subset of channels in
        the session with initiate, and the other channels in the session
        remain in the Uncommitted state.

        **Details of Independent Channel Operation**

        When you initialize with independent channels, each channel steps through the NI-DCPower
        programming state model independently of all other channels, and you can specify a subset
        of channels for most operations.

        **Note** You can make concurrent calls to a session from multiple threads, but the session
        executes the calls one at a time. If you specify multiple channels for a method or
        property, the session may perform the operation on multiple channels in parallel, though
        this is not guaranteed, and some operations may execute sequentially.

        **Related Topics:**

        `Programming States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

        Args:
            resource_name (str): Specifies the NI-DCPower resources to use in the session.
                NI-DCPower resources can be names of the instrument(s) assigned by Measurement &
                Automation Explorer (MAX) and the channel(s) to initialize. Specify the
                instrument(s) and channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3
                or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are
                instrument resource names and 0, 2, and 3 are channels.

                If you pass "" for this control, all channels of the instrument(s) are included in
                the session.

            reset (bool): Specifies whether to reset channel(s) during the initialization procedure.
                The default is False.

                To place channel(s) in a known startup state when creating a new session, set
                **reset** to True. This action is equivalent to using the reset
                method immediately after initializing the session.

                To open a session and leave the channel(s) in an existing configuration without
                passing through a transitional output state, set **reset** to False. Next, configure
                the channel(s) as in the previous session, change the desired settings, and then
                call the initiate method to write both settings.

            option_string (str): Specifies the initial value of certain properties for the session.
                The syntax for **optionString** is a list of properties with an assigned value where
                1 is True and 0 is False. For example:

                Simulate=0, DriverSetup=Model:<model number>; BoardType:<bus connector>

                To simulate a multi-instrument session, set Simulate to 1 and list multiple
                instruments for DriverSetup. For example:

                Simulate=1, DriverSetup=ResourceName:<instrument name>; Model:<model number>;
                BoardType:<bus connector> & ResourceName:<resource name>; Model:<model number>;
                BoardType:<bus connector>

                You do not have to specify a value for all the properties. If you do not specify a
                value for a property, the default value is used.

                For more information about simulating a device, refer to `Simulating an
                Instrument <REPLACE_DRIVER_SPECIFIC_URL_1(simulate)>`__.


        Returns:
            vi (int): Returns a session handle that you use to identify the session in all
                subsequent NI-DCPower method calls.

        '''
        vi = self._interpreter.initialize_with_independent_channels(resource_name, reset, option_string)
        return vi

    @ivi_synchronized
    def get_channel_names(self, indices):
        '''get_channel_names

        Returns a list of channel names for the given channel indices.

        Args:
            indices (basic sequence types or str or int): Index list for the channels in the session. Valid values are from zero to the total number of channels in the session minus one. The index string can be one of the following formats:

                -   A comma-separated list—for example, "0,2,3,1"
                -   A range using a hyphen—for example, "0-3"
                -   A range using a colon—for example, "0:3 "

                You can combine comma-separated lists and ranges that use a hyphen or colon. Both out-of-order and repeated indices are supported ("2,3,0," "1,2,2,3"). White space characters, including spaces, tabs, feeds, and carriage returns, are allowed between characters. Ranges can be incrementing or decrementing.


        Returns:
            names (list of str): The channel name(s) at the specified indices.

        '''
        return self._get_channel_names(indices)

    @ivi_synchronized
    def read_current_temperature(self):
        r'''read_current_temperature

        Returns the current onboard **temperature**, in degrees Celsius, of the
        device.

        Returns:
            temperature (float): Returns the onboard **temperature**, in degrees Celsius, of the device.

        '''
        temperature = self._interpreter.read_current_temperature()
        return temperature

    @ivi_synchronized
    def reset_device(self):
        r'''reset_device

        Resets the device to a known state. The method disables power
        generation, resets session properties to their default values, clears
        errors such as overtemperature and unexpected loss of auxiliary power,
        commits the session properties, and leaves the session in the
        Uncommitted state. This method also performs a hard reset on the
        device and driver software. This method has the same functionality as
        using reset in Measurement & Automation Explorer. Refer to the
        `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic for
        more information about NI-DCPower software states.

        This will also open the output relay on devices that have an output
        relay.

        Note:
        NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.
        '''
        self._interpreter.reset_device()

    @ivi_synchronized
    def reset_with_defaults(self):
        r'''reset_with_defaults

        Resets the device to a known state. This method disables power
        generation, resets session properties to their default values, commits
        the session properties, and leaves the session in the
        `Running <javascript:LaunchHelp('NI_DC_Power_Supplies_Help.chm::/programmingStates.html#running')>`__
        state. In addition to exhibiting the behavior of the reset
        method, this method can assign user-defined default values for
        configurable properties from the IVI configuration.
        '''
        self._interpreter.reset_with_defaults()

    def _close(self):
        r'''_close

        Closes the session specified in **vi** and deallocates the resources
        that NI-DCPower reserves. If power output is enabled when you call this
        method, the channels remain in their existing state and
        continue providing power. Use the ConfigureOutputEnabled
        method to disable power output on a per channel basis. Use the
        reset method to disable power output on all channel(s).

        **Related Topics:**

        `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

        Note:
        NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

        Note:
        One or more of the referenced methods are not in the Python API for this driver.
        '''
        self._interpreter.close()

    @ivi_synchronized
    def self_test(self):
        '''self_test

        Performs the device self-test routine and returns the test result(s).
        Calling this method implicitly calls the reset method.

        When calling self_test with the PXIe-4162/4163, specify all
        channels of your PXIe-4162/4163 with the channels input of
        __init__. You cannot self test a subset of
        PXIe-4162/4163 channels.

        Raises `SelfTestError` on self test failure. Properties on exception object:

        - code - failure code from driver
        - message - status message from driver

        +----------------+-------------------+
        | Self-Test Code | Description       |
        +================+===================+
        | 0              | Self test passed. |
        +----------------+-------------------+
        | 1              | Self test failed. |
        +----------------+-------------------+
        '''
        code, msg = self._self_test()
        if code:
            raise errors.SelfTestError(code, msg)
        return None

    @ivi_synchronized
    def _self_test(self):
        r'''_self_test

        Performs the device self-test routine and returns the test result(s).
        Calling this method implicitly calls the reset method.

        When calling self_test with the PXIe-4162/4163, specify all
        channels of your PXIe-4162/4163 with the channels input of
        __init__. You cannot self test a subset of
        PXIe-4162/4163 channels.

        Returns:
            self_test_result (int): Returns the value result from the device self-test.

                +----------------+-------------------+
                | Self-Test Code | Description       |
                +================+===================+
                | 0              | Self test passed. |
                +----------------+-------------------+
                | 1              | Self test failed. |
                +----------------+-------------------+

            self_test_message (str): Returns the self-test result message. The size of this array must be at
                least 256 bytes.

        '''
        self_test_result, self_test_message = self._interpreter.self_test()
        return self_test_result, self_test_message
