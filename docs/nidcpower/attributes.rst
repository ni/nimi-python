nidcpower.Session properties
============================

.. py:currentmodule:: nidcpower.Session

.. py:attribute:: active_advanced_sequence

    Specifies the advanced sequence to configure or generate.



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic.


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        active_advanced_sequence.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        active_advanced_sequence.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].active_advanced_sequence = var
            var = session['0,1'].active_advanced_sequence

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | str        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Source:Advanced:Active Advanced Sequence**
            - C Attribute: **NIDCPOWER_ATTR_ACTIVE_ADVANCED_SEQUENCE**

.. py:attribute:: active_advanced_sequence_step

    Specifies the advanced sequence step to configure.



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic.


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        active_advanced_sequence_step.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        active_advanced_sequence_step.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].active_advanced_sequence_step = var
            var = session['0,1'].active_advanced_sequence_step

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Source:Advanced:Active Advanced Sequence Step**
            - C Attribute: **NIDCPOWER_ATTR_ACTIVE_ADVANCED_SEQUENCE_STEP**

.. py:attribute:: aperture_time

    Specifies the measurement aperture time for the channel configuration. Aperture time is specified in the units set by  the :py:data:`nidcpower.Session.aperture_time_units` property.
    for information about supported devices.
    Refer to the Aperture Time topic in the NI DC Power Supplies and SMUs Help for more information about how to configure  your measurements and for information about valid values.
    Default Value: 0.01666666 seconds



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        aperture_time.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        aperture_time.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].aperture_time = var
            var = session['0,1'].aperture_time

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

            - LabVIEW Property: **Measurement:Aperture Time**
            - C Attribute: **NIDCPOWER_ATTR_APERTURE_TIME**

.. py:attribute:: aperture_time_units

    Specifies the units of the :py:data:`nidcpower.Session.aperture_time` property for the channel configuration.
    for information about supported devices.
    Refer to the Aperture Time topic in the NI DC Power Supplies and SMUs Help for more information about  how to configure your measurements and for information about valid values.
    Default Value: :py:data:`~nidcpower.ApertureTimeUnits.SECONDS`



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        aperture_time_units.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        aperture_time_units.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].aperture_time_units = var
            var = session['0,1'].aperture_time_units

    The following table lists the characteristics of this property.

    +----------------+--------------------------+
    | Characteristic | Value                    |
    +================+==========================+
    | Datatype       | _enums.ApertureTimeUnits |
    +----------------+--------------------------+
    | Permissions    | read-write               |
    +----------------+--------------------------+
    | Channel Based  | True                     |
    +----------------+--------------------------+
    | Resettable     | No                       |
    +----------------+--------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Measurement:Aperture Time Units**
            - C Attribute: **NIDCPOWER_ATTR_APERTURE_TIME_UNITS**

.. py:attribute:: auto_zero

    Specifies the auto-zero method to use on the device.
    Refer to the NI PXI-4132 Measurement Configuration and Timing and Auto Zero topics for more information  about how to configure your measurements.
    Default Value: The default value for the NI PXI-4132 is :py:data:`~nidcpower.AutoZero.ON`. The default value for  all other devices is :py:data:`~nidcpower.AutoZero.OFF`, which is the only supported value for these devices.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        auto_zero.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        auto_zero.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].auto_zero = var
            var = session['0,1'].auto_zero

    The following table lists the characteristics of this property.

    +----------------+-----------------+
    | Characteristic | Value           |
    +================+=================+
    | Datatype       | _enums.AutoZero |
    +----------------+-----------------+
    | Permissions    | read-write      |
    +----------------+-----------------+
    | Channel Based  | True            |
    +----------------+-----------------+
    | Resettable     | No              |
    +----------------+-----------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Measurement:Auto Zero**
            - C Attribute: **NIDCPOWER_ATTR_AUTO_ZERO**

.. py:attribute:: auxiliary_power_source_available

    Indicates whether an auxiliary power source is connected to the device.
    A value of False may indicate that the auxiliary input fuse has blown.  Refer to the Detecting Internal/Auxiliary Power topic in the NI DC Power Supplies and SMUs Help for  more information about internal and auxiliary power.
    power source to generate power. Use the :py:data:`nidcpower.Session.power_source_in_use` property to retrieve this information.



    .. note:: This property does not necessarily indicate if the device is using the auxiliary

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

            - LabVIEW Property: **Advanced:Auxiliary Power Source Available**
            - C Attribute: **NIDCPOWER_ATTR_AUXILIARY_POWER_SOURCE_AVAILABLE**

.. py:attribute:: cache

    Specifies whether to cache the value of properties.
    When caching is enabled, NI-DCPower records the current power supply settings and avoids sending  redundant commands to the device. Enabling caching can significantly increase execution speed.
    NI-DCPower might always cache or never cache particular properties regardless of the setting of this property.
    Use the :py:meth:`nidcpower.Session._initialize_with_channels` method to override this value.
    Default Value: True

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
            - C Attribute: **NIDCPOWER_ATTR_CACHE**

.. py:attribute:: channel_count

    Indicates the number of channels that NI-DCPower supports for the instrument that was chosen when  the current session was opened. For channel-based properties, the IVI engine maintains a separate  cache value for each channel.

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

.. py:attribute:: compliance_limit_symmetry

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



    .. note:: Refer to `Supported Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        information about supported devices.


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        compliance_limit_symmetry.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        compliance_limit_symmetry.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].compliance_limit_symmetry = var
            var = session['0,1'].compliance_limit_symmetry

    The following table lists the characteristics of this property.

    +----------------+--------------------------------+
    | Characteristic | Value                          |
    +================+================================+
    | Datatype       | _enums.ComplianceLimitSymmetry |
    +----------------+--------------------------------+
    | Permissions    | read-write                     |
    +----------------+--------------------------------+
    | Channel Based  | True                           |
    +----------------+--------------------------------+
    | Resettable     | No                             |
    +----------------+--------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Source:Advanced:Compliance Limit Symmetry**
            - C Attribute: **NIDCPOWER_ATTR_COMPLIANCE_LIMIT_SYMMETRY**

.. py:attribute:: current_compensation_frequency

    The frequency at which a pole-zero pair is added to the system when the channel is in  Constant Current mode.
    for information about supported devices.
    Default Value: Determined by the value of the :py:data:`~nidcpower.TransientResponse.NORMAL` setting of the  :py:data:`nidcpower.Session.transient_response` property.



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        current_compensation_frequency.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        current_compensation_frequency.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].current_compensation_frequency = var
            var = session['0,1'].current_compensation_frequency

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

            - LabVIEW Property: **Source:Custom Transient Response:Current:Compensation Frequency**
            - C Attribute: **NIDCPOWER_ATTR_CURRENT_COMPENSATION_FREQUENCY**

.. py:attribute:: current_gain_bandwidth

    The frequency at which the unloaded loop gain extrapolates to 0 dB in the absence of additional poles and zeroes.  This property takes effect when the channel is in Constant Current mode.
    for information about supported devices.
    Default Value: Determined by the value of the :py:data:`~nidcpower.TransientResponse.NORMAL` setting of the  :py:data:`nidcpower.Session.transient_response` property.



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        current_gain_bandwidth.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        current_gain_bandwidth.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].current_gain_bandwidth = var
            var = session['0,1'].current_gain_bandwidth

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

            - LabVIEW Property: **Source:Custom Transient Response:Current:Gain Bandwidth**
            - C Attribute: **NIDCPOWER_ATTR_CURRENT_GAIN_BANDWIDTH**

.. py:attribute:: current_level

    Specifies the current level, in amps, that the device attempts to generate on the specified channel(s).
    This property is applicable only if the :py:data:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.DC_CURRENT`.
    :py:data:`nidcpower.Session.output_enabled` property for more information about enabling the output channel.
    Valid Values: The valid values for this property are defined by the values to which the  :py:data:`nidcpower.Session.current_level_range` property is set.



    .. note:: The channel must be enabled for the specified current level to take effect. Refer to the


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        current_level.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        current_level.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].current_level = var
            var = session['0,1'].current_level

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

            - LabVIEW Property: **Source:DC Current:Current Level**
            - C Attribute: **NIDCPOWER_ATTR_CURRENT_LEVEL**

.. py:attribute:: current_level_autorange

    Specifies whether NI-DCPower automatically selects the current level range based on the desired current level for  the specified channels.
    If you set this property to :py:data:`~nidcpower.AutoZero.ON`, NI-DCPower ignores any changes you make to the  :py:data:`nidcpower.Session.current_level_range` property. If you change the :py:data:`nidcpower.Session.current_level_autorange` property from  :py:data:`~nidcpower.AutoZero.ON` to :py:data:`~nidcpower.AutoZero.OFF`, NI-DCPower retains the last value the :py:data:`nidcpower.Session.current_level_range`  property was set to (or the default value if the property was never set) and uses that value as the  current level range.
    Query the :py:data:`nidcpower.Session.current_level_range` property by using the :py:meth:`nidcpower.Session._get_attribute_vi_int32` method for  information about which range NI-DCPower automatically selects.
    The :py:data:`nidcpower.Session.current_level_autorange` property is applicable only if the :py:data:`nidcpower.Session.output_function` property  is set to :py:data:`~nidcpower.OutputFunction.DC_CURRENT`.
    Default Value: :py:data:`~nidcpower.AutoZero.OFF`




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        current_level_autorange.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        current_level_autorange.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].current_level_autorange = var
            var = session['0,1'].current_level_autorange

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

            - LabVIEW Property: **Source:DC Current:Current Level Autorange**
            - C Attribute: **NIDCPOWER_ATTR_CURRENT_LEVEL_AUTORANGE**

.. py:attribute:: current_level_range

    Specifies the current level range, in amps, for the specified channel(s).
    The range defines the valid value to which the current level can be set. Use the  :py:data:`nidcpower.Session.current_level_autorange` property to enable automatic selection of the current level range.
    The :py:data:`nidcpower.Session.current_level_range` property is applicable only if the :py:data:`nidcpower.Session.output_function` property is  set to :py:data:`~nidcpower.OutputFunction.DC_CURRENT`.
    :py:data:`nidcpower.Session.output_enabled` property for more information about enabling the output channel.
    For valid ranges, refer to the Ranges topic for your device in the NI DC Power Supplies and SMUs Help.



    .. note:: The channel must be enabled for the specified current level range to take effect. Refer to the


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        current_level_range.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        current_level_range.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].current_level_range = var
            var = session['0,1'].current_level_range

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

            - LabVIEW Property: **Source:DC Current:Current Level Range**
            - C Attribute: **NIDCPOWER_ATTR_CURRENT_LEVEL_RANGE**

.. py:attribute:: current_limit

    Specifies the current limit, in amps, that the output cannot exceed when generating the desired voltage level  on the specified channel(s).
    This property is applicable only if the :py:data:`nidcpower.Session.output_function` property is set to  :py:data:`~nidcpower.OutputFunction.DC_VOLTAGE` and the :py:data:`nidcpower.Session.compliance_limit_symmetry` property is set to  :py:data:`~nidcpower.NIDCPOWER_VAL_SYMMETRIC`.
    :py:data:`nidcpower.Session.output_enabled` property for more information about enabling the output channel.
    Valid Values: The valid values for this property are defined by the values to which  :py:data:`nidcpower.Session.current_limit_range` property is set.



    .. note:: The channel must be enabled for the specified current limit to take effect. Refer to the

    .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        current_limit.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        current_limit.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].current_limit = var
            var = session['0,1'].current_limit

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

            - LabVIEW Property: **Source:DC Voltage:Current Limit**
            - C Attribute: **NIDCPOWER_ATTR_CURRENT_LIMIT**

.. py:attribute:: current_limit_autorange

    Specifies whether NI-DCPower automatically selects the current limit range based on the desired current limit for the  specified channel(s).
    If you set this property to :py:data:`~nidcpower.AutoZero.ON`, NI-DCPower ignores any changes you make to the  :py:data:`nidcpower.Session.current_limit_range` property. If you change this property from :py:data:`~nidcpower.AutoZero.ON` to  :py:data:`~nidcpower.AutoZero.OFF`, NI-DCPower retains the last value the :py:data:`nidcpower.Session.current_limit_range` property was set to  (or the default value if the property was never set) and uses that value as the current limit range.
    Query the :py:data:`nidcpower.Session.current_limit_range` property by using the :py:meth:`nidcpower.Session._get_attribute_vi_int32` method for  information about which range NI-DCPower automatically selects.
    The :py:data:`nidcpower.Session.current_limit_autorange` property is applicable only if the :py:data:`nidcpower.Session.output_function` property  is set to :py:data:`~nidcpower.OutputFunction.DC_VOLTAGE`.
    Default Value: :py:data:`~nidcpower.AutoZero.OFF`




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        current_limit_autorange.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        current_limit_autorange.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].current_limit_autorange = var
            var = session['0,1'].current_limit_autorange

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

            - LabVIEW Property: **Source:DC Voltage:Current Limit Autorange**
            - C Attribute: **NIDCPOWER_ATTR_CURRENT_LIMIT_AUTORANGE**

