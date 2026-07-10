import faulthandler
import gc
import os
import pathlib
import pytest
import re
import subprocess
import sys
import threading
import time


def enable_native_teardown_diagnostics():
    '''Dump Python tracebacks for all threads if a fatal signal fires.

    The RHEL 9.6 / Python 3.10 system-test aborts (SIGABRT -6, SIGSEGV -11)
    happen inside the NI native runtime teardown at interpreter shutdown,
    after every test has already passed. Enabling faulthandler makes the
    interpreter print the Python stack of every live thread at the moment
    of the crash, so the offending thread/call chain shows up in the CI log
    next to the glibc assertion. This is safe to leave enabled permanently.
    '''
    if not faulthandler.is_enabled():
        faulthandler.enable(all_threads=True)


def finalize_test_process(exitstatus):
    '''Force a deterministic process teardown after the test session ends.

    - Runs gc.collect() a few times so session/driver finalizers execute
      while the interpreter is still fully alive, instead of at random
      during interpreter shutdown where the native mutex teardown race
      becomes fatal on newer glibc.
    - If NIMI_FORCE_HARD_EXIT is set, flushes output and calls os._exit(),
      which skips atexit handlers and native library unload entirely.
      Diagnostic use: if the -6 SIGABRT disappears when this is set, the
      crash is confirmed to live in interpreter-shutdown-time native
      teardown rather than in the tests or driver logic.

      NOTE: os._exit() also skips coverage's atexit writer, so coverage
      data will not be produced for a run that hard-exits. Only enable
      NIMI_FORCE_HARD_EXIT for diagnostic runs, not for coverage runs.
    '''
    for _ in range(3):
        gc.collect()
    if os.environ.get('NIMI_FORCE_HARD_EXIT'):
        sys.stdout.flush()
        sys.stderr.flush()
        os._exit(0 if exitstatus == 0 else 1)


class GrpcServerProcess:
    def __init__(self, config_file_path):
        server_exe = self._get_grpc_server_exe()
        self._proc = subprocess.Popen([str(server_exe), config_file_path], stdout=subprocess.PIPE)

        # Read/parse output until we find the port number or the process exits; discard the rest.
        try:
            self.server_port = None
            while self.server_port is None and self._proc.poll() is None:
                line = self._proc.stdout.readline()
                match = re.search(rb"Server listening on port (\d+)", line)
                if match:
                    self.server_port = int(match.group(1))

            if self._proc.poll() is not None:
                raise RuntimeError(f"Server exited with return code {self._proc.returncode}")

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
