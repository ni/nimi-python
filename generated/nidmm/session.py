# -*- coding: utf-8 -*-
# This file was generated
import ctypes

from nidmm import attributes
from nidmm import ctypes_types
from nidmm import enums
from nidmm import errors
from nidmm import library_singleton
from nidmm import python_types


class _Acquisition(object):
    def __init__(self, session):
        self.session = session

    def __enter__(self):
        self.session._initiate()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.session._abort()


class _SessionBase(object):
    '''Base class for all NI-DMM sessions.'''

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

    ac_max_freq = attributes.AttributeViReal64(1250007)
    '''
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
    '''
    ac_min_freq = attributes.AttributeViReal64(1250006)
    '''
    Specifies the minimum frequency component of the input signal for AC
    measurements. This property affects the DMM only when you set the
    Function property to AC measurements. The valid range is 1 Hz-300 kHz
    for the NI 4080/4081/4082 and NI 4070/4071/4072, 10 Hz-100 Hz for the NI
    4065, and 20 Hz-25 kHz for the NI 4050 and NI 4060.
    '''
    adc_calibration = attributes.AttributeEnum(attributes.AttributeViInt32, enums.ADCCalibration, 1150022)
    '''
    For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the ADC
    calibration mode.
    '''
    aperture_time = attributes.AttributeViReal64(1250321)
    '''
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
    '''
    aperture_time_units = attributes.AttributeEnum(attributes.AttributeViInt32, enums.ApertureTimeUnits, 1250322)
    '''
    Specifies the units of aperture time for the current configuration.

    Note: The NI 4060 does not support an aperture time set in seconds.
    '''
    auto_range_value = attributes.AttributeViReal64(1250331)
    '''
    Specifies the value of the range. If auto ranging is enabled, shows the
    actual value of the active range. The value of this property is set
    during a read operation.
    '''
    auto_zero = attributes.AttributeEnum(attributes.AttributeViInt32, enums.AutoZero, 1250332)
    '''
    Specifies the AutoZero mode. This property is not supported for the NI
    4050.
    '''
    buffer_size = attributes.AttributeViInt32(1150037)
    '''
    Specifies the size in samples of the internal data buffer. Maximum size
    is 134,217,727 (0X7FFFFFF) samples. When set to Auto (-1), NI-DMM
    chooses the buffer size.
    '''
    cable_comp_type = attributes.AttributeEnum(attributes.AttributeViInt32, enums.CableCompensationType, 1150045)
    '''
    For the NI 4081 and NI 4072 only, specifies the type of cable
    compensation that is applied to the current capacitance or inductance
    measurement for the current range.

    Note:
    Changing the function or the range using property nodes or through
    `niDMM Config
    Measurement <dmmviref.chm::/niDMM_Config_Measurement.html>`__ resets
    this property to the default value.
    '''
    cache = attributes.AttributeViBoolean(1050004)
    '''
    Specifies whether to cache the value of properties. When caching is
    enabled, the instrument driver keeps track of the current instrument
    settings and avoids sending redundant commands to the instrument. Thus,
    it significantly increases execution speed. The instrument driver can
    choose to always cache or to never cache particular properties
    regardless of the setting of this property. The default value is TRUE
    (1). Use `niDMM Initialize With
    Options <dmmviref.chm::/niDMM_Initialize_with_Options.html>`__ to
    override the default setting.
    '''
    channel_count = attributes.AttributeViInt32(1050203)
    '''
    Indicates the number of channels that the specific instrument driver
    supports. For each property for which the IVI_VAL_MULTI_CHANNEL flag
    property is set, the IVI engine maintains a separate cache value for
    each channel.
    '''
    config_product_number = attributes.AttributeViInt32(1150061)
    '''
    The PCI product ID.
    '''
    current_source = attributes.AttributeEnum(attributes.AttributeViReal64, enums.CurrentSource, 1150025)
    '''
    Specifies the current source provided during diode measurements.

    The NI 4050 and NI 4060 are not supported.
    '''
    dc_bias = attributes.AttributeEnum(attributes.AttributeViInt32, enums.DCBias, 1150053)
    '''
    For the NI 4082 and NI 4072 only, controls the available DC bias for
    capacitance measurements.
    '''
    dc_noise_rejection = attributes.AttributeEnum(attributes.AttributeViInt32, enums.DCNoiseRejection, 1150026)
    '''
    Specifies the DC noise rejection mode.

    Note: The NI 4050 and NI 4060 are not supported.
    '''
    driver_setup = attributes.AttributeViString(1050007)
    '''
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
    '''
    engine_major_version = attributes.AttributeViInt32(1050501)
    '''
    The major version number of the IVI engine.
    '''
    engine_minor_version = attributes.AttributeViInt32(1050502)
    '''
    The minor version number of the IVI engine.
    '''
    engine_revision = attributes.AttributeViString(1050553)
    '''
    A string that contains additional version information about the IVI
    engine.
    '''
    error_elaboration = attributes.AttributeViString(1050103)
    '''
    An optional string that contains additional information concerning the
    primary error condition.
    '''
    freq_voltage_auto_range_value = attributes.AttributeViReal64(1150044)
    '''
    For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the value of
    the frequency voltage range. If auto ranging is enabled, shows the
    actual value of the active frequency voltage range. If not Auto Ranging,
    the value is the same as that of the Frequency Voltage Range property.
    '''
    freq_voltage_range = attributes.AttributeViReal64(1250101)
    '''
    For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the maximum
    amplitude of the input signal for frequency measurements.

    +----------------+------+----------------------------------------------------------------------------------------------------------------------------------+
    | Auto Range On  | -1.0 | Configures the DMM to take an Auto Range measurement to calculate the voltage range before each frequency or period measurement. |
    +----------------+------+----------------------------------------------------------------------------------------------------------------------------------+
    | Auto Range Off | -2.0 | Disables Auto Ranging. NI-DMM sets the voltage range to the last calculated voltage range.                                       |
    +----------------+------+----------------------------------------------------------------------------------------------------------------------------------+
    '''
    function = attributes.AttributeEnum(attributes.AttributeViInt32, enums.Function, 1250001)
    '''
    Specifies the measurement function. If you are setting this property
    directly, you must also set the `Operation
    Mode <pniDMM_OperationMode.html>`__ property, which controls whether the
    DMM takes standard single or multipoint measurements, or acquires a
    waveform. If you are programming properties directly, you must set the
    Operation Mode property before setting other configuration properties.
    If the Operation Mode property is set to Waveform Mode, the only valid
    function types are Waveform Voltage and Waveform Current. Set the
    Operation Mode property to IVIDMM Mode to set all other function values.
    '''
    group_capabilities = attributes.AttributeViString(1050401)
    '''
    A string containing the capabilities and extension groups supported by
    the specific driver.
    '''
    idquery_response = attributes.AttributeViString(1150001)
    '''
    A string containing the type of instrument used in the current session.
    '''
    input_resistance = attributes.AttributeEnum(attributes.AttributeViReal64, enums.InputResistance, 1150029)
    '''
    Specifies the input resistance of the instrument.

    Note: The NI 4050 and NI 4060 are not supported.
    '''
    instrument_firmware_revision = attributes.AttributeViString(1050510)
    '''
    A string containing the instrument firmware revision number.
    '''
    instrument_manufacturer = attributes.AttributeViString(1050511)
    '''
    A string containing the manufacturer of the instrument.
    '''
    instrument_model = attributes.AttributeViString(1050512)
    '''
    A string containing the instrument model.
    '''
    interchange_check = attributes.AttributeViBoolean(1050021)
    '''
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
    '''
    io_resource_descriptor = attributes.AttributeViString(1050304)
    '''
    A string containing the resource descriptor of the instrument.
    '''
    latency = attributes.AttributeViInt32(1150034)
    '''
    Specifies the number of measurements transferred at a time from the
    instrument to an internal buffer. When set to Auto (-1), NI-DMM chooses
    the transfer size.
    '''
    lc_calculation_model = attributes.AttributeEnum(attributes.AttributeViInt32, enums.LCCalculationModel, 1150052)
    '''
    For the NI 4082 and NI 4072 only, specifies the type of algorithm that
    the measurement processing uses for capacitance and inductance
    measurements.
    '''
    lc_number_meas_to_average = attributes.AttributeViInt32(1150055)
    '''
    For the NI 4082 and NI 4072 only, specifies the number of LC
    measurements that are averaged to produce one reading.
    '''
    logical_name = attributes.AttributeViString(1050305)
    '''
    A string containing the logical name of the instrument.
    '''
    meas_complete_dest = attributes.AttributeEnum(attributes.AttributeViInt32, enums.MeasurementCompleteDest, 1250305)
    '''
    Specifies the destination of the measurement complete (MC) signal.

    To determine which values are supported by each device, refer to the
    `LabVIEW Trigger Routing <dmm.chm::/LVtrigger_routing.html>`__ section
    in the *NI Digital Multimeters Help*.

    Note: The NI 4050 is not supported.
    '''
    meas_dest_slope = attributes.AttributeEnum(attributes.AttributeViInt32, enums.MeasurementDestinationSlope, 1150002)
    '''
    Specifies the polarity of the generated measurement complete signal.
    '''
    number_of_averages = attributes.AttributeViInt32(1150032)
    '''
    Specifies the number of averages to perform in a measurement. For the NI
    4080/4081/4082 and NI 4070/4071/4072, applies only when the aperture
    time is not set to Auto and Auto Zero is ON. The Number of Averages
    Property will be ignored otherwise. The default is 4 for 7 1/2 digits;
    otherwise, the default is 1.

    The NI 4050 and NI 4060 are not supported.
    '''
    offset_comp_ohms = attributes.AttributeEnum(attributes.AttributeViInt32, enums.OffsetCompensatedOhms, 1150023)
    '''
    For the NI 4080/4081/4082 and NI 4070/4071/4072, enables or disables
    offset compensated ohms.
    '''
    open_cable_comp_conductance = attributes.AttributeViReal64(1150049)
    '''
    For the NI 4082 and NI 4072 only, specifies the active part
    (conductance) of the open cable compensation. The valid range is any
    real number >0. The default value (-1.0) indicates that compensation has
    not taken place.

    Note:
    Changing the function or the range using property nodes or through
    `niDMM Config
    Measurement <dmmviref.chm::/niDMM_Config_Measurement.html>`__ resets
    this property to the default value.
    '''
    open_cable_comp_susceptance = attributes.AttributeViReal64(1150048)
    '''
    For the NI 4082 and NI 4072 only, specifies the reactive part
    (susceptance) of the open cable compensation. The valid range is any
    real number >0. The default value (-1.0) indicates that compensation has
    not taken place.

    Note:
    Changing the function or the range using property nodes or through
    `niDMM Config
    Measurement <dmmviref.chm::/niDMM_Config_Measurement.html>`__ resets
    this property to the default value.
    '''
    operation_mode = attributes.AttributeEnum(attributes.AttributeViInt32, enums.OperationMode, 1150014)
    '''
    Specifies how the DMM acquires data.

    When you call `niDMM Config
    Measurement <dmmviref.chm::/niDMM_Config_Measurement.html>`__, NI-DMM
    sets this property to IVIDMM Mode. When you call `niDMM Configure
    Waveform
    Acquisition <dmmviref.chm::/niDMM_Configure_Waveform_Acquisition.html>`__,
    NI-DMM sets this property to Waveform Mode. If you are programming
    properties directly, you must set this property before setting other
    configuration properties.

    Note: The NI 4050 and NI 4060 are not supported.
    '''
    powerline_freq = attributes.AttributeEnum(attributes.AttributeViReal64, enums.PowerlineFrequency, 1250333)
    '''
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

    Note: For 400 Hz powerline frequency, use the 50 Hz setting.
    '''
    primary_error = attributes.AttributeViInt32(1050101)
    '''
    A code that describes the first error that occurred since the last call
    to niDMM Get Error for the session. The value follows the VXIplug&play
    conventions. A negative value describes an error condition. A positive
    value describes a warning condition. A zero indicates that no error or
    warning occurred. The error and warning values can be status codes
    defined by IVI, VISA, class drivers, or specific drivers.
    '''
    query_instrument_status = attributes.AttributeViBoolean(1050003)
    '''
    Specifies whether the instrument driver queries the instrument status
    after each operation. Querying the instrument status is very useful for
    debugging. After the user program is validated, this property can be set
    to FALSE (0) to disable status checking and maximize performance. The
    instrument driver can choose to ignore status checking for particular
    properties regardless of the setting of this property. The default value
    is TRUE (1). Use `niDMM Initialize With
    Options <dmmviref.chm::/niDMM_Initialize_with_Options.html>`__ to
    override the default setting.
    '''
    range = attributes.AttributeViReal64(1250002)
    '''
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

    Note:
    The NI 4050, NI 4060, and NI 4065 only support Auto Range when the
    trigger and sample trigger are set to Immediate.
    '''
    range_check = attributes.AttributeViBoolean(1050002)
    '''
    Specifies whether to validate property values and VI parameters. If
    enabled, the instrument driver validates the parameter values passed to
    driver VIs. Range checking parameters is very useful for debugging.
    After the user program is validated, you can set this property to FALSE
    (0) to disable range checking and maximize performance. The default
    value is TRUE (1). Use `niDMM Initialize With
    Options <dmmviref.chm::/niDMM_Initialize_With_Options.html>`__ to
    override the default setting.
    '''
    record_coercions = attributes.AttributeViBoolean(1050006)
    '''
    Specifies whether the IVI engine keeps a list of the value coercions it
    makes for ViInt32 and ViReal64 properties. The default value is FALSE
    (0). Use `niDMM Initialize With
    Options <dmmviref.chm::/niDMM_Initialize_with_Options.html>`__ to
    override the default setting. Use `niDMM Get Next Coercion
    Record <dmmviref.chm::/niDMM_Get_Next_Coercion_Record.html>`__ to
    extract and delete the oldest coercion record from the list.
    '''
    resolution_absolute = attributes.AttributeViReal64(1250008)
    '''
    Specifies the measurement resolution in absolute units. Setting this
    property to higher values increases the measurement accuracy. Setting
    this property to lower values increases the measurement speed.

    Note:
    NI-DMM ignores this property for capacitance and inductance measurements
    on the NI 4082 and NI 4072. To achieve better resolution for such
    measurements, use the Number of LC Measurements to Average property.
    '''
    resolution_digits = attributes.AttributeEnum(attributes.AttributeViReal64, enums.DigitsResolution, 1250003)
    '''
    Specifies the measurement resolution in digits. Setting this property to
    higher values increases the measurement accuracy. Setting this property
    to lower values increases the measurement speed.

    Note:
    NI-DMM ignores this property for capacitance and inductance measurements
    on the NI 4082 and NI 4072. To achieve better resolution for such
    measurements, use the `Number of LC Measurements to
    Average <pniDMM_NumberofLCMeasurementsToAverage.html>`__ property.
    '''
    sample_count = attributes.AttributeViInt32(1250301)
    '''
    Specifies the number of measurements the DMM takes each time it receives
    a trigger in a multiple point acquisition. Setting Sample Count to 0 on
    the NI 4050 and NI 4060 causes the device to take continuous
    measurements. Otherwise, setting Sample Count to 0 causes the
    conditional statement "Measurements equal to Sample Count" to always
    evaluate to False, and causes the DMM to continue taking measurements in
    the inner loop.
    '''
    sample_delay_mode = attributes.AttributeViInt32(1150031)
    '''
    For the NI 4060 only, specifies a delay interval after a sample trigger.

    +---+-------------------+---------------------------------------------------------------------------------------+
    | 0 | IVI compliant     | The Sample Interval property is only used when the Sample Trigger is set to Interval. |
    +---+-------------------+---------------------------------------------------------------------------------------+
    | 1 | Not IVI compliant | The Sample Interval property is used as a delay after any type of Sample Trigger.     |
    +---+-------------------+---------------------------------------------------------------------------------------+
    '''
    sample_interval = attributes.AttributeViReal64(1250303)
    '''
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

    Note: The NI 4080/4081/4082 and NI 4050 are not supported.
    '''
    sample_trigger = attributes.AttributeEnum(attributes.AttributeViInt32, enums.SampleTrigger, 1250302)
    '''
    Specifies the sample trigger source.

    To determine which values are supported by each device, refer to the
    `LabVIEW Trigger Routing <dmm.chm::/LVtrigger_routing.html>`__ section
    in the *NI Digital Multimeters Help*.
    '''
    sample_trigger_slope = attributes.AttributeEnum(attributes.AttributeViInt32, enums.SampleTrigSlope, 1150010)
    '''
    Specifies the edge of the signal from the specified sample trigger
    source on which the DMM is triggered.
    '''
    secondary_error = attributes.AttributeViInt32(1050102)
    '''
    An optional code that provides additional information concerning the
    primary error condition. The error and warning values can be status
    codes defined by IVI, VISA, class drivers, or specific drivers. Zero
    indicates no additional information.
    '''
    serial_number = attributes.AttributeViString(1150054)
    '''
    A string containing the serial number of the instrument. This property
    corresponds to the serial number label that is attached to most
    products.
    '''
    settle_time = attributes.AttributeViReal64(1150028)
    '''
    Specifies the settling time in seconds. Use this property to override
    the default settling time. To return to the default, set this property
    to Auto (-1).

    Note: The NI 4050 and NI 4060 are not supported.
    '''
    short_cable_comp_reactance = attributes.AttributeViReal64(1150046)
    '''
    For the NI 4082 and NI 4072 only, represents the reactive part
    (reactance) of the short cable compensation. The valid range is any real
    number >0. The default value (-1) indicates that compensation has not
    taken place.

    Note:
    Changing the VI or the range through this property or through `niDMM
    Config Measurement <dmmviref.chm::/niDMM_Config_Measurement.html>`__
    resets this property to the default value.
    '''
    short_cable_comp_resistance = attributes.AttributeViReal64(1150047)
    '''
    For the NI 4082 and NI 4072 only, represents the active part
    (resistance) of the short cable compensation. The valid range is any
    real number >0. The default value (-1) indicates that compensation has
    not taken place.

    Note:
    Changing the VI or the range through this property or through `niDMM
    Config Measurement <dmmviref.chm::/niDMM_Config_Measurement.html>`__
    resets this property to the default value.
    '''
    shunt_value = attributes.AttributeViReal64(1150003)
    '''
    For the NI 4050 only, specifies the shunt resistance value.

    Note:
    The NI 4050 requires an external shunt resistor for current
    measurements. This property should be set to the value of the shunt
    resistor.
    '''
    simulate = attributes.AttributeViBoolean(1050005)
    '''
    Specifies whether to simulate instrument driver I/O operations. If
    simulation is enabled, instrument driver functions perform range
    checking and call IVI Get and Set VIs, but they do not perform
    instrument I/O. For output parameters that represent instrument data,
    the instrument driver VIs return calculated values. The default value is
    FALSE (0). Use `niDMM Initialize With
    Options <dmmviref.chm::/niDMM_Initialize_with_Options.html>`__ to
    override the default setting.

    Note:
    Simulate can only be set within the `niDMM Initialize With
    Options <dmmviref.chm::/niDMM_Initialize_with_Options.html>`__ VI. The
    property value cannot be changed outside of the VI.
    '''
    specific_driver_class_spec_major_version = attributes.AttributeViInt32(1050515)
    '''
    The major version number of the class specification for the specific
    driver.
    '''
    specific_driver_class_spec_minor_version = attributes.AttributeViInt32(1050516)
    '''
    The minor version number of the class specification for the specific
    driver.
    '''
    specific_driver_description = attributes.AttributeViString(1050514)
    '''
    A string containing a description of the specific driver.
    '''
    specific_driver_major_version = attributes.AttributeViInt32(1050503)
    '''
    Returns the major version number of this instrument driver.
    '''
    specific_driver_minor_version = attributes.AttributeViInt32(1050504)
    '''
    Returns the minor version number of this instrument driver.
    '''
    specific_driver_prefix = attributes.AttributeViString(1050302)
    '''
    The prefix for the specific instrument driver. The name of each
    user-callable VI in this driver starts with this prefix. The prefix can
    be up to a maximum of eight characters.
    '''
    specific_driver_revision = attributes.AttributeViString(1050551)
    '''
    A string that contains additional version information about this
    instrument driver.
    '''
    specific_driver_vendor = attributes.AttributeViString(1050513)
    '''
    A string containing the vendor of the specific driver.
    '''
    supported_instrument_models = attributes.AttributeViString(1050327)
    '''
    A string containing the instrument models supported by the specific
    driver.
    '''
    temp_rtd_a = attributes.AttributeViReal64(1150121)
    '''
    Specifies the Callendar-Van Dusen A coefficient for RTD scaling when the
    **RTD Type property** is set to Custom.
    '''
    temp_rtd_b = attributes.AttributeViReal64(1150122)
    '''
    Specifies the Callendar-Van Dusen B coefficient for RTD scaling when the
    **RTD Type property** is set to Custom.
    '''
    temp_rtd_c = attributes.AttributeViReal64(1150123)
    '''
    Specifies the Callendar-Van Dusen C coefficient for RTD scaling when the
    **RTD Type property** is set to Custom.
    '''
    temp_rtd_res = attributes.AttributeViReal64(1250242)
    '''
    Specifies the RTD resistance at 0 degrees Celsius.
    '''
    temp_rtd_type = attributes.AttributeEnum(attributes.AttributeViInt32, enums.RTDType, 1150120)
    '''
    Specifies the RTD type.
    '''
    temp_tc_fixed_ref_junc = attributes.AttributeViReal64(1250233)
    '''
    Specifies the value of the fixed reference junction temperature for a
    thermocouple in degrees Celsius.
    '''
    temp_tc_ref_junc_type = attributes.AttributeEnum(attributes.AttributeViInt32, enums.ThermocoupleReferenceJunctionType, 1250232)
    '''
    Specifies the thermocouple reference junction type.
    '''
    temp_tc_type = attributes.AttributeEnum(attributes.AttributeViInt32, enums.ThermocoupleType, 1250231)
    '''
    Specifies the thermocouple type.
    '''
    temp_thermistor_a = attributes.AttributeViReal64(1150125)
    '''
    Specifies the Steinhart-Hart A coefficient for thermistor scaling when
    the **Thermistor Type property** is set to Custom.
    '''
    temp_thermistor_b = attributes.AttributeViReal64(1150126)
    '''
    Specifies the Steinhart-Hart B coefficient for thermistor scaling when
    the **Thermistor Type property** is set to Custom.
    '''
    temp_thermistor_c = attributes.AttributeViReal64(1150127)
    '''
    Specifies the Steinhart-Hart C coefficient for thermistor scaling when
    the **Thermistor Type property** is set to Custom.
    '''
    temp_thermistor_type = attributes.AttributeEnum(attributes.AttributeViInt32, enums.ThermistorType, 1150124)
    '''
    Specifies the thermistor type.
    '''
    temp_transducer_type = attributes.AttributeEnum(attributes.AttributeViInt32, enums.TransducerType, 1250201)
    '''
    Specifies the transducer type.
    '''
    trigger_count = attributes.AttributeViInt32(1250304)
    '''
    Specifies the number of triggers the DMM receives before returning to
    the Idle state. This property can be set to any positive ViInt32 value
    for the NI 4065, NI 4070/4071/4072, and NI 4080/4081/4082.

    The NI 4050/4060 only support this property being set to 1.

    Refer to `Multiple Point Acquisitions <dmm.chm::/multi_point.html>`__ in
    the *NI Digital Multimeters Help* for more information.
    '''
    trigger_delay = attributes.AttributeViReal64(1250005)
    '''
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
    '''
    trigger_slope = attributes.AttributeEnum(attributes.AttributeViInt32, enums.TriggerSlope, 1250334)
    '''
    Specifies the edge of the signal from the specified trigger source on
    which the DMM is triggered.
    '''
    trigger_source = attributes.AttributeEnum(attributes.AttributeViInt32, enums.TriggerSource, 1250004)
    '''
    Specifies the trigger source. When `niDMM
    Initiate <dmmviref.chm::/niDMM_Initiate.html>`__ is called, the DMM
    waits for the trigger specified with this property. After it receives
    the trigger, the DMM waits the length of time specified with the
    `Trigger Delay <pnidmm_TriggerDelay.html>`__ property. The DMM then
    takes a measurement.

    To determine which values are supported by each device, refer to the
    `LabVIEW Trigger Routing <dmm.chm::/LVtrigger_routing.html>`__ section
    in the *NI Digital Multimeters Help*.
    '''
    waveform_coupling = attributes.AttributeEnum(attributes.AttributeViInt32, enums.WaveformCoupling, 1150027)
    '''
    For the NI 4080/4081/4082 and NI 4070/4071/4072 only, specifies the
    coupling during a waveform acquisition.
    '''
    waveform_points = attributes.AttributeViInt32(1150019)
    '''
    For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the number of
    points to acquire in a waveform acquisition.
    '''
    waveform_rate = attributes.AttributeViReal64(1150018)
    '''
    Specifies the rate of the waveform acquisition in samples per second
    (S/s). The valid rate is calculated by dividing 1,800,000 by an integer
    divisor, and the rate falls between 10 and 1,800,000 samples per second.
    The waveform rate is coerced upwards to the next valid rate. The default
    value is 1,800,000 samples per second. Not supported by NI 4065.
    '''

    def __init__(self, repeated_capability):
        # TODO(marcoskirsch): rename to _library.
        self.library = library_singleton.get()
        self._repeated_capability = repeated_capability

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
            Use _get_error_message instead. It doesn't require a session.
            '''
            error_string = self._get_error_message(error_code)
            return error_string
        except errors.Error:
            return "Failed to retrieve error description."

    ''' These are code-generated '''

    def _abort(self):
        '''_abort

        Aborts a previously initiated measurement and returns the DMM to the
        Idle state.
        '''
        error_code = self.library.niDMM_Abort(self.vi)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def clear_interchange_warnings(self):
        '''clear_interchange_warnings

        Clears the list of current interchange warnings.
        '''
        error_code = self.library.niDMM_ClearInterchangeWarnings(self.vi)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_ac_bandwidth(self, ac_minimum_frequency_hz, ac_maximum_frequency_hz):
        '''configure_ac_bandwidth

        Configures the AC_MIN_FREQ and AC_MAX_FREQ
        attributes, which the DMM uses for AC measurements.

        Args:
            ac_minimum_frequency_hz (float):Specifies the minimum expected frequency component of the input signal
                in hertz. This parameter affects the DMM only when you set the
                function attribute to AC measurements. NI-DMM uses this
                parameter to calculate the proper aperture for the measurement.
                The driver sets the AC_MIN_FREQ attribute to this value.
                The valid range is 1 Hz–300 kHz for the NI 4080/4081/4082 and the NI
                4070/4071/4072, 10 Hz–100 Hz for the NI 4065, and 20 Hz–25 kHz for the
                NI 4050 and NI 4060.
            ac_maximum_frequency_hz (float):Specifies the maximum expected frequency component of the input signal
                in hertz within the device limits. This parameter is used only for error
                checking and verifies that the value of this parameter is less than the
                maximum frequency of the device.

                This parameter affects the DMM only when you set the
                function attribute to AC measurements. The driver sets the
                AC_MAX_FREQ attribute to this value. The valid range is 1
                Hz–300 kHz for the NI 4080/4081/4082 and the NI 4070/4071/4072, 10
                Hz–100 Hz for the NI 4065, and 20 Hz–25 kHz for the NI 4050 and NI 4060.
        '''
        error_code = self.library.niDMM_ConfigureACBandwidth(self.vi, ac_minimum_frequency_hz, ac_maximum_frequency_hz)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_adc_calibration(self, adc_calibration):
        '''configure_adc_calibration

        For the NI 4080/4081/4082 and NI 4070/4071/4072, allows the DMM to
        compensate for gain drift since the last external calibration or
        self-calibration. When **ADC_Calibration** is ON, the DMM measures an
        internal reference to calculate the correct gain for the measurement.
        When **ADC_Calibration** is OFF, the DMM does not compensate for
        changes to the gain.

        Args:
            adc_calibration (enums.ADCCalibration):Specifies the **ADC_Calibration** setting. The driver sets
                ADC_CALIBRATION to this value.
                NIDMM_VAL_ADC_CALIBRATION_ON enables **ADC_Calibration**.
                NIDMM_VAL_ADC_CALIBRATION_OFF disables **ADC_Calibration**. If you
                set the value to NIDMM_VAL_ADC_CALIBRATION_AUTO, the driver
                determines whether to enable **ADC_Calibration** based on the
                measurement function and resolution that you configure. If you configure
                the NI 4080/4081/4082 or NI 4070/4071/4072 for a 6½–digit and greater
                resolution DC measurement, the driver enables ADC Calibration. For all
                other measurement configurations, the driver disables
                **ADC_Calibration**.

                +------------------------------------------+-------+--------------------------------------------------------------------------------------------------+
                | Name                                     | Value | Description                                                                                      |
                +==========================================+=======+==================================================================================================+
                | NIDMM_VAL_ADC_CALIBRATION_AUTO (default) | -1.0  | The DMM enables or disables **ADC_Calibration** based on the configured function and resolution. |
                +------------------------------------------+-------+--------------------------------------------------------------------------------------------------+
                | NIDMM_VAL_ADC_CALIBRATION_OFF            | 0     | The DMM does not compensate for changes to the gain.                                             |
                +------------------------------------------+-------+--------------------------------------------------------------------------------------------------+
                | NIDMM_VAL_ADC_CALIBRATION_ON             | 1     | The DMM measures an internal reference to calculate the correct gain for the measurement.        |
                +------------------------------------------+-------+--------------------------------------------------------------------------------------------------+
        '''
        if type(adc_calibration) is not enums.ADCCalibration:
            raise TypeError('Parameter mode must be of type ' + str(enums.ADCCalibration))
        error_code = self.library.niDMM_ConfigureADCCalibration(self.vi, adc_calibration.value)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_auto_zero_mode(self, auto_zero_mode):
        '''configure_auto_zero_mode

        Configures the DMM for **Auto_Zero_Mode**. When **Auto_Zero_Mode**
        is ON, the DMM internally disconnects the input signal and takes a zero
        reading. It then subtracts the zero reading from the measurement. This
        prevents offset voltages present on the input circuitry of the DMM from
        affecting measurement accuracy. When **Auto_Zero_Mode** is OFF, the
        DMM does not compensate for zero reading offset.

        Args:
            auto_zero_mode (enums.AutoZero):Specifies the **auto_zero_mode**. NI-DMM sets the
                AUTO_ZERO attribute to this value.

                ON enables **auto_zero_mode** for each measurement. ONCE enables
                **auto_zero_mode** before the next measurement. The
                **auto_zero_mode** value is stored and used in subsequent measurements
                until the device is reconfigured.

                OFF disables **auto_zero_mode**. If you set this parameter to AUTO,
                NI-DMM determines whether to enable Auto Zero based on the measurement
                function that you configure. If you configure the NI 4080/4081/4082 or
                the NI 4070/4071/4072 for a 6½–digit and greater resolution DC
                measurement, NI-DMM sets **auto_zero_mode** to ON.

                For all other DC measurement configurations on the NI 4080/4081/4082 or
                the NI 4070/4071/4072, NI-DMM sets **auto_zero_mode** to ONCE. For all
                AC measurements or waveform acquisitions on the NI 4080/4081/4082 or the
                NI 4070/4071/4072, NI-DMM sets **auto_zero_mode** to OFF. For NI 4060,
                **auto_zero_mode** is set to OFF when AUTO is selected.

                For NI 4065 devices, **auto_zero_mode** is always ON.
                **auto_zero_mode** is an integral part of the signal measurement phase
                and adds no extra time to the overall measurement.

                +------------------------------------+----+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIDMM_VAL_AUTO_ZERO_AUTO (default) | -1 | NI-DMM chooses the Auto Zero setting based on the configured function and resolution.                                                                                                                      |
                +------------------------------------+----+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIDMM_VAL_AUTO_ZERO_OFF            | 0  | Disables Auto Zero.                                                                                                                                                                                        |
                +------------------------------------+----+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIDMM_VAL_AUTO_ZERO_ON             | 1  | The DMM internally disconnects the input signal following each measurement and takes a zero reading. It then subtracts the zero reading from the preceding reading.                                        |
                +------------------------------------+----+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIDMM_VAL_AUTO_ZERO_ONCE           | 2  | The DMM internally disconnects the input signal following the first measurement and takes a zero reading. It then subtracts the zero reading from the preceding reading and each measurement that follows. |
                +------------------------------------+----+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

                Note: The NI 4060/4065 does *not* support this setting.
        '''
        if type(auto_zero_mode) is not enums.AutoZero:
            raise TypeError('Parameter mode must be of type ' + str(enums.AutoZero))
        error_code = self.library.niDMM_ConfigureAutoZeroMode(self.vi, auto_zero_mode.value)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_cable_comp_type(self, cable_comp_type):
        '''configure_cable_comp_type

        For the NI 4082 and NI 4072 only, sets the
        CABLE_COMP_TYPE attribute for the current
        capacitance/inductance mode range.

        Args:
            cable_comp_type (enums.CableCompensationType):Specifies the type of cable compensation that is used for the current
                range.
        '''
        if type(cable_comp_type) is not enums.CableCompensationType:
            raise TypeError('Parameter mode must be of type ' + str(enums.CableCompensationType))
        error_code = self.library.niDMM_ConfigureCableCompType(self.vi, cable_comp_type.value)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_current_source(self, current_source):
        '''configure_current_source

        The NI 4050 and NI 4060 are not supported. Configures the
        **Current_Source** for diode measurements.

        Args:
            current_source (enums.CurrentSource):Specifies the **current_source** provided during diode measurements.
                For valid ranges, refer to the device sections for your device. The
                driver sets CURRENT_SOURCE to this value.

                +--------------------------------+--------+---------------------------------------------------+
                | NIDMM_VAL_1_MICROAMP           | 1 µA   | NI 4080/4081/4082 and NI 4070/4071/4072           |
                +--------------------------------+--------+---------------------------------------------------+
                | NIDMM_VAL_10_MICROAMP          | 10 µA  | NI 4080/4081/4082 and NI 4070/4071/4072 only      |
                +--------------------------------+--------+---------------------------------------------------+
                | NIDMM_VAL_100_MICROAMP         | 100 µA | NI 4080/4081/4082, NI 4070/4071/4072, and NI 4065 |
                +--------------------------------+--------+---------------------------------------------------+
                | NIDMM_VAL_1_MILLIAMP (default) | 1 mA   | NI 4080/4081/4082, NI 4070/4071/4072, and NI 4065 |
                +--------------------------------+--------+---------------------------------------------------+
        '''
        if type(current_source) is not enums.CurrentSource:
            raise TypeError('Parameter mode must be of type ' + str(enums.CurrentSource))
        error_code = self.library.niDMM_ConfigureCurrentSource(self.vi, current_source.value)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_fixed_ref_junction(self, fixed_reference_junction):
        '''configure_fixed_ref_junction

        Configures the fixed reference junction temperature for a thermocouple
        with a fixed reference junction type.

        Args:
            fixed_reference_junction (float):Specifies the reference junction temperature when a fixed reference
                junction is used to take a thermocouple measurement. The units are
                degrees Celsius. NI-DMM uses this value to set the Fixed Reference
                Junction property. The default is 25.00 (°C).
        '''
        error_code = self.library.niDMM_ConfigureFixedRefJunction(self.vi, fixed_reference_junction)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_frequency_voltage_range(self, voltage_range):
        '''configure_frequency_voltage_range

        For the NI 4080/4081/4082 and the NI 4070/4071/4072 only, specifies the
        expected maximum amplitude of the input signal for frequency and period
        measurements.

        Args:
            voltage_range (float):Sets the expected maximum amplitude of the input signal. Refer to the
                `NI 4080 <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/4080_functional_overview/>`__,
                `NI 4081 <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/4081_functional_overview/>`__,
                `NI 4072 <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/4082/>`__,
                `NI 4070 <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/4070_functional_overview/>`__,
                `NI 4071 <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/4071_functional_overview/>`__,
                and
                `NI 4072 <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/4072/>`__
                sections for a list of valid values. NI-DMM sets
                FREQ_VOLTAGE_RANGE to this value. The minimum
                peak-to-peak signal amplitude that can be detected is 10% of the
                specified **voltage_range**.

                +-----------------------------------+-------+----------------------------------------------------------------------------------------------------------------------------------+
                | Name                              | Value | Description                                                                                                                      |
                +===================================+=======+==================================================================================================================================+
                | NIDMM_VAL_AUTO_RANGE_ON (default) | -1.0  | Configures the DMM to take an Auto Range measurement to calculate the voltage range before each frequency or period measurement. |
                +-----------------------------------+-------+----------------------------------------------------------------------------------------------------------------------------------+
                | NIDMM_VAL_AUTO_RANGE_OFF          | -2.0  | Disables Auto Ranging. The driver sets the voltage range to the last calculated voltage range.                                   |
                +-----------------------------------+-------+----------------------------------------------------------------------------------------------------------------------------------+
        '''
        error_code = self.library.niDMM_ConfigureFrequencyVoltageRange(self.vi, voltage_range)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_meas_complete_dest(self, meas_complete_destination):
        '''configure_meas_complete_dest

        Specifies the destination of the DMM Measurement Complete (MC) signal.
        Refer to
        `Triggering <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/trigger/>`__
        for more information.

        Args:
            meas_complete_destination (enums.MeasurementCompleteDest):Specifies the destination of the Measurement Complete signal. This
                signal is issued when the DMM completes a single measurement. The driver
                sets the MEAS_COMPLETE_DEST attribute to this value. This
                signal is commonly referred to as Voltmeter Complete.

                Note:
                To determine which values are supported by each device, refer to the
                `LabWindows/CVI Trigger
                Routing <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/cvitrigger_routing/>`__
                section.
        '''
        if type(meas_complete_destination) is not enums.MeasurementCompleteDest:
            raise TypeError('Parameter mode must be of type ' + str(enums.MeasurementCompleteDest))
        error_code = self.library.niDMM_ConfigureMeasCompleteDest(self.vi, meas_complete_destination.value)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_meas_complete_slope(self, meas_complete_slope):
        '''configure_meas_complete_slope

        Sets the Measurement Complete signal to either rising edge (positive) or
        falling edge (negative) polarity.

        Args:
            meas_complete_slope (enums.Slope):Specifies the polarity of the signal that is generated. The driver sets
                MEAS_DEST_SLOPE to this value.

                +------------------------+---+--------------------+----------------------------------------------------------------+
                | Rising Edge            | 0 | NIDMM_VAL_POSITIVE | The driver triggers on the rising edge of the trigger signal.  |
                +------------------------+---+--------------------+----------------------------------------------------------------+
                | Falling Edge (default) | 1 | NIDMM_VAL_NEGATIVE | The driver triggers on the falling edge of the trigger signal. |
                +------------------------+---+--------------------+----------------------------------------------------------------+
        '''
        if type(meas_complete_slope) is not enums.Slope:
            raise TypeError('Parameter mode must be of type ' + str(enums.Slope))
        error_code = self.library.niDMM_ConfigureMeasCompleteSlope(self.vi, meas_complete_slope.value)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_measurement_absolute(self, measurement_function, range, resolution_absolute):
        '''configure_measurement_absolute

        Configures the common attributes of the measurement. These attributes
        include function, range, and
        RESOLUTION_ABSOLUTE.

        Args:
            measurement_function (enums.Function):Specifies the **measurement_function** used to acquire the measurement.
                The driver sets function to this value.
            range (float):Specifies the **range** for the function specified in the
                **Measurement_Function** parameter. When frequency is specified in the
                **Measurement_Function** parameter, you must supply the minimum
                frequency expected in the **range** parameter. For example, you must
                type in 100 Hz if you are measuring 101 Hz or higher.
                For all other functions, you must supply a **range** that exceeds the
                value that you are measuring. For example, you must type in 10 V if you
                are measuring 9 V. **range** values are coerced up to the closest input
                **range**. Refer to the `Devices
                Overview <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/devices/>`__
                for a list of valid ranges. The driver sets range to this
                value. The default is 0.02 V.

                +---------------------------+------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIDMM_VAL_AUTO_RANGE_ON   | -1.0 | NI-DMM performs an Auto Range before acquiring the measurement.                                                                                                                         |
                +---------------------------+------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIDMM_VAL_AUTO_RANGE_OFF  | -2.0 | NI-DMM sets the Range to the current AUTO_RANGE_VALUE and uses this range for all subsequent measurements until the measurement configuration is changed.                               |
                +---------------------------+------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIDMM_VAL_AUTO_RANGE_ONCE | -3.0 | NI-DMM performs an Auto Range before acquiring the measurement. The AUTO_RANGE_VALUE is stored and used for all subsequent measurements until the measurement configuration is changed. |
                +---------------------------+------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

                Note:
                The NI 4050, NI 4060, and NI 4065 only support Auto Range when the
                trigger and sample trigger are set to IMMEDIATE.
            resolution_absolute (float):Specifies the absolute resolution for the measurement. NI-DMM sets
                RESOLUTION_ABSOLUTE to this value. This parameter is
                ignored when the **Range** parameter is set to
                NIDMM_VAL_AUTO_RANGE_ON (-1.0) or NIDMM_VAL_AUTO_RANGE_ONCE
                (-3.0). The default is 0.001 V.

                Note:
                NI-DMM ignores this parameter for capacitance and inductance
                measurements on the NI 4072. To achieve better resolution for such
                measurements, use the LC_NUMBER_MEAS_TO_AVERAGE
                attribute.
        '''
        if type(measurement_function) is not enums.Function:
            raise TypeError('Parameter mode must be of type ' + str(enums.Function))
        error_code = self.library.niDMM_ConfigureMeasurementAbsolute(self.vi, measurement_function.value, range, resolution_absolute)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_measurement_digits(self, measurement_function, range, resolution_digits):
        '''configure_measurement_digits

        Configures the common attributes of the measurement. These attributes
        include function, range, and
        RESOLUTION_DIGITS.

        Args:
            measurement_function (enums.Function):Specifies the **measurement_function** used to acquire the measurement.
                The driver sets function to this value.
            range (float):Specifies the range for the function specified in the
                **Measurement_Function** parameter. When frequency is specified in the
                **Measurement_Function** parameter, you must supply the minimum
                frequency expected in the **range** parameter. For example, you must
                type in 100 Hz if you are measuring 101 Hz or higher.
                For all other functions, you must supply a range that exceeds the value
                that you are measuring. For example, you must type in 10 V if you are
                measuring 9 V. range values are coerced up to the closest input range.
                Refer to the `Devices
                Overview <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/devices/>`__
                for a list of valid ranges. The driver sets range to this
                value. The default is 0.02 V.

                +---------------------------+------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIDMM_VAL_AUTO_RANGE_ON   | -1.0 | NI-DMM performs an Auto Range before acquiring the measurement.                                                                                                                         |
                +---------------------------+------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIDMM_VAL_AUTO_RANGE_OFF  | -2.0 | NI-DMM sets the Range to the current AUTO_RANGE_VALUE and uses this range for all subsequent measurements until the measurement configuration is changed.                               |
                +---------------------------+------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIDMM_VAL_AUTO_RANGE_ONCE | -3.0 | NI-DMM performs an Auto Range before acquiring the measurement. The AUTO_RANGE_VALUE is stored and used for all subsequent measurements until the measurement configuration is changed. |
                +---------------------------+------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

                Note:
                The NI 4050, NI 4060, and NI 4065 only support Auto Range when the
                trigger and sample trigger are set to IMMEDIATE.
            resolution_digits (float):Specifies the resolution of the measurement in digits. The driver sets
                the `Devices
                Overview <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/devices/>`__
                for a list of valid ranges. The driver sets
                RESOLUTION_DIGITS attribute to this value. This parameter
                is ignored when the **Range** parameter is set to
                NIDMM_VAL_AUTO_RANGE_ON (-1.0) or NIDMM_VAL_AUTO_RANGE_ONCE
                (-3.0). The default is 5½.

                Note:
                NI-DMM ignores this parameter for capacitance and inductance
                measurements on the NI 4072. To achieve better resolution for such
                measurements, use the LC_NUMBER_MEAS_TO_AVERAGE
                attribute.
        '''
        if type(measurement_function) is not enums.Function:
            raise TypeError('Parameter mode must be of type ' + str(enums.Function))
        error_code = self.library.niDMM_ConfigureMeasurementDigits(self.vi, measurement_function.value, range, resolution_digits)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_multi_point(self, trigger_count, sample_count, sample_trigger, sample_interval):
        '''configure_multi_point

        Configures the attributes for multipoint measurements. These attributes
        include TRIGGER_COUNT, SAMPLE_COUNT,
        SAMPLE_TRIGGER, and SAMPLE_INTERVAL.

        For continuous acquisitions, set TRIGGER_COUNT or
        SAMPLE_COUNT to zero. For more information, refer to
        `Multiple Point
        Acquisitions <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/multi_point/>`__,
        `Triggering <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/trigger/>`__,
        and `Using
        Switches <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/switch_selection/>`__.

        Args:
            trigger_count (int):Sets the number of triggers you want the DMM to receive before returning
                to the Idle state. The driver sets TRIGGER_COUNT to this
                value. The default value is 1.
            sample_count (int):Sets the number of measurements the DMM makes in each measurement
                sequence initiated by a trigger. The driver sets
                SAMPLE_COUNT to this value. The default value is 1.
            sample_trigger (enums.SampleTrigger):Specifies the **sample_trigger** source you want to use. The driver
                sets SAMPLE_TRIGGER to this value. The default is
                Immediate.

                Note:
                To determine which values are supported by each device, refer to the
                `LabWindows/CVI Trigger
                Routing <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/cvitrigger_routing/>`__
                section.
            sample_interval (float):Sets the amount of time in seconds the DMM waits between measurement
                cycles. The driver sets SAMPLE_INTERVAL to this value.
                Specify a sample interval to add settling time between measurement
                cycles or to decrease the measurement rate. **sample_interval** only
                applies when the **Sample_Trigger** is set to INTERVAL.

                On the NI 4060, the **sample_interval** value is used as the settling
                time. When sample interval is set to 0, the DMM does not settle between
                measurement cycles. The NI 4065 and NI 4070/4071/4072 use the value
                specified in **sample_interval** as additional delay. The default value
                (-1) ensures that the DMM settles for a recommended time. This is the
                same as using an Immediate trigger.

                Note: This attribute is not used on the NI 4080/4081/4082 and the NI 4050.
        '''
        if type(sample_trigger) is not enums.SampleTrigger:
            raise TypeError('Parameter mode must be of type ' + str(enums.SampleTrigger))
        error_code = self.library.niDMM_ConfigureMultiPoint(self.vi, trigger_count, sample_count, sample_trigger.value, sample_interval)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_offset_comp_ohms(self, offset_comp_ohms):
        '''configure_offset_comp_ohms

        For NI 4080/4081/4082 and NI 4070/4071/4072, allows the DMM to
        compensate for voltage offsets in resistance measurements. When
        **Offset_Comp_Ohms** is enabled, the DMM measures the resistance twice
        (once with the current source on and again with it turned off). Any
        voltage offset present in both measurements is cancelled out.
        **Offset_Comp_Ohms** is useful when measuring resistance values less
        than 10 KΩ.

        Args:
            offset_comp_ohms (enums.OffsetCompensatedOhms):Enables or disables **offset_comp_ohms**. The driver sets
                OFFSET_COMP_OHMS to this value.

                +------------------------------------------+-------+------------------------------------+
                | Name                                     | Value | Description                        |
                +==========================================+=======+====================================+
                | NIDMM_VAL_OFFSET_COMP_OHMS_OFF (default) | 0     | Off disables **Offset_Comp_Ohms**. |
                +------------------------------------------+-------+------------------------------------+
                | NIDMM_VAL_OFFSET_COMP_OHMS_ON            | 1     | On enables **Offset_Comp_Ohms**.   |
                +------------------------------------------+-------+------------------------------------+
        '''
        if type(offset_comp_ohms) is not enums.OffsetCompensatedOhms:
            raise TypeError('Parameter mode must be of type ' + str(enums.OffsetCompensatedOhms))
        error_code = self.library.niDMM_ConfigureOffsetCompOhms(self.vi, offset_comp_ohms.value)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_open_cable_comp_values(self, conductance, susceptance):
        '''configure_open_cable_comp_values

        For the NI 4082 and NI 4072 only, configures the
        OPEN_CABLE_COMP_CONDUCTANCE and
        OPEN_CABLE_COMP_SUSCEPTANCE attributes.

        Args:
            conductance (float):Specifies the open cable compensation **conductance**.
            susceptance (float):Specifies the open cable compensation **susceptance**.
        '''
        error_code = self.library.niDMM_ConfigureOpenCableCompValues(self.vi, conductance, susceptance)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_power_line_frequency(self, power_line_frequency_hz):
        '''configure_power_line_frequency

        Specifies the powerline frequency.

        Args:
            power_line_frequency_hz (float):**Powerline Frequency** specifies the powerline frequency in hertz.
                NI-DMM sets the Powerline Frequency property to this value.
        '''
        error_code = self.library.niDMM_ConfigurePowerLineFrequency(self.vi, power_line_frequency_hz)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_rtd_custom(self, rtd_a, rtd_b, rtd_c):
        '''configure_rtd_custom

        Configures the A, B, and C parameters for a custom RTD.

        Args:
            rtd_a (float):Specifies the Callendar-Van Dusen A coefficient for RTD scaling when RTD
                Type parameter is set to Custom in the configure_rtd_type function.
                The default is 3.9083e-3 (Pt3851)
            rtd_b (float):Specifies the Callendar-Van Dusen B coefficient for RTD scaling when RTD
                Type parameter is set to Custom in the configure_rtd_type function.
                The default is -5.775e-7 (Pt3851).
            rtd_c (float):Specifies the Callendar-Van Dusen C coefficient for RTD scaling when RTD
                Type parameter is set to Custom in the configure_rtd_type function.
                The default is -4.183e-12 (Pt3851).
        '''
        error_code = self.library.niDMM_ConfigureRTDCustom(self.vi, rtd_a, rtd_b, rtd_c)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_rtd_type(self, rtd_type, rtd_resistance):
        '''configure_rtd_type

        Configures the RTD Type and RTD Resistance parameters for an RTD.

        Args:
            rtd_type (int):Specifies the type of RTD used to measure the temperature resistance.
                NI-DMM uses this value to set the RTD Type property. The default is
                NIDMM_VAL_TEMP_RTD_PT3851.

                +---------------------------------+
                | Enum                            |
                +=================================+
                | Callendar-Van Dusen Coefficient |
                +---------------------------------+
                | NIDMM_VAL_TEMP_RTD_PT3851       |
                +---------------------------------+
                | NIDMM_VAL_TEMP_RTD_PT3750       |
                +---------------------------------+
                | NIDMM_VAL_TEMP_RTD_PT3916       |
                +---------------------------------+
                | NIDMM_VAL_TEMP_RTD_PT3920       |
                +---------------------------------+
                | NIDMM_VAL_TEMP_RTD_PT3911       |
                +---------------------------------+
                | NIDMM_VAL_TEMP_RTD_PT3928       |
                +---------------------------------+
                | \*No standard. Check the TCR.   |
                +---------------------------------+
            rtd_resistance (float):Specifies the RTD resistance in ohms at 0 °C. NI-DMM uses this value to
                set the RTD Resistance property. The default is 100 (Ω).
        '''
        error_code = self.library.niDMM_ConfigureRTDType(self.vi, rtd_type, rtd_resistance)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_sample_trigger_slope(self, sample_trigger_slope):
        '''configure_sample_trigger_slope

        Sets the SAMPLE_TRIGGER_SLOPE to either rising edge
        (positive) or falling edge (negative) polarity.

        Args:
            sample_trigger_slope (enums.Slope):Specifies the polarity of the Trigger signal on which the measurement is
                triggered for values of either NIDMM_VAL_POSITIVE or
                NIDMM_VAL_NEGATIVE. The driver sets
                SAMPLE_TRIGGER_SLOPE to this value.

                +------------------------+---+--------------------+----------------------------------------------------------------+
                | Rising Edge            | 0 | NIDMM_VAL_POSITIVE | The driver triggers on the rising edge of the trigger signal.  |
                +------------------------+---+--------------------+----------------------------------------------------------------+
                | Falling Edge (default) | 1 | NIDMM_VAL_NEGATIVE | The driver triggers on the falling edge of the trigger signal. |
                +------------------------+---+--------------------+----------------------------------------------------------------+
        '''
        if type(sample_trigger_slope) is not enums.Slope:
            raise TypeError('Parameter mode must be of type ' + str(enums.Slope))
        error_code = self.library.niDMM_ConfigureSampleTriggerSlope(self.vi, sample_trigger_slope.value)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_short_cable_comp_values(self, resistance, reactance):
        '''configure_short_cable_comp_values

        For the NI 4082 and NI 4072 only, configures the
        SHORT_CABLE_COMP_RESISTANCE and
        SHORT_CABLE_COMP_REACTANCE attributes.

        Args:
            resistance (float):Specifies the short cable compensation **resistance**.
            reactance (float):Specifies the short cable compensation **reactance**.
        '''
        error_code = self.library.niDMM_ConfigureShortCableCompValues(self.vi, resistance, reactance)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_thermistor_custom(self, thermistor_a, thermistor_b, thermistor_c):
        '''configure_thermistor_custom

        Configures the A, B, and C parameters for a custom thermistor.

        Args:
            thermistor_a (float):Specifies the Steinhart-Hart A coefficient for thermistor scaling when
                Thermistor Type is set to Custom in the configure_thermistor_type
                function. The default is 1.0295e-3 (44006).
            thermistor_b (float):Specifies the Steinhart-Hart B coefficient for thermistor scaling when
                Thermistor Type is set to Custom in the configure_thermistor_type
                function. The default is 2.391e-4 (44006).
            thermistor_c (float):Specifies the Steinhart-Hart C coefficient for thermistor scaling when
                Thermistor Type is set to Custom in the configure_thermistor_type
                function. The default is 1.568e-7 (44006).
        '''
        error_code = self.library.niDMM_ConfigureThermistorCustom(self.vi, thermistor_a, thermistor_b, thermistor_c)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_thermistor_type(self, thermistor_type):
        '''configure_thermistor_type

        Configures the thermistor type.

        Args:
            thermistor_type (enums.TemperatureThermistorType):Specifies the type of thermistor used to measure the temperature. NI-DMM
                uses this value to set the Thermistor Type property. The default is
                NIDMM_VAL_TEMP_THERMISTOR_44006.

                +--------------------+--------------------+--------------------+--------------------+
                | **Defined Values** | **Thermistor       | **Value**          | **25 °C            |
                |                    | Type**             |                    | Resistance**       |
                +--------------------+--------------------+--------------------+--------------------+
                | NIDMM_VAL_TEMP_ | Custom             | 0                  | —                  |
                | THERMISTOR_CUSTOM |                    |                    |                    |
                +--------------------+--------------------+--------------------+--------------------+
                | NIDMM_VAL_TEMP_ | 44004              | 1                  | 2.25 kΩ            |
                | THERMISTOR_44004  |                    |                    |                    |
                +--------------------+--------------------+--------------------+--------------------+
                | NIDMM_VAL_TEMP_ | 44006              | 2                  | 10 kΩ              |
                | THERMISTOR_44006  |                    |                    |                    |
                +--------------------+--------------------+--------------------+--------------------+
                | NIDMM_VAL_TEMP_ | 44007              | 3                  | 5 kΩ               |
                | THERMISTOR_44007  |                    |                    |                    |
                +--------------------+--------------------+--------------------+--------------------+
        '''
        if type(thermistor_type) is not enums.TemperatureThermistorType:
            raise TypeError('Parameter mode must be of type ' + str(enums.TemperatureThermistorType))
        error_code = self.library.niDMM_ConfigureThermistorType(self.vi, thermistor_type.value)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_thermocouple(self, thermocouple_type, reference_junction_type):
        '''configure_thermocouple

        Configures the thermocouple type and reference junction type for a
        chosen thermocouple.

        Args:
            thermocouple_type (enums.ThermocoupleType):Specifies the type of thermocouple used to measure the temperature.
                NI-DMM uses this value to set the Thermocouple Type property. The
                default is NIDMM_VAL_TEMP_TC_J.

                +---------------------+---------------------+
                | NIDMM_VAL_TEMP_TC_B | Thermocouple type B |
                +---------------------+---------------------+
                | NIDMM_VAL_TEMP_TC_E | Thermocouple type E |
                +---------------------+---------------------+
                | NIDMM_VAL_TEMP_TC_J | Thermocouple type J |
                +---------------------+---------------------+
                | NIDMM_VAL_TEMP_TC_K | Thermocouple type K |
                +---------------------+---------------------+
                | NIDMM_VAL_TEMP_TC_N | Thermocouple type N |
                +---------------------+---------------------+
                | NIDMM_VAL_TEMP_TC_R | Thermocouple type R |
                +---------------------+---------------------+
                | NIDMM_VAL_TEMP_TC_S | Thermocouple type S |
                +---------------------+---------------------+
                | NIDMM_VAL_TEMP_TC_T | Thermocouple type T |
                +---------------------+---------------------+
            reference_junction_type (int):Specifies the type of reference junction to be used in the reference
                junction compensation of a thermocouple measurement. NI-DMM uses this
                value to set the Reference Junction Type property. The only supported
                value is NIDMM_VAL_TEMP_REF_JUNC_FIXED.
        '''
        if type(thermocouple_type) is not enums.ThermocoupleType:
            raise TypeError('Parameter mode must be of type ' + str(enums.ThermocoupleType))
        error_code = self.library.niDMM_ConfigureThermocouple(self.vi, thermocouple_type.value, reference_junction_type)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_transducer_type(self, transducer_type):
        '''configure_transducer_type

        Configures the transducer type.

        Args:
            transducer_type (enums.TemperatureTransducerType):Specifies the type of device used to measure the temperature. NI-DMM
                uses this value to set the Transducer Type property. The default is
                NIDMM_VAL_THERMOCOUPLE.

                +------------------------+--------------+
                | NIDMM_VAL_2_WIRE_RTD   | 2-wire RTD   |
                +------------------------+--------------+
                | NIDMM_VAL_4_WIRE_RTD   | 4-wire RTD   |
                +------------------------+--------------+
                | NIDMM_VAL_THERMISTOR   | Thermistor   |
                +------------------------+--------------+
                | NIDMM_VAL_THERMOCOUPLE | Thermocouple |
                +------------------------+--------------+
        '''
        if type(transducer_type) is not enums.TemperatureTransducerType:
            raise TypeError('Parameter mode must be of type ' + str(enums.TemperatureTransducerType))
        error_code = self.library.niDMM_ConfigureTransducerType(self.vi, transducer_type.value)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_trigger(self, trigger_source, trigger_delay):
        '''configure_trigger

        Configures the DMM **Trigger_Source** and **Trigger_Delay**. Refer to
        `Triggering <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/trigger/>`__
        and `Using
        Switches <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/switch_selection/>`__
        for more information.

        Args:
            trigger_source (enums.TriggerSource):Specifies the **trigger_source** that initiates the acquisition. The
                driver sets TRIGGER_SOURCE to this value. Software
                configures the DMM to wait until send_software_trigger is called
                before triggering the DMM.

                Note:
                To determine which values are supported by each device, refer to the
                `LabWindows/CVI Trigger
                Routing <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/cvitrigger_routing/>`__
                section.
            trigger_delay (float):Specifies the time that the DMM waits after it has received a trigger
                before taking a measurement. The driver sets the
                TRIGGER_DELAY attribute to this value. By default,
                **trigger_delay** is NIDMM_VAL_AUTO_DELAY (-1), which means the DMM
                waits an appropriate settling time before taking the measurement. On the
                NI 4060, if you set **trigger_delay** to 0, the DMM does not settle
                before taking the measurement. The NI 4065 and NI 4070/4071/4072 use the
                value specified in **trigger_delay** as additional settling time.

                Note:
                When using the NI 4050, **Trigger_Delay** must be set to
                NIDMM_VAL_AUTO_DELAY (-1).
        '''
        if type(trigger_source) is not enums.TriggerSource:
            raise TypeError('Parameter mode must be of type ' + str(enums.TriggerSource))
        error_code = self.library.niDMM_ConfigureTrigger(self.vi, trigger_source.value, trigger_delay)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_trigger_slope(self, trigger_slope):
        '''configure_trigger_slope

        Sets the TRIGGER_SLOPE attribute to either rising edge
        (positive) or falling edge (negative) polarity.

        Args:
            trigger_slope (enums.Slope):Specifies the polarity of the trigger signal on which the measurement is
                triggered for values of either NIDMM_VAL_POSITIVE or
                NIDMM_VAL_NEGATIVE. The driver sets the TRIGGER_SLOPE
                attribute to this value.

                +------------------------------+---+----------------------------------------------------------------+
                | NIDMM_VAL_POSITIVE           | 0 | The driver triggers on the rising edge of the trigger signal.  |
                +------------------------------+---+----------------------------------------------------------------+
                | NIDMM_VAL_NEGATIVE (default) | 1 | The driver triggers on the falling edge of the trigger signal. |
                +------------------------------+---+----------------------------------------------------------------+
        '''
        if type(trigger_slope) is not enums.Slope:
            raise TypeError('Parameter mode must be of type ' + str(enums.Slope))
        error_code = self.library.niDMM_ConfigureTriggerSlope(self.vi, trigger_slope.value)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_waveform_acquisition(self, measurement_function, range, rate, waveform_points):
        '''configure_waveform_acquisition

        Configures the DMM for waveform acquisitions. This feature is supported
        on the NI 4080/4081/4082 and the NI 4070/4071/4072.

        Args:
            measurement_function (enums.Function):Specifies the **measurement_function** used in a waveform acquisition.
                The driver sets function to this value.

                +--------------------------------------+------+------------------+
                | NIDMM_VAL_WAVEFORM_VOLTAGE (default) | 1003 | Voltage Waveform |
                +--------------------------------------+------+------------------+
                | NIDMM_VAL_WAVEFORM_CURRENT           | 1004 | Current Waveform |
                +--------------------------------------+------+------------------+
            range (float):Specifies the expected maximum amplitude of the input signal and sets
                the **range** for the **Measurement_Function**. NI-DMM sets
                range to this value. **range** values are coerced up to the
                closest input **range**. The default is 10.0.

                For valid ranges refer to the topics in
                `Devices <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/devices/>`__.

                Auto-ranging is not supported during waveform acquisitions.
            rate (float):Specifies the **rate** of the acquisition in samples per second. NI-DMM
                sets WAVEFORM_RATE to this value.

                The valid **Range** is 10.0–1,800,000 S/s. **rate** values are coerced
                to the closest integer divisor of 1,800,000. The default value is
                1,800,000.
            waveform_points (int):Specifies the number of points to acquire before the waveform
                acquisition completes. NI-DMM sets WAVEFORM_POINTS to this
                value.

                To calculate the maximum and minimum number of waveform points that you
                can acquire in one acquisition, refer to the `Waveform Acquisition
                Measurement
                Cycle <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/waveform_cycle/>`__.

                The default value is 500.
        '''
        if type(measurement_function) is not enums.Function:
            raise TypeError('Parameter mode must be of type ' + str(enums.Function))
        error_code = self.library.niDMM_ConfigureWaveformAcquisition(self.vi, measurement_function.value, range, rate, waveform_points)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_waveform_coupling(self, waveform_coupling):
        '''configure_waveform_coupling

        For the NI 4080/4081/4082 and the NI 4070/4071/4072, configures
        instrument coupling for voltage waveforms.

        Args:
            waveform_coupling (enums.WaveformCouplingMode):Selects DC or AC coupling. The driver sets
                WAVEFORM_COUPLING to this value.

                +------------------------------------------+-------+-------------+
                | Name                                     | Value | Description |
                +==========================================+=======+=============+
                | NIDMM_VAL_WAVEFORM_COUPLING_AC           | 0     | AC coupling |
                +------------------------------------------+-------+-------------+
                | NIDMM_VAL_WAVEFORM_COUPLING_DC (default) | 1     | DC coupling |
                +------------------------------------------+-------+-------------+
        '''
        if type(waveform_coupling) is not enums.WaveformCouplingMode:
            raise TypeError('Parameter mode must be of type ' + str(enums.WaveformCouplingMode))
        error_code = self.library.niDMM_ConfigureWaveformCoupling(self.vi, waveform_coupling.value)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disable(self):
        '''disable

        Places the instrument in a quiescent state where it has minimal or no
        impact on the system to which it is connected. If a measurement is in
        progress when this function is called, the measurement is aborted.
        '''
        error_code = self.library.niDMM_Disable(self.vi)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def fetch(self, maximum_time):
        '''fetch

        Returns the value from a previously initiated measurement. You must call
        _initiate before calling this function.

        Args:
            maximum_time (int):Specifies the **maximum_time** allowed for this function to complete in
                milliseconds. If the function does not complete within this time
                interval, the function returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                NIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout
                automatically.

        Returns:
            reading (float):The measured value returned from the DMM.
        '''
        reading_ctype = ctypes_types.ViReal64_ctype(0)
        error_code = self.library.niDMM_Fetch(self.vi, maximum_time, ctypes.pointer(reading_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return python_types.ViReal64(reading_ctype.value)

    def fetch_multi_point(self, maximum_time, array_size):
        '''fetch_multi_point

        Returns an array of values from a previously initiated multipoint
        measurement. The number of measurements the DMM makes is determined by
        the values you specify for the **Trigger_Count** and **Sample_Count**
        parameters of configure_multi_point. You must first call
        _initiate to initiate a measurement before calling this function.

        Args:
            maximum_time (int):Specifies the **maximum_time** allowed for this function to complete in
                milliseconds. If the function does not complete within this time
                interval, the function returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                NIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout
                automatically.
            array_size (int):Specifies the number of measurements to acquire. The maximum number of
                measurements for a finite acquisition is the (**Trigger Count** x
                **Sample Count**) parameters in configure_multi_point.

                For continuous acquisitions, up to 100,000 points can be returned at
                once. The number of measurements can be a subset. The valid range is any
                positive ViInt32. The default value is 1.

        Returns:
            reading_array (float):An array of measurement values.

                Note:
                The size of the **Reading_Array** must be at least the size that you
                specify for the **Array_Size** parameter.
            actual_number_of_points (int):Indicates the number of measured values actually retrieved from the DMM.
        '''
        reading_array_ctype = (ctypes_types.ViReal64_ctype * array_size)()
        actual_number_of_points_ctype = ctypes_types.ViInt32_ctype(0)
        error_code = self.library.niDMM_FetchMultiPoint(self.vi, maximum_time, array_size, ctypes.cast(reading_array_ctype, ctypes.POINTER(ctypes_types.ViReal64_ctype)), ctypes.pointer(actual_number_of_points_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [python_types.ViReal64(reading_array_ctype[i].value) for i in range(array_size)], python_types.ViInt32(actual_number_of_points_ctype.value)

    def fetch_waveform(self, maximum_time, array_size):
        '''fetch_waveform

        For the NI 4080/4081/4082 and the NI 4070/4071/4072, returns an array of
        values from a previously initiated waveform acquisition. You must call
        _initiate before calling this function.

        Args:
            maximum_time (int):Specifies the **maximum_time** allowed for this function to complete in
                milliseconds. If the function does not complete within this time
                interval, the function returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                NIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout
                automatically.
            array_size (int):Specifies the number of waveform points to return. You specify the total
                number of points that the DMM acquires in the **Waveform Points**
                parameter of configure_waveform_acquisition. The default value is
                1.

        Returns:
            waveform_array (float):**Waveform Array** is an array of measurement values stored in waveform
                data type.
            actual_number_of_points (int):Indicates the number of measured values actually retrieved from the DMM.
        '''
        waveform_array_ctype = (ctypes_types.ViReal64_ctype * array_size)()
        actual_number_of_points_ctype = ctypes_types.ViInt32_ctype(0)
        error_code = self.library.niDMM_FetchWaveform(self.vi, maximum_time, array_size, ctypes.cast(waveform_array_ctype, ctypes.POINTER(ctypes_types.ViReal64_ctype)), ctypes.pointer(actual_number_of_points_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [python_types.ViReal64(waveform_array_ctype[i].value) for i in range(array_size)], python_types.ViInt32(actual_number_of_points_ctype.value)

    def format_meas_absolute(self, measurement_function, range, resolution, measurement):
        '''format_meas_absolute

        Formats the **Measurement** to the proper number of displayed digits
        according to the **Measurement_Function**, **Range**, and
        **Resolution**. Returns the formatted data, range, and mode strings.

        Args:
            measurement_function (int):Specifies the **measurement_function** used to acquire the measurement.
                The driver sets function to this value.
            range (float):Specifies the range used to acquire the **Measurement**.
            resolution (float):Specifies the RESOLUTION_ABSOLUTE of the **Measurement**.
            measurement (float):Specifies the measured value returned from the DMM.

        Returns:
            mode_string (int):Returns a string containing the units of the **Measurement** mode.
            range_string (int):Returns the range of the **Measurement**, formatted into a
                string with the correct number of display digits.
            data_string (int):Returns the **Measurement**, formatted according to the
                function, range, and
                RESOLUTION_ABSOLUTE.
        '''
        mode_string_ctype = ctypes_types.ViChar_ctype(0)
        range_string_ctype = ctypes_types.ViChar_ctype(0)
        data_string_ctype = ctypes_types.ViChar_ctype(0)
        error_code = self.library.niDMM_FormatMeasAbsolute(measurement_function, range, resolution, measurement, ctypes.pointer(mode_string_ctype), ctypes.pointer(range_string_ctype), ctypes.pointer(data_string_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return python_types.ViChar(mode_string_ctype.value), python_types.ViChar(range_string_ctype.value), python_types.ViChar(data_string_ctype.value)

    def get_aperture_time_info(self):
        '''get_aperture_time_info

        Returns the DMM **Aperture_Time** and **Aperture_Time_Units**.

        Returns:
            aperture_time (float):Specifies the amount of time the DMM digitizes the input signal for a
                single measurement. This parameter does not include settling time.
                Returns the value of the APERTURE_TIME attribute. The
                units of this attribute depend on the value of the
                APERTURE_TIME_UNITS attribute.
                On the NI 4070/4071/4072, the minimum aperture time is 8.89 µs, and the
                maximum aperture time is 149 s. Any number of powerline cycles (PLCs)
                within the minimum and maximum ranges is allowed on the
                NI 4070/4071/4072.
                On the NI 4065 the minimum aperture time is 333 µs, and the maximum
                aperture time is 78.2 s. If setting the number of averages directly, the
                total measurement time is aperture time X the number of averages, which
                must be less than 72.8 s. The aperture times allowed are 333 µs, 667 µs,
                or multiples of 1.11 ms—for example 1.11 ms, 2.22 ms, 3.33 ms, and so
                on. If you set an aperture time other than 333 µs, 667 µs, or multiples
                of 1.11 ms, the value will be coerced up to the next supported aperture
                time.
                On the NI 4060, when the powerline frequency is 60, the PLCs allowed are
                1 PLC, 6 PLC, 12 PLC, and 120 PLC. When the powerline frequency is 50,
                the PLCs allowed are 1 PLC, 5 PLC, 10 PLC, and 100 PLC.
            aperture_time_units (enums.ApertureTimeUnits):Indicates the units of aperture time as powerline cycles (PLCs) or
                seconds. Returns the value of the APERTURE_TIME_UNITS
                attribute.

                +-----------------------------+---+------------------+
                | NIDMM_VAL_SECONDS           | 0 | Seconds          |
                +-----------------------------+---+------------------+
                | NIDMM_VAL_POWER_LINE_CYCLES | 1 | Powerline Cycles |
                +-----------------------------+---+------------------+
        '''
        aperture_time_ctype = ctypes_types.ViReal64_ctype(0)
        aperture_time_units_ctype = ctypes_types.ViInt32_ctype(0)
        error_code = self.library.niDMM_GetApertureTimeInfo(self.vi, ctypes.pointer(aperture_time_ctype), ctypes.pointer(aperture_time_units_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return python_types.ViReal64(aperture_time_ctype.value), enums.ApertureTimeUnits(aperture_time_units_ctype.value)

    def _get_attribute_vi_boolean(self, channel_name, attribute_id):
        '''_get_attribute_vi_boolean

        Queries the value of a ViBoolean attribute. You can use this function to
        get the values of instrument-specific attributes and inherent IVI
        attributes.

        If the attribute represents an instrument state, this function performs
        instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular attribute.
        -  State caching is enabled, and the currently cached value is invalid.

        Args:
            channel_name (str):This parameter is ignored. National Instruments DMMs do not support
                channel names since they only have a single channel. This parameter is
                included in order to support interchangeability and upgradability to
                multiple channel DMMs.

                The default value is " " (an empty string).
            attribute_id (int):Pass the ID of an attribute.

        Returns:
            attribute_value (bool):Returns the current value of the attribute. Pass the address of a
                ViBoolean variable.
        '''
        attribute_value_ctype = ctypes_types.ViBoolean_ctype(0)
        error_code = self.library.niDMM_GetAttributeViBoolean(self.vi, channel_name.encode('ascii'), attribute_id, ctypes.pointer(attribute_value_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return python_types.ViBoolean(attribute_value_ctype.value)

    def _get_attribute_vi_int32(self, channel_name, attribute_id):
        '''_get_attribute_vi_int32

        Queries the value of a ViInt32 attribute. You can use this function to
        get the values of instrument-specific attributes and inherent IVI
        attributes.

        If the attribute represents an instrument state, this function performs
        instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular attribute.
        -  State caching is enabled, and the currently cached value is invalid.

        Args:
            channel_name (str):This parameter is ignored. National Instruments DMMs do not support
                channel names since they only have a single channel. This parameter is
                included in order to support interchangeability and upgradability to
                multiple channel DMMs.

                The default value is " " (an empty string).
            attribute_id (int):Pass the ID of an attribute.

        Returns:
            attribute_value (int):Returns the current value of the attribute. Pass the address of a
                ViInt32 variable.
        '''
        attribute_value_ctype = ctypes_types.ViInt32_ctype(0)
        error_code = self.library.niDMM_GetAttributeViInt32(self.vi, channel_name.encode('ascii'), attribute_id, ctypes.pointer(attribute_value_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return python_types.ViInt32(attribute_value_ctype.value)

    def _get_attribute_vi_real64(self, channel_name, attribute_id):
        '''_get_attribute_vi_real64

        Queries the value of a ViReal64 attribute. You can use this function to
        get the values of instrument-specific attributes and inherent IVI
        attributes.

        If the attribute represents an instrument state, this function performs
        instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular attribute.
        -  State caching is enabled, and the currently cached value is invalid.

        Args:
            channel_name (str):This parameter is ignored. National Instruments DMMs do not support
                channel names since they only have a single channel. This parameter is
                included in order to support interchangeability and upgradability to
                multiple channel DMMs.

                The default value is " " (an empty string).
            attribute_id (int):Pass the ID of an attribute.

        Returns:
            attribute_value (float):Returns the current value of the attribute. Pass the address of a
                ViReal64 variable.
        '''
        attribute_value_ctype = ctypes_types.ViReal64_ctype(0)
        error_code = self.library.niDMM_GetAttributeViReal64(self.vi, channel_name.encode('ascii'), attribute_id, ctypes.pointer(attribute_value_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return python_types.ViReal64(attribute_value_ctype.value)

    def _get_attribute_vi_string(self, channel_name, attribute_id):
        '''_get_attribute_vi_string

        Queries the value of a ViString attribute. You can use this function to
        get the values of instrument-specific attributes and inherent IVI
        attributes.

        If the attribute represents an instrument state, this function performs
        instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular attribute.
        -  State caching is enabled, and the currently cached value is invalid.
           You must provide a ViChar array to serve as a buffer for the value.
           You pass the number of bytes in the buffer as the Array Size
           parameter.

        Args:
            channel_name (str):This parameter is ignored. National Instruments DMMs do not support
                channel names since they only have a single channel. This parameter is
                included in order to support interchangeability and upgradability to
                multiple channel DMMs.

                The default value is " " (an empty string).
            attribute_id (int):Pass the ID of an attribute.
            buffer_size (int):Pass the number of bytes in the ViChar array you specify for the
                **Attribute_Value** parameter.

                If the current value of the attribute, including the terminating NULL
                byte, contains more bytes that you indicate in this parameter, the
                function copies **buffer_size**—1 bytes into the buffer, places an
                ASCII NUL byte at the end of the buffer, and returns the buffer size you
                must pass to get the entire value. For example, if the value is "123456"
                and the **buffer_size** is 4, the function places "123" into the buffer
                and returns 7.

                If you pass a negative number, the function copies the value to the
                buffer regardless of the number of bytes in the value. If you pass 0,
                you can pass VI_NULL for the **Attribute_Value** buffer parameter.
        '''
        buffer_size = 0
        attribute_value_ctype = None
        error_code = self.library.niDMM_GetAttributeViString(self.vi, channel_name.encode('ascii'), attribute_id, buffer_size, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size = error_code
        attribute_value_ctype = ctypes.cast(ctypes.create_string_buffer(buffer_size), ctypes_types.ViString_ctype)
        error_code = self.library.niDMM_GetAttributeViString(self.vi, channel_name.encode('ascii'), attribute_id, buffer_size, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return attribute_value_ctype.value.decode("ascii")

    def get_auto_range_value(self):
        '''get_auto_range_value

        Returns the **Actual_Range** that the DMM is using, even when Auto
        Range is off.

        Returns:
            actual_range (float):Indicates the **actual_range** the DMM is using. Returns the value of
                the AUTO_RANGE_VALUE attribute. The units of the returned
                value depend on the function.
        '''
        actual_range_ctype = ctypes_types.ViReal64_ctype(0)
        error_code = self.library.niDMM_GetAutoRangeValue(self.vi, ctypes.pointer(actual_range_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return python_types.ViReal64(actual_range_ctype.value)

    def get_cal_count(self, cal_type):
        '''get_cal_count

        Returns the calibration **Count** for the specified type of calibration.

        Note: The NI 4050, NI 4060, and NI 4080/4081/4082 are not supported.

        Args:
            cal_type (int):Specifies the type of calibration performed (external or
                self-calibration).

                +-----------------------------------+---+----------------------+
                | NIDMM_VAL_INTERNAL_AREA (default) | 0 | Self-Calibration     |
                +-----------------------------------+---+----------------------+
                | NIDMM_VAL_EXTERNAL_AREA           | 1 | External Calibration |
                +-----------------------------------+---+----------------------+

                Note: The NI 4065 does not support self-calibration.

        Returns:
            count (int):The number of times calibration has been performed.
        '''
        count_ctype = ctypes_types.ViInt32_ctype(0)
        error_code = self.library.niDMM_GetCalCount(self.vi, cal_type, ctypes.pointer(count_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return python_types.ViInt32(count_ctype.value)

    def get_cal_date_and_time(self, cal_type):
        '''get_cal_date_and_time

        Returns the date and time of the last calibration performed.

        Note: The NI 4050 and NI 4060 are not supported.

        Args:
            cal_type (int):Specifies the type of calibration performed (external or
                self-calibration).

                +-----------------------------------+---+----------------------+
                | NIDMM_VAL_INTERNAL_AREA (default) | 0 | Self-Calibration     |
                +-----------------------------------+---+----------------------+
                | NIDMM_VAL_EXTERNAL_AREA           | 1 | External Calibration |
                +-----------------------------------+---+----------------------+

                Note: The NI 4065 does not support self-calibration.

        Returns:
            month (int):Indicates the **month** of the last calibration.
            day (int):Indicates the **day** of the last calibration.
            year (int):Indicates the **year** of the last calibration.
            hour (int):Indicates the **hour** of the last calibration.
            minute (int):Indicates the **minute** of the last calibration.
        '''
        month_ctype = ctypes_types.ViInt32_ctype(0)
        day_ctype = ctypes_types.ViInt32_ctype(0)
        year_ctype = ctypes_types.ViInt32_ctype(0)
        hour_ctype = ctypes_types.ViInt32_ctype(0)
        minute_ctype = ctypes_types.ViInt32_ctype(0)
        error_code = self.library.niDMM_GetCalDateAndTime(self.vi, cal_type, ctypes.pointer(month_ctype), ctypes.pointer(day_ctype), ctypes.pointer(year_ctype), ctypes.pointer(hour_ctype), ctypes.pointer(minute_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return python_types.ViInt32(month_ctype.value), python_types.ViInt32(day_ctype.value), python_types.ViInt32(year_ctype.value), python_types.ViInt32(hour_ctype.value), python_types.ViInt32(minute_ctype.value)

    def get_channel_name(self, index, buffer_size):
        '''get_channel_name

        Returns the **Channel_String** that is in the channel table at an
        **Index** you specify. Not applicable to National Instruments DMMs.
        Included for compliance with the *IviDmm Class Specification*.

        Args:
            index (int):A 1–based **index** into the channel table.
            buffer_size (int):Passes the number of bytes in the ViChar array you specify for the
                **Channel_String** parameter. If the next **Channel_String**,
                including the terminating NULL byte, contains more bytes than you
                indicate in this parameter, the function copies
                **buffer_size** –1 bytes into the buffer, places an ASCII NULL byte at
                the end of the buffer, and returns the buffer size you must pass to get
                the entire value.

                For example, if the value is "123456" and the **buffer_size** is 4, the
                function places "123" into the buffer and returns 7. If you pass a
                negative number, the function copies the value to the buffer regardless
                of the number of bytes in the value. If you pass 0, you can pass
                VI_NULL for the **Channel_String** buffer parameter. The default value
                is None.

        Returns:
            channel_string (int):Returns the **channel_string** that is in the channel table at the
                **Index** you specify. Do not modify the contents of the
                **channel_string**.
        '''
        channel_string_ctype = ctypes_types.ViChar_ctype(0)
        error_code = self.library.niDMM_GetChannelName(self.vi, index, buffer_size, ctypes.pointer(channel_string_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return python_types.ViChar(channel_string_ctype.value)

    def get_dev_temp(self, options):
        '''get_dev_temp

        Returns the current **Temperature** of the device.

        Note: The NI 4050 and NI 4060 are not supported.

        Args:
            options (str):Reserved.

        Returns:
            temperature (float):Returns the current **temperature** of the device.
        '''
        temperature_ctype = ctypes_types.ViReal64_ctype(0)
        error_code = self.library.niDMM_GetDevTemp(self.vi, options.encode('ascii'), ctypes.pointer(temperature_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return python_types.ViReal64(temperature_ctype.value)

    def _get_error(self):
        '''_get_error

        Returns the error information associated with the
        **Instrument_Handle**. This function retrieves and then clears the
        error information for the session. If you leave the
        **Instrument_Handle** unwired, this function retrieves and then clears
        the error information for the process.

        Args:
            buffer_size (int):Passes the number of bytes in the ViChar array you specify for the
                **Description** parameter. If the error description, including the
                terminating NULL byte, contains more bytes than you indicate in this
                parameter, the function copies **buffer_size** –1 bytes into the
                buffer, places an ASCII NULL byte at the end of the buffer, and returns
                the **buffer_size** you must pass to get the entire value.

                For example, if the value is "123456" and the **buffer_size** is 4, the
                function places "123" into the buffer and returns 7. If you pass a
                negative number, the function copies the value to the buffer regardless
                of the number of bytes in the value. If you pass 0, you can pass
                VI_NULL for the **Description** buffer parameter. The default value is
                None.

        Returns:
            error_code (int):Returns the **error_code** for the session or execution thread. If you
                pass 0 for the **Buffer_Size**, you can pass VI_NULL for this
                parameter.
        '''
        error_code_ctype = ctypes_types.ViStatus_ctype(0)
        buffer_size = 0
        description_ctype = None
        error_code = self.library.niDMM_GetError(self.vi, ctypes.pointer(error_code_ctype), buffer_size, description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=True)
        buffer_size = error_code
        description_ctype = ctypes.cast(ctypes.create_string_buffer(buffer_size), ctypes_types.ViString_ctype)
        error_code = self.library.niDMM_GetError(self.vi, ctypes.pointer(error_code_ctype), buffer_size, description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return python_types.ViStatus(error_code_ctype.value), description_ctype.value.decode("ascii")

    def _get_error_message(self, error_code):
        '''_get_error_message

        Returns the **Error_Message** as a user-readable string for the
        provided **Error_Code**. Calling this function with a **Buffer_Size**
        of 0 returns the size needed for the **Error_Message**.

        Args:
            error_code (int):The error code returned from the instrument for which you want to get a
                user-readable string.
            buffer_size (int):Specifies the number of bytes allocated for the **Error_Message**
                ViChar array. If the error description that this function returns
                (including terminating NULL byte) is larger than you indicated in
                **buffer_size**, the error description will be truncated to fit. If you
                pass 0 for **buffer_size**, the function returns the buffer size needed
                for **Error_Message**.
        '''
        buffer_size = 0
        error_message_ctype = None
        error_code = self.library.niDMM_GetErrorMessage(self.vi, error_code, buffer_size, error_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=True)
        buffer_size = error_code
        error_message_ctype = ctypes.cast(ctypes.create_string_buffer(buffer_size), ctypes_types.ViString_ctype)
        error_code = self.library.niDMM_GetErrorMessage(self.vi, error_code, buffer_size, error_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return error_message_ctype.value.decode("ascii")

    def get_last_cal_temp(self, cal_type):
        '''get_last_cal_temp

        Returns the **Temperature** during the last calibration procedure.

        Note: The NI 4050 and NI 4060 are not supported.

        Args:
            cal_type (int):Specifies the type of calibration performed (external or
                self-calibration).

                +-----------------------------------+---+----------------------+
                | NIDMM_VAL_INTERNAL_AREA (default) | 0 | Self-Calibration     |
                +-----------------------------------+---+----------------------+
                | NIDMM_VAL_EXTERNAL_AREA           | 1 | External Calibration |
                +-----------------------------------+---+----------------------+

                Note: The NI 4065 does not support self-calibration.

        Returns:
            temperature (float):Returns the **temperature** during the last calibration.
        '''
        temperature_ctype = ctypes_types.ViReal64_ctype(0)
        error_code = self.library.niDMM_GetLastCalTemp(self.vi, cal_type, ctypes.pointer(temperature_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return python_types.ViReal64(temperature_ctype.value)

    def get_measurement_period(self):
        '''get_measurement_period

        Returns the measurement **Period**, which is the amount of time it takes
        to complete one measurement with the current configuration. Use this
        function right before you begin acquiring data—after you have completely
        configured the measurement and after all configuration functions have
        been called.

        Returns:
            period (float):Returns the number of seconds it takes to make one measurement.

                The first measurement in a multipoint acquisition requires additional
                settling time. This function does not include this additional time or
                any TRIGGER_DELAY associated with the first measurement.
                Time required for internal measurements, such as
                AUTO_ZERO, is included.
        '''
        period_ctype = ctypes_types.ViReal64_ctype(0)
        error_code = self.library.niDMM_GetMeasurementPeriod(self.vi, ctypes.pointer(period_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return python_types.ViReal64(period_ctype.value)

    def get_next_coercion_record(self, buffer_size):
        '''get_next_coercion_record

        This function returns the coercion information associated with the IVI
        session, and it retrieves and clears the oldest instance in which NI-DMM
        coerced a value you specified to another value.

        If you set RECORD_COERCIONS to VI_TRUE (1), NI-DMM keeps
        a list of all coercions it makes on ViInt32 or ViReal64 values that you
        pass to NI-DMM functions. Use this function to retrieve information from
        that list.

        Args:
            buffer_size (int):Passes the number of bytes in the ViChar array you specify for the
                **Coercion_Record** parameter. If the next coercion record string,
                including the terminating NULL byte, contains more bytes than you
                indicate in this parameter, the function copies **buffer_size** – 1
                bytes into the buffer, places an ASCII NULL byte at the end of the
                buffer, and returns the buffer size you must pass to get the entire
                value.

                For example, if the value is "123456" and the **buffer_size** is 4, the
                function places "123" into the buffer and returns 7. If you pass a
                negative number, the function copies the value to the buffer regardless
                of the number of bytes in the value.

                If you pass 0, you can pass VI_NULL for the **Coercion_Record** buffer
                parameter.

                The default value is None.

        Returns:
            coercion_record (int):Returns the next **coercion_record** for the IVI session.

                If there are no coercions records, the function returns an empty string.
                The buffer must contain at least as many elements as the value you
                specify with the **Buffer_Size** parameter.
        '''
        coercion_record_ctype = ctypes_types.ViChar_ctype(0)
        error_code = self.library.niDMM_GetNextCoercionRecord(self.vi, buffer_size, ctypes.pointer(coercion_record_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return python_types.ViChar(coercion_record_ctype.value)

    def get_next_interchange_warning(self):
        '''get_next_interchange_warning

        This function returns the interchangeability warnings associated with
        the IVI session. It retrieves and clears the oldest instance in which
        the class driver recorded an interchangeability warning.
        Interchangeability warnings indicate that using your application with a
        different instrument might cause different behavior.

        The driver performs interchangeability checking when
        INTERCHANGE_CHECK is set to VI_TRUE (1). The function
        returns an empty string in the **Interchange_Warning** parameter if no
        interchangeability warnings remain for the session. In general, the
        instrument driver generates interchangeability warnings when an
        attribute that affects the behavior of the instrument is in a state that
        you did not specify.

        Args:
            buffer_size (int):Passes the number of bytes in the ViChar array you specify for the
                **Interchange_Warning** parameter. If the next interchangeability
                warning string, including the terminating NULL byte, contains more bytes
                than you indicate in this parameter, the function copies
                **buffer_size** –1 bytes into the buffer, places an ASCII NULL byte at
                the end of the buffer, and returns the buffer size you must pass to get
                the entire value.

                For example, if the value is "123456" and the **buffer_size** is 4, the
                function places "123" into the buffer and returns 7. If you pass a
                negative number, the function copies the value to the buffer regardless
                of the number of bytes in the value. If you pass 0, you can pass
                VI_NULL for the **Interchange_Warning** buffer parameter. The default
                value is None.
        '''
        buffer_size = 0
        interchange_warning_ctype = None
        error_code = self.library.niDMM_GetNextInterchangeWarning(self.vi, buffer_size, interchange_warning_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size = error_code
        interchange_warning_ctype = ctypes.cast(ctypes.create_string_buffer(buffer_size), ctypes_types.ViChar_ctype)
        error_code = self.library.niDMM_GetNextInterchangeWarning(self.vi, buffer_size, interchange_warning_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return interchange_warning_ctype.value.decode("ascii")

    def get_self_cal_supported(self):
        '''get_self_cal_supported

        Returns a Boolean value that expresses whether or not the DMM that you
        are using can perform self-calibration.

        Returns:
            self_cal_supported (bool):Returns whether Self Cal is supported for the device specified by the
                given session.

                +----------+---+-------------------------------------------------------------+
                | VI_TRUE  | 1 | The DMM that you are using can perform self-calibration.    |
                +----------+---+-------------------------------------------------------------+
                | VI_FALSE | 0 | The DMM that you are using cannot perform self-calibration. |
                +----------+---+-------------------------------------------------------------+
        '''
        self_cal_supported_ctype = ctypes_types.ViBoolean_ctype(0)
        error_code = self.library.niDMM_GetSelfCalSupported(self.vi, ctypes.pointer(self_cal_supported_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return python_types.ViBoolean(self_cal_supported_ctype.value)

    def _init_with_options(self, resource_name, id_query=False, reset_device=False, option_string=''):
        '''_init_with_options

        This function completes the following tasks:

        -  Creates a new IVI instrument driver session and, optionally, sets the
           initial state of the following session attributes:
           RANGE_CHECK, QUERY_INSTR_STATUS,
           cache, simulate,
           RECORD_COERCIONS.
        -  Opens a session to the device you specify for the **Resource_Name**
           parameter. If the **ID_Query** parameter is set to VI_TRUE, this
           function queries the instrument ID and checks that it is valid for
           this instrument driver.
        -  If the **Reset_Device** parameter is set to VI_TRUE, this function
           resets the instrument to a known state. Sends initialization commands
           to set the instrument to the state necessary for the operation of the
           instrument driver.
        -  Returns a ViSession handle that you use to identify the instrument in
           all subsequent instrument driver function calls.

        Args:
            resource_name (str):Caution:
                All IVI names for the **Resource_Name**, such as logical names or
                virtual names, are case-sensitive. If you use logical names, driver
                session names, or virtual names in your program, you must make sure that
                the name you use matches the name in the IVI Configuration Store file
                exactly, without any variations in the case of the characters in the
                name.

                | Contains the **resource_name** of the device to initialize. The
                  **resource_name** is assigned in Measurement & Automation Explorer
                  (MAX). Refer to `Related
                  Documentation <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/related_documentation/>`__
                  for the *NI Digital Multimeters Getting Started Guide* for more
                  information about configuring and testing the DMM in MAX.
                | Valid Syntax:

                -  NI-DAQmx name
                -  DAQ::NI-DAQmx name[::INSTR]
                -  DAQ::Traditional NI-DAQ device number[::INSTR]
                -  IVI logical name
            id_query (bool):Verifies that the device you initialize is one that the driver supports.
                NI-DMM automatically performs this query, so setting this parameter is
                not necessary.
                Defined Values:

                +-------------------+---+------------------+
                | VI_TRUE (default) | 1 | Perform ID Query |
                +-------------------+---+------------------+
                | VI_FALSE          | 0 | Skip ID Query    |
                +-------------------+---+------------------+
            reset_device (bool):Specifies whether to reset the instrument during the initialization
                procedure.
                Defined Values:

                +-------------------+---+--------------+
                | VI_TRUE (default) | 1 | Reset Device |
                +-------------------+---+--------------+
                | VI_FALSE          | 0 | Don't Reset  |
                +-------------------+---+--------------+
            option_string (str):| Sets the initial value of certain attributes for the session. The
                  following table specifies the attribute name, attribute constant, and
                  default value for each attribute that you can use in this parameter:

                The format of this string is, "AttributeName=Value." To set multiple
                attributes, separate their assignments with a comma.

                If you pass NULL or an empty string for this parameter, the session uses
                the default values for the attributes. You can override the default
                values by assigning a value explicitly in an **option_string**
                parameter. You do not have to specify all of the attributes and may
                leave any of them out (those left out use the default value).

                Refer to `Simulating NI Digital
                Multimeters <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/simulation/>`__
                for more information.

                +------------------+--------------------+-------------------+----+
                | Check            | RANGE_CHECK        | VI_TRUE           | 1  |
                +------------------+--------------------+-------------------+----+
                | QueryInstrStatus | QUERY_INSTR_STATUS | VI_FALSE          | 0  |
                +------------------+--------------------+-------------------+----+
                | Cache            | cache              | VI_TRUE           | 1  |
                +------------------+--------------------+-------------------+----+
                | Simulate         | simulate           | VI_FALSE          | 0  |
                +------------------+--------------------+-------------------+----+
                | RecordCoercions  | RECORD_COERCIONS   | VI_FALSE          | 0  |
                +------------------+--------------------+-------------------+----+
                | DriverSetup      | DRIVER_SETUP       | "" (empty string) | "" |
                +------------------+--------------------+-------------------+----+

        Returns:
            vi (int):Returns a ViSession handle that you use to identify the instrument in
                all subsequent instrument driver function calls.
        '''
        vi_ctype = ctypes_types.ViSession_ctype(0)
        error_code = self.library.niDMM_InitWithOptions(resource_name.encode('ascii'), id_query, reset_device, option_string.encode('ascii'), ctypes.pointer(vi_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return python_types.ViSession(vi_ctype.value)

    def _initiate(self):
        '''_initiate

        Initiates an acquisition. After you call this function, the DMM leaves
        the Idle state and enters the Wait-for-Trigger state. If trigger is set
        to Immediate mode, the DMM begins acquiring measurement data. Use
        fetch, fetch_multi_point, or fetch_waveform to
        retrieve the measurement data.
        '''
        error_code = self.library.niDMM_Initiate(self.vi)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def is_over_range(self, measurement_value):
        '''is_over_range

        Takes a **Measurement_Value** and determines if the value is a valid
        measurement or a value indicating that an overrange condition occurred.

        Args:
            measurement_value (float):The measured value returned from the DMM.

                Note:
                If an overrange condition occurs, the **Measurement_Value** contains
                an IEEE-defined NaN (Not a Number) value.

        Returns:
            is_over_range (bool):Returns whether the measurement value is a valid measurement or an
                overrange condition.

                +----------+---+-----------------------------------------------------------+
                | VI_TRUE  | 1 | The value indicates that an overrange condition occurred. |
                +----------+---+-----------------------------------------------------------+
                | VI_FALSE | 0 | The value is a valid measurement.                         |
                +----------+---+-----------------------------------------------------------+
        '''
        is_over_range_ctype = ctypes_types.ViBoolean_ctype(0)
        error_code = self.library.niDMM_IsOverRange(self.vi, measurement_value, ctypes.pointer(is_over_range_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return python_types.ViBoolean(is_over_range_ctype.value)

    def is_under_range(self, measurement_value):
        '''is_under_range

        Takes a **Measurement_Value** and determines if the value is a valid
        measurement or a value indicating that an underrange condition occurred.

        Args:
            measurement_value (float):The measured value returned from the DMM.

                Note:
                If an overrange condition occurs, the **Measurement_Value** contains
                an IEEE-defined NaN (Not a Number) value.

        Returns:
            is_under_range (bool):Returns whether the **Measurement_Value** is a valid measurement or an
                underrange condition.

                +----------+---+------------------------------------------------------------+
                | VI_TRUE  | 1 | The value indicates that an underrange condition occurred. |
                +----------+---+------------------------------------------------------------+
                | VI_FALSE | 0 | The value is a valid measurement.                          |
                +----------+---+------------------------------------------------------------+
        '''
        is_under_range_ctype = ctypes_types.ViBoolean_ctype(0)
        error_code = self.library.niDMM_IsUnderRange(self.vi, measurement_value, ctypes.pointer(is_under_range_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return python_types.ViBoolean(is_under_range_ctype.value)

    def perform_open_cable_comp(self):
        '''perform_open_cable_comp

        For the NI 4082 and NI 4072 only, performs the open cable compensation
        measurements for the current capacitance/inductance range, and returns
        open cable compensation **Conductance** and **Susceptance** values. You
        can use the return values of this function as inputs to
        configure_open_cable_comp_values.

        This function returns an error if the value of the function
        attribute is not set to NIDMM_VAL_CAPACITANCE (1005) or
        NIDMM_VAL_INDUCTANCE (1006).

        Returns:
            conductance (float):**conductance** is the measured value of open cable compensation
                **conductance**.
            susceptance (float):**susceptance** is the measured value of open cable compensation
                **susceptance**.
        '''
        conductance_ctype = ctypes_types.ViReal64_ctype(0)
        susceptance_ctype = ctypes_types.ViReal64_ctype(0)
        error_code = self.library.niDMM_PerformOpenCableComp(self.vi, ctypes.pointer(conductance_ctype), ctypes.pointer(susceptance_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return python_types.ViReal64(conductance_ctype.value), python_types.ViReal64(susceptance_ctype.value)

    def perform_short_cable_comp(self):
        '''perform_short_cable_comp

        Performs the short cable compensation measurements for the current
        capacitance/inductance range, and returns short cable compensation
        **Resistance** and **Reactance** values. You can use the return values
        of this function as inputs to configure_short_cable_comp_values.

        This function returns an error if the value of the function
        attribute is not set to NIDMM_VAL_CAPACITANCE (1005) or
        NIDMM_VAL_INDUCTANCE (1006).

        Returns:
            resistance (float):**resistance** is the measured value of short cable compensation
                **resistance**.
            reactance (float):**reactance** is the measured value of short cable compensation
                **reactance**.
        '''
        resistance_ctype = ctypes_types.ViReal64_ctype(0)
        reactance_ctype = ctypes_types.ViReal64_ctype(0)
        error_code = self.library.niDMM_PerformShortCableComp(self.vi, ctypes.pointer(resistance_ctype), ctypes.pointer(reactance_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return python_types.ViReal64(resistance_ctype.value), python_types.ViReal64(reactance_ctype.value)

    def read(self, maximum_time):
        '''read

        Acquires a single measurement and returns the measured value.

        Args:
            maximum_time (int):Specifies the **maximum_time** allowed for this function to complete in
                milliseconds. If the function does not complete within this time
                interval, the function returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                NIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout
                automatically.

        Returns:
            reading (float):The measured value returned from the DMM.
        '''
        reading_ctype = ctypes_types.ViReal64_ctype(0)
        error_code = self.library.niDMM_Read(self.vi, maximum_time, ctypes.pointer(reading_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return python_types.ViReal64(reading_ctype.value)

    def read_multi_point(self, maximum_time, array_size):
        '''read_multi_point

        Acquires multiple measurements and returns an array of measured values.
        The number of measurements the DMM makes is determined by the values you
        specify for the **Trigger_Count** and **Sample_Count** parameters in
        configure_multi_point.

        Args:
            maximum_time (int):Specifies the **maximum_time** allowed for this function to complete in
                milliseconds. If the function does not complete within this time
                interval, the function returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                NIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout
                automatically.
            array_size (int):Specifies the number of measurements to acquire. The maximum number of
                measurements for a finite acquisition is the (**Trigger Count** x
                **Sample Count**) parameters in configure_multi_point.

                For continuous acquisitions, up to 100,000 points can be returned at
                once. The number of measurements can be a subset. The valid range is any
                positive ViInt32. The default value is 1.

        Returns:
            reading_array (float):An array of measurement values.

                Note:
                The size of the **Reading_Array** must be at least the size that you
                specify for the **Array_Size** parameter.
            actual_number_of_points (int):Indicates the number of measured values actually retrieved from the DMM.
        '''
        reading_array_ctype = (ctypes_types.ViReal64_ctype * array_size)()
        actual_number_of_points_ctype = ctypes_types.ViInt32_ctype(0)
        error_code = self.library.niDMM_ReadMultiPoint(self.vi, maximum_time, array_size, ctypes.cast(reading_array_ctype, ctypes.POINTER(ctypes_types.ViReal64_ctype)), ctypes.pointer(actual_number_of_points_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [python_types.ViReal64(reading_array_ctype[i].value) for i in range(array_size)], python_types.ViInt32(actual_number_of_points_ctype.value)

    def read_status(self):
        '''read_status

        Returns measurement backlog and acquisition status. Use this function to
        determine how many measurements are available before calling
        fetch, fetch_multi_point, or fetch_waveform.

        Note: The NI 4050 is not supported.

        Returns:
            acquisition_backlog (int):The number of measurements available to be read. If the backlog
                continues to increase, data is eventually overwritten, resulting in an
                error.

                Note:
                On the NI 4060, the **Backlog** does not increase when autoranging. On
                the NI 4065, the **Backlog** does not increase when Range is set to AUTO
                RANGE ON (-1), or before the first point is fetched when Range is set to
                AUTO RANGE ONCE (-3). These behaviors are due to the autorange model of
                the devices.
            acquisition_status (enums.AcquisitionStatus):Indicates status of the acquisition. The following table shows the
                acquisition states:

                +---+----------------------------+
                | 0 | Running                    |
                +---+----------------------------+
                | 1 | Finished with backlog      |
                +---+----------------------------+
                | 2 | Finished with no backlog   |
                +---+----------------------------+
                | 3 | Paused                     |
                +---+----------------------------+
                | 4 | No acquisition in progress |
                +---+----------------------------+
        '''
        acquisition_backlog_ctype = ctypes_types.ViInt32_ctype(0)
        acquisition_status_ctype = ctypes_types.ViInt16_ctype(0)
        error_code = self.library.niDMM_ReadStatus(self.vi, ctypes.pointer(acquisition_backlog_ctype), ctypes.pointer(acquisition_status_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return python_types.ViInt32(acquisition_backlog_ctype.value), enums.AcquisitionStatus(acquisition_status_ctype.value)

    def read_waveform(self, maximum_time, array_size):
        '''read_waveform

        For the NI 4080/4081/4082 and the NI 4070/4071/4072, acquires a waveform
        and returns data as an array of values or as a waveform data type. The
        number of elements in the **Waveform_Array** is determined by the
        values you specify for the **Waveform_Points** parameter in
        configure_waveform_acquisition.

        Args:
            maximum_time (int):Specifies the **maximum_time** allowed for this function to complete in
                milliseconds. If the function does not complete within this time
                interval, the function returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                NIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout
                automatically.
            array_size (int):Specifies the number of waveform points to return. You specify the total
                number of points that the DMM acquires in the **Waveform Points**
                parameter of configure_waveform_acquisition. The default value is
                1.

        Returns:
            waveform_array (float):An array of measurement values.

                Note:
                The size of the **Waveform_Array** must be at least the size that you
                specify for the **Array_Size** parameter.
            actual_number_of_points (int):Indicates the number of measured values actually retrieved from the DMM.
        '''
        waveform_array_ctype = (ctypes_types.ViReal64_ctype * array_size)()
        actual_number_of_points_ctype = ctypes_types.ViInt32_ctype(0)
        error_code = self.library.niDMM_ReadWaveform(self.vi, maximum_time, array_size, ctypes.cast(waveform_array_ctype, ctypes.POINTER(ctypes_types.ViReal64_ctype)), ctypes.pointer(actual_number_of_points_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [python_types.ViReal64(waveform_array_ctype[i].value) for i in range(array_size)], python_types.ViInt32(actual_number_of_points_ctype.value)

    def reset_interchange_check(self):
        '''reset_interchange_check

        When developing a complex test system that consists of multiple test
        modules, it is generally a good idea to design the test modules so that
        they can run in any order. To do so requires ensuring that each test
        module completely configures the state of each instrument it uses.

        If a particular test module does not completely configure the state of
        an instrument, the state of the instrument depends on the configuration
        from a previously executed test module. If you execute the test modules
        in a different order, the behavior of the instrument and therefore the
        entire test module is likely to change. This change in behavior is
        generally instrument specific and represents an interchangeability
        problem. You can use this function to test for such cases. After you
        call this function, the interchangeability checking algorithms in NI-DMM
        ignore all previous configuration operations. By calling this function
        at the beginning of a test module, you can determine whether the test
        module has dependencies on the operation of previously executed test
        modules.

        This function does not clear the interchangeability warnings from the
        list of previously recorded interchangeability warnings. If you want to
        guarantee that get_next_interchange_warning only returns those
        interchangeability warnings that are generated after calling this
        function, you must clear the list of interchangeability warnings. You
        can clear the interchangeability warnings list by repeatedly calling
        get_next_interchange_warning until no more interchangeability
        warnings are returned. If you are not interested in the content of those
        warnings, you can call clear_interchange_warnings.
        '''
        error_code = self.library.niDMM_ResetInterchangeCheck(self.vi)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def reset_with_defaults(self):
        '''reset_with_defaults

        Resets the instrument to a known state and sends initialization commands
        to the DMM. The initialization commands set the DMM settings to the
        state necessary for the operation of NI-DMM. All user-defined default
        values associated with a logical name are applied after setting the DMM.
        '''
        error_code = self.library.niDMM_ResetWithDefaults(self.vi)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def self_cal(self):
        '''self_cal

        For the NI 4080/4081/4082 and the NI 4070/4071/4072, executes the
        self-calibration routine to maintain measurement accuracy.

        Note:
        This function calls reset, and any configurations previous to
        the call will be lost. All attributes will be set to their default
        values after the call returns.
        '''
        error_code = self.library.niDMM_SelfCal(self.vi)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def send_software_trigger(self):
        '''send_software_trigger

        Sends a command to trigger the DMM. Call this function if you have
        configured either the TRIGGER_SOURCE or
        SAMPLE_TRIGGER attributes. If the
        TRIGGER_SOURCE and/or SAMPLE_TRIGGER
        attributes are set to NIDMM_VAL_EXTERNAL or NIDMM_VAL_TTL\ *n*, you
        can use this function to override the trigger source that you configured
        and trigger the device. The NI 4050 and NI 4060 are not supported.
        '''
        error_code = self.library.niDMM_SendSoftwareTrigger(self.vi)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_boolean(self, channel_name, attribute_id, attribute_value):
        '''_set_attribute_vi_boolean

        This function sets the value of a ViBoolean attribute.

        This is a low-level function that you can use to set the values of
        instrument-specific attributes and inherent IVI attributes.

        If the attribute represents an instrument state, this function performs
        instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular attribute.
        -  State caching is enabled, and the currently cached value is invalid
           or is different than the value you specify.

        This instrument driver contains high-level functions that set most of
        the instrument attributes. It is best to use the high-level driver
        functions as much as possible. They handle order dependencies and
        multithread locking for you. In addition, they perform status checking
        only after setting all of the attributes.

        In contrast, when you set multiple attributes using the SetAttribute
        functions, the functions check the instrument status after each call.
        Also, when state caching is enabled, the high-level functions that
        configure multiple attributes perform instrument I/O only for the
        attributes whose value you change. Thus, you can safely call the
        high-level functions without the penalty of redundant instrument I/O.

        Args:
            channel_name (str):This parameter is ignored. National Instruments DMMs do not support
                channel names since they only have a single channel. This parameter is
                included in order to support interchangeability and upgradability to
                multiple channel DMMs.

                The default value is " " (an empty string).
            attribute_id (int):Pass the ID of an attribute.
            attribute_value (bool):Pass the value that you want to set the attribute to.
        '''
        error_code = self.library.niDMM_SetAttributeViBoolean(self.vi, channel_name.encode('ascii'), attribute_id, attribute_value)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_int32(self, channel_name, attribute_id, attribute_value):
        '''_set_attribute_vi_int32

        This function sets the value of a ViInt32 attribute.

        This is a low-level function that you can use to set the values of
        instrument-specific attributes and inherent IVI attributes.

        If the attribute represents an instrument state, this function performs
        instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular attribute.
        -  State caching is enabled, and the currently cached value is invalid
           or is different than the value you specify.

        This instrument driver contains high-level functions that set most of
        the instrument attributes. It is best to use the high-level driver
        functions as much as possible. They handle order dependencies and
        multithread locking for you. In addition, they perform status checking
        only after setting all of the attributes.

        In contrast, when you set multiple attributes using the SetAttribute
        functions, the functions check the instrument status after each call.
        Also, when state caching is enabled, the high-level functions that
        configure multiple attributes perform instrument I/O only for the
        attributes whose value you change. Thus, you can safely call the
        high-level functions without the penalty of redundant instrument I/O.

        Args:
            channel_name (str):This parameter is ignored. National Instruments DMMs do not support
                channel names since they only have a single channel. This parameter is
                included in order to support interchangeability and upgradability to
                multiple channel DMMs.

                The default value is " " (an empty string).
            attribute_id (int):Pass the ID of an attribute.
            attribute_value (int):Pass the value that you want to set the attribute to.
        '''
        error_code = self.library.niDMM_SetAttributeViInt32(self.vi, channel_name.encode('ascii'), attribute_id, attribute_value)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_real64(self, channel_name, attribute_id, attribute_value):
        '''_set_attribute_vi_real64

        This function sets the value of a ViReal64 attribute.

        This is a low-level function that you can use to set the values of
        instrument-specific attributes and inherent IVI attributes.

        If the attribute represents an instrument state, this function performs
        instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular attribute.
        -  State caching is enabled, and the currently cached value is invalid
           or is different than the value you specify.

        This instrument driver contains high-level functions that set most of
        the instrument attributes. It is best to use the high-level driver
        functions as much as possible. They handle order dependencies and
        multithread locking for you. In addition, they perform status checking
        only after setting all of the attributes.

        In contrast, when you set multiple attributes using the SetAttribute
        functions, the functions check the instrument status after each call.
        Also, when state caching is enabled, the high-level functions that
        configure multiple attributes perform instrument I/O only for the
        attributes whose value you change. Thus, you can safely call the
        high-level functions without the penalty of redundant instrument I/O.

        Args:
            channel_name (str):This parameter is ignored. National Instruments DMMs do not support
                channel names since they only have a single channel. This parameter is
                included in order to support interchangeability and upgradability to
                multiple channel DMMs.

                The default value is " " (an empty string).
            attribute_id (int):Pass the ID of an attribute.
            attribute_value (float):Pass the value that you want to set the attribute to.
        '''
        error_code = self.library.niDMM_SetAttributeViReal64(self.vi, channel_name.encode('ascii'), attribute_id, attribute_value)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_string(self, channel_name, attribute_id, attribute_value):
        '''_set_attribute_vi_string

        This function sets the value of a ViString attribute.

        This is a low-level function that you can use to set the values of
        instrument-specific attributes and inherent IVI attributes.

        If the attribute represents an instrument state, this function performs
        instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular attribute.
        -  State caching is enabled, and the currently cached value is invalid
           or is different than the value you specify.

        This instrument driver contains high-level functions that set most of
        the instrument attributes. It is best to use the high-level driver
        functions as much as possible. They handle order dependencies and
        multithread locking for you. In addition, they perform status checking
        only after setting all of the attributes.

        In contrast, when you set multiple attributes using the SetAttribute
        functions, the functions check the instrument status after each call.
        Also, when state caching is enabled, the high-level functions that
        configure multiple attributes perform instrument I/O only for the
        attributes whose value you change. Thus, you can safely call the
        high-level functions without the penalty of redundant instrument I/O.

        Args:
            channel_name (str):This parameter is ignored. National Instruments DMMs do not support
                channel names since they only have a single channel. This parameter is
                included in order to support interchangeability and upgradability to
                multiple channel DMMs.

                The default value is " " (an empty string).
            attribute_id (int):Pass the ID of an attribute.
            attribute_value (str):Pass the value that you want to set the attribute to.
        '''
        error_code = self.library.niDMM_SetAttributeViString(self.vi, channel_name.encode('ascii'), attribute_id, attribute_value.encode('ascii'))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _close(self):
        '''_close

        Closes the specified session and deallocates resources that it reserved.
        '''
        error_code = self.library.niDMM_close(self.vi)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def error_query(self):
        '''error_query

        Reads an **Error_Code** and message from the DMM error queue. National
        Instruments DMMs do not contain an error queue. Errors are reported as
        they occur. Therefore, this function does not detect errors; it is
        included for compliance with the *IviDmm Class Specification*.

        Returns:
            error_code (int):The **error_code** returned from the instrument.

                The default value is VI_SUCCESS (0).
            error_message (int):Formats the **Error_Code** into a user-readable message string.

                Note: The array must contain at least 256 elements ViChar[256].
        '''
        error_code_ctype = ctypes_types.ViStatus_ctype(0)
        error_message_ctype = ctypes_types.ViChar_ctype(0)
        error_code = self.library.niDMM_error_query(self.vi, ctypes.pointer(error_code_ctype), ctypes.pointer(error_message_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return python_types.ViStatus(error_code_ctype.value), python_types.ViChar(error_message_ctype.value)

    def reset(self):
        '''reset

        Resets the instrument to a known state and sends initialization commands
        to the instrument. The initialization commands set instrument settings
        to the state necessary for the operation of the instrument driver.
        '''
        error_code = self.library.niDMM_reset(self.vi)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def revision_query(self):
        '''revision_query

        Returns the revision numbers of the instrument driver and instrument
        firmware.

        Returns:
            instrument_driver_revision (int):Returns a string containing the instrument driver software revision
                numbers.

                Note: The array must contain at least 256 elements ViChar[256].
            firmware_revision (int):Returns a string containing the instrument **firmware_revision**
                numbers.

                Note: The array must contain at least 256 elements ViChar[256].
        '''
        instrument_driver_revision_ctype = ctypes_types.ViChar_ctype(0)
        firmware_revision_ctype = ctypes_types.ViChar_ctype(0)
        error_code = self.library.niDMM_revision_query(self.vi, ctypes.pointer(instrument_driver_revision_ctype), ctypes.pointer(firmware_revision_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return python_types.ViChar(instrument_driver_revision_ctype.value), python_types.ViChar(firmware_revision_ctype.value)

    def self_test(self):
        '''self_test

        Performs a self-test on the DMM to ensure that the DMM is functioning
        properly. Self-test does not calibrate the DMM.

        Note:
        This function calls reset, and any configurations previous to
        the call will be lost. All attributes will be set to their default
        values after the call returns.

        Returns:
            self_test_result (int):Contains the value returned from the instrument self-test. Zero
                indicates success.

                On the NI 4080/4082 and NI 4070/4072, the error code 1013 indicates that
                you should check the fuse and replace it, if necessary.

                Note:
                Self-test does not check the fuse on the NI 4065, NI 4071, and
                NI 4081. Hence, even if the fuse is blown on the device, self-test does
                not return error code 1013.
            self_test_message (int):This parameter contains the string returned from the instrument
                self-test. The array must contain at least 256 elements.

                For the NI 4050 and NI 4060, the error codes returned for self-test
                failures include the following:

                -  NIDMM_ERROR_AC_TEST_FAILURE
                -  NIDMM_ERROR_DC_TEST_FAILURE
                -  NIDMM_ERROR_RESISTANCE_TEST_FAILURE

                These error codes indicate that the DMM should be repaired.

                For the NI 4080/4081/4082 and the NI 4070/4071/4072, the error code
                returned for a self-test failure is NIDMM_ERROR_SELF_TEST_FAILURE.
                This error code indicates that the DMM should be repaired.
        '''
        self_test_result_ctype = ctypes_types.ViInt16_ctype(0)
        self_test_message_ctype = (ctypes_types.ViChar_ctype * 256)()
        error_code = self.library.niDMM_self_test(self.vi, ctypes.pointer(self_test_result_ctype), ctypes.cast(self_test_message_ctype, ctypes.POINTER(ctypes_types.ViChar_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return python_types.ViInt16(self_test_result_ctype.value), self_test_message_ctype.value.decode("ascii")


class _RepeatedCapability(_SessionBase):
    '''Allows for setting/getting properties and calling methods for specific repeated capabilities (such as channels) on your session.'''

    def __init__(self, vi, repeated_capability):
        super(_RepeatedCapability, self).__init__(repeated_capability)
        self.vi = vi
        self._is_frozen = True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass


class Session(_SessionBase):
    '''An NI-DMM session to a National Instruments Digital Multimeter'''

    def __init__(self, resource_name, id_query=False, reset_device=False, option_string=''):
        super(Session, self).__init__(repeated_capability='')
        # TODO(marcoskirsch): private members should start with _
        self.vi = 0  # This must be set before calling _init_with_options.
        self.vi = self._init_with_options(resource_name, id_query, reset_device, option_string)
        self._is_frozen = True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def __getitem__(self, repeated_capability):
        '''Set/get properties or call methods with a repeated capability (i.e. channels)'''
        return _RepeatedCapability(self.vi, repeated_capability)

    def initiate(self):
        return _Acquisition(self)

    def close(self):
        try:
            self._close()
        except errors.Error:
            # TODO(marcoskirsch): This will occur when session is "stolen". Change to log instead
            print("Failed to close session.")
        self.vi = 0


