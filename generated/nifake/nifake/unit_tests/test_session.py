import array
import datetime
import hightime
import nifake
import nifake.errors
import numpy

from unittest.mock import MagicMock
from unittest.mock import patch

import _mock_helper

SESSION_NUM_FOR_TEST = 42
GRPC_SESSION_OBJECT_FOR_TEST = object()


class TestSession(object):

    class PatchedLibraryInterpreter(nifake._library_interpreter.LibraryInterpreter):
        def __init__(self, encoding):
            for f in dir(self):
                if not f.startswith("_") and f not in {'get_session_handle', 'set_session_handle'}:
                    setattr(self, f, MagicMock(spec_set=getattr(self, f), side_effect=_mock_helper.MockFunctionCallError(f)))

    def setup_method(self, method):
        self.patched_library_interpreter = self.PatchedLibraryInterpreter(None)
        self.patched_library_interpreter_ctor = patch('nifake.session._library_interpreter.LibraryInterpreter', return_value=self.patched_library_interpreter)
        self.patched_library_interpreter_ctor.start()

        # We don't actually call into the nitclk DLL, but we do need to mock the function since it is called
        self.tclk_patched_library_singleton_get = patch('nitclk._library_interpreter._library_singleton.get', return_value=None)
        self.tclk_patched_library_singleton_get.start()

        # We shouldn't call into grpc
        self.patched_grpc_interpreter = patch('nifake._grpc_stub_interpreter.GrpcStubInterpreter', side_effect=AssertionError('Called into grpc!'))
        self.patched_grpc_interpreter.start()

        def interpreter_init(*args, **kwargs):
            self.patched_library_interpreter._close_on_exit = True
            return SESSION_NUM_FOR_TEST

        self.patched_library_interpreter.init_with_options.side_effect = interpreter_init
        self.patched_library_interpreter.close.side_effect = [None]

        # Mock lock/unlock
        self.patched_library_interpreter.lock.side_effect = lambda *args: None
        self.patched_library_interpreter.unlock.side_effect = lambda *args: None

    def teardown_method(self, method):
        self.patched_grpc_interpreter.stop()
        self.patched_library_interpreter_ctor.stop()
        self.tclk_patched_library_singleton_get.stop()

    # Session management

    def test_init_with_options_and_close(self):
        session = nifake.Session('dev1')
        self.patched_library_interpreter.init_with_options.assert_called_once_with('dev1', False, False, '')
        assert session._interpreter._vi == SESSION_NUM_FOR_TEST
        session.close()
        self.patched_library_interpreter.close.assert_called_once_with()

    def test_init_with_options_nondefault_and_close(self):
        session = nifake.Session('FakeDevice', 'Some string', True, True)
        self.patched_library_interpreter.init_with_options.assert_called_once_with('FakeDevice', True, True, 'Some string')
        assert session._interpreter._vi == SESSION_NUM_FOR_TEST
        session.close()
        self.patched_library_interpreter.close.assert_called_once_with()

    def test_close(self):
        session = nifake.Session('dev1')
        assert session._interpreter._vi == SESSION_NUM_FOR_TEST
        session.close()
        self.patched_library_interpreter.close.assert_called_once_with()
        assert session._interpreter._vi == 0

    def test_session_context_manager(self):
        with nifake.Session('dev1') as session:
            assert type(session) == nifake.Session
            self.patched_library_interpreter.init_with_options.assert_called_once_with('dev1', False, False, '')
            assert session._interpreter._vi == SESSION_NUM_FOR_TEST
        self.patched_library_interpreter.close.assert_called_once_with()
        assert session._interpreter._vi == 0

    def test_init_with_error(self):
        test_error_code = -1
        test_error_desc = 'Test'
        self.patched_library_interpreter.init_with_options.side_effect = nifake.errors.DriverError(test_error_code, test_error_desc)
        try:
            nifake.Session('dev1')
            assert False
        except nifake.Error as e:
            assert e.code == test_error_code
            assert e.description == test_error_desc

    def test_close_with_error(self):
        test_error_code = -1
        test_error_desc = 'Test'
        session = nifake.Session('dev1')
        assert session._interpreter._vi == SESSION_NUM_FOR_TEST
        self.patched_library_interpreter.close.side_effect = nifake.errors.DriverError(test_error_code, test_error_desc)
        try:
            session.close()
            assert False
        except nifake.Error as e:
            assert e.code == test_error_code
            assert e.description == test_error_desc
        self.patched_library_interpreter.close.assert_called_once_with()
        assert session._interpreter._vi == 0

    def test_session_context_manager_init_with_error(self):
        test_error_code = -1
        test_error_desc = 'Test'
        self.patched_library_interpreter.init_with_options.side_effect = nifake.errors.DriverError(test_error_code, test_error_desc)
        try:
            with nifake.Session('dev1') as session:
                assert type(session) == nifake.Session
                assert False
        except nifake.Error as e:
            assert e.code == test_error_code
            assert e.description == test_error_desc

    def test_session_context_manager_close_with_error(self):
        test_error_code = -1
        test_error_desc = 'Test'
        self.patched_library_interpreter.close.side_effect = nifake.errors.DriverError(test_error_code, test_error_desc)
        try:
            with nifake.Session('dev1') as session:
                assert type(session) == nifake.Session
                assert False
        except nifake.Error as e:
            assert e.code == test_error_code
            assert e.description == test_error_desc

    # Session locking

    def test_lock_session_none(self):
        with nifake.Session('dev1') as session:
            session.lock()
            self.patched_library_interpreter.lock.assert_called_once_with()

    def test_unlock_session_none(self):
        with nifake.Session('dev1') as session:
            session.unlock()
            self.patched_library_interpreter.unlock.assert_called_once_with()

    def test_lock_context_manager(self):
        with nifake.Session('dev1') as session:
            with session.lock():
                pass
            self.patched_library_interpreter.lock.assert_called_once_with()
            self.patched_library_interpreter.unlock.assert_called_once_with()

    def test_lock_context_manager_abnormal_exit(self):
        with nifake.Session('dev1') as session:
            try:
                with session.lock():
                    raise nifake.Error('Fake exception')
            except nifake.Error:
                pass
            self.patched_library_interpreter.lock.assert_called_once_with()
            self.patched_library_interpreter.unlock.assert_called_once_with()

    # Methods

    def test_self_test(self):
        test_error_code = 0
        self.patched_library_interpreter.self_test.side_effect = [(test_error_code, '')]
        with nifake.Session('dev1') as session:
            session.self_test()

    def test_self_test_fail(self):
        test_error_code = 1
        test_error_message = 'error message'
        self.patched_library_interpreter.self_test.side_effect = [(test_error_code, test_error_message)]
        with nifake.Session('dev1') as session:
            try:
                session.self_test()
                assert False
            except nifake.errors.SelfTestError as e:
                assert e.code == test_error_code
                assert e.message == test_error_message

    def test_acquisition_context_manager(self):
        self.patched_library_interpreter.initiate.side_effect = [None]
        self.patched_library_interpreter.abort.side_effect = [None]
        with nifake.Session('dev1') as session:
            with session.initiate():
                self.patched_library_interpreter.initiate.assert_called_once_with()
            self.patched_library_interpreter.abort.assert_called_once_with()
        self.patched_library_interpreter.close.assert_called_once_with()

    def test_acquisition_no_context_manager(self):
        self.patched_library_interpreter.initiate.side_effect = [None]
        self.patched_library_interpreter.abort.side_effect = [None]
        with nifake.Session('dev1') as session:
            session.initiate()
            self.patched_library_interpreter.initiate.assert_called_once_with()
            session.abort()
            self.patched_library_interpreter.abort.assert_called_once_with()
        self.patched_library_interpreter.close.assert_called_once_with()

    def test_single_point_read_timedelta(self):
        test_maximum_time_ns = 1    # nanoseconds
        test_maximum_time_s = 1e-9  # seconds
        test_maximum_time_timedelta = hightime.timedelta(nanoseconds=test_maximum_time_ns)
        test_reading = 5
        self.patched_library_interpreter.read.side_effect = [test_reading]
        with nifake.Session('dev1') as session:
            assert test_reading == session.read(test_maximum_time_timedelta)
            self.patched_library_interpreter.read.assert_called_once_with(test_maximum_time_s)

    def test_enum_input_function_with_defaults(self):
        default_turtle = nifake.Turtle.LEONARDO
        test_turtle = nifake.Turtle.DONATELLO
        self.patched_library_interpreter.enum_input_function_with_defaults.side_effect = [None, None]
        with nifake.Session('dev1') as session:
            session.enum_input_function_with_defaults()
            session.enum_input_function_with_defaults(test_turtle)
            from unittest.mock import call
            calls = [call(default_turtle), call(test_turtle)]
            self.patched_library_interpreter.enum_input_function_with_defaults.assert_has_calls(calls)

    def test_string_valued_enum_input_function_with_defaults(self):
        default_mobile_os_name = nifake.MobileOSNames.ANDROID
        test_mobile_os_name = nifake.MobileOSNames.IOS
        self.patched_library_interpreter.string_valued_enum_input_function_with_defaults.side_effect = [None, None]
        with nifake.Session('dev1') as session:
            session.string_valued_enum_input_function_with_defaults()
            session.string_valued_enum_input_function_with_defaults(test_mobile_os_name)
            from unittest.mock import call
            calls = [call(default_mobile_os_name), call(test_mobile_os_name)]
            self.patched_library_interpreter.string_valued_enum_input_function_with_defaults.assert_has_calls(calls)

    def test_fetch_waveform_into_wrong_type(self):
        length = 10
        with nifake.Session('dev1') as session:
            waveforms = [
                10,
                10.5,
                "Not a numpy.ndarray",
                range(length),
                [i + 0.0 for i in range(length)],
                numpy.empty(length, numpy.int32),
                numpy.empty(length, numpy.uint8)
            ]
            for w in waveforms:
                try:
                    session.fetch_waveform_into(w)
                    assert False
                except TypeError:
                    pass

    def test_parameters_are_multiple_types_error(self):
        boolean_val = True
        int32_val = 32
        int64_val = 6000000000
        enum_val = nifake.Turtle.LEONARDO
        float_val = 1.23
        float_enum_val = nifake.FloatEnum.SIX_POINT_FIVE
        string_val = 'Testing is fun?'
        with nifake.Session('dev1') as session:
            try:
                session.parameters_are_multiple_types(boolean_val, int32_val, int64_val, 123, float_val, float_enum_val, string_val)
                assert False
            except TypeError:
                pass
            try:
                session.parameters_are_multiple_types(boolean_val, int32_val, int64_val, enum_val, float_val, 0.123, string_val)
                assert False
            except TypeError:
                pass

    def test_error_with_rep_cap(self):
        test_error_code = -42
        test_error_desc = "The answer to the ultimate question"
        self.patched_library_interpreter.set_attribute_vi_real64.side_effect = nifake.errors.DriverError(test_error_code, test_error_desc)
        with nifake.Session('dev1') as session:
            try:
                session.channels['100'].read_write_double = 5.0
                assert False
            except nifake.Error as e:
                assert e.code == test_error_code
                assert e.description == test_error_desc

    def test_call_not_enough_parameters_error(self):
        with nifake.Session('dev1') as session:
            try:
                session.multiple_array_types(10)
                assert False
            except TypeError:
                pass

    def test_enum_input_function_with_defaults_bad_type_error(self):
        test_turtle = 123
        with nifake.Session('dev1') as session:
            try:
                session.enum_input_function_with_defaults(test_turtle)
                assert False
            except TypeError:
                pass

    def test_get_channel_names(self):
        channel_indices = [0, 3, 2]
        channel_indices_string = '0,3,2'
        expected_channel_names_string = 'ch0,ch3,ch2'
        expected_channel_names = ['ch0', 'ch3', 'ch2']
        self.patched_library_interpreter.get_channel_names.side_effect = [expected_channel_names_string]
        with nifake.Session('dev1') as session:
            channel_names_from_session = session.get_channel_names(channel_indices)
            assert channel_names_from_session == expected_channel_names
            self.patched_library_interpreter.get_channel_names.assert_called_once_with(channel_indices_string)

    # Repeated Capabilities

    def test_repeated_capability_method_on_session_timedelta(self):
        test_maximum_time_ms = 10     # milliseconds
        test_maximum_time_timedelta = hightime.timedelta(milliseconds=test_maximum_time_ms)
        test_reading = 5
        self.patched_library_interpreter.read_from_channel.side_effect = [test_reading]
        with nifake.Session('dev1') as session:
            value = session.read_from_channel(test_maximum_time_timedelta)
        self.patched_library_interpreter.read_from_channel.assert_called_once_with('', test_maximum_time_ms)
        assert value == test_reading

    def test_repeated_capability_method_on_specific_channel(self):
        test_maximum_time_ms = 10     # milliseconds
        test_maximum_time = hightime.timedelta(milliseconds=test_maximum_time_ms)
        test_reading = 5
        self.patched_library_interpreter.read_from_channel.side_effect = [test_reading]
        with nifake.Session('dev1') as session:
            value = session.channels['3'].read_from_channel(test_maximum_time)
        self.patched_library_interpreter.read_from_channel.assert_called_once_with('3', test_maximum_time_ms)
        assert value == test_reading

    def test_device_method_not_exist_on_repeated_capability_error(self):
        with nifake.Session('dev1') as session:
            try:
                session.channels['3'].simple_function()
                assert False, 'Method has no repeated capability so it shouldn\'t exist on _RepeatedCapability'
            except AttributeError:
                pass

    def test_repeated_capabilities_list(self):
        with nifake.Session('dev1') as session:
            assert session.channels['r0']._repeated_capability_list == ['r0']

    def test_chained_repeated_capabilities_list(self):
        with nifake.Session('dev1') as session:
            assert session.sites[0, 1].channels[2, 3]._repeated_capability_list == ['site0/2', 'site0/3', 'site1/2', 'site1/3']

    def test_chained_repeated_capability_method_on_specific_channel(self):
        test_maximum_time_ms = 10     # milliseconds
        test_maximum_time = hightime.timedelta(milliseconds=test_maximum_time_ms)
        test_reading = 5
        self.patched_library_interpreter.read_from_channel.side_effect = [test_reading]
        with nifake.Session('dev1') as session:
            value = session.sites[0, 1].channels[2, 3].read_from_channel(test_maximum_time)
        self.patched_library_interpreter.read_from_channel.assert_called_once_with('site0/2,site0/3,site1/2,site1/3', test_maximum_time_ms)
        assert value == test_reading

    def test_function_with_repeated_capability_type(self):
        self.patched_library_interpreter.function_with_repeated_capability_type.side_effect = [None]
        with nifake.Session('dev1') as session:
            session.channels['0-3'].function_with_repeated_capability_type()
            self.patched_library_interpreter.function_with_repeated_capability_type.assert_called_once_with('0,1,2,3')

    # Attributes

    def test_get_attribute_int32(self):
        test_number = 3
        self.patched_library_interpreter.get_attribute_vi_int32.side_effect = [test_number]
        with nifake.Session('dev1') as session:
            attr_int = session.read_write_integer
            assert(attr_int == test_number)
            self.patched_library_interpreter.get_attribute_vi_int32.assert_called_once_with('', 1000004)

    def test_set_attribute_int32(self):
        self.patched_library_interpreter.set_attribute_vi_int32.side_effect = [None]
        attribute_id = 1000004
        test_number = -10
        with nifake.Session('dev1') as session:
            session.read_write_integer = test_number
            self.patched_library_interpreter.set_attribute_vi_int32.assert_called_once_with('', attribute_id, test_number)

    def test_get_attribute_int32_with_converter(self):
        attribute_id = 1000008
        test_number_ms = 3
        test_number_s = 0.003
        self.patched_library_interpreter.get_attribute_vi_int32.side_effect = [test_number_ms]
        with nifake.Session('dev1') as session:
            attr_timedelta = session.read_write_integer_with_converter
            assert(attr_timedelta.total_seconds() == test_number_s)
            self.patched_library_interpreter.get_attribute_vi_int32.assert_called_once_with('', attribute_id)

    def test_set_attribute_int32_with_converter(self):
        self.patched_library_interpreter.set_attribute_vi_int32.side_effect = [None]
        attribute_id = 1000008
        test_number_ms = -10000
        with nifake.Session('dev1') as session:
            session.read_write_integer_with_converter = hightime.timedelta(milliseconds=test_number_ms)
            self.patched_library_interpreter.set_attribute_vi_int32.assert_called_once_with('', attribute_id, test_number_ms)

    def test_get_attribute_real64(self):
        attribute_id = 1000001
        test_number = 1.5
        self.patched_library_interpreter.get_attribute_vi_real64.side_effect = [test_number]
        with nifake.Session('dev1') as session:
            attr_double = session.read_write_double
            assert attr_double == test_number
            self.patched_library_interpreter.get_attribute_vi_real64.assert_called_once_with('', attribute_id)

    def test_set_attribute_real64(self):
        self.patched_library_interpreter.set_attribute_vi_real64.side_effect = [None]
        attribute_id = 1000001
        test_number = 10.1
        with nifake.Session('dev1') as session:
            session.read_write_double = test_number
            self.patched_library_interpreter.set_attribute_vi_real64.assert_called_once_with('', attribute_id, test_number)

    def test_get_attribute_real64_with_converter(self):
        attribute_id = 1000007
        test_number = 1e-9
        self.patched_library_interpreter.get_attribute_vi_real64.side_effect = [test_number]
        with nifake.Session('dev1') as session:
            attr_timedelta = session.read_write_double_with_converter
            assert attr_timedelta.total_seconds() == test_number
            self.patched_library_interpreter.get_attribute_vi_real64.assert_called_once_with('', attribute_id)

    def test_set_attribute_real64_with_converter(self):
        self.patched_library_interpreter.set_attribute_vi_real64.side_effect = [None]
        attribute_id = 1000007
        test_number = 1e-9
        with nifake.Session('dev1') as session:
            session.read_write_double_with_converter = hightime.timedelta(nanoseconds=1)
            self.patched_library_interpreter.set_attribute_vi_real64.assert_called_once_with('', attribute_id, test_number)

    def test_get_attribute_string(self):
        string = 'Testing is fun?'
        self.patched_library_interpreter.get_attribute_vi_string.side_effect = [string]
        attribute_id = 1000002
        with nifake.Session('dev1') as session:
            attr_string = session.read_write_string
            assert attr_string == string
            self.patched_library_interpreter.get_attribute_vi_string.assert_called_once_with('', attribute_id)

    def test_set_attribute_string(self):
        self.patched_library_interpreter.set_attribute_vi_string.side_effect = [None]
        attribute_id = 1000002
        attrib_string = 'This is test string'
        with nifake.Session('dev1') as session:
            session.read_write_string = attrib_string
            self.patched_library_interpreter.set_attribute_vi_string.assert_called_once_with('', attribute_id, 'This is test string')

    def test_get_attribute_string_with_converter(self):
        string = 'not that interesting'
        self.patched_library_interpreter.get_attribute_vi_string.side_effect = [string]
        attribute_id = 1000010
        with nifake.Session('dev1') as session:
            attr_string = session.read_write_string_repeated_capability
            assert attr_string == string
            self.patched_library_interpreter.get_attribute_vi_string.assert_called_once_with('', attribute_id)

    def test_set_attribute_string_with_converter(self):
        self.patched_library_interpreter.set_attribute_vi_string.side_effect = [None]
        attribute_id = 1000010
        with nifake.Session('dev1') as session:
            session.read_write_string_repeated_capability = 42
            self.patched_library_interpreter.set_attribute_vi_string.assert_called_once_with('', attribute_id, '42')

    def test_get_attribute_boolean(self):
        self.patched_library_interpreter.get_attribute_vi_boolean.side_effect = [1]
        attribute_id = 1000000
        with nifake.Session('dev1') as session:
            assert session.read_write_bool
            self.patched_library_interpreter.get_attribute_vi_boolean.assert_called_once_with('', attribute_id)

    def test_set_attribute_boolean(self):
        self.patched_library_interpreter.set_attribute_vi_boolean.side_effect = [None]
        attribute_id = 1000000
        attrib_bool = True
        with nifake.Session('dev1') as session:
            session.read_write_bool = attrib_bool
            self.patched_library_interpreter.set_attribute_vi_boolean.assert_called_once_with('', attribute_id, True)

    def test_get_attribute_enum_int32(self):
        self.patched_library_interpreter.get_attribute_vi_int32.side_effect = [nifake.Color.BLUE]
        with nifake.Session('dev1') as session:
            assert session.read_write_color == nifake.Color.BLUE
            attribute_id = 1000003
            self.patched_library_interpreter.get_attribute_vi_int32.assert_called_once_with('', attribute_id)

    def test_set_attribute_enum_int32(self):
        self.patched_library_interpreter.set_attribute_vi_int32.side_effect = [None]
        enum_value = nifake.Color.RED
        with nifake.Session('dev1') as session:
            session.read_write_color = enum_value
            attribute_id = 1000003
            self.patched_library_interpreter.set_attribute_vi_int32.assert_called_once_with('', attribute_id, enum_value.value)

    def test_get_attribute_enum_real64(self):
        enum_value = nifake.FloatEnum.SIX_POINT_FIVE
        self.patched_library_interpreter.get_attribute_vi_real64.side_effect = [enum_value]
        with nifake.Session('dev1') as session:
            assert session.float_enum == enum_value
            attribute_id = 1000005
            self.patched_library_interpreter.get_attribute_vi_real64.assert_called_once_with('', attribute_id)

    def test_set_attribute_enum_real64(self):
        self.patched_library_interpreter.set_attribute_vi_real64.side_effect = [None]
        enum_value = nifake.FloatEnum.FIVE_POINT_FIVE
        with nifake.Session('dev1') as session:
            session.float_enum = enum_value
            attribute_id = 1000005
            self.patched_library_interpreter.set_attribute_vi_real64.assert_called_once_with('', attribute_id, enum_value.value)

    def test_get_attribute_enum_with_converter(self):
        enum_value = nifake.EnumWithConverter.RED
        converted_value = True
        self.patched_library_interpreter.get_attribute_vi_int32.side_effect = [enum_value]
        with nifake.Session('dev1') as session:
            assert session.read_write_enum_with_converter == converted_value
            attribute_id = 1000011
            self.patched_library_interpreter.get_attribute_vi_int32.assert_called_once_with('', attribute_id)

    def test_get_attribute_enum_with_converter_invalid_value_from_driver(self):
        invalid_value_from_driver = 0
        expected_error_message = 'The NI-FAKE runtime returned an unexpected value. This can occur if it is too new for the nifake Python module. Upgrade the nifake Python module.'
        self.patched_library_interpreter.get_attribute_vi_int32.side_effect = [invalid_value_from_driver]
        with nifake.Session('dev1') as session:
            try:
                session.read_write_enum_with_converter
                assert False
            except nifake.errors.DriverTooNewError as actual_error:
                actual_error_message = actual_error.args[0]
                assert actual_error_message == expected_error_message
            attribute_id = 1000011
            self.patched_library_interpreter.get_attribute_vi_int32.assert_called_once_with('', attribute_id)

    def test_set_attribute_enum_with_converter(self):
        enum_value = nifake.EnumWithConverter.RED
        converted_value = True
        self.patched_library_interpreter.set_attribute_vi_int32.side_effect = [None]
        with nifake.Session('dev1') as session:
            session.read_write_enum_with_converter = converted_value
            attribute_id = 1000011
            self.patched_library_interpreter.set_attribute_vi_int32.assert_called_once_with('', attribute_id, enum_value.value)

    def test_set_attribute_enum_with_converter_invalid_input(self):
        invalid_input_value = 'invalid'
        expected_error_description = "Invalid value: invalid"
        self.patched_library_interpreter.set_attribute_vi_int32.side_effect = [None]
        with nifake.Session('dev1') as session:
            try:
                session.read_write_enum_with_converter = invalid_input_value
                assert False
            except ValueError as actual_error:
                actual_error_message = actual_error.args[0]
                assert actual_error_message == expected_error_description
            assert not self.patched_library_interpreter.set_attribute_vi_int32.called

    def test_get_attribute_channel(self):
        test_number = 100
        self.patched_library_interpreter.get_attribute_vi_int32.side_effect = [test_number]
        attribute_id = 1000004
        with nifake.Session('dev1') as session:
            attr_int = session.channels[['0', '1']].read_write_integer
            assert(attr_int == test_number)
            self.patched_library_interpreter.get_attribute_vi_int32.assert_called_once_with('0,1', attribute_id)

    def test_set_attribute_channel(self):
        self.patched_library_interpreter.set_attribute_vi_real64.side_effect = [None]
        attribute_id = 1000001
        test_number = 0.001
        with nifake.Session('dev1') as session:
            session.channels[range(24)].read_write_double = test_number
            self.patched_library_interpreter.set_attribute_vi_real64.assert_called_once_with('0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23', attribute_id, test_number)

    def test_get_attribute_int64(self):
        attribute_id = 1000006
        test_number = 6000000000
        self.patched_library_interpreter.get_attribute_vi_int64.side_effect = [test_number]
        with nifake.Session('dev1') as session:
            attr_int = session.read_write_int64
            assert(attr_int == test_number)
            self.patched_library_interpreter.get_attribute_vi_int64.assert_called_once_with('', attribute_id)

    def test_set_attribute_int64(self):
        self.patched_library_interpreter.set_attribute_vi_int64.side_effect = [None]
        attribute_id = 1000006
        test_number = -6000000000
        with nifake.Session('dev1') as session:
            session.read_write_int64 = test_number
            self.patched_library_interpreter.set_attribute_vi_int64.assert_called_once_with('', attribute_id, test_number)

    def test_get_attribute_error(self):
        test_error_code = -123
        test_error_desc = "ascending order"
        self.patched_library_interpreter.get_attribute_vi_real64.side_effect = nifake.errors.DriverError(test_error_code, test_error_desc)
        with nifake.Session('dev1') as session:
            try:
                session.read_write_double
                assert False
            except nifake.Error as e:
                assert e.code == test_error_code
                assert e.description == test_error_desc

    def test_set_attribute_error(self):
        attribute_id = 1000001
        test_error_code = -1
        test_error_desc = 'Test'
        self.patched_library_interpreter.set_attribute_vi_real64.side_effect = nifake.errors.DriverError(test_error_code, test_error_desc)
        with nifake.Session('dev1') as session:
            try:
                session.read_write_double = -42.0
                assert False
            except nifake.Error as e:
                assert e.code == test_error_code
                assert e.description == test_error_desc
                self.patched_library_interpreter.set_attribute_vi_real64.assert_called_once_with('', attribute_id, -42.0)

    def test_add_properties_to_session_error_set(self):
        with nifake.Session('dev1') as session:
            try:
                session.non_existent_property = 5
                assert False
            except AttributeError as e:
                assert str(e) == "'Session' object has no attribute 'non_existent_property'"

    def test_add_properties_to_session_error_get(self):
        with nifake.Session('dev1') as session:
            try:
                value = session.non_existent_property  # noqa: F841
                assert False
            except AttributeError as e:
                assert str(e) == "'Session' object has no attribute 'non_existent_property'"

    def test_add_properties_to_repeated_capability_error_set(self):
        with nifake.Session('dev1') as session:
            try:
                session.channels['0'].non_existent_property = 5
                assert False
            except AttributeError as e:
                assert str(e) == "'_SessionBase' object has no attribute 'non_existent_property'"

    def test_add_properties_to_repeated_capability_error_get(self):
        with nifake.Session('dev1') as session:
            try:
                value = session.channels['0'].non_existent_property  # noqa: F841
                assert False
            except AttributeError as e:
                assert str(e) == "'_SessionBase' object has no attribute 'non_existent_property'"

    def test_set_enum_attribute_int32_error(self):
        with nifake.Session('dev1') as session:
            try:
                session.read_write_color = 5
            except TypeError as e:
                assert str(e) == 'must be Color not int'

    def test_set_wrong_enum_attribute_int32_error(self):
        with nifake.Session('dev1') as session:
            try:
                session.read_write_color = nifake.FloatEnum.SIX_POINT_FIVE
            except TypeError as e:
                assert str(e) == 'must be Color not FloatEnum'

    def test_multiple_arrays_same_size_wrong_size_2(self):
        with nifake.Session('dev1') as session:
            input_array_of_floats1 = [0.041, 0.042, 0.043, 0.044]
            input_array_of_floats2 = [0.410, 0.420, 0.430]
            input_array_of_floats3 = [4.100, 4.200, 4.300, 4.400]
            input_array_of_floats4 = [41.00, 42.00, 43.00, 44.00]
            try:
                session.multiple_arrays_same_size(input_array_of_floats1, input_array_of_floats2, input_array_of_floats3, input_array_of_floats4)
            except ValueError:
                pass

    def test_multiple_arrays_same_size_wrong_size_3(self):
        with nifake.Session('dev1') as session:
            input_array_of_floats1 = [0.041, 0.042, 0.043, 0.044]
            input_array_of_floats2 = [0.410, 0.420, 0.430, 0.440]
            input_array_of_floats3 = [4.100, 4.200, 4.400]
            input_array_of_floats4 = [41.00, 42.00, 43.00, 44.00]
            try:
                session.multiple_arrays_same_size(input_array_of_floats1, input_array_of_floats2, input_array_of_floats3, input_array_of_floats4)
            except ValueError:
                pass

    def test_multiple_arrays_same_size_wrong_size_4(self):
        with nifake.Session('dev1') as session:
            input_array_of_floats1 = [0.041, 0.042, 0.043, 0.044]
            input_array_of_floats2 = [0.410, 0.420, 0.430, 0.440]
            input_array_of_floats3 = [4.100, 4.200, 4.300, 4.400]
            input_array_of_floats4 = [41.00, 42.00, 43.00, 44.00, 45.00]
            try:
                session.multiple_arrays_same_size(input_array_of_floats1, input_array_of_floats2, input_array_of_floats3, input_array_of_floats4)
            except ValueError:
                pass

    def test_get_cal_date_time(self):
        month = 12
        day = 30
        year = 1988
        hour = 10
        minute = 15
        self.patched_library_interpreter.get_cal_date_and_time.side_effect = [(month, day, year, hour, minute)]
        with nifake.Session('dev1') as session:
            last_cal = session.get_cal_date_and_time(0)
            assert isinstance(last_cal, hightime.datetime)
            assert hightime.datetime(year, month, day, hour, minute) == last_cal

    def test_get_cal_interval(self):
        self.patched_library_interpreter.get_cal_interval.side_effect = [24]
        with nifake.Session('dev1') as session:
            last_cal = session.get_cal_interval()
            assert isinstance(last_cal, hightime.timedelta)
            assert 730 == last_cal.days

    # Import/Export functions - Invalid types

    def test_import_attribute_configuration_buffer_list_i8_big(self):
        expected_list = [ord('a') * 100, ord('b') * 100, ord('c') * 100, ord('d') * 100]
        configuration = expected_list
        with nifake.Session('dev1') as session:
            self.get_ctypes_pointer_for_buffer_side_effect_items = [expected_list]
            self.get_ctypes_pointer_for_buffer_side_effect_count = 0
            try:
                session.import_attribute_configuration_buffer(configuration)
                assert False
            except ValueError:
                pass

    def test_import_attribute_configuration_buffer_list_i8_float(self):
        expected_list = [ord('a') * 1.0, ord('b') * 1.0, ord('c') * 1.0, ord('d') * 1.0]
        configuration = expected_list
        with nifake.Session('dev1') as session:
            self.get_ctypes_pointer_for_buffer_side_effect_items = [expected_list]
            self.get_ctypes_pointer_for_buffer_side_effect_count = 0
            try:
                session.import_attribute_configuration_buffer(configuration)
                assert False
            except TypeError:
                pass

    def test_import_attribute_configuration_buffer_list_i8_big_float(self):
        expected_list = [ord('a') * 100.0, ord('b') * 100.0, ord('c') * 100.0, ord('d') * 100.0]
        configuration = expected_list
        with nifake.Session('dev1') as session:
            self.get_ctypes_pointer_for_buffer_side_effect_items = [expected_list]
            self.get_ctypes_pointer_for_buffer_side_effect_count = 0
            try:
                session.import_attribute_configuration_buffer(configuration)
                assert False
            except TypeError:
                pass

    def test_export_attribute_configuration_buffer(self):
        expected_buffer_list = [ord('a'), ord('b'), ord('c'), ord('d'), ]
        self.patched_library_interpreter.export_attribute_configuration_buffer.side_effect = [expected_buffer_list]
        with nifake.Session('dev1') as session:
            actual_configuration = session.export_attribute_configuration_buffer()
            assert type(actual_configuration) is bytes
            assert actual_configuration == bytes(expected_buffer_list)
        self.patched_library_interpreter.export_attribute_configuration_buffer.assert_called_once_with()

    def test_channel_on_session(self):
        with nifake.Session('dev1') as session:
            try:
                session['100'].read_write_double = 5.0
                assert False
            except TypeError:
                pass

    def test_function_name(self):
        with nifake.Session('dev1') as session:
            # Pick a function that uses @ivi_synchronized
            assert session.bool_array_output_function.__name__ == 'bool_array_output_function'
            # Pick several functions that do not use @ivi_synchronized to make sure they don't break in the future
            assert session.lock.__name__ == 'lock'
            assert session._error_message.__name__ == '_error_message'
            assert session.initiate.__name__ == 'initiate'
            # Cannot use session.<property>.__name__ since that invokes the get attribute value and the returned value
            # (string, int, float) don't have __name__ properties

    def test_buffer_converter(self):
        self.patched_library_interpreter.double_all_the_nums.side_effect = [None]
        nums = [1, 2, 3, 4.2]
        nums_x2 = [x * 2 for x in nums]
        with nifake.Session('dev1') as session:
            session.double_all_the_nums(nums)
            self.patched_library_interpreter.double_all_the_nums.assert_called_once_with(nums_x2)

    def test_nitclk_integration(self):
        with nifake.Session('dev1') as session:
            assert str(type(session.tclk)) == "<class 'nitclk.session.SessionReference'>"

    def test_accept_list_of_time_values_as_floats(self):
        self.patched_library_interpreter.accept_list_of_durations_in_seconds.side_effect = [None]
        delays = [-1.5, 2.0]
        with nifake.Session('dev1') as session:
            session.accept_list_of_durations_in_seconds(delays)
            self.patched_library_interpreter.accept_list_of_durations_in_seconds.assert_called_once_with(delays)

    def test_accept_array_of_time_values_as_floats(self):
        self.patched_library_interpreter.accept_list_of_durations_in_seconds.side_effect = [None]
        time_values = [-1.5, 2.0]
        delays = array.array('d', time_values)
        with nifake.Session('dev1') as session:
            session.accept_list_of_durations_in_seconds(delays)
            self.patched_library_interpreter.accept_list_of_durations_in_seconds.assert_called_once_with(time_values)

    def test_accept_list_of_time_values_as_timedelta_instances(self):
        self.patched_library_interpreter.accept_list_of_durations_in_seconds.side_effect = [None]
        time_values = [-1.5, 2e-9]
        delays = [datetime.timedelta(seconds=-1.5), hightime.timedelta(nanoseconds=2)]
        with nifake.Session('dev1') as session:
            session.accept_list_of_durations_in_seconds(delays)
            self.patched_library_interpreter.accept_list_of_durations_in_seconds.assert_called_once_with(time_values)

    def test_return_timedelta(self):
        time_value = -1.5
        expected_timedelta = hightime.timedelta(seconds=time_value)
        self.patched_library_interpreter.return_duration_in_seconds.side_effect = [time_value]
        with nifake.Session('dev1') as session:
            returned_timedelta = session.return_duration_in_seconds()
            assert returned_timedelta == expected_timedelta
            self.patched_library_interpreter.return_duration_in_seconds.assert_called_once_with()

    def test_return_timedeltas(self):
        time_values = [-1.5, 2.0]
        expected_timedeltas = [hightime.timedelta(seconds=i) for i in time_values]
        self.patched_library_interpreter.return_list_of_durations_in_seconds.side_effect = [time_values]
        with nifake.Session('dev1') as session:
            returned_timedeltas = session.return_list_of_durations_in_seconds(len(expected_timedeltas))
            assert len(returned_timedeltas) == len(expected_timedeltas)
            assert returned_timedeltas == expected_timedeltas
            self.patched_library_interpreter.return_list_of_durations_in_seconds.assert_called_once_with(len(time_values))


