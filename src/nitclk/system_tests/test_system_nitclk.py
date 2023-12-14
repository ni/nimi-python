#!/usr/bin/python

import niscope
import nitclk
import pytest


@pytest.fixture(scope='function')
def single_niscope_session():
    with niscope.Session('', False, False, 'Simulate=1, DriverSetup=Model:5164;BoardType:PXIe') as simulated_session:
        yield simulated_session


@pytest.fixture(scope='function')
def multiple_niscope_sessions():
    with niscope.Session('', False, False, 'Simulate=1, DriverSetup=Model:5164;BoardType:PXIe') as simulated_session_1, niscope.Session('', False, False, 'Simulate=1, DriverSetup=Model:5164;BoardType:PXIe') as simulated_session_2:
        yield [simulated_session_1, simulated_session_2]


def test_nitclk_integration(single_niscope_session):
    assert isinstance(single_niscope_session.tclk, nitclk.SessionReference)


def test_nitclk_vi_string(single_niscope_session):
    # default is empty string
    assert single_niscope_session.tclk.exported_tclk_output_terminal == ''
    single_niscope_session.tclk.exported_tclk_output_terminal = 'PXI_Trig0'
    assert single_niscope_session.tclk.exported_tclk_output_terminal == 'PXI_Trig0'


def test_nitclk_session_reference(single_niscope_session):
    test_session = niscope.Session('FakeDevice', False, True, 'Simulate=1, DriverSetup=Model:5164; BoardType:PXIe')
    single_niscope_session.tclk.ref_trigger_master_session = test_session
    # We need to look at the actual session number inside the class
    # we know the type returned from session.tclk.pause_trigger_master_session will be nitclk.SessionReference
    # This test assumes knowledge of the class internals
    assert single_niscope_session.tclk.ref_trigger_master_session._interpreter._session_number == test_session.tclk._get_tclk_session_reference()
    assert single_niscope_session.tclk.ref_trigger_master_session._interpreter._session_number == test_session._interpreter._vi


def test_nitclk_vi_real64(single_niscope_session):
    # default is 0
    assert single_niscope_session.tclk.sample_clock_delay.total_seconds() == 0
    test_number = 4.2
    single_niscope_session.tclk.sample_clock_delay = test_number
    assert single_niscope_session.tclk.sample_clock_delay.total_seconds() == test_number


def test_nitclk_error_handling():
    test_session_reference = nitclk.SessionReference(42)  # Invalid session
    try:
        test_session_reference.exported_tclk_output_terminal = 'test'
        assert False
    except nitclk.errors.DriverError as e:
        assert e.code == -250032


def test_nitclk_configure_for_homogeneous_triggers(multiple_niscope_sessions):
    nitclk.configure_for_homogeneous_triggers(multiple_niscope_sessions)


def test_nitclk_sync_pulse_sender_synchronize(multiple_niscope_sessions):
    nitclk.configure_for_homogeneous_triggers(multiple_niscope_sessions)
    nitclk.setup_for_sync_pulse_sender_synchronize(multiple_niscope_sessions, .001)
    nitclk.synchronize_to_sync_pulse_sender(multiple_niscope_sessions, .001)
    nitclk.finish_sync_pulse_sender_synchronize(multiple_niscope_sessions, .001)


def test_nitclk_synchronize(multiple_niscope_sessions):
    nitclk.configure_for_homogeneous_triggers(multiple_niscope_sessions)
    nitclk.synchronize(multiple_niscope_sessions, .001)


def test_nitclk_initiate(multiple_niscope_sessions):
    nitclk.configure_for_homogeneous_triggers(multiple_niscope_sessions)
    nitclk.synchronize(multiple_niscope_sessions, .001)
    nitclk.initiate(multiple_niscope_sessions)


def test_nitclk_is_done(multiple_niscope_sessions):
    nitclk.configure_for_homogeneous_triggers(multiple_niscope_sessions)
    nitclk.synchronize(multiple_niscope_sessions, .001)
    nitclk.initiate(multiple_niscope_sessions)
    nitclk.is_done(multiple_niscope_sessions)


def test_nitclk_wait_until_done(multiple_niscope_sessions):
    nitclk.configure_for_homogeneous_triggers(multiple_niscope_sessions)
    nitclk.synchronize(multiple_niscope_sessions, .001)
    nitclk.initiate(multiple_niscope_sessions)
    nitclk.wait_until_done(multiple_niscope_sessions, .001)





