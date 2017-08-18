#!/usr/bin/python

import niswitch
import pytest
import nimodinst

@pytest.fixture(scope='function')
def device_info(request):
    device_info = {}
    device_name = "unknown"
    device_sn = "unknown"
    try:
        with nimodinst.Session('niswitch') as session:
            if len(session) > 0:
                device_name = session.device_name[0]
                device_sn = session.serial_number[0]

    except nimodinst.Error as e:
        sys.stderr.write(str(e))
        sys.exit(e.code)
    device_info['name'] = device_name
    device_info['sn'] = device_sn
    return device_info


def best_invalid_device_name():
    try:
        niswitch.Session("Foo!")
        assert False
    except niswitch.Error as e:
        assert e.code == -1074118654
        assert e.description.find("Invalid resource name.") != -1
        assert e.description.find("Foo!") != -1


def test_relayclose(device_info):
    with niswitch.Session(device_info['name']) as session:
        relayName = session.get_relay_name(1)
        positionInitial = session.get_relay_position(relayName)
        # Missing Relay Control ????
        
        positionFinal = session.get_relay_position(relayName)
        assert relayName
        assert positionInitial == positionFinal


def best_wrong_parameter_type(device_info):
    with niswitch.Session(device_info['name']) as session:
        try:
            # We are passing a number where an enum is expected.
            session.configure_measurement_digits(1, 10, 5.5)
            assert False
        except TypeError as e:
            print(e)
            pass


def best_warning(device_info):
    with niswitch.Session(device_info['name']) as session:
        session.configure_measurement_digits(niswitch.Function._2_WIRE_RESISTANCE, 1e6, 3.5)
        if not session.simulate:
           try:
               print(session.read(1000)) # Assume nothing is connected to device, overrange!
               assert False
           except niswitch.Warning as w:
               print(w)
               pass
        else:
           pytest.skip("Simulated")


def best_ViBoolean_attribute(device_info):
    with niswitch.Session(device_info['name']) as session:
        assert session.interchange_check is False
        # TODO(marcoskirsch): set a boolean


def best_ViString_attribute(device_info):
    with niswitch.Session(device_info['name']) as session:
        assert device_info['name'] == session.io_resource_descriptor
        # TODO(marcoskirsch): set a string


def best_ViInt32_attribute(device_info):
    with niswitch.Session(device_info['name']) as session:
        session.sample_count = 5
        assert 5 == session.sample_count


def best_ViReal64_attribute(device_info):
    with niswitch.Session(device_info['name']) as session:
        session.range = 50 # Coerces up!
        assert 100 == session.range


def best_Enum_attribute(device_info):
    with niswitch.Session(device_info['name']) as session:
        session.function = niswitch.Function.AC_CURRENT
        assert session.function == niswitch.Function.AC_CURRENT
        assert type(session.function) is niswitch.Function
        try:
            session.function = niswitch.LCCalculationModel.SERIES
            assert False
        except TypeError as e:
            print(e)
            pass


def best_acquisition(device_info):
    with niswitch.Session(device_info['name']) as session:
        session.configure_measurement_digits(niswitch.Function.DC_CURRENT, 1, 5.5)
        with session.initiate():
            print(session.fetch(1000))
        with session.initiate():
            print(session.fetch(1000))


def best_method_call_with_zero_parameter(device_info):
    with niswitch.Session(device_info['name']) as session:
        assert session.get_aperture_time_info()[1] == 0 # Assuming default aperture time unit will be seconds


def best_method_call_with_one_parameter(device_info):
    with niswitch.Session(device_info['name']) as session:
        session.configure_power_line_frequency(60)


def best_invalid_method_call(device_info):
    #calling a function, without parameter, But it has a mandate parameter
    with niswitch.Session(device_info['name']) as session:
        try:
            session.configure_power_line_frequency()
            assert False
        except TypeError as e:
            print (e)
            pass


def best_method_call_with_two_parameter(device_info):
    # Calling Configure Trigger function and asserting True if any error occurred while function call.
    with niswitch.Session(device_info['name']) as session:
        try:
            session.configure_trigger(niswitch.TriggerSource.IMMEDIATE, 1)
        except niswitch.Error as e:
            print (e)
            assert True


def best_multi_point_acquisition(device_info):
    with niswitch.Session(device_info['name']) as session:
        session.configure_multi_point(4, 2, niswitch.SampleTrigger.IMMEDIATE, 0)
        session.configure_measurement_digits(niswitch.Function.DC_VOLTS, 1, 5.5)
        measurements, numberOfMeasurements = session.read_multi_point(-1, 8)
        for measurement in measurements:
            print('{:10.4f}'.format(measurement))
        assert len(measurements) == 8
        assert numberOfMeasurements == 8


def best_library_singleton(device_info):
    with niswitch.Session(device_info['name']) as session:
        lib1 = session.library
    with niswitch.Session(device_info['name']) as session:
        lib2 = session.library
    assert lib1 == lib2


def best_self_test(device_info):
    with niswitch.Session(device_info['name']) as session:
        result, message = session.self_test()
        assert result == 0
        assert message == 'Self Test passed.'


def best_get_dev_temp(device_info):
    with niswitch.Session(device_info['name']) as session:
        temperature = session.get_dev_temp('')
        print(temperature)
        assert 20 <= temperature <= 50

        
def best_method_with_noinput_nooutput(device_info):
    with niswitch.Session(device_info['name']) as session:
        assert session.reset_with_defaults() == None
        
        
def best_method_with_ViBoolean_output_type_method(device_info):
    with niswitch.Session(device_info['name']) as session:
        assert session.get_self_cal_supported() in [True, False]
      
     
def best_method_with_enum_output_type_method(device_info):
    with niswitch.Session(device_info['name']) as session:
        #will have to update after https://github.com/ni/nimi-python/issues/128 fixed
        assert session.read_status()[1] == 4        
        
		
def best_writeonly_attribute(device_info):
    with niswitch.Session(device_info['name']) as session:
        try:
            session.channel_count = 5
        except niswitch.Error as e:
            assert e.code == -1074135027 #Error : Attribute is read-only.