.. py:attribute:: current_limit_high

    Specifies the maximum current, in amps, that the output can produce when
    generating the desired voltage on the specified channel(s).
    This property is applicable only if the `Compliance Limit
    Symmetry <p:py:meth:`nidcpower.Session.ComplianceLimitSymmetry`.html>`__ property is set to
    **Asymmetric** and the `Output
    Method <p:py:meth:`nidcpower.Session.OutputFunction`.html>`__ property is set to **DC
    Voltage**.
    You must also specify a `Current Limit
    Low <p:py:meth:`nidcpower.Session.CurrentLimitLow`.html>`__ to complete the asymmetric
    range.
    **Valid Values:** [1% of `Current Limit
    Range <p:py:meth:`nidcpower.Session.CurrentLimitRange`.html>`__, `Current Limit
    Range <p:py:meth:`nidcpower.Session.CurrentLimitRange`.html>`__]
    The range bounded by the limit high and limit low must include zero.
    **Default Value:** Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.
    **Related Topics:**
    `Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
    `Changing
    Ranges <NI_DC_Power_Supplies_Help.chm::/changing_ranges.html>`__
    `Overranging <NI_DC_Power_Supplies_Help.chm::/overranging.html>`__



    .. note:: The limit may be extended beyond the selected limit range if the
        `Overranging Enabled <p:py:meth:`nidcpower.Session.OverrangingEnabled`.html>`__ property is
        set to TRUE.

    .. note:: One or more of the referenced methods are not in the Python API for this driver.


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        current_limit_high.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        current_limit_high.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].current_limit_high = var
            var = session['0,1'].current_limit_high

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

            - LabVIEW Property: **Source:DC Voltage:Current Limit High**
            - C Attribute: **NIDCPOWER_ATTR_CURRENT_LIMIT_HIGH**

.. py:attribute:: current_limit_low

    Specifies the minimum current, in amps, that the output can produce when
    generating the desired voltage on the specified channel(s).
    This property is applicable only if the `Compliance Limit
    Symmetry <p:py:meth:`nidcpower.Session.ComplianceLimitSymmetry`.html>`__ property is set to
    **Asymmetric** and the `Output
    Method <p:py:meth:`nidcpower.Session.OutputFunction`.html>`__ property is set to **DC
    Voltage**.
    You must also specify a `Current Limit
    High <p:py:meth:`nidcpower.Session.CurrentLimitHigh`.html>`__ to complete the asymmetric
    range.
    **Valid Values:** [-`Current Limit
    Range <p:py:meth:`nidcpower.Session.CurrentLimitRange`.html>`__, -1% of `Current Limit
    Range <p:py:meth:`nidcpower.Session.CurrentLimitRange`.html>`__]
    The range bounded by the limit high and limit low must include zero.
    **Default Value:** Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.
    **Related Topics:**
    `Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
    `Changing
    Ranges <NI_DC_Power_Supplies_Help.chm::/changing_ranges.html>`__
    `Overranging <NI_DC_Power_Supplies_Help.chm::/overranging.html>`__



    .. note:: The limit may be extended beyond the selected limit range if the
        `Overranging Enabled <p:py:meth:`nidcpower.Session.OverrangingEnabled`.html>`__ property is
        set to TRUE.

    .. note:: One or more of the referenced methods are not in the Python API for this driver.


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        current_limit_low.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        current_limit_low.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].current_limit_low = var
            var = session['0,1'].current_limit_low

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

            - LabVIEW Property: **Source:DC Voltage:Current Limit Low**
            - C Attribute: **NIDCPOWER_ATTR_CURRENT_LIMIT_LOW**

.. py:attribute:: current_limit_range

    Specifies the current limit range, in amps, for the specified channel(s).
    The range defines the valid value to which the current limit can be set. Use the :py:data:`nidcpower.Session.current_limit_autorange`  property to enable automatic selection of the current limit range.
    The :py:data:`nidcpower.Session.current_limit_range` property is applicable only if the :py:data:`nidcpower.Session.output_function` property  is set to :py:data:`~nidcpower.OutputFunction.DC_VOLTAGE`.
    :py:data:`nidcpower.Session.output_enabled` property for more information about enabling the output channel.
    For valid ranges, refer to the Ranges topic for your device in the NI DC Power Supplies and SMUs Help.



    .. note:: The channel must be enabled for the specified current limit to take effect. Refer to the


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        current_limit_range.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        current_limit_range.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].current_limit_range = var
            var = session['0,1'].current_limit_range

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

            - LabVIEW Property: **Source:DC Voltage:Current Limit Range**
            - C Attribute: **NIDCPOWER_ATTR_CURRENT_LIMIT_RANGE**

.. py:attribute:: current_pole_zero_ratio

    The ratio of the pole frequency to the zero frequency when the channel is in  Constant Current mode.
    for information about supported devices.
    Default Value: Determined by the value of the :py:data:`~nidcpower.TransientResponse.NORMAL` setting of the :py:data:`nidcpower.Session.transient_response` property.



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        current_pole_zero_ratio.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        current_pole_zero_ratio.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].current_pole_zero_ratio = var
            var = session['0,1'].current_pole_zero_ratio

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

            - LabVIEW Property: **Source:Custom Transient Response:Current:Pole-Zero Ratio**
            - C Attribute: **NIDCPOWER_ATTR_CURRENT_POLE_ZERO_RATIO**

.. py:attribute:: dc_noise_rejection

    Determines the relative weighting of samples in a measurement. Refer to the NI PXIe-4140/4141 DC Noise Rejection,  NI PXIe-4142/4143 DC Noise Rejection, or NI PXIe-4144/4145 DC Noise Rejection topic in the NI DC Power Supplies  and SMUs Help for more information about noise rejection.
    for information about supported devices.
    Default Value: :py:data:`~nidcpower.TransientResponse.NORMAL`



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

    The following table lists the characteristics of this property.

    +----------------+-------------------------+
    | Characteristic | Value                   |
    +================+=========================+
    | Datatype       | _enums.DCNoiseRejection |
    +----------------+-------------------------+
    | Permissions    | read-write              |
    +----------------+-------------------------+
    | Channel Based  | False                   |
    +----------------+-------------------------+
    | Resettable     | No                      |
    +----------------+-------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Measurement:Advanced:DC Noise Rejection**
            - C Attribute: **NIDCPOWER_ATTR_DC_NOISE_REJECTION**

.. py:attribute:: digital_edge_measure_trigger_edge

    Specifies whether to configure the Measure trigger to assert on the rising or falling edge.
    :py:data:`nidcpower.Session.source_trigger_type` property is set to :py:data:`~nidcpower.TriggerType.DIGITAL_EDGE`.
    for information about supported devices.
    Default Value: :py:data:`~nidcpower.DigitalEdge.RISING`



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

    The following table lists the characteristics of this property.

    +----------------+--------------------+
    | Characteristic | Value              |
    +================+====================+
    | Datatype       | _enums.DigitalEdge |
    +----------------+--------------------+
    | Permissions    | read-write         |
    +----------------+--------------------+
    | Channel Based  | False              |
    +----------------+--------------------+
    | Resettable     | No                 |
    +----------------+--------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggers:Measure Trigger:Digital Edge:Edge**
            - C Attribute: **NIDCPOWER_ATTR_DIGITAL_EDGE_MEASURE_TRIGGER_EDGE**

.. py:attribute:: digital_edge_measure_trigger_input_terminal

    Specifies the input terminal for the Measure trigger. This property is used only when the  :py:data:`nidcpower.Session.measure_trigger_type` property is set to :py:data:`~nidcpower.TriggerType.DIGITAL_EDGE`.
    for this property.
    You can specify any valid input terminal for this property. Valid terminals are listed in  Measurement & Automation Explorer under the Device Routes tab.
    Input terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you  can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal  name, PXI_Trig0. The input terminal can also be a terminal from another device. For example, you can set the input  terminal on Dev1 to be /Dev2/SourceCompleteEvent.



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

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

    Specifies whether to configure the Pulse trigger to assert on the rising or falling edge.
    Default Value: :py:data:`~nidcpower.DigitalEdge.RISING`



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.

    The following table lists the characteristics of this property.

    +----------------+--------------------+
    | Characteristic | Value              |
    +================+====================+
    | Datatype       | _enums.DigitalEdge |
    +----------------+--------------------+
    | Permissions    | read-write         |
    +----------------+--------------------+
    | Channel Based  | False              |
    +----------------+--------------------+
    | Resettable     | No                 |
    +----------------+--------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggers:Pulse Trigger:Digital Edge:Edge**
            - C Attribute: **NIDCPOWER_ATTR_DIGITAL_EDGE_PULSE_TRIGGER_EDGE**

.. py:attribute:: digital_edge_pulse_trigger_input_terminal

    Specifies the input terminal for the Pulse trigger. This property is used only when the :py:data:`nidcpower.Session.pulse_trigger_type` property is set to digital edge.
    You can specify any valid input terminal for this property. Valid terminals are listed in Measurement & Automation Explorer under the Device Routes tab.
    Input terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0. The input terminal can also be a terminal from another device. For example, you can set the input terminal on Dev1 to be /Dev2/SourceCompleteEvent.



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.

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

    Specifies whether to configure the Sequence Advance trigger to assert on the rising or falling edge.
    for information about supported devices.
    Default Value: :py:data:`~nidcpower.DigitalEdge.RISING`



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

    The following table lists the characteristics of this property.

    +----------------+--------------------+
    | Characteristic | Value              |
    +================+====================+
    | Datatype       | _enums.DigitalEdge |
    +----------------+--------------------+
    | Permissions    | read-write         |
    +----------------+--------------------+
    | Channel Based  | False              |
    +----------------+--------------------+
    | Resettable     | No                 |
    +----------------+--------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggers:Sequence Advance Trigger:Digital Edge:Edge**
            - C Attribute: **NIDCPOWER_ATTR_DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_EDGE**

.. py:attribute:: digital_edge_sequence_advance_trigger_input_terminal

    Specifies the input terminal for the Sequence Advance trigger. Use this property only when the  :py:data:`nidcpower.Session.sequence_advance_trigger_type` property is set to :py:data:`~nidcpower.TriggerType.DIGITAL_EDGE`.
    the NI DC Power Supplies and SMUs Help for information about supported devices.
    You can specify any valid input terminal for this property. Valid terminals are listed in Measurement & Automation Explorer under the Device Routes tab.
    Input terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can  specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal  name, PXI_Trig0. The input terminal can also be a terminal from another device. For example, you can set the  input terminal on Dev1 to be /Dev2/SourceCompleteEvent.



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic in

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

    Specifies whether to configure the Source trigger to assert on the rising or falling edge.
    for information about supported devices.
    Default Value: :py:data:`~nidcpower.DigitalEdge.RISING`



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

    The following table lists the characteristics of this property.

    +----------------+--------------------+
    | Characteristic | Value              |
    +================+====================+
    | Datatype       | _enums.DigitalEdge |
    +----------------+--------------------+
    | Permissions    | read-write         |
    +----------------+--------------------+
    | Channel Based  | False              |
    +----------------+--------------------+
    | Resettable     | No                 |
    +----------------+--------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggers:Source Trigger:Digital Edge:Edge**
            - C Attribute: **NIDCPOWER_ATTR_DIGITAL_EDGE_SOURCE_TRIGGER_EDGE**

.. py:attribute:: digital_edge_source_trigger_input_terminal

    Specifies the input terminal for the Source trigger. Use this property only when the  :py:data:`nidcpower.Session.source_trigger_type` property is set to :py:data:`~nidcpower.TriggerType.DIGITAL_EDGE`.
    for information about supported devices.
    You can specify any valid input terminal for this property. Valid terminals are listed  in Measurement & Automation Explorer under the Device Routes tab.
    Input terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you  can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal  name, PXI_Trig0. The input terminal can also be a terminal from another device. For example, you can set the input  terminal on Dev1 to be /Dev2/SourceCompleteEvent.



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

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

    Specifies whether to configure the Start trigger to assert on the rising or falling edge.
    for information about supported devices.
    Default Value: :py:data:`~nidcpower.DigitalEdge.RISING`



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

    The following table lists the characteristics of this property.

    +----------------+--------------------+
    | Characteristic | Value              |
    +================+====================+
    | Datatype       | _enums.DigitalEdge |
    +----------------+--------------------+
    | Permissions    | read-write         |
    +----------------+--------------------+
    | Channel Based  | False              |
    +----------------+--------------------+
    | Resettable     | No                 |
    +----------------+--------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggers:Start Trigger:Digital Edge:Edge**
            - C Attribute: **NIDCPOWER_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE**

