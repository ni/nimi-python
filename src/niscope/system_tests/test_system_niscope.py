import niscope
import pytest


@pytest.fixture(scope='function')
def session():
    with niscope.Session('FakeDevice', False, True, 'Simulate=1, DriverSetup=Model:5164; BoardType:PXIe') as simulated_session:
        yield simulated_session


# Attribute tests
def test_vi_boolean_attribute(session):
    session.allow_more_records_than_memory = False
    default_option = session.allow_more_records_than_memory
    assert default_option is False


def test_vi_string_attribute(session):
    session.acq_arm_source = 'NISCOPE_VAL_IMMEDIATE'
    start_trigger_source = session.acq_arm_source
    assert start_trigger_source == 'NISCOPE_VAL_IMMEDIATE'


# Basic usability tests
def test_read(session):
    test_voltage = 1.0
    test_record_length = 2000
    test_channels = '0,1'
    test_num_channels = 2
    session.configure_vertical(test_voltage, niscope.VerticalCoupling.AC)
    session.configure_horizontal_timing(50000000, test_record_length, 50.0, 1, True)
    wfm, wfm_infos = session[test_channels].read(1, test_record_length)
    assert len(wfm) == test_num_channels * test_record_length
    assert len(wfm_infos) == test_num_channels


def test_fetch(session):
    test_voltage = 1.0
    test_record_length = 2000
    test_channels = '0,1'
    test_num_channels = 2
    session.configure_vertical(test_voltage, niscope.VerticalCoupling.AC)
    session.configure_horizontal_timing(50000000, test_record_length, 50.0, 1, True)
    with session.initiate():
        wfm, wfm_infos = session[test_channels].fetch(1, test_record_length)
    assert len(wfm) == test_num_channels * test_record_length
    assert len(wfm_infos) == test_num_channels


def test_self_test(session):
    result, message = session.self_test()
    assert result == 0
    assert message == 'Scope Self Tests PASSED.'


def test_reset(session):
    deault_fetch_relative_to = session.fetch_relative_to
    assert deault_fetch_relative_to == niscope.FetchRelativeTo.PRETRIGGER
    session.fetch_relative_to = niscope.FetchRelativeTo.READ_POINTER
    non_default_acqusition_type = session.fetch_relative_to
    assert non_default_acqusition_type == niscope.FetchRelativeTo.READ_POINTER
    session.reset()
    assert session.fetch_relative_to == niscope.FetchRelativeTo.PRETRIGGER


def test_reset_device(session):
    deault_meas_percentage_method = session.meas_percentage_method
    assert deault_meas_percentage_method == niscope.PercentageMethod.BASETOP
    session.meas_percentage_method = niscope.PercentageMethod.MINMAX
    non_default_meas_percentage_method = session.meas_percentage_method
    assert non_default_meas_percentage_method == niscope.PercentageMethod.MINMAX
    session.reset_device()
    assert session.meas_percentage_method == niscope.PercentageMethod.BASETOP


def test_reset_with_defaults(session):
    deault_meas_time_histogram_high_time = session.meas_time_histogram_high_time
    assert deault_meas_time_histogram_high_time == 0.0005
    session.meas_time_histogram_high_time = 0.0010
    non_default_meas_time_histogram_high_time = session.meas_time_histogram_high_time
    assert non_default_meas_time_histogram_high_time == 0.0010
    session.reset_with_defaults()
    assert session.meas_time_histogram_high_time == 0.0005


def test_get_error(session):
    try:
        session.instrument_model = ''
        assert False
    except niscope.Error as e:
        assert e.code == -1074135027  # Error : Attribute is read-only.
        assert e.description.find('Attribute is read-only.') != -1


def test_acquisition_status(session):
    assert session.acquisition_status() == niscope.AcquisitionStatus.COMPLETE


def test_self_cal(session):
    session.cal_self_calibrate(niscope.Option.SELF_CALIBRATE_ALL_CHANNELS)


