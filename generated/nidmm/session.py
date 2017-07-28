# This file was generated
import ctypes

from nidmm import ctypes_types
from nidmm import enums
from nidmm import errors
from nidmm import library


class AttributeViInt32(object):

    def __init__(self, attribute_id):
        self.attribute_id = attribute_id
        self.channel = ''

    def __get__(self, obj, objtype):
        assert objtype is Session
        return obj._get_attribute_vi_int32(self.channel, self.attribute_id)

    def __set__(self, obj, value):
        obj._set_attribute_vi_int32(self.channel, self.attribute_id, value)


class AttributeViReal64(object):

    def __init__(self, attribute_id):
        self.attribute_id = attribute_id
        self.channel = ''

    def __get__(self, obj, objtype):
        assert objtype is Session
        return obj._get_attribute_vi_real64(self.channel, self.attribute_id)

    def __set__(self, obj, value):
        obj._set_attribute_vi_real64(self.channel, self.attribute_id, value)


class AttributeViString(object):

    def __init__(self, attribute_id):
        self.attribute_id = attribute_id
        self.channel = ''

    def __get__(self, obj, objtype):
        assert objtype is Session
        return obj._get_attribute_vi_string(self.channel, self.attribute_id)

    def __set__(self, obj, value):
        obj._set_attribute_vi_string(self.channel, self.attribute_id, value)


class AttributeViBoolean(object):

    def __init__(self, attribute_id):
        self.attribute_id = attribute_id
        self.channel = ''

    def __get__(self, obj, objtype):
        assert objtype is Session
        return obj._get_attribute_vi_boolean(self.channel, self.attribute_id) is not 0

    def __set__(self, obj, value):
        obj._set_attribute_vi_boolean(self.channel, self.attribute_id, (value is not 0))


class AttributeEnum(object):

    def __init__(self, attribute_id, enum_meta_class):
        self.attribute_id = attribute_id
        self.attribute_type = enum_meta_class
        self.channel = ''

    def __get__(self, obj, objtype):
        assert objtype is Session
        return self.attribute_type(obj._get_attribute_vi_int32(self.channel, self.attribute_id))

    def __set__(self, obj, value):
        if type(value) is not self.attribute_type:
            raise TypeError('Value mode must be of type ' + str(self.attribute_type))
        obj._set_attribute_vi_int32(self.channel, self.attribute_id, value.value)


class Acquisition(object):
    def __init__(self, session):
        self.session = session

    def __enter__(self):
        self.session._initiate()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.session._abort()


