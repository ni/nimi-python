import nifgen
import pytest


@pytest.fixture(scope='function')
def session():
    with nifgen.Session('', False, 'Simulate=1, DriverSetup=Model:5433 (2CH);BoardType:PXIe') as simulated_session:
        yield simulated_session


def test_self_test(session):
    result, message = session.self_test()
    assert result == 0
    assert message == 'Self test passed'


def test_get_attribute_string(session):
    model = session.instrument_model
    assert model == 'NI PXIe-5433 (2CH)'


def test_error_message(session):
    # Calling the private function directly, as _get_error_message() only gets called when you have an invalid session,
    # and there is no good way for us to invalidate a simulated session.
    message = session._error_message(-1074135027)
    assert message.find('Attribute is read-only.') != -1


def test_get_error(session):
    try:
        session.instrument_model = ''
        assert False
    except nifgen.Error as e:
        assert e.code == -1074135027  # Error : Attribute is read-only.
        assert e.description.find('Attribute is read-only.') != -1


def test_method_get_self_cal_supported(session):
    assert session.get_self_cal_supported() in [True, False]


def test_get_self_cal_last_date_and_time():
    try:
        with nifgen.Session('', False, 'Simulate=1, DriverSetup=Model:5421;BoardType:PXI') as session:  # Simulated 5433 returns unrecoverable error when calling get_self_cal_last_date_and_time()
            year, month, day, hour, minute = session.get_self_cal_last_date_and_time()
            assert False
    except nifgen.Error as e:
        assert e.code == -1074118632  # This operation is not supported for simulated device


def test_self_cal(session):
        session.self_cal()


def test_standard_waveform(session):
    session.output_mode = nifgen.OutputMode.FUNC
    session.configure_standard_waveform(nifgen.Waveform.SINE, 2.0, 2000000, 1.0, 0.0)
    expected_frequency = 2000000
    with session.initiate():
        assert session.func_amplitude == 2.0
        assert session.func_waveform == nifgen.Waveform.SINE
        actual_frequency = session.func_frequency
        in_range = abs(actual_frequency - expected_frequency) <= max(1e-09 * max(abs(actual_frequency), abs(expected_frequency)), 0.0)   # https://stackoverflow.com/questions/5595425/what-is-the-best-way-to-compare-floats-for-almost-equality-in-python
        assert in_range is True
        assert session.func_dc_offset == 1.0
        assert session.func_start_phase == 0.0
        assert session.is_done() is False


def test_frequency_list(session):
    session.output_mode = nifgen.OutputMode.FREQ_LIST
    duration_array = [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01]
    frequency_array = [1000, 100900, 200800, 300700, 400600, 500500, 600400, 700300, 800200, 900100]
    waveform_handle = session.create_freq_list(nifgen.Waveform.SQUARE, frequency_array, duration_array)
    session.configure_freq_list(waveform_handle, 2.0, 0, 0)
    session.trigger_mode = nifgen.TriggerMode.CONTINUOUS
    session.output_enabled = True
    assert session.func_waveform == nifgen.Waveform.SQUARE
    assert session.func_amplitude == 2.0


def test_clear_freq_list(session):
    session.clear_freq_list(-1)


def test_configure_arb_waveform(session):
    waveform_data = [0.000000, 0.049068, 0.098017, 0.146730, 0.195090, 0.242980, 0.290285, 0.336890, 0.382683, 0.427555]
    session.output_mode = nifgen.OutputMode.ARB
    session.configure_arb_waveform(session.create_waveform_f64(waveform_data), 1.0, 0.0)


def test_disable(session):
    channel = session['0']
    assert channel.output_enabled is True
    session.disable()
    assert channel.output_enabled is False


def test_get_ext_cal_last_date_and_time():
    with nifgen.Session('', False, 'Simulate=1, DriverSetup=Model:5421;BoardType:PXI') as session:  # 5433 throws out unrecoverable error on calling get_ext_cal_last_date_and_time()
        try:
            session.get_ext_cal_last_date_and_time()
            assert False
        except nifgen.Error as e:
            assert e.code == -1074118632  # This operation is not supported for simulated device


