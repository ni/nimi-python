#!/usr/bin/python

import nidmm
import pytest
import nimodinst

@pytest.fixture(scope='function')
def device_info(request):
    device_info = {}
    device_name = "unknown"
    device_sn = "unknown"
    try:
        with nimodinst.Session('nidmm') as session:
            if len(session) > 0:
                device_name = session.device_name[0]
                device_sn = session.serial_number[0]

    except nimodinst.Error as e:
        sys.stderr.write(str(e))
        sys.exit(e.code)
    device_info['name'] = device_name
    device_info['sn'] = device_sn
    return device_info


def test_invalid_device_name():
    try:
        nidmm.Session("Foo!")
        assert False
    except nidmm.Error as e:
        assert e.code == -1074118656
        assert e.description.find("Device was not recognized. The device is not supported with this driver or version.") != -1
        assert e.description.find("Foo!") != -1


def test_take_simple_measurement_works(device_info):
    with nidmm.Session(device_info['name']) as session:
        session.configure_measurement_digits(nidmm.Function.DC_CURRENT, 1, 5.5)
        assert session.read(1000) != 0 # Assumes DMM reading is not exactly zero to support non-connected modules and simulated modules.


def test_wrong_parameter_type(device_info):
    with nidmm.Session(device_info['name']) as session:
        try:
            # We are passing a number where an enum is expected.
            session.configure_measurement_digits(1, 10, 5.5)
            assert False
        except TypeError as e:
            print(e)
            pass


def test_warning(device_info):
    with nidmm.Session(device_info['name']) as session:
        session.configure_measurement_digits(nidmm.Function._2_WIRE_RESISTANCE, 1e6, 3.5)
        if not session.simulate:
           try:
               print(session.read(1000)) # Assume nothing is connected to device, overrange!
               assert False
           except nidmm.Warning as w:
               print(w)
               pass
        else:
           pytest.skip("Simulated")


def test_ViBoolean_attribute(device_info):
    with nidmm.Session(device_info['name']) as session:
        assert session.interchange_check is False
        # TODO(marcoskirsch): set a boolean


def test_ViString_attribute(device_info):
    with nidmm.Session(device_info['name']) as session:
        assert device_info['name'] == session.io_resource_descriptor
        # TODO(marcoskirsch): set a string


def test_ViInt32_attribute(device_info):
    with nidmm.Session(device_info['name']) as session:
        session.sample_count = 5
        assert 5 == session.sample_count


def test_ViReal64_attribute(device_info):
    with nidmm.Session(device_info['name']) as session:
        session.range = 50 # Coerces up!
        assert 100 == session.range


def test_Enum_attribute(device_info):
    with nidmm.Session(device_info['name']) as session:
        session.function = nidmm.Function.AC_CURRENT
        assert session.function == nidmm.Function.AC_CURRENT
        assert type(session.function) is nidmm.Function
        try:
            session.function = nidmm.LCCalculationModel.SERIES
            assert False
        except TypeError as e:
            print(e)
            pass


def test_acquisition(device_info):
    with nidmm.Session(device_info['name']) as session:
        session.configure_measurement_digits(nidmm.Function.DC_CURRENT, 1, 5.5)
        with session.initiate():
            print(session.fetch(1000))
        with session.initiate():
            print(session.fetch(1000))


def test_method_call_with_zero_parameter(device_info):
    with nidmm.Session(device_info['name']) as session:
        assert session.get_aperture_time_info()[1] == 0 # Assuming default aperture time unit will be seconds


def test_method_call_with_one_parameter(device_info):
    with nidmm.Session(device_info['name']) as session:
        session.configure_power_line_frequency(60)


def test_invalid_method_call(device_info):
    #calling a function, without parameter, But it has a mandate parameter
    with nidmm.Session(device_info['name']) as session:
        try:
            session.configure_power_line_frequency()
            assert False
        except TypeError as e:
            print (e)
            pass


def test_method_call_with_two_parameter(device_info):
    # Calling Configure Trigger function and asserting True if any error occurred while function call.
    with nidmm.Session(device_info['name']) as session:
        try:
            session.configure_trigger(nidmm.TriggerSource.IMMEDIATE, 1)
        except nidmm.Error as e:
            print (e)
            assert True


def test_multi_point_acquisition(device_info):
    with nidmm.Session(device_info['name']) as session:
        session.configure_multi_point(4, 2, nidmm.SampleTrigger.IMMEDIATE, 0)
        session.configure_measurement_digits(nidmm.Function.DC_VOLTS, 1, 5.5)
        measurements, numberOfMeasurements = session.read_multi_point(-1, 8)
        for measurement in measurements:
            print('{:10.4f}'.format(measurement))
        assert len(measurements) == 8
        assert numberOfMeasurements == 8


def test_library_singleton(device_info):
    with nidmm.Session(device_info['name']) as session:
        lib1 = session.library
    with nidmm.Session(device_info['name']) as session:
        lib2 = session.library
    assert lib1 == lib2


def test_self_test(device_info):
    with nidmm.Session(device_info['name']) as session:
        result, message = session.self_test()
        assert result == 0
        assert message == 'Self Test passed.'


def test_get_dev_temp(device_info):
    with nidmm.Session(device_info['name']) as session:
        temperature = session.get_dev_temp('')
        print(temperature)
        assert 20 <= temperature <= 50
