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


# TODO(marcoskirsch): We may want to support this, plus a Session constructor that uses an existing ViSession.
class AttributeViSession(object):

    def __init__(self, attribute_id):
        self.attribute_id = attribute_id

    def __get__(self, obj, objtype):
        raise TypeError('Attributes of type ViSession are unsupported in Python')

    def __set__(self, obj, value):
        raise TypeError('Attributes of type ViSession are unsupported in Python')


class Session(object):
    '''An NI-DMM session to a National Instruments Digital Multimeter'''

    ac_max_freq = AttributeViReal64(1250007)
    '''
    See `ac_max_freq <nidmm_attributes.html#nidmm.attribute.ac_max_freq>`__
    '''
    ac_min_freq = AttributeViReal64(1250006)
    '''
    See `ac_min_freq <nidmm_attributes.html#nidmm.attribute.ac_min_freq>`__
    '''
    adc_calibration = AttributeEnum(1150022, enums.EnabledSetting)
    '''
    See `adc_calibration <nidmm_attributes.html#nidmm.attribute.adc_calibration>`__
    '''
    aperture_time = AttributeViReal64(1250321)
    '''
    See `aperture_time <nidmm_attributes.html#nidmm.attribute.aperture_time>`__
    '''
    aperture_time_units = AttributeEnum(1250322, enums.ApertureTimeUnits)
    '''
    See `aperture_time_units <nidmm_attributes.html#nidmm.attribute.aperture_time_units>`__
    '''
    auto_range_value = AttributeViReal64(1250331)
    '''
    See `auto_range_value <nidmm_attributes.html#nidmm.attribute.auto_range_value>`__
    '''
    auto_zero = AttributeEnum(1250332, enums.EnabledSetting)
    '''
    See `auto_zero <nidmm_attributes.html#nidmm.attribute.auto_zero>`__
    '''
    buffer_size = AttributeViInt32(1150037)
    '''
    See `buffer_size <nidmm_attributes.html#nidmm.attribute.buffer_size>`__
    '''
    cable_comp_type = AttributeEnum(1150045, enums.CableCompensationType)
    '''
    See `cable_comp_type <nidmm_attributes.html#nidmm.attribute.cable_comp_type>`__
    '''
    cache = AttributeViBoolean(1050004)
    '''
    See `cache <nidmm_attributes.html#nidmm.attribute.cache>`__
    '''
    channel_count = AttributeViInt32(1050203)
    '''
    See `channel_count <nidmm_attributes.html#nidmm.attribute.channel_count>`__
    '''
    class_driver_class_spec_major_version = AttributeViInt32(1050519)
    '''
    See `class_driver_class_spec_major_version <nidmm_attributes.html#nidmm.attribute.class_driver_class_spec_major_version>`__
    '''
    class_driver_class_spec_minor_version = AttributeViInt32(1050520)
    '''
    See `class_driver_class_spec_minor_version <nidmm_attributes.html#nidmm.attribute.class_driver_class_spec_minor_version>`__
    '''
    config_product_number = AttributeViInt32(1150061)
    '''
    See `config_product_number <nidmm_attributes.html#nidmm.attribute.config_product_number>`__
    '''
    current_source = AttributeViReal64(1150025)
    '''
    See `current_source <nidmm_attributes.html#nidmm.attribute.current_source>`__
    '''
    dc_bias = AttributeViInt32(1150053)
    '''
    See `dc_bias <nidmm_attributes.html#nidmm.attribute.dc_bias>`__
    '''
    dc_noise_rejection = AttributeEnum(1150026, enums.DCNoiseRejectionMode)
    '''
    See `dc_noise_rejection <nidmm_attributes.html#nidmm.attribute.dc_noise_rejection>`__
    '''
    driver_setup = AttributeViString(1050007)
    '''
    See `driver_setup <nidmm_attributes.html#nidmm.attribute.driver_setup>`__
    '''
    freq_voltage_auto_range_value = AttributeViReal64(1150044)
    '''
    See `freq_voltage_auto_range_value <nidmm_attributes.html#nidmm.attribute.freq_voltage_auto_range_value>`__
    '''
    freq_voltage_range = AttributeViReal64(1250101)
    '''
    See `freq_voltage_range <nidmm_attributes.html#nidmm.attribute.freq_voltage_range>`__
    '''
    function = AttributeEnum(1250001, enums.Function)
    '''
    See `function <nidmm_attributes.html#nidmm.attribute.function>`__
    '''
    group_capabilities = AttributeViString(1050401)
    '''
    See `group_capabilities <nidmm_attributes.html#nidmm.attribute.group_capabilities>`__
    '''
    input_resistance = AttributeViReal64(1150029)
    '''
    See `input_resistance <nidmm_attributes.html#nidmm.attribute.input_resistance>`__
    '''
    instrument_firmware_revision = AttributeViString(1050510)
    '''
    See `instrument_firmware_revision <nidmm_attributes.html#nidmm.attribute.instrument_firmware_revision>`__
    '''
    instrument_manufacturer = AttributeViString(1050511)
    '''
    See `instrument_manufacturer <nidmm_attributes.html#nidmm.attribute.instrument_manufacturer>`__
    '''
    instrument_model = AttributeViString(1050512)
    '''
    See `instrument_model <nidmm_attributes.html#nidmm.attribute.instrument_model>`__
    '''
    interchange_check = AttributeViBoolean(1050021)
    '''
    See `interchange_check <nidmm_attributes.html#nidmm.attribute.interchange_check>`__
    '''
    io_resource_descriptor = AttributeViString(1050304)
    '''
    See `io_resource_descriptor <nidmm_attributes.html#nidmm.attribute.io_resource_descriptor>`__
    '''
    io_session = AttributeViSession(1050322)
    '''
    See `io_session <nidmm_attributes.html#nidmm.attribute.io_session>`__
    '''
    latency = AttributeViInt32(1150034)
    '''
    See `latency <nidmm_attributes.html#nidmm.attribute.latency>`__
    '''
    lc_calculation_model = AttributeEnum(1150052, enums.LCCalculationModel)
    '''
    See `lc_calculation_model <nidmm_attributes.html#nidmm.attribute.lc_calculation_model>`__
    '''
    lc_number_meas_to_average = AttributeViInt32(1150055)
    '''
    See `lc_number_meas_to_average <nidmm_attributes.html#nidmm.attribute.lc_number_meas_to_average>`__
    '''
    logical_name = AttributeViString(1050305)
    '''
    See `logical_name <nidmm_attributes.html#nidmm.attribute.logical_name>`__
    '''
    meas_complete_dest = AttributeViInt32(1250305)
    '''
    See `meas_complete_dest <nidmm_attributes.html#nidmm.attribute.meas_complete_dest>`__
    '''
    meas_dest_slope = AttributeEnum(1150002, enums.Slope)
    '''
    See `meas_dest_slope <nidmm_attributes.html#nidmm.attribute.meas_dest_slope>`__
    '''
    number_of_averages = AttributeViInt32(1150032)
    '''
    See `number_of_averages <nidmm_attributes.html#nidmm.attribute.number_of_averages>`__
    '''
    offset_comp_ohms = AttributeEnum(1150023, enums.EnabledSetting)
    '''
    See `offset_comp_ohms <nidmm_attributes.html#nidmm.attribute.offset_comp_ohms>`__
    '''
    open_cable_comp_conductance = AttributeViReal64(1150049)
    '''
    See `open_cable_comp_conductance <nidmm_attributes.html#nidmm.attribute.open_cable_comp_conductance>`__
    '''
    open_cable_comp_susceptance = AttributeViReal64(1150048)
    '''
    See `open_cable_comp_susceptance <nidmm_attributes.html#nidmm.attribute.open_cable_comp_susceptance>`__
    '''
    operation_mode = AttributeEnum(1150014, enums.OperationMode)
    '''
    See `operation_mode <nidmm_attributes.html#nidmm.attribute.operation_mode>`__
    '''
    powerline_freq = AttributeViReal64(1250333)
    '''
    See `powerline_freq <nidmm_attributes.html#nidmm.attribute.powerline_freq>`__
    '''
    query_instrument_status = AttributeViBoolean(1050003)
    '''
    See `query_instrument_status <nidmm_attributes.html#nidmm.attribute.query_instrument_status>`__
    '''
    range = AttributeViReal64(1250002)
    '''
    See `range <nidmm_attributes.html#nidmm.attribute.range>`__
    '''
    range_check = AttributeViBoolean(1050002)
    '''
    See `range_check <nidmm_attributes.html#nidmm.attribute.range_check>`__
    '''
    record_coercions = AttributeViBoolean(1050006)
    '''
    See `record_coercions <nidmm_attributes.html#nidmm.attribute.record_coercions>`__
    '''
    resolution_absolute = AttributeViReal64(1250008)
    '''
    See `resolution_absolute <nidmm_attributes.html#nidmm.attribute.resolution_absolute>`__
    '''
    resolution_digits = AttributeViReal64(1250003)
    '''
    See `resolution_digits <nidmm_attributes.html#nidmm.attribute.resolution_digits>`__
    '''
    sample_count = AttributeViInt32(1250301)
    '''
    See `sample_count <nidmm_attributes.html#nidmm.attribute.sample_count>`__
    '''
    sample_interval = AttributeViReal64(1250303)
    '''
    See `sample_interval <nidmm_attributes.html#nidmm.attribute.sample_interval>`__
    '''
    sample_trigger = AttributeViInt32(1250302)
    '''
    See `sample_trigger <nidmm_attributes.html#nidmm.attribute.sample_trigger>`__
    '''
    sample_trigger_slope = AttributeEnum(1150010, enums.Slope)
    '''
    See `sample_trigger_slope <nidmm_attributes.html#nidmm.attribute.sample_trigger_slope>`__
    '''
    serial_number = AttributeViString(1150054)
    '''
    See `serial_number <nidmm_attributes.html#nidmm.attribute.serial_number>`__
    '''
    settle_time = AttributeViReal64(1150028)
    '''
    See `settle_time <nidmm_attributes.html#nidmm.attribute.settle_time>`__
    '''
    short_cable_comp_reactance = AttributeViReal64(1150046)
    '''
    See `short_cable_comp_reactance <nidmm_attributes.html#nidmm.attribute.short_cable_comp_reactance>`__
    '''
    short_cable_comp_resistance = AttributeViReal64(1150047)
    '''
    See `short_cable_comp_resistance <nidmm_attributes.html#nidmm.attribute.short_cable_comp_resistance>`__
    '''
    shunt_value = AttributeViReal64(1150003)
    '''
    See `shunt_value <nidmm_attributes.html#nidmm.attribute.shunt_value>`__
    '''
    simulate = AttributeViBoolean(1050005)
    '''
    See `simulate <nidmm_attributes.html#nidmm.attribute.simulate>`__
    '''
    specific_driver_class_spec_major_version = AttributeViInt32(1050515)
    '''
    See `specific_driver_class_spec_major_version <nidmm_attributes.html#nidmm.attribute.specific_driver_class_spec_major_version>`__
    '''
    specific_driver_class_spec_minor_version = AttributeViInt32(1050516)
    '''
    See `specific_driver_class_spec_minor_version <nidmm_attributes.html#nidmm.attribute.specific_driver_class_spec_minor_version>`__
    '''
    specific_driver_description = AttributeViString(1050514)
    '''
    See `specific_driver_description <nidmm_attributes.html#nidmm.attribute.specific_driver_description>`__
    '''
    specific_driver_prefix = AttributeViString(1050302)
    '''
    See `specific_driver_prefix <nidmm_attributes.html#nidmm.attribute.specific_driver_prefix>`__
    '''
    specific_driver_revision = AttributeViString(1050551)
    '''
    See `specific_driver_revision <nidmm_attributes.html#nidmm.attribute.specific_driver_revision>`__
    '''
    specific_driver_vendor = AttributeViString(1050513)
    '''
    See `specific_driver_vendor <nidmm_attributes.html#nidmm.attribute.specific_driver_vendor>`__
    '''
    supported_instrument_models = AttributeViString(1050327)
    '''
    See `supported_instrument_models <nidmm_attributes.html#nidmm.attribute.supported_instrument_models>`__
    '''
    temp_rtd_a = AttributeViReal64(1150121)
    '''
    See `temp_rtd_a <nidmm_attributes.html#nidmm.attribute.temp_rtd_a>`__
    '''
    temp_rtd_b = AttributeViReal64(1150122)
    '''
    See `temp_rtd_b <nidmm_attributes.html#nidmm.attribute.temp_rtd_b>`__
    '''
    temp_rtd_c = AttributeViReal64(1150123)
    '''
    See `temp_rtd_c <nidmm_attributes.html#nidmm.attribute.temp_rtd_c>`__
    '''
    temp_rtd_res = AttributeViReal64(1250242)
    '''
    See `temp_rtd_res <nidmm_attributes.html#nidmm.attribute.temp_rtd_res>`__
    '''
    temp_rtd_type = AttributeEnum(1150120, enums.TemperatureRTDType)
    '''
    See `temp_rtd_type <nidmm_attributes.html#nidmm.attribute.temp_rtd_type>`__
    '''
    temp_tc_fixed_ref_junc = AttributeViReal64(1250233)
    '''
    See `temp_tc_fixed_ref_junc <nidmm_attributes.html#nidmm.attribute.temp_tc_fixed_ref_junc>`__
    '''
    temp_tc_ref_junc_type = AttributeEnum(1250232, enums.TemperatureThermocoupleReferenceJunctionType)
    '''
    See `temp_tc_ref_junc_type <nidmm_attributes.html#nidmm.attribute.temp_tc_ref_junc_type>`__
    '''
    temp_tc_type = AttributeEnum(1250231, enums.TemperatureThermocoupleType)
    '''
    See `temp_tc_type <nidmm_attributes.html#nidmm.attribute.temp_tc_type>`__
    '''
    temp_thermistor_a = AttributeViReal64(1150125)
    '''
    See `temp_thermistor_a <nidmm_attributes.html#nidmm.attribute.temp_thermistor_a>`__
    '''
    temp_thermistor_b = AttributeViReal64(1150126)
    '''
    See `temp_thermistor_b <nidmm_attributes.html#nidmm.attribute.temp_thermistor_b>`__
    '''
    temp_thermistor_c = AttributeViReal64(1150127)
    '''
    See `temp_thermistor_c <nidmm_attributes.html#nidmm.attribute.temp_thermistor_c>`__
    '''
    temp_thermistor_type = AttributeEnum(1150124, enums.TemperatureThermistorType)
    '''
    See `temp_thermistor_type <nidmm_attributes.html#nidmm.attribute.temp_thermistor_type>`__
    '''
    temp_transducer_type = AttributeEnum(1250201, enums.TemperatureTransducerType)
    '''
    See `temp_transducer_type <nidmm_attributes.html#nidmm.attribute.temp_transducer_type>`__
    '''
    trigger_count = AttributeViInt32(1250304)
    '''
    See `trigger_count <nidmm_attributes.html#nidmm.attribute.trigger_count>`__
    '''
    trigger_delay = AttributeViReal64(1250005)
    '''
    See `trigger_delay <nidmm_attributes.html#nidmm.attribute.trigger_delay>`__
    '''
    trigger_slope = AttributeEnum(1250334, enums.Slope)
    '''
    See `trigger_slope <nidmm_attributes.html#nidmm.attribute.trigger_slope>`__
    '''
    trigger_source = AttributeViInt32(1250004)
    '''
    See `trigger_source <nidmm_attributes.html#nidmm.attribute.trigger_source>`__
    '''
    waveform_coupling = AttributeEnum(1150027, enums.WaveformCouplingMode)
    '''
    See `waveform_coupling <nidmm_attributes.html#nidmm.attribute.waveform_coupling>`__
    '''
    waveform_points = AttributeViInt32(1150019)
    '''
    See `waveform_points <nidmm_attributes.html#nidmm.attribute.waveform_points>`__
    '''
    waveform_rate = AttributeViReal64(1150018)
    '''
    See `waveform_rate <nidmm_attributes.html#nidmm.attribute.waveform_rate>`__
    '''

    def __init__(self, resource_name, id_query=0, reset_device=False, options_string=""):
        self.library = library.get_library()
        self.vi = 0  # This must be set before calling _init_with_options.
        self.vi = self._init_with_options(resource_name, id_query, reset_device, options_string)

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
