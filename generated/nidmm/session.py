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
        '''.. function:: _abort()

            Aborts a previously initiated measurement and returns the DMM to the
            Idle state.
        '''
        error_code = self.library.niDMM_Abort(self.vi)
        errors._handle_error(self, error_code)
        return

    def _clear_error(self):
        '''.. function:: _clear_error()

            Clears the error information for the current execution thread and the
            IVI session you specify. If you pass VI\_NULL for the
            **Instrument\_Handle** parameter, this function clears the error
            information only for the current execution thread.
        '''
        error_code = self.library.niDMM_ClearError(self.vi)
        errors._handle_error(self, error_code)
        return

    def clear_interchange_warnings(self):
        '''.. function:: clear_interchange_warnings()

            Clears the list of current interchange warnings.
        '''
        error_code = self.library.niDMM_ClearInterchangeWarnings(self.vi)
        errors._handle_error(self, error_code)
        return

    def configure_ac_bandwidth(self, ac_minimum_frequency_hz, ac_maximum_frequency_hz):
        '''.. function:: configure_ac_bandwidth(ac_minimum_frequency_hz, ac_maximum_frequency_hz)

            Purpose
            -------

            Configures the `
            NIDMM\_ATTR\_AC\_MIN\_FREQ <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_AC_MIN_FREQ.html')>`__
            and `
            NIDMM\_ATTR\_AC\_MAX\_FREQ <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'caNIDMM_ATTR_AC_MAX_FREQ.html')>`__
            attributes, which the DMM uses for AC measurements.

            :param ac_minimum_frequency_hz: Specifies the minimum expected frequency component of the input signal
                in hertz. This parameter affects the DMM only when you set the `
                NIDMM\_ATTR\_FUNCTION <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_FUNCTION.html')>`__
                attribute to AC measurements. NI-DMM uses this parameter to calculate
                the proper aperture for the measurement.
                The driver sets the `
                NIDMM\_ATTR\_AC\_MIN\_FREQ <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'caNIDMM_ATTR_AC_MIN_FREQ.html')>`__
                attribute to this value. The valid range is 1 Hz–300 kHz for the NI
                4080/4081/4082 and the NI 4070/4071/4072, 10 Hz–100 Hz for the NI 4065,
                and 20 Hz–25 kHz for the NI 4050 and NI 4060.
            :type ac_minimum_frequency_hz: ViReal64
            :param ac_maximum_frequency_hz: Specifies the maximum expected frequency component of the input signal
                in hertz within the device limits. This parameter is used only for error
                checking and verifies that the value of this parameter is less than the
                maximum frequency of the device.

                This parameter affects the DMM only when you set the `
                NIDMM\_ATTR\_FUNCTION <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'caNIDMM_ATTR_FUNCTION.html')>`__
                attribute to AC measurements. The driver sets the `
                NIDMM\_ATTR\_AC\_MAX\_FREQ <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_AC_MAX_FREQ.html')>`__
                attribute to this value. The valid range is 1 Hz–300 kHz for the NI
                4080/4081/4082 and the NI 4070/4071/4072, 10 Hz–100 Hz for the NI 4065,
                and 20 Hz–25 kHz for the NI 4050 and NI 4060.
            :type ac_maximum_frequency_hz: ViReal64
        '''
        error_code = self.library.niDMM_ConfigureACBandwidth(self.vi, ac_minimum_frequency_hz, ac_maximum_frequency_hz)
        errors._handle_error(self, error_code)
        return

    def configure_adc_calibration(self, adc_calibration):
        '''.. function:: configure_adc_calibration(adc_calibration)

            For the NI 4080/4081/4082 and NI 4070/4071/4072, allows the DMM to
            compensate for gain drift since the last external calibration or
            self-calibration. When **ADC\_Calibration** is ON, the DMM measures an
            internal reference to calculate the correct gain for the measurement.
            When **ADC\_Calibration** is OFF, the DMM does not compensate for
            changes to the gain.

            :param adc_calibration: Specifies the **ADC\_Calibration** setting. The driver sets `
                NIDMM\_ATTR\_ADC\_CALIBRATION <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_ADC_CALIBRATION.html')>`__
                to this value.
                NIDMM\_VAL\_ADC\_CALIBRATION\_ON enables **ADC\_Calibration**.
                NIDMM\_VAL\_ADC\_CALIBRATION\_OFF disables **ADC\_Calibration**. If you
                set the value to NIDMM\_VAL\_ADC\_CALIBRATION\_AUTO, the driver
                determines whether to enable **ADC\_Calibration** based on the
                measurement function and resolution that you configure. If you configure
                the NI 4080/4081/4082 or NI 4070/4071/4072 for a 6½–digit and greater
                resolution DC measurement, the driver enables ADC Calibration. For all
                other measurement configurations, the driver disables
                **ADC\_Calibration**.
                +------------------------------------------------+---------+-----------------------------------------------------------------------------------------------------+
                | Name                                           | Value   | Description                                                                                         |
                +================================================+=========+=====================================================================================================+
                | NIDMM\_VAL\_ADC\_CALIBRATION\_AUTO (default)   | -1.0    | The DMM enables or disables **ADC\_Calibration** based on the configured function and resolution.   |
                +------------------------------------------------+---------+-----------------------------------------------------------------------------------------------------+
                | NIDMM\_VAL\_ADC\_CALIBRATION\_OFF              |  0      | The DMM does not compensate for changes to the gain.                                                |
                +------------------------------------------------+---------+-----------------------------------------------------------------------------------------------------+
                | NIDMM\_VAL\_ADC\_CALIBRATION\_ON               |  1      | The DMM measures an internal reference to calculate the correct gain for the measurement.           |
                +------------------------------------------------+---------+-----------------------------------------------------------------------------------------------------+
            :type adc_calibration: enums.EnabledSetting
        '''
        if type(adc_calibration) is not enums.EnabledSetting:
            raise TypeError('Parameter mode must be of type ' + str(enums.EnabledSetting))
        error_code = self.library.niDMM_ConfigureADCCalibration(self.vi, adc_calibration.value)
        errors._handle_error(self, error_code)
        return

    def configure_auto_zero_mode(self, auto_zero_mode):
        '''.. function:: configure_auto_zero_mode(auto_zero_mode)

            Configures the DMM for **Auto\_Zero\_Mode**. When **Auto\_Zero\_Mode**
            is ON, the DMM internally disconnects the input signal and takes a zero
            reading. It then subtracts the zero reading from the measurement. This
            prevents offset voltages present on the input circuitry of the DMM from
            affecting measurement accuracy. When **Auto\_Zero\_Mode** is OFF, the
            DMM does not compensate for zero reading offset.

            :param auto_zero_mode: Specifies the **autoZeroMode**. NI-DMM sets the `
                NIDMM\_ATTR\_AUTO\_ZERO <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_AUTO_ZERO.html')>`__
                attribute to this value.

                ON enables **autoZeroMode** for each measurement. ONCE enables
                **autoZeroMode** before the next measurement. The **autoZeroMode** value
                is stored and used in subsequent measurements until the device is
                reconfigured.

                OFF disables **autoZeroMode**. If you set this parameter to AUTO, NI-DMM
                determines whether to enable Auto Zero based on the measurement function
                that you configure. If you configure the NI 4080/4081/4082 or the
                NI 4070/4071/4072 for a 6½–digit and greater resolution DC measurement,
                NI-DMM sets **autoZeroMode** to ON.

                For all other DC measurement configurations on the NI 4080/4081/4082 or
                the NI 4070/4071/4072, NI-DMM sets **autoZeroMode** to ONCE. For all AC
                measurements or waveform acquisitions on the NI 4080/4081/4082 or the
                NI 4070/4071/4072, NI-DMM sets **autoZeroMode** to OFF. For NI 4060,
                **autoZeroMode** is set to OFF when AUTO is selected.

                For NI 4065 devices, **autoZeroMode** is always ON. **autoZeroMode** is
                an integral part of the signal measurement phase and adds no extra time
                to the overall measurement.

                .. note::   The NI 4060/4065 does *not* support this setting.
            :type auto_zero_mode: enums.EnabledSetting
        '''
        if type(auto_zero_mode) is not enums.EnabledSetting:
            raise TypeError('Parameter mode must be of type ' + str(enums.EnabledSetting))
        error_code = self.library.niDMM_ConfigureAutoZeroMode(self.vi, auto_zero_mode.value)
        errors._handle_error(self, error_code)
        return

    def configure_cable_comp_type(self, cable_comp_type):
        '''.. function:: configure_cable_comp_type(cable_comp_type)

            Purpose
            -------

            For the NI 4082 and NI 4072 only, sets the `
            NIDMM\_ATTR\_CABLE\_COMPENSATION\_TYPE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'caNIDMM_ATTR_CABLE_COMP_TYPE.html')>`__
            attribute for the current capacitance/inductance mode range.

            :param cable_comp_type: Specifies the type of cable compensation that is used for the current
                range.
            :type cable_comp_type: enums.CableCompensationType
        '''
        if type(cable_comp_type) is not enums.CableCompensationType:
            raise TypeError('Parameter mode must be of type ' + str(enums.CableCompensationType))
        error_code = self.library.niDMM_ConfigureCableCompType(self.vi, cable_comp_type.value)
        errors._handle_error(self, error_code)
        return

    def configure_current_source(self, current_source):
        '''.. function:: configure_current_source(current_source)

            The NI 4050 and NI 4060 are not supported. Configures the
            **Current\_Source** for diode measurements.

            :param current_source: Specifies the **currentSource** provided during diode measurements. For
                valid ranges, refer to the device sections for your device. The driver
                sets `
                NIDMM\_ATTR\_CURRENT\_SOURCE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'caNIDMM_ATTR_CURRENT_SOURCE.html')>`__
                to this value.
                +-------------------------------------+----------+-----------------------------------------------------+
                | NIDMM\_VAL\_1\_MICROAMP             | 1 µA     | NI 4080/4081/4082 and NI 4070/4071/4072             |
                +-------------------------------------+----------+-----------------------------------------------------+
                | NIDMM\_VAL\_10\_MICROAMP            | 10 µA    | NI 4080/4081/4082 and NI 4070/4071/4072 only        |
                +-------------------------------------+----------+-----------------------------------------------------+
                | NIDMM\_VAL\_100\_MICROAMP           | 100 µA   | NI 4080/4081/4082, NI 4070/4071/4072, and NI 4065   |
                +-------------------------------------+----------+-----------------------------------------------------+
                | NIDMM\_VAL\_1\_MILLIAMP (default)   | 1 mA     | NI 4080/4081/4082, NI 4070/4071/4072, and NI 4065   |
                +-------------------------------------+----------+-----------------------------------------------------+
            :type current_source: enums.CurrentSource
        '''
        if type(current_source) is not enums.CurrentSource:
            raise TypeError('Parameter mode must be of type ' + str(enums.CurrentSource))
        error_code = self.library.niDMM_ConfigureCurrentSource(self.vi, current_source.value)
        errors._handle_error(self, error_code)
        return

    def configure_fixed_ref_junction(self, fixed_reference_junction):
        '''.. function:: configure_fixed_ref_junction(fixed_reference_junction)

            Configures the fixed reference junction temperature for a thermocouple
            with a fixed reference junction type.

            :param fixed_reference_junction: Specifies the reference junction temperature when a fixed reference
                junction is used to take a thermocouple measurement. The units are
                degrees Celsius. NI-DMM uses this value to set the Fixed Reference
                Junction property. The default is 25.00 (°C).
            :type fixed_reference_junction: ViReal64
        '''
        error_code = self.library.niDMM_ConfigureFixedRefJunction(self.vi, fixed_reference_junction)
        errors._handle_error(self, error_code)
        return

    def configure_frequency_voltage_range(self, voltage_range):
        '''.. function:: configure_frequency_voltage_range(voltage_range)

            For the NI 4080/4081/4082 and the NI 4070/4071/4072 only, specifies the
            expected maximum amplitude of the input signal for frequency and period
            measurements.

            :param voltage_range: Sets the expected maximum amplitude of the input signal. Refer to the
                `NI 4080 <javascript:LaunchHelp('dmm.chm::/4080_functional_overview.html')>`__,
                `NI 4081 <javascript:LaunchHelp('dmm.chm::/4081_functional_overview.html')>`__,
                `NI 4072 <javascript:LaunchHelp('dmm.chm::/4082.html')>`__,
                `NI 4070 <javascript:LaunchHelp('dmm.chm::/4070_functional_overview.html')>`__,
                `NI 4071 <javascript:LaunchHelp('dmm.chm::/4071_functional_overview.html')>`__,
                and `NI 4072 <javascript:LaunchHelp('dmm.chm::/4072.html')>`__ sections
                for a list of valid values. NI-DMM sets `
                NIDMM\_ATTR\_FREQ\_VOLTAGE\_RANGE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'caNIDMM_ATTR_FREQ_VOLTAGE_RANGE.html')>`__
                to this value. The minimum peak-to-peak signal amplitude that can be
                detected is 10% of the specified **voltageRange**.
                +-----------------------------------------+---------+------------------------------------------------------------------------------------------------------------------------------------+
                | Name                                    | Value   | Description                                                                                                                        |
                +=========================================+=========+====================================================================================================================================+
                | NIDMM\_VAL\_AUTO\_RANGE\_ON (default)   | -1.0    | Configures the DMM to take an Auto Range measurement to calculate the voltage range before each frequency or period measurement.   |
                +-----------------------------------------+---------+------------------------------------------------------------------------------------------------------------------------------------+
                | NIDMM\_VAL\_AUTO\_RANGE\_OFF            | -2.0    | Disables Auto Ranging. The driver sets the voltage range to the last calculated voltage range.                                     |
                +-----------------------------------------+---------+------------------------------------------------------------------------------------------------------------------------------------+
            :type voltage_range: ViReal64
        '''
        error_code = self.library.niDMM_ConfigureFrequencyVoltageRange(self.vi, voltage_range)
        errors._handle_error(self, error_code)
        return

    def configure_meas_complete_dest(self, meas_complete_destination):
        '''.. function:: configure_meas_complete_dest(meas_complete_destination)

            Specifies the destination of the DMM Measurement Complete (MC) signal.
            Refer to
            `Triggering <javascript:LaunchHelp('dmm.chm::/trigger.html')>`__ for
            more information.

            :param meas_complete_destination: Specifies the destination of the Measurement Complete signal. This
                signal is issued when the DMM completes a single measurement. The driver
                sets the `
                NIDMM\_ATTR\_MEAS\_COMPLETE\_DEST <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_MEAS_COMPLETE_DEST.html')>`__
                attribute to this value. This signal is commonly referred to as
                Voltmeter Complete. .. note::   To determine which values are supported
                by each device, refer to the `LabWindows/CVI Trigger
                Routing <javascript:LaunchHelp('dmm.chm::/CVItrigger_routing.html')>`__
                section.
            :type meas_complete_destination: enums.MeasurementCompleteDest
        '''
        if type(meas_complete_destination) is not enums.MeasurementCompleteDest:
            raise TypeError('Parameter mode must be of type ' + str(enums.MeasurementCompleteDest))
        error_code = self.library.niDMM_ConfigureMeasCompleteDest(self.vi, meas_complete_destination.value)
        errors._handle_error(self, error_code)
        return

    def configure_meas_complete_slope(self, meas_complete_slope):
        '''.. function:: configure_meas_complete_slope(meas_complete_slope)

            Sets the Measurement Complete signal to either rising edge (positive) or
            falling edge (negative) polarity.

            :param meas_complete_slope: Specifies the polarity of the signal that is generated. The driver sets
                `
                NIDMM\_ATTR\_MEAS\_DEST\_SLOPE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_MEAS_DEST_SLOPE.html')>`__
                to this value.
                +--------------------------+-----+------------------------+------------------------------------------------------------------+
                | Rising Edge              | 0   | NIDMM\_VAL\_POSITIVE   | The driver triggers on the rising edge of the trigger signal.    |
                +--------------------------+-----+------------------------+------------------------------------------------------------------+
                | Falling Edge (default)   | 1   | NIDMM\_VAL\_NEGATIVE   | The driver triggers on the falling edge of the trigger signal.   |
                +--------------------------+-----+------------------------+------------------------------------------------------------------+
            :type meas_complete_slope: enums.Slope
        '''
        if type(meas_complete_slope) is not enums.Slope:
            raise TypeError('Parameter mode must be of type ' + str(enums.Slope))
        error_code = self.library.niDMM_ConfigureMeasCompleteSlope(self.vi, meas_complete_slope.value)
        errors._handle_error(self, error_code)
        return

    def configure_measurement_absolute(self, measurement_function, range, resolution_absolute):
        '''.. function:: configure_measurement_absolute(measurement_function, range, resolution_absolute)

            ViStatus = niDMM\_ConfigureMeasurementAbsolute(ViSession
            Instrument\_Handle, ViInt32 Measurement\_Function, ViReal64 Range,
            ViReal64 Resolution\_Absolute)

            Purpose
            -------

            Configures the common attributes of the measurement. These attributes
            include `
            NIDMM\_ATTR\_FUNCTION <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_FUNCTION.html')>`__,
            `
            NIDMM\_ATTR\_RANGE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_RANGE.html')>`__,
            and `
            NIDMM\_ATTR\_RESOLUTION\_ABSOLUTE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_RESOLUTION_ABSOLUTE.html')>`__.

            :param measurement_function: Specifies the **measurementFunction** used to acquire the measurement.
                The driver sets `
                NIDMM\_ATTR\_FUNCTION <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_FUNCTION.html')>`__
                to this value.
            :type measurement_function: enums.Function
            :param range: Specifies the **range** for the function specified in the
                **Measurement\_Function** parameter. When frequency is specified in the
                **Measurement\_Function** parameter, you must supply the minimum
                frequency expected in the **range** parameter. For example, you must
                type in 100 Hz if you are measuring 101 Hz or higher.
                For all other functions, you must supply a **range** that exceeds the
                value that you are measuring. For example, you must type in 10 V if you
                are measuring 9 V. **range** values are coerced up to the closest input
                **range**. Refer to the `Devices
                Overview <javascript:LaunchHelp('dmm.chm::/devices.html')>`__ for a list
                of valid ranges. The driver sets `
                NIDMM\_ATTR\_RANGE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_RANGE.html')>`__
                to this value. The default is 0.02 V.
                .. note::   The NI 4050, NI 4060, and NI 4065 only support Auto range
                when the trigger and sample trigger are set to IMMEDIATE.
                NIDMM\_VAL\_AUTO\_RANGE\_ON
                -1.0
                NI-DMM performs an Auto range before acquiring the measurement.
                NIDMM\_VAL\_AUTO\_RANGE\_OFF
                -2.0
                NI-DMM sets the range to the current `
                NIDMM\_ATTR\_AUTO\_RANGE\_VALUE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_AUTO_RANGE_VALUE.html')>`__
                and uses this range
                for all subsequent measurements until the measurement configuration is
                changed.
                NIDMM\_VAL\_AUTO\_RANGE\_ONCE
                -3.0
                NI-DMM performs an Auto range before acquiring the measurement. The `
                NIDMM\_ATTR\_AUTO\_RANGE\_VALUE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_AUTO_RANGE_VALUE.html')>`__
                is stored and used for all subsequent measurements until the measurement
                configuration is changed.
            :type range: ViReal64
            :param resolution_absolute: Specifies the absolute resolution for the measurement. NI-DMM sets `
                NIDMM\_ATTR\_RESOLUTION\_ABSOLUTE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_RESOLUTION_ABSOLUTE.html')>`__
                to this value. This parameter is ignored when the **Range** parameter is
                set to NIDMM\_VAL\_AUTO\_RANGE\_ON (-1.0) or
                NIDMM\_VAL\_AUTO\_RANGE\_ONCE (-3.0). The default is 0.001 V.
                .. note::   NI-DMM ignores this parameter for capacitance and inductance
                measurements on the NI 4072. To achieve better resolution for such
                measurements, use the `
                NIDMM\_ATTR\_LC\_NUMBER\_MEAS\_TO\_AVERAGE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_LC_NUMBER_MEAS_TO_AVERAGE.html')>`__
                attribute.
            :type resolution_absolute: ViReal64
        '''
        if type(measurement_function) is not enums.Function:
            raise TypeError('Parameter mode must be of type ' + str(enums.Function))
        error_code = self.library.niDMM_ConfigureMeasurementAbsolute(self.vi, measurement_function.value, range, resolution_absolute)
        errors._handle_error(self, error_code)
        return

    def configure_measurement_digits(self, measurement_function, range, resolution_digits):
        '''.. function:: configure_measurement_digits(measurement_function, range, resolution_digits)

            ViStatus = niDMM\_ConfigureMeasurementDigits(ViSession
            Instrument\_Handle, ViInt32 Measurement\_Function, ViReal64 Range,
            ViReal64 Resolution\_Digits)

            Purpose
            -------

            Configures the common attributes of the measurement. These attributes
            include `
            NIDMM\_ATTR\_FUNCTION <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_FUNCTION.html')>`__,
            `
            NIDMM\_ATTR\_RANGE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_RANGE.html')>`__,
            and `
            NIDMM\_ATTR\_RESOLUTION\_DIGITS <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_RESOLUTION_DIGITS.html')>`__.

            :param measurement_function: Specifies the **measurementFunction** used to acquire the measurement.
                The driver sets `
                NIDMM\_ATTR\_FUNCTION <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_FUNCTION.html')>`__
                to this value.
            :type measurement_function: enums.Function
            :param range: Specifies the range for the function specified in the
                **Measurement\_Function** parameter. When frequency is specified in the
                **Measurement\_Function** parameter, you must supply the minimum
                frequency expected in the **range** parameter. For example, you must
                type in 100 Hz if you are measuring 101 Hz or higher.
                For all other functions, you must supply a range that exceeds the value
                that you are measuring. For example, you must type in 10 V if you are
                measuring 9 V. range values are coerced up to the closest input range.
                Refer to the `Devices
                Overview <javascript:LaunchHelp('dmm.chm::/devices.html')>`__ for a list
                of valid ranges. The driver sets `
                NIDMM\_ATTR\_RANGE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_RANGE.html')>`__
                to this value. The default is 0.02 V.
                .. note::   The NI 4050, NI 4060, and NI 4065 only support Auto range
                when the trigger and sample trigger are set to IMMEDIATE.
                NIDMM\_VAL\_AUTO\_RANGE\_ON
                -1.0
                NI-DMM performs an Auto range before acquiring the measurement.
                NIDMM\_VAL\_AUTO\_RANGE\_OFF
                -2.0
                NI-DMM sets the range to the current `
                NIDMM\_ATTR\_AUTO\_RANGE\_VALUE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_AUTO_RANGE_VALUE.html')>`__
                and uses this range
                for all subsequent measurements until the measurement configuration is
                changed.
                NIDMM\_VAL\_AUTO\_RANGE\_ONCE
                -3.0
                NI-DMM performs an Auto range before acquiring the measurement. The `
                NIDMM\_ATTR\_AUTO\_RANGE\_VALUE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_AUTO_RANGE_VALUE.html')>`__
                is stored and used for all subsequent measurements until the measurement
                configuration is changed.
            :type range: ViReal64
            :param resolution_digits: Specifies the resolution of the measurement in digits. The driver sets
                the `Devices
                Overview <javascript:LaunchHelp('dmm.chm::/devices.html')>`__ for a list
                of valid ranges. The driver sets `
                NIDMM\_ATTR\_RESOLUTION\_DIGITS <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_RESOLUTION_DIGITS.html')>`__
                attribute to this value. This parameter is ignored when the **Range**
                parameter is set to NIDMM\_VAL\_AUTO\_RANGE\_ON (-1.0) or
                NIDMM\_VAL\_AUTO\_RANGE\_ONCE (-3.0). The default is 5½.
                .. note::   NI-DMM ignores this parameter for capacitance and inductance
                measurements on the NI 4072. To achieve better resolution for such
                measurements, use the `
                NIDMM\_ATTR\_LC\_NUMBER\_MEAS\_TO\_AVERAGE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_LC_NUMBER_MEAS_TO_AVERAGE.html')>`__
                attribute.
            :type resolution_digits: ViReal64
        '''
        if type(measurement_function) is not enums.Function:
            raise TypeError('Parameter mode must be of type ' + str(enums.Function))
        error_code = self.library.niDMM_ConfigureMeasurementDigits(self.vi, measurement_function.value, range, resolution_digits)
        errors._handle_error(self, error_code)
        return

    def configure_multi_point(self, trigger_count, sample_count, sample_trigger, sample_interval):
        '''.. function:: configure_multi_point(trigger_count, sample_count, sample_trigger, sample_interval)

            Purpose
            -------

            Configures the attributes for multipoint measurements. These attributes
            include `
            NIDMM\_ATTR\_TRIGGER\_COUNT <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_TRIGGER_COUNT.html')>`__,
            `
            NIDMM\_ATTR\_SAMPLE\_COUNT <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_SAMPLE_COUNT.html')>`__,
            `
            NIDMM\_ATTR\_SAMPLE\_TRIGGER <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_SAMPLE_TRIGGER.html')>`__,
            and `
            NIDMM\_ATTR\_SAMPLE\_INTERVAL <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_SAMPLE_INTERVAL.html')>`__.

            For continuous acquisitions, set `
            NIDMM\_ATTR\_TRIGGER\_COUNT <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_TRIGGER_COUNT.html')>`__
            or `
            NIDMM\_ATTR\_SAMPLE\_COUNT <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_SAMPLE_COUNT.html')>`__
            to zero. For more information, refer to `Multiple Point
            Acquisitions <javascript:LaunchHelp('dmm.chm::/multi_point.html')>`__,
            `Triggering <javascript:LaunchHelp('dmm.chm::/trigger.html')>`__, and
            `Using
            Switches <javascript:LaunchHelp('dmm.chm::/switch_selection.html')>`__.

            :param trigger_count: Sets the number of triggers you want the DMM to receive before returning
                to the Idle state. The driver sets `
                NIDMM\_ATTR\_TRIGGER\_COUNT <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_TRIGGER_COUNT.html')>`__
                to this value. The default value is 1.
            :type trigger_count: ViInt32
            :param sample_count: Sets the number of measurements the DMM makes in each measurement
                sequence initiated by a trigger. The driver sets `
                NIDMM\_ATTR\_SAMPLE\_COUNT <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_SAMPLE_COUNT.html')>`__
                to this value. The default value is 1.
            :type sample_count: ViInt32
            :param sample_trigger: Specifies the **sampleTrigger** source you want to use. The driver sets
                `
                NIDMM\_ATTR\_SAMPLE\_TRIGGER <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'caNIDMM_ATTR_SAMPLE_TRIGGER.html')>`__
                to this value. The default is Immediate.
                .. note::   To determine which values are supported by each device,
                refer to the `LabWindows/CVI Trigger
                Routing <javascript:LaunchHelp('dmm.chm::/CVItrigger_routing.html')>`__
                section.
            :type sample_trigger: enums.SampleTrigger
            :param sample_interval: Sets the amount of time in seconds the DMM waits between measurement
                cycles. The driver sets `
                NIDMM\_ATTR\_SAMPLE\_INTERVAL <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'caNIDMM_ATTR_SAMPLE_INTERVAL.html')>`__
                to this value. Specify a sample interval to add settling time between
                measurement cycles or to decrease the measurement rate.
                **sampleInterval** only applies when the **Sample\_Trigger** is set to
                INTERVAL.

                On the NI 4060, the **sampleInterval** value is used as the settling
                time. When sample interval is set to 0, the DMM does not settle between
                measurement cycles. The NI 4065 and NI 4070/4071/4072 use the value
                specified in **sampleInterval** as additional delay. The default value
                (-1) ensures that the DMM settles for a recommended time. This is the
                same as using an Immediate trigger.

                .. note::   This attribute is not used on the NI 4080/4081/4082 and the
                NI 4050.
            :type sample_interval: ViReal64
        '''
        if type(sample_trigger) is not enums.SampleTrigger:
            raise TypeError('Parameter mode must be of type ' + str(enums.SampleTrigger))
        error_code = self.library.niDMM_ConfigureMultiPoint(self.vi, trigger_count, sample_count, sample_trigger.value, sample_interval)
        errors._handle_error(self, error_code)
        return

    def configure_offset_comp_ohms(self, offset_comp_ohms):
        '''.. function:: configure_offset_comp_ohms(offset_comp_ohms)

            For NI 4080/4081/4082 and NI 4070/4071/4072, allows the DMM to
            compensate for voltage offsets in resistance measurements. When
            **Offset\_Comp\_Ohms** is enabled, the DMM measures the resistance twice
            (once with the current source on and again with it turned off). Any
            voltage offset present in both measurements is cancelled out.
            **Offset\_Comp\_Ohms** is useful when measuring resistance values less
            than 10 KΩ.

            :param offset_comp_ohms: Enables or disables **offsetCompOhms**. The driver sets `
                NIDMM\_ATTR\_OFFSET\_COMP\_OHMS <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_OFFSET_COMP_OHMS.html')>`__
                to this value.
                +-------------------------------------------------+---------+--------------------------------------+
                | Name                                            | Value   | Description                          |
                +=================================================+=========+======================================+
                | NIDMM\_VAL\_OFFSET\_COMP\_OHMS\_OFF (default)   | 0       | Off disables \ **offsetCompOhms**.   |
                +-------------------------------------------------+---------+--------------------------------------+
                | NIDMM\_VAL\_OFFSET\_COMP\_OHMS\_ON              | 1       | On enables **offsetCompOhms**.       |
                +-------------------------------------------------+---------+--------------------------------------+
            :type offset_comp_ohms: enums.EnabledSetting
        '''
        if type(offset_comp_ohms) is not enums.EnabledSetting:
            raise TypeError('Parameter mode must be of type ' + str(enums.EnabledSetting))
        error_code = self.library.niDMM_ConfigureOffsetCompOhms(self.vi, offset_comp_ohms.value)
        errors._handle_error(self, error_code)
        return

    def configure_open_cable_comp_values(self, conductance, susceptance):
        '''.. function:: configure_open_cable_comp_values(conductance, susceptance)

            Purpose
            -------

            For the NI 4082 and NI 4072 only, configures the `
            NIDMM\_ATTR\_OPEN\_CABLE\_COMP\_CONDUCTANCE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'caNIDMM_ATTR_OPEN_CABLE_COMP_CONDUCTANCE.html')>`__
            and `
            NIDMM\_ATTR\_OPEN\_CABLE\_COMP\_SUSCEPTANCE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'caNIDMM_ATTR_OPEN_CABLE_COMP_SUSCEPTANCE.html')>`__
            attributes.

            :param conductance: Specifies the open cable compensation **conductance**.
            :type conductance: ViReal64
            :param susceptance: Specifies the open cable compensation **susceptance**.
            :type susceptance: ViReal64
        '''
        error_code = self.library.niDMM_ConfigureOpenCableCompValues(self.vi, conductance, susceptance)
        errors._handle_error(self, error_code)
        return

    def configure_power_line_frequency(self, power_line_frequency_hz):
        '''.. function:: configure_power_line_frequency(power_line_frequency_hz)

            Specifies the powerline frequency.

            :param power_line_frequency_hz: **Powerline Frequency** specifies the powerline frequency in hertz.
                NI-DMM sets the Powerline Frequency property to this value.
            :type power_line_frequency_hz: ViReal64
        '''
        error_code = self.library.niDMM_ConfigurePowerLineFrequency(self.vi, power_line_frequency_hz)
        errors._handle_error(self, error_code)
        return

    def configure_rtd_custom(self, rtd_a, rtd_b, rtd_c):
        '''.. function:: configure_rtd_custom(rtd_a, rtd_b, rtd_c)

            Configures the A, B, and C parameters for a custom RTD.

            :param rtd_a: Specifies the Callendar-Van Dusen A coefficient for RTD scaling when RTD
                Type parameter is set to Custom in the `
                niDMM\_ConfigureRTDType <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_ConfigureRTDType.html')>`__
                function. The default is 3.9083e-3 (Pt3851)
            :type rtd_a: ViReal64
            :param rtd_b: Specifies the Callendar-Van Dusen B coefficient for RTD scaling when RTD
                Type parameter is set to Custom in the `
                niDMM\_ConfigureRTDType <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_ConfigureRTDType.html')>`__
                function. The default is -5.775e-7 (Pt3851).
            :type rtd_b: ViReal64
            :param rtd_c: Specifies the Callendar-Van Dusen C coefficient for RTD scaling when RTD
                Type parameter is set to Custom in the `
                niDMM\_ConfigureRTDType <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_ConfigureRTDType.html')>`__
                function. The default is -4.183e-12 (Pt3851).
            :type rtd_c: ViReal64
        '''
        error_code = self.library.niDMM_ConfigureRTDCustom(self.vi, rtd_a, rtd_b, rtd_c)
        errors._handle_error(self, error_code)
        return

    def configure_rtd_type(self, rtd_type, rtd_resistance):
        '''.. function:: configure_rtd_type(rtd_type, rtd_resistance)

            Configures the RTD Type and RTD Resistance parameters for an RTD.

            :param rtd_type: Specifies the type of RTD used to measure the temperature resistance.
                NI-DMM uses this value to set the RTD Type property. The default is
                NIDMM\_VAL\_TEMP\_RTD\_PT3851.
                Enum
                Standards
                Material
                TCR (α)
                Typical R\ :sub:`0` (Ω)
                Callendar-Van Dusen Coefficient
                Notes
                NIDMM\_VAL\_TEMP\_RTD\_PT3851
                IEC-751
                DIN 43760
                BS 1904
                ASTM-E1137
                EN-60751
                Platinum
                .003851
                100 Ω
                1000 Ω
                A = 3.9083 × 10\ :sup:`–3`
                B = –5.775×10:sup:`–7`
                C = –4.183×10:sup:`–12`
                Most common RTDs
                NIDMM\_VAL\_TEMP\_RTD\_PT3750
                Low-cost vendor compliant RTD\*
                Platinum
                .003750
                1000 Ω
                A = 3.81 × 10\ :sup:`–3`
                B = –6.02×10:sup:`–7`
                C = –6.0×10:sup:`–12`
                Low-cost RTD
                NIDMM\_VAL\_TEMP\_RTD\_PT3916
                JISC 1604
                Platinum
                .003916
                100 Ω
                A = 3.9739 × 10\ :sup:`–3`
                B = –5.870×10:sup:`–7`
                C = –4.4 ×10\ :sup:`–12`
                Used in primarily in Japan
                NIDMM\_VAL\_TEMP\_RTD\_PT3920
                US Industrial Standard D-100
                American
                Platinum
                .003920
                100 Ω
                A = 3.9787 × 10\ :sup:`–3`
                B = –5.8686×10:sup:`–7`
                C = –4.167 ×10\ :sup:`–12`
                Low-cost RTD
                NIDMM\_VAL\_TEMP\_RTD\_PT3911
                US Industrial Standard
                American
                Platinum
                .003911
                100 Ω
                A = 3.9692 × 10\ :sup:`–3`
                B = –5.8495×10:sup:`–7`
                C = –4.233 ×10\ :sup:`–12`
                Low-cost RTD
                NIDMM\_VAL\_TEMP\_RTD\_PT3928
                ITS-90
                Platinum
                .003928
                100 Ω
                A = 3.9888 × 10\ :sup:`–3`
                B = –5.915×10:sup:`–7`
                C = –3.85 ×10\ :sup:`–12`
                The definition of temperature
                \*No standard. Check the TCR.
            :type rtd_type: ViInt32
            :param rtd_resistance: Specifies the RTD resistance in ohms at 0 °C. NI-DMM uses this value to
                set the RTD Resistance property. The default is 100 (Ω).
            :type rtd_resistance: ViReal64
        '''
        error_code = self.library.niDMM_ConfigureRTDType(self.vi, rtd_type, rtd_resistance)
        errors._handle_error(self, error_code)
        return

    def configure_sample_trigger_slope(self, sample_trigger_slope):
        '''.. function:: configure_sample_trigger_slope(sample_trigger_slope)

            Sets the `
            NIDMM\_ATTR\_SAMPLE\_TRIGGER\_SLOPE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_SAMPLE_TRIGGER_SLOPE.html')>`__
            to either rising edge (positive) or falling edge (negative) polarity.

            :param sample_trigger_slope: Specifies the polarity of the Trigger signal on which the measurement is
                triggered for values of either NIDMM\_VAL\_POSITIVE or
                NIDMM\_VAL\_NEGATIVE. The driver sets `
                NIDMM\_ATTR\_SAMPLE\_TRIGGER\_SLOPE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_SAMPLE_TRIGGER_SLOPE.html')>`__
                to this value.
                +--------------------------+-----+------------------------+------------------------------------------------------------------+
                | Rising Edge              | 0   | NIDMM\_VAL\_POSITIVE   | The driver triggers on the rising edge of the trigger signal.    |
                +--------------------------+-----+------------------------+------------------------------------------------------------------+
                | Falling Edge (default)   | 1   | NIDMM\_VAL\_NEGATIVE   | The driver triggers on the falling edge of the trigger signal.   |
                +--------------------------+-----+------------------------+------------------------------------------------------------------+
            :type sample_trigger_slope: enums.Slope
        '''
        if type(sample_trigger_slope) is not enums.Slope:
            raise TypeError('Parameter mode must be of type ' + str(enums.Slope))
        error_code = self.library.niDMM_ConfigureSampleTriggerSlope(self.vi, sample_trigger_slope.value)
        errors._handle_error(self, error_code)
        return

    def configure_short_cable_comp_values(self, resistance, reactance):
        '''.. function:: configure_short_cable_comp_values(resistance, reactance)

            Purpose
            -------

            For the NI 4082 and NI 4072 only, configures the
            `NIDMM\_ATTR\_SHORT\_CABLE\_COMP\_RESISTANCE <javascript:LaunchHelp('dmmcref.chm::/caNIDMM_ATTR_SHORT_CABLE_COMP_RESISTANCE.html')>`__
            and
            `NIDMM\_ATTR\_SHORT\_CABLE\_COMP\_REACTANCE <javascript:LaunchHelp('dmmcref.chm::/caNIDMM_ATTR_SHORT_CABLE_COMP_REACTANCE.html')>`__
            attributes.

            :param resistance: Specifies the short cable compensation **resistance**.
            :type resistance: ViReal64
            :param reactance: Specifies the short cable compensation **reactance**.
            :type reactance: ViReal64
        '''
        error_code = self.library.niDMM_ConfigureShortCableCompValues(self.vi, resistance, reactance)
        errors._handle_error(self, error_code)
        return

    def configure_thermistor_custom(self, thermistor_a, thermistor_b, thermistor_c):
        '''.. function:: configure_thermistor_custom(thermistor_a, thermistor_b, thermistor_c)

            Configures the A, B, and C parameters for a custom thermistor.

            :param thermistor_a: Specifies the Steinhart-Hart A coefficient for thermistor scaling when
                Thermistor Type is set to Custom in the `
                niDMM\_ConfigureThermistorType <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_ConfigureThermistorType.html')>`__
                function. The default is 1.0295e-3 (44006).
            :type thermistor_a: ViReal64
            :param thermistor_b: Specifies the Steinhart-Hart B coefficient for thermistor scaling when
                Thermistor Type is set to Custom in the `
                niDMM\_ConfigureThermistorType <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_ConfigureThermistorType.html')>`__
                function. The default is 2.391e-4 (44006).
            :type thermistor_b: ViReal64
            :param thermistor_c: Specifies the Steinhart-Hart C coefficient for thermistor scaling when
                Thermistor Type is set to Custom in the `
                niDMM\_ConfigureThermistorType <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_ConfigureThermistorType.html')>`__
                function. The default is 1.568e-7 (44006).
            :type thermistor_c: ViReal64
        '''
        error_code = self.library.niDMM_ConfigureThermistorCustom(self.vi, thermistor_a, thermistor_b, thermistor_c)
        errors._handle_error(self, error_code)
        return

    def configure_thermistor_type(self, thermistor_type):
        '''.. function:: configure_thermistor_type(thermistor_type)

            Configures the thermistor type.

            :param thermistor_type: Specifies the type of thermistor used to measure the temperature. NI-DMM
                uses this value to set the Thermistor Type property. The default is
                NIDMM\_VAL\_TEMP\_THERMISTOR\_44006.

                +--------------------+--------------------+--------------------+--------------------+
                | **Defined Values** | **Thermistor       | **Value**          | **25 °C            |
                |                    | Type**             |                    | Resistance**       |
                +--------------------+--------------------+--------------------+--------------------+
                | NIDMM\_VAL\_TEMP\_ | Custom             | 0                  | —                  |
                | THERMISTOR\_CUSTOM |                    |                    |                    |
                +--------------------+--------------------+--------------------+--------------------+
                | NIDMM\_VAL\_TEMP\_ | 44004              | 1                  | 2.25 kΩ            |
                | THERMISTOR\_44004  |                    |                    |                    |
                +--------------------+--------------------+--------------------+--------------------+
                | NIDMM\_VAL\_TEMP\_ | 44006              | 2                  | 10 kΩ              |
                | THERMISTOR\_44006  |                    |                    |                    |
                +--------------------+--------------------+--------------------+--------------------+
                | NIDMM\_VAL\_TEMP\_ | 44007              | 3                  | 5 kΩ               |
                | THERMISTOR\_44007  |                    |                    |                    |
                +--------------------+--------------------+--------------------+--------------------+
            :type thermistor_type: enums.TemperatureThermistorType
        '''
        if type(thermistor_type) is not enums.TemperatureThermistorType:
            raise TypeError('Parameter mode must be of type ' + str(enums.TemperatureThermistorType))
        error_code = self.library.niDMM_ConfigureThermistorType(self.vi, thermistor_type.value)
        errors._handle_error(self, error_code)
        return

    def configure_thermocouple(self, thermocouple_type, reference_junction_type):
        '''.. function:: configure_thermocouple(thermocouple_type, reference_junction_type)

            Configures the thermocouple type and reference junction type for a
            chosen thermocouple.

            :param thermocouple_type: Specifies the type of thermocouple used to measure the temperature.
                NI-DMM uses this value to set the Thermocouple Type property. The
                default is NIDMM\_VAL\_TEMP\_TC\_J.
                +---------------------------+-----------------------+
                | NIDMM\_VAL\_TEMP\_TC\_B   | Thermocouple type B   |
                +---------------------------+-----------------------+
                | NIDMM\_VAL\_TEMP\_TC\_E   | Thermocouple type E   |
                +---------------------------+-----------------------+
                | NIDMM\_VAL\_TEMP\_TC\_J   | Thermocouple type J   |
                +---------------------------+-----------------------+
                | NIDMM\_VAL\_TEMP\_TC\_K   | Thermocouple type K   |
                +---------------------------+-----------------------+
                | NIDMM\_VAL\_TEMP\_TC\_N   | Thermocouple type N   |
                +---------------------------+-----------------------+
                | NIDMM\_VAL\_TEMP\_TC\_R   | Thermocouple type R   |
                +---------------------------+-----------------------+
                | NIDMM\_VAL\_TEMP\_TC\_S   | Thermocouple type S   |
                +---------------------------+-----------------------+
                | NIDMM\_VAL\_TEMP\_TC\_T   | Thermocouple type T   |
                +---------------------------+-----------------------+
            :type thermocouple_type: ViInt32
            :param reference_junction_type: Specifies the type of reference junction to be used in the reference
                junction compensation of a thermocouple measurement. NI-DMM uses this
                value to set the Reference Junction Type property. The only supported
                value is NIDMM\_VAL\_TEMP\_REF\_JUNC\_FIXED.
            :type reference_junction_type: ViInt32
        '''
        error_code = self.library.niDMM_ConfigureThermocouple(self.vi, thermocouple_type, reference_junction_type)
        errors._handle_error(self, error_code)
        return

    def configure_transducer_type(self, transducer_type):
        '''.. function:: configure_transducer_type(transducer_type)

            Configures the transducer type.

            :param transducer_type: Specifies the type of device used to measure the temperature. NI-DMM
                uses this value to set the Transducer Type property. The default is
                NIDMM\_VAL\_THERMOCOUPLE.
                +----------------------------+----------------+
                | NIDMM\_VAL\_2\_WIRE\_RTD   | 2-wire RTD     |
                +----------------------------+----------------+
                | NIDMM\_VAL\_4\_WIRE\_RTD   | 4-wire RTD     |
                +----------------------------+----------------+
                | NIDMM\_VAL\_THERMISTOR     | Thermistor     |
                +----------------------------+----------------+
                | NIDMM\_VAL\_THERMOCOUPLE   | Thermocouple   |
                +----------------------------+----------------+
            :type transducer_type: enums.TemperatureTransducerType
        '''
        if type(transducer_type) is not enums.TemperatureTransducerType:
            raise TypeError('Parameter mode must be of type ' + str(enums.TemperatureTransducerType))
        error_code = self.library.niDMM_ConfigureTransducerType(self.vi, transducer_type.value)
        errors._handle_error(self, error_code)
        return

    def configure_trigger(self, trigger_source, trigger_delay):
        '''.. function:: configure_trigger(trigger_source, trigger_delay)

            Purpose
            -------

            Configures the DMM **Trigger\_Source** and **Trigger\_Delay**. Refer to
            `Triggering <javascript:LaunchHelp('dmm.chm::/trigger.html')>`__ and
            `Using
            Switches <javascript:LaunchHelp('dmm.chm::/switch_selection.html')>`__
            for more information.

            :param trigger_source: Specifies the **triggerSource** that initiates the acquisition. The
                driver sets `
                NIDMM\_ATTR\_TRIGGER\_SOURCE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'caNIDMM_ATTR_TRIGGER_SOURCE.html')>`__
                to this value. Software configures the DMM to wait until `
                niDMM\_SendSoftwareTrigger <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'cviniDMM_SendSoftwareTrigger.html')>`__
                is called before triggering the DMM.
                .. note::   To determine which values are supported by each device,
                refer to the `LabWindows/CVI Trigger
                Routing <javascript:LaunchHelp('dmm.chm::/CVItrigger_routing.html')>`__
                section.
            :type trigger_source: enums.TriggerSource
            :param trigger_delay: Specifies the time that the DMM waits after it has received a trigger
                before taking a measurement. The driver sets the
                `NIDMM\_ATTR\_TRIGGER\_DELAY <javascript:LaunchHelp('dmmcref.chm::/caNIDMM_ATTR_TRIGGER_DELAY.html')>`__
                attribute to this value. By default, **triggerDelay** is
                NIDMM\_VAL\_AUTO\_DELAY (-1), which means the DMM waits an appropriate
                settling time before taking the measurement. On the NI 4060, if you set
                **triggerDelay** to 0, the DMM does not settle before taking the
                measurement. The NI 4065 and NI 4070/4071/4072 use the value specified
                in **triggerDelay** as additional settling time. .. note::   When using
                the NI 4050, **triggerDelay** must be set to NIDMM\_VAL\_AUTO\_DELAY
                (-1).
            :type trigger_delay: ViReal64
        '''
        if type(trigger_source) is not enums.TriggerSource:
            raise TypeError('Parameter mode must be of type ' + str(enums.TriggerSource))
        error_code = self.library.niDMM_ConfigureTrigger(self.vi, trigger_source.value, trigger_delay)
        errors._handle_error(self, error_code)
        return

    def configure_trigger_slope(self, trigger_slope):
        '''.. function:: configure_trigger_slope(trigger_slope)

            Sets the `
            NIDMM\_ATTR\_TRIGGER\_SLOPE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_TRIGGER_SLOPE.html')>`__
            attribute to either rising edge (positive) or falling edge (negative)
            polarity.

            :param trigger_slope: Specifies the polarity of the trigger signal on which the measurement is
                triggered for values of either NIDMM\_VAL\_POSITIVE or
                NIDMM\_VAL\_NEGATIVE. The driver sets the `
                NIDMM\_ATTR\_TRIGGER\_SLOPE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_TRIGGER_SLOPE.html')>`__
                attribute to this value.
                +----------------------------------+-----+------------------------------------------------------------------+
                | NIDMM\_VAL\_POSITIVE             | 0   | The driver triggers on the rising edge of the trigger signal.    |
                +----------------------------------+-----+------------------------------------------------------------------+
                | NIDMM\_VAL\_NEGATIVE (default)   | 1   | The driver triggers on the falling edge of the trigger signal.   |
                +----------------------------------+-----+------------------------------------------------------------------+
            :type trigger_slope: enums.Slope
        '''
        if type(trigger_slope) is not enums.Slope:
            raise TypeError('Parameter mode must be of type ' + str(enums.Slope))
        error_code = self.library.niDMM_ConfigureTriggerSlope(self.vi, trigger_slope.value)
        errors._handle_error(self, error_code)
        return

    def configure_waveform_acquisition(self, measurement_function, range, rate, waveform_points):
        '''.. function:: configure_waveform_acquisition(measurement_function, range, rate, waveform_points)

            Configures the DMM for waveform acquisitions. This feature is supported
            on the NI 4080/4081/4082 and the NI 4070/4071/4072.

            :param measurement_function: Specifies the **measurementFunction** used in a waveform acquisition.
                The driver sets `
                NIDMM\_ATTR\_FUNCTION <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'caNIDMM_ATTR_FUNCTION.html')>`__
                to this value.
                +-------------------------------------------+--------+--------------------+
                | NIDMM\_VAL\_WAVEFORM\_VOLTAGE (default)   | 1003   | Voltage Waveform   |
                +-------------------------------------------+--------+--------------------+
                | NIDMM\_VAL\_WAVEFORM\_CURRENT             | 1004   | Current Waveform   |
                +-------------------------------------------+--------+--------------------+
            :type measurement_function: enums.Function
            :param range: Specifies the expected maximum amplitude of the input signal and sets
                the **range** for the **Measurement\_Function**. NI-DMM sets `
                NIDMM\_ATTR\_RANGE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'caNIDMM_ATTR_RANGE.html')>`__
                to this value. **range** values are coerced up to the closest input
                **range**. The default is 10.0.

                For valid ranges refer to the topics in
                `Devices <javascript:LaunchHelp('dmm.chm::/Devices.html')>`__.

                Auto-ranging is not supported during waveform acquisitions.
            :type range: ViReal64
            :param rate: Specifies the **rate** of the acquisition in samples per second. NI-DMM
                sets `
                NIDMM\_ATTR\_WAVEFORM\_RATE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'caNIDMM_ATTR_WAVEFORM_RATE.html')>`__
                to this value.

                The valid **Range** is 10.0–1,800,000 S/s. **rate** values are coerced
                to the closest integer divisor of 1,800,000. The default value is
                1,800,000.
            :type rate: ViReal64
            :param waveform_points: Specifies the number of points to acquire before the waveform
                acquisition completes. NI-DMM sets `
                NIDMM\_ATTR\_WAVEFORM\_POINTS <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'caNIDMM_ATTR_WAVEFORM_POINTS.html')>`__
                to this value.

                To calculate the maximum and minimum number of waveform points that you
                can acquire in one acquisition, refer to the `Waveform Acquisition
                Measurement
                Cycle <javascript:LaunchHelp('dmm.chm::/waveform_cycle.html')>`__.

                The default value is 500.
            :type waveform_points: ViInt32
        '''
        if type(measurement_function) is not enums.Function:
            raise TypeError('Parameter mode must be of type ' + str(enums.Function))
        error_code = self.library.niDMM_ConfigureWaveformAcquisition(self.vi, measurement_function.value, range, rate, waveform_points)
        errors._handle_error(self, error_code)
        return

    def configure_waveform_coupling(self, waveform_coupling):
        '''.. function:: configure_waveform_coupling(waveform_coupling)

            For the NI 4080/4081/4082 and the NI 4070/4071/4072, configures
            instrument coupling for voltage waveforms.

            :param waveform_coupling: Selects DC or AC coupling. The driver sets `
                NIDMM\_ATTR\_WAVEFORM\_COUPLING <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'caNIDMM_ATTR_WAVEFORM_COUPLING.html')>`__
                to this value.
                +------------------------------------------------+---------+---------------+
                | Name                                           | Value   | Description   |
                +================================================+=========+===============+
                | NIDMM\_VAL\_WAVEFORM\_COUPLING\_AC             | 0       | AC coupling   |
                +------------------------------------------------+---------+---------------+
                | NIDMM\_VAL\_WAVEFORM\_COUPLING\_DC (default)   | 1       | DC coupling   |
                +------------------------------------------------+---------+---------------+
            :type waveform_coupling: enums.WaveformCouplingMode
        '''
        if type(waveform_coupling) is not enums.WaveformCouplingMode:
            raise TypeError('Parameter mode must be of type ' + str(enums.WaveformCouplingMode))
        error_code = self.library.niDMM_ConfigureWaveformCoupling(self.vi, waveform_coupling.value)
        errors._handle_error(self, error_code)
        return

    def disable(self):
        '''.. function:: disable()

            Places the instrument in a quiescent state where it has minimal or no
            impact on the system to which it is connected. If a measurement is in
            progress when this function is called, the measurement is aborted.
        '''
        error_code = self.library.niDMM_Disable(self.vi)
        errors._handle_error(self, error_code)
        return

    def fetch(self, maximum_time):
        '''.. function:: fetch(maximum_time, reading)

            Purpose
            -------

            Returns the value from a previously initiated measurement. You must call
            `
            niDMM\_Initiate <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'cviniDMM_Initiate.html')>`__
            before calling this function.

            :param maximum_time: Specifies the **maximumTime** allowed for this function to complete in
                milliseconds. If the function does not complete within this time
                interval, the function returns the NIDMM\_ERROR\_MAX\_TIME\_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                NIDMM\_VAL\_TIME\_LIMIT\_AUTO (-1). The DMM calculates the timeout
                automatically.
            :type maximum_time: ViInt32

            :rtype: ViReal64
        '''
        reading_ctype = ctypes_types.ViReal64_ctype(0)
        error_code = self.library.niDMM_Fetch(self.vi, maximum_time, ctypes.pointer(reading_ctype))
        errors._handle_error(self, error_code)
        return reading_ctype.value

    def fetch_multi_point(self, maximum_time, array_size):
        '''.. function:: fetch_multi_point(maximum_time, array_size, reading_array, actual_number_of_points)

            Purpose
            -------

            Returns an array of values from a previously initiated multipoint
            measurement. The number of measurements the DMM makes is determined by
            the values you specify for the **Trigger\_Count** and **Sample\_Count**
            parameters of `
            niDMM\_ConfigureMultiPoint <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'cviniDMM_ConfigureMultiPoint.html')>`__.
            You must first call `
            niDMM\_Initiate <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'cviniDMM_Initiate.html')>`__
            to initiate a measurement before calling this function.

            :param maximum_time: Specifies the **maximumTime** allowed for this function to complete in
                milliseconds. If the function does not complete within this time
                interval, the function returns the NIDMM\_ERROR\_MAX\_TIME\_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                NIDMM\_VAL\_TIME\_LIMIT\_AUTO (-1). The DMM calculates the timeout
                automatically.
            :type maximum_time: ViInt32
            :param array_size: Specifies the number of measurements to acquire. The maximum number of
                measurements for a finite acquisition is the (**Trigger Count** x
                **Sample Count**) parameters in `
                niDMM\_ConfigureMultiPoint <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_ConfigureMultiPoint.html')>`__.

                For continuous acquisitions, up to 100,000 points can be returned at
                once. The number of measurements can be a subset. The valid range is any
                positive ViInt32. The default value is 1.
            :type array_size: ViInt32

            :rtype: tuple (reading_array, actual_number_of_points)
                WHERE
                reading_array (ViReal64): An array of measurement values.
                    +------------+-----------------------------------------------------------------------------------------------------------------------------+
                    | |image0|   | **Note**   The size of the **readingArray** must be at least the size that you specify for the **Array\_Size** parameter.   |
                    +------------+-----------------------------------------------------------------------------------------------------------------------------+

                    .. |image0| image:: note.gif
                actual_number_of_points (ViInt32): Indicates the number of measured values actually retrieved from the DMM.
        '''
        reading_array_ctype = ctypes_types.ViReal64_ctype(0)  # TODO(marcoskirsch): allocate a buffer
        actual_number_of_points_ctype = ctypes_types.ViInt32_ctype(0)
        error_code = self.library.niDMM_FetchMultiPoint(self.vi, maximum_time, array_size, ctypes.pointer(reading_array_ctype), ctypes.pointer(actual_number_of_points_ctype))
        errors._handle_error(self, error_code)
        return reading_array_ctype.value, actual_number_of_points_ctype.value

    def fetch_waveform(self, maximum_time, array_size):
        '''.. function:: fetch_waveform(maximum_time, array_size, waveform_array, actual_number_of_points)

            For the NI 4080/4081/4082 and the NI 4070/4071/4072, returns an array of
            values from a previously initiated waveform acquisition. You must call `
            niDMM\_Initiate <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_Initiate.html')>`__
            before calling this function.

            :param maximum_time: Specifies the **maximumTime** allowed for this function to complete in
                milliseconds. If the function does not complete within this time
                interval, the function returns the NIDMM\_ERROR\_MAX\_TIME\_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                NIDMM\_VAL\_TIME\_LIMIT\_AUTO (-1). The DMM calculates the timeout
                automatically.
            :type maximum_time: ViInt32
            :param array_size: Specifies the number of waveform points to return. You specify the total
                number of points that the DMM acquires in the **Waveform Points**
                parameter of `
                niDMM\_ConfigureWaveformAcquisition <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_ConfigureWaveformAcquisition.htm')>`__.
                The default value is 1.
            :type array_size: ViInt32

            :rtype: tuple (waveform_array, actual_number_of_points)
                WHERE
                waveform_array (ViReal64): **Waveform Array** is an array of measurement values stored in waveform
                    data type.
                actual_number_of_points (ViInt32): Indicates the number of measured values actually retrieved from the DMM.
        '''
        waveform_array_ctype = ctypes_types.ViReal64_ctype(0)  # TODO(marcoskirsch): allocate a buffer
        actual_number_of_points_ctype = ctypes_types.ViInt32_ctype(0)
        error_code = self.library.niDMM_FetchWaveform(self.vi, maximum_time, array_size, ctypes.pointer(waveform_array_ctype), ctypes.pointer(actual_number_of_points_ctype))
        errors._handle_error(self, error_code)
        return waveform_array_ctype.value, actual_number_of_points_ctype.value

    def format_meas_absolute(self, measurement_function, range, resolution, measurement):
        '''.. function:: format_meas_absolute(measurement_function, range, resolution, measurement, mode_string, range_string, data_string)

            Formats the **Measurement** to the proper number of displayed digits
            according to the **Measurement\_Function**, **Range**, and
            **Resolution**. Returns the formatted data, range, and mode strings.

            :param measurement_function: Specifies the **measurementFunction** used to acquire the measurement.
                The driver sets `
                NIDMM\_ATTR\_FUNCTION <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_FUNCTION.html')>`__
                to this value.
            :type measurement_function: ViInt32
            :param range: Specifies the `
                NIDMM\_ATTR\_RANGE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_RANGE.html')>`__
                used to acquire the **Measurement**.
            :type range: ViReal64
            :param resolution: Specifies the `
                NIDMM\_ATTR\_RESOLUTION\_ABSOLUTE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_RESOLUTION_ABSOLUTE.html')>`__
                of the **Measurement**.
            :type resolution: ViReal64
            :param measurement: Specifies the measured value returned from the DMM.
            :type measurement: ViReal64

            :rtype: tuple (mode_string, range_string, data_string)
                WHERE
                mode_string (ViChar): Returns a string containing the units of the **Measurement** mode.
                range_string (ViChar): Returns the `
                    NIDMM\_ATTR\_RANGE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_RANGE.html')>`__
                    of the **Measurement**, formatted into a string with the correct number
                    of display digits.
                data_string (ViChar): Returns the **Measurement**, formatted according to the `
                    NIDMM\_ATTR\_FUNCTION <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_FUNCTION.html')>`__,
                    `
                    NIDMM\_ATTR\_RANGE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_RANGE.html')>`__,
                    and `
                    NIDMM\_ATTR\_RESOLUTION\_ABSOLUTE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_RESOLUTION_ABSOLUTE.html')>`__.
        '''
        mode_string_ctype = ctypes_types.ViChar_ctype(0)  # TODO(marcoskirsch): allocate a buffer
        range_string_ctype = ctypes_types.ViChar_ctype(0)  # TODO(marcoskirsch): allocate a buffer
        data_string_ctype = ctypes_types.ViChar_ctype(0)  # TODO(marcoskirsch): allocate a buffer
        error_code = self.library.niDMM_FormatMeasAbsolute(measurement_function, range, resolution, measurement, ctypes.pointer(mode_string_ctype), ctypes.pointer(range_string_ctype), ctypes.pointer(data_string_ctype))
        errors._handle_error(self, error_code)
        return mode_string_ctype.value.decode("ascii"), range_string_ctype.value.decode("ascii"), data_string_ctype.value.decode("ascii")

    def get_aperture_time_info(self):
        '''.. function:: get_aperture_time_info(aperture_time, aperture_time_units)

            Returns the DMM **Aperture\_Time** and **Aperture\_Time\_Units**.

            :rtype: tuple (aperture_time, aperture_time_units)
                WHERE
                aperture_time (ViReal64): Specifies the amount of time the DMM digitizes the input signal for a
                    single measurement. This parameter does not include settling time.
                    Returns the value of the `
                    NIDMM\_ATTR\_APERTURE\_TIME <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_APERTURE_TIME.html')>`__
                    attribute. The units of this attribute depend on the value of the `
                    NIDMM\_ATTR\_APERTURE\_TIME\_UNITS <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_APERTURE_TIME_UNITS.html')>`__
                    attribute.
                    On the NI 4070/4071/4072, the minimum aperture time is 8.89 µs, and the
                    maximum aperture time is 149 s. Any number of powerline cycles (PLCs)
                    within the minimum and maximum ranges is allowed on the
                    NI 4070/4071/4072.
                    On the NI 4065 the minimum aperture time is 333 µs, and the maximum
                    aperture time is 78.2 s. If setting the number of averages directly, the
                    total measurement time is aperture time X the number of averages, which
                    must be less than 72.8 s. The aperture times allowed are 333 µs, 667 µs,
                    or multiples of 1.11 ms—for example 1.11 ms, 2.22 ms, 3.33 ms, and so
                    on. If you set an aperture time other than 333 µs, 667 µs, or multiples
                    of 1.11 ms, the value will be coerced up to the next supported aperture
                    time.
                    On the NI 4060, when the powerline frequency is 60, the PLCs allowed are
                    1 PLC, 6 PLC, 12 PLC, and 120 PLC. When the powerline frequency is 50,
                    the PLCs allowed are 1 PLC, 5 PLC, 10 PLC, and 100 PLC.
                aperture_time_units (enums.ApertureTimeUnits): Indicates the units of aperture time as powerline cycles (PLCs) or
                    seconds. Returns the value of the `
                    NIDMM\_ATTR\_APERTURE\_TIME\_UNITS <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_APERTURE_TIME_UNITS.html')>`__
                    attribute.
                    +-----------------------------------+-----+--------------------+
                    | NIDMM\_VAL\_SECONDS               | 0   | Seconds            |
                    +-----------------------------------+-----+--------------------+
                    | NIDMM\_VAL\_POWER\_LINE\_CYCLES   | 1   | Powerline Cycles   |
                    +-----------------------------------+-----+--------------------+
        '''
        aperture_time_ctype = ctypes_types.ViReal64_ctype(0)
        aperture_time_units_ctype = ctypes_types.ViInt32_ctype(0)
        error_code = self.library.niDMM_GetApertureTimeInfo(self.vi, ctypes.pointer(aperture_time_ctype), ctypes.pointer(aperture_time_units_ctype))
        errors._handle_error(self, error_code)
        return aperture_time_ctype.value, aperture_time_units_ctype.value

    def _get_attribute_vi_boolean(self, channel_name, attribute_id):
        '''.. function:: _get_attribute_vi_boolean(channel_name, attribute_id, attribute_value)

            Queries the value of a ViBoolean attribute. You can use this function to
            get the values of instrument-specific attributes and inherent IVI
            attributes.

            If the attribute represents an instrument state, this function performs
            instrument I/O in the following cases:

            -  State caching is disabled for the entire session or for the
               particular attribute.
            -  State caching is enabled, and the currently cached value is invalid.

            :param channel_name: This parameter is ignored. National Instruments DMMs do not support
                channel names since they only have a single channel. This parameter is
                included in order to support interchangeability and upgradability to
                multiple channel DMMs.

                The default value is " " (an empty string).
            :type channel_name: ViConstString
            :param attribute_id: Pass the ID of an attribute.
            :type attribute_id: ViAttr

            :rtype: ViBoolean
        '''
        attribute_value_ctype = ctypes_types.ViBoolean_ctype(0)
        error_code = self.library.niDMM_GetAttributeViBoolean(self.vi, channel_name.encode('ascii'), attribute_id, ctypes.pointer(attribute_value_ctype))
        errors._handle_error(self, error_code)
        return attribute_value_ctype.value

    def _get_attribute_vi_int32(self, channel_name, attribute_id):
        '''.. function:: _get_attribute_vi_int32(channel_name, attribute_id, attribute_value)

            Queries the value of a ViInt32 attribute. You can use this function to
            get the values of instrument-specific attributes and inherent IVI
            attributes.

            If the attribute represents an instrument state, this function performs
            instrument I/O in the following cases:

            -  State caching is disabled for the entire session or for the
               particular attribute.
            -  State caching is enabled, and the currently cached value is invalid.

            :param channel_name: This parameter is ignored. National Instruments DMMs do not support
                channel names since they only have a single channel. This parameter is
                included in order to support interchangeability and upgradability to
                multiple channel DMMs.

                The default value is " " (an empty string).
            :type channel_name: ViConstString
            :param attribute_id: Pass the ID of an attribute.
            :type attribute_id: ViAttr

            :rtype: ViInt32
        '''
        attribute_value_ctype = ctypes_types.ViInt32_ctype(0)
        error_code = self.library.niDMM_GetAttributeViInt32(self.vi, channel_name.encode('ascii'), attribute_id, ctypes.pointer(attribute_value_ctype))
        errors._handle_error(self, error_code)
        return attribute_value_ctype.value

    def _get_attribute_vi_real64(self, channel_name, attribute_id):
        '''.. function:: _get_attribute_vi_real64(channel_name, attribute_id, attribute_value)

            Purpose
            -------

            Queries the value of a ViReal64 attribute. You can use this function to
            get the values of instrument-specific attributes and inherent IVI
            attributes.

            If the attribute represents an instrument state, this function performs
            instrument I/O in the following cases:

            -  State caching is disabled for the entire session or for the
               particular attribute.
            -  State caching is enabled, and the currently cached value is invalid.

            :param channel_name: This parameter is ignored. National Instruments DMMs do not support
                channel names since they only have a single channel. This parameter is
                included in order to support interchangeability and upgradability to
                multiple channel DMMs.

                The default value is " " (an empty string).
            :type channel_name: ViConstString
            :param attribute_id: Pass the ID of an attribute.
            :type attribute_id: ViAttr

            :rtype: ViReal64
        '''
        attribute_value_ctype = ctypes_types.ViReal64_ctype(0)
        error_code = self.library.niDMM_GetAttributeViReal64(self.vi, channel_name.encode('ascii'), attribute_id, ctypes.pointer(attribute_value_ctype))
        errors._handle_error(self, error_code)
        return attribute_value_ctype.value

    def _get_attribute_vi_session(self, channel_name, attribute_id):
        '''.. function:: _get_attribute_vi_session(channel_name, attribute_id, attribute_value)

            Purpose
            -------

            Queries the value of a ViSession attribute. You can use this function to
            get the values of instrument-specific attributes and inherent IVI
            attributes.

            If the attribute represents an instrument state, this function performs
            instrument I/O in the following cases:

            -  State caching is disabled for the entire session or for the
               particular attribute.
            -  State caching is enabled, and the currently cached value is invalid.

            :param channel_name: This parameter is ignored. National Instruments DMMs do not support
                channel names since they only have a single channel. This parameter is
                included in order to support interchangeability and upgradability to
                multiple channel DMMs.

                The default value is " " (an empty string).
            :type channel_name: ViConstString
            :param attribute_id: Pass the ID of an attribute.
            :type attribute_id: ViAttr

            :rtype: ViSession
        '''
        attribute_value_ctype = ctypes_types.ViSession_ctype(0)
        error_code = self.library.niDMM_GetAttributeViSession(self.vi, channel_name.encode('ascii'), attribute_id, ctypes.pointer(attribute_value_ctype))
        errors._handle_error(self, error_code)
        return attribute_value_ctype.value

    def _get_attribute_vi_string(self, channel_name, attribute_id, buffer_size):
        '''.. function:: _get_attribute_vi_string(channel_name, attribute_id, buffer_size, attribute_value)

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

            :param channel_name: This parameter is ignored. National Instruments DMMs do not support
                channel names since they only have a single channel. This parameter is
                included in order to support interchangeability and upgradability to
                multiple channel DMMs.

                The default value is " " (an empty string).
            :type channel_name: ViConstString
            :param attribute_id: Pass the ID of an attribute.
            :type attribute_id: ViAttr
            :param buffer_size: Pass the number of bytes in the ViChar array you specify for the
                **Attribute\_Value** parameter.

                If the current value of the attribute, including the terminating NULL
                byte, contains more bytes that you indicate in this parameter, the
                function copies **bufferSize**—1 bytes into the buffer, places an ASCII
                NUL byte at the end of the buffer, and returns the buffer size you must
                pass to get the entire value. For example, if the value is "123456" and
                the **bufferSize** is 4, the function places "123" into the buffer and
                returns 7.

                If you pass a negative number, the function copies the value to the
                buffer regardless of the number of bytes in the value. If you pass 0,
                you can pass VI\_NULL for the **Attribute\_Value** buffer parameter.
            :type buffer_size: ViInt32

            :rtype: ViString
        '''
        attribute_value_ctype = ctypes_types.ViString_ctype(0)  # TODO(marcoskirsch): allocate a buffer
        error_code = self.library.niDMM_GetAttributeViString(self.vi, channel_name.encode('ascii'), attribute_id, buffer_size, attribute_value_ctype)
        errors._handle_error(self, error_code)
        return attribute_value_ctype.value

    def get_auto_range_value(self):
        '''.. function:: get_auto_range_value(actual_range)

            Returns the **Actual\_Range** that the DMM is using, even when Auto
            Range is off.

            :rtype: ViReal64
        '''
        actual_range_ctype = ctypes_types.ViReal64_ctype(0)
        error_code = self.library.niDMM_GetAutoRangeValue(self.vi, ctypes.pointer(actual_range_ctype))
        errors._handle_error(self, error_code)
        return actual_range_ctype.value

    def get_cal_count(self, cal_type):
        '''.. function:: get_cal_count(cal_type, count)

            Returns the calibration **Count** for the specified type of calibration.

            .. note::   The NI 4050, NI 4060, and NI 4080/4081/4082 are not
            supported.

            :param cal_type: Specifies the type of calibration performed (external or
                self-calibration).
                .. note::   The NI 4065 does not support self-calibration.
                0
                Self-Calibration
                NIDMM\_VAL\_EXTERNAL\_AREA
                1
                External Calibration
            :type cal_type: ViInt32

            :rtype: ViInt32
        '''
        count_ctype = ctypes_types.ViInt32_ctype(0)
        error_code = self.library.niDMM_GetCalCount(self.vi, cal_type, ctypes.pointer(count_ctype))
        errors._handle_error(self, error_code)
        return count_ctype.value

    def get_cal_date_and_time(self, cal_type):
        '''.. function:: get_cal_date_and_time(cal_type, month, day, year, hour, minute)

            Returns the date and time of the last calibration performed.

            .. note::   The NI 4050 and NI 4060 are not supported.

            :param cal_type: Specifies the type of calibration performed (external or
                self-calibration).
                .. note::   The NI 4065 does not support self-calibration.
                0
                Self-Calibration
                NIDMM\_VAL\_EXTERNAL\_AREA
                1
                External Calibration
            :type cal_type: ViInt32

            :rtype: tuple (month, day, year, hour, minute)
                WHERE
                month (ViInt32): Indicates the **month** of the last calibration.
                day (ViInt32): Indicates the **day** of the last calibration.
                year (ViInt32): Indicates the **year** of the last calibration.
                hour (ViInt32): Indicates the **hour** of the last calibration.
                minute (ViInt32): Indicates the **minute** of the last calibration.
        '''
        month_ctype = ctypes_types.ViInt32_ctype(0)
        day_ctype = ctypes_types.ViInt32_ctype(0)
        year_ctype = ctypes_types.ViInt32_ctype(0)
        hour_ctype = ctypes_types.ViInt32_ctype(0)
        minute_ctype = ctypes_types.ViInt32_ctype(0)
        error_code = self.library.niDMM_GetCalDateAndTime(self.vi, cal_type, ctypes.pointer(month_ctype), ctypes.pointer(day_ctype), ctypes.pointer(year_ctype), ctypes.pointer(hour_ctype), ctypes.pointer(minute_ctype))
        errors._handle_error(self, error_code)
        return month_ctype.value, day_ctype.value, year_ctype.value, hour_ctype.value, minute_ctype.value

    def get_channel_name(self, index, buffer_size):
        '''.. function:: get_channel_name(index, buffer_size, channel_string)

            Returns the **Channel\_String** that is in the channel table at an
            **Index** you specify. Not applicable to National Instruments DMMs.
            Included for compliance with the *IviDmm Class Specification*.

            :param index: A 1–based **index** into the channel table.
            :type index: ViInt32
            :param buffer_size: Passes the number of bytes in the ViChar array you specify for the
                **Channel\_String** parameter. If the next **Channel\_String**,
                including the terminating NULL byte, contains more bytes than you
                indicate in this parameter, the function copies **bufferSize** –1 bytes
                into the buffer, places an ASCII NULL byte at the end of the buffer, and
                returns the buffer size you must pass to get the entire value.

                For example, if the value is "123456" and the **bufferSize** is 4, the
                function places "123" into the buffer and returns 7. If you pass a
                negative number, the function copies the value to the buffer regardless
                of the number of bytes in the value. If you pass 0, you can pass
                VI\_NULL for the **Channel\_String** buffer parameter. The default value
                is None.
            :type buffer_size: ViInt32

            :rtype: ViChar
        '''
        channel_string_ctype = ctypes_types.ViChar_ctype(0)  # TODO(marcoskirsch): allocate a buffer
        error_code = self.library.niDMM_GetChannelName(self.vi, index, buffer_size, ctypes.pointer(channel_string_ctype))
        errors._handle_error(self, error_code)
        return channel_string_ctype.value.decode("ascii")

    def get_dev_temp(self, options):
        '''.. function:: get_dev_temp(options, temperature)

            Returns the current **Temperature** of the device.

            .. note::   The NI 4050 and NI 4060 are not supported.

            :param options: Reserved.
            :type options: ViString

            :rtype: ViReal64
        '''
        temperature_ctype = ctypes_types.ViReal64_ctype(0)
        error_code = self.library.niDMM_GetDevTemp(self.vi, options.encode('ascii'), ctypes.pointer(temperature_ctype))
        errors._handle_error(self, error_code)
        return temperature_ctype.value

    def _get_error(self, buffer_size):
        '''.. function:: _get_error(error_code, buffer_size, description)

            Returns the error information associated with the
            **Instrument\_Handle**. This function retrieves and then clears the
            error information for the session. If you leave the
            **Instrument\_Handle** unwired, this function retrieves and then clears
            the error information for the process.

            :param buffer_size: Passes the number of bytes in the ViChar array you specify for the
                **Description** parameter. If the error description, including the
                terminating NULL byte, contains more bytes than you indicate in this
                parameter, the function copies **bufferSize** –1 bytes into the buffer,
                places an ASCII NULL byte at the end of the buffer, and returns the
                **bufferSize** you must pass to get the entire value.

                For example, if the value is "123456" and the **bufferSize** is 4, the
                function places "123" into the buffer and returns 7. If you pass a
                negative number, the function copies the value to the buffer regardless
                of the number of bytes in the value. If you pass 0, you can pass
                VI\_NULL for the **Description** buffer parameter. The default value is
                None.
            :type buffer_size: ViInt32

            :rtype: tuple (error_code, description)
                WHERE
                error_code (ViStatus): Returns the **errorCode** for the session or execution thread. If you
                    pass 0 for the **Buffer\_Size**, you can pass VI\_NULL for this
                    parameter.
                description (ViChar): Returns the error **description** for the IVI session or execution
                    thread. If there is no **description**, the function returns an empty
                    string. The buffer must contain at least as many elements as the value
                    you specify with the **Buffer\_Size** parameter. If you pass 0 for the
                    **Buffer\_Size**, you can pass VI\_NULL for this parameter.
        '''
        error_code_ctype = ctypes_types.ViStatus_ctype(0)
        description_ctype = ctypes_types.ViChar_ctype(0)  # TODO(marcoskirsch): allocate a buffer
        error_code = self.library.niDMM_GetError(self.vi, ctypes.pointer(error_code_ctype), buffer_size, ctypes.pointer(description_ctype))
        errors._handle_error(self, error_code)
        return error_code_ctype.value, description_ctype.value.decode("ascii")

    def _get_error_message(self, error_code, buffer_size):
        '''.. function:: _get_error_message(error_code, buffer_size, error_message)

            Purpose
            -------

            Returns the **Error\_Message** as a user-readable string for the
            provided **Error\_Code**. Calling this function with a **Buffer\_Size**
            of 0 returns the size needed for the **Error\_Message**.

            :param error_code: The error code returned from the instrument for which you want to get a
                user-readable string.
            :type error_code: ViStatus
            :param buffer_size: Specifies the number of bytes allocated for the **Error\_Message**
                ViChar array. If the error description that this function returns
                (including terminating NULL byte) is larger than you indicated in
                **buffer\_size**, the error description will be truncated to fit. If you
                pass 0 for **buffer\_size**, the function returns the buffer size needed
                for **Error\_Message**.
            :type buffer_size: ViInt32

            :rtype: ViChar
        '''
        error_message_ctype = ctypes_types.ViChar_ctype(0)  # TODO(marcoskirsch): allocate a buffer
        error_code = self.library.niDMM_GetErrorMessage(self.vi, error_code, buffer_size, ctypes.pointer(error_message_ctype))
        errors._handle_error(self, error_code)
        return error_message_ctype.value.decode("ascii")

    def get_last_cal_temp(self, cal_type):
        '''.. function:: get_last_cal_temp(cal_type, temperature)

            Returns the **Temperature** during the last calibration procedure.

            .. note::   The NI 4050 and NI 4060 are not supported.

            :param cal_type: Specifies the type of calibration performed (external or
                self-calibration).
                .. note::   The NI 4065 does not support self-calibration.
                0
                Self-Calibration
                NIDMM\_VAL\_EXTERNAL\_AREA
                1
                External Calibration
            :type cal_type: ViInt32

            :rtype: ViReal64
        '''
        temperature_ctype = ctypes_types.ViReal64_ctype(0)
        error_code = self.library.niDMM_GetLastCalTemp(self.vi, cal_type, ctypes.pointer(temperature_ctype))
        errors._handle_error(self, error_code)
        return temperature_ctype.value

    def get_measurement_period(self):
        '''.. function:: get_measurement_period(period)

            Returns the measurement **Period**, which is the amount of time it takes
            to complete one measurement with the current configuration. Use this
            function right before you begin acquiring data—after you have completely
            configured the measurement and after all configuration functions have
            been called.

            :rtype: ViReal64
        '''
        period_ctype = ctypes_types.ViReal64_ctype(0)
        error_code = self.library.niDMM_GetMeasurementPeriod(self.vi, ctypes.pointer(period_ctype))
        errors._handle_error(self, error_code)
        return period_ctype.value

    def get_next_coercion_record(self, buffer_size):
        '''.. function:: get_next_coercion_record(buffer_size, coercion_record)

            This function returns the coercion information associated with the IVI
            session, and it retrieves and clears the oldest instance in which NI-DMM
            coerced a value you specified to another value.

            If you set `
            NIDMM\_ATTR\_RECORD\_COERCIONS <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_RECORD_COERCIONS.html')>`__
            to VI\_TRUE (1), NI-DMM keeps a list of all coercions it makes on
            ViInt32 or ViReal64 values that you pass to NI-DMM functions. Use this
            function to retrieve information from that list.

            :param buffer_size: Passes the number of bytes in the ViChar array you specify for the
                **Coercion\_Record** parameter. If the next coercion record string,
                including the terminating NULL byte, contains more bytes than you
                indicate in this parameter, the function copies **bufferSize** – 1 bytes
                into the buffer, places an ASCII NULL byte at the end of the buffer, and
                returns the buffer size you must pass to get the entire value.

                For example, if the value is "123456" and the **bufferSize** is 4, the
                function places "123" into the buffer and returns 7. If you pass a
                negative number, the function copies the value to the buffer regardless
                of the number of bytes in the value.

                If you pass 0, you can pass VI\_NULL for the **Coercion\_Record** buffer
                parameter.

                The default value is None.
            :type buffer_size: ViInt32

            :rtype: ViChar
        '''
        coercion_record_ctype = ctypes_types.ViChar_ctype(0)  # TODO(marcoskirsch): allocate a buffer
        error_code = self.library.niDMM_GetNextCoercionRecord(self.vi, buffer_size, ctypes.pointer(coercion_record_ctype))
        errors._handle_error(self, error_code)
        return coercion_record_ctype.value.decode("ascii")

    def get_next_interchange_warning(self, buffer_size):
        '''.. function:: get_next_interchange_warning(buffer_size, interchange_warning)

            This function returns the interchangeability warnings associated with
            the IVI session. It retrieves and clears the oldest instance in which
            the class driver recorded an interchangeability warning.
            Interchangeability warnings indicate that using your application with a
            different instrument might cause different behavior.

            The driver performs interchangeability checking when `
            NIDMM\_ATTR\_INTERCHANGE\_CHECK <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_INTERCHANGE_CHECK.html')>`__
            is set to VI\_TRUE (1). The function returns an empty string in the
            **Interchange\_Warning** parameter if no interchangeability warnings
            remain for the session. In general, the instrument driver generates
            interchangeability warnings when an attribute that affects the behavior
            of the instrument is in a state that you did not specify.

            :param buffer_size: Passes the number of bytes in the ViChar array you specify for the
                **Interchange\_Warning** parameter. If the next interchangeability
                warning string, including the terminating NULL byte, contains more bytes
                than you indicate in this parameter, the function copies
                **bufferSize** –1 bytes into the buffer, places an ASCII NULL byte at
                the end of the buffer, and returns the buffer size you must pass to get
                the entire value.

                For example, if the value is "123456" and the **bufferSize** is 4, the
                function places "123" into the buffer and returns 7. If you pass a
                negative number, the function copies the value to the buffer regardless
                of the number of bytes in the value. If you pass 0, you can pass
                VI\_NULL for the **Interchange\_Warning** buffer parameter. The default
                value is None.
            :type buffer_size: ViInt32

            :rtype: ViChar
        '''
        interchange_warning_ctype = ctypes_types.ViChar_ctype(0)  # TODO(marcoskirsch): allocate a buffer
        error_code = self.library.niDMM_GetNextInterchangeWarning(self.vi, buffer_size, ctypes.pointer(interchange_warning_ctype))
        errors._handle_error(self, error_code)
        return interchange_warning_ctype.value.decode("ascii")

    def get_self_cal_supported(self):
        '''.. function:: get_self_cal_supported(self_cal_supported)

            Returns a Boolean value that expresses whether or not the DMM that you
            are using can perform self-calibration.

            :rtype: ViBoolean
        '''
        self_cal_supported_ctype = ctypes_types.ViBoolean_ctype(0)
        error_code = self.library.niDMM_GetSelfCalSupported(self.vi, ctypes.pointer(self_cal_supported_ctype))
        errors._handle_error(self, error_code)
        return self_cal_supported_ctype.value

    def _init_with_options(self, resource_name, id_query, reset_device, option_string):
        '''.. function:: _init_with_options(resource_name, id_query, reset_device, option_string)

            This function completes the following tasks:

            -  Creates a new IVI instrument driver session and, optionally, sets the
               initial state of the following session attributes: `
               RangeCheck <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_RANGE_CHECK.html')>`__,
               `
               QueryInstrStatus <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_QUERY_INSTR_STATUS.html')>`__,
               `
               Cache <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_CACHE.html')>`__,
               `
               Simulate <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_SIMULATE.html')>`__,
               `
               Recordcoercions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_RECORD_COERCIONS.html')>`__.
            -  Opens a session to the device you specify for the **Resource\_Name**
               parameter. If the **ID\_Query** parameter is set to VI\_TRUE, this
               function queries the instrument ID and checks that it is valid for
               this instrument driver.
            -  If the **Reset\_Device** parameter is set to VI\_TRUE, this function
               resets the instrument to a known state. Sends initialization commands
               to set the instrument to the state necessary for the operation of the
               instrument driver.
            -  Returns a ViSession handle that you use to identify the instrument in
               all subsequent instrument driver function calls.

            :param resource_name: | Contains the **resourceName** of the device to initialize. The
                  **resourceName** is assigned in Measurement & Automation Explorer
                  (MAX). Refer to `Related
                  Documentation <javascript:LaunchHelp('dmm.chm::/related_documentation.html')>`__
                  for the *NI Digital Multimeters Getting Started Guide* for more
                  information about configuring and testing the DMM in MAX.
                | Valid Syntax:

                -  NI-DAQmx name
                -  DAQ::NI-DAQmx name[::INSTR]
                -  DAQ::Traditional NI-DAQ device number[::INSTR]
                -  IVI logical name

                .. caution::   All IVI names for the **resourceName**, such as logical
                names or virtual names, are case-sensitive. If you use logical names,
                driver session names, or virtual names in your program, you must make
                sure that the name you use matches the name in the IVI Configuration
                Store file exactly, without any variations in the case of the characters
                in the name.
            :type resource_name: ViString
            :param id_query: Verifies that the device you initialize is one that the driver supports.
                NI-DMM automatically performs this query, so setting this parameter is
                not necessary.
                Defined Values:
                +----------------------+-----+--------------------+
                | VI\_TRUE (default)   | 1   | Perform ID Query   |
                +----------------------+-----+--------------------+
                | VI\_FALSE            | 0   | Skip ID Query      |
                +----------------------+-----+--------------------+
            :type id_query: ViBoolean
            :param reset_device: Specifies whether to reset the instrument during the initialization
                procedure.
                Defined Values:
                +----------------------+-----+----------------+
                | VI\_TRUE (default)   | 1   | Reset Device   |
                +----------------------+-----+----------------+
                | VI\_FALSE            | 0   | Don't Reset    |
                +----------------------+-----+----------------+
            :type reset_device: ViBoolean
            :param option_string: | Sets the initial value of certain attributes for the session. The
                  following table specifies the attribute name, attribute constant, and
                  default value for each attribute that you can use in this parameter:

                +--------------------+-------------------------------------+---------------------+------+
                | Check              | NIDMM\_ATTR\_RANGE\_CHECK           | VI\_TRUE            | 1    |
                +--------------------+-------------------------------------+---------------------+------+
                | QueryInstrStatus   | NIDMM\_ATTR\_QUERY\_INSTR\_STATUS   | VI\_FALSE           | 0    |
                +--------------------+-------------------------------------+---------------------+------+
                | Cache              | NIDMM\_ATTR\_CACHE                  | VI\_TRUE            | 1    |
                +--------------------+-------------------------------------+---------------------+------+
                | Simulate           | NIDMM\_ATTR\_SIMULATE               | VI\_FALSE           | 0    |
                +--------------------+-------------------------------------+---------------------+------+
                | RecordCoercions    | NIDMM\_ATTR\_RECORD\_COERCIONS      | VI\_FALSE           | 0    |
                +--------------------+-------------------------------------+---------------------+------+
                | DriverSetup        | NIDMM\_ATTR\_DRIVER\_SETUP          | "" (empty string)   | ""   |
                +--------------------+-------------------------------------+---------------------+------+

                The format of this string is, "AttributeName=Value." To set multiple
                attributes, separate their assignments with a comma.

                If you pass NULL or an empty string for this parameter, the session uses
                the default values for the attributes. You can override the default
                values by assigning a value explicitly in an **optionString** parameter.
                You do not have to specify all of the attributes and may leave any of
                them out (those left out use the default value).

                Refer to `Simulating NI Digital
                Multimeters <javascript:LaunchHelp('dmm.chm::/simulation.html')>`__ for
                more information.
            :type option_string: ViString

            :rtype: ViSession
        '''
        vi_ctype = ctypes_types.ViSession_ctype(0)
        error_code = self.library.niDMM_InitWithOptions(resource_name.encode('ascii'), id_query, reset_device, option_string.encode('ascii'), ctypes.pointer(vi_ctype))
        errors._handle_error(self, error_code)
        return vi_ctype.value

    def _initiate(self):
        '''.. function:: _initiate()

            Purpose
            -------

            Initiates an acquisition. After you call this function, the DMM leaves
            the Idle state and enters the Wait-for-Trigger state. If trigger is set
            to Immediate mode, the DMM begins acquiring measurement data. Use `
            niDMM\_Fetch <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'cviniDMM_Fetch.html')>`__,
            `
            niDMM\_FetchMultiPoint <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'cviniDMM_FetchMultiPoint.html')>`__,
            or `
            niDMM\_FetchWaveform <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'cviniDMM_FetchWaveform.html')>`__
            to retrieve the measurement data.
        '''
        error_code = self.library.niDMM_Initiate(self.vi)
        errors._handle_error(self, error_code)
        return

    def is_over_range(self, measurement_value):
        '''.. function:: is_over_range(measurement_value, is_over_range)

            Takes a **Measurement\_Value** and determines if the value is a valid
            measurement or a value indicating that an overrange condition occurred.

            :param measurement_value: The measured value returned from the DMM.
                +------------+----------------------------------------------------------------------------------------------------------------------------+
                | |image0|   | **Note**   If an overrange condition occurs, the **measurementValue** contains an IEEE-defined NaN (Not a Number) value.   |
                +------------+----------------------------------------------------------------------------------------------------------------------------+

                .. |image0| image:: note.gif
            :type measurement_value: ViReal64

            :rtype: ViBoolean
        '''
        is_over_range_ctype = ctypes_types.ViBoolean_ctype(0)
        error_code = self.library.niDMM_IsOverRange(self.vi, measurement_value, ctypes.pointer(is_over_range_ctype))
        errors._handle_error(self, error_code)
        return is_over_range_ctype.value

    def is_under_range(self, measurement_value):
        '''.. function:: is_under_range(measurement_value, is_under_range)

            Takes a **Measurement\_Value** and determines if the value is a valid
            measurement or a value indicating that an underrange condition occurred.

            :param measurement_value: The measured value returned from the DMM.
                +------------+----------------------------------------------------------------------------------------------------------------------------+
                | |image0|   | **Note**   If an overrange condition occurs, the **measurementValue** contains an IEEE-defined NaN (Not a Number) value.   |
                +------------+----------------------------------------------------------------------------------------------------------------------------+

                .. |image0| image:: note.gif
            :type measurement_value: ViReal64

            :rtype: ViBoolean
        '''
        is_under_range_ctype = ctypes_types.ViBoolean_ctype(0)
        error_code = self.library.niDMM_IsUnderRange(self.vi, measurement_value, ctypes.pointer(is_under_range_ctype))
        errors._handle_error(self, error_code)
        return is_under_range_ctype.value

    def _lock_session(self):
        '''.. function:: _lock_session(caller_has_lock)

            This function obtains a multithread lock on the instrument session.
            Before it does so, it waits until all other execution threads have
            released their locks on the instrument session.

            Other threads might have obtained a lock on this session in the
            following ways:

            -  The user application called this function.
            -  A call to the instrument driver locked the session.
            -  A call to the IVI Library locked the session.

            After your call to this function returns successfully, no other threads
            can access the instrument session until you call `
            niDMM\_UnlockSession <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_UnlockSession.html')>`__.

            Use this function and `
            niDMM\_UnlockSession <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_UnlockSession.html')>`__
            around a sequence of calls to instrument driver functions if you require
            that the instrument retain its settings through the end of the sequence.
            You can safely make nested calls to this function within the same
            thread.

            To completely unlock the session, you must balance each call to this
            function with a call to `
            niDMM\_UnlockSession <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_UnlockSession.html')>`__.
            If, however, you use the **Caller\_Has\_Lock** parameter in all calls to
            this function and `
            niDMM\_UnlockSession <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_UnlockSession.html')>`__
            within a function, the IVI Library locks the session only once within
            the function regardless of the number of calls you make to this
            function. This feature allows you to call `
            niDMM\_UnlockSession <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_UnlockSession.html')>`__
            just once at the end of the function.

            :rtype: ViBoolean
        '''
        caller_has_lock_ctype = ctypes_types.ViBoolean_ctype(0)
        error_code = self.library.niDMM_LockSession(self.vi, ctypes.pointer(caller_has_lock_ctype))
        errors._handle_error(self, error_code)
        return caller_has_lock_ctype.value

    def perform_open_cable_comp(self):
        '''.. function:: perform_open_cable_comp(conductance, susceptance)

            Purpose
            -------

            For the NI 4082 and NI 4072 only, performs the open cable compensation
            measurements for the current capacitance/inductance range, and returns
            open cable compensation **Conductance** and **Susceptance** values. You
            can use the return values of this function as inputs to `
            niDMM\_ConfigureOpenCableCompValues <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'cviniDMM_ConfigureOpenCableCompValues.html')>`__.

            This function returns an error if the value of the `
            NIDMM\_ATTR\_FUNCTION <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'caNIDMM_ATTR_FUNCTION.html')>`__
            attribute is not set to NIDMM\_VAL\_CAPACITANCE (1005) or
            NIDMM\_VAL\_INDUCTANCE (1006).

            :rtype: tuple (conductance, susceptance)
                WHERE
                conductance (ViReal64): **conductance** is the measured value of open cable compensation
                    **conductance**.
                susceptance (ViReal64): **susceptance** is the measured value of open cable compensation
                    **susceptance**.
        '''
        conductance_ctype = ctypes_types.ViReal64_ctype(0)
        susceptance_ctype = ctypes_types.ViReal64_ctype(0)
        error_code = self.library.niDMM_PerformOpenCableComp(self.vi, ctypes.pointer(conductance_ctype), ctypes.pointer(susceptance_ctype))
        errors._handle_error(self, error_code)
        return conductance_ctype.value, susceptance_ctype.value

    def perform_short_cable_comp(self):
        '''.. function:: perform_short_cable_comp(resistance, reactance)

            Purpose
            -------

            Performs the short cable compensation measurements for the current
            capacitance/inductance range, and returns short cable compensation
            **Resistance** and **Reactance** values. You can use the return values
            of this function as inputs to `
            niDMM\_ConfigureShortCableCompValues <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'cviniDMM_ConfigureShortCableCompValues.html')>`__.

            This function returns an error if the value of the `
            NIDMM\_ATTR\_FUNCTION <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'caNIDMM_ATTR_FUNCTION.html')>`__
            attribute is not set to NIDMM\_VAL\_CAPACITANCE (1005) or
            NIDMM\_VAL\_INDUCTANCE (1006).

            :rtype: tuple (resistance, reactance)
                WHERE
                resistance (ViReal64): **resistance** is the measured value of short cable compensation
                    **resistance**.
                reactance (ViReal64): **reactance** is the measured value of short cable compensation
                    **reactance**.
        '''
        resistance_ctype = ctypes_types.ViReal64_ctype(0)
        reactance_ctype = ctypes_types.ViReal64_ctype(0)
        error_code = self.library.niDMM_PerformShortCableComp(self.vi, ctypes.pointer(resistance_ctype), ctypes.pointer(reactance_ctype))
        errors._handle_error(self, error_code)
        return resistance_ctype.value, reactance_ctype.value

    def read(self, maximum_time):
        '''.. function:: read(maximum_time, reading)

            Acquires a single measurement and returns the measured value.

            :param maximum_time: Specifies the **maximumTime** allowed for this function to complete in
                milliseconds. If the function does not complete within this time
                interval, the function returns the NIDMM\_ERROR\_MAX\_TIME\_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                NIDMM\_VAL\_TIME\_LIMIT\_AUTO (-1). The DMM calculates the timeout
                automatically.
            :type maximum_time: ViInt32

            :rtype: ViReal64
        '''
        reading_ctype = ctypes_types.ViReal64_ctype(0)
        error_code = self.library.niDMM_Read(self.vi, maximum_time, ctypes.pointer(reading_ctype))
        errors._handle_error(self, error_code)
        return reading_ctype.value

    def read_multi_point(self, maximum_time, array_size):
        '''.. function:: read_multi_point(maximum_time, array_size, reading_array, actual_number_of_points)

            Acquires multiple measurements and returns an array of measured values.
            The number of measurements the DMM makes is determined by the values you
            specify for the **Trigger\_Count** and **Sample\_Count** parameters in `
            niDMM\_ConfigureMultiPoint <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_ConfigureMultiPoint.html')>`__.

            :param maximum_time: Specifies the **maximumTime** allowed for this function to complete in
                milliseconds. If the function does not complete within this time
                interval, the function returns the NIDMM\_ERROR\_MAX\_TIME\_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                NIDMM\_VAL\_TIME\_LIMIT\_AUTO (-1). The DMM calculates the timeout
                automatically.
            :type maximum_time: ViInt32
            :param array_size: Specifies the number of measurements to acquire. The maximum number of
                measurements for a finite acquisition is the (**Trigger Count** x
                **Sample Count**) parameters in `
                niDMM\_ConfigureMultiPoint <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_ConfigureMultiPoint.html')>`__.

                For continuous acquisitions, up to 100,000 points can be returned at
                once. The number of measurements can be a subset. The valid range is any
                positive ViInt32. The default value is 1.
            :type array_size: ViInt32

            :rtype: tuple (reading_array, actual_number_of_points)
                WHERE
                reading_array (ViReal64): An array of measurement values.
                    +------------+-----------------------------------------------------------------------------------------------------------------------------+
                    | |image0|   | **Note**   The size of the **readingArray** must be at least the size that you specify for the **Array\_Size** parameter.   |
                    +------------+-----------------------------------------------------------------------------------------------------------------------------+

                    .. |image0| image:: note.gif
                actual_number_of_points (ViInt32): Indicates the number of measured values actually retrieved from the DMM.
        '''
        reading_array_ctype = ctypes_types.ViReal64_ctype(0)  # TODO(marcoskirsch): allocate a buffer
        actual_number_of_points_ctype = ctypes_types.ViInt32_ctype(0)
        error_code = self.library.niDMM_ReadMultiPoint(self.vi, maximum_time, array_size, ctypes.pointer(reading_array_ctype), ctypes.pointer(actual_number_of_points_ctype))
        errors._handle_error(self, error_code)
        return reading_array_ctype.value, actual_number_of_points_ctype.value

    def read_status(self):
        '''.. function:: read_status(acquisition_backlog, acquisition_status)

            Returns measurement backlog and acquisition status. Use this function to
            determine how many measurements are available before calling `
            niDMM\_Fetch <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_Fetch.html')>`__,
            `
            niDMM\_FetchMultipoint <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_FetchMultiPoint.html')>`__,
            or `
            niDMM\_FetchWaveform <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_FetchWaveform.html')>`__.

            .. note::   The NI 4050 is not supported.

            :rtype: tuple (acquisition_backlog, acquisition_status)
                WHERE
                acquisition_backlog (ViInt32): The number of measurements available to be read. If the backlog
                    continues to increase, data is eventually overwritten, resulting in an
                    error. .. note::   On the NI 4060, the **Backlog** does not increase
                    when autoranging. On the NI 4065, the **Backlog** does not increase when
                    Range is set to AUTO RANGE ON (-1), or before the first point is fetched
                    when Range is set to AUTO RANGE ONCE (-3). These behaviors are due to
                    the autorange model of the devices.
                acquisition_status (enums.AcquisitionStatus): Indicates status of the acquisition. The following table shows the
                    acquisition states:
                    +-----+------------------------------+
                    | 0   | Running                      |
                    +-----+------------------------------+
                    | 1   | Finished with backlog        |
                    +-----+------------------------------+
                    | 2   | Finished with no backlog     |
                    +-----+------------------------------+
                    | 3   | Paused                       |
                    +-----+------------------------------+
                    | 4   | No acquisition in progress   |
                    +-----+------------------------------+
        '''
        acquisition_backlog_ctype = ctypes_types.ViInt32_ctype(0)
        acquisition_status_ctype = ctypes_types.ViInt16_ctype(0)
        error_code = self.library.niDMM_ReadStatus(self.vi, ctypes.pointer(acquisition_backlog_ctype), ctypes.pointer(acquisition_status_ctype))
        errors._handle_error(self, error_code)
        return acquisition_backlog_ctype.value, acquisition_status_ctype.value

    def read_waveform(self, maximum_time, array_size):
        '''.. function:: read_waveform(maximum_time, array_size, waveform_array, actual_number_of_points)

            For the NI 4080/4081/4082 and the NI 4070/4071/4072, acquires a waveform
            and returns data as an array of values or as a waveform data type. The
            number of elements in the **Waveform\_Array** is determined by the
            values you specify for the **Waveform\_Points** parameter in `
            niDMM\_ConfigureWaveformAcquisition <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_ConfigureWaveformAcquisition.html')>`__.

            :param maximum_time: Specifies the **maximumTime** allowed for this function to complete in
                milliseconds. If the function does not complete within this time
                interval, the function returns the NIDMM\_ERROR\_MAX\_TIME\_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                NIDMM\_VAL\_TIME\_LIMIT\_AUTO (-1). The DMM calculates the timeout
                automatically.
            :type maximum_time: ViInt32
            :param array_size: Specifies the number of waveform points to return. You specify the total
                number of points that the DMM acquires in the **Waveform Points**
                parameter of `
                niDMM\_ConfigureWaveformAcquisition <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_ConfigureWaveformAcquisition.html')>`__.
                The default value is 1.
            :type array_size: ViInt32

            :rtype: tuple (waveform_array, actual_number_of_points)
                WHERE
                waveform_array (ViReal64): An array of measurement values.
                    +------------+------------------------------------------------------------------------------------------------------------------------------+
                    | |image0|   | **Note**   The size of the **waveformArray** must be at least the size that you specify for the **Array\_Size** parameter.   |
                    +------------+------------------------------------------------------------------------------------------------------------------------------+

                    .. |image0| image:: note.gif
                actual_number_of_points (ViInt32): Indicates the number of measured values actually retrieved from the DMM.
        '''
        waveform_array_ctype = ctypes_types.ViReal64_ctype(0)  # TODO(marcoskirsch): allocate a buffer
        actual_number_of_points_ctype = ctypes_types.ViInt32_ctype(0)
        error_code = self.library.niDMM_ReadWaveform(self.vi, maximum_time, array_size, ctypes.pointer(waveform_array_ctype), ctypes.pointer(actual_number_of_points_ctype))
        errors._handle_error(self, error_code)
        return waveform_array_ctype.value, actual_number_of_points_ctype.value

    def reset_interchange_check(self):
        '''.. function:: reset_interchange_check()

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
            guarantee that `
            niDMM\_GetNextInterchangeWarning <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_GetNextInterchangeWarning.html')>`__
            only returns those interchangeability warnings that are generated after
            calling this function, you must clear the list of interchangeability
            warnings. You can clear the interchangeability warnings list by
            repeatedly calling `
            niDMM\_GetNextInterchangeWarning <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_GetNextInterchangeWarning.html')>`__
            until no more interchangeability warnings are returned. If you are not
            interested in the content of those warnings, you can call `
            niDMM\_ClearInterchangeWarnings <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_ClearInterchangeWarnings.html')>`__.
        '''
        error_code = self.library.niDMM_ResetInterchangeCheck(self.vi)
        errors._handle_error(self, error_code)
        return

    def reset_with_defaults(self):
        '''.. function:: reset_with_defaults()

            Resets the instrument to a known state and sends initialization commands
            to the DMM. The initialization commands set the DMM settings to the
            state necessary for the operation of NI-DMM. All user-defined default
            values associated with a logical name are applied after setting the DMM.
        '''
        error_code = self.library.niDMM_ResetWithDefaults(self.vi)
        errors._handle_error(self, error_code)
        return

    def self_cal(self):
        '''.. function:: self_cal()

            For the NI 4080/4081/4082 and the NI 4070/4071/4072, executes the
            self-calibration routine to maintain measurement accuracy.

            .. note::   This function calls `
            niDMM\_reset <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_reset.html')>`__,
            and any configurations previous to the call will be lost. All attributes
            will be set to their default values after the call returns.
        '''
        error_code = self.library.niDMM_SelfCal(self.vi)
        errors._handle_error(self, error_code)
        return

    def send_software_trigger(self):
        '''.. function:: send_software_trigger()

            Purpose
            -------

            Sends a command to trigger the DMM. Call this function if you have
            configured either the `
            NIDMM\_ATTR\_TRIGGER\_SOURCE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'caNIDMM_ATTR_TRIGGER_SOURCE.html')>`__
            or `
            NIDMM\_ATTR\_SAMPLE\_TRIGGER <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'caNIDMM_ATTR_SAMPLE_TRIGGER.html')>`__
            attributes. If the `
            NIDMM\_ATTR\_TRIGGER\_SOURCE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'caNIDMM_ATTR_TRIGGER_SOURCE.html')>`__
            and/or `
            NIDMM\_ATTR\_SAMPLE\_TRIGGER <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'caNIDMM_ATTR_SAMPLE_TRIGGER.html')>`__
            attributes are set to NIDMM\_VAL\_EXTERNAL or NIDMM\_VAL\_TTL\ *n*, you
            can use this function to override the trigger source that you configured
            and trigger the device. The NI 4050 and NI 4060 are not supported.
        '''
        error_code = self.library.niDMM_SendSoftwareTrigger(self.vi)
        errors._handle_error(self, error_code)
        return

    def _set_attribute_vi_boolean(self, channel_name, attribute_id, attribute_value):
        '''.. function:: _set_attribute_vi_boolean(channel_name, attribute_id, attribute_value)

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

            :param channel_name: This parameter is ignored. National Instruments DMMs do not support
                channel names since they only have a single channel. This parameter is
                included in order to support interchangeability and upgradability to
                multiple channel DMMs.

                The default value is " " (an empty string).
            :type channel_name: ViConstString
            :param attribute_id: Pass the ID of an attribute.
            :type attribute_id: ViAttr
            :param attribute_value: Pass the value that you want to set the attribute to.
            :type attribute_value: ViBoolean
        '''
        error_code = self.library.niDMM_SetAttributeViBoolean(self.vi, channel_name.encode('ascii'), attribute_id, attribute_value)
        errors._handle_error(self, error_code)
        return

    def _set_attribute_vi_int32(self, channel_name, attribute_id, attribute_value):
        '''.. function:: _set_attribute_vi_int32(channel_name, attribute_id, attribute_value)

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

            :param channel_name: This parameter is ignored. National Instruments DMMs do not support
                channel names since they only have a single channel. This parameter is
                included in order to support interchangeability and upgradability to
                multiple channel DMMs.

                The default value is " " (an empty string).
            :type channel_name: ViConstString
            :param attribute_id: Pass the ID of an attribute.
            :type attribute_id: ViAttr
            :param attribute_value: Pass the value that you want to set the attribute to.
            :type attribute_value: ViInt32
        '''
        error_code = self.library.niDMM_SetAttributeViInt32(self.vi, channel_name.encode('ascii'), attribute_id, attribute_value)
        errors._handle_error(self, error_code)
        return

    def _set_attribute_vi_real64(self, channel_name, attribute_id, attribute_value):
        '''.. function:: _set_attribute_vi_real64(channel_name, attribute_id, attribute_value)

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

            :param channel_name: This parameter is ignored. National Instruments DMMs do not support
                channel names since they only have a single channel. This parameter is
                included in order to support interchangeability and upgradability to
                multiple channel DMMs.

                The default value is " " (an empty string).
            :type channel_name: ViConstString
            :param attribute_id: Pass the ID of an attribute.
            :type attribute_id: ViAttr
            :param attribute_value: Pass the value that you want to set the attribute to.
            :type attribute_value: ViReal64
        '''
        error_code = self.library.niDMM_SetAttributeViReal64(self.vi, channel_name.encode('ascii'), attribute_id, attribute_value)
        errors._handle_error(self, error_code)
        return

    def _set_attribute_vi_session(self, channel_name, attribute_id, attribute_value):
        '''.. function:: _set_attribute_vi_session(channel_name, attribute_id, attribute_value)

            Purpose
            -------

            This function sets the value of a ViSession attribute.

            This is a low-level function that you can use to set the values of
            instrument-specific attributes and inherent IVI attributes.

            If the attribute represents an instrument state, this function performs
            instrument I/O in the following cases:

            -  State caching is disabled for the entire session or for the
               particular attribute.
            -  State caching is enabled, and the currently cached value is invalid
               or is different than the value you specify.

            :param channel_name: This parameter is ignored. National Instruments DMMs do not support
                channel names since they only have a single channel. This parameter is
                included in order to support interchangeability and upgradability to
                multiple channel DMMs.

                The default value is " " (an empty string).
            :type channel_name: ViConstString
            :param attribute_id: Pass the ID of an attribute.
            :type attribute_id: ViAttr
            :param attribute_value: Pass the value that you want to set the attribute to.
            :type attribute_value: ViSession
        '''
        error_code = self.library.niDMM_SetAttributeViSession(self.vi, channel_name.encode('ascii'), attribute_id, attribute_value)
        errors._handle_error(self, error_code)
        return

    def _set_attribute_vi_string(self, channel_name, attribute_id, attribute_value):
        '''.. function:: _set_attribute_vi_string(channel_name, attribute_id, attribute_value)

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

            :param channel_name: This parameter is ignored. National Instruments DMMs do not support
                channel names since they only have a single channel. This parameter is
                included in order to support interchangeability and upgradability to
                multiple channel DMMs.

                The default value is " " (an empty string).
            :type channel_name: ViConstString
            :param attribute_id: Pass the ID of an attribute.
            :type attribute_id: ViAttr
            :param attribute_value: Pass the value that you want to set the attribute to.
            :type attribute_value: ViString
        '''
        error_code = self.library.niDMM_SetAttributeViString(self.vi, channel_name.encode('ascii'), attribute_id, attribute_value.encode('ascii'))
        errors._handle_error(self, error_code)
        return

    def _unlock_session(self):
        '''.. function:: _unlock_session(caller_has_lock)

            This function releases a lock that you acquired on an instrument session
            using niDMM\_LockSession. Refer to `
            niDMM\_LockSession <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_LockSession.html')>`__
            for additional information on session locks.

            :rtype: ViBoolean
        '''
        caller_has_lock_ctype = ctypes_types.ViBoolean_ctype(0)
        error_code = self.library.niDMM_UnlockSession(self.vi, ctypes.pointer(caller_has_lock_ctype))
        errors._handle_error(self, error_code)
        return caller_has_lock_ctype.value

    def _close(self):
        '''.. function:: _close()

            Purpose
            -------

            Closes the specified session and deallocates resources that it reserved.
        '''
        error_code = self.library.niDMM_close(self.vi)
        errors._handle_error(self, error_code)
        return

    def error_message(self, error_code):
        '''.. function:: error_message(error_code, error_message)

            Takes the **Error\_Code** returned by the instrument driver functions,
            interprets it, and returns it as a user-readable string.

            :param error_code: The **errorCode** returned from the instrument. The default is 0,
                indicating VI\_SUCCESS.
            :type error_code: ViStatus

            :rtype: ViChar
        '''
        error_message_ctype = ctypes_types.ViChar_ctype(0)  # TODO(marcoskirsch): allocate a buffer
        error_code = self.library.niDMM_error_message(self.vi, error_code, ctypes.pointer(error_message_ctype))
        errors._handle_error(self, error_code)
        return error_message_ctype.value.decode("ascii")

    def error_query(self):
        '''.. function:: error_query(error_code, error_message)

            Reads an **Error\_Code** and message from the DMM error queue. National
            Instruments DMMs do not contain an error queue. Errors are reported as
            they occur. Therefore, this function does not detect errors; it is
            included for compliance with the *IviDmm Class Specification*.

            :rtype: tuple (error_code, error_message)
                WHERE
                error_code (ViStatus): The **errorCode** returned from the instrument.

                    The default value is VI\_SUCCESS (0).
                error_message (ViChar): Formats the **Error\_Code** into a user-readable message string.
                    +------------+------------------------------------------------------------------------+
                    | |image0|   | **Note**   The array must contain at least 256 elements ViChar[256].   |
                    +------------+------------------------------------------------------------------------+

                    .. |image0| image:: note.gif
        '''
        error_code_ctype = ctypes_types.ViStatus_ctype(0)
        error_message_ctype = ctypes_types.ViChar_ctype(0)  # TODO(marcoskirsch): allocate a buffer
        error_code = self.library.niDMM_error_query(self.vi, ctypes.pointer(error_code_ctype), ctypes.pointer(error_message_ctype))
        errors._handle_error(self, error_code)
        return error_code_ctype.value, error_message_ctype.value.decode("ascii")

    def reset(self):
        '''.. function:: reset()

            Resets the instrument to a known state and sends initialization commands
            to the instrument. The initialization commands set instrument settings
            to the state necessary for the operation of the instrument driver.
        '''
        error_code = self.library.niDMM_reset(self.vi)
        errors._handle_error(self, error_code)
        return

    def revision_query(self):
        '''.. function:: revision_query(instrument_driver_revision, firmware_revision)

            Returns the revision numbers of the instrument driver and instrument
            firmware.

            :rtype: tuple (instrument_driver_revision, firmware_revision)
                WHERE
                instrument_driver_revision (ViChar): Returns a string containing the instrument driver software revision
                    numbers.
                    +------------+------------------------------------------------------------------------+
                    | |image0|   | **Note**   The array must contain at least 256 elements ViChar[256].   |
                    +------------+------------------------------------------------------------------------+

                    .. |image0| image:: note.gif
                firmware_revision (ViChar): Returns a string containing the instrument **firmwareRevision** numbers.
                    +------------+------------------------------------------------------------------------+
                    | |image0|   | **Note**   The array must contain at least 256 elements ViChar[256].   |
                    +------------+------------------------------------------------------------------------+

                    .. |image0| image:: note.gif
        '''
        instrument_driver_revision_ctype = ctypes_types.ViChar_ctype(0)  # TODO(marcoskirsch): allocate a buffer
        firmware_revision_ctype = ctypes_types.ViChar_ctype(0)  # TODO(marcoskirsch): allocate a buffer
        error_code = self.library.niDMM_revision_query(self.vi, ctypes.pointer(instrument_driver_revision_ctype), ctypes.pointer(firmware_revision_ctype))
        errors._handle_error(self, error_code)
        return instrument_driver_revision_ctype.value.decode("ascii"), firmware_revision_ctype.value.decode("ascii")

    def self_test(self):
        '''.. function:: self_test(self_test_result, self_test_message)

            Performs a self-test on the DMM to ensure that the DMM is functioning
            properly. Self-test does not calibrate the DMM.

            .. note::   This function calls `
            niDMM\_reset <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_reset.html')>`__,
            and any configurations previous to the call will be lost. All attributes
            will be set to their default values after the call returns.

            :rtype: tuple (self_test_result, self_test_message)
                WHERE
                self_test_result (ViInt16): Contains the value returned from the instrument self-test. Zero
                    indicates success.

                    On the NI 4080/4082 and NI 4070/4072, the error code 1013 indicates that
                    you should check the fuse and replace it, if necessary.

                    .. note::   Self-test does not check the fuse on the NI 4065, NI 4071,
                    and NI 4081. Hence, even if the fuse is blown on the device, self-test
                    does not return error code 1013.
                self_test_message (ViChar): This parameter contains the string returned from the instrument
                    self-test. The array must contain at least 256 elements.

                    For the NI 4050 and NI 4060, the error codes returned for self-test
                    failures include the following:

                    -  NIDMM\_ERROR\_AC\_TEST\_FAILURE
                    -  NIDMM\_ERROR\_DC\_TEST\_FAILURE
                    -  NIDMM\_ERROR\_RESISTANCE\_TEST\_FAILURE

                    These error codes indicate that the DMM should be repaired.

                    For the NI 4080/4081/4082 and the NI 4070/4071/4072, the error code
                    returned for a self-test failure is NIDMM\_ERROR\_SELF\_TEST\_FAILURE.
                    This error code indicates that the DMM should be repaired.
        '''
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
