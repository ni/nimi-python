import math
import mock_helper
import nifake
import sys
import warnings

from mock import ANY
from mock import patch

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

    # Session management

    def test_init_with_options_and_close(self):
        errors_patcher = patch('nifake.session.errors', spec_set=['handle_error', '_is_error'])
        patched_errors = errors_patcher.start()
        patched_errors._is_error.return_value = 0

        session = nifake.Session('dev1')
        self.patched_library.niFake_InitWithOptions.assert_called_once_with(b'dev1', 0, False, b'', ANY)
        patched_errors.handle_error.assert_called_once_with(session, self.patched_library.niFake_InitWithOptions.return_value, ignore_warnings=False, is_error_handling=False)
        session.close()
        self.patched_library.niFake_close.assert_called_once_with(SESSION_NUM_FOR_TEST)

        errors_patcher.stop()

    def test_init_with_options_nondefault_and_close(self):
        session = nifake.Session('FakeDevice', True, True, 'Some string')
        self.patched_library.niFake_InitWithOptions.assert_called_once_with(b'FakeDevice', True, True, b'Some string', ANY)
        session.close()
        self.patched_library.niFake_close.assert_called_once_with(SESSION_NUM_FOR_TEST)

    def test_close(self):
        session = nifake.Session('dev1')
        session.close()
        self.patched_library.niFake_close.assert_called_once_with(SESSION_NUM_FOR_TEST)

    def test_session_context_manager(self):
        with nifake.Session('dev1') as session:
            assert type(session) == nifake.Session
            self.patched_library.niFake_InitWithOptions.assert_called_once_with(b'dev1', 0, False, b'', ANY)
        self.patched_library.niFake_close.assert_called_once_with(SESSION_NUM_FOR_TEST)

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

    # TODO(marcoskirsch): This should test that when close errors it raises.
    # def test_close_errors(self):

    # TODO(marcoskirsch): This should test that when init errors it raises.
    # def test_session_context_manager_error_on_init

    # TODO(marcoskirsch): This should test that when close errors it logs a warning.
    # def test_session_context_manager_error_on_close

    # Methods

    def test_simple_function(self):
        self.patched_library.niFake_SimpleFunction.side_effect = self.side_effects_helper.niFake_SimpleFunction
        with nifake.Session('dev1') as session:
            session.simple_function()
            self.patched_library.niFake_SimpleFunction.assert_called_once_with(SESSION_NUM_FOR_TEST)

    def test_get_a_number(self):
        test_number = 16
        self.patched_library.niFake_GetANumber.side_effect = self.side_effects_helper.niFake_GetANumber
        self.side_effects_helper['GetANumber']['aNumber'] = test_number
        with nifake.Session('dev1') as session:
            test_result = session.get_a_number()
            assert isinstance(test_result, int)
            assert test_result == test_number
            self.patched_library.niFake_GetANumber.assert_called_once_with(SESSION_NUM_FOR_TEST, ANY)

    def test_one_input_function(self):
        test_number = 1
        self.patched_library.niFake_OneInputFunction.side_effect = self.side_effects_helper.niFake_OneInputFunction
        with nifake.Session('dev1') as session:
            session.one_input_function(test_number)
            self.patched_library.niFake_OneInputFunction.assert_called_once_with(SESSION_NUM_FOR_TEST, test_number)

    def test_vi_int_64_function(self):
        input_value = 1099511627776  # 2^40
        output_value = 2199023255552  # 2^41
        self.patched_library.niFake_Use64BitNumber.side_effect = self.side_effects_helper.niFake_Use64BitNumber
        self.side_effects_helper['Use64BitNumber']['output'] = output_value
        with nifake.Session('dev1') as session:
            assert session.use64_bit_number(input_value) == output_value
            self.patched_library.niFake_Use64BitNumber.assert_called_once_with(SESSION_NUM_FOR_TEST, input_value, ANY)

    def test_two_input_function(self):
        test_number = 1.5
        test_string = 'test'
        self.patched_library.niFake_TwoInputFunction.side_effect = self.side_effects_helper.niFake_TwoInputFunction
        with nifake.Session('dev1') as session:
            session.two_input_function(test_number, test_string)
            if sys.version_info.major < 3:
                self.patched_library.niFake_TwoInputFunction.assert_called_once_with(SESSION_NUM_FOR_TEST, test_number, test_string)
            else:
                self.patched_library.niFake_TwoInputFunction.assert_called_once_with(SESSION_NUM_FOR_TEST, test_number, test_string.encode('ascii'))

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
            self.patched_library.niFake_GetEnumValue.assert_called_once_with(SESSION_NUM_FOR_TEST, ANY, ANY)

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
            self.patched_library.niFake_EnumArrayOutputFunction.assert_called_once_with(SESSION_NUM_FOR_TEST, test_array_size, ANY)

    def test_get_a_boolean(self):
        self.patched_library.niFake_GetABoolean.side_effect = self.side_effects_helper.niFake_GetABoolean
        self.side_effects_helper['GetABoolean']['aBoolean'] = 1
        with nifake.Session('dev1') as session:
            test_result = session.get_a_boolean()
            assert isinstance(test_result, bool)
            assert test_result
            self.patched_library.niFake_GetABoolean.assert_called_once_with(SESSION_NUM_FOR_TEST, ANY)

    def test_get_a_list_booleans(self):
        self.patched_library.niFake_BoolArrayOutputFunction.side_effect = self.side_effects_helper.niFake_BoolArrayOutputFunction
        test_array = [1, 1, 0]
        test_array_size = len(test_array)
        self.side_effects_helper['BoolArrayOutputFunction']['anArray'] = test_array
        with nifake.Session('dev1') as session:
            test_result = session.bool_array_output_function(test_array_size)
            assert test_array_size == len(test_result)
            assert isinstance(test_result[0], bool)
            assert test_result == test_array
            self.patched_library.niFake_BoolArrayOutputFunction.assert_called_once_with(SESSION_NUM_FOR_TEST, test_array_size, ANY)

    def test_acquisition_context_manager(self):
        self.patched_library.niFake_Initiate.side_effect = self.side_effects_helper.niFake_Initiate
        self.patched_library.niFake_Abort.side_effect = self.side_effects_helper.niFake_Abort
        with nifake.Session('dev1') as session:
            with session.initiate():
                self.patched_library.niFake_Initiate.assert_called_once_with(SESSION_NUM_FOR_TEST)
            self.patched_library.niFake_Abort.assert_called_once_with(SESSION_NUM_FOR_TEST)
        self.patched_library.niFake_close.assert_called_once_with(SESSION_NUM_FOR_TEST)

    def test_single_point_read(self):
        test_maximum_time = 10
        test_reading = 5
        self.patched_library.niFake_Read.side_effect = self.side_effects_helper.niFake_Read
        self.side_effects_helper['Read']['reading'] = test_reading
        with nifake.Session('dev1') as session:
            assert test_reading == session.read(test_maximum_time)
            from mock import call
            calls = [call(SESSION_NUM_FOR_TEST, test_maximum_time, ANY)]
            self.patched_library.niFake_Read.assert_has_calls(calls)
            assert self.patched_library.niFake_Read.call_count == 1

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
            calls = [call(SESSION_NUM_FOR_TEST, 0), call(SESSION_NUM_FOR_TEST, 1)]  # 0 is the value of the default of nifake.Turtle.LEONARDO, 1 is the value of nifake.Turtle.DONATELLO
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
            from mock import call
            calls = [call(SESSION_NUM_FOR_TEST, test_maximum_time, len(test_reading_array), ANY, ANY)]
            self.patched_library.niFake_ReadMultiPoint.assert_has_calls(calls)
            assert self.patched_library.niFake_ReadMultiPoint.call_count == 1

    def test_array_input_function(self):
        test_array = [1, 2, 3, 4]
        test_array_size = len(test_array)
        self.patched_library.niFake_ArrayInputFunction.side_effect = self.side_effects_helper.niFake_ArrayInputFunction
        with nifake.Session('dev1') as session:
            session.array_input_function(test_array)
            self.patched_library.niFake_ArrayInputFunction.assert_called_once_with(SESSION_NUM_FOR_TEST, test_array_size, test_array)

    # TODO(marcoskirsch): Other read variations: waveform with ViReal64 and ViInt16 * 3 mechanisms

    # TODO(marcoskirsch):
    # def test_multiple_outputs of different types

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

    def test_invalid_method_call_not_enough_parameters_error(self):
        self.patched_library.niFake_GetAStringWithSpecifiedMaximumSize.side_effect = self.side_effects_helper.niFake_GetAStringWithSpecifiedMaximumSize
        with nifake.Session('dev1') as session:
            try:
                session.get_a_string_with_specified_maximum_size()
                assert False
            except TypeError as e:
                pass

    def test_invalid_method_call_wrong_type_error(self):
        self.patched_library.niFake_GetAStringWithSpecifiedMaximumSize.side_effect = self.side_effects_helper.niFake_GetAStringWithSpecifiedMaximumSize
        with nifake.Session('dev1') as session:
            try:
                session.get_a_string_with_specified_maximum_size('potato')
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

    '''
    # TODO(bhaswath): Enable test once issue 320 is fixed
    def test_read_with_warning(self):
        test_maximum_time = 10
        test_reading = float('nan')
        test_error_code = 42
        test_error_desc = "The answer to the ultimate question, only positive"
        self.patched_library.niFake_Read.side_effect = self.side_effects_helper.niFake_Read
        self.side_effects_helper['Read']['return'] = test_error_code
        self.side_effects_helper['Read']['reading'] = test_reading
        self.patched_library.niFake_GetError.side_effect = self.side_effects_helper.niFake_GetError
        self.side_effects_helper['GetError']['errorCode'] = test_error_code
        self.side_effects_helper['GetError']['description'] = test_error_desc
        with nifake.Session('dev1') as session:
            with warnings.catch_warnings(record=True) as w:
                assert test_reading == session.read(test_maximum_time)
                assert len(w) == 1
                assert issubclass(w[0].category, nifake.NifakeWarning)
                assert test_error_desc in str(w[0].message)
    '''

    # Retrieving buffers and strings

    def test_get_a_string_with_specified_maximum_size(self):
        single_character_string = 'a'
        self.patched_library.niFake_GetAStringWithSpecifiedMaximumSize.side_effect = self.side_effects_helper.niFake_GetAStringWithSpecifiedMaximumSize
        self.side_effects_helper['GetAStringWithSpecifiedMaximumSize']['aString'] = single_character_string
        with nifake.Session('dev1') as session:
            buffer_size = 19
            string_with_specified_buffer = session.get_a_string_with_specified_maximum_size(buffer_size)
            assert(string_with_specified_buffer == single_character_string)
            self.patched_library.niFake_GetAStringWithSpecifiedMaximumSize.assert_called_once_with(SESSION_NUM_FOR_TEST, ANY, ANY)

    def test_get_a_string_of_fixed_maximum_size(self):
        fixed_buffer_string = "this method will return fixed buffer string"
        self.patched_library.niFake_GetAStringOfFixedMaximumSize.side_effect = self.side_effects_helper.niFake_GetAStringOfFixedMaximumSize
        self.side_effects_helper['GetAStringOfFixedMaximumSize']['aString'] = fixed_buffer_string
        with nifake.Session('dev1') as session:
            returned_string = session.get_a_string_of_fixed_maximum_size()
            assert (returned_string == fixed_buffer_string)
            self.patched_library.niFake_GetAStringOfFixedMaximumSize.assert_called_once_with(SESSION_NUM_FOR_TEST, ANY)

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
            self.patched_library.niFake_ReturnANumberAndAString.assert_called_once_with(SESSION_NUM_FOR_TEST, ANY, ANY)

    # TODO(marcoskirsch):
    # def test_get_string_ivi_dance(self)

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

    # Repeated Capabilities

    def test_repeated_capability_method_on_session(self):
        test_maximum_time = 10
        test_reading = 5
        self.patched_library.niFake_ReadFromChannel.side_effect = self.side_effects_helper.niFake_ReadFromChannel
        self.side_effects_helper['ReadFromChannel']['reading'] = test_reading
        with nifake.Session('dev1') as session:
            value = session.read_from_channel(test_maximum_time)
        self.patched_library.niFake_ReadFromChannel.assert_called_once_with(SESSION_NUM_FOR_TEST, b'', test_maximum_time, ANY)
        assert value == test_reading

    def test_repeated_capability_method_on_specific_channel(self):
        test_maximum_time = 10
        test_reading = 5
        self.patched_library.niFake_ReadFromChannel.side_effect = self.side_effects_helper.niFake_ReadFromChannel
        self.side_effects_helper['ReadFromChannel']['reading'] = test_reading
        with nifake.Session('dev1') as session:
            value = session['3'].read_from_channel(test_maximum_time)
        self.patched_library.niFake_ReadFromChannel.assert_called_once_with(SESSION_NUM_FOR_TEST, b'3', test_maximum_time, ANY)
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
            self.patched_library.niFake_GetAttributeViInt32.assert_called_once_with(SESSION_NUM_FOR_TEST, b'', 1000004, ANY)

    def test_set_attribute_int32(self):
        self.patched_library.niFake_SetAttributeViInt32.side_effect = self.side_effects_helper.niFake_SetAttributeViInt32
        attribute_id = 1000004
        test_number = -10
        with nifake.Session('dev1') as session:
            session.read_write_integer = test_number
            self.patched_library.niFake_SetAttributeViInt32.assert_called_once_with(SESSION_NUM_FOR_TEST, b'', attribute_id, test_number)

    def test_get_attribute_real64(self):
        self.patched_library.niFake_GetAttributeViReal64.side_effect = self.side_effects_helper.niFake_GetAttributeViReal64
        test_number = 1.5
        self.side_effects_helper['GetAttributeViReal64']['attributeValue'] = test_number
        with nifake.Session('dev1') as session:
            attr_double = session.read_write_double
            assert attr_double == test_number
            from mock import call
            calls = [call(SESSION_NUM_FOR_TEST, b"", 1000001, ANY)]
            self.patched_library.niFake_GetAttributeViReal64.assert_has_calls(calls)
            assert self.patched_library.niFake_GetAttributeViReal64.call_count == 1

    # TODO(marcoskirsch):
    # def test_set_attribute_real64(self):

    def test_get_attribute_string(self):
        self.patched_library.niFake_GetAttributeViString.side_effect = self.side_effects_helper.niFake_GetAttributeViString
        string = 'Testing is fun?'
        self.side_effects_helper['GetAttributeViString']['attributeValue'] = string
        with nifake.Session('dev1') as session:
            attr_string = session.read_write_string
            assert attr_string == string
            from mock import call
            calls = [call(SESSION_NUM_FOR_TEST, b"", 1000002, 0, None), call(SESSION_NUM_FOR_TEST, b"", 1000002, 15, ANY)]
            self.patched_library.niFake_GetAttributeViString.assert_has_calls(calls)
            assert self.patched_library.niFake_GetAttributeViString.call_count == 2

    def test_set_attribute_string(self):
        self.patched_library.niFake_SetAttributeViString.side_effect = self.side_effects_helper.niFake_SetAttributeViString
        attribute_id = 1000002
        attrib_string = 'This is test string'
        with nifake.Session('dev1') as session:
            session.read_write_string = attrib_string
            self.patched_library.niFake_SetAttributeViString.assert_called_once_with(SESSION_NUM_FOR_TEST, b'', attribute_id, b'This is test string')

    def test_get_attribute_boolean(self):
        self.patched_library.niFake_GetAttributeViBoolean.side_effect = self.side_effects_helper.niFake_GetAttributeViBoolean
        self.side_effects_helper['GetAttributeViBoolean']['attributeValue'] = 1
        with nifake.Session('dev1') as session:
            assert session.read_write_bool
            self.patched_library.niFake_GetAttributeViBoolean.assert_called_once_with(SESSION_NUM_FOR_TEST, b"", 1000000, ANY)

    def test_set_attribute_boolean(self):
        self.patched_library.niFake_SetAttributeViBoolean.side_effect = self.side_effects_helper.niFake_SetAttributeViBoolean
        attribute_id = 1000000
        attrib_bool = True
        with nifake.Session('dev1') as session:
            session.read_write_bool = attrib_bool
            self.patched_library.niFake_SetAttributeViBoolean.assert_called_once_with(SESSION_NUM_FOR_TEST, b'', attribute_id, 1)

    def test_get_attribute_enum_int32(self):
        self.patched_library.niFake_GetAttributeViInt32.side_effect = self.side_effects_helper.niFake_GetAttributeViInt32
        self.side_effects_helper['GetAttributeViInt32']['attributeValue'] = nifake.Color.BLUE.value
        with nifake.Session('dev1') as session:
            assert session.read_write_color == nifake.Color.BLUE
            attribute_id = 1000003
            self.patched_library.niFake_GetAttributeViInt32.assert_called_once_with(SESSION_NUM_FOR_TEST, b'', attribute_id, ANY)

    def test_set_attribute_enum_int32(self):
        self.patched_library.niFake_SetAttributeViInt32.side_effect = self.side_effects_helper.niFake_SetAttributeViInt32
        enum_value = nifake.Color.RED
        with nifake.Session('dev1') as session:
            session.read_write_color = enum_value
            attribute_id = 1000003
            self.patched_library.niFake_SetAttributeViInt32.assert_called_once_with(SESSION_NUM_FOR_TEST, b'', attribute_id, enum_value.value)

    def test_get_attribute_enum_real64(self):
        self.patched_library.niFake_GetAttributeViReal64.side_effect = self.side_effects_helper.niFake_GetAttributeViReal64
        enum_value = nifake.FloatEnum._6_5
        self.side_effects_helper['GetAttributeViReal64']['attributeValue'] = enum_value.value
        with nifake.Session('dev1') as session:
            assert session.float_enum == enum_value
            attribute_id = 1000005
            self.patched_library.niFake_GetAttributeViReal64.assert_called_once_with(SESSION_NUM_FOR_TEST, b'', attribute_id, ANY)

    def test_set_attribute_enum_real64(self):
        self.patched_library.niFake_SetAttributeViReal64.side_effect = self.side_effects_helper.niFake_SetAttributeViReal64
        enum_value = nifake.FloatEnum._5_5
        with nifake.Session('dev1') as session:
            session.float_enum = enum_value
            attribute_id = 1000005
            self.patched_library.niFake_SetAttributeViReal64.assert_called_once_with(SESSION_NUM_FOR_TEST, b'', attribute_id, enum_value.value)

    def test_get_attribute_channel(self):
        self.patched_library.niFake_GetAttributeViInt32.side_effect = self.side_effects_helper.niFake_GetAttributeViInt32
        test_number = 100
        self.side_effects_helper['GetAttributeViInt32']['attributeValue'] = test_number
        with nifake.Session('dev1') as session:
            attr_int = session['0,1'].read_write_integer
            assert(attr_int == test_number)
            self.patched_library.niFake_GetAttributeViInt32.assert_called_once_with(SESSION_NUM_FOR_TEST, b'0,1', 1000004, ANY)

    def test_set_attribute_channel(self):
        self.patched_library.niFake_SetAttributeViReal64.side_effect = self.side_effects_helper.niFake_SetAttributeViReal64
        attribute_id = 1000001
        test_number = 0.001
        with nifake.Session('dev1') as session:
            session['0-24'].read_write_double = test_number
            self.patched_library.niFake_SetAttributeViReal64.assert_called_once_with(SESSION_NUM_FOR_TEST, b'0-24', attribute_id, test_number)

    # TODO(marcoskirsch)
    # def test_get_attribute_int64(self):
    # def test_set_attribute_int64(self):

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
                session.read_write_double = -42
                assert False
            except nifake.Error as e:
                assert e.code == test_error_code
                assert e.description == test_error_desc
                self.patched_library.niFake_SetAttributeViReal64.assert_called_once_with(SESSION_NUM_FOR_TEST, b'', 1000001, -42)

    def test_add_properties_to_session_error(self):
        with nifake.Session('dev1') as session:
            try:
                session.nonexistent_property = 5
                assert False
            except TypeError as e:
                pass
            try:
                value = session.nonexistent_property  # noqa: F841
                assert False
            except AttributeError as e:
                pass

    def test_set_enum_attribute_int32_error(self):
        with nifake.Session('dev1') as session:
            try:
                session.read_write_color = 5
            except TypeError as e:
                assert str(e) == 'must be nifake.Color not int'

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
        from mock import call
        calls = [call(SESSION_NUM_FOR_TEST, test_error_code, ANY)]
        self.patched_library.niFake_error_message.assert_has_calls(calls)
