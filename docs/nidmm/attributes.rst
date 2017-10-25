nidmm.Session properties
========================

.. py:currentmodule:: nidmm

.. py:attribute:: ac_max_freq

    Specifies the maximum frequency component of the input signal for AC
    measurements. This property is used only for error checking and verifies
    that the value of this parameter is less than the maximum frequency of
    the device. This property affects the DMM only when you set the Function
    property to AC measurements.

    The valid ranges are shown in the following table.

    +--------------------------------------+--------------+
    | NI 4080/4081/4082, NI 4070/4071/4072 | 1 Hz-300 kHz |
    +--------------------------------------+--------------+
    | NI 4065                              | 10 Hz-100 Hz |
    +--------------------------------------+--------------+
    | NI 4050/4060                         | 20 Hz-25 kHz |
    +--------------------------------------+--------------+

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

            - LabVIEW Property: **Configuration:Measurement Options:Max Frequency**
            - C Attribute: **NIDMM_ATTR_AC_MAX_FREQ**

.. py:attribute:: ac_min_freq

    Specifies the minimum frequency component of the input signal for AC
    measurements. This property affects the DMM only when you set the
    Function property to AC measurements. The valid range is 1 Hz-300 kHz
    for the NI 4080/4081/4082 and NI 4070/4071/4072, 10 Hz-100 Hz for the NI
    4065, and 20 Hz-25 kHz for the NI 4050 and NI 4060.

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

            - LabVIEW Property: **Configuration:Measurement Options:Min Frequency**
            - C Attribute: **NIDMM_ATTR_AC_MIN_FREQ**

.. py:attribute:: adc_calibration

    For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the ADC
    calibration mode.

    The following table lists the characteristics of this property.

    +----------------+---------------------------+
    | Characteristic | Value                     |
    +================+===========================+
    | Datatype       | :py:data:`ADCCalibration` |
    +----------------+---------------------------+
    | Permissions    | read-write                |
    +----------------+---------------------------+
    | Channel Based  | False                     |
    +----------------+---------------------------+
    | Resettable     | No                        |
    +----------------+---------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Configuration:Measurement Options:ADC Calibration**
            - C Attribute: **NIDMM_ATTR_ADC_CALIBRATION**

.. py:attribute:: aperture_time

    Specifies the measurement aperture time for the current configuration.
    Aperture time is specified in units set by the Aperture Time Units
    property. To override the default aperture, set this property to the
    desired aperture time after calling `niDMM Config
    Measurement <dmmviref.chm::/niDMM_Config_Measurement.html>`__. To return
    to the default, set this property to Aperture Time Auto (-1).

    Any number of powerline cycles (PLCs) within the minimum and maximum
    ranges is allowed on the NI 4080/4081/4082 and NI 4070/4071/4072.

    On the NI 4065 the minimum aperture time is 333 micro s and the maximum
    aperture time is 78.2 s. If setting the number of averages directly, the
    total measurement time is aperture time X the number of averages, which
    must be less than 72.8 s. The aperture times allowed are 333 micro s,
    667 micro s, or multiples of 1.11 ms—for example 1.11 ms, 2.22 ms, 3.33
    ms, and so on. If you set an aperture time other than 333 micro s, 667
    micro s, or multiples of 1.11 ms, the value will be coerced up to the
    next supported aperture time.

    On the NI 4060, when the powerline frequency is 60 Hz, the PLCs allowed
    are 1 PLC, 6 PLC, 12 PLC, and 120 PLC. When the powerline frequency is
    50 Hz, the PLCs allowed are 1 PLC, 5 PLC, 10 PLC, and 100 PLC.

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

            - LabVIEW Property: **Configuration:Advanced:Aperture Time**
            - C Attribute: **NIDMM_ATTR_APERTURE_TIME**

.. py:attribute:: aperture_time_units

    Specifies the units of aperture time for the current configuration.



    .. note:: The NI 4060 does not support an aperture time set in seconds.

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

            - LabVIEW Property: **Configuration:Advanced:Aperture Time Units**
            - C Attribute: **NIDMM_ATTR_APERTURE_TIME_UNITS**

.. py:attribute:: auto_range_value

    Specifies the value of the range. If auto ranging is enabled, shows the
    actual value of the active range. The value of this property is set
    during a read operation.

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

            - LabVIEW Property: **Configuration:Auto Range Value**
            - C Attribute: **NIDMM_ATTR_AUTO_RANGE_VALUE**

.. py:attribute:: auto_zero

    Specifies the AutoZero mode. This property is not supported for the NI
    4050.

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

            - LabVIEW Property: **Configuration:Measurement Options:Auto Zero**
            - C Attribute: **NIDMM_ATTR_AUTO_ZERO**

.. py:attribute:: buffer_size

    Specifies the size in samples of the internal data buffer. Maximum size
    is 134,217,727 (0X7FFFFFF) samples. When set to Auto (-1), NI-DMM
    chooses the buffer size.

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

            - LabVIEW Property: **Multi Point Acquisition:Advanced:Buffer Size**
            - C Attribute: **NIDMM_ATTR_BUFFER_SIZE**

.. py:attribute:: cable_comp_type

    For the NI 4081 and NI 4072 only, specifies the type of cable
    compensation that is applied to the current capacitance or inductance
    measurement for the current range.



    .. note:: Changing the function or the range using property nodes or through
        `niDMM Config
        Measurement <dmmviref.chm::/niDMM_Config_Measurement.html>`__ resets
        this property to the default value.

    The following table lists the characteristics of this property.

    +----------------+----------------------------------+
    | Characteristic | Value                            |
    +================+==================================+
    | Datatype       | :py:data:`CableCompensationType` |
    +----------------+----------------------------------+
    | Permissions    | read-write                       |
    +----------------+----------------------------------+
    | Channel Based  | False                            |
    +----------------+----------------------------------+
    | Resettable     | No                               |
    +----------------+----------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Configuration:Measurement Options:Capacitance and Inductance:Cable Compensation Type**
            - C Attribute: **NIDMM_ATTR_CABLE_COMP_TYPE**

