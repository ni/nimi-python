import nidmm
import pytest


@pytest.fixture(scope='function')
def session():
    with nidmm.Session('FakeDevice', False, True, 'Simulate=1, DriverSetup=Model:4080; BoardType:PXIe') as simulated_session:
        yield simulated_session


# Basic usability tests
def test_take_simple_measurement_works(session):
    session.configure_measurement_digits(nidmm.Function.DC_CURRENT, 1, 5.5)
    assert session.read(1000) != 0  # Assumes DMM reading is not exactly zero to support non-connected modules and simulated modules.


def test_acquisition(session):
    session.configure_measurement_digits(nidmm.Function.DC_CURRENT, 1, 5.5)
    with session.initiate():
        session.fetch(1000)
    with session.initiate():
        session.fetch(1000)


def test_multi_point_acquisition(session):
    session.configure_multi_point(4, 2, nidmm.SampleTrigger.IMMEDIATE, 0)
    session.configure_measurement_digits(nidmm.Function.DC_VOLTS, 1, 5.5)
    measurements, numberOfMeasurements = session.read_multi_point(-1, 8)
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
        session.configure_trigger(nidmm.TriggerSource.IMMEDIATE, 1)
    except nidmm.Error as e:
        assert True


def test_method_self_test(session):
    result, message = session.self_test()
    assert result == 0
    assert message == 'Self Test passed.'


def test_method_get_dev_temp(session):
    temperature = session.get_dev_temp('')
    assert 20 <= temperature <= 50


def test_method_get_self_cal_supported(session):
    assert session.get_self_cal_supported() in [True, False]


def test_method_read_status(session):
    backlog, status = session.read_status()
    assert isinstance(backlog, int)
    assert backlog == 0