.. py:attribute:: digital_edge_start_trigger_input_terminal

    Specifies the input terminal for the Start trigger. Use this property only when the :py:data:`nidcpower.Session.start_trigger_type`  property is set to :py:data:`~nidcpower.TriggerType.DIGITAL_EDGE`.
    for information about supported devices.
    You can specify any valid input terminal for this property. Valid terminals are listed in Measurement & Automation  Explorer under the Device Routes tab.
    Input terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can  specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name,  PXI_Trig0. The input terminal can also be a terminal from another device. For example, you can set the input terminal  on Dev1 to be /Dev2/SourceCompleteEvent.



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

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

    Indicates the Driver Setup string that you specified when initializing the driver.
    Some cases exist where you must specify the instrument driver options at initialization  time. An example of this case is specifying a particular device model from among a family  of devices that the driver supports. This property is useful when simulating a device.  You can specify the driver-specific options through the DriverSetup keyword in the optionsString  parameter in the :py:meth:`nidcpower.Session._initialize_with_channels` method or through the  IVI Configuration Utility.
    You can specify  driver-specific options through the DriverSetup keyword in the  optionsString parameter in the :py:meth:`nidcpower.Session._initialize_with_channels` method. If you do not specify a Driver Setup string, this property returns an empty string.

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
    Refer to the Device Routes tab in Measurement & Automation Explorer for a list of the terminals  available on your device.
    for information about supported devices.
    Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you  can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal  name, PXI_Trig0.



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

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
    Refer to the Device Routes tab in Measurement & Automation Explorer for a list of the terminals available on your device.
    Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.

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

    Specifies the output terminal for exporting the Sequence Advance trigger.
    Refer to the Device Routes tab in Measurement & Automation Explorer for a list of the terminals  available on your device.
    for information about supported devices.
    Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you  can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal  name, PXI_Trig0.



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

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
    Refer to the Device Routes tab in MAX for a list of the terminals available on your device.
    for information about supported devices.
    Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you  can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal  name, PXI_Trig0.



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

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
    Refer to the Device Routes tab in Measurement & Automation Explorer (MAX) for a list of the terminals available  on your device.
    Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you  can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name,  PXI_Trig0.
    for information about supported devices.



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

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

    Returns the number of measurements acquired that have not been fetched yet.

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

    Contains a comma-separated list of class-extension groups that NI-DCPower implements.

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

    Contains the firmware revision information for the device you are currently using.

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

    Contains the name of the manufacturer for the device you are currently using.

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

    Contains the model number or name of the device that you are currently using.

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

    Specifies whether to perform interchangeability checking and log interchangeability warnings when you  call NI-DCPower methods. True specifies that interchangeability checking is enabled.
    Interchangeability warnings indicate that using your application with a different power supply might  cause different behavior. Call the :py:meth:`nidcpower.Session.GetNextInterchangeWarning` method to retrieve  interchange warnings.
    Call the :py:meth:`nidcpower.Session.GetNextInterchangeWarning` method to clear the list of interchangeability warnings  without reading them.
    Interchangeability checking examines the properties in a capability group only if you specify a value  for at least one property within that group. Interchangeability warnings can occur when an property  affects the behavior of the device and you have not set that property or when the property has been  invalidated since you set it.
    Default Value: False



    .. note:: One or more of the referenced methods are not in the Python API for this driver.

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
            - C Attribute: **NIDCPOWER_ATTR_INTERCHANGE_CHECK**

.. py:attribute:: interlock_input_open

    Indicates whether the safety interlock circuit is open.
    Refer to the Safety Interlock topic in the NI DC Power Supplies and SMUs Help for more information about  the safety interlock circuit.
    about supported devices.



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information

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

            - LabVIEW Property: **Advanced:Interlock Input Open**
            - C Attribute: **NIDCPOWER_ATTR_INTERLOCK_INPUT_OPEN**

.. py:attribute:: io_resource_descriptor

    Indicates the resource descriptor NI-DCPower uses to identify the physical device.
    If you initialize NI-DCPower with a logical name, this property contains the resource descriptor  that corresponds to the entry in the IVI Configuration utility.
    If you initialize NI-DCPower with the resource descriptor, this property contains that value.

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

    Contains the logical name you specified when opening the current IVI session.
    You can pass a logical name to the :py:meth:`nidcpower.Session._initialize_with_channels` method.  The IVI Configuration utility must contain an entry for the logical name. The logical name entry  refers to a method section in the IVI Configuration file. The method section specifies a physical  device and initial user options.

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

    Specifies the number of samples that the active channel measurement buffer can hold.
    The default value is the maximum number of samples that a device is capable of recording in one second.
    for information about supported devices.
    Valid Values: 1000 to 2147483647
    Default Value: Varies by device. Refer to Supported Properties by Device topic in  the NI DC Power Supplies and SMUs Help for more information about default values.



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

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

    Specifies the amount of time to delay the generation of the Measure Complete event, in seconds.
    for information about supported devices.
    Valid Values: 0 to 167 seconds
    Default Value: The NI PXI-4132 and NI PXIe-4140/4141/4142/4143/4144/4145/4154 supports values from  0 seconds to 167 seconds.



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

    The following table lists the characteristics of this property.

    +----------------+--------------------+
    | Characteristic | Value              |
    +================+====================+
    | Datatype       | datetime.timedelta |
    +----------------+--------------------+
    | Permissions    | read-write         |
    +----------------+--------------------+
    | Channel Based  | False              |
    +----------------+--------------------+
    | Resettable     | No                 |
    +----------------+--------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Measure Complete Event:Event Delay**
            - C Attribute: **NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_DELAY**

.. py:attribute:: measure_complete_event_output_terminal

    Specifies the output terminal for exporting the Measure Complete event.
    for information about supported devices.
    Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal  is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or  with the shortened terminal name, PXI_Trig0.



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

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
    for information about supported devices.
    Default Value: :py:data:`~nidcpower.Polarity.HIGH`



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

    The following table lists the characteristics of this property.

    +----------------+-----------------+
    | Characteristic | Value           |
    +================+=================+
    | Datatype       | _enums.Polarity |
    +----------------+-----------------+
    | Permissions    | read-write      |
    +----------------+-----------------+
    | Channel Based  | False           |
    +----------------+-----------------+
    | Resettable     | No              |
    +----------------+-----------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Measure Complete Event:Pulse:Polarity**
            - C Attribute: **NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_PULSE_POLARITY**

.. py:attribute:: measure_complete_event_pulse_width

    Specifies the width of the Measure Complete event, in seconds.
    The minimum event pulse width value for PXI devices is 150 ns, and the minimum event pulse  width value for PXI Express devices is 250 ns.
    The maximum event pulse width value for all devices is 1.6 microseconds.
    for information about supported devices.
    Valid Values: 1.5e-7 to 1.6e-6
    Default Value: The default value for PXI devices is 150 ns. The default value  for PXI Express devices is 250 ns.



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

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

    Queries the amount of time, in seconds, between between the start of two consecutive measurements in a measure record.  Only query this property after the desired measurement settings are committed.
    for information about supported devices.
    two measurements and the rest would differ.



    .. note:: This property is not available when Auto Zero is configured to Once because the amount of time between the first

    The following table lists the characteristics of this property.

    +----------------+--------------------+
    | Characteristic | Value              |
    +================+====================+
    | Datatype       | datetime.timedelta |
    +----------------+--------------------+
    | Permissions    | read only          |
    +----------------+--------------------+
    | Channel Based  | False              |
    +----------------+--------------------+
    | Resettable     | No                 |
    +----------------+--------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Measurement:Measure Record Delta Time**
            - C Attribute: **NIDCPOWER_ATTR_MEASURE_RECORD_DELTA_TIME**

.. py:attribute:: measure_record_length

    Specifies how many measurements compose a measure record. When this property is set to a value greater than 1, the  :py:data:`nidcpower.Session.measure_when` property must be set to :py:data:`~nidcpower.MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE` or  :py:data:`~nidcpower.MeasureWhen.ON_MEASURE_TRIGGER`.
    for information about supported devices.
    Valid Values: 1 to 16,777,216
    Default Value: 1



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

    Specifies whether to take continuous measurements. Call the :py:meth:`nidcpower.Session.abort` method to stop continuous measurements.  When this property is set to False and the :py:data:`nidcpower.Session.source_mode` property is set to  :py:data:`~nidcpower.SourceMode.SINGLE_POINT`, the :py:data:`nidcpower.Session.measure_when` property must be set to  :py:data:`~nidcpower.MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE` or :py:data:`~nidcpower.MeasureWhen.ON_MEASURE_TRIGGER`. When this property is set to  False and the :py:data:`nidcpower.Session.source_mode` property is set to :py:data:`~nidcpower.SourceMode.SEQUENCE`, the :py:data:`nidcpower.Session.measure_when`  property must be set to :py:data:`~nidcpower.MeasureWhen.ON_MEASURE_TRIGGER`.
    for information about supported devices.
    Default Value: True



    .. note:: This property is not available in a session involving multiple channels.

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

            - LabVIEW Property: **Measurement:Measure Record Length Is Finite**
            - C Attribute: **NIDCPOWER_ATTR_MEASURE_RECORD_LENGTH_IS_FINITE**

.. py:attribute:: measure_trigger_type

    Specifies the behavior of the Measure trigger.
    for information about supported devices.
    Default Value: :py:data:`~nidcpower.TriggerType.DIGITAL_EDGE`



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

    The following table lists the characteristics of this property.

    +----------------+--------------------+
    | Characteristic | Value              |
    +================+====================+
    | Datatype       | _enums.TriggerType |
    +----------------+--------------------+
    | Permissions    | read-write         |
    +----------------+--------------------+
    | Channel Based  | False              |
    +----------------+--------------------+
    | Resettable     | No                 |
    +----------------+--------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggers:Measure Trigger:Trigger Type**
            - C Attribute: **NIDCPOWER_ATTR_MEASURE_TRIGGER_TYPE**

.. py:attribute:: measure_when

    Specifies when the measure unit should acquire measurements. Unless this property is configured to  :py:data:`~nidcpower.MeasureWhen.ON_MEASURE_TRIGGER`, the :py:data:`nidcpower.Session.measure_trigger_type` property is ignored.
    Refer to the Acquiring Measurements topic in the NI DC Power Supplies and SMUs Help for more information about how to  configure your measurements.
    Default Value: If the :py:data:`nidcpower.Session.source_mode` property is set to :py:data:`~nidcpower.SourceMode.SINGLE_POINT`, the default value is  :py:data:`~nidcpower.MeasureWhen.ON_DEMAND`. This value supports only the :py:meth:`nidcpower.Session.measure` method and :py:meth:`nidcpower.Session.measure_multiple`  method. If the :py:data:`nidcpower.Session.source_mode` property is set to :py:data:`~nidcpower.SourceMode.SEQUENCE`, the default value is  :py:data:`~nidcpower.MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE`. This value supports only the :py:meth:`nidcpower.Session._fetch_multiple` method.

    The following table lists the characteristics of this property.

    +----------------+--------------------+
    | Characteristic | Value              |
    +================+====================+
    | Datatype       | _enums.MeasureWhen |
    +----------------+--------------------+
    | Permissions    | read-write         |
    +----------------+--------------------+
    | Channel Based  | False              |
    +----------------+--------------------+
    | Resettable     | No                 |
    +----------------+--------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Measurement:Advanced:Measure When**
            - C Attribute: **NIDCPOWER_ATTR_MEASURE_WHEN**

.. py:attribute:: output_capacitance

    Specifies whether to use a low or high capacitance on the output for the specified channel(s).
    for information about supported devices.
    Refer to the NI PXI-4130 Output Capacitance Selection topic in the NI DC Power Supplies and SMUs Help for more  information about capacitance.



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        output_capacitance.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        output_capacitance.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].output_capacitance = var
            var = session['0,1'].output_capacitance

    The following table lists the characteristics of this property.

    +----------------+--------------------------+
    | Characteristic | Value                    |
    +================+==========================+
    | Datatype       | _enums.OutputCapacitance |
    +----------------+--------------------------+
    | Permissions    | read-write               |
    +----------------+--------------------------+
    | Channel Based  | True                     |
    +----------------+--------------------------+
    | Resettable     | No                       |
    +----------------+--------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Source:Advanced:Output Capacitance**
            - C Attribute: **NIDCPOWER_ATTR_OUTPUT_CAPACITANCE**

.. py:attribute:: output_connected

    Specifies whether the output relay is connected (closed) or disconnected (open). The :py:data:`nidcpower.Session.output_enabled`  property does not change based on this property; they are independent of each other.
    about supported devices.
    Set this property to False to disconnect the output terminal from the output.
    to the output terminal might discharge unless the relay is disconnected. Excessive connecting and disconnecting of the  output can cause premature wear on the relay.
    Default Value: True



    .. note:: Only disconnect the output when disconnecting is necessary for your application. For example, a battery connected


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        output_connected.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        output_connected.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].output_connected = var
            var = session['0,1'].output_connected

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

            - LabVIEW Property: **Source:Output Connected**
            - C Attribute: **NIDCPOWER_ATTR_OUTPUT_CONNECTED**

.. py:attribute:: output_enabled

    Specifies whether the output is enabled (True) or disabled (False).
    Depending on the value you specify for the :py:data:`nidcpower.Session.output_function` property, you also must set the  voltage level or current level in addition to  enabling the output
    the :py:meth:`nidcpower.Session._initiate` method. Refer to the Programming States topic in the NI DC Power Supplies and SMUs Help for  more information about NI-DCPower programming states.
    Default Value: The default value is True if you use the :py:meth:`nidcpower.Session._initialize_with_channels` method to open  the session. Otherwise the default value is False, including when you use a calibration session or the deprecated programming model.



    .. note:: If the session is in the Committed or Uncommitted states, enabling the output does not take effect until you call


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        output_enabled.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        output_enabled.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].output_enabled = var
            var = session['0,1'].output_enabled

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

            - LabVIEW Property: **Source:Output Enabled**
            - C Attribute: **NIDCPOWER_ATTR_OUTPUT_ENABLED**

