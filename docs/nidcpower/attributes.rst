nidcpower.Session properties
============================

.. py:currentmodule:: nidcpower

.. py:attribute:: active_advanced_sequence

    Specifies the advanced sequence to configure or generate.



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

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

            - LabVIEW Property: **Source:Advanced:Active Advanced Sequence**
            - C Attribute: **NIDCPOWER_ATTR_ACTIVE_ADVANCED_SEQUENCE**

.. py:attribute:: active_advanced_sequence_step

    Specifies the advanced sequence step to configure.



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

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

            - LabVIEW Property: **Source:Advanced:Active Advanced Sequence Step**
            - C Attribute: **NIDCPOWER_ATTR_ACTIVE_ADVANCED_SEQUENCE_STEP**

.. py:attribute:: aperture_time

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



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

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

            - LabVIEW Property: **Measurement:Aperture Time**
            - C Attribute: **NIDCPOWER_ATTR_APERTURE_TIME**

.. py:attribute:: aperture_time_units

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



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

    The following table lists the characteristics of this property.

    +----------------+------------------------------+
    | Characteristic | Value                        |
    +================+==============================+
    | Datatype       | :py:data:`ApertureTimeUnits` |
    +----------------+------------------------------+
    | Permissions    | read-write                   |
    +----------------+------------------------------+
    | Channel Based  | False                        |
    +----------------+------------------------------+
    | Resettable     | No                           |
    +----------------+------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Measurement:Aperture Time Units**
            - C Attribute: **NIDCPOWER_ATTR_APERTURE_TIME_UNITS**

.. py:attribute:: auto_zero

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

    The following table lists the characteristics of this property.

    +----------------+---------------------+
    | Characteristic | Value               |
    +================+=====================+
    | Datatype       | :py:data:`AutoZero` |
    +----------------+---------------------+
    | Permissions    | read-write          |
    +----------------+---------------------+
    | Channel Based  | False               |
    +----------------+---------------------+
    | Resettable     | No                  |
    +----------------+---------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Measurement:Auto Zero**
            - C Attribute: **NIDCPOWER_ATTR_AUTO_ZERO**

.. py:attribute:: auxiliary_power_source_available

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



    .. note:: This property does not necessarily indicate if the device is using the
        auxiliary power source to generate power. Use the `Power Source In
        Use <pniDCPower_PowerSourceInUse.html>`__ property to retrieve that
        information.

    The following table lists the characteristics of this property.

    +----------------+---------------------+
    | Characteristic | Value               |
    +================+=====================+
    | Datatype       | :py:data:`tBoolean` |
    +----------------+---------------------+
    | Permissions    | read only           |
    +----------------+---------------------+
    | Channel Based  | False               |
    +----------------+---------------------+
    | Resettable     | No                  |
    +----------------+---------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Advanced:Auxiliary Power Source Available**
            - C Attribute: **NIDCPOWER_ATTR_AUXILIARY_POWER_SOURCE_AVAILABLE**

.. py:attribute:: cache

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

    The following table lists the characteristics of this property.

    +----------------+---------------------+
    | Characteristic | Value               |
    +================+=====================+
    | Datatype       | :py:data:`tBoolean` |
    +----------------+---------------------+
    | Permissions    | read-write          |
    +----------------+---------------------+
    | Channel Based  | False               |
    +----------------+---------------------+
    | Resettable     | No                  |
    +----------------+---------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Inherent IVI Attributes:User Options:Cache**
            - C Attribute: **NIDCPOWER_ATTR_CACHE**

.. py:attribute:: channel_count

    Indicates the number of channels that NI-DCPower supports for the
    instrument that was chosen when the current session was opened. For
    channel-based properties, the IVI engine maintains a separate cache
    value for each channel.

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
            - C Attribute: **NIDCPOWER_ATTR_CHANNEL_COUNT**

.. py:attribute:: current_compensation_frequency

    The frequency at which a pole-zero pair is added to the system when the
    channel is in `Constant
    Current <NI_DC_Power_Supplies_Help.chm::/Constant_Current.html>`__ mode.

    **Default Value**: Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

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

            - LabVIEW Property: **Source:Custom Transient Response:Current:Compensation Frequency**
            - C Attribute: **NIDCPOWER_ATTR_CURRENT_COMPENSATION_FREQUENCY**

.. py:attribute:: current_gain_bandwidth

    The frequency at which the unloaded loop gain extrapolates to 0 dB in
    the absence of additional poles and zeroes. This property takes effect
    when the channel is in `Constant
    Current <NI_DC_Power_Supplies_Help.chm::/Constant_Current.html>`__ mode.

    **Default Value**: Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

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

            - LabVIEW Property: **Source:Custom Transient Response:Current:Gain Bandwidth**
            - C Attribute: **NIDCPOWER_ATTR_CURRENT_GAIN_BANDWIDTH**

.. py:attribute:: current_level

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



    .. note:: The channel must be enabled for the specified current level to take
        effect. Refer to the `Output Enabled <pniDCPower_OutputEnabled.html>`__
        property for more information about enabling the output channel.

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

            - LabVIEW Property: **Source:DC Current:Current Level**
            - C Attribute: **NIDCPOWER_ATTR_CURRENT_LEVEL**

.. py:attribute:: current_level_autorange

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

    The following table lists the characteristics of this property.

    +----------------+----------------------------------+
    | Characteristic | Value                            |
    +================+==================================+
    | Datatype       | :py:data:`CurrentLevelAutorange` |
    +----------------+----------------------------------+
    | Permissions    | read-write                       |
    +----------------+----------------------------------+
    | Channel Based  | False                            |
    +----------------+----------------------------------+
    | Resettable     | No                               |
    +----------------+----------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Source:DC Current:Current Level Autorange**
            - C Attribute: **NIDCPOWER_ATTR_CURRENT_LEVEL_AUTORANGE**

.. py:attribute:: current_level_range

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



    .. note:: The channel must be enabled for the specified current level range to
        take effect. Refer to the `Output
        Enabled <pniDCPower_OutputEnabled.html>`__ property for more information
        about enabling the output channel.

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

            - LabVIEW Property: **Source:DC Current:Current Level Range**
            - C Attribute: **NIDCPOWER_ATTR_CURRENT_LEVEL_RANGE**

.. py:attribute:: current_limit

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



    .. note:: The channel must be enabled for the specified current limit to take
        effect. Refer to the `Output Enabled <pniDCPower_OutputEnabled.html>`__
        property for more information about enabling the output channel.

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

            - LabVIEW Property: **Source:DC Voltage:Current Limit**
            - C Attribute: **NIDCPOWER_ATTR_CURRENT_LIMIT**

.. py:attribute:: current_limit_autorange

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

    The following table lists the characteristics of this property.

    +----------------+----------------------------------+
    | Characteristic | Value                            |
    +================+==================================+
    | Datatype       | :py:data:`CurrentLimitAutorange` |
    +----------------+----------------------------------+
    | Permissions    | read-write                       |
    +----------------+----------------------------------+
    | Channel Based  | False                            |
    +----------------+----------------------------------+
    | Resettable     | No                               |
    +----------------+----------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Source:DC Voltage:Current Limit Autorange**
            - C Attribute: **NIDCPOWER_ATTR_CURRENT_LIMIT_AUTORANGE**

.. py:attribute:: current_limit_behavior

    

    The following table lists the characteristics of this property.

    +----------------+---------------------------------+
    | Characteristic | Value                           |
    +================+=================================+
    | Datatype       | :py:data:`CurrentLimitBehavior` |
    +----------------+---------------------------------+
    | Permissions    | read only                       |
    +----------------+---------------------------------+
    | Channel Based  | False                           |
    +----------------+---------------------------------+
    | Resettable     | No                              |
    +----------------+---------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: ****
            - C Attribute: **NIDCPOWER_ATTR_CURRENT_LIMIT_BEHAVIOR**

.. py:attribute:: current_limit_range

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



    .. note:: The channel must be enabled for the specified current limit to take
        effect. Refer to the `Output Enabled <pniDCPower_OutputEnabled.html>`__
        property for more information about enabling the output channel.

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

            - LabVIEW Property: **Source:DC Voltage:Current Limit Range**
            - C Attribute: **NIDCPOWER_ATTR_CURRENT_LIMIT_RANGE**

.. py:attribute:: current_pole_zero_ratio

    The ratio of the pole frequency to the zero frequency when the channel
    is in `Constant
    Current <NI_DC_Power_Supplies_Help.chm::/Constant_Current.html>`__ mode.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

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

            - LabVIEW Property: **Source:Custom Transient Response:Current:Pole-Zero Ratio**
            - C Attribute: **NIDCPOWER_ATTR_CURRENT_POLE_ZERO_RATIO**