def test_get_ext_cal_last_temp(session):
    try:
        session.get_ext_cal_last_temp()
    except nifgen.Error as e:
        assert e.code == -1074135023  # Function or method not supported for 5413/23/33 and not supported on any other FGen when simulated


def test_get_ext_cal_recommended_interval(session):
    recommended_interval = session.get_ext_cal_recommended_interval()
    assert recommended_interval == 24  # recommended external cal interval is 24 months


''' TODO(Jaleel) Enable after Issue#558 fixed
def test_get_hardware_state():
    with nifgen.Session('', False, 'Simulate=1, DriverSetup=Model:5421;BoardType:PXI') as session:  # Function or method not supported for 5413/23/33
        assert session.get_hardware_state() == nifgen.HardwareState.IDLE
'''


def test_get_self_cal_last_temp(session):
    assert session.get_self_cal_last_temp() == 0.0  # returns 0.0 for a simulated 5433


def test_query_arb_wfm_capabilities(session):
    max_number_of_waveform, waveform_quantum, minimum_waveform_size, maximum_waveform_size = session.query_arb_wfm_capabilities()
    assert max_number_of_waveform == 4194304  # default values for max_number_of_waveform, waveform_quantum, minimum_waveform_size, maximum_waveform_size for a simulated 5433 is 4194304, 1, 4, 268435456 respectively
    assert waveform_quantum == 1
    assert minimum_waveform_size == 4
    assert maximum_waveform_size == 268435456


def test_query_freq_list_capabilities(session):
    maximum_number_of_freq_lists, minimum_frequency_list_length, maximum_frequency_list_length, minimum_frequency_list_duration, maximum_frequency_list_duration, frequency_list_duration_quantum = session.query_freq_list_capabilities()  # comparing with default values for simulated 5433
    assert maximum_number_of_freq_lists == 9999
    assert minimum_frequency_list_length == 1
    assert maximum_frequency_list_length == 1024
    assert minimum_frequency_list_duration == 1e-08
    assert maximum_frequency_list_duration == 2814749.76711
    assert frequency_list_duration_quantum == 1e-08


def test_read_current_temperature(session):
    assert session.read_current_temperature() > 25.0


def test_allocate_waveform(session):
    try:
        waveforme_data = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1]
        session.write_waveform(session.allocate_waveform(10), waveforme_data)
    except nifgen.Error as e:
        assert e.code == -1074126841  # Writing more data than allocated


def test_clear_waveform_memory(session):
    session.clear_arb_memory()
    session.clear_user_standard_waveform()
    session.clear_arb_sequence(-1)
    session.clear_arb_waveform(-1)


def test_query_arb_seq_capabilities(session):
    maximum_number_of_sequences, minimum_sequence_length, maximum_sequence_length, maximum_loop_count = session.query_arb_seq_capabilities()
    assert maximum_number_of_sequences == 65535
    assert minimum_sequence_length == 1
    assert maximum_sequence_length == 65535
    assert maximum_loop_count == 16777215


def test_arb_seq(session):
    waveform_data = [-32767, -25485, -18204, -10922, -3641, 3641, 10922, 18204, 25485, 32767]
    waveform_data_2 = [0, 9630, 15582, 15582, 9630, 0, -9630, -15582, -15582, -9630]
    session._abort_generation()
    session.arb_sample_rate = 20000000
    session.arb_gain = 1
    session.output_mode = nifgen.OutputMode.SEQ
    session.clear_arb_memory()
    session.create_waveform_i16(waveform_data)
    session.create_waveform_i16(waveform_data_2)
    session.clear_arb_sequence(-1)
    session.configure_arb_sequence(session.create_advanced_arb_sequence([0, 1], [1, 1], sample_counts_array=[], marker_location_array=[-1, -1])[1], 1, 0)  # May have to change sample_counts_array when issue#594 fixed
    session.commit()
    actual_sample_rate = session.arb_sample_rate
    in_range = abs(actual_sample_rate - 20000000) <= max(1e-09 * max(abs(actual_sample_rate), abs(20000000)), 0.0)   # https://stackoverflow.com/questions/5595425/what-is-the-best-way-to-compare-floats-for-almost-equality-in-python
    assert in_range is True
    session.arb_sample_rate = 10000000
    session.create_arb_sequence(2, [0, 1], [1, 1])
    actual_sample_rate = session.arb_sample_rate
    in_range = abs(actual_sample_rate - 10000000) <= max(1e-09 * max(abs(actual_sample_rate), abs(10000000)), 0.0)   # https://stackoverflow.com/questions/5595425/what-is-the-best-way-to-compare-floats-for-almost-equality-in-python
    assert in_range is True
    arb_gain = session.arb_gain
    assert arb_gain == 1


