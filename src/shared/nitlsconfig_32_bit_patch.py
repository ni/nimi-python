import ctypes
import os
import subprocess


def _patch_subprocess_for_32_bit_nitlsconfig_lookup():
    # Because nitlsconfig lives in System32, and the 32-bit system tests are run on a 64-bit machine, the installation
    # of nitlsconfig is invisible by default. To get around this, we can disable Wow64 redirection. In order to minimize
    # the impact of this, we patch the subprocess initialization specifically for calls to nitlsconfig
    if os.name != "nt":
        return

    original_init = subprocess.Popen.__init__

    def patched_init(self, args, *posargs, **kwargs):
        command = args[0] if isinstance(args, (list, tuple)) else args
        is_nitlsconfig = isinstance(command, str) and os.path.splitext(os.path.basename(command))[0].lower() == "nitlsconfig"
        if not is_nitlsconfig:
            return original_init(self, args, *posargs, **kwargs)

        old = ctypes.c_void_p()
        disabled = bool(ctypes.windll.kernel32.Wow64DisableWow64FsRedirection(ctypes.byref(old)))
        try:
            return original_init(self, args, *posargs, **kwargs)
        finally:
            if disabled:
                ctypes.windll.kernel32.Wow64RevertWow64FsRedirection(old)

    subprocess.Popen.__init__ = patched_init


_patch_subprocess_for_32_bit_nitlsconfig_lookup()
