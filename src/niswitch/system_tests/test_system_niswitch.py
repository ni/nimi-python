#!/usr/bin/python

import niswitch
import pytest
import warnings


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
def test_vi_boolean_attribute(session):
    session.interchange_check = False
    assert session.interchange_check is False
    session.interchange_check = True
    assert session.interchange_check is True


def test_vi_string_attribute(session):
    assert 'NI PXIe-2737' == session.instrument_model


def test_vi_int32_attribute(session):
    assert session.channel_count == 68


def test_vi_real64_attribute(session):
    session.settling_time = 0.1
    assert session.settling_time == 0.1


def test_enum_attribute():
    with niswitch.Session('', False, True, 'Simulate=1, DriverSetup=topology:2532/1-Wire 4x128 Matrix') as session:
        assert session.scan_mode == niswitch.ScanMode.BREAK_BEFORE_MAKE


def test_write_only_attribute(session):
    try:
        session.channel_count = 5
        assert False
    except niswitch.Error as e:
        assert e.code == -1074135027  # Error : Attribute is read-only.


# Function Tests
def test_method_reset(session):
    session.reset()


def test_method_set_path(session):
    session.set_path('r0->c0')


def test_method_can_connect(session):
    path_capability = session.can_connect('r0', 'r1')
    assert path_capability == niswitch.PathCapability.PATH_UNSUPPORTED


def test_method_reset_with_defaults(session):
    assert session.reset_with_defaults() is None


def test_functions_get_relay_name(session):
    relay_name = session.get_relay_name(1)
    assert relay_name == 'kr0c0'


def test_functions_get_channel_name(session):
    channel_name = session.get_channel_name(1)
    assert channel_name == 'r0'


def test_functions_revision_query(session):
    string1, string2 = session.revision_query()
    assert string1.find('Driver: NI-SWITCH for SwitchCA4 Device Support') != -1
    assert string2 == 'No revision information available'


def test_functions_get_next_coercion_record(session):
    coercion_record = session.get_next_coercion_record()
    assert len(coercion_record) == 0


def test_functions_get_next_interchange_warning(session):
    interchange_warning = session.get_next_interchange_warning()
    assert len(interchange_warning) == 0


def test_functions_self_test(session):
    self_test_result, self_test_string = session.self_test()
    assert self_test_result == 0
    assert self_test_string == 'No Error'


def test_functions_get_path(session):
    channel1 = 'r0'
    channel2 = 'c0'
    session.connect(channel1, channel2)
    path = session.get_path(channel1, channel2)
    assert path == 'r0->c0'
    session.disconnect(channel1, channel2)
    session.set_path(path)


def test_functions_error_query(session):
    with warnings.catch_warnings(record=True) as w:
        test_error_desc = '1073479940'  # Error Query not supported.
        error_result, error_string = session.error_query()
        assert len(w) == 1
        assert issubclass(w[0].category, niswitch.NiswitchWarning)
        assert test_error_desc in str(w[0].message)


def test_functions_error_message(session):
    message = session.error_message(-1074126847)
    assert message == 'Invalid path string.'


def test_functions_get_error_description(session):
    description = session.get_error_description(0)   # expect no errors
    assert description == ''