def test_arb_script(session):
    waveform_data = [0, 9630, 15582, 15582, 9630, 0, -9630, -15582, -15582, -9630]
    session.output_mode = nifgen.OutputMode.NIFGEN_VAL_OUTPUT_SCRIPT
    session.configure_digital_edge_script_trigger('ScriptTrigger0', 'PFI0', nifgen.ScriptTriggerDigitalEdgeEdge.RISING)
    session.write_named_waveform_i16('wfmSine', waveform_data)
    session.arb_sample_rate = 10000000
    script = '''script myScript0
    repeat 3
    Generate wfmSine
   end repeat
end script'''
    session.write_script(script)
    session.script_to_generate = 'myScript0'
    session.commit()
    session.delete_script('myScript0')
    actual_sample_rate = session.arb_sample_rate
    in_range = abs(actual_sample_rate - 10000000) <= max(1e-09 * max(abs(actual_sample_rate), abs(10000000)), 0.0)   # https://stackoverflow.com/questions/5595425/what-is-the-best-way-to-compare-floats-for-almost-equality-in-python
    assert in_range is True


def test_reset(session):
    default_output_mode = session.output_mode
    assert default_output_mode == nifgen.OutputMode.ARB
    session.output_mode = nifgen.OutputMode.SEQ
    assert session.output_mode == nifgen.OutputMode.SEQ
    session.reset()
    assert session.output_mode == nifgen.OutputMode.ARB


def test_reset_device(session):
    default_trigger_mode = session.trigger_mode
    assert default_trigger_mode == nifgen.TriggerMode.CONTINUOUS
    session.trigger_mode = nifgen.TriggerMode.STEPPED
    non_default_trigger_mode = nifgen.TriggerMode.STEPPED
    assert non_default_trigger_mode == nifgen.TriggerMode.STEPPED
    session.reset_device()
    assert session.trigger_mode == nifgen.TriggerMode.CONTINUOUS


def test_reset_with_default(session):
    default_sample_rate = session.arb_sample_rate
    assert default_sample_rate == 250000000.0
    session.arb_sample_rate = 100000000.0
    non_default_arb_sample_rate = session.arb_sample_rate
    assert non_default_arb_sample_rate == 100000000.0
    session.reset_with_defaults()
    assert session.arb_sample_rate == 250000000.0


def test_write_binary_waveform(session):
    session.write_binary16_waveform(session.allocate_waveform(10), [0, 0, 0, 1, 1, 1, 2, 2])


'''
(TODO) Jaleel , check it after issue #538 fixed
def test_set_waveform_next_write_possition(session):
    session.set_waveform_next_write_position(session.allocate_waveform(10), nifgen.RelativeTo.START, 5)  # Enable after RelativeTo enum added to enums_addon.py


def test_export_signal(session):
    expected_trigger_terminal = "PXI_Trig0"
    session.export_signal(nifgen.ExportSignal.START_TRIGGER, "", expected_trigger_terminal)  # Enable after issue #538 fixed
    assert expected_trigger_terminal == session.exported_start_trigger_output_terminal


def test_write_waveform_from_filei64(session):
    session.arb_sample_rate = 40000000
    session.create_waveform_from_file_i16(os.path.join(os.getcwd(), 'systemtest_dependencies', 'SineI16BigEndian_1000.bin'), nifgen.ByteOrder.BIG_ENDIAN)  # Enable after issue #538 fixed
    sample_rate = session.arb_sample_rate
    assert sample_rate == 40000000'''