class TestGrpcSession(object):

    class PatchedGrpcInterpreter(nifake._grpc_stub_interpreter.GrpcStubInterpreter):
        def __init__(self, grpc_options):
            for f in dir(self):
                if not f.startswith("_") and f not in {'get_session_handle', 'set_session_handle'}:
                    setattr(self, f, MagicMock(spec_set=getattr(self, f), side_effect=_mock_helper.MockFunctionCallError(f)))

    def setup_method(self, method):
        self.patched_grpc_interpreter = self.PatchedGrpcInterpreter(None)
        self.patched_grpc_constructor = patch('nifake._grpc_stub_interpreter.GrpcStubInterpreter', return_value=self.patched_grpc_interpreter)
        self.patched_grpc_constructor.start()

        # We don't actually call into the nitclk DLL, but we do need to mock the function since it is called
        self.tclk_patched_library_singleton_get = patch('nitclk._library_interpreter._library_singleton.get', return_value=None)
        self.tclk_patched_library_singleton_get.start()

        def interpreter_init(*args, **kwargs):
            self.patched_grpc_interpreter._close_on_exit = True
            return GRPC_SESSION_OBJECT_FOR_TEST

        self.patched_grpc_interpreter.init_with_options.side_effect = interpreter_init
        self.patched_grpc_interpreter._close_on_exit = True
        self.patched_grpc_interpreter.close.side_effect = [None]

        # Mock lock/unlock
        self.patched_grpc_interpreter.lock.side_effect = lambda *args: None
        self.patched_grpc_interpreter.unlock.side_effect = lambda *args: None

    def teardown_method(self, method):
        self.patched_grpc_constructor.stop()
        self.tclk_patched_library_singleton_get.stop()

    # Session management

    def test_init_with_options_and_close(self):
        session = nifake.Session('dev1', _grpc_options=nifake.GrpcSessionOptions(object(), ''))
        self.patched_grpc_interpreter.init_with_options.assert_called_once_with('dev1', False, False, '')
        assert session._interpreter._vi == GRPC_SESSION_OBJECT_FOR_TEST
        session.close()
        self.patched_grpc_interpreter.close.assert_called_once_with()

    # Session locking

    def test_lock_session_none(self):
        with nifake.Session('dev1', _grpc_options=nifake.GrpcSessionOptions(object(), '')) as session:
            session.lock()
            self.patched_grpc_interpreter.lock.assert_called_once_with()

    def test_unlock_session_none(self):
        with nifake.Session('dev1', _grpc_options=nifake.GrpcSessionOptions(object(), '')) as session:
            session.unlock()
            self.patched_grpc_interpreter.unlock.assert_called_once_with()

    def test_lock_context_manager(self):
        with nifake.Session('dev1', _grpc_options=nifake.GrpcSessionOptions(object(), '')) as session:
            with session.lock():
                pass
            self.patched_grpc_interpreter.lock.assert_called_once_with()
            self.patched_grpc_interpreter.unlock.assert_called_once_with()

    def test_lock_context_manager_abnormal_exit(self):
        with nifake.Session('dev1', _grpc_options=nifake.GrpcSessionOptions(object(), '')) as session:
            try:
                with session.lock():
                    raise nifake.Error('Fake exception')
            except nifake.Error:
                pass
            self.patched_grpc_interpreter.lock.assert_called_once_with()
            self.patched_grpc_interpreter.unlock.assert_called_once_with()

    # Methods

    def test_self_test(self):
        test_error_code = 0
        self.patched_grpc_interpreter.self_test.side_effect = [(test_error_code, '')]
        with nifake.Session('dev1', _grpc_options=nifake.GrpcSessionOptions(object(), '')) as session:
            session.self_test()

    def test_export_attribute_configuration_buffer(self):
        expected_buffer = b'abcd'
        self.patched_grpc_interpreter.export_attribute_configuration_buffer.side_effect = [expected_buffer]
        with nifake.Session('dev1', _grpc_options=nifake.GrpcSessionOptions(object(), '')) as session:
            actual_configuration = session.export_attribute_configuration_buffer()
            assert type(actual_configuration) is bytes
            assert actual_configuration == bytes(expected_buffer)
        self.patched_grpc_interpreter.export_attribute_configuration_buffer.assert_called_once_with()

    # Attributes

    def test_get_attribute_int32(self):
        test_number = 3
        self.patched_grpc_interpreter.get_attribute_vi_int32.side_effect = [test_number]
        with nifake.Session('dev1', _grpc_options=nifake.GrpcSessionOptions(object(), '')) as session:
            attr_int = session.read_write_integer
            assert(attr_int == test_number)
            self.patched_grpc_interpreter.get_attribute_vi_int32.assert_called_once_with('', 1000004)


# not session tests per se
def test_diagnostic_information():
    info = nifake.print_diagnostic_information()
    assert isinstance(info, dict)


def test_dunder_version():
    print('Version = {}'.format(nifake.__version__))
    assert type(nifake.__version__) is str
