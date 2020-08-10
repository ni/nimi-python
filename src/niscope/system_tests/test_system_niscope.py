import fasteners
import hightime
import math
import niscope
import numpy
import os
import pytest
import tempfile


instruments = ['FakeDevice1', 'FakeDevice2']
# TODO(sbethur): Use `get_channel_names` when #1402 is fixed
test_channels = 'FakeDevice2/0,FakeDevice1/1'


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
def single_instrument_session():
    with niscope.Session('FakeDevice', False, True, 'Simulate=1, DriverSetup=Model:5164; BoardType:PXIe') as simulated_session:
        yield simulated_session


@pytest.fixture(scope='function')
def session():
    with niscope.Session(','.join(instruments), False, True, 'Simulate=1, DriverSetup=Model:5164; BoardType:PXIe') as simulated_session:
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
    trigger_source = '/{0}/NISCOPE_VAL_IMMEDIATE'.format(instruments[1])
    session.acq_arm_source = trigger_source
    assert trigger_source == session.acq_arm_source


# Basic usability tests
def test_read(session):
    test_voltage = 1.0
    test_record_length = 2000
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
    test_num_channels = 2
    session.configure_vertical(test_voltage, niscope.VerticalCoupling.AC)
    session.configure_horizontal_timing(50000000, test_record_length, 50.0, 1, True)
    with session.initiate():
        waveforms = session.channels[test_channels].fetch()
    assert len(waveforms) == test_num_channels
    for i in range(len(waveforms)):
        assert len(waveforms[i].samples) == test_record_length


def test_fetch_array_measurement(session):
    test_voltage = 1.0
    test_record_length = 2000
    test_num_channels = 2
    test_num_records = 3
    session.configure_vertical(test_voltage, niscope.VerticalCoupling.AC)
    session.configure_horizontal_timing(50000000, test_record_length, 50.0, test_num_records, True)
    with session.initiate():
        waveforms = session.channels[test_channels].fetch_array_measurement(niscope.enums.ArrayMeasurement.ARRAY_GAIN)
    assert len(waveforms) == test_num_channels * test_num_records
    for i in range(len(waveforms)):
        assert len(waveforms[i].samples) == test_record_length


def test_fetch_binary8_into(session):
    test_voltage = 1.0
    test_record_length = 2000
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


def test_fetch_measurement_stats(session):
    test_voltage = 1.0
    test_record_length = 1000
    test_num_channels = 2
    test_num_records = 3
    session.configure_vertical(test_voltage, niscope.VerticalCoupling.AC)
    session.configure_horizontal_timing(50000000, test_record_length, 50.0, test_num_records, True)
    with session.initiate():
        measurement_stats = session.channels[test_channels].fetch_measurement_stats(niscope.enums.ScalarMeasurement.NO_MEASUREMENT, 5.0)

    assert len(measurement_stats) == test_num_channels * test_num_records
    for stat in measurement_stats:
        assert stat.result == 0.0


def test_clear_waveform_measurement_stats(session):
    test_voltage = 1.0
    test_record_length = 1000
    test_num_records = 1
    session.configure_vertical(test_voltage, niscope.VerticalCoupling.AC)
    session.configure_horizontal_timing(50000000, test_record_length, 50.0, test_num_records, True)
    with session.initiate():
        uncleared_stats = session.channels[test_channels].fetch_measurement_stats(niscope.enums.ScalarMeasurement.FREQUENCY, 5.0)
        uncleared_stats_2 = session.channels[test_channels].fetch_measurement_stats(niscope.enums.ScalarMeasurement.FREQUENCY, 5.0)
        session.channels[test_channels].clear_waveform_measurement_stats(niscope.enums.ClearableMeasurement.FREQUENCY)
        cleared_stats = session.channels[test_channels].fetch_measurement_stats(niscope.enums.ScalarMeasurement.FREQUENCY, 5.0)

    # The principle here is using consistent behavior (i.e. if stats are fetched twice on a single record/channel measurement in a row, it will always be the same)
    # to demonstrate that clearing the stats does in fact cause a measurable change.
    assert uncleared_stats[0].result == uncleared_stats_2[0].result
    assert uncleared_stats[0].stdev == uncleared_stats_2[0].stdev
    assert uncleared_stats[0].mean == uncleared_stats_2[0].mean
    assert uncleared_stats[0].min_val == uncleared_stats_2[0].min_val
    assert uncleared_stats[0].max_val == uncleared_stats_2[0].max_val
    assert uncleared_stats[0].num_in_stats == uncleared_stats_2[0].num_in_stats
    assert uncleared_stats[0].num_in_stats != cleared_stats[0].num_in_stats


