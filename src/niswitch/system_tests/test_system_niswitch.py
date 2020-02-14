#!/usr/bin/python

import datetime
import fasteners
import niswitch
import os
import pytest
import tempfile


# We need a lock file so multiple tests aren't hitting the db at the same time
# daqmx_sim_db_lock_file = os.path.join(tempfile.gettempdir(), 'daqmx_db.lock')
# daqmx_sim_db_lock = fasteners.InterProcessLock(daqmx_sim_db_lock_file)


@pytest.fixture(scope='function')
def session():
    with niswitch.Session('', '2737/2-Wire 4x64 Matrix', True, True) as simulated_session:
        yield simulated_session


# @pytest.fixture(scope='function')
# def session_2532_1():
#     with daqmx_sim_db_lock:
#         simulated_session = niswitch.Session('', '2532/1-Wire 4x128 Matrix', True, False)
#     yield simulated_session
#     with daqmx_sim_db_lock:
#         simulated_session.close()


@pytest.fixture(scope='function')
def session_2532():
    with niswitch.Session('', '2532/1-Wire 4x128 Matrix', True, False) as simulated_session:
        yield simulated_session


# Basic Use Case Tests
def test_relayclose(session):
    relay_name = 'kr0c0'
    assert session.get_relay_position(relay_name) == niswitch.RelayPosition.OPEN
    session.relay_control(relay_name, niswitch.RelayAction.CLOSE)
    assert session.get_relay_position(relay_name) == niswitch.RelayPosition.CLOSED
    relay_count = session.get_relay_count(relay_name)
    assert relay_count == 0


def test_channel_connection(session):
    channel1 = 'c0'
    channel2 = 'r0'
    assert session.can_connect(channel1, channel2) == niswitch.PathCapability.PATH_AVAILABLE
    session.connect(channel1, channel2)
    session.wait_for_debounce()
    assert session.is_debounced is True
    assert session.can_connect(channel1, channel2) == niswitch.PathCapability.PATH_EXISTS
    session.disconnect(channel1, channel2)
    assert session.can_connect(channel1, channel2) == niswitch.PathCapability.PATH_AVAILABLE
    session.connect(channel1, channel2)
    assert session.can_connect(channel1, channel2) == niswitch.PathCapability.PATH_EXISTS
    session.disconnect_all()
    assert session.can_connect(channel1, channel2) == niswitch.PathCapability.PATH_AVAILABLE


def test_continuous_software_scanning(session_2532):
    scan_list = 'r0->c0; r1->c1'
    session_2532.scan_list = scan_list
    assert session_2532.scan_list == scan_list
    session_2532.route_scan_advanced_output(niswitch.ScanAdvancedOutput.FRONTCONNECTOR, niswitch.ScanAdvancedOutput.NONE)
    session_2532.route_trigger_input(niswitch.TriggerInput.FRONTCONNECTOR, niswitch.TriggerInput.TTL0)
    session_2532.trigger_input = niswitch.TriggerInput.SOFTWARE_TRIG
    session_2532.scan_advanced_output = niswitch.ScanAdvancedOutput.NONE
    session_2532.scan_list = scan_list
    session_2532.scan_mode = niswitch.ScanMode.BREAK_BEFORE_MAKE
    session_2532.continuous_scan = True
    session_2532.commit()
    with session_2532.initiate():
        assert session_2532.is_scanning is True
        session_2532.send_software_trigger()
        try:
            session_2532.wait_for_scan_complete()
            assert False
        except niswitch.Error as e:
            assert e.code == -1074126826  # Error : Max time exceeded.


# Attribute Tests
# No R/W non-IVI boolean attributes on all devices
'''
def test_vi_boolean_attribute(session):
    session.power_down_latching_relays_after_debounce = False
    assert session.power_down_latching_relays_after_debounce is False
    session.power_down_latching_relays_after_debounce = True
    assert session.power_down_latching_relays_after_debounce is True
'''


def test_vi_string_attribute(session):
    assert 'NI PXIe-2737' == session.instrument_model


def test_vi_int32_attribute(session):
    assert session.channel_count == 68


def test_vi_real64_attribute(session):
    session.settling_time = datetime.timedelta(seconds=0.1)
    assert session.settling_time.total_seconds() == 0.1


def test_enum_attribute(session_2532):
    assert session_2532.scan_mode == niswitch.ScanMode.BREAK_BEFORE_MAKE


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


def test_functions_self_test(session):
    # We should not get an assert if self_test passes
    session.self_test()


def test_functions_get_path(session):
    channel1 = 'r0'
    channel2 = 'c0'
    session.connect(channel1, channel2)
    path = session.get_path(channel1, channel2)
    assert path == 'r0->c0'
    session.disconnect(channel1, channel2)
    session.set_path(path)


def test_functions_connect_disconnect_multiple(session):
    session.connect_multiple('c0->r0, c0->r1')   # expect no errors
    session.disconnect_multiple('c0->r0, c0->r1')   # expect no errors


def test_functions_disable(session):
    channel1 = 'c0'
    channel2 = 'r0'
    session.connect(channel1, channel2)
    session.disable()   # expect no errors
    assert session.can_connect(channel1, channel2) == niswitch.PathCapability.PATH_AVAILABLE


def test_error_message():
    try:
        # We pass in an invalid model name to force going to error_message
        with niswitch.Session('', 'Invalid Topology', True, True):
            assert False
    except niswitch.Error as e:
        assert e.code == -1074118654
        assert e.description.find('Invalid resource name.') != -1


