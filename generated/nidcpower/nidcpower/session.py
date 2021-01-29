# -*- coding: utf-8 -*-
# This file was generated
import array  # noqa: F401
import ctypes
# Used by @ivi_synchronized
from functools import wraps

import nidcpower._attributes as _attributes
import nidcpower._converters as _converters
import nidcpower._library_singleton as _library_singleton
import nidcpower._visatype as _visatype
import nidcpower.enums as enums
import nidcpower.errors as errors

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


class _Acquisition(object):
    def __init__(self, session):
        self._session = session
        self._session._initiate()

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

        return _SessionBase(vi=self._session._vi, repeated_capability_list=complete_rep_cap_list, library=self._session._library, encoding=self._session._encoding, freeze_it=True)


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

    Note: This property is not supported by all devices. Refer to Supported Properties by Device topic.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    active_advanced_sequence_step = _attributes.AttributeViInt64(1150075)
    '''Type: int

    Specifies the advanced sequence step to configure.

    Note: This property is not supported by all devices. Refer to Supported Properties by Device topic.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    actual_power_allocation = _attributes.AttributeViReal64(1150205)
    '''Type: float

    Returns the power, in watts, the device is sourcing on each active channel if the power_allocation_mode property is set to PowerAllocationMode.AUTOMATIC or PowerAllocationMode.MANUAL.

     Valid Values: [0, device per-channel maximum power]

     Default Value: Refer to the Supported Properties by Device topic for the default value by device.

    Note: This property is not supported by all devices. Refer to the Supported Properties by Device topic for information about supported devices.

     This property returns -1 when the power_allocation_mode property is set to PowerAllocationMode.DISABLED.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    aperture_time = _attributes.AttributeViReal64(1150058)
    '''Type: float

    Specifies the measurement aperture time for the channel configuration. Aperture time is specified in the units set by  the aperture_time_units property.
    for information about supported devices.
    Refer to the Aperture Time topic in the NI DC Power Supplies and SMUs Help for more information about how to configure  your measurements and for information about valid values.
    Default Value: 0.01666666 seconds

    Note: This property is not supported by all devices. Refer to Supported Properties by Device topic

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    aperture_time_units = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.ApertureTimeUnits, 1150059)
    '''Type: enums.ApertureTimeUnits

    Specifies the units of the aperture_time property for the channel configuration.
    for information about supported devices.
    Refer to the Aperture Time topic in the NI DC Power Supplies and SMUs Help for more information about  how to configure your measurements and for information about valid values.
    Default Value: ApertureTimeUnits.SECONDS

    Note: This property is not supported by all devices. Refer to Supported Properties by Device topic

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    autorange = _attributes.AttributeViInt32(1150244)
    '''Type: bool

    Specifies whether the hardware automatically selects the best range to measure the signal.  Note the highest range the algorithm uses is dependent on the corresponding limit range property. The algorithm the hardware uses can be controlled using the autorange_aperture_time_mode property.

    Note: Autoranging begins at module startup and remains active until the module is reconfigured or reset.  This property is not supported by all devices. Refer to Supported Properties by Device topic.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    autorange_aperture_time_mode = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.AutorangeApertureTimeMode, 1150246)
    '''Type: enums.AutorangeApertureTimeMode

    Specifies whether the aperture time used for the measurement autorange algorithm is determined automatically or customized using the autorange_minimum_aperture_time property.

    Note: This property is not supported by all devices. Refer to Supported Properties by Device topic.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    autorange_behavior = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.AutorangeBehavior, 1150245)
    '''Type: enums.AutorangeBehavior

    Specifies the algorithm the hardware uses for measurement autoranging.

    Note: This property is not supported by all devices. Refer to Supported Properties by Device topic.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    autorange_minimum_aperture_time = _attributes.AttributeViReal64(1150247)
    '''Type: float

    Specifies the measurement autorange aperture time used for the measurement autorange algorithm.  The aperture time is specified in the units set by the autorange_minimum_aperture_time_units property. This value will typically be smaller than the aperture time used for measurements.

    Note: For smaller ranges, the value is scaled up to account for noise. The factor used to scale the value is derived from the module capabilities.  This property is not supported by all devices. Refer to Supported Properties by Device topic.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    autorange_minimum_aperture_time_units = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.ApertureTimeUnits, 1150248)
    '''Type: enums.ApertureTimeUnits

    Specifies the units of the autorange_minimum_aperture_time property.

    Note: This property is not supported by all devices. Refer to Supported Properties by Device topic.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    autorange_minimum_current_range = _attributes.AttributeViReal64(1150255)
    '''Type: float

    Specifies the lowest range used during measurement autoranging.  Limiting the lowest range used during autoranging can improve the speed of the autoranging algorithm and minimize frequent and unpredictable range changes for noisy signals.

    Note: The maximum range used is the range that includes the value specified in the compliance limit property, voltage_limit_range property or current_limit_range property, depending on the selected output_function. This property is not supported by all devices. Refer to Supported Properties by Device topic.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    autorange_minimum_voltage_range = _attributes.AttributeViReal64(1150256)
    '''Type: float

    Specifies the lowest range used during measurement autoranging. The maximum range used is range that includes the value specified in the compliance limit property. Limiting the lowest range used during autoranging can improve the speed of the autoranging algorithm and/or minimize thrashing between ranges for noisy signals.

    Note: The maximum range used is the range that includes the value specified in the compliance limit property, voltage_limit_range property or current_limit_range property, depending on the selected output_function. This property is not supported by all devices. Refer to Supported Properties by Device topic.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    autorange_threshold_mode = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.AutorangeThresholdMode, 1150257)
    '''Type: enums.AutorangeThresholdMode

    Specifies thresholds used during autoranging to determine when range changing occurs.

    Note: This property is not supported by all devices. Refer to Supported Properties by Device topic.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    auto_zero = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.AutoZero, 1150055)
    '''Type: enums.AutoZero

    Specifies the auto-zero method to use on the device.
    Refer to the NI PXI-4132 Measurement Configuration and Timing and Auto Zero topics for more information  about how to configure your measurements.
    Default Value: The default value for the NI PXI-4132 is AutoZero.ON. The default value for  all other devices is AutoZero.OFF, which is the only supported value for these devices.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    auxiliary_power_source_available = _attributes.AttributeViBoolean(1150002)
    '''Type: bool

    Indicates whether an auxiliary power source is connected to the device.
    A value of False may indicate that the auxiliary input fuse has blown.  Refer to the Detecting Internal/Auxiliary Power topic in the NI DC Power Supplies and SMUs Help for  more information about internal and auxiliary power.
    power source to generate power. Use the power_source_in_use property to retrieve this information.

    Note: This property does not necessarily indicate if the device is using the auxiliary

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    channel_count = _attributes.AttributeViInt32(1050203)
    '''Type: int

    Indicates the number of channels that NI-DCPower supports for the instrument that was chosen when  the current session was opened. For channel-based properties, the IVI engine maintains a separate  cache value for each channel.
    '''
    compliance_limit_symmetry = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.ComplianceLimitSymmetry, 1150184)
    '''Type: enums.ComplianceLimitSymmetry

    Specifies whether compliance limits for current generation and voltage
    generation for the device are applied symmetrically about 0 V and 0 A or
    asymmetrically with respect to 0 V and 0 A.
    When set to **Symmetric**, voltage limits and current limits are set
    using a single property with a positive value. The resulting range is
    bounded by this positive value and its opposite.
    When set to **Asymmetric**, you must separately set a limit high and a
    limit low using distinct properties.
    For asymmetric limits, the range bounded by the limit high and limit low
    must include zero.
    **Default Value:** Symmetric
    **Related Topics:**
    `Compliance <NI_DC_Power_Supplies_Help.chm::/compliance.html>`__
    `Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
    `Changing
    Ranges <NI_DC_Power_Supplies_Help.chm::/changing_ranges.html>`__
    `Overranging <NI_DC_Power_Supplies_Help.chm::/overranging.html>`__

    Note:
    Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    current_compensation_frequency = _attributes.AttributeViReal64(1150071)
    '''Type: float

    The frequency at which a pole-zero pair is added to the system when the channel is in  Constant Current mode.
    for information about supported devices.
    Default Value: Determined by the value of the TransientResponse.NORMAL setting of the  transient_response property.

    Note: This property is not supported by all devices. Refer to Supported Properties by Device topic

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    current_gain_bandwidth = _attributes.AttributeViReal64(1150070)
    '''Type: float

    The frequency at which the unloaded loop gain extrapolates to 0 dB in the absence of additional poles and zeroes.  This property takes effect when the channel is in Constant Current mode.
    for information about supported devices.
    Default Value: Determined by the value of the TransientResponse.NORMAL setting of the  transient_response property.

    Note: This property is not supported by all devices. Refer to Supported Properties by Device topic

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    current_level = _attributes.AttributeViReal64(1150009)
    '''Type: float

    Specifies the current level, in amps, that the device attempts to generate on the specified channel(s).
    This property is applicable only if the output_function property is set to OutputFunction.DC_CURRENT.
    output_enabled property for more information about enabling the output channel.
    Valid Values: The valid values for this property are defined by the values to which the  current_level_range property is set.

    Note: The channel must be enabled for the specified current level to take effect. Refer to the

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    current_level_autorange = _attributes.AttributeViInt32(1150017)
    '''Type: bool

    Specifies whether NI-DCPower automatically selects the current level range based on the desired current level for  the specified channels.
    If you set this property to AutoZero.ON, NI-DCPower ignores any changes you make to the  current_level_range property. If you change the current_level_autorange property from  AutoZero.ON to AutoZero.OFF, NI-DCPower retains the last value the current_level_range  property was set to (or the default value if the property was never set) and uses that value as the  current level range.
    Query the current_level_range property by using the _get_attribute_vi_int32 method for  information about which range NI-DCPower automatically selects.
    The current_level_autorange property is applicable only if the output_function property  is set to OutputFunction.DC_CURRENT.
    Default Value: AutoZero.OFF

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    current_level_range = _attributes.AttributeViReal64(1150011)
    '''Type: float

    Specifies the current level range, in amps, for the specified channel(s).
    The range defines the valid value to which the current level can be set. Use the  current_level_autorange property to enable automatic selection of the current level range.
    The current_level_range property is applicable only if the output_function property is  set to OutputFunction.DC_CURRENT.
    output_enabled property for more information about enabling the output channel.
    For valid ranges, refer to the Ranges topic for your device in the NI DC Power Supplies and SMUs Help.

    Note: The channel must be enabled for the specified current level range to take effect. Refer to the

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    current_limit = _attributes.AttributeViReal64(1250005)
    '''Type: float

    Specifies the current limit, in amps, that the output cannot exceed when generating the desired voltage level  on the specified channel(s).
    This property is applicable only if the output_function property is set to  OutputFunction.DC_VOLTAGE and the compliance_limit_symmetry property is set to  ComplianceLimitSymmetry.SYMMETRIC.
    output_enabled property for more information about enabling the output channel.
    Valid Values: The valid values for this property are defined by the values to which  current_limit_range property is set.

    Note: The channel must be enabled for the specified current limit to take effect. Refer to the

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    current_limit_autorange = _attributes.AttributeViInt32(1150016)
    '''Type: bool

    Specifies whether NI-DCPower automatically selects the current limit range based on the desired current limit for the  specified channel(s).
    If you set this property to AutoZero.ON, NI-DCPower ignores any changes you make to the  current_limit_range property. If you change this property from AutoZero.ON to  AutoZero.OFF, NI-DCPower retains the last value the current_limit_range property was set to  (or the default value if the property was never set) and uses that value as the current limit range.
    Query the current_limit_range property by using the _get_attribute_vi_int32 method for  information about which range NI-DCPower automatically selects.
    The current_limit_autorange property is applicable only if the output_function property  is set to OutputFunction.DC_VOLTAGE.
    Default Value: AutoZero.OFF

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    current_limit_behavior = _attributes.AttributeViInt32(1250004)
    '''Type: int

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    current_limit_high = _attributes.AttributeViReal64(1150187)
    '''Type: float

    Specifies the maximum current, in amps, that the output can produce when
    generating the desired voltage on the specified channel(s).
    This property is applicable only if the `Compliance Limit
    Symmetry <pComplianceLimitSymmetry.html>`__ property is set to
    **Asymmetric** and the `Output
    Method <pOutputFunction.html>`__ property is set to **DC
    Voltage**.
    You must also specify a `Current Limit
    Low <pCurrentLimitLow.html>`__ to complete the asymmetric
    range.
    **Valid Values:** [1% of `Current Limit
    Range <pCurrentLimitRange.html>`__, `Current Limit
    Range <pCurrentLimitRange.html>`__]
    The range bounded by the limit high and limit low must include zero.
    **Default Value:** Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.
    **Related Topics:**
    `Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
    `Changing
    Ranges <NI_DC_Power_Supplies_Help.chm::/changing_ranges.html>`__
    `Overranging <NI_DC_Power_Supplies_Help.chm::/overranging.html>`__

    Note:
    The limit may be extended beyond the selected limit range if the
    `Overranging Enabled <pOverrangingEnabled.html>`__ property is
    set to TRUE.

    Note:
    One or more of the referenced methods are not in the Python API for this driver.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    current_limit_low = _attributes.AttributeViReal64(1150188)
    '''Type: float

    Specifies the minimum current, in amps, that the output can produce when
    generating the desired voltage on the specified channel(s).
    This property is applicable only if the `Compliance Limit
    Symmetry <pComplianceLimitSymmetry.html>`__ property is set to
    **Asymmetric** and the `Output
    Method <pOutputFunction.html>`__ property is set to **DC
    Voltage**.
    You must also specify a `Current Limit
    High <pCurrentLimitHigh.html>`__ to complete the asymmetric
    range.
    **Valid Values:** [-`Current Limit
    Range <pCurrentLimitRange.html>`__, -1% of `Current Limit
    Range <pCurrentLimitRange.html>`__]
    The range bounded by the limit high and limit low must include zero.
    **Default Value:** Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.
    **Related Topics:**
    `Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
    `Changing
    Ranges <NI_DC_Power_Supplies_Help.chm::/changing_ranges.html>`__
    `Overranging <NI_DC_Power_Supplies_Help.chm::/overranging.html>`__

    Note:
    The limit may be extended beyond the selected limit range if the
    `Overranging Enabled <pOverrangingEnabled.html>`__ property is
    set to TRUE.

    Note:
    One or more of the referenced methods are not in the Python API for this driver.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    current_limit_range = _attributes.AttributeViReal64(1150004)
    '''Type: float

    Specifies the current limit range, in amps, for the specified channel(s).
    The range defines the valid value to which the current limit can be set. Use the current_limit_autorange  property to enable automatic selection of the current limit range.
    The current_limit_range property is applicable only if the output_function property  is set to OutputFunction.DC_VOLTAGE.
    output_enabled property for more information about enabling the output channel.
    For valid ranges, refer to the Ranges topic for your device in the NI DC Power Supplies and SMUs Help.

    Note: The channel must be enabled for the specified current limit to take effect. Refer to the

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    current_pole_zero_ratio = _attributes.AttributeViReal64(1150072)
    '''Type: float

    The ratio of the pole frequency to the zero frequency when the channel is in  Constant Current mode.
    for information about supported devices.
    Default Value: Determined by the value of the TransientResponse.NORMAL setting of the transient_response property.

    Note: This property is not supported by all devices. Refer to Supported Properties by Device topic

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    dc_noise_rejection = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.DCNoiseRejection, 1150066)
    '''Type: enums.DCNoiseRejection

    Determines the relative weighting of samples in a measurement. Refer to the NI PXIe-4140/4141 DC Noise Rejection,  NI PXIe-4142/4143 DC Noise Rejection, or NI PXIe-4144/4145 DC Noise Rejection topic in the NI DC Power Supplies  and SMUs Help for more information about noise rejection.
    for information about supported devices.
    Default Value: TransientResponse.NORMAL

    Note: This property is not supported by all devices. Refer to Supported Properties by Device topic

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    digital_edge_measure_trigger_input_terminal = _attributes.AttributeViString(1150036)
    '''Type: str

    Specifies the input terminal for the Measure trigger. This property is used only when the  measure_trigger_type property is set to TriggerType.DIGITAL_EDGE.
    for this property.
    You can specify any valid input terminal for this property. Valid terminals are listed in  Measurement & Automation Explorer under the Device Routes tab.
    Input terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you  can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal  name, PXI_Trig0. The input terminal can also be a terminal from another device. For example, you can set the input  terminal on Dev1 to be /Dev2/SourceCompleteEvent.

    Note: This property is not supported by all devices. Refer to Supported Properties by Device topic

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    digital_edge_pulse_trigger_input_terminal = _attributes.AttributeViString(1150097)
    '''Type: str

    Specifies the input terminal for the Pulse trigger. This property is used only when the pulse_trigger_type property is set to digital edge.
    You can specify any valid input terminal for this property. Valid terminals are listed in Measurement & Automation Explorer under the Device Routes tab.
    Input terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0. The input terminal can also be a terminal from another device. For example, you can set the input terminal on Dev1 to be /Dev2/SourceCompleteEvent.

    Note: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    digital_edge_sequence_advance_trigger_input_terminal = _attributes.AttributeViString(1150028)
    '''Type: str

    Specifies the input terminal for the Sequence Advance trigger. Use this property only when the  sequence_advance_trigger_type property is set to TriggerType.DIGITAL_EDGE.
    the NI DC Power Supplies and SMUs Help for information about supported devices.
    You can specify any valid input terminal for this property. Valid terminals are listed in Measurement & Automation Explorer under the Device Routes tab.
    Input terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can  specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal  name, PXI_Trig0. The input terminal can also be a terminal from another device. For example, you can set the  input terminal on Dev1 to be /Dev2/SourceCompleteEvent.

    Note: This property is not supported by all devices. Refer to Supported Properties by Device topic in

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    digital_edge_shutdown_trigger_input_terminal = _attributes.AttributeViString(1150277)
    '''Type: str

    Specifies the input terminal for the Shutdown trigger. This property is used only when the shutdown_trigger_type property is set to digital edge.
    You can specify any valid input terminal for this property. Valid terminals are listed in Measurement & Automation Explorer under the Device Routes tab.
    Input terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0. The input terminal can also be a terminal from another device. For example, you can set the input terminal on Dev1 to be /Dev2/SourceCompleteEvent.

    Note: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    digital_edge_source_trigger_input_terminal = _attributes.AttributeViString(1150032)
    '''Type: str

    Specifies the input terminal for the Source trigger. Use this property only when the  source_trigger_type property is set to TriggerType.DIGITAL_EDGE.
    for information about supported devices.
    You can specify any valid input terminal for this property. Valid terminals are listed  in Measurement & Automation Explorer under the Device Routes tab.
    Input terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you  can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal  name, PXI_Trig0. The input terminal can also be a terminal from another device. For example, you can set the input  terminal on Dev1 to be /Dev2/SourceCompleteEvent.

    Note: This property is not supported by all devices. Refer to Supported Properties by Device topic

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    digital_edge_start_trigger_input_terminal = _attributes.AttributeViString(1150023)
    '''Type: str

    Specifies the input terminal for the Start trigger. Use this property only when the start_trigger_type  property is set to TriggerType.DIGITAL_EDGE.
    for information about supported devices.
    You can specify any valid input terminal for this property. Valid terminals are listed in Measurement & Automation  Explorer under the Device Routes tab.
    Input terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can  specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name,  PXI_Trig0. The input terminal can also be a terminal from another device. For example, you can set the input terminal  on Dev1 to be /Dev2/SourceCompleteEvent.

    Note: This property is not supported by all devices. Refer to Supported Properties by Device topic

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    driver_setup = _attributes.AttributeViString(1050007)
    '''Type: str

    Indicates the Driver Setup string that you specified when initializing the driver.
    Some cases exist where you must specify the instrument driver options at initialization  time. An example of this case is specifying a particular device model from among a family  of devices that the driver supports. This property is useful when simulating a device.  You can specify the driver-specific options through the DriverSetup keyword in the optionsString  parameter in the __init__ method or through the  IVI Configuration Utility.
    You can specify  driver-specific options through the DriverSetup keyword in the  optionsString parameter in the __init__ method. If you do not specify a Driver Setup string, this property returns an empty string.
    '''
    exported_measure_trigger_output_terminal = _attributes.AttributeViString(1150037)
    '''Type: str

    Specifies the output terminal for exporting the Measure trigger.
    Refer to the Device Routes tab in Measurement & Automation Explorer for a list of the terminals  available on your device.
    for information about supported devices.
    Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you  can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal  name, PXI_Trig0.

    Note: This property is not supported by all devices. Refer to Supported Properties by Device topic

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    exported_pulse_trigger_output_terminal = _attributes.AttributeViString(1150098)
    '''Type: str

    Specifies the output terminal for exporting the Pulse trigger.
    Refer to the Device Routes tab in Measurement & Automation Explorer for a list of the terminals available on your device.
    Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.

    Note: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    exported_sequence_advance_trigger_output_terminal = _attributes.AttributeViString(1150029)
    '''Type: str

    Specifies the output terminal for exporting the Sequence Advance trigger.
    Refer to the Device Routes tab in Measurement & Automation Explorer for a list of the terminals  available on your device.
    for information about supported devices.
    Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you  can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal  name, PXI_Trig0.

    Note: This property is not supported by all devices. Refer to Supported Properties by Device topic

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    exported_source_trigger_output_terminal = _attributes.AttributeViString(1150033)
    '''Type: str

    Specifies the output terminal for exporting the Source trigger.
    Refer to the Device Routes tab in MAX for a list of the terminals available on your device.
    for information about supported devices.
    Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you  can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal  name, PXI_Trig0.

    Note: This property is not supported by all devices. Refer to Supported Properties by Device topic

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    exported_start_trigger_output_terminal = _attributes.AttributeViString(1150024)
    '''Type: str

    Specifies the output terminal for exporting the Start trigger.
    Refer to the Device Routes tab in Measurement & Automation Explorer (MAX) for a list of the terminals available  on your device.
    Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you  can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name,  PXI_Trig0.
    for information about supported devices.

    Note: This property is not supported by all devices. Refer to Supported Properties by Device topic

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    fetch_backlog = _attributes.AttributeViInt32(1150056)
    '''Type: int

    Returns the number of measurements acquired that have not been fetched yet.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    instrument_firmware_revision = _attributes.AttributeViString(1050510)
    '''Type: str

    Contains the firmware revision information for the device you are currently using.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    instrument_manufacturer = _attributes.AttributeViString(1050511)
    '''Type: str

    Contains the name of the manufacturer for the device you are currently using.
    '''
    instrument_model = _attributes.AttributeViString(1050512)
    '''Type: str

    Contains the model number or name of the device that you are currently using.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    interlock_input_open = _attributes.AttributeViBoolean(1150105)
    '''Type: bool

    Indicates whether the safety interlock circuit is open.
    Refer to the Safety Interlock topic in the NI DC Power Supplies and SMUs Help for more information about  the safety interlock circuit.
    about supported devices.

    Note: This property is not supported by all devices. Refer to Supported Properties by Device for information

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    io_resource_descriptor = _attributes.AttributeViString(1050304)
    '''Type: str

    Indicates the resource descriptor NI-DCPower uses to identify the physical device.
    If you initialize NI-DCPower with a logical name, this property contains the resource descriptor  that corresponds to the entry in the IVI Configuration utility.
    If you initialize NI-DCPower with the resource descriptor, this property contains that value.
    '''
    logical_name = _attributes.AttributeViString(1050305)
    '''Type: str

    Contains the logical name you specified when opening the current IVI session.
    You can pass a logical name to the __init__ method.  The IVI Configuration utility must contain an entry for the logical name. The logical name entry  refers to a method section in the IVI Configuration file. The method section specifies a physical  device and initial user options.
    '''
    measure_buffer_size = _attributes.AttributeViInt32(1150077)
    '''Type: int

    Specifies the number of samples that the active channel measurement buffer can hold.
    The default value is the maximum number of samples that a device is capable of recording in one second.
    for information about supported devices.
    Valid Values: 1000 to 2147483647
    Default Value: Varies by device. Refer to Supported Properties by Device topic in  the NI DC Power Supplies and SMUs Help for more information about default values.

    Note: This property is not supported by all devices. Refer to Supported Properties by Device topic

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    measure_complete_event_delay = _attributes.AttributeViReal64TimeDeltaSeconds(1150046)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    Specifies the amount of time to delay the generation of the Measure Complete event, in seconds.
    for information about supported devices.
    Valid Values: 0 to 167 seconds
    Default Value: The NI PXI-4132 and NI PXIe-4140/4141/4142/4143/4144/4145/4154 supports values from  0 seconds to 167 seconds.

    Note: This property is not supported by all devices. Refer to Supported Properties by Device topic

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    measure_complete_event_output_terminal = _attributes.AttributeViString(1150047)
    '''Type: str

    Specifies the output terminal for exporting the Measure Complete event.
    for information about supported devices.
    Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal  is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or  with the shortened terminal name, PXI_Trig0.

    Note: This property is not supported by all devices. Refer to Supported Properties by Device topic

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    measure_complete_event_pulse_polarity = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.Polarity, 1150044)
    '''Type: enums.Polarity

    Specifies the behavior of the Measure Complete event.
    for information about supported devices.
    Default Value: Polarity.HIGH

    Note: This property is not supported by all devices. Refer to Supported Properties by Device topic

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    measure_complete_event_pulse_width = _attributes.AttributeViReal64(1150045)
    '''Type: float

    Specifies the width of the Measure Complete event, in seconds.
    The minimum event pulse width value for PXI devices is 150 ns, and the minimum event pulse  width value for PXI Express devices is 250 ns.
    The maximum event pulse width value for all devices is 1.6 microseconds.
    for information about supported devices.
    Valid Values: 1.5e-7 to 1.6e-6
    Default Value: The default value for PXI devices is 150 ns. The default value  for PXI Express devices is 250 ns.

    Note: This property is not supported by all devices. Refer to Supported Properties by Device topic

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    measure_record_delta_time = _attributes.AttributeViReal64TimeDeltaSeconds(1150065)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    Queries the amount of time, in seconds, between between the start of two consecutive measurements in a measure record.  Only query this property after the desired measurement settings are committed.
    for information about supported devices.
    two measurements and the rest would differ.

    Note: This property is not available when Auto Zero is configured to Once because the amount of time between the first

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    measure_record_length = _attributes.AttributeViInt32(1150063)
    '''Type: int

    Specifies how many measurements compose a measure record. When this property is set to a value greater than 1, the  measure_when property must be set to MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE or  MeasureWhen.ON_MEASURE_TRIGGER.
    for information about supported devices.
    Valid Values: 1 to 16,777,216
    Default Value: 1

    Note:
    This property is not available in a session involving multiple channels.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    measure_record_length_is_finite = _attributes.AttributeViBoolean(1150064)
    '''Type: bool

    Specifies whether to take continuous measurements. Call the abort method to stop continuous measurements.  When this property is set to False and the source_mode property is set to  SourceMode.SINGLE_POINT, the measure_when property must be set to  MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE or MeasureWhen.ON_MEASURE_TRIGGER. When this property is set to  False and the source_mode property is set to SourceMode.SEQUENCE, the measure_when  property must be set to MeasureWhen.ON_MEASURE_TRIGGER.
    for information about supported devices.
    Default Value: True

    Note:
    This property is not available in a session involving multiple channels.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    measure_trigger_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.TriggerType, 1150034)
    '''Type: enums.TriggerType

    Specifies the behavior of the Measure trigger.
    for information about supported devices.
    Default Value: TriggerType.DIGITAL_EDGE

    Note: This property is not supported by all devices. Refer to Supported Properties by Device topic

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    measure_when = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.MeasureWhen, 1150057)
    '''Type: enums.MeasureWhen

    Specifies when the measure unit should acquire measurements. Unless this property is configured to  MeasureWhen.ON_MEASURE_TRIGGER, the measure_trigger_type property is ignored.
    Refer to the Acquiring Measurements topic in the NI DC Power Supplies and SMUs Help for more information about how to  configure your measurements.
    Default Value: If the source_mode property is set to SourceMode.SINGLE_POINT, the default value is  MeasureWhen.ON_DEMAND. This value supports only the measure method and measure_multiple  method. If the source_mode property is set to SourceMode.SEQUENCE, the default value is  MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE. This value supports only the fetch_multiple method.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    merged_channels = _attributes.AttributeViStringRepeatedCapability(1150249)
    '''Type: str

    Specifies the channel(s) to merge with a designated primary channel of an SMU in order to increase the maximum current you can source from the SMU.
    This property designates the merge channels to combine with a primary channel. To designate the primary channel, initialize the session to the primary channel only.
    Note: You cannot change the merge configuration with this property when the session is in the Running state.
    For complete information on using merged channels with this property, refer to Merged Channels in the NI DC Power Supplies and SMUs Help.

    Note: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices. Devices that do not support this property behave as if no channels were merged.
    Default Value: Refer to the Supported Properties by Device topic for the default value by device.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    output_capacitance = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.OutputCapacitance, 1150014)
    '''Type: enums.OutputCapacitance

    Specifies whether to use a low or high capacitance on the output for the specified channel(s).
    for information about supported devices.
    Refer to the NI PXI-4130 Output Capacitance Selection topic in the NI DC Power Supplies and SMUs Help for more  information about capacitance.

    Note: This property is not supported by all devices. Refer to Supported Properties by Device topic

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    output_connected = _attributes.AttributeViBoolean(1150060)
    '''Type: bool

    Specifies whether the output relay is connected (closed) or disconnected (open). The output_enabled  property does not change based on this property; they are independent of each other.
    about supported devices.
    Set this property to False to disconnect the output terminal from the output.
    to the output terminal might discharge unless the relay is disconnected. Excessive connecting and disconnecting of the  output can cause premature wear on the relay.
    Default Value: True

    Note: Only disconnect the output when disconnecting is necessary for your application. For example, a battery connected

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    output_enabled = _attributes.AttributeViBoolean(1250006)
    '''Type: bool

    Specifies whether the output is enabled (True) or disabled (False).
    Depending on the value you specify for the output_function property, you also must set the  voltage level or current level in addition to  enabling the output
    the initiate method. Refer to the Programming States topic in the NI DC Power Supplies and SMUs Help for  more information about NI-DCPower programming states.
    Default Value: The default value is True if you use the __init__ method to open  the session. Otherwise the default value is False, including when you use a calibration session or the deprecated programming model.

    Note: If the session is in the Committed or Uncommitted states, enabling the output does not take effect until you call

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    output_function = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.OutputFunction, 1150008)
    '''Type: enums.OutputFunction

    Configures the method to generate on the specified channel(s).
    When OutputFunction.DC_VOLTAGE is selected, the device generates the desired voltage level on the output as long as the  output current is below the current limit. You can use the following properties to configure the channel when  OutputFunction.DC_VOLTAGE is selected:
    voltage_level
    current_limit
    current_limit_high
    current_limit_low
    voltage_level_range
    current_limit_range
    compliance_limit_symmetry
    When OutputFunction.DC_CURRENT is selected, the device generates the desired current level on the output as long as the  output voltage is below the voltage limit. You can use the following properties to configure the channel when  OutputFunction.DC_CURRENT is selected:
    current_level
    voltage_limit
    voltage_limit_high
    voltage_limit_low
    current_level_range
    voltage_limit_range
    compliance_limit_symmetry

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    output_resistance = _attributes.AttributeViReal64(1150061)
    '''Type: float

    Specifies the output resistance that the device attempts to generate for the specified channel(s). This property is  available only when you set the output_function property on a support device. Refer to a supported device's topic about output resistance for more information about selecting an output resistance.
    about supported devices.
    Default Value: 0.0

    Note: This property is not supported by all devices. Refer to Supported Properties by Device topic for information

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    overranging_enabled = _attributes.AttributeViBoolean(1150007)
    '''Type: bool

    Specifies whether NI-DCPower allows setting the voltage level, current level, voltage limit and current limit outside the  device specification limits. True means that overranging is enabled.
    Refer to the Ranges topic in the NI DC Power Supplies and SMUs Help for more information about overranging.
    Default Value: False

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    ovp_enabled = _attributes.AttributeViBoolean(1250002)
    '''Type: bool

    Enables (True) or disables (False) overvoltage protection (OVP).
    Refer to the Output Overvoltage Protection topic in the NI DC Power Supplies and SMUs Help for more information about  overvoltage protection.
    for information about supported devices.
    Default Value: False

    Note: This property is not supported by all devices. Refer to Supported Properties by Device topic

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    ovp_limit = _attributes.AttributeViReal64(1250003)
    '''Type: float

    Determines the voltage limit, in volts, beyond which overvoltage protection (OVP) engages.
    for information about supported devices.
    Valid Values: 2 V to 210 V
    Default Value: 210 V

    Note: This property is not supported by all devices. Refer to Supported Properties by Device topic

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    power_allocation_mode = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.PowerAllocationMode, 1150207)
    '''Type: enums.PowerAllocationMode

    Determines whether the device sources the power its source configuration requires or a specific wattage you request; determines whether NI-DCPower proactively checks that this sourcing power is within the maximum per-channel and overall sourcing power of the device.

     When this property configures NI-DCPower to perform a sourcing power check, a device is not permitted to source power in excess of its maximum per-channel or overall sourcing power. If the check determines a source configuration or power request would require the device to do so, NI-DCPower returns an error.

     When this property does not configure NI-DCPower to perform a sourcing power check, a device can attempt to fulfill source configurations that would require it to source power in excess of its maximum per-channel or overall sourcing power and may shut down to prevent damage.

     Default Value: Refer to the Supported Properties by Device topic for the default value by device.

    Note: This property is not supported by all devices. Refer to the Supported Properties by Device topic for information about supported devices. Devices that do not support this property behave as if this property were set to PowerAllocationMode.DISABLED.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    power_line_frequency = _attributes.AttributeViReal64(1150020)
    '''Type: float

    Specifies the power line frequency for specified channel(s). NI-DCPower uses this value to select a timebase for setting the  aperture_time property in power line cycles (PLCs).
    in the NI DC Power Supplies and SMUs Help for information about supported devices.
    Default Value: NIDCPOWER_VAL_60_HERTZ

    Note: This property is not supported by all devices. Refer to the Supported Properties by Device topic

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    power_source = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.PowerSource, 1150000)
    '''Type: enums.PowerSource

    Specifies the power source to use. NI-DCPower switches the power source used by the  device to the specified value.
    Default Value: PowerSource.AUTOMATIC
    is set to PowerSource.AUTOMATIC. However, if the session is in the Committed or Uncommitted state  when you set this property, the power source selection only occurs after you call the  initiate method.

    Note: Automatic selection is not persistent and occurs only at the time this property
    '''
    power_source_in_use = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.PowerSourceInUse, 1150001)
    '''Type: enums.PowerSourceInUse

    Indicates whether the device is using the internal or auxiliary power source to generate power.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    pulse_bias_current_level = _attributes.AttributeViReal64(1150088)
    '''Type: float

    Specifies the pulse bias current level, in amps, that the device attempts to generate on the specified channel(s) during the off phase of a pulse.
    This property is applicable only if the output_function property is set to OutputFunction.PULSE_CURRENT.
    Valid Values: The valid values for this property are defined by the values you specify for the pulse_current_level_range property.

    Note: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    pulse_bias_current_limit = _attributes.AttributeViReal64(1150083)
    '''Type: float

    Specifies the pulse bias current limit, in amps, that the output cannot exceed when generating the desired pulse bias voltage on the specified channel(s) during the off phase of a pulse.
    This property is applicable only if the output_function property is set to OutputFunction.PULSE_VOLTAGE.
    Valid Values: The valid values for this property are defined by the values you specify for the pulse_current_limit_range property.

    Note: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    pulse_bias_current_limit_high = _attributes.AttributeViReal64(1150195)
    '''Type: float

    Specifies the maximum current, in amps, that the output can produce when
    generating the desired pulse voltage on the specified channel(s) during
    the *off* phase of a pulse.
    This property is applicable only if the `Compliance Limit
    Symmetry <pComplianceLimitSymmetry.html>`__ property is set to
    **Asymmetric** and the `Output
    Method <pOutputFunction.html>`__ property is set to **Pulse
    Voltage**.
    You must also specify a `Pulse Bias Current Limit
    Low <pPulseBiasCurrentLimitLow.html>`__ to complete the
    asymmetric range.
    **Valid Values:** [1% of `Pulse Current Limit
    Range <pPulseCurrentLimitRange.html>`__, `Pulse Current Limit
    Range <pPulseCurrentLimitRange.html>`__]
    The range bounded by the limit high and limit low must include zero.
    **Default Value:** Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.
    **Related Topics:**
    `Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
    `Changing
    Ranges <NI_DC_Power_Supplies_Help.chm::/changing_ranges.html>`__
    `Overranging <NI_DC_Power_Supplies_Help.chm::/overranging.html>`__

    Note:
    The limit may be extended beyond the selected limit range if the
    `Overranging Enabled <pOverrangingEnabled.html>`__ property is
    set to TRUE or if the `Output
    Method <pOutputFunction.html>`__ property is set to a
    pulsing method.

    Note:
    One or more of the referenced methods are not in the Python API for this driver.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    pulse_bias_current_limit_low = _attributes.AttributeViReal64(1150196)
    '''Type: float

    Specifies the minimum current, in amps, that the output can produce when
    generating the desired pulse voltage on the specified channel(s) during
    the *off* phase of a pulse.
    This property is applicable only if the `Compliance Limit
    Symmetry <pComplianceLimitSymmetry.html>`__ property is set to
    **Asymmetric** and the `Output
    Method <pOutputFunction.html>`__ property is set to **Pulse
    Voltage**.
    You must also specify a `Pulse Bias Current Limit
    High <pPulseBiasCurrentLimitHigh.html>`__ to complete the
    asymmetric range.
    **Valid Values:** [-`Pulse Current Limit
    Range <pPulseCurrentLimitRange.html>`__, -1% of `Pulse Current
    Limit Range <pPulseCurrentLimitRange.html>`__]
    The range bounded by the limit high and limit low must include zero.
    **Default Value:** Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.
    **Related Topics:**
    `Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
    `Changing
    Ranges <NI_DC_Power_Supplies_Help.chm::/changing_ranges.html>`__
    `Overranging <NI_DC_Power_Supplies_Help.chm::/overranging.html>`__

    Note:
    The limit may be extended beyond the selected limit range if the
    `Overranging Enabled <pOverrangingEnabled.html>`__ property is
    set to TRUE or if the `Output
    Method <pOutputFunction.html>`__ property is set to a
    pulsing method.

    Note:
    One or more of the referenced methods are not in the Python API for this driver.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    pulse_bias_delay = _attributes.AttributeViReal64(1150092)
    '''Type: float

    Determines when, in seconds, the device generates the Pulse Complete event after generating the off level of a pulse.
    Valid Values: 0 to 167 seconds
    Default Value: 16.67 milliseconds

    Note: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    pulse_bias_voltage_level = _attributes.AttributeViReal64(1150082)
    '''Type: float

    Specifies the pulse bias voltage level, in volts, that the device attempts to generate on the specified channel(s) during the off phase of a pulse.
    This property is applicable only if the output_function property is set to OutputFunction.PULSE_VOLTAGE.
    Valid Values: The valid values for this property are defined by the values you specify for the pulse_voltage_level_range property.

    Note: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    pulse_bias_voltage_limit = _attributes.AttributeViReal64(1150089)
    '''Type: float

    Specifies the pulse voltage limit, in volts, that the output cannot exceed when generating the desired current on the specified channel(s) during the off phase of a pulse.
    This property is applicable only if the output_function property is set to OutputFunction.PULSE_CURRENT.
    Valid Values: The valid values for this property are defined by the values you specify for the pulse_voltage_limit_range property.

    Note: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    pulse_bias_voltage_limit_high = _attributes.AttributeViReal64(1150191)
    '''Type: float

    Specifies the maximum voltage, in volts, that the output can produce
    when generating the desired pulse current on the specified channel(s)
    during the *off* phase of a pulse.
    This property is applicable only if the `Compliance Limit
    Symmetry <pComplianceLimitSymmetry.html>`__ property is set to
    **Asymmetric** and the `Output
    Method <pOutputFunction.html>`__ property is set to **Pulse
    Current**.
    You must also specify a `Pulse Bias Voltage Limit
    Low <pPulseBiasVoltageLimitLow.html>`__ to complete the
    asymmetric range.
    **Valid Values:** [1% of `Pulse Voltage Limit
    Range <pPulseVoltageLimitRange.html>`__, `Pulse Voltage Limit
    Range <pPulseVoltageLimitRange.html>`__]
    The range bounded by the limit high and limit low must include zero.
    **Default Value:** Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.
    **Related Topics:**
    `Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
    `Changing
    Ranges <NI_DC_Power_Supplies_Help.chm::/changing_ranges.html>`__
    `Overranging <NI_DC_Power_Supplies_Help.chm::/overranging.html>`__

    Note:
    The limit may be extended beyond the selected limit range if the
    `Overranging Enabled <pOverrangingEnabled.html>`__ property is
    set to TRUE or if the `Output
    Method <pOutputFunction.html>`__ property is set to a
    pulsing method.

    Note:
    One or more of the referenced methods are not in the Python API for this driver.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    pulse_bias_voltage_limit_low = _attributes.AttributeViReal64(1150192)
    '''Type: float

    Specifies the minimum voltage, in volts, that the output can produce
    when generating the desired pulse current on the specified channel(s)
    during the *off* phase of a pulse.
    This property is applicable only if the `Compliance Limit
    Symmetry <pComplianceLimitSymmetry.html>`__ property is set to
    **Asymmetric** and the `Output
    Method <pOutputFunction.html>`__ property is set to **Pulse
    Current**.
    You must also specify a `Pulse Bias Voltage Limit
    High <pPulseBiasVoltageLimitHigh.html>`__ to complete the
    asymmetric range.
    **Valid Values:** [-`Pulse Voltage Limit
    Range <pPulseVoltageLimitRange.html>`__, -1% of `Pulse Voltage
    Limit Range <pPulseVoltageLimitRange.html>`__]
    The range bounded by the limit high and limit low must include zero.
    **Default Value:** Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.
    **Related Topics:**
    `Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
    `Changing
    Ranges <NI_DC_Power_Supplies_Help.chm::/changing_ranges.html>`__
    `Overranging <NI_DC_Power_Supplies_Help.chm::/overranging.html>`__

    Note:
    The limit may be extended beyond the selected limit range if the
    `Overranging Enabled <pOverrangingEnabled.html>`__ property is
    set to TRUE or if the `Output
    Method <pOutputFunction.html>`__ property is set to a
    pulsing method.

    Note:
    One or more of the referenced methods are not in the Python API for this driver.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    pulse_complete_event_output_terminal = _attributes.AttributeViString(1150099)
    '''Type: str

    Specifies the output terminal for exporting the Pulse Complete event.
    Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.
    Default Value:The default value for PXI Express devices is 250 ns.

    Note: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    pulse_complete_event_pulse_polarity = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.Polarity, 1150100)
    '''Type: enums.Polarity

    Specifies the behavior of the Pulse Complete event.
    Default Value: Polarity.HIGH

    Note: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    pulse_complete_event_pulse_width = _attributes.AttributeViReal64(1150101)
    '''Type: float

    Specifies the width of the Pulse Complete event, in seconds.
    The minimum event pulse width value for PXI Express devices is 250 ns.
    The maximum event pulse width value for PXI Express devices is 1.6 microseconds.
    Default Value: The default value for PXI Express devices is 250 ns.

    Note: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    pulse_current_level = _attributes.AttributeViReal64(1150086)
    '''Type: float

    Specifies the pulse current level, in amps, that the device attempts to generate on the specified channel(s) during the on phase of a pulse.
    This property is applicable only if the output_function property is set to OutputFunction.PULSE_CURRENT.
    Valid Values: The valid values for this property are defined by the values you specify for the pulse_current_level_range property.

    Note: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    pulse_current_level_range = _attributes.AttributeViReal64(1150090)
    '''Type: float

    Specifies the pulse current level range, in amps, for the specified channel(s).
    The range defines the valid values to which you can set the pulse current level and pulse bias current level.
    This property is applicable only if the output_function property is set to OutputFunction.PULSE_CURRENT.
    For valid ranges, refer to the ranges topic for your device in the NI DC Power Supplies and SMUs Help.

    Note: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    pulse_current_limit = _attributes.AttributeViReal64(1150081)
    '''Type: float

    Specifies the pulse current limit, in amps, that the output cannot exceed when generating the desired pulse voltage on the specified channel(s) during the on phase of a pulse.
    This property is applicable only if the output_function property is set to OutputFunction.PULSE_VOLTAGE and the compliance_limit_symmetry  property is set to ComplianceLimitSymmetry.SYMMETRIC.
    Valid Values: The valid values for this property are defined by the values you specify for the pulse_current_limit_range property.

    Note: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    pulse_current_limit_high = _attributes.AttributeViReal64(1150193)
    '''Type: float

    Specifies the maximum current, in amps, that the output can produce when
    generating the desired pulse voltage on the specified channel(s) during
    the *on* phase of a pulse.
    This property is applicable only if the `Compliance Limit
    Symmetry <pComplianceLimitSymmetry.html>`__ property is set to
    **Asymmetric** and the `Output
    Method <pOutputFunction.html>`__ property is set to **Pulse
    Voltage**.
    You must also specify a `Pulse Current Limit
    Low <pPulseCurrentLimitLow.html>`__ to complete the asymmetric
    range.
    **Valid Values:** [1% of `Pulse Current Limit
    Range <pPulseCurrentLimitRange.html>`__, `Pulse Current Limit
    Range <pPulseCurrentLimitRange.html>`__]
    The range bounded by the limit high and limit low must include zero.
    **Default Value:** Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.
    **Related Topics:**
    `Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
    `Changing
    Ranges <NI_DC_Power_Supplies_Help.chm::/changing_ranges.html>`__
    `Overranging <NI_DC_Power_Supplies_Help.chm::/overranging.html>`__

    Note:
    The limit may be extended beyond the selected limit range if the
    `Overranging Enabled <pOverrangingEnabled.html>`__ property is
    set to TRUE or if the `Output
    Method <pOutputFunction.html>`__ property is set to a
    pulsing method.

    Note:
    One or more of the referenced methods are not in the Python API for this driver.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    pulse_current_limit_low = _attributes.AttributeViReal64(1150194)
    '''Type: float

    Specifies the minimum current, in amps, that the output can produce when
    generating the desired pulse voltage on the specified channel(s) during
    the *on* phase of a pulse.
    This property is applicable only if the `Compliance Limit
    Symmetry <pComplianceLimitSymmetry.html>`__ property is set to
    **Asymmetric** and the `Output
    Method <pOutputFunction.html>`__ property is set to **Pulse
    Voltage**.
    You must also specify a `Pulse Current Limit
    High <pPulseCurrentLimitHigh.html>`__ to complete the
    asymmetric range.
    **Valid Values:** [-`Pulse Current Limit
    Range <pPulseCurrentLimitRange.html>`__, -1% of `Pulse Current
    Limit Range <pPulseCurrentLimitRange.html>`__]
    The range bounded by the limit high and limit low must include zero.
    **Default Value:** Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.
    **Related Topics:**
    `Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
    `Changing
    Ranges <NI_DC_Power_Supplies_Help.chm::/changing_ranges.html>`__
    `Overranging <NI_DC_Power_Supplies_Help.chm::/overranging.html>`__

    Note:
    The limit may be extended beyond the selected limit range if the
    `Overranging Enabled <pOverrangingEnabled.html>`__ property is
    set to TRUE or if the `Output
    Method <pOutputFunction.html>`__ property is set to a
    pulsing method.

    Note:
    One or more of the referenced methods are not in the Python API for this driver.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    pulse_current_limit_range = _attributes.AttributeViReal64(1150085)
    '''Type: float

    Specifies the pulse current limit range, in amps, for the specified channel(s).
    The range defines the valid values to which you can set the pulse current limit and pulse bias current limit.
    This property is applicable only if the output_function property is set to OutputFunction.PULSE_VOLTAGE.
    For valid ranges, refer to the ranges topic for your device in the NI DC Power Supplies and SMUs Help.

    Note: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    pulse_off_time = _attributes.AttributeViReal64TimeDeltaSeconds(1150094)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    Determines the length, in seconds, of the off phase of a pulse.
    Valid Values: 10 microseconds to 167 seconds
    Default Value: 34 milliseconds

    Note: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    pulse_on_time = _attributes.AttributeViReal64TimeDeltaSeconds(1150093)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    Determines the length, in seconds, of the on phase of a pulse.
    Valid Values: 10 microseconds to 167 seconds
    Default Value: 34 milliseconds

    Note: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    pulse_trigger_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.TriggerType, 1150095)
    '''Type: enums.TriggerType

    Specifies the behavior of the Pulse trigger.
    Default Value: TriggerType.NONE

    Note: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    pulse_voltage_level = _attributes.AttributeViReal64(1150080)
    '''Type: float

    Specifies the pulse current limit, in amps, that the output cannot exceed when generating the desired pulse voltage on the specified channel(s) during the on phase of a pulse.
    This property is applicable only if the output_function property is set to OutputFunction.PULSE_VOLTAGE.
    Valid Values: The valid values for this property are defined by the values you specify for the pulse_current_limit_range property.

    Note: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    pulse_voltage_level_range = _attributes.AttributeViReal64(1150084)
    '''Type: float

    Specifies the pulse voltage level range, in volts, for the specified channel(s).
    The range defines the valid values at which you can set the pulse voltage level and pulse bias voltage level.
    This property is applicable only if the output_function property is set to OutputFunction.PULSE_VOLTAGE.
    For valid ranges, refer to the ranges topic for your device in the NI DC Power Supplies and SMUs Help.

    Note: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    pulse_voltage_limit = _attributes.AttributeViReal64(1150087)
    '''Type: float

    Specifies the pulse voltage limit, in volts, that the output cannot exceed when generating the desired pulse current on the specified channel(s) during the on phase of a pulse.
    This property is applicable only if the output_function property is set to OutputFunction.PULSE_CURRENT and the compliance_limit_symmetry property  is set to ComplianceLimitSymmetry.SYMMETRIC.
    Valid Values: The valid values for this property are defined by the values you specify for the pulse_voltage_limit_range property.

    Note: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    pulse_voltage_limit_high = _attributes.AttributeViReal64(1150189)
    '''Type: float

    Specifies the maximum voltage, in volts, that the output can produce
    when generating the desired pulse current on the specified channel(s)
    during the *on* phase of a pulse.
    This property is applicable only if the `Compliance Limit
    Symmetry <pComplianceLimitSymmetry.html>`__ property is set to
    **Asymmetric** and the `Output
    Method <pOutputFunction.html>`__ property is set to **Pulse
    Current**.
    You must also specify a `Pulse Voltage Limit
    Low <pPulseVoltageLimitLow.html>`__ to complete the asymmetric
    range.
    **Valid Values:** [1% of `Pulse Voltage Limit
    Range <pPulseVoltageLimitRange.html>`__, `Pulse Voltage Limit
    Range <pPulseVoltageLimitRange.html>`__]
    The range bounded by the limit high and limit low must include zero.
    **Default Value:** Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.
    **Related Topics:**
    `Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
    `Changing
    Ranges <NI_DC_Power_Supplies_Help.chm::/changing_ranges.html>`__
    `Overranging <NI_DC_Power_Supplies_Help.chm::/overranging.html>`__

    Note:
    The limit may be extended beyond the selected limit range if the
    `Overranging Enabled <pOverrangingEnabled.html>`__ property is
    set to TRUE or if the `Output
    Method <pOutputFunction.html>`__ property is set to a
    pulsing method.

    Note:
    One or more of the referenced methods are not in the Python API for this driver.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    pulse_voltage_limit_low = _attributes.AttributeViReal64(1150190)
    '''Type: float

    Specifies the minimum voltage, in volts, that the output can produce
    when generating the desired pulse current on the specified channel(s)
    during the *on* phase of a pulse.
    This property is applicable only if the `Compliance Limit
    Symmetry <pComplianceLimitSymmetry.html>`__ property is set to
    **Asymmetric** and the `Output
    Method <pOutputFunction.html>`__ property is set to **Pulse
    Current**.
    You must also specify a `Pulse Voltage Limit
    High <pPulseVoltageLimitHigh.html>`__ to complete the
    asymmetric range.
    **Valid Values:** [-`Pulse Voltage Limit
    Range <pPulseVoltageLimitRange.html>`__, -1% of `Pulse Voltage
    Limit Range <pPulseVoltageLimitRange.html>`__]
    The range bounded by the limit high and limit low must include zero.
    **Default Value:** Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.
    **Related Topics:**
    `Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
    `Changing
    Ranges <NI_DC_Power_Supplies_Help.chm::/changing_ranges.html>`__
    `Overranging <NI_DC_Power_Supplies_Help.chm::/overranging.html>`__

    Note:
    The limit may be extended beyond the selected limit range if the
    `Overranging Enabled <pOverrangingEnabled.html>`__ property is
    set to TRUE or if the `Output
    Method <pOutputFunction.html>`__ property is set to a
    pulsing method.

    Note:
    One or more of the referenced methods are not in the Python API for this driver.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    pulse_voltage_limit_range = _attributes.AttributeViReal64(1150091)
    '''Type: float

    Specifies the pulse voltage limit range, in volts, for the specified channel(s).
    The range defines the valid values to which you can set the pulse voltage limit and pulse bias voltage limit.
    This property is applicable only if the output_function property is set to OutputFunction.PULSE_CURRENT.
    For valid ranges, refer to the ranges topic for your device in the NI DC Power Supplies and SMUs Help.

    Note: The channel must be enabled for the specified current limit to take effect. Refer to the output_enabled property for more information about enabling the output channel.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    query_instrument_status = _attributes.AttributeViBoolean(1050003)
    '''Type: bool

    Specifies whether NI-DCPower queries the device status after each operation.
    Querying the device status is useful for debugging. After you validate your program, you can set this  property to False to disable status checking and maximize performance.
    NI-DCPower ignores status checking for particular properties regardless of the setting of this property.
    Use the __init__ method to override this value.
    Default Value: True
    '''
    ready_for_pulse_trigger_event_output_terminal = _attributes.AttributeViString(1150102)
    '''Type: str

    Specifies the output terminal for exporting the Ready For Pulse Trigger event.
    Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.

    Note: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    ready_for_pulse_trigger_event_pulse_polarity = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.Polarity, 1150103)
    '''Type: enums.Polarity

    Specifies the behavior of the Ready For Pulse Trigger event.
    Default Value: Polarity.HIGH

    Note: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    ready_for_pulse_trigger_event_pulse_width = _attributes.AttributeViReal64(1150104)
    '''Type: float

    Specifies the width of the Ready For Pulse Trigger event, in seconds.
    The minimum event pulse width value for PXI Express devices is 250 ns.
    The maximum event pulse width value for all devices is 1.6 microseconds.
    Default Value: The default value for PXI Express devices is 250 ns

    Note: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
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

    Note: This property is not supported by all devices. Refer to Supported Properties by Device topic for information about supported devices.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    reset_average_before_measurement = _attributes.AttributeViBoolean(1150006)
    '''Type: bool

    Specifies whether the measurement returned from any measurement call starts with a new measurement call (True) or  returns a measurement that has already begun or completed(False).
    for information about supported devices.
    When you set the samples_to_average property in the Running state, the output channel measurements might  move out of synchronization. While NI-DCPower automatically synchronizes measurements upon the initialization of a  session, you can force a synchronization in the running state before you run the measure_multiple method. To  force a synchronization in the running state, set this property to True, and then run the measure_multiple  method, specifying all channels in the channel name parameter. You can set the  reset_average_before_measurement property to False after the measure_multiple method  completes.
    Default Value: True

    Note: This property is not supported by all devices. Refer to Supported Properties by Device topic

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    samples_to_average = _attributes.AttributeViInt32(1150003)
    '''Type: int

    Specifies the number of samples to average when you take a measurement.
    Increasing the number of samples to average decreases measurement noise but increases the time required to take  a measurement. Refer to the NI PXI-4110, NI PXI-4130, NI PXI-4132, or NI PXIe-4154 Averaging topic for  optional property settings to improve immunity to certain noise types, or refer to the NI PXIe-4140/4141  DC Noise Rejection, NI PXIe-4142/4143 DC Noise Rejection, or NI PXIe-4144/4145 DC Noise Rejection topic for  information about improving noise immunity for those devices.
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
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    self_calibration_persistence = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.SelfCalibrationPersistence, 1150073)
    '''Type: enums.SelfCalibrationPersistence

    Specifies whether the values calculated during self-calibration should be written to hardware to be used until the  next self-calibration or only used until the reset_device method is called or the machine  is powered down.
    This property affects the behavior of the self_cal method. When set to  SelfCalibrationPersistence.KEEP_IN_MEMORY, the values calculated by the self_cal method are used in  the existing session, as well as in all further sessions until you call the reset_device method  or restart the machine. When you set this property to SelfCalibrationPersistence.WRITE_TO_EEPROM, the values calculated  by the self_cal method are written to hardware and used in the existing session and  in all subsequent sessions until another call to the self_cal method is made.
    about supported devices.
    Default Value: SelfCalibrationPersistence.KEEP_IN_MEMORY

    Note: This property is not supported by all devices. Refer to Supported Properties by Device for information
    '''
    sense = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.Sense, 1150013)
    '''Type: enums.Sense

    Selects either local or remote sensing of the output voltage for the specified channel(s).
    Refer to the Local and Remote Sense topic in the NI DC Power Supplies and SMUs Help for more  information about sensing voltage on supported channels and about devices that support local and/or remote sensing.
    Default Value: The default value is Sense.LOCAL if the device supports local sense.  Otherwise, the default and only supported value is Sense.REMOTE.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    sequence_advance_trigger_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.TriggerType, 1150026)
    '''Type: enums.TriggerType

    Specifies the behavior of the Sequence Advance trigger.
    for information about supported devices.
    Default Value: TriggerType.NONE

    Note: This property is not supported by all devices. Refer to Supported Properties by Device topic

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    sequence_engine_done_event_output_terminal = _attributes.AttributeViString(1150050)
    '''Type: str

    Specifies the output terminal for exporting the Sequence Engine Done Complete event.
    for information about supported devices.
    Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal  is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or  with the shortened terminal name, PXI_Trig0.

    Note: This property is not supported by all devices. Refer to Supported Properties by Device topic

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    sequence_engine_done_event_pulse_polarity = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.Polarity, 1150048)
    '''Type: enums.Polarity

    Specifies the behavior of the Sequence Engine Done event.
    for information about supported devices.
    Default Value: Polarity.HIGH

    Note: This property is not supported by all devices. Refer to Supported Properties by Device topic

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    sequence_engine_done_event_pulse_width = _attributes.AttributeViReal64(1150049)
    '''Type: float

    Specifies the width of the Sequence Engine Done event, in seconds.
    The minimum event pulse width value for PXI devices is 150 ns, and the minimum event pulse width value  for PXI Express devices is 250 ns.
    The maximum event pulse width value for all devices is 1.6 microseconds.
    for information about supported devices.
    Valid Values: 1.5e-7 to 1.6e-6 seconds
    Default Value: The default value for PXI devices is 150 ns. The default value for PXI Express devices is 250 ns.

    Note: This property is not supported by all devices. Refer to Supported Properties by Device topic

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    sequence_iteration_complete_event_output_terminal = _attributes.AttributeViString(1150040)
    '''Type: str

    Specifies the output terminal for exporting the Sequence Iteration Complete event.
    for information about supported devices.
    Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal  is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or  with the shortened terminal name, PXI_Trig0.

    Note: This property is not supported by all devices. Refer to Supported Properties by Device topic

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    sequence_iteration_complete_event_pulse_polarity = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.Polarity, 1150038)
    '''Type: enums.Polarity

    Specifies the behavior of the Sequence Iteration Complete event.
    for information about supported devices.
    Default Value: Polarity.HIGH

    Note: This property is not supported by all devices. Refer to Supported Properties by Device topic

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    sequence_iteration_complete_event_pulse_width = _attributes.AttributeViReal64(1150039)
    '''Type: float

    Specifies the width of the Sequence Iteration Complete event, in seconds.
    The minimum event pulse width value for PXI devices is 150 ns, and the minimum event pulse width  value for PXI Express devices is 250 ns.
    The maximum event pulse width value for all devices is 1.6 microseconds.
    the NI DC Power Supplies and SMUs Help for information about supported devices.
    Valid Values: 1.5e-7 to 1.6e-6 seconds
    Default Value: The default value for PXI devices is 150 ns. The default value for PXI Express devices is 250 ns.

    Note: This property is not supported by all devices. Refer to Supported Properties by Device topic in

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    sequence_loop_count = _attributes.AttributeViInt32(1150025)
    '''Type: int

    Specifies the number of times a sequence is run after initiation.
    Refer to the Sequence Source Mode topic in the NI DC Power Supplies and SMUs Help for more information about the sequence  loop count.
    for information about supported devices. When the sequence_loop_count_is_finite property  is set to False, the sequence_loop_count property is ignored.
    Valid Range: 1 to 134217727
    Default Value: 1

    Note: This property is not supported by all devices. Refer to Supported Properties by Device topic

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    sequence_loop_count_is_finite = _attributes.AttributeViBoolean(1150078)
    '''Type: bool

    Specifies whether a sequence should repeat indefinitely.
    Refer to the Sequence Source Mode topic in the NI DC Power Supplies and SMUs Help for more information about  infinite sequencing.
    sequence_loop_count_is_finite property is set to False,  the sequence_loop_count property is ignored.
    Default Value: True

    Note: This property is not supported by all devices. When the

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    sequence_step_delta_time = _attributes.AttributeViReal64(1150198)
    '''Type: float

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    sequence_step_delta_time_enabled = _attributes.AttributeViBoolean(1150199)
    '''Type: bool

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    serial_number = _attributes.AttributeViString(1150152)
    '''Type: str

    Contains the serial number for the device you are currently using.
    '''
    shutdown_trigger_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.TriggerType, 1150275)
    '''Type: enums.TriggerType

    Specifies the behavior of the Shutdown trigger.
    Default Value: TriggerType.NONE

    Note: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    simulate = _attributes.AttributeViBoolean(1050005)
    '''Type: bool

    Specifies whether to simulate NI-DCPower I/O operations. True specifies that operation is simulated.
    Default Value: False
    '''
    source_complete_event_output_terminal = _attributes.AttributeViString(1150043)
    '''Type: str

    Specifies the output terminal for exporting the Source Complete event.
    for information about supported devices.
    Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you  can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal  name, PXI_Trig0.

    Note: This property is not supported by all devices. Refer to Supported Properties by Device topic

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    source_complete_event_pulse_polarity = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.Polarity, 1150041)
    '''Type: enums.Polarity

    Specifies the behavior of the Source Complete event.
    for information about supported devices.
    Default Value: Polarity.HIGH

    Note: This property is not supported by all devices. Refer to Supported Properties by Device topic

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    source_complete_event_pulse_width = _attributes.AttributeViReal64(1150042)
    '''Type: float

    Specifies the width of the Source Complete event, in seconds.
    for information about supported devices.
    The minimum event pulse width value for PXI devices is 150 ns, and the minimum event pulse width value  for PXI Express devices is 250 ns.
    The maximum event pulse width value for all devices is 1.6 microseconds
    Valid Values: 1.5e-7 to 1.6e-6 seconds
    Default Value: The default value for PXI devices is 150 ns. The default value for PXI Express devices is 250 ns.

    Note: This property is not supported by all devices. Refer to Supported Properties by Device topic

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    source_delay = _attributes.AttributeViReal64TimeDeltaSeconds(1150051)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    Determines when, in seconds, the device generates the Source Complete event, potentially starting a measurement if the  measure_when property is set to MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE.
    Refer to the Single Point Source Mode and Sequence Source Mode topics for more information.
    Valid Values: 0 to 167 seconds
    Default Value: 0.01667 seconds

    Note:
    Refer to Supported Properties by Device for information about supported devices.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    source_mode = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.SourceMode, 1150054)
    '''Type: enums.SourceMode

    Specifies whether to run a single output point or a sequence. Refer to the Single Point Source Mode and Sequence Source  Mode topics in the NI DC Power Supplies and SMUs Help for more information about source modes.
    Default value: SourceMode.SINGLE_POINT

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    source_trigger_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.TriggerType, 1150030)
    '''Type: enums.TriggerType

    Specifies the behavior of the Source trigger.
    for information about supported devices.
    Default Value: TriggerType.NONE

    Note: This property is not supported by all devices. Refer to Supported Properties by Device topic

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    specific_driver_description = _attributes.AttributeViString(1050514)
    '''Type: str

    Contains a brief description of the specific driver.
    '''
    specific_driver_prefix = _attributes.AttributeViString(1050302)
    '''Type: str

    Contains the prefix for NI-DCPower. The name of each user-callable  method in NI-DCPower begins with this prefix.
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
    for information about supported devices.
    Default Value: TriggerType.NONE

    Note: This property is not supported by all devices. Refer to Supported Properties by Device topic

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    supported_instrument_models = _attributes.AttributeViString(1050327)
    '''Type: str

    Contains a comma-separated (,) list of supported NI-DCPower device models.
    '''
    transient_response = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.TransientResponse, 1150062)
    '''Type: enums.TransientResponse

    Specifies the transient response. Refer to the Transient Response topic in the NI DC Power Supplies and SMUs Help  for more information about transient response.
    for information about supported devices.
    Default Value: TransientResponse.NORMAL

    Note: This property is not supported by all devices. Refer to Supported Properties by Device topic

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    voltage_compensation_frequency = _attributes.AttributeViReal64(1150068)
    '''Type: float

    The frequency at which a pole-zero pair is added to the system when the channel is in  Constant Voltage mode.
    for information about supported devices.
    Default value: Determined by the value of the TransientResponse.NORMAL setting of  the transient_response property.

    Note: This property is not supported by all devices. Refer to Supported Properties by Device topic

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    voltage_gain_bandwidth = _attributes.AttributeViReal64(1150067)
    '''Type: float

    The frequency at which the unloaded loop gain extrapolates to 0 dB in the absence of additional poles and zeroes. This property takes effect when the channel is in Constant Voltage mode.
    for information about supported devices.
    Default Value: Determined by the value of the TransientResponse.NORMAL setting of the  transient_response property.

    Note: This property is not supported by all devices. Refer to Supported Properties by Device topic

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    voltage_level = _attributes.AttributeViReal64(1250001)
    '''Type: float

    Specifies the voltage level, in volts, that the device attempts to generate on the specified channel(s).
    This property is applicable only if the output_function property is set to OutputFunction.DC_VOLTAGE.
    output_enabled property for more information about enabling the output channel.
    Valid Values: The valid values for this property are defined by the values you specify for the  voltage_level_range property.

    Note: The channel must be enabled for the specified voltage level to take effect. Refer to the

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    voltage_level_autorange = _attributes.AttributeViInt32(1150015)
    '''Type: bool

    Specifies whether NI-DCPower automatically selects the voltage level range based on the desired voltage level  for the specified channel(s).
    If you set this property to AutoZero.ON, NI-DCPower ignores any changes you make to the  voltage_level_range property. If you change the voltage_level_autorange property from  AutoZero.ON to AutoZero.OFF, NI-DCPower retains the last value the voltage_level_range  property was set to (or the default value if the property was never set) and uses that value as  the voltage level range.
    Query the voltage_level_range property by using the _get_attribute_vi_int32 method for  information about which range NI-DCPower automatically selects.
    The voltage_level_autorange property is applicable only if the output_function property  is set to OutputFunction.DC_VOLTAGE.
    Default Value: AutoZero.OFF

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    voltage_level_range = _attributes.AttributeViReal64(1150005)
    '''Type: float

    Specifies the voltage level range, in volts, for the specified channel(s).
    The range defines the valid values to which the voltage level can be set. Use the voltage_level_autorange  property to enable automatic selection of the voltage level range.
    The voltage_level_range property is applicable only if the output_function property is  set to OutputFunction.DC_VOLTAGE.
    output_enabled property for more information about enabling the output channel.
    For valid ranges, refer to the Ranges topic for your device in the NI DC Power Supplies and SMUs Help.

    Note: The channel must be enabled for the specified voltage level range to take effect. Refer to the

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    voltage_limit = _attributes.AttributeViReal64(1150010)
    '''Type: float

    Specifies the voltage limit, in volts, that the output cannot exceed when generating the desired current level  on the specified channels.
    This property is applicable only if the output_function property is set to OutputFunction.DC_CURRENT  and the compliance_limit_symmetry property is set to ComplianceLimitSymmetry.SYMMETRIC.
    output_enabled property for more information about enabling the output channel.
    Valid Values: The valid values for this property are defined by the values to which the  voltage_limit_range property is set.

    Note: The channel must be enabled for the specified current level to take effect. Refer to the

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    voltage_limit_autorange = _attributes.AttributeViInt32(1150018)
    '''Type: bool

    Specifies whether NI-DCPower automatically selects the voltage limit range based on the desired voltage limit for  the specified channel(s).
    If this property is set to AutoZero.ON, NI-DCPower ignores any changes you make to the  voltage_limit_range property. If you change the voltage_limit_autorange property from  AutoZero.ON to AutoZero.OFF, NI-DCPower retains the last value the voltage_limit_range  property was set to (or the default value if the property was never set) and uses that value as the voltage limit  range.
    Query the voltage_limit_range property by using the _get_attribute_vi_int32 method to find out  which range NI-DCPower automatically selects.
    The voltage_limit_autorange property is applicable only if the output_function property  is set to OutputFunction.DC_CURRENT.
    Default Value: AutoZero.OFF

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    voltage_limit_high = _attributes.AttributeViReal64(1150185)
    '''Type: float

    Specifies the maximum voltage, in volts, that the output can produce
    when generating the desired current on the specified channel(s).
    This property is applicable only if the `Compliance Limit
    Symmetry <pComplianceLimitSymmetry.html>`__ property is set to
    **Asymmetric** and the `Output
    Method <pOutputFunction.html>`__ property is set to **DC
    Current**.
    You must also specify a `Voltage Limit
    Low <pVoltageLimitLow.html>`__ to complete the asymmetric
    range.
    **Valid Values:** [1% of `Voltage Limit
    Range <pVoltageLimitRange.html>`__, `Voltage Limit
    Range <pVoltageLimitRange.html>`__]
    The range bounded by the limit high and limit low must include zero.
    **Default Value:** Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.
    **Related Topics:**
    `Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
    `Changing
    Ranges <NI_DC_Power_Supplies_Help.chm::/changing_ranges.html>`__
    `Overranging <NI_DC_Power_Supplies_Help.chm::/overranging.html>`__

    Note:
    The limit may be extended beyond the selected limit range if the
    `Overranging Enabled <pOverrangingEnabled.html>`__ property is
    set to TRUE.

    Note:
    One or more of the referenced methods are not in the Python API for this driver.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    voltage_limit_low = _attributes.AttributeViReal64(1150186)
    '''Type: float

    Specifies the minimum voltage, in volts, that the output can produce
    when generating the desired current on the specified channel(s).
    This property is applicable only if the `Compliance Limit
    Symmetry <pComplianceLimitSymmetry.html>`__ property is set to
    **Asymmetric** and the `Output
    Method <pOutputFunction.html>`__ property is set to **DC
    Current**.
    You must also specify a `Voltage Limit
    High <pVoltageLimitHigh.html>`__ to complete the asymmetric
    range.
    **Valid Values:** [-`Voltage Limit
    Range <pVoltageLimitRange.html>`__, -1% of `Voltage Limit
    Range <pVoltageLimitRange.html>`__]
    The range bounded by the limit high and limit low must include zero.
    **Default Value:** Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.
    **Related Topics:**
    `Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
    `Changing
    Ranges <NI_DC_Power_Supplies_Help.chm::/changing_ranges.html>`__
    `Overranging <NI_DC_Power_Supplies_Help.chm::/overranging.html>`__

    Note:
    The limit may be extended beyond the selected limit range if the
    `Overranging Enabled <pOverrangingEnabled.html>`__ property is
    set to TRUE.

    Note:
    One or more of the referenced methods are not in the Python API for this driver.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    voltage_limit_range = _attributes.AttributeViReal64(1150012)
    '''Type: float

    Specifies the voltage limit range, in volts, for the specified channel(s).
    The range defines the valid values to which the voltage limit can be set. Use the voltage_limit_autorange  property to enable automatic selection of the voltage limit range.
    The voltage_limit_range property is applicable only if the output_function property is  set to OutputFunction.DC_CURRENT.
    output_enabled property for more information about enabling the output channel.
    For valid ranges, refer to the Ranges topic for your device in the NI DC Power Supplies and SMUs Help.

    Note: The channel must be enabled for the specified voltage limit range to take effect. Refer to the

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''
    voltage_pole_zero_ratio = _attributes.AttributeViReal64(1150069)
    '''Type: float

    The ratio of the pole frequency to the zero frequency when the channel is in  Constant Voltage mode.
    for information about supported devices.
    Default value: Determined by the value of the TransientResponse.NORMAL setting of the  transient_response property.

    Note: This property is not supported by all devices. Refer to Supported Properties by Device topic

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidcpower.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidcpower.Session repeated capabilities container, and calling set/get value on the result.
    '''

    def __init__(self, repeated_capability_list, vi, library, encoding, freeze_it=False):
        self._repeated_capability_list = repeated_capability_list
        self._repeated_capability = ','.join(repeated_capability_list)
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

        self._is_frozen = freeze_it

    def __repr__(self):
        return '{0}.{1}({2})'.format('nidcpower', self.__class__.__name__, self._param_list)

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
        This method is not supported on all devices. Refer to `Supported
        Methods by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session repeated capabilities container, and calling this method on the result.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        error_code = self._library.niDCPower_CalSelfCalibrate(vi_ctype, channel_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

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
        This method is not supported on all devices. Refer to `Supported
        Methods by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session repeated capabilities container, and calling this method on the result.

        Args:
            aperture_time (float): Specifies the aperture time. Refer to the *Aperture Time* topic for your
                device in the *NI DC Power Supplies and SMUs Help* for more information.

            units (enums.ApertureTimeUnits): Specifies the units for **apertureTime**.
                **Defined Values**:

                +--------------------------------------------+------------------------------+
                | ApertureTimeUnits.SECONDS (1028)           | Specifies seconds.           |
                +--------------------------------------------+------------------------------+
                | ApertureTimeUnits.POWER_LINE_CYCLES (1029) | Specifies Power Line Cycles. |
                +--------------------------------------------+------------------------------+

        '''
        if type(units) is not enums.ApertureTimeUnits:
            raise TypeError('Parameter units must be of type ' + str(enums.ApertureTimeUnits))
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        aperture_time_ctype = _visatype.ViReal64(aperture_time)  # case S150
        units_ctype = _visatype.ViInt32(units.value)  # case S130
        error_code = self._library.niDCPower_ConfigureApertureTime(vi_ctype, channel_name_ctype, aperture_time_ctype, units_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

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

        Note: This method is not supported on all devices. Refer to `Supported Methods by Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm, supportedfunctions)>`__ for more information about supported devices.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session repeated capabilities container, and calling this method on the result.

        Args:
            count (int): Specifies the number of measurements to fetch.

            timeout (hightime.timedelta, datetime.timedelta, or float in seconds): Specifies the maximum time allowed for this method to complete. If the method does not complete within this time interval, NI-DCPower returns an error.

                Note: When setting the timeout interval, ensure you take into account any triggers so that the timeout interval is long enough for your application.


        Returns:
            measurements (list of Measurement): List of named tuples with fields:

                - **voltage** (float)
                - **current** (float)
                - **in_compliance** (bool)

        '''
        import collections
        Measurement = collections.namedtuple('Measurement', ['voltage', 'current', 'in_compliance'])

        voltage_measurements, current_measurements, in_compliance = self._fetch_multiple(timeout, count)

        return [Measurement(voltage=voltage_measurements[i], current=current_measurements[i], in_compliance=in_compliance[i]) for i in range(count)]

    @ivi_synchronized
    def measure_multiple(self):
        '''measure_multiple

        Returns a list of named tuples (Measurement) containing the measured voltage
        and current values on the specified output channel(s). Each call to this method
        blocks other method calls until the measurements are returned from the device.
        The order of the measurements returned in the array corresponds to the order
        on the specified output channel(s).

        Fields in Measurement:

        - **voltage** (float)
        - **current** (float)
        - **in_compliance** (bool) - Always None

        Note: This method is not supported on all devices. Refer to `Supported Methods by Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm, supportedfunctions)>`__ for more information about supported devices.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session repeated capabilities container, and calling this method on the result.

        Returns:
            measurements (list of Measurement): List of named tuples with fields:

                - **voltage** (float)
                - **current** (float)
                - **in_compliance** (bool) - Always None

        '''
        import collections
        Measurement = collections.namedtuple('Measurement', ['voltage', 'current', 'in_compliance'])

        voltage_measurements, current_measurements = self._measure_multiple()

        return [Measurement(voltage=voltage_measurements[i], current=current_measurements[i], in_compliance=None) for i in range(self._parse_channel_count())]

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
        This method is not supported on all devices. Refer to `Supported
        Methods by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session repeated capabilities container, and calling this method on the result.

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

            actual_count (int): Indicates the number of measured values actually retrieved from the
                device.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        timeout_ctype = _converters.convert_timedelta_to_seconds_real64(timeout)  # case S140
        count_ctype = _visatype.ViInt32(count)  # case S210
        voltage_measurements_size = count  # case B600
        voltage_measurements_array = array.array("d", [0] * voltage_measurements_size)  # case B600
        voltage_measurements_ctype = get_ctypes_pointer_for_buffer(value=voltage_measurements_array, library_type=_visatype.ViReal64)  # case B600
        current_measurements_size = count  # case B600
        current_measurements_array = array.array("d", [0] * current_measurements_size)  # case B600
        current_measurements_ctype = get_ctypes_pointer_for_buffer(value=current_measurements_array, library_type=_visatype.ViReal64)  # case B600
        in_compliance_size = count  # case B600
        in_compliance_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViBoolean, size=in_compliance_size)  # case B600
        actual_count_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDCPower_FetchMultiple(vi_ctype, channel_name_ctype, timeout_ctype, count_ctype, voltage_measurements_ctype, current_measurements_ctype, in_compliance_ctype, None if actual_count_ctype is None else (ctypes.pointer(actual_count_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return voltage_measurements_array, current_measurements_array, [bool(in_compliance_ctype[i]) for i in range(count_ctype.value)]

    @ivi_synchronized
    def _get_attribute_vi_boolean(self, attribute_id):
        r'''_get_attribute_vi_boolean

        | Queries the value of a ViBoolean property.
        | You can use this method to get the values of device-specific
          properties and inherent IVI properties.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session repeated capabilities container, and calling this method on the result.

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niDCPower_GetAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(attribute_value_ctype.value)

    @ivi_synchronized
    def _get_attribute_vi_int32(self, attribute_id):
        r'''_get_attribute_vi_int32

        | Queries the value of a ViInt32 property.
        | You can use this method to get the values of device-specific
          properties and inherent IVI properties.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session repeated capabilities container, and calling this method on the result.

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDCPower_GetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(attribute_value_ctype.value)

    @ivi_synchronized
    def _get_attribute_vi_int64(self, attribute_id):
        r'''_get_attribute_vi_int64

        | Queries the value of a ViInt64 property.
        | You can use this method to get the values of device-specific
          properties and inherent IVI properties.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session repeated capabilities container, and calling this method on the result.

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt64()  # case S220
        error_code = self._library.niDCPower_GetAttributeViInt64(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(attribute_value_ctype.value)

    @ivi_synchronized
    def _get_attribute_vi_real64(self, attribute_id):
        r'''_get_attribute_vi_real64

        | Queries the value of a ViReal64 property.
        | You can use this method to get the values of device-specific
          properties and inherent IVI properties.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session repeated capabilities container, and calling this method on the result.

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niDCPower_GetAttributeViReal64(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(attribute_value_ctype.value)

    @ivi_synchronized
    def _get_attribute_vi_string(self, attribute_id):
        r'''_get_attribute_vi_string

        | Queries the value of a ViString property.
        | You can use this method to get the values of device-specific
          properties and inherent IVI properties.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session repeated capabilities container, and calling this method on the result.

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        attribute_value_ctype = None  # case C050
        error_code = self._library.niDCPower_GetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, buffer_size_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        attribute_value_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.niDCPower_GetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, buffer_size_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return attribute_value_ctype.value.decode(self._encoding)

    def _get_error(self):
        r'''_get_error

        | Retrieves and then clears the IVI error information for the session or
          the current execution thread unless **bufferSize** is 0, in which case
          the method does not clear the error information. By passing 0 for
          the buffer size, you can ascertain the buffer size required to get the
          entire error description string and then call the method again with
          a sufficiently large buffer size.
        | If the user specifies a valid IVI session for **vi**, this method
          retrieves and then clears the error information for the session. If
          the user passes VI_NULL for **vi**, this method retrieves and then
          clears the error information for the current execution thread. If
          **vi** is an invalid session, the method does nothing and returns an
          error. Normally, the error information describes the first error that
          occurred since the user last called _get_error or
          ClearError.

        Note:
        One or more of the referenced methods are not in the Python API for this driver.

        Returns:
            code (int): Returns the error code for the session or execution thread.

            description (str): Returns the error description for the IVI session or execution thread.
                If there is no description, the method returns an empty string.
                The buffer must contain at least as many elements as the value you
                specify with **bufferSize**. If the error description, including the
                terminating NUL byte, contains more bytes than you indicate with
                **bufferSize**, the method copies (buffer size - 1) bytes into the
                buffer, places an ASCII NUL byte at the end of the buffer, and returns
                the buffer size you must pass to get the entire value. For example, if
                the value is 123456 and the buffer size is 4, the method places 123
                into the buffer and returns 7.
                If you pass 0 for **bufferSize**, you can pass VI_NULL for this
                property.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        code_ctype = _visatype.ViStatus()  # case S220
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        description_ctype = None  # case C050
        error_code = self._library.niDCPower_GetError(vi_ctype, None if code_ctype is None else (ctypes.pointer(code_ctype)), buffer_size_ctype, description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=True)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        description_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.niDCPower_GetError(vi_ctype, None if code_ctype is None else (ctypes.pointer(code_ctype)), buffer_size_ctype, description_ctype)
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
        self._lock_session()  # We do not call _lock_session() in the context manager so that this function can
        # act standalone as well and let the client call unlock() explicitly. If they do use the context manager,
        # that will handle the unlock for them
        return _Lock(self)

    def _lock_session(self):
        '''_lock_session

        Actual call to driver
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDCPower_LockSession(vi_ctype, None)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return

    @ivi_synchronized
    def measure(self, measurement_type):
        r'''measure

        Returns the measured value of either the voltage or current on the
        specified output channel. Each call to this method blocks other
        method calls until the hardware returns the **measurement**. To
        measure multiple output channels, use the measure_multiple
        method.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session repeated capabilities container, and calling this method on the result.

        Args:
            measurement_type (enums.MeasurementTypes): Specifies whether a voltage or current value is measured.
                **Defined Values**:

                +------------------------------+------------------------------+
                | MeasurementTypes.VOLTAGE (1) | The device measures voltage. |
                +------------------------------+------------------------------+
                | MeasurementTypes.CURRENT (0) | The device measures current. |
                +------------------------------+------------------------------+


        Returns:
            measurement (float): Returns the value of the measurement, either in volts for voltage or
                amps for current.

        '''
        if type(measurement_type) is not enums.MeasurementTypes:
            raise TypeError('Parameter measurement_type must be of type ' + str(enums.MeasurementTypes))
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        measurement_type_ctype = _visatype.ViInt32(measurement_type.value)  # case S130
        measurement_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niDCPower_Measure(vi_ctype, channel_name_ctype, measurement_type_ctype, None if measurement_ctype is None else (ctypes.pointer(measurement_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(measurement_ctype.value)

    @ivi_synchronized
    def _measure_multiple(self):
        r'''_measure_multiple

        Returns arrays of the measured voltage and current values on the
        specified output channel(s). Each call to this method blocks other
        method calls until the measurements are returned from the device. The
        order of the measurements returned in the array corresponds to the order
        on the specified output channel(s).

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session repeated capabilities container, and calling this method on the result.

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        voltage_measurements_size = self._parse_channel_count()  # case B560
        voltage_measurements_array = array.array("d", [0] * voltage_measurements_size)  # case B560
        voltage_measurements_ctype = get_ctypes_pointer_for_buffer(value=voltage_measurements_array, library_type=_visatype.ViReal64)  # case B560
        current_measurements_size = self._parse_channel_count()  # case B560
        current_measurements_array = array.array("d", [0] * current_measurements_size)  # case B560
        current_measurements_ctype = get_ctypes_pointer_for_buffer(value=current_measurements_array, library_type=_visatype.ViReal64)  # case B560
        error_code = self._library.niDCPower_MeasureMultiple(vi_ctype, channel_name_ctype, voltage_measurements_ctype, current_measurements_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return voltage_measurements_array, current_measurements_array

    @ivi_synchronized
    def _parse_channel_count(self):
        r'''_parse_channel_count

        Returns the number of channels.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session repeated capabilities container, and calling this method on the result.

        Returns:
            number_of_channels (int):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channels_string_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        number_of_channels_ctype = _visatype.ViUInt32()  # case S220
        error_code = self._library.niDCPower_ParseChannelCount(vi_ctype, channels_string_ctype, None if number_of_channels_ctype is None else (ctypes.pointer(number_of_channels_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(number_of_channels_ctype.value)

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
        One or more of the referenced methods are not in the Python API for this driver.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session repeated capabilities container, and calling this method on the result.

        Returns:
            in_compliance (bool): Returns whether the device output channel is in compliance.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        in_compliance_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niDCPower_QueryInCompliance(vi_ctype, channel_name_ctype, None if in_compliance_ctype is None else (ctypes.pointer(in_compliance_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(in_compliance_ctype.value)

    @ivi_synchronized
    def query_max_current_limit(self, voltage_level):
        r'''query_max_current_limit

        Queries the maximum current limit on an output channel if the output
        channel is set to the specified **voltageLevel**.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session repeated capabilities container, and calling this method on the result.

        Args:
            voltage_level (float): Specifies the voltage level to use when calculating the
                **maxCurrentLimit**.


        Returns:
            max_current_limit (float): Returns the maximum current limit that can be set with the specified
                **voltageLevel**.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        voltage_level_ctype = _visatype.ViReal64(voltage_level)  # case S150
        max_current_limit_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niDCPower_QueryMaxCurrentLimit(vi_ctype, channel_name_ctype, voltage_level_ctype, None if max_current_limit_ctype is None else (ctypes.pointer(max_current_limit_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(max_current_limit_ctype.value)

    @ivi_synchronized
    def query_max_voltage_level(self, current_limit):
        r'''query_max_voltage_level

        Queries the maximum voltage level on an output channel if the output
        channel is set to the specified **currentLimit**.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session repeated capabilities container, and calling this method on the result.

        Args:
            current_limit (float): Specifies the current limit to use when calculating the
                **maxVoltageLevel**.


        Returns:
            max_voltage_level (float): Returns the maximum voltage level that can be set on an output channel
                with the specified **currentLimit**.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        current_limit_ctype = _visatype.ViReal64(current_limit)  # case S150
        max_voltage_level_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niDCPower_QueryMaxVoltageLevel(vi_ctype, channel_name_ctype, current_limit_ctype, None if max_voltage_level_ctype is None else (ctypes.pointer(max_voltage_level_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(max_voltage_level_ctype.value)

    @ivi_synchronized
    def query_min_current_limit(self, voltage_level):
        r'''query_min_current_limit

        Queries the minimum current limit on an output channel if the output
        channel is set to the specified **voltageLevel**.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session repeated capabilities container, and calling this method on the result.

        Args:
            voltage_level (float): Specifies the voltage level to use when calculating the
                **minCurrentLimit**.


        Returns:
            min_current_limit (float): Returns the minimum current limit that can be set on an output channel
                with the specified **voltageLevel**.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        voltage_level_ctype = _visatype.ViReal64(voltage_level)  # case S150
        min_current_limit_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niDCPower_QueryMinCurrentLimit(vi_ctype, channel_name_ctype, voltage_level_ctype, None if min_current_limit_ctype is None else (ctypes.pointer(min_current_limit_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(min_current_limit_ctype.value)

    @ivi_synchronized
    def query_output_state(self, output_state):
        r'''query_output_state

        Queries the specified output channel to determine if the output channel
        is currently in the state specified by **outputState**.

        **Related Topics:**

        `Compliance <REPLACE_DRIVER_SPECIFIC_URL_1(compliance)>`__

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session repeated capabilities container, and calling this method on the result.

        Args:
            output_state (enums.OutputStates): Specifies the output state of the output channel that is being queried.
                **Defined Values**:

                +--------------------------+-------------------------------------------------------------------+
                | OutputStates.VOLTAGE (0) | The device maintains a constant voltage by adjusting the current. |
                +--------------------------+-------------------------------------------------------------------+
                | OutputStates.CURRENT (1) | The device maintains a constant current by adjusting the voltage. |
                +--------------------------+-------------------------------------------------------------------+


        Returns:
            in_state (bool): Returns whether the device output channel is in the specified output
                state.

        '''
        if type(output_state) is not enums.OutputStates:
            raise TypeError('Parameter output_state must be of type ' + str(enums.OutputStates))
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        output_state_ctype = _visatype.ViInt32(output_state.value)  # case S130
        in_state_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niDCPower_QueryOutputState(vi_ctype, channel_name_ctype, output_state_ctype, None if in_state_ctype is None else (ctypes.pointer(in_state_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(in_state_ctype.value)

    @ivi_synchronized
    def _set_attribute_vi_boolean(self, attribute_id, attribute_value):
        r'''_set_attribute_vi_boolean

        | Sets the value of a ViBoolean property.
        | This is a low-level method that you can use to set the values of
          device-specific properties and inherent IVI properties.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session repeated capabilities container, and calling this method on the result.

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViBoolean(attribute_value)  # case S150
        error_code = self._library.niDCPower_SetAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def _set_attribute_vi_int32(self, attribute_id, attribute_value):
        r'''_set_attribute_vi_int32

        | Sets the value of a ViInt32 property.
        | This is a low-level method that you can use to set the values of
          device-specific properties and inherent IVI properties.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session repeated capabilities container, and calling this method on the result.

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt32(attribute_value)  # case S150
        error_code = self._library.niDCPower_SetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def _set_attribute_vi_int64(self, attribute_id, attribute_value):
        r'''_set_attribute_vi_int64

        | Sets the value of a ViInt64 property.
        | This is a low-level method that you can use to set the values of
          device-specific properties and inherent IVI properties.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session repeated capabilities container, and calling this method on the result.

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt64(attribute_value)  # case S150
        error_code = self._library.niDCPower_SetAttributeViInt64(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def _set_attribute_vi_real64(self, attribute_id, attribute_value):
        r'''_set_attribute_vi_real64

        | Sets the value of a ViReal64 property.
        | This is a low-level method that you can use to set the values of
          device-specific properties and inherent IVI properties.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session repeated capabilities container, and calling this method on the result.

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViReal64(attribute_value)  # case S150
        error_code = self._library.niDCPower_SetAttributeViReal64(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def _set_attribute_vi_string(self, attribute_id, attribute_value):
        r'''_set_attribute_vi_string

        | Sets the value of a ViString property.
        | This is a low-level method that you can use to set the values of
          device-specific properties and inherent IVI properties.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session repeated capabilities container, and calling this method on the result.

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = ctypes.create_string_buffer(attribute_value.encode(self._encoding))  # case C020
        error_code = self._library.niDCPower_SetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

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
        This method is not supported on all devices. Refer to `Supported
        Methods by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session repeated capabilities container, and calling this method on the result.

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        values_ctype = get_ctypes_pointer_for_buffer(value=values, library_type=_visatype.ViReal64)  # case B550
        source_delays_ctype = get_ctypes_pointer_for_buffer(value=source_delays, library_type=_visatype.ViReal64)  # case B550
        size_ctype = _visatype.ViUInt32(0 if values is None else len(values))  # case S160
        if source_delays is not None and len(source_delays) != len(values):  # case S160
            raise ValueError("Length of source_delays and values parameters do not match.")  # case S160
        error_code = self._library.niDCPower_SetSequence(vi_ctype, channel_name_ctype, values_ctype, source_delays_ctype, size_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def unlock(self):
        '''unlock

        Releases a lock that you acquired on an device session using
        lock. Refer to lock for additional
        information on session locks.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDCPower_UnlockSession(vi_ctype, None)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code_ctype = _visatype.ViStatus(error_code)  # case S150
        error_message_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library.niDCPower_error_message(vi_ctype, error_code_ctype, error_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return error_message_ctype.value.decode(self._encoding)


class Session(_SessionBase):
    '''An NI-DCPower session to a National Instruments Programmable Power Supply or Source Measure Unit.'''

    def __init__(self, resource_name, channels=None, reset=False, options={}):
        r'''An NI-DCPower session to a National Instruments Programmable Power Supply or Source Measure Unit.

        Creates and returns a new NI-DCPower session to the power supply or SMU
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

        `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

        Args:
            resource_name (str): Specifies the **resourceName** assigned by Measurement & Automation
                Explorer (MAX), for example "PXI1Slot3" where "PXI1Slot3" is an
                instrument's **resourceName**. **resourceName** can also be a logical
                IVI name.

            channels (str, list, range, tuple): Specifies which output channel(s) to include in a new session. Specify
                multiple channels by using a channel list or a channel range. A channel
                list is a comma (,) separated sequence of channel names (for example,
                0,2 specifies channels 0 and 2). A channel range is a lower bound
                channel followed by a hyphen (-) or colon (:) followed by an upper bound
                channel (for example, 0-2 specifies channels 0, 1, and 2). In the
                Running state, multiple output channel configurations are performed
                sequentially based on the order specified in this parameter. If you do
                not specify any channels, by default all channels on the device are
                included in the session.

            reset (bool): Specifies whether to reset the device during the initialization
                procedure.

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


        Returns:
            session (nidcpower.Session): A session object representing the device.

        '''
        super(Session, self).__init__(repeated_capability_list=[], vi=None, library=None, encoding=None, freeze_it=False)
        channels = _converters.convert_repeated_capabilities_without_prefix(channels)
        options = _converters.convert_init_with_options_dictionary(options)
        self._library = _library_singleton.get()
        self._encoding = 'windows-1251'

        # Call specified init function
        self._vi = 0  # This must be set before calling _initialize_with_channels().
        self._vi = self._initialize_with_channels(resource_name, channels, reset, options)

        # Store the parameter list for later printing in __repr__
        param_list = []
        param_list.append("resource_name=" + pp.pformat(resource_name))
        param_list.append("channels=" + pp.pformat(channels))
        param_list.append("reset=" + pp.pformat(reset))
        param_list.append("options=" + pp.pformat(options))
        self._param_list = ', '.join(param_list)

        self._is_frozen = True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def initiate(self):
        '''initiate

        Starts generation or acquisition, causing the NI-DCPower session to
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
        '''
        return _Acquisition(self)

    def close(self):
        '''close

        Closes the session specified in **vi** and deallocates the resources
        that NI-DCPower reserves. If power output is enabled when you call this
        method, the output channels remain in their existing state and
        continue providing power. Use the ConfigureOutputEnabled
        method to disable power output on a per channel basis. Use the
        reset method to disable power output on all channel(s).

        **Related Topics:**

        `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

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

        Transitions the NI-DCPower session from the Running state to the
        Uncommitted state. If a sequence is running, it is stopped. Any
        configuration methods called after this method are not applied until
        the initiate method is called. If power output is enabled
        when you call the abort method, the output channels remain
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
        One or more of the referenced methods are not in the Python API for this driver.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDCPower_Abort(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def commit(self):
        r'''commit

        Applies previously configured settings to the device. Calling this
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
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDCPower_Commit(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def _create_advanced_sequence(self, sequence_name, attribute_ids, set_as_active_sequence):
        r'''_create_advanced_sequence

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

        Args:
            sequence_name (str): Specifies the name of the sequence to create.

            attribute_ids (list of int): Specifies the properties you reconfigure per step in the advanced
                sequence. The following table lists which properties can be configured
                in an advanced sequence for each NI-DCPower device that supports
                advanced sequencing. A Yes indicates that the property can be configured
                in advanced sequencing. An No indicates that the property cannot be
                configured in advanced sequencing.

                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | Property                       | PXIe-4135 | PXIe-4136 | PXIe-4137 | PXIe-4138 | PXIe-4139 | PXIe-4140/4142/4144 | PXIe-4141/4143/4145 | PXIe-4162/4163 |
                +================================+===========+===========+===========+===========+===========+=====================+=====================+================+
                | dc_noise_rejection             | Yes       | No        | Yes       | No        | Yes       | No                  | No                  | Yes            |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | aperture_time                  | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes            |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | measure_record_length          | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes            |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | sense                          | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes            |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | ovp_enabled                    | Yes       | Yes       | Yes       | No        | No        | No                  | No                  | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | ovp_limit                      | Yes       | Yes       | Yes       | No        | No        | No                  | No                  | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | pulse_bias_delay               | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | pulse_off_time                 | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | pulse_on_time                  | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | source_delay                   | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes            |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | current_compensation_frequency | Yes       | No        | Yes       | No        | Yes       | No                  | Yes                 | Yes            |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | current_gain_bandwidth         | Yes       | No        | Yes       | No        | Yes       | No                  | Yes                 | Yes            |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | current_pole_zero_ratio        | Yes       | No        | Yes       | No        | Yes       | No                  | Yes                 | Yes            |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | voltage_compensation_frequency | Yes       | No        | Yes       | No        | Yes       | No                  | Yes                 | Yes            |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | voltage_gain_bandwidth         | Yes       | No        | Yes       | No        | Yes       | No                  | Yes                 | Yes            |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | voltage_pole_zero_ratio        | Yes       | No        | Yes       | No        | Yes       | No                  | Yes                 | Yes            |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | current_level                  | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes            |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | current_level_range            | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes            |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | voltage_limit                  | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes            |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | voltage_limit_high             | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | voltage_limit_low              | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | voltage_limit_range            | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes            |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | current_limit                  | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes            |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | current_limit_high             | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | current_limit_low              | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | current_limit_range            | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes            |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | voltage_level                  | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes            |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | voltage_level_range            | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes            |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | output_enabled                 | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes            |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | output_function                | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes            |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | output_resistance              | Yes       | No        | Yes       | No        | Yes       | No                  | Yes                 | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | pulse_bias_current_level       | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | pulse_bias_voltage_limit       | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | pulse_bias_voltage_limit_high  | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | pulse_bias_voltage_limit_low   | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | pulse_current_level            | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | pulse_current_level_range      | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | pulse_voltage_limit            | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | pulse_voltage_limit_high       | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | pulse_voltage_limit_low        | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | pulse_voltage_limit_range      | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | pulse_bias_current_limit       | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | pulse_bias_current_limit_high  | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | pulse_bias_current_limit_low   | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | pulse_bias_voltage_level       | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | pulse_current_limit            | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | pulse_current_limit_high       | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | pulse_current_limit_low        | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | pulse_current_limit_range      | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | pulse_voltage_level            | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | pulse_voltage_level_range      | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | transient_response             | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes            |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+

            set_as_active_sequence (bool): Specifies that this current sequence is active.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        sequence_name_ctype = ctypes.create_string_buffer(sequence_name.encode(self._encoding))  # case C020
        attribute_id_count_ctype = _visatype.ViInt32(0 if attribute_ids is None else len(attribute_ids))  # case S160
        attribute_ids_ctype = get_ctypes_pointer_for_buffer(value=attribute_ids, library_type=_visatype.ViInt32)  # case B550
        set_as_active_sequence_ctype = _visatype.ViBoolean(set_as_active_sequence)  # case S150
        error_code = self._library.niDCPower_CreateAdvancedSequence(vi_ctype, sequence_name_ctype, attribute_id_count_ctype, attribute_ids_ctype, set_as_active_sequence_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def create_advanced_sequence_step(self, set_as_active_step=True):
        r'''create_advanced_sequence_step

        Creates a new advanced sequence step in the advanced sequence specified
        by the Active advanced sequence. When you create an advanced sequence
        step, each property you passed to the _create_advanced_sequence
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

        _create_advanced_sequence

        Note:
        This method is not supported on all devices. Refer to `Supported
        Methods by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.

        Args:
            set_as_active_step (bool): Specifies that this current step in the active sequence is active.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        set_as_active_step_ctype = _visatype.ViBoolean(set_as_active_step)  # case S150
        error_code = self._library.niDCPower_CreateAdvancedSequenceStep(vi_ctype, set_as_active_step_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

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
        This method is not supported on all devices. Refer to `Supported
        Methods by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.

        Args:
            sequence_name (str): specifies the name of the sequence to delete.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        sequence_name_ctype = ctypes.create_string_buffer(sequence_name.encode(self._encoding))  # case C020
        error_code = self._library.niDCPower_DeleteAdvancedSequence(vi_ctype, sequence_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def disable(self):
        r'''disable

        This method performs the same actions as the reset
        method, except that this method also immediately sets the
        output_enabled property to False.

        This method opens the output relay on devices that have an output
        relay.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDCPower_Disable(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        size_ctype = _visatype.ViInt32()  # case S170
        configuration_ctype = None  # case B580
        error_code = self._library.niDCPower_ExportAttributeConfigurationBuffer(vi_ctype, size_ctype, configuration_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        size_ctype = _visatype.ViInt32(error_code)  # case S180
        configuration_size = size_ctype.value  # case B590
        configuration_array = array.array("b", [0] * configuration_size)  # case B590
        configuration_ctype = get_ctypes_pointer_for_buffer(value=configuration_array, library_type=_visatype.ViInt8)  # case B590
        error_code = self._library.niDCPower_ExportAttributeConfigurationBuffer(vi_ctype, size_ctype, configuration_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return _converters.convert_to_bytes(configuration_array)

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.niDCPower_ExportAttributeConfigurationFile(vi_ctype, file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

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

        Args:
            sequence_name (str): Specifies the name of the sequence to create.

            property_names (list of str): Specifies the names of the properties you reconfigure per step in the advanced sequence. The following table lists which properties can be configured in an advanced sequence for each NI-DCPower device that supports advanced sequencing. A Yes indicates that the property can be configured in advanced sequencing. An No indicates that the property cannot be configured in advanced sequencing.

                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | Property                       | PXIe-4135 | PXIe-4136 | PXIe-4137 | PXIe-4138 | PXIe-4139 | PXIe-4140/4142/4144 | PXIe-4141/4143/4145 | PXIe-4162/4163 |
                +================================+===========+===========+===========+===========+===========+=====================+=====================+================+
                | dc_noise_rejection             | Yes       | No        | Yes       | No        | Yes       | No                  | No                  | Yes            |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | aperture_time                  | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes            |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | measure_record_length          | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes            |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | sense                          | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes            |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | ovp_enabled                    | Yes       | Yes       | Yes       | No        | No        | No                  | No                  | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | ovp_limit                      | Yes       | Yes       | Yes       | No        | No        | No                  | No                  | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | pulse_bias_delay               | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | pulse_off_time                 | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | pulse_on_time                  | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | source_delay                   | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes            |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | current_compensation_frequency | Yes       | No        | Yes       | No        | Yes       | No                  | Yes                 | Yes            |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | current_gain_bandwidth         | Yes       | No        | Yes       | No        | Yes       | No                  | Yes                 | Yes            |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | current_pole_zero_ratio        | Yes       | No        | Yes       | No        | Yes       | No                  | Yes                 | Yes            |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | voltage_compensation_frequency | Yes       | No        | Yes       | No        | Yes       | No                  | Yes                 | Yes            |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | voltage_gain_bandwidth         | Yes       | No        | Yes       | No        | Yes       | No                  | Yes                 | Yes            |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | voltage_pole_zero_ratio        | Yes       | No        | Yes       | No        | Yes       | No                  | Yes                 | Yes            |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | current_level                  | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes            |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | current_level_range            | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes            |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | voltage_limit                  | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes            |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | voltage_limit_high             | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | voltage_limit_low              | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | voltage_limit_range            | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes            |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | current_limit                  | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes            |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | current_limit_high             | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | current_limit_low              | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | current_limit_range            | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes            |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | voltage_level                  | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes            |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | voltage_level_range            | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes            |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | output_enabled                 | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes            |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | output_function                | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes            |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | output_resistance              | Yes       | No        | Yes       | No        | Yes       | No                  | Yes                 | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | pulse_bias_current_level       | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | pulse_bias_voltage_limit       | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | pulse_bias_voltage_limit_high  | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | pulse_bias_voltage_limit_low   | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | pulse_current_level            | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | pulse_current_level_range      | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | pulse_voltage_limit            | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | pulse_voltage_limit_high       | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | pulse_voltage_limit_low        | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | pulse_voltage_limit_range      | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | pulse_bias_current_limit       | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | pulse_bias_current_limit_high  | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | pulse_bias_current_limit_low   | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | pulse_bias_voltage_level       | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | pulse_current_limit            | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | pulse_current_limit_high       | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | pulse_current_limit_low        | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | pulse_current_limit_range      | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | pulse_voltage_level            | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | pulse_voltage_level_range      | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | transient_response             | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes            |
                +--------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+

            set_as_active_sequence (bool): Specifies that this current sequence is active.

        '''
        # The way the NI-DCPower C API is designed, we need to know all the attribute ID's upfront in order to call
        # `niDCPower_CreateAdvancedSequence`. In order to find the attribute ID of each property, we look at the
        # member Attribute objects of Session. We use a set since we don't have to worry about is it already there.
        attribute_ids_used = set()
        for prop in property_names:
            if prop not in Session.__base__.__dict__:
                raise KeyError('{0} is not an property on the nidcpower.Session'.format(prop))
            if not isinstance(Session.__base__.__dict__[prop], _attributes.Attribute) and not isinstance(Session.__base__.__dict__[prop], _attributes.AttributeEnum):
                raise TypeError('{0} is not a valid property: {1}'.format(prop, type(Session.__base__.__dict__[prop])))
            attribute_ids_used.add(Session.__base__.__dict__[prop]._attribute_id)

        self._create_advanced_sequence(sequence_name, list(attribute_ids_used), set_as_active_sequence)

    @ivi_synchronized
    def get_channel_name(self, index):
        r'''get_channel_name

        Retrieves the output **channelName** that corresponds to the requested
        **index**. Use the channel_count property to
        determine the upper bound of valid values for **index**.

        Args:
            index (int): Specifies which output channel name to return. The index values begin at
                1.


        Returns:
            channel_name (str): Returns the output channel name that corresponds to **index**.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        index_ctype = _visatype.ViInt32(index)  # case S150
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        channel_name_ctype = None  # case C050
        error_code = self._library.niDCPower_GetChannelName(vi_ctype, index_ctype, buffer_size_ctype, channel_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        channel_name_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.niDCPower_GetChannelName(vi_ctype, index_ctype, buffer_size_ctype, channel_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return channel_name_ctype.value.decode(self._encoding)

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        year_ctype = _visatype.ViInt32()  # case S220
        month_ctype = _visatype.ViInt32()  # case S220
        day_ctype = _visatype.ViInt32()  # case S220
        hour_ctype = _visatype.ViInt32()  # case S220
        minute_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDCPower_GetExtCalLastDateAndTime(vi_ctype, None if year_ctype is None else (ctypes.pointer(year_ctype)), None if month_ctype is None else (ctypes.pointer(month_ctype)), None if day_ctype is None else (ctypes.pointer(day_ctype)), None if hour_ctype is None else (ctypes.pointer(hour_ctype)), None if minute_ctype is None else (ctypes.pointer(minute_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(year_ctype.value), int(month_ctype.value), int(day_ctype.value), int(hour_ctype.value), int(minute_ctype.value)

    @ivi_synchronized
    def get_ext_cal_last_temp(self):
        r'''get_ext_cal_last_temp

        Returns the onboard **temperature** of the device, in degrees Celsius,
        during the last successful external calibration.

        Returns:
            temperature (float): Returns the onboard **temperature** of the device, in degrees Celsius,
                during the last successful external calibration.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        temperature_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niDCPower_GetExtCalLastTemp(vi_ctype, None if temperature_ctype is None else (ctypes.pointer(temperature_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(temperature_ctype.value)

    @ivi_synchronized
    def get_ext_cal_recommended_interval(self):
        r'''get_ext_cal_recommended_interval

        Returns the recommended maximum interval, in **months**, between
        external calibrations.

        Returns:
            months (hightime.timedelta): Specifies the recommended maximum interval, in **months**, between
                external calibrations.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        months_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDCPower_GetExtCalRecommendedInterval(vi_ctype, None if months_ctype is None else (ctypes.pointer(months_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return _converters.convert_month_to_timedelta(int(months_ctype.value))

    @ivi_synchronized
    def get_ext_cal_last_date_and_time(self):
        '''get_ext_cal_last_date_and_time

        Returns the date and time of the last successful calibration.

        Returns:
            month (hightime.datetime): Indicates date and time of the last calibration.

        '''
        year, month, day, hour, minute = self._get_ext_cal_last_date_and_time()
        return hightime.datetime(year, month, day, hour, minute)

    @ivi_synchronized
    def get_self_cal_last_date_and_time(self):
        '''get_self_cal_last_date_and_time

        Returns the date and time of the oldest successful self-calibration from among the channels in the session.

        Note: This method is not supported on all devices.

        Returns:
            month (hightime.datetime): Returns the date and time the device was last calibrated.

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
        This method is not supported on all devices. Refer to `Supported
        Methods by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.

        Returns:
            year (int): Returns the **year** the device was last calibrated.

            month (int): Returns the **month** in which the device was last calibrated.

            day (int): Returns the **day** on which the device was last calibrated.

            hour (int): Returns the **hour** (in 24-hour time) in which the device was last
                calibrated.

            minute (int): Returns the **minute** in which the device was last calibrated.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        year_ctype = _visatype.ViInt32()  # case S220
        month_ctype = _visatype.ViInt32()  # case S220
        day_ctype = _visatype.ViInt32()  # case S220
        hour_ctype = _visatype.ViInt32()  # case S220
        minute_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDCPower_GetSelfCalLastDateAndTime(vi_ctype, None if year_ctype is None else (ctypes.pointer(year_ctype)), None if month_ctype is None else (ctypes.pointer(month_ctype)), None if day_ctype is None else (ctypes.pointer(day_ctype)), None if hour_ctype is None else (ctypes.pointer(hour_ctype)), None if minute_ctype is None else (ctypes.pointer(minute_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(year_ctype.value), int(month_ctype.value), int(day_ctype.value), int(hour_ctype.value), int(minute_ctype.value)

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
        This method is not supported on all devices. Refer to `Supported
        Methods by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.

        Returns:
            temperature (float): Returns the onboard **temperature** of the device, in degrees Celsius,
                during the oldest successful calibration.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        temperature_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niDCPower_GetSelfCalLastTemp(vi_ctype, None if temperature_ctype is None else (ctypes.pointer(temperature_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(temperature_ctype.value)

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        size_ctype = _visatype.ViInt32(0 if configuration is None else len(configuration))  # case S160
        configuration_converted = _converters.convert_to_bytes(configuration)  # case B520
        configuration_ctype = get_ctypes_pointer_for_buffer(value=configuration_converted, library_type=_visatype.ViInt8)  # case B520
        error_code = self._library.niDCPower_ImportAttributeConfigurationBuffer(vi_ctype, size_ctype, configuration_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.niDCPower_ImportAttributeConfigurationFile(vi_ctype, file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _initialize_with_channels(self, resource_name, channels=None, reset=False, option_string=""):
        r'''_initialize_with_channels

        Creates and returns a new NI-DCPower session to the power supply or SMU
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

        `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

        Args:
            resource_name (str): Specifies the **resourceName** assigned by Measurement & Automation
                Explorer (MAX), for example "PXI1Slot3" where "PXI1Slot3" is an
                instrument's **resourceName**. **resourceName** can also be a logical
                IVI name.

            channels (str, list, range, tuple): Specifies which output channel(s) to include in a new session. Specify
                multiple channels by using a channel list or a channel range. A channel
                list is a comma (,) separated sequence of channel names (for example,
                0,2 specifies channels 0 and 2). A channel range is a lower bound
                channel followed by a hyphen (-) or colon (:) followed by an upper bound
                channel (for example, 0-2 specifies channels 0, 1, and 2). In the
                Running state, multiple output channel configurations are performed
                sequentially based on the order specified in this parameter. If you do
                not specify any channels, by default all channels on the device are
                included in the session.

            reset (bool): Specifies whether to reset the device during the initialization
                procedure.

            option_string (dict): Specifies the initial value of certain properties for the session. The
                syntax for **optionString** is a list of properties with an assigned
                value where 1 is True and 0 is False. For example:

                "Simulate=0"

                You do not have to specify a value for all the properties. If you do not
                specify a value for a property, the default value is used.

                For more information about simulating a device, refer to `Simulating a
                Power Supply or SMU <REPLACE_DRIVER_SPECIFIC_URL_1(simulate)>`__.


        Returns:
            vi (int): Returns a session handle that you use to identify the device in all
                subsequent NI-DCPower method calls.

        '''
        resource_name_ctype = ctypes.create_string_buffer(resource_name.encode(self._encoding))  # case C020
        channels_ctype = ctypes.create_string_buffer(_converters.convert_repeated_capabilities_without_prefix(channels).encode(self._encoding))  # case C040
        reset_ctype = _visatype.ViBoolean(reset)  # case S150
        option_string_ctype = ctypes.create_string_buffer(_converters.convert_init_with_options_dictionary(option_string).encode(self._encoding))  # case C040
        vi_ctype = _visatype.ViSession()  # case S220
        error_code = self._library.niDCPower_InitializeWithChannels(resource_name_ctype, channels_ctype, reset_ctype, option_string_ctype, None if vi_ctype is None else (ctypes.pointer(vi_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(vi_ctype.value)

    @ivi_synchronized
    def _initiate(self):
        r'''_initiate

        Starts generation or acquisition, causing the NI-DCPower session to
        leave the Uncommitted state or Committed state and enter the Running
        state. To return to the Uncommitted state call the abort
        method. Refer to the `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic in
        the *NI DC Power Supplies and SMUs Help* for information about the
        specific NI-DCPower software states.

        **Related Topics:**

        `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDCPower_Initiate(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def read_current_temperature(self):
        r'''read_current_temperature

        Returns the current onboard **temperature**, in degrees Celsius, of the
        device.

        Returns:
            temperature (float): Returns the onboard **temperature**, in degrees Celsius, of the device.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        temperature_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niDCPower_ReadCurrentTemperature(vi_ctype, None if temperature_ctype is None else (ctypes.pointer(temperature_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(temperature_ctype.value)

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
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDCPower_ResetDevice(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDCPower_ResetWithDefaults(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def send_software_edge_trigger(self, trigger):
        r'''send_software_edge_trigger

        Asserts the specified trigger. This method can override an external
        edge trigger.

        **Related Topics:**

        `Triggers <REPLACE_DRIVER_SPECIFIC_URL_1(trigger)>`__

        Note:
        This method is not supported on all devices. Refer to `Supported
        Methods by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.

        Args:
            trigger (enums.SendSoftwareEdgeTriggerType): Specifies which trigger to assert.
                **Defined Values:**

                +-----------------------------------------------+---------------------------------------+
                | NIDCPOWER_VAL_START_TRIGGER (1034)            | Asserts the Start trigger.            |
                +-----------------------------------------------+---------------------------------------+
                | NIDCPOWER_VAL_SOURCE_TRIGGER (1035)           | Asserts the Source trigger.           |
                +-----------------------------------------------+---------------------------------------+
                | NIDCPOWER_VAL_MEASURE_TRIGGER (1036)          | Asserts the Measure trigger.          |
                +-----------------------------------------------+---------------------------------------+
                | NIDCPOWER_VAL_SEQUENCE_ADVANCE_TRIGGER (1037) | Asserts the Sequence Advance trigger. |
                +-----------------------------------------------+---------------------------------------+
                | NIDCPOWER_VAL_PULSE_TRIGGER (1053)            | Asserts the Pulse trigger.            |
                +-----------------------------------------------+---------------------------------------+
                | NIDCPOWER_VAL_SHUTDOWN_TRIGGER (1118)         | Asserts the Shutdown trigger.         |
                +-----------------------------------------------+---------------------------------------+

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        '''
        if type(trigger) is not enums.SendSoftwareEdgeTriggerType:
            raise TypeError('Parameter trigger must be of type ' + str(enums.SendSoftwareEdgeTriggerType))
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        trigger_ctype = _visatype.ViInt32(trigger.value)  # case S130
        error_code = self._library.niDCPower_SendSoftwareEdgeTrigger(vi_ctype, trigger_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def wait_for_event(self, event_id, timeout=hightime.timedelta(seconds=10.0)):
        r'''wait_for_event

        Waits until the device has generated the specified event.

        The session monitors whether each type of event has occurred at least
        once since the last time this method or the initiate
        method were called. If an event has only been generated once and you
        call this method successively, the method times out. Individual
        events must be generated between separate calls of this method.

        Note:
        Refer to `Supported Methods by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.

        Args:
            event_id (enums.Event): Specifies which event to wait for.
                **Defined Values:**

                +--------------------------------------------------------+--------------------------------------------------+
                | NIDCPOWER_VAL_SOURCE_COMPLETE_EVENT (1030)             | Waits for the Source Complete event.             |
                +--------------------------------------------------------+--------------------------------------------------+
                | NIDCPOWER_VAL_MEASURE_COMPLETE_EVENT (1031)            | Waits for the Measure Complete event.            |
                +--------------------------------------------------------+--------------------------------------------------+
                | NIDCPOWER_VAL_SEQUENCE_ITERATION_COMPLETE_EVENT (1032) | Waits for the Sequence Iteration Complete event. |
                +--------------------------------------------------------+--------------------------------------------------+
                | NIDCPOWER_VAL_SEQUENCE_ENGINE_DONE_EVENT (1033)        | Waits for the Sequence Engine Done event.        |
                +--------------------------------------------------------+--------------------------------------------------+
                | NIDCPOWER_VAL_PULSE_COMPLETE_EVENT (1051 )             | Waits for the Pulse Complete event.              |
                +--------------------------------------------------------+--------------------------------------------------+
                | NIDCPOWER_VAL_READY_FOR_PULSE_TRIGGER_EVENT (1052)     | Waits for the Ready for Pulse Trigger event.     |
                +--------------------------------------------------------+--------------------------------------------------+

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        event_id_ctype = _visatype.ViInt32(event_id.value)  # case S130
        timeout_ctype = _converters.convert_timedelta_to_seconds_real64(timeout)  # case S140
        error_code = self._library.niDCPower_WaitForEvent(vi_ctype, event_id_ctype, timeout_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _close(self):
        r'''_close

        Closes the session specified in **vi** and deallocates the resources
        that NI-DCPower reserves. If power output is enabled when you call this
        method, the output channels remain in their existing state and
        continue providing power. Use the ConfigureOutputEnabled
        method to disable power output on a per channel basis. Use the
        reset method to disable power output on all channel(s).

        **Related Topics:**

        `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

        Note:
        One or more of the referenced methods are not in the Python API for this driver.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDCPower_close(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

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
    def reset(self):
        r'''reset

        Resets the device to a known state. This method disables power
        generation, resets session properties to their default values, commits
        the session properties, and leaves the session in the Uncommitted state.
        Refer to the `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic for
        more information about NI-DCPower software states.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDCPower_reset(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        self_test_result_ctype = _visatype.ViInt16()  # case S220
        self_test_message_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library.niDCPower_self_test(vi_ctype, None if self_test_result_ctype is None else (ctypes.pointer(self_test_result_ctype)), self_test_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(self_test_result_ctype.value), self_test_message_ctype.value.decode(self._encoding)