class Session(object):
    '''An NI-DMM session to a National Instruments Digital Multimeter'''

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

    absolute_resolution = AttributeViReal64(1250008)
    '''
    Specifies the measurement resolution in absolute units. Setting this
    property to higher values increases the measurement accuracy. Setting
    this property to lower values increases the measurement speed.
    '''
    adc_calibration = AttributeEnum(1150022, enums.ADCCalibration)
    '''
    For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the ADC
    calibration mode.
    '''
    aperture_time = AttributeViReal64(1250321)
    '''
    Specifies the measurement aperture time for the current configuration.
    Aperture time is specified in units set by the Aperture Time Units
    property. To override the default aperture, set this property to the
    desired aperture time after calling niDMM Config Measurement . To return
    to the default, set this property to Aperture Time Auto (-1).
    '''
    aperture_time_units = AttributeEnum(1250322, enums.ApertureTimeUnits)
    '''
    Specifies the units of aperture time for the current configuration.
    '''
    auto_range_value = AttributeViReal64(1250331)
    '''
    Specifies the value of the range. If auto ranging is enabled, shows the
    actual value of the active range. The value of this property is set
    during a read operation.
    '''
    auto_zero = AttributeEnum(1250332, enums.AutoZero)
    '''
    Specifies the AutoZero mode. This property is not supported for the NI
    4050.
    '''
    buffer_size = AttributeViInt32(1150037)
    '''
    Specifies the size in samples of the internal data buffer. Maximum size
    is 134,217,727 (0X7FFFFFF) samples. When set to Auto (-1), NI-DMM
    chooses the buffer size.
    '''
    cable_compensation_type = AttributeEnum(1150045, enums.CableCompensationType)
    '''
    For the NI 4081 and NI 4072 only, specifies the type of cable
    compensation that is applied to the current capacitance or inductance
    measurement for the current range.
    '''
    cache = AttributeViBoolean(1050004)
    '''
    Specifies whether to cache the value of properties. When caching is
    enabled, the instrument driver keeps track of the current instrument
    settings and avoids sending redundant commands to the instrument. Thus,
    it significantly increases execution speed. The instrument driver can
    choose to always cache or to never cache particular properties
    regardless of the setting of this property. The default value is TRUE
    (1). Use niDMM Initialize With Options to override the default setting.
    '''
    channel_count = AttributeViInt32(1050203)
    '''
    Indicates the number of channels that the specific instrument driver
    supports. For each property for which the IVI\_VAL\_MULTI\_CHANNEL flag
    property is set, the IVI engine maintains a separate cache value for
    each channel.
    '''
    conductance = AttributeViReal64(1150049)
    '''
    For the NI 4082 and NI 4072 only, specifies the active part
    (conductance) of the open cable compensation. The valid range is any
    real number >0. The default value (-1.0) indicates that compensation has
    not taken place.
    '''
    current_source = AttributeEnum(1150025, enums.CurrentSource)
    '''
    Specifies the current source provided during diode measurements.

    The NI 4050 and NI 4060 are not supported.
    '''
    dc_bias = AttributeEnum(1150053, enums.DCBias)
    '''
    For the NI 4082 and NI 4072 only, controls the available DC bias for
    capacitance measurements.
    '''
    dc_noise_rejection = AttributeEnum(1150026, enums.DCNoiseRejection)
    '''
    Specifies the DC noise rejection mode.
    '''
    digits_resolution = AttributeEnum(1250003, enums.DigitsResolution)
    '''
    Specifies the measurement resolution in digits. Setting this property to
    higher values increases the measurement accuracy. Setting this property
    to lower values increases the measurement speed.
    '''
    driver_setup = AttributeViString(1050007)
    '''
    This property indicates the Driver Setup string that the user specified
    when initializing the driver. Some cases exist where the end-user must
    specify instrument driver options at initialization time. An example of
    this is specifying a particular instrument model from among a family of
    instruments that the driver supports. This is useful when using
    simulation. The end-user can specify driver-specific options through the
    Driver Setup keyword in the Option String parameter in niDMM Initialize
    With Options . If the user does not specify a Driver Setup string, this
    property returns an empty string.
    '''
    engine_major_version = AttributeViInt32(1050501)
    '''
    The major version number of the IVI engine.
    '''
    engine_minor_version = AttributeViInt32(1050502)
    '''
    The minor version number of the IVI engine.
    '''
    engine_revision = AttributeViString(1050553)
    '''
    A string that contains additional version information about the IVI
    engine.
    '''
    error_elaboration = AttributeViString(1050103)
    '''
    An optional string that contains additional information concerning the
    primary error condition.
    '''
    frequency_voltage_auto_range_value = AttributeViReal64(1150044)
    '''
    For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the value of
    the frequency voltage range. If auto ranging is enabled, shows the
    actual value of the active frequency voltage range. If not Auto Ranging,
    the value is the same as that of the Frequency Voltage Range property.
    '''
    frequency_voltage_range = AttributeViReal64(1250101)
    '''
    For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the maximum
    amplitude of the input signal for frequency measurements.
    '''
    function = AttributeEnum(1250001, enums.Function)
    '''
    Specifies the measurement function. If you are setting this property
    directly, you must also set the Operation Mode property, which controls
    whether the DMM takes standard single or multipoint measurements, or
    acquires a waveform. If you are programming properties directly, you
    must set the Operation Mode property before setting other configuration
    properties. If the Operation Mode property is set to Waveform Mode, the
    only valid function types are Waveform Voltage and Waveform Current. Set
    the Operation Mode property to IVIDMM Mode to set all other function
    values.
    '''
    group_capabilities = AttributeViString(1050401)
    '''
    A string containing the capabilities and extension groups supported by
    the specific driver.
    '''
    idquery_response = AttributeViString(1150001)
    '''
    A string containing the type of instrument used in the current session.
    '''
    input_resistance = AttributeEnum(1150029, enums.InputResistance)
    '''
    Specifies the input resistance of the instrument.
    '''
    instrument_firmware_revision = AttributeViString(1050510)
    '''
    A string containing the instrument firmware revision number.
    '''
    instrument_manufacturer = AttributeViString(1050511)
    '''
    A string containing the manufacturer of the instrument.
    '''
    instrument_model = AttributeViString(1050512)
    '''
    A string containing the instrument model.
    '''
    instrument_product_id = AttributeViInt32(1150061)
    '''
    The PCI product ID.
    '''
    instrument_serial_number = AttributeViString(1150054)
    '''
    A string containing the serial number of the instrument. This property
    corresponds to the serial number label that is attached to most
    products.
    '''
    interchange_check = AttributeViBoolean(1050021)
    '''
    Specifies whether to perform interchangeability checking and log
    interchangeability warnings when you call niDMM VIs. Interchangeability
    warnings indicate that using your application with a different
    instrument might cause different behavior. Use niDMM Get Next
    Interchange Warning to extract interchange warnings. Use niDMM Clear
    Interchange Warnings to clear the list of interchangeability warnings
    without reading them. Interchangeability checking examines the
    properties in a capability group only if you specify a value for at
    least one property within that group. Interchangeability warnings can
    occur when a property affects the behavior of the instrument and you
    have not set that property, or the property has been invalidated since
    you set it.
    '''
    io_resource_descriptor = AttributeViString(1050304)
    '''
    A string containing the resource descriptor of the instrument.
    '''
    latency = AttributeViInt32(1150034)
    '''
    Specifies the number of measurements transferred at a time from the
    instrument to an internal buffer. When set to Auto (-1), NI-DMM chooses
    the transfer size.
    '''
    lc_calculation_model = AttributeEnum(1150052, enums.LCCalculationModel)
    '''
    For the NI 4082 and NI 4072 only, specifies the type of algorithm that
    the measurement processing uses for capacitance and inductance
    measurements.
    '''
    logical_name = AttributeViString(1050305)
    '''
    A string containing the logical name of the instrument.
    '''
    max_frequency = AttributeViReal64(1250007)
    '''
    Specifies the maximum frequency component of the input signal for AC
    measurements. This property is used only for error checking and verifies
    that the value of this parameter is less than the maximum frequency of
    the device. This property affects the DMM only when you set the Function
    property to AC measurements.
    '''
    measurement_completdest = AttributeEnum(1250305, enums.MeasurementCompleteDest)
    '''
    Specifies the destination of the measurement complete (MC) signal.

    To determine which values are supported by each device, refer to the
    LabVIEW Trigger Routing section in the *NI Digital Multimeters Help*.
    '''
    measurement_destination_slope = AttributeEnum(1150002, enums.MeasurementDestinationSlope)
    '''
    Specifies the polarity of the generated measurement complete signal.
    '''
    min_frequency = AttributeViReal64(1250006)
    '''
    Specifies the minimum frequency component of the input signal for AC
    measurements. This property affects the DMM only when you set the
    Function property to AC measurements. The valid range is 1 Hz-300 kHz
    for the NI 4080/4081/4082 and NI 4070/4071/4072, 10 Hz-100 Hz for the NI
    4065, and 20 Hz-25 kHz for the NI 4050 and NI 4060.
    '''
    number_of_averages = AttributeViInt32(1150032)
    '''
    Specifies the number of averages to perform in a measurement. For the NI
    4080/4081/4082 and NI 4070/4071/4072, applies only when the aperture
    time is not set to Auto and Auto Zero is ON. The Number of Averages
    Property will be ignored otherwise. The default is 4 for 7 1/2 digits;
    otherwise, the default is 1.

    The NI 4050 and NI 4060 are not supported.
    '''
    number_of_lc_measurements_to_average = AttributeViInt32(1150055)
    '''
    For the NI 4082 and NI 4072 only, specifies the number of LC
    measurements that are averaged to produce one reading.
    '''
    offset_compensated_ohms = AttributeEnum(1150023, enums.OffsetCompensatedOhms)
    '''
    For the NI 4080/4081/4082 and NI 4070/4071/4072, enables or disables
    offset compensated ohms.
    '''
    operation_mode = AttributeEnum(1150014, enums.OperationMode)
    '''
    Specifies how the DMM acquires data.

    .. note::
       The NI 4050 and NI 4060 are not supported.

    When you call niDMM Config Measurement , NI-DMM sets this property to
    IVIDMM Mode. When you call niDMM Configure Waveform Acquisition , NI-DMM
    sets this property to Waveform Mode. If you are programming properties
    directly, you must set this property before setting other configuration
    properties.
    '''
    powerline_frequency = AttributeEnum(1250333, enums.PowerlineFrequency)
    '''
    Specifies the powerline frequency. The NI 4060 and NI 4050 use this
    value to select an aperture time to reject powerline noise by selecting
    the appropriate internal sample clock and filter. The NI 4065, NI
    4070/4071/4072, and NI 4080/4081/4082 use this value to select timebases
    for setting the Aperture Time property in powerline cycles.
    '''
    primary_error = AttributeViInt32(1050101)
    '''
    A code that describes the first error that occurred since the last call
    to niDMM Get Error for the session. The value follows the VXIplug&play
    conventions. A negative value describes an error condition. A positive
    value describes a warning condition. A zero indicates that no error or
    warning occurred. The error and warning values can be status codes
    defined by IVI, VISA, class drivers, or specific drivers.
    '''
    query_instrument_status = AttributeViBoolean(1050003)
    '''
    Specifies whether the instrument driver queries the instrument status
    after each operation. Querying the instrument status is very useful for
    debugging. After the user program is validated, this property can be set
    to FALSE (0) to disable status checking and maximize performance. The
    instrument driver can choose to ignore status checking for particular
    properties regardless of the setting of this property. The default value
    is TRUE (1). Use niDMM Initialize With Options to override the default
    setting.
    '''
    range = AttributeViReal64(1250002)
    '''
    Specifies the measurement range. Use positive values to represent the
    absolute value of the maximum expected measurement. The value is in
    units appropriate for the current value of the Function property. For
    example, if the Function property is set to DC Volts, the units are
    volts.
    '''
    range_check = AttributeViBoolean(1050002)
    '''
    Specifies whether to validate property values and VI parameters. If
    enabled, the instrument driver validates the parameter values passed to
    driver VIs. Range checking parameters is very useful for debugging.
    After the user program is validated, you can set this property to FALSE
    (0) to disable range checking and maximize performance. The default
    value is TRUE (1). Use niDMM Initialize With Options to override the
    default setting.
    '''
    reactance = AttributeViReal64(1150046)
    '''
    For the NI 4082 and NI 4072 only, represents the reactive part
    (reactance) of the short cable compensation. The valid range is any real
    number >0. The default value (-1) indicates that compensation has not
    taken place.
    '''
    record_value_coercions = AttributeViBoolean(1050006)
    '''
    Specifies whether the IVI engine keeps a list of the value coercions it
    makes for ViInt32 and ViReal64 properties. The default value is FALSE
    (0). Use niDMM Initialize With Options to override the default setting.
    Use niDMM Get Next Coercion Record to extract and delete the oldest
    coercion record from the list.
    '''
    resistance = AttributeViReal64(1150047)
    '''
    For the NI 4082 and NI 4072 only, represents the active part
    (resistance) of the short cable compensation. The valid range is any
    real number >0. The default value (-1) indicates that compensation has
    not taken place.
    '''
    rtd_a = AttributeViReal64(1150121)
    '''
    Specifies the Callendar-Van Dusen A coefficient for RTD scaling when the
    **RTD Type property** is set to Custom.
    '''
    rtd_b = AttributeViReal64(1150122)
    '''
    Specifies the Callendar-Van Dusen B coefficient for RTD scaling when the
    **RTD Type property** is set to Custom.
    '''
    rtd_c = AttributeViReal64(1150123)
    '''
    Specifies the Callendar-Van Dusen C coefficient for RTD scaling when the
    **RTD Type property** is set to Custom.
    '''
    rtd_resistance = AttributeViReal64(1250242)
    '''
    Specifies the RTD resistance at 0 degrees Celsius.
    '''
    rtd_type = AttributeEnum(1150120, enums.RTDType)
    '''
    Specifies the RTD type.
    '''
    sample_count = AttributeViInt32(1250301)
    '''
    Specifies the number of measurements the DMM takes each time it receives
    a trigger in a multiple point acquisition. Setting Sample Count to 0 on
    the NI 4050 and NI 4060 causes the device to take continuous
    measurements. Otherwise, setting Sample Count to 0 causes the
    conditional statement "Measurements equal to Sample Count" to always
    evaluate to False, and causes the DMM to continue taking measurements in
    the inner loop.
    '''
    sample_delay_mode = AttributeViInt32(1150031)
    '''
    For the NI 4060 only, specifies a delay interval after a sample trigger.
    '''
    sample_interval = AttributeViReal64(1250303)
    '''
    Specifies the amount of time in seconds the DMM waits between
    measurement cycles. This property only applies when the Sample Trigger
    property is set to INTERVAL. The default value (-1) ensures that the DMM
    settles for a recommended time, which is the same as using an immediate
    trigger.
    '''
    sample_trigger = AttributeEnum(1250302, enums.SampleTrigger)
    '''
    Specifies the sample trigger source.

    To determine which values are supported by each device, refer to the
    LabVIEW Trigger Routing section in the *NI Digital Multimeters Help*.
    '''
    sample_trig_slope = AttributeEnum(1150010, enums.SampleTrigSlope)
    '''
    Specifies the edge of the signal from the specified sample trigger
    source on which the DMM is triggered.
    '''
    secondary_error = AttributeViInt32(1050102)
    '''
    An optional code that provides additional information concerning the
    primary error condition. The error and warning values can be status
    codes defined by IVI, VISA, class drivers, or specific drivers. Zero
    indicates no additional information.
    '''
    settle_time = AttributeViReal64(1150028)
    '''
    Specifies the settling time in seconds. Use this property to override
    the default settling time. To return to the default, set this property
    to Auto (-1).
    '''
    shunt_value = AttributeViReal64(1150003)
    '''
    For the NI 4050 only, specifies the shunt resistance value.
    '''
    simulate = AttributeViBoolean(1050005)
    '''
    Specifies whether to simulate instrument driver I/O operations. If
    simulation is enabled, instrument driver functions perform range
    checking and call IVI Get and Set VIs, but they do not perform
    instrument I/O. For output parameters that represent instrument data,
    the instrument driver VIs return calculated values. The default value is
    FALSE (0). Use niDMM Initialize With Options to override the default
    setting.
    '''
    specific_driver_class_spec_major_version = AttributeViInt32(1050515)
    '''
    The major version number of the class specification for the specific
    driver.
    '''
    specific_driver_class_spec_minor_version = AttributeViInt32(1050516)
    '''
    The minor version number of the class specification for the specific
    driver.
    '''
    specific_driver_description = AttributeViString(1050514)
    '''
    A string containing a description of the specific driver.
    '''
    specific_driver_major_version = AttributeViInt32(1050503)
    '''
    Returns the major version number of this instrument driver.
    '''
    specific_driver_minor_version = AttributeViInt32(1050504)
    '''
    Returns the minor version number of this instrument driver.
    '''
    specific_driver_prefix = AttributeViString(1050302)
    '''
    The prefix for the specific instrument driver. The name of each
    user-callable VI in this driver starts with this prefix. The prefix can
    be up to a maximum of eight characters.
    '''
    specific_driver_revision = AttributeViString(1050551)
    '''
    A string that contains additional version information about this
    instrument driver.
    '''
    specific_driver_vendor = AttributeViString(1050513)
    '''
    A string containing the vendor of the specific driver.
    '''
    supported_instrument_models = AttributeViString(1050327)
    '''
    A string containing the instrument models supported by the specific
    driver.
    '''
    susceptance = AttributeViReal64(1150048)
    '''
    For the NI 4082 and NI 4072 only, specifies the reactive part
    (susceptance) of the open cable compensation. The valid range is any
    real number >0. The default value (-1.0) indicates that compensation has
    not taken place.
    '''
    tc_fixed_ref_junction = AttributeViReal64(1250233)
    '''
    Specifies the value of the fixed reference junction temperature for a
    thermocouple in degrees Celsius.
    '''
    tc_ref_junction_type = AttributeEnum(1250232, enums.ThermocoupleReferenceJunctionType)
    '''
    Specifies the thermocouple reference junction type.
    '''
    thermistor_a = AttributeViReal64(1150125)
    '''
    Specifies the Steinhart-Hart A coefficient for thermistor scaling when
    the **Thermistor Type property** is set to Custom.
    '''
    thermistor_b = AttributeViReal64(1150126)
    '''
    Specifies the Steinhart-Hart B coefficient for thermistor scaling when
    the **Thermistor Type property** is set to Custom.
    '''
    thermistor_c = AttributeViReal64(1150127)
    '''
    Specifies the Steinhart-Hart C coefficient for thermistor scaling when
    the **Thermistor Type property** is set to Custom.
    '''
    thermistor_type = AttributeEnum(1150124, enums.ThermistorType)
    '''
    Specifies the thermistor type.
    '''
    thermocouple_type = AttributeEnum(1250231, enums.ThermocoupleType)
    '''
    Specifies the thermocouple type.
    '''
    transducer_type = AttributeEnum(1250201, enums.TransducerType)
    '''
    Specifies the transducer type.
    '''
    trigger_count = AttributeViInt32(1250304)
    '''
    Specifies the number of triggers the DMM receives before returning to
    the Idle state. This property can be set to any positive ViInt32 value
    for the NI 4065, NI 4070/4071/4072, and NI 4080/4081/4082.

    The NI 4050/4060 only support this property being set to 1.

    Refer to Multiple Point Acquisitions in the *NI Digital Multimeters
    Help* for more information.
    '''
    trigger_delay = AttributeViReal64(1250005)
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
    trigger_slope = AttributeEnum(1250334, enums.TriggerSlope)
    '''
    Specifies the edge of the signal from the specified trigger source on
    which the DMM is triggered.
    '''
    trigger_source = AttributeEnum(1250004, enums.TriggerSource)
    '''
    Specifies the trigger source. When niDMM Initiate is called, the DMM
    waits for the trigger specified with this property. After it receives
    the trigger, the DMM waits the length of time specified with the Trigger
    Delay property. The DMM then takes a measurement.

    To determine which values are supported by each device, refer to the
    LabVIEW Trigger Routing section in the *NI Digital Multimeters Help*.
    '''
    waveform_coupling = AttributeEnum(1150027, enums.WaveformCoupling)
    '''
    For the NI 4080/4081/4082 and NI 4070/4071/4072 only, specifies the
    coupling during a waveform acquisition.
    '''
    waveform_points = AttributeViInt32(1150019)
    '''
    For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the number of
    points to acquire in a waveform acquisition.
    '''
    waveform_rate = AttributeViReal64(1150018)
    '''
    Specifies the rate of the waveform acquisition in samples per second
    (S/s). The valid rate is calculated by dividing 1,800,000 by an integer
    divisor, and the rate falls between 10 and 1,800,000 samples per second.
    The waveform rate is coerced upwards to the next valid rate. The default
    value is 1,800,000 samples per second. Not supported by NI 4065.
    '''

    def __init__(self, resource_name, id_query=0, reset_device=False, options_string=""):
        self.library = library.get_library()
        self.vi = 0  # This must be set before calling _init_with_options.
        self.vi = self._init_with_options(resource_name, id_query, reset_device, options_string)

        self._is_frozen = True

    def __setattr__(self, key, value):
        if self._is_frozen and key not in dir(self):
            raise TypeError("%r is a frozen class" % self)
        object.__setattr__(self, key, value)

    def initiate(self):
        return Acquisition(self)

    def __del__(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        # TODO(marcoskirsch): Should we raise an exception on double close? Look at what File does.
        try:
            self._close()
        except errors.Error:
            # TODO(marcoskirsch): This will occur when session is "stolen". Change to log instead
            print("Failed to close session.")
        self.vi = 0

    # method needed for generic driver exceptions
    def _get_error_description(self, error_code):
        new_error_code = ctypes_types.ViStatus_ctype(0)
        buffer_size = self.library.niDMM_GetError(self.vi, ctypes.byref(new_error_code), 0, None)
        assert (new_error_code.value == error_code)

        if (buffer_size > 0):
            '''
            Return code > 0 from first call to GetError represents the size of
            the description.  Call it again.
            Ignore incoming IVI error code and return description from the driver
            (trust that the IVI error code was properly stored in the session
            by the driver)
            '''
            error_code = ctypes_types.ViStatus_ctype(error_code)
            error_message = ctypes.create_string_buffer(buffer_size)
            self.library.niDMM_GetError(self.vi, ctypes.byref(error_code), buffer_size, ctypes.cast(error_message, ctypes.POINTER(ctypes_types.ViChar_ctype)))
        else:
            '''
            Return code <= 0 from GetError indicates a problem.  This is expected
            when the session is invalid (IVI spec requires GetError to fail).
            Use GetErrorMessage instead.  It doesn't require a session.

            Call niDMM_GetErrorMessage, pass VI_NULL for the buffer in order to retrieve
            the length of the error message.
            '''
            error_code = buffer_size
            buffer_size = self.library.niDMM_GetErrorMessage(self.vi, error_code, 0, None)
            error_message = ctypes.create_string_buffer(buffer_size)
            self.library.niDMM_GetErrorMessage(self.vi, error_code, buffer_size, ctypes.cast(error_message, ctypes.POINTER(ctypes_types.ViChar_ctype)))

        # TODO(marcoskirsch): By hardcoding encoding "ascii", internationalized strings will throw.
        #       Which encoding should we be using? https://docs.python.org/3/library/codecs.html#standard-encodings
        return new_error_code.value, error_message.value.decode("ascii")

    ''' These are code-generated '''

    def _abort(self):
        error_code = self.library.niDMM_Abort(self.vi)
        errors._handle_error(self, error_code)
        return

    def _clear_error(self):
        error_code = self.library.niDMM_ClearError(self.vi)
        errors._handle_error(self, error_code)
        return

    def clear_interchange_warnings(self):
        error_code = self.library.niDMM_ClearInterchangeWarnings(self.vi)
        errors._handle_error(self, error_code)
        return

    def configure_ac_bandwidth(self, min_freq, max_freq):
        error_code = self.library.niDMM_ConfigureACBandwidth(self.vi, min_freq, max_freq)
        errors._handle_error(self, error_code)
        return

    def configure_adc_calibration(self, adc_gain_comp):
        if type(adc_gain_comp) is not enums.EnabledSetting:
            raise TypeError('Parameter mode must be of type ' + str(enums.EnabledSetting))
        error_code = self.library.niDMM_ConfigureADCCalibration(self.vi, adc_gain_comp.value)
        errors._handle_error(self, error_code)
        return

    def configure_auto_zero_mode(self, auto_zero_mode):
        if type(auto_zero_mode) is not enums.EnabledSetting:
            raise TypeError('Parameter mode must be of type ' + str(enums.EnabledSetting))
        error_code = self.library.niDMM_ConfigureAutoZeroMode(self.vi, auto_zero_mode.value)
        errors._handle_error(self, error_code)
        return

    def configure_cable_comp_type(self, type_of_compensation):
        if type(type_of_compensation) is not enums.CableCompensationType:
            raise TypeError('Parameter mode must be of type ' + str(enums.CableCompensationType))
        error_code = self.library.niDMM_ConfigureCableCompType(self.vi, type_of_compensation.value)
        errors._handle_error(self, error_code)
        return

    def configure_current_source(self, diode_current_src):
        if type(diode_current_src) is not enums.CurrentSource:
            raise TypeError('Parameter mode must be of type ' + str(enums.CurrentSource))
        error_code = self.library.niDMM_ConfigureCurrentSource(self.vi, diode_current_src.value)
        errors._handle_error(self, error_code)
        return

    def configure_fixed_ref_junction(self, fixed_ref_junction):
        error_code = self.library.niDMM_ConfigureFixedRefJunction(self.vi, fixed_ref_junction)
        errors._handle_error(self, error_code)
        return

    def configure_frequency_voltage_range(self, frequency_voltage_range):
        error_code = self.library.niDMM_ConfigureFrequencyVoltageRange(self.vi, frequency_voltage_range)
        errors._handle_error(self, error_code)
        return

    def configure_meas_complete_dest(self, destination):
        if type(destination) is not enums.Terminal:
            raise TypeError('Parameter mode must be of type ' + str(enums.Terminal))
        error_code = self.library.niDMM_ConfigureMeasCompleteDest(self.vi, destination.value)
        errors._handle_error(self, error_code)
        return

    def configure_meas_complete_slope(self, polarity):
        if type(polarity) is not enums.Slope:
            raise TypeError('Parameter mode must be of type ' + str(enums.Slope))
        error_code = self.library.niDMM_ConfigureMeasCompleteSlope(self.vi, polarity.value)
        errors._handle_error(self, error_code)
        return

    def configure_measurement_absolute(self, meas_function, range, resolution_absolute):
        if type(meas_function) is not enums.Function:
            raise TypeError('Parameter mode must be of type ' + str(enums.Function))
        error_code = self.library.niDMM_ConfigureMeasurementAbsolute(self.vi, meas_function.value, range, resolution_absolute)
        errors._handle_error(self, error_code)
        return

    def configure_measurement_digits(self, meas_function, range, resolution_digits):
        if type(meas_function) is not enums.Function:
            raise TypeError('Parameter mode must be of type ' + str(enums.Function))
        error_code = self.library.niDMM_ConfigureMeasurementDigits(self.vi, meas_function.value, range, resolution_digits)
        errors._handle_error(self, error_code)
        return

    def configure_multi_point(self, trigger_count, sample_count, sample_trigger, sample_interval):
        if type(sample_trigger) is not enums.Terminal:
            raise TypeError('Parameter mode must be of type ' + str(enums.Terminal))
        error_code = self.library.niDMM_ConfigureMultiPoint(self.vi, trigger_count, sample_count, sample_trigger.value, sample_interval)
        errors._handle_error(self, error_code)
        return

    def configure_offset_comp_ohms(self, offset_comp_ohms):
        if type(offset_comp_ohms) is not enums.EnabledSetting:
            raise TypeError('Parameter mode must be of type ' + str(enums.EnabledSetting))
        error_code = self.library.niDMM_ConfigureOffsetCompOhms(self.vi, offset_comp_ohms.value)
        errors._handle_error(self, error_code)
        return

    def configure_open_cable_comp_values(self, conductance, susceptance):
        error_code = self.library.niDMM_ConfigureOpenCableCompValues(self.vi, conductance, susceptance)
        errors._handle_error(self, error_code)
        return

    def configure_power_line_frequency(self, frequency):
        error_code = self.library.niDMM_ConfigurePowerLineFrequency(self.vi, frequency)
        errors._handle_error(self, error_code)
        return

    def configure_rtd_custom(self, a, b, c):
        error_code = self.library.niDMM_ConfigureRTDCustom(self.vi, a, b, c)
        errors._handle_error(self, error_code)
        return

    def configure_rtd_type(self, rtd_type, resistance):
        error_code = self.library.niDMM_ConfigureRTDType(self.vi, rtd_type, resistance)
        errors._handle_error(self, error_code)
        return

    def configure_sample_trigger_slope(self, polarity):
        if type(polarity) is not enums.Slope:
            raise TypeError('Parameter mode must be of type ' + str(enums.Slope))
        error_code = self.library.niDMM_ConfigureSampleTriggerSlope(self.vi, polarity.value)
        errors._handle_error(self, error_code)
        return

    def configure_short_cable_comp_values(self, resistance, reactance):
        error_code = self.library.niDMM_ConfigureShortCableCompValues(self.vi, resistance, reactance)
        errors._handle_error(self, error_code)
        return

    def configure_thermistor_custom(self, a, b, c):
        error_code = self.library.niDMM_ConfigureThermistorCustom(self.vi, a, b, c)
        errors._handle_error(self, error_code)
        return

    def configure_thermistor_type(self, thermistor_type):
        if type(thermistor_type) is not enums.TemperatureThermistorType:
            raise TypeError('Parameter mode must be of type ' + str(enums.TemperatureThermistorType))
        error_code = self.library.niDMM_ConfigureThermistorType(self.vi, thermistor_type.value)
        errors._handle_error(self, error_code)
        return

    def configure_thermocouple(self, thermocouple_type, ref_junction_type):
        error_code = self.library.niDMM_ConfigureThermocouple(self.vi, thermocouple_type, ref_junction_type)
        errors._handle_error(self, error_code)
        return

    def configure_transducer_type(self, transducer_type):
        if type(transducer_type) is not enums.TemperatureTransducerType:
            raise TypeError('Parameter mode must be of type ' + str(enums.TemperatureTransducerType))
        error_code = self.library.niDMM_ConfigureTransducerType(self.vi, transducer_type.value)
        errors._handle_error(self, error_code)
        return

    def configure_trigger(self, trig_source, trigger_delay):
        if type(trig_source) is not enums.Terminal:
            raise TypeError('Parameter mode must be of type ' + str(enums.Terminal))
        error_code = self.library.niDMM_ConfigureTrigger(self.vi, trig_source.value, trigger_delay)
        errors._handle_error(self, error_code)
        return

    def configure_trigger_slope(self, polarity):
        if type(polarity) is not enums.Slope:
            raise TypeError('Parameter mode must be of type ' + str(enums.Slope))
        error_code = self.library.niDMM_ConfigureTriggerSlope(self.vi, polarity.value)
        errors._handle_error(self, error_code)
        return

    def configure_waveform_acquisition(self, function, range, rate, waveform_points):
        if type(function) is not enums.Function:
            raise TypeError('Parameter mode must be of type ' + str(enums.Function))
        error_code = self.library.niDMM_ConfigureWaveformAcquisition(self.vi, function.value, range, rate, waveform_points)
        errors._handle_error(self, error_code)
        return

    def configure_waveform_coupling(self, coupling):
        if type(coupling) is not enums.WaveformCouplingMode:
            raise TypeError('Parameter mode must be of type ' + str(enums.WaveformCouplingMode))
        error_code = self.library.niDMM_ConfigureWaveformCoupling(self.vi, coupling.value)
        errors._handle_error(self, error_code)
        return

    def disable(self):
        error_code = self.library.niDMM_Disable(self.vi)
        errors._handle_error(self, error_code)
        return

    def fetch(self, max_time):
        reading_ctype = ctypes_types.ViReal64_ctype(0)
        error_code = self.library.niDMM_Fetch(self.vi, max_time, ctypes.pointer(reading_ctype))
        errors._handle_error(self, error_code)
        return reading_ctype.value

    def fetch_multi_point(self, max_time, array_size, reading_array):
        actual_pts_ctype = ctypes_types.ViInt32_ctype(0)
        error_code = self.library.niDMM_FetchMultiPoint(self.vi, max_time, array_size, reading_array, ctypes.pointer(actual_pts_ctype))
        errors._handle_error(self, error_code)
        return actual_pts_ctype.value

    def fetch_waveform(self, max_time, array_size, waveform_array):
        actual_points_ctype = ctypes_types.ViInt32_ctype(0)
        error_code = self.library.niDMM_FetchWaveform(self.vi, max_time, array_size, waveform_array, ctypes.pointer(actual_points_ctype))
        errors._handle_error(self, error_code)
        return actual_points_ctype.value

    def get_aperture_time_info(self):
        aperture_time_ctype = ctypes_types.ViReal64_ctype(0)
        aperture_time_units_ctype = ctypes_types.ViInt32_ctype(0)
        error_code = self.library.niDMM_GetApertureTimeInfo(self.vi, ctypes.pointer(aperture_time_ctype), ctypes.pointer(aperture_time_units_ctype))
        errors._handle_error(self, error_code)
        return aperture_time_ctype.value, aperture_time_units_ctype.value

    def _get_attribute_vi_boolean(self, channel_name, attribute_id):
        value_ctype = ctypes_types.ViBoolean_ctype(0)
        error_code = self.library.niDMM_GetAttributeViBoolean(self.vi, channel_name.encode('ascii'), attribute_id, ctypes.pointer(value_ctype))
        errors._handle_error(self, error_code)
        return value_ctype.value

    def _get_attribute_vi_int32(self, channel_name, attribute_id):
        value_ctype = ctypes_types.ViInt32_ctype(0)
        error_code = self.library.niDMM_GetAttributeViInt32(self.vi, channel_name.encode('ascii'), attribute_id, ctypes.pointer(value_ctype))
        errors._handle_error(self, error_code)
        return value_ctype.value

    def _get_attribute_vi_real64(self, channel_name, attribute_id):
        value_ctype = ctypes_types.ViReal64_ctype(0)
        error_code = self.library.niDMM_GetAttributeViReal64(self.vi, channel_name.encode('ascii'), attribute_id, ctypes.pointer(value_ctype))
        errors._handle_error(self, error_code)
        return value_ctype.value

    def _get_attribute_vi_session(self, channel_name, attribute_id):
        value_ctype = ctypes_types.ViSession_ctype(0)
        error_code = self.library.niDMM_GetAttributeViSession(self.vi, channel_name.encode('ascii'), attribute_id, ctypes.pointer(value_ctype))
        errors._handle_error(self, error_code)
        return value_ctype.value

    def _get_attribute_vi_string(self, channel_name, attribute_id, buf_size):
        value_ctype = ctypes_types.ViString_ctype(0)  # TODO(marcoskirsch): allocate a buffer
        error_code = self.library.niDMM_GetAttributeViString(self.vi, channel_name.encode('ascii'), attribute_id, buf_size, value_ctype)
        errors._handle_error(self, error_code)
        return value_ctype.value

    def get_auto_range_value(self):
        auto_range_value_ctype = ctypes_types.ViReal64_ctype(0)
        error_code = self.library.niDMM_GetAutoRangeValue(self.vi, ctypes.pointer(auto_range_value_ctype))
        errors._handle_error(self, error_code)
        return auto_range_value_ctype.value

    def get_cal_count(self, cal_type):
        count_ctype = ctypes_types.ViInt32_ctype(0)
        error_code = self.library.niDMM_GetCalCount(self.vi, cal_type, ctypes.pointer(count_ctype))
        errors._handle_error(self, error_code)
        return count_ctype.value

    def get_cal_date_and_time(self, cal_type):
        month_ctype = ctypes_types.ViInt32_ctype(0)
        day_ctype = ctypes_types.ViInt32_ctype(0)
        year_ctype = ctypes_types.ViInt32_ctype(0)
        hour_ctype = ctypes_types.ViInt32_ctype(0)
        minute_ctype = ctypes_types.ViInt32_ctype(0)
        error_code = self.library.niDMM_GetCalDateAndTime(self.vi, cal_type, ctypes.pointer(month_ctype), ctypes.pointer(day_ctype), ctypes.pointer(year_ctype), ctypes.pointer(hour_ctype), ctypes.pointer(minute_ctype))
        errors._handle_error(self, error_code)
        return month_ctype.value, day_ctype.value, year_ctype.value, hour_ctype.value, minute_ctype.value

    def get_channel_name(self, index, buffer_size, name):
        error_code = self.library.niDMM_GetChannelName(self.vi, index, buffer_size, name)
        errors._handle_error(self, error_code)
        return

    def get_dev_temp(self, reserved):
        temperature_ctype = ctypes_types.ViReal64_ctype(0)
        error_code = self.library.niDMM_GetDevTemp(self.vi, reserved.encode('ascii'), ctypes.pointer(temperature_ctype))
        errors._handle_error(self, error_code)
        return temperature_ctype.value

    def _get_error(self, buffer_size):
        error_code_ctype = ctypes_types.ViStatus_ctype(0)
        description_ctype = ctypes_types.ViChar_ctype(0)  # TODO(marcoskirsch): allocate a buffer
        error_code = self.library.niDMM_GetError(self.vi, ctypes.pointer(error_code_ctype), buffer_size, ctypes.pointer(description_ctype))
        errors._handle_error(self, error_code)
        return error_code_ctype.value, description_ctype.value.decode("ascii")

    def _get_error_message(self, error_code, buffer_size):
        err_message_ctype = ctypes_types.ViChar_ctype(0)  # TODO(marcoskirsch): allocate a buffer
        error_code = self.library.niDMM_GetErrorMessage(self.vi, error_code, buffer_size, ctypes.pointer(err_message_ctype))
        errors._handle_error(self, error_code)
        return err_message_ctype.value.decode("ascii")

    def get_last_cal_temp(self, cal_type):
        temperature_ctype = ctypes_types.ViReal64_ctype(0)
        error_code = self.library.niDMM_GetLastCalTemp(self.vi, cal_type, ctypes.pointer(temperature_ctype))
        errors._handle_error(self, error_code)
        return temperature_ctype.value

    def get_measurement_period(self):
        period_ctype = ctypes_types.ViReal64_ctype(0)
        error_code = self.library.niDMM_GetMeasurementPeriod(self.vi, ctypes.pointer(period_ctype))
        errors._handle_error(self, error_code)
        return period_ctype.value

    def get_next_coercion_record(self, buffer_size, record):
        error_code = self.library.niDMM_GetNextCoercionRecord(self.vi, buffer_size, record)
        errors._handle_error(self, error_code)
        return

    def get_next_interchange_warning(self, buffer_size):
        warn_string_ctype = ctypes_types.ViChar_ctype(0)  # TODO(marcoskirsch): allocate a buffer
        error_code = self.library.niDMM_GetNextInterchangeWarning(self.vi, buffer_size, ctypes.pointer(warn_string_ctype))
        errors._handle_error(self, error_code)
        return warn_string_ctype.value.decode("ascii")

    def get_self_cal_supported(self):
        self_cal_supported_ctype = ctypes_types.ViBoolean_ctype(0)
        error_code = self.library.niDMM_GetSelfCalSupported(self.vi, ctypes.pointer(self_cal_supported_ctype))
        errors._handle_error(self, error_code)
        return self_cal_supported_ctype.value

    def _init_with_options(self, resource_name, id_query, reset_device, options_string):
        new_vi_ctype = ctypes_types.ViSession_ctype(0)
        error_code = self.library.niDMM_InitWithOptions(resource_name.encode('ascii'), id_query, reset_device, options_string.encode('ascii'), ctypes.pointer(new_vi_ctype))
        errors._handle_error(self, error_code)
        return new_vi_ctype.value

    def _initiate(self):
        error_code = self.library.niDMM_Initiate(self.vi)
        errors._handle_error(self, error_code)
        return

    def invalidate_all_attributes(self):
        error_code = self.library.niDMM_InvalidateAllAttributes(self.vi)
        errors._handle_error(self, error_code)
        return

    def is_over_range(self, measurement_value):
        is_over_range_ctype = ctypes_types.ViBoolean_ctype(0)
        error_code = self.library.niDMM_IsOverRange(self.vi, measurement_value, ctypes.pointer(is_over_range_ctype))
        errors._handle_error(self, error_code)
        return is_over_range_ctype.value

    def is_under_range(self, measurement_value):
        is_under_range_ctype = ctypes_types.ViBoolean_ctype(0)
        error_code = self.library.niDMM_IsUnderRange(self.vi, measurement_value, ctypes.pointer(is_under_range_ctype))
        errors._handle_error(self, error_code)
        return is_under_range_ctype.value

    def _lock_session(self):
        caller_has_lock_ctype = ctypes_types.ViBoolean_ctype(0)
        error_code = self.library.niDMM_LockSession(self.vi, ctypes.pointer(caller_has_lock_ctype))
        errors._handle_error(self, error_code)
        return caller_has_lock_ctype.value

    def perform_open_cable_comp(self):
        conductance_ctype = ctypes_types.ViReal64_ctype(0)
        susceptance_ctype = ctypes_types.ViReal64_ctype(0)
        error_code = self.library.niDMM_PerformOpenCableComp(self.vi, ctypes.pointer(conductance_ctype), ctypes.pointer(susceptance_ctype))
        errors._handle_error(self, error_code)
        return conductance_ctype.value, susceptance_ctype.value

    def perform_short_cable_comp(self):
        resistance_ctype = ctypes_types.ViReal64_ctype(0)
        reactance_ctype = ctypes_types.ViReal64_ctype(0)
        error_code = self.library.niDMM_PerformShortCableComp(self.vi, ctypes.pointer(resistance_ctype), ctypes.pointer(reactance_ctype))
        errors._handle_error(self, error_code)
        return resistance_ctype.value, reactance_ctype.value

    def read(self, max_time):
        reading_ctype = ctypes_types.ViReal64_ctype(0)
        error_code = self.library.niDMM_Read(self.vi, max_time, ctypes.pointer(reading_ctype))
        errors._handle_error(self, error_code)
        return reading_ctype.value

    def read_multi_point(self, max_time, array_size, reading_array):
        actual_pts_ctype = ctypes_types.ViInt32_ctype(0)
        error_code = self.library.niDMM_ReadMultiPoint(self.vi, max_time, array_size, reading_array, ctypes.pointer(actual_pts_ctype))
        errors._handle_error(self, error_code)
        return actual_pts_ctype.value

    def read_status(self):
        acq_backlog_ctype = ctypes_types.ViInt32_ctype(0)
        acq_done_ctype = ctypes_types.ViInt16_ctype(0)
        error_code = self.library.niDMM_ReadStatus(self.vi, ctypes.pointer(acq_backlog_ctype), ctypes.pointer(acq_done_ctype))
        errors._handle_error(self, error_code)
        return acq_backlog_ctype.value, acq_done_ctype.value

    def read_waveform(self, max_time, array_size, waveform_array):
        actual_points_ctype = ctypes_types.ViInt32_ctype(0)
        error_code = self.library.niDMM_ReadWaveform(self.vi, max_time, array_size, waveform_array, ctypes.pointer(actual_points_ctype))
        errors._handle_error(self, error_code)
        return actual_points_ctype.value

    def reset_interchange_check(self):
        error_code = self.library.niDMM_ResetInterchangeCheck(self.vi)
        errors._handle_error(self, error_code)
        return

    def reset_with_defaults(self):
        error_code = self.library.niDMM_ResetWithDefaults(self.vi)
        errors._handle_error(self, error_code)
        return

    def self_cal(self):
        error_code = self.library.niDMM_SelfCal(self.vi)
        errors._handle_error(self, error_code)
        return

    def send_software_trigger(self):
        error_code = self.library.niDMM_SendSoftwareTrigger(self.vi)
        errors._handle_error(self, error_code)
        return

    def _set_attribute_vi_boolean(self, channel_name, attribute_id, value):
        error_code = self.library.niDMM_SetAttributeViBoolean(self.vi, channel_name.encode('ascii'), attribute_id, value)
        errors._handle_error(self, error_code)
        return

    def _set_attribute_vi_int32(self, channel_name, attribute_id, value):
        error_code = self.library.niDMM_SetAttributeViInt32(self.vi, channel_name.encode('ascii'), attribute_id, value)
        errors._handle_error(self, error_code)
        return

    def _set_attribute_vi_real64(self, channel_name, attribute_id, value):
        error_code = self.library.niDMM_SetAttributeViReal64(self.vi, channel_name.encode('ascii'), attribute_id, value)
        errors._handle_error(self, error_code)
        return

    def _set_attribute_vi_session(self, channel_name, attribute_id, value):
        error_code = self.library.niDMM_SetAttributeViSession(self.vi, channel_name.encode('ascii'), attribute_id, value)
        errors._handle_error(self, error_code)
        return

    def _set_attribute_vi_string(self, channel_name, attribute_id, value):
        error_code = self.library.niDMM_SetAttributeViString(self.vi, channel_name.encode('ascii'), attribute_id, value.encode('ascii'))
        errors._handle_error(self, error_code)
        return

    def _unlock_session(self):
        caller_has_lock_ctype = ctypes_types.ViBoolean_ctype(0)
        error_code = self.library.niDMM_UnlockSession(self.vi, ctypes.pointer(caller_has_lock_ctype))
        errors._handle_error(self, error_code)
        return caller_has_lock_ctype.value

    def _close(self):
        error_code = self.library.niDMM_close(self.vi)
        errors._handle_error(self, error_code)
        return

    def reset(self):
        error_code = self.library.niDMM_reset(self.vi)
        errors._handle_error(self, error_code)
        return

    def revision_query(self, driver_rev, instr_rev):
        error_code = self.library.niDMM_revision_query(self.vi, driver_rev, instr_rev)
        errors._handle_error(self, error_code)
        return

    def self_test(self):
        self_test_result_ctype = ctypes_types.ViInt16_ctype(0)
        self_test_message_ctype = ctypes_types.ViChar_ctype(0)  # TODO(marcoskirsch): allocate a buffer
        error_code = self.library.niDMM_self_test(self.vi, ctypes.pointer(self_test_result_ctype), ctypes.pointer(self_test_message_ctype))
        errors._handle_error(self, error_code)
        return self_test_result_ctype.value, self_test_message_ctype.value.decode("ascii")

    ''' These are temporarily hand-coded because the generator can't handle buffers yet '''

    def _get_attribute_vi_string(self, channel_name, attribute_id):  # noqa: F811
        # Do the IVI dance
        # Don't use _handle_error, because positive value in error_code means size, not warning.
        buffer_size = 0
        value_ctype = ctypes.cast(ctypes.create_string_buffer(buffer_size), ctypes_types.ViString_ctype)
        error_code = self.library.niDMM_GetAttributeViString(self.vi, channel_name.encode('ascii'), attribute_id, buffer_size, value_ctype)
        if(errors._is_error(error_code)):
            raise errors.Error(self.library, self.vi, error_code)
        buffer_size = error_code
        value_ctype = ctypes.cast(ctypes.create_string_buffer(buffer_size), ctypes_types.ViString_ctype)
        error_code = self.library.niDMM_GetAttributeViString(self.vi, channel_name.encode('ascii'), attribute_id, buffer_size, value_ctype)
        errors._handle_error(self, error_code)
        return value_ctype.value.decode("ascii")