.. py:attribute:: output_function

    Configures the method to generate on the specified channel(s).
    When :py:data:`~nidcpower.OutputFunction.DC_VOLTAGE` is selected, the device generates the desired voltage level on the output as long as the  output current is below the current limit. You can use the following properties to configure the channel when  :py:data:`~nidcpower.OutputFunction.DC_VOLTAGE` is selected:
    :py:data:`nidcpower.Session.voltage_level`
    :py:data:`nidcpower.Session.current_limit`
    :py:data:`nidcpower.Session.current_limit_high`
    :py:data:`nidcpower.Session.current_limit_low`
    :py:data:`nidcpower.Session.voltage_level_range`
    :py:data:`nidcpower.Session.current_limit_range`
    When :py:data:`~nidcpower.OutputFunction.DC_CURRENT` is selected, the device generates the desired current level on the output as long as the  output voltage is below the voltage limit. You can use the following properties to configure the channel when  :py:data:`~nidcpower.OutputFunction.DC_CURRENT` is selected:
    :py:data:`nidcpower.Session.current_level`
    :py:data:`nidcpower.Session.voltage_limit`
    :py:data:`nidcpower.Session.voltage_limit_high`
    :py:data:`nidcpower.Session.voltage_limit_low`
    :py:data:`nidcpower.Session.current_level_range`
    :py:data:`nidcpower.Session.voltage_limit_range`
    Default Value: :py:data:`~nidcpower.OutputFunction.DC_VOLTAGE`




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        output_function.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        output_function.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].output_function = var
            var = session['0,1'].output_function

    The following table lists the characteristics of this property.

    +----------------+-----------------------+
    | Characteristic | Value                 |
    +================+=======================+
    | Datatype       | _enums.OutputFunction |
    +----------------+-----------------------+
    | Permissions    | read-write            |
    +----------------+-----------------------+
    | Channel Based  | True                  |
    +----------------+-----------------------+
    | Resettable     | No                    |
    +----------------+-----------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Source:Output Function**
            - C Attribute: **NIDCPOWER_ATTR_OUTPUT_FUNCTION**

.. py:attribute:: output_resistance

    Specifies the output resistance that the device attempts to generate for the specified channel(s). This property is  available only when you set the :py:data:`nidcpower.Session.output_function` property on a support device. Refer to a supported device's topic about output resistance for more information about selecting an output resistance.
    about supported devices.
    Default Value: 0.0



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic for information


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        output_resistance.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        output_resistance.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].output_resistance = var
            var = session['0,1'].output_resistance

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

            - LabVIEW Property: **Source:Output Resistance**
            - C Attribute: **NIDCPOWER_ATTR_OUTPUT_RESISTANCE**

.. py:attribute:: overranging_enabled

    Specifies whether NI-DCPower allows setting the voltage level, current level, voltage limit and current limit outside the  device specification limits. True means that overranging is enabled.
    Refer to the Ranges topic in the NI DC Power Supplies and SMUs Help for more information about overranging.
    Default Value: False

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

            - LabVIEW Property: **Source:Advanced:Overranging Enabled**
            - C Attribute: **NIDCPOWER_ATTR_OVERRANGING_ENABLED**

.. py:attribute:: ovp_enabled

    Enables (True) or disables (False) overvoltage protection (OVP).
    Refer to the Output Overvoltage Protection topic in the NI DC Power Supplies and SMUs Help for more information about  overvoltage protection.
    for information about supported devices.
    Default Value: False



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

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

            - LabVIEW Property: **Source:Advanced:OVP Enabled**
            - C Attribute: **NIDCPOWER_ATTR_OVP_ENABLED**

.. py:attribute:: ovp_limit

    Determines the voltage limit, in volts, beyond which overvoltage protection (OVP) engages.
    for information about supported devices.
    Valid Values: 2 V to 210 V
    Default Value: 210 V



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

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

    Specifies the power line frequency for specified channel(s). NI-DCPower uses this value to select a timebase for setting the  :py:data:`nidcpower.Session.aperture_time` property in power line cycles (PLCs).
    in the NI DC Power Supplies and SMUs Help for information about supported devices.
    Default Value: :py:data:`~nidcpower.NIDCPOWER_VAL_60_HERTZ`



    .. note:: This property is not supported by all devices. Refer to the Supported Properties by Device topic

    .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        power_line_frequency.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        power_line_frequency.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].power_line_frequency = var
            var = session['0,1'].power_line_frequency

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

            - LabVIEW Property: **Measurement:Power Line Frequency**
            - C Attribute: **NIDCPOWER_ATTR_POWER_LINE_FREQUENCY**

.. py:attribute:: power_source

    Specifies the power source to use. NI-DCPower switches the power source used by the  device to the specified value.
    Default Value: :py:data:`~nidcpower.PowerSource.AUTOMATIC`
    is set to :py:data:`~nidcpower.PowerSource.AUTOMATIC`. However, if the session is in the Committed or Uncommitted state  when you set this property, the power source selection only occurs after you call the  :py:meth:`nidcpower.Session._initiate` method.



    .. note:: Automatic selection is not persistent and occurs only at the time this property

    The following table lists the characteristics of this property.

    +----------------+--------------------+
    | Characteristic | Value              |
    +================+====================+
    | Datatype       | _enums.PowerSource |
    +----------------+--------------------+
    | Permissions    | read-write         |
    +----------------+--------------------+
    | Channel Based  | False              |
    +----------------+--------------------+
    | Resettable     | No                 |
    +----------------+--------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Advanced:Power Source**
            - C Attribute: **NIDCPOWER_ATTR_POWER_SOURCE**

.. py:attribute:: power_source_in_use

    Indicates whether the device is using the internal or auxiliary power source to generate power.

    The following table lists the characteristics of this property.

    +----------------+-------------------------+
    | Characteristic | Value                   |
    +================+=========================+
    | Datatype       | _enums.PowerSourceInUse |
    +----------------+-------------------------+
    | Permissions    | read only               |
    +----------------+-------------------------+
    | Channel Based  | False                   |
    +----------------+-------------------------+
    | Resettable     | No                      |
    +----------------+-------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Advanced:Power Source In Use**
            - C Attribute: **NIDCPOWER_ATTR_POWER_SOURCE_IN_USE**

.. py:attribute:: pulse_bias_current_level

    Specifies the pulse bias current level, in amps, that the device attempts to generate on the specified channel(s) during the off phase of a pulse.
    This property is applicable only if the :py:data:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.PULSE_CURRENT`.
    Valid Values: The valid values for this property are defined by the values you specify for the :py:data:`nidcpower.Session.pulse_current_level_range` property.



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        pulse_bias_current_level.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        pulse_bias_current_level.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].pulse_bias_current_level = var
            var = session['0,1'].pulse_bias_current_level

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

            - LabVIEW Property: **Source:Pulse Current:Pulse Bias Current Level**
            - C Attribute: **NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LEVEL**

.. py:attribute:: pulse_bias_current_limit

    Specifies the pulse bias current limit, in amps, that the output cannot exceed when generating the desired pulse bias voltage on the specified channel(s) during the off phase of a pulse.
    This property is applicable only if the :py:data:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.PULSE_VOLTAGE`.
    Valid Values: The valid values for this property are defined by the values you specify for the :py:data:`nidcpower.Session.pulse_current_limit_range` property.



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        pulse_bias_current_limit.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        pulse_bias_current_limit.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].pulse_bias_current_limit = var
            var = session['0,1'].pulse_bias_current_limit

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

            - LabVIEW Property: **Source:Pulse Voltage:Pulse Bias Current Limit**
            - C Attribute: **NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT**

.. py:attribute:: pulse_bias_current_limit_high

    Specifies the maximum current, in amps, that the output can produce when
    generating the desired pulse voltage on the specified channel(s) during
    the *off* phase of a pulse.
    This property is applicable only if the `Compliance Limit
    Symmetry <p:py:meth:`nidcpower.Session.ComplianceLimitSymmetry`.html>`__ property is set to
    **Asymmetric** and the `Output
    Method <p:py:meth:`nidcpower.Session.OutputFunction`.html>`__ property is set to **Pulse
    Voltage**.
    You must also specify a `Pulse Bias Current Limit
    Low <p:py:meth:`nidcpower.Session.PulseBiasCurrentLimitLow`.html>`__ to complete the
    asymmetric range.
    **Valid Values:** [1% of `Pulse Current Limit
    Range <p:py:meth:`nidcpower.Session.PulseCurrentLimitRange`.html>`__, `Pulse Current Limit
    Range <p:py:meth:`nidcpower.Session.PulseCurrentLimitRange`.html>`__]
    The range bounded by the limit high and limit low must include zero.
    **Default Value:** Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.
    **Related Topics:**
    `Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
    `Changing
    Ranges <NI_DC_Power_Supplies_Help.chm::/changing_ranges.html>`__
    `Overranging <NI_DC_Power_Supplies_Help.chm::/overranging.html>`__



    .. note:: The limit may be extended beyond the selected limit range if the
        `Overranging Enabled <p:py:meth:`nidcpower.Session.OverrangingEnabled`.html>`__ property is
        set to TRUE or if the `Output
        Method <p:py:meth:`nidcpower.Session.OutputFunction`.html>`__ property is set to a
        pulsing method.

    .. note:: One or more of the referenced methods are not in the Python API for this driver.


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        pulse_bias_current_limit_high.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        pulse_bias_current_limit_high.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].pulse_bias_current_limit_high = var
            var = session['0,1'].pulse_bias_current_limit_high

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

            - LabVIEW Property: **Source:Pulse Voltage:Pulse Bias Current Limit High**
            - C Attribute: **NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT_HIGH**

.. py:attribute:: pulse_bias_current_limit_low

    Specifies the minimum current, in amps, that the output can produce when
    generating the desired pulse voltage on the specified channel(s) during
    the *off* phase of a pulse.
    This property is applicable only if the `Compliance Limit
    Symmetry <p:py:meth:`nidcpower.Session.ComplianceLimitSymmetry`.html>`__ property is set to
    **Asymmetric** and the `Output
    Method <p:py:meth:`nidcpower.Session.OutputFunction`.html>`__ property is set to **Pulse
    Voltage**.
    You must also specify a `Pulse Bias Current Limit
    High <p:py:meth:`nidcpower.Session.PulseBiasCurrentLimitHigh`.html>`__ to complete the
    asymmetric range.
    **Valid Values:** [-`Pulse Current Limit
    Range <p:py:meth:`nidcpower.Session.PulseCurrentLimitRange`.html>`__, -1% of `Pulse Current
    Limit Range <p:py:meth:`nidcpower.Session.PulseCurrentLimitRange`.html>`__]
    The range bounded by the limit high and limit low must include zero.
    **Default Value:** Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.
    **Related Topics:**
    `Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
    `Changing
    Ranges <NI_DC_Power_Supplies_Help.chm::/changing_ranges.html>`__
    `Overranging <NI_DC_Power_Supplies_Help.chm::/overranging.html>`__



    .. note:: The limit may be extended beyond the selected limit range if the
        `Overranging Enabled <p:py:meth:`nidcpower.Session.OverrangingEnabled`.html>`__ property is
        set to TRUE or if the `Output
        Method <p:py:meth:`nidcpower.Session.OutputFunction`.html>`__ property is set to a
        pulsing method.

    .. note:: One or more of the referenced methods are not in the Python API for this driver.


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        pulse_bias_current_limit_low.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        pulse_bias_current_limit_low.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].pulse_bias_current_limit_low = var
            var = session['0,1'].pulse_bias_current_limit_low

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

            - LabVIEW Property: **Source:Pulse Voltage:Pulse Bias Current Limit Low**
            - C Attribute: **NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT_LOW**

.. py:attribute:: pulse_bias_delay

    Determines when, in seconds, the device generates the Pulse Complete event after generating the off level of a pulse.
    Valid Values: 0 to 167 seconds
    Default Value: 16.67 milliseconds



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        pulse_bias_delay.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        pulse_bias_delay.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].pulse_bias_delay = var
            var = session['0,1'].pulse_bias_delay

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

            - LabVIEW Property: **Source:Advanced:Pulse Bias Delay**
            - C Attribute: **NIDCPOWER_ATTR_PULSE_BIAS_DELAY**

