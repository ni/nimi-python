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
        print (relayName)
        positionInitial = session.get_relay_position(relayName)
        if positionInitial == 10: # if relay is open, close relay
            session.relay_control(relayName, 21)
        else:
            session.relay_control(relayName, 20)
        positionMiddle = session.get_relay_position(relayName)
        if positionMiddle == 10: # if relay is open, close relay
            session.relay_control(relayName, 21)
        else:
            session.relay_control(relayName, 20)
        positionFinal = session.get_relay_position(relayName)
        assert relayName
        assert positionInitial != positionMiddle
        assert positionMiddle != positionFinal
        assert positionInitial == positionFinal


def test_channel_connection(device_info):
   with niswitch.Session(device_info['name']) as session:
       channel1 = session.get_channel_name(1)
       for x in range (2, session.channel_count):
           channel2 = session.get_channel_name(x)
           if session.can_connect(channel1, channel2) == 1: #path available
               session.connect(channel1, channel2)
               session.disconnect(channel1, channel2)
               session.connect(channel1, channel2)
               session.disconnect_all()
               pass
               break


def test_wrong_parameter_type(device_info):
    with niswitch.Session(device_info['name']) as session:
        try:
            # We are passing a number where an enum is expected.
            session.trigger_input(1)
            assert False
        except TypeError as e:
            print(e)
            pass


def test_warning(device_info):
    with niswitch.Session(device_info['name']) as session:
       channel1 = session.get_channel_name(1)
       for x in range (2, session.channel_count):
           channel2 = session.get_channel_name(x)
           if session.can_connect(channel1, channel2) == 1: #path available
               session.connect(channel1, channel2)
               try:
                   session.can_connect(channel1, channel2)
               except niswitch.Warning as w:
                   print(w)
                   break
                   pass


def best_ViBoolean_attribute(device_info):
    with niswitch.Session(device_info['name']) as session:
        session.interchange_check = False
        assert session.interchange_check is False
        session.interchange_check = True
        assert session.interchange_check is True


def test_ViString_attribute(device_info):
    with niswitch.Session(device_info['name']) as session:
        assert device_info['name'] == session.io_resource_descriptor


def test_ViInt32_attribute(device_info):
    with niswitch.Session(device_info['name']) as session:
        assert session.channel_count > 0


def test_ViReal64_attribute(device_info):
    with niswitch.Session(device_info['name']) as session:
        session.settling_time = 0.1
        assert session.settling_time == 0.1


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


def test_method_call_with_zero_parameter(device_info):
    with niswitch.Session(device_info['name']) as session:
        session.reset()
        pass


def test_method_call_with_one_parameter(device_info):
    with niswitch.Session(device_info['name']) as session:
        session.get_channel_name(1)


def test_invalid_method_call(device_info):
    #calling a function, without parameter, But it has a mandate parameter
    with niswitch.Session(device_info['name']) as session:
        try:
            session.get_channel_name()
            assert False
        except TypeError as e:
            print (e)
            pass


def test_method_call_with_two_parameter(device_info):
    # Calling Configure Trigger function and asserting True if any error occurred while function call.
    with niswitch.Session(device_info['name']) as session:
        try:
            session.can_connect(session.get_channel_name(1), session.get_channel_name(2))
        except niswitch.Error as e:
            print (e)
            assert True


def test_library_singleton(device_info):
    with niswitch.Session(device_info['name']) as session:
        lib1 = session.library
    with niswitch.Session(device_info['name']) as session:
        lib2 = session.library
    assert lib1 == lib2


def test_method_with_noinput_nooutput(device_info):
    with niswitch.Session(device_info['name']) as session:
        assert session.reset_with_defaults() == None


def best_method_with_enum_output_type_method(device_info):
    with niswitch.Session(device_info['name']) as session:
        #will have to update after https://github.com/ni/nimi-python/issues/128 fixed
        assert session.read_status()[1] == 4


def test_writeonly_attribute(device_info):
    with niswitch.Session(device_info['name']) as session:
        try:
            session.channel_count = 5
        except niswitch.Error as e:
            assert e.code == -1074135027 #Error : Attribute is read-only.


def test_string_functions(device_info):
    with niswitch.Session(device_info['name']) as session:
        result, message = session.self_test()
        assert result == 0
        assert len(message) > 1
        channel1 = session.get_channel_name(1)
        for x in range (2, session.channel_count):
            channel2 = session.get_channel_name(x)
            if session.can_connect(channel1, channel2) == 1: #path available
                path = session.get_path(channel1, channel2)
                assert len(path) > 1
                break
        
        
        
