#!/usr/bin/python

import sys, os
# Add parent directory to the path, so that we load the locally sourced nidmm module.
sys.path.append(os.path.join(sys.path[0],'..'))

import nidmm

testCount = 0


testCount = testCount+1
print("\nTest " + str(testCount) + ": Invalid device name")
try:
    nidmm.Session("Foo!")
except nidmm.Error as e:
    if (e.code != -1074118656):
        raise e
    if (e.elaboration.find("Device was not recognized. The device is not supported with this driver or version.") == -1):
        raise e
    if (e.elaboration.find("Foo!") == -1):
        raise e
    print("pass")


testCount = testCount+1
print("\nTest " + str(testCount) + ": Take a simple measurement")
with nidmm.Session("Dev1") as session:
    session.configureMeasurementDigits(nidmm.Function.DC_VOLTS, 10, 5.5)
    print("Measurement: " + str(session.read()))
    print("pass")


testCount = testCount+1
print("\nTest " + str(testCount) + ": Pass the wrong type to a function")
with nidmm.Session("Dev1") as session:
    try:
        # We are passing a number where an enum is expected.
        session.configureMeasurementDigits(1, 10, 5.5)
    except TypeError as e:
        print(e)
        pass
    print("pass")

assert isinstance(nidmm.Function.DC_VOLTS, nidmm.Function)
assert nidmm.Function(1) is nidmm.Function.DC_VOLTS
assert nidmm.Function(1).value

testCount = testCount+1
print("\nTest " + str(testCount) + ": Set and get attributes")
with nidmm.Session("Dev1") as session:
    if(session.specificDriverClassSpecMajorVersion != 4): raise Exception("Fail")
    if(session.specificDriverClassSpecMinorVersion != 1): raise Exception("Fail")
    session.sampleCount = 5
    if(session.sampleCount != 5): raise Exception("Fail")
    session.triggerCount = 2
    if(session.triggerCount != 2): raise Exception("Fail")
    session.range = 50 # Coerces up!
    if(session.range != 100): raise Exception("Fail")
    session.resolutionDigits = 3.5
    if(session.resolutionDigits != 3.5): raise Exception("Fail")
    if(session.serialNumber is "1A67CAC"): raise Exception("Fail")
    if(session.simulate): raise Exception("Fail")
    print("pass")