.. py:attribute:: cache

    Specifies whether to cache the value of properties. When caching is
    enabled, the instrument driver keeps track of the current instrument
    settings and avoids sending redundant commands to the instrument. Thus,
    it significantly increases execution speed. The instrument driver can
    choose to always cache or to never cache particular properties
    regardless of the setting of this property. The default value is TRUE
    (1). Use `niDMM Initialize With
    Options <dmmviref.chm::/niDMM_Initialize_with_Options.html>`__ to
    override the default setting.

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
            - C Attribute: **NIDMM_ATTR_CACHE**

.. py:attribute:: channel_count

    Indicates the number of channels that the specific instrument driver
    supports. For each property for which the IVI\_VAL\_MULTI\_CHANNEL flag
    property is set, the IVI engine maintains a separate cache value for
    each channel.

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

            - LabVIEW Property: **Inherent IVI Attributes:Instrument Capabilities:Channel Count**
            - C Attribute: **NIDMM_ATTR_CHANNEL_COUNT**

.. py:attribute:: config_product_number

    The PCI product ID.

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

            - LabVIEW Property: **Inherent IVI Attributes:Instrument Identification:Instrument Product ID**
            - C Attribute: **NIDMM_ATTR_CONFIG_PRODUCT_NUMBER**

.. py:attribute:: current_source

    Specifies the current source provided during diode measurements.

    The NI 4050 and NI 4060 are not supported.

    The following table lists the characteristics of this property.

    +----------------+--------------------------+
    | Characteristic | Value                    |
    +================+==========================+
    | Datatype       | :py:data:`CurrentSource` |
    +----------------+--------------------------+
    | Permissions    | read-write               |
    +----------------+--------------------------+
    | Channel Based  | False                    |
    +----------------+--------------------------+
    | Resettable     | No                       |
    +----------------+--------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Configuration:Measurement Options:Current Source**
            - C Attribute: **NIDMM_ATTR_CURRENT_SOURCE**

.. py:attribute:: dc_bias

    For the NI 4082 and NI 4072 only, controls the available DC bias for
    capacitance measurements.

    The following table lists the characteristics of this property.

    +----------------+-------------------+
    | Characteristic | Value             |
    +================+===================+
    | Datatype       | :py:data:`DCBias` |
    +----------------+-------------------+
    | Permissions    | read-write        |
    +----------------+-------------------+
    | Channel Based  | False             |
    +----------------+-------------------+
    | Resettable     | No                |
    +----------------+-------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Configuration:Measurement Options:Capacitance and Inductance:Advanced:DC Bias**
            - C Attribute: **NIDMM_ATTR_DC_BIAS**

.. py:attribute:: dc_noise_rejection

    Specifies the DC noise rejection mode.



    .. note:: The NI 4050 and NI 4060 are not supported.

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

            - LabVIEW Property: **Configuration:Measurement Options:DC Noise Rejection**
            - C Attribute: **NIDMM_ATTR_DC_NOISE_REJECTION**

.. py:attribute:: driver_setup

    This property indicates the Driver Setup string that the user specified
    when initializing the driver. Some cases exist where the end-user must
    specify instrument driver options at initialization time. An example of
    this is specifying a particular instrument model from among a family of
    instruments that the driver supports. This is useful when using
    simulation. The end-user can specify driver-specific options through the
    Driver Setup keyword in the Option String parameter in `niDMM Initialize
    With Options <dmmviref.chm::/niDMM_Initialize_with_Options.html>`__. If
    the user does not specify a Driver Setup string, this property returns
    an empty string.

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

            - LabVIEW Property: **Inherent IVI Attributes:User Options:Driver Setup**
            - C Attribute: **NIDMM_ATTR_DRIVER_SETUP**

.. py:attribute:: freq_voltage_auto_range_value

    For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the value of
    the frequency voltage range. If auto ranging is enabled, shows the
    actual value of the active frequency voltage range. If not Auto Ranging,
    the value is the same as that of the Frequency Voltage Range property.

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

            - LabVIEW Property: **Configuration:Measurement Options:Frequency Voltage Auto Range Value**
            - C Attribute: **NIDMM_ATTR_FREQ_VOLTAGE_AUTO_RANGE_VALUE**

.. py:attribute:: freq_voltage_range

    For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the maximum
    amplitude of the input signal for frequency measurements.

    +----------------+------+----------------------------------------------------------------------------------------------------------------------------------+
    | Auto Range On  | -1.0 | Configures the DMM to take an Auto Range measurement to calculate the voltage range before each frequency or period measurement. |
    +----------------+------+----------------------------------------------------------------------------------------------------------------------------------+
    | Auto Range Off | -2.0 | Disables Auto Ranging. NI-DMM sets the voltage range to the last calculated voltage range.                                       |
    +----------------+------+----------------------------------------------------------------------------------------------------------------------------------+

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

            - LabVIEW Property: **Configuration:Measurement Options:Frequency Voltage Range**
            - C Attribute: **NIDMM_ATTR_FREQ_VOLTAGE_RANGE**

