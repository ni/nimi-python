#!/usr/bin/python

import niswitch
import pytest
import re

@pytest.fixture(scope='function')
def session():
    with niswitch.Session('', False, True, 'Simulate=1, DriverSetup=topology:2737/2-Wire 4x64 Matrix') as simulated_session:
        yield simulated_session


def test_invalid_device_name():
    try:
        niswitch.Session("Foo!")
        assert False
    except niswitch.Error as e:
        assert e.code == -1074118654
        assert e.description.find("Invalid resource name.") != -1
        assert e.description.find("Foo!") != -1


def test_relayclose(session):
    relayName = 'kr0c0'
    assert session.get_relay_position(relayName) == niswitch.RelayPosition.OPEN
    session.relay_control(relayName, niswitch.RelayAction.CLOSE_RELAY)
    assert session.get_relay_position(relayName) == niswitch.RelayPosition.CLOSED
    assert relayName


def test_channel_connection(session):
    channel1 = 'c0'
    channel2 = 'r0'
    assert session.can_connect(channel1, channel2) == niswitch.PathCapability.PATH_AVAILABLE
    session.connect(channel1, channel2)
    assert session.can_connect(channel1, channel2) == niswitch.PathCapability.PATH_EXISTS
    session.disconnect(channel1, channel2)
    assert session.can_connect(channel1, channel2) == niswitch.PathCapability.PATH_AVAILABLE
    session.connect(channel1, channel2)
    assert session.can_connect(channel1, channel2) == niswitch.PathCapability.PATH_EXISTS
    session.disconnect_all()
    assert session.can_connect(channel1, channel2) == niswitch.PathCapability.PATH_AVAILABLE


def test_wrong_parameter_type(session):
    relayName = 'kr0c0'
    try:
        session.relay_control(relayName, 10)
        assert False
    except TypeError as e:
        print(e)
        pass


def test_warning(session):
    channel1 = 'r0'
    channel2 = 'c0'
    session.connect(channel1, channel2)
    try:
        session.can_connect(channel1, channel2)
    except niswitch.Warning as w:
        print(w)


def test_ViBoolean_attribute(session):
    session.interchange_check = False
    assert session.interchange_check is False
    session.interchange_check = True
    assert session.interchange_check is True


def test_ViString_attribute(session):
    assert 'NI PXIe-2737' == session.instrument_model


def test_ViInt32_attribute(session):
    assert session.channel_count > 0


def test_ViReal64_attribute(session):
    session.settling_time = 0.1
    assert session.settling_time == 0.1


def test_Enum_attribute():
    with niswitch.Session('', False, True, 'Simulate=1, DriverSetup=topology:2532/1-Wire 4x128 Matrix') as session:
        assert session.scan_mode == niswitch.ScanMode.BREAK_BEFORE_MAKE

def test_method_call_with_zero_parameter(session):
    session.reset()


def test_method_call_with_one_parameter(session):
    session.set_path('r0->c0')


def test_invalid_method_call(session):
    #calling a function, without parameter, But it has a mandate parameter
    try:
        session.get_channel_name()
        assert False
    except TypeError as e:
        print (e)


def test_method_call_with_two_parameter(session):
    try:
        session.can_connect('r0', 'r1')
    except niswitch.Error as e:
        print (e)
        assert True


def test_library_singleton():
    with niswitch.Session('', False, True, 'Simulate=1, DriverSetup=topology:2737/2-Wire 4x64 Matrix') as session:
        lib1 = session.library
    with niswitch.Session('', False, True, 'Simulate=1, DriverSetup=topology:2737/2-Wire 4x64 Matrix') as session:
       lib2 = session.library
    assert lib1 == lib2


def test_method_with_noinput_nooutput(session):
    assert session.reset_with_defaults() == None


def test_writeonly_attribute(session):
    try:
        session.channel_count = 5
    except niswitch.Error as e:
        assert e.code == -1074135027 #Error : Attribute is read-only.


def test_functions_addon_string_changes_get_relay_name(session):
    string = session.get_relay_name(1)
    assert len(string) > 1
    assert string == 'kr0c0'


def test_functions_addon_string_changes_get_channel_name(session):
    string = session.get_channel_name(1)
    assert len(string) > 1
    assert string == 'r0'



def test_functions_addon_string_changes_revision_query(session):
    string1, string2 = session.revision_query()
    assert len(string1) > 1
    assert string1 == 'Driver: NI-SWITCH for SwitchCA4 Device Support 17.0.0, Compiler: MSVC 9.00'
    assert len(string2) > 1
    assert string2 == 'No revision information available'


def test_functions_addon_string_changes_get_next_coercion_record(session):
    string = session.get_next_coercion_record()
    assert len(string) == 0


def test_functions_addon_string_changes_get_next_interchange_warning(session):
    string = session.get_next_interchange_warning()
    assert len(string) == 0


def test_functions_addon_string_changes_self_test(session):
    result, string = session.self_test()
    assert result == 0
    assert len(string) > 1
    assert string == 'No Error'


def test_functions_addon_string_changes_get_path(session):
    channel1 = 'r0'
    channel2 = 'c0'
    session.connect(channel1, channel2)
    string = session.get_path(channel1, channel2)
    assert len(string) > 1
    assert string == 'r0->c0'
    session.disconnect(channel1, channel2)
    session.set_path(string)


def test_functions_addon_string_changes_error_query(session):
    try:
        result, string = session.error_query()
        assert 0
    except niswitch.Warning as w: #NI-SWITCH does not support error_query and throws a warning
        print(w)


def test_functions_addon_string_changes_error_message(session):
    string = session.error_message(-1074126847)
    assert len(string) > 1
    assert string == 'Invalid path string.'


def test_functions_addon_string_changes_private_get_error_description(session):
    error, string = session._get_error_description(0)   #expect no errors
    assert error == 0
    assert string == ''