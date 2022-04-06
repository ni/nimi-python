#!/usr/bin/python

import nimodinst
import re


def test_bad_device_family():
    with nimodinst.Session('FAKE') as session:
        assert len(session) == 0


def test_no_device_family():
    with nimodinst.Session('') as session:
        assert len(session) > 0, 'This test expects an instrument in the system (real or simulated).'


def test_device_family_string_with_dashes():
    with nimodinst.Session('NI-DMM') as session:
        assert len(session) > 0, 'This test expects a DMM in the system (real or simulated).'


def test_device_family_string_without_dashes():
    with nimodinst.Session('nidmm') as session:
        assert len(session) > 0, 'This test expects a DMM in the system (real or simulated).'


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


def test_device_name_attribute():
    with nimodinst.Session('') as session:
        assert len(session) > 0, 'This test expects an instrument in the system (real or simulated).'
        assert isinstance(session.devices[0].device_name, str)
        assert len(session.devices[0].device_name) > 0  # device name must be at least 1 character


def test_device_model_attribute():
    with nimodinst.Session('') as session:
        assert len(session) > 0, 'This test expects an instrument in the system (real or simulated).'
        assert len(session.devices[0].device_model) > 0
        assert isinstance(session.devices[0].device_model, str)
        pattern = r'(NI )?[A-Z]+e?-\d\d\d\d'
        assert re.search(pattern, session.devices[0].device_model) is not None  # NI Model numbers are generally "NI PXIe-2532", but might also be "USB-2532"


def test_serial_number_attribute():
    with nimodinst.Session('') as session:
        assert len(session) > 0, 'This test expects an instrument in the system (real or simulated).'
        pattern = r'^[0-9A-F]+$'
        assert isinstance(session.devices[0].serial_number, str)
        assert (len(session.devices[0].serial_number) == 0) | (re.search(pattern, session.devices[0].serial_number) is not None)  # NI Serial numbers hex unless it is simulated than it is 0


def test_bus_number_attribute():
    with nimodinst.Session('') as session:
        assert len(session) > 0, 'This test expects an instrument in the system (real or simulated).'
        assert isinstance(session.devices[0].bus_number, int)


def test_chassis_number_attribute():
    with nimodinst.Session('') as session:
        assert len(session) > 0, 'This test expects an instrument in the system (real or simulated).'
        assert isinstance(session.devices[0].chassis_number, int)


def test_max_pciexpress_link_width_attribute():
    with nimodinst.Session('') as session:
        assert len(session) > 0, 'This test expects an instrument in the system (real or simulated).'
        assert isinstance(session.devices[0].max_pciexpress_link_width, int)


def test_pciexpress_link_width_attribute():
    with nimodinst.Session('') as session:
        assert len(session) > 0, 'This test expects an instrument in the system (real or simulated).'
        assert isinstance(session.devices[0].pciexpress_link_width, int)


def test_slot_number_attribute():
    with nimodinst.Session('') as session:
        assert len(session) > 0, 'This test expects an instrument in the system (real or simulated).'
        assert isinstance(session.devices[0].slot_number, int)


def test_socket_number_attribute():
    with nimodinst.Session('') as session:
        assert len(session) > 0, 'This test expects an instrument in the system (real or simulated).'
        assert isinstance(session.devices[0].socket_number, int)