.. py:attribute:: function

    Specifies the measurement function. If you are setting this property
    directly, you must also set the `Operation
    Mode <pniDMM_OperationMode.html>`__ property, which controls whether the
    DMM takes standard single or multipoint measurements, or acquires a
    waveform. If you are programming properties directly, you must set the
    Operation Mode property before setting other configuration properties.
    If the Operation Mode property is set to Waveform Mode, the only valid
    function types are Waveform Voltage and Waveform Current. Set the
    Operation Mode property to IVIDMM Mode to set all other function values.

    The following table lists the characteristics of this property.

    +----------------+---------------------+
    | Characteristic | Value               |
    +================+=====================+
    | Datatype       | :py:data:`Function` |
    +----------------+---------------------+
    | Permissions    | read-write          |
    +----------------+---------------------+
    | Channel Based  | False               |
    +----------------+---------------------+
    | Resettable     | No                  |
    +----------------+---------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Configuration:Function**
            - C Attribute: **NIDMM_ATTR_FUNCTION**

.. py:attribute:: group_capabilities

    A string containing the capabilities and extension groups supported by
    the specific driver.

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

            - LabVIEW Property: **Inherent IVI Attributes:Specific Driver Capabilities:Group Capabilities**
            - C Attribute: **NIDMM_ATTR_GROUP_CAPABILITIES**

.. py:attribute:: input_resistance

    Specifies the input resistance of the instrument.



    .. note:: The NI 4050 and NI 4060 are not supported.

    The following table lists the characteristics of this property.

    +----------------+----------------------------+
    | Characteristic | Value                      |
    +================+============================+
    | Datatype       | :py:data:`InputResistance` |
    +----------------+----------------------------+
    | Permissions    | read-write                 |
    +----------------+----------------------------+
    | Channel Based  | False                      |
    +----------------+----------------------------+
    | Resettable     | No                         |
    +----------------+----------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Configuration:Measurement Options:Input Resistance**
            - C Attribute: **NIDMM_ATTR_INPUT_RESISTANCE**

.. py:attribute:: instrument_firmware_revision

    A string containing the instrument firmware revision number.

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

            - LabVIEW Property: **Inherent IVI Attributes:Instrument Identification:Instrument Firmware Revision**
            - C Attribute: **NIDMM_ATTR_INSTRUMENT_FIRMWARE_REVISION**

.. py:attribute:: instrument_manufacturer

    A string containing the manufacturer of the instrument.

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

            - LabVIEW Property: **Inherent IVI Attributes:Instrument Identification:Instrument Manufacturer**
            - C Attribute: **NIDMM_ATTR_INSTRUMENT_MANUFACTURER**

.. py:attribute:: instrument_model

    A string containing the instrument model.

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

            - LabVIEW Property: **Inherent IVI Attributes:Instrument Identification:Instrument Model**
            - C Attribute: **NIDMM_ATTR_INSTRUMENT_MODEL**

.. py:attribute:: interchange_check

    Specifies whether to perform interchangeability checking and log
    interchangeability warnings when you call niDMM VIs. Interchangeability
    warnings indicate that using your application with a different
    instrument might cause different behavior. Use `niDMM Get Next
    Interchange
    Warning <dmmviref.chm::/niDMM_Get_Next_Interchange_Warning.html>`__ to
    extract interchange warnings. Use `niDMM Clear Interchange
    Warnings <dmmviref.chm::/niDMM_Clear_Interchange_Warnings.html>`__ to
    clear the list of interchangeability warnings without reading them.
    Interchangeability checking examines the properties in a capability
    group only if you specify a value for at least one property within that
    group. Interchangeability warnings can occur when a property affects the
    behavior of the instrument and you have not set that property, or the
    property has been invalidated since you set it.

    +-------+---+
    | TRUE  | 1 |
    +-------+---+
    | FALSE | 0 |
    +-------+---+

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
            - C Attribute: **NIDMM_ATTR_INTERCHANGE_CHECK**

.. py:attribute:: latency

    Specifies the number of measurements transferred at a time from the
    instrument to an internal buffer. When set to Auto (-1), NI-DMM chooses
    the transfer size.

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

            - LabVIEW Property: **Multi Point Acquisition:Advanced:Latency**
            - C Attribute: **NIDMM_ATTR_LATENCY**

.. py:attribute:: lc_calculation_model

    For the NI 4082 and NI 4072 only, specifies the type of algorithm that
    the measurement processing uses for capacitance and inductance
    measurements.

    The following table lists the characteristics of this property.

    +----------------+-------------------------------+
    | Characteristic | Value                         |
    +================+===============================+
    | Datatype       | :py:data:`LCCalculationModel` |
    +----------------+-------------------------------+
    | Permissions    | read-write                    |
    +----------------+-------------------------------+
    | Channel Based  | False                         |
    +----------------+-------------------------------+
    | Resettable     | No                            |
    +----------------+-------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Configuration:Measurement Options:Capacitance and Inductance:Advanced:Calculation Model**
            - C Attribute: **NIDMM_ATTR_LC_CALCULATION_MODEL**

.. py:attribute:: lc_number_meas_to_average

    For the NI 4082 and NI 4072 only, specifies the number of LC
    measurements that are averaged to produce one reading.

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

            - LabVIEW Property: **Configuration:Measurement Options:Capacitance and Inductance:Number of LC Measurements To Average**
            - C Attribute: **NIDMM_ATTR_LC_NUMBER_MEAS_TO_AVERAGE**

.. py:attribute:: logical_name

    A string containing the logical name of the instrument.

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
            - C Attribute: **NIDMM_ATTR_LOGICAL_NAME**

.. py:attribute:: meas_complete_dest

    Specifies the destination of the measurement complete (MC) signal.

    To determine which values are supported by each device, refer to the
    `LabVIEW Trigger Routing <dmm.chm::/LVtrigger_routing.html>`__ section
    in the *NI Digital Multimeters Help*.



    .. note:: The NI 4050 is not supported.

    The following table lists the characteristics of this property.

    +----------------+------------------------------------+
    | Characteristic | Value                              |
    +================+====================================+
    | Datatype       | :py:data:`MeasurementCompleteDest` |
    +----------------+------------------------------------+
    | Permissions    | read-write                         |
    +----------------+------------------------------------+
    | Channel Based  | False                              |
    +----------------+------------------------------------+
    | Resettable     | No                                 |
    +----------------+------------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Trigger:Measurement Complete Dest**
            - C Attribute: **NIDMM_ATTR_MEAS_COMPLETE_DEST**

