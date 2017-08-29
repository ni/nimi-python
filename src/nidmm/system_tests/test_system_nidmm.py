#!/usr/bin/python

import nidmm
import pytest


@pytest.fixture(scope='function')
def create_session():    with nidmm.Session('FakeDevice', False, True, 'Simulate=1, DriverSetup=Model:4080; BoardType:PXIe') as session:        yield session


def test_invalid_device_name():    try:        nidmm.Session("Foo!")        assert False    except nidmm.Error as e:        assert e.code == -1074118656        assert e.description.find("Device was not recognized. The device is not supported with this driver or version.") != -1        assert e.description.find("Foo!") != -1


def test_take_simple_measurement_works(create_session):    create_session.configure_measurement_digits(nidmm.Function.DC_CURRENT, 1, 5.5)    assert create_session.read(1000) != 0  # Assumes DMM reading is not exactly zero to support non-connected modules and simulated modules.


def test_wrong_parameter_type(create_session):    try:        # We are passing a number where an enum is expected.        create_session.configure_measurement_digits(1, 10, 5.5)        assert False    except TypeError as e:        print(e)        pass


def test_vi_boolean_attribute(create_session):    assert create_session.interchange_check is False    # TODO(marcoskirsch): set a boolean


def test_vi_string_attribute(create_session):    assert 'FakeDevice' == create_session.io_resource_descriptor    # TODO(marcoskirsch): set a string


def test_vi_int32_attribute(create_session):    create_session.sample_count = 5    assert 5 == create_session.sample_count


def test_vi_real64_attribute(create_session):    create_session.range = 50  # Coerces up!    assert 100 == create_session.range


def test_enum_attribute(create_session):    create_session.function = nidmm.Function.AC_CURRENT    assert create_session.function == nidmm.Function.AC_CURRENT    assert type(create_session.function) is nidmm.Function    try:        create_session.function = nidmm.LCCalculationModel.SERIES        assert False    except TypeError as e:        print(e)        pass


def test_acquisition(create_session):    create_session.configure_measurement_digits(nidmm.Function.DC_CURRENT, 1, 5.5)    with create_session.initiate():        print(create_session.fetch(1000))    with create_session.initiate():        print(create_session.fetch(1000))


def test_method_call_with_zero_parameter(create_session):    assert create_session.get_aperture_time_info()[1] == nidmm.ApertureTimeUnits.SECONDS  # Assuming default aperture time unit will be seconds


def test_method_call_with_one_parameter(create_session):    create_session.configure_power_line_frequency(60)


def test_invalid_method_call(create_session):    # calling a function, without parameter, But it has a mandate parameter    try:        create_session.configure_power_line_frequency()        assert False    except TypeError as e:        print(e)        pass


def test_method_call_with_two_parameter(create_session):    # Calling Configure Trigger function and asserting True if any error occurred while function call.    try:        create_session.configure_trigger(nidmm.TriggerSource.IMMEDIATE, 1)    except nidmm.Error as e:        print(e)        assert True


def test_multi_point_acquisition(create_session):    create_session.configure_multi_point(4, 2, nidmm.SampleTrigger.IMMEDIATE, 0)    create_session.configure_measurement_digits(nidmm.Function.DC_VOLTS, 1, 5.5)    measurements, numberOfMeasurements = create_session.read_multi_point(-1, 8)    for measurement in measurements:        print('{:10.4f}'.format(measurement))    assert len(measurements) == 8    assert numberOfMeasurements == 8


def test_library_singleton():    with nidmm.Session('FakeDevice', False, True, 'Simulate=1, DriverSetup=Model:4080; BoardType:PXIe') as session:        lib1 = session.library    with nidmm.Session('FakeDevice', False, True, 'Simulate=1, DriverSetup=Model:4080; BoardType:PXIe') as session:        lib2 = session.library    assert lib1 == lib2


def test_self_test(create_session):    result, message = create_session.self_test()    assert result == 0    assert message == 'Self Test passed.'


def test_get_dev_temp(create_session):    temperature = create_session.get_dev_temp('')    print(temperature)    assert 20 <= temperature <= 50


def test_method_with_noinput_nooutput(create_session):    assert create_session.reset_with_defaults() is None


def test_method_with_vi_boolean_output_type_method(create_session):    assert create_session.get_self_cal_supported() in [True, False]


def test_method_with_enum_output_type_method(create_session):    assert create_session.read_status()[1] == nidmm.AcquisitionStatus.NO_ACQUISITION_IN_PROGRESS


def test_writeonly_attribute(create_session):    try:        create_session.channel_count = 5        assert False    except nidmm.Error as e:        assert e.code == -1074135027  # Error : Attribute is read-only.


def test_init_with_valid_optionstring():    with nidmm.Session('FakeDevice', False, True, 'Simulate = 1') as session:        assert session.simulate is True


def test_init_with_invalid_optionstring():    try:        with nidmm.Session('FakeDevice', False, True, 'Invalidstring = 1'):            assert False    except nidmm.Error as e:        assert e.code == -1074134965  # Error : The option string parameter contains an entry with an unknown option name.


def test_invalid_value_attribute(create_session):    try:        create_session.settle_time = -5        assert False    except nidmm.Error as e:        assert e.code == -1074135024  # Error : Invalid value for parameter or property.


def test_vi_int32_output_function(create_session):    backlog, status = create_session.read_status()
    assert isinstance(backlog, int)
    assert backlog == 0

