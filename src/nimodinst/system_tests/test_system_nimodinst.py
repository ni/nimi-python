#!/usr/bin/python

import nimodinst
import pytest
import re


# Many of the tests below require at least one instrument (real or simulated) to be present in the
# system. nimodinst cannot create its own simulated devices; it enumerates instruments configured
# for other drivers. Because these simulated instruments cannot be created via nisimdev in this
# environment, the tests are skipped here and are expected to run through the pipeline where
# instruments are preconfigured.
_requires_instrument_skip_reason = (
    'Requires an instrument (real or simulated) present in the system, which cannot be created via '
    'nisimdev in this environment. Run through pipeline where instruments are preconfigured.'
)


def test_bad_device_family():
    with nimodinst.Session('FAKE') as session:
        assert len(session) == 0


@pytest.mark.skip(reason=_requires_instrument_skip_reason)
def test_no_device_family():
    with nimodinst.Session('') as session:
        assert len(session) > 0, 'This test expects an instrument in the system (real or simulated).'


@pytest.mark.skip(reason=_requires_instrument_skip_reason)
def test_device_family_string_with_dashes():
    with nimodinst.Session('NI-SCOPE') as session:
        assert len(session) > 0, 'This test expects a device supported by NI-SCOPE in the system (real or simulated).'


@pytest.mark.skip(reason=_requires_instrument_skip_reason)
def test_device_family_string_without_dashes():
    with nimodinst.Session('niscope') as session:
        assert len(session) > 0, 'This test expects a device supported by NI-SCOPE in the system (real or simulated).'


def test_int_attribute_error_on_non_existant_device():
    with nimodinst.Session('') as session:
        device = len(session) + 1
        try:
            session.devices[device].slot_number
            assert False
        except IndexError:
            pass


def test_string_attribute_error_on_non_existant_device():
    with nimodinst.Session('') as session:
        device = len(session) + 1
        try:
            session.devices[device].slot_number
            assert False
        except IndexError:
            pass


@pytest.mark.skip(reason=_requires_instrument_skip_reason)
def test_device_name_attribute():
    with nimodinst.Session('') as session:
        assert len(session) > 0, 'This test expects an instrument in the system (real or simulated).'
        assert isinstance(session.devices[0].device_name, str)
        assert len(session.devices[0].device_name) > 0  # device name must be at least 1 character


@pytest.mark.skip(reason=_requires_instrument_skip_reason)
def test_device_model_attribute():
    with nimodinst.Session('') as session:
        assert len(session) > 0, 'This test expects an instrument in the system (real or simulated).'
        assert len(session.devices[0].device_model) > 0
        assert isinstance(session.devices[0].device_model, str)
        pattern = r'(NI )?[A-Z]+e?-\d\d\d\d'
        assert re.search(pattern, session.devices[0].device_model) is not None  # NI Model numbers are generally "NI PXIe-2532", but might also be "USB-2532"


@pytest.mark.skip(reason=_requires_instrument_skip_reason)
def test_serial_number_attribute():
    with nimodinst.Session('') as session:
        assert len(session) > 0, 'This test expects an instrument in the system (real or simulated).'
        pattern = r'^[0-9A-F]+$'
        assert isinstance(session.devices[0].serial_number, str)
        assert (len(session.devices[0].serial_number) == 0) or (re.search(pattern, session.devices[0].serial_number) is not None)  # NI Serial numbers hex unless it is simulated than it is 0


@pytest.mark.skip(reason=_requires_instrument_skip_reason)
def test_bus_number_attribute():
    with nimodinst.Session('') as session:
        assert len(session) > 0, 'This test expects an instrument in the system (real or simulated).'
        assert isinstance(session.devices[0].bus_number, int)


@pytest.mark.skip(reason=_requires_instrument_skip_reason)
def test_chassis_number_attribute():
    with nimodinst.Session('') as session:
        assert len(session) > 0, 'This test expects an instrument in the system (real or simulated).'
        assert isinstance(session.devices[0].chassis_number, int)


@pytest.mark.skip(reason=_requires_instrument_skip_reason)
def test_max_pciexpress_link_width_attribute():
    with nimodinst.Session('') as session:
        assert len(session) > 0, 'This test expects an instrument in the system (real or simulated).'
        assert isinstance(session.devices[0].max_pciexpress_link_width, int)


@pytest.mark.skip(reason=_requires_instrument_skip_reason)
def test_pciexpress_link_width_attribute():
    with nimodinst.Session('') as session:
        assert len(session) > 0, 'This test expects an instrument in the system (real or simulated).'
        assert isinstance(session.devices[0].pciexpress_link_width, int)


@pytest.mark.skip(reason=_requires_instrument_skip_reason)
def test_slot_number_attribute():
    with nimodinst.Session('') as session:
        assert len(session) > 0, 'This test expects an instrument in the system (real or simulated).'
        assert isinstance(session.devices[0].slot_number, int)


@pytest.mark.skip(reason=_requires_instrument_skip_reason)
def test_socket_number_attribute():
    with nimodinst.Session('') as session:
        assert len(session) > 0, 'This test expects an instrument in the system (real or simulated).'
        assert isinstance(session.devices[0].socket_number, int)
