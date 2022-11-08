import grpc
import hightime
import math
import nidmm
import numpy
import os
import pathlib
import pytest
import subprocess
import tempfile
import time


class SystemTests:
    # Basic usability tests
    def test_take_simple_measurement_works(self, session):
        session.configure_measurement_digits(nidmm.Function.DC_CURRENT, 1, 5.5)
        assert session.read() != 0  # Assumes DMM reading is not exactly zero to support non-connected modules and simulated modules.

    def test_acquisition(self, session):
        session.configure_measurement_digits(nidmm.Function.DC_CURRENT, 1, 5.5)
        with session.initiate():
            session.fetch()
        with session.initiate():
            session.fetch()

    def test_multi_point_acquisition(self, session):
        session.configure_multi_point(4, 2)
        session.configure_measurement_digits(nidmm.Function.DC_VOLTS, 1, 5.5)
        measurements = session.read_multi_point(8)
        assert len(measurements) == 8

    # Attribute tests
    def test_vi_string_attribute(self, session):
        assert session.serial_number == 'FFFFFFFF'
        try:
            session.serial_number = 'FFFFFFFA'
        except nidmm.Error as e:
            assert e.code == -1074135027  # Attribute is read-only

    def test_vi_int32_attribute(self, session):
        session.sample_count = 5
        assert 5 == session.sample_count

    def test_vi_real64_attribute(self, session):
        session.range = 50  # Coerces up!
        assert 100 == session.range

    def test_enum_attribute(self, session):
        session.function = nidmm.Function.AC_CURRENT
        assert session.function == nidmm.Function.AC_CURRENT
        assert type(session.function) is nidmm.Function
        try:
            session.function = nidmm.LCCalculationModel.SERIES
            assert False
        except TypeError:
            pass

    def test_writeonly_attribute(self, session):
        try:
            session.channel_count = 5
            assert False
        except nidmm.Error as e:
            assert e.code == -1074135027  # Error : Attribute is read-only.

    # Function tests
    def test_method_configure_trigger(self, session):
        # Calling Configure Trigger function and asserting True if any error occurred while function call.
        try:
            session.configure_trigger(nidmm.TriggerSource.IMMEDIATE)
        except nidmm.Error:
            assert True

    def test_method_self_test(self, session):
        # We should not get an assert if self_test passes
        session.self_test()

    def test_method_get_dev_temp(self, session):
        temperature = session.get_dev_temp('')
        assert 20 <= temperature <= 50

    def test_method_reset_with_defaults(self, session):
        assert session.reset_with_defaults() is None

    def test_method_get_self_cal_supported(self, session):
        assert session.get_self_cal_supported() in [True, False]

    def test_method_read_status(self, session):
        backlog, status = session.read_status()
        assert isinstance(backlog, int)
        assert backlog == 0

    def test_fetch_error_while_not_initiated(self, session):
        try:
            session.fetch()
            assert False
        except nidmm.Error as e:
            assert e.code == -1074118641   # called fetch before calling Initiate or after calling Abort

    def test_multi_point_acquisition_with_measurement_absolute(self, session):
        session.configure_multi_point(4, 2)
        session.configure_measurement_absolute(nidmm.Function.DC_VOLTS, 0.02, 0.001)
        measurements = session.read_multi_point(8)
        assert len(measurements) == 8

    def test_disable(self, session):
        session.configure_measurement_digits(nidmm.Function.DC_VOLTS, 10, 5.5)
        with session.initiate():
            time.sleep(0.1)
            backlog, acquisition_state = session.read_status()
            assert acquisition_state == nidmm.AcquisitionStatus.FINISHED_WITH_BACKLOG
            session.disable()
            backlog, acquisition_state = session.read_status()
            assert acquisition_state == nidmm.AcquisitionStatus.NO_ACQUISITION_IN_PROGRESS

    def test_fetch_multiple(self, session):
        session.configure_measurement_digits(nidmm.Function.DC_VOLTS, 10, 5.5)
        session.configure_multi_point(sample_count=10, trigger_count=1)
        with session.initiate():
            measurements = session.fetch_multi_point(5)
            assert len(measurements) == 5
            measurements = session.fetch_multi_point(5)
            backlog, acquisition_state = session.read_status()
            assert acquisition_state == nidmm.AcquisitionStatus.FINISHED_WITH_NO_BACKLOG

    def test_get_auto_range_value(self, session):
        with session.initiate():
            session.fetch()
            auto_range_value_property = session.auto_range_value
            assert auto_range_value_property == 300   # simulated device auto_range_value to maximum 300

    def test_get_cal_date_time(self, session):
        last_cal = session.get_cal_date_and_time(0)
        assert last_cal.month == 3
        assert last_cal.day == 1
        assert last_cal.year == 1940
        assert last_cal.hour == 0
        assert last_cal.minute == 0   # cal_date_and_time should be 03/01/1940:00:00 for simulated 408x devices; 407x and 4065 returns 00/00/0000:00:00

    def test_get_last_cal_temperature(self, session):
        last_cal_temp = session.get_last_cal_temp(0)
        assert last_cal_temp == 25   # last_cal_temp should be 25 for simulated 408x devices; 407x and 4065 returns 0

    def test_trigger_max_time_exceeded_errror(self, session):
        try:
            session.configure_measurement_digits(nidmm.Function.DC_VOLTS, 10, 5.5)
            session.configure_multi_point(sample_count=10, trigger_count=1)
            session.read_multi_point(15)
            assert False
        except nidmm.Error as e:
            assert e.code == -1074126845  # Max Time exceeded before operation completed

    def test_self_cal(self, session):
        try:
            session.self_cal()
        except nidmm.Error:
            assert False

    def test_configure_rtd(self, session):
        session.configure_rtd_type(nidmm.RTDType.CUSTOM, 110)
        assert session.temp_rtd_type == nidmm.RTDType.CUSTOM
        assert session.temp_rtd_res == 110
        session.configure_rtd_custom(0.1, 0.2, 0.3)
        assert session.temp_rtd_a == 0.1
        assert session.temp_rtd_b == 0.2
        assert session.temp_rtd_c == 0.3

    def test_configure_thermistor(self, session):
        session.temp_thermistor_type = nidmm.ThermistorType.CUSTOM
        session.configure_thermistor_custom(0.1, 0.2, 0.3)
        assert session.temp_thermistor_a == 0.1
        assert session.temp_thermistor_b == 0.2
        assert session.temp_thermistor_c == 0.3

    def test_configure_thermocouple(self, session):
        session.configure_thermocouple(nidmm.ThermocoupleType.K, nidmm.ThermocoupleReferenceJunctionType.FIXED)
        assert session.temp_tc_type == nidmm.ThermocoupleType.K
        assert session.temp_tc_ref_junc_type == nidmm.ThermocoupleReferenceJunctionType.FIXED

    def test_configure_waveform_acquisition(self, session):
        session.configure_waveform_acquisition(nidmm.Function.WAVEFORM_VOLTAGE, 100, 1800000, 400)
        assert session.function == nidmm.Function.WAVEFORM_VOLTAGE
        assert session.range == 100
        assert session.waveform_rate == 1800000
        assert session.waveform_points == 400

    def test_fetch_waveform(self, session):
        number_of_points_to_read = 100
        session.configure_waveform_acquisition(nidmm.Function.WAVEFORM_VOLTAGE, 10, 1800000, number_of_points_to_read)
        with session.initiate():
            measurements = session.fetch_waveform(number_of_points_to_read)
            assert len(measurements) == number_of_points_to_read
            assert isinstance(measurements[1], float)

    def test_fetch_waveform_error(self, session):
        number_of_points_to_read = 100
        try:
            session.configure_waveform_acquisition(nidmm.Function.WAVEFORM_VOLTAGE, 10, 1800000, number_of_points_to_read)
            with session.initiate():
                session.fetch_waveform(number_of_points_to_read * 2, maximum_time=hightime.timedelta(milliseconds=1))   # trying to fetch points more than configured
                assert False
        except nidmm.Error as e:
            assert e.code == -1074126845  # Max Time exceeded before operation completed

    def test_perform_cable_compensation(self, session):
        session.configure_measurement_digits(nidmm.Function.CAPACITANCE, 0.002, 5.5)
        conductance, susceptance = session.perform_open_cable_comp()
        assert conductance == 0   # simulated device should return conductance, susceptance as 0
        assert susceptance == 0
        resistance, reactance = session.perform_short_cable_comp()
        assert resistance == 0   # simulated device should return resistance,reactance as 0
        assert reactance == 0

    def test_read_waveform(self, session):
        session.configure_waveform_acquisition(nidmm.Function.WAVEFORM_VOLTAGE, 10, 1800000, 1000)
        with session.initiate():
            number_of_points_to_read = 100
            measurements = session.read_waveform(number_of_points_to_read)
            assert len(measurements) == number_of_points_to_read
            assert isinstance(measurements[1], float)

    def test_send_software_trigger(self, session):
        session.configure_measurement_digits(nidmm.Function.DC_VOLTS, 10, 5.5)
        session.configure_multi_point(sample_count=0, sample_trigger=nidmm.SampleTrigger.SOFTWARE_TRIG, trigger_count=1)
        with session.initiate():
            session.send_software_trigger()    # Send_software_trigger will send triggers automatically for simulated devices. This line of code confirms there is no error while calling send_trigger function
            session.fetch_multi_point(3)

    def test_reset_method(self, session):
        default_function = session.function
        session.function = nidmm.Function.PERIOD
        session.reset()
        function_after_reset = session.function
        assert default_function == function_after_reset

    def test_import_export_buffer(self, session):
        test_value_1 = 1
        test_value_2 = 2
        session.sample_count = test_value_1
        assert session.sample_count == test_value_1
        buffer = session.export_attribute_configuration_buffer()
        session.sample_count = test_value_2
        assert session.sample_count == test_value_2
        session.import_attribute_configuration_buffer(buffer)
        assert session.sample_count == test_value_1

    def test_import_export_file(self, session):
        test_value_1 = 1
        test_value_2 = 2
        temp_file = tempfile.NamedTemporaryFile(suffix='.txt', delete=False)
        # NamedTemporaryFile() returns the file already opened, so we need to close it before we can use it
        temp_file.close()
        path = temp_file.name
        session.sample_count = test_value_1
        assert session.sample_count == test_value_1
        session.export_attribute_configuration_file(path)
        session.sample_count = test_value_2
        assert session.sample_count == test_value_2
        session.import_attribute_configuration_file(path)
        assert session.sample_count == test_value_1
        os.remove(path)

    # No boolean attributes that aren't IVI
    '''
    def test_vi_boolean_attribute(self, session):
        assert session.interchange_check is False

    def test_set_boolean_attribute(self, session):
        session.cache = False
        assert session.cache is False
        session.cache = True
        assert session.cache is True
    '''

    def test_get_ext_cal_recommended_interval(self, session):
        interval = session.get_ext_cal_recommended_interval()
        assert interval.days == 730

    def test_locks_are_reentrant(self, session):
        with session.lock():
            with session.lock():
                interval = session.get_ext_cal_recommended_interval()
                assert interval.days == 730


