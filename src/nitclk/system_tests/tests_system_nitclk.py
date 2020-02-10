#!/usr/bin/python

import datetime
import fasteners
import niscope
import nitclk
import os
import pytest
import tempfile


# We need a lock file so multiple tests aren't hitting the simulated HW at the same time
daqmx_sim_5124_lock_file = os.path.join(tempfile.gettempdir(), 'daqmx_5124.lock')
daqmx_sim_5124_lock = fasteners.InterProcessLock(daqmx_sim_5124_lock_file)
daqmx_sim_5142_lock_file = os.path.join(tempfile.gettempdir(), 'daqmx_5142.lock')
daqmx_sim_5142_lock = fasteners.InterProcessLock(daqmx_sim_5142_lock_file)


@pytest.fixture(scope='function')
def session_5124():
    with daqmx_sim_5124_lock:
        with niscope.Session('5124') as simulated_session:
            yield simulated_session


@pytest.fixture(scope='function')
def session_multiple_sessions():
    with daqmx_sim_5124_lock, daqmx_sim_5142_lock:
        with niscope.Session('5124') as simulated_session_5124, niscope.Session('5142') as simulated_session_5142:
            yield [simulated_session_5124, simulated_session_5142]


def test_nitclk_integration(session_5124):
    assert type(session_5124.tclk) == nitclk.SessionReference


def test_nitclk_vi_string(session_5124):
    # default is empty string
    assert session_5124.tclk.exported_tclk_output_terminal == ''
    session_5124.tclk.exported_tclk_output_terminal = 'PXI_Trig0'
    assert session_5124.tclk.exported_tclk_output_terminal == 'PXI_Trig0'


def test_nitclk_session_reference(session_5124):
    test_session = niscope.Session('FakeDevice', False, True, 'Simulate=1, DriverSetup=Model:5164; BoardType:PXIe')
    session_5124.tclk.ref_trigger_master_session = test_session
    # We need to look at the actual session number inside the class
    # we know the type returned from session.tclk.pause_trigger_master_session will be nitclk.SessionReference
    # This test assumes knowledge of the class internals
    assert session_5124.tclk.ref_trigger_master_session._session_number == test_session.tclk._get_tclk_session_reference()
    assert session_5124.tclk.ref_trigger_master_session._session_number == test_session._vi


def test_nitclk_vi_real64(session_5124):
    # default is 0
    assert session_5124.tclk.sample_clock_delay == 0
    test_number = 4.2
    session_5124.tclk.sample_clock_delay = test_number
    assert session_5124.tclk.sample_clock_delay.total_seconds() == test_number


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
    session_multiple_sessions[0].tclk.sync_pulse_clock_source = 'PXI_CLK100'
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