.. py:attribute:: meas_dest_slope

    Specifies the polarity of the generated measurement complete signal.

    The following table lists the characteristics of this property.

    +----------------+----------------------------------------+
    | Characteristic | Value                                  |
    +================+========================================+
    | Datatype       | :py:data:`MeasurementDestinationSlope` |
    +----------------+----------------------------------------+
    | Permissions    | read-write                             |
    +----------------+----------------------------------------+
    | Channel Based  | False                                  |
    +----------------+----------------------------------------+
    | Resettable     | No                                     |
    +----------------+----------------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Trigger:Measurement Destination Slope**
            - C Attribute: **NIDMM_ATTR_MEAS_DEST_SLOPE**

.. py:attribute:: number_of_averages

    Specifies the number of averages to perform in a measurement. For the NI
    4080/4081/4082 and NI 4070/4071/4072, applies only when the aperture
    time is not set to Auto and Auto Zero is ON. The Number of Averages
    Property will be ignored otherwise. The default is 4 for 7 1/2 digits;
    otherwise, the default is 1.

    The NI 4050 and NI 4060 are not supported.

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

            - LabVIEW Property: **Configuration:Advanced:Number Of Averages**
            - C Attribute: **NIDMM_ATTR_NUMBER_OF_AVERAGES**

.. py:attribute:: offset_comp_ohms

    For the NI 4080/4081/4082 and NI 4070/4071/4072, enables or disables
    offset compensated ohms.

    The following table lists the characteristics of this property.

    +----------------+----------------------------------+
    | Characteristic | Value                            |
    +================+==================================+
    | Datatype       | :py:data:`OffsetCompensatedOhms` |
    +----------------+----------------------------------+
    | Permissions    | read-write                       |
    +----------------+----------------------------------+
    | Channel Based  | False                            |
    +----------------+----------------------------------+
    | Resettable     | No                               |
    +----------------+----------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Configuration:Measurement Options:Offset Compensated Ohms**
            - C Attribute: **NIDMM_ATTR_OFFSET_COMP_OHMS**

.. py:attribute:: open_cable_comp_conductance

    For the NI 4082 and NI 4072 only, specifies the active part
    (conductance) of the open cable compensation. The valid range is any
    real number >0. The default value (-1.0) indicates that compensation has
    not taken place.



    .. note:: Changing the function or the range using property nodes or through
        `niDMM Config
        Measurement <dmmviref.chm::/niDMM_Config_Measurement.html>`__ resets
        this property to the default value.

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

            - LabVIEW Property: **Configuration:Measurement Options:Capacitance and Inductance:Open Cable Compensation Values:Conductance**
            - C Attribute: **NIDMM_ATTR_OPEN_CABLE_COMP_CONDUCTANCE**

.. py:attribute:: open_cable_comp_susceptance

    For the NI 4082 and NI 4072 only, specifies the reactive part
    (susceptance) of the open cable compensation. The valid range is any
    real number >0. The default value (-1.0) indicates that compensation has
    not taken place.



    .. note:: Changing the function or the range using property nodes or through
        `niDMM Config
        Measurement <dmmviref.chm::/niDMM_Config_Measurement.html>`__ resets
        this property to the default value.

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

            - LabVIEW Property: **Configuration:Measurement Options:Capacitance and Inductance:Open Cable Compensation Values:Susceptance**
            - C Attribute: **NIDMM_ATTR_OPEN_CABLE_COMP_SUSCEPTANCE**

.. py:attribute:: operation_mode

    Specifies how the DMM acquires data.

    When you call `niDMM Config
    Measurement <dmmviref.chm::/niDMM_Config_Measurement.html>`__, NI-DMM
    sets this property to IVIDMM Mode. When you call `niDMM Configure
    Waveform
    Acquisition <dmmviref.chm::/niDMM_Configure_Waveform_Acquisition.html>`__,
    NI-DMM sets this property to Waveform Mode. If you are programming
    properties directly, you must set this property before setting other
    configuration properties.



    .. note:: The NI 4050 and NI 4060 are not supported.

    The following table lists the characteristics of this property.

    +----------------+--------------------------+
    | Characteristic | Value                    |
    +================+==========================+
    | Datatype       | :py:data:`OperationMode` |
    +----------------+--------------------------+
    | Permissions    | read-write               |
    +----------------+--------------------------+
    | Channel Based  | False                    |
    +----------------+--------------------------+
    | Resettable     | No                       |
    +----------------+--------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Configuration:Advanced:Operation Mode**
            - C Attribute: **NIDMM_ATTR_OPERATION_MODE**

