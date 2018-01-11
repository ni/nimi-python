import math
import nidmm
import numpy
import pytest
import time


@pytest.fixture(scope='function')
def session():
    with nidmm.Session('FakeDevice', True, 'Simulate=1, DriverSetup=Model:4082; BoardType:PXIe') as simulated_session:
        yield simulated_session


# Basic usability tests
def test_take_simple_measurement_works(session):
    session.configure_measurement_digits(nidmm.Function.DC_CURRENT, 1, 5.5)
    assert session.read() != 0  # Assumes DMM reading is not exactly zero to support non-connected modules and simulated modules.


def test_acquisition(session):
    session.configure_measurement_digits(nidmm.Function.DC_CURRENT, 1, 5.5)
    with session.initiate():
        session.fetch()
    with session.initiate():
        session.fetch()


def test_multi_point_acquisition(session):
    session.configure_multi_point(4, 2)
    session.configure_measurement_digits(nidmm.Function.DC_VOLTS, 1, 5.5)
    measurements = session.read_multi_point(8)
    assert len(measurements) == 8


# Attribute tests
def test_vi_boolean_attribute(session):
    assert session.interchange_check is False


def test_vi_string_attribute(session):
    assert session.serial_number == 'FFFFFFFF'
    try:
        session.serial_number = 'FFFFFFFA'
    except nidmm.Error as e:
        assert e.code == -1074135027  # Attribute is read-only


def test_vi_int32_attribute(session):
    session.sample_count = 5
    assert 5 == session.sample_count


def test_vi_real64_attribute(session):
    session.range = 50  # Coerces up!
    assert 100 == session.range


def test_enum_attribute(session):
    session.function = nidmm.Function.AC_CURRENT
    assert session.function == nidmm.Function.AC_CURRENT
    assert type(session.function) is nidmm.Function
    try:
        session.function = nidmm.LCCalculationModel.SERIES
        assert False
    except TypeError as e:
        pass


def test_writeonly_attribute(session):
    try:
        session.channel_count = 5
        assert False
    except nidmm.Error as e:
        assert e.code == -1074135027  # Error : Attribute is read-only.


# Function tests
def test_method_get_aperture_time_info(session):
    assert session.get_aperture_time_info()[1] == nidmm.ApertureTimeUnits.SECONDS  # Assuming default aperture time unit will be seconds


def test_method_configure_power_line_frequency(session):
    session.configure_power_line_frequency(60)


def test_method_configure_trigger(session):
    # Calling Configure Trigger function and asserting True if any error occurred while function call.
    try:
        session.configure_trigger(nidmm.TriggerSource.IMMEDIATE)
    except nidmm.Error as e:
        assert True


def test_method_self_test(session):
    result, message = session.self_test()
    assert result == 0
    assert message == 'Self Test passed.'


def test_method_get_dev_temp(session):
    temperature = session.get_dev_temp('')
    assert 20 <= temperature <= 50


def test_method_reset_with_defaults(session):
    assert session.reset_with_defaults() is None


def test_method_get_self_cal_supported(session):
    assert session.get_self_cal_supported() in [True, False]


def test_method_read_status(session):
    backlog, status = session.read_status()
    assert isinstance(backlog, int)
    assert backlog == 0


def test_fetch_error_while_not_initiated(session):
    try:
        session.fetch(1000)
        assert False
    except nidmm.Error as e:
        assert e.code == -1074118641   # called fetch before calling Initiate or after calling Abort


def test_multi_point_acquisition_with_measurement_absolute(session):
    session.configure_multi_point(4, 2)
    session.configure_measurement_absolute(nidmm.Function.DC_VOLTS, 0.02, 0.001)
    measurements = session.read_multi_point(8)
    assert len(measurements) == 8


def test_disable(session):
    session.configure_measurement_digits(nidmm.Function.DC_VOLTS, 10, 5.5)
    with session.initiate():
        time.sleep(0.1)
        backlog, acquisition_state = session.read_status()
        assert acquisition_state == nidmm.AcquisitionStatus.FINISHED_WITH_BACKLOG
        session.disable()
        backlog, acquisition_state = session.read_status()
        assert acquisition_state == nidmm.AcquisitionStatus.NO_ACQUISITION_IN_PROGRESS