.. py:attribute:: dc_noise_rejection

    Determines the relative weighting of samples in a measurement.

    For information about improving noise immunity for NI-DCPower devices
    that support DC noise rejection, refer to `Measurement Noise
    Rejection <NI_DC_Power_Supplies_Help.chm::/noiseRejectMeasure.html>`__

    **Default Value**: **Normal**

    **Related topics:**

    `Measurement Noise
    Rejection <NI_DC_Power_Supplies_Help.chm::/NoiseRejectMeasure.html>`__



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

    The following table lists the characteristics of this property.

    +----------------+-----------------------------+
    | Characteristic | Value                       |
    +================+=============================+
    | Datatype       | :py:data:`DCNoiseRejection` |
    +----------------+-----------------------------+
    | Permissions    | read-write                  |
    +----------------+-----------------------------+
    | Channel Based  | False                       |
    +----------------+-----------------------------+
    | Resettable     | No                          |
    +----------------+-----------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Measurement:Advanced:DC Noise Rejection**
            - C Attribute: **NIDCPOWER_ATTR_DC_NOISE_REJECTION**

.. py:attribute:: digital_edge_measure_trigger_edge

    Specifies whether to configure the Measure trigger to assert on the
    rising or falling edge.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    **Related topics:**

    `Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

    The following table lists the characteristics of this property.

    +----------------+------------------------+
    | Characteristic | Value                  |
    +================+========================+
    | Datatype       | :py:data:`DigitalEdge` |
    +----------------+------------------------+
    | Permissions    | read-write             |
    +----------------+------------------------+
    | Channel Based  | False                  |
    +----------------+------------------------+
    | Resettable     | No                     |
    +----------------+------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggers:Measure Trigger:Digital Edge:Edge**
            - C Attribute: **NIDCPOWER_ATTR_DIGITAL_EDGE_MEASURE_TRIGGER_EDGE**

.. py:attribute:: digital_edge_measure_trigger_input_terminal

    Specifies the input terminal for the Measure trigger. This property is
    used only when the `Measure Trigger
    Type <pniDCPower_MeasureTriggerType.html>`__ property is set to
    **Digital Edge**.

    You can specify any valid input terminal for this property. Valid
    terminals are listed in Measurement & Automation Explorer under the
    **Device Routes** tab.

    Input terminals can be specified in one of two ways. If the device is
    named Dev1 and your terminal is PXI\_Trig0, you can specify the terminal
    with the fully qualified terminal name, /Dev1/PXI\_Trig0, or with the
    shortened terminal name, PXI\_Trig0. The input terminal can also be a
    terminal from another device. For example, you can set the input
    terminal on Dev1 to be /Dev2/SourceCompleteEvent.

    **Related topics:**

    `Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

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

            - LabVIEW Property: **Triggers:Measure Trigger:Digital Edge:Input Terminal**
            - C Attribute: **NIDCPOWER_ATTR_DIGITAL_EDGE_MEASURE_TRIGGER_INPUT_TERMINAL**

.. py:attribute:: digital_edge_pulse_trigger_edge

    Specifies whether to configure the Pulse trigger to assert on the rising
    or falling edge.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    **Related topics:**

    `Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

    The following table lists the characteristics of this property.

    +----------------+------------------------+
    | Characteristic | Value                  |
    +================+========================+
    | Datatype       | :py:data:`DigitalEdge` |
    +----------------+------------------------+
    | Permissions    | read-write             |
    +----------------+------------------------+
    | Channel Based  | False                  |
    +----------------+------------------------+
    | Resettable     | No                     |
    +----------------+------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggers:Pulse Trigger:Digital Edge:Edge**
            - C Attribute: **NIDCPOWER_ATTR_DIGITAL_EDGE_PULSE_TRIGGER_EDGE**

.. py:attribute:: digital_edge_pulse_trigger_input_terminal

    Specifies the input terminal for the Pulse trigger. This property is
    used only when the `Pulse Trigger
    Type <pniDCPower_StartTriggerType.html>`__ property is set to **Digital
    Edge**.

    You can specify any valid input terminal for this property. Valid
    terminals are listed in Measurement & Automation Explorer under the
    **Device Routes** tab.

    Input terminals can be specified in one of two ways. If the device is
    named Dev1 and your terminal is PXI\_Trig0, you can specify the terminal
    with the fully qualified terminal name, /Dev1/PXI\_Trig0, or with the
    shortened terminal name, PXI\_Trig0. The input terminal can also be a
    terminal from another device. For example, you can set the input
    terminal on Dev1 to be /Dev2/SourceCompleteEvent.

    **Related topics:**

    `Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

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

            - LabVIEW Property: **Triggers:Pulse Trigger:Digital Edge:Input Terminal**
            - C Attribute: **NIDCPOWER_ATTR_DIGITAL_EDGE_PULSE_TRIGGER_INPUT_TERMINAL**

.. py:attribute:: digital_edge_sequence_advance_trigger_edge

    Specifies whether to configure the Sequence trigger to assert on the
    rising or falling edge.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    **Related topics:**

    `Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

    The following table lists the characteristics of this property.

    +----------------+------------------------+
    | Characteristic | Value                  |
    +================+========================+
    | Datatype       | :py:data:`DigitalEdge` |
    +----------------+------------------------+
    | Permissions    | read-write             |
    +----------------+------------------------+
    | Channel Based  | False                  |
    +----------------+------------------------+
    | Resettable     | No                     |
    +----------------+------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggers:Sequence Advance Trigger:Digital Edge:Edge**
            - C Attribute: **NIDCPOWER_ATTR_DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_EDGE**

.. py:attribute:: digital_edge_sequence_advance_trigger_input_terminal

    Specifies the input terminal for the Sequence Advance trigger. This
    property is used only when the `Sequence Advance Trigger
    Type <pniDCPower_SequenceAdvanceTriggerType.html>`__ property is set to
    **Digital Edge**.

    You can specify any valid input terminal for this property. Valid
    terminals are listed in Measurement & Automation Explorer under the
    **Device Routes** tab.

    Input terminals can be specified in one of two ways. If the device is
    named Dev1 and your terminal is PXI\_Trig0, you can specify the terminal
    with the fully qualified terminal name, /Dev1/PXI\_Trig0, or with the
    shortened terminal name, PXI\_Trig0. The input terminal can also be a
    terminal from another device. For example, you can set the input
    terminal on Dev1 to be /Dev2/SourceCompleteEvent.

    **Related topics:**

    `Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

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

            - LabVIEW Property: **Triggers:Sequence Advance Trigger:Digital Edge:Input Terminal**
            - C Attribute: **NIDCPOWER_ATTR_DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_INPUT_TERMINAL**

.. py:attribute:: digital_edge_source_trigger_edge

    Specifies whether to configure the Source trigger to assert on the
    rising or falling edge.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    **Related topics:**

    `Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

    The following table lists the characteristics of this property.

    +----------------+------------------------+
    | Characteristic | Value                  |
    +================+========================+
    | Datatype       | :py:data:`DigitalEdge` |
    +----------------+------------------------+
    | Permissions    | read-write             |
    +----------------+------------------------+
    | Channel Based  | False                  |
    +----------------+------------------------+
    | Resettable     | No                     |
    +----------------+------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggers:Source Trigger:Digital Edge:Edge**
            - C Attribute: **NIDCPOWER_ATTR_DIGITAL_EDGE_SOURCE_TRIGGER_EDGE**

.. py:attribute:: digital_edge_source_trigger_input_terminal

    Specifies the input terminal for the Source trigger. This property is
    used only when the `Source Trigger
    Type <pniDCPower_SourceTriggerType.html>`__ property is set to **Digital
    Edge**.

    You can specify any valid input terminal for this property. Valid
    terminals are listed in Measurement & Automation Explorer under the
    **Device Routes** tab.

    Input terminals can be specified in one of two ways. If the device is
    named Dev1 and your terminal is PXI\_Trig0, you can specify the terminal
    with the fully qualified terminal name, /Dev1/PXI\_Trig0, or with the
    shortened terminal name, PXI\_Trig0. The input terminal can also be a
    terminal from another device. For example, you can set the input
    terminal on Dev1 to be /Dev2/SourceCompleteEvent.

    **Related topics:**

    `Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

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

            - LabVIEW Property: **Triggers:Source Trigger:Digital Edge:Input Terminal**
            - C Attribute: **NIDCPOWER_ATTR_DIGITAL_EDGE_SOURCE_TRIGGER_INPUT_TERMINAL**

