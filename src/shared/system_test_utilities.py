import os
import pathlib
import pytest
import re
import subprocess
import threading
import time


class GrpcServerProcess:
    _SERVER_STARTUP_TIMEOUT = 60

    def __init__(self, config_file_path):
        server_exe = self._get_grpc_server_exe()
        self._proc = subprocess.Popen(
            [str(server_exe), config_file_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        self._stderr_lines = []
        self._stderr_thread = threading.Thread(target=self._capture_stderr, daemon=True)
        self._stderr_thread.start()

        # Read/parse output until we find the port number, the process exits, or we time out.
        try:
            self.server_port = None
            reader_thread = threading.Thread(target=self._read_port, daemon=True)
            reader_thread.start()
            reader_thread.join(timeout=self._SERVER_STARTUP_TIMEOUT)

            if reader_thread.is_alive():
                self._proc.kill()
                self._stderr_thread.join(timeout=5)
                stderr_output = b''.join(self._stderr_lines).decode(errors='replace').strip()
                msg = f"Server did not start within {self._SERVER_STARTUP_TIMEOUT} seconds"
                if stderr_output:
                    msg += f"\nServer stderr:\n{stderr_output}"
                raise RuntimeError(msg)

            if self._proc.poll() is not None:
                self._stderr_thread.join(timeout=5)
                stderr_output = b''.join(self._stderr_lines).decode(errors='replace').strip()
                msg = f"Server exited with return code {self._proc.returncode}"
                if stderr_output:
                    msg += f"\nServer stderr:\n{stderr_output}"
                raise RuntimeError(msg)

            if self.server_port is None:
                raise RuntimeError("Server process ended without reporting a port")

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

    def _read_port(self):
        while self.server_port is None and self._proc.poll() is None:
            line = self._proc.stdout.readline()
            if not line:
                break
            match = re.search(rb"Server listening on port (\d+)", line)
            if match:
                self.server_port = int(match.group(1))

    def _capture_stderr(self):
        for line in self._proc.stderr:
            self._stderr_lines.append(line)

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
