import math
import niscope
import numpy
import pytest
import sys
import tempfile


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
    test_channels = range(2)
    test_num_channels = 2
    test_num_records = 3
    session.configure_vertical(test_voltage, niscope.VerticalCoupling.AC)
    session.configure_horizontal_timing(50000000, test_record_length, 50.0, test_num_records, True)
    waveforms = session.channels[test_channels].read(num_samples=test_record_length, num_records=test_num_records)
    assert len(waveforms) == test_num_channels * test_num_records
    for i in range(len(waveforms)):
        assert len(waveforms[i].samples) == test_record_length


def test_fetch(session):
    test_voltage = 1.0
    test_record_length = 2000
    test_channels = range(2)
    test_num_channels = 2
    test_num_records = 3
    session.configure_vertical(test_voltage, niscope.VerticalCoupling.AC)
    session.configure_horizontal_timing(50000000, test_record_length, 50.0, test_num_records, True)
    with session.initiate():
        waveforms = session.channels[test_channels].fetch(num_samples=test_record_length, num_records=test_num_records)
    assert len(waveforms) == test_num_channels * test_num_records
    for i in range(len(waveforms)):
        assert len(waveforms[i].samples) == test_record_length


def test_fetch_defaults(session):
    test_voltage = 1.0
    test_record_length = 2000
    test_channels = range(2)
    test_num_channels = 2
    session.configure_vertical(test_voltage, niscope.VerticalCoupling.AC)
    session.configure_horizontal_timing(50000000, test_record_length, 50.0, 1, True)
    with session.initiate():
        waveforms = session.channels[test_channels].fetch()
    assert len(waveforms) == test_num_channels
    for i in range(len(waveforms)):
        assert len(waveforms[i].samples) == test_record_length


def test_fetch_binary8_into(session):
    test_voltage = 1.0
    test_record_length = 2000
    test_channels = range(2)
    test_num_channels = 2
    waveform = numpy.ndarray(test_num_channels * test_record_length, dtype=numpy.int8)
    # Initialize with NaN so we can later verify all samples were overwritten by the driver.
    waveform.fill(float('nan'))
    session.configure_vertical(test_voltage, niscope.VerticalCoupling.AC)
    session.configure_horizontal_timing(50000000, test_record_length, 50.0, 1, True)
    with session.initiate():
        waveforms = session.channels[test_channels].fetch_into(waveform=waveform)

    for sample in waveform:
        assert not math.isnan(sample)
    assert len(waveforms) == test_num_channels

    for i in range(len(waveforms)):
        record_wfm = waveforms[i].samples
        assert len(record_wfm) == test_record_length
        for j in range(len(record_wfm)):
            assert record_wfm[j] == waveform[i * test_record_length + j]


def test_fetch_binary16_into(session):
    test_voltage = 1.0
    test_record_length = 2000
    test_channels = range(2)
    test_num_channels = 2
    waveform = numpy.ndarray(test_num_channels * test_record_length, dtype=numpy.int16)
    # Initialize with NaN so we can later verify all samples were overwritten by the driver.
    waveform.fill(float('nan'))
    session.configure_vertical(test_voltage, niscope.VerticalCoupling.AC)
    session.configure_horizontal_timing(50000000, test_record_length, 50.0, 1, True)
    with session.initiate():
        waveforms = session.channels[test_channels].fetch_into(waveform=waveform)

    for sample in waveform:
        assert not math.isnan(sample)
    assert len(waveforms) == test_num_channels

    for i in range(len(waveforms)):
        record_wfm = waveforms[i].samples
        assert len(record_wfm) == test_record_length
        for j in range(len(record_wfm)):
            assert record_wfm[j] == waveform[i * test_record_length + j]