.. py:attribute:: digital_edge_start_trigger_edge

    Specifies whether to configure the Start trigger to assert on the rising
    or falling edge.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    **Related topics:**

    `Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

    The following table lists the characteristics of this property.

    +----------------+------------------------+
    | Characteristic | Value                  |
    +================+========================+
    | Datatype       | :py:data:`DigitalEdge` |
    +----------------+------------------------+
    | Permissions    | read-write             |
    +----------------+------------------------+
    | Channel Based  | False                  |
    +----------------+------------------------+
    | Resettable     | No                     |
    +----------------+------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggers:Start Trigger:Digital Edge:Edge**
            - C Attribute: **NIDCPOWER_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE**

.. py:attribute:: digital_edge_start_trigger_input_terminal

    Specifies the input terminal for the Start trigger. This property is
    used only when the `Start Trigger
    Type <pniDCPower_StartTriggerType.html>`__ property is set to **Digital
    Edge**.

    You can specify any valid input terminal for this property. Valid
    terminals are listed in Measurement & Automation Explorer under the
    **Device Routes** tab.

    Input terminals can be specified in one of two ways. If the device is
    named Dev1 and your terminal is PXI\_Trig0, you can specify the terminal
    with the fully qualified terminal name, /Dev1/PXI\_Trig0, or with the
    shortened terminal name, PXI\_Trig0. The input terminal can also be a
    terminal from another device. For example, you can set the input
    terminal on Dev1 to be /Dev2/SourceCompleteEvent.

    **Related topics:**

    `Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

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

            - LabVIEW Property: **Triggers:Start Trigger:Digital Edge:Input Terminal**
            - C Attribute: **NIDCPOWER_ATTR_DIGITAL_EDGE_START_TRIGGER_INPUT_TERMINAL**

.. py:attribute:: driver_setup

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
            - C Attribute: **NIDCPOWER_ATTR_DRIVER_SETUP**

.. py:attribute:: exported_measure_trigger_output_terminal

    Specifies the output terminal for exporting the Measure trigger.

    Refer to the **Device Routes** tab in Measurement & Automation Explorer
    for a list of the terminals available on your device.

    Output terminals can be specified in one of two ways. If the device is
    named Dev1 and your terminal is PXI\_Trig0, you can specify the terminal
    with the fully qualified terminal name, /Dev1/PXI\_Trig0, or with the
    shortened terminal name, PXI\_Trig0.

    **Related topics:**

    `Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

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

            - LabVIEW Property: **Triggers:Measure Trigger:Export Output Terminal**
            - C Attribute: **NIDCPOWER_ATTR_EXPORTED_MEASURE_TRIGGER_OUTPUT_TERMINAL**

.. py:attribute:: exported_pulse_trigger_output_terminal

    Specifies the output terminal for exporting the Pulse trigger.

    Refer to the **Device Routes** tab in Measurement & Automation Explorer
    for a list of the terminals available on your device.

    Output terminals can be specified in one of two ways. If the device is
    named Dev1 and your terminal is PXI\_Trig0, you can specify the terminal
    with the fully qualified terminal name, /Dev1/PXI\_Trig0, or with the
    shortened terminal name, PXI\_Trig0.

    **Related topics:**

    `Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

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

            - LabVIEW Property: **Triggers:Pulse Trigger:Export Output Terminal**
            - C Attribute: **NIDCPOWER_ATTR_EXPORTED_PULSE_TRIGGER_OUTPUT_TERMINAL**

.. py:attribute:: exported_sequence_advance_trigger_output_terminal

    Specifies the output terminal for exporting the Sequence Advance
    trigger.

    Refer to the **Device Routes** tab in Measurement & Automation Explorer
    for a list of the terminals available on your device.

    Output terminals can be specified in one of two ways. If the device is
    named Dev1 and your terminal is PXI\_Trig0, you can specify the terminal
    with the fully qualified terminal name, /Dev1/PXI\_Trig0, or with the
    shortened terminal name, PXI\_Trig0.

    **Related topics:**

    `Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

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

            - LabVIEW Property: **Triggers:Sequence Advance Trigger:Export Output Terminal**
            - C Attribute: **NIDCPOWER_ATTR_EXPORTED_SEQUENCE_ADVANCE_TRIGGER_OUTPUT_TERMINAL**

.. py:attribute:: exported_source_trigger_output_terminal

    Specifies the output terminal for exporting the Source trigger.

    Refer to the **Device Routes** tab in Measurement & Automation Explorer
    for a list of the terminals available on your device.

    Output terminals can be specified in one of two ways. If the device is
    named Dev1 and your terminal is PXI\_Trig0, you can specify the terminal
    with the fully qualified terminal name, /Dev1/PXI\_Trig0, or with the
    shortened terminal name, PXI\_Trig0.

    **Related topics:**

    `Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

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

            - LabVIEW Property: **Triggers:Source Trigger:Export Output Terminal**
            - C Attribute: **NIDCPOWER_ATTR_EXPORTED_SOURCE_TRIGGER_OUTPUT_TERMINAL**

.. py:attribute:: exported_start_trigger_output_terminal

    Specifies the output terminal for exporting the Start trigger.

    Refer to the **Device Routes** tab in Measurement & Automation Explorer
    for a list of the terminals available on your device.

    Output terminals can be specified in one of two ways. If the device is
    named Dev1 and your terminal is PXI\_Trig0, you can specify the terminal
    with the fully qualified terminal name, /Dev1/PXI\_Trig0, or with the
    shortened terminal name, PXI\_Trig0.

    **Related topics:**

    `Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

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

            - LabVIEW Property: **Triggers:Start Trigger:Export Output Terminal**
            - C Attribute: **NIDCPOWER_ATTR_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL**

.. py:attribute:: fetch_backlog

    Returns the number of measurements acquired that have not been fetched
    yet.

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

            - LabVIEW Property: **Measurement:Fetch Backlog**
            - C Attribute: **NIDCPOWER_ATTR_FETCH_BACKLOG**

.. py:attribute:: group_capabilities

    Contains a comma-separated (,) list of class-extension groups that
    NI-DCPower implements.

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
            - C Attribute: **NIDCPOWER_ATTR_GROUP_CAPABILITIES**

.. py:attribute:: instrument_firmware_revision

    Contains the firmware revision information for the device you are
    currently using.

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
            - C Attribute: **NIDCPOWER_ATTR_INSTRUMENT_FIRMWARE_REVISION**

.. py:attribute:: instrument_manufacturer

    Contains the name of the manufacturer for the device you are currently
    using.

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
            - C Attribute: **NIDCPOWER_ATTR_INSTRUMENT_MANUFACTURER**

.. py:attribute:: instrument_model

    Contains the model number or name of the device you are currently using.

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
            - C Attribute: **NIDCPOWER_ATTR_INSTRUMENT_MODEL**

.. py:attribute:: interchange_check

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

    The following table lists the characteristics of this property.

    +----------------+---------------------+
    | Characteristic | Value               |
    +================+=====================+
    | Datatype       | :py:data:`tBoolean` |
    +----------------+---------------------+
    | Permissions    | read-write          |
    +----------------+---------------------+
    | Channel Based  | False               |
    +----------------+---------------------+
    | Resettable     | No                  |
    +----------------+---------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Inherent IVI Attributes:User Options:Interchange Check**
            - C Attribute: **NIDCPOWER_ATTR_INTERCHANGE_CHECK**

.. py:attribute:: interlock_input_open

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

    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

    The following table lists the characteristics of this property.

    +----------------+---------------------+
    | Characteristic | Value               |
    +================+=====================+
    | Datatype       | :py:data:`tBoolean` |
    +----------------+---------------------+
    | Permissions    | read only           |
    +----------------+---------------------+
    | Channel Based  | False               |
    +----------------+---------------------+
    | Resettable     | No                  |
    +----------------+---------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Advanced:Interlock Input Open**
            - C Attribute: **NIDCPOWER_ATTR_INTERLOCK_INPUT_OPEN**

.. py:attribute:: io_resource_descriptor

    Indicates the resource descriptor NI-DCPower uses to identify the
    physical device.

    If you initialize NI-DCPower with a logical name, this property contains
    the resource descriptor that corresponds to the entry in the IVI
    Configuration Utility. If you initialize NI-DCPower with the resource
    descriptor, this property contains that value.

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

            - LabVIEW Property: **Inherent IVI Attributes:Advanced Session Information:Resource Descriptor**
            - C Attribute: **NIDCPOWER_ATTR_IO_RESOURCE_DESCRIPTOR**

.. py:attribute:: logical_name

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
            - C Attribute: **NIDCPOWER_ATTR_LOGICAL_NAME**

.. py:attribute:: measure_buffer_size

    Specifies the number of samples that the active channel measurement
    buffer can hold.

    **The Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    **Valid Range**: 1000 to 2147483647

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

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

            - LabVIEW Property: **Measurement:Advanced:Measure Buffer Size**
            - C Attribute: **NIDCPOWER_ATTR_MEASURE_BUFFER_SIZE**

.. py:attribute:: measure_complete_event_delay

    Specifies the amount of time to delay the generation of the Measure
    Complete event, in seconds.

    The NI PXI-4132 and NI PXIe-4140/4141/4142/4143/4144/4145/4154 support
    values from 0 seconds to 167 seconds.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

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

            - LabVIEW Property: **Events:Measure Complete Event:Event Delay**
            - C Attribute: **NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_DELAY**

.. py:attribute:: measure_complete_event_output_terminal

    Specifies the output terminal for exporting the Measure Complete event.

    Output terminals can be specified in one of two ways. If the device is
    named Dev1 and your terminal is PXI\_Trig0, you can specify the terminal
    with the fully qualified terminal name, /Dev1/PXI\_Trig0, or with the
    shortened terminal name, PXI\_Trig0.



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

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

            - LabVIEW Property: **Events:Measure Complete Event:Output Terminal**
            - C Attribute: **NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_OUTPUT_TERMINAL**

.. py:attribute:: measure_complete_event_pulse_polarity

    Specifies the behavior of the Measure Complete event.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

    The following table lists the characteristics of this property.

    +----------------+---------------------+
    | Characteristic | Value               |
    +================+=====================+
    | Datatype       | :py:data:`Polarity` |
    +----------------+---------------------+
    | Permissions    | read-write          |
    +----------------+---------------------+
    | Channel Based  | False               |
    +----------------+---------------------+
    | Resettable     | No                  |
    +----------------+---------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Measure Complete Event:Pulse:Polarity**
            - C Attribute: **NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_PULSE_POLARITY**

.. py:attribute:: measure_complete_event_pulse_width

    Specifies the width of the Measure Complete event, in seconds.

    The minimum event pulse width value for the NI PXI-4132 is 150 ns, and
    the minimum event pulse width value for PXI Express devices is 250 ns.

    The maximum event pulse width value for all devices is 1.6 microseconds.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

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

            - LabVIEW Property: **Events:Measure Complete Event:Pulse:Width**
            - C Attribute: **NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_PULSE_WIDTH**

.. py:attribute:: measure_record_delta_time

    Queries the amount of time, in seconds, between the start of two
    consecutive measurements in a measure record. Only query this property
    after the desired measurement settings are committed.



    .. note:: This property is not available when the `Auto
        Zero <pniDCPower_AutoZero.html>`__ property is set to **Once** because
        the amount of time between the first two measurements and the rest would
        differ.

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

            - LabVIEW Property: **Measurement:Measure Record Delta Time**
            - C Attribute: **NIDCPOWER_ATTR_MEASURE_RECORD_DELTA_TIME**

.. py:attribute:: measure_record_length

    Specifies how many measurements compose a measure record. When this
    property is set to a value greater than 1, the `Measure
    When <pniDCPower_MeasureWhen.html>`__ property must be set to
    **Automatically after Source Complete** or **On Measure Trigger**.

    **Valid Values**: 1 to 16,777,216

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.



    .. note:: This property is not available in a session involving multiple channels.

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

            - LabVIEW Property: **Measurement:Measure Record Length**
            - C Attribute: **NIDCPOWER_ATTR_MEASURE_RECORD_LENGTH**

.. py:attribute:: measure_record_length_is_finite

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



    .. note:: This property is not available in a session involving multiple channels.

    The following table lists the characteristics of this property.

    +----------------+---------------------+
    | Characteristic | Value               |
    +================+=====================+
    | Datatype       | :py:data:`tBoolean` |
    +----------------+---------------------+
    | Permissions    | read-write          |
    +----------------+---------------------+
    | Channel Based  | False               |
    +----------------+---------------------+
    | Resettable     | No                  |
    +----------------+---------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Measurement:Measure Record Length Is Finite**
            - C Attribute: **NIDCPOWER_ATTR_MEASURE_RECORD_LENGTH_IS_FINITE**

.. py:attribute:: measure_trigger_type

    Specifies the behavior of the Measure trigger.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    **Related topics:**

    `Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

    The following table lists the characteristics of this property.

    +----------------+------------------------+
    | Characteristic | Value                  |
    +================+========================+
    | Datatype       | :py:data:`TriggerType` |
    +----------------+------------------------+
    | Permissions    | read-write             |
    +----------------+------------------------+
    | Channel Based  | False                  |
    +----------------+------------------------+
    | Resettable     | No                     |
    +----------------+------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggers:Measure Trigger:Trigger Type**
            - C Attribute: **NIDCPOWER_ATTR_MEASURE_TRIGGER_TYPE**

