import nifake
import pytest


def test_get_uninstalled_driver_library_raises_driver_not_installed_error():
    with pytest.raises(nifake.errors.DriverNotInstalledError):
        nifake._library_singleton.get()
