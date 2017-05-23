#!/usr/bin/python

import sys, os
# Add parent directory to the path, so that we load the locally sourced nidmm module and not require installation.
sys.path.append(os.path.join(sys.path[0],'..'))

import nidmm

testCount = 0


def test_invalid_device_name():
    try:
        nidmm.Session("Foo!")
        assert false
    except nidmm.Error as e:
        assert e.code == -1074118656
        assert e.elaboration.find("Device was not recognized. The device is not supported with this driver or version.") != -1
        assert e.elaboration.find("Foo!") != -1


def test_take_simple_measurement_works():
    with nidmm.Session("Dev1") as session:
        session.configureMeasurementDigits(nidmm.Function.DC_VOLTS, 10, 5.5)
        assert session.read() < 0.1 # Assume nothing is connected to device, reads back around 0.


def test_wrong_parameter_type():
    with nidmm.Session("Dev1") as session:
        try:
            # We are passing a number where an enum is expected.
            session.configureMeasurementDigits(1, 10, 5.5)
            assert false
        except TypeError as e:
            print(e)
            pass


def test_set_get_attributes():
    with nidmm.Session("Dev1") as session:
        assert session.specificDriverClassSpecMajorVersion == 4
        assert session.specificDriverClassSpecMinorVersion == 1
        session.sampleCount = 5
        assert session.sampleCount == 5
        session.triggerCount = 2
        assert session.triggerCount == 2
        session.range = 50 # Coerces up!
        assert session.range == 100
        session.resolutionDigits = 3.5
        assert session.resolutionDigits == 3.5
        x = session.serialNumber
        print(type(x))
        print(type(session.serialNumber))
        print(session.serialNumber)
        assert session.serialNumber == "1A67CAC"
        assert session.simulate is False