.. py:attribute:: measure_when

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

    The following table lists the characteristics of this property.

    +----------------+------------------------+
    | Characteristic | Value                  |
    +================+========================+
    | Datatype       | :py:data:`MeasureWhen` |
    +----------------+------------------------+
    | Permissions    | read-write             |
    +----------------+------------------------+
    | Channel Based  | False                  |
    +----------------+------------------------+
    | Resettable     | No                     |
    +----------------+------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Measurement:Advanced:Measure When**
            - C Attribute: **NIDCPOWER_ATTR_MEASURE_WHEN**

.. py:attribute:: output_capacitance

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



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

    The following table lists the characteristics of this property.

    +----------------+------------------------------+
    | Characteristic | Value                        |
    +================+==============================+
    | Datatype       | :py:data:`OutputCapacitance` |
    +----------------+------------------------------+
    | Permissions    | read-write                   |
    +----------------+------------------------------+
    | Channel Based  | False                        |
    +----------------+------------------------------+
    | Resettable     | No                           |
    +----------------+------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Source:Advanced:Output Capacitance**
            - C Attribute: **NIDCPOWER_ATTR_OUTPUT_CAPACITANCE**

.. py:attribute:: output_connected

    Specifies whether the output relay is connected (closed) or disconnected
    (open). The `Output Enabled <pniDCPower_OutputEnabled.html>`__ property
    does not change based on this property; they are independent of each
    other.

    Set this property to FALSE to disconnect the output terminal from the
    output.

    **Default Value**: Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.



    .. note:: Only disconnect the output when disconnecting is necessary for your
        application. For example, a battery connected to the output terminal
        might discharge unless the relay is disconnected. Excessive connecting
        and disconnecting of the output can cause premature wear on
        electromechanical relays, such as those used by the NI PXI-4132 or NI
        PXIe-4138/39.

    The following table lists the characteristics of this property.

    +----------------+---------------------+
    | Characteristic | Value               |
    +================+=====================+
    | Datatype       | :py:data:`tBoolean` |
    +----------------+---------------------+
    | Permissions    | read-write          |
    +----------------+---------------------+
    | Channel Based  | False               |
    +----------------+---------------------+
    | Resettable     | No                  |
    +----------------+---------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Source:Output Connected**
            - C Attribute: **NIDCPOWER_ATTR_OUTPUT_CONNECTED**

.. py:attribute:: output_enabled

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



    .. note:: If the session is in the Committed or Uncommitted states, enabling the
        output does not take effect until you call the `niDCPower
        Initiate <NIDCPowerVIRef.chm::/niDCPower_Initiate.html>`__ VI. Refer to
        the `Programming
        States <NI_DC_Power_Supplies_Help.chm::/programmingStates.html>`__ topic
        in the *NI DC Power Supplies and SMUs Help* for more information about
        NI-DCPower programming states.

    The following table lists the characteristics of this property.

    +----------------+---------------------+
    | Characteristic | Value               |
    +================+=====================+
    | Datatype       | :py:data:`tBoolean` |
    +----------------+---------------------+
    | Permissions    | read-write          |
    +----------------+---------------------+
    | Channel Based  | False               |
    +----------------+---------------------+
    | Resettable     | No                  |
    +----------------+---------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Source:Output Enabled**
            - C Attribute: **NIDCPOWER_ATTR_OUTPUT_ENABLED**

.. py:attribute:: output_function

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

    The following table lists the characteristics of this property.

    +----------------+---------------------------+
    | Characteristic | Value                     |
    +================+===========================+
    | Datatype       | :py:data:`OutputFunction` |
    +----------------+---------------------------+
    | Permissions    | read-write                |
    +----------------+---------------------------+
    | Channel Based  | False                     |
    +----------------+---------------------------+
    | Resettable     | No                        |
    +----------------+---------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Source:Output Function**
            - C Attribute: **NIDCPOWER_ATTR_OUTPUT_FUNCTION**

.. py:attribute:: output_resistance

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



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

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

            - LabVIEW Property: **Source:Output Resistance**
            - C Attribute: **NIDCPOWER_ATTR_OUTPUT_RESISTANCE**

.. py:attribute:: overranging_enabled

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

    The following table lists the characteristics of this property.

    +----------------+---------------------+
    | Characteristic | Value               |
    +================+=====================+
    | Datatype       | :py:data:`tBoolean` |
    +----------------+---------------------+
    | Permissions    | read-write          |
    +----------------+---------------------+
    | Channel Based  | False               |
    +----------------+---------------------+
    | Resettable     | No                  |
    +----------------+---------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Source:Advanced:Overranging Enabled**
            - C Attribute: **NIDCPOWER_ATTR_OVERRANGING_ENABLED**

.. py:attribute:: ovp_enabled

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

    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

    The following table lists the characteristics of this property.

    +----------------+---------------------+
    | Characteristic | Value               |
    +================+=====================+
    | Datatype       | :py:data:`tBoolean` |
    +----------------+---------------------+
    | Permissions    | read-write          |
    +----------------+---------------------+
    | Channel Based  | False               |
    +----------------+---------------------+
    | Resettable     | No                  |
    +----------------+---------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Source:Advanced:OVP Enabled**
            - C Attribute: **NIDCPOWER_ATTR_OVP_ENABLED**

