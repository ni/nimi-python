import array
import ctypes
import datetime
import math
import nifake
import nifake.errors
import numpy
import six
import warnings

from mock import patch

import _matchers
import _mock_helper

# from mock import ANY
# Tests


SESSION_NUM_FOR_TEST = 42


class TestSession(object):

    def setup_method(self, method):
        self.patched_library_patcher = patch('nifake._library.Library', autospec=True)
        self.patched_library = self.patched_library_patcher.start()
        self.patched_library_singleton_get = patch('nifake.session._library_singleton.get', return_value=self.patched_library)
        self.patched_library_singleton_get.start()

        self.side_effects_helper = _mock_helper.SideEffectsHelper()
        self.side_effects_helper.set_side_effects_and_return_values(self.patched_library)
        self.patched_library.niFake_InitWithOptions.side_effect = self.side_effects_helper.niFake_InitWithOptions
        self.disallow_close = self.patched_library.niFake_close.side_effect
        self.patched_library.niFake_close.side_effect = self.side_effects_helper.niFake_close

        self.side_effects_helper['InitWithOptions']['vi'] = SESSION_NUM_FOR_TEST

        self.get_ctypes_pointer_for_buffer_side_effect_count = 0
        self.get_ctypes_pointer_for_buffer_side_effect_items = []

        # Mock lock/unlock
        self.LockSession_side_effect_cache = self.patched_library.niFake_LockSession.side_effect
        self.patched_library.niFake_LockSession.side_effect = self.side_effects_helper.niFake_LockSession
        self.side_effects_helper['LockSession']['callerHasLock'] = True
        self.UnlockSession_side_effect_cache = self.patched_library.niFake_UnlockSession.side_effect
        self.patched_library.niFake_UnlockSession.side_effect = self.side_effects_helper.niFake_UnlockSession
        self.side_effects_helper['UnlockSession']['callerHasLock'] = False

    def teardown_method(self, method):
        self.patched_library_singleton_get.stop()
        self.patched_library_patcher.stop()

    def niFake_read_warning(self, vi, maximum_time, reading):  # noqa: N802
        reading.contents.value = self.reading
        return self.error_code_return

    def get_ctypes_pointer_for_buffer_side_effect(self, value, library_type=None):
        ret_val = self.get_ctypes_pointer_for_buffer_side_effect_items[self.get_ctypes_pointer_for_buffer_side_effect_count]
        self.get_ctypes_pointer_for_buffer_side_effect_count += 1
        return ret_val

    # Session management

    def test_init_with_options_and_close(self):
        errors_patcher = patch('nifake.session.errors', spec_set=['handle_error', '_is_error'])
        patched_errors = errors_patcher.start()
        patched_errors._is_error.return_value = 0

        session = nifake.Session('dev1')
        self.patched_library.niFake_InitWithOptions.assert_called_once_with(_matchers.ViStringMatcher('dev1'), _matchers.ViBooleanMatcher(False), _matchers.ViBooleanMatcher(False), _matchers.ViStringMatcher(''), _matchers.ViSessionPointerMatcher())
        patched_errors.handle_error.assert_called_once_with(session, self.patched_library.niFake_InitWithOptions.return_value, ignore_warnings=False, is_error_handling=False)
        session.close()
        self.patched_library.niFake_close.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST))

        errors_patcher.stop()

    def test_init_with_options_nondefault_and_close(self):
        session = nifake.Session('FakeDevice', 'Some string', True, True)
        self.patched_library.niFake_InitWithOptions.assert_called_once_with(_matchers.ViStringMatcher('FakeDevice'), _matchers.ViBooleanMatcher(True), _matchers.ViBooleanMatcher(True), _matchers.ViStringMatcher('Some string'), _matchers.ViSessionPointerMatcher())
        session.close()
        self.patched_library.niFake_close.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST))

    def test_close(self):
        session = nifake.Session('dev1')
        session.close()
        self.patched_library.niFake_close.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST))

    def test_session_context_manager(self):
        with nifake.Session('dev1') as session:
            assert type(session) == nifake.Session
            self.patched_library.niFake_InitWithOptions.assert_called_once_with(_matchers.ViStringMatcher('dev1'), _matchers.ViBooleanMatcher(False), _matchers.ViBooleanMatcher(False), _matchers.ViStringMatcher(''), _matchers.ViSessionPointerMatcher())
        self.patched_library.niFake_close.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST))

    def test_init_with_error(self):
        test_error_code = -1
        test_error_desc = 'Test'
        self.patched_library.niFake_InitWithOptions.side_effect = self.side_effects_helper.niFake_InitWithOptions
        self.side_effects_helper['InitWithOptions']['return'] = test_error_code
        self.side_effects_helper['InitWithOptions']['vi'] = SESSION_NUM_FOR_TEST
        self.patched_library.niFake_GetError.side_effect = self.side_effects_helper.niFake_GetError
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
        self.patched_library.niFake_close.side_effect = self.side_effects_helper.niFake_close
        session = nifake.Session('dev1')
        self.side_effects_helper['close']['return'] = test_error_code
        self.patched_library.niFake_GetError.side_effect = self.side_effects_helper.niFake_GetError
        self.side_effects_helper['GetError']['errorCode'] = test_error_code
        self.side_effects_helper['GetError']['description'] = test_error_desc
        try:
            session.close()
            assert False
        except nifake.Error as e:
            assert e.code == test_error_code
            assert e.description == test_error_desc
            assert session._vi == 0
        self.patched_library.niFake_close.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST))

    def test_session_context_manager_init_with_error(self):
        test_error_code = -1
        test_error_desc = 'Test'
        self.patched_library.niFake_InitWithOptions.side_effect = self.side_effects_helper.niFake_InitWithOptions
        self.side_effects_helper['InitWithOptions']['return'] = test_error_code
        self.side_effects_helper['InitWithOptions']['vi'] = SESSION_NUM_FOR_TEST
        self.patched_library.niFake_GetError.side_effect = self.side_effects_helper.niFake_GetError
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
        self.patched_library.niFake_close.side_effect = self.side_effects_helper.niFake_close
        self.side_effects_helper['close']['return'] = test_error_code
        self.patched_library.niFake_GetError.side_effect = self.side_effects_helper.niFake_GetError
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
            self.patched_library.niFake_LockSession.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), None)

    def test_unlock_session_none(self):
        with nifake.Session('dev1') as session:
            session.unlock()
            self.patched_library.niFake_UnlockSession.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), None)

    def test_lock_context_manager(self):
        with nifake.Session('dev1') as session:
            with session.lock():
                pass
            self.patched_library.niFake_LockSession.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), None)
            self.patched_library.niFake_UnlockSession.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), None)

    def test_lock_context_manager_abnormal_exit(self):
        with nifake.Session('dev1') as session:
            try:
                with session.lock():
                    raise nifake.Error('Fake exception')
            except nifake.Error:
                pass
            self.patched_library.niFake_LockSession.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), None)
            self.patched_library.niFake_UnlockSession.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), None)

    # Methods
    def test_simple_function(self):
        self.patched_library.niFake_PoorlyNamedSimpleFunction.side_effect = self.side_effects_helper.niFake_PoorlyNamedSimpleFunction
        with nifake.Session('dev1') as session:
            session.simple_function()
            self.patched_library.niFake_PoorlyNamedSimpleFunction.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST))

    def test_self_test(self):
        self.patched_library.niFake_self_test.side_effect = self.side_effects_helper.niFake_self_test
        test_error_code = 0
        self.side_effects_helper['self_test']['selfTestResult'] = test_error_code
        self.side_effects_helper['self_test']['selfTestMessage'] = ''
        with nifake.Session('dev1') as session:
            session.self_test()

    def test_self_test_fail(self):
        self.patched_library.niFake_self_test.side_effect = self.side_effects_helper.niFake_self_test
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
        self.patched_library.niFake_GetANumber.side_effect = self.side_effects_helper.niFake_GetANumber
        self.side_effects_helper['GetANumber']['aNumber'] = test_number
        with nifake.Session('dev1') as session:
            test_result = session.get_a_number()
            assert isinstance(test_result, int)
            assert test_result == test_number
            self.patched_library.niFake_GetANumber.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt16PointerMatcher())

    def test_one_input_function(self):
        test_number = 1
        self.patched_library.niFake_OneInputFunction.side_effect = self.side_effects_helper.niFake_OneInputFunction
        with nifake.Session('dev1') as session:
            session.one_input_function(test_number)
            self.patched_library.niFake_OneInputFunction.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(test_number))

    def test_vi_int_64_function(self):
        input_value = 1099511627776  # 2^40
        output_value = 2199023255552  # 2^41
        self.patched_library.niFake_Use64BitNumber.side_effect = self.side_effects_helper.niFake_Use64BitNumber
        self.side_effects_helper['Use64BitNumber']['output'] = output_value
        with nifake.Session('dev1') as session:
            assert session.use64_bit_number(input_value) == output_value
            self.patched_library.niFake_Use64BitNumber.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt64Matcher(input_value), _matchers.ViInt64PointerMatcher())

    def test_two_input_function(self):
        test_number = 1.5
        test_string = 'test'
        self.patched_library.niFake_TwoInputFunction.side_effect = self.side_effects_helper.niFake_TwoInputFunction
        with nifake.Session('dev1') as session:
            session.two_input_function(test_number, test_string)
            self.patched_library.niFake_TwoInputFunction.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViReal64Matcher(test_number), _matchers.ViStringMatcher(test_string))

    def test_get_enum_value(self):
        test_number = 1
        test_turtle = nifake.Turtle.LEONARDO
        self.patched_library.niFake_GetEnumValue.side_effect = self.side_effects_helper.niFake_GetEnumValue
        self.side_effects_helper['GetEnumValue']['aQuantity'] = test_number
        self.side_effects_helper['GetEnumValue']['aTurtle'] = 0
        with nifake.Session('dev1') as session:
            test_result_number, test_result_enum = session.get_enum_value()
            assert isinstance(test_result_number, int)
            assert test_result_number == test_number
            assert isinstance(test_result_enum, nifake.Turtle)
            assert test_result_enum == test_turtle
            self.patched_library.niFake_GetEnumValue.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32PointerMatcher(), _matchers.ViInt16PointerMatcher())

    def test_get_a_list_enums(self):
        self.patched_library.niFake_EnumArrayOutputFunction.side_effect = self.side_effects_helper.niFake_EnumArrayOutputFunction
        test_list = [1, 1, 0]
        self.side_effects_helper['EnumArrayOutputFunction']['anArray'] = test_list
        with nifake.Session('dev1') as session:
            test_result = session.enum_array_output_function(len(test_list))
            assert len(test_list) == len(test_result)
            for expected_value, actual_value in zip(test_list, test_result):
                assert isinstance(actual_value, nifake.Turtle)
                assert actual_value.value == expected_value
            self.patched_library.niFake_EnumArrayOutputFunction.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(test_list)), _matchers.ViInt16BufferMatcher(len(test_list)))

    def test_get_a_boolean(self):
        self.patched_library.niFake_GetABoolean.side_effect = self.side_effects_helper.niFake_GetABoolean
        self.side_effects_helper['GetABoolean']['aBoolean'] = 1
        with nifake.Session('dev1') as session:
            test_result = session.get_a_boolean()
            assert isinstance(test_result, bool)
            assert test_result
            self.patched_library.niFake_GetABoolean.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViBooleanPointerMatcher())

    def test_get_a_list_booleans(self):
        self.patched_library.niFake_BoolArrayOutputFunction.side_effect = self.side_effects_helper.niFake_BoolArrayOutputFunction
        test_list = [1, 1, 0]
        self.side_effects_helper['BoolArrayOutputFunction']['anArray'] = test_list
        with nifake.Session('dev1') as session:
            test_result = session.bool_array_output_function(len(test_list))
            assert len(test_list) == len(test_result)
            for expected_value, actual_value in zip(test_list, test_result):
                assert isinstance(actual_value, bool)
                assert actual_value == bool(expected_value)
            self.patched_library.niFake_BoolArrayOutputFunction.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(test_list)), _matchers.ViBooleanBufferMatcher(len(test_list)))

    def test_acquisition_context_manager(self):
        self.patched_library.niFake_Initiate.side_effect = self.side_effects_helper.niFake_Initiate
        self.patched_library.niFake_Abort.side_effect = self.side_effects_helper.niFake_Abort
        with nifake.Session('dev1') as session:
            with session.initiate():
                self.patched_library.niFake_Initiate.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST))
            self.patched_library.niFake_Abort.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST))
        self.patched_library.niFake_close.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST))

    def test_acquisition_no_context_manager(self):
        self.patched_library.niFake_Initiate.side_effect = self.side_effects_helper.niFake_Initiate
        self.patched_library.niFake_Abort.side_effect = self.side_effects_helper.niFake_Abort
        with nifake.Session('dev1') as session:
            session.initiate()
            self.patched_library.niFake_Initiate.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST))
            session.abort()
            self.patched_library.niFake_Abort.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST))
        self.patched_library.niFake_close.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST))

    def test_single_point_read_timedelta(self):
        test_maximum_time_ms = 100  # milliseconds
        test_maximum_time_s = .1    # seconds
        test_maximum_time_timedelta = datetime.timedelta(milliseconds=test_maximum_time_ms)
        test_reading = 5
        self.patched_library.niFake_Read.side_effect = self.side_effects_helper.niFake_Read
        self.side_effects_helper['Read']['reading'] = test_reading
        with nifake.Session('dev1') as session:
            assert test_reading == session.read(test_maximum_time_timedelta)
            self.patched_library.niFake_Read.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViReal64Matcher(test_maximum_time_s), _matchers.ViReal64PointerMatcher())

    def test_single_point_read_nan(self):
        test_maximum_time_s = 10.0
        test_maximum_time = datetime.timedelta(seconds=test_maximum_time_s)
        test_reading = float('NaN')
        self.patched_library.niFake_Read.side_effect = self.side_effects_helper.niFake_Read
        self.side_effects_helper['Read']['reading'] = test_reading
        with nifake.Session('dev1') as session:
            assert math.isnan(session.read(test_maximum_time))

    def test_enum_input_function_with_defaults(self):
        test_turtle = nifake.Turtle.DONATELLO
        self.patched_library.niFake_EnumInputFunctionWithDefaults.side_effect = self.side_effects_helper.niFake_EnumInputFunctionWithDefaults
        with nifake.Session('dev1') as session:
            session.enum_input_function_with_defaults()
            session.enum_input_function_with_defaults(test_turtle)
            from mock import call
            calls = [call(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt16Matcher(0)), call(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt16Matcher(1))]  # 0 is the value of the default of nifake.Turtle.LEONARDO, 1 is the value of nifake.Turtle.DONATELLO
            self.patched_library.niFake_EnumInputFunctionWithDefaults.assert_has_calls(calls)

    def test_fetch_waveform(self):
        expected_waveform_list = [1.0, 0.1, 42, .42]
        self.patched_library.niFake_FetchWaveform.side_effect = self.side_effects_helper.niFake_FetchWaveform
        self.side_effects_helper['FetchWaveform']['waveformData'] = expected_waveform_list
        self.side_effects_helper['FetchWaveform']['actualNumberOfSamples'] = len(expected_waveform_list)

        # Because we are mocking get_ctypes_pointer_for_buffer() we don't end up using the array allocated in the function call. Instead, we will allocate the arrays here
        # and have the mock return them. These are the ones that are actually filled in by the function.
        expected_waveform = array.array('d', [0] * len(expected_waveform_list))
        expected_waveform_ctypes = ctypes.cast(expected_waveform.buffer_info()[0], ctypes.POINTER(nifake._visatype.ViReal64 * len(expected_waveform_list)))

        with nifake.Session('dev1') as session:
            self.get_ctypes_pointer_for_buffer_side_effect_items = [expected_waveform_ctypes]
            self.get_ctypes_pointer_for_buffer_side_effect_count = 0
            self.patched_library.niFake_WriteWaveform.side_effect = self.side_effects_helper.niFake_WriteWaveform
            with patch('nifake.session.get_ctypes_pointer_for_buffer', side_effect=self.get_ctypes_pointer_for_buffer_side_effect):
                # Because we have mocked away get_ctypes_pointer_for_buffer(), we ignore the return values here and look at our already allocated arrays to make
                # sure they are filled in correctly
                session.fetch_waveform(len(expected_waveform_list))
            assert isinstance(expected_waveform[0], float)
            assert len(expected_waveform) == len(expected_waveform_list)
            for i in range(len(expected_waveform)):
                assert expected_waveform[i] == expected_waveform_list[i]
        self.patched_library.niFake_FetchWaveform.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(expected_waveform)), _matchers.ViReal64BufferMatcher(expected_waveform), _matchers.ViInt32PointerMatcher())

    def test_fetch_waveform_into(self):
        expected_waveform = [1.0, 0.1, 42, .42]
        self.patched_library.niFake_FetchWaveform.side_effect = self.side_effects_helper.niFake_FetchWaveform
        self.side_effects_helper['FetchWaveform']['waveformData'] = expected_waveform
        self.side_effects_helper['FetchWaveform']['actualNumberOfSamples'] = len(expected_waveform)
        with nifake.Session('dev1') as session:
            waveform = numpy.empty(len(expected_waveform), numpy.float64)
            session.fetch_waveform_into(waveform)
            assert numpy.array_equal(waveform, expected_waveform)
            self.patched_library.niFake_FetchWaveform.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(expected_waveform)), _matchers.ViReal64BufferMatcher(expected_waveform), _matchers.ViInt32PointerMatcher())

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
            self.patched_library.niFake_WriteWaveform.side_effect = self.side_effects_helper.niFake_WriteWaveform
            with patch('nifake.session.get_ctypes_pointer_for_buffer', side_effect=self.get_ctypes_pointer_for_buffer_side_effect):
                session.write_waveform(expected_array)
            self.patched_library.niFake_WriteWaveform.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(expected_waveform)), _matchers.ViReal64BufferMatcher(expected_array))

    def test_write_waveform_numpy(self):
        expected_waveform = numpy.array([1.1, 2.2, 3.3, 4.4], order='C')
        self.patched_library.niFake_WriteWaveform.side_effect = self.side_effects_helper.niFake_WriteWaveform
        with nifake.Session('dev1') as session:
            session.write_waveform_numpy(expected_waveform)
            self.patched_library.niFake_WriteWaveform.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(expected_waveform)), _matchers.ViReal64BufferMatcher(expected_waveform))

    def test_return_multiple_types(self):
        self.patched_library.niFake_ReturnMultipleTypes.side_effect = self.side_effects_helper.niFake_ReturnMultipleTypes
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
            assert isinstance(result_int64, six.integer_types)
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
            assert isinstance(result_string, six.text_type)
            assert self.patched_library.niFake_ReturnMultipleTypes.call_count == 2

    def test_multiple_array_types(self):
        self.patched_library.niFake_MultipleArrayTypes.side_effect = self.side_effects_helper.niFake_MultipleArrayTypes
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
            self.patched_library.niFake_MultipleArrayTypes.assert_called_once_with(
                _matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST),
                _matchers.ViInt32Matcher(output_array_size),
                _matchers.ViReal64BufferMatcher(output_array_size),
                _matchers.ViReal64BufferMatcher(len(expected_output_array_of_fixed_length)),
                _matchers.ViInt32Matcher(len(input_array_of_integers)),
                _matchers.ViReal64BufferMatcher(input_array_of_floats),
                _matchers.ViInt16BufferMatcher(input_array_of_integers),
            )

    def test_multiple_array_types_none_input(self):
        self.patched_library.niFake_MultipleArrayTypes.side_effect = self.side_effects_helper.niFake_MultipleArrayTypes
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
            self.patched_library.niFake_MultipleArrayTypes.assert_called_once_with(
                _matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST),
                _matchers.ViInt32Matcher(output_array_size),
                _matchers.ViReal64BufferMatcher(output_array_size),
                _matchers.ViReal64BufferMatcher(len(expected_output_array_of_fixed_length)),
                _matchers.ViInt32Matcher(len(input_array_of_floats)),
                _matchers.ViReal64BufferMatcher(input_array_of_floats),
                None
            )

    def test_multiple_arrays_same_size(self):
        self.patched_library.niFake_MultipleArraysSameSize.side_effect = self.side_effects_helper.niFake_MultipleArraysSameSize
        input_array_of_floats1 = [0.041, 0.042, 0.043, 0.044]
        input_array_of_floats2 = [0.410, 0.420, 0.430, 0.440]
        input_array_of_floats3 = [4.100, 4.200, 4.300, 4.400]
        input_array_of_floats4 = [41.00, 42.00, 43.00, 44.00]
        with nifake.Session('dev1') as session:
            session.multiple_arrays_same_size(input_array_of_floats1, input_array_of_floats2, input_array_of_floats3, input_array_of_floats4)
            self.patched_library.niFake_MultipleArraysSameSize.assert_called_once_with(
                _matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST),
                _matchers.ViReal64BufferMatcher(input_array_of_floats1),
                _matchers.ViReal64BufferMatcher(input_array_of_floats2),
                _matchers.ViReal64BufferMatcher(input_array_of_floats3),
                _matchers.ViReal64BufferMatcher(input_array_of_floats4),
                _matchers.ViInt32Matcher(len(input_array_of_floats1)),
            )

    def test_multiple_arrays_same_size_none_input(self):
        self.patched_library.niFake_MultipleArraysSameSize.side_effect = self.side_effects_helper.niFake_MultipleArraysSameSize
        input_array_of_floats1 = [0.041, 0.042, 0.043, 0.044]
        with nifake.Session('dev1') as session:
            session.multiple_arrays_same_size(input_array_of_floats1, None, None, None)
            self.patched_library.niFake_MultipleArraysSameSize.assert_called_once_with(
                _matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST),
                _matchers.ViReal64BufferMatcher(input_array_of_floats1),
                None,
                None,
                None,
                _matchers.ViInt32Matcher(len(input_array_of_floats1)),
            )

    def test_multiple_arrays_same_size_wrong_size_2(self):
        self.patched_library.niFake_MultipleArraysSameSize.side_effect = self.side_effects_helper.niFake_MultipleArraysSameSize
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
        self.patched_library.niFake_MultipleArraysSameSize.side_effect = self.side_effects_helper.niFake_MultipleArraysSameSize
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
        self.patched_library.niFake_MultipleArraysSameSize.side_effect = self.side_effects_helper.niFake_MultipleArraysSameSize
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
        self.patched_library.niFake_ParametersAreMultipleTypes.side_effect = self.side_effects_helper.niFake_ParametersAreMultipleTypes
        boolean_val = True
        int32_val = 32
        int64_val = 6000000000
        enum_val = nifake.Turtle.LEONARDO
        float_val = 1.23
        float_enum_val = nifake.FloatEnum.SIX_POINT_FIVE
        string_val = 'Testing is fun?'
        with nifake.Session('dev1') as session:
            session.parameters_are_multiple_types(boolean_val, int32_val, int64_val, enum_val, float_val, float_enum_val, string_val)
            self.patched_library.niFake_ParametersAreMultipleTypes.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViBooleanMatcher(boolean_val), _matchers.ViInt32Matcher(int32_val), _matchers.ViInt64Matcher(int64_val), _matchers.ViInt16Matcher(enum_val.value), _matchers.ViReal64Matcher(float_val), _matchers.ViReal64Matcher(float_enum_val.value), _matchers.ViInt32Matcher(len(string_val)), _matchers.ViStringMatcher(string_val))

    def test_parameters_are_multiple_types_error(self):
        test_error_code = -42
        test_error_desc = "The answer to the ultimate question"
        self.patched_library.niFake_ParametersAreMultipleTypes.side_effect = self.side_effects_helper.niFake_ParametersAreMultipleTypes
        self.side_effects_helper['ParametersAreMultipleTypes']['return'] = test_error_code
        self.patched_library.niFake_GetError.side_effect = self.side_effects_helper.niFake_GetError
        self.side_effects_helper['GetError']['errorCode'] = test_error_code
        self.side_effects_helper['GetError']['description'] = test_error_desc
        self.patched_library.niFake_ParametersAreMultipleTypes.side_effect = self.side_effects_helper.niFake_ParametersAreMultipleTypes
        self.side_effects_helper['ParametersAreMultipleTypes']['return'] = test_error_code
        self.patched_library.niFake_GetError.side_effect = self.side_effects_helper.niFake_GetError
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
        self.patched_library.niFake_PoorlyNamedSimpleFunction.side_effect = self.side_effects_helper.niFake_PoorlyNamedSimpleFunction
        self.side_effects_helper['PoorlyNamedSimpleFunction']['return'] = test_error_code
        self.patched_library.niFake_GetError.side_effect = self.side_effects_helper.niFake_GetError
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
        self.patched_library.niFake_SetAttributeViReal64.side_effect = self.side_effects_helper.niFake_SetAttributeViReal64
        self.side_effects_helper['SetAttributeViReal64']['return'] = test_error_code
        self.patched_library.niFake_GetError.side_effect = self.side_effects_helper.niFake_GetError
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
        self.patched_library.niFake_EnumInputFunctionWithDefaults.side_effect = self.side_effects_helper.niFake_EnumInputFunctionWithDefaults
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
        self.patched_library.niFake_PoorlyNamedSimpleFunction.side_effect = self.side_effects_helper.niFake_PoorlyNamedSimpleFunction
        self.side_effects_helper['PoorlyNamedSimpleFunction']['return'] = test_error_code
        self.patched_library.niFake_GetError.side_effect = self.side_effects_helper.niFake_GetError
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
        test_maximum_time = datetime.timedelta(seconds=test_maximum_time_s)
        test_reading = float('nan')
        test_error_code = 42
        test_error_desc = "The answer to the ultimate question, only positive"
        self.patched_library.niFake_Read.side_effect = self.niFake_read_warning
        self.error_code_return = test_error_code
        self.reading = test_reading
        self.patched_library.niFake_GetError.side_effect = self.side_effects_helper.niFake_GetError
        self.side_effects_helper['GetError']['errorCode'] = test_error_code
        self.side_effects_helper['GetError']['description'] = test_error_desc
        with nifake.Session('dev1') as session:
            with warnings.catch_warnings(record=True) as w:
                assert math.isnan(session.read(test_maximum_time))
                assert len(w) == 1
                assert issubclass(w[0].category, nifake.DriverWarning)
                assert test_error_desc in str(w[0].message)

    # Retrieving buffers and strings

    def test_get_a_string_of_fixed_maximum_size(self):
        test_string = "A string no larger than the max size of 256 allowed by the function."
        self.patched_library.niFake_GetAStringOfFixedMaximumSize.side_effect = self.side_effects_helper.niFake_GetAStringOfFixedMaximumSize
        self.side_effects_helper['GetAStringOfFixedMaximumSize']['aString'] = test_string
        with nifake.Session('dev1') as session:
            returned_string = session.get_a_string_of_fixed_maximum_size()
            assert returned_string == test_string
            self.patched_library.niFake_GetAStringOfFixedMaximumSize.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViCharBufferMatcher(256))

    def test_get_a_string_of_size_python_code(self):
        test_size = 4
        expected_string_size = test_size - 1
        test_string = "A string that is larger than test_size."
        expected_string = test_string[:expected_string_size]
        self.patched_library.niFake_GetAStringUsingPythonCode.side_effect = self.side_effects_helper.niFake_GetAStringUsingPythonCode
        self.side_effects_helper['GetAStringUsingPythonCode']['aString'] = expected_string
        with nifake.Session('dev1') as session:
            returned_string = session.get_a_string_using_python_code(test_size)
            assert returned_string == expected_string
            self.patched_library.niFake_GetAStringUsingPythonCode.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt16Matcher(test_size), _matchers.ViCharBufferMatcher(test_size))

    def test_return_a_number_and_a_string(self):
        test_string = "this string"
        test_number = 13
        self.patched_library.niFake_ReturnANumberAndAString.side_effect = self.side_effects_helper.niFake_ReturnANumberAndAString
        self.side_effects_helper['ReturnANumberAndAString']['aString'] = test_string
        self.side_effects_helper['ReturnANumberAndAString']['aNumber'] = test_number
        with nifake.Session('dev1') as session:
            returned_number, returned_string = session.return_a_number_and_a_string()
            assert (returned_string == test_string)
            assert (returned_number == test_number)
            self.patched_library.niFake_ReturnANumberAndAString.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt16PointerMatcher(), _matchers.ViCharBufferMatcher(256))

    def test_get_an_ivi_dance_string(self):
        self.patched_library.niFake_GetAnIviDanceString.side_effect = self.side_effects_helper.niFake_GetAnIviDanceString
        string_val = 'Testing is fun?'
        self.side_effects_helper['GetAnIviDanceString']['aString'] = string_val
        with nifake.Session('dev1') as session:
            result_string = session.get_an_ivi_dance_string()
            assert result_string == string_val
            from mock import call
            calls = [call(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(0), None), call(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(string_val)), _matchers.ViCharBufferMatcher(len(string_val)))]
            self.patched_library.niFake_GetAnIviDanceString.assert_has_calls(calls)
            assert self.patched_library.niFake_GetAnIviDanceString.call_count == 2

    def test_get_string_ivi_dance_error(self):
        test_error_code = -1234
        test_error_desc = "ascending order"
        self.patched_library.niFake_GetAttributeViString.side_effect = self.side_effects_helper.niFake_GetAttributeViString
        self.side_effects_helper['GetAttributeViString']['attributeValue'] = 'Testing is fun?'
        self.side_effects_helper['GetAttributeViString']['return'] = test_error_code
        self.patched_library.niFake_GetError.side_effect = self.side_effects_helper.niFake_GetError
        self.side_effects_helper['GetError']['errorCode'] = test_error_code
        self.side_effects_helper['GetError']['description'] = test_error_desc
        with nifake.Session('dev1') as session:
            try:
                session.read_write_string
                assert False
            except nifake.Error as e:
                assert e.code == test_error_code
                assert e.description == test_error_desc

    def test_get_array_using_ivi_dance(self):
        self.patched_library.niFake_GetArrayUsingIVIDance.side_effect = self.side_effects_helper.niFake_GetArrayUsingIVIDance
        self.side_effects_helper['GetArrayUsingIVIDance']['arrayOut'] = [1.1, 2.2]
        with nifake.Session('dev1') as session:
            result_array = session.get_array_using_ivi_dance()
            assert result_array == [1.1, 2.2]

    # Repeated Capabilities

    def test_repeated_capability_method_on_session_timedelta(self):
        test_maximum_time_ms = 10     # milliseconds
        test_maximum_time_us = 10000  # microseconds
        test_maximum_time_timedelta = datetime.timedelta(milliseconds=test_maximum_time_ms)
        test_reading = 5
        self.patched_library.niFake_ReadFromChannel.side_effect = self.side_effects_helper.niFake_ReadFromChannel
        self.side_effects_helper['ReadFromChannel']['reading'] = test_reading
        with nifake.Session('dev1') as session:
            value = session.read_from_channel(test_maximum_time_timedelta)
        self.patched_library.niFake_ReadFromChannel.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViInt32Matcher(test_maximum_time_us), _matchers.ViReal64PointerMatcher())
        assert value == test_reading

    def test_repeated_capability_method_on_specific_channel(self):
        test_maximum_time_ms = 10     # milliseconds
        test_maximum_time_us = 10000  # microseconds
        test_maximum_time = datetime.timedelta(milliseconds=test_maximum_time_ms)
        test_reading = 5
        self.patched_library.niFake_ReadFromChannel.side_effect = self.side_effects_helper.niFake_ReadFromChannel
        self.side_effects_helper['ReadFromChannel']['reading'] = test_reading
        with nifake.Session('dev1') as session:
            value = session.channels['3'].read_from_channel(test_maximum_time)
        self.patched_library.niFake_ReadFromChannel.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher('3'), _matchers.ViInt32Matcher(test_maximum_time_us), _matchers.ViReal64PointerMatcher())
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

    # Attributes

    def test_get_attribute_int32(self):
        self.patched_library.niFake_GetAttributeViInt32.side_effect = self.side_effects_helper.niFake_GetAttributeViInt32
        test_number = 3
        self.side_effects_helper['GetAttributeViInt32']['attributeValue'] = test_number
        with nifake.Session('dev1') as session:
            attr_int = session.read_write_integer
            assert(attr_int == test_number)
            self.patched_library.niFake_GetAttributeViInt32.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(1000004), _matchers.ViInt32PointerMatcher())

    def test_set_attribute_int32(self):
        self.patched_library.niFake_SetAttributeViInt32.side_effect = self.side_effects_helper.niFake_SetAttributeViInt32
        attribute_id = 1000004
        test_number = -10
        with nifake.Session('dev1') as session:
            session.read_write_integer = test_number
            self.patched_library.niFake_SetAttributeViInt32.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViInt32Matcher(test_number))

    def test_get_attribute_int32_with_converter(self):
        self.patched_library.niFake_GetAttributeViInt32.side_effect = self.side_effects_helper.niFake_GetAttributeViInt32
        attribute_id = 1000008
        test_number_ms = 3
        test_number_s = 0.003
        self.side_effects_helper['GetAttributeViInt32']['attributeValue'] = test_number_ms
        with nifake.Session('dev1') as session:
            attr_timedelta = session.read_write_integer_with_converter
            assert(attr_timedelta.total_seconds() == test_number_s)
            self.patched_library.niFake_GetAttributeViInt32.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViInt32PointerMatcher())

    def test_set_attribute_int32_with_converter(self):
        self.patched_library.niFake_SetAttributeViInt32.side_effect = self.side_effects_helper.niFake_SetAttributeViInt32
        attribute_id = 1000008
        test_number_s = -10
        test_number_ms = -10000
        with nifake.Session('dev1') as session:
            session.read_write_integer_with_converter = datetime.timedelta(seconds=test_number_s)
            self.patched_library.niFake_SetAttributeViInt32.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViInt32Matcher(test_number_ms))

    def test_get_attribute_real64(self):
        self.patched_library.niFake_GetAttributeViReal64.side_effect = self.side_effects_helper.niFake_GetAttributeViReal64
        test_number = 1.5
        self.side_effects_helper['GetAttributeViReal64']['attributeValue'] = test_number
        with nifake.Session('dev1') as session:
            attr_double = session.read_write_double
            assert attr_double == test_number
            self.patched_library.niFake_GetAttributeViReal64.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(1000001), _matchers.ViReal64PointerMatcher())

    def test_set_attribute_real64(self):
        self.patched_library.niFake_SetAttributeViReal64.side_effect = self.side_effects_helper.niFake_SetAttributeViReal64
        attribute_id = 1000001
        test_number = 10.1
        with nifake.Session('dev1') as session:
            session.read_write_double = test_number
            self.patched_library.niFake_SetAttributeViReal64.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViReal64Matcher(test_number))

    def test_get_attribute_real64_with_converter(self):
        self.patched_library.niFake_GetAttributeViReal64.side_effect = self.side_effects_helper.niFake_GetAttributeViReal64
        attribute_id = 1000007
        test_number = 1.5
        self.side_effects_helper['GetAttributeViReal64']['attributeValue'] = test_number
        with nifake.Session('dev1') as session:
            attr_timedelta = session.read_write_double_with_converter
            assert attr_timedelta.total_seconds() == test_number
            self.patched_library.niFake_GetAttributeViReal64.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViReal64PointerMatcher())

    def test_set_attribute_real64_with_converter(self):
        self.patched_library.niFake_SetAttributeViReal64.side_effect = self.side_effects_helper.niFake_SetAttributeViReal64
        attribute_id = 1000007
        test_number = -10.1
        with nifake.Session('dev1') as session:
            session.read_write_double_with_converter = datetime.timedelta(seconds=test_number)
            self.patched_library.niFake_SetAttributeViReal64.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViReal64Matcher(test_number))

    def test_get_attribute_string(self):
        self.patched_library.niFake_GetAttributeViString.side_effect = self.side_effects_helper.niFake_GetAttributeViString
        string = 'Testing is fun?'
        self.side_effects_helper['GetAttributeViString']['attributeValue'] = string
        with nifake.Session('dev1') as session:
            attr_string = session.read_write_string
            assert attr_string == string
            from mock import call
            calls = [call(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(1000002), _matchers.ViInt32Matcher(0), None), call(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(1000002), _matchers.ViInt32Matcher(15), _matchers.ViCharBufferMatcher(len(string)))]
            self.patched_library.niFake_GetAttributeViString.assert_has_calls(calls)
            assert self.patched_library.niFake_GetAttributeViString.call_count == 2

    def test_set_attribute_string(self):
        self.patched_library.niFake_SetAttributeViString.side_effect = self.side_effects_helper.niFake_SetAttributeViString
        attribute_id = 1000002
        attrib_string = 'This is test string'
        with nifake.Session('dev1') as session:
            session.read_write_string = attrib_string
            self.patched_library.niFake_SetAttributeViString.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViStringMatcher('This is test string'))

    def test_get_attribute_boolean(self):
        self.patched_library.niFake_GetAttributeViBoolean.side_effect = self.side_effects_helper.niFake_GetAttributeViBoolean
        self.side_effects_helper['GetAttributeViBoolean']['attributeValue'] = 1
        with nifake.Session('dev1') as session:
            assert session.read_write_bool
            self.patched_library.niFake_GetAttributeViBoolean.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(1000000), _matchers.ViBooleanPointerMatcher())

    def test_set_attribute_boolean(self):
        self.patched_library.niFake_SetAttributeViBoolean.side_effect = self.side_effects_helper.niFake_SetAttributeViBoolean
        attribute_id = 1000000
        attrib_bool = True
        with nifake.Session('dev1') as session:
            session.read_write_bool = attrib_bool
            self.patched_library.niFake_SetAttributeViBoolean.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViBooleanMatcher(True))

    def test_get_attribute_enum_int32(self):
        self.patched_library.niFake_GetAttributeViInt32.side_effect = self.side_effects_helper.niFake_GetAttributeViInt32
        self.side_effects_helper['GetAttributeViInt32']['attributeValue'] = nifake.Color.BLUE.value
        with nifake.Session('dev1') as session:
            assert session.read_write_color == nifake.Color.BLUE
            attribute_id = 1000003
            self.patched_library.niFake_GetAttributeViInt32.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViInt32PointerMatcher())

    def test_set_attribute_enum_int32(self):
        self.patched_library.niFake_SetAttributeViInt32.side_effect = self.side_effects_helper.niFake_SetAttributeViInt32
        enum_value = nifake.Color.RED
        with nifake.Session('dev1') as session:
            session.read_write_color = enum_value
            attribute_id = 1000003
            self.patched_library.niFake_SetAttributeViInt32.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViInt32Matcher(enum_value.value))

    def test_get_attribute_enum_real64(self):
        self.patched_library.niFake_GetAttributeViReal64.side_effect = self.side_effects_helper.niFake_GetAttributeViReal64
        enum_value = nifake.FloatEnum.SIX_POINT_FIVE
        self.side_effects_helper['GetAttributeViReal64']['attributeValue'] = enum_value.value
        with nifake.Session('dev1') as session:
            assert session.float_enum == enum_value
            attribute_id = 1000005
            self.patched_library.niFake_GetAttributeViReal64.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViReal64PointerMatcher())

    def test_set_attribute_enum_real64(self):
        self.patched_library.niFake_SetAttributeViReal64.side_effect = self.side_effects_helper.niFake_SetAttributeViReal64
        enum_value = nifake.FloatEnum.FIVE_POINT_FIVE
        with nifake.Session('dev1') as session:
            session.float_enum = enum_value
            attribute_id = 1000005
            self.patched_library.niFake_SetAttributeViReal64.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViReal64Matcher(enum_value.value))

    def test_get_attribute_channel(self):
        self.patched_library.niFake_GetAttributeViInt32.side_effect = self.side_effects_helper.niFake_GetAttributeViInt32
        test_number = 100
        self.side_effects_helper['GetAttributeViInt32']['attributeValue'] = test_number
        with nifake.Session('dev1') as session:
            attr_int = session.channels[['0', '1']].read_write_integer
            assert(attr_int == test_number)
            self.patched_library.niFake_GetAttributeViInt32.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher('0,1'), _matchers.ViAttrMatcher(1000004), _matchers.ViInt32PointerMatcher())

    def test_set_attribute_channel(self):
        self.patched_library.niFake_SetAttributeViReal64.side_effect = self.side_effects_helper.niFake_SetAttributeViReal64
        attribute_id = 1000001
        test_number = 0.001
        with nifake.Session('dev1') as session:
            session.channels[range(24)].read_write_double = test_number
            self.patched_library.niFake_SetAttributeViReal64.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher('0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23'), _matchers.ViAttrMatcher(attribute_id), _matchers.ViReal64Matcher(test_number))

    def test_get_attribute_int64(self):
        self.patched_library.niFake_GetAttributeViInt64.side_effect = self.side_effects_helper.niFake_GetAttributeViInt64
        attribute_id = 1000006
        test_number = 6000000000
        self.side_effects_helper['GetAttributeViInt64']['attributeValue'] = test_number
        with nifake.Session('dev1') as session:
            attr_int = session.read_write_int64
            assert(attr_int == test_number)
            self.patched_library.niFake_GetAttributeViInt64.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViInt64PointerMatcher())

    def test_set_attribute_int64(self):
        self.patched_library.niFake_SetAttributeViInt64.side_effect = self.side_effects_helper.niFake_SetAttributeViInt64
        attribute_id = 1000006
        test_number = -6000000000
        with nifake.Session('dev1') as session:
            session.read_write_int64 = test_number
            self.patched_library.niFake_SetAttributeViInt64.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViInt64Matcher(test_number))

    def test_get_attribute_error(self):
        test_error_code = -123
        test_error_desc = "ascending order"
        self.patched_library.niFake_GetAttributeViReal64.side_effect = self.side_effects_helper.niFake_GetAttributeViReal64
        self.side_effects_helper['GetAttributeViReal64']['attributeValue'] = 'Testing is fun?'
        self.side_effects_helper['GetAttributeViReal64']['return'] = test_error_code
        self.patched_library.niFake_GetError.side_effect = self.side_effects_helper.niFake_GetError
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
        self.patched_library.niFake_SetAttributeViReal64.side_effect = self.side_effects_helper.niFake_SetAttributeViReal64
        self.side_effects_helper['SetAttributeViReal64']['return'] = test_error_code
        self.patched_library.niFake_GetError.side_effect = self.side_effects_helper.niFake_GetError
        self.side_effects_helper['GetError']['errorCode'] = test_error_code
        self.side_effects_helper['GetError']['description'] = test_error_desc
        with nifake.Session('dev1') as session:
            try:
                session.read_write_double = -42.0
                assert False
            except nifake.Error as e:
                assert e.code == test_error_code
                assert e.description == test_error_desc
                self.patched_library.niFake_SetAttributeViReal64.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(1000001), _matchers.ViReal64Matcher(-42.0))

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
        self.patched_library.niFake_PoorlyNamedSimpleFunction.side_effect = self.side_effects_helper.niFake_PoorlyNamedSimpleFunction
        self.side_effects_helper['PoorlyNamedSimpleFunction']['return'] = test_error_code
        self.patched_library.niFake_GetError.side_effect = self.side_effects_helper.niFake_GetError
        self.side_effects_helper['GetError']['errorCode'] = -1
        self.side_effects_helper['GetError']['description'] = "Shouldn't get this"
        self.side_effects_helper['GetError']['return'] = -2
        self.patched_library.niFake_error_message.side_effect = self.side_effects_helper.niFake_error_message
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
        self.patched_library.niFake_PoorlyNamedSimpleFunction.side_effect = self.side_effects_helper.niFake_PoorlyNamedSimpleFunction
        self.side_effects_helper['PoorlyNamedSimpleFunction']['return'] = test_error_code
        self.patched_library.niFake_GetError.side_effect = self.side_effects_helper.niFake_GetError
        self.side_effects_helper['GetError']['errorCode'] = -1
        self.side_effects_helper['GetError']['description'] = "Shouldn't get this"
        self.side_effects_helper['GetError']['return'] = -2
        self.patched_library.niFake_error_message.side_effect = self.side_effects_helper.niFake_error_message
        self.side_effects_helper['error_message']['errorMessage'] = test_error_desc
        with nifake.Session('dev1') as session:
            try:
                session.simple_function()
            except nifake.Error as e:
                assert e.code == test_error_code
                assert e.description == test_error_desc
        self.patched_library.niFake_error_message.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(test_error_code), _matchers.ViCharBufferMatcher(256))

    # Custom types

    def test_set_custom_type(self):
        self.patched_library.niFake_SetCustomType.side_effect = self.side_effects_helper.niFake_SetCustomType
        cs = nifake.CustomStruct(struct_int=42, struct_double=4.2)
        with nifake.Session('dev1') as session:
            session.set_custom_type(cs)
            self.patched_library.niFake_SetCustomType.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.CustomTypeMatcher(nifake.custom_struct, nifake.custom_struct(cs)))

    def test_get_custom_type(self):
        self.patched_library.niFake_GetCustomType.side_effect = self.side_effects_helper.niFake_GetCustomType
        cs_ctype = nifake.custom_struct(struct_int=42, struct_double=4.2)
        self.side_effects_helper['GetCustomType']['cs'] = cs_ctype
        with nifake.Session('dev1') as session:
            cs = session.get_custom_type()
            assert cs.struct_int == cs_ctype.struct_int
            assert cs.struct_double == cs_ctype.struct_double

    def test_set_custom_type_array(self):
        self.patched_library.niFake_SetCustomTypeArray.side_effect = self.side_effects_helper.niFake_SetCustomTypeArray
        cs = [nifake.CustomStruct(struct_int=42, struct_double=4.2), nifake.CustomStruct(struct_int=43, struct_double=4.3), nifake.CustomStruct(struct_int=42, struct_double=4.3)]
        cs_ctype = (nifake.custom_struct * len(cs))(*[nifake.custom_struct(c) for c in cs])
        with nifake.Session('dev1') as session:
            session.set_custom_type_array(cs)
            self.patched_library.niFake_SetCustomTypeArray.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(cs)), _matchers.CustomTypeBufferMatcher(nifake.custom_struct, cs_ctype))

    def test_get_custom_type_array(self):
        self.patched_library.niFake_GetCustomTypeArray.side_effect = self.side_effects_helper.niFake_GetCustomTypeArray
        cs = [nifake.CustomStruct(struct_int=42, struct_double=4.2), nifake.CustomStruct(struct_int=43, struct_double=4.3), nifake.CustomStruct(struct_int=42, struct_double=4.3)]
        cs_ctype = (nifake.custom_struct * len(cs))(*[nifake.custom_struct(c) for c in cs])
        self.side_effects_helper['GetCustomTypeArray']['cs'] = cs_ctype
        with nifake.Session('dev1') as session:
            cs_test = session.get_custom_type_array(len(cs_ctype))
            assert len(cs_test) == len(cs_ctype)
            for actual, expected in zip(cs_test, cs):
                assert actual.struct_int == expected.struct_int
                assert actual.struct_double == expected.struct_double

    # python-code size mechanism

    def test_get_array_using_python_code_double(self):
        import nifake._visatype
        self.patched_library.niFake_GetArraySizeForPythonCode.side_effect = self.side_effects_helper.niFake_GetArraySizeForPythonCode
        self.patched_library.niFake_GetArrayForPythonCodeDouble.side_effect = self.side_effects_helper.niFake_GetArrayForPythonCodeDouble
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
        self.patched_library.niFake_GetArraySizeForPythonCode.side_effect = self.side_effects_helper.niFake_GetArraySizeForPythonCode
        self.patched_library.niFake_GetArrayForPythonCodeCustomType.side_effect = self.side_effects_helper.niFake_GetArrayForPythonCodeCustomType
        cs = [nifake.CustomStruct(struct_int=42, struct_double=4.2), nifake.CustomStruct(struct_int=43, struct_double=4.3), nifake.CustomStruct(struct_int=42, struct_double=4.3)]
        cs_ctype = (nifake.custom_struct * len(cs))(*[nifake.custom_struct(c) for c in cs])
        self.side_effects_helper['GetArraySizeForPythonCode']['sizeOut'] = len(cs)
        self.side_effects_helper['GetArrayForPythonCodeCustomType']['arrayOut'] = cs_ctype
        with nifake.Session('dev1') as session:
            cs_test = session.get_array_for_python_code_custom_type()
            assert len(cs_test) == len(cs)
            for actual, expected in zip(cs_test, cs):
                assert actual.struct_int == expected.struct_int
                assert actual.struct_double == expected.struct_double

    def test_get_cal_date_time(self):
        self.patched_library.niFake_GetCalDateAndTime.side_effect = self.side_effects_helper.niFake_GetCalDateAndTime
        month = 12
        day = 30
        year = 1988
        hour = 10
        minute = 15
        self.side_effects_helper['GetCalDateAndTime']['return'] = 0
        self.side_effects_helper['GetCalDateAndTime']['Month'] = month
        self.side_effects_helper['GetCalDateAndTime']['Day'] = day
        self.side_effects_helper['GetCalDateAndTime']['Year'] = year
        self.side_effects_helper['GetCalDateAndTime']['Hour'] = hour
        self.side_effects_helper['GetCalDateAndTime']['Minute'] = minute
        with nifake.Session('dev1') as session:
            last_cal = session.get_cal_date_and_time(0)
            assert isinstance(last_cal, datetime.datetime)
            assert datetime.datetime(year, month, day, hour, minute) == last_cal

    def test_get_cal_interval(self):
        self.patched_library.niFake_GetCalInterval = self.side_effects_helper.niFake_GetCalInterval
        self.side_effects_helper['GetCalInterval']['Months'] = 24
        with nifake.Session('dev1') as session:
            last_cal = session.get_cal_interval()
            assert isinstance(last_cal, datetime.timedelta)
            assert 730 == last_cal.days

    def test_matcher_prints(self):
        assert _matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST).__repr__() == "ViSessionMatcher(" + str(nifake._visatype.ViSession) + ", 42)"
        assert _matchers.ViAttrMatcher(SESSION_NUM_FOR_TEST).__repr__() == "ViAttrMatcher(" + str(nifake._visatype.ViAttr) + ", 42)"
        assert _matchers.ViInt32Matcher(4).__repr__() == "ViInt32Matcher(" + str(nifake._visatype.ViInt32) + ", 4)"
        assert _matchers.ViStringMatcher('0-24').__repr__() == "ViStringMatcher('0-24')"
        assert _matchers.ViReal64Matcher(-42.0).__repr__() == "ViReal64Matcher(" + str(nifake._visatype.ViReal64) + ", -42.0)"
        assert _matchers.ViReal64PointerMatcher().__repr__() == "ViReal64PointerMatcher(" + str(nifake._visatype.ViReal64) + ")"
        assert _matchers.ViInt32PointerMatcher().__repr__() == "ViInt32PointerMatcher(" + str(nifake._visatype.ViInt32) + ")"
        cs = [nifake.CustomStruct(struct_int=42, struct_double=4.2), nifake.CustomStruct(struct_int=43, struct_double=4.3), nifake.CustomStruct(struct_int=42, struct_double=4.3)]
        cs_ctype = (nifake.custom_struct * len(cs))(*[nifake.custom_struct(c) for c in cs])
        assert _matchers.CustomTypeMatcher(nifake.custom_struct, nifake.custom_struct(cs[0])).__repr__() == "CustomTypeMatcher(<class 'nifake.custom_struct.custom_struct'>, custom_struct(data=None, struct_int=42, struct_double=4.2))"
        assert _matchers.CustomTypeBufferMatcher(nifake.custom_struct, cs_ctype).__repr__() == "CustomTypeBufferMatcher(<class 'nifake.custom_struct.custom_struct'>, [custom_struct(data=None, struct_int=42, struct_double=4.2), custom_struct(data=None, struct_int=43, struct_double=4.3), custom_struct(data=None, struct_int=42, struct_double=4.3)])"

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
            # Cannot use session.<property>.__name__ since that invokes the get attribute value


# not session tests per se
def test_diagnostic_information():
    info = nifake.print_diagnostic_information()
    assert isinstance(info, dict)


def test_dunder_version():
    print('Version = {}'.format(nifake.__version__))
    assert type(nifake.__version__) is str

