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

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    active_advanced_sequence_step = attributes.AttributeViInt64(1150075)
    '''
    Specifies the advanced sequence step to configure.

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    aperture_time = attributes.AttributeViReal64(1150058)
    '''
    Specifies the measurement aperture time for the channel configuration.
    Aperture time is specified in the units set by the `Aperture Time
    Units <pniDCPower_ApertureTimeUnits.html>`__ property.

    Refer to the `Aperture
    Time <NI_DC_Power_Supplies_Help.chm::/Aperture.html>`__ topic in the *NI
    DC Power Supplies and SMUs Help* for more information about how to
    configure your measurements and for information about valid values.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    **Related topics:**

    `Aperture Time <NI_DC_Power_Supplies_Help.chm::/Aperture.html>`__

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    aperture_time_units = attributes.AttributeEnum(attributes.AttributeViInt32, enums.ApertureTimeUnits, 1150059)
    '''
    Specifies the units of the `Aperture
    Time <pniDCPower_ApertureTime.html>`__ property for the channel
    configuration.

    Refer to the `Aperture
    Time <NI_DC_Power_Supplies_Help.chm::/Aperture.html>`__ topic in the *NI
    DC Power Supplies and SMUs Help* for more information about how to
    configure your measurements and for information about valid values.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    **Related topics:**

    `Aperture Time <NI_DC_Power_Supplies_Help.chm::/Aperture.html>`__

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    auto_zero = attributes.AttributeEnum(attributes.AttributeViInt32, enums.AutoZero, 1150055)
    '''
    Specifies the auto-zero method to use on the device.

    Refer to the `NI PXI-4132 Measurement Configuration and
    Timing <NI_DC_Power_Supplies_Help.chm::/4132_MeasureConfigTiming.html>`__
    and `Auto Zero <NI_DC_Power_Supplies_Help.chm::/AutoZero.html>`__ topics
    in the *NI DC Power Supplies and SMUs Help* for more information about
    how to configure your measurements.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    **Related topics:**

    `Auto Zero <NI_DC_Power_Supplies_Help.chm::/AutoZero.html>`__
    '''
    auxiliary_power_source_available = attributes.AttributeViBoolean(1150002)
    '''
    Indicates whether an auxiliary power source is connected to the device.

    A value of FALSE may indicate that the auxiliary input fuse has blown.
    Refer to the `Detecting Internal/Auxiliary
    Power <NI_DC_Power_Supplies_Help.chm::/Detecting_Internal_Auxiliary_Power.html>`__
    topic in the *NI DC Power Supplies and SMUs Help* for more information
    about internal and auxiliary power.

    **Related topics:**

    `NI PXI-4110 Internal and Auxiliary
    Power <NI_DC_Power_Supplies_Help.chm::/4110_Internal_Auxiliary_Power.html>`__

    `NI PXI-4130 Internal and Auxiliary
    Power <NI_DC_Power_Supplies_Help.chm::/4130_Internal_Auxiliary_Power.html>`__

    Note:
    This property does not necessarily indicate if the device is using the
    auxiliary power source to generate power. Use the `Power Source In
    Use <pniDCPower_PowerSourceInUse.html>`__ property to retrieve that
    information.
    '''
    cache = attributes.AttributeViBoolean(1050004)
    '''
    Specifies whether to cache the value of properties.

    When caching is enabled, NI-DCPower records the current power supply
    settings and avoids sending redundant commands to the device. Enabling
    caching can significantly increase execution speed.

    NI-DCPower might always cache or never cache particular properties
    regardless of the setting of this property.

    Use the `niDCPower Initialize With
    Channels <NIDCPowerVIRef.chm::/niDCPower_Initialize_With_Channels.html>`__
    VI to override this value.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.
    '''
    channel_count = attributes.AttributeViInt32(1050203)
    '''
    Indicates the number of channels that NI-DCPower supports for the
    instrument that was chosen when the current session was opened. For
    channel-based properties, the IVI engine maintains a separate cache
    value for each channel.
    '''
    current_compensation_frequency = attributes.AttributeViReal64(1150071)
    '''
    The frequency at which a pole-zero pair is added to the system when the
    channel is in `Constant
    Current <NI_DC_Power_Supplies_Help.chm::/Constant_Current.html>`__ mode.

    **Default Value**: Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    current_gain_bandwidth = attributes.AttributeViReal64(1150070)
    '''
    The frequency at which the unloaded loop gain extrapolates to 0 dB in
    the absence of additional poles and zeroes. This property takes effect
    when the channel is in `Constant
    Current <NI_DC_Power_Supplies_Help.chm::/Constant_Current.html>`__ mode.

    **Default Value**: Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    current_level = attributes.AttributeViReal64(1150009)
    '''
    Specifies the current level, in amps, that the device attempts to
    generate on the specified channel(s).

    This property is applicable only if the `Output
    Function <pniDCPower_OutputFunction.html>`__ property is set to **DC
    Current**.

    **Valid Values:** The valid values for this property are defined by the
    values to which the `Current Level
    Range <pniDCPower_CurrentLevelRange.html>`__ property is set.

    **Related topics:**

    `Constant Current
    Mode <NI_DC_Power_Supplies_Help.chm::/Constant_Current.html>`__

    Note:
    The channel must be enabled for the specified current level to take
    effect. Refer to the `Output Enabled <pniDCPower_OutputEnabled.html>`__
    property for more information about enabling the output channel.
    '''
    current_level_autorange = attributes.AttributeEnum(attributes.AttributeViInt32, enums.CurrentLevelAutorange, 1150017)
    '''
    Specifies whether NI-DCPower automatically selects the current level
    range based on the desired current level for the specified channel(s).

    If you set this property to **On**, NI-DCPower ignores any changes you
    make to the `Current Level Range <pniDCPower_CurrentLevelRange.html>`__
    property. If you change the Current Level Autorange property from **On**
    to **Off**, NI-DCPower retains the last value the `Current Level
    Range <pniDCPower_CurrentLevelRange.html>`__ property was set to (or the
    default value if it was never set) and uses that value as the current
    level range.

    Refer to the `Current Level Range <pniDCPower_CurrentLevelRange.html>`__
    property for information about which range NI-DCPower automatically
    selects.

    The Current Level Autorange property is applicable only if the `Output
    Function <pniDCPower_OutputFunction.html>`__ property is set to **DC
    Current**.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    **Related topics:**

    `Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
    '''
    current_level_range = attributes.AttributeViReal64(1150011)
    '''
    Specifies the current level range, in amps, for the specified
    channel(s).

    The range defines the valid values to which the current level can be
    set. Use the `Current Level
    Autorange <pniDCPower_CurrentLevelAutorange.html>`__ property to enable
    automatic selection of the current level range.

    The Current Level Range property is applicable only if the `Output
    Function <pniDCPower_OutputFunction.html>`__ property is set to **DC
    Current**.

    For valid ranges for your device, refer to
    `Ranges <NI_DC_Power_Supplies_Help.chm::/Ranges.html>`__.

    **Related topics:**

    `Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__

    Note:
    The channel must be enabled for the specified current level range to
    take effect. Refer to the `Output
    Enabled <pniDCPower_OutputEnabled.html>`__ property for more information
    about enabling the output channel.
    '''
    current_limit = attributes.AttributeViReal64(1250005)
    '''
    Specifies the current limit, in amps, that the output cannot exceed when
    generating the desired voltage on the specified channel(s). Limit is
    specified as a positive value, but symmetric positive and negative
    limits are enforced simultaneously.

    This property is applicable only if the `Output
    Function <pniDCPower_OutputFunction.html>`__ property is set to **DC
    Voltage**.

    **Valid Values:** The valid values for this property are defined by the
    values to which the `Current Limit
    Range <pniDCPower_CurrentLimitRange.html>`__ property is set.

    **Related topics:**

    `Compliance <NI_DC_Power_Supplies_Help.chm::/compliance.html>`__

    Note:
    The channel must be enabled for the specified current limit to take
    effect. Refer to the `Output Enabled <pniDCPower_OutputEnabled.html>`__
    property for more information about enabling the output channel.
    '''
    current_limit_autorange = attributes.AttributeEnum(attributes.AttributeViInt32, enums.CurrentLimitAutorange, 1150016)
    '''
    Specifies whether NI-DCPower automatically selects the current limit
    range based on the desired current limit for the specified channel(s).

    If you set this property to **On**, NI-DCPower ignores any changes you
    make to the `Current Limit Range <pniDCPower_CurrentLimitRange.html>`__
    property. If you change the Current Limit Autorange property from **On**
    to **Off**, NI-DCPower retains the last value the Current Limit Range
    property was set to (or the default value if it was never set) and uses
    that value as the current limit range.

    Refer to the `Current Limit Range <pniDCPower_CurrentLimitRange.html>`__
    property for information about which range NI-DCPower automatically
    selects.

    The Current Limit Autorange property is applicable only if the channel
    is configured to **DC Voltage** in the `Output
    Function <pniDCPower_OutputFunction.html>`__ property.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    **Related topics:**

    `Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
    '''
    current_limit_range = attributes.AttributeViReal64(1150004)
    '''
    Specifies the current limit range, in amps, for the specified
    channel(s).

    The range defines the valid values to which the current limit can be
    set. Use the `Current Limit
    Autorange <pniDCPower_CurrentLimitAutorange.html>`__ property to enable
    automatic selection of the current limit range.

    The Current Limit Range property is applicable only if the `Output
    Function <pniDCPower_OutputFunction.html>`__ property is set to **DC
    Voltage**.

    For valid ranges for your device, refer to
    `Ranges <NI_DC_Power_Supplies_Help.chm::/Ranges.html>`__.

    **Related topics:**

    `Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__

    Note:
    The channel must be enabled for the specified current limit to take
    effect. Refer to the `Output Enabled <pniDCPower_OutputEnabled.html>`__
    property for more information about enabling the output channel.
    '''
    current_pole_zero_ratio = attributes.AttributeViReal64(1150072)
    '''
    The ratio of the pole frequency to the zero frequency when the channel
    is in `Constant
    Current <NI_DC_Power_Supplies_Help.chm::/Constant_Current.html>`__ mode.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    dc_noise_rejection = attributes.AttributeEnum(attributes.AttributeViInt32, enums.DCNoiseRejection, 1150066)
    '''
    Determines the relative weighting of samples in a measurement.

    For information about improving noise immunity for NI-DCPower devices
    that support DC noise rejection, refer to `Measurement Noise
    Rejection <NI_DC_Power_Supplies_Help.chm::/noiseRejectMeasure.html>`__

    **Default Value**: **Normal**

    **Related topics:**

    `Measurement Noise
    Rejection <NI_DC_Power_Supplies_Help.chm::/NoiseRejectMeasure.html>`__

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    digital_edge_measure_trigger_edge = attributes.AttributeEnum(attributes.AttributeViInt32, enums.DigitalEdge, 1150035)
    '''
    Specifies whether to configure the Measure trigger to assert on the
    rising or falling edge.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    **Related topics:**

    `Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    digital_edge_measure_trigger_input_terminal = attributes.AttributeViString(1150036)
    '''
    Specifies the input terminal for the Measure trigger. This property is
    used only when the `Measure Trigger
    Type <pniDCPower_MeasureTriggerType.html>`__ property is set to
    **Digital Edge**.

    You can specify any valid input terminal for this property. Valid
    terminals are listed in Measurement & Automation Explorer under the
    **Device Routes** tab.

    Input terminals can be specified in one of two ways. If the device is
    named Dev1 and your terminal is PXI_Trig0, you can specify the terminal
    with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the
    shortened terminal name, PXI_Trig0. The input terminal can also be a
    terminal from another device. For example, you can set the input
    terminal on Dev1 to be /Dev2/SourceCompleteEvent.

    **Related topics:**

    `Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    digital_edge_pulse_trigger_edge = attributes.AttributeEnum(attributes.AttributeViInt32, enums.DigitalEdge, 1150096)
    '''
    Specifies whether to configure the Pulse trigger to assert on the rising
    or falling edge.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    **Related topics:**

    `Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    digital_edge_pulse_trigger_input_terminal = attributes.AttributeViString(1150097)
    '''
    Specifies the input terminal for the Pulse trigger. This property is
    used only when the `Pulse Trigger
    Type <pniDCPower_StartTriggerType.html>`__ property is set to **Digital
    Edge**.

    You can specify any valid input terminal for this property. Valid
    terminals are listed in Measurement & Automation Explorer under the
    **Device Routes** tab.

    Input terminals can be specified in one of two ways. If the device is
    named Dev1 and your terminal is PXI_Trig0, you can specify the terminal
    with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the
    shortened terminal name, PXI_Trig0. The input terminal can also be a
    terminal from another device. For example, you can set the input
    terminal on Dev1 to be /Dev2/SourceCompleteEvent.

    **Related topics:**

    `Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    digital_edge_sequence_advance_trigger_edge = attributes.AttributeEnum(attributes.AttributeViInt32, enums.DigitalEdge, 1150027)
    '''
    Specifies whether to configure the Sequence trigger to assert on the
    rising or falling edge.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    **Related topics:**

    `Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    digital_edge_sequence_advance_trigger_input_terminal = attributes.AttributeViString(1150028)
    '''
    Specifies the input terminal for the Sequence Advance trigger. This
    property is used only when the `Sequence Advance Trigger
    Type <pniDCPower_SequenceAdvanceTriggerType.html>`__ property is set to
    **Digital Edge**.

    You can specify any valid input terminal for this property. Valid
    terminals are listed in Measurement & Automation Explorer under the
    **Device Routes** tab.

    Input terminals can be specified in one of two ways. If the device is
    named Dev1 and your terminal is PXI_Trig0, you can specify the terminal
    with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the
    shortened terminal name, PXI_Trig0. The input terminal can also be a
    terminal from another device. For example, you can set the input
    terminal on Dev1 to be /Dev2/SourceCompleteEvent.

    **Related topics:**

    `Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    digital_edge_source_trigger_edge = attributes.AttributeEnum(attributes.AttributeViInt32, enums.DigitalEdge, 1150031)
    '''
    Specifies whether to configure the Source trigger to assert on the
    rising or falling edge.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    **Related topics:**

    `Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    digital_edge_source_trigger_input_terminal = attributes.AttributeViString(1150032)
    '''
    Specifies the input terminal for the Source trigger. This property is
    used only when the `Source Trigger
    Type <pniDCPower_SourceTriggerType.html>`__ property is set to **Digital
    Edge**.

    You can specify any valid input terminal for this property. Valid
    terminals are listed in Measurement & Automation Explorer under the
    **Device Routes** tab.

    Input terminals can be specified in one of two ways. If the device is
    named Dev1 and your terminal is PXI_Trig0, you can specify the terminal
    with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the
    shortened terminal name, PXI_Trig0. The input terminal can also be a
    terminal from another device. For example, you can set the input
    terminal on Dev1 to be /Dev2/SourceCompleteEvent.

    **Related topics:**

    `Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    digital_edge_start_trigger_edge = attributes.AttributeEnum(attributes.AttributeViInt32, enums.DigitalEdge, 1150022)
    '''
    Specifies whether to configure the Start trigger to assert on the rising
    or falling edge.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    **Related topics:**

    `Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    digital_edge_start_trigger_input_terminal = attributes.AttributeViString(1150023)
    '''
    Specifies the input terminal for the Start trigger. This property is
    used only when the `Start Trigger
    Type <pniDCPower_StartTriggerType.html>`__ property is set to **Digital
    Edge**.

    You can specify any valid input terminal for this property. Valid
    terminals are listed in Measurement & Automation Explorer under the
    **Device Routes** tab.

    Input terminals can be specified in one of two ways. If the device is
    named Dev1 and your terminal is PXI_Trig0, you can specify the terminal
    with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the
    shortened terminal name, PXI_Trig0. The input terminal can also be a
    terminal from another device. For example, you can set the input
    terminal on Dev1 to be /Dev2/SourceCompleteEvent.

    **Related topics:**

    `Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    driver_setup = attributes.AttributeViString(1050007)
    '''
    Indicates the Driver Setup string that you specified when initializing
    the driver.

    Some cases exist where you must specify the instrument driver options at
    initialization time. An example of this case is specifying a particular
    instrument model from among a family of instruments that the driver
    supports. This property is useful when
    `simulating <NI_DC_Power_Supplies_Help.chm::/simulate.html>`__ a device.
    You can specify the driver-specific options through the Driver Setup
    keyword in the **options string** parameter in the `niDCPower Initialize
    with
    Options <NIDCPowerVIRef.chm::/niDCPower_Initialize_With_Options.html>`__
    VI or through the IVI Configuration Utility.

    If you do not specify a Driver Setup string, this property returns an
    empty string.
    '''
    exported_measure_trigger_output_terminal = attributes.AttributeViString(1150037)
    '''
    Specifies the output terminal for exporting the Measure trigger.

    Refer to the **Device Routes** tab in Measurement & Automation Explorer
    for a list of the terminals available on your device.

    Output terminals can be specified in one of two ways. If the device is
    named Dev1 and your terminal is PXI_Trig0, you can specify the terminal
    with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the
    shortened terminal name, PXI_Trig0.

    **Related topics:**

    `Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    exported_pulse_trigger_output_terminal = attributes.AttributeViString(1150098)
    '''
    Specifies the output terminal for exporting the Pulse trigger.

    Refer to the **Device Routes** tab in Measurement & Automation Explorer
    for a list of the terminals available on your device.

    Output terminals can be specified in one of two ways. If the device is
    named Dev1 and your terminal is PXI_Trig0, you can specify the terminal
    with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the
    shortened terminal name, PXI_Trig0.

    **Related topics:**

    `Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    exported_sequence_advance_trigger_output_terminal = attributes.AttributeViString(1150029)
    '''
    Specifies the output terminal for exporting the Sequence Advance
    trigger.

    Refer to the **Device Routes** tab in Measurement & Automation Explorer
    for a list of the terminals available on your device.

    Output terminals can be specified in one of two ways. If the device is
    named Dev1 and your terminal is PXI_Trig0, you can specify the terminal
    with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the
    shortened terminal name, PXI_Trig0.

    **Related topics:**

    `Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    exported_source_trigger_output_terminal = attributes.AttributeViString(1150033)
    '''
    Specifies the output terminal for exporting the Source trigger.

    Refer to the **Device Routes** tab in Measurement & Automation Explorer
    for a list of the terminals available on your device.

    Output terminals can be specified in one of two ways. If the device is
    named Dev1 and your terminal is PXI_Trig0, you can specify the terminal
    with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the
    shortened terminal name, PXI_Trig0.

    **Related topics:**

    `Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    exported_start_trigger_output_terminal = attributes.AttributeViString(1150024)
    '''
    Specifies the output terminal for exporting the Start trigger.

    Refer to the **Device Routes** tab in Measurement & Automation Explorer
    for a list of the terminals available on your device.

    Output terminals can be specified in one of two ways. If the device is
    named Dev1 and your terminal is PXI_Trig0, you can specify the terminal
    with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the
    shortened terminal name, PXI_Trig0.

    **Related topics:**

    `Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    fetch_backlog = attributes.AttributeViInt32(1150056)
    '''
    Returns the number of measurements acquired that have not been fetched
    yet.
    '''
    group_capabilities = attributes.AttributeViString(1050401)
    '''
    Contains a comma-separated (,) list of class-extension groups that
    NI-DCPower implements.
    '''
    instrument_firmware_revision = attributes.AttributeViString(1050510)
    '''
    Contains the firmware revision information for the device you are
    currently using.
    '''
    instrument_manufacturer = attributes.AttributeViString(1050511)
    '''
    Contains the name of the manufacturer for the device you are currently
    using.
    '''
    instrument_model = attributes.AttributeViString(1050512)
    '''
    Contains the model number or name of the device you are currently using.
    '''
    interchange_check = attributes.AttributeViBoolean(1050021)
    '''
    Specifies whether to perform interchangeability checking and log
    interchangeability warnings when you call NI-DCPower VIs. TRUE specifies
    that interchangeability checking is enabled.

    Interchangeability warnings indicate that using your application with a
    different power supply might cause different behavior. Call the
    `niDCPower Get Next Interchange
    Warning <NIDCPowerVIRef.chm::/niDCPower_Get_Next_Interchange_Warning.html>`__
    VI to retrieve interchange warnings.

    Call the `niDCPower Clear Interchange
    Warnings <NIDCPowerVIRef.chm::/niDCPower_Clear_Interchange_Warnings.html>`__
    VI to clear the list of interchangeability warnings without reading
    them.

    Interchangeability checking examines the properties in a capability
    group only if you specify a value for at least one property within that
    group. Interchangeability warnings can occur when a property affects the
    behavior of the device and you have not set that property or when the
    property has been invalidated since you set it.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.
    '''
    interlock_input_open = attributes.AttributeViBoolean(1150105)
    '''
    Indicates whether the safety interlock circuit is open.

    Refer to the `Safety
    Interlock <NI_DC_Power_Supplies_Help.chm::/Interlock.html>`__ topic in
    the *NI DC Power Supplies and SMUs Help* for more information about the
    interlock circuit.

    **Defined Values**

    +-------+-----------------------------------+
    | FALSE | Safety interlock input is closed. |
    +-------+-----------------------------------+
    | TRUE  | Safety interlock input is open.   |
    +-------+-----------------------------------+

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    io_resource_descriptor = attributes.AttributeViString(1050304)
    '''
    Indicates the resource descriptor NI-DCPower uses to identify the
    physical device.

    If you initialize NI-DCPower with a logical name, this property contains
    the resource descriptor that corresponds to the entry in the IVI
    Configuration Utility. If you initialize NI-DCPower with the resource
    descriptor, this property contains that value.
    '''
    logical_name = attributes.AttributeViString(1050305)
    '''
    Contains the logical name you specified when opening the current IVI
    session.

    You can pass a logical name to the `niDCPower
    Initialize <NIDCPowerVIRef.chm::/niDCPower_Initialize.html>`__ or
    `niDCPower Initialize with
    Options <NIDCPowerVIRef.chm::/niDCPower_Initialize_With_Options.html>`__
    VIs. The IVI Configuration Utility must contain an entry for the logical
    name. The logical name entry refers to a virtual instrument section in
    the IVI configuration file. The virtual instrument section specifies a
    physical device and initial user settings.
    '''
    measure_buffer_size = attributes.AttributeViInt32(1150077)
    '''
    Specifies the number of samples that the active channel measurement
    buffer can hold.

    **The Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    **Valid Range**: 1000 to 2147483647

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    measure_complete_event_delay = attributes.AttributeViReal64(1150046)
    '''
    Specifies the amount of time to delay the generation of the Measure
    Complete event, in seconds.

    The NI PXI-4132 and NI PXIe-4140/4141/4142/4143/4144/4145/4154 support
    values from 0 seconds to 167 seconds.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    measure_complete_event_output_terminal = attributes.AttributeViString(1150047)
    '''
    Specifies the output terminal for exporting the Measure Complete event.

    Output terminals can be specified in one of two ways. If the device is
    named Dev1 and your terminal is PXI_Trig0, you can specify the terminal
    with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the
    shortened terminal name, PXI_Trig0.

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    measure_complete_event_pulse_polarity = attributes.AttributeEnum(attributes.AttributeViInt32, enums.Polarity, 1150044)
    '''
    Specifies the behavior of the Measure Complete event.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    measure_complete_event_pulse_width = attributes.AttributeViReal64(1150045)
    '''
    Specifies the width of the Measure Complete event, in seconds.

    The minimum event pulse width value for the NI PXI-4132 is 150 ns, and
    the minimum event pulse width value for PXI Express devices is 250 ns.

    The maximum event pulse width value for all devices is 1.6 microseconds.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    measure_record_delta_time = attributes.AttributeViReal64(1150065)
    '''
    Queries the amount of time, in seconds, between the start of two
    consecutive measurements in a measure record. Only query this property
    after the desired measurement settings are committed.

    Note:
    This property is not available when the `Auto
    Zero <pniDCPower_AutoZero.html>`__ property is set to **Once** because
    the amount of time between the first two measurements and the rest would
    differ.
    '''
    measure_record_length = attributes.AttributeViInt32(1150063)
    '''
    Specifies how many measurements compose a measure record. When this
    property is set to a value greater than 1, the `Measure
    When <pniDCPower_MeasureWhen.html>`__ property must be set to
    **Automatically after Source Complete** or **On Measure Trigger**.

    **Valid Values**: 1 to 16,777,216

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    Note: This property is not available in a session involving multiple channels.
    '''
    measure_record_length_is_finite = attributes.AttributeViBoolean(1150064)
    '''
    Specifies whether to take continuous measurements. Call the `niDCPower
    Abort <NIDCPowerVIRef.chm::/niDCPower_Abort.html>`__ VI to stop
    continuous measurements. When this property is set to FALSE and the
    `Source Mode <pniDCPower_SourceMode.html>`__ property is set to **Single
    Point**, the `Measure When <pniDCPower_MeasureWhen.html>`__ property
    must be set to **Automatically after Source Complete** or **On Measure
    Trigger**. When this property is set to FALSE and the Source Mode
    property is set to **Sequence**, the Measure When property must be set
    to **On Measure Trigger**.

    **Default Value**: TRUE

    Note: This property is not available in a session involving multiple channels.
    '''
    measure_trigger_type = attributes.AttributeEnum(attributes.AttributeViInt32, enums.TriggerType, 1150034)
    '''
    Specifies the behavior of the Measure trigger.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    **Related topics:**

    `Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    measure_when = attributes.AttributeEnum(attributes.AttributeViInt32, enums.MeasureWhen, 1150057)
    '''
    Specifies when the measure unit should acquire measurements. Unless this
    property is configured to **On Measure Trigger**, the `Measure Trigger
    Type <pniDCPower_MeasureTriggerType.html>`__ property is ignored.

    Refer to the `Acquiring
    Measurements <NI_DC_Power_Supplies_Help.chm::/AcquiringMeasurements.html>`__
    topic in the *NI DC Power Supplies and SMUs Help* for more information
    about how to configure your measurements.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.
    '''
    output_capacitance = attributes.AttributeEnum(attributes.AttributeViInt32, enums.OutputCapacitance, 1150014)
    '''
    Specifies whether to use a low or high capacitance on the output for the
    specified channel(s).

    Refer to the `NI PXI-4130 Output Capacitance
    Selection <NI_DC_Power_Supplies_Help.chm::/4130_Output_Cap_Select.html>`__
    topic in the *NI DC Power Supplies and SMUs Help* for more information
    about capacitance.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    **Related topics:**

    `Output
    Capacitance <NI_DC_Power_Supplies_Help.chm::/Capacitance.html>`__

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    output_connected = attributes.AttributeViBoolean(1150060)
    '''
    Specifies whether the output relay is connected (closed) or disconnected
    (open). The `Output Enabled <pniDCPower_OutputEnabled.html>`__ property
    does not change based on this property; they are independent of each
    other.

    Set this property to FALSE to disconnect the output terminal from the
    output.

    **Default Value**: Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    Note:
    Only disconnect the output when disconnecting is necessary for your
    application. For example, a battery connected to the output terminal
    might discharge unless the relay is disconnected. Excessive connecting
    and disconnecting of the output can cause premature wear on
    electromechanical relays, such as those used by the NI PXI-4132 or NI
    PXIe-4138/39.
    '''
    output_enabled = attributes.AttributeViBoolean(1250006)
    '''
    Specifies whether the output is enabled (TRUE) or disabled (FALSE).

    Depending on the value you specify for the `Output
    Function <pniDCPower_OutputFunction.html>`__ property, you also must set
    the voltage level or current level in addition to enabling the output.

    This property has no effect on the output disconnect relay. To toggle
    the relay, use the `Output
    Connected <pniDCPower_OutputConnected.html>`__ property.

    **Default Value**: Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    Note:
    If the session is in the Committed or Uncommitted states, enabling the
    output does not take effect until you call the `niDCPower
    Initiate <NIDCPowerVIRef.chm::/niDCPower_Initiate.html>`__ VI. Refer to
    the `Programming
    States <NI_DC_Power_Supplies_Help.chm::/programmingStates.html>`__ topic
    in the *NI DC Power Supplies and SMUs Help* for more information about
    NI-DCPower programming states.
    '''
    output_function = attributes.AttributeEnum(attributes.AttributeViInt32, enums.OutputFunction, 1150008)
    '''
    Configures the function to generate on the specified channel(s).

    When **DC Voltage** is selected, the device generates the desired
    voltage level on the output as long as the output current is below the
    current limit. You can use the following properties to configure the
    channel when **DC Voltage** is selected:

    `Voltage Level <pniDCPower_VoltageLevel.html>`__ `Current
    Limit <pniDCPower_CurrentLimit.html>`__ `Voltage Level
    Range <pniDCPower_VoltageLevelRange.html>`__ `Current Limit
    Range <pniDCPower_CurrentLimitRange.html>`__

    When **DC Current** is selected, the device generates the desired
    current level on the output as long as the output voltage is below the
    voltage limit. You can use the following properties to configure the
    channel when **DC Current** is selected:

    `Current Level <pniDCPower_CurrentLevel.html>`__ `Voltage
    Limit <pniDCPower_VoltageLimit.html>`__ `Current Level
    Range <pniDCPower_CurrentLevelRange.html>`__ `Voltage Limit
    Range <pniDCPower_VoltageLimitRange.html>`__

    **Default Value**: Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    **Related topics:**

    `Constant Voltage
    Mode <NI_DC_Power_Supplies_Help.chm::/Constant_Voltage.html>`__

    `Constant Current
    Mode <NI_DC_Power_Supplies_Help.chm::/Constant_Current.html>`__
    '''
    output_resistance = attributes.AttributeViReal64(1150061)
    '''
    Specifies the output resistance that the device attempts to generate for
    the specified channel(s). This property is available only when you set
    the `Output Function <pniDCPower_OutputFunction.html>`__ property to
    **DC Voltage**. Refer to `NI PXIe-4154 Programmable Output
    Resistance <NI_DC_Power_Supplies_Help.chm::/4154_Prog_Output_Resist.html>`__
    for more information about selecting an output resistance.

    **Valid Values**: Vary by device. Refer to the device specifications or
    the Programmable Output Resistance topic for your device for more
    information about supported values.

    **Default Value**: Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    overranging_enabled = attributes.AttributeViBoolean(1150007)
    '''
    Specifies whether NI-DCPower allows setting the `voltage
    level <NIDCPowerVIRef.chm::/niDCPower_Configure_Voltage_Level.html>`__,
    `current
    level <NIDCPowerVIRef.chm::/niDCPower_Configure_Current_Level.html>`__,
    `voltage
    limit <NIDCPowerVIRef.chm::/niDCPower_Configure_Voltage_Limit.html>`__,
    and `current
    limit <NIDCPowerVIRef.chm::/niDCPower_Configure_Current_Limit.html>`__
    outside the device specification limits. TRUE means that overranging is
    enabled.

    Refer to the `Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
    topic in the *NI DC Power Supplies and SMUs Help* for more information
    about overranging.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    **Related topics:**

    `Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
    '''
    ovp_enabled = attributes.AttributeViBoolean(1250002)
    '''
    Enables (TRUE) or disables (FALSE) overvoltage protection (OVP).

    Refer to `Output Overvoltage
    Protection <NI_DC_Power_Supplies_Help.chm::/OutputOvervoltageProtection.html>`__
    for more information about overvoltage protection.

    **Defined Values**

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    **Related topics:**

    `NI PXIe-4154
    Protection <NI_DC_Power_Supplies_Help.chm::/4154_Protection.html>`__

    `PXIe-4135
    Protection <NI_DC_Power_Supplies_Help.chm::/4135_Protection.html>`__

    `NI PXIe-4136/4137
    Protection <NI_DC_Power_Supplies_Help.chm::/4136_4137_Protection.html>`__

    `Output Overvoltage
    Protection <NI_DC_Power_Supplies_Help.chm::/OutputOvervoltageProtection.html>`__

    +-------+-------------------------------------+
    | FALSE | Overvoltage protection is disabled. |
    +-------+-------------------------------------+
    | TRUE  | Overvoltage protection is enabled.  |
    +-------+-------------------------------------+

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    ovp_limit = attributes.AttributeViReal64(1250003)
    '''
    Determines the voltage limit, in volts, beyond which overvoltage
    protection (OVP) engages. Limit is specified as a positive value, but
    symmetric positive and negative limits are enforced simultaneously. For
    example, setting the OVP Limit to 65 will configure the OVP feature to
    trigger an OVP error if the output exceeds ±65 V.

    **Valid Values**:Vary by device.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    **Related topics:**

    `PXIe-4135
    Protection <NI_DC_Power_Supplies_Help.chm:://4135_Protection.html>`__

    `NI PXIe-4136/4137
    Protection <NI_DC_Power_Supplies_Help.chm::/4136_4137_Protection.html>`__

    Note:
    Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    power_line_frequency = attributes.AttributeEnum(attributes.AttributeViReal64, enums.PowerLineFrequency, 1150020)
    '''
    Specifies the power line frequency for specified channel(s). NI-DCPower
    uses this value to select a timebase for setting the `Aperture
    Time <pniDCPower_ApertureTime.html>`__ property in power line cycles
    (PLCs).

    Refer to the following topics for more information about how to
    configure your measurements:

    `NI PXIe-4112 Measurement Configuration and
    Timing <NI_DC_Power_Supplies_Help.chm::/4112_MeasureConfigTiming.html>`__
    `NI PXIe-4113 Measurement Configuration and
    Timing <NI_DC_Power_Supplies_Help.chm::/4113_MeasureConfigTiming.html>`__
    `NI PXI-4132 Measurement Configuration and
    Timing <NI_DC_Power_Supplies_Help.chm::/4132_MeasureConfigTiming.html>`__
    `Measurement Noise
    Rejection <NI_DC_Power_Supplies_Help.chm::/noiseRejectMeasure.html>`__

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    **Related topics:**

    `Measurement Noise
    Rejection <NI_DC_Power_Supplies_Help.chm::/NoiseRejectMeasure.html>`__

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    power_source = attributes.AttributeEnum(attributes.AttributeViInt32, enums.PowerSource, 1150000)
    '''
    Specifies the power source to use. NI-DCPower switches the power source
    used by the device to the specified value.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    **Related topics:**

    `NI PXI-4110 Internal and Auxiliary
    Power <NI_DC_Power_Supplies_Help.chm::/4110_Internal_Auxiliary_Power.html>`__

    `NI PXI-4130 Internal and Auxiliary
    Power <NI_DC_Power_Supplies_Help.chm::/4130_Internal_Auxiliary_Power.html>`__

    Note:
    Automatic selection is not persistent and occurs only at the time this
    property is set to **Automatic**. However, if the session is in the
    `Committed or
    Uncommitted <NI_DC_Power_Supplies_Help.chm::/programmingStates.html>`__
    state when you set this property, the power source selection only occurs
    after you call the `niDCPower
    Initiate <NIDCPowerVIRef.chm::/niDCPower_Initiate.html>`__ VI.
    '''
    power_source_in_use = attributes.AttributeEnum(attributes.AttributeViInt32, enums.PowerSourceInUse, 1150001)
    '''
    Indicates whether the device is using the internal or auxiliary power
    source to generate power.
    '''
    pulse_bias_current_level = attributes.AttributeViReal64(1150088)
    '''
    Specifies the pulse bias current level, in amps, that the device
    attempts to generate on the specified channel(s) during the off phase of
    a pulse.

    This property is applicable only if the `Output
    Function <pniDCPower_OutputFunction.html>`__ property is set to **Pulse
    Current**.

    **Valid Values:** The valid values for this property are defined by the
    values you specify for the `Pulse Current Level
    Range <pniDCPower_PulseCurrentLevelRange.html>`__ property.

    Note:
    Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    pulse_bias_current_limit = attributes.AttributeViReal64(1150083)
    '''
    Specifies the pulse bias current limit, in amps, that the output cannot
    exceed when generating the desired pulse bias voltage on the specified
    channel(s) during the off phase of a pulse. Limit is specified as a
    positive value, but symmetric positive and negative limits are enforced
    simultaneously.

    This property is applicable only if the `Output
    Function <pniDCPower_OutputFunction.html>`__ property is set to **Pulse
    Voltage**.

    **Valid Values:** The valid values for this property are defined by the
    values you specify for the `Pulse Current Limit
    Range <pniDCPower_PulseCurrentLimitRange.html>`__ property.

    Note:
    Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    pulse_bias_delay = attributes.AttributeViReal64(1150092)
    '''
    Determines when, in seconds, the device generates the Pulse Complete
    event after generating the off level of a pulse.

    **Valid Values**: 0 to 167 seconds

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    Note:
    Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    pulse_bias_voltage_level = attributes.AttributeViReal64(1150082)
    '''
    Specifies the pulse bias voltage level, in volts, that the device
    attempts to generate on the specified channel(s) during the off phase of
    a pulse.

    This property is applicable only if the `Output
    Function <pniDCPower_OutputFunction.html>`__ property is set to **Pulse
    Voltage**.

    **Valid Values:** The valid values for this property are defined by the
    values you specify for the `Pulse Voltage Level
    Range <pniDCPower_PulseVoltageLevelRange.html>`__ property.

    Note:
    Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    pulse_bias_voltage_limit = attributes.AttributeViReal64(1150089)
    '''
    Specifies the pulse voltage limit, in volts, that the output cannot
    exceed when generating the desired current on the specified channel(s)
    during the off phase of a pulse. Limit is specified as a positive value,
    but symmetric positive and negative limits are enforced simultaneously.

    This property is applicable only if the `Output
    Function <pniDCPower_OutputFunction.html>`__ property is set to **Pulse
    Current**.

    **Valid Values:** The valid values for this property are defined by the
    values you specify for the `Pulse Voltage Limit
    Range <pniDCPower_PulseVoltageLimitRange.html>`__ property.

    Note:
    Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    pulse_complete_event_output_terminal = attributes.AttributeViString(1150099)
    '''
    Specifies the output terminal for exporting the Pulse Complete event.

    Output terminals can be specified in one of two ways. If the device is
    named Dev1 and your terminal is PXI_Trig0, you can specify the terminal
    with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the
    shortened terminal name, PXI_Trig0.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    pulse_complete_event_pulse_polarity = attributes.AttributeEnum(attributes.AttributeViInt32, enums.Polarity, 1150100)
    '''
    Specifies the behavior of the Pulse Complete event.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    pulse_complete_event_pulse_width = attributes.AttributeViReal64(1150101)
    '''
    Specifies the width of the Pulse Complete event, in seconds.

    The minimum event pulse width value for PXI Express devices is 250 ns.

    The maximum event pulse width value for all devices is 1.6 microseconds.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    pulse_current_level = attributes.AttributeViReal64(1150086)
    '''
    Specifies the pulse current level, in amps, that the device attempts to
    generate on the specified channel(s) during the on phase of a pulse.

    This property is applicable only if the `Output
    Function <pniDCPower_OutputFunction.html>`__ property is set to **Pulse
    Current**.

    **Valid Values:** The valid values for this property are defined by the
    values you specify for the `Pulse Current Level
    Range <pniDCPower_PulseCurrentLevelRange.html>`__ property.

    Note:
    Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    pulse_current_level_range = attributes.AttributeViReal64(1150090)
    '''
    Specifies the pulse current level range, in amps, for the specified
    channel(s).

    The range defines the valid values to which you can set the **pulse
    current level** and **pulse bias current level**.

    The Pulse Current Level Range property is applicable only if the `Output
    Function <pniDCPower_OutputFunction.html>`__ property is set to **Pulse
    Current**.

    For valid ranges for your device, refer to
    `Ranges <NI_DC_Power_Supplies_Help.chm::/Ranges.html>`__.

    Note:
    Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    pulse_current_limit = attributes.AttributeViReal64(1150081)
    '''
    Specifies the pulse current limit, in amps, that the output cannot
    exceed when generating the desired pulse voltage on the specified
    channel(s) during the on phase of a pulse. Limit is specified as a
    positive value, but symmetric positive and negative limits are enforced
    simultaneously.

    This property is applicable only if the `Output
    Function <pniDCPower_OutputFunction.html>`__ property is set to **Pulse
    Voltage**.

    **Valid Values:** The valid values for this property are defined by the
    values you specify for the `Pulse Current Limit
    Range <pniDCPower_PulseCurrentLimitRange.html>`__ property.

    Note:
    Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    pulse_current_limit_range = attributes.AttributeViReal64(1150085)
    '''
    Specifies the pulse current limit range, in amps, for the specified
    channel(s).

    The range defines the valid values to which you can set the **pulse
    current limit** and **pulse bias current limit**.

    This property is applicable only if the `Output
    Function <pniDCPower_OutputFunction.html>`__ property is set to **Pulse
    Voltage**.

    For valid ranges for your device, refer to
    `Ranges <NI_DC_Power_Supplies_Help.chm::/Ranges.html>`__.

    Note:
    Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    pulse_off_time = attributes.AttributeViReal64(1150094)
    '''
    Determines the length, in seconds, of the off phase of a pulse.

    **Valid Values**: 50 microseconds to 167 seconds

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    Note:
    Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    pulse_on_time = attributes.AttributeViReal64(1150093)
    '''
    Determines the length, in seconds, of the on phase of a pulse.

    **Valid Values**:50 microseconds to 167 seconds

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    Note:
    Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    pulse_trigger_type = attributes.AttributeEnum(attributes.AttributeViInt32, enums.TriggerType, 1150095)
    '''
    Specifies the behavior of the Pulse trigger.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    **Related topics:**

    `Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    pulse_voltage_level = attributes.AttributeViReal64(1150080)
    '''
    Specifies the pulse voltage level, in volts, that the device attempts to
    generate on the specified channel(s) during the on phase of a pulse.

    This property is applicable only if the `Output
    Function <pniDCPower_OutputFunction.html>`__ property is set to **Pulse
    Voltage**.

    **Valid Values:** The valid values for this property are defined by the
    values you specify for the `Pulse Voltage Level
    Range <pniDCPower_PulseVoltageLevelRange.html>`__ property.

    Note:
    Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    pulse_voltage_level_range = attributes.AttributeViReal64(1150084)
    '''
    Specifies the pulse voltage level range, in volts, for the specified
    channel(s).

    The range defines the valid values at which you can set the **pulse
    voltage level** and **pulse bias voltage level**.

    This property is applicable only if the `Output
    Function <pniDCPower_OutputFunction.html>`__ property is set to **Pulse
    Voltage**.

    For valid ranges for your device, refer to
    `Ranges <NI_DC_Power_Supplies_Help.chm::/Ranges.html>`__.

    Note:
    Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    pulse_voltage_limit = attributes.AttributeViReal64(1150087)
    '''
    Specifies the pulse voltage limit, in volts, that the output cannot
    exceed when generating the desired pulse current on the specified
    channel(s) during the on phase of a pulse. Limit is specified as a
    positive value, but symmetric positive and negative limits are enforced
    simultaneously.

    This property is applicable only if the `Output
    Function <pniDCPower_OutputFunction.html>`__ property is set to **Pulse
    Current**.

    **Valid Values:** The valid values for this property are defined by the
    values you specify for the `Pulse Voltage Limit
    Range <pniDCPower_PulseVoltageLimitRange.html>`__ property.

    Note:
    Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    pulse_voltage_limit_range = attributes.AttributeViReal64(1150091)
    '''
    Specifies the pulse voltage limit range, in volts, for the specified
    channel(s).

    The range defines the valid values to which you can set the **pulse
    voltage limit** and **pulse bias voltage limit**.

    This property is applicable only if the `Output
    Function <pniDCPower_OutputFunction.html>`__ property is set to **Pulse
    Current**.

    For valid ranges for your device, refer to
    `Ranges <NI_DC_Power_Supplies_Help.chm::/Ranges.html>`__.

    Note:
    The channel must be enabled for the specified pulse current limit to
    take effect. Refer to the `Output
    Enabled <pniDCPower_OutputEnabled.html>`__ property for more information
    about enabling the output channel.
    '''
    query_instrument_status = attributes.AttributeViBoolean(1050003)
    '''
    Specifies whether NI-DCPower queries the device status after each
    operation.

    Querying the device status is useful for debugging. After you validate
    your program, you can set this property to FALSE to disable status
    checking and maximize performance.

    NI-DCPower ignores status checking for particular properties regardless
    of the setting of this property.

    Use the `niDCPower Initialize with
    Options <NIDCPowerVIRef.chm::/niDCPower_Initialize_With_Options.html>`__
    VI to override this value.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.
    '''
    range_check = attributes.AttributeViBoolean(1050002)
    '''
    Specifies whether to validate property values and VI parameters.

    If this property is enabled, NI-DCPower validates the parameter values
    that you pass to NI-DCPower VIs. Range-checking parameters is useful for
    debugging. After you validate your program, you can set this property to
    FALSE to disable range checking and maximize performance.

    Use the `niDCPower Initialize with
    Options <NIDCPowerVIRef.chm::/niDCPower_Initialize_With_Options.html>`__
    VI to override the default value.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.
    '''
    ready_for_pulse_trigger_event_output_terminal = attributes.AttributeViString(1150102)
    '''
    Specifies the output terminal for exporting the Ready For Pulse Trigger
    event.

    Output terminals can be specified in one of two ways. If the device is
    named Dev1 and your terminal is PXI_Trig0, you can specify the terminal
    with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the
    shortened terminal name, PXI_Trig0.

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    ready_for_pulse_trigger_event_pulse_polarity = attributes.AttributeEnum(attributes.AttributeViInt32, enums.Polarity, 1150103)
    '''
    Specifies the behavior of the Ready For Pulse Trigger event.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    ready_for_pulse_trigger_event_pulse_width = attributes.AttributeViReal64(1150104)
    '''
    Specifies the width of the Ready For Pulse Trigger event, in seconds.

    The minimum event pulse width value for PXI Express devices is 250 ns.

    The maximum event pulse width value for all devices is 1.6 microseconds.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    record_coercions = attributes.AttributeViBoolean(1050006)
    '''
    Specifies whether the IVI engine records the value coercions it makes
    for ViInt32 and ViReal64 properties.

    Call the `niDCPower Get Next Coercion
    Record <NIDCPowerVIRef.chm::/niDCPower_Get_Next_Coercion_Record.html>`__
    VI to read and delete the earliest coercion record from the list.

    Use the `niDCPower Initialize with
    Options <NIDCPowerVIRef.chm::/niDCPower_Initialize_With_Options.html>`__
    VI to override this value.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.
    '''
    reset_average_before_measurement = attributes.AttributeViBoolean(1150006)
    '''
    Specifies whether the measurement returned from any measurement call
    starts with a new measurement call (TRUE) or returns a measurement that
    has already begun or completed (FALSE).

    When you set the `Samples to
    Average <pniDCPower_SamplesToAverage.html>`__ property in the `Running
    state <NI_DC_Power_Supplies_Help.chm::/programmingStates.html>`__, the
    output channel measurements might move out of synchronization. While
    NI-DCPower automatically synchronizes measurements upon the
    initialization of a session, you can force a synchronization in the
    running state before you run the `niDCPower Measure
    Multiple <NIDCPowerVIRef.chm::/niDCPower_Measure_Multiple.html>`__ VI.
    To force a synchronization in the running state, set the Reset Average
    Before Measurement property to TRUE, and then run the niDCPower Measure
    Multiple VI specifying all channels in the **channel name** parameter.
    You can set the Reset Average Before Measurement property to FALSE after
    the niDCPower Measure Multiple VI completes.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    samples_to_average = attributes.AttributeViInt32(1150003)
    '''
    Specifies the number of samples to average when you take a measurement.

    Increasing the number of samples to average decreases measurement noise
    but increases the time required to take a measurement. Refer to the `NI
    PXI-4110 <NI_DC_Power_Supplies_Help.chm::/4110_Measure_Avg.html>`__, `NI
    PXI-4130 <NI_DC_Power_Supplies_Help.chm::/4130_Measure_Avg.html>`__, `NI
    PXI-4132 <NI_DC_Power_Supplies_Help.chm::/4132_Measure_Avg.html>`__, or
    `NI PXIe-4154 <NI_DC_Power_Supplies_Help.chm::/4154_Measure_Avg.html>`__
    averaging topic for optional property settings to improve immunity to
    certain noise types. For information about improving noise immunity for
    NI-DCPower devices that support DC noise rejection, refer to
    `Measurement Noise
    Rejection <NI_DC_Power_Supplies_Help.chm::/noiseRejectMeasure.html>`__

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    **Related topics:**

    `Measurement Noise
    Rejection <NI_DC_Power_Supplies_Help.chm::/NoiseRejectMeasure.html>`__

    +---------------------------------------+---------------------------------+
    | **Device**                            | **Range of Samples to Average** |
    +---------------------------------------+---------------------------------+
    | NI PXI-4110 and NI PXI-4130           | 1 to 511                        |
    +---------------------------------------+---------------------------------+
    | NI PXI-4132                           | 1 to 127                        |
    +---------------------------------------+---------------------------------+
    | NI PXIe-4112/4113                     | 1                               |
    +---------------------------------------+---------------------------------+
    | PXIe-4135                             | 1                               |
    +---------------------------------------+---------------------------------+
    | NI PXIe-4136/4137                     | 1                               |
    +---------------------------------------+---------------------------------+
    | NI PXIe-4138/4139                     | 1                               |
    +---------------------------------------+---------------------------------+
    | NI PXIe-4140/4141/4142/4143/4144/4145 | 1                               |
    +---------------------------------------+---------------------------------+
    | NI PXIe-4154                          | 1 to 65,535                     |
    +---------------------------------------+---------------------------------+
    | PXIe-4162/4163                        | 1                               |
    +---------------------------------------+---------------------------------+
    '''
    self_calibration_persistence = attributes.AttributeEnum(attributes.AttributeViInt32, enums.SelfCalibrationPersistence, 1150073)
    '''
    Specifies whether the values calculated during self-calibration should
    be written to hardware to be used until the next self-calibration or
    only used until the `niDCPower Reset
    Device <NIDCPowerVIRef.chm::/niDCPower_Reset_Device.html>`__ VI is
    called or the machine is powered down.

    This property affects the behavior of the `niDCPower Cal Self
    Calibrate <NIDCPowerVIRef.chm::/niDCPower_Cal_Self_Calibrate.html>`__
    VI. When set to **Keep in Memory**, the values calculated by the
    niDCPower Cal Self Calibrate VI are used in the existing session, as
    well as in all further sessions until you call the niDCPower Reset
    Device VI or restart the machine. When you set this property to **Write
    to EEPROM**, the values calculated by the niDCPower Cal Self Calibrate
    VI are written to hardware and used in the existing session and in all
    subsequent sessions until another call to the niDCPower Cal Self
    Calibrate VI is made.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    **Related topics:**

    `Self-Calibration <NI_DC_Power_Supplies_Help.chm::/selfcal.html>`__

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    sense = attributes.AttributeEnum(attributes.AttributeViInt32, enums.Sense, 1150013)
    '''
    Selects either local or remote sensing of the output voltage for the
    specified channel(s).

    Refer to the `Local and Remote
    Sense <NI_DC_Power_Supplies_Help.chm::/local_and_remote_sense.html>`__
    topic in the *NI DC Power Supplies and SMUs Help* for more information
    about sensing voltage on supported channels and about devices that
    support local and/or remote sensing.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    **Related topics:**

    `Local and Remote
    Sense <NI_DC_Power_Supplies_Help.chm::/local_and_remote_sense.html>`__
    '''
    sequence_advance_trigger_type = attributes.AttributeEnum(attributes.AttributeViInt32, enums.TriggerType, 1150026)
    '''
    Specifies the behavior of the Sequence Advance trigger.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    **Related topics:**

    `Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    sequence_engine_done_event_output_terminal = attributes.AttributeViString(1150050)
    '''
    Specifies the output terminal for exporting the Sequence Engine Done
    Complete event.

    Output terminals can be specified in one of two ways. If the device is
    named Dev1 and your terminal is PXI_Trig0, you can specify the terminal
    with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the
    shortened terminal name, PXI_Trig0.

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    sequence_engine_done_event_pulse_polarity = attributes.AttributeEnum(attributes.AttributeViInt32, enums.Polarity, 1150048)
    '''
    Specifies the behavior of the Sequence Engine Done event.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    sequence_engine_done_event_pulse_width = attributes.AttributeViReal64(1150049)
    '''
    Specifies the width of the Sequence Engine Done event, in seconds.

    The minimum event pulse width value for the NI PXI-4132 is 150 ns, and
    the minimum event pulse width value for PXI Express devices is 250 ns.

    The maximum event pulse width value for all devices is 1.6 microseconds.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    sequence_iteration_complete_event_output_terminal = attributes.AttributeViString(1150040)
    '''
    Specifies the output terminal for exporting the Sequence Iteration
    Complete event.

    Output terminals can be specified in one of two ways. If the device is
    named Dev1 and your terminal is PXI_Trig0, you can specify the terminal
    with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the
    shortened terminal name, PXI_Trig0.

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    sequence_iteration_complete_event_pulse_polarity = attributes.AttributeEnum(attributes.AttributeViInt32, enums.Polarity, 1150038)
    '''
    Specifies the behavior of the Sequence Iteration Complete event.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    sequence_iteration_complete_event_pulse_width = attributes.AttributeViReal64(1150039)
    '''
    Specifies the width of the Sequence Iteration Complete event, in
    seconds.

    The minimum event pulse width value for the NI PXI-4132 is 150 ns, and
    the minimum event pulse width value for PXI Express devices is 250 ns.

    The maximum event pulse width value for all devices is 1.6 microseconds.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    sequence_loop_count = attributes.AttributeViInt32(1150025)
    '''
    Specifies the number of times a sequence is run after initiation.

    Refer to the `Sequence Source
    Mode <NI_DC_Power_Supplies_Help.chm::/Sequencing.html>`__ topic in the
    *NI DC Power Supplies and SMUs Help* for more information about the
    sequence loop count.

    **Valid Range**: 1 to 134217727

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices. When the `Sequence Loop Count Is
    Finite <pniDCPower_SequenceLoopCountIsFinite.html>`__ property is set to
    FALSE, the Sequence Loop Count property is ignored.
    '''
    sequence_loop_count_is_finite = attributes.AttributeViBoolean(1150078)
    '''
    Specifies whether a sequence should repeat indefinitely.

    Refer to the `Sequence Source
    Mode <NI_DC_Power_Supplies_Help.chm::/Sequencing.html>`__ topic in the
    *NI DC Power Supplies and SMUs Help* for more information about infinite
    sequencing.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices. When the Sequence Loop Count Is
    Finite property is set to FALSE, the `Sequence Loop
    Count <pniDCPower_SequenceLoopCount.html>`__ property is ignored.
    '''
    simulate = attributes.AttributeViBoolean(1050005)
    '''
    Specifies whether to simulate NI-DCPower I/O operations. TRUE specifies
    that operation is simulated.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.
    '''
    source_complete_event_output_terminal = attributes.AttributeViString(1150043)
    '''
    Specifies the output terminal for exporting the Source Complete event.

    Output terminals can be specified in one of two ways. If the device is
    named Dev1 and your terminal is PXI_Trig0, you can specify the terminal
    with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the
    shortened terminal name, PXI_Trig0.

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    source_complete_event_pulse_polarity = attributes.AttributeEnum(attributes.AttributeViInt32, enums.Polarity, 1150041)
    '''
    Specifies the behavior of the Source Complete event.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    source_complete_event_pulse_width = attributes.AttributeViReal64(1150042)
    '''
    Specifies the width of the Source Complete event, in seconds.

    The minimum event pulse width value for the NI PXI-4132 is 150 ns, and
    the minimum event pulse width value for PXI Express devices is 250 ns.

    The maximum event pulse width value for all devices is 1.6 microseconds.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    source_delay = attributes.AttributeViReal64(1150051)
    '''
    Determines when, in seconds, the device generates the Source Complete
    event, potentially starting a measurement if the `Measure
    When <pniDCPower_MeasureWhen.html>`__ property is set to **Automatically
    After Source Complete**.

    Refer to the `Single Point source
    mode <NI_DC_Power_Supplies_Help.chm::/Singlept.html>`__ and `Sequence
    source mode <NI_DC_Power_Supplies_Help.chm::/Sequencing.html>`__ topics
    in the *NI DC Power Supplies and SMUs Help* for more information.

    **Valid Values**: For PXIe-4162/4163, 0-10 seconds, for all other
    supported devices, 0 to 167 seconds

    **Default Value**: Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    **Related topics:**

    `Settling Time <NI_DC_Power_Supplies_Help.chm::/SettlingTime.html>`__

    Note:
    Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    source_mode = attributes.AttributeEnum(attributes.AttributeViInt32, enums.SourceMode, 1150054)
    '''
    Specifies whether to run a single output point or a sequence. Refer to
    the `Single Point source
    mode <NI_DC_Power_Supplies_Help.chm::/Singlept.html>`__ and `Sequence
    source mode <NI_DC_Power_Supplies_Help.chm::/Sequencing.html>`__ topics
    in the *NI DC Power Supplies and SMUs Help* for more information about
    source modes.

    **Default Value**: Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.
    '''
    source_trigger_type = attributes.AttributeEnum(attributes.AttributeViInt32, enums.TriggerType, 1150030)
    '''
    Specifies the behavior of the Source trigger.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    **Related topics:**

    `Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    specific_driver_class_spec_major_version = attributes.AttributeViInt32(1050515)
    '''
    Contains the major version number of the class specification with which
    NI-DCPower is compliant.
    '''
    specific_driver_class_spec_minor_version = attributes.AttributeViInt32(1050516)
    '''
    Contains the minor version number of the class specification with which
    NI-DCPower is compliant.
    '''
    specific_driver_description = attributes.AttributeViString(1050514)
    '''
    Contains a brief description of the specific driver.
    '''
    specific_driver_prefix = attributes.AttributeViString(1050302)
    '''
    Contains the prefix for NI-DCPower. The name of each user-callable VI in
    NI-DCPower begins with this prefix.
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

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    **Related topics:**

    `Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    supported_instrument_models = attributes.AttributeViString(1050327)
    '''
    Contains a comma-separated (,) list of supported NI-DCPower device
    models.
    '''
    transient_response = attributes.AttributeEnum(attributes.AttributeViInt32, enums.TransientResponse, 1150062)
    '''
    Specifies the transient response. Refer to the `Transient
    Response <NI_DC_Power_Supplies_Help.chm::/Transient_Response.html>`__
    topic in the *NI DC Power Supplies and SMUs Help* for more information
    about transient response.

    **Default Value**: Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    **Related topics:**

    `Transient
    Response <NI_DC_Power_Supplies_Help.chm::/Transient_Response.html>`__

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    voltage_compensation_frequency = attributes.AttributeViReal64(1150068)
    '''
    The frequency at which a pole-zero pair is added to the system when the
    channel is in `Constant
    Voltage <NI_DC_Power_Supplies_Help.chm::/Constant_Voltage.html>`__ mode.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    voltage_gain_bandwidth = attributes.AttributeViReal64(1150067)
    '''
    The frequency at which the unloaded loop gain extrapolates to 0 dB in
    the absence of additional poles and zeroes. This property takes effect
    when the channel is in `Constant
    Voltage <NI_DC_Power_Supplies_Help.chm::/Constant_Voltage.html>`__ mode.

    **Default Value**: Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''
    voltage_level = attributes.AttributeViReal64(1250001)
    '''
    Specifies the voltage level, in volts, that the device attempts to
    generate on the specified channel(s).

    This property is applicable only if the `Output
    Function <pniDCPower_OutputFunction.html>`__ property is set to **DC
    Voltage**.

    **Valid Values:** The valid values for this property are defined by the
    values you specify for the `Voltage Level
    Range <pniDCPower_VoltageLevelRange.html>`__ property.

    **Related topics:**

    `Constant Voltage
    Mode <NI_DC_Power_Supplies_Help.chm::/Constant_Voltage.html>`__

    Note:
    The channel must be enabled for the specified voltage level to take
    effect. Refer to the `Output Enabled <pniDCPower_OutputEnabled.html>`__
    property for more information about enabling the output channel.
    '''
    voltage_level_autorange = attributes.AttributeEnum(attributes.AttributeViInt32, enums.VoltageLevelAutorange, 1150015)
    '''
    Specifies whether NI-DCPower automatically selects the voltage level
    range based on the desired voltage level for the specified channel(s).

    If you set this property to **On**, NI-DCPower ignores any changes you
    make to the `Voltage Level Range <pniDCPower_VoltageLevelRange.html>`__
    property. If you change the Voltage Level Autorange property from **On**
    to **Off**, NI-DCPower retains the last value that the `Voltage Level
    Range <pniDCPower_VoltageLevelRange.html>`__ property was set to (or the
    default value if it was never set) and uses that value as the voltage
    level range.

    Refer to the `Voltage Level Range <pniDCPower_VoltageLevelRange.html>`__
    property for information about which range NI-DCPower automatically
    selects.

    The Voltage Level Autorange property is applicable only if the `Output
    Function <pniDCPower_OutputFunction.html>`__ property is set to **DC
    Voltage**.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    **Related topics:**

    `Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
    '''
    voltage_level_range = attributes.AttributeViReal64(1150005)
    '''
    Specifies the voltage level range, in volts, for the specified
    channel(s).

    The range defines the valid values to which the voltage level can be
    set. Use the `Voltage Level
    Autorange <pniDCPower_VoltageLevelAutorange.html>`__ property to enable
    automatic selection of the voltage level range.

    The Voltage Level Range property is applicable only if the `Output
    Function <pniDCPower_OutputFunction.html>`__ property is set to **DC
    Voltage**.

    For valid ranges for your device, refer to
    `Ranges <NI_DC_Power_Supplies_Help.chm::/Ranges.html>`__.

    **Related topics:**

    `Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__

    Note:
    The channel must be enabled for the specified voltage level range to
    take effect. Refer to the `Output
    Enabled <pniDCPower_OutputEnabled.html>`__ property for more information
    about enabling the output channel.
    '''
    voltage_limit = attributes.AttributeViReal64(1150010)
    '''
    Specifies the voltage limit, in volts, that the output cannot exceed
    when generating the desired current level on the specified channels.
    Limit is specified as a positive value, but symmetric positive and
    negative limits are enforced simultaneously.

    This property is applicable only if the `Output
    Function <pniDCPower_OutputFunction.html>`__ property is set to **DC
    Current**.

    **Valid Values:** The valid values for this attribute are defined by the
    values to which the `Voltage Limit
    Range <pniDCPower_VoltageLimitRange.html>`__ property is set.

    **Related topics:**

    `Compliance <NI_DC_Power_Supplies_Help.chm::/compliance.html>`__

    Note:
    The channel must be enabled for the specified current level to take
    effect. Refer to the `Output Enabled <pniDCPower_OutputEnabled.html>`__
    property for more information about enabling the output channel.
    '''
    voltage_limit_autorange = attributes.AttributeEnum(attributes.AttributeViInt32, enums.VoltageLimitAutorange, 1150018)
    '''
    Specifies whether NI-DCPower automatically selects the voltage limit
    range based on the desired voltage limit for the specified channel(s).

    If you set this property to **On**, NI-DCPower ignores any changes you
    make to the `Voltage Limit Range <pniDCPower_VoltageLimitRange.html>`__
    property. If you change the Voltage Limit Autorange property from **On**
    to **Off**, NI-DCPower retains the last value that the `Voltage Limit
    Range <pniDCPower_VoltageLimitRange.html>`__ property was set to (or the
    default value if it was never set) and uses that value as the voltage
    limit range.

    Refer to the `Voltage Limit Range <pniDCPower_VoltageLimitRange.html>`__
    property for information about which range NI-DCPower automatically
    selects.

    The Voltage Limit Autorange property is applicable only if the `Output
    Function <pniDCPower_OutputFunction.html>`__ property is set to **DC
    Current**.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    **Related topics:**

    `Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
    '''
    voltage_limit_range = attributes.AttributeViReal64(1150012)
    '''
    Specifies the voltage limit range, in volts, for the specified
    channel(s).

    The range defines the valid values to which the voltage limit can be
    set. Use the `Voltage Limit
    Autorange <pniDCPower_VoltageLimitAutorange.html>`__ property to enable
    automatic selection of the voltage limit range.

    The Voltage Limit Range property is applicable only if the `Output
    Function <pniDCPower_OutputFunction.html>`__ property is set to **DC
    Current**.

    For valid ranges for your device, refer to
    `Ranges <NI_DC_Power_Supplies_Help.chm::/Ranges.html>`__.

    **Related topics:**

    `Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__

    Note:
    The channel must be enabled for the specified voltage limit range to
    take effect. Refer to the `Output
    Enabled <pniDCPower_OutputEnabled.html>`__ property for more information
    about enabling the output channel.
    '''
    voltage_pole_zero_ratio = attributes.AttributeViReal64(1150069)
    '''
    The ratio of the pole frequency to the zero frequency when the channel
    is in `Constant
    Voltage <NI_DC_Power_Supplies_Help.chm::/Constant_Voltage.html>`__ mode.

    **Default Value**: Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    Note:
    This property is not supported by all devices. Refer to `Supported
    Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    information about supported devices.
    '''

    def __init__(self, repeated_capability):
        self._library = library_singleton.get()
        self._repeated_capability = repeated_capability
        self._encoding = 'windows-1251'

    def __setattr__(self, key, value):
        if self._is_frozen and key not in dir(self):
            raise TypeError("%r is a frozen class" % self)
        object.__setattr__(self, key, value)

    def get_error_description(self, error_code):
        '''get_error_description

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

    def configure_aperture_time(self, aperture_time, units):
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

        Args:
            channel_name (string): Specifies the output channel(s) to which this configuration value
                applies. Specify multiple channels by using a channel list or a channel
                range. A channel list is a comma (,) separated sequence of channel names
                (for example, 0,2 specifies channels 0 and 2). A channel range is a
                lower bound channel followed by a hyphen (-) or colon (:) followed by an
                upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
                In the Running state, multiple output channel configurations are
                performed sequentially based on the order specified in this parameter.
            aperture_time (float): Specifies the aperture time. Refer to the *Aperture Time* topic for your
                device in the *NI DC Power Supplies and SMUs Help* for more information.
            units (int): Specifies the units for **apertureTime**.
                **Defined Values**:

                +----------------------------------------+------------------------------+
                | NIDCPOWER_VAL_SECONDS (1028)           | Specifies seconds.           |
                +----------------------------------------+------------------------------+
                | NIDCPOWER_VAL_POWER_LINE_CYCLES (1029) | Specifies Power Line Cycles. |
                +----------------------------------------+------------------------------+
        '''
        error_code = self._library.niDCPower_ConfigureApertureTime(self._vi, self._repeated_capability.encode(self._encoding), aperture_time, units)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def fetch_multiple(self, timeout, count):
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

        Args:
            channel_name (string): Specifies the output channel(s) to which this configuration value
                applies. Specify multiple channels by using a channel list or a channel
                range. A channel list is a comma (,) separated sequence of channel names
                (for example, 0,2 specifies channels 0 and 2). A channel range is a
                lower bound channel followed by a hyphen (-) or colon (:) followed by an
                upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
                In the Running state, multiple output channel configurations are
                performed sequentially based on the order specified in this parameter.
            timeout (float): Specifies the maximum time allowed for this function to complete, in
                seconds. If the function does not complete within this time interval,
                NI-DCPower returns an error.

                Note:
                When setting the timeout interval, ensure you take into account any
                triggers so that the timeout interval is long enough for your
                application.
            count (int): Specifies the number of measurements to fetch.

        Returns:
            voltage_measurements (string): Returns an array of voltage measurements. Ensure that sufficient space
                has been allocated for the returned array.
            current_measurements (string): Returns an array of current measurements. Ensure that sufficient space
                has been allocated for the returned array.
            in_compliance (string): Returns an array of Boolean values indicating whether the output was in
                compliance at the time the measurement was taken. Ensure that sufficient
                space has been allocated for the returned array.
            actual_count (int): Indicates the number of measured values actually retrieved from the
                device.
        '''
        voltage_measurements_ctype = (visatype.ViChar * 1)()
        current_measurements_ctype = (visatype.ViChar * 1)()
        in_compliance_ctype = (visatype.ViChar * 1)()
        actual_count_ctype = visatype.ViInt32(0)
        error_code = self._library.niDCPower_FetchMultiple(self._vi, self._repeated_capability.encode(self._encoding), timeout, count, voltage_measurements_ctype, current_measurements_ctype, in_compliance_ctype, ctypes.pointer(actual_count_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return voltage_measurements_ctype.value.decode(self._encoding), current_measurements_ctype.value.decode(self._encoding), in_compliance_ctype.value.decode(self._encoding), int(actual_count_ctype.value)

    def _get_attribute_vi_boolean(self, attribute_id):
        '''_get_attribute_vi_boolean

        | Queries the value of a ViBoolean attribute.
        | You can use this function to get the values of device-specific
          attributes and inherent IVI attributes.

        Args:
            channel_name (string): Specifies the output channel(s) to which this configuration value
                applies. Specify multiple channels by using a channel list or a channel
                range. A channel list is a comma (,) separated sequence of channel names
                (for example, 0,2 specifies channels 0 and 2). A channel range is a
                lower bound channel followed by a hyphen (-) or colon (:) followed by an
                upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
                In the Running state, multiple output channel configurations are
                performed sequentially based on the order specified in this parameter.
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
        attribute_value_ctype = visatype.ViBoolean(0)
        error_code = self._library.niDCPower_GetAttributeViBoolean(self._vi, self._repeated_capability.encode(self._encoding), attribute_id, ctypes.pointer(attribute_value_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(attribute_value_ctype.value)

    def _get_attribute_vi_int32(self, attribute_id):
        '''_get_attribute_vi_int32

        | Queries the value of a ViInt32 attribute.
        | You can use this function to get the values of device-specific
          attributes and inherent IVI attributes.

        Args:
            channel_name (string): Specifies the output channel(s) to which this configuration value
                applies. Specify multiple channels by using a channel list or a channel
                range. A channel list is a comma (,) separated sequence of channel names
                (for example, 0,2 specifies channels 0 and 2). A channel range is a
                lower bound channel followed by a hyphen (-) or colon (:) followed by an
                upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
                In the Running state, multiple output channel configurations are
                performed sequentially based on the order specified in this parameter.
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
        attribute_value_ctype = visatype.ViInt32(0)
        error_code = self._library.niDCPower_GetAttributeViInt32(self._vi, self._repeated_capability.encode(self._encoding), attribute_id, ctypes.pointer(attribute_value_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(attribute_value_ctype.value)

    def _get_attribute_vi_int64(self, attribute_id):
        '''_get_attribute_vi_int64

        | Queries the value of a ViInt64 attribute.
        | You can use this function to get the values of device-specific
          attributes and inherent IVI attributes.

        Args:
            channel_name (string): Specifies the output channel(s) to which this configuration value
                applies. Specify multiple channels by using a channel list or a channel
                range. A channel list is a comma (,) separated sequence of channel names
                (for example, 0,2 specifies channels 0 and 2). A channel range is a
                lower bound channel followed by a hyphen (-) or colon (:) followed by an
                upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
                In the Running state, multiple output channel configurations are
                performed sequentially based on the order specified in this parameter.
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
        attribute_value_ctype = visatype.ViInt64(0)
        error_code = self._library.niDCPower_GetAttributeViInt64(self._vi, self._repeated_capability.encode(self._encoding), attribute_id, ctypes.pointer(attribute_value_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(attribute_value_ctype.value)

    def _get_attribute_vi_real64(self, attribute_id):
        '''_get_attribute_vi_real64

        | Queries the value of a ViReal64 attribute.
        | You can use this function to get the values of device-specific
          attributes and inherent IVI attributes.

        Args:
            channel_name (string): Specifies the output channel(s) to which this configuration value
                applies. Specify multiple channels by using a channel list or a channel
                range. A channel list is a comma (,) separated sequence of channel names
                (for example, 0,2 specifies channels 0 and 2). A channel range is a
                lower bound channel followed by a hyphen (-) or colon (:) followed by an
                upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
                In the Running state, multiple output channel configurations are
                performed sequentially based on the order specified in this parameter.
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
        attribute_value_ctype = visatype.ViReal64(0)
        error_code = self._library.niDCPower_GetAttributeViReal64(self._vi, self._repeated_capability.encode(self._encoding), attribute_id, ctypes.pointer(attribute_value_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(attribute_value_ctype.value)

    def _get_attribute_vi_string(self, attribute_id):
        '''_get_attribute_vi_string

        | Queries the value of a ViString attribute.
        | You can use this function to get the values of device-specific
          attributes and inherent IVI attributes.

        Args:
            channel_name (string): Specifies the output channel(s) to which this configuration value
                applies. Specify multiple channels by using a channel list or a channel
                range. A channel list is a comma (,) separated sequence of channel names
                (for example, 0,2 specifies channels 0 and 2). A channel range is a
                lower bound channel followed by a hyphen (-) or colon (:) followed by an
                upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
                In the Running state, multiple output channel configurations are
                performed sequentially based on the order specified in this parameter.
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
        buffer_size = 0
        attribute_value_ctype = None
        error_code = self._library.niDCPower_GetAttributeViString(self._vi, self._repeated_capability.encode(self._encoding), attribute_id, buffer_size, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size = error_code
        attribute_value_ctype = (visatype.ViChar * buffer_size)()
        error_code = self._library.niDCPower_GetAttributeViString(self._vi, self._repeated_capability.encode(self._encoding), attribute_id, buffer_size, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return attribute_value_ctype.value.decode(self._encoding)

    def get_channel_name(self, index):
        '''get_channel_name

        Retrieves the output **channelName** that corresponds to the requested
        **index**. Use the CHANNEL_COUNT attribute to
        determine the upper bound of valid values for **index**.

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
        buffer_size = 0
        channel_name_ctype = None
        error_code = self._library.niDCPower_GetChannelName(self._vi, index, buffer_size, channel_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size = error_code
        channel_name_ctype = (visatype.ViChar * buffer_size)()
        error_code = self._library.niDCPower_GetChannelName(self._vi, index, buffer_size, channel_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return channel_name_ctype.value.decode(self._encoding)

    def measure(self, measurement_type):
        '''measure

        Returns the measured value of either the voltage or current on the
        specified output channel. Each call to this function blocks other
        function calls until the hardware returns the **measurement**. To
        measure multiple output channels, use the measure_multiple
        function.

        Args:
            channel_name (string): Specifies the output channel to measure. Only one measurement at a time
                may be made with the measure function. Use the
                measure_multiple function to measure multiple channels.
            measurement_type (int): Specifies whether a voltage or current value is measured.
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
        measurement_ctype = visatype.ViReal64(0)
        error_code = self._library.niDCPower_Measure(self._vi, self._repeated_capability.encode(self._encoding), measurement_type, ctypes.pointer(measurement_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(measurement_ctype.value)

    def measure_multiple(self):
        '''measure_multiple

        Returns arrays of the measured voltage and current values on the
        specified output channel(s). Each call to this function blocks other
        function calls until the measurements are returned from the device. The
        order of the measurements returned in the array corresponds to the order
        on the specified output channel(s).

        Args:
            channel_name (string): Specifies the output channels to measure. You can specify multiple
                channels by using a channel list or a channel range. A channel list is a
                comma (,) separated sequence of channel names (e.g. 0,2 specifies
                channels 0 and 2). A channel range is a lower bound channel followed by
                a hyphen (-) or colon (:) followed by an upper bound channel (e.g. 0-2
                specifies channels 0, 1, and 2). If you do not specify a channel name,
                the function uses all channels in the session.

        Returns:
            voltage_measurements (string): Returns an array of voltage measurements. The measurements in the array
                are returned in the same order as the channels specified in
                **channelName**. Ensure that sufficient space has been allocated for the
                returned array.
            current_measurements (string): Returns an array of current measurements. The measurements in the array
                are returned in the same order as the channels specified in
                **channelName**. Ensure that sufficient space has been allocated for the
                returned array.
        '''
        voltage_measurements_ctype = (visatype.ViChar * 1)()
        current_measurements_ctype = (visatype.ViChar * 1)()
        error_code = self._library.niDCPower_MeasureMultiple(self._vi, self._repeated_capability.encode(self._encoding), voltage_measurements_ctype, current_measurements_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return voltage_measurements_ctype.value.decode(self._encoding), current_measurements_ctype.value.decode(self._encoding)

    def query_in_compliance(self):
        '''query_in_compliance

        Queries the specified output device to determine if it is operating at
        the `compliance <REPLACE_DRIVER_SPECIFIC_URL_2(compliance)>`__ limit.

        The compliance limit is the current limit when the output function is
        set to NIDCPOWER_VAL_DC_VOLTAGE. If the output is operating at the
        compliance limit, the output reaches the current limit before the
        desired voltage level. Refer to the configure_output_function
        function and the configure_current_limit function for more
        information about output function and current limit, respectively.

        The compliance limit is the voltage limit when the output function is
        set to NIDCPOWER_VAL_DC_CURRENT. If the output is operating at the
        compliance limit, the output reaches the voltage limit before the
        desired current level. Refer to the configure_output_function
        function and the configure_voltage_limit function for more
        information about output function and voltage limit, respectively.

        **Related Topics:**

        `Compliance <REPLACE_DRIVER_SPECIFIC_URL_1(compliance)>`__

        Args:
            channel_name (string): Specifies the output channel to query. Compliance status can only be
                queried for one channel at a time.

        Returns:
            in_compliance (bool): Returns whether the device output channel is in compliance.
        '''
        in_compliance_ctype = visatype.ViBoolean(0)
        error_code = self._library.niDCPower_QueryInCompliance(self._vi, self._repeated_capability.encode(self._encoding), ctypes.pointer(in_compliance_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(in_compliance_ctype.value)

    def query_max_current_limit(self, voltage_level):
        '''query_max_current_limit

        Queries the maximum current limit on an output channel if the output
        channel is set to the specified **voltageLevel**.

        Args:
            channel_name (string): Specifies the output channel to query. The maximum current limit may
                only be queried for one channel at a time.
            voltage_level (float): Specifies the voltage level to use when calculating the
                **maxCurrentLimit**.

        Returns:
            max_current_limit (float): Returns the maximum current limit that can be set with the specified
                **voltageLevel**.
        '''
        max_current_limit_ctype = visatype.ViReal64(0)
        error_code = self._library.niDCPower_QueryMaxCurrentLimit(self._vi, self._repeated_capability.encode(self._encoding), voltage_level, ctypes.pointer(max_current_limit_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(max_current_limit_ctype.value)

    def query_max_voltage_level(self, current_limit):
        '''query_max_voltage_level

        Queries the maximum voltage level on an output channel if the output
        channel is set to the specified **currentLimit**.

        Args:
            channel_name (string): Specifies the output channel to query. The maximum voltage level may
                only be queried for one channel at a time.
            current_limit (float): Specifies the current limit to use when calculating the
                **maxVoltageLevel**.

        Returns:
            max_voltage_level (float): Returns the maximum voltage level that can be set on an output channel
                with the specified **currentLimit**.
        '''
        max_voltage_level_ctype = visatype.ViReal64(0)
        error_code = self._library.niDCPower_QueryMaxVoltageLevel(self._vi, self._repeated_capability.encode(self._encoding), current_limit, ctypes.pointer(max_voltage_level_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(max_voltage_level_ctype.value)

    def query_min_current_limit(self, voltage_level):
        '''query_min_current_limit

        Queries the minimum current limit on an output channel if the output
        channel is set to the specified **voltageLevel**.

        Args:
            channel_name (string): Specifies the output channel to query. The minimum current limit may
                only be queried for one channel at a time.
            voltage_level (float): Specifies the voltage level to use when calculating the
                **minCurrentLimit**.

        Returns:
            min_current_limit (float): Returns the minimum current limit that can be set on an output channel
                with the specified **voltageLevel**.
        '''
        min_current_limit_ctype = visatype.ViReal64(0)
        error_code = self._library.niDCPower_QueryMinCurrentLimit(self._vi, self._repeated_capability.encode(self._encoding), voltage_level, ctypes.pointer(min_current_limit_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(min_current_limit_ctype.value)

    def query_output_state(self, output_state):
        '''query_output_state

        Queries the specified output channel to determine if the output channel
        is currently in the state specified by **outputState**.

        **Related Topics:**

        `Compliance <REPLACE_DRIVER_SPECIFIC_URL_1(compliance)>`__

        Args:
            channel_name (string): Specifies the output channel to query. The output state may only be
                queried for one channel at a time.
            output_state (int): Specifies the output state of the output channel that is being queried.
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
        in_state_ctype = visatype.ViBoolean(0)
        error_code = self._library.niDCPower_QueryOutputState(self._vi, self._repeated_capability.encode(self._encoding), output_state, ctypes.pointer(in_state_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(in_state_ctype.value)

    def _set_attribute_vi_boolean(self, attribute_id, attribute_value):
        '''_set_attribute_vi_boolean

        | Sets the value of a ViBoolean attribute.
        | This is a low-level function that you can use to set the values of
          device-specific attributes and inherent IVI attributes.

        Args:
            channel_name (string): Specifies the output channel(s) to which this configuration value
                applies. Specify multiple channels by using a channel list or a channel
                range. A channel list is a comma (,) separated sequence of channel names
                (for example, 0,2 specifies channels 0 and 2). A channel range is a
                lower bound channel followed by a hyphen (-) or colon (:) followed by an
                upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
                In the Running state, multiple output channel configurations are
                performed sequentially based on the order specified in this parameter.
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
        error_code = self._library.niDCPower_SetAttributeViBoolean(self._vi, self._repeated_capability.encode(self._encoding), attribute_id, attribute_value)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_int32(self, attribute_id, attribute_value):
        '''_set_attribute_vi_int32

        | Sets the value of a ViInt32 attribute.
        | This is a low-level function that you can use to set the values of
          device-specific attributes and inherent IVI attributes.

        Args:
            channel_name (string): Specifies the output channel(s) to which this configuration value
                applies. Specify multiple channels by using a channel list or a channel
                range. A channel list is a comma (,) separated sequence of channel names
                (for example, 0,2 specifies channels 0 and 2). A channel range is a
                lower bound channel followed by a hyphen (-) or colon (:) followed by an
                upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
                In the Running state, multiple output channel configurations are
                performed sequentially based on the order specified in this parameter.
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
        error_code = self._library.niDCPower_SetAttributeViInt32(self._vi, self._repeated_capability.encode(self._encoding), attribute_id, attribute_value)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_int64(self, attribute_id, attribute_value):
        '''_set_attribute_vi_int64

        | Sets the value of a ViInt64 attribute.
        | This is a low-level function that you can use to set the values of
          device-specific attributes and inherent IVI attributes.

        Args:
            channel_name (string): Specifies the output channel(s) to which this configuration value
                applies. Specify multiple channels by using a channel list or a channel
                range. A channel list is a comma (,) separated sequence of channel names
                (for example, 0,2 specifies channels 0 and 2). A channel range is a
                lower bound channel followed by a hyphen (-) or colon (:) followed by an
                upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
                In the Running state, multiple output channel configurations are
                performed sequentially based on the order specified in this parameter.
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
        error_code = self._library.niDCPower_SetAttributeViInt64(self._vi, self._repeated_capability.encode(self._encoding), attribute_id, attribute_value)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_real64(self, attribute_id, attribute_value):
        '''_set_attribute_vi_real64

        | Sets the value of a ViReal64 attribute.
        | This is a low-level function that you can use to set the values of
          device-specific attributes and inherent IVI attributes.

        Args:
            channel_name (string): Specifies the output channel(s) to which this configuration value
                applies. Specify multiple channels by using a channel list or a channel
                range. A channel list is a comma (,) separated sequence of channel names
                (for example, 0,2 specifies channels 0 and 2). A channel range is a
                lower bound channel followed by a hyphen (-) or colon (:) followed by an
                upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
                In the Running state, multiple output channel configurations are
                performed sequentially based on the order specified in this parameter.
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
        error_code = self._library.niDCPower_SetAttributeViReal64(self._vi, self._repeated_capability.encode(self._encoding), attribute_id, attribute_value)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_string(self, attribute_id, attribute_value):
        '''_set_attribute_vi_string

        | Sets the value of a ViString attribute.
        | This is a low-level function that you can use to set the values of
          device-specific attributes and inherent IVI attributes.

        Args:
            channel_name (string): Specifies the output channel(s) to which this configuration value
                applies. Specify multiple channels by using a channel list or a channel
                range. A channel list is a comma (,) separated sequence of channel names
                (for example, 0,2 specifies channels 0 and 2). A channel range is a
                lower bound channel followed by a hyphen (-) or colon (:) followed by an
                upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
                In the Running state, multiple output channel configurations are
                performed sequentially based on the order specified in this parameter.
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
        error_code = self._library.niDCPower_SetAttributeViString(self._vi, self._repeated_capability.encode(self._encoding), attribute_id, attribute_value.encode(self._encoding))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_sequence(self, values, source_delays, size):
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

        Args:
            channel_name (string): Specifies the output channel to which this configuration value applies.
                You can only set a sequence for one channel at a time.
            values (string): Specifies the series of voltage levels or current levels, depending on
                the configured `output
                function <REPLACE_DRIVER_SPECIFIC_URL_1(programming_output)>`__.
                **Valid values**:
                The valid values for this parameter are defined by the voltage level
                range or current level range.
            source_delays (string): Specifies the source delay that follows the configuration of each value
                in the sequence.
                **Valid Values**:
                The valid values are between 0 and 167 seconds.
            size (int): The number of elements in the Values and the Source Delays arrays. The
                Values and Source Delays arrays should have the same size.
        '''
        error_code = self._library.niDCPower_SetSequence(self._vi, self._repeated_capability.encode(self._encoding), values.encode(self._encoding), source_delays.encode(self._encoding), size)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return


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
        except errors.Error:
            # TODO(marcoskirsch): This will occur when session is "stolen". Change to log instead
            print("Failed to close session.")
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

        Use the configure_output_enabled function to disable power
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
        error_code = self._library.niDCPower_Abort(self._vi)
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
        error_code = self._library.niDCPower_Commit(self._vi)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_digital_edge_measure_trigger(self, input_terminal, edge):
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
            edge (int): Specifies whether to configure the Measure trigger to assert on the
                rising or falling edge.
                **Defined Values:**

                +------------------------------+----------------------------------------------------------------+
                | NIDCPOWER_VAL_RISING (1016)  | Asserts the trigger on the rising edge of the digital signal.  |
                +------------------------------+----------------------------------------------------------------+
                | NIDCPOWER_VAL_FALLING (1017) | Asserts the trigger on the falling edge of the digital signal. |
                +------------------------------+----------------------------------------------------------------+
        '''
        error_code = self._library.niDCPower_ConfigureDigitalEdgeMeasureTrigger(self._vi, input_terminal.encode(self._encoding), edge)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_digital_edge_pulse_trigger(self, input_terminal, edge):
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
            edge (int): Specifies whether to configure the Pulse trigger to assert on the rising
                or falling edge.
                **Defined Values:**

                +------------------------------+----------------------------------------------------------------+
                | NIDCPOWER_VAL_RISING (1016)  | Asserts the trigger on the rising edge of the digital signal.  |
                +------------------------------+----------------------------------------------------------------+
                | NIDCPOWER_VAL_FALLING (1017) | Asserts the trigger on the falling edge of the digital signal. |
                +------------------------------+----------------------------------------------------------------+
        '''
        error_code = self._library.niDCPower_ConfigureDigitalEdgePulseTrigger(self._vi, input_terminal.encode(self._encoding), edge)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_digital_edge_sequence_advance_trigger(self, input_terminal, edge):
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
            edge (int): Specifies whether to configure the Sequence Advance trigger to assert on
                the rising or falling edge.
                **Defined Values:**

                +------------------------------+----------------------------------------------------------------+
                | NIDCPOWER_VAL_RISING (1016)  | Asserts the trigger on the rising edge of the digital signal.  |
                +------------------------------+----------------------------------------------------------------+
                | NIDCPOWER_VAL_FALLING (1017) | Asserts the trigger on the falling edge of the digital signal. |
                +------------------------------+----------------------------------------------------------------+
        '''
        error_code = self._library.niDCPower_ConfigureDigitalEdgeSequenceAdvanceTrigger(self._vi, input_terminal.encode(self._encoding), edge)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_digital_edge_source_trigger(self, input_terminal, edge):
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
            edge (int): Specifies whether to configure the Source trigger to assert on the
                rising or falling edge.
                **Defined Values:**

                +------------------------------+----------------------------------------------------------------+
                | NIDCPOWER_VAL_RISING (1016)  | Asserts the trigger on the rising edge of the digital signal.  |
                +------------------------------+----------------------------------------------------------------+
                | NIDCPOWER_VAL_FALLING (1017) | Asserts the trigger on the falling edge of the digital signal. |
                +------------------------------+----------------------------------------------------------------+
        '''
        error_code = self._library.niDCPower_ConfigureDigitalEdgeSourceTrigger(self._vi, input_terminal.encode(self._encoding), edge)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_digital_edge_start_trigger(self, input_terminal, edge):
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
            edge (int): Specifies whether to configure the Start trigger to assert on the rising
                or falling edge.
                **Defined Values:**

                +------------------------------+----------------------------------------------------------------+
                | NIDCPOWER_VAL_RISING (1016)  | Asserts the trigger on the rising edge of the digital signal.  |
                +------------------------------+----------------------------------------------------------------+
                | NIDCPOWER_VAL_FALLING (1017) | Asserts the trigger on the falling edge of the digital signal. |
                +------------------------------+----------------------------------------------------------------+
        '''
        error_code = self._library.niDCPower_ConfigureDigitalEdgeStartTrigger(self._vi, input_terminal.encode(self._encoding), edge)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def create_advanced_sequence(self, sequence_name, attribute_id_count, attribute_ids, set_as_active_sequence):
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
            attribute_ids (string): Specifies the attributes you reconfigure per step in the advanced
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
        error_code = self._library.niDCPower_CreateAdvancedSequence(self._vi, sequence_name.encode(self._encoding), attribute_id_count, attribute_ids.encode(self._encoding), set_as_active_sequence)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def create_advanced_sequence_step(self, set_as_active_step):
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
        error_code = self._library.niDCPower_CreateAdvancedSequenceStep(self._vi, set_as_active_step)
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
        error_code = self._library.niDCPower_DeleteAdvancedSequence(self._vi, sequence_name.encode(self._encoding))
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
        error_code = self._library.niDCPower_Disable(self._vi)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def export_signal(self, signal, signal_identifier, output_terminal):
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
            signal (int): Specifies which trigger or event to export.
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
        error_code = self._library.niDCPower_ExportSignal(self._vi, signal, signal_identifier.encode(self._encoding), output_terminal.encode(self._encoding))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

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
          clear_error.

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
        code_ctype = visatype.ViStatus(0)
        buffer_size = 0
        description_ctype = None
        error_code = self._library.niDCPower_GetError(self._vi, ctypes.pointer(code_ctype), buffer_size, description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=True)
        buffer_size = error_code
        description_ctype = (visatype.ViChar * buffer_size)()
        error_code = self._library.niDCPower_GetError(self._vi, ctypes.pointer(code_ctype), buffer_size, description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return int(code_ctype.value), description_ctype.value.decode(self._encoding)

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
        year_ctype = visatype.ViInt32(0)
        month_ctype = visatype.ViInt32(0)
        day_ctype = visatype.ViInt32(0)
        hour_ctype = visatype.ViInt32(0)
        minute_ctype = visatype.ViInt32(0)
        error_code = self._library.niDCPower_GetSelfCalLastDateAndTime(self._vi, ctypes.pointer(year_ctype), ctypes.pointer(month_ctype), ctypes.pointer(day_ctype), ctypes.pointer(hour_ctype), ctypes.pointer(minute_ctype))
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
        temperature_ctype = visatype.ViReal64(0)
        error_code = self._library.niDCPower_GetSelfCalLastTemp(self._vi, ctypes.pointer(temperature_ctype))
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
        vi_ctype = visatype.ViSession(0)
        error_code = self._library.niDCPower_InitializeWithChannels(resource_name.encode(self._encoding), channels.encode(self._encoding), reset, option_string.encode(self._encoding), ctypes.pointer(vi_ctype))
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
        error_code = self._library.niDCPower_Initiate(self._vi)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def read_current_temperature(self):
        '''read_current_temperature

        Returns the current onboard **temperature**, in degrees Celsius, of the
        device.

        Returns:
            temperature (float): Returns the onboard **temperature**, in degrees Celsius, of the device.
        '''
        temperature_ctype = visatype.ViReal64(0)
        error_code = self._library.niDCPower_ReadCurrentTemperature(self._vi, ctypes.pointer(temperature_ctype))
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
        error_code = self._library.niDCPower_ResetDevice(self._vi)
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
        error_code = self._library.niDCPower_ResetWithDefaults(self._vi)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def send_software_edge_trigger(self, trigger):
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
            trigger (int): Specifies which trigger to assert.
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
        error_code = self._library.niDCPower_SendSoftwareEdgeTrigger(self._vi, trigger)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def wait_for_event(self, event_id, timeout):
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
            event_id (int): Specifies which event to wait for.
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
        error_code = self._library.niDCPower_WaitForEvent(self._vi, event_id, timeout)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _close(self):
        '''_close

        Closes the session specified in **vi** and deallocates the resources
        that NI-DCPower reserves. If power output is enabled when you call this
        function, the output channels remain in their existing state and
        continue providing power. Use the configure_output_enabled
        function to disable power output on a per channel basis. Use the
        reset function to disable power output on all channel(s).

        **Related Topics:**

        `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__
        '''
        error_code = self._library.niDCPower_close(self._vi)
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
        error_message_ctype = (visatype.ViChar * 256)()
        error_code = self._library.niDCPower_error_message(self._vi, error_code, error_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return error_message_ctype.value.decode(self._encoding)

    def reset(self):
        '''reset

        Resets the device to a known state. This function disables power
        generation, resets session attributes to their default values, commits
        the session attributes, and leaves the session in the Uncommitted state.
        Refer to the `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic for
        more information about NI-DCPower software states.
        '''
        error_code = self._library.niDCPower_reset(self._vi)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def revision_query(self):
        '''revision_query

        Returns the revision information of NI-DCPower and the device firmware.

        Returns:
            instrument_driver_revision (string): Returns the driver revision information for NI-DCPower.
            firmware_revision (string): Returns firmware revision information for the device you are using. The
                size of this array must be at least 256 bytes.
        '''
        instrument_driver_revision_ctype = (visatype.ViChar * 256)()
        firmware_revision_ctype = (visatype.ViChar * 256)()
        error_code = self._library.niDCPower_revision_query(self._vi, instrument_driver_revision_ctype, firmware_revision_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return instrument_driver_revision_ctype.value.decode(self._encoding), firmware_revision_ctype.value.decode(self._encoding)

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
        self_test_result_ctype = visatype.ViInt16(0)
        self_test_message_ctype = (visatype.ViChar * 256)()
        error_code = self._library.niDCPower_self_test(self._vi, ctypes.pointer(self_test_result_ctype), self_test_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(self_test_result_ctype.value), self_test_message_ctype.value.decode(self._encoding)