.. py:attribute:: ovp_limit

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



    .. note:: Refer to `Supported Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

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

            - LabVIEW Property: **Source:Advanced:OVP Limit**
            - C Attribute: **NIDCPOWER_ATTR_OVP_LIMIT**

.. py:attribute:: power_line_frequency

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



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

    The following table lists the characteristics of this property.

    +----------------+-------------------------------+
    | Characteristic | Value                         |
    +================+===============================+
    | Datatype       | :py:data:`PowerLineFrequency` |
    +----------------+-------------------------------+
    | Permissions    | read-write                    |
    +----------------+-------------------------------+
    | Channel Based  | False                         |
    +----------------+-------------------------------+
    | Resettable     | No                            |
    +----------------+-------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Measurement:Power Line Frequency**
            - C Attribute: **NIDCPOWER_ATTR_POWER_LINE_FREQUENCY**

.. py:attribute:: power_source

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



    .. note:: Automatic selection is not persistent and occurs only at the time this
        property is set to **Automatic**. However, if the session is in the
        `Committed or
        Uncommitted <NI_DC_Power_Supplies_Help.chm::/programmingStates.html>`__
        state when you set this property, the power source selection only occurs
        after you call the `niDCPower
        Initiate <NIDCPowerVIRef.chm::/niDCPower_Initiate.html>`__ VI.

    The following table lists the characteristics of this property.

    +----------------+------------------------+
    | Characteristic | Value                  |
    +================+========================+
    | Datatype       | :py:data:`PowerSource` |
    +----------------+------------------------+
    | Permissions    | read-write             |
    +----------------+------------------------+
    | Channel Based  | False                  |
    +----------------+------------------------+
    | Resettable     | No                     |
    +----------------+------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Advanced:Power Source**
            - C Attribute: **NIDCPOWER_ATTR_POWER_SOURCE**

.. py:attribute:: power_source_in_use

    Indicates whether the device is using the internal or auxiliary power
    source to generate power.

    The following table lists the characteristics of this property.

    +----------------+-----------------------------+
    | Characteristic | Value                       |
    +================+=============================+
    | Datatype       | :py:data:`PowerSourceInUse` |
    +----------------+-----------------------------+
    | Permissions    | read only                   |
    +----------------+-----------------------------+
    | Channel Based  | False                       |
    +----------------+-----------------------------+
    | Resettable     | No                          |
    +----------------+-----------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Advanced:Power Source In Use**
            - C Attribute: **NIDCPOWER_ATTR_POWER_SOURCE_IN_USE**

.. py:attribute:: pulse_bias_current_level

    Specifies the pulse bias current level, in amps, that the device
    attempts to generate on the specified channel(s) during the off phase of
    a pulse.

    This property is applicable only if the `Output
    Function <pniDCPower_OutputFunction.html>`__ property is set to **Pulse
    Current**.

    **Valid Values:** The valid values for this property are defined by the
    values you specify for the `Pulse Current Level
    Range <pniDCPower_PulseCurrentLevelRange.html>`__ property.



    .. note:: Refer to `Supported Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

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

            - LabVIEW Property: **Source:Pulse Current:Pulse Bias Current Level**
            - C Attribute: **NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LEVEL**

.. py:attribute:: pulse_bias_current_limit

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



    .. note:: Refer to `Supported Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

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

            - LabVIEW Property: **Source:Pulse Voltage:Pulse Bias Current Limit**
            - C Attribute: **NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT**

.. py:attribute:: pulse_bias_delay

    Determines when, in seconds, the device generates the Pulse Complete
    event after generating the off level of a pulse.

    **Valid Values**: 0 to 167 seconds

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.



    .. note:: Refer to `Supported Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

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

            - LabVIEW Property: **Source:Advanced:Pulse Bias Delay**
            - C Attribute: **NIDCPOWER_ATTR_PULSE_BIAS_DELAY**

.. py:attribute:: pulse_bias_voltage_level

    Specifies the pulse bias voltage level, in volts, that the device
    attempts to generate on the specified channel(s) during the off phase of
    a pulse.

    This property is applicable only if the `Output
    Function <pniDCPower_OutputFunction.html>`__ property is set to **Pulse
    Voltage**.

    **Valid Values:** The valid values for this property are defined by the
    values you specify for the `Pulse Voltage Level
    Range <pniDCPower_PulseVoltageLevelRange.html>`__ property.



    .. note:: Refer to `Supported Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

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

            - LabVIEW Property: **Source:Pulse Voltage:Pulse Bias Voltage Level**
            - C Attribute: **NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LEVEL**

.. py:attribute:: pulse_bias_voltage_limit

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



    .. note:: Refer to `Supported Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

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

            - LabVIEW Property: **Source:Pulse Current:Pulse Bias Voltage Limit**
            - C Attribute: **NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT**

.. py:attribute:: pulse_complete_event_output_terminal

    Specifies the output terminal for exporting the Pulse Complete event.

    Output terminals can be specified in one of two ways. If the device is
    named Dev1 and your terminal is PXI\_Trig0, you can specify the terminal
    with the fully qualified terminal name, /Dev1/PXI\_Trig0, or with the
    shortened terminal name, PXI\_Trig0.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

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

            - LabVIEW Property: **Events:Pulse Complete Event:Output Terminal**
            - C Attribute: **NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_OUTPUT_TERMINAL**

.. py:attribute:: pulse_complete_event_pulse_polarity

    Specifies the behavior of the Pulse Complete event.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

    The following table lists the characteristics of this property.

    +----------------+---------------------+
    | Characteristic | Value               |
    +================+=====================+
    | Datatype       | :py:data:`Polarity` |
    +----------------+---------------------+
    | Permissions    | read-write          |
    +----------------+---------------------+
    | Channel Based  | False               |
    +----------------+---------------------+
    | Resettable     | No                  |
    +----------------+---------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Pulse Complete Event:Pulse:Polarity**
            - C Attribute: **NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_PULSE_POLARITY**

.. py:attribute:: pulse_complete_event_pulse_width

    Specifies the width of the Pulse Complete event, in seconds.

    The minimum event pulse width value for PXI Express devices is 250 ns.

    The maximum event pulse width value for all devices is 1.6 microseconds.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

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

            - LabVIEW Property: **Events:Pulse Complete Event:Pulse:Width**
            - C Attribute: **NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_PULSE_WIDTH**

.. py:attribute:: pulse_current_level

    Specifies the pulse current level, in amps, that the device attempts to
    generate on the specified channel(s) during the on phase of a pulse.

    This property is applicable only if the `Output
    Function <pniDCPower_OutputFunction.html>`__ property is set to **Pulse
    Current**.

    **Valid Values:** The valid values for this property are defined by the
    values you specify for the `Pulse Current Level
    Range <pniDCPower_PulseCurrentLevelRange.html>`__ property.



    .. note:: Refer to `Supported Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

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

            - LabVIEW Property: **Source:Pulse Current:Pulse Current Level**
            - C Attribute: **NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL**

.. py:attribute:: pulse_current_level_range

    Specifies the pulse current level range, in amps, for the specified
    channel(s).

    The range defines the valid values to which you can set the **pulse
    current level** and **pulse bias current level**.

    The Pulse Current Level Range property is applicable only if the `Output
    Function <pniDCPower_OutputFunction.html>`__ property is set to **Pulse
    Current**.

    For valid ranges for your device, refer to
    `Ranges <NI_DC_Power_Supplies_Help.chm::/Ranges.html>`__.



    .. note:: Refer to `Supported Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

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

            - LabVIEW Property: **Source:Pulse Current:Pulse Current Level Range**
            - C Attribute: **NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL_RANGE**

.. py:attribute:: pulse_current_limit

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



    .. note:: Refer to `Supported Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

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

            - LabVIEW Property: **Source:Pulse Voltage:Pulse Current Limit**
            - C Attribute: **NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT**

.. py:attribute:: pulse_current_limit_range

    Specifies the pulse current limit range, in amps, for the specified
    channel(s).

    The range defines the valid values to which you can set the **pulse
    current limit** and **pulse bias current limit**.

    This property is applicable only if the `Output
    Function <pniDCPower_OutputFunction.html>`__ property is set to **Pulse
    Voltage**.

    For valid ranges for your device, refer to
    `Ranges <NI_DC_Power_Supplies_Help.chm::/Ranges.html>`__.



    .. note:: Refer to `Supported Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

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

            - LabVIEW Property: **Source:Pulse Voltage:Pulse Current Limit Range**
            - C Attribute: **NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_RANGE**

