import fasteners
import math
import niscope
import numpy
import os
import pytest
import tempfile


# There are system tests below that need either a PXI-5124 or a PXI-5142 instead of the PXIe-5164 we use everywhere else
# because of specific capabilities on those models. Due to internal NI bug 969274, opening a simulated session to those models
# sometimes fails. As a workaround, the nimi-bot VMs are configured with one persistently simulated instrument of each kind respectively
# named "5124" and "5142". If you want to run these tests on your own system, you will need to create these two simulated
# instruments using MAX.
# In addition, we need a global lock in order to keep us from opening more than one session to the same simulated instrument
# at the same time. This is because NI-SCOPE (like other MI driver runtimes) disallow two simultaneous sessions to the same
# instrument, even when the instrument is simulated. This will impact the performance at which system tests run because we
# parallelize at the tox level :(.
daqmx_sim_5124_lock_file = os.path.join(tempfile.gettempdir(), 'daqmx_5124.lock')
daqmx_sim_5124_lock = fasteners.InterProcessLock(daqmx_sim_5124_lock_file)
daqmx_sim_5142_lock_file = os.path.join(tempfile.gettempdir(), 'daqmx_5142.lock')
daqmx_sim_5142_lock = fasteners.InterProcessLock(daqmx_sim_5142_lock_file)


@pytest.fixture(scope='function')
def session():
    with niscope.Session('FakeDevice', False, True, 'Simulate=1, DriverSetup=Model:5164; BoardType:PXIe') as simulated_session:
        yield simulated_session


@pytest.fixture(scope='function')
def session_5124():
    with daqmx_sim_5124_lock:
        with niscope.Session('5124') as simulated_session:  # 5124 is needed for video triggering
            yield simulated_session


@pytest.fixture(scope='function')
def session_5142():
    with daqmx_sim_5142_lock:
        with niscope.Session('5142') as simulated_session:  # 5142 is needed for OSP
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


def test_get_self_cal_last_date_time(session):
    last_cal = session.get_self_cal_last_date_and_time()
    assert last_cal.month == 3
    assert last_cal.day == 1
    assert last_cal.year == 1940
    assert last_cal.hour == 0
    assert last_cal.minute == 0


def test_get_ext_cal_last_date_time(session):
    last_cal = session.get_ext_cal_last_date_and_time()
    assert last_cal.month == 3
    assert last_cal.day == 1
    assert last_cal.year == 1940
    assert last_cal.hour == 0
    assert last_cal.minute == 0


def test_get_self_cal_last_temperature(session):
    last_cal_temp = session.get_self_cal_last_temp()
    assert last_cal_temp == 25


def test_get_ext_cal_last_temperature(session):
    last_cal_temp = session.get_ext_cal_last_temp()
    assert last_cal_temp == 25


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


def test_filter_coefficients(session_5142):
    assert [1.0] + [0.0] * 34 == session_5142.get_equalization_filter_coefficients()  # coefficients list should have 35 items
    try:
        filter_coefficients = [1.0, 0.0, 0.0]
        session_5142.configure_equalization_filter_coefficients(filter_coefficients)
    except niscope.Error as e:
        assert "Incorrect number of filter coefficients." in e.description
        assert e.code == -1074135024
    filter_coefficients = [0.01] * 35
    try:
        # TODO(marcoskirsch): The following should work. It doesn't due to internal NI-SCOPE driver bug 959625.
        #                     The bug is fixed in NI-SCOPE 20.0 which has not shipped at the time of this writing.
        #                     The workaround is to explicitly pass a channel rather than the default "" to the driver runtime
        #                     which should be equivalent to "all channels" (in the PXI-5142 case, that would be "0,1").
        session_5142.configure_equalization_filter_coefficients(filter_coefficients)
        assert False, "Looks like NI-SCOPE bug 959625 has been fixed. You can now remove this try/except clause"
    except niscope.errors.DriverError as e:
        assert e.code == -214202
    session_5142.channels[0].configure_equalization_filter_coefficients(filter_coefficients)
    assert filter_coefficients == session_5142.get_equalization_filter_coefficients()


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
    temp_file = tempfile.NamedTemporaryFile(suffix='.txt', delete=False)
    # NamedTemporaryFile() returns the file already opened, so we need to close it before we can use it
    temp_file.close()
    path = temp_file.name
    session.vertical_range = test_value_1
    assert session.vertical_range == test_value_1
    session.export_attribute_configuration_file(path)
    session.vertical_range = test_value_2
    assert session.vertical_range == test_value_2
    session.import_attribute_configuration_file(path)
    assert session.vertical_range == test_value_1
    os.remove(path)


def test_configure_trigger_software(session):
    session.configure_trigger_software()


def test_configure_trigger_video(session_5124):
    session_5124.configure_trigger_video('0', niscope.VideoSignalFormat.PAL, niscope.VideoTriggerEvent.FIELD1, niscope.VideoPolarity.POSITIVE, niscope.TriggerCoupling.DC)
    assert niscope.VideoSignalFormat.PAL == session_5124.tv_trigger_signal_format
    assert niscope.VideoTriggerEvent.FIELD1 == session_5124.tv_trigger_event
    assert niscope.VideoPolarity.POSITIVE == session_5124.tv_trigger_polarity
    assert niscope.TriggerCoupling.DC == session_5124.trigger_coupling


def test_configure_trigger_window(session):
    session.configure_trigger_window('1', 0, 5, niscope.TriggerWindowMode.ENTERING, niscope.TriggerCoupling.DC)
    assert '1' == session.trigger_source
    assert niscope.TriggerWindowMode.ENTERING == session.trigger_window_mode