.. py:attribute:: powerline_freq

    Specifies the powerline frequency. The NI 4060 and NI 4050 use this
    value to select an aperture time to reject powerline noise by selecting
    the appropriate internal sample clock and filter. The NI 4065, NI
    4070/4071/4072, and NI 4080/4081/4082 use this value to select timebases
    for setting the Aperture Time property in powerline cycles.

    After configuring powerline frequency, set the Aperture Time Units
    property to PLCs. When setting the Aperture Time property, select the
    number of PLCs for the powerline frequency. For example, if powerline
    frequency = 50 Hz (or 20 ms) and aperture time in PLCs = 5, then
    aperture time in seconds = 20 ms \* 5 PLCs = 100 ms. Similarly, if
    powerline frequency = 60 Hz (or 16.667 ms) and aperture time in PLCs =
    6, then aperture time in seconds = 16.667 ms \* 6 PLCs = 100 ms.



    .. note:: For 400 Hz powerline frequency, use the 50 Hz setting.

    The following table lists the characteristics of this property.

    +----------------+-------------------------------+
    | Characteristic | Value                         |
    +================+===============================+
    | Datatype       | :py:data:`PowerlineFrequency` |
    +----------------+-------------------------------+
    | Permissions    | read-write                    |
    +----------------+-------------------------------+
    | Channel Based  | False                         |
    +----------------+-------------------------------+
    | Resettable     | No                            |
    +----------------+-------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Configuration:Measurement Options:Powerline Frequency**
            - C Attribute: **NIDMM_ATTR_POWERLINE_FREQ**

.. py:attribute:: range

    Specifies the measurement range. Use positive values to represent the
    absolute value of the maximum expected measurement. The value is in
    units appropriate for the current value of the Function property. For
    example, if the Function property is set to DC Volts, the units are
    volts.

    +--------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | (-1.0) | Auto Range On   | NI-DMM performs an Auto Range before acquiring the measurement.                                                                                                                                                               |
    +--------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | (-2.0) | Auto Range Off  | NI-DMM sets the Range to the current `Auto Range Value <pnidmm_AutoRangeValue.html>`__ and uses this range for all subsequent measurements until the measurement configuration is changed.                                    |
    +--------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | (-3.0) | Auto Range Once | NI-DMM performs an Auto Range before acquiring the next measurement. The `Auto Range Value <pnidmm_AutoRangeValue.html>`__ is stored and used for all subsequent measurements until the measurement configuration is changed. |
    +--------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    .. note:: The NI 4050, NI 4060, and NI 4065 only support Auto Range when the
        trigger and sample trigger are set to Immediate.

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

            - LabVIEW Property: **Configuration:Range**
            - C Attribute: **NIDMM_ATTR_RANGE**

.. py:attribute:: range_check

    Specifies whether to validate property values and VI parameters. If
    enabled, the instrument driver validates the parameter values passed to
    driver VIs. Range checking parameters is very useful for debugging.
    After the user program is validated, you can set this property to FALSE
    (0) to disable range checking and maximize performance. The default
    value is TRUE (1). Use `niDMM Initialize With
    Options <dmmviref.chm::/niDMM_Initialize_With_Options.html>`__ to
    override the default setting.

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
            - C Attribute: **NIDMM_ATTR_RANGE_CHECK**

.. py:attribute:: record_coercions

    Specifies whether the IVI engine keeps a list of the value coercions it
    makes for ViInt32 and ViReal64 properties. The default value is FALSE
    (0). Use `niDMM Initialize With
    Options <dmmviref.chm::/niDMM_Initialize_with_Options.html>`__ to
    override the default setting. Use `niDMM Get Next Coercion
    Record <dmmviref.chm::/niDMM_Get_Next_Coercion_Record.html>`__ to
    extract and delete the oldest coercion record from the list.

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
            - C Attribute: **NIDMM_ATTR_RECORD_COERCIONS**

.. py:attribute:: resolution_absolute

    Specifies the measurement resolution in absolute units. Setting this
    property to higher values increases the measurement accuracy. Setting
    this property to lower values increases the measurement speed.



    .. note:: NI-DMM ignores this property for capacitance and inductance measurements
        on the NI 4082 and NI 4072. To achieve better resolution for such
        measurements, use the Number of LC Measurements to Average property.

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

            - LabVIEW Property: **Configuration:Absolute Resolution**
            - C Attribute: **NIDMM_ATTR_RESOLUTION_ABSOLUTE**

.. py:attribute:: sample_count

    Specifies the number of measurements the DMM takes each time it receives
    a trigger in a multiple point acquisition. Setting Sample Count to 0 on
    the NI 4050 and NI 4060 causes the device to take continuous
    measurements. Otherwise, setting Sample Count to 0 causes the
    conditional statement "Measurements equal to Sample Count" to always
    evaluate to False, and causes the DMM to continue taking measurements in
    the inner loop.

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

            - LabVIEW Property: **Multi Point Acquisition:Sample Count**
            - C Attribute: **NIDMM_ATTR_SAMPLE_COUNT**

.. py:attribute:: sample_interval

    Specifies the amount of time in seconds the DMM waits between
    measurement cycles. This property only applies when the Sample Trigger
    property is set to INTERVAL. The default value (-1) ensures that the DMM
    settles for a recommended time, which is the same as using an immediate
    trigger.

    The NI 4065 and NI 4070/4071/4072 use the value specified in this
    property as additional delay. On these devices, the onboard timing
    resolution is 34.72 ns and the valid range is 0-149 s.

    On the NI 4060, the value for this property is used as the settling
    time. When this property is set to 0, the NI 4060 does not settle
    between measurement cycles. The onboard timing resolution is 1 micro s
    on the NI 4060.

    Only positive values are valid when setting the sample interval.



    .. note:: The NI 4080/4081/4082 and NI 4050 are not supported.

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

            - LabVIEW Property: **Multi Point Acquisition:Sample Interval**
            - C Attribute: **NIDMM_ATTR_SAMPLE_INTERVAL**

.. py:attribute:: sample_trigger

    Specifies the sample trigger source.

    To determine which values are supported by each device, refer to the
    `LabVIEW Trigger Routing <dmm.chm::/LVtrigger_routing.html>`__ section
    in the *NI Digital Multimeters Help*.

    The following table lists the characteristics of this property.

    +----------------+--------------------------+
    | Characteristic | Value                    |
    +================+==========================+
    | Datatype       | :py:data:`SampleTrigger` |
    +----------------+--------------------------+
    | Permissions    | read-write               |
    +----------------+--------------------------+
    | Channel Based  | False                    |
    +----------------+--------------------------+
    | Resettable     | No                       |
    +----------------+--------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Multi Point Acquisition:Sample Trigger**
            - C Attribute: **NIDMM_ATTR_SAMPLE_TRIGGER**