def test_waveform_processing(session):
    test_voltage = 1.0
    test_record_length = 1000
    test_num_channels = 2
    test_num_records = 3
    session.configure_vertical(test_voltage, niscope.VerticalCoupling.AC)
    session.configure_horizontal_timing(50000000, test_record_length, 50.0, test_num_records, True)
    with session.initiate():
        session.add_waveform_processing(niscope.enums.ArrayMeasurement.DERIVATIVE)
        processed_waveforms = session.channels[test_channels].fetch_measurement_stats(niscope.enums.ScalarMeasurement.MID_REF_VOLTS, 5.0)
        session.clear_waveform_processing()
        unprocessed_waveforms = session.channels[test_channels].fetch_measurement_stats(niscope.enums.ScalarMeasurement.MID_REF_VOLTS, 5.0)

    assert len(processed_waveforms) == test_num_channels * test_num_records
    assert len(unprocessed_waveforms) == test_num_channels * test_num_records
    # Here the idea is to leave a large margin to not test too specifically for any returned values but to demonstrate that the waveform processing does
    # undeniably cause a consistent shift in the values returned. The "0" exception for processed is due to the nature of derivatives -- if two samples
    # next to each other are identical, the derivative will be 0.
    for processed, unprocessed in zip(processed_waveforms, unprocessed_waveforms):
        assert abs(unprocessed.result) < 1
        assert abs(processed.result) > 1 or processed.result == 0


def test_measurement_stats_str(session):
    test_voltage = 1.0
    test_record_length = 1000
    test_num_records = 1
    session.configure_vertical(test_voltage, niscope.VerticalCoupling.AC)
    session.configure_horizontal_timing(50000000, test_record_length, 50.0, test_num_records, True)
    with session.initiate():
        measurement_stat = session.channels[test_channels].fetch_measurement_stats(niscope.enums.ScalarMeasurement.NO_MEASUREMENT, 5.0)

    assert isinstance(measurement_stat[0].__str__(), str)
    assert isinstance(measurement_stat[0].__repr__(), str)


def test_get_self_cal_last_date_time(single_instrument_session):
    last_cal = single_instrument_session.get_self_cal_last_date_and_time()
    assert last_cal.month == 12
    assert last_cal.day == 21
    assert last_cal.year == 1999
    assert last_cal.hour == 0
    assert last_cal.minute == 0


def test_get_ext_cal_last_date_time(single_instrument_session):
    last_cal = single_instrument_session.get_ext_cal_last_date_and_time()
    assert last_cal.month == 12
    assert last_cal.day == 21
    assert last_cal.year == 1999
    assert last_cal.hour == 0
    assert last_cal.minute == 0


def test_get_self_cal_last_temperature(single_instrument_session):
    last_cal_temp = single_instrument_session.get_self_cal_last_temp()
    assert last_cal_temp == 25


def test_get_ext_cal_last_temperature(single_instrument_session):
    last_cal_temp = single_instrument_session.get_ext_cal_last_temp()
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
    deault_meas_time_histogram_high_time = session.meas_time_histogram_high_time
    assert deault_meas_time_histogram_high_time == hightime.timedelta(microseconds=500)
    session.meas_time_histogram_high_time = hightime.timedelta(microseconds=1000)
    non_default_meas_time_histogram_high_time = session.meas_time_histogram_high_time
    assert non_default_meas_time_histogram_high_time == hightime.timedelta(microseconds=1000)
    session.reset_device()
    assert session.meas_time_histogram_high_time == hightime.timedelta(microseconds=500)


def test_reset_with_defaults(session):
    deault_meas_time_histogram_high_time = session.meas_time_histogram_high_time
    assert deault_meas_time_histogram_high_time == hightime.timedelta(microseconds=500)
    session.meas_time_histogram_high_time = hightime.timedelta(microseconds=1000)
    non_default_meas_time_histogram_high_time = session.meas_time_histogram_high_time
    assert non_default_meas_time_histogram_high_time == hightime.timedelta(microseconds=1000)
    session.reset_device()
    assert session.meas_time_histogram_high_time == hightime.timedelta(microseconds=500)


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
    session_5142.configure_equalization_filter_coefficients(filter_coefficients)
    assert filter_coefficients == session_5142.get_equalization_filter_coefficients()


def test_send_software_trigger_edge(session):
    session.send_software_trigger_edge(niscope.WhichTrigger.ARM_REFERENCE)


def test_disable(session):
    assert session.allow_more_records_than_memory is False
    session.allow_more_records_than_memory = True
    session.disable()
    assert session.allow_more_records_than_memory is False


# Basic configuration tests
def test_configure_ref_levels(single_instrument_session):
    single_instrument_session._configure_ref_levels()
    assert 90.0 == single_instrument_session.meas_chan_high_ref_level


def test_configure_trigger_digital(session):
    trigger_source = '/{0}/VAL_RTSI_0'.format(instruments[1])
    session.configure_trigger_digital(trigger_source)
    session.vertical_range = 5
    assert trigger_source == session.trigger_source


def test_configure_trigger_edge(session):
    assert niscope.TriggerSlope.POSITIVE == session.trigger_slope
    trigger_source = '{0}/0'.format(instruments[1])
    session.configure_trigger_edge(trigger_source, 0.0, niscope.TriggerCoupling.DC)
    session.commit()
    assert trigger_source == session.trigger_source
    assert niscope.TriggerCoupling.DC == session.trigger_coupling


def test_configure_trigger_hysteresis(session):
    trigger_source = '{0}/1'.format(instruments[1])
    session.configure_trigger_hysteresis(trigger_source, 0.0, 0.05, niscope.TriggerCoupling.DC)
    assert trigger_source == session.trigger_source
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
    trigger_source = '{0}/1'.format(instruments[1])
    session.configure_trigger_window(trigger_source, 0, 5, niscope.TriggerWindowMode.ENTERING, niscope.TriggerCoupling.DC)
    assert trigger_source == session.trigger_source
    assert niscope.TriggerWindowMode.ENTERING == session.trigger_window_mode


