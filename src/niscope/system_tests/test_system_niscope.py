import collections
import fasteners
import grpc
import hightime
import math
import niscope
import numpy
import os
import pathlib
import pytest
import subprocess
import tempfile
import time


class SystemTests:
    _instruments = ['FakeDevice1', 'FakeDevice2']
    # TODO(sbethur): Use `get_channel_names` when #1402 is fixed
    _test_channels = 'FakeDevice2/0,FakeDevice1/1'

    # There are system tests below that need either a PXI-5124 or a PXI-5142 instead of the PXIe-5164 we use everywhere else
    # because of specific capabilities on those models. Due to internal NI bug 969274, opening a simulated session to those models
    # sometimes fails. As a workaround, the nimi-bot VMs are configured with one persistently simulated instrument of each kind respectively
    # named "5124" and "5142". If you want to run these tests on your own system, you will need to create these two simulated
    # instruments using MAX.
    # In addition, we need a global lock in order to keep us from opening more than one session to the same simulated instrument
    # at the same time. This is because NI-SCOPE (like other MI driver runtimes) disallow two simultaneous sessions to the same
    # instrument, even when the instrument is simulated. This will impact the performance at which system tests run because we
    # parallelize at the tox level :(.
    _daqmx_sim_5124_lock_file = os.path.join(tempfile.gettempdir(), 'daqmx_5124.lock')
    _daqmx_sim_5124_lock = fasteners.InterProcessLock(_daqmx_sim_5124_lock_file)
    _daqmx_sim_5142_lock_file = os.path.join(tempfile.gettempdir(), 'daqmx_5142.lock')
    _daqmx_sim_5142_lock = fasteners.InterProcessLock(_daqmx_sim_5142_lock_file)

    # Attribute tests
    def test_vi_boolean_attribute(self, multi_instrument_session):
        multi_instrument_session.allow_more_records_than_memory = False
        default_option = multi_instrument_session.allow_more_records_than_memory
        assert default_option is False

    def test_vi_string_attribute(self, multi_instrument_session):
        trigger_source = '/{0}/NISCOPE_VAL_IMMEDIATE'.format(self._instruments[1])
        multi_instrument_session.acq_arm_source = trigger_source
        assert trigger_source == multi_instrument_session.acq_arm_source

    # Basic usability tests
    def test_read(self, multi_instrument_session):
        test_voltage = 1.0
        test_record_length = 2000
        test_num_channels = 2
        test_num_records = 3
        multi_instrument_session.configure_vertical(test_voltage, niscope.VerticalCoupling.AC)
        multi_instrument_session.configure_horizontal_timing(50000000, test_record_length, 50.0, test_num_records, True)
        waveforms = multi_instrument_session.channels[self._test_channels].read(num_samples=test_record_length, num_records=test_num_records)
        assert len(waveforms) == test_num_channels * test_num_records
        for i in range(len(waveforms)):
            assert len(waveforms[i].samples) == test_record_length

    def test_fetch(self, multi_instrument_session):
        test_voltage = 1.0
        test_record_length = 2000
        test_num_channels = 2
        test_starting_record_number = 2
        test_num_records_to_acquire = 5
        test_num_records_to_fetch = test_num_records_to_acquire - test_starting_record_number
        multi_instrument_session.configure_vertical(test_voltage, niscope.VerticalCoupling.AC)
        multi_instrument_session.configure_horizontal_timing(50000000, test_record_length, 50.0, test_num_records_to_acquire, True)
        with multi_instrument_session.initiate():
            waveforms = multi_instrument_session.channels[self._test_channels].fetch(
                num_samples=test_record_length,
                record_number=test_starting_record_number,
                num_records=test_num_records_to_fetch)
        assert len(waveforms) == test_num_channels * test_num_records_to_fetch
        expected_channels = self._test_channels.split(',') * test_num_records_to_fetch
        expected_records = [2, 2, 3, 3, 4, 4]
        for i in range(len(waveforms)):
            assert len(waveforms[i].samples) == test_record_length
            assert waveforms[i].channel == expected_channels[i]
            assert waveforms[i].record == expected_records[i]

    def test_fetch_defaults(self, multi_instrument_session):
        test_voltage = 1.0
        test_record_length = 2000
        test_num_channels = 2
        multi_instrument_session.configure_vertical(test_voltage, niscope.VerticalCoupling.AC)
        multi_instrument_session.configure_horizontal_timing(50000000, test_record_length, 50.0, 1, True)
        with multi_instrument_session.initiate():
            waveforms = multi_instrument_session.channels[self._test_channels].fetch()
        assert len(waveforms) == test_num_channels
        for i in range(len(waveforms)):
            assert len(waveforms[i].samples) == test_record_length

    @pytest.fixture(params=[(1000, 1000), (2000, 2000), (3000, 2000)], ids=["less_than_actual", "equal_to_actual", "greater_than_actual"])
    def measurement_wfm_length(self, request):
        MeasWfmLength = collections.namedtuple('MeasurementWaveformLength', ['passed_in', 'expected'])
        return MeasWfmLength(passed_in=request.param[0], expected=request.param[1])

    def test_fetch_array_measurement(self, multi_instrument_session, measurement_wfm_length):
        test_voltage = 1.0
        test_record_length = 1000
        test_num_channels = 2
        test_meas_wfm_length = measurement_wfm_length.passed_in
        test_array_meas_function = niscope.ArrayMeasurement.ARRAY_GAIN
        test_starting_record_number = 2
        test_num_records_to_acquire = 5
        test_num_records_to_fetch = test_num_records_to_acquire - test_starting_record_number
        multi_instrument_session.configure_vertical(test_voltage, niscope.VerticalCoupling.AC)
        multi_instrument_session.configure_horizontal_timing(50000000, test_record_length, 50.0, test_num_records_to_acquire, True)

        with multi_instrument_session.initiate():
            waveforms = multi_instrument_session.channels[self._test_channels].fetch_array_measurement(
                array_meas_function=test_array_meas_function,
                meas_wfm_size=test_meas_wfm_length,
                relative_to=niscope.FetchRelativeTo.PRETRIGGER,
                offset=5,
                record_number=test_starting_record_number,
                num_records=test_num_records_to_fetch,
                meas_num_samples=2000,
                timeout=hightime.timedelta(seconds=4))

        assert len(waveforms) == test_num_channels * test_num_records_to_fetch
        expected_channels = self._test_channels.split(',') * test_num_records_to_fetch
        expected_records = [2, 2, 3, 3, 4, 4]
        for i in range(len(waveforms)):
            assert len(waveforms[i].samples) == measurement_wfm_length.expected
            assert waveforms[i].channel == expected_channels[i]
            assert waveforms[i].record == expected_records[i]

    def test_fetch_array_measurement_defaults(self, multi_instrument_session):
        test_voltage = 1.0
        test_record_length = 1000
        test_num_channels = 2
        test_num_records = 3
        test_array_meas_function = niscope.ArrayMeasurement.ARRAY_GAIN

        multi_instrument_session.configure_vertical(test_voltage, niscope.VerticalCoupling.AC)
        multi_instrument_session.configure_horizontal_timing(50000000, test_record_length, 50.0, test_num_records, True)

        with multi_instrument_session.initiate():
            waveforms = multi_instrument_session.channels[self._test_channels].fetch_array_measurement(
                array_meas_function=test_array_meas_function)

        assert len(waveforms) == test_num_channels * test_num_records
        for i in range(len(waveforms)):
            assert len(waveforms[i].samples) == test_record_length

    def test_fetch_measurement_stats(self, multi_instrument_session):
        test_voltage = 1.0
        test_record_length = 1000
        test_num_channels = 2
        test_num_records = 3
        test_starting_record_number = 2
        test_num_records_to_acquire = 5
        test_num_records_to_fetch = test_num_records_to_acquire - test_starting_record_number
        multi_instrument_session.configure_vertical(test_voltage, niscope.VerticalCoupling.AC)
        multi_instrument_session.configure_horizontal_timing(50000000, test_record_length, 50.0, test_num_records_to_acquire, True)
        with multi_instrument_session.initiate():
            measurement_stats = multi_instrument_session.channels[self._test_channels].fetch_measurement_stats(
                scalar_meas_function=niscope.enums.ScalarMeasurement.NO_MEASUREMENT,
                relative_to=niscope.FetchRelativeTo.PRETRIGGER,
                offset=5,
                record_number=test_starting_record_number,
                num_records=test_num_records_to_fetch,
                timeout=hightime.timedelta(seconds=4))

        assert len(measurement_stats) == test_num_channels * test_num_records
        expected_channels = self._test_channels.split(',') * test_num_records_to_fetch
        expected_records = [2, 2, 3, 3, 4, 4]
        for i in range(len(measurement_stats)):
            assert measurement_stats[i].result == 0.0
            assert measurement_stats[i].channel == expected_channels[i]
            assert measurement_stats[i].record == expected_records[i]

    def test_fetch_measurement_stats_defaults(self, multi_instrument_session):
        test_voltage = 1.0
        test_record_length = 1000
        test_num_channels = 2
        test_num_records = 3
        multi_instrument_session.configure_vertical(test_voltage, niscope.VerticalCoupling.AC)
        multi_instrument_session.configure_horizontal_timing(50000000, test_record_length, 50.0, test_num_records, True)
        with multi_instrument_session.initiate():
            measurement_stats = multi_instrument_session.channels[self._test_channels].fetch_measurement_stats(niscope.enums.ScalarMeasurement.NO_MEASUREMENT)

        assert len(measurement_stats) == test_num_channels * test_num_records
        for stat in measurement_stats:
            assert stat.result == 0.0

    def test_filter_coefficients(self, session_5142):
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

    def test_configure_trigger_video(self, session_5124):
        session_5124.configure_trigger_video('0', niscope.VideoSignalFormat.PAL, niscope.VideoTriggerEvent.FIELD1, niscope.VideoPolarity.POSITIVE, niscope.TriggerCoupling.DC)
        assert niscope.VideoSignalFormat.PAL == session_5124.tv_trigger_signal_format
        assert niscope.VideoTriggerEvent.FIELD1 == session_5124.tv_trigger_event
        assert niscope.VideoPolarity.POSITIVE == session_5124.tv_trigger_polarity
        assert niscope.TriggerCoupling.DC == session_5124.trigger_coupling

    def test_clear_waveform_measurement_stats(self, multi_instrument_session):
        test_voltage = 1.0
        test_record_length = 1000
        test_num_records = 1
        multi_instrument_session.configure_vertical(test_voltage, niscope.VerticalCoupling.AC)
        multi_instrument_session.configure_horizontal_timing(50000000, test_record_length, 50.0, test_num_records, True)
        with multi_instrument_session.initiate():
            uncleared_stats = multi_instrument_session.channels[self._test_channels].fetch_measurement_stats(niscope.enums.ScalarMeasurement.FREQUENCY)
            uncleared_stats_2 = multi_instrument_session.channels[self._test_channels].fetch_measurement_stats(niscope.enums.ScalarMeasurement.FREQUENCY)
            multi_instrument_session.channels[self._test_channels].clear_waveform_measurement_stats(niscope.enums.ClearableMeasurement.FREQUENCY)
            cleared_stats = multi_instrument_session.channels[self._test_channels].fetch_measurement_stats(niscope.enums.ScalarMeasurement.FREQUENCY)

        # The principle here is using consistent behavior (i.e. if stats are fetched twice on a single record/channel measurement in a row, it will always be the same)
        # to demonstrate that clearing the stats does in fact cause a measurable change.
        assert uncleared_stats[0].result == uncleared_stats_2[0].result
        assert uncleared_stats[0].stdev == uncleared_stats_2[0].stdev
        assert uncleared_stats[0].mean == uncleared_stats_2[0].mean
        assert uncleared_stats[0].min_val == uncleared_stats_2[0].min_val
        assert uncleared_stats[0].max_val == uncleared_stats_2[0].max_val
        assert uncleared_stats[0].num_in_stats == uncleared_stats_2[0].num_in_stats
        assert uncleared_stats[0].num_in_stats != cleared_stats[0].num_in_stats

    def test_waveform_processing(self, multi_instrument_session):
        test_voltage = 1.0
        test_record_length = 1000
        test_num_channels = 2
        test_num_records = 3
        multi_instrument_session.configure_vertical(test_voltage, niscope.VerticalCoupling.AC)
        multi_instrument_session.configure_horizontal_timing(50000000, test_record_length, 50.0, test_num_records, True)
        with multi_instrument_session.initiate():
            multi_instrument_session.add_waveform_processing(niscope.enums.ArrayMeasurement.DERIVATIVE)
            processed_waveforms = multi_instrument_session.channels[self._test_channels].fetch_measurement_stats(niscope.enums.ScalarMeasurement.MID_REF_VOLTS)
            multi_instrument_session.clear_waveform_processing()
            unprocessed_waveforms = multi_instrument_session.channels[self._test_channels].fetch_measurement_stats(niscope.enums.ScalarMeasurement.MID_REF_VOLTS)

        assert len(processed_waveforms) == test_num_channels * test_num_records
        assert len(unprocessed_waveforms) == test_num_channels * test_num_records
        # Here the idea is to leave a large margin to not test too specifically for any returned values but to demonstrate that the waveform processing does
        # undeniably cause a consistent shift in the values returned. The "0" exception for processed is due to the nature of derivatives -- if two samples
        # next to each other are identical, the derivative will be 0.
        for processed, unprocessed in zip(processed_waveforms, unprocessed_waveforms):
            assert abs(unprocessed.result) < 1
            assert abs(processed.result) > 1 or processed.result == 0

    def test_measurement_stats_str(self, multi_instrument_session):
        test_voltage = 1.0
        test_record_length = 1000
        test_num_records = 1
        multi_instrument_session.configure_vertical(test_voltage, niscope.VerticalCoupling.AC)
        multi_instrument_session.configure_horizontal_timing(50000000, test_record_length, 50.0, test_num_records, True)
        with multi_instrument_session.initiate():
            measurement_stat = multi_instrument_session.channels[self._test_channels].fetch_measurement_stats(niscope.enums.ScalarMeasurement.NO_MEASUREMENT)

        assert isinstance(measurement_stat[0].__str__(), str)
        assert isinstance(measurement_stat[0].__repr__(), str)

    def test_self_test(self, multi_instrument_session):
        # We should not get an assert if self_test passes
        multi_instrument_session.self_test()

    def test_reset(self, multi_instrument_session):
        default_fetch_relative_to = multi_instrument_session._fetch_relative_to
        assert default_fetch_relative_to == niscope.FetchRelativeTo.PRETRIGGER
        multi_instrument_session._fetch_relative_to = niscope.FetchRelativeTo.READ_POINTER
        non_default_acquisition_type = multi_instrument_session._fetch_relative_to
        assert non_default_acquisition_type == niscope.FetchRelativeTo.READ_POINTER
        multi_instrument_session.reset()
        assert multi_instrument_session._fetch_relative_to == niscope.FetchRelativeTo.PRETRIGGER

    def test_reset_device(self, multi_instrument_session):
        default_meas_time_histogram_high_time = multi_instrument_session.meas_time_histogram_high_time
        assert default_meas_time_histogram_high_time == hightime.timedelta(microseconds=500)
        multi_instrument_session.meas_time_histogram_high_time = hightime.timedelta(microseconds=1000)
        non_default_meas_time_histogram_high_time = multi_instrument_session.meas_time_histogram_high_time
        assert non_default_meas_time_histogram_high_time == hightime.timedelta(microseconds=1000)
        multi_instrument_session.reset_device()
        assert multi_instrument_session.meas_time_histogram_high_time == hightime.timedelta(microseconds=500)

    def test_reset_with_defaults(self, multi_instrument_session):
        default_meas_time_histogram_high_time = multi_instrument_session.meas_time_histogram_high_time
        assert default_meas_time_histogram_high_time == hightime.timedelta(microseconds=500)
        multi_instrument_session.meas_time_histogram_high_time = hightime.timedelta(microseconds=1000)
        non_default_meas_time_histogram_high_time = multi_instrument_session.meas_time_histogram_high_time
        assert non_default_meas_time_histogram_high_time == hightime.timedelta(microseconds=1000)
        multi_instrument_session.reset_device()
        assert multi_instrument_session.meas_time_histogram_high_time == hightime.timedelta(microseconds=500)

    def test_get_error(self, multi_instrument_session):
        try:
            multi_instrument_session.instrument_model = ''
            assert False
        except niscope.Error as e:
            assert e.code == -1074135027  # Error : Attribute is read-only.
            assert e.description.find('Attribute is read-only.') != -1

    def test_acquisition_status(self, multi_instrument_session):
        assert multi_instrument_session.acquisition_status() == niscope.AcquisitionStatus.COMPLETE

    def test_self_cal(self, multi_instrument_session):
        multi_instrument_session.self_cal(niscope.Option.SELF_CALIBRATE_ALL_CHANNELS)

    def test_probe_compensation_signal(self, multi_instrument_session):
        multi_instrument_session.probe_compensation_signal_start()
        multi_instrument_session.probe_compensation_signal_stop()

    def test_configure_horizontal_timing(self, multi_instrument_session):
        multi_instrument_session.configure_vertical(5.0, niscope.VerticalCoupling.DC)
        multi_instrument_session.auto_setup()
        multi_instrument_session.configure_horizontal_timing(10000000, 1000, 50.0, 1, True)
        multi_instrument_session.trigger_modifier = niscope.TriggerModifier.AUTO
        multi_instrument_session.configure_trigger_immediate()
        multi_instrument_session.horz_record_length == 1000
        multi_instrument_session.horz_sample_rate == 10000000

    def test_configure_chan_characteristics(self, multi_instrument_session):
        multi_instrument_session.vertical_range = 4.0
        multi_instrument_session.configure_chan_characteristics(50, 0)
        assert 50.0 == multi_instrument_session.input_impedance

    def test_send_software_trigger_edge(self, multi_instrument_session):
        multi_instrument_session.send_software_trigger_edge(niscope.WhichTrigger.ARM_REFERENCE)

    def test_disable(self, multi_instrument_session):
        assert multi_instrument_session.allow_more_records_than_memory is False
        multi_instrument_session.allow_more_records_than_memory = True
        multi_instrument_session.disable()
        assert multi_instrument_session.allow_more_records_than_memory is False

    # Basic configuration tests
    def test_configure_trigger_digital(self, multi_instrument_session):
        trigger_source = '/{0}/VAL_RTSI_0'.format(self._instruments[1])
        multi_instrument_session.configure_trigger_digital(trigger_source)
        multi_instrument_session.vertical_range = 5
        assert trigger_source == multi_instrument_session.trigger_source

    def test_configure_trigger_edge(self, multi_instrument_session):
        assert niscope.TriggerSlope.POSITIVE == multi_instrument_session.trigger_slope
        trigger_source = '{0}/0'.format(self._instruments[1])
        multi_instrument_session.configure_trigger_edge(trigger_source, 0.0, niscope.TriggerCoupling.DC)
        multi_instrument_session.commit()
        assert trigger_source == multi_instrument_session.trigger_source
        assert niscope.TriggerCoupling.DC == multi_instrument_session.trigger_coupling

    def test_configure_trigger_hysteresis(self, multi_instrument_session):
        trigger_source = '{0}/1'.format(self._instruments[1])
        multi_instrument_session.configure_trigger_hysteresis(trigger_source, 0.0, 0.05, niscope.TriggerCoupling.DC)
        assert trigger_source == multi_instrument_session.trigger_source
        assert niscope.TriggerCoupling.DC == multi_instrument_session.trigger_coupling

    def test_import_export_buffer(self, multi_instrument_session):
        test_value_1 = 1
        test_value_2 = 5
        multi_instrument_session.vertical_range = test_value_1
        assert multi_instrument_session.vertical_range == test_value_1
        buffer = multi_instrument_session.export_attribute_configuration_buffer()
        multi_instrument_session.vertical_range = test_value_2
        assert multi_instrument_session.vertical_range == test_value_2
        multi_instrument_session.import_attribute_configuration_buffer(buffer)
        assert multi_instrument_session.vertical_range == test_value_1

    def test_import_export_file(self, multi_instrument_session):
        test_value_1 = 1
        test_value_2 = 5
        temp_file = tempfile.NamedTemporaryFile(suffix='.txt', delete=False)
        # NamedTemporaryFile() returns the file already opened, so we need to close it before we can use it
        temp_file.close()
        path = temp_file.name
        multi_instrument_session.vertical_range = test_value_1
        assert multi_instrument_session.vertical_range == test_value_1
        multi_instrument_session.export_attribute_configuration_file(path)
        multi_instrument_session.vertical_range = test_value_2
        assert multi_instrument_session.vertical_range == test_value_2
        multi_instrument_session.import_attribute_configuration_file(path)
        assert multi_instrument_session.vertical_range == test_value_1
        os.remove(path)

    def test_configure_trigger_software(self, multi_instrument_session):
        multi_instrument_session.configure_trigger_software()

    def test_configure_trigger_window(self, multi_instrument_session):
        trigger_source = '{0}/1'.format(self._instruments[1])
        multi_instrument_session.configure_trigger_window(trigger_source, 0, 5, niscope.TriggerWindowMode.ENTERING, niscope.TriggerCoupling.DC)
        assert trigger_source == multi_instrument_session.trigger_source
        assert niscope.TriggerWindowMode.ENTERING == multi_instrument_session.trigger_window_mode


