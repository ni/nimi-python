#!/usr/bin/python

import nimodinst
import re
        
def test_bad_device_family(family):
    with nimodinst.Session('FAKE') as session:
        assert len(session) == 0


def test_no_device_family(family):
    with nimodinst.Session(family) as session:
        assert len(session) > 0, 'Must have hardware for ModInst tests to be valid.'


def test_device_family_string_with_dashes(family):
    modifiedFamily = family.upper()[:2] + '-' + family.upper()[2:] #Changing nidmm to NI-DMM
    with nimodinst.Session(modifiedFamily) as session:
        assert len(session) > 0, 'Must have hardware for this tests to be valid.'


def test_device_family_string_without_dashes(family):
    with nimodinst.Session(family) as session:
        assert len(session) > 0, 'Must have hardware for ModInst tests to be valid.'


def test_int_attribute_error_on_non_existant_device(family):
    with nimodinst.Session(family) as session:
        device = len(session) + 1
        try:
            session.slot_number[device]
            assert False
        except nimodinst.Error as e:
            assert e.code == -250202  # NIMODINST_ERROR_INVALID_DEVICE_INDEX
            assert e.description.lower().find('the device index is out of the range of valid device indices for this session.') != -1


def test_string_attribute_error_on_non_existant_device(family):
    with nimodinst.Session(family) as session:
        device = len(session) + 1
        try:
            session.slot_number[device]
            assert False
        except nimodinst.Error as e:
            assert e.code == -250202  # NIMODINST_ERROR_INVALID_DEVICE_INDEX
            assert e.description.lower().find('the device index is out of the range of valid device indices for this session.') != -1


def test_writeonly_attribute(family):
    with nimodinst.Session(family) as session:
        assert len(session) > 0, 'Must have hardware for ModInst tests to be valid.'
        try:
            session.device_name[0] = 'New Name'
            assert False
        except TypeError as e:
            assert str(e).find('does not support item assignment') != -1


def test_device_name_attribute(family):
    with nimodinst.Session(family) as session:
        assert len(session) > 0, 'Must have hardware for ModInst tests to be valid.'
        assert isinstance(session.device_name[0], str)
        assert len(session.device_name[0]) > 0  # device name must be at least 1 character


def test_device_model_attribute(family):
    with nimodinst.Session(family) as session:
        assert len(session) > 0, 'Must have hardware for ModInst tests to be valid.'
        assert len(session.device_model[0]) > 0
        assert isinstance(session.device_model[0], str)
        pattern = r'(NI )?[A-Z]+e?-\d\d\d\d'
        assert re.search(pattern, session.device_model[0]) is not None  # NI Model numbers are generally "NI PXIe-2532", but might also be "USB-2532"


def test_serial_number_attribute(family):
    with nimodinst.Session(family) as session:
        assert len(session) > 0, 'Must have hardware for ModInst tests to be valid.'
        pattern = r'^[0-9A-F]+$'
        assert isinstance(session.serial_number[0], str)
        assert (len(session.serial_number[0]) == 0) | (re.search(pattern, session.serial_number[0]) is not None)  # NI Serial numbers hex unless it is simulated than it is 0


def test_bus_number_attribute(family):
    with nimodinst.Session(family) as session:
        assert len(session) > 0, 'Must have hardware for ModInst tests to be valid.'
        assert isinstance(session.bus_number[0], int)


def test_chassis_number_attribute(family):
    with nimodinst.Session(family) as session:
        assert len(session) > 0, 'Must have hardware for ModInst tests to be valid.'
        assert isinstance(session.chassis_number[0], int)


def test_max_pciexpress_link_width_attribute(family):
    with nimodinst.Session(family) as session:
        assert len(session) > 0, 'Must have hardware for ModInst tests to be valid.'
        assert isinstance(session.max_pciexpress_link_width[0], int)


def test_pciexpress_link_width_attribute(family):
    with nimodinst.Session(family) as session:
        assert len(session) > 0, 'Must have hardware for ModInst tests to be valid.'
        assert isinstance(session.pciexpress_link_width[0], int)


def test_slot_number_attribute(family):
    with nimodinst.Session(family) as session:
        assert len(session) > 0, 'Must have hardware for ModInst tests to be valid.'
        assert isinstance(session.slot_number[0], int)


def test_socket_number_attribute(family):
    with nimodinst.Session(family) as session:
        assert len(session) > 0, 'Must have hardware for ModInst tests to be valid.'
        assert isinstance(session.socket_number[0], int)
