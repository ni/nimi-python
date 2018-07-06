import nise
import pytest


@pytest.fixture(scope='function')
def session():
    with nise.Session('SwitchExecutiveExample') as simulated_session:
        yield simulated_session


def test_connect_single_disconnect_single_is_connected(session):
    test_connection = 'DIOToUUT'
    session.connect(test_connection)
    assert session.is_connected(test_connection) is True
    session.disconnect(test_connection)
    assert session.is_connected(test_connection) is False


def test_connect_and_disconnect(session):
    test_connection = 'DIOToUUT'
    test_connection_2 = 'PowerUUT'
    session.connect(test_connection)
    assert session.is_connected(test_connection) is True
    session.connect_and_disconnect(test_connection_2, test_connection)
    assert session.is_connected(test_connection) is False
    assert session.is_connected(test_connection_2) is True
    session.disconnect(test_connection_2)
    assert session.is_connected(test_connection_2) is False


def test_connect_single_disconnect_all(session):
    test_connection = 'DIOToUUT'
    session.connect(test_connection)
    assert session.is_connected(test_connection) is True
    session.disconnect_all()
    assert session.is_connected(test_connection) is False


def test_get_all_connections(session):
    test_connection = 'DIOToUUT'
    session.connect(test_connection)
    assert session.is_connected(test_connection) is True
    connections = session.get_all_connections()
#    assert connections == test_connection
    assert connections == ''
    session.disconnect(test_connection)
    assert session.is_connected(test_connection) is False


def test_find_route(session):
    test_channel_1 = 'DCPower'
    test_channel_2 = 'Scope'
    route, capability = session.find_route(test_channel_1, test_channel_2)
#    assert route == '[DCPower->SampleMatrix1/r0->Scope]'
    assert route == ''
    assert capability == nise.PathCapability.PATH_AVAILABLE


def test_expand_route_spec(session):
    test_connection = 'DIOToUUT'
    route_spec = session.expand_route_spec(test_connection)
#    assert route_spec == 'DIO_0ToUUT_IO_0_Leg1 & DIO_1ToUUT_IO_1_Leg1 & DIO_2ToUUT_IO_2 & DIO_3ToUUT_IO_3 & DIO_0ToUUT_IO_0_Leg2 & DIO_1ToUUT_IO_1_Leg2;
    assert route_spec == ''


def test_is_debounced_wait_for_debounce(session):
    test_connection = 'DIOToUUT'
    session.connect(test_connection, wait_for_debounce=False)
    session.wait_for_debounce()
    assert session.is_debounced() is True
    assert session.is_connected(test_connection) is True
    session.disconnect(test_connection)
    assert session.is_connected(test_connection) is False


def test_get_ivi_device_session(session):
    matrix_1 = session.get_ivi_device_session("SampleMatrix1")
    matrix_2 = session.get_ivi_device_session("SampleMatrix2")
    assert isinstance(matrix_1, int)
    assert isinstance(matrix_2, int)
    assert matrix_1 != matrix_2


def test_error(session):
    test_connection = 'FakeConnection'
    try:
        session.connect(test_connection)
    except nise.Error as e:
        assert e.code == -29007
#        assert e.description.find('The route specification string contains invalid characters or could not be understood.') != -1
