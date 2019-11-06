import nidigital
import pytest

instr = ['PXI1Slot2', 'PXI1Slot5']


@pytest.fixture(scope='function')
def multi_instrument_session():
    with nidigital.Session(resource_name=','.join(instr), options='Simulate=1, DriverSetup=Model:6570') as simulated_session:
        yield simulated_session


def test_property_boolean(multi_instrument_session):
    multi_instrument_session.channels[instr[0] + '/0'].ppmu_allow_extended_voltage_range = True
    assert multi_instrument_session.channels[instr[0] + '/0'].ppmu_allow_extended_voltage_range == True


def test_property_int32(multi_instrument_session):
    multi_instrument_session.channels[instr[0] + '/0'].termination_mode = nidigital.TerminationMode.HIGH_Z
    assert multi_instrument_session.channels[instr[0] + '/0'].termination_mode == nidigital.TerminationMode.HIGH_Z


def test_property_int64(multi_instrument_session):
    multi_instrument_session.cycle_number_history_ram_trigger_cycle_number = 42
    assert multi_instrument_session.cycle_number_history_ram_trigger_cycle_number == 42


def test_property_real64(multi_instrument_session):
    multi_instrument_session.channels[instr[0] + '/0'].ppmu_voltage_level = 4
    assert multi_instrument_session.channels[instr[0] + '/0'].ppmu_voltage_level == pytest.approx(4, rel=1e-3)


def test_property_string(multi_instrument_session):
    multi_instrument_session.start_label = 'foo'
    assert multi_instrument_session.start_label == 'foo'
