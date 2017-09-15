import mock_helper
import nifake
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

    def test_init_with_options(self):
        errors_patcher = patch('nifake.session.errors', spec_set=['handle_error', '_is_error'])
        patched_errors = errors_patcher.start()
        patched_errors._is_error.return_value = 0

        self.patched_library.niFake_close.side_effect = self.disallow_close
        session = nifake.Session('dev1')
        assert(session.vi == SESSION_NUM_FOR_TEST)
        self.patched_library.niFake_InitWithOptions.assert_called_once_with(b'dev1', 0, False, b'', ANY)
        patched_errors.handle_error.assert_called_once_with(session, self.patched_library.niFake_InitWithOptions.return_value, ignore_warnings=False, is_error_handling=False)

        errors_patcher.stop()

    def test_close(self):
        session = nifake.Session('dev1')
        session.close()
        self.patched_library.niFake_close.assert_called_once_with(SESSION_NUM_FOR_TEST)

    def test_session_context_manager(self):
        with nifake.Session('dev1') as session:
            assert(session.vi == SESSION_NUM_FOR_TEST)
            self.patched_library.niFake_InitWithOptions.assert_called_once_with(b'dev1', 0, False, b'', ANY)
        self.patched_library.niFake_close.assert_called_once_with(SESSION_NUM_FOR_TEST)

    def test_get_error_description_get_error(self):
        test_error_code = -42
        test_error_desc = "The answer to the ultimate question"
        self.patched_library.niFake_GetError.side_effect = self.side_effects_helper.niFake_GetError
        self.side_effects_helper['GetError']['errorCode'] = test_error_code
        self.side_effects_helper['GetError']['description'] = test_error_desc
        with nifake.Session('dev1') as session:
            error_desc = session.get_error_description(test_error_code)
            assert error_desc == test_error_desc

    def test_simple_function(self):
        self.patched_library.niFake_SimpleFunction.side_effect = self.side_effects_helper.niFake_SimpleFunction
        with nifake.Session('dev1') as session:
            session.simple_function()
            self.patched_library.niFake_SimpleFunction.assert_called_once_with(SESSION_NUM_FOR_TEST)

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

    def test_ivi_dance_with_error(self):
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
                session._get_attribute_vi_string("", 5)
                assert False
            except nifake.Error as e:
                assert e.code == test_error_code
                assert e.description == test_error_desc

    def test_get_string_attribute_private(self):
        self.patched_library.niFake_GetAttributeViString.side_effect = self.side_effects_helper.niFake_GetAttributeViString
        string = 'Testing is fun?'
        self.side_effects_helper['GetAttributeViString']['attributeValue'] = string
        with nifake.Session('dev1') as session:
            attr_string = session._get_attribute_vi_string("", 5)
            assert(attr_string == string)
            from mock import call
            calls = [call(SESSION_NUM_FOR_TEST, b"", 5, 0, None), call(SESSION_NUM_FOR_TEST, b"", 5, 15, ANY)]
            self.patched_library.niFake_GetAttributeViString.assert_has_calls(calls)
            assert self.patched_library.niFake_GetAttributeViString.call_count == 2

    def test_get_string_attribute(self):
        self.patched_library.niFake_GetAttributeViString.side_effect = self.side_effects_helper.niFake_GetAttributeViString
        string = 'Testing is fun?'
        self.side_effects_helper['GetAttributeViString']['attributeValue'] = string
        with nifake.Session('dev1') as session:
            attr_string = session.read_write_string
            assert(attr_string == string)
            from mock import call
            calls = [call(SESSION_NUM_FOR_TEST, b"", 1000002, 0, None), call(SESSION_NUM_FOR_TEST, b"", 1000002, 15, ANY)]
            self.patched_library.niFake_GetAttributeViString.assert_has_calls(calls)
            assert self.patched_library.niFake_GetAttributeViString.call_count == 2

    def test_get_a_number(self):
        test_number = 16
        self.patched_library.niFake_GetANumber.side_effect = self.side_effects_helper.niFake_GetANumber
        self.side_effects_helper['GetANumber']['aNumber'] = test_number
        with nifake.Session('dev1') as session:
            test_result = session.get_a_number()
            assert isinstance(test_result, int)
            assert test_result == test_number
            self.patched_library.niFake_GetANumber.assert_called_once_with(SESSION_NUM_FOR_TEST, ANY)

    def test_invalid_attribute_value(self):
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

    def test_error_on_init(self):
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

    def test_invalid_method_call_not_enough_parameters(self):
        self.patched_library.niFake_GetAStringWithSpecifiedMaximumSize.side_effect = self.side_effects_helper.niFake_GetAStringWithSpecifiedMaximumSize
        with nifake.Session('dev1') as session:
            try:
                session.get_a_string_with_specified_maximum_size()
                assert False
            except TypeError as e:
                pass

    def test_invalid_method_call_wrong_type(self):
        self.patched_library.niFake_GetAStringWithSpecifiedMaximumSize.side_effect = self.side_effects_helper.niFake_GetAStringWithSpecifiedMaximumSize
        with nifake.Session('dev1') as session:
            try:
                session.get_a_string_with_specified_maximum_size('potato')
                assert False
            except TypeError as e:
                pass

    def test_library_singleton(self):
        with nifake.Session('dev1') as session:
            lib1 = session.library
        with nifake.Session('dev2') as session:
            lib2 = session.library
        assert lib1 is lib2

    def test_one_input_function(self):
        test_number = 1
        self.patched_library.niFake_OneInputFunction.side_effect = self.side_effects_helper.niFake_OneInputFunction
        with nifake.Session('dev1') as session:
            session.one_input_function(test_number)
            self.patched_library.niFake_OneInputFunction.assert_called_once_with(SESSION_NUM_FOR_TEST, test_number)

    def test_two_input_function(self):
        test_number = 1.5
        test_string = 'test'
        self.patched_library.niFake_TwoInputFunction.side_effect = self.side_effects_helper.niFake_TwoInputFunction
        with nifake.Session('dev1') as session:
            session.two_input_function(test_number, test_string)
            self.patched_library.niFake_TwoInputFunction.assert_called_once_with(SESSION_NUM_FOR_TEST, test_number, test_string)

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

    def test_get_a_boolean(self):
        test_boolean = True
        self.patched_library.niFake_GetABoolean.side_effect = self.side_effects_helper.niFake_GetABoolean
        self.side_effects_helper['GetABoolean']['aBoolean'] = test_boolean
        with nifake.Session('dev1') as session:
            test_result = session.get_a_boolean()
            assert isinstance(test_result, bool)
            assert test_result == test_boolean
            self.patched_library.niFake_GetABoolean.assert_called_once_with(SESSION_NUM_FOR_TEST, ANY)

    def test_set_enum_attribute(self):
        self.patched_library.niFake_SetAttributeViInt32.side_effect = self.side_effects_helper.niFake_SetAttributeViInt32
        enum_value = nifake.Color.RED
        with nifake.Session('dev1') as session:
            session.read_write_color = enum_value
            attribute_id = 1000003
            self.patched_library.niFake_SetAttributeViInt32.assert_called_once_with(SESSION_NUM_FOR_TEST, b'', attribute_id, enum_value.value)

    def test_set_enum_attribute_bad_type(self):
        with nifake.Session('dev1') as session:
            try:
                session.read_write_color = 5
            except TypeError as e:
                assert str(e) == 'must be nifake.Color not int'

    def test_get_enum_attribute(self):
        self.patched_library.niFake_GetAttributeViInt32.side_effect = self.side_effects_helper.niFake_GetAttributeViInt32
        self.side_effects_helper['GetAttributeViInt32']['attributeValue'] = nifake.Color.BLUE.value
        with nifake.Session('dev1') as session:
            assert session.read_write_color == nifake.Color.BLUE
            attribute_id = 1000003
            self.patched_library.niFake_GetAttributeViInt32.assert_called_once_with(SESSION_NUM_FOR_TEST, b'', attribute_id, ANY)

    def test_acquisition_context_manager(self):
        self.patched_library.niFake_Initiate.side_effect = self.side_effects_helper.niFake_Initiate
        self.patched_library.niFake_Abort.side_effect = self.side_effects_helper.niFake_Abort
        with nifake.Session('dev1') as session:
            with session.initiate():
                self.patched_library.niFake_Initiate.assert_called_once_with(SESSION_NUM_FOR_TEST)
            self.patched_library.niFake_Abort.assert_called_once_with(SESSION_NUM_FOR_TEST)
        self.patched_library.niFake_close.assert_called_once_with(SESSION_NUM_FOR_TEST)

    def test_cannot_add_properties_to_session(self):
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

    def test_get_vi_real64_attribute(self):
        self.patched_library.niFake_GetAttributeViReal64.side_effect = self.side_effects_helper.niFake_GetAttributeViReal64
        test_number = 1.5
        self.side_effects_helper['GetAttributeViReal64']['attributeValue'] = test_number
        with nifake.Session('dev1') as session:
            attr_double = session.read_write_double
            assert(attr_double == test_number)
            from mock import call
            calls = [call(SESSION_NUM_FOR_TEST, b"", 1000001, ANY)]
            self.patched_library.niFake_GetAttributeViReal64.assert_has_calls(calls)
            assert self.patched_library.niFake_GetAttributeViReal64.call_count == 1

    def test_get_vi_bool_attribute(self):
        self.patched_library.niFake_GetAttributeViBoolean.side_effect = self.side_effects_helper.niFake_GetAttributeViBoolean
        test_boolean = True
        self.side_effects_helper['GetAttributeViBoolean']['attributeValue'] = test_boolean
        with nifake.Session('dev1') as session:
            attr_bool = session.read_write_bool
            assert(attr_bool == test_boolean)
            from mock import call
            calls = [call(SESSION_NUM_FOR_TEST, b"", 1000000, ANY)]
            self.patched_library.niFake_GetAttributeViBoolean.assert_has_calls(calls)
            assert self.patched_library.niFake_GetAttributeViBoolean.call_count == 1

    def test_error_get_vi_real64_attribute(self):
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
                session._get_attribute_vi_real64("", 'invalidattribute')
                assert False
            except nifake.Error as e:
                assert e.code == test_error_code
                assert e.description == test_error_desc

    def test_get_error_description_get_error_message(self):
        test_error_code = -42
        test_error_desc = "The answer to the ultimate question"
        self.patched_library.niFake_GetError.side_effect = self.side_effects_helper.niFake_GetError
        self.side_effects_helper['GetError']['errorCode'] = -1
        self.side_effects_helper['GetError']['description'] = "Shouldn't get this"
        self.side_effects_helper['GetError']['return'] = -2
        self.patched_library.niFake_GetErrorMessage.side_effect = self.side_effects_helper.niFake_GetErrorMessage
        self.side_effects_helper['GetErrorMessage']['errorMessage'] = test_error_desc
        with nifake.Session('dev1') as session:
            error_desc = session.get_error_description(test_error_code)
            assert error_desc == test_error_desc
        from mock import call
        calls = [call(SESSION_NUM_FOR_TEST, test_error_code, 0, None), call(SESSION_NUM_FOR_TEST, len(test_error_desc), len(test_error_desc), ANY)]
        self.patched_library.niFake_GetErrorMessage.assert_has_calls(calls)

    '''
    def test_set_string_attribute(self):
        pass
    '''

    ''''
    # TODO(marcoskirsch): Flesh out test coverage for all NI-FAKE functions and attributes.
    # Test with multiple pointer types, ensuring proper return values (i.e. parameters in correct order)
    def test_multiple_return_params(self):
        self.patched_library.niFake_GetCalDateAndTime.side_effect = self.side_effects_helper.niFake_GetCalDateAndTime
        self.side_effects_helper['GetCalDateAndTime']['month'] = 6
        self.side_effects_helper['GetCalDateAndTime']['day'] = 30
        self.side_effects_helper['GetCalDateAndTime']['year'] = 2017
        self.side_effects_helper['GetCalDateAndTime']['hour'] = 10
        self.side_effects_helper['GetCalDateAndTime']['minute'] = 12
        with nifake.Session('dev1') as session:
            month, day, year, hour, minute = session.get_cal_date_and_time(0)
            assert(month == 6)
            assert(day == 30)
            assert(year == 2017)
            assert(hour == 10)
            assert(minute == 12)
            self.patched_library.niFake_GetCalDateAndTime.assert_called_once_with(SESSION_NUM_FOR_TEST, 0, ANY, ANY, ANY, ANY, ANY)
            assert self.patched_errors.handle_error.call_count == 2
            self.patched_errors.handle_error.assert_called_with(session, self.patched_library.niFake_GetCalDateAndTime.return_value)
    '''

    def test_init_with_options_nondefault(self):
        session = nifake.Session('FakeDevice', True, True, 'Some string')
        assert(session.vi == SESSION_NUM_FOR_TEST)
        self.patched_library.niFake_InitWithOptions.assert_called_once_with(b'FakeDevice', True, True, b'Some string', ANY)

    def test_get_vi_int32_attribute(self):
        self.patched_library.niFake_GetAttributeViInt32.side_effect = self.side_effects_helper.niFake_GetAttributeViInt32
        test_number = 3
        self.side_effects_helper['GetAttributeViInt32']['attributeValue'] = test_number
        with nifake.Session('dev1') as session:
            attr_int = session.read_write_integer
            assert(attr_int == test_number)
            self.patched_library.niFake_GetAttributeViInt32.assert_called_once_with(SESSION_NUM_FOR_TEST, b'', 1000004, ANY)

    def test_set_vi_int32_attribute(self):
        self.patched_library.niFake_SetAttributeViInt32.side_effect = self.side_effects_helper.niFake_SetAttributeViInt32
        attribute_id = 1000004
        test_number = 1
        with nifake.Session('dev1') as session:
            session.read_write_integer = test_number
            self.patched_library.niFake_SetAttributeViInt32.assert_called_once_with(SESSION_NUM_FOR_TEST, b'', attribute_id, 1)