.. py:attribute:: pulse_bias_voltage_level

    Specifies the pulse bias voltage level, in volts, that the device attempts to generate on the specified channel(s) during the off phase of a pulse.
    This property is applicable only if the :py:data:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.PULSE_VOLTAGE`.
    Valid Values: The valid values for this property are defined by the values you specify for the :py:data:`nidcpower.Session.pulse_voltage_level_range` property.



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        pulse_bias_voltage_level.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        pulse_bias_voltage_level.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].pulse_bias_voltage_level = var
            var = session['0,1'].pulse_bias_voltage_level

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

            - LabVIEW Property: **Source:Pulse Voltage:Pulse Bias Voltage Level**
            - C Attribute: **NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LEVEL**

.. py:attribute:: pulse_bias_voltage_limit

    Specifies the pulse voltage limit, in volts, that the output cannot exceed when generating the desired current on the specified channel(s) during the off phase of a pulse.
    This property is applicable only if the :py:data:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.PULSE_CURRENT`.
    Valid Values: The valid values for this property are defined by the values you specify for the :py:data:`nidcpower.Session.pulse_voltage_limit_range` property.



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        pulse_bias_voltage_limit.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        pulse_bias_voltage_limit.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].pulse_bias_voltage_limit = var
            var = session['0,1'].pulse_bias_voltage_limit

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

            - LabVIEW Property: **Source:Pulse Current:Pulse Bias Voltage Limit**
            - C Attribute: **NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT**

.. py:attribute:: pulse_bias_voltage_limit_high

    Specifies the maximum voltage, in volts, that the output can produce
    when generating the desired pulse current on the specified channel(s)
    during the *off* phase of a pulse.
    This property is applicable only if the `Compliance Limit
    Symmetry <p:py:meth:`nidcpower.Session.ComplianceLimitSymmetry`.html>`__ property is set to
    **Asymmetric** and the `Output
    Method <p:py:meth:`nidcpower.Session.OutputFunction`.html>`__ property is set to **Pulse
    Current**.
    You must also specify a `Pulse Bias Voltage Limit
    Low <p:py:meth:`nidcpower.Session.PulseBiasVoltageLimitLow`.html>`__ to complete the
    asymmetric range.
    **Valid Values:** [1% of `Pulse Voltage Limit
    Range <p:py:meth:`nidcpower.Session.PulseVoltageLimitRange`.html>`__, `Pulse Voltage Limit
    Range <p:py:meth:`nidcpower.Session.PulseVoltageLimitRange`.html>`__]
    The range bounded by the limit high and limit low must include zero.
    **Default Value:** Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.
    **Related Topics:**
    `Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
    `Changing
    Ranges <NI_DC_Power_Supplies_Help.chm::/changing_ranges.html>`__
    `Overranging <NI_DC_Power_Supplies_Help.chm::/overranging.html>`__



    .. note:: The limit may be extended beyond the selected limit range if the
        `Overranging Enabled <p:py:meth:`nidcpower.Session.OverrangingEnabled`.html>`__ property is
        set to TRUE or if the `Output
        Method <p:py:meth:`nidcpower.Session.OutputFunction`.html>`__ property is set to a
        pulsing method.

    .. note:: One or more of the referenced methods are not in the Python API for this driver.


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        pulse_bias_voltage_limit_high.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        pulse_bias_voltage_limit_high.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].pulse_bias_voltage_limit_high = var
            var = session['0,1'].pulse_bias_voltage_limit_high

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

            - LabVIEW Property: **Source:Pulse Current:Pulse Bias Voltage Limit High**
            - C Attribute: **NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT_HIGH**

.. py:attribute:: pulse_bias_voltage_limit_low

    Specifies the minimum voltage, in volts, that the output can produce
    when generating the desired pulse current on the specified channel(s)
    during the *off* phase of a pulse.
    This property is applicable only if the `Compliance Limit
    Symmetry <p:py:meth:`nidcpower.Session.ComplianceLimitSymmetry`.html>`__ property is set to
    **Asymmetric** and the `Output
    Method <p:py:meth:`nidcpower.Session.OutputFunction`.html>`__ property is set to **Pulse
    Current**.
    You must also specify a `Pulse Bias Voltage Limit
    High <p:py:meth:`nidcpower.Session.PulseBiasVoltageLimitHigh`.html>`__ to complete the
    asymmetric range.
    **Valid Values:** [-`Pulse Voltage Limit
    Range <p:py:meth:`nidcpower.Session.PulseVoltageLimitRange`.html>`__, -1% of `Pulse Voltage
    Limit Range <p:py:meth:`nidcpower.Session.PulseVoltageLimitRange`.html>`__]
    The range bounded by the limit high and limit low must include zero.
    **Default Value:** Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.
    **Related Topics:**
    `Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
    `Changing
    Ranges <NI_DC_Power_Supplies_Help.chm::/changing_ranges.html>`__
    `Overranging <NI_DC_Power_Supplies_Help.chm::/overranging.html>`__



    .. note:: The limit may be extended beyond the selected limit range if the
        `Overranging Enabled <p:py:meth:`nidcpower.Session.OverrangingEnabled`.html>`__ property is
        set to TRUE or if the `Output
        Method <p:py:meth:`nidcpower.Session.OutputFunction`.html>`__ property is set to a
        pulsing method.

    .. note:: One or more of the referenced methods are not in the Python API for this driver.


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        pulse_bias_voltage_limit_low.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        pulse_bias_voltage_limit_low.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].pulse_bias_voltage_limit_low = var
            var = session['0,1'].pulse_bias_voltage_limit_low

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

            - LabVIEW Property: **Source:Pulse Current:Pulse Bias Voltage Limit Low**
            - C Attribute: **NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT_LOW**

.. py:attribute:: pulse_complete_event_output_terminal

    Specifies the output terminal for exporting the Pulse Complete event.
    Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.
    Default Value:The default value for PXI Express devices is 250 ns.



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.

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
    Default Value: :py:data:`~nidcpower.Polarity.HIGH`



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.

    The following table lists the characteristics of this property.

    +----------------+-----------------+
    | Characteristic | Value           |
    +================+=================+
    | Datatype       | _enums.Polarity |
    +----------------+-----------------+
    | Permissions    | read-write      |
    +----------------+-----------------+
    | Channel Based  | False           |
    +----------------+-----------------+
    | Resettable     | No              |
    +----------------+-----------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Pulse Complete Event:Pulse:Polarity**
            - C Attribute: **NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_PULSE_POLARITY**

.. py:attribute:: pulse_complete_event_pulse_width

    Specifies the width of the Pulse Complete event, in seconds.
    The minimum event pulse width value for PXI Express devices is 250 ns.
    The maximum event pulse width value for PXI Express devices is 1.6 microseconds.
    Default Value: The default value for PXI Express devices is 250 ns.



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.

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

    Specifies the pulse current level, in amps, that the device attempts to generate on the specified channel(s) during the on phase of a pulse.
    This property is applicable only if the :py:data:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.PULSE_CURRENT`.
    Valid Values: The valid values for this property are defined by the values you specify for the :py:data:`nidcpower.Session.pulse_current_level_range` property.



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        pulse_current_level.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        pulse_current_level.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].pulse_current_level = var
            var = session['0,1'].pulse_current_level

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

            - LabVIEW Property: **Source:Pulse Current:Pulse Current Level**
            - C Attribute: **NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL**

.. py:attribute:: pulse_current_level_range

    Specifies the pulse current level range, in amps, for the specified channel(s).
    The range defines the valid values to which you can set the pulse current level and pulse bias current level.
    This property is applicable only if the :py:data:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.PULSE_CURRENT`.
    For valid ranges, refer to the ranges topic for your device in the NI DC Power Supplies and SMUs Help.



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        pulse_current_level_range.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        pulse_current_level_range.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].pulse_current_level_range = var
            var = session['0,1'].pulse_current_level_range

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

            - LabVIEW Property: **Source:Pulse Current:Pulse Current Level Range**
            - C Attribute: **NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL_RANGE**

.. py:attribute:: pulse_current_limit

    Specifies the pulse current limit, in amps, that the output cannot exceed when generating the desired pulse voltage on the specified channel(s) during the on phase of a pulse.
    This property is applicable only if the :py:data:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.PULSE_VOLTAGE` and the :py:data:`nidcpower.Session.compliance_limit_symmetry`  property is set to :py:data:`~nidcpower.NIDCPOWER_VAL_SYMMETRIC`.
    Valid Values: The valid values for this property are defined by the values you specify for the :py:data:`nidcpower.Session.pulse_current_limit_range` property.



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.

    .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        pulse_current_limit.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        pulse_current_limit.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].pulse_current_limit = var
            var = session['0,1'].pulse_current_limit

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

            - LabVIEW Property: **Source:Pulse Voltage:Pulse Current Limit**
            - C Attribute: **NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT**

.. py:attribute:: pulse_current_limit_high

    Specifies the maximum current, in amps, that the output can produce when
    generating the desired pulse voltage on the specified channel(s) during
    the *on* phase of a pulse.
    This property is applicable only if the `Compliance Limit
    Symmetry <p:py:meth:`nidcpower.Session.ComplianceLimitSymmetry`.html>`__ property is set to
    **Asymmetric** and the `Output
    Method <p:py:meth:`nidcpower.Session.OutputFunction`.html>`__ property is set to **Pulse
    Voltage**.
    You must also specify a `Pulse Current Limit
    Low <p:py:meth:`nidcpower.Session.PulseCurrentLimitLow`.html>`__ to complete the asymmetric
    range.
    **Valid Values:** [1% of `Pulse Current Limit
    Range <p:py:meth:`nidcpower.Session.PulseCurrentLimitRange`.html>`__, `Pulse Current Limit
    Range <p:py:meth:`nidcpower.Session.PulseCurrentLimitRange`.html>`__]
    The range bounded by the limit high and limit low must include zero.
    **Default Value:** Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.
    **Related Topics:**
    `Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
    `Changing
    Ranges <NI_DC_Power_Supplies_Help.chm::/changing_ranges.html>`__
    `Overranging <NI_DC_Power_Supplies_Help.chm::/overranging.html>`__



    .. note:: The limit may be extended beyond the selected limit range if the
        `Overranging Enabled <p:py:meth:`nidcpower.Session.OverrangingEnabled`.html>`__ property is
        set to TRUE or if the `Output
        Method <p:py:meth:`nidcpower.Session.OutputFunction`.html>`__ property is set to a
        pulsing method.

    .. note:: One or more of the referenced methods are not in the Python API for this driver.


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        pulse_current_limit_high.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        pulse_current_limit_high.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].pulse_current_limit_high = var
            var = session['0,1'].pulse_current_limit_high

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

            - LabVIEW Property: **Source:Pulse Voltage:Pulse Current Limit High**
            - C Attribute: **NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_HIGH**

.. py:attribute:: pulse_current_limit_low

    Specifies the minimum current, in amps, that the output can produce when
    generating the desired pulse voltage on the specified channel(s) during
    the *on* phase of a pulse.
    This property is applicable only if the `Compliance Limit
    Symmetry <p:py:meth:`nidcpower.Session.ComplianceLimitSymmetry`.html>`__ property is set to
    **Asymmetric** and the `Output
    Method <p:py:meth:`nidcpower.Session.OutputFunction`.html>`__ property is set to **Pulse
    Voltage**.
    You must also specify a `Pulse Current Limit
    High <p:py:meth:`nidcpower.Session.PulseCurrentLimitHigh`.html>`__ to complete the
    asymmetric range.
    **Valid Values:** [-`Pulse Current Limit
    Range <p:py:meth:`nidcpower.Session.PulseCurrentLimitRange`.html>`__, -1% of `Pulse Current
    Limit Range <p:py:meth:`nidcpower.Session.PulseCurrentLimitRange`.html>`__]
    The range bounded by the limit high and limit low must include zero.
    **Default Value:** Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.
    **Related Topics:**
    `Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
    `Changing
    Ranges <NI_DC_Power_Supplies_Help.chm::/changing_ranges.html>`__
    `Overranging <NI_DC_Power_Supplies_Help.chm::/overranging.html>`__



    .. note:: The limit may be extended beyond the selected limit range if the
        `Overranging Enabled <p:py:meth:`nidcpower.Session.OverrangingEnabled`.html>`__ property is
        set to TRUE or if the `Output
        Method <p:py:meth:`nidcpower.Session.OutputFunction`.html>`__ property is set to a
        pulsing method.

    .. note:: One or more of the referenced methods are not in the Python API for this driver.


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        pulse_current_limit_low.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        pulse_current_limit_low.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].pulse_current_limit_low = var
            var = session['0,1'].pulse_current_limit_low

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

            - LabVIEW Property: **Source:Pulse Voltage:Pulse Current Limit Low**
            - C Attribute: **NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_LOW**

.. py:attribute:: pulse_current_limit_range

    Specifies the pulse current limit range, in amps, for the specified channel(s).
    The range defines the valid values to which you can set the pulse current limit and pulse bias current limit.
    This property is applicable only if the :py:data:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.PULSE_VOLTAGE`.
    For valid ranges, refer to the ranges topic for your device in the NI DC Power Supplies and SMUs Help.



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        pulse_current_limit_range.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        pulse_current_limit_range.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].pulse_current_limit_range = var
            var = session['0,1'].pulse_current_limit_range

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

            - LabVIEW Property: **Source:Pulse Voltage:Pulse Current Limit Range**
            - C Attribute: **NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_RANGE**

.. py:attribute:: pulse_off_time

    Determines the length, in seconds, of the off phase of a pulse.
    Valid Values: 10 microseconds to 167 seconds
    Default Value: 34 milliseconds



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        pulse_off_time.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        pulse_off_time.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].pulse_off_time = var
            var = session['0,1'].pulse_off_time

    The following table lists the characteristics of this property.

    +----------------+--------------------+
    | Characteristic | Value              |
    +================+====================+
    | Datatype       | datetime.timedelta |
    +----------------+--------------------+
    | Permissions    | read-write         |
    +----------------+--------------------+
    | Channel Based  | True               |
    +----------------+--------------------+
    | Resettable     | No                 |
    +----------------+--------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Source:Advanced:Pulse Off Time**
            - C Attribute: **NIDCPOWER_ATTR_PULSE_OFF_TIME**