class TestLibrary(SystemTests):
    @pytest.fixture(scope='function')
    def single_instrument_session(self):
        with niscope.Session('FakeDevice', False, True, 'Simulate=1, DriverSetup=Model:5164; BoardType:PXIe') as simulated_session:
            yield simulated_session

    @pytest.fixture(scope='function')
    def multi_instrument_session(self):
        with niscope.Session(','.join(self._instruments), False, True, 'Simulate=1, DriverSetup=Model:5164; BoardType:PXIe') as simulated_session:
            yield simulated_session

    @pytest.fixture(scope='function')
    def session_5124(self):
        with self._daqmx_sim_5124_lock:
            with niscope.Session('5124') as simulated_session:  # 5124 is needed for video triggering
                yield simulated_session

    @pytest.fixture(scope='function')
    def session_5142(self):
        with self._daqmx_sim_5142_lock:
            with niscope.Session('5142') as simulated_session:  # 5142 is needed for OSP
                yield simulated_session

    @pytest.fixture(params=[numpy.int8, numpy.int16, numpy.int32, numpy.float64])
    def fetch_waveform_type(self, request):
        return request.param

    def test_fetch_into(self, multi_instrument_session, fetch_waveform_type):
        test_voltage = 1.0
        test_record_length = 2000
        test_num_channels = 2
        test_starting_record_number = 2
        test_num_records_to_acquire = 5
        test_num_records_to_fetch = test_num_records_to_acquire - test_starting_record_number
        waveform = numpy.ndarray(test_num_channels * test_num_records_to_fetch * test_record_length, dtype=fetch_waveform_type)
        # Initialize with NaN so we can later verify all samples were overwritten by the driver.
        waveform.fill(float('nan'))
        multi_instrument_session.configure_vertical(test_voltage, niscope.VerticalCoupling.AC)
        multi_instrument_session.configure_horizontal_timing(50000000, test_record_length, 50.0, test_num_records_to_acquire, True)
        with multi_instrument_session.initiate():
            waveforms = multi_instrument_session.channels[self._test_channels].fetch_into(
                waveform=waveform,
                record_number=test_starting_record_number,
                num_records=test_num_records_to_fetch)

        for sample in waveform:
            assert not math.isnan(sample)
        assert len(waveforms) == test_num_channels * test_num_records_to_fetch

        expected_channels = self._test_channels.split(',') * test_num_records_to_fetch
        expected_records = [2, 2, 3, 3, 4, 4]
        for i in range(len(waveforms)):
            record_wfm = waveforms[i].samples
            assert len(record_wfm) == test_record_length
            for j in range(len(record_wfm)):
                assert record_wfm[j] == waveform[i * test_record_length + j]
            assert waveforms[i].channel == expected_channels[i]
            assert waveforms[i].record == expected_records[i]

    def test_error_message(self):
        try:
            # We pass in an invalid model name to force going to error_message
            with niscope.Session('FakeDevice', False, True, 'Simulate=1, DriverSetup=Model:invalid_model; BoardType:PXIe'):
                assert False
        except niscope.Error as e:
            assert e.code == -1074118609
            assert e.description.find('Simulation does not support the selected model and board type.') != -1

    def test_get_self_cal_last_date_time(self, single_instrument_session):
        last_cal = single_instrument_session.get_self_cal_last_date_and_time()
        assert last_cal.month == 12
        assert last_cal.day == 21
        assert last_cal.year == 1999
        assert last_cal.hour == 0
        assert last_cal.minute == 0

    def test_get_ext_cal_last_date_time(self, single_instrument_session):
        last_cal = single_instrument_session.get_ext_cal_last_date_and_time()
        assert last_cal.month == 12
        assert last_cal.day == 21
        assert last_cal.year == 1999
        assert last_cal.hour == 0
        assert last_cal.minute == 0

    def test_get_self_cal_last_temperature(self, single_instrument_session):
        last_cal_temp = single_instrument_session.get_self_cal_last_temp()
        assert last_cal_temp == 25

    def test_get_ext_cal_last_temperature(self, single_instrument_session):
        last_cal_temp = single_instrument_session.get_ext_cal_last_temp()
        assert last_cal_temp == 25

    def test_configure_ref_levels(self, single_instrument_session):
        single_instrument_session._configure_ref_levels()
        assert 90.0 == single_instrument_session.meas_chan_high_ref_level