.. py:attribute:: sample_trigger_slope

    Specifies the edge of the signal from the specified sample trigger
    source on which the DMM is triggered.

    The following table lists the characteristics of this property.

    +----------------+----------------------------+
    | Characteristic | Value                      |
    +================+============================+
    | Datatype       | :py:data:`SampleTrigSlope` |
    +----------------+----------------------------+
    | Permissions    | read-write                 |
    +----------------+----------------------------+
    | Channel Based  | False                      |
    +----------------+----------------------------+
    | Resettable     | No                         |
    +----------------+----------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Multi Point Acquisition:Sample Trig Slope**
            - C Attribute: **NIDMM_ATTR_SAMPLE_TRIGGER_SLOPE**

.. py:attribute:: serial_number

    A string containing the serial number of the instrument. This property
    corresponds to the serial number label that is attached to most
    products.

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

            - LabVIEW Property: **Inherent IVI Attributes:Instrument Identification:Instrument Serial Number**
            - C Attribute: **NIDMM_ATTR_SERIAL_NUMBER**

.. py:attribute:: settle_time

    Specifies the settling time in seconds. Use this property to override
    the default settling time. To return to the default, set this property
    to Auto (-1).



    .. note:: The NI 4050 and NI 4060 are not supported.

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

            - LabVIEW Property: **Configuration:Advanced:Settle Time**
            - C Attribute: **NIDMM_ATTR_SETTLE_TIME**

.. py:attribute:: short_cable_comp_reactance

    For the NI 4082 and NI 4072 only, represents the reactive part
    (reactance) of the short cable compensation. The valid range is any real
    number >0. The default value (-1) indicates that compensation has not
    taken place.



    .. note:: Changing the VI or the range through this property or through `niDMM
        Config Measurement <dmmviref.chm::/niDMM_Config_Measurement.html>`__
        resets this property to the default value.

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

            - LabVIEW Property: **Configuration:Measurement Options:Capacitance and Inductance:Short Cable Compensation Values:Reactance**
            - C Attribute: **NIDMM_ATTR_SHORT_CABLE_COMP_REACTANCE**

.. py:attribute:: short_cable_comp_resistance

    For the NI 4082 and NI 4072 only, represents the active part
    (resistance) of the short cable compensation. The valid range is any
    real number >0. The default value (-1) indicates that compensation has
    not taken place.



    .. note:: Changing the VI or the range through this property or through `niDMM
        Config Measurement <dmmviref.chm::/niDMM_Config_Measurement.html>`__
        resets this property to the default value.

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

            - LabVIEW Property: **Configuration:Measurement Options:Capacitance and Inductance:Short Cable Compensation Values:Resistance**
            - C Attribute: **NIDMM_ATTR_SHORT_CABLE_COMP_RESISTANCE**

.. py:attribute:: shunt_value

    For the NI 4050 only, specifies the shunt resistance value.



    .. note:: The NI 4050 requires an external shunt resistor for current
        measurements. This property should be set to the value of the shunt
        resistor.

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

            - LabVIEW Property: **Configuration:Measurement Options:Shunt Value**
            - C Attribute: **NIDMM_ATTR_SHUNT_VALUE**

.. py:attribute:: simulate

    Specifies whether to simulate instrument driver I/O operations. If
    simulation is enabled, instrument driver functions perform range
    checking and call IVI Get and Set VIs, but they do not perform
    instrument I/O. For output parameters that represent instrument data,
    the instrument driver VIs return calculated values. The default value is
    FALSE (0). Use `niDMM Initialize With
    Options <dmmviref.chm::/niDMM_Initialize_with_Options.html>`__ to
    override the default setting.



    .. note:: Simulate can only be set within the `niDMM Initialize With
        Options <dmmviref.chm::/niDMM_Initialize_with_Options.html>`__ VI. The
        property value cannot be changed outside of the VI.

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
            - C Attribute: **NIDMM_ATTR_SIMULATE**

.. py:attribute:: specific_driver_class_spec_major_version

    The major version number of the class specification for the specific
    driver.

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

            - LabVIEW Property: **Inherent IVI Attributes:Specific Driver Identification:Specific Driver Class Spec Major Version**
            - C Attribute: **NIDMM_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION**

.. py:attribute:: specific_driver_class_spec_minor_version

    The minor version number of the class specification for the specific
    driver.

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

            - LabVIEW Property: **Inherent IVI Attributes:Specific Driver Identification:Specific Driver Class Spec Minor Version**
            - C Attribute: **NIDMM_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION**

.. py:attribute:: specific_driver_description

    A string containing a description of the specific driver.

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

            - LabVIEW Property: **Inherent IVI Attributes:Specific Driver Identification:Specific Driver Description**
            - C Attribute: **NIDMM_ATTR_SPECIFIC_DRIVER_DESCRIPTION**

.. py:attribute:: specific_driver_vendor

    A string containing the vendor of the specific driver.

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

            - LabVIEW Property: **Inherent IVI Attributes:Specific Driver Identification:Specific Driver Vendor**
            - C Attribute: **NIDMM_ATTR_SPECIFIC_DRIVER_VENDOR**

.. py:attribute:: supported_instrument_models

    A string containing the instrument models supported by the specific
    driver.

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

            - LabVIEW Property: **Inherent IVI Attributes:Specific Driver Capabilities:Supported Instrument Models**
            - C Attribute: **NIDMM_ATTR_SUPPORTED_INSTRUMENT_MODELS**