.. py:attribute:: pulse_on_time

    Determines the length, in seconds, of the on phase of a pulse.
    Valid Values: 10 microseconds to 167 seconds
    Default Value: 34 milliseconds



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        pulse_on_time.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        pulse_on_time.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].pulse_on_time = var
            var = session['0,1'].pulse_on_time

    The following table lists the characteristics of this property.

    +----------------+--------------------+
    | Characteristic | Value              |
    +================+====================+
    | Datatype       | datetime.timedelta |
    +----------------+--------------------+
    | Permissions    | read-write         |
    +----------------+--------------------+
    | Channel Based  | True               |
    +----------------+--------------------+
    | Resettable     | No                 |
    +----------------+--------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Source:Advanced:Pulse On Time**
            - C Attribute: **NIDCPOWER_ATTR_PULSE_ON_TIME**

.. py:attribute:: pulse_trigger_type

    Specifies the behavior of the Pulse trigger.
    Default Value: :py:data:`~nidcpower.TriggerType.NONE`



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.

    The following table lists the characteristics of this property.

    +----------------+--------------------+
    | Characteristic | Value              |
    +================+====================+
    | Datatype       | _enums.TriggerType |
    +----------------+--------------------+
    | Permissions    | read-write         |
    +----------------+--------------------+
    | Channel Based  | False              |
    +----------------+--------------------+
    | Resettable     | No                 |
    +----------------+--------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggers:Pulse Trigger:Trigger Type**
            - C Attribute: **NIDCPOWER_ATTR_PULSE_TRIGGER_TYPE**

.. py:attribute:: pulse_voltage_level

    Specifies the pulse current limit, in amps, that the output cannot exceed when generating the desired pulse voltage on the specified channel(s) during the on phase of a pulse.
    This property is applicable only if the :py:data:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.PULSE_VOLTAGE`.
    Valid Values: The valid values for this property are defined by the values you specify for the :py:data:`nidcpower.Session.pulse_current_limit_range` property.



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        pulse_voltage_level.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        pulse_voltage_level.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].pulse_voltage_level = var
            var = session['0,1'].pulse_voltage_level

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

            - LabVIEW Property: **Source:Pulse Voltage:Pulse Voltage Level**
            - C Attribute: **NIDCPOWER_ATTR_PULSE_VOLTAGE_LEVEL**

.. py:attribute:: pulse_voltage_level_range

    Specifies the pulse voltage level range, in volts, for the specified channel(s).
    The range defines the valid values at which you can set the pulse voltage level and pulse bias voltage level.
    This property is applicable only if the :py:data:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.PULSE_VOLTAGE`.
    For valid ranges, refer to the ranges topic for your device in the NI DC Power Supplies and SMUs Help.



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        pulse_voltage_level_range.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        pulse_voltage_level_range.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].pulse_voltage_level_range = var
            var = session['0,1'].pulse_voltage_level_range

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

            - LabVIEW Property: **Source:Pulse Voltage:Pulse Voltage Level Range**
            - C Attribute: **NIDCPOWER_ATTR_PULSE_VOLTAGE_LEVEL_RANGE**

.. py:attribute:: pulse_voltage_limit

    Specifies the pulse voltage limit, in volts, that the output cannot exceed when generating the desired pulse current on the specified channel(s) during the on phase of a pulse.
    This property is applicable only if the :py:data:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.PULSE_CURRENT` and the :py:data:`nidcpower.Session.compliance_limit_symmetry` property  is set to :py:data:`~nidcpower.NIDCPOWER_VAL_SYMMETRIC`.
    Valid Values: The valid values for this property are defined by the values you specify for the :py:data:`nidcpower.Session.pulse_voltage_limit_range` property.



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.

    .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        pulse_voltage_limit.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        pulse_voltage_limit.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].pulse_voltage_limit = var
            var = session['0,1'].pulse_voltage_limit

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

            - LabVIEW Property: **Source:Pulse Current:Pulse Voltage Limit**
            - C Attribute: **NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT**

.. py:attribute:: pulse_voltage_limit_high

    Specifies the maximum voltage, in volts, that the output can produce
    when generating the desired pulse current on the specified channel(s)
    during the *on* phase of a pulse.
    This property is applicable only if the `Compliance Limit
    Symmetry <p:py:meth:`nidcpower.Session.ComplianceLimitSymmetry`.html>`__ property is set to
    **Asymmetric** and the `Output
    Method <p:py:meth:`nidcpower.Session.OutputFunction`.html>`__ property is set to **Pulse
    Current**.
    You must also specify a `Pulse Voltage Limit
    Low <p:py:meth:`nidcpower.Session.PulseVoltageLimitLow`.html>`__ to complete the asymmetric
    range.
    **Valid Values:** [1% of `Pulse Voltage Limit
    Range <p:py:meth:`nidcpower.Session.PulseVoltageLimitRange`.html>`__, `Pulse Voltage Limit
    Range <p:py:meth:`nidcpower.Session.PulseVoltageLimitRange`.html>`__]
    The range bounded by the limit high and limit low must include zero.
    **Default Value:** Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.
    **Related Topics:**
    `Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
    `Changing
    Ranges <NI_DC_Power_Supplies_Help.chm::/changing_ranges.html>`__
    `Overranging <NI_DC_Power_Supplies_Help.chm::/overranging.html>`__



    .. note:: The limit may be extended beyond the selected limit range if the
        `Overranging Enabled <p:py:meth:`nidcpower.Session.OverrangingEnabled`.html>`__ property is
        set to TRUE or if the `Output
        Method <p:py:meth:`nidcpower.Session.OutputFunction`.html>`__ property is set to a
        pulsing method.

    .. note:: One or more of the referenced methods are not in the Python API for this driver.


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        pulse_voltage_limit_high.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        pulse_voltage_limit_high.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].pulse_voltage_limit_high = var
            var = session['0,1'].pulse_voltage_limit_high

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

            - LabVIEW Property: **Source:Pulse Current:Pulse Voltage Limit High**
            - C Attribute: **NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_HIGH**

.. py:attribute:: pulse_voltage_limit_low

    Specifies the minimum voltage, in volts, that the output can produce
    when generating the desired pulse current on the specified channel(s)
    during the *on* phase of a pulse.
    This property is applicable only if the `Compliance Limit
    Symmetry <p:py:meth:`nidcpower.Session.ComplianceLimitSymmetry`.html>`__ property is set to
    **Asymmetric** and the `Output
    Method <p:py:meth:`nidcpower.Session.OutputFunction`.html>`__ property is set to **Pulse
    Current**.
    You must also specify a `Pulse Voltage Limit
    High <p:py:meth:`nidcpower.Session.PulseVoltageLimitHigh`.html>`__ to complete the
    asymmetric range.
    **Valid Values:** [-`Pulse Voltage Limit
    Range <p:py:meth:`nidcpower.Session.PulseVoltageLimitRange`.html>`__, -1% of `Pulse Voltage
    Limit Range <p:py:meth:`nidcpower.Session.PulseVoltageLimitRange`.html>`__]
    The range bounded by the limit high and limit low must include zero.
    **Default Value:** Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.
    **Related Topics:**
    `Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
    `Changing
    Ranges <NI_DC_Power_Supplies_Help.chm::/changing_ranges.html>`__
    `Overranging <NI_DC_Power_Supplies_Help.chm::/overranging.html>`__



    .. note:: The limit may be extended beyond the selected limit range if the
        `Overranging Enabled <p:py:meth:`nidcpower.Session.OverrangingEnabled`.html>`__ property is
        set to TRUE or if the `Output
        Method <p:py:meth:`nidcpower.Session.OutputFunction`.html>`__ property is set to a
        pulsing method.

    .. note:: One or more of the referenced methods are not in the Python API for this driver.


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        pulse_voltage_limit_low.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        pulse_voltage_limit_low.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].pulse_voltage_limit_low = var
            var = session['0,1'].pulse_voltage_limit_low

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

            - LabVIEW Property: **Source:Pulse Current:Pulse Voltage Limit Low**
            - C Attribute: **NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_LOW**

.. py:attribute:: pulse_voltage_limit_range

    Specifies the pulse voltage limit range, in volts, for the specified channel(s).
    The range defines the valid values to which you can set the pulse voltage limit and pulse bias voltage limit.
    This property is applicable only if the :py:data:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.PULSE_CURRENT`.
    For valid ranges, refer to the ranges topic for your device in the NI DC Power Supplies and SMUs Help.



    .. note:: The channel must be enabled for the specified current limit to take effect. Refer to the :py:data:`nidcpower.Session.output_enabled` property for more information about enabling the output channel.


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        pulse_voltage_limit_range.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        pulse_voltage_limit_range.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].pulse_voltage_limit_range = var
            var = session['0,1'].pulse_voltage_limit_range

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

            - LabVIEW Property: **Source:Pulse Current:Pulse Voltage Limit Range**
            - C Attribute: **NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_RANGE**

.. py:attribute:: query_instrument_status

    Specifies whether NI-DCPower queries the device status after each operation.
    Querying the device status is useful for debugging. After you validate your program, you can set this  property to False to disable status checking and maximize performance.
    NI-DCPower ignores status checking for particular properties regardless of the setting of this property.
    Use the :py:meth:`nidcpower.Session._initialize_with_channels` method to override this value.
    Default Value: True

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

            - LabVIEW Property: **Inherent IVI Attributes:User Options:Query Instrument Status**
            - C Attribute: **NIDCPOWER_ATTR_QUERY_INSTRUMENT_STATUS**

.. py:attribute:: range_check

    Specifies whether to validate property values and method parameters.
    If this property is enabled, NI-DCPower validates the parameter values that you pass to NI-DCPower methods.  Range checking parameters is useful for debugging. After you validate your program, you can set this  property to False to disable range checking and maximize performance.
    Use the :py:meth:`nidcpower.Session._initialize_with_channels` method to override this value.
    Default Value: True

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
            - C Attribute: **NIDCPOWER_ATTR_RANGE_CHECK**

.. py:attribute:: ready_for_pulse_trigger_event_output_terminal

    Specifies the output terminal for exporting the Ready For Pulse Trigger event.
    Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.

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
    Default Value: :py:data:`~nidcpower.Polarity.HIGH`



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.

    The following table lists the characteristics of this property.

    +----------------+-----------------+
    | Characteristic | Value           |
    +================+=================+
    | Datatype       | _enums.Polarity |
    +----------------+-----------------+
    | Permissions    | read-write      |
    +----------------+-----------------+
    | Channel Based  | False           |
    +----------------+-----------------+
    | Resettable     | No              |
    +----------------+-----------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Ready For Pulse Trigger Event:Pulse:Polarity**
            - C Attribute: **NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_PULSE_POLARITY**

.. py:attribute:: ready_for_pulse_trigger_event_pulse_width

    Specifies the width of the Ready For Pulse Trigger event, in seconds.
    The minimum event pulse width value for PXI Express devices is 250 ns.
    The maximum event pulse width value for all devices is 1.6 microseconds.
    Default Value: The default value for PXI Express devices is 250 ns



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.

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

    Specifies whether the IVI engine records the value coercions it makes for ViInt32 and ViReal64 properties.  Call the :py:meth:`nidcpower.Session.GetNextCoercionRecord` method to read and delete the earliest coercion record from the list.
    Default Value: The default value is False. Use the :py:meth:`nidcpower.Session._initialize_with_channels` method to override this value.



    .. note:: One or more of the referenced methods are not in the Python API for this driver.

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
            - C Attribute: **NIDCPOWER_ATTR_RECORD_COERCIONS**

.. py:attribute:: reset_average_before_measurement

    Specifies whether the measurement returned from any measurement call starts with a new measurement call (True) or  returns a measurement that has already begun or completed(False).
    for information about supported devices.
    When you set the :py:data:`nidcpower.Session.samples_to_average` property in the Running state, the output channel measurements might  move out of synchronization. While NI-DCPower automatically synchronizes measurements upon the initialization of a  session, you can force a synchronization in the running state before you run the :py:meth:`nidcpower.Session.measure_multiple` method. To  force a synchronization in the running state, set this property to True, and then run the :py:meth:`nidcpower.Session.measure_multiple`  method, specifying all channels in the channel name parameter. You can set the  :py:data:`nidcpower.Session.reset_average_before_measurement` property to False after the :py:meth:`nidcpower.Session.measure_multiple` method  completes.
    Default Value: True



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        reset_average_before_measurement.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        reset_average_before_measurement.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].reset_average_before_measurement = var
            var = session['0,1'].reset_average_before_measurement

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

            - LabVIEW Property: **Measurement:Advanced:Reset Average Before Measurement**
            - C Attribute: **NIDCPOWER_ATTR_RESET_AVERAGE_BEFORE_MEASUREMENT**

