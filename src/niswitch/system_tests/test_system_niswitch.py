#!/usr/bin/python

import fasteners
import grpc
import hightime
import niswitch
import os
import pathlib
import pytest
import subprocess
import tempfile
import time

# We need a lock file so multiple tests aren't hitting the db at the same time
# Trying to create simulated DAQmx devices at the same time (which can happen when running
# tox with --parallel N, or when two different drivers are being tested at the same time on
# the same machine, can result in an internal error:
# -2147220733: MAX:  (Hex 0x80040303) Internal error: The requested object was not found in
# the configuration database. Please note the steps you performed that led to this error and
# contact technical support at http://ni.com/support.
# This is filed as internal bug 255545
daqmx_sim_db_lock_file = os.path.join(tempfile.gettempdir(), 'daqmx_db.lock')
daqmx_sim_db_lock = fasteners.InterProcessLock(daqmx_sim_db_lock_file)


class SystemTests:
    @pytest.fixture(scope='function')
    def session(self, session_creation_kwargs):
        with niswitch.Session('', '2737/2-Wire 4x64 Matrix', True, True, **session_creation_kwargs) as simulated_session:
            yield simulated_session

    @pytest.fixture(scope='function')
    def session_2532(self, session_creation_kwargs):
        with daqmx_sim_db_lock:
            simulated_session = niswitch.Session('', '2532/1-Wire 4x128 Matrix', True, False, **session_creation_kwargs)
        yield simulated_session
        with daqmx_sim_db_lock:
            simulated_session.close()

    # Basic Use Case Tests
    def test_relayclose(self, session):
        relay_name = 'kr0c0'
        assert session.get_relay_position(relay_name) == niswitch.RelayPosition.OPEN
        session.relay_control(relay_name, niswitch.RelayAction.CLOSE)
        assert session.get_relay_position(relay_name) == niswitch.RelayPosition.CLOSED
        relay_count = session.get_relay_count(relay_name)
        assert relay_count == 0

    def test_channel_connection(self, session):
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

    @pytest.mark.skip(reason="TODO(sbethur): Intermittent failures, GitHub issue #1622.")
    def test_continuous_software_scanning(self, session_2532):
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

    def test_vi_string_attribute(self, session):
        assert 'NI PXIe-2737' == session.instrument_model

    def test_vi_int32_attribute(self, session):
        assert session.channel_count == 68

    def test_vi_real64_attribute(self, session):
        session.settling_time = hightime.timedelta(seconds=0.1)
        assert session.settling_time.total_seconds() == 0.1

    @pytest.mark.skip(reason="TODO(sbethur): Intermittent failures, GitHub issue #1622.")
    def test_enum_attribute(self, session_2532):
        assert session_2532.scan_mode == niswitch.ScanMode.BREAK_BEFORE_MAKE

    def test_write_only_attribute(self, session):
        try:
            session.channel_count = 5
            assert False
        except niswitch.Error as e:
            assert e.code == -1074135027  # Error : Attribute is read-only.

    # Function Tests
    def test_method_reset(self, session):
        session.reset()

    def test_method_set_path(self, session):
        session.set_path('r0->c0')

    def test_method_can_connect(self, session):
        path_capability = session.can_connect('r0', 'r1')
        assert path_capability == niswitch.PathCapability.PATH_UNSUPPORTED

    def test_method_reset_with_defaults(self, session):
        assert session.reset_with_defaults() is None

    def test_functions_get_relay_name(self, session):
        relay_name = session.get_relay_name(1)
        assert relay_name == 'kr0c0'

    def test_functions_get_channel_name(self, session):
        channel_name = session.get_channel_name(1)
        assert channel_name == 'r0'

    def test_functions_self_test(self, session):
        # We should not get an assert if self_test passes
        session.self_test()

    def test_locks_are_reentrant(self, session):
        with session.lock():
            with session.lock():
                # We should not get an assert if self_test passes
                session.self_test()

    def test_functions_get_path(self, session):
        channel1 = 'r0'
        channel2 = 'c0'
        session.connect(channel1, channel2)
        path = session.get_path(channel1, channel2)
        assert path == 'r0->c0'
        session.disconnect(channel1, channel2)
        session.set_path(path)

    def test_functions_connect_disconnect_multiple(self, session):
        session.connect_multiple('c0->r0, c0->r1')   # expect no errors
        session.disconnect_multiple('c0->r0, c0->r1')   # expect no errors

    def test_functions_disable(self, session):
        channel1 = 'c0'
        channel2 = 'r0'
        session.connect(channel1, channel2)
        session.disable()   # expect no errors
        assert session.can_connect(channel1, channel2) == niswitch.PathCapability.PATH_AVAILABLE

    def test_error_message(self, session_creation_kwargs):
        try:
            # We pass in an invalid model name to force going to error_message
            with niswitch.Session('', 'Invalid Topology', True, True, **session_creation_kwargs):
                assert False
        except niswitch.Error as e:
            assert e.code == -1074118654
            assert e.description.find('Invalid resource name.') != -1


class TestLibrary(SystemTests):
    @pytest.fixture(scope='class')
    def session_creation_kwargs(self):
        return {}


class TestGrpc(SystemTests):
    server_address = "localhost"
    server_port = "31763"

    def _get_grpc_server_exe(self):
        if os.name != "nt":
            pytest.skip("Only supported on Windows")
        import winreg
        try:
            reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
            read64key = winreg.KEY_READ | winreg.KEY_WOW64_64KEY
            with winreg.OpenKey(reg, r"SOFTWARE\National Instruments\Common\Installer", access=read64key) as key:
                shared_dir, _ = winreg.QueryValueEx(key, "NISHAREDDIR64")
        except OSError:
            pytest.skip("NI gRPC Device Server not installed")
        server_exe = pathlib.Path(shared_dir) / "NI gRPC Device Server" / "ni_grpc_device_server.exe"
        if not server_exe.exists():
            pytest.skip("NI gRPC Device Server not installed")
        return server_exe

    @pytest.fixture(scope='class')
    def grpc_channel(self):
        # TODO(DavidCurtiss): Remove the next 3 lines once (and the above method) the server is started automatically
        server_exe = self._get_grpc_server_exe()
        proc = subprocess.Popen([str(server_exe)])
        time.sleep(3)
        try:
            channel = grpc.insecure_channel(f"{self.server_address}:{self.server_port}")
            yield channel
        finally:
            proc.kill()

    @pytest.fixture(scope='class')
    def session_creation_kwargs(self, grpc_channel):
        grpc_options = niswitch.GrpcSessionOptions(grpc_channel, "")
        return {'_grpc_options': grpc_options}
