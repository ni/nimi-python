#FRANKTODO
import datetime
import math
import nise
import numpy
import pytest
import time


@pytest.fixture(scope='function')
def session():
    with nise.Session('SwitchExecutiveExample', "") as simulated_session:
        yield simulated_session


# Basic usability tests
def test_connect_disconnect(session):
    test_connection = 'DIOToUUT'
    session.connect(test_connection)
    assert session.is_connected(test_connection) is True  # Assumes DMM reading is not exactly zero to support non-connected modules and simulated modules.
    session.disconnect(test_connection)
    assert session.is_connected(test_connection) is False

'''
def test_acquisition(session):
    session.configure_measurement_digits(nise.Function.DC_CURRENT, 1, 5.5)
    with session.initiate():
        session.fetch()
    with session.initiate():
        session.fetch()


def test_multi_point_acquisition(session):
    session.configure_multi_point(4, 2)
    session.configure_measurement_digits(nise.Function.DC_VOLTS, 1, 5.5)
    measurements = session.read_multi_point(8)
    assert len(measurements) == 8
'''
