#!/usr/bin/python

import niswitch
import pytest


@pytest.fixture(scope='function')
def session():
    with niswitch.Session('', '2737/2-Wire 4x64 Matrix', True, True) as simulated_session:
        yield simulated_session


# Basic Use Case Tests
def test_relayclose(session):
    relay_name = 'kr0c0'
    assert session.get_relay_position(relay_name) == niswitch.RelayPosition.OPEN
    session.relay_control(relay_name, niswitch.RelayAction.CLOSE_RELAY)
    assert session.get_relay_position(relay_name) == niswitch.RelayPosition.CLOSED
    relay_count = session.get_relay_count(relay_name)
    assert relay_count == 0


def test_channel_connection(session):
    channel1 = 'c0'
    channel2 = 'r0'
    assert session.can_connect(channel1, channel2) == niswitch.PathCapability.PATH_AVAILABLE
    session.connect(channel1, channel2)
    session.wait_for_debounce()
    assert session.is_debounced() is True
    assert session.can_connect(channel1, channel2) == niswitch.PathCapability.PATH_EXISTS
    session.disconnect(channel1, channel2)
    assert session.can_connect(channel1, channel2) == niswitch.PathCapability.PATH_AVAILABLE
    session.connect(channel1, channel2)
    assert session.can_connect(channel1, channel2) == niswitch.PathCapability.PATH_EXISTS
    session.disconnect_all()
    assert session.can_connect(channel1, channel2) == niswitch.PathCapability.PATH_AVAILABLE


def test_continuous_software_scanning(session):
    with niswitch.Session('', '2532/1-Wire 4x128 Matrix', True, False) as session:
        scan_list = 'r0->c0; r1->c1'
        session.scan_list = scan_list
        assert session.scan_list == scan_list
        session.route_scan_advanced_output(niswitch.ScanAdvancedOutput.FRONTCONNECTOR, niswitch.ScanAdvancedOutput.NONE)
        session.route_trigger_input(niswitch.TriggerInput.FRONTCONNECTOR, niswitch.TriggerInput.PXI_TRIG0)
        session.configure_scan_list(scan_list, niswitch.ScanMode.BREAK_BEFORE_MAKE)
        session.configure_scan_trigger(niswitch.TriggerInput.SW_TRIG_FUNC, niswitch.ScanAdvancedOutput.NONE)
        session.set_continuous_scan(True)
        session.commit()
        with session.initiate():
            assert session.is_scanning() is True
            session.send_software_trigger()
            try:
                session.wait_for_scan_complete()
                assert False
            except niswitch.Error as e:
                assert e.code == -1074126826  # Error : Max time exceeded.


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
    with niswitch.Session('', '2532/1-Wire 4x128 Matrix', True, False) as session:
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


def test_functions_get_error_description(session):
    description = session.get_error_description(0)   # expect no errors
    assert description == ''


def test_functions_connect_disconnect_multiple(session):
    session.connect_multiple('c0->r0, c0->r1')   # expect no errors
    session.disconnect_multiple('c0->r0, c0->r1')   # expect no errors


def test_functions_disable(session):
    channel1 = 'c0'
    channel2 = 'r0'
    session.connect(channel1, channel2)
    session.disable()   # expect no errors
    assert session.can_connect(channel1, channel2) == niswitch.PathCapability.PATH_AVAILABLE


def test_error_message(session):
    # Testing a private function, as there is no way to natively get to this function on a simulated session.
    message = session._error_message(-1074135027)
    assert message == 'IVI:  (Hex 0xBFFA000D) Attribute is read-only.'
