#!/usr/bin/python

import pytest
import nimodinst

@pytest.fixture(scope='function')
def device_info(request):
    device_info = {}
    device_name = "unknown"
    device_sn = "unknown"
    try:
        with nimodinst.Session('nidmm') as session:
            if len(session) > 0:
                device_name = session.device_name[0]
                device_sn = session.serial_number[0]

    except nimodinst.Error as e:
        sys.stderr.write(str(e))
        sys.exit(e.code)
    device_info['name'] = device_name
    device_info['sn'] = device_sn
    return device_info


def test_bad_device_family():
    with nimodinst.Session('FAKE') as session:
        assert len(session) == 0


def test_no_device_family():
    with nimodinst.Session('') as session:
        assert len(session) > 0


def test_device_family_string_with_dashes():
    with nimodinst.Session('NI-DMM') as session:
        assert len(session) > 0


def test_device_family_string_without_dashes():
    with nimodinst.Session('nidmm') as session:
        assert len(session) > 0


def test_int_attribute_error_not_existant():
    with nimodinst.Session('') as session:
        device = len(session) + 1
        try:
            session.slot_number[device]
        except nimodinst.Error as e:
            assert e.code == -250202
            assert e.description.lower().find('the device index is out of the range of valid device indices for this session.') != -1


def test_string_attribute_error_not_existant():
    with nimodinst.Session('') as session:
        device = len(session) + 1
        try:
            session.slot_number[device]
        except nimodinst.Error as e:
            assert e.code == -250202
            assert e.description.lower().find('the device index is out of the range of valid device indices for this session.') != -1


def test_writeonly_attribute(device_info):
    with nimodinst.Session('') as session:
        assert len(session) > 0
        try:
            session.device_name[0] = 'New Name'
        except TypeError as e:
            assert str(e).find('does not support item assignment') != -1


def test_device_name_attribute():
    with nimodinst.Session('') as session:
        assert len(session) > 0
        assert len(session.device_name[0]) > 0 #device name must be at least 1 character


def test_device_model_attribute():
    with nimodinst.Session('') as session:
        assert len(session) > 0
        assert len(session.device_model[0]) > 0
        assert session.device_model[0].find('-') != -1 #This is always a - in ni products.


def test_serial_number_attribute():
    with nimodinst.Session('') as session:
        assert len(session) > 0
        if session.slot_number[0] == -1:
            pytest.skip("Simulated device")
        else:
            assert (len(session.serial_number[0]) == 7) | (len(session.serial_number[0]) == 8) # NI Serial numbers are 7 or 8 characters


def test_bus_number_attribute():
    with nimodinst.Session('') as session:
        assert len(session) > 0
        if session.bus_number[0] == 0:
            pytest.skip("Simulated device")
        else:
            assert session.bus_number[0] > 0


def test_chassis_number_attribute():
    with nimodinst.Session('') as session:
        assert len(session) > 0
        if session.chassis_number[0] == -1:
            pytest.skip("Simulated device")
        else:
            assert session.chassis_number[0] > 0


def test_max_pciexpress_link_width_attribute():
    with nimodinst.Session('') as session:
        assert len(session) > 0
        if session.max_pciexpress_link_width[0] == -1:
            pytest.skip("Simulated device or not supported")
        else:
            assert session.max_pciexpress_link_width[0] > 0


def test_pciexpress_link_width_attribute():
    with nimodinst.Session('') as session:
        assert len(session) > 0
        if session.pciexpress_link_width[0] == -1:
            pytest.skip("Simulated device or not supported")
        else:
            assert session.pciexpress_link_width[0] > 0


def test_slot_number_attribute():
    with nimodinst.Session('') as session:
        assert len(session) > 0
        if session.slot_number[0] == -1:
            pytest.skip("Simulated device")
        else:
            assert session.slot_number[0] > 0


def test_socket_number_attribute():
    with nimodinst.Session('') as session:
        assert len(session) > 0
        if session.socket_number[0] == 0:
            pytest.skip("Simulated device or not supported")
        else:
            assert session.socket_number[0] > 0
