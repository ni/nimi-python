import nifake
import pytest


def test_driver_runtime_not_installed_raises_driver_not_installed_error():
    with pytest.raises(nifake.errors.DriverNotInstalledError):
        nifake._library_singleton.get()