.. py:attribute:: samples_to_average

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




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        samples_to_average.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        samples_to_average.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].samples_to_average = var
            var = session['0,1'].samples_to_average

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Measurement:Samples To Average**
            - C Attribute: **NIDCPOWER_ATTR_SAMPLES_TO_AVERAGE**

.. py:attribute:: self_calibration_persistence

    Specifies whether the values calculated during self-calibration should be written to hardware to be used until the  next self-calibration or only used until the :py:meth:`nidcpower.Session.reset_device` method is called or the machine  is powered down.
    This property affects the behavior of the :py:meth:`nidcpower.Session.CalSelfCalibrate` method. When set to  :py:data:`~nidcpower.SelfCalibrationPersistence.KEEP_IN_MEMORY`, the values calculated by the :py:meth:`nidcpower.Session.CalSelfCalibrate` method are used in  the existing session, as well as in all further sessions until you call the :py:meth:`nidcpower.Session.reset_device` method  or restart the machine. When you set this property to :py:data:`~nidcpower.SelfCalibrationPersistence.WRITE_TO_EEPROM`, the values calculated  by the :py:meth:`nidcpower.Session.CalSelfCalibrate` method are written to hardware and used in the existing session and  in all subsequent sessions until another call to the :py:meth:`nidcpower.Session.CalSelfCalibrate` method is made.
    about supported devices.
    Default Value: :py:data:`~nidcpower.SelfCalibrationPersistence.KEEP_IN_MEMORY`



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information

    .. note:: One or more of the referenced methods are not in the Python API for this driver.

    The following table lists the characteristics of this property.

    +----------------+-----------------------------------+
    | Characteristic | Value                             |
    +================+===================================+
    | Datatype       | _enums.SelfCalibrationPersistence |
    +----------------+-----------------------------------+
    | Permissions    | read-write                        |
    +----------------+-----------------------------------+
    | Channel Based  | False                             |
    +----------------+-----------------------------------+
    | Resettable     | No                                |
    +----------------+-----------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Advanced:Self-Calibration Persistence**
            - C Attribute: **NIDCPOWER_ATTR_SELF_CALIBRATION_PERSISTENCE**

.. py:attribute:: sense

    Selects either local or remote sensing of the output voltage for the specified channel(s).
    Refer to the Local and Remote Sense topic in the NI DC Power Supplies and SMUs Help for more  information about sensing voltage on supported channels and about devices that support local and/or remote sensing.
    Default Value: The default value is :py:data:`~nidcpower.Sense.LOCAL` if the device supports local sense.  Otherwise, the default and only supported value is :py:data:`~nidcpower.Sense.REMOTE`.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        sense.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        sense.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].sense = var
            var = session['0,1'].sense

    The following table lists the characteristics of this property.

    +----------------+--------------+
    | Characteristic | Value        |
    +================+==============+
    | Datatype       | _enums.Sense |
    +----------------+--------------+
    | Permissions    | read-write   |
    +----------------+--------------+
    | Channel Based  | True         |
    +----------------+--------------+
    | Resettable     | No           |
    +----------------+--------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Measurement:Sense**
            - C Attribute: **NIDCPOWER_ATTR_SENSE**

.. py:attribute:: sequence_advance_trigger_type

    Specifies the behavior of the Sequence Advance trigger.
    for information about supported devices.
    Default Value: :py:data:`~nidcpower.TriggerType.NONE`



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

    The following table lists the characteristics of this property.

    +----------------+--------------------+
    | Characteristic | Value              |
    +================+====================+
    | Datatype       | _enums.TriggerType |
    +----------------+--------------------+
    | Permissions    | read-write         |
    +----------------+--------------------+
    | Channel Based  | False              |
    +----------------+--------------------+
    | Resettable     | No                 |
    +----------------+--------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggers:Sequence Advance Trigger:Trigger Type**
            - C Attribute: **NIDCPOWER_ATTR_SEQUENCE_ADVANCE_TRIGGER_TYPE**

.. py:attribute:: sequence_engine_done_event_output_terminal

    Specifies the output terminal for exporting the Sequence Engine Done Complete event.
    for information about supported devices.
    Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal  is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or  with the shortened terminal name, PXI_Trig0.



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

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
    for information about supported devices.
    Default Value: :py:data:`~nidcpower.Polarity.HIGH`



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

    The following table lists the characteristics of this property.

    +----------------+-----------------+
    | Characteristic | Value           |
    +================+=================+
    | Datatype       | _enums.Polarity |
    +----------------+-----------------+
    | Permissions    | read-write      |
    +----------------+-----------------+
    | Channel Based  | False           |
    +----------------+-----------------+
    | Resettable     | No              |
    +----------------+-----------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Sequence Engine Done Event:Pulse:Polarity**
            - C Attribute: **NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_PULSE_POLARITY**

.. py:attribute:: sequence_engine_done_event_pulse_width

    Specifies the width of the Sequence Engine Done event, in seconds.
    The minimum event pulse width value for PXI devices is 150 ns, and the minimum event pulse width value  for PXI Express devices is 250 ns.
    The maximum event pulse width value for all devices is 1.6 microseconds.
    for information about supported devices.
    Valid Values: 1.5e-7 to 1.6e-6 seconds
    Default Value: The default value for PXI devices is 150 ns. The default value for PXI Express devices is 250 ns.



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

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

    Specifies the output terminal for exporting the Sequence Iteration Complete event.
    for information about supported devices.
    Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal  is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or  with the shortened terminal name, PXI_Trig0.



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

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
    for information about supported devices.
    Default Value: :py:data:`~nidcpower.Polarity.HIGH`



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

    The following table lists the characteristics of this property.

    +----------------+-----------------+
    | Characteristic | Value           |
    +================+=================+
    | Datatype       | _enums.Polarity |
    +----------------+-----------------+
    | Permissions    | read-write      |
    +----------------+-----------------+
    | Channel Based  | False           |
    +----------------+-----------------+
    | Resettable     | No              |
    +----------------+-----------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Sequence Iteration Complete Event:Pulse:Polarity**
            - C Attribute: **NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_POLARITY**

.. py:attribute:: sequence_iteration_complete_event_pulse_width

    Specifies the width of the Sequence Iteration Complete event, in seconds.
    The minimum event pulse width value for PXI devices is 150 ns, and the minimum event pulse width  value for PXI Express devices is 250 ns.
    The maximum event pulse width value for all devices is 1.6 microseconds.
    the NI DC Power Supplies and SMUs Help for information about supported devices.
    Valid Values: 1.5e-7 to 1.6e-6 seconds
    Default Value: The default value for PXI devices is 150 ns. The default value for PXI Express devices is 250 ns.



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic in

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
    Refer to the Sequence Source Mode topic in the NI DC Power Supplies and SMUs Help for more information about the sequence  loop count.
    for information about supported devices. When the :py:data:`nidcpower.Session.sequence_loop_count_is_finite` property  is set to False, the :py:data:`nidcpower.Session.sequence_loop_count` property is ignored.
    Valid Range: 1 to 134217727
    Default Value: 1



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

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
    Refer to the Sequence Source Mode topic in the NI DC Power Supplies and SMUs Help for more information about  infinite sequencing.
    :py:data:`nidcpower.Session.sequence_loop_count_is_finite` property is set to False,  the :py:data:`nidcpower.Session.sequence_loop_count` property is ignored.
    Default Value: True



    .. note:: This property is not supported by all devices. When the

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

            - LabVIEW Property: **Source:Advanced:Sequence Loop Count Is Finite**
            - C Attribute: **NIDCPOWER_ATTR_SEQUENCE_LOOP_COUNT_IS_FINITE**

.. py:attribute:: simulate

    Specifies whether to simulate NI-DCPower I/O operations. True specifies that operation is simulated.
    Default Value: False

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
            - C Attribute: **NIDCPOWER_ATTR_SIMULATE**

.. py:attribute:: source_complete_event_output_terminal

    Specifies the output terminal for exporting the Source Complete event.
    for information about supported devices.
    Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you  can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal  name, PXI_Trig0.



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

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
    for information about supported devices.
    Default Value: :py:data:`~nidcpower.Polarity.HIGH`



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

    The following table lists the characteristics of this property.

    +----------------+-----------------+
    | Characteristic | Value           |
    +================+=================+
    | Datatype       | _enums.Polarity |
    +----------------+-----------------+
    | Permissions    | read-write      |
    +----------------+-----------------+
    | Channel Based  | False           |
    +----------------+-----------------+
    | Resettable     | No              |
    +----------------+-----------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Source Complete Event:Pulse:Polarity**
            - C Attribute: **NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_PULSE_POLARITY**

.. py:attribute:: source_complete_event_pulse_width

    Specifies the width of the Source Complete event, in seconds.
    for information about supported devices.
    The minimum event pulse width value for PXI devices is 150 ns, and the minimum event pulse width value  for PXI Express devices is 250 ns.
    The maximum event pulse width value for all devices is 1.6 microseconds
    Valid Values: 1.5e-7 to 1.6e-6 seconds
    Default Value: The default value for PXI devices is 150 ns. The default value for PXI Express devices is 250 ns.



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

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

    Determines when, in seconds, the device generates the Source Complete event, potentially starting a measurement if the  :py:data:`nidcpower.Session.measure_when` property is set to :py:data:`~nidcpower.MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE`.
    Refer to the Single Point Source Mode and Sequence Source Mode topics for more information.
    Valid Values: 0 to 167 seconds
    Default Value: 0.01667 seconds



    .. note:: Refer to Supported Properties by Device for information about supported devices.


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        source_delay.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        source_delay.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].source_delay = var
            var = session['0,1'].source_delay

    The following table lists the characteristics of this property.

    +----------------+--------------------+
    | Characteristic | Value              |
    +================+====================+
    | Datatype       | datetime.timedelta |
    +----------------+--------------------+
    | Permissions    | read-write         |
    +----------------+--------------------+
    | Channel Based  | True               |
    +----------------+--------------------+
    | Resettable     | No                 |
    +----------------+--------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Source:Advanced:Source Delay**
            - C Attribute: **NIDCPOWER_ATTR_SOURCE_DELAY**

.. py:attribute:: source_mode

    Specifies whether to run a single output point or a sequence. Refer to the Single Point Source Mode and Sequence Source  Mode topics in the NI DC Power Supplies and SMUs Help for more information about source modes.
    Default value: :py:data:`~nidcpower.SourceMode.SINGLE_POINT`

    The following table lists the characteristics of this property.

    +----------------+-------------------+
    | Characteristic | Value             |
    +================+===================+
    | Datatype       | _enums.SourceMode |
    +----------------+-------------------+
    | Permissions    | read-write        |
    +----------------+-------------------+
    | Channel Based  | False             |
    +----------------+-------------------+
    | Resettable     | No                |
    +----------------+-------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Source:Source Mode**
            - C Attribute: **NIDCPOWER_ATTR_SOURCE_MODE**

.. py:attribute:: source_trigger_type

    Specifies the behavior of the Source trigger.
    for information about supported devices.
    Default Value: :py:data:`~nidcpower.TriggerType.NONE`



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

    The following table lists the characteristics of this property.

    +----------------+--------------------+
    | Characteristic | Value              |
    +================+====================+
    | Datatype       | _enums.TriggerType |
    +----------------+--------------------+
    | Permissions    | read-write         |
    +----------------+--------------------+
    | Channel Based  | False              |
    +----------------+--------------------+
    | Resettable     | No                 |
    +----------------+--------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggers:Source Trigger:Trigger Type**
            - C Attribute: **NIDCPOWER_ATTR_SOURCE_TRIGGER_TYPE**

.. py:attribute:: specific_driver_class_spec_major_version

    Contains the major version number of the class specification with which NI-DCPower is compliant.

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

    Contains the minor version number of the class specification with which NI-DCPower is compliant.

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

    Contains the prefix for NI-DCPower. The name of each user-callable  method in NI-DCPower begins with this prefix.

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
    for information about supported devices.
    Default Value: :py:data:`~nidcpower.TriggerType.NONE`



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

    The following table lists the characteristics of this property.

    +----------------+--------------------+
    | Characteristic | Value              |
    +================+====================+
    | Datatype       | _enums.TriggerType |
    +----------------+--------------------+
    | Permissions    | read-write         |
    +----------------+--------------------+
    | Channel Based  | False              |
    +----------------+--------------------+
    | Resettable     | No                 |
    +----------------+--------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggers:Start Trigger:Trigger Type**
            - C Attribute: **NIDCPOWER_ATTR_START_TRIGGER_TYPE**

.. py:attribute:: supported_instrument_models

    Contains a comma-separated (,) list of supported NI-DCPower device models.

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

    Specifies the transient response. Refer to the Transient Response topic in the NI DC Power Supplies and SMUs Help  for more information about transient response.
    for information about supported devices.
    Default Value: :py:data:`~nidcpower.TransientResponse.NORMAL`



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        transient_response.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        transient_response.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].transient_response = var
            var = session['0,1'].transient_response

    The following table lists the characteristics of this property.

    +----------------+--------------------------+
    | Characteristic | Value                    |
    +================+==========================+
    | Datatype       | _enums.TransientResponse |
    +----------------+--------------------------+
    | Permissions    | read-write               |
    +----------------+--------------------------+
    | Channel Based  | True                     |
    +----------------+--------------------------+
    | Resettable     | No                       |
    +----------------+--------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Source:Transient Response**
            - C Attribute: **NIDCPOWER_ATTR_TRANSIENT_RESPONSE**

