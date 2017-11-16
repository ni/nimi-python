# -*- coding: utf-8 -*-
# This file was generated
import ctypes

from nidcpower import attributes
from nidcpower import enums
from nidcpower import errors
from nidcpower import library_singleton
from nidcpower import visatype


class _Acquisition(object):
    def __init__(self, session):
        self._session = session

    def __enter__(self):
        self._session._initiate()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._session._abort()


class _SessionBase(object):
    '''Base class for all NI-DCPower sessions.'''

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

    active_advanced_sequence = attributes.AttributeViString(1150074)
    '''
    Specifies the advanced sequence to configure or generate.

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device topic.

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    active_advanced_sequence.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    active_advanced_sequence.Session instance, and calling set/get value on the result.:

        session['0,1'].active_advanced_sequence = var
        var = session['0,1'].active_advanced_sequence
    '''
    active_advanced_sequence_step = attributes.AttributeViInt64(1150075)
    '''
    Specifies the advanced sequence step to configure.

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device topic.

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    active_advanced_sequence_step.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    active_advanced_sequence_step.Session instance, and calling set/get value on the result.:

        session['0,1'].active_advanced_sequence_step = var
        var = session['0,1'].active_advanced_sequence_step
    '''
    aperture_time = attributes.AttributeViReal64(1150058)
    '''
    Specifies the measurement aperture time for the channel configuration. Aperture time is specified in the units set by  the NIDCPOWER_ATTR_APERTURE_TIME_UNITS attribute.
    for information about supported devices.
    Refer to the Aperture Time topic in the NI DC Power Supplies and SMUs Help for more information about how to configure  your measurements and for information about valid values.
    Default Value: 0.01666666 seconds

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device topic

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    aperture_time.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    aperture_time.Session instance, and calling set/get value on the result.:

        session['0,1'].aperture_time = var
        var = session['0,1'].aperture_time
    '''
    aperture_time_units = attributes.AttributeEnum(attributes.AttributeViInt32, enums.ApertureTimeUnits, 1150059)
    '''
    Specifies the units of the NIDCPOWER_ATTR_APERTURE_TIME attribute for the channel configuration.
    for information about supported devices.
    Refer to the Aperture Time topic in the NI DC Power Supplies and SMUs Help for more information about  how to configure your measurements and for information about valid values.
    Default Value: NIDCPOWER_VAL_SECONDS

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device topic

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    aperture_time_units.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    aperture_time_units.Session instance, and calling set/get value on the result.:

        session['0,1'].aperture_time_units = var
        var = session['0,1'].aperture_time_units
    '''
    auto_zero = attributes.AttributeEnum(attributes.AttributeViInt32, enums.AutoZero, 1150055)
    '''
    Specifies the auto-zero method to use on the device.
    Refer to the NI PXI-4132 Measurement Configuration and Timing and Auto Zero topics for more information  about how to configure your measurements.
    Default Value: The default value for the NI PXI-4132 is NIDCPOWER_VAL_ON. The default value for  all other devices is NIDCPOWER_VAL_OFF, which is the only supported value for these devices.

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    auto_zero.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    auto_zero.Session instance, and calling set/get value on the result.:

        session['0,1'].auto_zero = var
        var = session['0,1'].auto_zero
    '''
    auxiliary_power_source_available = attributes.AttributeViBoolean(1150002)
    '''
    Indicates whether an auxiliary power source is connected to the device.
    A value of VI_FALSE may indicate that the auxiliary input fuse has blown.  Refer to the Detecting Internal/Auxiliary Power topic in the NI DC Power Supplies and SMUs Help for  more information about internal and auxiliary power.
    power source to generate power. Use the NIDCPOWER_ATTR_POWER_SOURCE_IN_USE attribute to retrieve this information.

    Note: This attribute does not necessarily indicate if the device is using the auxiliary
    '''
    cache = attributes.AttributeViBoolean(1050004)
    '''
    Specifies whether to cache the value of attributes.
    When caching is enabled, NI-DCPower records the current power supply settings and avoids sending  redundant commands to the device. Enabling caching can significantly increase execution speed.
    NI-DCPower might always cache or never cache particular attributes regardless of the setting of this attribute.
    Use the niDCPower_InitializeWithChannels function to override this value.
    Default Value: VI_TRUE
    '''
    channel_count = attributes.AttributeViInt32(1050203)
    '''
    Indicates the number of channels that NI-DCPower supports for the instrument that was chosen when  the current session was opened. For channel-based attributes, the IVI engine maintains a separate  cache value for each channel.
    '''
    current_compensation_frequency = attributes.AttributeViReal64(1150071)
    '''
    The frequency at which a pole-zero pair is added to the system when the channel is in  Constant Current mode.
    for information about supported devices.
    Default Value: Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the  NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute.

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device topic

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    current_compensation_frequency.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    current_compensation_frequency.Session instance, and calling set/get value on the result.:

        session['0,1'].current_compensation_frequency = var
        var = session['0,1'].current_compensation_frequency
    '''
    current_gain_bandwidth = attributes.AttributeViReal64(1150070)
    '''
    The frequency at which the unloaded loop gain extrapolates to 0 dB in the absence of additional poles and zeroes.  This attribute takes effect when the channel is in Constant Current mode.
    for information about supported devices.
    Default Value: Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the  NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute.

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device topic

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    current_gain_bandwidth.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    current_gain_bandwidth.Session instance, and calling set/get value on the result.:

        session['0,1'].current_gain_bandwidth = var
        var = session['0,1'].current_gain_bandwidth
    '''
    current_level = attributes.AttributeViReal64(1150009)
    '''
    Specifies the current level, in amps, that the device attempts to generate on the specified channel(s).
    This attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_DC_CURRENT.
    NIDCPOWER_ATTR_OUTPUT_ENABLED attribute for more information about enabling the output channel.
    Valid Values: The valid values for this attribute are defined by the values to which the  NIDCPOWER_ATTR_CURRENT_LEVEL_RANGE attribute is set.

    Note: The channel must be enabled for the specified current level to take effect. Refer to the

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    current_level.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    current_level.Session instance, and calling set/get value on the result.:

        session['0,1'].current_level = var
        var = session['0,1'].current_level
    '''
    current_level_autorange = attributes.AttributeEnum(attributes.AttributeViInt32, enums.CurrentLevelAutorange, 1150017)
    '''
    Specifies whether NI-DCPower automatically selects the current level range based on the desired current level for  the specified channels.
    If you set this attribute to NIDCPOWER_VAL_ON, NI-DCPower ignores any changes you make to the  NIDCPOWER_ATTR_CURRENT_LEVEL_RANGE attribute. If you change the NIDCPOWER_ATTR_CURRENT_LEVEL_AUTORANGE attribute from  NIDCPOWER_VAL_ON to NIDCPOWER_VAL_OFF, NI-DCPower retains the last value the NIDCPOWER_ATTR_CURRENT_LEVEL_RANGE  attribute was set to (or the default value if the attribute was never set) and uses that value as the  current level range.
    Query the NIDCPOWER_ATTR_CURRENT_LEVEL_RANGE attribute by using the niDCPower_GetAttributeViInt32 function for  information about which range NI-DCPower automatically selects.
    The NIDCPOWER_ATTR_CURRENT_LEVEL_AUTORANGE attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute  is set to NIDCPOWER_VAL_DC_CURRENT.
    Default Value: NIDCPOWER_VAL_OFF

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    current_level_autorange.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    current_level_autorange.Session instance, and calling set/get value on the result.:

        session['0,1'].current_level_autorange = var
        var = session['0,1'].current_level_autorange
    '''
    current_level_range = attributes.AttributeViReal64(1150011)
    '''
    Specifies the current level range, in amps, for the specified channel(s).
    The range defines the valid value to which the current level can be set. Use the  NIDCPOWER_ATTR_CURRENT_LEVEL_AUTORANGE attribute to enable automatic selection of the current level range.
    The NIDCPOWER_ATTR_CURRENT_LEVEL_RANGE attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is  set to NIDCPOWER_VAL_DC_CURRENT.
    NIDCPOWER_ATTR_OUTPUT_ENABLED attribute for more information about enabling the output channel.
    For valid ranges, refer to the Ranges topic for your device in the NI DC Power Supplies and SMUs Help.

    Note: The channel must be enabled for the specified current level range to take effect. Refer to the

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    current_level_range.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    current_level_range.Session instance, and calling set/get value on the result.:

        session['0,1'].current_level_range = var
        var = session['0,1'].current_level_range
    '''
    current_limit = attributes.AttributeViReal64(1250005)
    '''
    Specifies the current limit, in amps, that the output cannot exceed when generating the desired voltage level  on the specified channel(s).
    This attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to  NIDCPOWER_VAL_DC_VOLTAGE.
    NIDCPOWER_ATTR_OUTPUT_ENABLED attribute for more information about enabling the output channel.
    Valid Values: The valid values for this attribute are defined by the values to which  NIDCPOWER_ATTR_CURRENT_LIMIT_RANGE attribute is set.

    Note: The channel must be enabled for the specified current limit to take effect. Refer to the

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    current_limit.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    current_limit.Session instance, and calling set/get value on the result.:

        session['0,1'].current_limit = var
        var = session['0,1'].current_limit
    '''
    current_limit_autorange = attributes.AttributeEnum(attributes.AttributeViInt32, enums.CurrentLimitAutorange, 1150016)
    '''
    Specifies whether NI-DCPower automatically selects the current limit range based on the desired current limit for the  specified channel(s).
    If you set this attribute to NIDCPOWER_VAL_ON, NI-DCPower ignores any changes you make to the  NIDCPOWER_ATTR_CURRENT_LIMIT_RANGE attribute. If you change this attribute from NIDCPOWER_VAL_ON to  NIDCPOWER_VAL_OFF, NI-DCPower retains the last value the NIDCPOWER_ATTR_CURRENT_LIMIT_RANGE attribute was set to  (or the default value if the attribute was never set) and uses that value as the current limit range.
    Query the NIDCPOWER_ATTR_CURRENT_LIMIT_RANGE attribute by using the niDCPower_GetAttributeViInt32 function for  information about which range NI-DCPower automatically selects.
    The NIDCPOWER_ATTR_CURRENT_LIMIT_AUTORANGE attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute  is set to NIDCPOWER_VAL_DC_VOLTAGE.
    Default Value: NIDCPOWER_VAL_OFF

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    current_limit_autorange.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    current_limit_autorange.Session instance, and calling set/get value on the result.:

        session['0,1'].current_limit_autorange = var
        var = session['0,1'].current_limit_autorange
    '''
    current_limit_range = attributes.AttributeViReal64(1150004)
    '''
    Specifies the current limit range, in amps, for the specified channel(s).
    The range defines the valid value to which the current limit can be set. Use the NIDCPOWER_ATTR_CURRENT_LIMIT_AUTORANGE  attribute to enable automatic selection of the current limit range.
    The NIDCPOWER_ATTR_CURRENT_LIMIT_RANGE attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute  is set to NIDCPOWER_VAL_DC_VOLTAGE.
    NIDCPOWER_ATTR_OUTPUT_ENABLED attribute for more information about enabling the output channel.
    For valid ranges, refer to the Ranges topic for your device in the NI DC Power Supplies and SMUs Help.

    Note: The channel must be enabled for the specified current limit to take effect. Refer to the

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    current_limit_range.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    current_limit_range.Session instance, and calling set/get value on the result.:

        session['0,1'].current_limit_range = var
        var = session['0,1'].current_limit_range
    '''
    current_pole_zero_ratio = attributes.AttributeViReal64(1150072)
    '''
    The ratio of the pole frequency to the zero frequency when the channel is in  Constant Current mode.
    for information about supported devices.
    Default Value: Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute.

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device topic

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    current_pole_zero_ratio.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    current_pole_zero_ratio.Session instance, and calling set/get value on the result.:

        session['0,1'].current_pole_zero_ratio = var
        var = session['0,1'].current_pole_zero_ratio
    '''
    dc_noise_rejection = attributes.AttributeEnum(attributes.AttributeViInt32, enums.DCNoiseRejection, 1150066)
    '''
    Determines the relative weighting of samples in a measurement. Refer to the NI PXIe-4140/4141 DC Noise Rejection,  NI PXIe-4142/4143 DC Noise Rejection, or NI PXIe-4144/4145 DC Noise Rejection topic in the NI DC Power Supplies  and SMUs Help for more information about noise rejection.
    for information about supported devices.
    Default Value: NIDCPOWER_VAL_NORMAL

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device topic
    '''
    digital_edge_measure_trigger_edge = attributes.AttributeEnum(attributes.AttributeViInt32, enums.DigitalEdge, 1150035)
    '''
    Specifies whether to configure the Measure trigger to assert on the rising or falling edge.
    NIDCPOWER_ATTR_SOURCE_TRIGGER_TYPE attribute is set to NIDCPOWER_VAL_DIGITAL_EDGE.
    for information about supported devices.
    Default Value: NIDCPOWER_VAL_RISING

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device topic
    '''
    digital_edge_measure_trigger_input_terminal = attributes.AttributeViString(1150036)
    '''
    Specifies the input terminal for the Measure trigger. This attribute is used only when the  NIDCPOWER_ATTR_MEASURE_TRIGGER_TYPE attribute is set to NIDCPOWER_VAL_DIGITAL_EDGE.
    for this attribute.
    You can specify any valid input terminal for this attribute. Valid terminals are listed in  Measurement & Automation Explorer under the Device Routes tab.
    Input terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you  can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal  name, PXI_Trig0. The input terminal can also be a terminal from another device. For example, you can set the input  terminal on Dev1 to be /Dev2/SourceCompleteEvent.

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device topic
    '''
    digital_edge_pulse_trigger_edge = attributes.AttributeEnum(attributes.AttributeViInt32, enums.DigitalEdge, 1150096)
    '''
    Specifies whether to configure the Pulse trigger to assert on the rising or falling edge.
    Default Value: NIDCPOWER_VAL_RISING

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device for information about supported devices.
    '''
    digital_edge_pulse_trigger_input_terminal = attributes.AttributeViString(1150097)
    '''
    Specifies the input terminal for the Pulse trigger. This attribute is used only when the NIDCPOWER_ATTR_PULSE_TRIGGER_TYPE attribute is set to digital edge.
    You can specify any valid input terminal for this attribute. Valid terminals are listed in Measurement & Automation Explorer under the Device Routes tab.
    Input terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0. The input terminal can also be a terminal from another device. For example, you can set the input terminal on Dev1 to be /Dev2/SourceCompleteEvent.

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device for information about supported devices.
    '''
    digital_edge_sequence_advance_trigger_edge = attributes.AttributeEnum(attributes.AttributeViInt32, enums.DigitalEdge, 1150027)
    '''
    Specifies whether to configure the Sequence Advance trigger to assert on the rising or falling edge.
    for information about supported devices.
    Default Value: NIDCPOWER_VAL_RISING

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device topic
    '''
    digital_edge_sequence_advance_trigger_input_terminal = attributes.AttributeViString(1150028)
    '''
    Specifies the input terminal for the Sequence Advance trigger. Use this attribute only when the  NIDCPOWER_ATTR_SEQUENCE_ADVANCE_TRIGGER_TYPE attribute is set to NIDCPOWER_VAL_DIGITAL_EDGE.
    the NI DC Power Supplies and SMUs Help for information about supported devices.
    You can specify any valid input terminal for this attribute. Valid terminals are listed in Measurement & Automation Explorer under the Device Routes tab.
    Input terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can  specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal  name, PXI_Trig0. The input terminal can also be a terminal from another device. For example, you can set the  input terminal on Dev1 to be /Dev2/SourceCompleteEvent.

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device topic in
    '''
    digital_edge_source_trigger_edge = attributes.AttributeEnum(attributes.AttributeViInt32, enums.DigitalEdge, 1150031)
    '''
    Specifies whether to configure the Source trigger to assert on the rising or falling edge.
    for information about supported devices.
    Default Value: NIDCPOWER_VAL_RISING

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device topic
    '''
    digital_edge_source_trigger_input_terminal = attributes.AttributeViString(1150032)
    '''
    Specifies the input terminal for the Source trigger. Use this attribute only when the  NIDCPOWER_ATTR_SOURCE_TRIGGER_TYPE attribute is set to NIDCPOWER_VAL_DIGITAL_EDGE.
    for information about supported devices.
    You can specify any valid input terminal for this attribute. Valid terminals are listed  in Measurement & Automation Explorer under the Device Routes tab.
    Input terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you  can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal  name, PXI_Trig0. The input terminal can also be a terminal from another device. For example, you can set the input  terminal on Dev1 to be /Dev2/SourceCompleteEvent.

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device topic
    '''
    digital_edge_start_trigger_edge = attributes.AttributeEnum(attributes.AttributeViInt32, enums.DigitalEdge, 1150022)
    '''
    Specifies whether to configure the Start trigger to assert on the rising or falling edge.
    for information about supported devices.
    Default Value: NIDCPOWER_VAL_RISING

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device topic
    '''
    digital_edge_start_trigger_input_terminal = attributes.AttributeViString(1150023)
    '''
    Specifies the input terminal for the Start trigger. Use this attribute only when the NIDCPOWER_ATTR_START_TRIGGER_TYPE  attribute is set to NIDCPOWER_VAL_DIGITAL_EDGE.
    for information about supported devices.
    You can specify any valid input terminal for this attribute. Valid terminals are listed in Measurement & Automation  Explorer under the Device Routes tab.
    Input terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can  specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name,  PXI_Trig0. The input terminal can also be a terminal from another device. For example, you can set the input terminal  on Dev1 to be /Dev2/SourceCompleteEvent.

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device topic
    '''
    driver_setup = attributes.AttributeViString(1050007)
    '''
    Indicates the Driver Setup string that you specified when initializing the driver.
    Some cases exist where you must specify the instrument driver options at initialization  time. An example of this case is specifying a particular device model from among a family  of devices that the driver supports. This attribute is useful when simulating a device.  You can specify the driver-specific options through the DriverSetup keyword in the optionsString  parameter in the niDCPower_InitializeWithChannels function or through the  IVI Configuration Utility.
    You can specify  driver-specific options through the DriverSetup keyword in the  optionsString parameter in the niDCPower_InitializeWithChannels function. If you do not specify a Driver Setup string, this attribute returns an empty string.
    '''
    exported_measure_trigger_output_terminal = attributes.AttributeViString(1150037)
    '''
    Specifies the output terminal for exporting the Measure trigger.
    Refer to the Device Routes tab in Measurement & Automation Explorer for a list of the terminals  available on your device.
    for information about supported devices.
    Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you  can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal  name, PXI_Trig0.

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device topic
    '''
    exported_pulse_trigger_output_terminal = attributes.AttributeViString(1150098)
    '''
    Specifies the output terminal for exporting the Pulse trigger.
    Refer to the Device Routes tab in Measurement & Automation Explorer for a list of the terminals available on your device.
    Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device for information about supported devices.
    '''
    exported_sequence_advance_trigger_output_terminal = attributes.AttributeViString(1150029)
    '''
    Specifies the output terminal for exporting the Sequence Advance trigger.
    Refer to the Device Routes tab in Measurement & Automation Explorer for a list of the terminals  available on your device.
    for information about supported devices.
    Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you  can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal  name, PXI_Trig0.

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device topic
    '''
    exported_source_trigger_output_terminal = attributes.AttributeViString(1150033)
    '''
    Specifies the output terminal for exporting the Source trigger.
    Refer to the Device Routes tab in MAX for a list of the terminals available on your device.
    for information about supported devices.
    Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you  can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal  name, PXI_Trig0.

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device topic
    '''
    exported_start_trigger_output_terminal = attributes.AttributeViString(1150024)
    '''
    Specifies the output terminal for exporting the Start trigger.
    Refer to the Device Routes tab in Measurement & Automation Explorer (MAX) for a list of the terminals available  on your device.
    Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you  can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name,  PXI_Trig0.
    for information about supported devices.

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device topic
    '''
    fetch_backlog = attributes.AttributeViInt32(1150056)
    '''
    Returns the number of measurements acquired that have not been fetched yet.
    '''
    group_capabilities = attributes.AttributeViString(1050401)
    '''
    Contains a comma-separated list of class-extension groups that NI-DCPower implements.
    '''
    instrument_firmware_revision = attributes.AttributeViString(1050510)
    '''
    Contains the firmware revision information for the device you are currently using.
    '''
    instrument_manufacturer = attributes.AttributeViString(1050511)
    '''
    Contains the name of the manufacturer for the device you are currently using.
    '''
    instrument_model = attributes.AttributeViString(1050512)
    '''
    Contains the model number or name of the device that you are currently using.
    '''
    interchange_check = attributes.AttributeViBoolean(1050021)
    '''
    Specifies whether to perform interchangeability checking and log interchangeability warnings when you  call NI-DCPower functions. VI_TRUE specifies that interchangeability checking is enabled.
    Interchangeability warnings indicate that using your application with a different power supply might  cause different behavior. Call the niDCPower_GetNextInterchangeWarning function to retrieve  interchange warnings.
    Call the niDCPower_GetNextInterchangeWarning function to clear the list of interchangeability warnings  without reading them.
    Interchangeability checking examines the attributes in a capability group only if you specify a value  for at least one attribute within that group. Interchangeability warnings can occur when an attribute  affects the behavior of the device and you have not set that attribute or when the attribute has been  invalidated since you set it.
    Default Value: VI_FALSE
    '''
    interlock_input_open = attributes.AttributeViBoolean(1150105)
    '''
    Indicates whether the safety interlock circuit is open.
    Refer to the Safety Interlock topic in the NI DC Power Supplies and SMUs Help for more information about  the safety interlock circuit.
    about supported devices.

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device for information
    '''
    io_resource_descriptor = attributes.AttributeViString(1050304)
    '''
    Indicates the resource descriptor NI-DCPower uses to identify the physical device.
    If you initialize NI-DCPower with a logical name, this attribute contains the resource descriptor  that corresponds to the entry in the IVI Configuration utility.
    If you initialize NI-DCPower with the resource descriptor, this attribute contains that value.
    '''
    logical_name = attributes.AttributeViString(1050305)
    '''
    Contains the logical name you specified when opening the current IVI session.
    You can pass a logical name to the niDCPower_InitializeWithChannels function.  The IVI Configuration utility must contain an entry for the logical name. The logical name entry  refers to a function section in the IVI Configuration file. The function section specifies a physical  device and initial user options.
    '''
    measure_buffer_size = attributes.AttributeViInt32(1150077)
    '''
    Specifies the number of samples that the active channel measurement buffer can hold.
    The default value is the maximum number of samples that a device is capable of recording in one second.
    for information about supported devices.
    Valid Values: 1000 to 2147483647
    Default Value: Varies by device. Refer to Supported Attributes by Device topic in  the NI DC Power Supplies and SMUs Help for more information about default values.

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device topic
    '''
    measure_complete_event_delay = attributes.AttributeViReal64(1150046)
    '''
    Specifies the amount of time to delay the generation of the Measure Complete event, in seconds.
    for information about supported devices.
    Valid Values: 0 to 167 seconds
    Default Value: The NI PXI-4132 and NI PXIe-4140/4141/4142/4143/4144/4145/4154 supports values from  0 seconds to 167 seconds.

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device topic
    '''
    measure_complete_event_output_terminal = attributes.AttributeViString(1150047)
    '''
    Specifies the output terminal for exporting the Measure Complete event.
    for information about supported devices.
    Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal  is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or  with the shortened terminal name, PXI_Trig0.

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device topic
    '''
    measure_complete_event_pulse_polarity = attributes.AttributeEnum(attributes.AttributeViInt32, enums.Polarity, 1150044)
    '''
    Specifies the behavior of the Measure Complete event.
    for information about supported devices.
    Default Value: NIDCPOWER_VAL_ACTIVE_HIGH

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device topic
    '''
    measure_complete_event_pulse_width = attributes.AttributeViReal64(1150045)
    '''
    Specifies the width of the Measure Complete event, in seconds.
    The minimum event pulse width value for PXI devices is 150 ns, and the minimum event pulse  width value for PXI Express devices is 250 ns.
    The maximum event pulse width value for all devices is 1.6 microseconds.
    for information about supported devices.
    Valid Values: 1.5e-7 to 1.6e-6
    Default Value: The default value for PXI devices is 150 ns. The default value  for PXI Express devices is 250 ns.

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device topic
    '''
    measure_record_delta_time = attributes.AttributeViReal64(1150065)
    '''
    Queries the amount of time, in seconds, between between the start of two consecutive measurements in a measure record.  Only query this attribute after the desired measurement settings are committed.
    for information about supported devices.
    two measurements and the rest would differ.

    Note: This attribute is not available when Auto Zero is configured to Once because the amount of time between the first
    '''
    measure_record_length = attributes.AttributeViInt32(1150063)
    '''
    Specifies how many measurements compose a measure record. When this attribute is set to a value greater than 1, the  NIDCPOWER_ATTR_MEASURE_WHEN attribute must be set to NIDCPOWER_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE or  NIDCPOWER_VAL_ON_MEASURE_TRIGGER.
    for information about supported devices.
    Valid Values: 1 to 16,777,216
    Default Value: 1

    Note:
    This attribute is not available in a session involving multiple channels.
    '''
    measure_record_length_is_finite = attributes.AttributeViBoolean(1150064)
    '''
    Specifies whether to take continuous measurements. Call the niDCPower_Abort function to stop continuous measurements.  When this attribute is set to VI_FALSE and the NIDCPOWER_ATTR_SOURCE_MODE attribute is set to  NIDCPOWER_VAL_SINGLE_POINT, the NIDCPOWER_ATTR_MEASURE_WHEN attribute must be set to  NIDCPOWER_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE or NIDCPOWER_VAL_ON_MEASURE_TRIGGER. When this attribute is set to  VI_FALSE and the NIDCPOWER_ATTR_SOURCE_MODE attribute is set to NIDCPOWER_VAL_SEQUENCE, the NIDCPOWER_ATTR_MEASURE_WHEN  attribute must be set to NIDCPOWER_VAL_ON_MEASURE_TRIGGER.
    for information about supported devices.
    Default Value: VI_TRUE

    Note:
    This attribute is not available in a session involving multiple channels.
    '''
    measure_trigger_type = attributes.AttributeEnum(attributes.AttributeViInt32, enums.TriggerType, 1150034)
    '''
    Specifies the behavior of the Measure trigger.
    for information about supported devices.
    Default Value: NIDCPOWER_VAL_DIGITAL_EDGE

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device topic
    '''
    measure_when = attributes.AttributeEnum(attributes.AttributeViInt32, enums.MeasureWhen, 1150057)
    '''
    Specifies when the measure unit should acquire measurements. Unless this attribute is configured to  NIDCPOWER_VAL_ON_MEASURE_TRIGGER, the NIDCPOWER_ATTR_MEASURE_TRIGGER_TYPE attribute is ignored.
    Refer to the Acquiring Measurements topic in the NI DC Power Supplies and SMUs Help for more information about how to  configure your measurements.
    Default Value: If the NIDCPOWER_ATTR_SOURCE_MODE attribute is set to NIDCPOWER_VAL_SINGLE_POINT, the default value is  NIDCPOWER_VAL_ON_DEMAND. This value supports only the niDCPower_Measure function and niDCPower_MeasureMultiple  function. If the NIDCPOWER_ATTR_SOURCE_MODE attribute is set to NIDCPOWER_VAL_SEQUENCE, the default value is  NIDCPOWER_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE. This value supports only the niDCPower_FetchMultiple function.
    '''
    output_capacitance = attributes.AttributeEnum(attributes.AttributeViInt32, enums.OutputCapacitance, 1150014)
    '''
    Specifies whether to use a low or high capacitance on the output for the specified channel(s).
    for information about supported devices.
    Refer to the NI PXI-4130 Output Capacitance Selection topic in the NI DC Power Supplies and SMUs Help for more  information about capacitance.

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device topic

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    output_capacitance.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    output_capacitance.Session instance, and calling set/get value on the result.:

        session['0,1'].output_capacitance = var
        var = session['0,1'].output_capacitance
    '''
    output_connected = attributes.AttributeViBoolean(1150060)
    '''
    Specifies whether the output relay is connected (closed) or disconnected (open). The NIDCPOWER_ATTR_OUTPUT_ENABLED  attribute does not change based on this attribute; they are independent of each other.
    about supported devices.
    Set this attribute to VI_FALSE to disconnect the output terminal from the output.
    to the output terminal might discharge unless the relay is disconnected. Excessive connecting and disconnecting of the  output can cause premature wear on the relay.
    Default Value: VI_TRUE

    Note: Only disconnect the output when disconnecting is necessary for your application. For example, a battery connected

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    output_connected.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    output_connected.Session instance, and calling set/get value on the result.:

        session['0,1'].output_connected = var
        var = session['0,1'].output_connected
    '''
    output_enabled = attributes.AttributeViBoolean(1250006)
    '''
    Specifies whether the output is enabled (VI_TRUE) or disabled (VI_FALSE).
    Depending on the value you specify for the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute, you also must set the  voltage level or current level in addition to  enabling the output
    the niDCPower_Initiate function. Refer to the Programming States topic in the NI DC Power Supplies and SMUs Help for  more information about NI-DCPower programming states.
    Default Value: The default value is VI_TRUE if you use the niDCPower_InitializeWithChannels function to open  the session. Otherwise the default value is VI_FALSE, including when you use a calibration session or the deprecated programming model.

    Note: If the session is in the Committed or Uncommitted states, enabling the output does not take effect until you call

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    output_enabled.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    output_enabled.Session instance, and calling set/get value on the result.:

        session['0,1'].output_enabled = var
        var = session['0,1'].output_enabled
    '''
    output_function = attributes.AttributeEnum(attributes.AttributeViInt32, enums.OutputFunction, 1150008)
    '''
    Configures the function to generate on the specified channel(s).
    When NIDCPOWER_VAL_DC_VOLTAGE is selected, the device generates the desired voltage level on the output as long as the  output current is below the current limit. You can use the following attributes to configure the channel when  NIDCPOWER_VAL_DC_VOLTAGE is selected:
    NIDCPOWER_ATTR_VOLTAGE_LEVEL
    NIDCPOWER_ATTR_CURRENT_LIMIT
    NIDCPOWER_ATTR_VOLTAGE_LEVEL_RANGE
    NIDCPOWER_ATTR_CURRENT_LIMIT_RANGE
    When NIDCPOWER_VAL_DC_CURRENT is selected, the device generates the desired current level on the output as long as the  output voltage is below the voltage limit. You can use the following attributes to configure the channel when  NIDCPOWER_VAL_DC_CURRENT is selected:
    NIDCPOWER_ATTR_CURRENT_LEVEL
    NIDCPOWER_ATTR_VOLTAGE_LIMIT
    NIDCPOWER_ATTR_CURRENT_LEVEL_RANGE
    NIDCPOWER_ATTR_VOLTAGE_LIMIT_RANGE
    Default Value: NIDCPOWER_VAL_DC_VOLTAGE

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    output_function.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    output_function.Session instance, and calling set/get value on the result.:

        session['0,1'].output_function = var
        var = session['0,1'].output_function
    '''
    output_resistance = attributes.AttributeViReal64(1150061)
    '''
    Specifies the output resistance that the device attempts to generate for the specified channel(s). This attribute is  available only when you set the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute on a support device. Refer to a supported device's topic about output resistance for more information about selecting an output resistance.
    about supported devices.
    Default Value: 0.0

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device topic for information

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    output_resistance.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    output_resistance.Session instance, and calling set/get value on the result.:

        session['0,1'].output_resistance = var
        var = session['0,1'].output_resistance
    '''
    overranging_enabled = attributes.AttributeViBoolean(1150007)
    '''
    Specifies whether NI-DCPower allows setting the voltage level, current level, voltage limit and current limit outside the  device specification limits. VI_TRUE means that overranging is enabled.
    Refer to the Ranges topic in the NI DC Power Supplies and SMUs Help for more information about overranging.
    Default Value: VI_FALSE
    '''
    ovp_enabled = attributes.AttributeViBoolean(1250002)
    '''
    Enables (VI_TRUE) or disables (VI_FALSE) overvoltage protection (OVP).
    Refer to the Output Overvoltage Protection topic in the NI DC Power Supplies and SMUs Help for more information about  overvoltage protection.
    for information about supported devices.
    Default Value: VI_FALSE

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device topic
    '''
    ovp_limit = attributes.AttributeViReal64(1250003)
    '''
    Determines the voltage limit, in volts, beyond which overvoltage protection (OVP) engages.
    for information about supported devices.
    Valid Values: 2 V to 210 V
    Default Value: 210 V

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device topic
    '''
    power_line_frequency = attributes.AttributeEnum(attributes.AttributeViReal64, enums.PowerLineFrequency, 1150020)
    '''
    Specifies the power line frequency for specified channel(s). NI-DCPower uses this value to select a timebase for setting the  NIDCPOWER_ATTR_APERTURE_TIME attribute in power line cycles (PLCs).
    in the NI DC Power Supplies and SMUs Help for information about supported devices.
    Default Value: NIDCPOWER_VAL_60_HERTZ

    Note: This attribute is not supported by all devices. Refer to the Supported Attributes by Device topic

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    power_line_frequency.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    power_line_frequency.Session instance, and calling set/get value on the result.:

        session['0,1'].power_line_frequency = var
        var = session['0,1'].power_line_frequency
    '''
    power_source = attributes.AttributeEnum(attributes.AttributeViInt32, enums.PowerSource, 1150000)
    '''
    Specifies the power source to use. NI-DCPower switches the power source used by the  device to the specified value.
    Default Value: NIDCPOWER_VAL_AUTOMATIC
    is set to NIDCPOWER_VAL_AUTOMATIC. However, if the session is in the Committed or Uncommitted state  when you set this attribute, the power source selection only occurs after you call the  niDCPower_Initiate function.

    Note: Automatic selection is not persistent and occurs only at the time this attribute
    '''
    power_source_in_use = attributes.AttributeEnum(attributes.AttributeViInt32, enums.PowerSourceInUse, 1150001)
    '''
    Indicates whether the device is using the internal or auxiliary power source to generate power.
    '''
    pulse_bias_current_level = attributes.AttributeViReal64(1150088)
    '''
    Specifies the pulse bias current level, in amps, that the device attempts to generate on the specified channel(s) during the off phase of a pulse.
    This attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_PULSE_CURRENT.
    Valid Values: The valid values for this attribute are defined by the values you specify for the NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL_RANGE attribute.

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device for information about supported devices.

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    pulse_bias_current_level.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    pulse_bias_current_level.Session instance, and calling set/get value on the result.:

        session['0,1'].pulse_bias_current_level = var
        var = session['0,1'].pulse_bias_current_level
    '''
    pulse_bias_current_limit = attributes.AttributeViReal64(1150083)
    '''
    Specifies the pulse bias current limit, in amps, that the output cannot exceed when generating the desired pulse bias voltage on the specified channel(s) during the off phase of a pulse.
    This attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_PULSE_VOLTAGE.
    Valid Values: The valid values for this attribute are defined by the values you specify for the NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_RANGE property.

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device for information about supported devices.

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    pulse_bias_current_limit.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    pulse_bias_current_limit.Session instance, and calling set/get value on the result.:

        session['0,1'].pulse_bias_current_limit = var
        var = session['0,1'].pulse_bias_current_limit
    '''
    pulse_bias_delay = attributes.AttributeViReal64(1150092)
    '''
    Determines when, in seconds, the device generates the Pulse Complete event after generating the off level of a pulse.
    Valid Values: 0 to 167 seconds
    Default Value: 16.67 milliseconds

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device for information about supported devices.

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    pulse_bias_delay.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    pulse_bias_delay.Session instance, and calling set/get value on the result.:

        session['0,1'].pulse_bias_delay = var
        var = session['0,1'].pulse_bias_delay
    '''
    pulse_bias_voltage_level = attributes.AttributeViReal64(1150082)
    '''
    Specifies the pulse bias voltage level, in volts, that the device attempts to generate on the specified channel(s) during the off phase of a pulse.
    This attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_PULSE_VOLTAGE.
    Valid Values: The valid values for this attribute are defined by the values you specify for the NIDCPOWER_ATTR_PULSE_VOLTAGE_LEVEL_RANGE attribute.

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device for information about supported devices.

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    pulse_bias_voltage_level.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    pulse_bias_voltage_level.Session instance, and calling set/get value on the result.:

        session['0,1'].pulse_bias_voltage_level = var
        var = session['0,1'].pulse_bias_voltage_level
    '''
    pulse_bias_voltage_limit = attributes.AttributeViReal64(1150089)
    '''
    Specifies the pulse voltage limit, in volts, that the output cannot exceed when generating the desired current on the specified channel(s) during the off phase of a pulse.
    This attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_PULSE_CURRENT.
    Valid Values: The valid values for this attribute are defined by the values you specify for the NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_RANGE attribute.

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device for information about supported devices.

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    pulse_bias_voltage_limit.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    pulse_bias_voltage_limit.Session instance, and calling set/get value on the result.:

        session['0,1'].pulse_bias_voltage_limit = var
        var = session['0,1'].pulse_bias_voltage_limit
    '''
    pulse_complete_event_output_terminal = attributes.AttributeViString(1150099)
    '''
    Specifies the output terminal for exporting the Pulse Complete event.
    Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.
    Default Value:The default value for PXI Express devices is 250 ns.

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device for information about supported devices.
    '''
    pulse_complete_event_pulse_polarity = attributes.AttributeEnum(attributes.AttributeViInt32, enums.Polarity, 1150100)
    '''
    Specifies the behavior of the Pulse Complete event.
    Default Value: NIDCPOWER_VAL_ACTIVE_HIGH

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device for information about supported devices.
    '''
    pulse_complete_event_pulse_width = attributes.AttributeViReal64(1150101)
    '''
    Specifies the width of the Pulse Complete event, in seconds.
    The minimum event pulse width value for PXI Express devices is 250 ns.
    The maximum event pulse width value for PXI Express devices is 1.6 microseconds.
    Default Value: The default value for PXI Express devices is 250 ns.

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device for information about supported devices.
    '''
    pulse_current_level = attributes.AttributeViReal64(1150086)
    '''
    Specifies the pulse current level, in amps, that the device attempts to generate on the specified channel(s) during the on phase of a pulse.
    This attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_PULSE_CURRENT.
    Valid Values: The valid values for this attribute are defined by the values you specify for the NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL_RANGE attribute.

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device for information about supported devices.

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    pulse_current_level.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    pulse_current_level.Session instance, and calling set/get value on the result.:

        session['0,1'].pulse_current_level = var
        var = session['0,1'].pulse_current_level
    '''
    pulse_current_level_range = attributes.AttributeViReal64(1150090)
    '''
    Specifies the pulse current level range, in amps, for the specified channel(s).
    The range defines the valid values to which you can set the pulse current level and pulse bias current level.
    This attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_PULSE_CURRENT.
    For valid ranges, refer to the ranges topic for your device in the NI DC Power Supplies and SMUs Help.

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device for information about supported devices.

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    pulse_current_level_range.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    pulse_current_level_range.Session instance, and calling set/get value on the result.:

        session['0,1'].pulse_current_level_range = var
        var = session['0,1'].pulse_current_level_range
    '''
    pulse_current_limit = attributes.AttributeViReal64(1150081)
    '''
    Specifies the pulse current limit, in amps, that the output cannot exceed when generating the desired pulse voltage on the specified channel(s) during the on phase of a pulse.
    This attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_PULSE_VOLTAGE.
    Valid Values: The valid values for this attribute are defined by the values you specify for the NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_RANGE attribute.

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device for information about supported devices.

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    pulse_current_limit.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    pulse_current_limit.Session instance, and calling set/get value on the result.:

        session['0,1'].pulse_current_limit = var
        var = session['0,1'].pulse_current_limit
    '''
    pulse_current_limit_range = attributes.AttributeViReal64(1150085)
    '''
    Specifies the pulse current limit range, in amps, for the specified channel(s).
    The range defines the valid values to which you can set the pulse current limit and pulse bias current limit.
    This attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_PULSE_VOLTAGE.
    For valid ranges, refer to the ranges topic for your device in the NI DC Power Supplies and SMUs Help.

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device for information about supported devices.

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    pulse_current_limit_range.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    pulse_current_limit_range.Session instance, and calling set/get value on the result.:

        session['0,1'].pulse_current_limit_range = var
        var = session['0,1'].pulse_current_limit_range
    '''
    pulse_off_time = attributes.AttributeViReal64(1150094)
    '''
    Determines the length, in seconds, of the off phase of a pulse.
    Valid Values: 10 microseconds to 167 seconds
    Default Value: 34 milliseconds

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device for information about supported devices.

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    pulse_off_time.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    pulse_off_time.Session instance, and calling set/get value on the result.:

        session['0,1'].pulse_off_time = var
        var = session['0,1'].pulse_off_time
    '''
    pulse_on_time = attributes.AttributeViReal64(1150093)
    '''
    Determines the length, in seconds, of the on phase of a pulse.
    Valid Values: 10 microseconds to 167 seconds
    Default Value: 34 milliseconds

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device for information about supported devices.

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    pulse_on_time.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    pulse_on_time.Session instance, and calling set/get value on the result.:

        session['0,1'].pulse_on_time = var
        var = session['0,1'].pulse_on_time
    '''
    pulse_trigger_type = attributes.AttributeEnum(attributes.AttributeViInt32, enums.TriggerType, 1150095)
    '''
    Specifies the behavior of the Pulse trigger.
    Default Value: NIDCPOWER_VAL_NONE

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device for information about supported devices.
    '''
    pulse_voltage_level = attributes.AttributeViReal64(1150080)
    '''
    Specifies the pulse current limit, in amps, that the output cannot exceed when generating the desired pulse voltage on the specified channel(s) during the on phase of a pulse.
    This attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_PULSE_VOLTAGE.
    Valid Values: The valid values for this attribute are defined by the values you specify for the NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_RANGE attribute.

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device for information about supported devices.

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    pulse_voltage_level.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    pulse_voltage_level.Session instance, and calling set/get value on the result.:

        session['0,1'].pulse_voltage_level = var
        var = session['0,1'].pulse_voltage_level
    '''
    pulse_voltage_level_range = attributes.AttributeViReal64(1150084)
    '''
    Specifies the pulse voltage level range, in volts, for the specified channel(s).
    The range defines the valid values at which you can set the pulse voltage level and pulse bias voltage level.
    This attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_PULSE_VOLTAGE.
    For valid ranges, refer to the ranges topic for your device in the NI DC Power Supplies and SMUs Help.

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device for information about supported devices.

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    pulse_voltage_level_range.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    pulse_voltage_level_range.Session instance, and calling set/get value on the result.:

        session['0,1'].pulse_voltage_level_range = var
        var = session['0,1'].pulse_voltage_level_range
    '''
    pulse_voltage_limit = attributes.AttributeViReal64(1150087)
    '''
    Specifies the pulse voltage limit, in volts, that the output cannot exceed when generating the desired pulse current on the specified channel(s) during the on phase of a pulse.
    This attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_PULSE_CURRENT.
    Valid Values: The valid values for this attribute are defined by the values you specify for the NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_RANGE attribute.

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device for information about supported devices.

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    pulse_voltage_limit.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    pulse_voltage_limit.Session instance, and calling set/get value on the result.:

        session['0,1'].pulse_voltage_limit = var
        var = session['0,1'].pulse_voltage_limit
    '''
    pulse_voltage_limit_range = attributes.AttributeViReal64(1150091)
    '''
    Specifies the pulse voltage limit range, in volts, for the specified channel(s).
    The range defines the valid values to which you can set the pulse voltage limit and pulse bias voltage limit.
    This attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_PULSE_CURRENT.
    For valid ranges, refer to the ranges topic for your device in the NI DC Power Supplies and SMUs Help.

    Note: The channel must be enabled for the specified current limit to take effect. Refer to the NIDCPOWER_ATTR_OUTPUT_ENABLED attribute for more information about enabling the output channel.

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    pulse_voltage_limit_range.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    pulse_voltage_limit_range.Session instance, and calling set/get value on the result.:

        session['0,1'].pulse_voltage_limit_range = var
        var = session['0,1'].pulse_voltage_limit_range
    '''
    query_instrument_status = attributes.AttributeViBoolean(1050003)
    '''
    Specifies whether NI-DCPower queries the device status after each operation.
    Querying the device status is useful for debugging. After you validate your program, you can set this  attribute to VI_FALSE to disable status checking and maximize performance.
    NI-DCPower ignores status checking for particular attributes regardless of the setting of this attribute.
    Use the niDCPower_InitializeWithChannels function to override this value.
    Default Value: VI_TRUE
    '''
    range_check = attributes.AttributeViBoolean(1050002)
    '''
    Specifies whether to validate attribute values and function parameters.
    If this attribute is enabled, NI-DCPower validates the parameter values that you pass to NI-DCPower functions.  Range checking parameters is useful for debugging. After you validate your program, you can set this  attribute to VI_FALSE to disable range checking and maximize performance.
    Use the niDCPower_InitializeWithChannels function to override this value.
    Default Value: VI_TRUE
    '''
    ready_for_pulse_trigger_event_output_terminal = attributes.AttributeViString(1150102)
    '''
    Specifies the output terminal for exporting the Ready For Pulse Trigger event.
    Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device for information about supported devices.
    '''
    ready_for_pulse_trigger_event_pulse_polarity = attributes.AttributeEnum(attributes.AttributeViInt32, enums.Polarity, 1150103)
    '''
    Specifies the behavior of the Ready For Pulse Trigger event.
    Default Value: NIDCPOWER_VAL_ACTIVE_HIGH

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device for information about supported devices.
    '''
    ready_for_pulse_trigger_event_pulse_width = attributes.AttributeViReal64(1150104)
    '''
    Specifies the width of the Ready For Pulse Trigger event, in seconds.
    The minimum event pulse width value for PXI Express devices is 250 ns.
    The maximum event pulse width value for all devices is 1.6 microseconds.
    Default Value: The default value for PXI Express devices is 250 ns

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device for information about supported devices.
    '''
    record_coercions = attributes.AttributeViBoolean(1050006)
    '''
    Specifies whether the IVI engine records the value coercions it makes for ViInt32 and ViReal64 attributes.  Call the niDCPower_GetNextCoercionRecord function to read and delete the earliest coercion record from the list.
    Default Value: The default value is VI_FALSE. Use the niDCPower_InitializeWithChannels function to override this value.
    '''
    reset_average_before_measurement = attributes.AttributeViBoolean(1150006)
    '''
    Specifies whether the measurement returned from any measurement call starts with a new measurement call (VI_TRUE) or  returns a measurement that has already begun or completed(VI_FALSE).
    for information about supported devices.
    When you set the NIDCPOWER_ATTR_SAMPLES_TO_AVERAGE attribute in the Running state, the output channel measurements might  move out of synchronization. While NI-DCPower automatically synchronizes measurements upon the initialization of a  session, you can force a synchronization in the running state before you run the niDCPower_MeasureMultiple function. To  force a synchronization in the running state, set this attribute to VI_TRUE, and then run the niDCPower_MeasureMultiple  function, specifying all channels in the channel name parameter. You can set the  NIDCPOWER_ATTR_RESET_AVERAGE_BEFORE_MEASUREMENT attribute to VI_FALSE after the niDCPower_MeasureMultiple function  completes.
    Default Value: VI_TRUE

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device topic

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    reset_average_before_measurement.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    reset_average_before_measurement.Session instance, and calling set/get value on the result.:

        session['0,1'].reset_average_before_measurement = var
        var = session['0,1'].reset_average_before_measurement
    '''
    samples_to_average = attributes.AttributeViInt32(1150003)
    '''
    Specifies the number of samples to average when you take a measurement.
    Increasing the number of samples to average decreases measurement noise but increases the time required to take  a measurement. Refer to the NI PXI-4110, NI PXI-4130, NI PXI-4132, or NI PXIe-4154 Averaging topic for  optional attribute settings to improve immunity to certain noise types, or refer to the NI PXIe-4140/4141  DC Noise Rejection, NI PXIe-4142/4143 DC Noise Rejection, or NI PXIe-4144/4145 DC Noise Rejection topic for  information about improving noise immunity for those devices.
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
    This property can use repeated capabilities (usually channels). If set or get directly on the
    samples_to_average.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    samples_to_average.Session instance, and calling set/get value on the result.:

        session['0,1'].samples_to_average = var
        var = session['0,1'].samples_to_average
    '''
    self_calibration_persistence = attributes.AttributeEnum(attributes.AttributeViInt32, enums.SelfCalibrationPersistence, 1150073)
    '''
    Specifies whether the values calculated during self-calibration should be written to hardware to be used until the  next self-calibration or only used until the niDCPower_ResetDevice function is called or the machine  is powered down.
    This attribute affects the behavior of the niDCPower_CalSelfCalibrate function. When set to  NIDCPOWER_VAL_KEEP_IN_MEMORY, the values calculated by the niDCPower_CalSelfCalibrate function are used in  the existing session, as well as in all further sessions until you call the niDCPower_ResetDevice function  or restart the machine. When you set this property to NIDCPOWER_VAL_WRITE_TO_EEPROM, the values calculated  by the niDCPower_CalSelfCalibrate function are written to hardware and used in the existing session and  in all subsequent sessions until another call to the niDCPower_CalSelfCalibrate function is made.
    about supported devices.
    Default Value: NIDCPOWER_VAL_KEEP_IN_MEMORY

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device for information
    '''
    sense = attributes.AttributeEnum(attributes.AttributeViInt32, enums.Sense, 1150013)
    '''
    Selects either local or remote sensing of the output voltage for the specified channel(s).
    Refer to the Local and Remote Sense topic in the NI DC Power Supplies and SMUs Help for more  information about sensing voltage on supported channels and about devices that support local and/or remote sensing.
    Default Value: The default value is NIDCPOWER_VAL_LOCAL if the device supports local sense.  Otherwise, the default and only supported value is NIDCPOWER_VAL_REMOTE.

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    sense.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    sense.Session instance, and calling set/get value on the result.:

        session['0,1'].sense = var
        var = session['0,1'].sense
    '''
    sequence_advance_trigger_type = attributes.AttributeEnum(attributes.AttributeViInt32, enums.TriggerType, 1150026)
    '''
    Specifies the behavior of the Sequence Advance trigger.
    for information about supported devices.
    Default Value: NIDCPOWER_VAL_NONE

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device topic
    '''
    sequence_engine_done_event_output_terminal = attributes.AttributeViString(1150050)
    '''
    Specifies the output terminal for exporting the Sequence Engine Done Complete event.
    for information about supported devices.
    Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal  is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or  with the shortened terminal name, PXI_Trig0.

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device topic
    '''
    sequence_engine_done_event_pulse_polarity = attributes.AttributeEnum(attributes.AttributeViInt32, enums.Polarity, 1150048)
    '''
    Specifies the behavior of the Sequence Engine Done event.
    for information about supported devices.
    Default Value: NIDCPOWER_VAL_ACTIVE_HIGH

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device topic
    '''
    sequence_engine_done_event_pulse_width = attributes.AttributeViReal64(1150049)
    '''
    Specifies the width of the Sequence Engine Done event, in seconds.
    The minimum event pulse width value for PXI devices is 150 ns, and the minimum event pulse width value  for PXI Express devices is 250 ns.
    The maximum event pulse width value for all devices is 1.6 microseconds.
    for information about supported devices.
    Valid Values: 1.5e-7 to 1.6e-6 seconds
    Default Value: The default value for PXI devices is 150 ns. The default value for PXI Express devices is 250 ns.

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device topic
    '''
    sequence_iteration_complete_event_output_terminal = attributes.AttributeViString(1150040)
    '''
    Specifies the output terminal for exporting the Sequence Iteration Complete event.
    for information about supported devices.
    Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal  is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or  with the shortened terminal name, PXI_Trig0.

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device topic
    '''
    sequence_iteration_complete_event_pulse_polarity = attributes.AttributeEnum(attributes.AttributeViInt32, enums.Polarity, 1150038)
    '''
    Specifies the behavior of the Sequence Iteration Complete event.
    for information about supported devices.
    Default Value: NIDCPOWER_VAL_ACTIVE_HIGH

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device topic
    '''
    sequence_iteration_complete_event_pulse_width = attributes.AttributeViReal64(1150039)
    '''
    Specifies the width of the Sequence Iteration Complete event, in seconds.
    The minimum event pulse width value for PXI devices is 150 ns, and the minimum event pulse width  value for PXI Express devices is 250 ns.
    The maximum event pulse width value for all devices is 1.6 microseconds.
    the NI DC Power Supplies and SMUs Help for information about supported devices.
    Valid Values: 1.5e-7 to 1.6e-6 seconds
    Default Value: The default value for PXI devices is 150 ns. The default value for PXI Express devices is 250 ns.

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device topic in
    '''
    sequence_loop_count = attributes.AttributeViInt32(1150025)
    '''
    Specifies the number of times a sequence is run after initiation.
    Refer to the Sequence Source Mode topic in the NI DC Power Supplies and SMUs Help for more information about the sequence  loop count.
    for information about supported devices. When the NIDCPOWER_ATTR_SEQUENCE_LOOP_COUNT_IS_FINITE attribute  is set to VI_FALSE, the NIDCPOWER_ATTR_SEQUENCE_LOOP_COUNT attribute is ignored.
    Valid Range: 1 to 134217727
    Default Value: 1

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device topic
    '''
    sequence_loop_count_is_finite = attributes.AttributeViBoolean(1150078)
    '''
    Specifies whether a sequence should repeat indefinitely.
    Refer to the Sequence Source Mode topic in the NI DC Power Supplies and SMUs Help for more information about  infinite sequencing.
    NIDCPOWER_ATTR_SEQUENCE_LOOP_COUNT_IS_FINITE attribute is set to VI_FALSE,  the NIDCPOWER_ATTR_SEQUENCE_LOOP_COUNT attribute is ignored.
    Default Value: VI_TRUE

    Note: This attribute is not supported by all devices. When the
    '''
    simulate = attributes.AttributeViBoolean(1050005)
    '''
    Specifies whether to simulate NI-DCPower I/O operations. VI_TRUE specifies that operation is simulated.
    Default Value: VI_FALSE
    '''
    source_complete_event_output_terminal = attributes.AttributeViString(1150043)
    '''
    Specifies the output terminal for exporting the Source Complete event.
    for information about supported devices.
    Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you  can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal  name, PXI_Trig0.

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device topic
    '''
    source_complete_event_pulse_polarity = attributes.AttributeEnum(attributes.AttributeViInt32, enums.Polarity, 1150041)
    '''
    Specifies the behavior of the Source Complete event.
    for information about supported devices.
    Default Value: NIDCPOWER_VAL_ACTIVE_HIGH

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device topic
    '''
    source_complete_event_pulse_width = attributes.AttributeViReal64(1150042)
    '''
    Specifies the width of the Source Complete event, in seconds.
    for information about supported devices.
    The minimum event pulse width value for PXI devices is 150 ns, and the minimum event pulse width value  for PXI Express devices is 250 ns.
    The maximum event pulse width value for all devices is 1.6 microseconds
    Valid Values: 1.5e-7 to 1.6e-6 seconds
    Default Value: The default value for PXI devices is 150 ns. The default value for PXI Express devices is 250 ns.

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device topic
    '''
    source_delay = attributes.AttributeViReal64(1150051)
    '''
    Determines when, in seconds, the device generates the Source Complete event, potentially starting a measurement if the  NIDCPOWER_ATTR_MEASURE_WHEN attribute is set to NIDCPOWER_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE.
    Refer to the Single Point Source Mode and Sequence Source Mode topics for more information.
    Valid Values: 0 to 167 seconds
    Default Value: 0.01667 seconds

    Note:
    Refer to Supported Attributes by Device for information about supported devices.

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    source_delay.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    source_delay.Session instance, and calling set/get value on the result.:

        session['0,1'].source_delay = var
        var = session['0,1'].source_delay
    '''
    source_mode = attributes.AttributeEnum(attributes.AttributeViInt32, enums.SourceMode, 1150054)
    '''
    Specifies whether to run a single output point or a sequence. Refer to the Single Point Source Mode and Sequence Source  Mode topics in the NI DC Power Supplies and SMUs Help for more information about source modes.
    Default value: NIDCPOWER_VAL_SINGLE_POINT
    '''
    source_trigger_type = attributes.AttributeEnum(attributes.AttributeViInt32, enums.TriggerType, 1150030)
    '''
    Specifies the behavior of the Source trigger.
    for information about supported devices.
    Default Value: NIDCPOWER_VAL_NONE

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device topic
    '''
    specific_driver_class_spec_major_version = attributes.AttributeViInt32(1050515)
    '''
    Contains the major version number of the class specification with which NI-DCPower is compliant.
    '''
    specific_driver_class_spec_minor_version = attributes.AttributeViInt32(1050516)
    '''
    Contains the minor version number of the class specification with which NI-DCPower is compliant.
    '''
    specific_driver_description = attributes.AttributeViString(1050514)
    '''
    Contains a brief description of the specific driver.
    '''
    specific_driver_prefix = attributes.AttributeViString(1050302)
    '''
    Contains the prefix for NI-DCPower. The name of each user-callable  function in NI-DCPower begins with this prefix.
    '''
    specific_driver_revision = attributes.AttributeViString(1050551)
    '''
    Contains additional version information about NI-DCPower.
    '''
    specific_driver_vendor = attributes.AttributeViString(1050513)
    '''
    Contains the name of the vendor that supplies NI-DCPower.
    '''
    start_trigger_type = attributes.AttributeEnum(attributes.AttributeViInt32, enums.TriggerType, 1150021)
    '''
    Specifies the behavior of the Start trigger.
    for information about supported devices.
    Default Value: NIDCPOWER_VAL_NONE

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device topic
    '''
    supported_instrument_models = attributes.AttributeViString(1050327)
    '''
    Contains a comma-separated (,) list of supported NI-DCPower device models.
    '''
    transient_response = attributes.AttributeEnum(attributes.AttributeViInt32, enums.TransientResponse, 1150062)
    '''
    Specifies the transient response. Refer to the Transient Response topic in the NI DC Power Supplies and SMUs Help  for more information about transient response.
    for information about supported devices.
    Default Value: NIDCPOWER_VAL_NORMAL

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device topic

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    transient_response.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    transient_response.Session instance, and calling set/get value on the result.:

        session['0,1'].transient_response = var
        var = session['0,1'].transient_response
    '''
    voltage_compensation_frequency = attributes.AttributeViReal64(1150068)
    '''
    The frequency at which a pole-zero pair is added to the system when the channel is in  Constant Voltage mode.
    for information about supported devices.
    Default value: Determined by the value of the NIDCPOWER_VAL_NORMAL setting of  the NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute.

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device topic

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    voltage_compensation_frequency.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    voltage_compensation_frequency.Session instance, and calling set/get value on the result.:

        session['0,1'].voltage_compensation_frequency = var
        var = session['0,1'].voltage_compensation_frequency
    '''
    voltage_gain_bandwidth = attributes.AttributeViReal64(1150067)
    '''
    The frequency at which the unloaded loop gain extrapolates to 0 dB in the absence of additional poles and zeroes. This attribute takes effect when the channel is in Constant Voltage mode.
    for information about supported devices.
    Default Value: Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the  NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute.

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device topic

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    voltage_gain_bandwidth.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    voltage_gain_bandwidth.Session instance, and calling set/get value on the result.:

        session['0,1'].voltage_gain_bandwidth = var
        var = session['0,1'].voltage_gain_bandwidth
    '''
    voltage_level = attributes.AttributeViReal64(1250001)
    '''
    Specifies the voltage level, in volts, that the device attempts to generate on the specified channel(s).
    This attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_DC_VOLTAGE.
    NIDCPOWER_ATTR_OUTPUT_ENABLED attribute for more information about enabling the output channel.
    Valid Values: The valid values for this attribute are defined by the values you specify for the  NIDCPOWER_ATTR_VOLTAGE_LEVEL_RANGE attribute.

    Note: The channel must be enabled for the specified voltage level to take effect. Refer to the

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    voltage_level.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    voltage_level.Session instance, and calling set/get value on the result.:

        session['0,1'].voltage_level = var
        var = session['0,1'].voltage_level
    '''
    voltage_level_autorange = attributes.AttributeEnum(attributes.AttributeViInt32, enums.VoltageLevelAutorange, 1150015)
    '''
    Specifies whether NI-DCPower automatically selects the voltage level range based on the desired voltage level  for the specified channel(s).
    If you set this attribute to NIDCPOWER_VAL_ON, NI-DCPower ignores any changes you make to the  NIDCPOWER_ATTR_VOLTAGE_LEVEL_RANGE attribute. If you change the NIDCPOWER_ATTR_VOLTAGE_LEVEL_AUTORANGE attribute from  NIDCPOWER_VAL_ON to NIDCPOWER_VAL_OFF, NI-DCPower retains the last value the NIDCPOWER_ATTR_VOLTAGE_LEVEL_RANGE  attribute was set to (or the default value if the attribute was never set) and uses that value as  the voltage level range.
    Query the NIDCPOWER_ATTR_VOLTAGE_LEVEL_RANGE attribute by using the niDCPower_GetAttributeViInt32 function for  information about which range NI-DCPower automatically selects.
    The NIDCPOWER_ATTR_VOLTAGE_LEVEL_AUTORANGE attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute  is set to NIDCPOWER_VAL_DC_VOLTAGE.
    Default Value: NIDCPOWER_VAL_OFF

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    voltage_level_autorange.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    voltage_level_autorange.Session instance, and calling set/get value on the result.:

        session['0,1'].voltage_level_autorange = var
        var = session['0,1'].voltage_level_autorange
    '''
    voltage_level_range = attributes.AttributeViReal64(1150005)
    '''
    Specifies the voltage level range, in volts, for the specified channel(s).
    The range defines the valid values to which the voltage level can be set. Use the NIDCPOWER_ATTR_VOLTAGE_LEVEL_AUTORANGE  attribute to enable automatic selection of the voltage level range.
    The NIDCPOWER_ATTR_VOLTAGE_LEVEL_RANGE attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is  set to NIDCPOWER_VAL_DC_VOLTAGE.
    NIDCPOWER_ATTR_OUTPUT_ENABLED attribute for more information about enabling the output channel.
    For valid ranges, refer to the Ranges topic for your device in the NI DC Power Supplies and SMUs Help.

    Note: The channel must be enabled for the specified voltage level range to take effect. Refer to the

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    voltage_level_range.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    voltage_level_range.Session instance, and calling set/get value on the result.:

        session['0,1'].voltage_level_range = var
        var = session['0,1'].voltage_level_range
    '''
    voltage_limit = attributes.AttributeViReal64(1150010)
    '''
    Specifies the voltage limit, in volts, that the output cannot exceed when generating the desired current level  on the specified channels.
    This attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_DC_CURRENT.
    NIDCPOWER_ATTR_OUTPUT_ENABLED attribute for more information about enabling the output channel.
    Valid Values: The valid values for this attribute are defined by the values to which the  NIDCPOWER_ATTR_VOLTAGE_LIMIT_RANGE attribute is set.

    Note: The channel must be enabled for the specified current level to take effect. Refer to the

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    voltage_limit.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    voltage_limit.Session instance, and calling set/get value on the result.:

        session['0,1'].voltage_limit = var
        var = session['0,1'].voltage_limit
    '''
    voltage_limit_autorange = attributes.AttributeEnum(attributes.AttributeViInt32, enums.VoltageLimitAutorange, 1150018)
    '''
    Specifies whether NI-DCPower automatically selects the voltage limit range based on the desired voltage limit for  the specified channel(s).
    If this attribute is set to NIDCPOWER_VAL_ON, NI-DCPower ignores any changes you make to the  NIDCPOWER_ATTR_VOLTAGE_LIMIT_RANGE attribute. If you change the NIDCPOWER_ATTR_VOLTAGE_LIMIT_AUTORANGE attribute from  NIDCPOWER_VAL_ON to NIDCPOWER_VAL_OFF, NI-DCPower retains the last value the NIDCPOWER_ATTR_VOLTAGE_LIMIT_RANGE  attribute was set to (or the default value if the attribute was never set) and uses that value as the voltage limit  range.
    Query the NIDCPOWER_ATTR_VOLTAGE_LIMIT_RANGE attribute by using the niDCPower_GetAttributeViInt32 function to find out  which range NI-DCPower automatically selects.
    The NIDCPOWER_ATTR_VOLTAGE_LIMIT_AUTORANGE attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute  is set to NIDCPOWER_VAL_DC_CURRENT.
    Default Value: NIDCPOWER_VAL_OFF

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    voltage_limit_autorange.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    voltage_limit_autorange.Session instance, and calling set/get value on the result.:

        session['0,1'].voltage_limit_autorange = var
        var = session['0,1'].voltage_limit_autorange
    '''
    voltage_limit_range = attributes.AttributeViReal64(1150012)
    '''
    Specifies the voltage limit range, in volts, for the specified channel(s).
    The range defines the valid values to which the voltage limit can be set. Use the NIDCPOWER_ATTR_VOLTAGE_LIMIT_AUTORANGE  attribute to enable automatic selection of the voltage limit range.
    The NIDCPOWER_ATTR_VOLTAGE_LIMIT_RANGE attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is  set to NIDCPOWER_VAL_DC_CURRENT.
    NIDCPOWER_ATTR_OUTPUT_ENABLED attribute for more information about enabling the output channel.
    For valid ranges, refer to the Ranges topic for your device in the NI DC Power Supplies and SMUs Help.

    Note: The channel must be enabled for the specified voltage limit range to take effect. Refer to the

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    voltage_limit_range.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    voltage_limit_range.Session instance, and calling set/get value on the result.:

        session['0,1'].voltage_limit_range = var
        var = session['0,1'].voltage_limit_range
    '''
    voltage_pole_zero_ratio = attributes.AttributeViReal64(1150069)
    '''
    The ratio of the pole frequency to the zero frequency when the channel is in  Constant Voltage mode.
    for information about supported devices.
    Default value: Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the  NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute.

    Note: This attribute is not supported by all devices. Refer to Supported Attributes by Device topic

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    voltage_pole_zero_ratio.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    voltage_pole_zero_ratio.Session instance, and calling set/get value on the result.:

        session['0,1'].voltage_pole_zero_ratio = var
        var = session['0,1'].voltage_pole_zero_ratio
    '''

    def __init__(self, repeated_capability):
        self._library = library_singleton.get()
        self._repeated_capability = repeated_capability
        self._encoding = 'windows-1251'

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

    def configure_aperture_time(self, aperture_time, units=enums.ApertureTimeUnits.SECONDS):
        '''configure_aperture_time

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
        This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session instance, and calling this method on the result.:

            session['0,1'].configure_aperture_time(aperture_time, units=nidcpower.ApertureTimeUnits.SECONDS)

        Args:
            aperture_time (float): Specifies the aperture time. Refer to the *Aperture Time* topic for your
                device in the *NI DC Power Supplies and SMUs Help* for more information.
            units (enums.ApertureTimeUnits): Specifies the units for **apertureTime**.
                **Defined Values**:

                +----------------------------------------+------------------------------+
                | NIDCPOWER_VAL_SECONDS (1028)           | Specifies seconds.           |
                +----------------------------------------+------------------------------+
                | NIDCPOWER_VAL_POWER_LINE_CYCLES (1029) | Specifies Power Line Cycles. |
                +----------------------------------------+------------------------------+
        '''
        if type(units) is not enums.ApertureTimeUnits:
            raise TypeError('Parameter mode must be of type ' + str(enums.ApertureTimeUnits))
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        aperture_time_ctype = visatype.ViReal64(aperture_time)  # case 9
        units_ctype = visatype.ViInt32(units.value)  # case 10
        error_code = self._library.niDCPower_ConfigureApertureTime(vi_ctype, channel_name_ctype, aperture_time_ctype, units_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def fetch_multiple(self, count, timeout=1.0):
        '''fetch_multiple

        Returns an array of voltage measurements, an array of current
        measurements, and an array of compliance measurements that were
        previously taken and are stored in the NI-DCPower buffer. This function
        should not be used when the MEASURE_WHEN attribute is
        set to NIDCPOWER_VAL_ON_DEMAND. You must first call
        _initiate before calling this function.

        Refer to the `Acquiring
        Measurements <REPLACE_DRIVER_SPECIFIC_URL_1(acquiringmeasurements)>`__
        and `Compliance <REPLACE_DRIVER_SPECIFIC_URL_1(compliance)>`__ topics in
        the *NI DC Power Supplies and SMUs Help* for more information about
        configuring this function.

        Note:
        This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session instance, and calling this method on the result.:

            session['0,1'].fetch_multiple(count, timeout=1.0)

        Args:
            timeout (float): Specifies the maximum time allowed for this function to complete, in
                seconds. If the function does not complete within this time interval,
                NI-DCPower returns an error.

                Note:
                When setting the timeout interval, ensure you take into account any
                triggers so that the timeout interval is long enough for your
                application.
            count (int): Specifies the number of measurements to fetch.

        Returns:
            voltage_measurements (list of float): Returns an array of voltage measurements. Ensure that sufficient space
                has been allocated for the returned array.
            current_measurements (list of float): Returns an array of current measurements. Ensure that sufficient space
                has been allocated for the returned array.
            in_compliance (list of bool): Returns an array of Boolean values indicating whether the output was in
                compliance at the time the measurement was taken. Ensure that sufficient
                space has been allocated for the returned array.
            actual_count (int): Indicates the number of measured values actually retrieved from the
                device.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        timeout_ctype = visatype.ViReal64(timeout)  # case 9
        count_ctype = visatype.ViInt32(count)  # case 8
        voltage_measurements_ctype = (visatype.ViReal64 * count)()  # case 13
        current_measurements_ctype = (visatype.ViReal64 * count)()  # case 13
        in_compliance_ctype = (visatype.ViBoolean * count)()  # case 13
        actual_count_ctype = visatype.ViInt32()  # case 14
        error_code = self._library.niDCPower_FetchMultiple(vi_ctype, channel_name_ctype, timeout_ctype, count_ctype, voltage_measurements_ctype, current_measurements_ctype, in_compliance_ctype, ctypes.pointer(actual_count_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(voltage_measurements_ctype[i]) for i in range(count_ctype.value)], [float(current_measurements_ctype[i]) for i in range(count_ctype.value)], [bool(in_compliance_ctype[i]) for i in range(count_ctype.value)], int(actual_count_ctype.value)

    def _get_attribute_vi_boolean(self, attribute_id):
        '''_get_attribute_vi_boolean

        | Queries the value of a ViBoolean attribute.
        | You can use this function to get the values of device-specific
          attributes and inherent IVI attributes.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session instance, and calling this method on the result.:

            session['0,1']._get_attribute_vi_boolean(attribute_id)

        Args:
            attribute_id (int): Specifies the ID of an attribute. From the function panel window, you
                can use this control as follows.

                -  In the function panel window, click on the control or press **Enter**
                   or the spacebar to display a dialog box containing hierarchical list
                   of the available attributes. Help text is shown for each attribute.
                   Select an attribute by double-clicking on it or by selecting it and
                   then pressing **Enter**.
                -  A ring control at the top of the dialog box allows you to see all IVI
                   attributes or only the attributes of type ViBoolean. If you choose to
                   see all IVI attributes, the data types appear to the right of the
                   attribute names in the list box. Attributes with data types other
                   than ViBoolean are dim. If you select an attribute data type that is
                   dim, LabWindows/CVI transfers you to the function panel for the
                   corresponding function that is consistent with the data type.
                -  If you want to enter a variable name, press **Ctrl**\ +\ **T** to
                   change this ring control to a manual input box. If the attribute in
                   this ring control has named constants as valid values, you can view
                   the constants by moving to the value control and pressing **Enter**.

        Returns:
            attribute_value (bool): Returns the current value of the attribute. Passes the address of a
                ViBoolean variable.
                If the attribute currently showing in the attribute ring control has
                constants as valid values, you can view a list of the constants by
                pressing **Enter** on this control. Select a value by double-clicking on
                it or by selecting it and then pressing **Enter**.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case 9
        attribute_value_ctype = visatype.ViBoolean()  # case 14
        error_code = self._library.niDCPower_GetAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_id_ctype, ctypes.pointer(attribute_value_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(attribute_value_ctype.value)

    def _get_attribute_vi_int32(self, attribute_id):
        '''_get_attribute_vi_int32

        | Queries the value of a ViInt32 attribute.
        | You can use this function to get the values of device-specific
          attributes and inherent IVI attributes.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session instance, and calling this method on the result.:

            session['0,1']._get_attribute_vi_int32(attribute_id)

        Args:
            attribute_id (int): Specifies the ID of an attribute. From the function panel window, you
                can use this control as follows.

                -  In the function panel window, click on the control or press **Enter**
                   or the spacebar to display a dialog box containing hierarchical list
                   of the available attributes. Help text is shown for each attribute.
                   Select an attribute by double-clicking on it or by selecting it and
                   then pressing **Enter**.
                -  A ring control at the top of the dialog box allows you to see all IVI
                   attributes or only the attributes of type ViInt32. If you choose to
                   see all IVI attributes, the data types appear to the right of the
                   attribute names in the list box. Attributes with data types other
                   than ViInt32 are dim. If you select an attribute data type that is
                   dim, LabWindows/CVI transfers you to the function panel for the
                   corresponding function that is consistent with the data type.
                -  If you want to enter a variable name, press **Ctrl**\ +\ **T** to
                   change this ring control to a manual input box. If the attribute in
                   this ring control has named constants as valid values, you can view
                   the constants by moving to the value control and pressing **Enter**.

        Returns:
            attribute_value (int): Returns the current value of the attribute. Passes the address of a
                ViInt32 variable.
                If the attribute currently showing in the attribute ring control has
                constants as valid values, you can view a list of the constants by
                pressing **Enter** on this control. Select a value by double-clicking on
                it or by selecting it and then pressing **Enter**.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case 9
        attribute_value_ctype = visatype.ViInt32()  # case 14
        error_code = self._library.niDCPower_GetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_id_ctype, ctypes.pointer(attribute_value_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(attribute_value_ctype.value)

    def _get_attribute_vi_int64(self, attribute_id):
        '''_get_attribute_vi_int64

        | Queries the value of a ViInt64 attribute.
        | You can use this function to get the values of device-specific
          attributes and inherent IVI attributes.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session instance, and calling this method on the result.:

            session['0,1']._get_attribute_vi_int64(attribute_id)

        Args:
            attribute_id (int): Specifies the ID of an attribute. From the function panel window, you
                can use this control as follows.

                -  In the function panel window, click on the control or press **Enter**
                   or the spacebar to display a dialog box containing hierarchical list
                   of the available attributes. Help text is shown for each attribute.
                   Select an attribute by double-clicking on it or by selecting it and
                   then pressing **Enter**.
                -  A ring control at the top of the dialog box allows you to see all IVI
                   attributes or only the attributes of type ViReal64. If you choose to
                   see all IVI attributes, the data types appear to the right of the
                   attribute names in the list box. Attributes with data types other
                   than ViReal64 are dim. If you select an attribute data type that is
                   dim, LabWindows/CVI transfers you to the function panel for the
                   corresponding function that is consistent with the data type.
                -  If you want to enter a variable name, press **Ctrl**\ +\ **T** to
                   change this ring control to a manual input box. If the attribute in
                   this ring control has named constants as valid values, you can view
                   the constants by moving to the value control and pressing **Enter**.

        Returns:
            attribute_value (int): Returns the current value of the attribute. Passes the address of a
                ViReal64 variable.
                If the attribute currently showing in the attribute ring control has
                constants as valid values, you can view a list of the constants by
                pressing **Enter** on this control. Select a value by double-clicking on
                it or by selecting it and then pressing **Enter**.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case 9
        attribute_value_ctype = visatype.ViInt64()  # case 14
        error_code = self._library.niDCPower_GetAttributeViInt64(vi_ctype, channel_name_ctype, attribute_id_ctype, ctypes.pointer(attribute_value_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(attribute_value_ctype.value)

    def _get_attribute_vi_real64(self, attribute_id):
        '''_get_attribute_vi_real64

        | Queries the value of a ViReal64 attribute.
        | You can use this function to get the values of device-specific
          attributes and inherent IVI attributes.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session instance, and calling this method on the result.:

            session['0,1']._get_attribute_vi_real64(attribute_id)

        Args:
            attribute_id (int): Specifies the ID of an attribute. From the function panel window, you
                can use this control as follows.

                -  In the function panel window, click on the control or press **Enter**
                   or the spacebar to display a dialog box containing hierarchical list
                   of the available attributes. Help text is shown for each attribute.
                   Select an attribute by double-clicking on it or by selecting it and
                   then pressing **Enter**.
                -  A ring control at the top of the dialog box allows you to see all IVI
                   attributes or only the attributes of type ViReal64. If you choose to
                   see all IVI attributes, the data types appear to the right of the
                   attribute names in the list box. Attributes with data types other
                   than ViReal64 are dim. If you select an attribute data type that is
                   dim, LabWindows/CVI transfers you to the function panel for the
                   corresponding function that is consistent with the data type.
                -  If you want to enter a variable name, press **Ctrl**\ +\ **T** to
                   change this ring control to a manual input box. If the attribute in
                   this ring control has named constants as valid values, you can view
                   the constants by moving to the value control and pressing **Enter**.

        Returns:
            attribute_value (float): Returns the current value of the attribute. Passes the address of a
                ViReal64 variable.
                If the attribute currently showing in the attribute ring control has
                constants as valid values, you can view a list of the constants by
                pressing **Enter** on this control. Select a value by double-clicking on
                it or by selecting it and then pressing **Enter**.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case 9
        attribute_value_ctype = visatype.ViReal64()  # case 14
        error_code = self._library.niDCPower_GetAttributeViReal64(vi_ctype, channel_name_ctype, attribute_id_ctype, ctypes.pointer(attribute_value_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(attribute_value_ctype.value)

    def _get_attribute_vi_string(self, attribute_id):
        '''_get_attribute_vi_string

        | Queries the value of a ViString attribute.
        | You can use this function to get the values of device-specific
          attributes and inherent IVI attributes.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session instance, and calling this method on the result.:

            session['0,1']._get_attribute_vi_string(attribute_id)

        Args:
            attribute_id (int): Specifies the ID of an attribute. From the function panel window, you
                can use this control as follows.

                -  In the function panel window, click on the control or press or the
                   spacebar to display a dialog box containing hierarchical list of the
                   available attributes. Help text is shown for each attribute. Select
                   an attribute by double-clicking on it or by selecting it and then
                   pressing .
                -  A ring control at the top of the dialog box allows you to see all IVI
                   attributes or only the attributes of type ViString. If you choose to
                   see all IVI attributes, the data types appear to the right of the
                   attribute names in the list box. Attributes with data types other
                   than ViString are dimmed. If you select an attribute data type that
                   is dimmed, LabWindows/CVI transfers you to the function panel for the
                   corresponding function that is consistent with the data type.
                -  If you want to enter a variable name, press to change this ring
                   control to a manual input control. If the attribute in this ring
                   control has named constants as valid values, you can view the
                   constants by moving to the value control and pressing .
            buffer_size (int): Passes the number of bytes in the buffer and specifies the number of
                bytes in the ViChar array you specify for **value**. If the current
                value of **value**, including the terminating NUL byte, is larger than
                the size you indicate in this parameter, the function copies (buffer
                size - 1) bytes into the buffer, places an ASCII NUL byte at the end of
                the buffer, and returns the buffer size you must pass to get the entire
                value. For example, if the value is 123456 and the buffer size is 4, the
                function places 123 into the buffer and returns 7.
                To obtain the required buffer size, you can pass 0 for this attribute
                and VI_NULL for **value**. If you want the function to fill in the
                buffer regardless of the number of bytes in the value, pass a negative
                number for this attribute.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case 9
        buffer_size_ctype = visatype.ViInt32()  # case 7
        attribute_value_ctype = None  # case 12
        error_code = self._library.niDCPower_GetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, buffer_size_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = visatype.ViInt32(error_code)  # TODO(marcoskirsch): use get_ctype_variable_declaration_snippet()
        attribute_value_ctype = (visatype.ViChar * buffer_size_ctype.value)()  # TODO(marcoskirsch): use get_ctype_variable_declaration_snippet()
        error_code = self._library.niDCPower_GetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, buffer_size_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return attribute_value_ctype.value.decode(self._encoding)

    def get_channel_name(self, index):
        '''get_channel_name

        Retrieves the output **channelName** that corresponds to the requested
        **index**. Use the CHANNEL_COUNT attribute to
        determine the upper bound of valid values for **index**.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session instance, and calling this method on the result.:

            session['0,1'].get_channel_name(index)

        Args:
            index (int): Specifies which output channel name to return. The index values begin at
                1.
            buffer_size (int): Specifies the number of bytes in the ViChar array you specify for
                **channelName**. If the **channelName**, including the terminating NUL
                byte, contains more bytes than you indicate in this attribute, the
                function copies (buffer size - 1) bytes into the buffer, places an ASCII
                NUL byte at the end of the buffer, and returns the buffer size you must
                pass to get the entire value. For example, if the value is 123456 and
                the buffer size is 4, the function places 123 into the buffer and
                returns 7.
                If you pass 0, you can pass VI_NULL for **channelName**.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        index_ctype = visatype.ViInt32(index)  # case 9
        buffer_size_ctype = visatype.ViInt32()  # case 7
        channel_name_ctype = None  # case 12
        error_code = self._library.niDCPower_GetChannelName(vi_ctype, index_ctype, buffer_size_ctype, channel_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = visatype.ViInt32(error_code)  # TODO(marcoskirsch): use get_ctype_variable_declaration_snippet()
        channel_name_ctype = (visatype.ViChar * buffer_size_ctype.value)()  # TODO(marcoskirsch): use get_ctype_variable_declaration_snippet()
        error_code = self._library.niDCPower_GetChannelName(vi_ctype, index_ctype, buffer_size_ctype, channel_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return channel_name_ctype.value.decode(self._encoding)

    def _get_error(self):
        '''_get_error

        | Retrieves and then clears the IVI error information for the session or
          the current execution thread unless **bufferSize** is 0, in which case
          the function does not clear the error information. By passing 0 for
          the buffer size, you can ascertain the buffer size required to get the
          entire error description string and then call the function again with
          a sufficiently large buffer size.
        | If the user specifies a valid IVI session for **vi**, this function
          retrieves and then clears the error information for the session. If
          the user passes VI_NULL for **vi**, this function retrieves and then
          clears the error information for the current execution thread. If
          **vi** is an invalid session, the function does nothing and returns an
          error. Normally, the error information describes the first error that
          occurred since the user last called _get_error or
          ClearError.

        Args:
            buffer_size (int): Specifies the number of bytes in the ViChar array you specify for
                **description**.
                If the error description, including the terminating NUL byte, contains
                more bytes than you indicate in this attribute, the function copies
                (buffer size - 1) bytes into the buffer, places an ASCII NUL byte at the
                end of the buffer, and returns the buffer size you must pass to get the
                entire value. For example, if the value is 123456 and the buffer size is
                4, the function places 123 into the buffer and returns 7.
                If you pass 0 for this attribute, you can pass VI_NULL for
                **description**.

        Returns:
            code (int): Returns the error code for the session or execution thread.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        code_ctype = visatype.ViStatus()  # case 14
        buffer_size_ctype = visatype.ViInt32()  # case 7
        description_ctype = None  # case 12
        error_code = self._library.niDCPower_GetError(vi_ctype, ctypes.pointer(code_ctype), buffer_size_ctype, description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=True)
        buffer_size_ctype = visatype.ViInt32(error_code)  # TODO(marcoskirsch): use get_ctype_variable_declaration_snippet()
        description_ctype = (visatype.ViChar * buffer_size_ctype.value)()  # TODO(marcoskirsch): use get_ctype_variable_declaration_snippet()
        error_code = self._library.niDCPower_GetError(vi_ctype, ctypes.pointer(code_ctype), buffer_size_ctype, description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return int(code_ctype.value), description_ctype.value.decode(self._encoding)

    def measure(self, measurement_type):
        '''measure

        Returns the measured value of either the voltage or current on the
        specified output channel. Each call to this function blocks other
        function calls until the hardware returns the **measurement**. To
        measure multiple output channels, use the MeasureMultiple
        function.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session instance, and calling this method on the result.:

            session['0,1'].measure(measurement_type)

        Args:
            measurement_type (enums.MeasurementTypes): Specifies whether a voltage or current value is measured.
                **Defined Values**:

                +-----------------------------------+------------------------------+
                | NIDCPOWER_VAL_MEASURE_VOLTAGE (1) | The device measures voltage. |
                +-----------------------------------+------------------------------+
                | NIDCPOWER_VAL_MEASURE_CURRENT (0) | The device measures current. |
                +-----------------------------------+------------------------------+

        Returns:
            measurement (float): Returns the value of the measurement, either in volts for voltage or
                amps for current.
        '''
        if type(measurement_type) is not enums.MeasurementTypes:
            raise TypeError('Parameter mode must be of type ' + str(enums.MeasurementTypes))
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        measurement_type_ctype = visatype.ViInt32(measurement_type.value)  # case 10
        measurement_ctype = visatype.ViReal64()  # case 14
        error_code = self._library.niDCPower_Measure(vi_ctype, channel_name_ctype, measurement_type_ctype, ctypes.pointer(measurement_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(measurement_ctype.value)

    def query_in_compliance(self):
        '''query_in_compliance

        Queries the specified output device to determine if it is operating at
        the `compliance <REPLACE_DRIVER_SPECIFIC_URL_2(compliance)>`__ limit.

        The compliance limit is the current limit when the output function is
        set to NIDCPOWER_VAL_DC_VOLTAGE. If the output is operating at the
        compliance limit, the output reaches the current limit before the
        desired voltage level. Refer to the ConfigureOutputFunction
        function and the ConfigureCurrentLimit function for more
        information about output function and current limit, respectively.

        The compliance limit is the voltage limit when the output function is
        set to NIDCPOWER_VAL_DC_CURRENT. If the output is operating at the
        compliance limit, the output reaches the voltage limit before the
        desired current level. Refer to the ConfigureOutputFunction
        function and the ConfigureVoltageLimit function for more
        information about output function and voltage limit, respectively.

        **Related Topics:**

        `Compliance <REPLACE_DRIVER_SPECIFIC_URL_1(compliance)>`__

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session instance, and calling this method on the result.:

            session['0,1'].query_in_compliance()

        Returns:
            in_compliance (bool): Returns whether the device output channel is in compliance.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        in_compliance_ctype = visatype.ViBoolean()  # case 14
        error_code = self._library.niDCPower_QueryInCompliance(vi_ctype, channel_name_ctype, ctypes.pointer(in_compliance_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(in_compliance_ctype.value)

    def query_max_current_limit(self, voltage_level):
        '''query_max_current_limit

        Queries the maximum current limit on an output channel if the output
        channel is set to the specified **voltageLevel**.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session instance, and calling this method on the result.:

            session['0,1'].query_max_current_limit(voltage_level)

        Args:
            voltage_level (float): Specifies the voltage level to use when calculating the
                **maxCurrentLimit**.

        Returns:
            max_current_limit (float): Returns the maximum current limit that can be set with the specified
                **voltageLevel**.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        voltage_level_ctype = visatype.ViReal64(voltage_level)  # case 9
        max_current_limit_ctype = visatype.ViReal64()  # case 14
        error_code = self._library.niDCPower_QueryMaxCurrentLimit(vi_ctype, channel_name_ctype, voltage_level_ctype, ctypes.pointer(max_current_limit_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(max_current_limit_ctype.value)

    def query_max_voltage_level(self, current_limit):
        '''query_max_voltage_level

        Queries the maximum voltage level on an output channel if the output
        channel is set to the specified **currentLimit**.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session instance, and calling this method on the result.:

            session['0,1'].query_max_voltage_level(current_limit)

        Args:
            current_limit (float): Specifies the current limit to use when calculating the
                **maxVoltageLevel**.

        Returns:
            max_voltage_level (float): Returns the maximum voltage level that can be set on an output channel
                with the specified **currentLimit**.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        current_limit_ctype = visatype.ViReal64(current_limit)  # case 9
        max_voltage_level_ctype = visatype.ViReal64()  # case 14
        error_code = self._library.niDCPower_QueryMaxVoltageLevel(vi_ctype, channel_name_ctype, current_limit_ctype, ctypes.pointer(max_voltage_level_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(max_voltage_level_ctype.value)

    def query_min_current_limit(self, voltage_level):
        '''query_min_current_limit

        Queries the minimum current limit on an output channel if the output
        channel is set to the specified **voltageLevel**.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session instance, and calling this method on the result.:

            session['0,1'].query_min_current_limit(voltage_level)

        Args:
            voltage_level (float): Specifies the voltage level to use when calculating the
                **minCurrentLimit**.

        Returns:
            min_current_limit (float): Returns the minimum current limit that can be set on an output channel
                with the specified **voltageLevel**.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        voltage_level_ctype = visatype.ViReal64(voltage_level)  # case 9
        min_current_limit_ctype = visatype.ViReal64()  # case 14
        error_code = self._library.niDCPower_QueryMinCurrentLimit(vi_ctype, channel_name_ctype, voltage_level_ctype, ctypes.pointer(min_current_limit_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(min_current_limit_ctype.value)

    def query_output_state(self, output_state):
        '''query_output_state

        Queries the specified output channel to determine if the output channel
        is currently in the state specified by **outputState**.

        **Related Topics:**

        `Compliance <REPLACE_DRIVER_SPECIFIC_URL_1(compliance)>`__

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session instance, and calling this method on the result.:

            session['0,1'].query_output_state(output_state)

        Args:
            output_state (enums.OutputStates): Specifies the output state of the output channel that is being queried.
                **Defined Values**:

                +-------------------------------------------+-------------------------------------------------------------------+
                | NIDCPOWER_VAL_OUTPUT_CONSTANT_VOLTAGE (0) | The device maintains a constant voltage by adjusting the current. |
                +-------------------------------------------+-------------------------------------------------------------------+
                | NIDCPOWER_VAL_OUTPUT_CONSTANT_CURRENT (1) | The device maintains a constant current by adjusting the voltage. |
                +-------------------------------------------+-------------------------------------------------------------------+

        Returns:
            in_state (bool): Returns whether the device output channel is in the specified output
                state.
        '''
        if type(output_state) is not enums.OutputStates:
            raise TypeError('Parameter mode must be of type ' + str(enums.OutputStates))
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        output_state_ctype = visatype.ViInt32(output_state.value)  # case 10
        in_state_ctype = visatype.ViBoolean()  # case 14
        error_code = self._library.niDCPower_QueryOutputState(vi_ctype, channel_name_ctype, output_state_ctype, ctypes.pointer(in_state_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(in_state_ctype.value)

    def _set_attribute_vi_boolean(self, attribute_id, attribute_value):
        '''_set_attribute_vi_boolean

        | Sets the value of a ViBoolean attribute.
        | This is a low-level function that you can use to set the values of
          device-specific attributes and inherent IVI attributes.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session instance, and calling this method on the result.:

            session['0,1']._set_attribute_vi_boolean(attribute_id, attribute_value)

        Args:
            attribute_id (int): Specifies the ID of an attribute. From the function panel window, you
                can use this control as follows.

                -  In the function panel window, click on the control or press **Enter**
                   or the spacebar to display a dialog box containing hierarchical list
                   of the available attributes. Attributes whose value cannot be set are
                   dim. Help text is shown for each attribute. Select an attribute by
                   double-clicking on it or by selecting it and then pressing **Enter**.
                -  Read-only attributes appear dim in the list box. If you select a
                   read-only attribute, an error message appears. A ring control at the
                   top of the dialog box allows you to see all IVI attributes or only
                   the attributes of type ViBoolean. If you choose to see all IVI
                   attributes, the data types appear to the right of the attribute names
                   in the list box. Attributes with data types other than ViBoolean are
                   dim. If you select an attribute data type that is dim, LabWindows/CVI
                   transfers you to the function panel for the corresponding function
                   that is consistent with the data type.
                -  If you want to enter a variable name, press **Ctrl**\ +\ **T** to
                   change this ring control to a manual input box. If the attribute in
                   this ring control has named constants as valid values, you can view
                   the constants by moving to the value control and pressing **Enter**.
            attribute_value (bool): Specifies the value to which you want to set the attribute. If the
                attribute currently showing in the attribute ring control has constants
                as valid values, you can view a list of the constants by pressing
                **Enter** on this control. Select a value by double-clicking on it or by
                selecting it and then pressing **Enter**.

                Note:
                Some of the values might not be valid depending upon the current
                settings of the device session.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case 9
        attribute_value_ctype = visatype.ViBoolean(attribute_value)  # case 9
        error_code = self._library.niDCPower_SetAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_int32(self, attribute_id, attribute_value):
        '''_set_attribute_vi_int32

        | Sets the value of a ViInt32 attribute.
        | This is a low-level function that you can use to set the values of
          device-specific attributes and inherent IVI attributes.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session instance, and calling this method on the result.:

            session['0,1']._set_attribute_vi_int32(attribute_id, attribute_value)

        Args:
            attribute_id (int): Specifies the ID of an attribute. From the function panel window, you
                can use this control as follows.

                -  In the function panel window, click on the control or press **Enter**
                   or the spacebar to display a dialog box containing hierarchical list
                   of the available attributes. Attributes whose value cannot be set are
                   dim. Help text is shown for each attribute. Select an attribute by
                   double-clicking on it or by selecting it and then pressing **Enter**.
                -  Read-only attributes appear dim in the list box. If you select a
                   read-only attribute, an error message appears. A ring control at the
                   top of the dialog box allows you to see all IVI attributes or only
                   the attributes of type ViInt32. If you choose to see all IVI
                   attributes, the data types appear to the right of the attribute names
                   in the list box. Attributes with data types other than ViInt32 are
                   dim. If you select an attribute data type that is dim, LabWindows/CVI
                   transfers you to the function panel for the corresponding function
                   that is consistent with the data type.
                -  If you want to enter a variable name, press **Ctrl**\ +\ **T** to
                   change this ring control to a manual input box. If the attribute in
                   this ring control has named constants as valid values, you can view
                   the constants by moving to the value control and pressing **Enter**.
            attribute_value (int): Specifies the value to which you want to set the attribute. If the
                attribute currently showing in the attribute ring control has constants
                as valid values, you can view a list of the constants by pressing
                **Enter** on this control. Select a value by double-clicking on it or by
                selecting it and then pressing **Enter**.

                Note:
                Some of the values might not be valid depending upon the current
                settings of the device session.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case 9
        attribute_value_ctype = visatype.ViInt32(attribute_value)  # case 9
        error_code = self._library.niDCPower_SetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_int64(self, attribute_id, attribute_value):
        '''_set_attribute_vi_int64

        | Sets the value of a ViInt64 attribute.
        | This is a low-level function that you can use to set the values of
          device-specific attributes and inherent IVI attributes.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session instance, and calling this method on the result.:

            session['0,1']._set_attribute_vi_int64(attribute_id, attribute_value)

        Args:
            attribute_id (int): Specifies the ID of an attribute. From the function panel window, you
                can use this control as follows.

                -  In the function panel window, click on the control or press **Enter**
                   or the spacebar to display a dialog box containing hierarchical list
                   of the available attributes. Attributes whose value cannot be set are
                   dim. Help text is shown for each attribute. Select an attribute by
                   double-clicking on it or by selecting it and then pressing **Enter**.
                -  Read-only attributes appear dim in the list box. If you select a
                   read-only attribute, an error message appears. A ring control at the
                   top of the dialog box allows you to see all IVI attributes or only
                   the attributes of type ViReal64. If you choose to see all IVI
                   attributes, the data types appear to the right of the attribute names
                   in the list box. Attributes with data types other than ViReal64 are
                   dim. If you select an attribute data type that is dim, LabWindows/CVI
                   transfers you to the function panel for the corresponding function
                   that is consistent with the data type.
                -  If you want to enter a variable name, press **Ctrl**\ +\ **T** to
                   change this ring control to a manual input box. If the attribute in
                   this ring control has named constants as valid values, you can view
                   the constants by moving to the value control and pressing **Enter**.
            attribute_value (int): Specifies the value to which you want to set the attribute. If the
                attribute currently showing in the attribute ring control has constants
                as valid values, you can view a list of the constants by pressing
                **Enter** on this control. Select a value by double-clicking on it or by
                selecting it and then pressing **Enter**.

                Note:
                Some of the values might not be valid depending upon the current
                settings of the device session.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case 9
        attribute_value_ctype = visatype.ViInt64(attribute_value)  # case 9
        error_code = self._library.niDCPower_SetAttributeViInt64(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_real64(self, attribute_id, attribute_value):
        '''_set_attribute_vi_real64

        | Sets the value of a ViReal64 attribute.
        | This is a low-level function that you can use to set the values of
          device-specific attributes and inherent IVI attributes.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session instance, and calling this method on the result.:

            session['0,1']._set_attribute_vi_real64(attribute_id, attribute_value)

        Args:
            attribute_id (int): Specifies the ID of an attribute. From the function panel window, you
                can use this control as follows.

                -  In the function panel window, click on the control or press **Enter**
                   or the spacebar to display a dialog box containing hierarchical list
                   of the available attributes. Attributes whose value cannot be set are
                   dim. Help text is shown for each attribute. Select an attribute by
                   double-clicking on it or by selecting it and then pressing **Enter**.
                -  Read-only attributes appear dim in the list box. If you select a
                   read-only attribute, an error message appears. A ring control at the
                   top of the dialog box allows you to see all IVI attributes or only
                   the attributes of type ViReal64. If you choose to see all IVI
                   attributes, the data types appear to the right of the attribute names
                   in the list box. Attributes with data types other than ViReal64 are
                   dim. If you select an attribute data type that is dim, LabWindows/CVI
                   transfers you to the function panel for the corresponding function
                   that is consistent with the data type.
                -  If you want to enter a variable name, press **Ctrl**\ +\ **T** to
                   change this ring control to a manual input box. If the attribute in
                   this ring control has named constants as valid values, you can view
                   the constants by moving to the value control and pressing **Enter**.
            attribute_value (float): Specifies the value to which you want to set the attribute. If the
                attribute currently showing in the attribute ring control has constants
                as valid values, you can view a list of the constants by pressing
                **Enter** on this control. Select a value by double-clicking on it or by
                selecting it and then pressing **Enter**.

                Note:
                Some of the values might not be valid depending upon the current
                settings of the device session.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case 9
        attribute_value_ctype = visatype.ViReal64(attribute_value)  # case 9
        error_code = self._library.niDCPower_SetAttributeViReal64(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_string(self, attribute_id, attribute_value):
        '''_set_attribute_vi_string

        | Sets the value of a ViString attribute.
        | This is a low-level function that you can use to set the values of
          device-specific attributes and inherent IVI attributes.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session instance, and calling this method on the result.:

            session['0,1']._set_attribute_vi_string(attribute_id, attribute_value)

        Args:
            attribute_id (int): Specifies the ID of an attribute. From the function panel window, you
                can use this control as follows.

                -  In the function panel window, click on the control or press **Enter**
                   or the spacebar to display a dialog box containing hierarchical list
                   of the available attributes. Attributes whose value cannot be set are
                   dim. Help text is shown for each attribute. Select an attribute by
                   double-clicking on it or by selecting it and then pressing **Enter**.
                -  Read-only attributes appear dim in the list box. If you select a
                   read-only attribute, an error message appears. A ring control at the
                   top of the dialog box allows you to see all IVI attributes or only
                   the attributes of type ViString. If you choose to see all IVI
                   attributes, the data types appear to the right of the attribute names
                   in the list box. Attributes with data types other than ViString are
                   dim. If you select an attribute data type that is dim, LabWindows/CVI
                   transfers you to the function panel for the corresponding function
                   that is consistent with the data type.
                -  If you want to enter a variable name, press **Ctrl**\ +\ **T** to
                   change this ring control to a manual input box. If the attribute in
                   this ring control has named constants as valid values, you can view
                   the constants by moving to the value control and pressing **Enter**.
            attribute_value (string): Specifies the value to which you want to set the attribute. If the
                attribute currently showing in the attribute ring control has constants
                as valid values, you can view a list of the constants by pressing
                **Enter** on this control. Select a value by double-clicking on it or by
                selecting it and then pressing **Enter**.

                Note:
                Some of the values might not be valid depending upon the current
                settings of the device session.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case 9
        attribute_value_ctype = ctypes.create_string_buffer(attribute_value.encode(self._encoding))  # case 3
        error_code = self._library.niDCPower_SetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_sequence(self, source_delays, values=None):
        '''set_sequence

        Configures a series of voltage or current outputs and corresponding
        source delays. The source mode must be set to
        `Sequence <REPLACE_DRIVER_SPECIFIC_URL_1(sequencing)>`__ for this
        function to take effect.

        Refer to the `Configuring the Source
        Unit <REPLACE_DRIVER_SPECIFIC_URL_1(configuringthesourceunit)>`__ topic
        in the *NI DC Power Supplies and SMUs Help* for more information about
        how to configure your device.

        Use this function in the Uncommitted or Committed programming states.
        Refer to the `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic in
        the *NI DC Power Supplies and SMUs Help* for more information about
        NI-DCPower programming states.

        Note:
        This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session instance, and calling this method on the result.:

            session['0,1'].set_sequence(source_delays, values=None)

        Args:
            values (list of float): Specifies the series of voltage levels or current levels, depending on
                the configured `output
                function <REPLACE_DRIVER_SPECIFIC_URL_1(programming_output)>`__.
                **Valid values**:
                The valid values for this parameter are defined by the voltage level
                range or current level range.
            source_delays (list of float): Specifies the source delay that follows the configuration of each value
                in the sequence.
                **Valid Values**:
                The valid values are between 0 and 167 seconds.
            size (int): The number of elements in the Values and the Source Delays arrays. The
                Values and Source Delays arrays should have the same size.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        values_ctype = None if values is None else (visatype.ViReal64 * len(values))(*values)  # case 4
        source_delays_ctype = None if source_delays is None else (visatype.ViReal64 * len(source_delays))(*source_delays)  # case 4
        size_ctype = visatype.ViUInt32(0 if values is None else len(values))  # case 6
        error_code = self._library.niDCPower_SetSequence(vi_ctype, channel_name_ctype, values_ctype, source_delays_ctype, size_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _error_message(self, error_code):
        '''_error_message

        Converts a status code returned by an instrument driver function into a
        user-readable string.

        Args:
            error_code (int): Specifies the **status** parameter that is returned from any of the
                NI-DCPower functions.

        Returns:
            error_message (string): Returns the user-readable message string that corresponds to the status
                code you specify.
                You must pass a ViChar array with at least 256 bytes.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        error_code_ctype = visatype.ViStatus(error_code)  # case 9
        error_message_ctype = (visatype.ViChar * 256)()  # case 11
        error_code = self._library.niDCPower_error_message(vi_ctype, error_code_ctype, error_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return error_message_ctype.value.decode(self._encoding)


class _RepeatedCapability(_SessionBase):
    '''Allows for setting/getting properties and calling methods for specific repeated capabilities (such as channels) on your session.'''

    def __init__(self, vi, repeated_capability):
        super(_RepeatedCapability, self).__init__(repeated_capability)
        self._vi = vi
        self._is_frozen = True


class Session(_SessionBase):
    '''An NI-DCPower session to a National Instruments Programmable Power Supply or Source Measure Unit.'''

    def __init__(self, resource_name, channels='', reset=False, option_string=''):
        super(Session, self).__init__(repeated_capability='')
        self._vi = 0  # This must be set before calling _initialize_with_channels().
        self._vi = self._initialize_with_channels(resource_name, channels, reset, option_string)
        self._is_frozen = True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def __getitem__(self, repeated_capability):
        '''Set/get properties or call methods with a repeated capability (i.e. channels)'''
        return _RepeatedCapability(self._vi, repeated_capability)

    def initiate(self):
        return _Acquisition(self)

    def close(self):
        try:
            self._close()
        except errors.Error as e:
            self._vi = 0
            raise
        self._vi = 0

    ''' These are code-generated '''

    def _abort(self):
        '''_abort

        Transitions the NI-DCPower session from the Running state to the
        Committed state. If a sequence is running, it is stopped. Any
        configuration functions called after this function are not applied until
        the _initiate function is called. If power output is enabled
        when you call the _abort function, the output channels remain
        in their current state and continue providing power.

        Use the ConfigureOutputEnabled function to disable power
        output on a per channel basis. Use the reset function to
        disable output on all channels.

        Refer to the `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic in
        the *NI DC Power Supplies and SMUs Help* for information about the
        specific NI-DCPower software states.

        **Related Topics:**

        `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        error_code = self._library.niDCPower_Abort(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def commit(self):
        '''commit

        Applies previously configured settings to the device. Calling this
        function moves the NI-DCPower session from the Uncommitted state into
        the Committed state. After calling this function, modifying any
        attribute reverts the NI-DCPower session to the Uncommitted state. Use
        the _initiate function to transition to the Running state.
        Refer to the `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic in
        the *NI DC Power Supplies and SMUs Help* for details about the specific
        NI-DCPower software states.

        **Related Topics:**

        `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        error_code = self._library.niDCPower_Commit(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_digital_edge_measure_trigger(self, input_terminal, edge=enums.DigitalEdge.RISING):
        '''configure_digital_edge_measure_trigger

        Configures the Measure trigger for digital edge triggering.

        Note:
        This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.

        Args:
            input_terminal (string): Specifies the input terminal for the digital edge Measure trigger.

                You can specify any valid input terminal for this function. Valid
                terminals are listed in MAX under the **Device Routes** tab. For
                PXIe-4162/4163, refer to the Signal Routing topic for the device to
                determine which routes are available. This information is not available
                on a Device Routes tab in MAX.

                Input terminals can be specified in one of two ways. If the device is
                named Dev1 and your terminal is PXI_Trig0, you can specify the terminal
                with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the
                shortened terminal name, PXI_Trig0. The input terminal can also be a
                terminal from another device. For example, you can set the input
                terminal on Dev1 to be /Dev2/SourceCompleteEvent.
            edge (enums.DigitalEdge): Specifies whether to configure the Measure trigger to assert on the
                rising or falling edge.
                **Defined Values:**

                +------------------------------+----------------------------------------------------------------+
                | NIDCPOWER_VAL_RISING (1016)  | Asserts the trigger on the rising edge of the digital signal.  |
                +------------------------------+----------------------------------------------------------------+
                | NIDCPOWER_VAL_FALLING (1017) | Asserts the trigger on the falling edge of the digital signal. |
                +------------------------------+----------------------------------------------------------------+
        '''
        if type(edge) is not enums.DigitalEdge:
            raise TypeError('Parameter mode must be of type ' + str(enums.DigitalEdge))
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        input_terminal_ctype = ctypes.create_string_buffer(input_terminal.encode(self._encoding))  # case 3
        edge_ctype = visatype.ViInt32(edge.value)  # case 10
        error_code = self._library.niDCPower_ConfigureDigitalEdgeMeasureTrigger(vi_ctype, input_terminal_ctype, edge_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_digital_edge_pulse_trigger(self, input_terminal, edge=enums.DigitalEdge.RISING):
        '''configure_digital_edge_pulse_trigger

        Configures the Pulse trigger for digital edge triggering.

        Note:
        This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.

        Args:
            input_terminal (string): Specifies the input terminal for the digital edge Pulse trigger.

                You can specify any valid input terminal for this function. Valid
                terminals are listed in MAX under the **Device Routes** tab. For
                PXIe-4162/4163, refer to the Signal Routing topic for the device to
                determine which routes are available. This information is not available
                on a Device Routes tab in MAX.

                Input terminals can be specified in one of two ways. If the device is
                named Dev1 and your terminal is PXI_Trig0, you can specify the terminal
                with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the
                shortened terminal name, PXI_Trig0. The input terminal can also be a
                terminal from another device. For example, you can set the input
                terminal on Dev1 to be /Dev2/SourceCompleteEvent.
            edge (enums.DigitalEdge): Specifies whether to configure the Pulse trigger to assert on the rising
                or falling edge.
                **Defined Values:**

                +------------------------------+----------------------------------------------------------------+
                | NIDCPOWER_VAL_RISING (1016)  | Asserts the trigger on the rising edge of the digital signal.  |
                +------------------------------+----------------------------------------------------------------+
                | NIDCPOWER_VAL_FALLING (1017) | Asserts the trigger on the falling edge of the digital signal. |
                +------------------------------+----------------------------------------------------------------+
        '''
        if type(edge) is not enums.DigitalEdge:
            raise TypeError('Parameter mode must be of type ' + str(enums.DigitalEdge))
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        input_terminal_ctype = ctypes.create_string_buffer(input_terminal.encode(self._encoding))  # case 3
        edge_ctype = visatype.ViInt32(edge.value)  # case 10
        error_code = self._library.niDCPower_ConfigureDigitalEdgePulseTrigger(vi_ctype, input_terminal_ctype, edge_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_digital_edge_sequence_advance_trigger(self, input_terminal, edge=enums.DigitalEdge.RISING):
        '''configure_digital_edge_sequence_advance_trigger

        Configures the Sequence Advance trigger for digital edge triggering.

        Note:
        This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.

        Args:
            input_terminal (string): Specifies the input terminal for the digital edge Sequence Advance
                trigger.

                You can specify any valid input terminal for this function. Valid
                terminals are listed in MAX under the **Device Routes** tab. For
                PXIe-4162/4163, refer to the Signal Routing topic for the device to
                determine which routes are available. This information is not available
                on a Device Routes tab in MAX.

                Input terminals can be specified in one of two ways. If the device is
                named Dev1 and your terminal is PXI_Trig0, you can specify the terminal
                with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the
                shortened terminal name, PXI_Trig0. The input terminal can also be a
                terminal from another device. For example, you can set the input
                terminal on Dev1 to be /Dev2/SourceCompleteEvent.
            edge (enums.DigitalEdge): Specifies whether to configure the Sequence Advance trigger to assert on
                the rising or falling edge.
                **Defined Values:**

                +------------------------------+----------------------------------------------------------------+
                | NIDCPOWER_VAL_RISING (1016)  | Asserts the trigger on the rising edge of the digital signal.  |
                +------------------------------+----------------------------------------------------------------+
                | NIDCPOWER_VAL_FALLING (1017) | Asserts the trigger on the falling edge of the digital signal. |
                +------------------------------+----------------------------------------------------------------+
        '''
        if type(edge) is not enums.DigitalEdge:
            raise TypeError('Parameter mode must be of type ' + str(enums.DigitalEdge))
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        input_terminal_ctype = ctypes.create_string_buffer(input_terminal.encode(self._encoding))  # case 3
        edge_ctype = visatype.ViInt32(edge.value)  # case 10
        error_code = self._library.niDCPower_ConfigureDigitalEdgeSequenceAdvanceTrigger(vi_ctype, input_terminal_ctype, edge_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_digital_edge_source_trigger(self, input_terminal, edge=enums.DigitalEdge.RISING):
        '''configure_digital_edge_source_trigger

        Configures the Source trigger for digital edge triggering.

        Note:
        This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.

        Args:
            input_terminal (string): Specifies the input terminal for the digital edge Source trigger.

                You can specify any valid input terminal for this function. Valid
                terminals are listed in MAX under the **Device Routes** tab. For
                PXIe-4162/4163, refer to the Signal Routing topic for the device to
                determine which routes are available. This information is not available
                on a Device Routes tab in MAX.

                Input terminals can be specified in one of two ways. If the device is
                named Dev1 and your terminal is PXI_Trig0, you can specify the terminal
                with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the
                shortened terminal name, PXI_Trig0. The input terminal can also be a
                terminal from another device. For example, you can set the input
                terminal on Dev1 to be /Dev2/SourceCompleteEvent.
            edge (enums.DigitalEdge): Specifies whether to configure the Source trigger to assert on the
                rising or falling edge.
                **Defined Values:**

                +------------------------------+----------------------------------------------------------------+
                | NIDCPOWER_VAL_RISING (1016)  | Asserts the trigger on the rising edge of the digital signal.  |
                +------------------------------+----------------------------------------------------------------+
                | NIDCPOWER_VAL_FALLING (1017) | Asserts the trigger on the falling edge of the digital signal. |
                +------------------------------+----------------------------------------------------------------+
        '''
        if type(edge) is not enums.DigitalEdge:
            raise TypeError('Parameter mode must be of type ' + str(enums.DigitalEdge))
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        input_terminal_ctype = ctypes.create_string_buffer(input_terminal.encode(self._encoding))  # case 3
        edge_ctype = visatype.ViInt32(edge.value)  # case 10
        error_code = self._library.niDCPower_ConfigureDigitalEdgeSourceTrigger(vi_ctype, input_terminal_ctype, edge_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_digital_edge_start_trigger(self, input_terminal, edge=enums.DigitalEdge.RISING):
        '''configure_digital_edge_start_trigger

        Configures the Start trigger for digital edge triggering.

        Note:
        This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.

        Args:
            input_terminal (string): Specifies the input terminal for the digital edge Start trigger.

                You can specify any valid input terminal for this function. Valid
                terminals are listed in MAX under the **Device Routes** tab. For
                PXIe-4162/4163, refer to the Signal Routing topic for the device to
                determine which routes are available. This information is not available
                on a Device Routes tab in MAX.

                Input terminals can be specified in one of two ways. If the device is
                named Dev1 and your terminal is PXI_Trig0, you can specify the terminal
                with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the
                shortened terminal name, PXI_Trig0. The input terminal can also be a
                terminal from another device. For example, you can set the input
                terminal on Dev1 to be /Dev2/SourceCompleteEvent.
            edge (enums.DigitalEdge): Specifies whether to configure the Start trigger to assert on the rising
                or falling edge.
                **Defined Values:**

                +------------------------------+----------------------------------------------------------------+
                | NIDCPOWER_VAL_RISING (1016)  | Asserts the trigger on the rising edge of the digital signal.  |
                +------------------------------+----------------------------------------------------------------+
                | NIDCPOWER_VAL_FALLING (1017) | Asserts the trigger on the falling edge of the digital signal. |
                +------------------------------+----------------------------------------------------------------+
        '''
        if type(edge) is not enums.DigitalEdge:
            raise TypeError('Parameter mode must be of type ' + str(enums.DigitalEdge))
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        input_terminal_ctype = ctypes.create_string_buffer(input_terminal.encode(self._encoding))  # case 3
        edge_ctype = visatype.ViInt32(edge.value)  # case 10
        error_code = self._library.niDCPower_ConfigureDigitalEdgeStartTrigger(vi_ctype, input_terminal_ctype, edge_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def create_advanced_sequence(self, sequence_name, attribute_ids, set_as_active_sequence=True):
        '''create_advanced_sequence

        Creates an empty advanced sequence. Call the
        create_advanced_sequence_step function to add steps to the
        active advanced sequence.

        **Support for this function**

        You must set the source mode to Sequence to use this function.

        Using the set_sequence function with Advanced Sequence
        functions is unsupported.

        Use this function in the Uncommitted or Committed programming states.
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
        This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.

        Args:
            sequence_name (string): Specifies the name of the sequence to create.
            attribute_id_count (int): Specifies the number of attributes in the attributeIDs array.
            attribute_ids (list of int): Specifies the attributes you reconfigure per step in the advanced
                sequence. The following table lists which attributes can be configured
                in an advanced sequence for each NI-DCPower device that supports
                advanced sequencing. A ✓ indicates that the attribute can be configured
                in advanced sequencing. An ✕ indicates that the attribute cannot be
                configured in advanced sequencing.

                +--------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
                | Attribute                      | PXIe-4135 | NI 4136 | NI 4137 | NI 4138 | NI 4139 | NI 4140/4142/4144 | NI 4141/4143/4145 | PXIe-4162/4163 |
                +================================+===========+=========+=========+=========+=========+===================+===================+================+
                | DC_NOISE_REJECTION             | ✓         | ✕       | ✓       | ✕       | ✓       | ✕                 | ✕                 | ✓              |
                +--------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
                | APERTURE_TIME                  | ✓         | ✓       | ✓       | ✓       | ✓       | ✓                 | ✓                 | ✓              |
                +--------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
                | MEASURE_RECORD_LENGTH          | ✓         | ✓       | ✓       | ✓       | ✓       | ✓                 | ✓                 | ✓              |
                +--------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
                | sense                          | ✓         | ✓       | ✓       | ✓       | ✓       | ✓                 | ✓                 | ✓              |
                +--------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
                | OVP_ENABLED                    | ✓         | ✓       | ✓       | ✕       | ✕       | ✕                 | ✕                 | ✕              |
                +--------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
                | OVP_LIMIT                      | ✓         | ✓       | ✓       | ✕       | ✕       | ✕                 | ✕                 | ✕              |
                +--------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
                | PULSE_BIAS_DELAY               | ✓         | ✓       | ✓       | ✓       | ✓       | ✕                 | ✕                 | ✕              |
                +--------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
                | PULSE_OFF_TIME                 | ✓         | ✓       | ✓       | ✓       | ✓       | ✕                 | ✕                 | ✕              |
                +--------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
                | PULSE_ON_TIME                  | ✓         | ✓       | ✓       | ✓       | ✓       | ✕                 | ✕                 | ✕              |
                +--------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
                | SOURCE_DELAY                   | ✓         | ✓       | ✓       | ✓       | ✓       | ✓                 | ✓                 | ✓              |
                +--------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
                | CURRENT_COMPENSATION_FREQUENCY | ✓         | ✕       | ✓       | ✕       | ✓       | ✕                 | ✓                 | ✓              |
                +--------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
                | CURRENT_GAIN_BANDWIDTH         | ✓         | ✕       | ✓       | ✕       | ✓       | ✕                 | ✓                 | ✓              |
                +--------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
                | CURRENT_POLE_ZERO_RATIO        | ✓         | ✕       | ✓       | ✕       | ✓       | ✕                 | ✓                 | ✓              |
                +--------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
                | VOLTAGE_COMPENSATION_FREQUENCY | ✓         | ✕       | ✓       | ✕       | ✓       | ✕                 | ✓                 | ✓              |
                +--------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
                | VOLTAGE_GAIN_BANDWIDTH         | ✓         | ✕       | ✓       | ✕       | ✓       | ✕                 | ✓                 | ✓              |
                +--------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
                | VOLTAGE_POLE_ZERO_RATIO        | ✓         | ✕       | ✓       | ✕       | ✓       | ✕                 | ✓                 | ✓              |
                +--------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
                | CURRENT_LEVEL                  | ✓         | ✓       | ✓       | ✓       | ✓       | ✓                 | ✓                 | ✓              |
                +--------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
                | CURRENT_LEVEL_RANGE            | ✓         | ✓       | ✓       | ✓       | ✓       | ✓                 | ✓                 | ✓              |
                +--------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
                | VOLTAGE_LIMIT                  | ✓         | ✓       | ✓       | ✓       | ✓       | ✓                 | ✓                 | ✓              |
                +--------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
                | VOLTAGE_LIMIT_RANGE            | ✓         | ✓       | ✓       | ✓       | ✓       | ✓                 | ✓                 | ✓              |
                +--------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
                | CURRENT_LIMIT                  | ✓         | ✓       | ✓       | ✓       | ✓       | ✓                 | ✓                 | ✓              |
                +--------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
                | CURRENT_LIMIT_RANGE            | ✓         | ✓       | ✓       | ✓       | ✓       | ✓                 | ✓                 | ✓              |
                +--------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
                | VOLTAGE_LEVEL                  | ✓         | ✓       | ✓       | ✓       | ✓       | ✓                 | ✓                 | ✓              |
                +--------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
                | VOLTAGE_LEVEL_RANGE            | ✓         | ✓       | ✓       | ✓       | ✓       | ✓                 | ✓                 | ✓              |
                +--------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
                | OUTPUT_ENABLED                 | ✓         | ✓       | ✓       | ✓       | ✓       | ✓                 | ✓                 | ✓              |
                +--------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
                | OUTPUT_FUNCTION                | ✓         | ✓       | ✓       | ✓       | ✓       | ✓                 | ✓                 | ✓              |
                +--------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
                | OUTPUT_RESISTANCE              | ✓         | ✕       | ✓       | ✕       | ✓       | ✕                 | ✓                 | ✕              |
                +--------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
                | PULSE_BIAS_CURRENT_LEVEL       | ✓         | ✓       | ✓       | ✓       | ✓       | ✕                 | ✕                 | ✕              |
                +--------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
                | PULSE_BIAS_VOLTAGE_LIMIT       | ✓         | ✓       | ✓       | ✓       | ✓       | ✕                 | ✕                 | ✕              |
                +--------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
                | PULSE_CURRENT_LEVEL            | ✓         | ✓       | ✓       | ✓       | ✓       | ✕                 | ✕                 | ✕              |
                +--------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
                | PULSE_CURRENT_LEVEL_RANGE      | ✓         | ✓       | ✓       | ✓       | ✓       | ✕                 | ✕                 | ✕              |
                +--------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
                | PULSE_VOLTAGE_LIMIT            | ✓         | ✓       | ✓       | ✓       | ✓       | ✕                 | ✕                 | ✕              |
                +--------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
                | PULSE_VOLTAGE_LIMIT_RANGE      | ✓         | ✓       | ✓       | ✓       | ✓       | ✕                 | ✕                 | ✕              |
                +--------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
                | PULSE_BIAS_CURRENT_LIMIT       | ✓         | ✓       | ✓       | ✓       | ✓       | ✕                 | ✕                 | ✕              |
                +--------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
                | PULSE_BIAS_VOLTAGE_LEVEL       | ✓         | ✓       | ✓       | ✓       | ✓       | ✕                 | ✕                 | ✕              |
                +--------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
                | PULSE_CURRENT_LIMIT            | ✓         | ✓       | ✓       | ✓       | ✓       | ✕                 | ✕                 | ✕              |
                +--------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
                | PULSE_CURRENT_LIMIT_RANGE      | ✓         | ✓       | ✓       | ✓       | ✓       | ✕                 | ✕                 | ✕              |
                +--------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
                | PULSE_VOLTAGE_LEVEL            | ✓         | ✓       | ✓       | ✓       | ✓       | ✕                 | ✕                 | ✕              |
                +--------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
                | PULSE_VOLTAGE_LEVEL_RANGE      | ✓         | ✓       | ✓       | ✓       | ✓       | ✕                 | ✕                 | ✕              |
                +--------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
                | TRANSIENT_RESPONSE             | ✓         | ✓       | ✓       | ✓       | ✓       | ✓                 | ✓                 | ✓              |
                +--------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
            set_as_active_sequence (bool): Specifies that this current sequence is active.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        sequence_name_ctype = ctypes.create_string_buffer(sequence_name.encode(self._encoding))  # case 3
        attribute_id_count_ctype = visatype.ViInt32(0 if attribute_ids is None else len(attribute_ids))  # case 6
        attribute_ids_ctype = None if attribute_ids is None else (visatype.ViInt32 * len(attribute_ids))(*attribute_ids)  # case 4
        set_as_active_sequence_ctype = visatype.ViBoolean(set_as_active_sequence)  # case 9
        error_code = self._library.niDCPower_CreateAdvancedSequence(vi_ctype, sequence_name_ctype, attribute_id_count_ctype, attribute_ids_ctype, set_as_active_sequence_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def create_advanced_sequence_step(self, set_as_active_step=True):
        '''create_advanced_sequence_step

        Creates a new advanced sequence step in the advanced sequence specified
        by the Active advanced sequence. When you create an advanced sequence
        step, each attribute you passed to the create_advanced_sequence
        function is reset to its default value for that step unless otherwise
        specified.

        **Support for this Function**

        You must set the source mode to Sequence to use this function.

        Using the set_sequence function with Advanced Sequence
        functions is unsupported.

        **Related Topics**:

        `Advanced Sequence
        Mode <REPLACE_DRIVER_SPECIFIC_URL_1(advancedsequencemode)>`__

        `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

        create_advanced_sequence

        Note:
        This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.

        Args:
            set_as_active_step (bool): Specifies that this current step in the active sequence is active.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        set_as_active_step_ctype = visatype.ViBoolean(set_as_active_step)  # case 9
        error_code = self._library.niDCPower_CreateAdvancedSequenceStep(vi_ctype, set_as_active_step_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def delete_advanced_sequence(self, sequence_name):
        '''delete_advanced_sequence

        Deletes a previously created advanced sequence and all the advanced
        sequence steps in the advanced sequence.

        **Support for this Function**

        You must set the source mode to Sequence to use this function.

        Using the set_sequence function with Advanced Sequence
        functions is unsupported.

        **Related Topics**:

        `Advanced Sequence
        Mode <REPLACE_DRIVER_SPECIFIC_URL_1(advancedsequencemode)>`__

        `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

        Note:
        This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.

        Args:
            sequence_name (string): specifies the name of the sequence to delete.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        sequence_name_ctype = ctypes.create_string_buffer(sequence_name.encode(self._encoding))  # case 3
        error_code = self._library.niDCPower_DeleteAdvancedSequence(vi_ctype, sequence_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disable(self):
        '''disable

        This function performs the same actions as the reset
        function, except that this function also immediately sets the
        OUTPUT_ENABLED attribute to VI_FALSE.

        This function opens the output relay on devices that have an output
        relay.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        error_code = self._library.niDCPower_Disable(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def export_signal(self, signal, output_terminal, signal_identifier=''):
        '''export_signal

        Routes signals (triggers and events) to the output terminal you specify.
        The route is created when the session is commit.

        **Related Topics:**

        `Triggers <REPLACE_DRIVER_SPECIFIC_URL_1(trigger)>`__

        Note:
        This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.

        Args:
            signal (enums.ExportSignal): Specifies which trigger or event to export.
                **Defined Values:**

                +--------------------------------------------------------+------------------------------------------------+
                | NIDCPOWER_VAL_SOURCE_COMPLETE_EVENT (1030)             | Exports the Source Complete event.             |
                +--------------------------------------------------------+------------------------------------------------+
                | NIDCPOWER_VAL_MEASURE_COMPLETE_EVENT (1031)            | Exports the Measure Complete event.            |
                +--------------------------------------------------------+------------------------------------------------+
                | NIDCPOWER_VAL_SEQUENCE_ITERATION_COMPLETE_EVENT (1032) | Exports the Sequence Iteration Complete event. |
                +--------------------------------------------------------+------------------------------------------------+
                | NIDCPOWER_VAL_SEQUENCE_ENGINE_DONE_EVENT (1033)        | Exports the Sequence Engine Done event.        |
                +--------------------------------------------------------+------------------------------------------------+
                | NIDCPOWER_VAL_PULSE_COMPLETE_EVENT (1051)              | Exports the Pulse Complete event.              |
                +--------------------------------------------------------+------------------------------------------------+
                | NIDCPOWER_VAL_READY_FOR_PULSE_TRIGGER_EVENT (1052)     | Exports the Ready Pulse Trigger event.         |
                +--------------------------------------------------------+------------------------------------------------+
                | NIDCPOWER_VAL_START_TRIGGER (1034)                     | Exports the Start trigger.                     |
                +--------------------------------------------------------+------------------------------------------------+
                | NIDCPOWER_VAL_SOURCE_TRIGGER (1035)                    | Exports the Source trigger.                    |
                +--------------------------------------------------------+------------------------------------------------+
                | NIDCPOWER_VAL_MEASURE_TRIGGER (1036)                   | Exports the Measure trigger.                   |
                +--------------------------------------------------------+------------------------------------------------+
                | NIDCPOWER_VAL_SEQUENCE_ADVANCE_TRIGGER (1037)          | Exports the Sequence Advance trigger.          |
                +--------------------------------------------------------+------------------------------------------------+
                | NIDCPOWER_VAL_PULSE_TRIGGER (1053)                     | Exports the Pulse trigger.                     |
                +--------------------------------------------------------+------------------------------------------------+
            signal_identifier (string): Reserved for future use. Pass in an empty string for this parameter.
            output_terminal (string): Specifies where to export the selected signal.
                **Relative Terminals**:

                +-------------+----------------------+
                | ""          | Do not export signal |
                +-------------+----------------------+
                | "PXI_Trig0" | PXI trigger line 0   |
                +-------------+----------------------+
                | "PXI_Trig1" | PXI trigger line 1   |
                +-------------+----------------------+
                | "PXI_Trig2" | PXI trigger line 2   |
                +-------------+----------------------+
                | "PXI_Trig3" | PXI trigger line 3   |
                +-------------+----------------------+
                | "PXI_Trig4" | PXI trigger line 4   |
                +-------------+----------------------+
                | "PXI_Trig5" | PXI trigger line 5   |
                +-------------+----------------------+
                | "PXI_Trig6" | PXI trigger line 6   |
                +-------------+----------------------+
                | "PXI_Trig7" | PXI trigger line 7   |
                +-------------+----------------------+
        '''
        if type(signal) is not enums.ExportSignal:
            raise TypeError('Parameter mode must be of type ' + str(enums.ExportSignal))
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        signal_ctype = visatype.ViInt32(signal.value)  # case 10
        signal_identifier_ctype = ctypes.create_string_buffer(signal_identifier.encode(self._encoding))  # case 3
        output_terminal_ctype = ctypes.create_string_buffer(output_terminal.encode(self._encoding))  # case 3
        error_code = self._library.niDCPower_ExportSignal(vi_ctype, signal_ctype, signal_identifier_ctype, output_terminal_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def get_ext_cal_last_date_and_time(self):
        '''get_ext_cal_last_date_and_time

        Returns the date and time of the last successful calibration. The time
        returned is 24-hour (military) local time; for example, if the device
        was calibrated at 2:30 PM, this function returns 14 for **hours** and 30
        for **minutes**.

        Returns:
            year (int): Returns the **year** the device was last calibrated.
            month (int): Returns the **month** in which the device was last calibrated.
            day (int): Returns the **day** on which the device was last calibrated.
            hour (int): Returns the **hour** (in 24-hour time) in which the device was last
                calibrated.
            minute (int): Returns the **minute** in which the device was last calibrated.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        year_ctype = visatype.ViInt32()  # case 14
        month_ctype = visatype.ViInt32()  # case 14
        day_ctype = visatype.ViInt32()  # case 14
        hour_ctype = visatype.ViInt32()  # case 14
        minute_ctype = visatype.ViInt32()  # case 14
        error_code = self._library.niDCPower_GetExtCalLastDateAndTime(vi_ctype, ctypes.pointer(year_ctype), ctypes.pointer(month_ctype), ctypes.pointer(day_ctype), ctypes.pointer(hour_ctype), ctypes.pointer(minute_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(year_ctype.value), int(month_ctype.value), int(day_ctype.value), int(hour_ctype.value), int(minute_ctype.value)

    def get_ext_cal_last_temp(self):
        '''get_ext_cal_last_temp

        Returns the onboard **temperature** of the device, in degrees Celsius,
        during the last successful external calibration.

        Returns:
            temperature (float): Returns the onboard **temperature** of the device, in degrees Celsius,
                during the last successful external calibration.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        temperature_ctype = visatype.ViReal64()  # case 14
        error_code = self._library.niDCPower_GetExtCalLastTemp(vi_ctype, ctypes.pointer(temperature_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(temperature_ctype.value)

    def get_ext_cal_recommended_interval(self):
        '''get_ext_cal_recommended_interval

        Returns the recommended maximum interval, in **months**, between
        external calibrations.

        Returns:
            months (int): Specifies the recommended maximum interval, in **months**, between
                external calibrations.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        months_ctype = visatype.ViInt32()  # case 14
        error_code = self._library.niDCPower_GetExtCalRecommendedInterval(vi_ctype, ctypes.pointer(months_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(months_ctype.value)

    def get_self_cal_last_date_and_time(self):
        '''get_self_cal_last_date_and_time

        Returns the date and time of the oldest successful self-calibration from
        among the channels in the session.

        The time returned is 24-hour (military) local time; for example, if you
        have a session using channels 1 and 2, and a self-calibration was
        performed on channel 1 at 2:30 PM, and a self-calibration was performed
        on channel 2 at 3:00 PM on the same day, this function returns 14 for
        **hours** and 30 for **minutes**.

        Note:
        This function is not supported on all devices. Refer to `Supported
        Functions by
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
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        year_ctype = visatype.ViInt32()  # case 14
        month_ctype = visatype.ViInt32()  # case 14
        day_ctype = visatype.ViInt32()  # case 14
        hour_ctype = visatype.ViInt32()  # case 14
        minute_ctype = visatype.ViInt32()  # case 14
        error_code = self._library.niDCPower_GetSelfCalLastDateAndTime(vi_ctype, ctypes.pointer(year_ctype), ctypes.pointer(month_ctype), ctypes.pointer(day_ctype), ctypes.pointer(hour_ctype), ctypes.pointer(minute_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(year_ctype.value), int(month_ctype.value), int(day_ctype.value), int(hour_ctype.value), int(minute_ctype.value)

    def get_self_cal_last_temp(self):
        '''get_self_cal_last_temp

        Returns the onboard temperature of the device, in degrees Celsius,
        during the oldest successful self-calibration from among the channels in
        the session.

        For example, if you have a session using channels 1 and 2, and you
        perform a self-calibration on channel 1 with a device temperature of 25
        degrees Celsius at 2:00, and a self-calibration was performed on channel
        2 at 27 degrees Celsius at 3:00 on the same day, this function returns
        25 for the **temperature** parameter.

        Note:
        This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.

        Returns:
            temperature (float): Returns the onboard **temperature** of the device, in degrees Celsius,
                during the oldest successful calibration.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        temperature_ctype = visatype.ViReal64()  # case 14
        error_code = self._library.niDCPower_GetSelfCalLastTemp(vi_ctype, ctypes.pointer(temperature_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(temperature_ctype.value)

    def _initialize_with_channels(self, resource_name, channels='', reset=False, option_string=''):
        '''_initialize_with_channels

        Creates and returns a new NI-DCPower session to the power supply or SMU
        specified in **resource name** to be used in all subsequent NI-DCPower
        function calls. With this function, you can optionally set the initial
        state of the following session attributes:

        -  simulate
        -  DRIVER_SETUP

        After calling this function, the session will be in the Uncommitted
        state. Refer to the `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic for
        details about specific software states.

        To place the device in a known start-up state when creating a new
        session, set **reset** to VI_TRUE. This action is equivalent to using
        the reset function immediately after initializing the
        session.

        To open a session and leave the device in its existing configuration
        without passing through a transitional output state, set **reset** to
        VI_FALSE. Then configure the device as in the previous session,
        changing only the desired settings, and then call the
        _initiate function.

        **Related Topics:**

        `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

        Args:
            resource_name (string): Specifies the **resourceName** assigned by Measurement & Automation
                Explorer (MAX), for example "PXI1Slot3" where "PXI1Slot3" is an
                instrument's **resourceName**. **resourceName** can also be a logical
                IVI name.
            channels (string): Specifies which output channel(s) to include in a new session. Specify
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
            option_string (string): Specifies the initial value of certain attributes for the session. The
                syntax for **optionString** is a list of attributes with an assigned
                value where 1 is VI_TRUE and 0 is VI_FALSE. For example:

                "Simulate=0"

                You do not have to specify a value for all the attributes. If you do not
                specify a value for an attribute, the default value is used.

                For more information about simulating a device, refer to `Simulating a
                Power Supply or SMU <REPLACE_DRIVER_SPECIFIC_URL_1(simulate)>`__.

        Returns:
            vi (int): Returns a session handle that you use to identify the device in all
                subsequent NI-DCPower function calls.
        '''
        resource_name_ctype = ctypes.create_string_buffer(resource_name.encode(self._encoding))  # case 3
        channels_ctype = ctypes.create_string_buffer(channels.encode(self._encoding))  # case 3
        reset_ctype = visatype.ViBoolean(reset)  # case 9
        option_string_ctype = ctypes.create_string_buffer(option_string.encode(self._encoding))  # case 3
        vi_ctype = visatype.ViSession()  # case 14
        error_code = self._library.niDCPower_InitializeWithChannels(resource_name_ctype, channels_ctype, reset_ctype, option_string_ctype, ctypes.pointer(vi_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(vi_ctype.value)

    def _initiate(self):
        '''_initiate

        Starts generation or acquisition, causing the NI-DCPower session to
        leave the Uncommitted state or Committed state and enter the Running
        state. To return to the Committed state call the _abort
        function. Refer to the `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic in
        the *NI DC Power Supplies and SMUs Help* for information about the
        specific NI-DCPower software states.

        **Related Topics:**

        `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        error_code = self._library.niDCPower_Initiate(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def read_current_temperature(self):
        '''read_current_temperature

        Returns the current onboard **temperature**, in degrees Celsius, of the
        device.

        Returns:
            temperature (float): Returns the onboard **temperature**, in degrees Celsius, of the device.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        temperature_ctype = visatype.ViReal64()  # case 14
        error_code = self._library.niDCPower_ReadCurrentTemperature(vi_ctype, ctypes.pointer(temperature_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(temperature_ctype.value)

    def reset_device(self):
        '''reset_device

        Resets the device to a known state. The function disables power
        generation, resets session attributes to their default values, clears
        errors such as overtemperature and unexpected loss of auxiliary power,
        commits the session attributes, and leaves the session in the
        Uncommitted state. This function also performs a hard reset on the
        device and driver software. This function has the same functionality as
        using reset in Measurement & Automation Explorer. Refer to the
        `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic for
        more information about NI-DCPower software states.

        This will also open the output relay on devices that have an output
        relay.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        error_code = self._library.niDCPower_ResetDevice(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def reset_with_defaults(self):
        '''reset_with_defaults

        Resets the device to a known state. This function disables power
        generation, resets session attributes to their default values, commits
        the session attributes, and leaves the session in the
        `Running <javascript:LaunchHelp('NI_DC_Power_Supplies_Help.chm::/programmingStates.html#running')>`__
        state. In addition to exhibiting the behavior of the reset
        function, this function can assign user-defined default values for
        configurable attributes from the IVI configuration.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        error_code = self._library.niDCPower_ResetWithDefaults(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def send_software_edge_trigger(self, trigger=enums.SendSoftwareEdgeTriggerType.START):
        '''send_software_edge_trigger

        Asserts the specified trigger. This function can override an external
        edge trigger.

        **Related Topics:**

        `Triggers <REPLACE_DRIVER_SPECIFIC_URL_1(trigger)>`__

        Note:
        This function is not supported on all devices. Refer to `Supported
        Functions by
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
                | NIDCPOWER_VAL_PULSE_TRIGGER (1053             | Asserts the Pulse trigger.            |
                +-----------------------------------------------+---------------------------------------+
        '''
        if type(trigger) is not enums.SendSoftwareEdgeTriggerType:
            raise TypeError('Parameter mode must be of type ' + str(enums.SendSoftwareEdgeTriggerType))
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        trigger_ctype = visatype.ViInt32(trigger.value)  # case 10
        error_code = self._library.niDCPower_SendSoftwareEdgeTrigger(vi_ctype, trigger_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def wait_for_event(self, event_id, timeout=10.0):
        '''wait_for_event

        Waits until the device has generated the specified event.

        The session monitors whether each type of event has occurred at least
        once since the last time this function or the _initiate
        function were called. If an event has only been generated once and you
        call this function successively, the function times out. Individual
        events must be generated between separate calls of this function.

        Note:
        Refer to `Supported Functions by
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
            timeout (float): Specifies the maximum time allowed for this function to complete, in
                seconds. If the function does not complete within this time interval,
                NI-DCPower returns an error.

                Note:
                When setting the timeout interval, ensure you take into account any
                triggers so that the timeout interval is long enough for your
                application.
        '''
        if type(event_id) is not enums.Event:
            raise TypeError('Parameter mode must be of type ' + str(enums.Event))
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        event_id_ctype = visatype.ViInt32(event_id.value)  # case 10
        timeout_ctype = visatype.ViReal64(timeout)  # case 9
        error_code = self._library.niDCPower_WaitForEvent(vi_ctype, event_id_ctype, timeout_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _close(self):
        '''_close

        Closes the session specified in **vi** and deallocates the resources
        that NI-DCPower reserves. If power output is enabled when you call this
        function, the output channels remain in their existing state and
        continue providing power. Use the ConfigureOutputEnabled
        function to disable power output on a per channel basis. Use the
        reset function to disable power output on all channel(s).

        **Related Topics:**

        `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        error_code = self._library.niDCPower_close(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def reset(self):
        '''reset

        Resets the device to a known state. This function disables power
        generation, resets session attributes to their default values, commits
        the session attributes, and leaves the session in the Uncommitted state.
        Refer to the `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic for
        more information about NI-DCPower software states.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        error_code = self._library.niDCPower_reset(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def self_test(self):
        '''self_test

        Performs the device self-test routine and returns the test result(s).
        Calling this function implicitly calls the reset function.

        Returns:
            self_test_result (int): Returns the value result from the device self-test.

                +----------------+-------------------+
                | Self-Test Code | Description       |
                +================+===================+
                | 0              | Self test passed. |
                +----------------+-------------------+
                | 1              | Self test failed. |
                +----------------+-------------------+
            self_test_message (string): Returns the self-test result message. The size of this array must be at
                least 256 bytes.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        self_test_result_ctype = visatype.ViInt16()  # case 14
        self_test_message_ctype = (visatype.ViChar * 256)()  # case 11
        error_code = self._library.niDCPower_self_test(vi_ctype, ctypes.pointer(self_test_result_ctype), self_test_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(self_test_result_ctype.value), self_test_message_ctype.value.decode(self._encoding)