.. py:attribute:: temp_rtd_a

    Specifies the Callendar-Van Dusen A coefficient for RTD scaling when the
    **RTD Type property** is set to Custom.

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

            - LabVIEW Property: **Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD A**
            - C Attribute: **NIDMM_ATTR_TEMP_RTD_A**

.. py:attribute:: temp_rtd_b

    Specifies the Callendar-Van Dusen B coefficient for RTD scaling when the
    **RTD Type property** is set to Custom.

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

            - LabVIEW Property: **Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD B**
            - C Attribute: **NIDMM_ATTR_TEMP_RTD_B**

.. py:attribute:: temp_rtd_c

    Specifies the Callendar-Van Dusen C coefficient for RTD scaling when the
    **RTD Type property** is set to Custom.

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

            - LabVIEW Property: **Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD C**
            - C Attribute: **NIDMM_ATTR_TEMP_RTD_C**

.. py:attribute:: temp_rtd_res

    Specifies the RTD resistance at 0 degrees Celsius.

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

            - LabVIEW Property: **Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD Resistance**
            - C Attribute: **NIDMM_ATTR_TEMP_RTD_RES**

.. py:attribute:: temp_rtd_type

    Specifies the RTD type.

    The following table lists the characteristics of this property.

    +----------------+--------------------+
    | Characteristic | Value              |
    +================+====================+
    | Datatype       | :py:data:`RTDType` |
    +----------------+--------------------+
    | Permissions    | read-write         |
    +----------------+--------------------+
    | Channel Based  | False              |
    +----------------+--------------------+
    | Resettable     | No                 |
    +----------------+--------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD Type**
            - C Attribute: **NIDMM_ATTR_TEMP_RTD_TYPE**

.. py:attribute:: temp_tc_fixed_ref_junc

    Specifies the value of the fixed reference junction temperature for a
    thermocouple in degrees Celsius.

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

            - LabVIEW Property: **Configuration:Measurement Options:Temperature:Thermocouple:Fixed Reference Junction**
            - C Attribute: **NIDMM_ATTR_TEMP_TC_FIXED_REF_JUNC**

.. py:attribute:: temp_tc_ref_junc_type

    Specifies the thermocouple reference junction type.

    The following table lists the characteristics of this property.

    +----------------+----------------------------------------------+
    | Characteristic | Value                                        |
    +================+==============================================+
    | Datatype       | :py:data:`ThermocoupleReferenceJunctionType` |
    +----------------+----------------------------------------------+
    | Permissions    | read-write                                   |
    +----------------+----------------------------------------------+
    | Channel Based  | False                                        |
    +----------------+----------------------------------------------+
    | Resettable     | No                                           |
    +----------------+----------------------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Configuration:Measurement Options:Temperature:Thermocouple:Reference Junction Type**
            - C Attribute: **NIDMM_ATTR_TEMP_TC_REF_JUNC_TYPE**

.. py:attribute:: temp_tc_type

    Specifies the thermocouple type.

    The following table lists the characteristics of this property.

    +----------------+-----------------------------+
    | Characteristic | Value                       |
    +================+=============================+
    | Datatype       | :py:data:`ThermocoupleType` |
    +----------------+-----------------------------+
    | Permissions    | read-write                  |
    +----------------+-----------------------------+
    | Channel Based  | False                       |
    +----------------+-----------------------------+
    | Resettable     | No                          |
    +----------------+-----------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Configuration:Measurement Options:Temperature:Thermocouple:Thermocouple Type**
            - C Attribute: **NIDMM_ATTR_TEMP_TC_TYPE**

.. py:attribute:: temp_thermistor_a

    Specifies the Steinhart-Hart A coefficient for thermistor scaling when
    the **Thermistor Type property** is set to Custom.

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

            - LabVIEW Property: **Configuration:Measurement Options:Temperature:Thermistor:Thermistor A**
            - C Attribute: **NIDMM_ATTR_TEMP_THERMISTOR_A**

.. py:attribute:: temp_thermistor_b

    Specifies the Steinhart-Hart B coefficient for thermistor scaling when
    the **Thermistor Type property** is set to Custom.

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

            - LabVIEW Property: **Configuration:Measurement Options:Temperature:Thermistor:Thermistor B**
            - C Attribute: **NIDMM_ATTR_TEMP_THERMISTOR_B**

.. py:attribute:: temp_thermistor_c

    Specifies the Steinhart-Hart C coefficient for thermistor scaling when
    the **Thermistor Type property** is set to Custom.

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

            - LabVIEW Property: **Configuration:Measurement Options:Temperature:Thermistor:Thermistor C**
            - C Attribute: **NIDMM_ATTR_TEMP_THERMISTOR_C**

.. py:attribute:: temp_thermistor_type

    Specifies the thermistor type.

    The following table lists the characteristics of this property.

    +----------------+---------------------------+
    | Characteristic | Value                     |
    +================+===========================+
    | Datatype       | :py:data:`ThermistorType` |
    +----------------+---------------------------+
    | Permissions    | read-write                |
    +----------------+---------------------------+
    | Channel Based  | False                     |
    +----------------+---------------------------+
    | Resettable     | No                        |
    +----------------+---------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Configuration:Measurement Options:Temperature:Thermistor:Thermistor Type**
            - C Attribute: **NIDMM_ATTR_TEMP_THERMISTOR_TYPE**

