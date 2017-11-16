import niscope
import pytest


@pytest.fixture(scope='function')
def session():
    with niscope.Session('FakeDevice', False, True, 'Simulate=1, DriverSetup=Model:5164; BoardType:PXIe') as simulated_session:
        yield simulated_session


def test_self_test(session):
    result, message = session.self_test()
    assert result == 0
    assert message == 'Scope Self Tests PASSED.'


def test_get_channel_name(session):
    assert session.get_channel_name(2, 3) == '1'


def test_reset(session):
    deault_fetch_relative_to = session.fetch_relative_to
    assert deault_fetch_relative_to == niscope.FetchRelativeTo.PRETRIGGER
    session.fetch_relative_to = niscope.FetchRelativeTo.READ_POINTER
    non_default_acqusition_type = session.fetch_relative_to
    assert non_default_acqusition_type == niscope.FetchRelativeTo.READ_POINTER
    session.reset()
    assert session.fetch_relative_to == niscope.FetchRelativeTo.PRETRIGGER


def test_reset_device(session):
    deault_meas_percentage_method = session.meas_percentage_method
    assert deault_meas_percentage_method == niscope.PercentageMethod.BASETOP
    session.meas_percentage_method = niscope.PercentageMethod.MINMAX
    non_default_meas_percentage_method = session.meas_percentage_method
    assert non_default_meas_percentage_method == niscope.PercentageMethod.MINMAX
    session.reset_device()
    assert session.meas_percentage_method == niscope.PercentageMethod.BASETOP


def test_reset_with_defaults(session):
    deault_meas_time_histogram_high_time = session.meas_time_histogram_high_time
    assert deault_meas_time_histogram_high_time == 0.0005
    session.meas_time_histogram_high_time = 0.0010
    non_default_meas_time_histogram_high_time = session.meas_time_histogram_high_time
    assert non_default_meas_time_histogram_high_time == 0.0010
    session.reset_with_defaults()
    assert session.meas_time_histogram_high_time == 0.0005


def test_sample_rate(session):
    assert session.sample_rate() == 1000000.0  # default sample rate for simulated 5164


def test_get_error(session):
    try:
        session.instrument_model = ''
        assert False
    except niscope.Error as e:
        assert e.code == -1074135027  # Error : Attribute is read-only.
        assert e.description.find('Attribute is read-only.') != -1
