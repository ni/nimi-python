#!/usr/bin/python

import niswitch
import pytest


@pytest.fixture(scope='function')
def session():
    with niswitch.Session('', False, True, 'Simulate=1, DriverSetup=topology:2737/2-Wire 4x64 Matrix') as simulated_session:
        yield simulated_session


# Basic Use Case Tests
def test_relayclose(session):
    relay_name = 'kr0c0'
    assert session.get_relay_position(relay_name) == niswitch.RelayPosition.OPEN
    session.relay_control(relay_name, niswitch.RelayAction.CLOSE_RELAY)
    assert session.get_relay_position(relay_name) == niswitch.RelayPosition.CLOSED
    assert relay_name


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


# Attribute Tests
def test_viboolean_attribute(session):
    session.interchange_check = False
    assert session.interchange_check is False
    session.interchange_check = True
    assert session.interchange_check is True


def test_vistring_attribute(session):
    assert 'NI PXIe-2737' == session.instrument_model


def test_viint32_attribute(session):
    assert session.channel_count > 0


def test_rireal64_attribute(session):
    session.settling_time = 0.1
    assert session.settling_time == 0.1


def test_enum_attribute():
    with niswitch.Session('', False, True, 'Simulate=1, DriverSetup=topology:2532/1-Wire 4x128 Matrix') as session:
        assert session.scan_mode == niswitch.ScanMode.BREAK_BEFORE_MAKE


def test_writeonly_attribute(session):
    try:
        session.channel_count = 5
    except niswitch.Error as e:
        assert e.code == -1074135027  # Error : Attribute is read-only.


# Function Tests
def test_method_reset(session):
    session.reset()


def test_method_set_path(session):
    session.set_path('r0->c0')


def test_method_can_connect(session):
    try:
        session.can_connect('r0', 'r1')
    except niswitch.Error as e:
        pass


def test_method_reset_with_defaults(session):
    assert session.reset_with_defaults() is None


def test_functions_get_relay_name(session):
    string = session.get_relay_name(1)
    assert len(string) > 1
    assert string == 'kr0c0'


def test_functions_get_channel_name(session):
    string = session.get_channel_name(1)
    assert len(string) > 1
    assert string == 'r0'


def test_functions_revision_query(session):
    string1, string2 = session.revision_query()
    assert len(string1) > 1
    assert string1 == 'Driver: NI-SWITCH for SwitchCA4 Device Support 17.0.0, Compiler: MSVC 9.00'
    assert len(string2) > 1
    assert string2 == 'No revision information available'


def test_functions_get_next_coercion_record(session):
    string = session.get_next_coercion_record()
    assert len(string) == 0


def test_functions_get_next_interchange_warning(session):
    string = session.get_next_interchange_warning()
    assert len(string) == 0


def test_functions_self_test(session):
    result, string = session.self_test()
    assert result == 0
    assert len(string) > 1
    assert string == 'No Error'


def test_functions_get_path(session):
    channel1 = 'r0'
    channel2 = 'c0'
    session.connect(channel1, channel2)
    string = session.get_path(channel1, channel2)
    assert len(string) > 1
    assert string == 'r0->c0'
    session.disconnect(channel1, channel2)
    session.set_path(string)


def test_functions_error_query(session):
    try:
        result, string = session.error_query()
        assert 0
    except niswitch.Warning as w:  # NI-SWITCH does not support error_query and throws a warning
        pass


def test_functions_error_message(session):
    string = session.error_message(-1074126847)
    assert len(string) > 1
    assert string == 'Invalid path string.'


def test_functions_get_error_description(session):
    string = session.get_error_description(0)   # expect no errors
    assert string == ''