def test_fetch_multiple(session):
    session.configure_measurement_digits(nidmm.Function.DC_VOLTS, 10, 5.5)
    session.configure_multi_point(sample_count=10, trigger_count=1)
    with session.initiate():
        measurements = session.fetch_multi_point(5)
        assert len(measurements) == 5
        measurements = session.fetch_multi_point(5)
        backlog, acquisition_state = session.read_status()
        assert acquisition_state == nidmm.AcquisitionStatus.FINISHED_WITH_NO_BACKLOG


def test_get_auto_range_value(session):
    with session.initiate():
        session.fetch()
        auto_range_value_property = session.auto_range_value
        auto_range_value_function = session.get_auto_range_value()
        assert auto_range_value_function == auto_range_value_property
        assert auto_range_value_function == 300   # simulated device auto_range_value to maximum 300


def test_get_cal_date_time(session):
    month, day, year, hour, minute = session.get_cal_date_and_time(0)
    assert month == 3
    assert day == 1
    assert year == 1940
    assert hour == 0
    assert minute == 0   # cal_date_and_time should be 03/01/1940:00:00 for simulated 408x devices; 407x and 4065 returns 00/00/0000:00:00


def test_get_last_cal_temperature(session):
    last_cal_temp = session.get_last_cal_temp(0)
    assert last_cal_temp == 25   # last_cal_temp should be 25 for simulated 408x devices; 407x and 4065 returns 0


def test_trigger_max_time_exceeded_errror(session):
    try:
        session.configure_measurement_digits(nidmm.Function.DC_VOLTS, 10, 5.5)
        session.configure_multi_point(sample_count=10, trigger_count=1)
        session.read_multi_point(15)
        assert False
    except nidmm.Error as e:
        assert e.code == -1074126845  # Max Time exceeded before operation completed


def test_self_cal(session):
    try:
        session.self_cal()
    except nidmm.Error as e:
        assert False


def test_configure_ac_bandwidth(session):
    session.configure_ac_bandwidth(2, 300)
    assert session.ac_min_freq == 2
    assert session.ac_max_freq == 300


def test_configure_rtd(session):
    session.configure_rtd_type(nidmm.RTDType.CUSTOM, 110)
    assert session.temp_rtd_type == nidmm.RTDType.CUSTOM
    assert session.temp_rtd_res == 110
    session.configure_rtd_custom(0.1, 0.2, 0.3)
    assert session.temp_rtd_a == 0.1
    assert session.temp_rtd_b == 0.2
    assert session.temp_rtd_c == 0.3


def test_configure_thermistor(session):
    session.temp_thermistor_type = nidmm.ThermistorType.CUSTOM
    session.configure_thermistor_custom(0.1, 0.2, 0.3)
    assert session.temp_thermistor_a == 0.1
    assert session.temp_thermistor_b == 0.2
    assert session.temp_thermistor_c == 0.3


def test_configure_thermocouple(session):
    session.configure_thermocouple(nidmm.ThermocoupleType.K, nidmm.ThermocoupleReferenceJunctionType.FIXED)
    assert session.temp_tc_type == nidmm.ThermocoupleType.K
    assert session.temp_tc_ref_junc_type == nidmm.ThermocoupleReferenceJunctionType.FIXED


def test_configure_cable_compensation(session):
    session.configure_open_cable_comp_values(100, 101)
    assert session.open_cable_comp_conductance == 100
    assert session.open_cable_comp_susceptance == 101
    session.configure_short_cable_comp_values(100, 101)
    assert session.short_cable_comp_resistance == 100
    assert session.short_cable_comp_reactance == 101


def test_configure_waveform_acquisition(session):
    session.configure_waveform_acquisition(nidmm.Function.WAVEFORM_VOLTAGE, 100, 1800000, 400)
    assert session.function == nidmm.Function.WAVEFORM_VOLTAGE
    assert session.range == 100
    assert session.waveform_rate == 1800000
    assert session.waveform_points == 400


