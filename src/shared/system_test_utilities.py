import os
import pathlib
import pytest
import subprocess
import threading
import time


class GrpcServerProcess:
    def __init__(self):
        server_exe = self._get_grpc_server_exe()
        self._proc = subprocess.Popen([str(server_exe)], stdout=subprocess.PIPE)

        # Read/parse first line of output; discard the rest
        try:
            first_line = self._proc.stdout.readline()
            assert first_line.startswith(b"Server listening on port "), f"Unrecognized output: {first_line}"
            self.server_port = int(first_line.replace(b"Server listening on port ", b"").strip())

            self._stdout_thread = threading.Thread(target=self._discard_output, args=(self._proc.stdout,), daemon=True)
            self._stdout_thread.start()
        except Exception:
            self._proc.kill()
            raise

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._proc.kill()

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

    def _discard_output(self, stdout):
        while True:
            data = stdout.read(8196)
            if not data:
                return


def impl_test_multi_threading_lock_unlock(session):
    t1_lock_engaged = threading.Event()
    release_t1_lock = threading.Event()

    def lock_wait_unlock():
        session.lock()
        t1_lock_engaged.set()
        assert session.instrument_manufacturer != ''
        release_t1_lock.wait()
        session.unlock()

    def lock_unlock():
        session.lock()
        assert session.instrument_model != ''
        session.unlock()

    # test that lock, unlock functions work properly
    t1 = threading.Thread(target=lock_wait_unlock)
    t2 = threading.Thread(target=lock_unlock)

    t1.start()
    t2.start()

    t1_lock_engaged.wait()
    time.sleep(2.0)
    # t1 is blocked by the release event, t2 should be blocked by t1's lock
    assert t2.is_alive()
    release_t1_lock.set()
    t2.join()

    assert not t1.is_alive()
    assert not t2.is_alive()

def impl_test_multi_threading_ivi_synchronized_wrapper_releases_lock(ivi_method_to_call):
    # test that the 2nd thread doesn't hang
    t1 = threading.Thread(target=ivi_method_to_call)
    t2 = threading.Thread(target=ivi_method_to_call)

    t1.start()
    t1.join()
    assert not t1.is_alive()

    t2.start()
    t2.join()
    assert not t2.is_alive()
