import nidigital
import pytest
import os

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


def test_source_waveform_parallel_broadcast(multi_instrument_session):
    configure_session(multi_instrument_session)

    multi_instrument_session.create_source_waveform_parallel(
        pin_list='LowPins',
        waveform_name='new_waveform',
        data_mapping=2600)

    multi_instrument_session.write_source_waveform_broadcast_u32(
        waveform_name='new_waveform',
        waveform_data=[i for i in range(4)])

    multi_instrument_session.burst_pattern(
        site_list='',
        start_label='new_pattern',
        select_digital_function=False,
        wait_until_done=True,
        timeout=5)

    pass_fail = multi_instrument_session.get_site_pass_fail(site_list='')
    assert pass_fail == [True, True]


def configure_session(session):
    test_files_dir = os.path.join(os.getcwd(), 'src', 'nidigital', 'system_tests', 'test_files')

    session.load_pin_map(os.path.join(test_files_dir, 'pin_map.pinmap'))

    session.load_specifications(os.path.join(test_files_dir, 'specifications.specs'))
    session.load_levels(os.path.join(test_files_dir, 'pin_levels.digilevels'))
    session.load_timing(os.path.join(test_files_dir, 'timing.digitiming'))
    session.apply_levels_and_timing(
        site_list='',
        levels_sheet='pin_levels',
        timing_sheet='timing',
        initial_state_high_pins='',
        initial_state_low_pins='',
        initial_state_tristate_pins='')

    session.load_pattern(os.path.join(test_files_dir, 'pattern.digipat'))
