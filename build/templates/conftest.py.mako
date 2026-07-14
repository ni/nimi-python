<%
    config = template_parameters['metadata'].config
    module_name = config['module_name']
%>\
"""Diagnostic conftest.py — generated for ${module_name} system tests.

Gathers evidence for the glibc 2.34 libpthread-merge crash hypothesis:
  - Fatal glibc error / SIGABRT (-6) or SIGSEGV (-11) during process teardown
  - Root cause candidate: pthread_create is always present in glibc 2.34+,
    so NI drivers that previously detected its absence and ran in single-threaded
    mode now always take the multi-threaded code path, whose cleanup has a bug
    under Python's interpreter shutdown sequence on RHEL 9.

Evidence collected:
  1. Thread count at session start / end / atexit — if the driver spawns threads
     on RHEL 9 that it did not on RHEL 8, this is direct confirmation.
  2. /proc/self/maps libpthread entries — on RHEL 8 libpthread.so.0 is a real DSO
     with multiple large mappings; on RHEL 9 it is a tiny stub.
  3. fault_handler_<pid>.log — faulthandler writes all-thread stack traces to this
     file on SIGABRT and SIGSEGV using raw write() so the data is flushed even if
     the process is killed mid-cleanup.
"""
import atexit
import faulthandler
import os
import signal
import sys
import threading

import pytest


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _log_threads(when):
    threads = threading.enumerate()
    print(f"\n[DIAGNOSTIC {when}] Active threads ({len(threads)}):")
    for t in threads:
        print(f"  [{t.ident:>10}] name={t.name!r:<40} daemon={t.daemon} alive={t.is_alive()}")


def _log_proc_status_threads():
    """Read Threads: from /proc/self/status — kernel-level count, includes
    any threads the NI driver runtime created outside of Python's knowledge."""
    try:
        with open("/proc/self/status") as f:
            for line in f:
                if line.startswith("Threads:"):
                    print(f"[DIAGNOSTIC /proc/self/status] {line.strip()}")
                    return
    except OSError:
        pass


def _log_libpthread_maps():
    """Parse /proc/self/maps to show libpthread DSO state.

    Expected output comparison:
      RHEL 8 (glibc 2.28): multiple mappings, libpthread-2.28.so, total size ~100 KB
      RHEL 9 (glibc 2.34): one tiny mapping, libpthread.so.0 stub, total size ~4 KB
                            OR no libpthread entry at all (fully absorbed into libc)
    """
    try:
        with open("/proc/self/maps") as f:
            maps = f.read()
        pthread_entries = [line for line in maps.splitlines() if "libpthread" in line]
        if pthread_entries:
            print(f"\n[DIAGNOSTIC /proc/self/maps] libpthread entries ({len(pthread_entries)}):")
            for entry in pthread_entries:
                print(f"  {entry}")
        else:
            print(
                "\n[DIAGNOSTIC /proc/self/maps] libpthread NOT found — "
                "confirms glibc 2.34+ where libpthread was merged into libc.so.6. "
                "pthread_create is now always present; drivers that checked for its "
                "absence to choose single-threaded mode will always take the "
                "multi-threaded code path on this system."
            )
    except OSError as exc:
        print(f"\n[DIAGNOSTIC /proc/self/maps] Could not read: {exc}")


def _atexit_callback():
    """Registered early so it runs near the start of atexit processing,
    before library destructors and driver cleanup fire."""
    print("\n[DIAGNOSTIC ATEXIT] Python atexit phase beginning — "
          "library destructors will run after this.")
    _log_threads("ATEXIT")
    _log_proc_status_threads()


# ---------------------------------------------------------------------------
# Session-scoped autouse fixture
# ---------------------------------------------------------------------------

@pytest.fixture(autouse=True, scope="session")
def _diagnostic_logging():
    """Diagnostic fixture active for all ${module_name} system tests.

    Placed in the tox rootdir conftest so it is loaded regardless of whether
    the tests are in examples/ or system_tests/.
    """
    # ------------------------------------------------------------------
    # 1. Faulthandler to stderr
    #    - PYTHONUNBUFFERED=1 (set in tox setenv) ensures stderr is not
    #      buffered, so the output is flushed to the build log even on crash.
    #    - faulthandler uses raw write() syscalls internally, so it is safe
    #      to call from a signal handler and will not deadlock.
    #    - stdout is used (not stderr) because pytest -s passes stdout directly
    #      to the CI build log, whereas stderr routing varies by runner.
    #    - SIGABRT (exit -6) is NOT handled by default; register explicitly.
    # ------------------------------------------------------------------
    faulthandler.enable(file=sys.stdout, all_threads=True)

    try:
        faulthandler.register(signal.SIGABRT, file=sys.stdout, all_threads=True, chain=True)
    except (AttributeError, OSError):
        pass  # faulthandler.register not available on all platforms

    # ------------------------------------------------------------------
    # 2. atexit handler — runs at the start of Python's atexit phase,
    #    before C library destructors, giving a snapshot of what threads
    #    are still alive when cleanup begins
    # ------------------------------------------------------------------
    atexit.register(_atexit_callback)

    # ------------------------------------------------------------------
    # 3. Baseline measurements at session start
    # ------------------------------------------------------------------
    _log_libpthread_maps()
    _log_proc_status_threads()
    _log_threads("SESSION_START")

    yield

    # ------------------------------------------------------------------
    # 4. Post-session measurements — compare thread count with SESSION_START.
    #    A higher count here means the driver leaked threads.
    # ------------------------------------------------------------------
    _log_threads("SESSION_END")
    _log_proc_status_threads()
    sys.stdout.flush()