.. py:attribute:: pulse_off_time

    Determines the length, in seconds, of the off phase of a pulse.

    **Valid Values**: 50 microseconds to 167 seconds

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.



    .. note:: Refer to `Supported Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

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

            - LabVIEW Property: **Source:Advanced:Pulse Off Time**
            - C Attribute: **NIDCPOWER_ATTR_PULSE_OFF_TIME**

.. py:attribute:: pulse_on_time

    Determines the length, in seconds, of the on phase of a pulse.

    **Valid Values**:50 microseconds to 167 seconds

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.



    .. note:: Refer to `Supported Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

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

            - LabVIEW Property: **Source:Advanced:Pulse On Time**
            - C Attribute: **NIDCPOWER_ATTR_PULSE_ON_TIME**

.. py:attribute:: pulse_trigger_type

    Specifies the behavior of the Pulse trigger.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    **Related topics:**

    `Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

    The following table lists the characteristics of this property.

    +----------------+------------------------+
    | Characteristic | Value                  |
    +================+========================+
    | Datatype       | :py:data:`TriggerType` |
    +----------------+------------------------+
    | Permissions    | read-write             |
    +----------------+------------------------+
    | Channel Based  | False                  |
    +----------------+------------------------+
    | Resettable     | No                     |
    +----------------+------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggers:Pulse Trigger:Trigger Type**
            - C Attribute: **NIDCPOWER_ATTR_PULSE_TRIGGER_TYPE**

.. py:attribute:: pulse_voltage_level

    Specifies the pulse voltage level, in volts, that the device attempts to
    generate on the specified channel(s) during the on phase of a pulse.

    This property is applicable only if the `Output
    Function <pniDCPower_OutputFunction.html>`__ property is set to **Pulse
    Voltage**.

    **Valid Values:** The valid values for this property are defined by the
    values you specify for the `Pulse Voltage Level
    Range <pniDCPower_PulseVoltageLevelRange.html>`__ property.



    .. note:: Refer to `Supported Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

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

            - LabVIEW Property: **Source:Pulse Voltage:Pulse Voltage Level**
            - C Attribute: **NIDCPOWER_ATTR_PULSE_VOLTAGE_LEVEL**

.. py:attribute:: pulse_voltage_level_range

    Specifies the pulse voltage level range, in volts, for the specified
    channel(s).

    The range defines the valid values at which you can set the **pulse
    voltage level** and **pulse bias voltage level**.

    This property is applicable only if the `Output
    Function <pniDCPower_OutputFunction.html>`__ property is set to **Pulse
    Voltage**.

    For valid ranges for your device, refer to
    `Ranges <NI_DC_Power_Supplies_Help.chm::/Ranges.html>`__.



    .. note:: Refer to `Supported Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

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

            - LabVIEW Property: **Source:Pulse Voltage:Pulse Voltage Level Range**
            - C Attribute: **NIDCPOWER_ATTR_PULSE_VOLTAGE_LEVEL_RANGE**

.. py:attribute:: pulse_voltage_limit

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



    .. note:: Refer to `Supported Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

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

            - LabVIEW Property: **Source:Pulse Current:Pulse Voltage Limit**
            - C Attribute: **NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT**

.. py:attribute:: pulse_voltage_limit_range

    Specifies the pulse voltage limit range, in volts, for the specified
    channel(s).

    The range defines the valid values to which you can set the **pulse
    voltage limit** and **pulse bias voltage limit**.

    This property is applicable only if the `Output
    Function <pniDCPower_OutputFunction.html>`__ property is set to **Pulse
    Current**.

    For valid ranges for your device, refer to
    `Ranges <NI_DC_Power_Supplies_Help.chm::/Ranges.html>`__.



    .. note:: The channel must be enabled for the specified pulse current limit to
        take effect. Refer to the `Output
        Enabled <pniDCPower_OutputEnabled.html>`__ property for more information
        about enabling the output channel.

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

            - LabVIEW Property: **Source:Pulse Current:Pulse Voltage Limit Range**
            - C Attribute: **NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_RANGE**

.. py:attribute:: query_instrument_status

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

    The following table lists the characteristics of this property.

    +----------------+---------------------+
    | Characteristic | Value               |
    +================+=====================+
    | Datatype       | :py:data:`tBoolean` |
    +----------------+---------------------+
    | Permissions    | read-write          |
    +----------------+---------------------+
    | Channel Based  | False               |
    +----------------+---------------------+
    | Resettable     | No                  |
    +----------------+---------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Inherent IVI Attributes:User Options:Query Instrument Status**
            - C Attribute: **NIDCPOWER_ATTR_QUERY_INSTRUMENT_STATUS**

.. py:attribute:: range_check

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

    The following table lists the characteristics of this property.

    +----------------+---------------------+
    | Characteristic | Value               |
    +================+=====================+
    | Datatype       | :py:data:`tBoolean` |
    +----------------+---------------------+
    | Permissions    | read-write          |
    +----------------+---------------------+
    | Channel Based  | False               |
    +----------------+---------------------+
    | Resettable     | No                  |
    +----------------+---------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Inherent IVI Attributes:User Options:Range Check**
            - C Attribute: **NIDCPOWER_ATTR_RANGE_CHECK**

.. py:attribute:: ready_for_pulse_trigger_event_output_terminal

    Specifies the output terminal for exporting the Ready For Pulse Trigger
    event.

    Output terminals can be specified in one of two ways. If the device is
    named Dev1 and your terminal is PXI\_Trig0, you can specify the terminal
    with the fully qualified terminal name, /Dev1/PXI\_Trig0, or with the
    shortened terminal name, PXI\_Trig0.



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

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

            - LabVIEW Property: **Events:Ready For Pulse Trigger Event:Output Terminal**
            - C Attribute: **NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_OUTPUT_TERMINAL**

.. py:attribute:: ready_for_pulse_trigger_event_pulse_polarity

    Specifies the behavior of the Ready For Pulse Trigger event.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

    The following table lists the characteristics of this property.

    +----------------+---------------------+
    | Characteristic | Value               |
    +================+=====================+
    | Datatype       | :py:data:`Polarity` |
    +----------------+---------------------+
    | Permissions    | read-write          |
    +----------------+---------------------+
    | Channel Based  | False               |
    +----------------+---------------------+
    | Resettable     | No                  |
    +----------------+---------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Ready For Pulse Trigger Event:Pulse:Polarity**
            - C Attribute: **NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_PULSE_POLARITY**

.. py:attribute:: ready_for_pulse_trigger_event_pulse_width

    Specifies the width of the Ready For Pulse Trigger event, in seconds.

    The minimum event pulse width value for PXI Express devices is 250 ns.

    The maximum event pulse width value for all devices is 1.6 microseconds.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

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

            - LabVIEW Property: **Events:Ready For Pulse Trigger Event:Pulse:Width**
            - C Attribute: **NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_PULSE_WIDTH**

.. py:attribute:: record_coercions

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

    The following table lists the characteristics of this property.

    +----------------+---------------------+
    | Characteristic | Value               |
    +================+=====================+
    | Datatype       | :py:data:`tBoolean` |
    +----------------+---------------------+
    | Permissions    | read-write          |
    +----------------+---------------------+
    | Channel Based  | False               |
    +----------------+---------------------+
    | Resettable     | No                  |
    +----------------+---------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Inherent IVI Attributes:User Options:Record Value Coercions**
            - C Attribute: **NIDCPOWER_ATTR_RECORD_COERCIONS**

.. py:attribute:: reset_average_before_measurement

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



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

    The following table lists the characteristics of this property.

    +----------------+---------------------+
    | Characteristic | Value               |
    +================+=====================+
    | Datatype       | :py:data:`tBoolean` |
    +----------------+---------------------+
    | Permissions    | read-write          |
    +----------------+---------------------+
    | Channel Based  | False               |
    +----------------+---------------------+
    | Resettable     | No                  |
    +----------------+---------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Measurement:Advanced:Reset Average Before Measurement**
            - C Attribute: **NIDCPOWER_ATTR_RESET_AVERAGE_BEFORE_MEASUREMENT**

.. py:attribute:: samples_to_average

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

            - LabVIEW Property: **Measurement:Samples To Average**
            - C Attribute: **NIDCPOWER_ATTR_SAMPLES_TO_AVERAGE**

.. py:attribute:: self_calibration_persistence

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



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

    The following table lists the characteristics of this property.

    +----------------+---------------------------------------+
    | Characteristic | Value                                 |
    +================+=======================================+
    | Datatype       | :py:data:`SelfCalibrationPersistence` |
    +----------------+---------------------------------------+
    | Permissions    | read-write                            |
    +----------------+---------------------------------------+
    | Channel Based  | False                                 |
    +----------------+---------------------------------------+
    | Resettable     | No                                    |
    +----------------+---------------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Advanced:Self-Calibration Persistence**
            - C Attribute: **NIDCPOWER_ATTR_SELF_CALIBRATION_PERSISTENCE**

.. py:attribute:: sense

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

    The following table lists the characteristics of this property.

    +----------------+------------------+
    | Characteristic | Value            |
    +================+==================+
    | Datatype       | :py:data:`Sense` |
    +----------------+------------------+
    | Permissions    | read-write       |
    +----------------+------------------+
    | Channel Based  | False            |
    +----------------+------------------+
    | Resettable     | No               |
    +----------------+------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Measurement:Sense**
            - C Attribute: **NIDCPOWER_ATTR_SENSE**