class TestLibrary(SystemTests):
    @pytest.fixture(scope='function')
    def session(self):
        with nidmm.Session('FakeDevice', False, True, 'Simulate=1, DriverSetup=Model:4082; BoardType:PXIe') as simulated_session:
            yield simulated_session

    def test_fetch_waveform_into(self, session):
        number_of_points_to_read = 100
        session.configure_waveform_acquisition(nidmm.Function.WAVEFORM_VOLTAGE, 10, 1800000, number_of_points_to_read)
        with session.initiate():
            waveform = numpy.empty(number_of_points_to_read, dtype=numpy.float64)
            # Initialize with NaN so we can later verify all samples were overwritten by the driver.
            waveform.fill(float('nan'))
            session.fetch_waveform_into(waveform)
        for sample in waveform:
            assert not math.isnan(sample)

    def test_error_message(self):
        try:
            # We pass in an invalid model name to force going to error_message
            with nidmm.Session('FakeDevice', False, True, 'Simulate=1, DriverSetup=Model:invalid_model; BoardType:PXIe'):
                assert False
        except nidmm.Error as e:
            assert e.code == -1074134964
            assert e.description.find('The option string parameter contains an entry with an unknown option value.') != -1


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
        # TODO(DavidCurtiss): Remove the next 3 lines once (and the above method) the server is started automatically
        server_exe = self._get_grpc_server_exe()
        proc = subprocess.Popen([str(server_exe)])
        time.sleep(3)
        try:
            channel = grpc.insecure_channel(f"{self.server_address}:{self.server_port}")
            yield channel
        finally:
            proc.kill()

    @pytest.fixture(scope='function')
    def session(self, grpc_channel):
        grpc_options = nidmm.GrpcSessionOptions(grpc_channel, "")
        with nidmm.Session('FakeDevice', False, True, 'Simulate=1, DriverSetup=Model:4082; BoardType:PXIe', _grpc_options=grpc_options) as simulated_session:
            yield simulated_session

    def test_error_message(self, grpc_channel):
        grpc_options = nidmm.GrpcSessionOptions(grpc_channel, "")
        try:
            # We pass in an invalid model name to force going to error_message
            with nidmm.Session('FakeDevice', False, True, 'Simulate=1, DriverSetup=Model:invalid_model; BoardType:PXIe', _grpc_options=grpc_options):
                assert False
        except nidmm.Error as e:
            assert e.code == -1074134964
            assert e.description.find('The option string parameter contains an entry with an unknown option value.') != -1

    def test_new_session_already_exists(self, grpc_channel):
        session_name = 'existing_session'
        expected_error_message = "Cannot initialize '" + session_name + "' when a session already exists."
        expected_grpc_error = grpc.StatusCode.ALREADY_EXISTS
        init_behavior = nidmm.SessionInitializationBehavior.INITIALIZE_SERVER_SESSION
        grpc_options = nidmm.GrpcSessionOptions(grpc_channel, session_name, init_behavior)
        with nidmm.Session('FakeDevice', False, True, 'Simulate=1, DriverSetup=Model:4082; BoardType:PXIe', _grpc_options=grpc_options):
            try:
                with nidmm.Session('FakeDevice', False, True, 'Simulate=1, DriverSetup=Model:4082; BoardType:PXIe', _grpc_options=grpc_options):
                    assert False
            except nidmm.Error as e:
                assert e.rpc_code == expected_grpc_error
                assert e.description == expected_error_message
                assert str(e) == f'{expected_grpc_error}: {expected_error_message}'

    def test_attach_to_non_existent_session(self, grpc_channel):
        session_name = 'non_existent_session'
        expected_error_message = "Cannot attach to '" + session_name + "' because a session has not been initialized."
        expected_grpc_error = grpc.StatusCode.FAILED_PRECONDITION
        init_behavior = nidmm.SessionInitializationBehavior.ATTACH_TO_SERVER_SESSION
        grpc_options = nidmm.GrpcSessionOptions(grpc_channel, session_name, init_behavior)
        try:
            with nidmm.Session('FakeDevice', False, True, 'Simulate=1, DriverSetup=Model:4082; BoardType:PXIe', _grpc_options=grpc_options):
                assert False
        except nidmm.Error as e:
            assert e.rpc_code == expected_grpc_error
            assert e.description == expected_error_message
            assert str(e) == f'{expected_grpc_error}: {expected_error_message}'
