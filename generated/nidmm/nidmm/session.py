# -*- coding: utf-8 -*-
# This file was generated
import array  # noqa: F401
# Used by @ivi_synchronized
from functools import wraps

import nidmm._attributes as _attributes
import nidmm._converters as _converters
import nidmm._library_interpreter as _library_interpreter
import nidmm.enums as enums
import nidmm.errors as errors

import hightime

# Used for __repr__
import pprint
pp = pprint.PrettyPrinter(indent=4)


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


class _SessionBase(object):
    '''Base class for all NI-DMM sessions.'''

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

    ac_max_freq = _attributes.AttributeViReal64(1250007)
    '''Type: float

    Specifies the maximum frequency component of the input signal for AC  measurements. This property is used only for error checking and verifies  that the value of this parameter is less than the maximum frequency  of the device. This property affects the DMM only when you set the   method property to AC measurements.
    The valid range is 1 Hz-300 kHz for the NI 4070/4071/4072, 10 Hz-100 kHz  for the NI 4065, and 20 Hz-25 kHz for the NI 4050 and NI 4060.
    '''
    ac_min_freq = _attributes.AttributeViReal64(1250006)
    '''Type: float

    Specifies the minimum frequency component of the input signal for AC  measurements. This property affects the DMM only when you set the  method property to AC measurements.
    The valid range is 1 Hz-300 kHz for the NI 4070/4071/4072, 10 Hz-100 kHz  for the NI 4065, and 20 Hz-25 kHz for the NI 4050 and NI 4060.
    '''
    adc_calibration = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.ADCCalibration, 1150022)
    '''Type: enums.ADCCalibration

    For the NI 4070/4071/4072 only, specifies the ADC calibration mode.
    '''
    aperture_time = _attributes.AttributeViReal64(1250321)
    '''Type: float

    Specifies the measurement aperture time for the current configuration.  Aperture time is specified in units set by aperture_time_units. To  override the default aperture, set this property to the desired  aperture time after calling ConfigureMeasurement. To return to the  default, set this property to NIDMM_VAL_APERTURE_TIME_AUTO (-1).
    On the NI 4070/4071/4072, the minimum aperture time is 8.89 usec,  and the maximum aperture time is 149 sec. Any number of powerline cycles (PLCs)  within the minimum and maximum ranges is allowed on the NI 4070/4071/4072.
    On the NI 4065 the minimum aperture time is 333 µs, and the maximum aperture time  is 78.2 s. If setting the number of averages directly, the total measurement time is  aperture time X the number of averages, which must be less than 72.8 s. The aperture  times allowed are 333 µs, 667 µs, or multiples of 1.11 ms-for example 1.11 ms, 2.22 ms,  3.33 ms, and so on. If you set an aperture time other than 333 µs, 667 µs, or multiples  of 1.11 ms, the value will be coerced up to the next supported aperture time.
    On the NI 4060, when the powerline frequency is 60 Hz, the PLCs allowed are  1 PLC, 6 PLC, 12 PLC, and 120 PLC. When the powerline frequency is 50 Hz, the  PLCs allowed are 1 PLC, 5 PLC, 10 PLC, and 100 PLC.

    Note:
    One or more of the referenced methods are not in the Python API for this driver.

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    aperture_time_units = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.ApertureTimeUnits, 1250322)
    '''Type: enums.ApertureTimeUnits

    Specifies the units of aperture time for the current configuration.
    The NI 4060 does not support an aperture time set in seconds.
    '''
    auto_range_value = _attributes.AttributeViReal64(1250331)
    '''Type: float

    Specifies the value of the range. If auto ranging, shows the actual value of  the active range. The value of this property is set during a read operation.
    '''
    auto_zero = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.AutoZero, 1250332)
    '''Type: enums.AutoZero

    Specifies the AutoZero mode.
    The NI 4050 is not supported.
    '''
    buffer_size = _attributes.AttributeViInt32(1150037)
    '''Type: int

    Size in samples of the internal data buffer. Maximum is 134,217,727 (OX7FFFFFF) samples. When  set to NIDMM_VAL_BUFFER_SIZE_AUTO (-1), NI-DMM chooses the buffer size.

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    cable_comp_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.CableCompensationType, 1150045)
    '''Type: enums.CableCompensationType

    For the NI 4072 only,  the type of cable compensation that is applied to the current capacitance  or inductance measurement for the current range.
    Changing the method or the range through this property or through configure_measurement_digits  resets the value of this property to the default value.
    '''
    channel_count = _attributes.AttributeViInt32(1050203)
    '''Type: int

    Indicates the number of channels that the specific instrument driver  supports. For each property for which the IVI_VAL_MULTI_CHANNEL flag  property is set, the IVI engine maintains a separate cache value for each  channel.
    '''
    current_source = _attributes.AttributeViReal64(1150025)
    '''Type: float

    Specifies the current source provided during diode measurements.
    The NI 4050 and NI 4060 are not supported.
    '''
    dc_bias = _attributes.AttributeViInt32(1150053)
    '''Type: int

    For the NI 4072 only, controls the available DC bias for capacitance measurements.
    '''
    dc_noise_rejection = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.DCNoiseRejection, 1150026)
    '''Type: enums.DCNoiseRejection

    Specifies the DC noise rejection mode.
    The NI 4050 and NI 4060 are not supported.
    '''
    driver_setup = _attributes.AttributeViString(1050007)
    '''Type: str

    This property indicates the Driver Setup string that the user specified when  initializing the driver.
    Some cases exist where the end-user must specify instrument driver options  at initialization time.  An example of this is specifying a particular  instrument model from among a family of instruments that the driver supports.   This is useful when using simulation.  The end-user can specify  driver-specific options through the DriverSetup keyword in the optionsString  parameter to the niDMM Init With Options.vi.
    If the user does not specify a Driver Setup string, this property returns  an empty string.
    '''
    freq_voltage_auto_range = _attributes.AttributeViReal64(1150044)
    '''Type: float

    For the NI 4070/4071/4072 only, specifies the value of the frequency voltage range.  If Auto Ranging, shows the actual value of the active frequency voltage range.  If not Auto Ranging, the value of this property is the same as that of  freq_voltage_range.
    '''
    freq_voltage_range = _attributes.AttributeViReal64(1250101)
    '''Type: float

    Specifies the maximum amplitude of the input signal for frequency  measurements.
    '''
    function = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.Function, 1250001)
    '''Type: enums.Function

    Specifies the measurement method.
    Refer to the method topic in  the NI Digital Multimeters Help for device-specific information.
    If you are setting this property directly, you must also set the operation_mode property,  which controls whether the DMM takes standard single or multipoint measurements, or acquires a waveform.  If you are programming properties directly, you must set the operation_mode property before  setting other configuration properties. If the operation_mode property is set to OperationMode.WAVEFORM,  the only valid method types are Method.WAVEFORM_VOLTAGE and Method.WAVEFORM_CURRENT. Set the  operation_mode property to OperationMode.IVIDMM to set all other method values.
    '''
    input_resistance = _attributes.AttributeViReal64(1150029)
    '''Type: float

    Specifies the input resistance of the instrument.
    The NI 4050 and NI 4060 are not supported.
    '''
    instrument_firmware_revision = _attributes.AttributeViString(1050510)
    '''Type: str

    A string containing the instrument firmware revision number.
    '''
    instrument_manufacturer = _attributes.AttributeViString(1050511)
    '''Type: str

    A string containing the manufacturer of the instrument.
    '''
    instrument_model = _attributes.AttributeViString(1050512)
    '''Type: str

    A string containing the instrument model.
    '''
    instrument_product_id = _attributes.AttributeViInt32(1150061)
    '''Type: int

    The PCI product ID.
    '''
    io_resource_descriptor = _attributes.AttributeViString(1050304)
    '''Type: str

    A string containing the resource descriptor of the instrument.
    '''
    lc_calculation_model = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.LCCalculationModel, 1150052)
    '''Type: enums.LCCalculationModel

    For the NI 4072 only, specifies the type of algorithm that the measurement processing uses for  capacitance and inductance measurements.
    '''
    lc_number_meas_to_average = _attributes.AttributeViInt32(1150055)
    '''Type: int

    For the NI 4072 only, specifies the number of LC measurements that are averaged to produce one reading.
    '''
    logical_name = _attributes.AttributeViString(1050305)
    '''Type: str

    A string containing the logical name of the instrument.
    '''
    meas_complete_dest = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.MeasurementCompleteDest, 1250305)
    '''Type: enums.MeasurementCompleteDest

    Specifies the destination of the measurement complete (MC) signal.
    The NI 4050 is not supported.
    To determine which values are supported by each device, refer to the LabWindows/CVI Trigger Routing section in  the NI Digital Multimeters Help.
    '''
    number_of_averages = _attributes.AttributeViInt32(1150032)
    '''Type: int

    Specifies the number of averages to perform in a measurement. For the NI 4070/4071/4072,  applies only when the aperture time is not set to AUTO and Auto Zero is ON.  The default is 1.
    The NI 4050 and NI 4060 are not supported.
    '''
    offset_comp_ohms = _attributes.AttributeViInt32(1150023)
    '''Type: int

    For the NI 4070/4071/4072 only, enables or disables offset compensated ohms.
    '''
    open_cable_comp_conductance = _attributes.AttributeViReal64(1150049)
    '''Type: float

    For the NI 4072 only, specifies the active part (conductance) of the open cable compensation.  The valid range is any real number greater than 0. The default value (-1.0)  indicates that compensation has not taken place.
    Changing the method or the range through this property or through configure_measurement_digits  resets the value of this property to the default value.
    '''
    open_cable_comp_susceptance = _attributes.AttributeViReal64(1150048)
    '''Type: float

    For the NI 4072 only, specifies the reactive part (susceptance) of the open cable compensation.  The valid range is any real number greater than 0. The default value (-1.0)  indicates that compensation has not taken place.
    Changing the method or the range through this property or through configure_measurement_digits  resets the value of this property to the default value.
    '''
    operation_mode = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.OperationMode, 1150014)
    '''Type: enums.OperationMode

    Specifies how the NI 4065 and NI 4070/4071/4072 acquire data. When you call  configure_measurement_digits, NI-DMM sets this property to OperationMode.IVIDMM.  When you call configure_waveform_acquisition, NI-DMM sets this property to OperationMode.WAVEFORM.  If you are programming properties directly, you must set this property before  setting other configuration properties.
    '''
    powerline_freq = _attributes.AttributeViReal64(1250333)
    '''Type: float

    Specifies the powerline frequency. The NI 4050 and NI 4060 use this value to select an aperture time to reject  powerline noise by selecting the appropriate internal sample clock and filter. The NI 4065 and  NI 4070/4071/4072 use this value to select a timebase for setting the aperture_time  property in powerline cycles (PLCs).
    After configuring powerline frequency, set the aperture_time_units property to PLCs.  When setting the aperture_time property, select the number of PLCs for the powerline frequency.  For example, if powerline frequency = 50 Hz (or 20ms) and aperture time in PLCs = 5, then aperture time in  Seconds = 20ms * 5 PLCs = 100 ms. Similarly, if powerline frequency = 60 Hz (or 16.667 ms) and aperture time  in PLCs = 6, then aperture time in Seconds = 16.667 ms * 6 PLCs = 100 ms.
    '''
    range = _attributes.AttributeViReal64(1250002)
    '''Type: float

    Specifies the measurement range. Use positive values to represent the  absolute value of the maximum expected measurement. The value is in units  appropriate for the current value of the method property. For  example, if method is set to NIDMM_VAL_VOLTS, the units are  volts.
    The NI 4050 and NI 4060 only support Auto Range when the trigger and  sample trigger is set to IMMEDIATE.
    NIDMM_VAL_AUTO_RANGE_ON -1.0
    NI-DMM performs an Auto Range before acquiring the measurement.
    NIDMM_VAL_AUTO_RANGE_OFF -2.0
    NI-DMM sets the Range to the current auto_range_value and uses this range  for all subsequent measurements until the measurement configuration is changed.
    NIDMM_VAL_AUTO_RANGE_ONCE -3.0
    NI-DMM performs an Auto Range before acquiring the next measurement. The auto_range_value  is stored and used for all subsequent measurements until the measurement configuration is changed.

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    resolution_absolute = _attributes.AttributeViReal64(1250008)
    '''Type: float

    Specifies the measurement resolution in absolute units. Setting this  property to higher values increases the measurement accuracy. Setting this  property to lower values increases the measurement speed.
    NI-DMM ignores this property for capacitance and inductance measurements on the NI 4072.  To achieve better resolution for such measurements, use the lc_number_meas_to_average property.
    '''
    resolution_digits = _attributes.AttributeViReal64(1250003)
    '''Type: float

    Specifies the measurement resolution in digits. Setting this  property to higher values increases the measurement accuracy. Setting this  property to lower values increases the measurement speed.
    NI-DMM ignores this property for capacitance and inductance measurements on the NI 4072.  To achieve better resolution for such measurements, use the lc_number_meas_to_average property.
    '''
    sample_count = _attributes.AttributeViInt32(1250301)
    '''Type: int

    Specifies the number of measurements the DMM takes each time it receives a  trigger in a multiple point acquisition.
    '''
    sample_interval = _attributes.AttributeViReal64TimeDeltaSeconds(1250303)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    Specifies the amount of time in seconds the DMM waits between measurement cycles.  This property only applies when the sample_trigger property is set to INTERVAL.
    On the NI 4060, the value for this property is used as the settling time.  When this property is set to 0, the NI 4060 does not settle between  measurement cycles. The onboard timing resolution is 1 µs on the NI 4060.
    The NI 4065 and NI 4070/4071/4072 use the value specified in this property as additional  delay. On the NI 4065 and NI 4070/4071/4072, the onboard timing resolution is 34.72 ns and  the valid range is 0-149 s.
    Only positive values are valid when setting the sample interval.
    The NI 4050 is not supported.
    '''
    sample_trigger = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.SampleTrigger, 1250302)
    '''Type: enums.SampleTrigger

    Specifies the sample trigger source.
    To determine which values are supported by each device, refer to the LabWindows/CVI Trigger Routing section in  the NI Digital Multimeters Help.
    '''
    serial_number = _attributes.AttributeViString(1150054)
    '''Type: str

    A string containing the serial number of the instrument. This property corresponds  to the serial number label that is attached to most products.
    '''
    settle_time = _attributes.AttributeViReal64TimeDeltaSeconds(1150028)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    Specifies the settling time in seconds. To override the default settling time,  set this property. To return to the default, set this property to  NIDMM_VAL_SETTLE_TIME_AUTO (-1).
    The NI 4050 and NI 4060 are not supported.

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    short_cable_comp_reactance = _attributes.AttributeViReal64(1150046)
    '''Type: float

    For the NI 4072 only, represents the reactive part (reactance) of the short cable compensation.  The valid range is any real number greater than 0. The default value (-1)  indicates that compensation has not taken place.
    Changing the method or the range through this property or through configure_measurement_digits  resets the value of this property to the default value.
    '''
    short_cable_comp_resistance = _attributes.AttributeViReal64(1150047)
    '''Type: float

    For the NI 4072 only, represents the active part (resistance) of the short cable compensation.  The valid range is any real number greater than 0. The default value (-1)  indicates that compensation has not taken place.
    Changing the method or the range through this property or through configure_measurement_digits  resets the value of this property to the default value.
    '''
    simulate = _attributes.AttributeViBoolean(1050005)
    '''Type: bool

    Specifies whether or not to simulate instrument driver I/O operations. If  simulation is enabled, instrument driver methods perform range checking and  call IVI Get and Set methods, but they do not perform  instrument I/O. For output parameters that represent instrument data, the  instrument driver methods return calculated values.
    The default value is False (0). Use the __init__ method to  override this setting.
    Simulate can only be set within the InitWithOptions method.  The property value cannot be changed outside of the method.
    '''
    specific_driver_description = _attributes.AttributeViString(1050514)
    '''Type: str

    A string containing a description of the specific driver.
    '''
    specific_driver_major_version = _attributes.AttributeViInt32(1050503)
    '''Type: int

    Returns the major version number of this instrument driver.
    '''
    specific_driver_minor_version = _attributes.AttributeViInt32(1050504)
    '''Type: int

    The minor version number of this instrument driver.
    '''
    specific_driver_revision = _attributes.AttributeViString(1050551)
    '''Type: str

    A string that contains additional version information about this specific  instrument driver.
    '''
    specific_driver_vendor = _attributes.AttributeViString(1050513)
    '''Type: str

    A string containing the vendor of the specific driver.
    '''
    supported_instrument_models = _attributes.AttributeViString(1050327)
    '''Type: str

    A string containing the instrument models supported by the specific driver.
    '''
    temp_rtd_a = _attributes.AttributeViReal64(1150121)
    '''Type: float

    Specifies the Callendar-Van Dusen A coefficient for RTD scaling when the RTD Type property   is set to Custom. The default value is 3.9083e-3 (Pt3851).
    '''
    temp_rtd_b = _attributes.AttributeViReal64(1150122)
    '''Type: float

    Specifies the Callendar-Van Dusen B coefficient for RTD scaling when the RTD Type property  is set to Custom. The default value is -5.775e-7(Pt3851).
    '''
    temp_rtd_c = _attributes.AttributeViReal64(1150123)
    '''Type: float

    Specifies the Callendar-Van Dusen C coefficient for RTD scaling when the RTD Type property  is set to Custom. The default value is -4.183e-12(Pt3851).
    '''
    temp_rtd_res = _attributes.AttributeViReal64(1250242)
    '''Type: float

    Specifies the RTD resistance at 0 degrees Celsius. This applies to all supported RTDs,  including custom RTDs. The default value is 100 (?).
    '''
    temp_rtd_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.RTDType, 1150120)
    '''Type: enums.RTDType

    Specifies the type of RTD used to measure temperature. The default value is RTDType.PT3851.
    Refer to the temp_rtd_type topic in the NI Digital Multimeters Help for additional information about defined values.
    '''
    temp_tc_fixed_ref_junc = _attributes.AttributeViReal64(1250233)
    '''Type: float

    Specifies the reference junction temperature when a fixed reference junction is used to take  a thermocouple measurement. The default value is 25.0 (°C).
    '''
    temp_tc_ref_junc_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.ThermocoupleReferenceJunctionType, 1250232)
    '''Type: enums.ThermocoupleReferenceJunctionType

    Specifies the type of reference junction to be used in the reference junction compensation  of a thermocouple. The only supported value, ThermocoupleReferenceJunctionType.FIXED, is fixed.
    '''
    temp_tc_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.ThermocoupleType, 1250231)
    '''Type: enums.ThermocoupleType

    Specifies the type of thermocouple used to measure the temperature. The default value is ThermocoupleType.J.
    '''
    temp_thermistor_a = _attributes.AttributeViReal64(1150125)
    '''Type: float

    Specifies the Steinhart-Hart A coefficient for thermistor scaling when the Thermistor Type  property is set to Custom. The default value is 0.0010295 (44006).
    '''
    temp_thermistor_b = _attributes.AttributeViReal64(1150126)
    '''Type: float

    Specifies the Steinhart-Hart B coefficient for thermistor scaling when the Thermistor Type  proerty is set to Custom. The default value is 0.0002391 (44006).
    '''
    temp_thermistor_c = _attributes.AttributeViReal64(1150127)
    '''Type: float

    Specifies the Steinhart-Hart C coefficient for thermistor scaling when the Thermistor Type  property is set to Custom. The default value is 1.568e-7 (44006).
    '''
    temp_thermistor_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.ThermistorType, 1150124)
    '''Type: enums.ThermistorType

    Specifies the type of thermistor used to measure the temperature. The default value is  ThermistorType.THERMISTOR_44006.
    Refer to the temp_thermistor_type topic in the NI Digital Multimeters Help for additional information about defined values.
    '''
    temp_transducer_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.TransducerType, 1250201)
    '''Type: enums.TransducerType

    Specifies the type of device used to measure the temperature. The default value is NIDMM_VAL_4_THERMOCOUPLE.

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    trigger_count = _attributes.AttributeViInt32(1250304)
    '''Type: int

    Specifies the number of triggers the DMM receives before returning to the  Idle state.
    This property can be set to any positive ViInt32 value for the NI 4065 and NI 4070/4071/4072.
    The NI 4050 and NI 4060 support this property being set to 1.
    Refer to the Multiple Point Acquisitions section of the NI Digital Multimeters Help for more information.
    '''
    trigger_delay = _attributes.AttributeViReal64TimeDeltaSeconds(1250005)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    Specifies the time (in seconds) that the DMM waits after it has received a trigger before taking a measurement.  The default value is AUTO DELAY (-1), which means that the DMM waits an appropriate settling time before taking  the measurement. (-1) signifies that AUTO DELAY is on, and (-2) signifies that AUTO DELAY is off.
    The NI 4065 and NI 4070/4071/4072 use the value specified in this property as additional settling time.  For the The NI 4065 and NI 4070/4071/4072, the valid range for Trigger Delay is AUTO DELAY (-1) or 0.0-149.0  seconds and the onboard timing resolution is 34.72 ns.
    On the NI 4060, if this property is set to 0, the DMM does not settle before taking the measurement.  On the NI 4060, the valid range for AUTO DELAY (-1) is 0.0-12.0 seconds and the onboard timing resolution  is 100 ms.
    When using the NI 4050, this property must be set to AUTO DELAY (-1).
    Use positive values to set the trigger delay in seconds.
    Valid Range: NIDMM_VAL_AUTO_DELAY (-1.0), 0.0-12.0 seconds (NI 4060 only)
    Default Value: NIDMM_VAL_AUTO_DELAY

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    trigger_source = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.TriggerSource, 1250004)
    '''Type: enums.TriggerSource

    Specifies the trigger source. When _initiate is called, the DMM waits  for the trigger specified with this property. After it receives the trigger,  the DMM waits the length of time specified with the trigger_delay  property. The DMM then takes a measurement.
    This property is not supported on the NI 4050.
    To determine which values are supported by each device, refer to the LabWindows/CVI Trigger Routing section in  the NI Digital Multimeters Help.
    '''
    waveform_coupling = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.WaveformCoupling, 1150027)
    '''Type: enums.WaveformCoupling

    For the NI 4070/4071/4072 only, specifies the coupling during a waveform acquisition.
    '''
    waveform_points = _attributes.AttributeViInt32(1150019)
    '''Type: int

    For the NI 4070/4071/4072 only, specifies the number of points to acquire in a waveform acquisition.
    '''
    waveform_rate = _attributes.AttributeViReal64(1150018)
    '''Type: float

    For the NI 4070/4071/4072 only, specifies the rate of the waveform acquisition in Samples per second (S/s).  The valid Range is 10.0-1,800,000 S/s. Values are coerced to the  closest integer divisor of 1,800,000. The default value is 1,800,000.
    '''

    def __init__(self, repeated_capability_list, all_channels_in_session, interpreter, freeze_it=False):
        self._repeated_capability_list = repeated_capability_list
        self._repeated_capability = ','.join(repeated_capability_list)
        self._all_channels_in_session = all_channels_in_session
        self._interpreter = interpreter

        # Store the parameter list for later printing in __repr__
        param_list = []
        param_list.append("repeated_capability_list=" + pp.pformat(repeated_capability_list))
        param_list.append("interpreter=" + pp.pformat(interpreter))
        self._param_list = ', '.join(param_list)

        # Finally, set _is_frozen to True which is used to prevent clients from accidentally adding
        # members when trying to set a property with a typo.
        self._is_frozen = freeze_it

    def __repr__(self):
        return '{0}.{1}({2})'.format('nidmm', self.__class__.__name__, self._param_list)

    def __setattr__(self, key, value):
        if self._is_frozen and key not in dir(self):
            raise AttributeError("'{0}' object has no attribute '{1}'".format(type(self).__name__, key))
        object.__setattr__(self, key, value)

    ''' These are code-generated '''

    @ivi_synchronized
    def _get_attribute_vi_boolean(self, attribute_id):
        r'''_get_attribute_vi_boolean

        Queries the value of a ViBoolean property. You can use this method to
        get the values of instrument-specific properties and inherent IVI
        properties.

        If the property represents an instrument state, this method performs
        instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled, and the currently cached value is invalid.

        Tip:
        This method can be called on specific channels within your :py:class:`nidmm.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_boolean`

        To call the method on all channels, you can call it directly on the :py:class:`nidmm.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_boolean`

        Args:
            attribute_id (int): Pass the ID of a property.


        Returns:
            attribute_value (bool): Returns the current value of the property. Pass the address of a
                ViBoolean variable.

        '''
        attribute_value = self._interpreter.get_attribute_vi_boolean(self._repeated_capability, attribute_id)
        return attribute_value

    @ivi_synchronized
    def _get_attribute_vi_int32(self, attribute_id):
        r'''_get_attribute_vi_int32

        Queries the value of a ViInt32 property. You can use this method to
        get the values of instrument-specific properties and inherent IVI
        properties.

        If the property represents an instrument state, this method performs
        instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled, and the currently cached value is invalid.

        Tip:
        This method can be called on specific channels within your :py:class:`nidmm.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_int32`

        To call the method on all channels, you can call it directly on the :py:class:`nidmm.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_int32`

        Args:
            attribute_id (int): Pass the ID of a property.


        Returns:
            attribute_value (int): Returns the current value of the property. Pass the address of a
                ViInt32 variable.

        '''
        attribute_value = self._interpreter.get_attribute_vi_int32(self._repeated_capability, attribute_id)
        return attribute_value

    @ivi_synchronized
    def _get_attribute_vi_real64(self, attribute_id):
        r'''_get_attribute_vi_real64

        Queries the value of a ViReal64 property. You can use this method to
        get the values of instrument-specific properties and inherent IVI
        properties.

        If the property represents an instrument state, this method performs
        instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled, and the currently cached value is invalid.

        Tip:
        This method can be called on specific channels within your :py:class:`nidmm.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_real64`

        To call the method on all channels, you can call it directly on the :py:class:`nidmm.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_real64`

        Args:
            attribute_id (int): Pass the ID of a property.


        Returns:
            attribute_value (float): Returns the current value of the property. Pass the address of a
                ViReal64 variable.

        '''
        attribute_value = self._interpreter.get_attribute_vi_real64(self._repeated_capability, attribute_id)
        return attribute_value

    @ivi_synchronized
    def _get_attribute_vi_string(self, attribute_id):
        r'''_get_attribute_vi_string

        Queries the value of a ViString property. You can use this method to
        get the values of instrument-specific properties and inherent IVI
        properties.

        If the property represents an instrument state, this method performs
        instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled, and the currently cached value is invalid.
           You must provide a ViChar array to serve as a buffer for the value.
           You pass the number of bytes in the buffer as the Array Size
           parameter.

        Tip:
        This method can be called on specific channels within your :py:class:`nidmm.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_string`

        To call the method on all channels, you can call it directly on the :py:class:`nidmm.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_string`

        Args:
            attribute_id (int): Pass the ID of a property.


        Returns:
            attribute_value (str): The buffer in which the method returns the current value of the
                property. The buffer must be of type ViChar and have at least as many
                bytes as indicated in the **Buffer_Size** parameter.

                If you specify 0 for the **Buffer_Size** parameter, you can pass
                VI_NULL for this parameter.

        '''
        attribute_value = self._interpreter.get_attribute_vi_string(self._repeated_capability, attribute_id)
        return attribute_value

    def lock(self):
        '''lock

        Obtains a multithread lock on the device session. Before doing so, the
        software waits until all other execution threads release their locks
        on the device session.

        Other threads may have obtained a lock on this session for the
        following reasons:

            -  The application called the lock method.
            -  A call to NI-DMM locked the session.
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
            lock (context manager): When used in a with statement, nidmm.Session.lock acts as
            a context manager and unlock will be called when the with block is exited
        '''
        self._interpreter.lock()  # We do not call this in the context manager so that this function can
        # act standalone as well and let the client call unlock() explicitly. If they do use the context manager,
        # that will handle the unlock for them
        return _Lock(self)

    @ivi_synchronized
    def _set_attribute_vi_boolean(self, attribute_id, attribute_value):
        r'''_set_attribute_vi_boolean

        This method sets the value of a ViBoolean property.

        This is a low-level method that you can use to set the values of
        instrument-specific properties and inherent IVI properties.

        If the property represents an instrument state, this method performs
        instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled, and the currently cached value is invalid
           or is different than the value you specify.

        This instrument driver contains high-level methods that set most of
        the instrument properties. It is best to use the high-level driver
        methods as much as possible. They handle order dependencies and
        multithread locking for you. In addition, they perform status checking
        only after setting all of the properties.

        In contrast, when you set multiple properties using the SetAttribute
        methods, the methods check the instrument status after each call.
        Also, when state caching is enabled, the high-level methods that
        configure multiple properties perform instrument I/O only for the
        properties whose value you change. Thus, you can safely call the
        high-level methods without the penalty of redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`nidmm.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_boolean`

        To call the method on all channels, you can call it directly on the :py:class:`nidmm.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_boolean`

        Args:
            attribute_id (int): Pass the ID of a property.

            attribute_value (bool): Pass the value that you want to set the property to.

        '''
        self._interpreter.set_attribute_vi_boolean(self._repeated_capability, attribute_id, attribute_value)

    @ivi_synchronized
    def _set_attribute_vi_int32(self, attribute_id, attribute_value):
        r'''_set_attribute_vi_int32

        This method sets the value of a ViInt32 property.

        This is a low-level method that you can use to set the values of
        instrument-specific properties and inherent IVI properties.

        If the property represents an instrument state, this method performs
        instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled, and the currently cached value is invalid
           or is different than the value you specify.

        This instrument driver contains high-level methods that set most of
        the instrument properties. It is best to use the high-level driver
        methods as much as possible. They handle order dependencies and
        multithread locking for you. In addition, they perform status checking
        only after setting all of the properties.

        In contrast, when you set multiple properties using the SetAttribute
        methods, the methods check the instrument status after each call.
        Also, when state caching is enabled, the high-level methods that
        configure multiple properties perform instrument I/O only for the
        properties whose value you change. Thus, you can safely call the
        high-level methods without the penalty of redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`nidmm.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_int32`

        To call the method on all channels, you can call it directly on the :py:class:`nidmm.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_int32`

        Args:
            attribute_id (int): Pass the ID of a property.

            attribute_value (int): Pass the value that you want to set the property to.

        '''
        self._interpreter.set_attribute_vi_int32(self._repeated_capability, attribute_id, attribute_value)

    @ivi_synchronized
    def _set_attribute_vi_real64(self, attribute_id, attribute_value):
        r'''_set_attribute_vi_real64

        This method sets the value of a ViReal64 property.

        This is a low-level method that you can use to set the values of
        instrument-specific properties and inherent IVI properties.

        If the property represents an instrument state, this method performs
        instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled, and the currently cached value is invalid
           or is different than the value you specify.

        This instrument driver contains high-level methods that set most of
        the instrument properties. It is best to use the high-level driver
        methods as much as possible. They handle order dependencies and
        multithread locking for you. In addition, they perform status checking
        only after setting all of the properties.

        In contrast, when you set multiple properties using the SetAttribute
        methods, the methods check the instrument status after each call.
        Also, when state caching is enabled, the high-level methods that
        configure multiple properties perform instrument I/O only for the
        properties whose value you change. Thus, you can safely call the
        high-level methods without the penalty of redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`nidmm.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_real64`

        To call the method on all channels, you can call it directly on the :py:class:`nidmm.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_real64`

        Args:
            attribute_id (int): Pass the ID of a property.

            attribute_value (float): Pass the value that you want to set the property to.

        '''
        self._interpreter.set_attribute_vi_real64(self._repeated_capability, attribute_id, attribute_value)

    @ivi_synchronized
    def _set_attribute_vi_string(self, attribute_id, attribute_value):
        r'''_set_attribute_vi_string

        This method sets the value of a ViString property.

        This is a low-level method that you can use to set the values of
        instrument-specific properties and inherent IVI properties.

        If the property represents an instrument state, this method performs
        instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled, and the currently cached value is invalid
           or is different than the value you specify.

        This instrument driver contains high-level methods that set most of
        the instrument properties. It is best to use the high-level driver
        methods as much as possible. They handle order dependencies and
        multithread locking for you. In addition, they perform status checking
        only after setting all of the properties.

        In contrast, when you set multiple properties using the SetAttribute
        methods, the methods check the instrument status after each call.
        Also, when state caching is enabled, the high-level methods that
        configure multiple properties perform instrument I/O only for the
        properties whose value you change. Thus, you can safely call the
        high-level methods without the penalty of redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`nidmm.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_string`

        To call the method on all channels, you can call it directly on the :py:class:`nidmm.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_string`

        Args:
            attribute_id (int): Pass the ID of a property.

            attribute_value (str): Pass the value that you want to set the property to.

        '''
        self._interpreter.set_attribute_vi_string(self._repeated_capability, attribute_id, attribute_value)

    def unlock(self):
        '''unlock

        Releases a lock that you acquired on an device session using
        lock. Refer to lock for additional
        information on session locks.
        '''
        self._interpreter.unlock()

    def _error_message(self, error_code):
        r'''_error_message

        Takes the **Error_Code** returned by the instrument driver methods,
        interprets it, and returns it as a user-readable string.

        Note:
        When using grpc-device, this method will call GetErrorMessage server-side while providing the same interface.

        Args:
            error_code (int): The **error_code** returned from the instrument. The default is 0,
                indicating VI_SUCCESS.


        Returns:
            error_message (str): The error information formatted into a string.

        '''
        error_message = self._interpreter.error_message(error_code)
        return error_message


class Session(_SessionBase):
    '''An NI-DMM session to an NI digital multimeter'''

    def __init__(self, resource_name, id_query=False, reset_device=False, options={}, *, grpc_options=None):
        r'''An NI-DMM session to an NI digital multimeter

        This method completes the following tasks:

        -  Creates a new IVI instrument driver session and, optionally, sets the
           initial state of the following session properties:
           RANGE_CHECK, QUERY_INSTR_STATUS,
           CACHE, simulate,
           RECORD_COERCIONS.
        -  Opens a session to the device you specify for the **Resource_Name**
           parameter. If the **ID_Query** parameter is set to True, this
           method queries the instrument ID and checks that it is valid for
           this instrument driver.
        -  If the **Reset_Device** parameter is set to True, this method
           resets the instrument to a known state. Sends initialization commands
           to set the instrument to the state necessary for the operation of the
           instrument driver.
        -  Returns a ViSession handle that you use to identify the instrument in
           all subsequent instrument driver method calls.

        Note:
        One or more of the referenced properties are not in the Python API for this driver.

        Args:
            resource_name (str): Caution:
                All IVI names for the **Resource_Name**, such as logical names or
                virtual names, are case-sensitive. If you use logical names, driver
                session names, or virtual names in your program, you must make sure that
                the name you use matches the name in the IVI Configuration Store file
                exactly, without any variations in the case of the characters in the
                name.

                | Contains the **resource_name** of the device to initialize. The
                  **resource_name** is assigned in Measurement & Automation Explorer
                  (MAX). Refer to `Related
                  Documentation <REPLACE_DRIVER_SPECIFIC_URL_1(related_documentation)>`__
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

                +----------------+---+------------------+
                | True (default) | 1 | Perform ID Query |
                +----------------+---+------------------+
                | False          | 0 | Skip ID Query    |
                +----------------+---+------------------+

            reset_device (bool): Specifies whether to reset the instrument during the initialization
                procedure.
                Defined Values:

                +----------------+---+--------------+
                | True (default) | 1 | Reset Device |
                +----------------+---+--------------+
                | False          | 0 | Don't Reset  |
                +----------------+---+--------------+

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

            grpc_options (nidmm.grpc_session_options.GrpcSessionOptions): MeasurementLink gRPC session options


        Returns:
            session (nidmm.Session): A session object representing the device.

        '''
        if grpc_options:
            import nidmm._grpc_stub_interpreter as _grpc_stub_interpreter
            interpreter = _grpc_stub_interpreter.GrpcStubInterpreter(grpc_options)
        else:
            interpreter = _library_interpreter.LibraryInterpreter(encoding='windows-1251')

        # Initialize the superclass with default values first, populate them later
        super(Session, self).__init__(
            repeated_capability_list=[],
            interpreter=interpreter,
            freeze_it=False,
            all_channels_in_session=None
        )
        options = _converters.convert_init_with_options_dictionary(options)

        # Call specified init function
        # Note that _interpreter default-initializes the session handle in its constructor, so that
        # if _init_with_options fails, the error handler can reference it.
        # And then here, once _init_with_options succeeds, we call set_session_handle
        # with the actual session handle.
        self._interpreter.set_session_handle(self._init_with_options(resource_name, id_query, reset_device, options))

        # Store the parameter list for later printing in __repr__
        param_list = []
        param_list.append("resource_name=" + pp.pformat(resource_name))
        param_list.append("reset_device=" + pp.pformat(reset_device))
        param_list.append("options=" + pp.pformat(options))
        self._param_list = ', '.join(param_list)

        # Store the list of channels in the Session which is needed by some nimi-python modules.
        # Use try/except because not all the modules support channels.
        # self.get_channel_names() and self.channel_count can only be called after the session
        # handle is set
        try:
            self._all_channels_in_session = self.get_channel_names(range(self.channel_count))
        except AttributeError:
            self._all_channels_in_session = None

        # Finally, set _is_frozen to True which is used to prevent clients from accidentally adding
        # members when trying to set a property with a typo.
        self._is_frozen = True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self._interpreter._close_on_exit:
            self.close()

    def initiate(self):
        '''initiate

        Initiates an acquisition. After you call this method, the DMM leaves
        the Idle state and enters the Wait-for-Trigger state. If trigger is set
        to Immediate mode, the DMM begins acquiring measurement data. Use
        fetch, fetch_multi_point, or fetch_waveform to
        retrieve the measurement data.

        Note:
        This method will return a Python context manager that will initiate on entering and abort on exit.
        '''
        return _Acquisition(self)

    def close(self):
        '''close

        Closes the specified session and deallocates resources that it reserved.

        Note:
        This method is not needed when using the session context manager
        '''
        try:
            self._close()
        except errors.DriverError:
            self._interpreter.set_session_handle()
            raise
        self._interpreter.set_session_handle()

    ''' These are code-generated '''

    @ivi_synchronized
    def abort(self):
        r'''abort

        Aborts a previously initiated measurement and returns the DMM to the
        Idle state.
        '''
        self._interpreter.abort()

    @ivi_synchronized
    def configure_measurement_absolute(self, measurement_function, range, resolution_absolute):
        r'''configure_measurement_absolute

        Configures the common properties of the measurement. These properties
        include method, range, and
        resolution_absolute.

        Args:
            measurement_function (enums.Function): Specifies the **measurement_function** used to acquire the measurement.
                The driver sets method to this value.

            range (float): Specifies the **range** for the method specified in the
                **Measurement_Function** parameter. When frequency is specified in the
                **Measurement_Function** parameter, you must supply the minimum
                frequency expected in the **range** parameter. For example, you must
                type in 100 Hz if you are measuring 101 Hz or higher.
                For all other methods, you must supply a **range** that exceeds the
                value that you are measuring. For example, you must type in 10 V if you
                are measuring 9 V. **range** values are coerced up to the closest input
                **range**. Refer to the `Devices
                Overview <REPLACE_DRIVER_SPECIFIC_URL_1(devices)>`__ for a list of valid
                ranges. The driver sets range to this value. The default is
                0.02 V.

                +---------------------------+------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIDMM_VAL_AUTO_RANGE_ON   | -1.0 | NI-DMM performs an Auto Range before acquiring the measurement.                                                                                                                         |
                +---------------------------+------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIDMM_VAL_AUTO_RANGE_OFF  | -2.0 | NI-DMM sets the Range to the current auto_range_value and uses this range for all subsequent measurements until the measurement configuration is changed.                               |
                +---------------------------+------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIDMM_VAL_AUTO_RANGE_ONCE | -3.0 | NI-DMM performs an Auto Range before acquiring the measurement. The auto_range_value is stored and used for all subsequent measurements until the measurement configuration is changed. |
                +---------------------------+------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

                Note:
                The NI 4050, NI 4060, and NI 4065 only support Auto Range when the
                trigger and sample trigger are set to IMMEDIATE.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            resolution_absolute (float): Specifies the absolute resolution for the measurement. NI-DMM sets
                resolution_absolute to this value. The PXIe-4080/4081/4082
                uses the resolution you specify. The NI 4065 and NI 4070/4071/4072
                ignore this parameter when the **Range** parameter is set to
                NIDMM_VAL_AUTO_RANGE_ON (-1.0) or NIDMM_VAL_AUTO_RANGE_ONCE
                (-3.0). The default is 0.001 V.

                Note:
                NI-DMM ignores this parameter for capacitance and inductance
                measurements on the NI 4072. To achieve better resolution for such
                measurements, use the lc_number_meas_to_average
                property.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        '''
        if type(measurement_function) is not enums.Function:
            raise TypeError('Parameter measurement_function must be of type ' + str(enums.Function))
        self._interpreter.configure_measurement_absolute(measurement_function, range, resolution_absolute)

    @ivi_synchronized
    def configure_measurement_digits(self, measurement_function, range, resolution_digits):
        r'''configure_measurement_digits

        Configures the common properties of the measurement. These properties
        include method, range, and
        resolution_digits.

        Args:
            measurement_function (enums.Function): Specifies the **measurement_function** used to acquire the measurement.
                The driver sets method to this value.

            range (float): Specifies the range for the method specified in the
                **Measurement_Function** parameter. When frequency is specified in the
                **Measurement_Function** parameter, you must supply the minimum
                frequency expected in the **range** parameter. For example, you must
                type in 100 Hz if you are measuring 101 Hz or higher.
                For all other methods, you must supply a range that exceeds the value
                that you are measuring. For example, you must type in 10 V if you are
                measuring 9 V. range values are coerced up to the closest input range.
                Refer to the `Devices
                Overview <REPLACE_DRIVER_SPECIFIC_URL_1(devices)>`__ for a list of valid
                ranges. The driver sets range to this value. The default is
                0.02 V.

                +---------------------------+------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIDMM_VAL_AUTO_RANGE_ON   | -1.0 | NI-DMM performs an Auto Range before acquiring the measurement.                                                                                                                         |
                +---------------------------+------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIDMM_VAL_AUTO_RANGE_OFF  | -2.0 | NI-DMM sets the Range to the current auto_range_value and uses this range for all subsequent measurements until the measurement configuration is changed.                               |
                +---------------------------+------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIDMM_VAL_AUTO_RANGE_ONCE | -3.0 | NI-DMM performs an Auto Range before acquiring the measurement. The auto_range_value is stored and used for all subsequent measurements until the measurement configuration is changed. |
                +---------------------------+------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

                Note:
                The NI 4050, NI 4060, and NI 4065 only support Auto Range when the
                trigger and sample trigger are set to IMMEDIATE.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            resolution_digits (float): Specifies the resolution of the measurement in digits. The driver sets
                the `Devices Overview <REPLACE_DRIVER_SPECIFIC_URL_1(devices)>`__ for a
                list of valid ranges. The driver sets resolution_digits
                property to this value. The PXIe-4080/4081/4082 uses the resolution you
                specify. The NI 4065 and NI 4070/4071/4072 ignore this parameter when
                the **Range** parameter is set to NIDMM_VAL_AUTO_RANGE_ON (-1.0) or
                NIDMM_VAL_AUTO_RANGE_ONCE (-3.0). The default is 5½.

                Note:
                NI-DMM ignores this parameter for capacitance and inductance
                measurements on the NI 4072. To achieve better resolution for such
                measurements, use the lc_number_meas_to_average
                property.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        '''
        if type(measurement_function) is not enums.Function:
            raise TypeError('Parameter measurement_function must be of type ' + str(enums.Function))
        self._interpreter.configure_measurement_digits(measurement_function, range, resolution_digits)

    @ivi_synchronized
    def configure_multi_point(self, trigger_count, sample_count, sample_trigger=enums.SampleTrigger.IMMEDIATE, sample_interval=hightime.timedelta(seconds=-1)):
        r'''configure_multi_point

        Configures the properties for multipoint measurements. These properties
        include trigger_count, sample_count,
        sample_trigger, and sample_interval.

        For continuous acquisitions, set trigger_count or
        sample_count to zero. For more information, refer to
        `Multiple Point
        Acquisitions <REPLACE_DRIVER_SPECIFIC_URL_1(multi_point)>`__,
        `Triggering <REPLACE_DRIVER_SPECIFIC_URL_1(trigger)>`__, and `Using
        Switches <REPLACE_DRIVER_SPECIFIC_URL_1(switch_selection)>`__.

        Args:
            trigger_count (int): Sets the number of triggers you want the DMM to receive before returning
                to the Idle state. The driver sets trigger_count to this
                value. The default value is 1.

            sample_count (int): Sets the number of measurements the DMM makes in each measurement
                sequence initiated by a trigger. The driver sets
                sample_count to this value. The default value is 1.

            sample_trigger (enums.SampleTrigger): Specifies the **sample_trigger** source you want to use. The driver
                sets sample_trigger to this value. The default is
                Immediate.

                Note:
                To determine which values are supported by each device, refer to the
                `LabWindows/CVI Trigger
                Routing <REPLACE_DRIVER_SPECIFIC_URL_1(cvitrigger_routing)>`__ section.

            sample_interval (hightime.timedelta, datetime.timedelta, or float in seconds): Sets the amount of time in seconds the DMM waits between measurement
                cycles. The driver sets sample_interval to this value.
                Specify a sample interval to add settling time between measurement
                cycles or to decrease the measurement rate. **sample_interval** only
                applies when the **Sample_Trigger** is set to INTERVAL.

                On the NI 4060, the **sample_interval** value is used as the settling
                time. When sample interval is set to 0, the DMM does not settle between
                measurement cycles. The NI 4065 and NI 4070/4071/4072 use the value
                specified in **sample_interval** as additional delay. The default value
                (-1) ensures that the DMM settles for a recommended time. This is the
                same as using an Immediate trigger.

                Note: This property is not used on the NI 4080/4081/4082 and the NI 4050.

        '''
        if type(sample_trigger) is not enums.SampleTrigger:
            raise TypeError('Parameter sample_trigger must be of type ' + str(enums.SampleTrigger))
        sample_interval = _converters.convert_timedelta_to_seconds_real64(sample_interval)
        self._interpreter.configure_multi_point(trigger_count, sample_count, sample_trigger, sample_interval)

    @ivi_synchronized
    def configure_rtd_custom(self, rtd_a, rtd_b, rtd_c):
        r'''configure_rtd_custom

        Configures the A, B, and C parameters for a custom RTD.

        Args:
            rtd_a (float): Specifies the Callendar-Van Dusen A coefficient for RTD scaling when RTD
                Type parameter is set to Custom in the configure_rtd_type method.
                The default is 3.9083e-3 (Pt3851)

            rtd_b (float): Specifies the Callendar-Van Dusen B coefficient for RTD scaling when RTD
                Type parameter is set to Custom in the configure_rtd_type method.
                The default is -5.775e-7 (Pt3851).

            rtd_c (float): Specifies the Callendar-Van Dusen C coefficient for RTD scaling when RTD
                Type parameter is set to Custom in the configure_rtd_type method.
                The default is -4.183e-12 (Pt3851).

        '''
        self._interpreter.configure_rtd_custom(rtd_a, rtd_b, rtd_c)

    @ivi_synchronized
    def configure_rtd_type(self, rtd_type, rtd_resistance):
        r'''configure_rtd_type

        Configures the RTD Type and RTD Resistance parameters for an RTD.

        Args:
            rtd_type (enums.RTDType): Specifies the type of RTD used to measure the temperature resistance.
                NI-DMM uses this value to set the RTD Type property. The default is
                RTDType.PT3851.

                +---------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+
                | Enum                            | Standards                                     | Material | TCR (α) | Typical R\ :sub:`0` (Ω) | Notes                                                                         |                               |
                +=================================+===============================================+==========+=========+=========================+===============================================================================+===============================+
                | Callendar-Van Dusen Coefficient |                                               |          |         |                         |                                                                               |                               |
                +---------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+
                | RTDType.PT3851                  | IEC-751 DIN 43760 BS 1904 ASTM-E1137 EN-60751 | Platinum | .003851 | 100 Ω 1000 Ω            | A = 3.9083 × 10\ :sup:`–3` B = –5.775×10:sup:`–7` C = –4.183×10:sup:`–12`     | Most common RTDs              |
                +---------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+
                | RTDType.PT3750                  | Low-cost vendor compliant RTD\*               | Platinum | .003750 | 1000 Ω                  | A = 3.81 × 10\ :sup:`–3` B = –6.02×10:sup:`–7` C = –6.0×10:sup:`–12`          | Low-cost RTD                  |
                +---------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+
                | RTDType.PT3916                  | JISC 1604                                     | Platinum | .003916 | 100 Ω                   | A = 3.9739 × 10\ :sup:`–3` B = –5.870×10:sup:`–7` C = –4.4 ×10\ :sup:`–12`    | Used in primarily in Japan    |
                +---------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+
                | RTDType.PT3920                  | US Industrial Standard D-100 American         | Platinum | .003920 | 100 Ω                   | A = 3.9787 × 10\ :sup:`–3` B = –5.8686×10:sup:`–7` C = –4.167 ×10\ :sup:`–12` | Low-cost RTD                  |
                +---------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+
                | RTDType.PT3911                  | US Industrial Standard American               | Platinum | .003911 | 100 Ω                   | A = 3.9692 × 10\ :sup:`–3` B = –5.8495×10:sup:`–7` C = –4.233 ×10\ :sup:`–12` | Low-cost RTD                  |
                +---------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+
                | RTDType.PT3928                  | ITS-90                                        | Platinum | .003928 | 100 Ω                   | A = 3.9888 × 10\ :sup:`–3` B = –5.915×10:sup:`–7` C = –3.85 ×10\ :sup:`–12`   | The definition of temperature |
                +---------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+
                | \*No standard. Check the TCR.   |                                               |          |         |                         |                                                                               |                               |
                +---------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+

            rtd_resistance (float): Specifies the RTD resistance in ohms at 0 °C. NI-DMM uses this value to
                set the RTD Resistance property. The default is 100 (Ω).

        '''
        if type(rtd_type) is not enums.RTDType:
            raise TypeError('Parameter rtd_type must be of type ' + str(enums.RTDType))
        self._interpreter.configure_rtd_type(rtd_type, rtd_resistance)

    @ivi_synchronized
    def configure_thermistor_custom(self, thermistor_a, thermistor_b, thermistor_c):
        r'''configure_thermistor_custom

        Configures the A, B, and C parameters for a custom thermistor.

        Args:
            thermistor_a (float): Specifies the Steinhart-Hart A coefficient for thermistor scaling when
                Thermistor Type is set to Custom in the ConfigureThermistorType
                method. The default is 1.0295e-3 (44006).

                Note:
                One or more of the referenced methods are not in the Python API for this driver.

            thermistor_b (float): Specifies the Steinhart-Hart B coefficient for thermistor scaling when
                Thermistor Type is set to Custom in the ConfigureThermistorType
                method. The default is 2.391e-4 (44006).

                Note:
                One or more of the referenced methods are not in the Python API for this driver.

            thermistor_c (float): Specifies the Steinhart-Hart C coefficient for thermistor scaling when
                Thermistor Type is set to Custom in the ConfigureThermistorType
                method. The default is 1.568e-7 (44006).

                Note:
                One or more of the referenced methods are not in the Python API for this driver.

        '''
        self._interpreter.configure_thermistor_custom(thermistor_a, thermistor_b, thermistor_c)

    @ivi_synchronized
    def configure_thermocouple(self, thermocouple_type, reference_junction_type=enums.ThermocoupleReferenceJunctionType.FIXED):
        r'''configure_thermocouple

        Configures the thermocouple type and reference junction type for a
        chosen thermocouple.

        Args:
            thermocouple_type (enums.ThermocoupleType): Specifies the type of thermocouple used to measure the temperature.
                NI-DMM uses this value to set the Thermocouple Type property. The
                default is ThermocoupleType.J.

                +--------------------+---------------------+
                | ThermocoupleType.B | Thermocouple type B |
                +--------------------+---------------------+
                | ThermocoupleType.E | Thermocouple type E |
                +--------------------+---------------------+
                | ThermocoupleType.J | Thermocouple type J |
                +--------------------+---------------------+
                | ThermocoupleType.K | Thermocouple type K |
                +--------------------+---------------------+
                | ThermocoupleType.N | Thermocouple type N |
                +--------------------+---------------------+
                | ThermocoupleType.R | Thermocouple type R |
                +--------------------+---------------------+
                | ThermocoupleType.S | Thermocouple type S |
                +--------------------+---------------------+
                | ThermocoupleType.T | Thermocouple type T |
                +--------------------+---------------------+

            reference_junction_type (enums.ThermocoupleReferenceJunctionType): Specifies the type of reference junction to be used in the reference
                junction compensation of a thermocouple measurement. NI-DMM uses this
                value to set the Reference Junction Type property. The only supported
                value is ThermocoupleReferenceJunctionType.FIXED.

        '''
        if type(thermocouple_type) is not enums.ThermocoupleType:
            raise TypeError('Parameter thermocouple_type must be of type ' + str(enums.ThermocoupleType))
        if type(reference_junction_type) is not enums.ThermocoupleReferenceJunctionType:
            raise TypeError('Parameter reference_junction_type must be of type ' + str(enums.ThermocoupleReferenceJunctionType))
        self._interpreter.configure_thermocouple(thermocouple_type, reference_junction_type)

    @ivi_synchronized
    def configure_trigger(self, trigger_source, trigger_delay=hightime.timedelta(seconds=-1)):
        r'''configure_trigger

        Configures the DMM **Trigger_Source** and **Trigger_Delay**. Refer to
        `Triggering <REPLACE_DRIVER_SPECIFIC_URL_1(trigger)>`__ and `Using
        Switches <REPLACE_DRIVER_SPECIFIC_URL_1(switch_selection)>`__ for more
        information.

        Args:
            trigger_source (enums.TriggerSource): Specifies the **trigger_source** that initiates the acquisition. The
                driver sets trigger_source to this value. Software
                configures the DMM to wait until send_software_trigger is called
                before triggering the DMM.

                Note:
                To determine which values are supported by each device, refer to the
                `LabWindows/CVI Trigger
                Routing <REPLACE_DRIVER_SPECIFIC_URL_1(cvitrigger_routing)>`__ section.

            trigger_delay (hightime.timedelta, datetime.timedelta, or float in seconds): Specifies the time that the DMM waits after it has received a trigger
                before taking a measurement. The driver sets the
                trigger_delay property to this value. By default,
                **trigger_delay** is NIDMM_VAL_AUTO_DELAY (-1), which means the DMM
                waits an appropriate settling time before taking the measurement. On the
                NI 4060, if you set **trigger_delay** to 0, the DMM does not settle
                before taking the measurement. The NI 4065 and NI 4070/4071/4072 use the
                value specified in **trigger_delay** as additional settling time.

                Note:
                When using the NI 4050, **Trigger_Delay** must be set to
                NIDMM_VAL_AUTO_DELAY (-1).

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        '''
        if type(trigger_source) is not enums.TriggerSource:
            raise TypeError('Parameter trigger_source must be of type ' + str(enums.TriggerSource))
        trigger_delay = _converters.convert_timedelta_to_seconds_real64(trigger_delay)
        self._interpreter.configure_trigger(trigger_source, trigger_delay)

    @ivi_synchronized
    def configure_waveform_acquisition(self, measurement_function, range, rate, waveform_points):
        r'''configure_waveform_acquisition

        Configures the DMM for waveform acquisitions. This feature is supported
        on the NI 4080/4081/4082 and the NI 4070/4071/4072.

        Args:
            measurement_function (enums.Function): Specifies the **measurement_function** used in a waveform acquisition.
                The driver sets method to this value.

                +-----------------------------------+------+------------------+
                | Method.WAVEFORM_VOLTAGE (default) | 1003 | Voltage Waveform |
                +-----------------------------------+------+------------------+
                | Method.WAVEFORM_CURRENT           | 1004 | Current Waveform |
                +-----------------------------------+------+------------------+

            range (float): Specifies the expected maximum amplitude of the input signal and sets
                the **range** for the **Measurement_Function**. NI-DMM sets
                range to this value. **range** values are coerced up to the
                closest input **range**. The default is 10.0.

                For valid ranges refer to the topics in
                `Devices <REPLACE_DRIVER_SPECIFIC_URL_1(devices)>`__.

                Auto-ranging is not supported during waveform acquisitions.

            rate (float): Specifies the **rate** of the acquisition in samples per second. NI-DMM
                sets waveform_rate to this value.

                The valid **Range** is 10.0–1,800,000 S/s. **rate** values are coerced
                to the closest integer divisor of 1,800,000. The default value is
                1,800,000.

            waveform_points (int): Specifies the number of points to acquire before the waveform
                acquisition completes. NI-DMM sets waveform_points to this
                value.

                To calculate the maximum and minimum number of waveform points that you
                can acquire in one acquisition, refer to the `Waveform Acquisition
                Measurement Cycle <REPLACE_DRIVER_SPECIFIC_URL_1(waveform_cycle)>`__.

                The default value is 500.

        '''
        if type(measurement_function) is not enums.Function:
            raise TypeError('Parameter measurement_function must be of type ' + str(enums.Function))
        self._interpreter.configure_waveform_acquisition(measurement_function, range, rate, waveform_points)

    @ivi_synchronized
    def disable(self):
        r'''disable

        Places the instrument in a quiescent state where it has minimal or no
        impact on the system to which it is connected. If a measurement is in
        progress when this method is called, the measurement is aborted.
        '''
        self._interpreter.disable()

    @ivi_synchronized
    def export_attribute_configuration_buffer(self):
        r'''export_attribute_configuration_buffer

        Exports the property configuration of the session to the specified
        configuration buffer.

        You can export and import session property configurations only between
        devices with identical model numbers.

        This method verifies that the properties you have configured for the
        session are valid. If the configuration is invalid, NI‑DMM returns an
        error.

        **Coercion Behavior for Certain Devices**

        Imported and exported property configurations contain coerced values
        for the following NI‑DMM devices:

        -  PXI/PCI/PCIe/USB‑4065
        -  PXI/PCI‑4070
        -  PXI‑4071
        -  PXI‑4072

        NI‑DMM coerces property values when the value you set is within the
        allowed range for the property but is not one of the discrete valid
        values the property supports. For example, for a property that
        coerces values up, if you choose a value of 4 when the adjacent valid
        values are 1 and 10, the property coerces the value to 10.

        **Related Topics:**

        `Using Properties and Properties with
        NI‑DMM <REPLACE_DRIVER_SPECIFIC_URL_1(properties)>`__

        `Setting Properties Before Reading
        Properties <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__

        Note: Not supported on the PCMCIA‑4050 or the PXI/PCI‑4060.

        Returns:
            configuration (bytes): Specifies the byte array buffer to be populated with the exported
                property configuration.

        '''
        configuration = self._interpreter.export_attribute_configuration_buffer()
        return _converters.convert_to_bytes(configuration)

    @ivi_synchronized
    def export_attribute_configuration_file(self, file_path):
        r'''export_attribute_configuration_file

        Exports the property configuration of the session to the specified
        file.

        You can export and import session property configurations only between
        devices with identical model numbers.

        This method verifies that the properties you have configured for the
        session are valid. If the configuration is invalid, NI‑DMM returns an
        error.

        **Coercion Behavior for Certain Devices**

        Imported and exported property configurations contain coerced values
        for the following NI‑DMM devices:

        -  PXI/PCI/PCIe/USB‑4065
        -  PXI/PCI‑4070
        -  PXI‑4071
        -  PXI‑4072

        NI‑DMM coerces property values when the value you set is within the
        allowed range for the property but is not one of the discrete valid
        values the property supports. For example, for a property that
        coerces values up, if you choose a value of 4 when the adjacent valid
        values are 1 and 10, the property coerces the value to 10.

        **Related Topics:**

        `Using Properties and Properties with
        NI‑DMM <REPLACE_DRIVER_SPECIFIC_URL_1(properties)>`__

        `Setting Properties Before Reading
        Properties <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__

        Note: Not supported on the PCMCIA‑4050 or the PXI/PCI‑4060.

        Args:
            file_path (str): Specifies the absolute path to the file to contain the exported
                property configuration. If you specify an empty or relative path, this
                method returns an error.
                **Default file extension:**\  .nidmmconfig

        '''
        self._interpreter.export_attribute_configuration_file(file_path)

    @ivi_synchronized
    def fetch(self, maximum_time=hightime.timedelta(milliseconds=-1)):
        r'''fetch

        Returns the value from a previously initiated measurement. You must call
        _initiate before calling this method.

        Args:
            maximum_time (hightime.timedelta, datetime.timedelta, or int in milliseconds): Specifies the **maximum_time** allowed for this method to complete in
                milliseconds. If the method does not complete within this time
                interval, the method returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                NIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout
                automatically.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        Returns:
            reading (float): The measured value returned from the DMM.

        '''
        maximum_time = _converters.convert_timedelta_to_milliseconds_int32(maximum_time)
        reading = self._interpreter.fetch(maximum_time)
        return reading

    @ivi_synchronized
    def fetch_multi_point(self, array_size, maximum_time=hightime.timedelta(milliseconds=-1)):
        r'''fetch_multi_point

        Returns an array of values from a previously initiated multipoint
        measurement. The number of measurements the DMM makes is determined by
        the values you specify for the **Trigger_Count** and **Sample_Count**
        parameters of configure_multi_point. You must first call
        _initiate to initiate a measurement before calling this method.

        Args:
            array_size (int): Specifies the number of measurements to acquire. The maximum number of
                measurements for a finite acquisition is the (**Trigger Count** x
                **Sample Count**) parameters in configure_multi_point.

                For continuous acquisitions, up to 100,000 points can be returned at
                once. The number of measurements can be a subset. The valid range is any
                positive ViInt32. The default value is 1.

            maximum_time (hightime.timedelta, datetime.timedelta, or int in milliseconds): Specifies the **maximum_time** allowed for this method to complete in
                milliseconds. If the method does not complete within this time
                interval, the method returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                NIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout
                automatically.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        Returns:
            reading_array (array.array("d")): An array of measurement values.

                Note:
                The size of the **Reading_Array** must be at least the size that you
                specify for the **Array_Size** parameter.

        '''
        maximum_time = _converters.convert_timedelta_to_milliseconds_int32(maximum_time)
        reading_array = self._interpreter.fetch_multi_point(maximum_time, array_size)
        return reading_array

    @ivi_synchronized
    def fetch_waveform(self, array_size, maximum_time=hightime.timedelta(milliseconds=-1)):
        r'''fetch_waveform

        For the NI 4080/4081/4082 and the NI 4070/4071/4072, returns an array of
        values from a previously initiated waveform acquisition. You must call
        _initiate before calling this method.

        Args:
            array_size (int): Specifies the number of waveform points to return. You specify the total
                number of points that the DMM acquires in the **Waveform Points**
                parameter of configure_waveform_acquisition. The default value is
                1.

            maximum_time (hightime.timedelta, datetime.timedelta, or int in milliseconds): Specifies the **maximum_time** allowed for this method to complete in
                milliseconds. If the method does not complete within this time
                interval, the method returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                NIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout
                automatically.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        Returns:
            waveform_array (array.array("d")): **Waveform Array** is an array of measurement values stored in waveform
                data type.

        '''
        maximum_time = _converters.convert_timedelta_to_milliseconds_int32(maximum_time)
        waveform_array = self._interpreter.fetch_waveform(maximum_time, array_size)
        return waveform_array

    @ivi_synchronized
    def fetch_waveform_into(self, waveform_array, maximum_time=hightime.timedelta(milliseconds=-1)):
        r'''fetch_waveform_into

        For the NI 4080/4081/4082 and the NI 4070/4071/4072, returns an array of
        values from a previously initiated waveform acquisition. You must call
        _initiate before calling this method.

        Args:
            waveform_array (numpy.array(dtype=numpy.float64)): **Waveform Array** is an array of measurement values stored in waveform
                data type.

            maximum_time (hightime.timedelta, datetime.timedelta, or int in milliseconds): Specifies the **maximum_time** allowed for this method to complete in
                milliseconds. If the method does not complete within this time
                interval, the method returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                NIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout
                automatically.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        '''
        import numpy

        if type(waveform_array) is not numpy.ndarray:
            raise TypeError('waveform_array must be {0}, is {1}'.format(numpy.ndarray, type(waveform_array)))
        if numpy.isfortran(waveform_array) is True:
            raise TypeError('waveform_array must be in C-order')
        if waveform_array.dtype is not numpy.dtype('float64'):
            raise TypeError('waveform_array must be numpy.ndarray of dtype=float64, is ' + str(waveform_array.dtype))
        maximum_time = _converters.convert_timedelta_to_milliseconds_int32(maximum_time)
        self._interpreter.fetch_waveform_into(waveform_array, maximum_time)

    @ivi_synchronized
    def _get_cal_date_and_time(self, cal_type):
        r'''_get_cal_date_and_time

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

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        Returns:
            month (int): Indicates the **month** of the last calibration.

            day (int): Indicates the **day** of the last calibration.

            year (int): Indicates the **year** of the last calibration.

            hour (int): Indicates the **hour** of the last calibration.

            minute (int): Indicates the **minute** of the last calibration.

        '''
        month, day, year, hour, minute = self._interpreter.get_cal_date_and_time(cal_type)
        return month, day, year, hour, minute

    @ivi_synchronized
    def get_dev_temp(self, options=""):
        r'''get_dev_temp

        Returns the current **Temperature** of the device.

        Note: The NI 4050 and NI 4060 are not supported.

        Args:
            options (str): Reserved.


        Returns:
            temperature (float): Returns the current **temperature** of the device.

        '''
        temperature = self._interpreter.get_dev_temp(options)
        return temperature

    @ivi_synchronized
    def get_ext_cal_recommended_interval(self):
        r'''get_ext_cal_recommended_interval

        Returns the recommended interval between external recalibration in
        **Months**.

        Note: The NI 4050 and NI 4060 are not supported.

        Returns:
            months (hightime.timedelta): Returns the recommended number of **months** between external
                calibrations.

        '''
        months = self._interpreter.get_ext_cal_recommended_interval()
        return _converters.convert_month_to_timedelta(months)

    @ivi_synchronized
    def get_cal_date_and_time(self, cal_type):
        '''get_cal_date_and_time

        Returns the date and time of the last calibration performed.

        Note: The NI 4050 and NI 4060 are not supported.

        Args:
            cal_type (int): Specifies the type of calibration performed (external or self-calibration).

                +-----------------------------------+---+----------------------+
                | NIDMM_VAL_INTERNAL_AREA (default) | 0 | Self-Calibration     |
                +-----------------------------------+---+----------------------+
                | NIDMM_VAL_EXTERNAL_AREA           | 1 | External Calibration |
                +-----------------------------------+---+----------------------+

                Note: The NI 4065 does not support self-calibration.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        Returns:
            last_cal_datetime (hightime.datetime): Indicates date and time of the last calibration.

        '''
        month, day, year, hour, minute = self._get_cal_date_and_time(cal_type)
        return hightime.datetime(year, month, day, hour, minute)

    @ivi_synchronized
    def get_last_cal_temp(self, cal_type):
        r'''get_last_cal_temp

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

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        Returns:
            temperature (float): Returns the **temperature** during the last calibration.

        '''
        temperature = self._interpreter.get_last_cal_temp(cal_type)
        return temperature

    @ivi_synchronized
    def get_self_cal_supported(self):
        r'''get_self_cal_supported

        Returns a Boolean value that expresses whether or not the DMM that you
        are using can perform self-calibration.

        Returns:
            self_cal_supported (bool): Returns whether Self Cal is supported for the device specified by the
                given session.

                +-------+---+-------------------------------------------------------------+
                | True  | 1 | The DMM that you are using can perform self-calibration.    |
                +-------+---+-------------------------------------------------------------+
                | False | 0 | The DMM that you are using cannot perform self-calibration. |
                +-------+---+-------------------------------------------------------------+

        '''
        self_cal_supported = self._interpreter.get_self_cal_supported()
        return self_cal_supported

    @ivi_synchronized
    def import_attribute_configuration_buffer(self, configuration):
        r'''import_attribute_configuration_buffer

        Imports a property configuration to the session from the specified
        configuration buffer.

        You can export and import session property configurations only between
        devices with identical model numbers.

        **Coercion Behavior for Certain Devices**

        Imported and exported property configurations contain coerced values
        for the following NI‑DMM devices:

        -  PXI/PCI/PCIe/USB‑4065
        -  PXI/PCI‑4070
        -  PXI‑4071
        -  PXI‑4072

        NI‑DMM coerces property values when the value you set is within the
        allowed range for the property but is not one of the discrete valid
        values the property supports. For example, for a property that
        coerces values up, if you choose a value of 4 when the adjacent valid
        values are 1 and 10, the property coerces the value to 10.

        **Related Topics:**

        `Using Properties and Properties with
        NI‑DMM <REPLACE_DRIVER_SPECIFIC_URL_1(properties)>`__

        `Setting Properties Before Reading
        Properties <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__

        Note: Not supported on the PCMCIA‑4050 or the PXI/PCI‑4060.

        Args:
            configuration (bytes): Specifies the byte array buffer that contains the property
                configuration to import.

        '''
        configuration = _converters.convert_to_bytes(configuration)
        self._interpreter.import_attribute_configuration_buffer(configuration)

    @ivi_synchronized
    def import_attribute_configuration_file(self, file_path):
        r'''import_attribute_configuration_file

        Imports a property configuration to the session from the specified
        file.

        You can export and import session property configurations only between
        devices with identical model numbers.

        **Coercion Behavior for Certain Devices**

        Imported and exported property configurations contain coerced values
        for the following NI‑DMM devices:

        -  PXI/PCI/PCIe/USB‑4065
        -  PXI/PCI‑4070
        -  PXI‑4071
        -  PXI‑4072

        NI‑DMM coerces property values when the value you set is within the
        allowed range for the property but is not one of the discrete valid
        values the property supports. For example, for a property that
        coerces values up, if you choose a value of 4 when the adjacent valid
        values are 1 and 10, the property coerces the value to 10.

        **Related Topics:**

        `Using Properties and Properties with
        NI‑DMM <REPLACE_DRIVER_SPECIFIC_URL_1(properties)>`__

        `Setting Properties Before Reading
        Properties <javascript:LaunchHelp('DMM.chm::/setting_before_reading_attributes')>`__

        Note: Not supported on the PCMCIA‑4050 or the PXI/PCI‑4060.

        Args:
            file_path (str): Specifies the absolute path to the file containing the property
                configuration to import. If you specify an empty or relative path, this
                method returns an error.
                **Default File Extension:**\  .nidmmconfig

        '''
        self._interpreter.import_attribute_configuration_file(file_path)

    def _init_with_options(self, resource_name, id_query=False, reset_device=False, option_string=""):
        r'''_init_with_options

        This method completes the following tasks:

        -  Creates a new IVI instrument driver session and, optionally, sets the
           initial state of the following session properties:
           RANGE_CHECK, QUERY_INSTR_STATUS,
           CACHE, simulate,
           RECORD_COERCIONS.
        -  Opens a session to the device you specify for the **Resource_Name**
           parameter. If the **ID_Query** parameter is set to True, this
           method queries the instrument ID and checks that it is valid for
           this instrument driver.
        -  If the **Reset_Device** parameter is set to True, this method
           resets the instrument to a known state. Sends initialization commands
           to set the instrument to the state necessary for the operation of the
           instrument driver.
        -  Returns a ViSession handle that you use to identify the instrument in
           all subsequent instrument driver method calls.

        Note:
        One or more of the referenced properties are not in the Python API for this driver.

        Args:
            resource_name (str): Caution:
                All IVI names for the **Resource_Name**, such as logical names or
                virtual names, are case-sensitive. If you use logical names, driver
                session names, or virtual names in your program, you must make sure that
                the name you use matches the name in the IVI Configuration Store file
                exactly, without any variations in the case of the characters in the
                name.

                | Contains the **resource_name** of the device to initialize. The
                  **resource_name** is assigned in Measurement & Automation Explorer
                  (MAX). Refer to `Related
                  Documentation <REPLACE_DRIVER_SPECIFIC_URL_1(related_documentation)>`__
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

                +----------------+---+------------------+
                | True (default) | 1 | Perform ID Query |
                +----------------+---+------------------+
                | False          | 0 | Skip ID Query    |
                +----------------+---+------------------+

            reset_device (bool): Specifies whether to reset the instrument during the initialization
                procedure.
                Defined Values:

                +----------------+---+--------------+
                | True (default) | 1 | Reset Device |
                +----------------+---+--------------+
                | False          | 0 | Don't Reset  |
                +----------------+---+--------------+

            option_string (dict): | Sets the initial value of certain properties for the session. The
                  following table specifies the property name, property constant, and
                  default value for each property that you can use in this parameter:

                The format of this string is, "AttributeName=Value." To set multiple
                properties, separate their assignments with a comma.

                If you pass NULL or an empty string for this parameter, the session uses
                the default values for the properties. You can override the default
                values by assigning a value explicitly in an **option_string**
                parameter. You do not have to specify all of the properties and may
                leave any of them out (those left out use the default value).

                Refer to `Simulating NI Digital
                Multimeters <REPLACE_DRIVER_SPECIFIC_URL_1(simulation)>`__ for more
                information.

                +------------------+--------------------+-------------------+----+
                | Check            | RANGE_CHECK        | True              | 1  |
                +------------------+--------------------+-------------------+----+
                | QueryInstrStatus | QUERY_INSTR_STATUS | False             | 0  |
                +------------------+--------------------+-------------------+----+
                | Cache            | CACHE              | True              | 1  |
                +------------------+--------------------+-------------------+----+
                | Simulate         | simulate           | False             | 0  |
                +------------------+--------------------+-------------------+----+
                | RecordCoercions  | RECORD_COERCIONS   | False             | 0  |
                +------------------+--------------------+-------------------+----+
                | DriverSetup      | driver_setup       | "" (empty string) | "" |
                +------------------+--------------------+-------------------+----+

                Note:
                One or more of the referenced properties are not in the Python API for this driver.


        Returns:
            vi (int): Returns a ViSession handle that you use to identify the instrument in
                all subsequent instrument driver method calls.

        '''
        option_string = _converters.convert_init_with_options_dictionary(option_string)
        vi = self._interpreter.init_with_options(resource_name, id_query, reset_device, option_string)
        return vi

    @ivi_synchronized
    def _initiate(self):
        r'''_initiate

        Initiates an acquisition. After you call this method, the DMM leaves
        the Idle state and enters the Wait-for-Trigger state. If trigger is set
        to Immediate mode, the DMM begins acquiring measurement data. Use
        fetch, fetch_multi_point, or fetch_waveform to
        retrieve the measurement data.
        '''
        self._interpreter.initiate()

    @ivi_synchronized
    def perform_open_cable_comp(self):
        r'''perform_open_cable_comp

        For the NI 4082 and NI 4072 only, performs the open cable compensation
        measurements for the current capacitance/inductance range, and returns
        open cable compensation **Conductance** and **Susceptance** values. You
        can use the return values of this method as inputs to
        ConfigureOpenCableCompValues.

        This method returns an error if the value of the method
        property is not set to Method.CAPACITANCE (1005) or
        Method.INDUCTANCE (1006).

        Note:
        One or more of the referenced methods are not in the Python API for this driver.

        Returns:
            conductance (float): **conductance** is the measured value of open cable compensation
                **conductance**.

            susceptance (float): **susceptance** is the measured value of open cable compensation
                **susceptance**.

        '''
        conductance, susceptance = self._interpreter.perform_open_cable_comp()
        return conductance, susceptance

    @ivi_synchronized
    def perform_short_cable_comp(self):
        r'''perform_short_cable_comp

        Performs the short cable compensation measurements for the current
        capacitance/inductance range, and returns short cable compensation
        **Resistance** and **Reactance** values. You can use the return values
        of this method as inputs to ConfigureShortCableCompValues.

        This method returns an error if the value of the method
        property is not set to Method.CAPACITANCE (1005) or
        Method.INDUCTANCE (1006).

        Note:
        One or more of the referenced methods are not in the Python API for this driver.

        Returns:
            resistance (float): **resistance** is the measured value of short cable compensation
                **resistance**.

            reactance (float): **reactance** is the measured value of short cable compensation
                **reactance**.

        '''
        resistance, reactance = self._interpreter.perform_short_cable_comp()
        return resistance, reactance

    @ivi_synchronized
    def read(self, maximum_time=hightime.timedelta(milliseconds=-1)):
        r'''read

        Acquires a single measurement and returns the measured value.

        Args:
            maximum_time (hightime.timedelta, datetime.timedelta, or int in milliseconds): Specifies the **maximum_time** allowed for this method to complete in
                milliseconds. If the method does not complete within this time
                interval, the method returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                NIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout
                automatically.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        Returns:
            reading (float): The measured value returned from the DMM.

        '''
        maximum_time = _converters.convert_timedelta_to_milliseconds_int32(maximum_time)
        reading = self._interpreter.read(maximum_time)
        return reading

    @ivi_synchronized
    def read_multi_point(self, array_size, maximum_time=hightime.timedelta(milliseconds=-1)):
        r'''read_multi_point

        Acquires multiple measurements and returns an array of measured values.
        The number of measurements the DMM makes is determined by the values you
        specify for the **Trigger_Count** and **Sample_Count** parameters in
        configure_multi_point.

        Args:
            array_size (int): Specifies the number of measurements to acquire. The maximum number of
                measurements for a finite acquisition is the (**Trigger Count** x
                **Sample Count**) parameters in configure_multi_point.

                For continuous acquisitions, up to 100,000 points can be returned at
                once. The number of measurements can be a subset. The valid range is any
                positive ViInt32. The default value is 1.

            maximum_time (hightime.timedelta, datetime.timedelta, or int in milliseconds): Specifies the **maximum_time** allowed for this method to complete in
                milliseconds. If the method does not complete within this time
                interval, the method returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                NIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout
                automatically.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        Returns:
            reading_array (array.array("d")): An array of measurement values.

                Note:
                The size of the **Reading_Array** must be at least the size that you
                specify for the **Array_Size** parameter.

        '''
        maximum_time = _converters.convert_timedelta_to_milliseconds_int32(maximum_time)
        reading_array = self._interpreter.read_multi_point(maximum_time, array_size)
        return reading_array

    @ivi_synchronized
    def read_status(self):
        r'''read_status

        Returns measurement backlog and acquisition status. Use this method to
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
        acquisition_backlog, acquisition_status = self._interpreter.read_status()
        return acquisition_backlog, acquisition_status

    @ivi_synchronized
    def read_waveform(self, array_size, maximum_time=hightime.timedelta(milliseconds=-1)):
        r'''read_waveform

        For the NI 4080/4081/4082 and the NI 4070/4071/4072, acquires a waveform
        and returns data as an array of values or as a waveform data type. The
        number of elements in the **Waveform_Array** is determined by the
        values you specify for the **Waveform_Points** parameter in
        configure_waveform_acquisition.

        Args:
            array_size (int): Specifies the number of waveform points to return. You specify the total
                number of points that the DMM acquires in the **Waveform Points**
                parameter of configure_waveform_acquisition. The default value is
                1.

            maximum_time (hightime.timedelta, datetime.timedelta, or int in milliseconds): Specifies the **maximum_time** allowed for this method to complete in
                milliseconds. If the method does not complete within this time
                interval, the method returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                NIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout
                automatically.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        Returns:
            waveform_array (array.array("d")): An array of measurement values.

                Note:
                The size of the **Waveform_Array** must be at least the size that you
                specify for the **Array_Size** parameter.

        '''
        maximum_time = _converters.convert_timedelta_to_milliseconds_int32(maximum_time)
        waveform_array = self._interpreter.read_waveform(maximum_time, array_size)
        return waveform_array

    @ivi_synchronized
    def reset_with_defaults(self):
        r'''reset_with_defaults

        Resets the instrument to a known state and sends initialization commands
        to the DMM. The initialization commands set the DMM settings to the
        state necessary for the operation of NI-DMM. All user-defined default
        values associated with a logical name are applied after setting the DMM.
        '''
        self._interpreter.reset_with_defaults()

    @ivi_synchronized
    def self_cal(self):
        r'''self_cal

        For the NI 4080/4081/4082 and the NI 4070/4071/4072, executes the
        self-calibration routine to maintain measurement accuracy.

        Note:
        This method calls reset, and any configurations previous to
        the call will be lost. All properties will be set to their default
        values after the call returns.
        '''
        self._interpreter.self_cal()

    @ivi_synchronized
    def send_software_trigger(self):
        r'''send_software_trigger

        Sends a command to trigger the DMM. Call this method if you have
        configured either the trigger_source or
        sample_trigger properties. If the
        trigger_source and/or sample_trigger
        properties are set to NIDMM_VAL_EXTERNAL or NIDMM_VAL_TTL\ *n*, you
        can use this method to override the trigger source that you configured
        and trigger the device. The NI 4050 and NI 4060 are not supported.

        Note:
        One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
        '''
        self._interpreter.send_software_trigger()

    def _close(self):
        r'''_close

        Closes the specified session and deallocates resources that it reserved.
        '''
        self._interpreter.close()

    @ivi_synchronized
    def self_test(self):
        '''self_test

        Performs a self-test on the DMM to ensure that the DMM is functioning
        properly. Self-test does not calibrate the DMM. Zero
        indicates success.

        On the NI 4080/4082 and NI 4070/4072, the error code 1013 indicates that
        you should check the fuse and replace it, if necessary.

        Raises `SelfTestError` on self test failure. Properties on exception object:

        - code - failure code from driver
        - message - status message from driver

        Note: Self-test does not check the fuse on the NI 4065, NI 4071, and NI 4081. Hence, even if the fuse is blown on the device, self-test does not return error code 1013.

        Note: This method calls reset, and any configurations previous to the call will be lost. All properties will be set to their default values after the call returns.
        '''
        code, msg = self._self_test()
        if code:
            raise errors.SelfTestError(code, msg)
        return None

    @ivi_synchronized
    def reset(self):
        r'''reset

        Resets the instrument to a known state and sends initialization commands
        to the instrument. The initialization commands set instrument settings
        to the state necessary for the operation of the instrument driver.
        '''
        self._interpreter.reset()

    @ivi_synchronized
    def _self_test(self):
        r'''_self_test

        Performs a self-test on the DMM to ensure that the DMM is functioning
        properly. Self-test does not calibrate the DMM.

        Note:
        This method calls reset, and any configurations previous to
        the call will be lost. All properties will be set to their default
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

            self_test_message (str): This parameter contains the string returned from the instrument
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
        self_test_result, self_test_message = self._interpreter.self_test()
        return self_test_result, self_test_message
