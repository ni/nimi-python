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
        with nifgen.Session('', False, 'Simulate=1, DriverSetup=Model:5421;BoardType:PXI') as session:
            year, month, day, hour, minute = session.get_self_cal_last_date_and_time()
            assert False
    except nifgen.Error as e:
        assert e.code == -1074118632  # This operation is not supported for simulated device


def test_self_cal(session):
        session.self_cal()


def test_standard_waveform(session):
    session.configure_output_mode(nifgen.OutputMode.NIFGEN_VAL_OUTPUT_FUNC)
    session.configure_standard_waveform(nifgen.Waveform.SINE, 2.0, 0.0, 2000000, 0.0)
    session.output_enabled = True
    session.configure_trigger_mode(nifgen.TriggerMode.NIFGEN_VAL_CONTINUOUS)
    session.configure_trigger_source(nifgen.TriggerSource.NIFGEN_VAL_IMMEDIATE)
    with session.initiate():
        assert session.func_amplitude == 2.0
        assert session.func_waveform == nifgen.Waveform.SINE
        assert session.is_done() is False


def test_no_waveform_data(session):
    try:
        with session.initiate():
            assert False
    except nifgen.Error as e:
        assert e.code == -1074118636  # No waveforms have been created


def test_frequency_list(session):
    session.configure_output_mode(nifgen.OutputMode.NIFGEN_VAL_OUTPUT_FREQ_LIST)
    session.clear_freq_list(-1)
    duration_array = [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01]
    frequency_array = [1000, 100900, 200800, 300700, 400600, 500500, 600400, 700300, 800200, 900100]
    waveform_handle = session.create_freq_list(nifgen.Waveform.SQUARE, 10, frequency_array, duration_array)
    session.configure_freq_list(waveform_handle, 2.0, 0, 0)
    session.configure_trigger_mode(nifgen.TriggerMode.NIFGEN_VAL_CONTINUOUS)
    session.disable_start_trigger()
    session.output_enabled = True
    with session.initiate():
        assert session.func_waveform == nifgen.Waveform.SQUARE
    session.configure_software_edge_start_trigger()
    session.output_enabled = True
    with session.initiate():
        assert session.func_waveform == nifgen.Waveform.SQUARE