def test_fetch_binary32_into(session):
    test_voltage = 1.0
    test_record_length = 2000
    test_channels = range(2)
    test_num_channels = 2
    waveform = numpy.ndarray(test_num_channels * test_record_length, dtype=numpy.int32)
    # Initialize with NaN so we can later verify all samples were overwritten by the driver.
    waveform.fill(float('nan'))
    session.configure_vertical(test_voltage, niscope.VerticalCoupling.AC)
    session.configure_horizontal_timing(50000000, test_record_length, 50.0, 1, True)
    with session.initiate():
        waveforms = session.channels[test_channels].fetch_into(waveform=waveform)

    for sample in waveform:
        assert not math.isnan(sample)
    assert len(waveforms) == test_num_channels

    for i in range(len(waveforms)):
        record_wfm = waveforms[i].samples
        assert len(record_wfm) == test_record_length
        for j in range(len(record_wfm)):
            assert record_wfm[j] == waveform[i * test_record_length + j]


def test_fetch_double_into(session):
    test_voltage = 1.0
    test_record_length = 2000
    test_channels = range(2)
    test_num_channels = 2
    waveform = numpy.ndarray(test_num_channels * test_record_length, dtype=numpy.float64)
    # Initialize with NaN so we can later verify all samples were overwritten by the driver.
    waveform.fill(float('nan'))
    session.configure_vertical(test_voltage, niscope.VerticalCoupling.AC)
    session.configure_horizontal_timing(50000000, test_record_length, 50.0, 1, True)
    with session.initiate():
        waveforms = session.channels[test_channels].fetch_into(waveform=waveform)

    for sample in waveform:
        assert not math.isnan(sample)
    assert len(waveforms) == test_num_channels

    for i in range(len(waveforms)):
        record_wfm = waveforms[i].samples
        assert len(record_wfm) == test_record_length
        for j in range(len(record_wfm)):
            assert record_wfm[j] == waveform[i * test_record_length + j]


def test_self_test(session):
    # We should not get an assert if self_test passes
    session.self_test()


def test_reset(session):
    deault_fetch_relative_to = session._fetch_relative_to
    assert deault_fetch_relative_to == niscope.FetchRelativeTo.PRETRIGGER
    session._fetch_relative_to = niscope.FetchRelativeTo.READ_POINTER
    non_default_acqusition_type = session._fetch_relative_to
    assert non_default_acqusition_type == niscope.FetchRelativeTo.READ_POINTER
    session.reset()
    assert session._fetch_relative_to == niscope.FetchRelativeTo.PRETRIGGER


def test_reset_device(session):
    deault_meas_time_histogram_high_time = session._meas_time_histogram_high_time
    assert deault_meas_time_histogram_high_time == 0.0005
    session._meas_time_histogram_high_time = 0.0010
    non_default_meas_time_histogram_high_time = session._meas_time_histogram_high_time
    assert non_default_meas_time_histogram_high_time == 0.0010
    session.reset_device()
    assert session._meas_time_histogram_high_time == 0.0005


def test_reset_with_defaults(session):
    deault_meas_time_histogram_high_time = session._meas_time_histogram_high_time
    assert deault_meas_time_histogram_high_time == 0.0005
    session._meas_time_histogram_high_time = 0.0010
    non_default_meas_time_histogram_high_time = session._meas_time_histogram_high_time
    assert non_default_meas_time_histogram_high_time == 0.0010
    session.reset_with_defaults()
    assert session._meas_time_histogram_high_time == 0.0005


def test_error_message():
    try:
        # We pass in an invalid model name to force going to error_message
        with niscope.Session('FakeDevice', False, True, 'Simulate=1, DriverSetup=Model:invalid_model; BoardType:PXIe'):
            assert False
    except niscope.Error as e:
        assert e.code == -1074118609
        assert e.description.find('Simulation does not support the selected model and board type.') != -1


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
    session.self_cal(niscope.Option.SELF_CALIBRATE_ALL_CHANNELS)


def test_probe_compensation_signal(session):
    session.probe_compensation_signal_start()
    session.probe_compensation_signal_stop()


def test_configure_horizontal_timing(session):
    session.configure_vertical(5.0, niscope.VerticalCoupling.DC)
    session.auto_setup()
    session.configure_horizontal_timing(10000000, 1000, 50.0, 1, True)
    session.trigger_modifier = niscope.TriggerModifier.AUTO
    session.configure_trigger_immediate()
    session.horz_record_length == 1000
    session.horz_sample_rate == 10000000