def test_fetch_waveform(session):
    number_of_points_to_read = 100
    session.configure_waveform_acquisition(nidmm.Function.WAVEFORM_VOLTAGE, 10, 1800000, number_of_points_to_read)
    with session.initiate():
        measurements = session.fetch_waveform(number_of_points_to_read)
        assert len(measurements) == number_of_points_to_read
        assert isinstance(measurements[1], float)


def test_fetch_waveform_into(session):
    number_of_points_to_read = 100
    session.configure_waveform_acquisition(nidmm.Function.WAVEFORM_VOLTAGE, 10, 1800000, number_of_points_to_read)
    with session.initiate():
        waveform = numpy.empty(number_of_points_to_read, dtype=numpy.float64)
        # Initialize with NaN so we can later verify all samples were overwritten by the driver.
        waveform.fill(float('nan'))
        session.fetch_waveform_into(waveform)
    for sample in waveform:
        assert not math.isnan(sample)


def test_fetch_waveform_error(session):
    number_of_points_to_read = 100
    try:
        session.configure_waveform_acquisition(nidmm.Function.WAVEFORM_VOLTAGE, 10, 1800000, number_of_points_to_read)
        with session.initiate():
            session.fetch_waveform(number_of_points_to_read * 2, maximum_time=1)   # trying to fetch points more than configured
            assert False
    except nidmm.Error as e:
        assert e.code == -1074126845  # Max Time exceeded before operation completed


def test_get_measurement_period():
        with nidmm.Session('FakeDevice', True, 'Simulate=1, DriverSetup=Model:4072; BoardType:PXI') as session:
            session.configure_measurement_digits(nidmm.Function.DC_VOLTS, 10, 5.5)
            measurement_period = session.get_measurement_period()
            expected_period = 0.0071333333333333335  # 0.0071333333333333335 is the time required for 4072 to take a DC_VOLT measurement with range 10V on Digits_resolution 5.5
            in_range = abs(measurement_period - expected_period) <= max(1e-09 * max(abs(measurement_period), abs(expected_period)), 0.0)   # https://stackoverflow.com/questions/5595425/what-is-the-best-way-to-compare-floats-for-almost-equality-in-python
            assert in_range is True


def test_perform_cable_compensation(session):
    session.configure_measurement_digits(nidmm.Function.CAPACITANCE, 0.002, 5.5)
    conductance, susceptance = session.perform_open_cable_comp()
    assert conductance == 0   # simulated device should return conductance, susceptance as 0
    assert susceptance == 0
    resistance, reactance = session.perform_short_cable_comp()
    assert resistance == 0   # simulated device should return resistance,reactance as 0
    assert reactance == 0


def test_read_waveform(session):
    session.configure_waveform_acquisition(nidmm.Function.WAVEFORM_VOLTAGE, 10, 1800000, 1000)
    with session.initiate():
        number_of_points_to_read = 100
        measurements = session.read_waveform(number_of_points_to_read)
        assert len(measurements) == number_of_points_to_read
        assert isinstance(measurements[1], float)


def test_send_software_trigger(session):
    session.configure_measurement_digits(nidmm.Function.DC_VOLTS, 10, 5.5)
    session.configure_multi_point(sample_count=0, sample_trigger=nidmm.SampleTrigger.SOFTWARE_TRIG, trigger_count=1)
    with session.initiate():
        session.send_software_trigger()    # Send_software_trigger will send triggers automatically for simulated devices. This line of code confirms there is no error while calling send_trigger function
        session.fetch_multi_point(3)


def test_reset_method(session):
    default_function = session.function
    session.function = nidmm.Function.PERIOD
    session.reset()
    function_after_reset = session.function
    assert default_function == function_after_reset


def test_error_message(session):
    # Calling the private function directly, as _get_error_message() only gets called when you have an invalid session,
    # and there is no good way for us to invalidate a simulated session.
    message = session._error_message(-1074118641)
    assert message == 'The data is not available. This can be caused by calling Fetch or FetchMultiPoint before calling Initiate or after calling Abort.'


def test_set_boolean_attribute(session):
    session.cache = False
    assert session.cache is False
    session.cache = True
    assert session.cache is True


def test_get_ext_cal_recommended_interval(session):
    months = session.get_ext_cal_recommended_interval()
    assert months == 24