def test_probe_compensation_signal(session):
    session.probe_compensation_signal_start()
    session.probe_compensation_signal_start()


def test_configure_horizontal_timing(session):
    session.configure_vertical(5.0, niscope.VerticalCoupling.DC)
    session.auto_setup()
    session.configure_horizontal_timing(10000000, 1000, 50.0, 1, True)
    session.trigger_modifier = niscope.TriggerModifier.AUTO
    session.configure_trigger_immediate()
    session.horz_record_length == 1000
    session.horz_sample_rate == 10000000


def test_waveform_processing(session):
    session.configure_vertical(5.0, niscope.VerticalCoupling.DC)
    session.configure_horizontal_timing(10000000, 4096, 50.0, 1, True)
    session['0'].read(5, 2000)
    session.add_waveform_processing(niscope.ArrayMeasurement.NO_MEASUREMENT)
    session.add_waveform_processing(niscope.ArrayMeasurement.FFT_AMP_SPECTRUM_DB)
    session.clear_waveform_measurement_stats(niscope.ClearableMeasurement.ALL_MEASUREMENTS)
    session.clear_waveform_processing()
    session.horz_record_length == 4096
    session.horz_sample_rate == 10000000


def test_fetch_read_measuremet(session):
    active_channel = session['0']
    read_measurement = active_channel.read_measurement(niscope.ScalarMeasurement.FREQUENCY)[0]  # fetching first measurement from returned array
    expected_measurement = 10000
    in_range = abs(read_measurement - expected_measurement) <= max(1e-02 * max(abs(read_measurement), abs(expected_measurement)), 0.0)  # https://stackoverflow.com/questions/5595425/what-is-the-best-way-to-compare-floats-for-almost-equality-in-python
    assert in_range is True
    fetch_measurement = active_channel.fetch_measurement(niscope.ScalarMeasurement.FREQUENCY)[0]
    in_range = abs(fetch_measurement - expected_measurement) <= max(1e-02 * max(abs(fetch_measurement), abs(expected_measurement)), 0.0)  # https://stackoverflow.com/questions/5595425/what-is-the-best-way-to-compare-floats-for-almost-equality-in-python
    assert in_range is True
    measurement_stats = active_channel.fetch_measurement_stats(niscope.ScalarMeasurement.FREQUENCY)[0][0]  # extracting single measurement from fetch_measurement_stats
    in_range = abs(measurement_stats - expected_measurement) <= max(1e-02 * max(abs(measurement_stats), abs(expected_measurement)), 0.0)  # https://stackoverflow.com/questions/5595425/what-is-the-best-way-to-compare-floats-for-almost-equality-in-python
    assert in_range is True


def test_configure_chan_characteristics(session):
    session.vertical_range = 4.0
    session.configure_chan_characteristics(niscope.InputImpedance._50_OHMS, 0)
    assert 50.0 == session.input_impedance


# TODO(injaleea): check after issue #639 fixed, will have to modify after according to fix for issue#614
def test_filters():
    with niscope.Session('FakeDevice', False, True, 'Simulate=1, DriverSetup=Model:5142; BoardType:PXIe') as session:  # filter coefficients methods are available on devices with OSP
        assert [1.0, 0.0, 0.0] == session.get_equalization_filter_coefficients(3)
        try:
            fir_conf = [1.0, 0.0, 0.0]
            session.configure_equalization_filter_coefficients(fir_conf)
        except niscope.Error as e:
            assert e.code == -1074135024  # coefficients list should have 35 items


def test_send_software_trigger_edge(session):
    session.send_software_trigger_edge(niscope.WhichTrigger.ARM_REFERENCE)


def test_disable(session):
    assert session.allow_more_records_than_memory is False
    session.allow_more_records_than_memory = True
    session.disable()
    assert session.allow_more_records_than_memory is False
