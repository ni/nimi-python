#!/usr/bin/python

import datetime
import fasteners
import niscope
import nitclk
import os
import pytest
import tempfile

# nitclk does not work with session based simulated devices.
# As a workaround, the nimi-bot VMs are configured with two persistently simulated PXIe-5122 instruments named
# "5122_1" and "5122_2". If you want to run these tests on your own system, you will need to create these two
# simulated instruments.
# In addition, we need a global lock in order to keep us from opening more than one session to the same simulated instrument
# at the same time. This is because NI-SCOPE (like other MI driver runtimes) disallow two simultaneous sessions to the same
# instrument, even when the instrument is simulated. This will impact the performance at which system tests run because we
# parallelize at the tox level :(.
daqmx_sim_5122_1_lock_file = os.path.join(tempfile.gettempdir(), 'daqmx_5122_1.lock')
daqmx_sim_5122_1_lock = fasteners.InterProcessLock(daqmx_sim_5122_1_lock_file)
daqmx_sim_5122_2_lock_file = os.path.join(tempfile.gettempdir(), 'daqmx_5122_2.lock')
daqmx_sim_5122_2_lock = fasteners.InterProcessLock(daqmx_sim_5122_2_lock_file)


@pytest.fixture(scope='function')
def session_5122_1():
    with daqmx_sim_5122_1_lock:
        with niscope.Session('5124') as simulated_session:
            yield simulated_session


@pytest.fixture(scope='function')
def session_multiple_sessions():
    with daqmx_sim_5122_1_lock, daqmx_sim_5122_2_lock:
        with niscope.Session('5122_1') as simulated_session_5122_1, niscope.Session('5122_2') as simulated_session_5122_2:
            yield [simulated_session_5122_1, simulated_session_5122_2]


def test_nitclk_integration(session_5122_1):
    assert type(session_5122_1.tclk) == nitclk.SessionReference


def test_nitclk_vi_string(session_5122_1):
    # default is empty string
    assert session_5122_1.tclk.exported_tclk_output_terminal == ''
    session_5122_1.tclk.exported_tclk_output_terminal = 'PXI_Trig0'
    assert session_5122_1.tclk.exported_tclk_output_terminal == 'PXI_Trig0'


def test_nitclk_session_reference(session_5122_1):
    test_session = niscope.Session('FakeDevice', False, True, 'Simulate=1, DriverSetup=Model:5164; BoardType:PXIe')
    session_5122_1.tclk.ref_trigger_master_session = test_session
    # We need to look at the actual session number inside the class
    # we know the type returned from session.tclk.pause_trigger_master_session will be nitclk.SessionReference
    # This test assumes knowledge of the class internals
    assert session_5122_1.tclk.ref_trigger_master_session._session_number == test_session.tclk._get_tclk_session_reference()
    assert session_5122_1.tclk.ref_trigger_master_session._session_number == test_session._vi


def test_nitclk_vi_real64(session_5122_1):
    # default is 0
    assert session_5122_1.tclk.sample_clock_delay.total_seconds() == 0
    test_number = 4.2
    session_5122_1.tclk.sample_clock_delay = test_number
    assert session_5122_1.tclk.sample_clock_delay.total_seconds() == test_number


def test_nitclk_error_handling():
    test_session_reference = nitclk.SessionReference(42)  # Invalid session
    try:
        test_session_reference.exported_tclk_output_terminal = 'test'
        assert False
    except nitclk.errors.DriverError as e:
        assert e.code == -250032


def test_nitclk_configure_for_homogeneous_triggers(session_multiple_sessions):
    nitclk.configure_for_homogeneous_triggers(session_multiple_sessions)


def test_nitclk_sync_pulse_sender_synchronize(session_multiple_sessions):
    nitclk.configure_for_homogeneous_triggers(session_multiple_sessions)
    nitclk.setup_for_sync_pulse_sender_synchronize(session_multiple_sessions, .001)
    nitclk.synchronize_to_sync_pulse_sender(session_multiple_sessions, .001)
    nitclk.finish_sync_pulse_sender_synchronize(session_multiple_sessions, .001)


def test_nitclk_synchronize(session_multiple_sessions):
    nitclk.configure_for_homogeneous_triggers(session_multiple_sessions)
    nitclk.synchronize(session_multiple_sessions, .001)


def test_nitclk_initiate(session_multiple_sessions):
    nitclk.configure_for_homogeneous_triggers(session_multiple_sessions)
    nitclk.synchronize(session_multiple_sessions, .001)
    nitclk.initiate(session_multiple_sessions)


def test_nitclk_is_done(session_multiple_sessions):
    nitclk.configure_for_homogeneous_triggers(session_multiple_sessions)
    nitclk.synchronize(session_multiple_sessions, .001)
    nitclk.initiate(session_multiple_sessions)
    nitclk.is_done(session_multiple_sessions)


def test_nitclk_wait_until_done(session_multiple_sessions):
    nitclk.configure_for_homogeneous_triggers(session_multiple_sessions)
    nitclk.synchronize(session_multiple_sessions, .001)
    nitclk.initiate(session_multiple_sessions)
    nitclk.wait_until_done(session_multiple_sessions, .001)