.. py:attribute:: voltage_compensation_frequency

    The frequency at which a pole-zero pair is added to the system when the channel is in  Constant Voltage mode.
    for information about supported devices.
    Default value: Determined by the value of the :py:data:`~nidcpower.TransientResponse.NORMAL` setting of  the :py:data:`nidcpower.Session.transient_response` property.



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        voltage_compensation_frequency.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        voltage_compensation_frequency.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].voltage_compensation_frequency = var
            var = session['0,1'].voltage_compensation_frequency

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

            - LabVIEW Property: **Source:Custom Transient Response:Voltage:Compensation Frequency**
            - C Attribute: **NIDCPOWER_ATTR_VOLTAGE_COMPENSATION_FREQUENCY**

.. py:attribute:: voltage_gain_bandwidth

    The frequency at which the unloaded loop gain extrapolates to 0 dB in the absence of additional poles and zeroes. This property takes effect when the channel is in Constant Voltage mode.
    for information about supported devices.
    Default Value: Determined by the value of the :py:data:`~nidcpower.TransientResponse.NORMAL` setting of the  :py:data:`nidcpower.Session.transient_response` property.



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        voltage_gain_bandwidth.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        voltage_gain_bandwidth.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].voltage_gain_bandwidth = var
            var = session['0,1'].voltage_gain_bandwidth

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

            - LabVIEW Property: **Source:Custom Transient Response:Voltage:Gain Bandwidth**
            - C Attribute: **NIDCPOWER_ATTR_VOLTAGE_GAIN_BANDWIDTH**

.. py:attribute:: voltage_level

    Specifies the voltage level, in volts, that the device attempts to generate on the specified channel(s).
    This property is applicable only if the :py:data:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.DC_VOLTAGE`.
    :py:data:`nidcpower.Session.output_enabled` property for more information about enabling the output channel.
    Valid Values: The valid values for this property are defined by the values you specify for the  :py:data:`nidcpower.Session.voltage_level_range` property.



    .. note:: The channel must be enabled for the specified voltage level to take effect. Refer to the


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        voltage_level.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        voltage_level.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].voltage_level = var
            var = session['0,1'].voltage_level

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

            - LabVIEW Property: **Source:DC Voltage:Voltage Level**
            - C Attribute: **NIDCPOWER_ATTR_VOLTAGE_LEVEL**

.. py:attribute:: voltage_level_autorange

    Specifies whether NI-DCPower automatically selects the voltage level range based on the desired voltage level  for the specified channel(s).
    If you set this property to :py:data:`~nidcpower.AutoZero.ON`, NI-DCPower ignores any changes you make to the  :py:data:`nidcpower.Session.voltage_level_range` property. If you change the :py:data:`nidcpower.Session.voltage_level_autorange` property from  :py:data:`~nidcpower.AutoZero.ON` to :py:data:`~nidcpower.AutoZero.OFF`, NI-DCPower retains the last value the :py:data:`nidcpower.Session.voltage_level_range`  property was set to (or the default value if the property was never set) and uses that value as  the voltage level range.
    Query the :py:data:`nidcpower.Session.voltage_level_range` property by using the :py:meth:`nidcpower.Session._get_attribute_vi_int32` method for  information about which range NI-DCPower automatically selects.
    The :py:data:`nidcpower.Session.voltage_level_autorange` property is applicable only if the :py:data:`nidcpower.Session.output_function` property  is set to :py:data:`~nidcpower.OutputFunction.DC_VOLTAGE`.
    Default Value: :py:data:`~nidcpower.AutoZero.OFF`




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        voltage_level_autorange.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        voltage_level_autorange.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].voltage_level_autorange = var
            var = session['0,1'].voltage_level_autorange

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

            - LabVIEW Property: **Source:DC Voltage:Voltage Level Autorange**
            - C Attribute: **NIDCPOWER_ATTR_VOLTAGE_LEVEL_AUTORANGE**

.. py:attribute:: voltage_level_range

    Specifies the voltage level range, in volts, for the specified channel(s).
    The range defines the valid values to which the voltage level can be set. Use the :py:data:`nidcpower.Session.voltage_level_autorange`  property to enable automatic selection of the voltage level range.
    The :py:data:`nidcpower.Session.voltage_level_range` property is applicable only if the :py:data:`nidcpower.Session.output_function` property is  set to :py:data:`~nidcpower.OutputFunction.DC_VOLTAGE`.
    :py:data:`nidcpower.Session.output_enabled` property for more information about enabling the output channel.
    For valid ranges, refer to the Ranges topic for your device in the NI DC Power Supplies and SMUs Help.



    .. note:: The channel must be enabled for the specified voltage level range to take effect. Refer to the


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        voltage_level_range.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        voltage_level_range.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].voltage_level_range = var
            var = session['0,1'].voltage_level_range

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

            - LabVIEW Property: **Source:DC Voltage:Voltage Level Range**
            - C Attribute: **NIDCPOWER_ATTR_VOLTAGE_LEVEL_RANGE**

.. py:attribute:: voltage_limit

    Specifies the voltage limit, in volts, that the output cannot exceed when generating the desired current level  on the specified channels.
    This property is applicable only if the :py:data:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.DC_CURRENT`  and the :py:data:`nidcpower.Session.compliance_limit_symmetry` property is set to :py:data:`~nidcpower.NIDCPOWER_VAL_SYMMETRIC`.
    :py:data:`nidcpower.Session.output_enabled` property for more information about enabling the output channel.
    Valid Values: The valid values for this property are defined by the values to which the  :py:data:`nidcpower.Session.voltage_limit_range` property is set.



    .. note:: The channel must be enabled for the specified current level to take effect. Refer to the

    .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        voltage_limit.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        voltage_limit.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].voltage_limit = var
            var = session['0,1'].voltage_limit

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

            - LabVIEW Property: **Source:DC Current:Voltage Limit**
            - C Attribute: **NIDCPOWER_ATTR_VOLTAGE_LIMIT**

.. py:attribute:: voltage_limit_autorange

    Specifies whether NI-DCPower automatically selects the voltage limit range based on the desired voltage limit for  the specified channel(s).
    If this property is set to :py:data:`~nidcpower.AutoZero.ON`, NI-DCPower ignores any changes you make to the  :py:data:`nidcpower.Session.voltage_limit_range` property. If you change the :py:data:`nidcpower.Session.voltage_limit_autorange` property from  :py:data:`~nidcpower.AutoZero.ON` to :py:data:`~nidcpower.AutoZero.OFF`, NI-DCPower retains the last value the :py:data:`nidcpower.Session.voltage_limit_range`  property was set to (or the default value if the property was never set) and uses that value as the voltage limit  range.
    Query the :py:data:`nidcpower.Session.voltage_limit_range` property by using the :py:meth:`nidcpower.Session._get_attribute_vi_int32` method to find out  which range NI-DCPower automatically selects.
    The :py:data:`nidcpower.Session.voltage_limit_autorange` property is applicable only if the :py:data:`nidcpower.Session.output_function` property  is set to :py:data:`~nidcpower.OutputFunction.DC_CURRENT`.
    Default Value: :py:data:`~nidcpower.AutoZero.OFF`




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        voltage_limit_autorange.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        voltage_limit_autorange.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].voltage_limit_autorange = var
            var = session['0,1'].voltage_limit_autorange

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

            - LabVIEW Property: **Source:DC Current:Voltage Limit Autorange**
            - C Attribute: **NIDCPOWER_ATTR_VOLTAGE_LIMIT_AUTORANGE**

.. py:attribute:: voltage_limit_high

    Specifies the maximum voltage, in volts, that the output can produce
    when generating the desired current on the specified channel(s).
    This property is applicable only if the `Compliance Limit
    Symmetry <p:py:meth:`nidcpower.Session.ComplianceLimitSymmetry`.html>`__ property is set to
    **Asymmetric** and the `Output
    Method <p:py:meth:`nidcpower.Session.OutputFunction`.html>`__ property is set to **DC
    Current**.
    You must also specify a `Voltage Limit
    Low <p:py:meth:`nidcpower.Session.VoltageLimitLow`.html>`__ to complete the asymmetric
    range.
    **Valid Values:** [1% of `Voltage Limit
    Range <p:py:meth:`nidcpower.Session.VoltageLimitRange`.html>`__, `Voltage Limit
    Range <p:py:meth:`nidcpower.Session.VoltageLimitRange`.html>`__]
    The range bounded by the limit high and limit low must include zero.
    **Default Value:** Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.
    **Related Topics:**
    `Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
    `Changing
    Ranges <NI_DC_Power_Supplies_Help.chm::/changing_ranges.html>`__
    `Overranging <NI_DC_Power_Supplies_Help.chm::/overranging.html>`__



    .. note:: The limit may be extended beyond the selected limit range if the
        `Overranging Enabled <p:py:meth:`nidcpower.Session.OverrangingEnabled`.html>`__ property is
        set to TRUE.

    .. note:: One or more of the referenced methods are not in the Python API for this driver.


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        voltage_limit_high.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        voltage_limit_high.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].voltage_limit_high = var
            var = session['0,1'].voltage_limit_high

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

            - LabVIEW Property: **Source:DC Current:Voltage Limit High**
            - C Attribute: **NIDCPOWER_ATTR_VOLTAGE_LIMIT_HIGH**

.. py:attribute:: voltage_limit_low

    Specifies the minimum voltage, in volts, that the output can produce
    when generating the desired current on the specified channel(s).
    This property is applicable only if the `Compliance Limit
    Symmetry <p:py:meth:`nidcpower.Session.ComplianceLimitSymmetry`.html>`__ property is set to
    **Asymmetric** and the `Output
    Method <p:py:meth:`nidcpower.Session.OutputFunction`.html>`__ property is set to **DC
    Current**.
    You must also specify a `Voltage Limit
    High <p:py:meth:`nidcpower.Session.VoltageLimitHigh`.html>`__ to complete the asymmetric
    range.
    **Valid Values:** [-`Voltage Limit
    Range <p:py:meth:`nidcpower.Session.VoltageLimitRange`.html>`__, -1% of `Voltage Limit
    Range <p:py:meth:`nidcpower.Session.VoltageLimitRange`.html>`__]
    The range bounded by the limit high and limit low must include zero.
    **Default Value:** Refer to `Supported Properties by
    Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
    the default value by device.
    **Related Topics:**
    `Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
    `Changing
    Ranges <NI_DC_Power_Supplies_Help.chm::/changing_ranges.html>`__
    `Overranging <NI_DC_Power_Supplies_Help.chm::/overranging.html>`__



    .. note:: The limit may be extended beyond the selected limit range if the
        `Overranging Enabled <p:py:meth:`nidcpower.Session.OverrangingEnabled`.html>`__ property is
        set to TRUE.

    .. note:: One or more of the referenced methods are not in the Python API for this driver.


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        voltage_limit_low.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        voltage_limit_low.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].voltage_limit_low = var
            var = session['0,1'].voltage_limit_low

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

            - LabVIEW Property: **Source:DC Current:Voltage Limit Low**
            - C Attribute: **NIDCPOWER_ATTR_VOLTAGE_LIMIT_LOW**

.. py:attribute:: voltage_limit_range

    Specifies the voltage limit range, in volts, for the specified channel(s).
    The range defines the valid values to which the voltage limit can be set. Use the :py:data:`nidcpower.Session.voltage_limit_autorange`  property to enable automatic selection of the voltage limit range.
    The :py:data:`nidcpower.Session.voltage_limit_range` property is applicable only if the :py:data:`nidcpower.Session.output_function` property is  set to :py:data:`~nidcpower.OutputFunction.DC_CURRENT`.
    :py:data:`nidcpower.Session.output_enabled` property for more information about enabling the output channel.
    For valid ranges, refer to the Ranges topic for your device in the NI DC Power Supplies and SMUs Help.



    .. note:: The channel must be enabled for the specified voltage limit range to take effect. Refer to the


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        voltage_limit_range.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        voltage_limit_range.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].voltage_limit_range = var
            var = session['0,1'].voltage_limit_range

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

            - LabVIEW Property: **Source:DC Current:Voltage Limit Range**
            - C Attribute: **NIDCPOWER_ATTR_VOLTAGE_LIMIT_RANGE**

.. py:attribute:: voltage_pole_zero_ratio

    The ratio of the pole frequency to the zero frequency when the channel is in  Constant Voltage mode.
    for information about supported devices.
    Default value: Determined by the value of the :py:data:`~nidcpower.TransientResponse.NORMAL` setting of the  :py:data:`nidcpower.Session.transient_response` property.



    .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        voltage_pole_zero_ratio.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        voltage_pole_zero_ratio.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].voltage_pole_zero_ratio = var
            var = session['0,1'].voltage_pole_zero_ratio

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

            - LabVIEW Property: **Source:Custom Transient Response:Voltage:Pole-Zero Ratio**
            - C Attribute: **NIDCPOWER_ATTR_VOLTAGE_POLE_ZERO_RATIO**