.. py:attribute:: sequence_advance_trigger_type

    Specifies the behavior of the Sequence Advance trigger.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    **Related topics:**

    `Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

    The following table lists the characteristics of this property.

    +----------------+------------------------+
    | Characteristic | Value                  |
    +================+========================+
    | Datatype       | :py:data:`TriggerType` |
    +----------------+------------------------+
    | Permissions    | read-write             |
    +----------------+------------------------+
    | Channel Based  | False                  |
    +----------------+------------------------+
    | Resettable     | No                     |
    +----------------+------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggers:Sequence Advance Trigger:Trigger Type**
            - C Attribute: **NIDCPOWER_ATTR_SEQUENCE_ADVANCE_TRIGGER_TYPE**

.. py:attribute:: sequence_engine_done_event_output_terminal

    Specifies the output terminal for exporting the Sequence Engine Done
    Complete event.

    Output terminals can be specified in one of two ways. If the device is
    named Dev1 and your terminal is PXI\_Trig0, you can specify the terminal
    with the fully qualified terminal name, /Dev1/PXI\_Trig0, or with the
    shortened terminal name, PXI\_Trig0.



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

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

            - LabVIEW Property: **Events:Sequence Engine Done Event:Output Terminal**
            - C Attribute: **NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_OUTPUT_TERMINAL**

.. py:attribute:: sequence_engine_done_event_pulse_polarity

    Specifies the behavior of the Sequence Engine Done event.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

    The following table lists the characteristics of this property.

    +----------------+---------------------+
    | Characteristic | Value               |
    +================+=====================+
    | Datatype       | :py:data:`Polarity` |
    +----------------+---------------------+
    | Permissions    | read-write          |
    +----------------+---------------------+
    | Channel Based  | False               |
    +----------------+---------------------+
    | Resettable     | No                  |
    +----------------+---------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Sequence Engine Done Event:Pulse:Polarity**
            - C Attribute: **NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_PULSE_POLARITY**

.. py:attribute:: sequence_engine_done_event_pulse_width

    Specifies the width of the Sequence Engine Done event, in seconds.

    The minimum event pulse width value for the NI PXI-4132 is 150 ns, and
    the minimum event pulse width value for PXI Express devices is 250 ns.

    The maximum event pulse width value for all devices is 1.6 microseconds.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

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

            - LabVIEW Property: **Events:Sequence Engine Done Event:Pulse:Width**
            - C Attribute: **NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_PULSE_WIDTH**

.. py:attribute:: sequence_iteration_complete_event_output_terminal

    Specifies the output terminal for exporting the Sequence Iteration
    Complete event.

    Output terminals can be specified in one of two ways. If the device is
    named Dev1 and your terminal is PXI\_Trig0, you can specify the terminal
    with the fully qualified terminal name, /Dev1/PXI\_Trig0, or with the
    shortened terminal name, PXI\_Trig0.



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

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

            - LabVIEW Property: **Events:Sequence Iteration Complete Event:Output Terminal**
            - C Attribute: **NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_OUTPUT_TERMINAL**

.. py:attribute:: sequence_iteration_complete_event_pulse_polarity

    Specifies the behavior of the Sequence Iteration Complete event.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

    The following table lists the characteristics of this property.

    +----------------+---------------------+
    | Characteristic | Value               |
    +================+=====================+
    | Datatype       | :py:data:`Polarity` |
    +----------------+---------------------+
    | Permissions    | read-write          |
    +----------------+---------------------+
    | Channel Based  | False               |
    +----------------+---------------------+
    | Resettable     | No                  |
    +----------------+---------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Sequence Iteration Complete Event:Pulse:Polarity**
            - C Attribute: **NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_POLARITY**

.. py:attribute:: sequence_iteration_complete_event_pulse_width

    Specifies the width of the Sequence Iteration Complete event, in
    seconds.

    The minimum event pulse width value for the NI PXI-4132 is 150 ns, and
    the minimum event pulse width value for PXI Express devices is 250 ns.

    The maximum event pulse width value for all devices is 1.6 microseconds.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

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

            - LabVIEW Property: **Events:Sequence Iteration Complete Event:Pulse:Width**
            - C Attribute: **NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_WIDTH**

.. py:attribute:: sequence_loop_count

    Specifies the number of times a sequence is run after initiation.

    Refer to the `Sequence Source
    Mode <NI_DC_Power_Supplies_Help.chm::/Sequencing.html>`__ topic in the
    *NI DC Power Supplies and SMUs Help* for more information about the
    sequence loop count.

    **Valid Range**: 1 to 134217727

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices. When the `Sequence Loop Count Is
        Finite <pniDCPower_SequenceLoopCountIsFinite.html>`__ property is set to
        FALSE, the Sequence Loop Count property is ignored.

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

            - LabVIEW Property: **Source:Advanced:Sequence Loop Count**
            - C Attribute: **NIDCPOWER_ATTR_SEQUENCE_LOOP_COUNT**

.. py:attribute:: sequence_loop_count_is_finite

    Specifies whether a sequence should repeat indefinitely.

    Refer to the `Sequence Source
    Mode <NI_DC_Power_Supplies_Help.chm::/Sequencing.html>`__ topic in the
    *NI DC Power Supplies and SMUs Help* for more information about infinite
    sequencing.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices. When the Sequence Loop Count Is
        Finite property is set to FALSE, the `Sequence Loop
        Count <pniDCPower_SequenceLoopCount.html>`__ property is ignored.

    The following table lists the characteristics of this property.

    +----------------+---------------------+
    | Characteristic | Value               |
    +================+=====================+
    | Datatype       | :py:data:`tBoolean` |
    +----------------+---------------------+
    | Permissions    | read-write          |
    +----------------+---------------------+
    | Channel Based  | False               |
    +----------------+---------------------+
    | Resettable     | No                  |
    +----------------+---------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Source:Advanced:Sequence Loop Count Is Finite**
            - C Attribute: **NIDCPOWER_ATTR_SEQUENCE_LOOP_COUNT_IS_FINITE**

.. py:attribute:: simulate

    Specifies whether to simulate NI-DCPower I/O operations. TRUE specifies
    that operation is simulated.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    The following table lists the characteristics of this property.

    +----------------+---------------------+
    | Characteristic | Value               |
    +================+=====================+
    | Datatype       | :py:data:`tBoolean` |
    +----------------+---------------------+
    | Permissions    | read-write          |
    +----------------+---------------------+
    | Channel Based  | False               |
    +----------------+---------------------+
    | Resettable     | No                  |
    +----------------+---------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Inherent IVI Attributes:User Options:Simulate**
            - C Attribute: **NIDCPOWER_ATTR_SIMULATE**

.. py:attribute:: source_complete_event_output_terminal

    Specifies the output terminal for exporting the Source Complete event.

    Output terminals can be specified in one of two ways. If the device is
    named Dev1 and your terminal is PXI\_Trig0, you can specify the terminal
    with the fully qualified terminal name, /Dev1/PXI\_Trig0, or with the
    shortened terminal name, PXI\_Trig0.



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

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

            - LabVIEW Property: **Events:Source Complete Event:Output Terminal**
            - C Attribute: **NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_OUTPUT_TERMINAL**

.. py:attribute:: source_complete_event_pulse_polarity

    Specifies the behavior of the Source Complete event.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

    The following table lists the characteristics of this property.

    +----------------+---------------------+
    | Characteristic | Value               |
    +================+=====================+
    | Datatype       | :py:data:`Polarity` |
    +----------------+---------------------+
    | Permissions    | read-write          |
    +----------------+---------------------+
    | Channel Based  | False               |
    +----------------+---------------------+
    | Resettable     | No                  |
    +----------------+---------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Source Complete Event:Pulse:Polarity**
            - C Attribute: **NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_PULSE_POLARITY**

.. py:attribute:: source_complete_event_pulse_width

    Specifies the width of the Source Complete event, in seconds.

    The minimum event pulse width value for the NI PXI-4132 is 150 ns, and
    the minimum event pulse width value for PXI Express devices is 250 ns.

    The maximum event pulse width value for all devices is 1.6 microseconds.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

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

            - LabVIEW Property: **Events:Source Complete Event:Pulse:Width**
            - C Attribute: **NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_PULSE_WIDTH**

.. py:attribute:: source_delay

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



    .. note:: Refer to `Supported Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

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

            - LabVIEW Property: **Source:Advanced:Source Delay**
            - C Attribute: **NIDCPOWER_ATTR_SOURCE_DELAY**

