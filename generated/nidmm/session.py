# -*- coding: utf-8 -*-
# This file was generated
import ctypes

from nidmm import attributes
from nidmm import enums
from nidmm import errors
from nidmm import library_singleton
from nidmm import visatype


class _Acquisition(object):
    def __init__(self, session):
        self._session = session

    def __enter__(self):
        self._session._initiate()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._session._abort()


class _SessionBase(object):
    '''Base class for all NI-DMM sessions.'''

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

    ac_max_freq = attributes.AttributeViReal64(1250007)
    '''
    Specifies the maximum frequency component of the input signal for AC  measurements. This attribute is used only for error checking and verifies  that the value of this parameter is less than the maximum frequency  of the device. This attribute affects the DMM only when you set the   NIDMM_ATTR_FUNCTION attribute to AC measurements.
    The valid range is 1 Hz-300 kHz for the NI 4070/4071/4072, 10 Hz-100 kHz  for the NI 4065, and 20 Hz-25 kHz for the NI 4050 and NI 4060.
    '''
    ac_min_freq = attributes.AttributeViReal64(1250006)
    '''
    Specifies the minimum frequency component of the input signal for AC  measurements. This attribute affects the DMM only when you set the  NIDMM_ATTR_FUNCTION attribute to AC measurements.
    The valid range is 1 Hz-300 kHz for the NI 4070/4071/4072, 10 Hz-100 kHz  for the NI 4065, and 20 Hz-25 kHz for the NI 4050 and NI 4060.
    '''
    adc_calibration = attributes.AttributeEnum(attributes.AttributeViInt32, enums.ADCCalibration, 1150022)
    '''
    For the NI 4070/4071/4072 only, specifies the ADC calibration mode.
    '''
    aperture_time = attributes.AttributeViReal64(1250321)
    '''
    Specifies the measurement aperture time for the current configuration.  Aperture time is specified in units set by NIDMM_ATTR_APERTURE_TIME_UNITS. To  override the default aperture, set this attribute to the desired  aperture time after calling niDMM_ConfigureMeasurement. To return to the  default, set this attribute to NIDMM_VAL_APERTURE_TIME_AUTO (-1).
    On the NI 4070/4071/4072, the minimum aperture time is 8.89 usec,  and the maximum aperture time is 149 sec. Any number of powerline cycles (PLCs)  within the minimum and maximum ranges is allowed on the NI 4070/4071/4072.
    On the NI 4065 the minimum aperture time is 333 µs, and the maximum aperture time  is 78.2 s. If setting the number of averages directly, the total measurement time is  aperture time X the number of averages, which must be less than 72.8 s. The aperture  times allowed are 333 µs, 667 µs, or multiples of 1.11 ms-for example 1.11 ms, 2.22 ms,  3.33 ms, and so on. If you set an aperture time other than 333 µs, 667 µs, or multiples  of 1.11 ms, the value will be coerced up to the next supported aperture time.
    On the NI 4060, when the powerline frequency is 60 Hz, the PLCs allowed are  1 PLC, 6 PLC, 12 PLC, and 120 PLC. When the powerline frequency is 50 Hz, the  PLCs allowed are 1 PLC, 5 PLC, 10 PLC, and 100 PLC.
    '''
    aperture_time_units = attributes.AttributeEnum(attributes.AttributeViInt32, enums.ApertureTimeUnits, 1250322)
    '''
    Specifies the units of aperture time for the current configuration.
    The NI 4060 does not support an aperture time set in seconds.
    '''
    auto_range_value = attributes.AttributeViReal64(1250331)
    '''
    Specifies the value of the range. If auto ranging, shows the actual value of  the active range. The value of this attribute is set during a read operation.
    '''
    auto_zero = attributes.AttributeEnum(attributes.AttributeViInt32, enums.AutoZero, 1250332)
    '''
    Specifies the AutoZero mode.
    The NI 4050 is not supported.
    '''
    buffer_size = attributes.AttributeViInt32(1150037)
    '''
    Size in samples of the internal data buffer. Maximum is 134,217,727 (OX7FFFFFF) samples. When  set to NIDMM_VAL_BUFFER_SIZE_AUTO (-1), NI-DMM chooses the buffer size.
    '''
    cable_comp_type = attributes.AttributeEnum(attributes.AttributeViInt32, enums.CableCompensationType, 1150045)
    '''
    For the NI 4072 only,  the type of cable compensation that is applied to the current capacitance  or inductance measurement for the current range.
    Changing the function or the range through this attribute or through niDMM_ConfigureMeasurementDigits  resets the value of this attribute to the default value.
    '''
    cache = attributes.AttributeViBoolean(1050004)
    '''
    Specifies whether to cache the value of attributes. When caching is enabled,  the instrument driver keeps track of the current instrument settings and  avoids sending redundant commands to the instrument. Thus, it significantly  increases execution speed. The instrument driver can choose always to cache  or to never cache particular attributes regardless of the setting of this  attribute. The default value is VI_TRUE (1). Use the niDMM_InitWithOptions  function to override this value.
    '''
    channel_count = attributes.AttributeViInt32(1050203)
    '''
    Indicates the number of channels that the specific instrument driver  supports. For each attribute for which the IVI_VAL_MULTI_CHANNEL flag  attribute is set, the IVI engine maintains a separate cache value for each  channel.
    '''
    current_source = attributes.AttributeEnum(attributes.AttributeViReal64, enums.CurrentSource, 1150025)
    '''
    Specifies the current source provided during diode measurements.
    The NI 4050 and NI 4060 are not supported.
    '''
    dc_bias = attributes.AttributeEnum(attributes.AttributeViInt32, enums.DCBias, 1150053)
    '''
    For the NI 4072 only, controls the available DC bias for capacitance measurements.
    '''
    dc_noise_rejection = attributes.AttributeEnum(attributes.AttributeViInt32, enums.DCNoiseRejection, 1150026)
    '''
    Specifies the DC noise rejection mode.
    The NI 4050 and NI 4060 are not supported.
    '''
    driver_setup = attributes.AttributeViString(1050007)
    '''
    This attribute indicates the Driver Setup string that the user specified when  initializing the driver.
    Some cases exist where the end-user must specify instrument driver options  at initialization time.  An example of this is specifying a particular  instrument model from among a family of instruments that the driver supports.   This is useful when using simulation.  The end-user can specify  driver-specific options through the DriverSetup keyword in the optionsString  parameter to the niDMM Init With Options.vi.
    If the user does not specify a Driver Setup string, this attribute returns  an empty string.
    '''
    frequency_voltage_auto_range_value = attributes.AttributeViReal64(1150044)
    '''
    For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the value of
    the frequency voltage range. If auto ranging is enabled, shows the
    actual value of the active frequency voltage range. If not Auto Ranging,
    the value is the same as that of the Frequency Voltage Range property.
    '''
    freq_voltage_range = attributes.AttributeViReal64(1250101)
    '''
    Specifies the maximum amplitude of the input signal for frequency  measurements.
    '''
    function = attributes.AttributeEnum(attributes.AttributeViInt32, enums.Function, 1250001)
    '''
    Specifies the measurement function.
    Refer to the NIDMM_ATTR_FUNCTION topic in  the NI Digital Multimeters Help for device-specific information.
    If you are setting this attribute directly, you must also set the NIDMM_ATTR_OPERATION_MODE attribute,  which controls whether the DMM takes standard single or multipoint measurements, or acquires a waveform.  If you are programming attributes directly, you must set the NIDMM_ATTR_OPERATION_MODE attribute before  setting other configuration attributes. If the NIDMM_ATTR_OPERATION_MODE attribute is set to NIDMM_VAL_WAVEFORM_MODE,  the only valid function types are NIDMM_VAL_WAVEFORM_VOLTAGE and NIDMM_VAL_WAVEFORM_CURRENT. Set the  NIDMM_ATTR_OPERATION_MODE attribute to NIDMM_VAL_IVIDMM_MODE to set all other function values.
    '''
    group_capabilities = attributes.AttributeViString(1050401)
    '''
    A string containing the capabilities and extension groups supported by the  specific driver.
    '''
    input_resistance = attributes.AttributeEnum(attributes.AttributeViReal64, enums.InputResistance, 1150029)
    '''
    Specifies the input resistance of the instrument.
    The NI 4050 and NI 4060 are not supported.
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
    instrument_product_id = attributes.AttributeViInt32(1150061)
    '''
    The PCI product ID.
    '''
    interchange_check = attributes.AttributeViBoolean(1050021)
    '''
    Specifies whether to perform interchangeability checking and log  interchangeability warnings when you call niDMM functions.
    The default value is VI_FALSE.
    Interchangeability warnings indicate that using your application with a  different instrument might cause different behavior.  Call niDMM_GetNextInterchangeWarning  to extract interchange warnings.  Call niDMM_ClearInterchangeWarnings  to clear the list of interchangeability warnings  without reading them.
    Interchangeability checking examines the attributes in a capability group  only if you specify a value for at least one attribute within that group.   Interchangeability warnings can occur when an attribute affects the behavior  of the instrument and you have not set that attribute, or the attribute has  been invalidated since you set it.
    '''
    latency = attributes.AttributeViInt32(1150034)
    '''
    Specifies the number of measurements transferred at a time from the  instrument to an internal buffer. When set to NIDMM_VAL_LATENCY_AUTO (-1),  NI-DMM chooses the transfer size.
    '''
    lc_calculation_model = attributes.AttributeEnum(attributes.AttributeViInt32, enums.LCCalculationModel, 1150052)
    '''
    For the NI 4072 only, specifies the type of algorithm that the measurement processing uses for  capacitance and inductance measurements.
    '''
    lc_number_meas_to_average = attributes.AttributeViInt32(1150055)
    '''
    For the NI 4072 only, specifies the number of LC measurements that are averaged to produce one reading.
    '''
    logical_name = attributes.AttributeViString(1050305)
    '''
    A string containing the logical name of the instrument.
    '''
    meas_complete_dest = attributes.AttributeEnum(attributes.AttributeViInt32, enums.MeasurementCompleteDest, 1250305)
    '''
    Specifies the destination of the measurement complete (MC) signal.
    The NI 4050 is not supported.
    To determine which values are supported by each device, refer to the LabWindows/CVI Trigger Routing section in  the NI Digital Multimeters Help.
    '''
    meas_dest_slope = attributes.AttributeEnum(attributes.AttributeViInt32, enums.MeasurementDestinationSlope, 1150002)
    '''
    Specifies the polarity of the generated measurement complete signal.
    '''
    number_of_averages = attributes.AttributeViInt32(1150032)
    '''
    Specifies the number of averages to perform in a measurement. For the NI 4070/4071/4072,  applies only when the aperture time is not set to AUTO and Auto Zero is ON.  The default is 1.
    The NI 4050 and NI 4060 are not supported.
    '''
    offset_comp_ohms = attributes.AttributeEnum(attributes.AttributeViInt32, enums.OffsetCompensatedOhms, 1150023)
    '''
    For the NI 4070/4071/4072 only, enables or disables offset compensated ohms.
    '''
    open_cable_comp_conductance = attributes.AttributeViReal64(1150049)
    '''
    For the NI 4072 only, specifies the active part (conductance) of the open cable compensation.  The valid range is any real number greater than 0. The default value (-1.0)  indicates that compensation has not taken place.
    Changing the function or the range through this attribute or through niDMM_ConfigureMeasurementDigits  resets the value of this attribute to the default value.
    '''
    open_cable_comp_susceptance = attributes.AttributeViReal64(1150048)
    '''
    For the NI 4072 only, specifies the reactive part (susceptance) of the open cable compensation.  The valid range is any real number greater than 0. The default value (-1.0)  indicates that compensation has not taken place.
    Changing the function or the range through this attribute or through niDMM_ConfigureMeasurementDigits  resets the value of this attribute to the default value.
    '''
    operation_mode = attributes.AttributeEnum(attributes.AttributeViInt32, enums.OperationMode, 1150014)
    '''
    Specifies how the NI 4065 and NI 4070/4071/4072 acquire data. When you call  niDMM_ConfigureMeasurementDigits, NI-DMM sets this attribute to NIDMM_VAL_IVIDMM_MODE.  When you call niDMM_ConfigureWaveformAcquisition, NI-DMM sets this attribute to NIDMM_VAL_WAVEFORM_MODE.  If you are programming attributes directly, you must set this attribute before  setting other configuration attributes.
    '''
    powerline_freq = attributes.AttributeEnum(attributes.AttributeViReal64, enums.PowerlineFrequency, 1250333)
    '''
    Specifies the powerline frequency. The NI 4050 and NI 4060 use this value to select an aperture time to reject  powerline noise by selecting the appropriate internal sample clock and filter. The NI 4065 and  NI 4070/4071/4072 use this value to select a timebase for setting the NIDMM_ATTR_APERTURE_TIME  attribute in powerline cycles (PLCs).
    After configuring powerline frequency, set the NIDMM_ATTR_APERTURE_TIME_UNITS attribute to PLCs.  When setting the NIDMM_ATTR_APERTURE_TIME attribute, select the number of PLCs for the powerline frequency.  For example, if powerline frequency = 50 Hz (or 20ms) and aperture time in PLCs = 5, then aperture time in  Seconds = 20ms * 5 PLCs = 100 ms. Similarly, if powerline frequency = 60 Hz (or 16.667 ms) and aperture time  in PLCs = 6, then aperture time in Seconds = 16.667 ms * 6 PLCs = 100 ms.
    '''
    range = attributes.AttributeViReal64(1250002)
    '''
    Specifies the measurement range. Use positive values to represent the  absolute value of the maximum expected measurement. The value is in units  appropriate for the current value of the NIDMM_ATTR_FUNCTION attribute. For  example, if NIDMM_ATTR_FUNCTION is set to NIDMM_VAL_VOLTS, the units are  volts.
    The NI 4050 and NI 4060 only support Auto Range when the trigger and  sample trigger is set to IMMEDIATE.
    NIDMM_VAL_AUTO_RANGE_ON -1.0
    NI-DMM performs an Auto Range before acquiring the measurement.
    NIDMM_VAL_AUTO_RANGE_OFF -2.0
    NI-DMM sets the Range to the current NIDMM_ATTR_AUTO_RANGE_VALUE and uses this range  for all subsequent measurements until the measurement configuration is changed.
    NIDMM_VAL_AUTO_RANGE_ONCE -3.0
    NI-DMM performs an Auto Range before acquiring the next measurement. The NIDMM_ATTR_AUTO_RANGE_VALUE  is stored and used for all subsequent measurements until the measurement configuration is changed.
    '''
    range_check = attributes.AttributeViBoolean(1050002)
    '''
    Specifies whether to validate attribute values and function parameters. If  enabled, the instrument driver validates the parameter values passed to  driver functions. Range checking parameters is very useful for debugging.  After the user program is validated, this attribute can be set to VI_FALSE (0) to  disable range checking and maximize performance.
    The default value is VI_TRUE (1). Use the niDMM_InitWithOptions function to  override this value.
    '''
    record_coercions = attributes.AttributeViBoolean(1050006)
    '''
    Specifies whether the IVI engine keeps a list of the value coercions it makes  for ViInt32 and ViReal64 attributes. Call niDMM_GetNextCoercionRecord to extract  and delete the oldest coercion record from the list.
    The default value is VI_FALSE (0). Use the niDMM_InitWithOptions function to  override this value.
    '''
    resolution_absolute = attributes.AttributeViReal64(1250008)
    '''
    Specifies the measurement resolution in absolute units. Setting this  attribute to higher values increases the measurement accuracy. Setting this  attribute to lower values increases the measurement speed.
    NI-DMM ignores this attribute for capacitance and inductance measurements on the NI 4072.  To achieve better resolution for such measurements, use the NIDMM_ATTR_LC_NUMBER_MEAS_TO_AVERAGE attribute.
    '''
    sample_count = attributes.AttributeViInt32(1250301)
    '''
    Specifies the number of measurements the DMM takes each time it receives a  trigger in a multiple point acquisition.
    '''
    sample_interval = attributes.AttributeViReal64(1250303)
    '''
    Specifies the amount of time in seconds the DMM waits between measurement cycles.  This attribute only applies when the NIDMM_ATTR_SAMPLE_TRIGGER attribute is set to INTERVAL.
    On the NI 4060, the value for this attribute is used as the settling time.  When this attribute is set to 0, the NI 4060 does not settle between  measurement cycles. The onboard timing resolution is 1 µs on the NI 4060.
    The NI 4065 and NI 4070/4071/4072 use the value specified in this attribute as additional  delay. On the NI 4065 and NI 4070/4071/4072, the onboard timing resolution is 34.72 ns and  the valid range is 0-149 s.
    Only positive values are valid when setting the sample interval.
    The NI 4050 is not supported.
    '''
    sample_trigger = attributes.AttributeEnum(attributes.AttributeViInt32, enums.SampleTrigger, 1250302)
    '''
    Specifies the sample trigger source.
    To determine which values are supported by each device, refer to the LabWindows/CVI Trigger Routing section in  the NI Digital Multimeters Help.
    '''
    sample_trigger_slope = attributes.AttributeEnum(attributes.AttributeViInt32, enums.SampleTrigSlope, 1150010)
    '''
    Specifies the edge of the signal from the specified sample trigger source on  which the DMM is triggered.
    '''
    serial_number = attributes.AttributeViString(1150054)
    '''
    A string containing the serial number of the instrument. This attribute corresponds  to the serial number label that is attached to most products.
    '''
    settle_time = attributes.AttributeViReal64(1150028)
    '''
    Specifies the settling time in seconds. To override the default settling time,  set this attribute. To return to the default, set this attribute to  NIDMM_VAL_SETTLE_TIME_AUTO (-1).
    The NI 4050 and NI 4060 are not supported.
    '''
    short_cable_comp_reactance = attributes.AttributeViReal64(1150046)
    '''
    For the NI 4072 only, represents the reactive part (reactance) of the short cable compensation.  The valid range is any real number greater than 0. The default value (-1)  indicates that compensation has not taken place.
    Changing the function or the range through this attribute or through niDMM_ConfigureMeasurementDigits  resets the value of this attribute to the default value.
    '''
    short_cable_comp_resistance = attributes.AttributeViReal64(1150047)
    '''
    For the NI 4072 only, represents the active part (resistance) of the short cable compensation.  The valid range is any real number greater than 0. The default value (-1)  indicates that compensation has not taken place.
    Changing the function or the range through this attribute or through niDMM_ConfigureMeasurementDigits  resets the value of this attribute to the default value.
    '''
    shunt_value = attributes.AttributeViReal64(1150003)
    '''
    For the NI 4050 only, specifies the shunt resistance value.
    The NI 4050 requires an external shunt resistor for current measurements.  This attribute should be set to the value of shunt resistor.
    '''
    simulate = attributes.AttributeViBoolean(1050005)
    '''
    Specifies whether or not to simulate instrument driver I/O operations. If  simulation is enabled, instrument driver functions perform range checking and  call IVI Get and Set functions, but they do not perform  instrument I/O. For output parameters that represent instrument data, the  instrument driver functions return calculated values.
    The default value is VI_FALSE (0). Use the niDMM_InitWithOptions function to  override this setting.
    Simulate can only be set within the InitWithOptions function.  The attribute value cannot be changed outside of the function.
    '''
    specific_driver_class_spec_major_version = attributes.AttributeViInt32(1050515)
    '''
    The major version number of the class specification for the specific driver.
    '''
    specific_driver_class_spec_minor_version = attributes.AttributeViInt32(1050516)
    '''
    The minor version number of the class specification for the specific driver.
    '''
    specific_driver_description = attributes.AttributeViString(1050514)
    '''
    A string containing a description of the specific driver.
    '''
    specific_driver_vendor = attributes.AttributeViString(1050513)
    '''
    A string containing the vendor of the specific driver.
    '''
    supported_instrument_models = attributes.AttributeViString(1050327)
    '''
    A string containing the instrument models supported by the specific driver.
    '''
    temp_rtd_a = attributes.AttributeViReal64(1150121)
    '''
    Specifies the Callendar-Van Dusen A coefficient for RTD scaling when the RTD Type property   is set to Custom. The default value is 3.9083e-3 (Pt3851).
    '''
    temp_rtd_b = attributes.AttributeViReal64(1150122)
    '''
    Specifies the Callendar-Van Dusen B coefficient for RTD scaling when the RTD Type property  is set to Custom. The default value is -5.775e-7(Pt3851).
    '''
    temp_rtd_c = attributes.AttributeViReal64(1150123)
    '''
    Specifies the Callendar-Van Dusen C coefficient for RTD scaling when the RTD Type property  is set to Custom. The default value is -4.183e-12(Pt3851).
    '''
    temp_rtd_res = attributes.AttributeViReal64(1250242)
    '''
    Specifies the RTD resistance at 0 degrees Celsius. This applies to all supported RTDs,  including custom RTDs. The default value is 100 (?).
    '''
    temp_rtd_type = attributes.AttributeEnum(attributes.AttributeViInt32, enums.RTDType, 1150120)
    '''
    Specifies the type of RTD used to measure temperature. The default value is NIDMM_VAL_TEMP_RTD_PT3851.
    Refer to the NIDMM_ATTR_TEMP_RTD_TYPE topic in the NI Digital Multimeters Help for additional information about defined values.
    '''
    temp_tc_fixed_ref_junc = attributes.AttributeViReal64(1250233)
    '''
    Specifies the reference junction temperature when a fixed reference junction is used to take  a thermocouple measurement. The default value is 25.0 (°C).
    '''
    temp_tc_ref_junc_type = attributes.AttributeEnum(attributes.AttributeViInt32, enums.ThermocoupleReferenceJunctionType, 1250232)
    '''
    Specifies the type of reference junction to be used in the reference junction compensation  of a thermocouple. The only supported value, NIDMM_VAL_TEMP_REF_JUNC_FIXED, is fixed.
    '''
    temp_tc_type = attributes.AttributeEnum(attributes.AttributeViInt32, enums.ThermocoupleType, 1250231)
    '''
    Specifies the type of thermocouple used to measure the temperature. The default value is NIDMM_VAL_TEMP_TC_J.
    '''
    temp_thermistor_a = attributes.AttributeViReal64(1150125)
    '''
    Specifies the Steinhart-Hart A coefficient for thermistor scaling when the Thermistor Type  property is set to Custom. The default value is 0.0010295 (44006).
    '''
    temp_thermistor_b = attributes.AttributeViReal64(1150126)
    '''
    Specifies the Steinhart-Hart B coefficient for thermistor scaling when the Thermistor Type  proerty is set to Custom. The default value is 0.0002391 (44006).
    '''
    temp_thermistor_c = attributes.AttributeViReal64(1150127)
    '''
    Specifies the Steinhart-Hart C coefficient for thermistor scaling when the Thermistor Type  property is set to Custom. The default value is 1.568e-7 (44006).
    '''
    temp_thermistor_type = attributes.AttributeEnum(attributes.AttributeViInt32, enums.ThermistorType, 1150124)
    '''
    Specifies the type of thermistor used to measure the temperature. The default value is  NIDMM_VAL_TEMP_THERMISTOR_44006.
    Refer to the NIDMM_ATTR_TEMP_THERMISTOR_TYPE topic in the NI Digital Multimeters Help for additional information about defined values.
    '''
    temp_transducer_type = attributes.AttributeEnum(attributes.AttributeViInt32, enums.TransducerType, 1250201)
    '''
    Specifies the type of device used to measure the temperature. The default value is NIDMM_VAL_4_THERMOCOUPLE.
    '''
    trigger_count = attributes.AttributeViInt32(1250304)
    '''
    Specifies the number of triggers the DMM receives before returning to the  Idle state.
    This attribute can be set to any positive ViInt32 value for the NI 4065 and NI 4070/4071/4072.
    The NI 4050 and NI 4060 support this attribute being set to 1.
    Refer to the Multiple Point Acquisitions section of the NI Digital Multimeters Help for more information.
    '''
    trigger_delay = attributes.AttributeViReal64(1250005)
    '''
    Specifies the time (in seconds) that the DMM waits after it has received a trigger before taking a measurement.  The default value is AUTO DELAY (-1), which means that the DMM waits an appropriate settling time before taking  the measurement. (-1) signifies that AUTO DELAY is on, and (-2) signifies that AUTO DELAY is off.
    The NI 4065 and NI 4070/4071/4072 use the value specified in this attribute as additional settling time.  For the The NI 4065 and NI 4070/4071/4072, the valid range for Trigger Delay is AUTO DELAY (-1) or 0.0-149.0  seconds and the onboard timing resolution is 34.72 ns.
    On the NI 4060, if this attribute is set to 0, the DMM does not settle before taking the measurement.  On the NI 4060, the valid range for AUTO DELAY (-1) is 0.0-12.0 seconds and the onboard timing resolution  is 100 ms.
    When using the NI 4050, this attribute must be set to AUTO DELAY (-1).
    Use positive values to set the trigger delay in seconds.
    Valid Range: NIDMM_VAL_AUTO_DELAY (-1.0), 0.0-12.0 seconds (NI 4060 only)
    Default Value: NIDMM_VAL_AUTO_DELAY
    '''
    trigger_slope = attributes.AttributeEnum(attributes.AttributeViInt32, enums.TriggerSlope, 1250334)
    '''
    Specifies the edge of the signal from the specified trigger source on which  the DMM is triggered.
    '''
    trigger_source = attributes.AttributeEnum(attributes.AttributeViInt32, enums.TriggerSource, 1250004)
    '''
    Specifies the trigger source. When niDMM_Initiate is called, the DMM waits  for the trigger specified with this attribute. After it receives the trigger,  the DMM waits the length of time specified with the NIDMM_ATTR_TRIGGER_DELAY  attribute. The DMM then takes a measurement.
    This attribute is not supported on the NI 4050.
    To determine which values are supported by each device, refer to the LabWindows/CVI Trigger Routing section in  the NI Digital Multimeters Help.
    '''
    waveform_coupling = attributes.AttributeEnum(attributes.AttributeViInt32, enums.WaveformCoupling, 1150027)
    '''
    For the NI 4070/4071/4072 only, specifies the coupling during a waveform acquisition.
    '''
    waveform_points = attributes.AttributeViInt32(1150019)
    '''
    For the NI 4070/4071/4072 only, specifies the number of points to acquire in a waveform acquisition.
    '''
    waveform_rate = attributes.AttributeViReal64(1150018)
    '''
    For the NI 4070/4071/4072 only, specifies the rate of the waveform acquisition in Samples per second (S/s).  The valid Range is 10.0-1,800,000 S/s. Values are coerced to the  closest integer divisor of 1,800,000. The default value is 1,800,000.
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

    def _get_attribute_vi_boolean(self, attribute_id):
        '''_get_attribute_vi_boolean

        Queries the value of a ViBoolean attribute. You can use this function to
        get the values of instrument-specific attributes and inherent IVI
        attributes.

        If the attribute represents an instrument state, this function performs
        instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular attribute.
        -  State caching is enabled, and the currently cached value is invalid.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nidmm.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidmm.Session instance, and calling this method on the result.:

            session['0,1']._get_attribute_vi_boolean(attribute_id)

        Args:
            attribute_id (int): Pass the ID of an attribute.

        Returns:
            attribute_value (bool): Returns the current value of the attribute. Pass the address of a
                ViBoolean variable.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case 9
        attribute_value_ctype = visatype.ViBoolean()  # case 14
        error_code = self._library.niDMM_GetAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_id_ctype, ctypes.pointer(attribute_value_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(attribute_value_ctype.value)

    def _get_attribute_vi_int32(self, attribute_id):
        '''_get_attribute_vi_int32

        Queries the value of a ViInt32 attribute. You can use this function to
        get the values of instrument-specific attributes and inherent IVI
        attributes.

        If the attribute represents an instrument state, this function performs
        instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular attribute.
        -  State caching is enabled, and the currently cached value is invalid.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nidmm.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidmm.Session instance, and calling this method on the result.:

            session['0,1']._get_attribute_vi_int32(attribute_id)

        Args:
            attribute_id (int): Pass the ID of an attribute.

        Returns:
            attribute_value (int): Returns the current value of the attribute. Pass the address of a
                ViInt32 variable.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case 9
        attribute_value_ctype = visatype.ViInt32()  # case 14
        error_code = self._library.niDMM_GetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_id_ctype, ctypes.pointer(attribute_value_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(attribute_value_ctype.value)

    def _get_attribute_vi_real64(self, attribute_id):
        '''_get_attribute_vi_real64

        Queries the value of a ViReal64 attribute. You can use this function to
        get the values of instrument-specific attributes and inherent IVI
        attributes.

        If the attribute represents an instrument state, this function performs
        instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular attribute.
        -  State caching is enabled, and the currently cached value is invalid.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nidmm.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidmm.Session instance, and calling this method on the result.:

            session['0,1']._get_attribute_vi_real64(attribute_id)

        Args:
            attribute_id (int): Pass the ID of an attribute.

        Returns:
            attribute_value (float): Returns the current value of the attribute. Pass the address of a
                ViReal64 variable.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case 9
        attribute_value_ctype = visatype.ViReal64()  # case 14
        error_code = self._library.niDMM_GetAttributeViReal64(vi_ctype, channel_name_ctype, attribute_id_ctype, ctypes.pointer(attribute_value_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(attribute_value_ctype.value)

    def _get_attribute_vi_string(self, attribute_id):
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

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nidmm.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidmm.Session instance, and calling this method on the result.:

            session['0,1']._get_attribute_vi_string(attribute_id)

        Args:
            attribute_id (int): Pass the ID of an attribute.
            buffer_size (int): Pass the number of bytes in the ViChar array you specify for the
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
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case 9
        buffer_size_ctype = visatype.ViInt32()  # case 7
        attribute_value_ctype = None  # case 12
        error_code = self._library.niDMM_GetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, buffer_size_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = visatype.ViInt32(error_code)  # TODO(marcoskirsch): use get_ctype_variable_declaration_snippet()
        attribute_value_ctype = (visatype.ViChar * buffer_size_ctype.value)()  # TODO(marcoskirsch): use get_ctype_variable_declaration_snippet()
        error_code = self._library.niDMM_GetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, buffer_size_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return attribute_value_ctype.value.decode(self._encoding)

    def _get_error(self):
        '''_get_error

        Returns the error information associated with the
        **Instrument_Handle**. This function retrieves and then clears the
        error information for the session. If you leave the
        **Instrument_Handle** unwired, this function retrieves and then clears
        the error information for the process.

        Args:
            buffer_size (int): Passes the number of bytes in the ViChar array you specify for the
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
            error_code (int): Returns the **error_code** for the session or execution thread. If you
                pass 0 for the **Buffer_Size**, you can pass VI_NULL for this
                parameter.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        error_code_ctype = visatype.ViStatus()  # case 14
        buffer_size_ctype = visatype.ViInt32()  # case 7
        description_ctype = None  # case 12
        error_code = self._library.niDMM_GetError(vi_ctype, ctypes.pointer(error_code_ctype), buffer_size_ctype, description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=True)
        buffer_size_ctype = visatype.ViInt32(error_code)  # TODO(marcoskirsch): use get_ctype_variable_declaration_snippet()
        description_ctype = (visatype.ViChar * buffer_size_ctype.value)()  # TODO(marcoskirsch): use get_ctype_variable_declaration_snippet()
        error_code = self._library.niDMM_GetError(vi_ctype, ctypes.pointer(error_code_ctype), buffer_size_ctype, description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return int(error_code_ctype.value), description_ctype.value.decode(self._encoding)

    def _set_attribute_vi_boolean(self, attribute_id, attribute_value):
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

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nidmm.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidmm.Session instance, and calling this method on the result.:

            session['0,1']._set_attribute_vi_boolean(attribute_id, attribute_value)

        Args:
            attribute_id (int): Pass the ID of an attribute.
            attribute_value (bool): Pass the value that you want to set the attribute to.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case 9
        attribute_value_ctype = visatype.ViBoolean(attribute_value)  # case 9
        error_code = self._library.niDMM_SetAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_int32(self, attribute_id, attribute_value):
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

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nidmm.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidmm.Session instance, and calling this method on the result.:

            session['0,1']._set_attribute_vi_int32(attribute_id, attribute_value)

        Args:
            attribute_id (int): Pass the ID of an attribute.
            attribute_value (int): Pass the value that you want to set the attribute to.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case 9
        attribute_value_ctype = visatype.ViInt32(attribute_value)  # case 9
        error_code = self._library.niDMM_SetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_real64(self, attribute_id, attribute_value):
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

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nidmm.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidmm.Session instance, and calling this method on the result.:

            session['0,1']._set_attribute_vi_real64(attribute_id, attribute_value)

        Args:
            attribute_id (int): Pass the ID of an attribute.
            attribute_value (float): Pass the value that you want to set the attribute to.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case 9
        attribute_value_ctype = visatype.ViReal64(attribute_value)  # case 9
        error_code = self._library.niDMM_SetAttributeViReal64(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_string(self, attribute_id, attribute_value):
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

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nidmm.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidmm.Session instance, and calling this method on the result.:

            session['0,1']._set_attribute_vi_string(attribute_id, attribute_value)

        Args:
            attribute_id (int): Pass the ID of an attribute.
            attribute_value (string): Pass the value that you want to set the attribute to.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case 9
        attribute_value_ctype = ctypes.create_string_buffer(attribute_value.encode(self._encoding))  # case 3
        error_code = self._library.niDMM_SetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _error_message(self, error_code):
        '''_error_message

        Takes the **Error_Code** returned by the instrument driver functions,
        interprets it, and returns it as a user-readable string.

        Args:
            error_code (int): The **error_code** returned from the instrument. The default is 0,
                indicating VI_SUCCESS.

        Returns:
            error_message (string): The error information formatted into a string.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        error_code_ctype = visatype.ViStatus(error_code)  # case 9
        error_message_ctype = (visatype.ViChar * 256)()  # case 11
        error_code = self._library.niDMM_error_message(vi_ctype, error_code_ctype, error_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return error_message_ctype.value.decode(self._encoding)


class _RepeatedCapability(_SessionBase):
    '''Allows for setting/getting properties and calling methods for specific repeated capabilities (such as channels) on your session.'''

    def __init__(self, vi, repeated_capability):
        super(_RepeatedCapability, self).__init__(repeated_capability)
        self._vi = vi
        self._is_frozen = True


class Session(_SessionBase):
    '''An NI-DMM session to a National Instruments Digital Multimeter'''

    def __init__(self, resource_name, id_query=False, reset_device=False, option_string=''):
        super(Session, self).__init__(repeated_capability='')
        self._vi = 0  # This must be set before calling _init_with_options().
        self._vi = self._init_with_options(resource_name, id_query, reset_device, option_string)
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

        Aborts a previously initiated measurement and returns the DMM to the
        Idle state.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        error_code = self._library.niDMM_Abort(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_ac_bandwidth(self, ac_minimum_frequency_hz, ac_maximum_frequency_hz):
        '''configure_ac_bandwidth

        Configures the AC_MIN_FREQ and AC_MAX_FREQ
        attributes, which the DMM uses for AC measurements.

        Args:
            ac_minimum_frequency_hz (float): Specifies the minimum expected frequency component of the input signal
                in hertz. This parameter affects the DMM only when you set the
                function attribute to AC measurements. NI-DMM uses this
                parameter to calculate the proper aperture for the measurement.
                The driver sets the AC_MIN_FREQ attribute to this value.
                The valid range is 1 Hz–300 kHz for the NI 4080/4081/4082 and the NI
                4070/4071/4072, 10 Hz–100 Hz for the NI 4065, and 20 Hz–25 kHz for the
                NI 4050 and NI 4060.
            ac_maximum_frequency_hz (float): Specifies the maximum expected frequency component of the input signal
                in hertz within the device limits. This parameter is used only for error
                checking and verifies that the value of this parameter is less than the
                maximum frequency of the device.

                This parameter affects the DMM only when you set the
                function attribute to AC measurements. The driver sets the
                AC_MAX_FREQ attribute to this value. The valid range is 1
                Hz–300 kHz for the NI 4080/4081/4082 and the NI 4070/4071/4072, 10
                Hz–100 Hz for the NI 4065, and 20 Hz–25 kHz for the NI 4050 and NI 4060.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        ac_minimum_frequency_hz_ctype = visatype.ViReal64(ac_minimum_frequency_hz)  # case 9
        ac_maximum_frequency_hz_ctype = visatype.ViReal64(ac_maximum_frequency_hz)  # case 9
        error_code = self._library.niDMM_ConfigureACBandwidth(vi_ctype, ac_minimum_frequency_hz_ctype, ac_maximum_frequency_hz_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_measurement_absolute(self, measurement_function, range, resolution_absolute):
        '''configure_measurement_absolute

        Configures the common attributes of the measurement. These attributes
        include function, range, and
        RESOLUTION_ABSOLUTE.

        Args:
            measurement_function (enums.Function): Specifies the **measurement_function** used to acquire the measurement.
                The driver sets function to this value.
            range (float): Specifies the **range** for the function specified in the
                **Measurement_Function** parameter. When frequency is specified in the
                **Measurement_Function** parameter, you must supply the minimum
                frequency expected in the **range** parameter. For example, you must
                type in 100 Hz if you are measuring 101 Hz or higher.
                For all other functions, you must supply a **range** that exceeds the
                value that you are measuring. For example, you must type in 10 V if you
                are measuring 9 V. **range** values are coerced up to the closest input
                **range**. Refer to the `Devices
                Overview <devices>`__ for a list of valid
                ranges. The driver sets range to this value. The default is
                0.02 V.

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
            resolution_absolute (float): Specifies the absolute resolution for the measurement. NI-DMM sets
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
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        measurement_function_ctype = visatype.ViInt32(measurement_function.value)  # case 10
        range_ctype = visatype.ViReal64(range)  # case 9
        resolution_absolute_ctype = visatype.ViReal64(resolution_absolute)  # case 9
        error_code = self._library.niDMM_ConfigureMeasurementAbsolute(vi_ctype, measurement_function_ctype, range_ctype, resolution_absolute_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_measurement_digits(self, measurement_function, range, resolution_digits):
        '''configure_measurement_digits

        Configures the common attributes of the measurement. These attributes
        include function, range, and
        RESOLUTION_DIGITS.

        Args:
            measurement_function (enums.Function): Specifies the **measurement_function** used to acquire the measurement.
                The driver sets function to this value.
            range (float): Specifies the range for the function specified in the
                **Measurement_Function** parameter. When frequency is specified in the
                **Measurement_Function** parameter, you must supply the minimum
                frequency expected in the **range** parameter. For example, you must
                type in 100 Hz if you are measuring 101 Hz or higher.
                For all other functions, you must supply a range that exceeds the value
                that you are measuring. For example, you must type in 10 V if you are
                measuring 9 V. range values are coerced up to the closest input range.
                Refer to the `Devices
                Overview <devices>`__ for a list of valid
                ranges. The driver sets range to this value. The default is
                0.02 V.

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
            resolution_digits (float): Specifies the resolution of the measurement in digits. The driver sets
                the `Devices Overview <devices>`__ for a
                list of valid ranges. The driver sets RESOLUTION_DIGITS
                attribute to this value. This parameter is ignored when the **Range**
                parameter is set to NIDMM_VAL_AUTO_RANGE_ON (-1.0) or
                NIDMM_VAL_AUTO_RANGE_ONCE (-3.0). The default is 5½.

                Note:
                NI-DMM ignores this parameter for capacitance and inductance
                measurements on the NI 4072. To achieve better resolution for such
                measurements, use the LC_NUMBER_MEAS_TO_AVERAGE
                attribute.
        '''
        if type(measurement_function) is not enums.Function:
            raise TypeError('Parameter mode must be of type ' + str(enums.Function))
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        measurement_function_ctype = visatype.ViInt32(measurement_function.value)  # case 10
        range_ctype = visatype.ViReal64(range)  # case 9
        resolution_digits_ctype = visatype.ViReal64(resolution_digits)  # case 9
        error_code = self._library.niDMM_ConfigureMeasurementDigits(vi_ctype, measurement_function_ctype, range_ctype, resolution_digits_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_multi_point(self, trigger_count, sample_count, sample_trigger=enums.SampleTrigger.IMMEDIATE, sample_interval=-1):
        '''configure_multi_point

        Configures the attributes for multipoint measurements. These attributes
        include TRIGGER_COUNT, SAMPLE_COUNT,
        SAMPLE_TRIGGER, and SAMPLE_INTERVAL.

        For continuous acquisitions, set TRIGGER_COUNT or
        SAMPLE_COUNT to zero. For more information, refer to
        `Multiple Point
        Acquisitions <multi_point>`__,
        `Triggering <trigger>`__, and `Using
        Switches <switch_selection>`__.

        Args:
            trigger_count (int): Sets the number of triggers you want the DMM to receive before returning
                to the Idle state. The driver sets TRIGGER_COUNT to this
                value. The default value is 1.
            sample_count (int): Sets the number of measurements the DMM makes in each measurement
                sequence initiated by a trigger. The driver sets
                SAMPLE_COUNT to this value. The default value is 1.
            sample_trigger (enums.SampleTrigger): Specifies the **sample_trigger** source you want to use. The driver
                sets SAMPLE_TRIGGER to this value. The default is
                Immediate.

                Note:
                To determine which values are supported by each device, refer to the
                `LabWindows/CVI Trigger
                Routing <cvitrigger_routing>`__ section.
            sample_interval (float): Sets the amount of time in seconds the DMM waits between measurement
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
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        trigger_count_ctype = visatype.ViInt32(trigger_count)  # case 9
        sample_count_ctype = visatype.ViInt32(sample_count)  # case 9
        sample_trigger_ctype = visatype.ViInt32(sample_trigger.value)  # case 10
        sample_interval_ctype = visatype.ViReal64(sample_interval)  # case 9
        error_code = self._library.niDMM_ConfigureMultiPoint(vi_ctype, trigger_count_ctype, sample_count_ctype, sample_trigger_ctype, sample_interval_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_open_cable_comp_values(self, conductance, susceptance):
        '''configure_open_cable_comp_values

        For the NI 4082 and NI 4072 only, configures the
        OPEN_CABLE_COMP_CONDUCTANCE and
        OPEN_CABLE_COMP_SUSCEPTANCE attributes.

        Args:
            conductance (float): Specifies the open cable compensation **conductance**.
            susceptance (float): Specifies the open cable compensation **susceptance**.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        conductance_ctype = visatype.ViReal64(conductance)  # case 9
        susceptance_ctype = visatype.ViReal64(susceptance)  # case 9
        error_code = self._library.niDMM_ConfigureOpenCableCompValues(vi_ctype, conductance_ctype, susceptance_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_power_line_frequency(self, power_line_frequency_hz):
        '''configure_power_line_frequency

        Specifies the powerline frequency.

        Args:
            power_line_frequency_hz (float): **Powerline Frequency** specifies the powerline frequency in hertz.
                NI-DMM sets the Powerline Frequency property to this value.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        power_line_frequency_hz_ctype = visatype.ViReal64(power_line_frequency_hz)  # case 9
        error_code = self._library.niDMM_ConfigurePowerLineFrequency(vi_ctype, power_line_frequency_hz_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_rtd_custom(self, rtd_a, rtd_b, rtd_c):
        '''configure_rtd_custom

        Configures the A, B, and C parameters for a custom RTD.

        Args:
            rtd_a (float): Specifies the Callendar-Van Dusen A coefficient for RTD scaling when RTD
                Type parameter is set to Custom in the configure_rtd_type function.
                The default is 3.9083e-3 (Pt3851)
            rtd_b (float): Specifies the Callendar-Van Dusen B coefficient for RTD scaling when RTD
                Type parameter is set to Custom in the configure_rtd_type function.
                The default is -5.775e-7 (Pt3851).
            rtd_c (float): Specifies the Callendar-Van Dusen C coefficient for RTD scaling when RTD
                Type parameter is set to Custom in the configure_rtd_type function.
                The default is -4.183e-12 (Pt3851).
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        rtd_a_ctype = visatype.ViReal64(rtd_a)  # case 9
        rtd_b_ctype = visatype.ViReal64(rtd_b)  # case 9
        rtd_c_ctype = visatype.ViReal64(rtd_c)  # case 9
        error_code = self._library.niDMM_ConfigureRTDCustom(vi_ctype, rtd_a_ctype, rtd_b_ctype, rtd_c_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_rtd_type(self, rtd_type, rtd_resistance):
        '''configure_rtd_type

        Configures the RTD Type and RTD Resistance parameters for an RTD.

        Args:
            rtd_type (enums.RTDType): Specifies the type of RTD used to measure the temperature resistance.
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
            rtd_resistance (float): Specifies the RTD resistance in ohms at 0 °C. NI-DMM uses this value to
                set the RTD Resistance property. The default is 100 (Ω).
        '''
        if type(rtd_type) is not enums.RTDType:
            raise TypeError('Parameter mode must be of type ' + str(enums.RTDType))
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        rtd_type_ctype = visatype.ViInt32(rtd_type.value)  # case 10
        rtd_resistance_ctype = visatype.ViReal64(rtd_resistance)  # case 9
        error_code = self._library.niDMM_ConfigureRTDType(vi_ctype, rtd_type_ctype, rtd_resistance_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_short_cable_comp_values(self, resistance, reactance):
        '''configure_short_cable_comp_values

        For the NI 4082 and NI 4072 only, configures the
        SHORT_CABLE_COMP_RESISTANCE and
        SHORT_CABLE_COMP_REACTANCE attributes.

        Args:
            resistance (float): Specifies the short cable compensation **resistance**.
            reactance (float): Specifies the short cable compensation **reactance**.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        resistance_ctype = visatype.ViReal64(resistance)  # case 9
        reactance_ctype = visatype.ViReal64(reactance)  # case 9
        error_code = self._library.niDMM_ConfigureShortCableCompValues(vi_ctype, resistance_ctype, reactance_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_thermistor_custom(self, thermistor_a, thermistor_b, thermistor_c):
        '''configure_thermistor_custom

        Configures the A, B, and C parameters for a custom thermistor.

        Args:
            thermistor_a (float): Specifies the Steinhart-Hart A coefficient for thermistor scaling when
                Thermistor Type is set to Custom in the ConfigureThermistorType
                function. The default is 1.0295e-3 (44006).
            thermistor_b (float): Specifies the Steinhart-Hart B coefficient for thermistor scaling when
                Thermistor Type is set to Custom in the ConfigureThermistorType
                function. The default is 2.391e-4 (44006).
            thermistor_c (float): Specifies the Steinhart-Hart C coefficient for thermistor scaling when
                Thermistor Type is set to Custom in the ConfigureThermistorType
                function. The default is 1.568e-7 (44006).
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        thermistor_a_ctype = visatype.ViReal64(thermistor_a)  # case 9
        thermistor_b_ctype = visatype.ViReal64(thermistor_b)  # case 9
        thermistor_c_ctype = visatype.ViReal64(thermistor_c)  # case 9
        error_code = self._library.niDMM_ConfigureThermistorCustom(vi_ctype, thermistor_a_ctype, thermistor_b_ctype, thermistor_c_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_thermocouple(self, thermocouple_type, reference_junction_type=enums.ThermocoupleReferenceJunctionType.FIXED):
        '''configure_thermocouple

        Configures the thermocouple type and reference junction type for a
        chosen thermocouple.

        Args:
            thermocouple_type (enums.ThermocoupleType): Specifies the type of thermocouple used to measure the temperature.
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
            reference_junction_type (enums.ThermocoupleReferenceJunctionType): Specifies the type of reference junction to be used in the reference
                junction compensation of a thermocouple measurement. NI-DMM uses this
                value to set the Reference Junction Type property. The only supported
                value is NIDMM_VAL_TEMP_REF_JUNC_FIXED.
        '''
        if type(thermocouple_type) is not enums.ThermocoupleType:
            raise TypeError('Parameter mode must be of type ' + str(enums.ThermocoupleType))
        if type(reference_junction_type) is not enums.ThermocoupleReferenceJunctionType:
            raise TypeError('Parameter mode must be of type ' + str(enums.ThermocoupleReferenceJunctionType))
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        thermocouple_type_ctype = visatype.ViInt32(thermocouple_type.value)  # case 10
        reference_junction_type_ctype = visatype.ViInt32(reference_junction_type.value)  # case 10
        error_code = self._library.niDMM_ConfigureThermocouple(vi_ctype, thermocouple_type_ctype, reference_junction_type_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_trigger(self, trigger_source, trigger_delay=-1):
        '''configure_trigger

        Configures the DMM **Trigger_Source** and **Trigger_Delay**. Refer to
        `Triggering <trigger>`__ and `Using
        Switches <switch_selection>`__ for more
        information.

        Args:
            trigger_source (enums.TriggerSource): Specifies the **trigger_source** that initiates the acquisition. The
                driver sets TRIGGER_SOURCE to this value. Software
                configures the DMM to wait until send_software_trigger is called
                before triggering the DMM.

                Note:
                To determine which values are supported by each device, refer to the
                `LabWindows/CVI Trigger
                Routing <cvitrigger_routing>`__ section.
            trigger_delay (float): Specifies the time that the DMM waits after it has received a trigger
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
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        trigger_source_ctype = visatype.ViInt32(trigger_source.value)  # case 10
        trigger_delay_ctype = visatype.ViReal64(trigger_delay)  # case 9
        error_code = self._library.niDMM_ConfigureTrigger(vi_ctype, trigger_source_ctype, trigger_delay_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_waveform_acquisition(self, measurement_function, range, rate, waveform_points):
        '''configure_waveform_acquisition

        Configures the DMM for waveform acquisitions. This feature is supported
        on the NI 4080/4081/4082 and the NI 4070/4071/4072.

        Args:
            measurement_function (enums.Function): Specifies the **measurement_function** used in a waveform acquisition.
                The driver sets function to this value.

                +--------------------------------------+------+------------------+
                | NIDMM_VAL_WAVEFORM_VOLTAGE (default) | 1003 | Voltage Waveform |
                +--------------------------------------+------+------------------+
                | NIDMM_VAL_WAVEFORM_CURRENT           | 1004 | Current Waveform |
                +--------------------------------------+------+------------------+
            range (float): Specifies the expected maximum amplitude of the input signal and sets
                the **range** for the **Measurement_Function**. NI-DMM sets
                range to this value. **range** values are coerced up to the
                closest input **range**. The default is 10.0.

                For valid ranges refer to the topics in
                `Devices <devices>`__.

                Auto-ranging is not supported during waveform acquisitions.
            rate (float): Specifies the **rate** of the acquisition in samples per second. NI-DMM
                sets WAVEFORM_RATE to this value.

                The valid **Range** is 10.0–1,800,000 S/s. **rate** values are coerced
                to the closest integer divisor of 1,800,000. The default value is
                1,800,000.
            waveform_points (int): Specifies the number of points to acquire before the waveform
                acquisition completes. NI-DMM sets WAVEFORM_POINTS to this
                value.

                To calculate the maximum and minimum number of waveform points that you
                can acquire in one acquisition, refer to the `Waveform Acquisition
                Measurement Cycle <waveform_cycle>`__.

                The default value is 500.
        '''
        if type(measurement_function) is not enums.Function:
            raise TypeError('Parameter mode must be of type ' + str(enums.Function))
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        measurement_function_ctype = visatype.ViInt32(measurement_function.value)  # case 10
        range_ctype = visatype.ViReal64(range)  # case 9
        rate_ctype = visatype.ViReal64(rate)  # case 9
        waveform_points_ctype = visatype.ViInt32(waveform_points)  # case 9
        error_code = self._library.niDMM_ConfigureWaveformAcquisition(vi_ctype, measurement_function_ctype, range_ctype, rate_ctype, waveform_points_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disable(self):
        '''disable

        Places the instrument in a quiescent state where it has minimal or no
        impact on the system to which it is connected. If a measurement is in
        progress when this function is called, the measurement is aborted.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        error_code = self._library.niDMM_Disable(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def fetch(self, maximum_time=-1):
        '''fetch

        Returns the value from a previously initiated measurement. You must call
        _initiate before calling this function.

        Args:
            maximum_time (int): Specifies the **maximum_time** allowed for this function to complete in
                milliseconds. If the function does not complete within this time
                interval, the function returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                NIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout
                automatically.

        Returns:
            reading (float): The measured value returned from the DMM.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        maximum_time_ctype = visatype.ViInt32(maximum_time)  # case 9
        reading_ctype = visatype.ViReal64()  # case 14
        error_code = self._library.niDMM_Fetch(vi_ctype, maximum_time_ctype, ctypes.pointer(reading_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(reading_ctype.value)

    def fetch_multi_point(self, array_size, maximum_time=-1):
        '''fetch_multi_point

        Returns an array of values from a previously initiated multipoint
        measurement. The number of measurements the DMM makes is determined by
        the values you specify for the **Trigger_Count** and **Sample_Count**
        parameters of configure_multi_point. You must first call
        _initiate to initiate a measurement before calling this function.

        Args:
            maximum_time (int): Specifies the **maximum_time** allowed for this function to complete in
                milliseconds. If the function does not complete within this time
                interval, the function returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                NIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout
                automatically.
            array_size (int): Specifies the number of measurements to acquire. The maximum number of
                measurements for a finite acquisition is the (**Trigger Count** x
                **Sample Count**) parameters in configure_multi_point.

                For continuous acquisitions, up to 100,000 points can be returned at
                once. The number of measurements can be a subset. The valid range is any
                positive ViInt32. The default value is 1.

        Returns:
            reading_array (list of float): An array of measurement values.

                Note:
                The size of the **Reading_Array** must be at least the size that you
                specify for the **Array_Size** parameter.
            actual_number_of_points (int): Indicates the number of measured values actually retrieved from the DMM.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        maximum_time_ctype = visatype.ViInt32(maximum_time)  # case 9
        array_size_ctype = visatype.ViInt32(array_size)  # case 8
        reading_array_ctype = (visatype.ViReal64 * array_size)()  # case 13
        actual_number_of_points_ctype = visatype.ViInt32()  # case 14
        error_code = self._library.niDMM_FetchMultiPoint(vi_ctype, maximum_time_ctype, array_size_ctype, reading_array_ctype, ctypes.pointer(actual_number_of_points_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(reading_array_ctype[i]) for i in range(array_size_ctype.value)], int(actual_number_of_points_ctype.value)

    def fetch_waveform(self, array_size, maximum_time=-1):
        '''fetch_waveform

        For the NI 4080/4081/4082 and the NI 4070/4071/4072, returns an array of
        values from a previously initiated waveform acquisition. You must call
        _initiate before calling this function.

        Args:
            maximum_time (int): Specifies the **maximum_time** allowed for this function to complete in
                milliseconds. If the function does not complete within this time
                interval, the function returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                NIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout
                automatically.
            array_size (int): Specifies the number of waveform points to return. You specify the total
                number of points that the DMM acquires in the **Waveform Points**
                parameter of configure_waveform_acquisition. The default value is
                1.

        Returns:
            waveform_array (list of float): **Waveform Array** is an array of measurement values stored in waveform
                data type.
            actual_number_of_points (int): Indicates the number of measured values actually retrieved from the DMM.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        maximum_time_ctype = visatype.ViInt32(maximum_time)  # case 9
        array_size_ctype = visatype.ViInt32(array_size)  # case 8
        waveform_array_ctype = (visatype.ViReal64 * array_size)()  # case 13
        actual_number_of_points_ctype = visatype.ViInt32()  # case 14
        error_code = self._library.niDMM_FetchWaveform(vi_ctype, maximum_time_ctype, array_size_ctype, waveform_array_ctype, ctypes.pointer(actual_number_of_points_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(waveform_array_ctype[i]) for i in range(array_size_ctype.value)], int(actual_number_of_points_ctype.value)

    def get_aperture_time_info(self):
        '''get_aperture_time_info

        Returns the DMM **Aperture_Time** and **Aperture_Time_Units**.

        Returns:
            aperture_time (float): Specifies the amount of time the DMM digitizes the input signal for a
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
            aperture_time_units (enums.ApertureTimeUnits): Indicates the units of aperture time as powerline cycles (PLCs) or
                seconds. Returns the value of the APERTURE_TIME_UNITS
                attribute.

                +-----------------------------+---+------------------+
                | NIDMM_VAL_SECONDS           | 0 | Seconds          |
                +-----------------------------+---+------------------+
                | NIDMM_VAL_POWER_LINE_CYCLES | 1 | Powerline Cycles |
                +-----------------------------+---+------------------+
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        aperture_time_ctype = visatype.ViReal64()  # case 14
        aperture_time_units_ctype = visatype.ViInt32()  # case 14
        error_code = self._library.niDMM_GetApertureTimeInfo(vi_ctype, ctypes.pointer(aperture_time_ctype), ctypes.pointer(aperture_time_units_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(aperture_time_ctype.value), enums.ApertureTimeUnits(aperture_time_units_ctype.value)

    def get_auto_range_value(self):
        '''get_auto_range_value

        Returns the **Actual_Range** that the DMM is using, even when Auto
        Range is off.

        Returns:
            actual_range (float): Indicates the **actual_range** the DMM is using. Returns the value of
                the AUTO_RANGE_VALUE attribute. The units of the returned
                value depend on the function.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        actual_range_ctype = visatype.ViReal64()  # case 14
        error_code = self._library.niDMM_GetAutoRangeValue(vi_ctype, ctypes.pointer(actual_range_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(actual_range_ctype.value)

    def get_cal_date_and_time(self, cal_type):
        '''get_cal_date_and_time

        Returns the date and time of the last calibration performed.

        Note: The NI 4050 and NI 4060 are not supported.

        Args:
            cal_type (int): Specifies the type of calibration performed (external or
                self-calibration).

                +-----------------------------------+---+----------------------+
                | NIDMM_VAL_INTERNAL_AREA (default) | 0 | Self-Calibration     |
                +-----------------------------------+---+----------------------+
                | NIDMM_VAL_EXTERNAL_AREA           | 1 | External Calibration |
                +-----------------------------------+---+----------------------+

                Note: The NI 4065 does not support self-calibration.

        Returns:
            month (int): Indicates the **month** of the last calibration.
            day (int): Indicates the **day** of the last calibration.
            year (int): Indicates the **year** of the last calibration.
            hour (int): Indicates the **hour** of the last calibration.
            minute (int): Indicates the **minute** of the last calibration.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        cal_type_ctype = visatype.ViInt32(cal_type)  # case 9
        month_ctype = visatype.ViInt32()  # case 14
        day_ctype = visatype.ViInt32()  # case 14
        year_ctype = visatype.ViInt32()  # case 14
        hour_ctype = visatype.ViInt32()  # case 14
        minute_ctype = visatype.ViInt32()  # case 14
        error_code = self._library.niDMM_GetCalDateAndTime(vi_ctype, cal_type_ctype, ctypes.pointer(month_ctype), ctypes.pointer(day_ctype), ctypes.pointer(year_ctype), ctypes.pointer(hour_ctype), ctypes.pointer(minute_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(month_ctype.value), int(day_ctype.value), int(year_ctype.value), int(hour_ctype.value), int(minute_ctype.value)

    def get_dev_temp(self, options=''):
        '''get_dev_temp

        Returns the current **Temperature** of the device.

        Note: The NI 4050 and NI 4060 are not supported.

        Args:
            options (string): Reserved.

        Returns:
            temperature (float): Returns the current **temperature** of the device.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        options_ctype = ctypes.create_string_buffer(options.encode(self._encoding))  # case 3
        temperature_ctype = visatype.ViReal64()  # case 14
        error_code = self._library.niDMM_GetDevTemp(vi_ctype, options_ctype, ctypes.pointer(temperature_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(temperature_ctype.value)

    def get_last_cal_temp(self, cal_type):
        '''get_last_cal_temp

        Returns the **Temperature** during the last calibration procedure.

        Note: The NI 4050 and NI 4060 are not supported.

        Args:
            cal_type (int): Specifies the type of calibration performed (external or
                self-calibration).

                +-----------------------------------+---+----------------------+
                | NIDMM_VAL_INTERNAL_AREA (default) | 0 | Self-Calibration     |
                +-----------------------------------+---+----------------------+
                | NIDMM_VAL_EXTERNAL_AREA           | 1 | External Calibration |
                +-----------------------------------+---+----------------------+

                Note: The NI 4065 does not support self-calibration.

        Returns:
            temperature (float): Returns the **temperature** during the last calibration.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        cal_type_ctype = visatype.ViInt32(cal_type)  # case 9
        temperature_ctype = visatype.ViReal64()  # case 14
        error_code = self._library.niDMM_GetLastCalTemp(vi_ctype, cal_type_ctype, ctypes.pointer(temperature_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(temperature_ctype.value)

    def get_measurement_period(self):
        '''get_measurement_period

        Returns the measurement **Period**, which is the amount of time it takes
        to complete one measurement with the current configuration. Use this
        function right before you begin acquiring data—after you have completely
        configured the measurement and after all configuration functions have
        been called.

        Returns:
            period (float): Returns the number of seconds it takes to make one measurement.

                The first measurement in a multipoint acquisition requires additional
                settling time. This function does not include this additional time or
                any TRIGGER_DELAY associated with the first measurement.
                Time required for internal measurements, such as
                AUTO_ZERO, is included.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        period_ctype = visatype.ViReal64()  # case 14
        error_code = self._library.niDMM_GetMeasurementPeriod(vi_ctype, ctypes.pointer(period_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(period_ctype.value)

    def get_self_cal_supported(self):
        '''get_self_cal_supported

        Returns a Boolean value that expresses whether or not the DMM that you
        are using can perform self-calibration.

        Returns:
            self_cal_supported (bool): Returns whether Self Cal is supported for the device specified by the
                given session.

                +----------+---+-------------------------------------------------------------+
                | VI_TRUE  | 1 | The DMM that you are using can perform self-calibration.    |
                +----------+---+-------------------------------------------------------------+
                | VI_FALSE | 0 | The DMM that you are using cannot perform self-calibration. |
                +----------+---+-------------------------------------------------------------+
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        self_cal_supported_ctype = visatype.ViBoolean()  # case 14
        error_code = self._library.niDMM_GetSelfCalSupported(vi_ctype, ctypes.pointer(self_cal_supported_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(self_cal_supported_ctype.value)

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
            resource_name (string): Caution:
                All IVI names for the **Resource_Name**, such as logical names or
                virtual names, are case-sensitive. If you use logical names, driver
                session names, or virtual names in your program, you must make sure that
                the name you use matches the name in the IVI Configuration Store file
                exactly, without any variations in the case of the characters in the
                name.

                | Contains the **resource_name** of the device to initialize. The
                  **resource_name** is assigned in Measurement & Automation Explorer
                  (MAX). Refer to `Related
                  Documentation <related_documentation>`__
                  for the *NI Digital Multimeters Getting Started Guide* for more
                  information about configuring and testing the DMM in MAX.
                | Valid Syntax:

                -  NI-DAQmx name
                -  DAQ::NI-DAQmx name[::INSTR]
                -  DAQ::Traditional NI-DAQ device number[::INSTR]
                -  IVI logical name
            id_query (bool): Verifies that the device you initialize is one that the driver supports.
                NI-DMM automatically performs this query, so setting this parameter is
                not necessary.
                Defined Values:

                +-------------------+---+------------------+
                | VI_TRUE (default) | 1 | Perform ID Query |
                +-------------------+---+------------------+
                | VI_FALSE          | 0 | Skip ID Query    |
                +-------------------+---+------------------+
            reset_device (bool): Specifies whether to reset the instrument during the initialization
                procedure.
                Defined Values:

                +-------------------+---+--------------+
                | VI_TRUE (default) | 1 | Reset Device |
                +-------------------+---+--------------+
                | VI_FALSE          | 0 | Don't Reset  |
                +-------------------+---+--------------+
            option_string (string): | Sets the initial value of certain attributes for the session. The
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
                Multimeters <simulation>`__ for more
                information.

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
            vi (int): Returns a ViSession handle that you use to identify the instrument in
                all subsequent instrument driver function calls.
        '''
        resource_name_ctype = ctypes.create_string_buffer(resource_name.encode(self._encoding))  # case 3
        id_query_ctype = visatype.ViBoolean(id_query)  # case 9
        reset_device_ctype = visatype.ViBoolean(reset_device)  # case 9
        option_string_ctype = ctypes.create_string_buffer(option_string.encode(self._encoding))  # case 3
        vi_ctype = visatype.ViSession()  # case 14
        error_code = self._library.niDMM_InitWithOptions(resource_name_ctype, id_query_ctype, reset_device_ctype, option_string_ctype, ctypes.pointer(vi_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(vi_ctype.value)

    def _initiate(self):
        '''_initiate

        Initiates an acquisition. After you call this function, the DMM leaves
        the Idle state and enters the Wait-for-Trigger state. If trigger is set
        to Immediate mode, the DMM begins acquiring measurement data. Use
        fetch, fetch_multi_point, or fetch_waveform to
        retrieve the measurement data.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        error_code = self._library.niDMM_Initiate(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

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
            conductance (float): **conductance** is the measured value of open cable compensation
                **conductance**.
            susceptance (float): **susceptance** is the measured value of open cable compensation
                **susceptance**.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        conductance_ctype = visatype.ViReal64()  # case 14
        susceptance_ctype = visatype.ViReal64()  # case 14
        error_code = self._library.niDMM_PerformOpenCableComp(vi_ctype, ctypes.pointer(conductance_ctype), ctypes.pointer(susceptance_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(conductance_ctype.value), float(susceptance_ctype.value)

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
            resistance (float): **resistance** is the measured value of short cable compensation
                **resistance**.
            reactance (float): **reactance** is the measured value of short cable compensation
                **reactance**.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        resistance_ctype = visatype.ViReal64()  # case 14
        reactance_ctype = visatype.ViReal64()  # case 14
        error_code = self._library.niDMM_PerformShortCableComp(vi_ctype, ctypes.pointer(resistance_ctype), ctypes.pointer(reactance_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(resistance_ctype.value), float(reactance_ctype.value)

    def read(self, maximum_time=-1):
        '''read

        Acquires a single measurement and returns the measured value.

        Args:
            maximum_time (int): Specifies the **maximum_time** allowed for this function to complete in
                milliseconds. If the function does not complete within this time
                interval, the function returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                NIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout
                automatically.

        Returns:
            reading (float): The measured value returned from the DMM.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        maximum_time_ctype = visatype.ViInt32(maximum_time)  # case 9
        reading_ctype = visatype.ViReal64()  # case 14
        error_code = self._library.niDMM_Read(vi_ctype, maximum_time_ctype, ctypes.pointer(reading_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(reading_ctype.value)

    def read_multi_point(self, array_size, maximum_time=-1):
        '''read_multi_point

        Acquires multiple measurements and returns an array of measured values.
        The number of measurements the DMM makes is determined by the values you
        specify for the **Trigger_Count** and **Sample_Count** parameters in
        configure_multi_point.

        Args:
            maximum_time (int): Specifies the **maximum_time** allowed for this function to complete in
                milliseconds. If the function does not complete within this time
                interval, the function returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                NIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout
                automatically.
            array_size (int): Specifies the number of measurements to acquire. The maximum number of
                measurements for a finite acquisition is the (**Trigger Count** x
                **Sample Count**) parameters in configure_multi_point.

                For continuous acquisitions, up to 100,000 points can be returned at
                once. The number of measurements can be a subset. The valid range is any
                positive ViInt32. The default value is 1.

        Returns:
            reading_array (list of float): An array of measurement values.

                Note:
                The size of the **Reading_Array** must be at least the size that you
                specify for the **Array_Size** parameter.
            actual_number_of_points (int): Indicates the number of measured values actually retrieved from the DMM.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        maximum_time_ctype = visatype.ViInt32(maximum_time)  # case 9
        array_size_ctype = visatype.ViInt32(array_size)  # case 8
        reading_array_ctype = (visatype.ViReal64 * array_size)()  # case 13
        actual_number_of_points_ctype = visatype.ViInt32()  # case 14
        error_code = self._library.niDMM_ReadMultiPoint(vi_ctype, maximum_time_ctype, array_size_ctype, reading_array_ctype, ctypes.pointer(actual_number_of_points_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(reading_array_ctype[i]) for i in range(array_size_ctype.value)], int(actual_number_of_points_ctype.value)

    def read_status(self):
        '''read_status

        Returns measurement backlog and acquisition status. Use this function to
        determine how many measurements are available before calling
        fetch, fetch_multi_point, or fetch_waveform.

        Note: The NI 4050 is not supported.

        Returns:
            acquisition_backlog (int): The number of measurements available to be read. If the backlog
                continues to increase, data is eventually overwritten, resulting in an
                error.

                Note:
                On the NI 4060, the **Backlog** does not increase when autoranging. On
                the NI 4065, the **Backlog** does not increase when Range is set to AUTO
                RANGE ON (-1), or before the first point is fetched when Range is set to
                AUTO RANGE ONCE (-3). These behaviors are due to the autorange model of
                the devices.
            acquisition_status (enums.AcquisitionStatus): Indicates status of the acquisition. The following table shows the
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
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        acquisition_backlog_ctype = visatype.ViInt32()  # case 14
        acquisition_status_ctype = visatype.ViInt16()  # case 14
        error_code = self._library.niDMM_ReadStatus(vi_ctype, ctypes.pointer(acquisition_backlog_ctype), ctypes.pointer(acquisition_status_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(acquisition_backlog_ctype.value), enums.AcquisitionStatus(acquisition_status_ctype.value)

    def read_waveform(self, array_size, maximum_time=-1):
        '''read_waveform

        For the NI 4080/4081/4082 and the NI 4070/4071/4072, acquires a waveform
        and returns data as an array of values or as a waveform data type. The
        number of elements in the **Waveform_Array** is determined by the
        values you specify for the **Waveform_Points** parameter in
        configure_waveform_acquisition.

        Args:
            maximum_time (int): Specifies the **maximum_time** allowed for this function to complete in
                milliseconds. If the function does not complete within this time
                interval, the function returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                NIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout
                automatically.
            array_size (int): Specifies the number of waveform points to return. You specify the total
                number of points that the DMM acquires in the **Waveform Points**
                parameter of configure_waveform_acquisition. The default value is
                1.

        Returns:
            waveform_array (list of float): An array of measurement values.

                Note:
                The size of the **Waveform_Array** must be at least the size that you
                specify for the **Array_Size** parameter.
            actual_number_of_points (int): Indicates the number of measured values actually retrieved from the DMM.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        maximum_time_ctype = visatype.ViInt32(maximum_time)  # case 9
        array_size_ctype = visatype.ViInt32(array_size)  # case 8
        waveform_array_ctype = (visatype.ViReal64 * array_size)()  # case 13
        actual_number_of_points_ctype = visatype.ViInt32()  # case 14
        error_code = self._library.niDMM_ReadWaveform(vi_ctype, maximum_time_ctype, array_size_ctype, waveform_array_ctype, ctypes.pointer(actual_number_of_points_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(waveform_array_ctype[i]) for i in range(array_size_ctype.value)], int(actual_number_of_points_ctype.value)

    def reset_with_defaults(self):
        '''reset_with_defaults

        Resets the instrument to a known state and sends initialization commands
        to the DMM. The initialization commands set the DMM settings to the
        state necessary for the operation of NI-DMM. All user-defined default
        values associated with a logical name are applied after setting the DMM.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        error_code = self._library.niDMM_ResetWithDefaults(vi_ctype)
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
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        error_code = self._library.niDMM_SelfCal(vi_ctype)
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
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        error_code = self._library.niDMM_SendSoftwareTrigger(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _close(self):
        '''_close

        Closes the specified session and deallocates resources that it reserved.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        error_code = self._library.niDMM_close(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def reset(self):
        '''reset

        Resets the instrument to a known state and sends initialization commands
        to the instrument. The initialization commands set instrument settings
        to the state necessary for the operation of the instrument driver.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        error_code = self._library.niDMM_reset(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def self_test(self):
        '''self_test

        Performs a self-test on the DMM to ensure that the DMM is functioning
        properly. Self-test does not calibrate the DMM.

        Note:
        This function calls reset, and any configurations previous to
        the call will be lost. All attributes will be set to their default
        values after the call returns.

        Returns:
            self_test_result (int): Contains the value returned from the instrument self-test. Zero
                indicates success.

                On the NI 4080/4082 and NI 4070/4072, the error code 1013 indicates that
                you should check the fuse and replace it, if necessary.

                Note:
                Self-test does not check the fuse on the NI 4065, NI 4071, and
                NI 4081. Hence, even if the fuse is blown on the device, self-test does
                not return error code 1013.
            self_test_message (string): This parameter contains the string returned from the instrument
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
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        self_test_result_ctype = visatype.ViInt16()  # case 14
        self_test_message_ctype = (visatype.ViChar * 256)()  # case 11
        error_code = self._library.niDMM_self_test(vi_ctype, ctypes.pointer(self_test_result_ctype), self_test_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(self_test_result_ctype.value), self_test_message_ctype.value.decode(self._encoding)



