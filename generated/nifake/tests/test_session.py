import matchers
import math
import mock_helper
import nifake
import warnings

from mock import patch

# Tests


SESSION_NUM_FOR_TEST = 42


class TestSession(object):

    def setup_method(self, method):
        self.patched_library_patcher = patch('nifake.library.Library', autospec=True)
        self.patched_library = self.patched_library_patcher.start()
        self.patched_library_singleton_get = patch('nifake.session.library_singleton.get', return_value=self.patched_library)
        self.patched_library_singleton_get.start()

        self.side_effects_helper = mock_helper.SideEffectsHelper()
        self.side_effects_helper.set_side_effects_and_return_values(self.patched_library)
        self.patched_library.niFake_InitWithOptions.side_effect = self.side_effects_helper.niFake_InitWithOptions
        self.disallow_close = self.patched_library.niFake_close.side_effect
        self.patched_library.niFake_close.side_effect = self.side_effects_helper.niFake_close

        self.side_effects_helper['InitWithOptions']['vi'] = SESSION_NUM_FOR_TEST

    def teardown_method(self, method):
        self.patched_library_singleton_get.stop()
        self.patched_library_patcher.stop()

    def niFake_read_warning(self, vi, maximum_time, reading):  # noqa: N802
        reading.contents.value = self.reading
        return self.error_code_return

    # Session management

    def test_init_with_options_and_close(self):
        errors_patcher = patch('nifake.session.errors', spec_set=['handle_error', '_is_error'])
        patched_errors = errors_patcher.start()
        patched_errors._is_error.return_value = 0

        session = nifake.Session('dev1')
        self.patched_library.niFake_InitWithOptions.assert_called_once_with(matchers.ViStringMatcher('dev1'), matchers.ViBooleanMatcher(False), matchers.ViBooleanMatcher(False), matchers.ViStringMatcher(''), matchers.ViSessionPointerMatcher())
        patched_errors.handle_error.assert_called_once_with(session, self.patched_library.niFake_InitWithOptions.return_value, ignore_warnings=False, is_error_handling=False)
        session.close()
        self.patched_library.niFake_close.assert_called_once_with(matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST))

        errors_patcher.stop()

    def test_init_with_options_nondefault_and_close(self):
        session = nifake.Session('FakeDevice', True, True, 'Some string')
        self.patched_library.niFake_InitWithOptions.assert_called_once_with(matchers.ViStringMatcher('FakeDevice'), matchers.ViBooleanMatcher(True), matchers.ViBooleanMatcher(True), matchers.ViStringMatcher('Some string'), matchers.ViSessionPointerMatcher())
        session.close()
        self.patched_library.niFake_close.assert_called_once_with(matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST))

    def test_close(self):
        session = nifake.Session('dev1')
        session.close()
        self.patched_library.niFake_close.assert_called_once_with(matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST))

    def test_session_context_manager(self):
        with nifake.Session('dev1') as session:
            assert type(session) == nifake.Session
            self.patched_library.niFake_InitWithOptions.assert_called_once_with(matchers.ViStringMatcher('dev1'), matchers.ViBooleanMatcher(False), matchers.ViBooleanMatcher(False), matchers.ViStringMatcher(''), matchers.ViSessionPointerMatcher())
        self.patched_library.niFake_close.assert_called_once_with(matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST))

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
        self.patched_library.niFake_close.assert_called_once_with(matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST))

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

    # Methods

    def test_simple_function(self):
        self.patched_library.niFake_SimpleFunction.side_effect = self.side_effects_helper.niFake_SimpleFunction
        with nifake.Session('dev1') as session:
            session.simple_function()
            self.patched_library.niFake_SimpleFunction.assert_called_once_with(matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST))

    def test_get_a_number(self):
        test_number = 16
        self.patched_library.niFake_GetANumber.side_effect = self.side_effects_helper.niFake_GetANumber
        self.side_effects_helper['GetANumber']['aNumber'] = test_number
        with nifake.Session('dev1') as session:
            test_result = session.get_a_number()
            assert isinstance(test_result, int)
            assert test_result == test_number
            self.patched_library.niFake_GetANumber.assert_called_once_with(matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), matchers.ViInt16PointerMatcher())

    def test_one_input_function(self):
        test_number = 1
        self.patched_library.niFake_OneInputFunction.side_effect = self.side_effects_helper.niFake_OneInputFunction
        with nifake.Session('dev1') as session:
            session.one_input_function(test_number)
            self.patched_library.niFake_OneInputFunction.assert_called_once_with(matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), matchers.ViInt32Matcher(test_number))

    def test_vi_int_64_function(self):
        input_value = 1099511627776  # 2^40
        output_value = 2199023255552  # 2^41
        self.patched_library.niFake_Use64BitNumber.side_effect = self.side_effects_helper.niFake_Use64BitNumber
        self.side_effects_helper['Use64BitNumber']['output'] = output_value
        with nifake.Session('dev1') as session:
            assert session.use64_bit_number(input_value) == output_value
            self.patched_library.niFake_Use64BitNumber.assert_called_once_with(matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), matchers.ViInt64Matcher(input_value), matchers.ViInt64PointerMatcher())

    def test_two_input_function(self):
        test_number = 1.5
        test_string = 'test'
        self.patched_library.niFake_TwoInputFunction.side_effect = self.side_effects_helper.niFake_TwoInputFunction
        with nifake.Session('dev1') as session:
            session.two_input_function(test_number, test_string)
            self.patched_library.niFake_TwoInputFunction.assert_called_once_with(matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), matchers.ViReal64Matcher(test_number), matchers.ViStringMatcher(test_string))

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
            self.patched_library.niFake_GetEnumValue.assert_called_once_with(matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), matchers.ViInt32PointerMatcher(), matchers.ViInt16PointerMatcher())

    def test_get_a_list_enums(self):
        self.patched_library.niFake_EnumArrayOutputFunction.side_effect = self.side_effects_helper.niFake_EnumArrayOutputFunction
        test_array = [1, 1, 0]
        test_array_size = len(test_array)
        self.side_effects_helper['EnumArrayOutputFunction']['anArray'] = test_array
        with nifake.Session('dev1') as session:
            test_result = session.enum_array_output_function(test_array_size)
            assert test_array_size == len(test_result)
            for i in range(test_array_size):
                assert isinstance(test_result[i], nifake.Turtle)
                assert test_result[i].value == test_array[i]
            self.patched_library.niFake_EnumArrayOutputFunction.assert_called_once_with(matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), matchers.ViInt32Matcher(test_array_size), matchers.ViInt16BufferMatcher(test_array_size))

    def test_get_a_boolean(self):
        self.patched_library.niFake_GetABoolean.side_effect = self.side_effects_helper.niFake_GetABoolean
        self.side_effects_helper['GetABoolean']['aBoolean'] = 1
        with nifake.Session('dev1') as session:
            test_result = session.get_a_boolean()
            assert isinstance(test_result, bool)
            assert test_result
            self.patched_library.niFake_GetABoolean.assert_called_once_with(matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), matchers.ViBooleanPointerMatcher())

    def test_get_a_list_booleans(self):
        self.patched_library.niFake_BoolArrayOutputFunction.side_effect = self.side_effects_helper.niFake_BoolArrayOutputFunction
        test_array = [1, 1, 0]
        test_array_size = len(test_array)
        self.side_effects_helper['BoolArrayOutputFunction']['anArray'] = test_array
        with nifake.Session('dev1') as session:
            test_result = session.bool_array_output_function(test_array_size)
            assert test_array_size == len(test_result)
            for i in range(test_array_size):
                assert isinstance(test_result[0], bool)
                assert test_result[i] == bool(test_array[i])
            self.patched_library.niFake_BoolArrayOutputFunction.assert_called_once_with(matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), matchers.ViInt32Matcher(test_array_size), matchers.ViBooleanBufferMatcher(test_array_size))

    def test_acquisition_context_manager(self):
        self.patched_library.niFake_Initiate.side_effect = self.side_effects_helper.niFake_Initiate
        self.patched_library.niFake_Abort.side_effect = self.side_effects_helper.niFake_Abort
        with nifake.Session('dev1') as session:
            with session.initiate():
                self.patched_library.niFake_Initiate.assert_called_once_with(matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST))
            self.patched_library.niFake_Abort.assert_called_once_with(matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST))
        self.patched_library.niFake_close.assert_called_once_with(matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST))

    def test_single_point_read(self):
        test_maximum_time = 10
        test_reading = 5
        self.patched_library.niFake_Read.side_effect = self.side_effects_helper.niFake_Read
        self.side_effects_helper['Read']['reading'] = test_reading
        with nifake.Session('dev1') as session:
            assert test_reading == session.read(test_maximum_time)
            self.patched_library.niFake_Read.assert_called_once_with(matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), matchers.ViInt32Matcher(test_maximum_time), matchers.ViReal64PointerMatcher())

    def test_single_point_read_nan(self):
        test_maximum_time = 10
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
            calls = [call(matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), matchers.ViInt16Matcher(0)), call(matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), matchers.ViInt16Matcher(1))]  # 0 is the value of the default of nifake.Turtle.LEONARDO, 1 is the value of nifake.Turtle.DONATELLO
            self.patched_library.niFake_EnumInputFunctionWithDefaults.assert_has_calls(calls)

    def test_multipoint_read(self):
        test_maximum_time = 1000
        test_reading_array = [1.0, 0.1, 42, .42]
        test_actual_number_of_points = len(test_reading_array)
        self.patched_library.niFake_ReadMultiPoint.side_effect = self.side_effects_helper.niFake_ReadMultiPoint
        self.side_effects_helper['ReadMultiPoint']['readingArray'] = test_reading_array
        self.side_effects_helper['ReadMultiPoint']['actualNumberOfPoints'] = test_actual_number_of_points
        with nifake.Session('dev1') as session:
            measurements, points = session.read_multi_point(test_maximum_time, len(test_reading_array))
            assert len(measurements) == test_actual_number_of_points
            assert isinstance(measurements[0], float)
            assert points == test_actual_number_of_points
            assert measurements == test_reading_array
            self.patched_library.niFake_ReadMultiPoint.assert_called_once_with(matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), matchers.ViInt32Matcher(test_maximum_time), matchers.ViInt32Matcher(len(test_reading_array)), matchers.ViReal64BufferMatcher(len(test_reading_array)), matchers.ViInt32PointerMatcher())

    def test_array_input_function(self):
        test_array = [1, 2, 3, 4]
        test_array_size = len(test_array)
        self.patched_library.niFake_ArrayInputFunction.side_effect = self.side_effects_helper.niFake_ArrayInputFunction
        with nifake.Session('dev1') as session:
            session.array_input_function(test_array)
            self.patched_library.niFake_ArrayInputFunction.assert_called_once_with(matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), matchers.ViInt32Matcher(test_array_size), matchers.ViReal64BufferMatcher(test_array))

    def test_return_multiple_types(self):
        self.patched_library.niFake_ReturnMultipleTypes.side_effect = self.side_effects_helper.niFake_ReturnMultipleTypes
        boolean_val = True
        int32_val = 32
        int64_val = 6000000000
        enum_val = nifake.Turtle.LEONARDO
        float_val = 1.23
        float_enum_val = nifake.FloatEnum._6_5
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
            try:
                assert isinstance(result_string, basestring)
            except NameError:
                assert isinstance(result_string, str)
            assert self.patched_library.niFake_ReturnMultipleTypes.call_count == 2

    def test_multiple_array_types(self):
        self.patched_library.niFake_MultipleArrayTypes.side_effect = self.side_effects_helper.niFake_MultipleArrayTypes
        passed_in_array = [0.0, 1.0]
        passed_in_array_size = len(passed_in_array)
        fixed_size_array = [2.0, 3.0, 4.0]
        len_array = [5.0, 6.0, 7.0, 8.0]
        self.side_effects_helper['MultipleArrayTypes']['passedInArray'] = passed_in_array
        self.side_effects_helper['MultipleArrayTypes']['aFixedArray'] = fixed_size_array
        self.side_effects_helper['MultipleArrayTypes']['return'] = 0
        with nifake.Session('dev1') as session:
            passed_in_array_result, fixed_size_array_result = session.multiple_array_types(passed_in_array_size, len_array)
            assert passed_in_array == passed_in_array_result
            assert fixed_size_array == fixed_size_array_result

    def test_parameters_are_multiple_types(self):
        self.patched_library.niFake_ParametersAreMultipleTypes.side_effect = self.side_effects_helper.niFake_ParametersAreMultipleTypes
        boolean_val = True
        int32_val = 32
        int64_val = 6000000000
        enum_val = nifake.Turtle.LEONARDO
        float_val = 1.23
        float_enum_val = nifake.FloatEnum._6_5
        string_val = 'Testing is fun?'
        with nifake.Session('dev1') as session:
            session.parameters_are_multiple_types(boolean_val, int32_val, int64_val, enum_val, float_val, float_enum_val, string_val)
            self.patched_library.niFake_ParametersAreMultipleTypes.assert_called_once_with(matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), matchers.ViBooleanMatcher(boolean_val), matchers.ViInt32Matcher(int32_val), matchers.ViInt64Matcher(int64_val), matchers.ViInt16Matcher(enum_val.value), matchers.ViReal64Matcher(float_val), matchers.ViReal64Matcher(float_enum_val.value), matchers.ViInt32Matcher(len(string_val)), matchers.ViStringMatcher(string_val))

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
        float_enum_val = nifake.FloatEnum._6_5
        string_val = 'Testing is fun?'
        with nifake.Session('dev1') as session:
            try:
                session.parameters_are_multiple_types(boolean_val, int32_val, int64_val, 123, float_val, float_enum_val, string_val)
                assert False
            except TypeError as e:
                pass
            try:
                session.parameters_are_multiple_types(boolean_val, int32_val, int64_val, enum_val, float_val, 0.123, string_val)
                assert False
            except TypeError as e:
                pass

    def test_method_with_error(self):
        test_error_code = -42
        test_error_desc = "The answer to the ultimate question"
        self.patched_library.niFake_SimpleFunction.side_effect = self.side_effects_helper.niFake_SimpleFunction
        self.side_effects_helper['SimpleFunction']['return'] = test_error_code
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
                session['100'].read_write_double = 5.0
                assert False
            except nifake.Error as e:
                assert e.code == test_error_code
                assert e.description == test_error_desc

    def test_call_not_enough_parameters_error(self):
        with nifake.Session('dev1') as session:
            try:
                session.multiple_array_types(10)
                assert False
            except TypeError as e:
                pass

    def test_invalid_method_call_wrong_type_error(self):
        with nifake.Session('dev1') as session:
            try:
                session.multiple_array_types('potato', [0.0, 0.1, 0.2])
                assert False
            except TypeError as e:
                pass

    def test_enum_input_function_with_defaults_bad_type_error(self):
        test_turtle = 123
        self.patched_library.niFake_EnumInputFunctionWithDefaults.side_effect = self.side_effects_helper.niFake_EnumInputFunctionWithDefaults
        with nifake.Session('dev1') as session:
            try:
                session.enum_input_function_with_defaults(test_turtle)
                assert False
            except TypeError as e:
                pass

    def test_method_with_warning(self):
        test_error_code = 42
        test_error_desc = "The answer to the ultimate question, only positive"
        self.patched_library.niFake_SimpleFunction.side_effect = self.side_effects_helper.niFake_SimpleFunction
        self.side_effects_helper['SimpleFunction']['return'] = test_error_code
        self.patched_library.niFake_GetError.side_effect = self.side_effects_helper.niFake_GetError
        self.side_effects_helper['GetError']['errorCode'] = test_error_code
        self.side_effects_helper['GetError']['description'] = test_error_desc
        with nifake.Session('dev1') as session:
            with warnings.catch_warnings(record=True) as w:
                session.simple_function()
                assert len(w) == 1
                assert issubclass(w[0].category, nifake.NifakeWarning)
                assert test_error_desc in str(w[0].message)

    def test_read_with_warning(self):
        test_maximum_time = 10
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
                assert issubclass(w[0].category, nifake.NifakeWarning)
                assert test_error_desc in str(w[0].message)

    # Retrieving buffers and strings

    def test_get_a_string_of_fixed_maximum_size(self):
        test_string = "A string no larger than the max size of 256 allowed by the function."
        self.patched_library.niFake_GetAStringOfFixedMaximumSize.side_effect = self.side_effects_helper.niFake_GetAStringOfFixedMaximumSize
        self.side_effects_helper['GetAStringOfFixedMaximumSize']['aString'] = test_string
        with nifake.Session('dev1') as session:
            returned_string = session.get_a_string_of_fixed_maximum_size()
            assert returned_string == test_string
            self.patched_library.niFake_GetAStringOfFixedMaximumSize.assert_called_once_with(matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), matchers.ViCharBufferMatcher(256))

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
            self.patched_library.niFake_ReturnANumberAndAString.assert_called_once_with(matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), matchers.ViInt16PointerMatcher(), matchers.ViCharBufferMatcher(256))

    def test_get_an_ivi_dance_string(self):
        self.patched_library.niFake_GetAnIviDanceString.side_effect = self.side_effects_helper.niFake_GetAnIviDanceString
        string_val = 'Testing is fun?'
        self.side_effects_helper['GetAnIviDanceString']['aString'] = ''
        self.side_effects_helper['GetAnIviDanceString']['return'] = len(string_val)
        self.side_effects_helper['GetAnIviDanceString']['aString'] = string_val
        self.side_effects_helper['GetAnIviDanceString']['return'] = 0
        with nifake.Session('dev1') as session:
            result_string = session.get_an_ivi_dance_string()
            assert result_string == string_val
            from mock import call
            calls = [call(matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), matchers.ViInt32Matcher(0), None), call(matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), matchers.ViInt32Matcher(len(string_val)), matchers.ViCharBufferMatcher(len(string_val)))]
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
        self.side_effects_helper['GetArrayUsingIVIDance']['arrayOut'] = None
        self.side_effects_helper['GetArrayUsingIVIDance']['return'] = 2
        self.side_effects_helper['GetArrayUsingIVIDance']['arrayOut'] = [1.1, 2.2]
        self.side_effects_helper['GetArrayUsingIVIDance']['return'] = 0
        with nifake.Session('dev1') as session:
            result_array = session.get_array_using_ivi_dance()
            assert result_array == [1.1, 2.2]

    # Repeated Capabilities

    def test_repeated_capability_method_on_session(self):
        test_maximum_time = 10
        test_reading = 5
        self.patched_library.niFake_ReadFromChannel.side_effect = self.side_effects_helper.niFake_ReadFromChannel
        self.side_effects_helper['ReadFromChannel']['reading'] = test_reading
        with nifake.Session('dev1') as session:
            value = session.read_from_channel(test_maximum_time)
        self.patched_library.niFake_ReadFromChannel.assert_called_once_with(matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), matchers.ViStringMatcher(''), matchers.ViInt32Matcher(test_maximum_time), matchers.ViReal64PointerMatcher())
        assert value == test_reading

    def test_repeated_capability_method_on_specific_channel(self):
        test_maximum_time = 10
        test_reading = 5
        self.patched_library.niFake_ReadFromChannel.side_effect = self.side_effects_helper.niFake_ReadFromChannel
        self.side_effects_helper['ReadFromChannel']['reading'] = test_reading
        with nifake.Session('dev1') as session:
            value = session['3'].read_from_channel(test_maximum_time)
        self.patched_library.niFake_ReadFromChannel.assert_called_once_with(matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), matchers.ViStringMatcher('3'), matchers.ViInt32Matcher(test_maximum_time), matchers.ViReal64PointerMatcher())
        assert value == test_reading

    def test_device_method_not_exist_on_repeated_capability_error(self):
        with nifake.Session('dev1') as session:
            try:
                session['3'].simple_function()
                assert False, 'Method has no repeated capability so it shouldn\'t exist on _RepeatedCapability'
            except AttributeError:
                pass

    # Attributes

    def test_get_attribute_int32(self):
        self.patched_library.niFake_GetAttributeViInt32.side_effect = self.side_effects_helper.niFake_GetAttributeViInt32
        test_number = 3
        self.side_effects_helper['GetAttributeViInt32']['attributeValue'] = test_number
        with nifake.Session('dev1') as session:
            attr_int = session.read_write_integer
            assert(attr_int == test_number)
            self.patched_library.niFake_GetAttributeViInt32.assert_called_once_with(matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), matchers.ViStringMatcher(''), matchers.ViInt32Matcher(1000004), matchers.ViInt32PointerMatcher())

    def test_set_attribute_int32(self):
        self.patched_library.niFake_SetAttributeViInt32.side_effect = self.side_effects_helper.niFake_SetAttributeViInt32
        attribute_id = 1000004
        test_number = -10
        with nifake.Session('dev1') as session:
            session.read_write_integer = test_number
            self.patched_library.niFake_SetAttributeViInt32.assert_called_once_with(matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), matchers.ViStringMatcher(''), matchers.ViInt32Matcher(attribute_id), matchers.ViInt32Matcher(test_number))

    def test_get_attribute_real64(self):
        self.patched_library.niFake_GetAttributeViReal64.side_effect = self.side_effects_helper.niFake_GetAttributeViReal64
        test_number = 1.5
        self.side_effects_helper['GetAttributeViReal64']['attributeValue'] = test_number
        with nifake.Session('dev1') as session:
            attr_double = session.read_write_double
            assert attr_double == test_number
            self.patched_library.niFake_GetAttributeViReal64.assert_called_once_with(matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), matchers.ViStringMatcher(''), matchers.ViInt32Matcher(1000001), matchers.ViReal64PointerMatcher())

    def test_set_attribute_real64(self):
        self.patched_library.niFake_SetAttributeViReal64.side_effect = self.side_effects_helper.niFake_SetAttributeViReal64
        attribute_id = 1000001
        test_number = -10.1
        with nifake.Session('dev1') as session:
            session.read_write_double = test_number
            self.patched_library.niFake_SetAttributeViReal64.assert_called_once_with(matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), matchers.ViStringMatcher(''), matchers.ViInt32Matcher(attribute_id), matchers.ViReal64Matcher(test_number))

    def test_get_attribute_string(self):
        self.patched_library.niFake_GetAttributeViString.side_effect = self.side_effects_helper.niFake_GetAttributeViString
        string = 'Testing is fun?'
        self.side_effects_helper['GetAttributeViString']['attributeValue'] = string
        with nifake.Session('dev1') as session:
            attr_string = session.read_write_string
            assert attr_string == string
            from mock import call
            calls = [call(matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), matchers.ViStringMatcher(''), matchers.ViInt32Matcher(1000002), matchers.ViInt32Matcher(0), None), call(matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), matchers.ViStringMatcher(''), matchers.ViInt32Matcher(1000002), matchers.ViInt32Matcher(15), matchers.ViCharBufferMatcher(len(string)))]
            self.patched_library.niFake_GetAttributeViString.assert_has_calls(calls)
            assert self.patched_library.niFake_GetAttributeViString.call_count == 2

    def test_set_attribute_string(self):
        self.patched_library.niFake_SetAttributeViString.side_effect = self.side_effects_helper.niFake_SetAttributeViString
        attribute_id = 1000002
        attrib_string = 'This is test string'
        with nifake.Session('dev1') as session:
            session.read_write_string = attrib_string
            self.patched_library.niFake_SetAttributeViString.assert_called_once_with(matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), matchers.ViStringMatcher(''), matchers.ViInt32Matcher(attribute_id), matchers.ViStringMatcher('This is test string'))

    def test_get_attribute_boolean(self):
        self.patched_library.niFake_GetAttributeViBoolean.side_effect = self.side_effects_helper.niFake_GetAttributeViBoolean
        self.side_effects_helper['GetAttributeViBoolean']['attributeValue'] = 1
        with nifake.Session('dev1') as session:
            assert session.read_write_bool
            self.patched_library.niFake_GetAttributeViBoolean.assert_called_once_with(matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), matchers.ViStringMatcher(''), matchers.ViInt32Matcher(1000000), matchers.ViBooleanPointerMatcher())

    def test_set_attribute_boolean(self):
        self.patched_library.niFake_SetAttributeViBoolean.side_effect = self.side_effects_helper.niFake_SetAttributeViBoolean
        attribute_id = 1000000
        attrib_bool = True
        with nifake.Session('dev1') as session:
            session.read_write_bool = attrib_bool
            self.patched_library.niFake_SetAttributeViBoolean.assert_called_once_with(matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), matchers.ViStringMatcher(''), matchers.ViInt32Matcher(attribute_id), matchers.ViBooleanMatcher(True))

    def test_get_attribute_enum_int32(self):
        self.patched_library.niFake_GetAttributeViInt32.side_effect = self.side_effects_helper.niFake_GetAttributeViInt32
        self.side_effects_helper['GetAttributeViInt32']['attributeValue'] = nifake.Color.BLUE.value
        with nifake.Session('dev1') as session:
            assert session.read_write_color == nifake.Color.BLUE
            attribute_id = 1000003
            self.patched_library.niFake_GetAttributeViInt32.assert_called_once_with(matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), matchers.ViStringMatcher(''), matchers.ViInt32Matcher(attribute_id), matchers.ViInt32PointerMatcher())

    def test_set_attribute_enum_int32(self):
        self.patched_library.niFake_SetAttributeViInt32.side_effect = self.side_effects_helper.niFake_SetAttributeViInt32
        enum_value = nifake.Color.RED
        with nifake.Session('dev1') as session:
            session.read_write_color = enum_value
            attribute_id = 1000003
            self.patched_library.niFake_SetAttributeViInt32.assert_called_once_with(matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), matchers.ViStringMatcher(''), matchers.ViInt32Matcher(attribute_id), matchers.ViInt32Matcher(enum_value.value))

    def test_get_attribute_enum_real64(self):
        self.patched_library.niFake_GetAttributeViReal64.side_effect = self.side_effects_helper.niFake_GetAttributeViReal64
        enum_value = nifake.FloatEnum._6_5
        self.side_effects_helper['GetAttributeViReal64']['attributeValue'] = enum_value.value
        with nifake.Session('dev1') as session:
            assert session.float_enum == enum_value
            attribute_id = 1000005
            self.patched_library.niFake_GetAttributeViReal64.assert_called_once_with(matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), matchers.ViStringMatcher(''), matchers.ViInt32Matcher(attribute_id), matchers.ViReal64PointerMatcher())

    def test_set_attribute_enum_real64(self):
        self.patched_library.niFake_SetAttributeViReal64.side_effect = self.side_effects_helper.niFake_SetAttributeViReal64
        enum_value = nifake.FloatEnum._5_5
        with nifake.Session('dev1') as session:
            session.float_enum = enum_value
            attribute_id = 1000005
            self.patched_library.niFake_SetAttributeViReal64.assert_called_once_with(matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), matchers.ViStringMatcher(''), matchers.ViInt32Matcher(attribute_id), matchers.ViReal64Matcher(enum_value.value))

    def test_get_attribute_channel(self):
        self.patched_library.niFake_GetAttributeViInt32.side_effect = self.side_effects_helper.niFake_GetAttributeViInt32
        test_number = 100
        self.side_effects_helper['GetAttributeViInt32']['attributeValue'] = test_number
        with nifake.Session('dev1') as session:
            attr_int = session['0,1'].read_write_integer
            assert(attr_int == test_number)
            self.patched_library.niFake_GetAttributeViInt32.assert_called_once_with(matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), matchers.ViStringMatcher('0,1'), matchers.ViInt32Matcher(1000004), matchers.ViInt32PointerMatcher())

    def test_set_attribute_channel(self):
        self.patched_library.niFake_SetAttributeViReal64.side_effect = self.side_effects_helper.niFake_SetAttributeViReal64
        attribute_id = 1000001
        test_number = 0.001
        with nifake.Session('dev1') as session:
            session['0-24'].read_write_double = test_number
            self.patched_library.niFake_SetAttributeViReal64.assert_called_once_with(matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), matchers.ViStringMatcher('0-24'), matchers.ViInt32Matcher(attribute_id), matchers.ViReal64Matcher(test_number))

    def test_get_attribute_int64(self):
        self.patched_library.niFake_GetAttributeViInt64.side_effect = self.side_effects_helper.niFake_GetAttributeViInt64
        attribute_id = 1000006
        test_number = 6000000000
        self.side_effects_helper['GetAttributeViInt64']['attributeValue'] = test_number
        with nifake.Session('dev1') as session:
            attr_int = session.read_write_int64
            assert(attr_int == test_number)
            self.patched_library.niFake_GetAttributeViInt64.assert_called_once_with(matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), matchers.ViStringMatcher(''), matchers.ViInt32Matcher(attribute_id), matchers.ViInt64PointerMatcher())

    def test_set_attribute_int64(self):
        self.patched_library.niFake_SetAttributeViInt64.side_effect = self.side_effects_helper.niFake_SetAttributeViInt64
        attribute_id = 1000006
        test_number = -6000000000
        with nifake.Session('dev1') as session:
            session.read_write_int64 = test_number
            self.patched_library.niFake_SetAttributeViInt64.assert_called_once_with(matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), matchers.ViStringMatcher(''), matchers.ViInt32Matcher(attribute_id), matchers.ViInt64Matcher(test_number))

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
                self.patched_library.niFake_SetAttributeViReal64.assert_called_once_with(matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), matchers.ViStringMatcher(''), matchers.ViInt32Matcher(1000001), matchers.ViReal64Matcher(-42.0))

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
                session['0'].non_existent_property = 5
                assert False
            except AttributeError as e:
                assert str(e) == "'_RepeatedCapability' object has no attribute 'non_existent_property'"

    def test_add_properties_to_repeated_capability_error_get(self):
        with nifake.Session('dev1') as session:
            try:
                value = session['0'].non_existent_property  # noqa: F841
                assert False
            except AttributeError as e:
                assert str(e) == "'_RepeatedCapability' object has no attribute 'non_existent_property'"

    def test_set_enum_attribute_int32_error(self):
        with nifake.Session('dev1') as session:
            try:
                session.read_write_color = 5
            except TypeError as e:
                assert str(e) == 'must be Color not int'

    def test_set_wrong_enum_attribute_int32_error(self):
        with nifake.Session('dev1') as session:
            try:
                session.read_write_color = nifake.FloatEnum._6_5
            except TypeError as e:
                assert str(e) == 'must be Color not FloatEnum'

    # Error descriptions

    def test_get_error_and_error_message_returns_error(self):
        test_error_code = -42
        self.patched_library.niFake_SimpleFunction.side_effect = self.side_effects_helper.niFake_SimpleFunction
        self.side_effects_helper['SimpleFunction']['return'] = test_error_code
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
        self.patched_library.niFake_SimpleFunction.side_effect = self.side_effects_helper.niFake_SimpleFunction
        self.side_effects_helper['SimpleFunction']['return'] = test_error_code
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
        self.patched_library.niFake_error_message.assert_called_once_with(matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), matchers.ViInt32Matcher(test_error_code), matchers.ViCharBufferMatcher(256))