.. py:attribute:: source_mode

    Specifies whether to run a single output point or a sequence. Refer to
    the `Single Point source
    mode <NI_DC_Power_Supplies_Help.chm::/Singlept.html>`__ and `Sequence
    source mode <NI_DC_Power_Supplies_Help.chm::/Sequencing.html>`__ topics
    in the *NI DC Power Supplies and SMUs Help* for more information about
    source modes.

    **Default Value**: Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    The following table lists the characteristics of this property.

    +----------------+-----------------------+
    | Characteristic | Value                 |
    +================+=======================+
    | Datatype       | :py:data:`SourceMode` |
    +----------------+-----------------------+
    | Permissions    | read-write            |
    +----------------+-----------------------+
    | Channel Based  | False                 |
    +----------------+-----------------------+
    | Resettable     | No                    |
    +----------------+-----------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Source:Source Mode**
            - C Attribute: **NIDCPOWER_ATTR_SOURCE_MODE**

.. py:attribute:: source_trigger_type

    Specifies the behavior of the Source trigger.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    **Related topics:**

    `Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

    The following table lists the characteristics of this property.

    +----------------+------------------------+
    | Characteristic | Value                  |
    +================+========================+
    | Datatype       | :py:data:`TriggerType` |
    +----------------+------------------------+
    | Permissions    | read-write             |
    +----------------+------------------------+
    | Channel Based  | False                  |
    +----------------+------------------------+
    | Resettable     | No                     |
    +----------------+------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggers:Source Trigger:Trigger Type**
            - C Attribute: **NIDCPOWER_ATTR_SOURCE_TRIGGER_TYPE**

.. py:attribute:: specific_driver_class_spec_major_version

    Contains the major version number of the class specification with which
    NI-DCPower is compliant.

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
            - C Attribute: **NIDCPOWER_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION**

.. py:attribute:: specific_driver_class_spec_minor_version

    Contains the minor version number of the class specification with which
    NI-DCPower is compliant.

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
            - C Attribute: **NIDCPOWER_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION**

.. py:attribute:: specific_driver_description

    Contains a brief description of the specific driver.

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
            - C Attribute: **NIDCPOWER_ATTR_SPECIFIC_DRIVER_DESCRIPTION**

.. py:attribute:: specific_driver_prefix

    Contains the prefix for NI-DCPower. The name of each user-callable VI in
    NI-DCPower begins with this prefix.

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

            - LabVIEW Property: **Inherent IVI Attributes:Driver Identification:Driver Prefix**
            - C Attribute: **NIDCPOWER_ATTR_SPECIFIC_DRIVER_PREFIX**

.. py:attribute:: specific_driver_revision

    Contains additional version information about NI-DCPower.

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

            - LabVIEW Property: **Inherent IVI Attributes:Driver Identification:Revision**
            - C Attribute: **NIDCPOWER_ATTR_SPECIFIC_DRIVER_REVISION**

.. py:attribute:: specific_driver_vendor

    Contains the name of the vendor that supplies NI-DCPower.

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
            - C Attribute: **NIDCPOWER_ATTR_SPECIFIC_DRIVER_VENDOR**

.. py:attribute:: start_trigger_type

    Specifies the behavior of the Start trigger.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.

    **Related topics:**

    `Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

    The following table lists the characteristics of this property.

    +----------------+------------------------+
    | Characteristic | Value                  |
    +================+========================+
    | Datatype       | :py:data:`TriggerType` |
    +----------------+------------------------+
    | Permissions    | read-write             |
    +----------------+------------------------+
    | Channel Based  | False                  |
    +----------------+------------------------+
    | Resettable     | No                     |
    +----------------+------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggers:Start Trigger:Trigger Type**
            - C Attribute: **NIDCPOWER_ATTR_START_TRIGGER_TYPE**

.. py:attribute:: supported_instrument_models

    Contains a comma-separated (,) list of supported NI-DCPower device
    models.

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
            - C Attribute: **NIDCPOWER_ATTR_SUPPORTED_INSTRUMENT_MODELS**

.. py:attribute:: transient_response

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



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

    The following table lists the characteristics of this property.

    +----------------+------------------------------+
    | Characteristic | Value                        |
    +================+==============================+
    | Datatype       | :py:data:`TransientResponse` |
    +----------------+------------------------------+
    | Permissions    | read-write                   |
    +----------------+------------------------------+
    | Channel Based  | False                        |
    +----------------+------------------------------+
    | Resettable     | No                           |
    +----------------+------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Source:Transient Response**
            - C Attribute: **NIDCPOWER_ATTR_TRANSIENT_RESPONSE**

.. py:attribute:: voltage_compensation_frequency

    The frequency at which a pole-zero pair is added to the system when the
    channel is in `Constant
    Voltage <NI_DC_Power_Supplies_Help.chm::/Constant_Voltage.html>`__ mode.

    **Default Value**:Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

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

            - LabVIEW Property: **Source:Custom Transient Response:Voltage:Compensation Frequency**
            - C Attribute: **NIDCPOWER_ATTR_VOLTAGE_COMPENSATION_FREQUENCY**

.. py:attribute:: voltage_gain_bandwidth

    The frequency at which the unloaded loop gain extrapolates to 0 dB in
    the absence of additional poles and zeroes. This property takes effect
    when the channel is in `Constant
    Voltage <NI_DC_Power_Supplies_Help.chm::/Constant_Voltage.html>`__ mode.

    **Default Value**: Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

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

            - LabVIEW Property: **Source:Custom Transient Response:Voltage:Gain Bandwidth**
            - C Attribute: **NIDCPOWER_ATTR_VOLTAGE_GAIN_BANDWIDTH**

.. py:attribute:: voltage_level

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



    .. note:: The channel must be enabled for the specified voltage level to take
        effect. Refer to the `Output Enabled <pniDCPower_OutputEnabled.html>`__
        property for more information about enabling the output channel.

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

            - LabVIEW Property: **Source:DC Voltage:Voltage Level**
            - C Attribute: **NIDCPOWER_ATTR_VOLTAGE_LEVEL**

.. py:attribute:: voltage_level_autorange

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

    The following table lists the characteristics of this property.

    +----------------+----------------------------------+
    | Characteristic | Value                            |
    +================+==================================+
    | Datatype       | :py:data:`VoltageLevelAutorange` |
    +----------------+----------------------------------+
    | Permissions    | read-write                       |
    +----------------+----------------------------------+
    | Channel Based  | False                            |
    +----------------+----------------------------------+
    | Resettable     | No                               |
    +----------------+----------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Source:DC Voltage:Voltage Level Autorange**
            - C Attribute: **NIDCPOWER_ATTR_VOLTAGE_LEVEL_AUTORANGE**

.. py:attribute:: voltage_level_range

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



    .. note:: The channel must be enabled for the specified voltage level range to
        take effect. Refer to the `Output
        Enabled <pniDCPower_OutputEnabled.html>`__ property for more information
        about enabling the output channel.

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

            - LabVIEW Property: **Source:DC Voltage:Voltage Level Range**
            - C Attribute: **NIDCPOWER_ATTR_VOLTAGE_LEVEL_RANGE**

.. py:attribute:: voltage_limit

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



    .. note:: The channel must be enabled for the specified current level to take
        effect. Refer to the `Output Enabled <pniDCPower_OutputEnabled.html>`__
        property for more information about enabling the output channel.

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

            - LabVIEW Property: **Source:DC Current:Voltage Limit**
            - C Attribute: **NIDCPOWER_ATTR_VOLTAGE_LIMIT**

.. py:attribute:: voltage_limit_autorange

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

    The following table lists the characteristics of this property.

    +----------------+----------------------------------+
    | Characteristic | Value                            |
    +================+==================================+
    | Datatype       | :py:data:`VoltageLimitAutorange` |
    +----------------+----------------------------------+
    | Permissions    | read-write                       |
    +----------------+----------------------------------+
    | Channel Based  | False                            |
    +----------------+----------------------------------+
    | Resettable     | No                               |
    +----------------+----------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Source:DC Current:Voltage Limit Autorange**
            - C Attribute: **NIDCPOWER_ATTR_VOLTAGE_LIMIT_AUTORANGE**

.. py:attribute:: voltage_limit_range

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



    .. note:: The channel must be enabled for the specified voltage limit range to
        take effect. Refer to the `Output
        Enabled <pniDCPower_OutputEnabled.html>`__ property for more information
        about enabling the output channel.

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

            - LabVIEW Property: **Source:DC Current:Voltage Limit Range**
            - C Attribute: **NIDCPOWER_ATTR_VOLTAGE_LIMIT_RANGE**

.. py:attribute:: voltage_pole_zero_ratio

    The ratio of the pole frequency to the zero frequency when the channel
    is in `Constant
    Voltage <NI_DC_Power_Supplies_Help.chm::/Constant_Voltage.html>`__ mode.

    **Default Value**: Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.



    .. note:: This property is not supported by all devices. Refer to `Supported
        Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.

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

            - LabVIEW Property: **Source:Custom Transient Response:Voltage:Pole-Zero Ratio**
            - C Attribute: **NIDCPOWER_ATTR_VOLTAGE_POLE_ZERO_RATIO**