def test_configure_chan_characteristics(session):
    session.vertical_range = 4.0
    session.configure_chan_characteristics(50, 0)
    assert 50.0 == session.input_impedance


def test_filter_coefficients():
    with niscope.Session('FakeDevice', False, True, 'Simulate=1, DriverSetup=Model:5142; BoardType:PXI') as session:  # filter coefficients methods are available on devices with OSP
        assert [1.0] + [0.0] * 34 == session.get_equalization_filter_coefficients() # coefficients list should have 35 items
        try:
            filter_coefficients = [1.0, 0.0, 0.0]
            session.configure_equalization_filter_coefficients(filter_coefficients)
        except niscope.Error as e:
            assert e.code == -1074135024
        filter_coefficients = [0.01] * 35
        session.configure_equalization_filter_coefficients(filter_coefficients)
        assert filter_coefficients == session.get_equalization_filter_coefficients()

def test_send_software_trigger_edge(session):
    session.send_software_trigger_edge(niscope.WhichTrigger.ARM_REFERENCE)


def test_disable(session):
    assert session.allow_more_records_than_memory is False
    session.allow_more_records_than_memory = True
    session.disable()
    assert session.allow_more_records_than_memory is False


def test_configure_ref_levels(session):
    session._configure_ref_levels()
    assert 90.0 == session._meas_chan_high_ref_level


def test_configure_trigger_digital(session):
    session.configure_trigger_digital('VAL_RTSI_0')
    session.vertical_range = 5
    assert 'VAL_RTSI_0' == session.trigger_source


def test_configure_trigger_edge(session):
    assert niscope.TriggerSlope.POSITIVE == session.trigger_slope
    session.configure_trigger_edge('0', 0.0, niscope.TriggerCoupling.DC)
    session.commit()
    assert '0' == session.trigger_source
    assert niscope.TriggerCoupling.DC == session.trigger_coupling


def test_configure_trigger_hysteresis(session):
    session.configure_trigger_hysteresis('1', 0.0, 0.05, niscope.TriggerCoupling.DC)
    assert '1' == session.trigger_source
    assert niscope.TriggerCoupling.DC == session.trigger_coupling


def test_import_export_buffer(session):
    test_value_1 = 1
    test_value_2 = 5
    session.vertical_range = test_value_1
    assert session.vertical_range == test_value_1
    buffer = session.export_attribute_configuration_buffer()
    session.vertical_range = test_value_2
    assert session.vertical_range == test_value_2
    session.import_attribute_configuration_buffer(buffer)
    assert session.vertical_range == test_value_1


def test_import_export_file(session):
    test_value_1 = 1
    test_value_2 = 5
    path = tempfile.gettempdir() + 'test.txt'
    session.vertical_range = test_value_1
    assert session.vertical_range == test_value_1
    session.export_attribute_configuration_file(path)
    session.vertical_range = test_value_2
    assert session.vertical_range == test_value_2
    session.import_attribute_configuration_file(path)
    assert session.vertical_range == test_value_1


def test_configure_trigger_software(session):
    session.configure_trigger_software()


def test_configure_trigger_video():
    with niscope.Session('FakeDevice', False, True, 'Simulate=1, DriverSetup=Model:5124; BoardType:PXI') as session:  # Unable to invoke configure_trigger_video method on 5164
        session.configure_trigger_video('0', niscope.VideoSignalFormat.PAL, niscope.VideoTriggerEvent.FIELD1, niscope.VideoPolarity.POSITIVE, niscope.TriggerCoupling.DC)
        assert niscope.VideoSignalFormat.PAL == session.tv_trigger_signal_format
        assert niscope.VideoTriggerEvent.FIELD1 == session.tv_trigger_event
        assert niscope.VideoPolarity.POSITIVE == session.tv_trigger_polarity
        assert niscope.TriggerCoupling.DC == session.trigger_coupling


def test_configure_trigger_window(session):
    session.configure_trigger_window('1', 0, 5, niscope.TriggerWindowMode.ENTERING, niscope.TriggerCoupling.DC)
    assert '1' == session.trigger_source
    assert niscope.TriggerWindowMode.ENTERING == session.trigger_window_mode


