import array
import ctypes
import math
import nifake
import nifake.errors
import numpy
import warnings

from unittest.mock import call
from unittest.mock import MagicMock
from unittest.mock import patch

import _matchers
import _mock_helper

SESSION_NUM_FOR_TEST = 42


class TestLibraryInterpreter(object):

    class PatchedLibrary(nifake._library.Library):
        def __init__(self, ctypes_library):
            super().__init__(ctypes_library)

            for f in dir(self):
                if f.startswith("niFake_") and not f.endswith("_cfunc"):
                    setattr(self, f, MagicMock())

    def setup_method(self, method):
        self.patched_library = self.PatchedLibrary(None)
        self.patched_library_singleton_get = patch('nifake._library_interpreter._library_singleton.get', return_value=self.patched_library)
        self.patched_library_singleton_get.start()

        self.side_effects_helper = _mock_helper.SideEffectsHelper()
        self.side_effects_helper.set_side_effects_and_return_values(self.patched_library)

        self.get_ctypes_pointer_for_buffer_side_effect_count = 0
        self.get_ctypes_pointer_for_buffer_side_effect_items = []

    def teardown_method(self, method):
        self.patched_library_singleton_get.stop()

    def get_initialized_library_interpreter(self):
        interpreter = nifake._library_interpreter.LibraryInterpreter('windows-1251')
        interpreter._vi = SESSION_NUM_FOR_TEST
        return interpreter

    def niFake_read_warning(self, vi, maximum_time, reading):  # noqa: N802
        reading.contents.value = self.reading
        return self.error_code_return

    def get_ctypes_pointer_for_buffer_side_effect(self, value, library_type=None):
        ret_val = self.get_ctypes_pointer_for_buffer_side_effect_items[self.get_ctypes_pointer_for_buffer_side_effect_count]
        self.get_ctypes_pointer_for_buffer_side_effect_count += 1
        return ret_val

    # Methods

    def test_simple_function(self):
        self.patched_library.niFake_PoorlyNamedSimpleFunction.side_effect = self.side_effects_helper.niFake_PoorlyNamedSimpleFunction
        interpreter = self.get_initialized_library_interpreter()
        interpreter.simple_function()
        self.patched_library.niFake_PoorlyNamedSimpleFunction.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST))

    def test_get_a_number(self):
        test_number = 16
        self.patched_library.niFake_GetANumber.side_effect = self.side_effects_helper.niFake_GetANumber
        self.side_effects_helper['GetANumber']['aNumber'] = test_number
        interpreter = self.get_initialized_library_interpreter()
        test_result = interpreter.get_a_number()
        assert isinstance(test_result, int)
        assert test_result == test_number
        self.patched_library.niFake_GetANumber.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt16PointerMatcher())

    def test_one_input_function(self):
        test_number = 1
        self.patched_library.niFake_OneInputFunction.side_effect = self.side_effects_helper.niFake_OneInputFunction
        interpreter = self.get_initialized_library_interpreter()
        interpreter.one_input_function(test_number)
        self.patched_library.niFake_OneInputFunction.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(test_number))

    def test_vi_int_64_function(self):
        input_value = 2 ** 40
        output_value = 2 ** 41
        self.patched_library.niFake_Use64BitNumber.side_effect = self.side_effects_helper.niFake_Use64BitNumber
        self.side_effects_helper['Use64BitNumber']['output'] = output_value
        interpreter = self.get_initialized_library_interpreter()
        assert interpreter.use64_bit_number(input_value) == output_value
        self.patched_library.niFake_Use64BitNumber.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt64Matcher(input_value), _matchers.ViInt64PointerMatcher())

    def test_two_input_function(self):
        test_number = 1.5
        test_string = 'test'
        self.patched_library.niFake_TwoInputFunction.side_effect = self.side_effects_helper.niFake_TwoInputFunction
        interpreter = self.get_initialized_library_interpreter()
        interpreter.two_input_function(test_number, test_string)
        self.patched_library.niFake_TwoInputFunction.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViReal64Matcher(test_number), _matchers.ViStringMatcher(test_string))

    def test_get_enum_value(self):
        test_number = 1
        test_turtle = nifake.Turtle.LEONARDO
        self.patched_library.niFake_GetEnumValue.side_effect = self.side_effects_helper.niFake_GetEnumValue
        self.side_effects_helper['GetEnumValue']['aQuantity'] = test_number
        self.side_effects_helper['GetEnumValue']['aTurtle'] = 0
        interpreter = self.get_initialized_library_interpreter()
        test_result_number, test_result_enum = interpreter.get_enum_value()
        assert isinstance(test_result_number, int)
        assert test_result_number == test_number
        assert isinstance(test_result_enum, nifake.Turtle)
        assert test_result_enum == test_turtle
        self.patched_library.niFake_GetEnumValue.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32PointerMatcher(), _matchers.ViInt16PointerMatcher())

    def test_get_a_list_enums(self):
        self.patched_library.niFake_EnumArrayOutputFunction.side_effect = self.side_effects_helper.niFake_EnumArrayOutputFunction
        test_list = [1, 1, 0]
        self.side_effects_helper['EnumArrayOutputFunction']['anArray'] = test_list
        interpreter = self.get_initialized_library_interpreter()
        test_result = interpreter.enum_array_output_function(len(test_list))
        assert len(test_list) == len(test_result)
        for expected_value, actual_value in zip(test_list, test_result):
            assert isinstance(actual_value, nifake.Turtle)
            assert actual_value.value == expected_value
        self.patched_library.niFake_EnumArrayOutputFunction.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(test_list)), _matchers.ViInt16BufferMatcher(len(test_list)))

    def test_get_a_boolean(self):
        self.patched_library.niFake_GetABoolean.side_effect = self.side_effects_helper.niFake_GetABoolean
        self.side_effects_helper['GetABoolean']['aBoolean'] = 1
        interpreter = self.get_initialized_library_interpreter()
        test_result = interpreter.get_a_boolean()
        assert isinstance(test_result, bool)
        assert test_result
        self.patched_library.niFake_GetABoolean.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViBooleanPointerMatcher())

    def test_get_a_list_booleans(self):
        self.patched_library.niFake_BoolArrayOutputFunction.side_effect = self.side_effects_helper.niFake_BoolArrayOutputFunction
        test_list = [1, 1, 0]
        self.side_effects_helper['BoolArrayOutputFunction']['anArray'] = test_list
        interpreter = self.get_initialized_library_interpreter()
        test_result = interpreter.bool_array_output_function(len(test_list))
        assert len(test_list) == len(test_result)
        for expected_value, actual_value in zip(test_list, test_result):
            assert isinstance(actual_value, bool)
            assert actual_value == bool(expected_value)
        self.patched_library.niFake_BoolArrayOutputFunction.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(test_list)), _matchers.ViBooleanBufferMatcher(len(test_list)))

    def test_single_point_read_nan(self):
        test_maximum_time_s = 10.0
        test_reading = float('NaN')
        self.patched_library.niFake_Read.side_effect = self.side_effects_helper.niFake_Read
        self.side_effects_helper['Read']['reading'] = test_reading
        interpreter = self.get_initialized_library_interpreter()
        assert math.isnan(interpreter.read(test_maximum_time_s))

    def test_fetch_waveform(self):
        expected_waveform_list = [1.0, 0.1, 42, .42]
        self.patched_library.niFake_FetchWaveform.side_effect = self.side_effects_helper.niFake_FetchWaveform
        self.side_effects_helper['FetchWaveform']['waveformData'] = expected_waveform_list
        self.side_effects_helper['FetchWaveform']['actualNumberOfSamples'] = len(expected_waveform_list)

        # Because we are mocking _get_ctypes_pointer_for_buffer() we don't end up using the array allocated in the function call. Instead, we will allocate the arrays here
        # and have the mock return them. These are the ones that are actually filled in by the function.
        expected_waveform = array.array('d', [0] * len(expected_waveform_list))
        expected_waveform_ctypes = ctypes.cast(expected_waveform.buffer_info()[0], ctypes.POINTER(nifake._visatype.ViReal64 * len(expected_waveform_list)))

        interpreter = self.get_initialized_library_interpreter()
        self.get_ctypes_pointer_for_buffer_side_effect_items = [expected_waveform_ctypes]
        self.get_ctypes_pointer_for_buffer_side_effect_count = 0
        self.patched_library.niFake_WriteWaveform.side_effect = self.side_effects_helper.niFake_WriteWaveform
        with patch('nifake._library_interpreter._get_ctypes_pointer_for_buffer', side_effect=self.get_ctypes_pointer_for_buffer_side_effect):
            # Because we have mocked away _get_ctypes_pointer_for_buffer(), we ignore the return values here and look at our already allocated arrays to make
            # sure they are filled in correctly
            interpreter.fetch_waveform(len(expected_waveform_list))
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
        interpreter = self.get_initialized_library_interpreter()
        waveform = numpy.empty(len(expected_waveform), numpy.float64)
        interpreter.fetch_waveform_into(waveform)
        assert numpy.array_equal(waveform, expected_waveform)
        self.patched_library.niFake_FetchWaveform.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(expected_waveform)), _matchers.ViReal64BufferMatcher(expected_waveform), _matchers.ViInt32PointerMatcher())

    def test_write_waveform(self):
        expected_waveform = [1.1, 2.2, 3.3, 4.4]
        expected_array = array.array('d', expected_waveform)
        interpreter = self.get_initialized_library_interpreter()
        self.get_ctypes_pointer_for_buffer_side_effect_items = [expected_waveform]
        self.get_ctypes_pointer_for_buffer_side_effect_count = 0
        self.patched_library.niFake_WriteWaveform.side_effect = self.side_effects_helper.niFake_WriteWaveform
        with patch('nifake._library_interpreter._get_ctypes_pointer_for_buffer', side_effect=self.get_ctypes_pointer_for_buffer_side_effect):
            interpreter.write_waveform(expected_array)
        self.patched_library.niFake_WriteWaveform.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(expected_waveform)), _matchers.ViReal64BufferMatcher(expected_array))

    def test_write_waveform_numpy(self):
        expected_waveform = numpy.array([1.1, 2.2, 3.3, 4.4], order='C')
        self.patched_library.niFake_WriteWaveform.side_effect = self.side_effects_helper.niFake_WriteWaveform
        interpreter = self.get_initialized_library_interpreter()
        interpreter.write_waveform_numpy(expected_waveform)
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
        interpreter = self.get_initialized_library_interpreter()
        result_boolean, result_int32, result_int64, result_enum, result_float, result_float_enum, result_array, result_string = interpreter.return_multiple_types(array_size)
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
        interpreter = self.get_initialized_library_interpreter()
        output_array, output_array_of_fixed_length = interpreter.multiple_array_types(output_array_size, input_array_of_floats, input_array_of_integers)
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
        interpreter = self.get_initialized_library_interpreter()
        output_array, output_array_of_fixed_length = interpreter.multiple_array_types(output_array_size, input_array_of_floats, None)
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
        interpreter = self.get_initialized_library_interpreter()
        interpreter.multiple_arrays_same_size(input_array_of_floats1, input_array_of_floats2, input_array_of_floats3, input_array_of_floats4)
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
        interpreter = self.get_initialized_library_interpreter()
        interpreter.multiple_arrays_same_size(input_array_of_floats1, None, None, None)
        self.patched_library.niFake_MultipleArraysSameSize.assert_called_once_with(
            _matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST),
            _matchers.ViReal64BufferMatcher(input_array_of_floats1),
            None,
            None,
            None,
            _matchers.ViInt32Matcher(len(input_array_of_floats1)),
        )

    def test_parameters_are_multiple_types(self):
        self.patched_library.niFake_ParametersAreMultipleTypes.side_effect = self.side_effects_helper.niFake_ParametersAreMultipleTypes
        boolean_val = True
        int32_val = 32
        int64_val = 6000000000
        enum_val = nifake.Turtle.LEONARDO
        float_val = 1.23
        float_enum_val = nifake.FloatEnum.SIX_POINT_FIVE
        string_val = 'Testing is fun?'
        interpreter = self.get_initialized_library_interpreter()
        interpreter.parameters_are_multiple_types(boolean_val, int32_val, int64_val, enum_val, float_val, float_enum_val, string_val)
        self.patched_library.niFake_ParametersAreMultipleTypes.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViBooleanMatcher(boolean_val), _matchers.ViInt32Matcher(int32_val), _matchers.ViInt64Matcher(int64_val), _matchers.ViInt16Matcher(enum_val.value), _matchers.ViReal64Matcher(float_val), _matchers.ViReal64Matcher(float_enum_val.value), _matchers.ViStringMatcher(string_val))

    def test_method_with_error(self):
        test_error_code = -42
        test_error_desc = "The answer to the ultimate question"
        self.patched_library.niFake_PoorlyNamedSimpleFunction.side_effect = self.side_effects_helper.niFake_PoorlyNamedSimpleFunction
        self.side_effects_helper['PoorlyNamedSimpleFunction']['return'] = test_error_code
        self.patched_library.niFake_GetError.side_effect = self.side_effects_helper.niFake_GetError
        self.side_effects_helper['GetError']['errorCode'] = test_error_code
        self.side_effects_helper['GetError']['description'] = test_error_desc
        interpreter = self.get_initialized_library_interpreter()
        try:
            interpreter.simple_function()
            assert False
        except nifake.Error as e:
            assert e.code == test_error_code
            assert e.description == test_error_desc

    def test_call_not_enough_parameters_error(self):
        interpreter = self.get_initialized_library_interpreter()
        try:
            interpreter.multiple_array_types(10)
            assert False
        except TypeError:
            pass

    def test_invalid_method_call_wrong_type_error(self):
        interpreter = self.get_initialized_library_interpreter()
        try:
            interpreter.multiple_array_types('potato', [0.0, 0.1, 0.2])
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
        interpreter = self.get_initialized_library_interpreter()
        with warnings.catch_warnings(record=True) as w:
            interpreter.simple_function()
            assert len(w) == 1
            assert issubclass(w[0].category, nifake.DriverWarning)
            assert test_error_desc in str(w[0].message)
            assert f'Warning {test_error_code} occurred.' in str(w[0].message)

    def test_read_with_warning(self):
        # We want to capture all of our warnings, not just the first one
        warnings.filterwarnings("always", category=nifake.DriverWarning)

        test_maximum_time_s = 10.0
        test_reading = float('nan')
        test_error_code = 42
        test_error_desc = "The answer to the ultimate question, only positive"
        self.patched_library.niFake_Read.side_effect = self.niFake_read_warning
        self.error_code_return = test_error_code
        self.reading = test_reading
        self.patched_library.niFake_GetError.side_effect = self.side_effects_helper.niFake_GetError
        self.side_effects_helper['GetError']['errorCode'] = test_error_code
        self.side_effects_helper['GetError']['description'] = test_error_desc
        interpreter = self.get_initialized_library_interpreter()
        with warnings.catch_warnings(record=True) as w:
            assert math.isnan(interpreter.read(test_maximum_time_s))
            assert len(w) == 1
            assert issubclass(w[0].category, nifake.DriverWarning)
            assert test_error_desc in str(w[0].message)
            assert f'Warning {test_error_code} occurred.' in str(w[0].message)

    def test_library_interpreter_always_uses_same_library_instance(self):
        interpreter1 = nifake._library_interpreter.LibraryInterpreter('windows-1251')
        interpreter2 = nifake._library_interpreter.LibraryInterpreter('windows-1251')
        assert interpreter1 is not interpreter2
        assert interpreter1._library is interpreter2._library

    def test_set_runtime_environment_is_called_if_present(self):
        self.patched_library_singleton_get.stop()
        self.patched_library_singleton_lib = patch('nifake._library.Library', return_value=self.patched_library)
        self.patched_library.niFake_SetRuntimeEnvironment.side_effect = self.side_effects_helper.niFake_SetRuntimeEnvironment
        self.patched_library_singleton_lib.start()
        self.get_initialized_library_interpreter()
        self.patched_library.niFake_SetRuntimeEnvironment.assert_called_once()
        self.patched_library_singleton_lib.stop()
        self.patched_library_singleton_get.start()

    def test_set_runtime_environment_not_present_in_driver_runtime(self):

        class TypesLibrary:
            item = ""

        self.patched_library_singleton_get.stop()
        self.patched_library = self.PatchedLibrary(TypesLibrary)
        self.patched_library_singleton_lib = patch('nifake._library.Library', return_value=self.patched_library)
        self.patched_library_singleton_lib.start()
        try:
            # Call _get_library_function directly so that exception is not caught in _library_singleton get
            self.get_initialized_library_interpreter()._library._get_library_function('niFake_SetRuntimeEnvironment')
            assert False
        except nifake.errors.DriverTooOldError:
            pass
        nifake._library_singleton._instance = None
        self.get_initialized_library_interpreter()

        self.patched_library_singleton_lib.stop()
        self.patched_library_singleton_get.start()

    def test_set_runtime_environment_not_defined(self):
        self.patched_library_singleton_get.stop()
        delattr(self.patched_library, 'niFake_SetRuntimeEnvironment')
        self.patched_library_singleton_lib = patch('nifake._library.Library', return_value=self.patched_library)
        self.patched_library_singleton_lib.start()
        nifake._library_singleton._instance = None
        interpreter = self.get_initialized_library_interpreter()
        try:
            interpreter._library.niFake_SetRuntimeEnvironment('', '', '', '')
            assert False
        except nifake.errors.DriverTooOldError:
            pass
        nifake._library_singleton._instance = None
        self.get_initialized_library_interpreter()

        self.patched_library_singleton_lib.stop()
        self.patched_library_singleton_get.start()

    # Retrieving buffers and strings

    def test_get_a_string_of_fixed_maximum_size(self):
        test_string = "A string no larger than the max size of 256 allowed by the function."
        self.patched_library.niFake_GetAStringOfFixedMaximumSize.side_effect = self.side_effects_helper.niFake_GetAStringOfFixedMaximumSize
        self.side_effects_helper['GetAStringOfFixedMaximumSize']['aString'] = test_string
        interpreter = self.get_initialized_library_interpreter()
        returned_string = interpreter.get_a_string_of_fixed_maximum_size()
        assert returned_string == test_string
        self.patched_library.niFake_GetAStringOfFixedMaximumSize.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViCharBufferMatcher(256))

    def test_get_a_string_of_size_python_code(self):
        test_size = 4
        expected_string_size = test_size - 1
        test_string = "A string that is larger than test_size."
        expected_string = test_string[:expected_string_size]
        self.patched_library.niFake_GetAStringUsingPythonCode.side_effect = self.side_effects_helper.niFake_GetAStringUsingPythonCode
        self.side_effects_helper['GetAStringUsingPythonCode']['aString'] = expected_string
        interpreter = self.get_initialized_library_interpreter()
        returned_string = interpreter.get_a_string_using_python_code(test_size)
        assert returned_string == expected_string
        self.patched_library.niFake_GetAStringUsingPythonCode.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt16Matcher(test_size), _matchers.ViCharBufferMatcher(test_size))

    def test_return_a_number_and_a_string(self):
        test_string = "this string"
        test_number = 13
        self.patched_library.niFake_ReturnANumberAndAString.side_effect = self.side_effects_helper.niFake_ReturnANumberAndAString
        self.side_effects_helper['ReturnANumberAndAString']['aString'] = test_string
        self.side_effects_helper['ReturnANumberAndAString']['aNumber'] = test_number
        interpreter = self.get_initialized_library_interpreter()
        returned_number, returned_string = interpreter.return_a_number_and_a_string()
        assert (returned_string == test_string)
        assert (returned_number == test_number)
        self.patched_library.niFake_ReturnANumberAndAString.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt16PointerMatcher(), _matchers.ViCharBufferMatcher(256))

    def test_get_an_ivi_dance_char_array(self):
        self.patched_library.niFake_GetAnIviDanceCharArray.side_effect = self.side_effects_helper.niFake_GetAnIviDanceCharArray
        string_val = 'Testing is fun?'
        self.side_effects_helper['GetAnIviDanceCharArray']['charArray'] = string_val
        interpreter = self.get_initialized_library_interpreter()
        result_string = interpreter.get_an_ivi_dance_char_array()
        assert result_string == string_val
        calls = [
            call(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(0), None),
            call(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(string_val)), _matchers.ViCharBufferMatcher(len(string_val)))
        ]
        self.patched_library.niFake_GetAnIviDanceCharArray.assert_has_calls(calls)
        assert self.patched_library.niFake_GetAnIviDanceCharArray.call_count == 2

    def test_get_string_ivi_dance_error(self):
        read_write_string_attribute_id = 1000002
        test_error_code = -1234
        test_error_desc = "ascending order"
        self.patched_library.niFake_GetAttributeViString.side_effect = self.side_effects_helper.niFake_GetAttributeViString
        self.side_effects_helper['GetAttributeViString']['attributeValue'] = 'Testing is fun?'
        self.side_effects_helper['GetAttributeViString']['return'] = test_error_code
        self.patched_library.niFake_GetError.side_effect = self.side_effects_helper.niFake_GetError
        self.side_effects_helper['GetError']['errorCode'] = test_error_code
        self.side_effects_helper['GetError']['description'] = test_error_desc
        interpreter = self.get_initialized_library_interpreter()
        try:
            interpreter.get_attribute_vi_string('', read_write_string_attribute_id)
            assert False
        except nifake.Error as e:
            assert e.code == test_error_code
            assert e.description == test_error_desc

    def test_get_an_ivi_dance_with_a_twist_string(self):
        self.patched_library.niFake_GetAnIviDanceWithATwistString.side_effect = self.side_effects_helper.niFake_GetAnIviDanceWithATwistString
        string_val = 'Testing is fun?'
        self.side_effects_helper['GetAnIviDanceWithATwistString']['aString'] = string_val
        self.side_effects_helper['GetAnIviDanceWithATwistString']['actualSize'] = len(string_val)
        interpreter = self.get_initialized_library_interpreter()
        result_string = interpreter.get_an_ivi_dance_with_a_twist_string()
        assert result_string == string_val
        calls = [
            call(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(0), None, _matchers.ViInt32PointerMatcher()),
            call(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(string_val)), _matchers.ViCharBufferMatcher(len(string_val)), _matchers.ViInt32PointerMatcher())
        ]
        self.patched_library.niFake_GetAnIviDanceWithATwistString.assert_has_calls(calls)
        assert self.patched_library.niFake_GetAnIviDanceWithATwistString.call_count == 2

    def test_get_array_using_ivi_dance(self):
        self.patched_library.niFake_GetArrayUsingIviDance.side_effect = self.side_effects_helper.niFake_GetArrayUsingIviDance
        self.side_effects_helper['GetArrayUsingIviDance']['arrayOut'] = [1.1, 2.2]
        interpreter = self.get_initialized_library_interpreter()
        result_array = interpreter.get_array_using_ivi_dance()
        assert result_array == [1.1, 2.2]

    # Attributes

    def test_get_attribute_int32(self):
        self.patched_library.niFake_GetAttributeViInt32.side_effect = self.side_effects_helper.niFake_GetAttributeViInt32
        attribute_id = 1000004
        test_number = 3
        self.side_effects_helper['GetAttributeViInt32']['attributeValue'] = test_number
        interpreter = self.get_initialized_library_interpreter()
        attr_int = interpreter.get_attribute_vi_int32('', attribute_id)
        assert(attr_int == test_number)
        self.patched_library.niFake_GetAttributeViInt32.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViInt32PointerMatcher())

    def test_set_attribute_int32(self):
        self.patched_library.niFake_SetAttributeViInt32.side_effect = self.side_effects_helper.niFake_SetAttributeViInt32
        attribute_id = 1000004
        test_number = -10
        interpreter = self.get_initialized_library_interpreter()
        interpreter.set_attribute_vi_int32('', attribute_id, test_number)
        self.patched_library.niFake_SetAttributeViInt32.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViInt32Matcher(test_number))

    def test_get_attribute_real64(self):
        self.patched_library.niFake_GetAttributeViReal64.side_effect = self.side_effects_helper.niFake_GetAttributeViReal64
        attribute_id = 1000001
        test_number = 1.5
        self.side_effects_helper['GetAttributeViReal64']['attributeValue'] = test_number
        interpreter = self.get_initialized_library_interpreter()
        attr_double = interpreter.get_attribute_vi_real64('', attribute_id)
        assert attr_double == test_number
        self.patched_library.niFake_GetAttributeViReal64.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViReal64PointerMatcher())

    def test_set_attribute_real64(self):
        self.patched_library.niFake_SetAttributeViReal64.side_effect = self.side_effects_helper.niFake_SetAttributeViReal64
        attribute_id = 1000001
        test_number = 10.1
        interpreter = self.get_initialized_library_interpreter()
        interpreter.set_attribute_vi_real64('', attribute_id, test_number)
        self.patched_library.niFake_SetAttributeViReal64.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViReal64Matcher(test_number))

    def test_get_attribute_string(self):
        self.patched_library.niFake_GetAttributeViString.side_effect = self.side_effects_helper.niFake_GetAttributeViString
        attribute_id = 1000002
        string = 'Testing is fun?'
        self.side_effects_helper['GetAttributeViString']['attributeValue'] = string
        interpreter = self.get_initialized_library_interpreter()
        attr_string = interpreter.get_attribute_vi_string('', attribute_id)
        assert attr_string == string
        calls = [
            call(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(1000002), _matchers.ViInt32Matcher(0), None),
            call(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViInt32Matcher(15), _matchers.ViCharBufferMatcher(len(string)))
        ]
        self.patched_library.niFake_GetAttributeViString.assert_has_calls(calls)
        assert self.patched_library.niFake_GetAttributeViString.call_count == 2

    def test_set_attribute_string(self):
        self.patched_library.niFake_SetAttributeViString.side_effect = self.side_effects_helper.niFake_SetAttributeViString
        attribute_id = 1000002
        attrib_string = 'This is test string'
        interpreter = self.get_initialized_library_interpreter()
        interpreter.set_attribute_vi_string('', attribute_id, attrib_string)
        self.patched_library.niFake_SetAttributeViString.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViStringMatcher('This is test string'))

    def test_get_attribute_boolean(self):
        self.patched_library.niFake_GetAttributeViBoolean.side_effect = self.side_effects_helper.niFake_GetAttributeViBoolean
        attribute_id = 1000000
        self.side_effects_helper['GetAttributeViBoolean']['attributeValue'] = 1
        interpreter = self.get_initialized_library_interpreter()
        assert interpreter.get_attribute_vi_boolean('', attribute_id)
        self.patched_library.niFake_GetAttributeViBoolean.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViBooleanPointerMatcher())

    def test_set_attribute_boolean(self):
        self.patched_library.niFake_SetAttributeViBoolean.side_effect = self.side_effects_helper.niFake_SetAttributeViBoolean
        attribute_id = 1000000
        attrib_bool = True
        interpreter = self.get_initialized_library_interpreter()
        interpreter.set_attribute_vi_boolean('', attribute_id, attrib_bool)
        self.patched_library.niFake_SetAttributeViBoolean.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViBooleanMatcher(True))

    def test_get_attribute_int64(self):
        self.patched_library.niFake_GetAttributeViInt64.side_effect = self.side_effects_helper.niFake_GetAttributeViInt64
        attribute_id = 1000006
        test_number = 6000000000
        self.side_effects_helper['GetAttributeViInt64']['attributeValue'] = test_number
        interpreter = self.get_initialized_library_interpreter()
        attr_int = interpreter.get_attribute_vi_int64('', attribute_id)
        assert(attr_int == test_number)
        self.patched_library.niFake_GetAttributeViInt64.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViInt64PointerMatcher())

    def test_set_attribute_int64(self):
        self.patched_library.niFake_SetAttributeViInt64.side_effect = self.side_effects_helper.niFake_SetAttributeViInt64
        attribute_id = 1000006
        test_number = -6000000000
        interpreter = self.get_initialized_library_interpreter()
        interpreter.set_attribute_vi_int64('', attribute_id, test_number)
        self.patched_library.niFake_SetAttributeViInt64.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViInt64Matcher(test_number))

    # Error descriptions

    def test_get_error_returns_mismatched_error_code(self):
        test_error_code = -42
        test_error_desc = "The answer to the ultimate question, only positive"
        wrong_error_code = 54
        wrong_error_desc = "What is six times nine"
        self.patched_library.niFake_PoorlyNamedSimpleFunction.side_effect = self.side_effects_helper.niFake_PoorlyNamedSimpleFunction
        self.side_effects_helper['PoorlyNamedSimpleFunction']['return'] = test_error_code
        self.patched_library.niFake_GetError.side_effect = self.side_effects_helper.niFake_GetError
        self.side_effects_helper['GetError']['errorCode'] = wrong_error_code
        self.side_effects_helper['GetError']['description'] = wrong_error_desc
        self.patched_library.niFake_error_message.side_effect = self.side_effects_helper.niFake_error_message
        self.side_effects_helper['error_message']['errorMessage'] = test_error_desc
        interpreter = self.get_initialized_library_interpreter()
        try:
            interpreter.simple_function()
            assert False
        except nifake.Error as e:
            assert e.code == test_error_code
            assert e.description == test_error_desc
        self.patched_library.niFake_PoorlyNamedSimpleFunction.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST))
        self.patched_library.niFake_error_message.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(test_error_code), _matchers.ViCharBufferMatcher(256))

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
        interpreter = self.get_initialized_library_interpreter()
        try:
            interpreter.simple_function()
            assert False
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
        interpreter = self.get_initialized_library_interpreter()
        try:
            interpreter.simple_function()
            assert False
        except nifake.Error as e:
            assert e.code == test_error_code
            assert e.description == test_error_desc
        self.patched_library.niFake_error_message.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(test_error_code), _matchers.ViCharBufferMatcher(256))

    # Custom types

    def test_set_custom_type(self):
        self.patched_library.niFake_SetCustomType.side_effect = self.side_effects_helper.niFake_SetCustomType
        cs = nifake.CustomStruct(struct_int=42, struct_double=4.2)
        interpreter = self.get_initialized_library_interpreter()
        interpreter.set_custom_type(cs)
        self.patched_library.niFake_SetCustomType.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.CustomTypeMatcher(nifake.struct_CustomStruct, nifake.struct_CustomStruct(cs)))

    def test_get_custom_type(self):
        self.patched_library.niFake_GetCustomType.side_effect = self.side_effects_helper.niFake_GetCustomType
        cs_ctype = nifake.struct_CustomStruct(struct_int=42, struct_double=4.2)
        self.side_effects_helper['GetCustomType']['cs'] = cs_ctype
        interpreter = self.get_initialized_library_interpreter()
        cs = interpreter.get_custom_type()
        assert cs.struct_int == cs_ctype.struct_int
        assert cs.struct_double == cs_ctype.struct_double

    def test_set_custom_type_array(self):
        self.patched_library.niFake_SetCustomTypeArray.side_effect = self.side_effects_helper.niFake_SetCustomTypeArray
        cs = [nifake.CustomStruct(struct_int=42, struct_double=4.2), nifake.CustomStruct(struct_int=43, struct_double=4.3), nifake.CustomStruct(struct_int=42, struct_double=4.3)]
        cs_ctype = (nifake.struct_CustomStruct * len(cs))(*[nifake.struct_CustomStruct(c) for c in cs])
        interpreter = self.get_initialized_library_interpreter()
        interpreter.set_custom_type_array(cs)
        self.patched_library.niFake_SetCustomTypeArray.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(cs)), _matchers.CustomTypeBufferMatcher(nifake.struct_CustomStruct, cs_ctype))

    def test_get_custom_type_array(self):
        self.patched_library.niFake_GetCustomTypeArray.side_effect = self.side_effects_helper.niFake_GetCustomTypeArray
        cs = [nifake.CustomStruct(struct_int=42, struct_double=4.2), nifake.CustomStruct(struct_int=43, struct_double=4.3), nifake.CustomStruct(struct_int=42, struct_double=4.3)]
        cs_ctype = (nifake.struct_CustomStruct * len(cs))(*[nifake.struct_CustomStruct(c) for c in cs])
        self.side_effects_helper['GetCustomTypeArray']['cs'] = cs_ctype
        interpreter = self.get_initialized_library_interpreter()
        cs_test = interpreter.get_custom_type_array(len(cs_ctype))
        assert len(cs_test) == len(cs_ctype)
        for actual, expected in zip(cs_test, cs):
            assert actual.struct_int == expected.struct_int
            assert actual.struct_double == expected.struct_double

    def test_get_custom_type_typedef(self):
        self.patched_library.niFake_GetCustomTypeTypedef.side_effect = self.side_effects_helper.niFake_GetCustomTypeTypedef
        cst = nifake.CustomStructTypedef(struct_int=42, struct_double=4.2)
        cst_ctype = nifake.struct_CustomStructTypedef(cst)
        csnt = nifake.CustomStructNestedTypedef(
            struct_custom_struct=nifake.CustomStruct(struct_int=43, struct_double=4.3),
            struct_custom_struct_typedef=nifake.CustomStructTypedef(struct_int=44, struct_double=4.4)
        )
        csnt_ctype = nifake.struct_CustomStructNestedTypedef(csnt)
        self.side_effects_helper['GetCustomTypeTypedef']['cst'] = cst_ctype
        self.side_effects_helper['GetCustomTypeTypedef']['csnt'] = csnt_ctype
        interpreter = self.get_initialized_library_interpreter()
        cst_test, csnt_test = interpreter.get_custom_type_typedef()
        assert cst_test.struct_int == cst.struct_int
        assert cst_test.struct_double == cst.struct_double
        assert csnt_test.struct_custom_struct.struct_int == csnt.struct_custom_struct.struct_int
        assert csnt_test.struct_custom_struct.struct_double == csnt.struct_custom_struct.struct_double
        assert csnt_test.struct_custom_struct_typedef.struct_int == csnt.struct_custom_struct_typedef.struct_int
        assert csnt_test.struct_custom_struct_typedef.struct_double == csnt.struct_custom_struct_typedef.struct_double

    # python-code size mechanism

    def test_get_array_using_python_code_double(self):
        import nifake._visatype
        self.patched_library.niFake_GetArraySizeForPythonCode.side_effect = self.side_effects_helper.niFake_GetArraySizeForPythonCode
        self.patched_library.niFake_GetArrayForPythonCodeDouble.side_effect = self.side_effects_helper.niFake_GetArrayForPythonCodeDouble
        array_out = [42.0, 43.0, 44.0]
        array_out_ctype = (nifake._visatype.ViReal64 * len(array_out))(*array_out)
        self.side_effects_helper['GetArraySizeForPythonCode']['sizeOut'] = len(array_out)
        self.side_effects_helper['GetArrayForPythonCodeDouble']['arrayOut'] = array_out_ctype
        interpreter = self.get_initialized_library_interpreter()
        array_out_test = interpreter.get_array_for_python_code_double()
        assert len(array_out_test) == len(array_out)
        for actual, expected in zip(array_out_test, array_out):
            assert actual == expected

    def test_get_array_using_python_code_custom_type(self):
        import nifake._visatype
        self.patched_library.niFake_GetArraySizeForPythonCode.side_effect = self.side_effects_helper.niFake_GetArraySizeForPythonCode
        self.patched_library.niFake_GetArrayForPythonCodeCustomType.side_effect = self.side_effects_helper.niFake_GetArrayForPythonCodeCustomType
        cs = [nifake.CustomStruct(struct_int=42, struct_double=4.2), nifake.CustomStruct(struct_int=43, struct_double=4.3), nifake.CustomStruct(struct_int=42, struct_double=4.3)]
        cs_ctype = (nifake.struct_CustomStruct * len(cs))(*[nifake.struct_CustomStruct(c) for c in cs])
        self.side_effects_helper['GetArraySizeForPythonCode']['sizeOut'] = len(cs)
        self.side_effects_helper['GetArrayForPythonCodeCustomType']['arrayOut'] = cs_ctype
        interpreter = self.get_initialized_library_interpreter()
        cs_test = interpreter.get_array_for_python_code_custom_type()
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
        self.side_effects_helper['GetCalDateAndTime']['month'] = month
        self.side_effects_helper['GetCalDateAndTime']['day'] = day
        self.side_effects_helper['GetCalDateAndTime']['year'] = year
        self.side_effects_helper['GetCalDateAndTime']['hour'] = hour
        self.side_effects_helper['GetCalDateAndTime']['minute'] = minute
        interpreter = self.get_initialized_library_interpreter()
        last_cal = interpreter.get_cal_date_and_time(0)
        assert (month, day, year, hour, minute) == last_cal

    # Import/Export functions

    def test_import_attribute_configuration_buffer_list_i8(self):
        self.patched_library.niFake_ImportAttributeConfigurationBuffer.side_effect = self.side_effects_helper.niFake_ImportAttributeConfigurationBuffer
        expected_list = [ord('a'), ord('b'), ord('c'), ord('d')]
        configuration = expected_list
        interpreter = self.get_initialized_library_interpreter()
        self.get_ctypes_pointer_for_buffer_side_effect_items = [expected_list]
        self.get_ctypes_pointer_for_buffer_side_effect_count = 0
        with patch('nifake._library_interpreter._get_ctypes_pointer_for_buffer', side_effect=self.get_ctypes_pointer_for_buffer_side_effect):
            interpreter.import_attribute_configuration_buffer(configuration)
        self.patched_library.niFake_ImportAttributeConfigurationBuffer.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(configuration)), _matchers.ViInt8BufferMatcher(expected_list))

    def test_import_attribute_configuration_buffer_bytes(self):
        self.patched_library.niFake_ImportAttributeConfigurationBuffer.side_effect = self.side_effects_helper.niFake_ImportAttributeConfigurationBuffer
        expected_list = [ord('a'), ord('b'), ord('c'), ord('d')]
        configuration = b'abcd'
        interpreter = self.get_initialized_library_interpreter()
        self.get_ctypes_pointer_for_buffer_side_effect_items = [expected_list]
        self.get_ctypes_pointer_for_buffer_side_effect_count = 0
        with patch('nifake._library_interpreter._get_ctypes_pointer_for_buffer', side_effect=self.get_ctypes_pointer_for_buffer_side_effect):
            interpreter.import_attribute_configuration_buffer(configuration)
        self.patched_library.niFake_ImportAttributeConfigurationBuffer.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(configuration)), _matchers.ViInt8BufferMatcher(expected_list))

    def test_import_attribute_configuration_buffer_bytearray(self):
        self.patched_library.niFake_ImportAttributeConfigurationBuffer.side_effect = self.side_effects_helper.niFake_ImportAttributeConfigurationBuffer
        expected_list = [ord('a'), ord('b'), ord('c'), ord('d')]
        configuration = bytearray(b'abcd')
        interpreter = self.get_initialized_library_interpreter()
        self.get_ctypes_pointer_for_buffer_side_effect_items = [expected_list]
        self.get_ctypes_pointer_for_buffer_side_effect_count = 0
        with patch('nifake._library_interpreter._get_ctypes_pointer_for_buffer', side_effect=self.get_ctypes_pointer_for_buffer_side_effect):
            interpreter.import_attribute_configuration_buffer(configuration)
        self.patched_library.niFake_ImportAttributeConfigurationBuffer.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(configuration)), _matchers.ViInt8BufferMatcher(expected_list))

    def test_import_attribute_configuration_buffer_array_bytes(self):
        self.patched_library.niFake_ImportAttributeConfigurationBuffer.side_effect = self.side_effects_helper.niFake_ImportAttributeConfigurationBuffer
        expected_list = [ord('a'), ord('b'), ord('c'), ord('d')]
        configuration = array.array('b', b'abcd')
        interpreter = self.get_initialized_library_interpreter()
        self.get_ctypes_pointer_for_buffer_side_effect_items = [expected_list]
        self.get_ctypes_pointer_for_buffer_side_effect_count = 0
        with patch('nifake._library_interpreter._get_ctypes_pointer_for_buffer', side_effect=self.get_ctypes_pointer_for_buffer_side_effect):
            interpreter.import_attribute_configuration_buffer(configuration)
        self.patched_library.niFake_ImportAttributeConfigurationBuffer.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(configuration)), _matchers.ViInt8BufferMatcher(expected_list))

    def test_import_attribute_configuration_buffer_str(self):
        self.patched_library.niFake_ImportAttributeConfigurationBuffer.side_effect = self.side_effects_helper.niFake_ImportAttributeConfigurationBuffer
        expected_list = [ord('a'), ord('b'), ord('c'), ord('d')]
        configuration = 'abcd'
        interpreter = self.get_initialized_library_interpreter()
        self.get_ctypes_pointer_for_buffer_side_effect_items = [expected_list]
        self.get_ctypes_pointer_for_buffer_side_effect_count = 0
        with patch('nifake._library_interpreter._get_ctypes_pointer_for_buffer', side_effect=self.get_ctypes_pointer_for_buffer_side_effect):
            interpreter.import_attribute_configuration_buffer(configuration)
        self.patched_library.niFake_ImportAttributeConfigurationBuffer.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(configuration)), _matchers.ViInt8BufferMatcher(expected_list))

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
