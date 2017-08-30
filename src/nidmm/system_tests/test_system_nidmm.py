#!/usr/bin/python

import nidmm
import pytest


@pytest.fixture(scope='function')
def session():
    with nidmm.Session('FakeDevice', False, True, 'Simulate=1, DriverSetup=Model:4080; BoardType:PXIe') as simulated_session:
        yield simulated_session


def test_take_simple_measurement_works(session):
    session.configure_measurement_digits(nidmm.Function.DC_CURRENT, 1, 5.5)
    assert session.read(1000) != 0  # Assumes DMM reading is not exactly zero to support non-connected modules and simulated modules.


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
        print(e)
        pass


def test_acquisition(session):
    session.configure_measurement_digits(nidmm.Function.DC_CURRENT, 1, 5.5)
    with session.initiate():
        print(session.fetch(1000))
    with session.initiate():
        print(session.fetch(1000))


def test_multi_point_acquisition(session):
    session.configure_multi_point(4, 2, nidmm.SampleTrigger.IMMEDIATE, 0)
    session.configure_measurement_digits(nidmm.Function.DC_VOLTS, 1, 5.5)
    measurements, numberOfMeasurements = session.read_multi_point(-1, 8)
    for measurement in measurements:
        print('{:10.4f}'.format(measurement))
    assert len(measurements) == 8
    assert numberOfMeasurements == 8


def test_self_test(session):
    result, message = session.self_test()
    assert result == 0
    assert message == 'Self Test passed.'


def test_get_dev_temp(session):
    temperature = session.get_dev_temp('')
    print(temperature)
    assert 20 <= temperature <= 50
