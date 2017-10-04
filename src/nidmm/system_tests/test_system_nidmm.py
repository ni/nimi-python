import nidmm
import pytest
# import re  used in commented test test_revision_query_string. Disabling since flake-8 fails for unused import
import time


@pytest.fixture(scope='function')
def session():
    with nidmm.Session('FakeDevice', False, True, 'Simulate=1, DriverSetup=Model:4082; BoardType:PXIe') as simulated_session:
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
    measurements, numberOfMeasurements = session.read_multi_point(8)
    assert len(measurements) == 8
    assert numberOfMeasurements == 8


# Attribute tests
def test_vi_boolean_attribute(session):
    assert session.interchange_check is False


def test_vi_string_attribute(session):
    session.error_elaboration = 'Test'
    assert 'Test' == session.error_elaboration


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
    measurements, numberOfMeasurements = session.read_multi_point(8)
    assert len(measurements) == 8
    assert numberOfMeasurements == 8


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
        assert len(measurements[0]) == 5
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
        measurements, numberOfMeasurements = session.read_multi_point(15)
    except nidmm.Error as e:
        assert e.code == -1074126845  # Max Time exceeded before operation completed


'''
# TODO(injaleea): Enable test after #396 is fixed
def test_revision_query_string(session):
    instr_driver_version, firmware_revision = session.revision_query()
    pattern = re.compile("\d+\.\d+\.\d")
    assert pattern.match(instr_driver_version)  # Assuming driver version will be always Major.Minor.Build format
'''


def test_self_cal(session):
    try:
        session.self_cal()
    except nidmm.Error as e:
        assert False

def test_configure_functions(session):
    session.configure_ac_bandwidth(1,300)
    session.configure_rtd_custom(3.9083e-3, -5.775e-7, -4.183e-12)
    session.configure_rtd_type(nidmm.RTDType.PT_3750, 100)
    session.configure_thermistor_custom(1.0295e-3, 2.391e-4, 1.568e-7)
    session.configure_thermocouple(nidmm.ThermocoupleType.J, nidmm.ThermocoupleReferenceJunctionType.FIXED)
    session.configure_open_cable_comp_values(100, 101)
    session.configure_short_cable_comp_values(100,101)
    session.configure_waveform_acquisition(nidmm.Function.WAVEFORM_VOLTAGE, 10, 1800000,500)