class TestGrpc(SystemTests):
    server_address = "localhost"
    server_port = "31763"

    def _get_grpc_server_exe(self):
        if os.name != "nt":
            pytest.skip("Only supported on Windows")
        import winreg
        try:
            reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
            read64key = winreg.KEY_READ | winreg.KEY_WOW64_64KEY
            with winreg.OpenKey(reg, r"SOFTWARE\National Instruments\Common\Installer", access=read64key) as key:
                shared_dir, _ = winreg.QueryValueEx(key, "NISHAREDDIR64")
        except OSError:
            pytest.skip("NI gRPC Device Server not installed")
        server_exe = pathlib.Path(shared_dir) / "NI gRPC Device Server" / "ni_grpc_device_server.exe"
        if not server_exe.exists():
            pytest.skip("NI gRPC Device Server not installed")
        return server_exe

    @pytest.fixture(scope='class')
    def grpc_channel(self):
        server_exe = self._get_grpc_server_exe()
        proc = subprocess.Popen([str(server_exe)])
        time.sleep(3)
        try:
            channel = grpc.insecure_channel(f"{self.server_address}:{self.server_port}")
            yield channel
        finally:
            proc.kill()

    @pytest.fixture(scope='class')
    def grpc_options(self, grpc_channel):
        grpc_options = niscope.GrpcSessionOptions(grpc_channel, "")
        yield grpc_options

    @pytest.fixture(scope='function')
    def single_instrument_session(self, grpc_options):
        with niscope.Session('FakeDevice', False, True, 'Simulate=1, DriverSetup=Model:5164; BoardType:PXIe', _grpc_options=grpc_options) as simulated_session:
            yield simulated_session

    @pytest.fixture(scope='function')
    def multi_instrument_session(self, grpc_options):
        with niscope.Session(','.join(self._instruments), False, True, 'Simulate=1, DriverSetup=Model:5164; BoardType:PXIe', _grpc_options=grpc_options) as simulated_session:
            yield simulated_session

    @pytest.fixture(scope='function')
    def session_5124(self, grpc_options):
        with self._daqmx_sim_5124_lock:
            with niscope.Session('5124', _grpc_options=grpc_options) as simulated_session:  # 5124 is needed for video triggering
                yield simulated_session

    @pytest.fixture(scope='function')
    def session_5142(self, grpc_options):
        with self._daqmx_sim_5142_lock:
            with niscope.Session('5142', _grpc_options=grpc_options) as simulated_session:  # 5142 is needed for OSP
                yield simulated_session

    def test_error_message(self, grpc_options):
        try:
            # We pass in an invalid model name to force going to error_message
            with niscope.Session('FakeDevice', False, True, 'Simulate=1, DriverSetup=Model:invalid_model; BoardType:PXIe', _grpc_options=grpc_options):
                assert False
        except niscope.Error as e:
            assert e.code == -1074118609
            assert e.description.find('Simulation does not support the selected model and board type.') != -1

    def test_get_self_cal_last_date_time(self, single_instrument_session):
        with pytest.raises(NotImplementedError) as exc_info:
            single_instrument_session.get_self_cal_last_date_and_time()
        assert exc_info.value.args[0] == 'cal_fetch_date is not supported over gRPC'
        assert str(exc_info.value) == 'cal_fetch_date is not supported over gRPC'

    def test_get_ext_cal_last_date_time(self, single_instrument_session):
        with pytest.raises(NotImplementedError) as exc_info:
            single_instrument_session.get_ext_cal_last_date_and_time()
        assert exc_info.value.args[0] == 'cal_fetch_date is not supported over gRPC'
        assert str(exc_info.value) == 'cal_fetch_date is not supported over gRPC'

    def test_get_self_cal_last_temperature(self, single_instrument_session):
        with pytest.raises(NotImplementedError) as exc_info:
            single_instrument_session.get_self_cal_last_temp()
        assert exc_info.value.args[0] == 'cal_fetch_temperature is not supported over gRPC'
        assert str(exc_info.value) == 'cal_fetch_temperature is not supported over gRPC'

    def test_get_ext_cal_last_temperature(self, single_instrument_session):
        with pytest.raises(NotImplementedError) as exc_info:
            single_instrument_session.get_ext_cal_last_temp()
        assert exc_info.value.args[0] == 'cal_fetch_temperature is not supported over gRPC'
        assert str(exc_info.value) == 'cal_fetch_temperature is not supported over gRPC'

    def test_configure_ref_levels(self, single_instrument_session):
        with pytest.raises(NotImplementedError) as exc_info:
            single_instrument_session._configure_ref_levels()
        assert exc_info.value.args[0] == 'configure_ref_levels is not supported over gRPC'
        assert str(exc_info.value) == 'configure_ref_levels is not supported over gRPC'
