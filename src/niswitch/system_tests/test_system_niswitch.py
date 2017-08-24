#!/usr/bin/python

import niswitch
import pytest
import nimodinst
import re

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


def test_invalid_device_name():
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
        position_initial = session.get_relay_position(relayName)
        if position_initial == 10: # if relay is open, close relay
            session.relay_control(relayName, 21)
        else:
            session.relay_control(relayName, 20)
        position_middle = session.get_relay_position(relayName)
        if position_middle == 10: # if relay is open, close relay
            session.relay_control(relayName, 21)
        else:
            session.relay_control(relayName, 20)
        position_final = session.get_relay_position(relayName)
        assert relayName
        assert position_initial != position_middle
        assert position_middle != position_final
        assert position_initial == position_final


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
               break


def test_wrong_parameter_type(device_info):
    with niswitch.Session(device_info['name']) as session:
        string1, string2 = session.revision_query()
        assert len(string1) > 1
        if string1.lower().find('ca4') != -1 : #skip if it says CA4 as enums are not supported
            pytest.skip("No Enums in functions yet.")
        else:
            try:
                # We are passing a number where an enum is expected.
                session.trigger_input(1)
                assert False
            except TypeError as e:
                print(e)


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


def test_ViBoolean_attribute(device_info):
#    with niswitch.Session(device_info['name']) as session:
#        session.interchange_check = False
#        assert session.interchange_check is False
#        session.interchange_check = True
#        assert session.interchange_check is True
      pytest.skip("Issue 144")


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


def test_Enum_attribute(device_info):
    with niswitch.Session(device_info['name']) as session:
        string1, string2 = session.revision_query()
        assert len(string1) > 1
        if string1.lower().find('ca4') != -1 : #skip if it says CA4 as enums are not supported
            pytest.skip("No Enums in functions yet.")
        else:
           session.scan_mode = niswitch.ScanMode.NONE
           assert session.scan_mode == niswitch.ScanMode.NONE
           assert type(session.scan_mode) is niswitch.ScanMode
           try:
               session.scan_mode = niswitch.TriggerInput.IMMEDIATE
               assert False
           except TypeError as e:
               print(e)


def test_method_call_with_zero_parameter(device_info):
    with niswitch.Session(device_info['name']) as session:
        session.reset()


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


def test_method_with_enum(device_info):
    with niswitch.Session(device_info['name']) as session:
        #will have to update after https://github.com/ni/nimi-python/issues/128 fixed
        #session.configure_scan_trigger(0.01, niswitch.TriggerInput.IMMEDIATE, niswitch.ScanAdvancedOutput.NONE)
        pytest.skip("No Enums in functions yet.")


def test_writeonly_attribute(device_info):
    with niswitch.Session(device_info['name']) as session:
        try:
            session.channel_count = 5
        except niswitch.Error as e:
            assert e.code == -1074135027 #Error : Attribute is read-only.


def test_functions_addon_string_changes_get_relay_name(device_info):
    with niswitch.Session(device_info['name']) as session:
        string = session.get_relay_name(1)
        assert len(string) > 1
        pattern = r'[a-z][0-9]'
        assert re.search(pattern, string.lower()) != None #string should contain something like "k0" or "kb0c0"


def test_functions_addon_string_changes_get_channel_name(device_info):
    with niswitch.Session(device_info['name']) as session:
        string = session.get_channel_name(1)
        assert len(string) > 1
        pattern = r'[a-z][0-9]'
        assert re.search(pattern, string.lower()) != None #string should contain something like "c0" or "ch0"



def test_functions_addon_string_changes_revision_query(device_info):
    with niswitch.Session(device_info['name']) as session:
        string1, string2 = session.revision_query()
        assert len(string1) > 1
        assert string1.lower().find('switch') != -1 #string should contain the name of the driver somewhere
        assert len(string2) > 1
        assert string2.lower().find('revision') != -1 #string should contain that there is no revision information


def test_functions_addon_string_changes_get_next_coercion_record(device_info):
    with niswitch.Session(device_info['name']) as session:
        string = session.get_next_coercion_record()
        assert len(string) == 0


def test_functions_addon_string_changes_get_next_interchange_warning(device_info):
    with niswitch.Session(device_info['name']) as session:
        string = session.get_next_interchange_warning()
        assert len(string) == 0


def test_functions_addon_string_changes_self_test(device_info):
    with niswitch.Session(device_info['name']) as session:
        result, string = session.self_test()
        assert result == 0
        assert len(string) > 1
        assert (string.lower().find('pass') != -1) | (string.lower().find('no error') != -1) #self test should return the word pass somewhere for real devices and "no error" for simulated


def test_functions_addon_string_changes_get_path(device_info):
    with niswitch.Session(device_info['name']) as session:
        channel1 = session.get_channel_name(1)
        for x in range (2, session.channel_count):
            channel2 = session.get_channel_name(x)
            if session.can_connect(channel1, channel2) == 1: #path available
                session.connect(channel1, channel2)
                string = session.get_path(channel1, channel2)
                assert len(string) > 1
                assert string.find('->') != -1   #path should contain -> as in "c0->r0"
                session.disconnect(channel1, channel2)
                session.set_path(string)
                break


def test_functions_addon_string_changes_error_query(device_info):
    with niswitch.Session(device_info['name']) as session:
        string1, string2 = session.revision_query()
        assert len(string1) > 1
        if string1.lower().find('ca4') != -1 : #skip if it says CA4 as this is not supported
            pytest.skip("No Enums in functions yet.")
        else:
            try:
                result, string = session.error_query()
            except niswitch.Warning as w: #NI-SWITCH does not support error_query and throws a warning
                print(w)


def test_functions_addon_string_changes_error_message(device_info):
    with niswitch.Session(device_info['name']) as session:
        string = session.error_message(-1074126847)
        assert len(string) > 1
        assert string.lower().find('invalid') != -1  #should return invalid path string
        
def test_functions_addon_string_changes_private_get_error_description(device_info):
    with niswitch.Session(device_info['name']) as session:
        error, string = session._get_error_description(0)   #expect no errors
        assert error == 0
        assert string == ''