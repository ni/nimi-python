import array
import ctypes
import datetime
import hightime
import math
import nifake
import nifake.errors
import numpy
import platform
import warnings

from unittest.mock import MagicMock
from unittest.mock import patch

import _matchers
import _mock_helper

# from unittest.mock import ANY
# Tests


SESSION_NUM_FOR_TEST = 42


class TestSession(object):

    class PatchedLibrary(nifake._library.Library):
        def __init__(self, ctypes_library):
            super().__init__(ctypes_library)

            for f in dir(self):
                if f.startswith("niFake_") and f.endswith("_cfunc"):
                    setattr(self, f, MagicMock())

    def setup_method(self, method):
        self.patched_library = self.PatchedLibrary(None)
        self.patched_library_singleton_get = patch('nifake._library_interpreter._library_singleton.get', return_value=self.patched_library)
        self.patched_library_singleton_get.start()

        # We don't actually call into the nitclk DLL, but we do need to mock the function since it is called
        self.tclk_patched_library_singleton_get = patch('nitclk._library_interpreter._library_singleton.get', return_value=None)
        self.tclk_patched_library_singleton_get.start()

        self.side_effects_helper = _mock_helper.SideEffectsHelper()
        self.side_effects_helper.set_side_effects_and_return_values(self.patched_library)
        self.patched_library.niFake_InitWithOptions_cfunc.side_effect = self.side_effects_helper.niFake_InitWithOptions
        self.disallow_close = self.patched_library.niFake_close_cfunc.side_effect
        self.patched_library.niFake_close_cfunc.side_effect = self.side_effects_helper.niFake_close

        self.side_effects_helper['InitWithOptions']['vi'] = SESSION_NUM_FOR_TEST

        self.get_ctypes_pointer_for_buffer_side_effect_count = 0
        self.get_ctypes_pointer_for_buffer_side_effect_items = []

        # Mock lock/unlock
        self.LockSession_side_effect_cache = self.patched_library.niFake_LockSession_cfunc.side_effect
        self.patched_library.niFake_LockSession_cfunc.side_effect = self.side_effects_helper.niFake_LockSession
        self.side_effects_helper['LockSession']['callerHasLock'] = True
        self.UnlockSession_side_effect_cache = self.patched_library.niFake_UnlockSession_cfunc.side_effect
        self.patched_library.niFake_UnlockSession_cfunc.side_effect = self.side_effects_helper.niFake_UnlockSession
        self.side_effects_helper['UnlockSession']['callerHasLock'] = False

    def teardown_method(self, method):
        self.patched_library_singleton_get.stop()
        self.tclk_patched_library_singleton_get.stop()

    def niFake_read_warning(self, vi, maximum_time, reading):  # noqa: N802
        reading.contents.value = self.reading
        return self.error_code_return

    def get_ctypes_pointer_for_buffer_side_effect(self, value, library_type=None):
        ret_val = self.get_ctypes_pointer_for_buffer_side_effect_items[self.get_ctypes_pointer_for_buffer_side_effect_count]
        self.get_ctypes_pointer_for_buffer_side_effect_count += 1
        return ret_val

    # Session management

    def test_init_with_options_and_close(self):
        with patch('nifake._library_interpreter.errors', spec_set=['handle_error', '_is_error']) as patched_errors:
            patched_errors._is_error.return_value = 0

            session = nifake.Session('dev1')
            self.patched_library.niFake_InitWithOptions_cfunc.assert_called_once_with(_matchers.ViStringMatcher('dev1'), _matchers.ViBooleanMatcher(False), _matchers.ViBooleanMatcher(False), _matchers.ViStringMatcher(''), _matchers.ViSessionPointerMatcher())
            patched_errors.handle_error.assert_called_once_with(session._library, session, self.patched_library.niFake_InitWithOptions_cfunc.return_value, ignore_warnings=False, is_error_handling=False)
            session.close()
            self.patched_library.niFake_close_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST))

    def test_init_with_options_nondefault_and_close(self):
        session = nifake.Session('FakeDevice', 'Some string', True, True)
        self.patched_library.niFake_InitWithOptions_cfunc.assert_called_once_with(_matchers.ViStringMatcher('FakeDevice'), _matchers.ViBooleanMatcher(True), _matchers.ViBooleanMatcher(True), _matchers.ViStringMatcher('Some string'), _matchers.ViSessionPointerMatcher())
        session.close()
        self.patched_library.niFake_close_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST))

    def test_close(self):
        session = nifake.Session('dev1')
        session.close()
        self.patched_library.niFake_close_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST))

    def test_session_context_manager(self):
        with nifake.Session('dev1') as session:
            assert type(session) == nifake.Session
            self.patched_library.niFake_InitWithOptions_cfunc.assert_called_once_with(_matchers.ViStringMatcher('dev1'), _matchers.ViBooleanMatcher(False), _matchers.ViBooleanMatcher(False), _matchers.ViStringMatcher(''), _matchers.ViSessionPointerMatcher())
        self.patched_library.niFake_close_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST))

    def test_init_with_error(self):
        test_error_code = -1
        test_error_desc = 'Test'
        self.patched_library.niFake_InitWithOptions_cfunc.side_effect = self.side_effects_helper.niFake_InitWithOptions
        self.side_effects_helper['InitWithOptions']['return'] = test_error_code
        self.side_effects_helper['InitWithOptions']['vi'] = SESSION_NUM_FOR_TEST
        self.patched_library.niFake_GetError_cfunc.side_effect = self.side_effects_helper.niFake_GetError
        self.side_effects_helper['GetError']['errorCode'] = test_error_code
        self.side_effects_helper['GetError']['description'] = test_error_desc
        try:
            nifake.Session('dev1')
            assert False
        except nifake.Error as e:
            assert e.code == test_error_code
            assert e.description == test_error_desc

    def test_close_with_error(self):
        test_error_code = -1
        test_error_desc = 'Test'
        self.patched_library.niFake_close_cfunc.side_effect = self.side_effects_helper.niFake_close
        session = nifake.Session('dev1')
        self.side_effects_helper['close']['return'] = test_error_code
        self.patched_library.niFake_GetError_cfunc.side_effect = self.side_effects_helper.niFake_GetError
        self.side_effects_helper['GetError']['errorCode'] = test_error_code
        self.side_effects_helper['GetError']['description'] = test_error_desc
        try:
            session.close()
            assert False
        except nifake.Error as e:
            assert e.code == test_error_code
            assert e.description == test_error_desc
            assert session._vi == 0
        self.patched_library.niFake_close_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST))

    def test_session_context_manager_init_with_error(self):
        test_error_code = -1
        test_error_desc = 'Test'
        self.patched_library.niFake_InitWithOptions_cfunc.side_effect = self.side_effects_helper.niFake_InitWithOptions
        self.side_effects_helper['InitWithOptions']['return'] = test_error_code
        self.side_effects_helper['InitWithOptions']['vi'] = SESSION_NUM_FOR_TEST
        self.patched_library.niFake_GetError_cfunc.side_effect = self.side_effects_helper.niFake_GetError
        self.side_effects_helper['GetError']['errorCode'] = test_error_code
        self.side_effects_helper['GetError']['description'] = test_error_desc
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
        self.patched_library.niFake_close_cfunc.side_effect = self.side_effects_helper.niFake_close
        self.side_effects_helper['close']['return'] = test_error_code
        self.patched_library.niFake_GetError_cfunc.side_effect = self.side_effects_helper.niFake_GetError
        self.side_effects_helper['GetError']['errorCode'] = test_error_code
        self.side_effects_helper['GetError']['description'] = test_error_desc
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
            self.patched_library.niFake_LockSession_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViBooleanPointerMatcher())

    def test_unlock_session_none(self):
        with nifake.Session('dev1') as session:
            session.unlock()
            self.patched_library.niFake_UnlockSession_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViBooleanPointerMatcher())

    def test_lock_context_manager(self):
        with nifake.Session('dev1') as session:
            with session.lock():
                pass
            self.patched_library.niFake_LockSession_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViBooleanPointerMatcher())
            self.patched_library.niFake_UnlockSession_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViBooleanPointerMatcher())

    def test_lock_context_manager_abnormal_exit(self):
        with nifake.Session('dev1') as session:
            try:
                with session.lock():
                    raise nifake.Error('Fake exception')
            except nifake.Error:
                pass
            self.patched_library.niFake_LockSession_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViBooleanPointerMatcher())
            self.patched_library.niFake_UnlockSession_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViBooleanPointerMatcher())

    # Methods
    def test_simple_function(self):
        self.patched_library.niFake_PoorlyNamedSimpleFunction_cfunc.side_effect = self.side_effects_helper.niFake_PoorlyNamedSimpleFunction
        with nifake.Session('dev1') as session:
            session.simple_function()
            self.patched_library.niFake_PoorlyNamedSimpleFunction_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST))

    def test_self_test(self):
        self.patched_library.niFake_self_test_cfunc.side_effect = self.side_effects_helper.niFake_self_test
        test_error_code = 0
        self.side_effects_helper['self_test']['selfTestResult'] = test_error_code
        self.side_effects_helper['self_test']['selfTestMessage'] = ''
        with nifake.Session('dev1') as session:
            session.self_test()

    def test_self_test_fail(self):
        self.patched_library.niFake_self_test_cfunc.side_effect = self.side_effects_helper.niFake_self_test
        test_error_code = 1
        test_error_message = 'error message'
        self.side_effects_helper['self_test']['selfTestResult'] = test_error_code
        self.side_effects_helper['self_test']['selfTestMessage'] = test_error_message
        with nifake.Session('dev1') as session:
            try:
                session.self_test()
                assert False
            except nifake.errors.SelfTestError as e:
                assert e.code == test_error_code
                assert e.message == test_error_message

    def test_get_a_number(self):
        test_number = 16
        self.patched_library.niFake_GetANumber_cfunc.side_effect = self.side_effects_helper.niFake_GetANumber
        self.side_effects_helper['GetANumber']['aNumber'] = test_number
        with nifake.Session('dev1') as session:
            test_result = session.get_a_number()
            assert isinstance(test_result, int)
            assert test_result == test_number
            self.patched_library.niFake_GetANumber_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt16PointerMatcher())

    def test_one_input_function(self):
        test_number = 1
        self.patched_library.niFake_OneInputFunction_cfunc.side_effect = self.side_effects_helper.niFake_OneInputFunction
        with nifake.Session('dev1') as session:
            session.one_input_function(test_number)
            self.patched_library.niFake_OneInputFunction_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(test_number))

    def test_vi_int_64_function(self):
        input_value = 1099511627776  # 2^40
        output_value = 2199023255552  # 2^41
        self.patched_library.niFake_Use64BitNumber_cfunc.side_effect = self.side_effects_helper.niFake_Use64BitNumber
        self.side_effects_helper['Use64BitNumber']['output'] = output_value
        with nifake.Session('dev1') as session:
            assert session.use64_bit_number(input_value) == output_value
            self.patched_library.niFake_Use64BitNumber_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt64Matcher(input_value), _matchers.ViInt64PointerMatcher())

    def test_two_input_function(self):
        test_number = 1.5
        test_string = 'test'
        self.patched_library.niFake_TwoInputFunction_cfunc.side_effect = self.side_effects_helper.niFake_TwoInputFunction
        with nifake.Session('dev1') as session:
            session.two_input_function(test_number, test_string)
            self.patched_library.niFake_TwoInputFunction_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViReal64Matcher(test_number), _matchers.ViStringMatcher(test_string))

    def test_get_enum_value(self):
        test_number = 1
        test_turtle = nifake.Turtle.LEONARDO
        self.patched_library.niFake_GetEnumValue_cfunc.side_effect = self.side_effects_helper.niFake_GetEnumValue
        self.side_effects_helper['GetEnumValue']['aQuantity'] = test_number
        self.side_effects_helper['GetEnumValue']['aTurtle'] = 0
        with nifake.Session('dev1') as session:
            test_result_number, test_result_enum = session.get_enum_value()
            assert isinstance(test_result_number, int)
            assert test_result_number == test_number
            assert isinstance(test_result_enum, nifake.Turtle)
            assert test_result_enum == test_turtle
            self.patched_library.niFake_GetEnumValue_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32PointerMatcher(), _matchers.ViInt16PointerMatcher())

    def test_get_a_list_enums(self):
        self.patched_library.niFake_EnumArrayOutputFunction_cfunc.side_effect = self.side_effects_helper.niFake_EnumArrayOutputFunction
        test_list = [1, 1, 0]
        self.side_effects_helper['EnumArrayOutputFunction']['anArray'] = test_list
        with nifake.Session('dev1') as session:
            test_result = session.enum_array_output_function(len(test_list))
            assert len(test_list) == len(test_result)
            for expected_value, actual_value in zip(test_list, test_result):
                assert isinstance(actual_value, nifake.Turtle)
                assert actual_value.value == expected_value
            self.patched_library.niFake_EnumArrayOutputFunction_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(test_list)), _matchers.ViInt16BufferMatcher(len(test_list)))

    def test_get_a_boolean(self):
        self.patched_library.niFake_GetABoolean_cfunc.side_effect = self.side_effects_helper.niFake_GetABoolean
        self.side_effects_helper['GetABoolean']['aBoolean'] = 1
        with nifake.Session('dev1') as session:
            test_result = session.get_a_boolean()
            assert isinstance(test_result, bool)
            assert test_result
            self.patched_library.niFake_GetABoolean_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViBooleanPointerMatcher())

    def test_get_a_list_booleans(self):
        self.patched_library.niFake_BoolArrayOutputFunction_cfunc.side_effect = self.side_effects_helper.niFake_BoolArrayOutputFunction
        test_list = [1, 1, 0]
        self.side_effects_helper['BoolArrayOutputFunction']['anArray'] = test_list
        with nifake.Session('dev1') as session:
            test_result = session.bool_array_output_function(len(test_list))
            assert len(test_list) == len(test_result)
            for expected_value, actual_value in zip(test_list, test_result):
                assert isinstance(actual_value, bool)
                assert actual_value == bool(expected_value)
            self.patched_library.niFake_BoolArrayOutputFunction_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(test_list)), _matchers.ViBooleanBufferMatcher(len(test_list)))

    def test_acquisition_context_manager(self):
        self.patched_library.niFake_Initiate_cfunc.side_effect = self.side_effects_helper.niFake_Initiate
        self.patched_library.niFake_Abort_cfunc.side_effect = self.side_effects_helper.niFake_Abort
        with nifake.Session('dev1') as session:
            with session.initiate():
                self.patched_library.niFake_Initiate_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST))
            self.patched_library.niFake_Abort_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST))
        self.patched_library.niFake_close_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST))

    def test_acquisition_no_context_manager(self):
        self.patched_library.niFake_Initiate_cfunc.side_effect = self.side_effects_helper.niFake_Initiate
        self.patched_library.niFake_Abort_cfunc.side_effect = self.side_effects_helper.niFake_Abort
        with nifake.Session('dev1') as session:
            session.initiate()
            self.patched_library.niFake_Initiate_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST))
            session.abort()
            self.patched_library.niFake_Abort_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST))
        self.patched_library.niFake_close_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST))

    def test_single_point_read_timedelta(self):
        test_maximum_time_ns = 1    # nanoseconds
        test_maximum_time_s = 1e-9  # seconds
        test_maximum_time_timedelta = hightime.timedelta(nanoseconds=test_maximum_time_ns)
        test_reading = 5
        self.patched_library.niFake_Read_cfunc.side_effect = self.side_effects_helper.niFake_Read
        self.side_effects_helper['Read']['reading'] = test_reading
        with nifake.Session('dev1') as session:
            assert test_reading == session.read(test_maximum_time_timedelta)
            self.patched_library.niFake_Read_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViReal64Matcher(test_maximum_time_s), _matchers.ViReal64PointerMatcher())

    def test_single_point_read_nan(self):
        test_maximum_time_s = 10.0
        test_maximum_time = hightime.timedelta(seconds=test_maximum_time_s)
        test_reading = float('NaN')
        self.patched_library.niFake_Read_cfunc.side_effect = self.side_effects_helper.niFake_Read
        self.side_effects_helper['Read']['reading'] = test_reading
        with nifake.Session('dev1') as session:
            assert math.isnan(session.read(test_maximum_time))

    def test_enum_input_function_with_defaults(self):
        test_turtle = nifake.Turtle.DONATELLO
        self.patched_library.niFake_EnumInputFunctionWithDefaults_cfunc.side_effect = self.side_effects_helper.niFake_EnumInputFunctionWithDefaults
        with nifake.Session('dev1') as session:
            session.enum_input_function_with_defaults()
            session.enum_input_function_with_defaults(test_turtle)
            from unittest.mock import call
            calls = [call(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt16Matcher(0)), call(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt16Matcher(1))]  # 0 is the value of the default of nifake.Turtle.LEONARDO, 1 is the value of nifake.Turtle.DONATELLO
            self.patched_library.niFake_EnumInputFunctionWithDefaults_cfunc.assert_has_calls(calls)

    def test_string_valued_enum_input_function_with_defaults(self):
        test_mobile_os_name = nifake.MobileOSNames.IOS
        self.patched_library.niFake_StringValuedEnumInputFunctionWithDefaults_cfunc.side_effect = self.side_effects_helper.niFake_StringValuedEnumInputFunctionWithDefaults
        with nifake.Session('dev1') as session:
            session.string_valued_enum_input_function_with_defaults()
            session.string_valued_enum_input_function_with_defaults(test_mobile_os_name)
            from unittest.mock import call
            calls = [call(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher('Android')), call(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher('iOS'))]  # 'ANDROID' is the value of the default of nifake.MobileOSNames.Android, 'iOS' is the value of nifake.MobileOSNames.IOS
            self.patched_library.niFake_StringValuedEnumInputFunctionWithDefaults_cfunc.assert_has_calls(calls)

    def test_fetch_waveform(self):
        expected_waveform_list = [1.0, 0.1, 42, .42]
        self.patched_library.niFake_FetchWaveform_cfunc.side_effect = self.side_effects_helper.niFake_FetchWaveform
        self.side_effects_helper['FetchWaveform']['waveformData'] = expected_waveform_list
        self.side_effects_helper['FetchWaveform']['actualNumberOfSamples'] = len(expected_waveform_list)

        # Because we are mocking get_ctypes_pointer_for_buffer() we don't end up using the array allocated in the function call. Instead, we will allocate the arrays here
        # and have the mock return them. These are the ones that are actually filled in by the function.
        expected_waveform = array.array('d', [0] * len(expected_waveform_list))
        expected_waveform_ctypes = ctypes.cast(expected_waveform.buffer_info()[0], ctypes.POINTER(nifake._visatype.ViReal64 * len(expected_waveform_list)))

        with nifake.Session('dev1') as session:
            self.get_ctypes_pointer_for_buffer_side_effect_items = [expected_waveform_ctypes]
            self.get_ctypes_pointer_for_buffer_side_effect_count = 0
            self.patched_library.niFake_WriteWaveform_cfunc.side_effect = self.side_effects_helper.niFake_WriteWaveform
            with patch('nifake._library_interpreter.get_ctypes_pointer_for_buffer', side_effect=self.get_ctypes_pointer_for_buffer_side_effect):
                # Because we have mocked away get_ctypes_pointer_for_buffer(), we ignore the return values here and look at our already allocated arrays to make
                # sure they are filled in correctly
                session.fetch_waveform(len(expected_waveform_list))
            assert isinstance(expected_waveform[0], float)
            assert len(expected_waveform) == len(expected_waveform_list)
            for i in range(len(expected_waveform)):
                assert expected_waveform[i] == expected_waveform_list[i]
        self.patched_library.niFake_FetchWaveform_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(expected_waveform)), _matchers.ViReal64BufferMatcher(expected_waveform), _matchers.ViInt32PointerMatcher())

    def test_fetch_waveform_into(self):
        expected_waveform = [1.0, 0.1, 42, .42]
        self.patched_library.niFake_FetchWaveform_cfunc.side_effect = self.side_effects_helper.niFake_FetchWaveform
        self.side_effects_helper['FetchWaveform']['waveformData'] = expected_waveform
        self.side_effects_helper['FetchWaveform']['actualNumberOfSamples'] = len(expected_waveform)
        with nifake.Session('dev1') as session:
            waveform = numpy.empty(len(expected_waveform), numpy.float64)
            session.fetch_waveform_into(waveform)
            assert numpy.array_equal(waveform, expected_waveform)
            self.patched_library.niFake_FetchWaveform_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(expected_waveform)), _matchers.ViReal64BufferMatcher(expected_waveform), _matchers.ViInt32PointerMatcher())

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

    def test_write_waveform(self):
        expected_waveform = [1.1, 2.2, 3.3, 4.4]
        expected_array = array.array('d', expected_waveform)
        with nifake.Session('dev1') as session:
            self.get_ctypes_pointer_for_buffer_side_effect_items = [expected_waveform]
            self.get_ctypes_pointer_for_buffer_side_effect_count = 0
            self.patched_library.niFake_WriteWaveform_cfunc.side_effect = self.side_effects_helper.niFake_WriteWaveform
            with patch('nifake._library_interpreter.get_ctypes_pointer_for_buffer', side_effect=self.get_ctypes_pointer_for_buffer_side_effect):
                session.write_waveform(expected_array)
            self.patched_library.niFake_WriteWaveform_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(expected_waveform)), _matchers.ViReal64BufferMatcher(expected_array))

    def test_write_waveform_numpy(self):
        expected_waveform = numpy.array([1.1, 2.2, 3.3, 4.4], order='C')
        self.patched_library.niFake_WriteWaveform_cfunc.side_effect = self.side_effects_helper.niFake_WriteWaveform
        with nifake.Session('dev1') as session:
            session.write_waveform_numpy(expected_waveform)
            self.patched_library.niFake_WriteWaveform_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(expected_waveform)), _matchers.ViReal64BufferMatcher(expected_waveform))

    def test_return_multiple_types(self):
        self.patched_library.niFake_ReturnMultipleTypes_cfunc.side_effect = self.side_effects_helper.niFake_ReturnMultipleTypes
        boolean_val = True
        int32_val = 32
        int64_val = 6000000000
        enum_val = nifake.Turtle.LEONARDO
        float_val = 1.23
        float_enum_val = nifake.FloatEnum.SIX_POINT_FIVE
        array_val = [0, 1, 2]
        array_size = len(array_val)
        string_val = 'Testing is fun?'
        self.side_effects_helper['ReturnMultipleTypes']['return'] = len(string_val)
        self.side_effects_helper['ReturnMultipleTypes']['aBoolean'] = boolean_val
        self.side_effects_helper['ReturnMultipleTypes']['anInt32'] = int32_val
        self.side_effects_helper['ReturnMultipleTypes']['anInt64'] = int64_val
        self.side_effects_helper['ReturnMultipleTypes']['anIntEnum'] = enum_val.value
        self.side_effects_helper['ReturnMultipleTypes']['aFloat'] = float_val
        self.side_effects_helper['ReturnMultipleTypes']['aFloatEnum'] = float_enum_val.value
        self.side_effects_helper['ReturnMultipleTypes']['anArray'] = array_val
        self.side_effects_helper['ReturnMultipleTypes']['aString'] = string_val
        self.side_effects_helper['ReturnMultipleTypes']['return'] = 0
        with nifake.Session('dev1') as session:
            result_boolean, result_int32, result_int64, result_enum, result_float, result_float_enum, result_array, result_string = session.return_multiple_types(array_size)
            assert result_boolean == boolean_val
            assert isinstance(result_boolean, bool)
            assert result_int32 == int32_val
            assert isinstance(result_int32, int)
            assert result_int64 == int64_val
            assert isinstance(result_int64, int)
            assert result_enum == enum_val
            assert isinstance(result_enum, nifake.Turtle)
            assert result_float == float_val
            assert isinstance(result_float, float)
            assert result_float_enum == float_enum_val
            assert isinstance(result_float_enum, nifake.FloatEnum)
            assert result_array == array_val
            assert isinstance(result_array, list)
            assert isinstance(result_array[0], float)
            assert result_string == string_val
            assert isinstance(result_string, str)
            assert self.patched_library.niFake_ReturnMultipleTypes_cfunc.call_count == 2

    def test_multiple_array_types(self):
        self.patched_library.niFake_MultipleArrayTypes_cfunc.side_effect = self.side_effects_helper.niFake_MultipleArrayTypes
        expected_output_array = [0.2, 0.4]
        expected_output_array_of_fixed_length = [-6, -7, -8]
        output_array_size = len(expected_output_array)
        input_array_of_integers = [1, 2]
        input_array_of_floats = [-1.0, -2.0]
        self.side_effects_helper['MultipleArrayTypes']['outputArray'] = expected_output_array
        self.side_effects_helper['MultipleArrayTypes']['outputArrayOfFixedLength'] = expected_output_array_of_fixed_length
        with nifake.Session('dev1') as session:
            output_array, output_array_of_fixed_length = session.multiple_array_types(output_array_size, input_array_of_floats, input_array_of_integers)
            assert output_array == output_array
            assert expected_output_array_of_fixed_length == output_array_of_fixed_length
            self.patched_library.niFake_MultipleArrayTypes_cfunc.assert_called_once_with(
                _matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST),
                _matchers.ViInt32Matcher(output_array_size),
                _matchers.ViReal64BufferMatcher(output_array_size),
                _matchers.ViReal64BufferMatcher(len(expected_output_array_of_fixed_length)),
                _matchers.ViInt32Matcher(len(input_array_of_integers)),
                _matchers.ViReal64BufferMatcher(input_array_of_floats),
                _matchers.ViInt16BufferMatcher(input_array_of_integers),
            )

    def test_multiple_array_types_none_input(self):
        self.patched_library.niFake_MultipleArrayTypes_cfunc.side_effect = self.side_effects_helper.niFake_MultipleArrayTypes
        expected_output_array = [0.2, 0.4]
        expected_output_array_of_fixed_length = [-6, -7, -8]
        output_array_size = len(expected_output_array)
        input_array_of_floats = [0.1, 0.2]
        self.side_effects_helper['MultipleArrayTypes']['outputArray'] = expected_output_array
        self.side_effects_helper['MultipleArrayTypes']['outputArrayOfFixedLength'] = expected_output_array_of_fixed_length
        with nifake.Session('dev1') as session:
            output_array, output_array_of_fixed_length = session.multiple_array_types(output_array_size, input_array_of_floats)
            assert output_array == output_array
            assert expected_output_array_of_fixed_length == output_array_of_fixed_length
            self.patched_library.niFake_MultipleArrayTypes_cfunc.assert_called_once_with(
                _matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST),
                _matchers.ViInt32Matcher(output_array_size),
                _matchers.ViReal64BufferMatcher(output_array_size),
                _matchers.ViReal64BufferMatcher(len(expected_output_array_of_fixed_length)),
                _matchers.ViInt32Matcher(len(input_array_of_floats)),
                _matchers.ViReal64BufferMatcher(input_array_of_floats),
                None
            )

    def test_multiple_arrays_same_size(self):
        self.patched_library.niFake_MultipleArraysSameSize_cfunc.side_effect = self.side_effects_helper.niFake_MultipleArraysSameSize
        input_array_of_floats1 = [0.041, 0.042, 0.043, 0.044]
        input_array_of_floats2 = [0.410, 0.420, 0.430, 0.440]
        input_array_of_floats3 = [4.100, 4.200, 4.300, 4.400]
        input_array_of_floats4 = [41.00, 42.00, 43.00, 44.00]
        with nifake.Session('dev1') as session:
            session.multiple_arrays_same_size(input_array_of_floats1, input_array_of_floats2, input_array_of_floats3, input_array_of_floats4)
            self.patched_library.niFake_MultipleArraysSameSize_cfunc.assert_called_once_with(
                _matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST),
                _matchers.ViReal64BufferMatcher(input_array_of_floats1),
                _matchers.ViReal64BufferMatcher(input_array_of_floats2),
                _matchers.ViReal64BufferMatcher(input_array_of_floats3),
                _matchers.ViReal64BufferMatcher(input_array_of_floats4),
                _matchers.ViInt32Matcher(len(input_array_of_floats1)),
            )

    def test_multiple_arrays_same_size_none_input(self):
        self.patched_library.niFake_MultipleArraysSameSize_cfunc.side_effect = self.side_effects_helper.niFake_MultipleArraysSameSize
        input_array_of_floats1 = [0.041, 0.042, 0.043, 0.044]
        with nifake.Session('dev1') as session:
            session.multiple_arrays_same_size(input_array_of_floats1, None, None, None)
            self.patched_library.niFake_MultipleArraysSameSize_cfunc.assert_called_once_with(
                _matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST),
                _matchers.ViReal64BufferMatcher(input_array_of_floats1),
                None,
                None,
                None,
                _matchers.ViInt32Matcher(len(input_array_of_floats1)),
            )

    def test_multiple_arrays_same_size_wrong_size_2(self):
        self.patched_library.niFake_MultipleArraysSameSize_cfunc.side_effect = self.side_effects_helper.niFake_MultipleArraysSameSize
        input_array_of_floats1 = [0.041, 0.042, 0.043, 0.044]
        input_array_of_floats2 = [0.410, 0.420, 0.430]
        input_array_of_floats3 = [4.100, 4.200, 4.300, 4.400]
        input_array_of_floats4 = [41.00, 42.00, 43.00, 44.00]
        with nifake.Session('dev1') as session:
            try:
                session.multiple_arrays_same_size(input_array_of_floats1, input_array_of_floats2, input_array_of_floats3, input_array_of_floats4)
                assert False
            except ValueError:
                pass

    def test_multiple_arrays_same_size_wrong_size_3(self):
        self.patched_library.niFake_MultipleArraysSameSize_cfunc.side_effect = self.side_effects_helper.niFake_MultipleArraysSameSize
        input_array_of_floats1 = [0.041, 0.042, 0.043, 0.044]
        input_array_of_floats2 = [0.410, 0.420, 0.430, 0.440]
        input_array_of_floats3 = [4.100, 4.200, 4.400]
        input_array_of_floats4 = [41.00, 42.00, 43.00, 44.00]
        with nifake.Session('dev1') as session:
            try:
                session.multiple_arrays_same_size(input_array_of_floats1, input_array_of_floats2, input_array_of_floats3, input_array_of_floats4)
                assert False
            except ValueError:
                pass

    def test_multiple_arrays_same_size_wrong_size_4(self):
        self.patched_library.niFake_MultipleArraysSameSize_cfunc.side_effect = self.side_effects_helper.niFake_MultipleArraysSameSize
        input_array_of_floats1 = [0.041, 0.042, 0.043, 0.044]
        input_array_of_floats2 = [0.410, 0.420, 0.430, 0.440]
        input_array_of_floats3 = [4.100, 4.200, 4.300, 4.400]
        input_array_of_floats4 = [41.00, 42.00, 43.00, 44.00, 45.00]
        with nifake.Session('dev1') as session:
            try:
                session.multiple_arrays_same_size(input_array_of_floats1, input_array_of_floats2, input_array_of_floats3, input_array_of_floats4)
                assert False
            except ValueError:
                pass

    def test_parameters_are_multiple_types(self):
        self.patched_library.niFake_ParametersAreMultipleTypes_cfunc.side_effect = self.side_effects_helper.niFake_ParametersAreMultipleTypes
        boolean_val = True
        int32_val = 32
        int64_val = 6000000000
        enum_val = nifake.Turtle.LEONARDO
        float_val = 1.23
        float_enum_val = nifake.FloatEnum.SIX_POINT_FIVE
        string_val = 'Testing is fun?'
        with nifake.Session('dev1') as session:
            session.parameters_are_multiple_types(boolean_val, int32_val, int64_val, enum_val, float_val, float_enum_val, string_val)
            self.patched_library.niFake_ParametersAreMultipleTypes_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViBooleanMatcher(boolean_val), _matchers.ViInt32Matcher(int32_val), _matchers.ViInt64Matcher(int64_val), _matchers.ViInt16Matcher(enum_val.value), _matchers.ViReal64Matcher(float_val), _matchers.ViReal64Matcher(float_enum_val.value), _matchers.ViInt32Matcher(len(string_val)), _matchers.ViStringMatcher(string_val))

    def test_parameters_are_multiple_types_error(self):
        test_error_code = -42
        test_error_desc = "The answer to the ultimate question"
        self.patched_library.niFake_ParametersAreMultipleTypes_cfunc.side_effect = self.side_effects_helper.niFake_ParametersAreMultipleTypes
        self.side_effects_helper['ParametersAreMultipleTypes']['return'] = test_error_code
        self.patched_library.niFake_GetError_cfunc.side_effect = self.side_effects_helper.niFake_GetError
        self.side_effects_helper['GetError']['errorCode'] = test_error_code
        self.side_effects_helper['GetError']['description'] = test_error_desc
        self.patched_library.niFake_ParametersAreMultipleTypes_cfunc.side_effect = self.side_effects_helper.niFake_ParametersAreMultipleTypes
        self.side_effects_helper['ParametersAreMultipleTypes']['return'] = test_error_code
        self.patched_library.niFake_GetError_cfunc.side_effect = self.side_effects_helper.niFake_GetError
        self.side_effects_helper['GetError']['errorCode'] = test_error_code
        self.side_effects_helper['GetError']['description'] = test_error_desc
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

    def test_method_with_error(self):
        test_error_code = -42
        test_error_desc = "The answer to the ultimate question"
        self.patched_library.niFake_PoorlyNamedSimpleFunction_cfunc.side_effect = self.side_effects_helper.niFake_PoorlyNamedSimpleFunction
        self.side_effects_helper['PoorlyNamedSimpleFunction']['return'] = test_error_code
        self.patched_library.niFake_GetError_cfunc.side_effect = self.side_effects_helper.niFake_GetError
        self.side_effects_helper['GetError']['errorCode'] = test_error_code
        self.side_effects_helper['GetError']['description'] = test_error_desc
        with nifake.Session('dev1') as session:
            try:
                session.simple_function()
                assert False
            except nifake.Error as e:
                assert e.code == test_error_code
                assert e.description == test_error_desc

    def test_error_with_rep_cap(self):
        test_error_code = -42
        test_error_desc = "The answer to the ultimate question"
        self.patched_library.niFake_SetAttributeViReal64_cfunc.side_effect = self.side_effects_helper.niFake_SetAttributeViReal64
        self.side_effects_helper['SetAttributeViReal64']['return'] = test_error_code
        self.patched_library.niFake_GetError_cfunc.side_effect = self.side_effects_helper.niFake_GetError
        self.side_effects_helper['GetError']['errorCode'] = test_error_code
        self.side_effects_helper['GetError']['description'] = test_error_desc
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

    def test_invalid_method_call_wrong_type_error(self):
        with nifake.Session('dev1') as session:
            try:
                session.multiple_array_types('potato', [0.0, 0.1, 0.2])
                assert False
            except TypeError:
                pass

    def test_enum_input_function_with_defaults_bad_type_error(self):
        test_turtle = 123
        self.patched_library.niFake_EnumInputFunctionWithDefaults_cfunc.side_effect = self.side_effects_helper.niFake_EnumInputFunctionWithDefaults
        with nifake.Session('dev1') as session:
            try:
                session.enum_input_function_with_defaults(test_turtle)
                assert False
            except TypeError:
                pass

    def test_method_with_warning(self):
        # We want to capture all of our warnings, not just the first one
        warnings.filterwarnings("always", category=nifake.DriverWarning)

        test_error_code = 42
        test_error_desc = "The answer to the ultimate question, only positive"
        self.patched_library.niFake_PoorlyNamedSimpleFunction_cfunc.side_effect = self.side_effects_helper.niFake_PoorlyNamedSimpleFunction
        self.side_effects_helper['PoorlyNamedSimpleFunction']['return'] = test_error_code
        self.patched_library.niFake_GetError_cfunc.side_effect = self.side_effects_helper.niFake_GetError
        self.side_effects_helper['GetError']['errorCode'] = test_error_code
        self.side_effects_helper['GetError']['description'] = test_error_desc
        with nifake.Session('dev1') as session:
            with warnings.catch_warnings(record=True) as w:
                session.simple_function()
                assert len(w) == 1
                assert issubclass(w[0].category, nifake.DriverWarning)
                assert test_error_desc in str(w[0].message)

    def test_read_with_warning(self):
        # We want to capture all of our warnings, not just the first one
        warnings.filterwarnings("always", category=nifake.DriverWarning)

        test_maximum_time_s = 10.0
        test_maximum_time = hightime.timedelta(seconds=test_maximum_time_s)
        test_reading = float('nan')
        test_error_code = 42
        test_error_desc = "The answer to the ultimate question, only positive"
        self.patched_library.niFake_Read_cfunc.side_effect = self.niFake_read_warning
        self.error_code_return = test_error_code
        self.reading = test_reading
        self.patched_library.niFake_GetError_cfunc.side_effect = self.side_effects_helper.niFake_GetError
        self.side_effects_helper['GetError']['errorCode'] = test_error_code
        self.side_effects_helper['GetError']['description'] = test_error_desc
        with nifake.Session('dev1') as session:
            with warnings.catch_warnings(record=True) as w:
                assert math.isnan(session.read(test_maximum_time))
                assert len(w) == 1
                assert issubclass(w[0].category, nifake.DriverWarning)
                assert test_error_desc in str(w[0].message)

    def test_get_channel_names(self):
        channel_indices = [0, 3, 2]
        expected_channel_names_string = '0,3,2'
        expected_channel_names_string_size = len(expected_channel_names_string)
        expected_channel_names = ['0', '3', '2']
        self.patched_library.niFake_GetChannelNames_cfunc.side_effect = self.side_effects_helper.niFake_GetChannelNames
        self.side_effects_helper['GetChannelNames']['names'] = expected_channel_names_string
        with nifake.Session('dev1') as session:
            channel_names_from_session = session.get_channel_names(channel_indices)
            assert channel_names_from_session == expected_channel_names
            from unittest.mock import call
            expected_calls = [
                call(
                    _matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST),
                    _matchers.ViStringMatcher(expected_channel_names_string),
                    _matchers.ViInt32Matcher(0),
                    None
                ),
                call(
                    _matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST),
                    _matchers.ViStringMatcher(expected_channel_names_string),
                    _matchers.ViInt32Matcher(expected_channel_names_string_size),
                    _matchers.ViCharBufferMatcher(expected_channel_names_string_size)
                )
            ]
            self.patched_library.niFake_GetChannelNames_cfunc.assert_has_calls(expected_calls)
            assert self.patched_library.niFake_GetChannelNames_cfunc.call_count == len(expected_calls)

    # Retrieving buffers and strings

    def test_get_a_string_of_fixed_maximum_size(self):
        test_string = "A string no larger than the max size of 256 allowed by the function."
        self.patched_library.niFake_GetAStringOfFixedMaximumSize_cfunc.side_effect = self.side_effects_helper.niFake_GetAStringOfFixedMaximumSize
        self.side_effects_helper['GetAStringOfFixedMaximumSize']['aString'] = test_string
        with nifake.Session('dev1') as session:
            returned_string = session.get_a_string_of_fixed_maximum_size()
            assert returned_string == test_string
            self.patched_library.niFake_GetAStringOfFixedMaximumSize_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViCharBufferMatcher(256))

    def test_get_a_string_of_size_python_code(self):
        test_size = 4
        expected_string_size = test_size - 1
        test_string = "A string that is larger than test_size."
        expected_string = test_string[:expected_string_size]
        self.patched_library.niFake_GetAStringUsingPythonCode_cfunc.side_effect = self.side_effects_helper.niFake_GetAStringUsingPythonCode
        self.side_effects_helper['GetAStringUsingPythonCode']['aString'] = expected_string
        with nifake.Session('dev1') as session:
            returned_string = session.get_a_string_using_python_code(test_size)
            assert returned_string == expected_string
            self.patched_library.niFake_GetAStringUsingPythonCode_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt16Matcher(test_size), _matchers.ViCharBufferMatcher(test_size))

    def test_return_a_number_and_a_string(self):
        test_string = "this string"
        test_number = 13
        self.patched_library.niFake_ReturnANumberAndAString_cfunc.side_effect = self.side_effects_helper.niFake_ReturnANumberAndAString
        self.side_effects_helper['ReturnANumberAndAString']['aString'] = test_string
        self.side_effects_helper['ReturnANumberAndAString']['aNumber'] = test_number
        with nifake.Session('dev1') as session:
            returned_number, returned_string = session.return_a_number_and_a_string()
            assert (returned_string == test_string)
            assert (returned_number == test_number)
            self.patched_library.niFake_ReturnANumberAndAString_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt16PointerMatcher(), _matchers.ViCharBufferMatcher(256))

    def test_get_an_ivi_dance_string(self):
        self.patched_library.niFake_GetAnIviDanceString_cfunc.side_effect = self.side_effects_helper.niFake_GetAnIviDanceString
        string_val = 'Testing is fun?'
        self.side_effects_helper['GetAnIviDanceString']['aString'] = string_val
        with nifake.Session('dev1') as session:
            result_string = session.get_an_ivi_dance_string()
            assert result_string == string_val
            from unittest.mock import call
            calls = [call(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(0), None), call(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(string_val)), _matchers.ViCharBufferMatcher(len(string_val)))]
            self.patched_library.niFake_GetAnIviDanceString_cfunc.assert_has_calls(calls)
            assert self.patched_library.niFake_GetAnIviDanceString_cfunc.call_count == 2

    def test_get_string_ivi_dance_error(self):
        test_error_code = -1234
        test_error_desc = "ascending order"
        self.patched_library.niFake_GetAttributeViString_cfunc.side_effect = self.side_effects_helper.niFake_GetAttributeViString
        self.side_effects_helper['GetAttributeViString']['attributeValue'] = 'Testing is fun?'
        self.side_effects_helper['GetAttributeViString']['return'] = test_error_code
        self.patched_library.niFake_GetError_cfunc.side_effect = self.side_effects_helper.niFake_GetError
        self.side_effects_helper['GetError']['errorCode'] = test_error_code
        self.side_effects_helper['GetError']['description'] = test_error_desc
        with nifake.Session('dev1') as session:
            try:
                session.read_write_string
                assert False
            except nifake.Error as e:
                assert e.code == test_error_code
                assert e.description == test_error_desc

    def test_get_an_ivi_dance_with_a_twist_string(self):
        self.patched_library.niFake_GetAnIviDanceWithATwistString_cfunc.side_effect = self.side_effects_helper.niFake_GetAnIviDanceWithATwistString
        string_val = 'Testing is fun?'
        self.side_effects_helper['GetAnIviDanceWithATwistString']['aString'] = string_val
        self.side_effects_helper['GetAnIviDanceWithATwistString']['actualSize'] = len(string_val)
        with nifake.Session('dev1') as session:
            result_string = session.get_an_ivi_dance_with_a_twist_string()
            assert result_string == string_val
            from unittest.mock import call
            calls = [
                call(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(0), None, _matchers.ViInt32PointerMatcher()),
                call(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(string_val)), _matchers.ViCharBufferMatcher(len(string_val)), _matchers.ViInt32PointerMatcher())
            ]
            self.patched_library.niFake_GetAnIviDanceWithATwistString_cfunc.assert_has_calls(calls)
            assert self.patched_library.niFake_GetAnIviDanceWithATwistString_cfunc.call_count == 2

    def test_get_array_using_ivi_dance(self):
        self.patched_library.niFake_GetArrayUsingIviDance_cfunc.side_effect = self.side_effects_helper.niFake_GetArrayUsingIviDance
        self.side_effects_helper['GetArrayUsingIviDance']['arrayOut'] = [1.1, 2.2]
        with nifake.Session('dev1') as session:
            result_array = session.get_array_using_ivi_dance()
            assert result_array == [1.1, 2.2]

    # Repeated Capabilities

    def test_repeated_capability_method_on_session_timedelta(self):
        test_maximum_time_ms = 10     # milliseconds
        test_maximum_time_timedelta = hightime.timedelta(milliseconds=test_maximum_time_ms)
        test_reading = 5
        self.patched_library.niFake_ReadFromChannel_cfunc.side_effect = self.side_effects_helper.niFake_ReadFromChannel
        self.side_effects_helper['ReadFromChannel']['reading'] = test_reading
        with nifake.Session('dev1') as session:
            value = session.read_from_channel(test_maximum_time_timedelta)
        self.patched_library.niFake_ReadFromChannel_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViInt32Matcher(test_maximum_time_ms), _matchers.ViReal64PointerMatcher())
        assert value == test_reading

    def test_repeated_capability_method_on_specific_channel(self):
        test_maximum_time_ms = 10     # milliseconds
        test_maximum_time = hightime.timedelta(milliseconds=test_maximum_time_ms)
        test_reading = 5
        self.patched_library.niFake_ReadFromChannel_cfunc.side_effect = self.side_effects_helper.niFake_ReadFromChannel
        self.side_effects_helper['ReadFromChannel']['reading'] = test_reading
        with nifake.Session('dev1') as session:
            value = session.channels['3'].read_from_channel(test_maximum_time)
        self.patched_library.niFake_ReadFromChannel_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher('3'), _matchers.ViInt32Matcher(test_maximum_time_ms), _matchers.ViReal64PointerMatcher())
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
        self.patched_library.niFake_ReadFromChannel_cfunc.side_effect = self.side_effects_helper.niFake_ReadFromChannel
        self.side_effects_helper['ReadFromChannel']['reading'] = test_reading
        with nifake.Session('dev1') as session:
            value = session.sites[0, 1].channels[2, 3].read_from_channel(test_maximum_time)
        self.patched_library.niFake_ReadFromChannel_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher('site0/2,site0/3,site1/2,site1/3'), _matchers.ViInt32Matcher(test_maximum_time_ms), _matchers.ViReal64PointerMatcher())
        assert value == test_reading

    def test_function_with_repeated_capability_type(self):
        self.patched_library.niFake_FunctionWithRepeatedCapabilityType_cfunc.side_effect = self.side_effects_helper.niFake_FunctionWithRepeatedCapabilityType
        with nifake.Session('dev1') as session:
            session.channels['0-3'].function_with_repeated_capability_type()
            self.patched_library.niFake_FunctionWithRepeatedCapabilityType_cfunc.assert_called_once_with(
                _matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST),
                _matchers.ViStringMatcher('0,1,2,3')
            )

    # Attributes

    def test_get_attribute_int32(self):
        self.patched_library.niFake_GetAttributeViInt32_cfunc.side_effect = self.side_effects_helper.niFake_GetAttributeViInt32
        test_number = 3
        self.side_effects_helper['GetAttributeViInt32']['attributeValue'] = test_number
        with nifake.Session('dev1') as session:
            attr_int = session.read_write_integer
            assert(attr_int == test_number)
            self.patched_library.niFake_GetAttributeViInt32_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(1000004), _matchers.ViInt32PointerMatcher())

    def test_set_attribute_int32(self):
        self.patched_library.niFake_SetAttributeViInt32_cfunc.side_effect = self.side_effects_helper.niFake_SetAttributeViInt32
        attribute_id = 1000004
        test_number = -10
        with nifake.Session('dev1') as session:
            session.read_write_integer = test_number
            self.patched_library.niFake_SetAttributeViInt32_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViInt32Matcher(test_number))

    def test_get_attribute_int32_with_converter(self):
        self.patched_library.niFake_GetAttributeViInt32_cfunc.side_effect = self.side_effects_helper.niFake_GetAttributeViInt32
        attribute_id = 1000008
        test_number_ms = 3
        test_number_s = 0.003
        self.side_effects_helper['GetAttributeViInt32']['attributeValue'] = test_number_ms
        with nifake.Session('dev1') as session:
            attr_timedelta = session.read_write_integer_with_converter
            assert(attr_timedelta.total_seconds() == test_number_s)
            self.patched_library.niFake_GetAttributeViInt32_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViInt32PointerMatcher())

    def test_set_attribute_int32_with_converter(self):
        self.patched_library.niFake_SetAttributeViInt32_cfunc.side_effect = self.side_effects_helper.niFake_SetAttributeViInt32
        attribute_id = 1000008
        test_number_ms = -10000
        with nifake.Session('dev1') as session:
            session.read_write_integer_with_converter = hightime.timedelta(milliseconds=test_number_ms)
            self.patched_library.niFake_SetAttributeViInt32_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViInt32Matcher(test_number_ms))

    def test_get_attribute_real64(self):
        self.patched_library.niFake_GetAttributeViReal64_cfunc.side_effect = self.side_effects_helper.niFake_GetAttributeViReal64
        test_number = 1.5
        self.side_effects_helper['GetAttributeViReal64']['attributeValue'] = test_number
        with nifake.Session('dev1') as session:
            attr_double = session.read_write_double
            assert attr_double == test_number
            self.patched_library.niFake_GetAttributeViReal64_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(1000001), _matchers.ViReal64PointerMatcher())

    def test_set_attribute_real64(self):
        self.patched_library.niFake_SetAttributeViReal64_cfunc.side_effect = self.side_effects_helper.niFake_SetAttributeViReal64
        attribute_id = 1000001
        test_number = 10.1
        with nifake.Session('dev1') as session:
            session.read_write_double = test_number
            self.patched_library.niFake_SetAttributeViReal64_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViReal64Matcher(test_number))

    def test_get_attribute_real64_with_converter(self):
        self.patched_library.niFake_GetAttributeViReal64_cfunc.side_effect = self.side_effects_helper.niFake_GetAttributeViReal64
        attribute_id = 1000007
        test_number = 1e-9
        self.side_effects_helper['GetAttributeViReal64']['attributeValue'] = test_number
        with nifake.Session('dev1') as session:
            attr_timedelta = session.read_write_double_with_converter
            assert attr_timedelta.total_seconds() == test_number
            self.patched_library.niFake_GetAttributeViReal64_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViReal64PointerMatcher())

    def test_set_attribute_real64_with_converter(self):
        self.patched_library.niFake_SetAttributeViReal64_cfunc.side_effect = self.side_effects_helper.niFake_SetAttributeViReal64
        attribute_id = 1000007
        test_number = 1e-9
        with nifake.Session('dev1') as session:
            session.read_write_double_with_converter = hightime.timedelta(nanoseconds=1)
            self.patched_library.niFake_SetAttributeViReal64_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViReal64Matcher(test_number))

    def test_get_attribute_string(self):
        self.patched_library.niFake_GetAttributeViString_cfunc.side_effect = self.side_effects_helper.niFake_GetAttributeViString
        string = 'Testing is fun?'
        self.side_effects_helper['GetAttributeViString']['attributeValue'] = string
        with nifake.Session('dev1') as session:
            attr_string = session.read_write_string
            assert attr_string == string
            from unittest.mock import call
            calls = [call(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(1000002), _matchers.ViInt32Matcher(0), None), call(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(1000002), _matchers.ViInt32Matcher(15), _matchers.ViCharBufferMatcher(len(string)))]
            self.patched_library.niFake_GetAttributeViString_cfunc.assert_has_calls(calls)
            assert self.patched_library.niFake_GetAttributeViString_cfunc.call_count == 2

    def test_set_attribute_string(self):
        self.patched_library.niFake_SetAttributeViString_cfunc.side_effect = self.side_effects_helper.niFake_SetAttributeViString
        attribute_id = 1000002
        attrib_string = 'This is test string'
        with nifake.Session('dev1') as session:
            session.read_write_string = attrib_string
            self.patched_library.niFake_SetAttributeViString_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViStringMatcher('This is test string'))

    def test_get_attribute_string_with_converter(self):
        self.patched_library.niFake_GetAttributeViString_cfunc.side_effect = self.side_effects_helper.niFake_GetAttributeViString
        string = 'not that interesting'
        self.side_effects_helper['GetAttributeViString']['attributeValue'] = string
        with nifake.Session('dev1') as session:
            attr_string = session.read_write_string_repeated_capability
            assert attr_string == string
            from unittest.mock import call
            calls = [call(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(1000010), _matchers.ViInt32Matcher(0), None), call(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(1000010), _matchers.ViInt32Matcher(20), _matchers.ViCharBufferMatcher(len(string)))]
            self.patched_library.niFake_GetAttributeViString_cfunc.assert_has_calls(calls)
            assert self.patched_library.niFake_GetAttributeViString_cfunc.call_count == 2

    def test_set_attribute_string_with_converter(self):
        self.patched_library.niFake_SetAttributeViString_cfunc.side_effect = self.side_effects_helper.niFake_SetAttributeViString
        attribute_id = 1000010
        with nifake.Session('dev1') as session:
            session.read_write_string_repeated_capability = 42
            self.patched_library.niFake_SetAttributeViString_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViStringMatcher('42'))

    def test_get_attribute_boolean(self):
        self.patched_library.niFake_GetAttributeViBoolean_cfunc.side_effect = self.side_effects_helper.niFake_GetAttributeViBoolean
        self.side_effects_helper['GetAttributeViBoolean']['attributeValue'] = 1
        with nifake.Session('dev1') as session:
            assert session.read_write_bool
            self.patched_library.niFake_GetAttributeViBoolean_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(1000000), _matchers.ViBooleanPointerMatcher())

    def test_set_attribute_boolean(self):
        self.patched_library.niFake_SetAttributeViBoolean_cfunc.side_effect = self.side_effects_helper.niFake_SetAttributeViBoolean
        attribute_id = 1000000
        attrib_bool = True
        with nifake.Session('dev1') as session:
            session.read_write_bool = attrib_bool
            self.patched_library.niFake_SetAttributeViBoolean_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViBooleanMatcher(True))

    def test_get_attribute_enum_int32(self):
        self.patched_library.niFake_GetAttributeViInt32_cfunc.side_effect = self.side_effects_helper.niFake_GetAttributeViInt32
        self.side_effects_helper['GetAttributeViInt32']['attributeValue'] = nifake.Color.BLUE.value
        with nifake.Session('dev1') as session:
            assert session.read_write_color == nifake.Color.BLUE
            attribute_id = 1000003
            self.patched_library.niFake_GetAttributeViInt32_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViInt32PointerMatcher())

    def test_set_attribute_enum_int32(self):
        self.patched_library.niFake_SetAttributeViInt32_cfunc.side_effect = self.side_effects_helper.niFake_SetAttributeViInt32
        enum_value = nifake.Color.RED
        with nifake.Session('dev1') as session:
            session.read_write_color = enum_value
            attribute_id = 1000003
            self.patched_library.niFake_SetAttributeViInt32_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViInt32Matcher(enum_value.value))

    def test_get_attribute_enum_real64(self):
        self.patched_library.niFake_GetAttributeViReal64_cfunc.side_effect = self.side_effects_helper.niFake_GetAttributeViReal64
        enum_value = nifake.FloatEnum.SIX_POINT_FIVE
        self.side_effects_helper['GetAttributeViReal64']['attributeValue'] = enum_value.value
        with nifake.Session('dev1') as session:
            assert session.float_enum == enum_value
            attribute_id = 1000005
            self.patched_library.niFake_GetAttributeViReal64_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViReal64PointerMatcher())

    def test_set_attribute_enum_real64(self):
        self.patched_library.niFake_SetAttributeViReal64_cfunc.side_effect = self.side_effects_helper.niFake_SetAttributeViReal64
        enum_value = nifake.FloatEnum.FIVE_POINT_FIVE
        with nifake.Session('dev1') as session:
            session.float_enum = enum_value
            attribute_id = 1000005
            self.patched_library.niFake_SetAttributeViReal64_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViReal64Matcher(enum_value.value))

    def test_get_attribute_enum_with_converter(self):
        enum_value = nifake.EnumWithConverter.RED
        converted_value = True
        self.patched_library.niFake_GetAttributeViInt32_cfunc.side_effect = self.side_effects_helper.niFake_GetAttributeViInt32
        self.side_effects_helper['GetAttributeViInt32']['attributeValue'] = enum_value.value
        with nifake.Session('dev1') as session:
            assert session.read_write_enum_with_converter == converted_value
            attribute_id = 1000011
            self.patched_library.niFake_GetAttributeViInt32_cfunc.assert_called_once_with(
                _matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST),
                _matchers.ViStringMatcher(''),
                _matchers.ViAttrMatcher(attribute_id),
                _matchers.ViInt32PointerMatcher()
            )

    def test_get_attribute_enum_with_converter_invalid_value_from_driver(self):
        invalid_value_from_driver = 0
        expected_error_message = 'The NI-FAKE runtime returned an unexpected value. This can occur if it is too new for the nifake Python module. Upgrade the nifake Python module.'
        self.patched_library.niFake_GetAttributeViInt32_cfunc.side_effect = self.side_effects_helper.niFake_GetAttributeViInt32
        self.side_effects_helper['GetAttributeViInt32']['attributeValue'] = invalid_value_from_driver
        with nifake.Session('dev1') as session:
            try:
                session.read_write_enum_with_converter
                assert False
            except nifake.errors.DriverTooNewError as actual_error:
                actual_error_message = actual_error.args[0]
                assert actual_error_message == expected_error_message
            attribute_id = 1000011
            self.patched_library.niFake_GetAttributeViInt32_cfunc.assert_called_once_with(
                _matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST),
                _matchers.ViStringMatcher(''),
                _matchers.ViAttrMatcher(attribute_id),
                _matchers.ViInt32PointerMatcher()
            )

    def test_set_attribute_enum_with_converter(self):
        enum_value = nifake.EnumWithConverter.RED
        converted_value = True
        self.patched_library.niFake_SetAttributeViInt32_cfunc.side_effect = self.side_effects_helper.niFake_SetAttributeViInt32
        with nifake.Session('dev1') as session:
            session.read_write_enum_with_converter = converted_value
            attribute_id = 1000011
            self.patched_library.niFake_SetAttributeViInt32_cfunc.assert_called_once_with(
                _matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST),
                _matchers.ViStringMatcher(''),
                _matchers.ViAttrMatcher(attribute_id),
                _matchers.ViInt32Matcher(enum_value.value)
            )

    def test_set_attribute_enum_with_converter_invalid_input(self):
        invalid_input_value = 'invalid'
        expected_error_description = "Invalid value: invalid"
        self.patched_library.niFake_SetAttributeViInt32_cfunc.side_effect = self.side_effects_helper.niFake_SetAttributeViInt32
        with nifake.Session('dev1') as session:
            try:
                session.read_write_enum_with_converter = invalid_input_value
                assert False
            except ValueError as actual_error:
                actual_error_message = actual_error.args[0]
                assert actual_error_message == expected_error_description
            assert not self.patched_library.niFake_SetAttributeViInt32_cfunc.called

    def test_get_attribute_channel(self):
        self.patched_library.niFake_GetAttributeViInt32_cfunc.side_effect = self.side_effects_helper.niFake_GetAttributeViInt32
        test_number = 100
        self.side_effects_helper['GetAttributeViInt32']['attributeValue'] = test_number
        with nifake.Session('dev1') as session:
            attr_int = session.channels[['0', '1']].read_write_integer
            assert(attr_int == test_number)
            self.patched_library.niFake_GetAttributeViInt32_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher('0,1'), _matchers.ViAttrMatcher(1000004), _matchers.ViInt32PointerMatcher())

    def test_set_attribute_channel(self):
        self.patched_library.niFake_SetAttributeViReal64_cfunc.side_effect = self.side_effects_helper.niFake_SetAttributeViReal64
        attribute_id = 1000001
        test_number = 0.001
        with nifake.Session('dev1') as session:
            session.channels[range(24)].read_write_double = test_number
            self.patched_library.niFake_SetAttributeViReal64_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher('0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23'), _matchers.ViAttrMatcher(attribute_id), _matchers.ViReal64Matcher(test_number))

    def test_get_attribute_int64(self):
        self.patched_library.niFake_GetAttributeViInt64_cfunc.side_effect = self.side_effects_helper.niFake_GetAttributeViInt64
        attribute_id = 1000006
        test_number = 6000000000
        self.side_effects_helper['GetAttributeViInt64']['attributeValue'] = test_number
        with nifake.Session('dev1') as session:
            attr_int = session.read_write_int64
            assert(attr_int == test_number)
            self.patched_library.niFake_GetAttributeViInt64_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViInt64PointerMatcher())

    def test_set_attribute_int64(self):
        self.patched_library.niFake_SetAttributeViInt64_cfunc.side_effect = self.side_effects_helper.niFake_SetAttributeViInt64
        attribute_id = 1000006
        test_number = -6000000000
        with nifake.Session('dev1') as session:
            session.read_write_int64 = test_number
            self.patched_library.niFake_SetAttributeViInt64_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViInt64Matcher(test_number))

    def test_get_attribute_error(self):
        test_error_code = -123
        test_error_desc = "ascending order"
        self.patched_library.niFake_GetAttributeViReal64_cfunc.side_effect = self.side_effects_helper.niFake_GetAttributeViReal64
        self.side_effects_helper['GetAttributeViReal64']['attributeValue'] = 'Testing is fun?'
        self.side_effects_helper['GetAttributeViReal64']['return'] = test_error_code
        self.patched_library.niFake_GetError_cfunc.side_effect = self.side_effects_helper.niFake_GetError
        self.side_effects_helper['GetError']['errorCode'] = test_error_code
        self.side_effects_helper['GetError']['description'] = test_error_desc
        with nifake.Session('dev1') as session:
            try:
                session.read_write_double
                assert False
            except nifake.Error as e:
                assert e.code == test_error_code
                assert e.description == test_error_desc

    def test_set_attribute_error(self):
        test_error_code = -1
        test_error_desc = 'Test'
        self.patched_library.niFake_SetAttributeViReal64_cfunc.side_effect = self.side_effects_helper.niFake_SetAttributeViReal64
        self.side_effects_helper['SetAttributeViReal64']['return'] = test_error_code
        self.patched_library.niFake_GetError_cfunc.side_effect = self.side_effects_helper.niFake_GetError
        self.side_effects_helper['GetError']['errorCode'] = test_error_code
        self.side_effects_helper['GetError']['description'] = test_error_desc
        with nifake.Session('dev1') as session:
            try:
                session.read_write_double = -42.0
                assert False
            except nifake.Error as e:
                assert e.code == test_error_code
                assert e.description == test_error_desc
                self.patched_library.niFake_SetAttributeViReal64_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(1000001), _matchers.ViReal64Matcher(-42.0))

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

    # Error descriptions

    def test_get_error_and_error_message_returns_error(self):
        test_error_code = -42
        self.patched_library.niFake_PoorlyNamedSimpleFunction_cfunc.side_effect = self.side_effects_helper.niFake_PoorlyNamedSimpleFunction
        self.side_effects_helper['PoorlyNamedSimpleFunction']['return'] = test_error_code
        self.patched_library.niFake_GetError_cfunc.side_effect = self.side_effects_helper.niFake_GetError
        self.side_effects_helper['GetError']['errorCode'] = -1
        self.side_effects_helper['GetError']['description'] = "Shouldn't get this"
        self.side_effects_helper['GetError']['return'] = -2
        self.patched_library.niFake_error_message_cfunc.side_effect = self.side_effects_helper.niFake_error_message
        self.side_effects_helper['error_message']['errorMessage'] = "Also shouldn't get this"
        self.side_effects_helper['error_message']['return'] = -3
        with nifake.Session('dev1') as session:
            try:
                session.simple_function()
            except nifake.Error as e:
                assert e.code == test_error_code
                assert e.description == 'Failed to retrieve error description.'

    def test_get_error_description_error_message_error(self):
        test_error_code = -42
        test_error_desc = "The answer to the ultimate question"
        self.patched_library.niFake_PoorlyNamedSimpleFunction_cfunc.side_effect = self.side_effects_helper.niFake_PoorlyNamedSimpleFunction
        self.side_effects_helper['PoorlyNamedSimpleFunction']['return'] = test_error_code
        self.patched_library.niFake_GetError_cfunc.side_effect = self.side_effects_helper.niFake_GetError
        self.side_effects_helper['GetError']['errorCode'] = -1
        self.side_effects_helper['GetError']['description'] = "Shouldn't get this"
        self.side_effects_helper['GetError']['return'] = -2
        self.patched_library.niFake_error_message_cfunc.side_effect = self.side_effects_helper.niFake_error_message
        self.side_effects_helper['error_message']['errorMessage'] = test_error_desc
        with nifake.Session('dev1') as session:
            try:
                session.simple_function()
            except nifake.Error as e:
                assert e.code == test_error_code
                assert e.description == test_error_desc
        self.patched_library.niFake_error_message_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(test_error_code), _matchers.ViCharBufferMatcher(256))

    # Custom types

    def test_set_custom_type(self):
        self.patched_library.niFake_SetCustomType_cfunc.side_effect = self.side_effects_helper.niFake_SetCustomType
        cs = nifake.CustomStruct(struct_int=42, struct_double=4.2)
        with nifake.Session('dev1') as session:
            session.set_custom_type(cs)
            self.patched_library.niFake_SetCustomType_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.CustomTypeMatcher(nifake.struct_CustomStruct, nifake.struct_CustomStruct(cs)))

    def test_get_custom_type(self):
        self.patched_library.niFake_GetCustomType_cfunc.side_effect = self.side_effects_helper.niFake_GetCustomType
        cs_ctype = nifake.struct_CustomStruct(struct_int=42, struct_double=4.2)
        self.side_effects_helper['GetCustomType']['cs'] = cs_ctype
        with nifake.Session('dev1') as session:
            cs = session.get_custom_type()
            assert cs.struct_int == cs_ctype.struct_int
            assert cs.struct_double == cs_ctype.struct_double

    def test_set_custom_type_array(self):
        self.patched_library.niFake_SetCustomTypeArray_cfunc.side_effect = self.side_effects_helper.niFake_SetCustomTypeArray
        cs = [nifake.CustomStruct(struct_int=42, struct_double=4.2), nifake.CustomStruct(struct_int=43, struct_double=4.3), nifake.CustomStruct(struct_int=42, struct_double=4.3)]
        cs_ctype = (nifake.struct_CustomStruct * len(cs))(*[nifake.struct_CustomStruct(c) for c in cs])
        with nifake.Session('dev1') as session:
            session.set_custom_type_array(cs)
            self.patched_library.niFake_SetCustomTypeArray_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(cs)), _matchers.CustomTypeBufferMatcher(nifake.struct_CustomStruct, cs_ctype))

    def test_get_custom_type_array(self):
        self.patched_library.niFake_GetCustomTypeArray_cfunc.side_effect = self.side_effects_helper.niFake_GetCustomTypeArray
        cs = [nifake.CustomStruct(struct_int=42, struct_double=4.2), nifake.CustomStruct(struct_int=43, struct_double=4.3), nifake.CustomStruct(struct_int=42, struct_double=4.3)]
        cs_ctype = (nifake.struct_CustomStruct * len(cs))(*[nifake.struct_CustomStruct(c) for c in cs])
        self.side_effects_helper['GetCustomTypeArray']['cs'] = cs_ctype
        with nifake.Session('dev1') as session:
            cs_test = session.get_custom_type_array(len(cs_ctype))
            assert len(cs_test) == len(cs_ctype)
            for actual, expected in zip(cs_test, cs):
                assert actual.struct_int == expected.struct_int
                assert actual.struct_double == expected.struct_double

    def test_get_custom_type_typedef(self):
        self.patched_library.niFake_GetCustomTypeTypedef_cfunc.side_effect = self.side_effects_helper.niFake_GetCustomTypeTypedef
        cst = nifake.CustomStructTypedef(struct_int=42, struct_double=4.2)
        cst_ctype = nifake.struct_CustomStructTypedef(cst)
        csnt = nifake.CustomStructNestedTypedef(
            struct_custom_struct=nifake.CustomStruct(struct_int=43, struct_double=4.3),
            struct_custom_struct_typedef=nifake.CustomStructTypedef(struct_int=44, struct_double=4.4)
        )
        csnt_ctype = nifake.struct_CustomStructNestedTypedef(csnt)
        self.side_effects_helper['GetCustomTypeTypedef']['cst'] = cst_ctype
        self.side_effects_helper['GetCustomTypeTypedef']['csnt'] = csnt_ctype
        with nifake.Session('dev1') as session:
            cst_test, csnt_test = session.get_custom_type_typedef()
            assert cst_test.struct_int == cst.struct_int
            assert cst_test.struct_double == cst.struct_double
            assert csnt_test.struct_custom_struct.struct_int == csnt.struct_custom_struct.struct_int
            assert csnt_test.struct_custom_struct.struct_double == csnt.struct_custom_struct.struct_double
            assert csnt_test.struct_custom_struct_typedef.struct_int == csnt.struct_custom_struct_typedef.struct_int
            assert csnt_test.struct_custom_struct_typedef.struct_double == csnt.struct_custom_struct_typedef.struct_double

    # python-code size mechanism

    def test_get_array_using_python_code_double(self):
        import nifake._visatype
        self.patched_library.niFake_GetArraySizeForPythonCode_cfunc.side_effect = self.side_effects_helper.niFake_GetArraySizeForPythonCode
        self.patched_library.niFake_GetArrayForPythonCodeDouble_cfunc.side_effect = self.side_effects_helper.niFake_GetArrayForPythonCodeDouble
        array_out = [42.0, 43.0, 44.0]
        array_out_ctype = (nifake._visatype.ViReal64 * len(array_out))(*array_out)
        self.side_effects_helper['GetArraySizeForPythonCode']['sizeOut'] = len(array_out)
        self.side_effects_helper['GetArrayForPythonCodeDouble']['arrayOut'] = array_out_ctype
        with nifake.Session('dev1') as session:
            array_out_test = session.get_array_for_python_code_double()
            assert len(array_out_test) == len(array_out)
            for actual, expected in zip(array_out_test, array_out):
                assert actual == expected

    def test_get_array_using_python_code_custom_type(self):
        import nifake._visatype
        self.patched_library.niFake_GetArraySizeForPythonCode_cfunc.side_effect = self.side_effects_helper.niFake_GetArraySizeForPythonCode
        self.patched_library.niFake_GetArrayForPythonCodeCustomType_cfunc.side_effect = self.side_effects_helper.niFake_GetArrayForPythonCodeCustomType
        cs = [nifake.CustomStruct(struct_int=42, struct_double=4.2), nifake.CustomStruct(struct_int=43, struct_double=4.3), nifake.CustomStruct(struct_int=42, struct_double=4.3)]
        cs_ctype = (nifake.struct_CustomStruct * len(cs))(*[nifake.struct_CustomStruct(c) for c in cs])
        self.side_effects_helper['GetArraySizeForPythonCode']['sizeOut'] = len(cs)
        self.side_effects_helper['GetArrayForPythonCodeCustomType']['arrayOut'] = cs_ctype
        with nifake.Session('dev1') as session:
            cs_test = session.get_array_for_python_code_custom_type()
            assert len(cs_test) == len(cs)
            for actual, expected in zip(cs_test, cs):
                assert actual.struct_int == expected.struct_int
                assert actual.struct_double == expected.struct_double

    def test_get_cal_date_time(self):
        self.patched_library.niFake_GetCalDateAndTime_cfunc.side_effect = self.side_effects_helper.niFake_GetCalDateAndTime
        month = 12
        day = 30
        year = 1988
        hour = 10
        minute = 15
        self.side_effects_helper['GetCalDateAndTime']['return'] = 0
        self.side_effects_helper['GetCalDateAndTime']['month'] = month
        self.side_effects_helper['GetCalDateAndTime']['day'] = day
        self.side_effects_helper['GetCalDateAndTime']['year'] = year
        self.side_effects_helper['GetCalDateAndTime']['hour'] = hour
        self.side_effects_helper['GetCalDateAndTime']['minute'] = minute
        with nifake.Session('dev1') as session:
            last_cal = session.get_cal_date_and_time(0)
            assert isinstance(last_cal, hightime.datetime)
            assert hightime.datetime(year, month, day, hour, minute) == last_cal

    def test_get_cal_interval(self):
        self.patched_library.niFake_GetCalInterval_cfunc = self.side_effects_helper.niFake_GetCalInterval
        self.side_effects_helper['GetCalInterval']['months'] = 24
        with nifake.Session('dev1') as session:
            last_cal = session.get_cal_interval()
            assert isinstance(last_cal, hightime.timedelta)
            assert 730 == last_cal.days

    # Import/Export functions

    def test_import_attribute_configuration_buffer_list_i8(self):
        self.patched_library.niFake_ImportAttributeConfigurationBuffer_cfunc.side_effect = self.side_effects_helper.niFake_ImportAttributeConfigurationBuffer
        expected_list = [ord('a'), ord('b'), ord('c'), ord('d')]
        configuration = expected_list
        with nifake.Session('dev1') as session:
            self.get_ctypes_pointer_for_buffer_side_effect_items = [expected_list]
            self.get_ctypes_pointer_for_buffer_side_effect_count = 0
            with patch('nifake._library_interpreter.get_ctypes_pointer_for_buffer', side_effect=self.get_ctypes_pointer_for_buffer_side_effect):
                session.import_attribute_configuration_buffer(configuration)
            self.patched_library.niFake_ImportAttributeConfigurationBuffer_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(configuration)), _matchers.ViInt8BufferMatcher(expected_list))

    def test_import_attribute_configuration_buffer_bytes(self):
        self.patched_library.niFake_ImportAttributeConfigurationBuffer_cfunc.side_effect = self.side_effects_helper.niFake_ImportAttributeConfigurationBuffer
        expected_list = [ord('a'), ord('b'), ord('c'), ord('d')]
        configuration = b'abcd'
        with nifake.Session('dev1') as session:
            self.get_ctypes_pointer_for_buffer_side_effect_items = [expected_list]
            self.get_ctypes_pointer_for_buffer_side_effect_count = 0
            with patch('nifake._library_interpreter.get_ctypes_pointer_for_buffer', side_effect=self.get_ctypes_pointer_for_buffer_side_effect):
                session.import_attribute_configuration_buffer(configuration)
            self.patched_library.niFake_ImportAttributeConfigurationBuffer_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(configuration)), _matchers.ViInt8BufferMatcher(expected_list))

    def test_import_attribute_configuration_buffer_bytearray(self):
        self.patched_library.niFake_ImportAttributeConfigurationBuffer_cfunc.side_effect = self.side_effects_helper.niFake_ImportAttributeConfigurationBuffer
        expected_list = [ord('a'), ord('b'), ord('c'), ord('d')]
        configuration = bytearray(b'abcd')
        with nifake.Session('dev1') as session:
            self.get_ctypes_pointer_for_buffer_side_effect_items = [expected_list]
            self.get_ctypes_pointer_for_buffer_side_effect_count = 0
            with patch('nifake._library_interpreter.get_ctypes_pointer_for_buffer', side_effect=self.get_ctypes_pointer_for_buffer_side_effect):
                session.import_attribute_configuration_buffer(configuration)
            self.patched_library.niFake_ImportAttributeConfigurationBuffer_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(configuration)), _matchers.ViInt8BufferMatcher(expected_list))

    def test_import_attribute_configuration_buffer_array_bytes(self):
        self.patched_library.niFake_ImportAttributeConfigurationBuffer_cfunc.side_effect = self.side_effects_helper.niFake_ImportAttributeConfigurationBuffer
        expected_list = [ord('a'), ord('b'), ord('c'), ord('d')]
        configuration = array.array('b', b'abcd')
        with nifake.Session('dev1') as session:
            self.get_ctypes_pointer_for_buffer_side_effect_items = [expected_list]
            self.get_ctypes_pointer_for_buffer_side_effect_count = 0
            with patch('nifake._library_interpreter.get_ctypes_pointer_for_buffer', side_effect=self.get_ctypes_pointer_for_buffer_side_effect):
                session.import_attribute_configuration_buffer(configuration)
            self.patched_library.niFake_ImportAttributeConfigurationBuffer_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(configuration)), _matchers.ViInt8BufferMatcher(expected_list))

    def test_import_attribute_configuration_buffer_str(self):
        self.patched_library.niFake_ImportAttributeConfigurationBuffer_cfunc.side_effect = self.side_effects_helper.niFake_ImportAttributeConfigurationBuffer
        expected_list = [ord('a'), ord('b'), ord('c'), ord('d')]
        configuration = 'abcd'
        with nifake.Session('dev1') as session:
            self.get_ctypes_pointer_for_buffer_side_effect_items = [expected_list]
            self.get_ctypes_pointer_for_buffer_side_effect_count = 0
            with patch('nifake._library_interpreter.get_ctypes_pointer_for_buffer', side_effect=self.get_ctypes_pointer_for_buffer_side_effect):
                session.import_attribute_configuration_buffer(configuration)
            self.patched_library.niFake_ImportAttributeConfigurationBuffer_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(configuration)), _matchers.ViInt8BufferMatcher(expected_list))

    # Invalid types
    def test_import_attribute_configuration_buffer_list_i8_big(self):
        self.patched_library.niFake_ImportAttributeConfigurationBuffer_cfunc.side_effect = self.side_effects_helper.niFake_ImportAttributeConfigurationBuffer
        expected_list = [ord('a') * 100, ord('b') * 100, ord('c') * 100, ord('d') * 100]
        configuration = expected_list
        with nifake.Session('dev1') as session:
            self.get_ctypes_pointer_for_buffer_side_effect_items = [expected_list]
            self.get_ctypes_pointer_for_buffer_side_effect_count = 0
            with patch('nifake._library_interpreter.get_ctypes_pointer_for_buffer', side_effect=self.get_ctypes_pointer_for_buffer_side_effect):
                try:
                    session.import_attribute_configuration_buffer(configuration)
                    assert False
                except ValueError:
                    pass

    def test_import_attribute_configuration_buffer_list_i8_float(self):
        self.patched_library.niFake_ImportAttributeConfigurationBuffer_cfunc.side_effect = self.side_effects_helper.niFake_ImportAttributeConfigurationBuffer
        expected_list = [ord('a') * 1.0, ord('b') * 1.0, ord('c') * 1.0, ord('d') * 1.0]
        configuration = expected_list
        with nifake.Session('dev1') as session:
            self.get_ctypes_pointer_for_buffer_side_effect_items = [expected_list]
            self.get_ctypes_pointer_for_buffer_side_effect_count = 0
            with patch('nifake._library_interpreter.get_ctypes_pointer_for_buffer', side_effect=self.get_ctypes_pointer_for_buffer_side_effect):
                try:
                    session.import_attribute_configuration_buffer(configuration)
                    assert False
                except TypeError:
                    pass

    def test_import_attribute_configuration_buffer_list_i8_big_float(self):
        self.patched_library.niFake_ImportAttributeConfigurationBuffer_cfunc.side_effect = self.side_effects_helper.niFake_ImportAttributeConfigurationBuffer
        expected_list = [ord('a') * 100.0, ord('b') * 100.0, ord('c') * 100.0, ord('d') * 100.0]
        configuration = expected_list
        with nifake.Session('dev1') as session:
            self.get_ctypes_pointer_for_buffer_side_effect_items = [expected_list]
            self.get_ctypes_pointer_for_buffer_side_effect_count = 0
            with patch('nifake._library_interpreter.get_ctypes_pointer_for_buffer', side_effect=self.get_ctypes_pointer_for_buffer_side_effect):
                try:
                    session.import_attribute_configuration_buffer(configuration)
                    assert False
                except TypeError:
                    pass

    def test_export_attribute_configuration_buffer(self):
        self.patched_library.niFake_ExportAttributeConfigurationBuffer_cfunc.side_effect = self.side_effects_helper.niFake_ExportAttributeConfigurationBuffer
        expected_buffer_list = [ord('a'), ord('b'), ord('c'), ord('d'), ]

        # Because we are mocking get_ctypes_pointer_for_buffer() we don't end up using the array allocated in the function call. Instead, we will allocate the arrays here
        # and have the mock return them. These are the ones that are actually filled in by the function.
        expected_buffer = array.array('b', [0] * len(expected_buffer_list))
        expected_buffer_ctypes = ctypes.cast(expected_buffer.buffer_info()[0], ctypes.POINTER(nifake._visatype.ViInt8 * len(expected_buffer_list)))

        self.side_effects_helper['ExportAttributeConfigurationBuffer']['configuration'] = expected_buffer_list
        with nifake.Session('dev1') as session:
            self.get_ctypes_pointer_for_buffer_side_effect_items = [expected_buffer_ctypes]
            self.get_ctypes_pointer_for_buffer_side_effect_count = 0
            with patch('nifake._library_interpreter.get_ctypes_pointer_for_buffer', side_effect=self.get_ctypes_pointer_for_buffer_side_effect):
                actual_configuration = session.export_attribute_configuration_buffer()
            assert type(actual_configuration) is bytes
            assert len(actual_configuration) == len(expected_buffer_list)
            # Since we mocked get_ctypes_pointer_for_buffer, we didn't actually fill in actual_configuration. Instead we look for the expected values to
            # be in the expected buffer that we returned from the mock
            for i in range(len(expected_buffer)):
                assert expected_buffer[i] == expected_buffer_list[i]

    def test_matcher_prints(self):
        assert _matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST).__repr__() == "ViSessionMatcher(" + str(nifake._visatype.ViSession) + ", 42)"
        assert _matchers.ViAttrMatcher(SESSION_NUM_FOR_TEST).__repr__() == "ViAttrMatcher(" + str(nifake._visatype.ViAttr) + ", 42)"
        assert _matchers.ViInt32Matcher(4).__repr__() == "ViInt32Matcher(" + str(nifake._visatype.ViInt32) + ", 4)"
        assert _matchers.ViStringMatcher('0-24').__repr__() == "ViStringMatcher('0-24')"
        assert _matchers.ViReal64Matcher(-42.0).__repr__() == "ViReal64Matcher(" + str(nifake._visatype.ViReal64) + ", -42.0)"
        assert _matchers.ViReal64PointerMatcher().__repr__() == "ViReal64PointerMatcher(" + str(nifake._visatype.ViReal64) + ")"
        assert _matchers.ViInt32PointerMatcher().__repr__() == "ViInt32PointerMatcher(" + str(nifake._visatype.ViInt32) + ")"
        cs = [nifake.CustomStruct(struct_int=42, struct_double=4.2), nifake.CustomStruct(struct_int=43, struct_double=4.3), nifake.CustomStruct(struct_int=42, struct_double=4.3)]
        cs_ctype = (nifake.struct_CustomStruct * len(cs))(*[nifake.struct_CustomStruct(c) for c in cs])
        assert _matchers.CustomTypeMatcher(nifake.struct_CustomStruct, nifake.struct_CustomStruct(cs[0])).__repr__() == "CustomTypeMatcher(<class 'nifake.custom_struct.struct_CustomStruct'>, struct_CustomStruct(data=None, struct_int=42, struct_double=4.2))"
        assert _matchers.CustomTypeBufferMatcher(nifake.struct_CustomStruct, cs_ctype).__repr__() == "CustomTypeBufferMatcher(<class 'nifake.custom_struct.struct_CustomStruct'>, [struct_CustomStruct(data=None, struct_int=42, struct_double=4.2), struct_CustomStruct(data=None, struct_int=43, struct_double=4.3), struct_CustomStruct(data=None, struct_int=42, struct_double=4.3)])"

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
        self.patched_library.niFake_DoubleAllTheNums_cfunc.side_effect = self.side_effects_helper.niFake_DoubleAllTheNums
        nums = [1, 2, 3, 4.2]
        nums_x2 = [x * 2 for x in nums]
        with nifake.Session('dev1') as session:
            session.double_all_the_nums(nums)
            self.patched_library.niFake_DoubleAllTheNums_cfunc.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(nums)), _matchers.ViReal64BufferMatcher(nums_x2))

    def test_nitclk_integration(self):
        with nifake.Session('dev1') as session:
            assert str(type(session.tclk)) == "<class 'nitclk.session.SessionReference'>"

    def test_accept_list_of_time_values_as_floats(self):
        self.patched_library.niFake_AcceptListOfDurationsInSeconds_cfunc.side_effect = self.side_effects_helper.niFake_AcceptListOfDurationsInSeconds
        delays = [-1.5, 2.0]
        with nifake.Session('dev1') as session:
            session.accept_list_of_durations_in_seconds(delays)
            self.patched_library.niFake_AcceptListOfDurationsInSeconds_cfunc.assert_called_once_with(
                _matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST),
                _matchers.ViInt32Matcher(len(delays)),
                _matchers.ViReal64BufferMatcher(delays)
            )

    def test_accept_array_of_time_values_as_floats(self):
        self.patched_library.niFake_AcceptListOfDurationsInSeconds_cfunc.side_effect = self.side_effects_helper.niFake_AcceptListOfDurationsInSeconds
        time_values = [-1.5, 2.0]
        delays = array.array('d', time_values)
        with nifake.Session('dev1') as session:
            session.accept_list_of_durations_in_seconds(delays)
            self.patched_library.niFake_AcceptListOfDurationsInSeconds_cfunc.assert_called_once_with(
                _matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST),
                _matchers.ViInt32Matcher(len(delays)),
                _matchers.ViReal64BufferMatcher(time_values)
            )

    def test_accept_list_of_time_values_as_timedelta_instances(self):
        self.patched_library.niFake_AcceptListOfDurationsInSeconds_cfunc.side_effect = self.side_effects_helper.niFake_AcceptListOfDurationsInSeconds
        time_values = [-1.5, 2e-9]
        delays = [datetime.timedelta(seconds=-1.5), hightime.timedelta(nanoseconds=2)]
        with nifake.Session('dev1') as session:
            session.accept_list_of_durations_in_seconds(delays)
            self.patched_library.niFake_AcceptListOfDurationsInSeconds_cfunc.assert_called_once_with(
                _matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST),
                _matchers.ViInt32Matcher(len(delays)),
                _matchers.ViReal64BufferMatcher(time_values)
            )

    def test_return_timedelta(self):
        self.patched_library.niFake_ReturnDurationInSeconds_cfunc.side_effect = self.side_effects_helper.niFake_ReturnDurationInSeconds
        time_value = -1.5
        expected_timedelta = hightime.timedelta(seconds=time_value)
        self.side_effects_helper['ReturnDurationInSeconds']['timedelta'] = time_value
        with nifake.Session('dev1') as session:
            returned_timedelta = session.return_duration_in_seconds()
            assert returned_timedelta == expected_timedelta
            self.patched_library.niFake_ReturnDurationInSeconds_cfunc.assert_called_once_with(
                _matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST),
                _matchers.ViReal64PointerMatcher()
            )

    def test_return_timedeltas(self):
        self.patched_library.niFake_ReturnListOfDurationsInSeconds_cfunc.side_effect = self.side_effects_helper.niFake_ReturnListOfDurationsInSeconds
        time_values = [-1.5, 2.0]
        time_values_ctype = (nifake._visatype.ViReal64 * len(time_values))(*time_values)
        expected_timedeltas = [hightime.timedelta(seconds=i) for i in time_values]
        self.side_effects_helper['ReturnListOfDurationsInSeconds']['timedeltas'] = time_values_ctype
        with nifake.Session('dev1') as session:
            returned_timedeltas = session.return_list_of_durations_in_seconds(len(expected_timedeltas))
            assert len(returned_timedeltas) == len(expected_timedeltas)
            assert returned_timedeltas == expected_timedeltas
            self.patched_library.niFake_ReturnListOfDurationsInSeconds_cfunc.assert_called_once_with(
                _matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST),
                _matchers.ViInt32Matcher(len(time_values)),
                _matchers.ViReal64BufferMatcher(len(time_values))
            )


# not session tests per se
def test_diagnostic_information():
    info = nifake.print_diagnostic_information()
    assert isinstance(info, dict)


def test_dunder_version():
    print('Version = {}'.format(nifake.__version__))
    assert type(nifake.__version__) is str


def test_library_error():
    if platform.architecture()[0] == '64bit':
        ctypes_class_name = 'ctypes.CDLL'
    else:
        ctypes_class_name = 'ctypes.WinDLL'
    with patch(ctypes_class_name) as mock_ctypes:
        mock_ctypes_instance = mock_ctypes.return_value
        # Ensure these methods return 0 because they are called in session creation
        mock_ctypes_instance.niFake_InitWithOptions.return_value = 0
        mock_ctypes_instance.niFake_LockSession.return_value = 0
        mock_ctypes_instance.niFake_UnlockSession.return_value = 0
        # Delete function to simulate missing function from driver runtime
        delattr(mock_ctypes_instance, 'niFake_Abort')

        session = nifake.Session('dev1')

        try:
            session.abort()
            assert False
        except nifake.errors.DriverTooOldError as e:
            message = e.args[0]
            assert message == 'A function was not found in the NI-FAKE runtime. Please visit http://www.ni.com/downloads/drivers/ to download a newer version and install it.'