.. py:attribute:: temp_transducer_type

    Specifies the transducer type.

    The following table lists the characteristics of this property.

    +----------------+---------------------------+
    | Characteristic | Value                     |
    +================+===========================+
    | Datatype       | :py:data:`TransducerType` |
    +----------------+---------------------------+
    | Permissions    | read-write                |
    +----------------+---------------------------+
    | Channel Based  | False                     |
    +----------------+---------------------------+
    | Resettable     | No                        |
    +----------------+---------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Configuration:Measurement Options:Temperature:Transducer Type**
            - C Attribute: **NIDMM_ATTR_TEMP_TRANSDUCER_TYPE**

.. py:attribute:: trigger_count

    Specifies the number of triggers the DMM receives before returning to
    the Idle state. This property can be set to any positive ViInt32 value
    for the NI 4065, NI 4070/4071/4072, and NI 4080/4081/4082.

    The NI 4050/4060 only support this property being set to 1.

    Refer to `Multiple Point Acquisitions <dmm.chm::/multi_point.html>`__ in
    the *NI Digital Multimeters Help* for more information.

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

            - LabVIEW Property: **Multi Point Acquisition:Trigger Count**
            - C Attribute: **NIDMM_ATTR_TRIGGER_COUNT**

.. py:attribute:: trigger_delay

    Specifies the time (in seconds) that the DMM waits after it has received
    a trigger before taking a measurement. The default value is Auto Delay
    (-1), which means that the DMM waits an appropriate settling time before
    taking the measurement.

    The NI 4080/4081/4082 uses the value specified in this property as
    additional settling time. The valid range for Trigger Delay is Auto
    Delay (-1) or 0.0 - 150.0 seconds, and the onboard timing resolution is
    10.0 ns.

    The NI 4065 and NI 4070/4071/4072 use the value specified in this
    property as additional settling time. For these devices, the valid range
    for Trigger Delay is Auto Delay (-1) or 0.0 - 149.0 seconds and the
    onboard timing resolution is 34.72 ns.

    On the NI 4060, if this property is set to 0, the DMM does not settle
    before taking the measurement. On the NI 4060, the valid range for
    Trigger Delay (-1) is 0.0-12.0 seconds and the onboard timing resolution
    is 100 ms.

    When using the NI 4050, this property must be set to Auto Delay (-1).

    Use positive values to set the trigger delay in seconds.

    Valid Range: Auto Delay (-1.0), 0.0-12.0 seconds (NI 4060 only),
    0.0-149.0 seconds (NI 4065 and NI 4070/4071/4072)

    Default Value: Auto Delay

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

            - LabVIEW Property: **Trigger:Trigger Delay**
            - C Attribute: **NIDMM_ATTR_TRIGGER_DELAY**

.. py:attribute:: trigger_slope

    Specifies the edge of the signal from the specified trigger source on
    which the DMM is triggered.

    The following table lists the characteristics of this property.

    +----------------+-------------------------+
    | Characteristic | Value                   |
    +================+=========================+
    | Datatype       | :py:data:`TriggerSlope` |
    +----------------+-------------------------+
    | Permissions    | read-write              |
    +----------------+-------------------------+
    | Channel Based  | False                   |
    +----------------+-------------------------+
    | Resettable     | No                      |
    +----------------+-------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Trigger:Trigger Slope**
            - C Attribute: **NIDMM_ATTR_TRIGGER_SLOPE**

.. py:attribute:: trigger_source

    Specifies the trigger source. When `niDMM
    Initiate <dmmviref.chm::/niDMM_Initiate.html>`__ is called, the DMM
    waits for the trigger specified with this property. After it receives
    the trigger, the DMM waits the length of time specified with the
    `Trigger Delay <pnidmm_TriggerDelay.html>`__ property. The DMM then
    takes a measurement.

    To determine which values are supported by each device, refer to the
    `LabVIEW Trigger Routing <dmm.chm::/LVtrigger_routing.html>`__ section
    in the *NI Digital Multimeters Help*.

    The following table lists the characteristics of this property.

    +----------------+--------------------------+
    | Characteristic | Value                    |
    +================+==========================+
    | Datatype       | :py:data:`TriggerSource` |
    +----------------+--------------------------+
    | Permissions    | read-write               |
    +----------------+--------------------------+
    | Channel Based  | False                    |
    +----------------+--------------------------+
    | Resettable     | No                       |
    +----------------+--------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Trigger:Trigger Source**
            - C Attribute: **NIDMM_ATTR_TRIGGER_SOURCE**

.. py:attribute:: waveform_coupling

    For the NI 4080/4081/4082 and NI 4070/4071/4072 only, specifies the
    coupling during a waveform acquisition.

    The following table lists the characteristics of this property.

    +----------------+-----------------------------+
    | Characteristic | Value                       |
    +================+=============================+
    | Datatype       | :py:data:`WaveformCoupling` |
    +----------------+-----------------------------+
    | Permissions    | read-write                  |
    +----------------+-----------------------------+
    | Channel Based  | False                       |
    +----------------+-----------------------------+
    | Resettable     | No                          |
    +----------------+-----------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Waveform Acquisition:Waveform Coupling**
            - C Attribute: **NIDMM_ATTR_WAVEFORM_COUPLING**

.. py:attribute:: waveform_points

    For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the number of
    points to acquire in a waveform acquisition.

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

            - LabVIEW Property: **Waveform Acquisition:Waveform Points**
            - C Attribute: **NIDMM_ATTR_WAVEFORM_POINTS**

.. py:attribute:: waveform_rate

    Specifies the rate of the waveform acquisition in samples per second
    (S/s). The valid rate is calculated by dividing 1,800,000 by an integer
    divisor, and the rate falls between 10 and 1,800,000 samples per second.
    The waveform rate is coerced upwards to the next valid rate. The default
    value is 1,800,000 samples per second. Not supported by NI 4065.

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

            - LabVIEW Property: **Waveform Acquisition:Waveform Rate**
            - C Attribute: **NIDMM_ATTR_WAVEFORM_RATE**


