import mock_helper
import nifake

from mock import ANY
from mock import patch
# from mock import call

SESSION_NUM_FOR_TEST = 42


class TestSession(object):

    def setup_method(self, method):
        self.patched_ctypes_library_patcher = patch('nifake.ctypes_library.NifakeCtypesLibrary', autospec=True)
        self.patched_ctypes_library = self.patched_ctypes_library_patcher.start()
        self.patched_get_library_patcher = patch('nifake.session.library.get_library', return_value=self.patched_ctypes_library)
        self.patched_get_library_patcher.start()

        self.side_effects_helper = mock_helper.SideEffectsHelper()
        self.side_effects_helper.set_side_effects_and_return_values(self.patched_ctypes_library)
        self.patched_ctypes_library.niFake_InitWithOptions.side_effect = self.side_effects_helper.niFake_InitWithOptions
        self.disallow_close = self.patched_ctypes_library.niFake_close.side_effect
        self.patched_ctypes_library.niFake_close.side_effect = self.side_effects_helper.niFake_close

        self.side_effects_helper['InitWithOptions']['vi'] = SESSION_NUM_FOR_TEST

    def teardown_method(self, method):
        self.patched_get_library_patcher.stop()
        self.patched_ctypes_library_patcher.stop()

    def test_init_with_options(self):
        errors_patcher = patch('nifake.session.errors', spec_set=['_handle_error', '_is_error'])
        patched_errors = errors_patcher.start()
        patched_errors._is_error.return_value = 0

        self.patched_ctypes_library.niFake_close.side_effect = self.disallow_close
        session = nifake.Session('dev1')
        assert(session.vi == SESSION_NUM_FOR_TEST)
        self.patched_ctypes_library.niFake_InitWithOptions.assert_called_once_with(b'dev1', 0, False, b'', ANY)
        patched_errors._handle_error.assert_called_once_with(session, self.patched_ctypes_library.niFake_InitWithOptions.return_value)

        errors_patcher.stop()

    def test_close(self):
        session = nifake.Session('dev1')
        session.close()
        self.patched_ctypes_library.niFake_close.assert_called_once_with(SESSION_NUM_FOR_TEST)

    def test_session_context_manager(self):
        with nifake.Session('dev1') as session:
            assert(session.vi == SESSION_NUM_FOR_TEST)
            self.patched_ctypes_library.niFake_InitWithOptions.assert_called_once_with(b'dev1', 0, False, b'', ANY)
        self.patched_ctypes_library.niFake_close.assert_called_once_with(SESSION_NUM_FOR_TEST)

    def test_get_error_description_get_error(self):
        test_error_code = -42
        test_error_desc = "The answer to the ultimate question"
        self.patched_ctypes_library.niFake_GetError.side_effect = self.side_effects_helper.niFake_GetError
        self.side_effects_helper['GetError']['errorCode'] = test_error_code
        self.side_effects_helper['GetError']['description'] = test_error_desc
        with nifake.Session('dev1') as session:
            error_code, error_desc = session._get_error_description(test_error_code)
            assert error_code == test_error_code
            assert error_desc == test_error_desc

    '''
    def test_get_error_description_get_error_message(self):
        test_error_code = -42
        test_error_desc = "The answer to the ultimate question"
        self.patched_ctypes_library.niFake_GetError.side_effect = self.side_effects_helper.niFake_GetError
        self.side_effects_helper['GetError']['errorCode'] = -1
        self.side_effects_helper['GetError']['description'] = "Shouldn't get this"
        self.side_effects_helper['GetError']['return'] = -2
        self.patched_ctypes_library.niFake_GetErrorMessage.side_effect = self.side_effects_helper.niFake_GetErrorMessage
        self.side_effects_helper['GetErrorMessage']['errorMessage'] = test_error_desc
        with nifake.Session('dev1') as session:
            error_code, error_desc = session._get_error_description(test_error_code)
            assert error_code == test_error_code
            assert error_desc == test_error_desc
    '''

    def test_method_with_error(self):
        test_error_code = -42
        test_error_desc = "The answer to the ultimate question"
        self.patched_ctypes_library.niFake_reset.side_effect = self.side_effects_helper.niFake_reset
        self.side_effects_helper['reset']['return'] = test_error_code
        self.patched_ctypes_library.niFake_GetError.side_effect = self.side_effects_helper.niFake_GetError
        self.side_effects_helper['GetError']['errorCode'] = test_error_code
        self.side_effects_helper['GetError']['description'] = test_error_desc
        with nifake.Session('dev1') as session:
            try:
                session.reset()
                assert False
            except nifake.Error as e:
                assert e.code == test_error_code
                assert e.description == test_error_desc

    def test_ivi_dance_with_error(self):
        test_error_code = -1234
        test_error_desc = "ascending order"
        self.patched_ctypes_library.niFake_GetAttributeViString.side_effect = self.side_effects_helper.niFake_GetAttributeViString
        self.side_effects_helper['GetAttributeViString']['attributeValue'] = 'Testing is fun?'
        self.side_effects_helper['GetAttributeViString']['return'] = test_error_code
        self.patched_ctypes_library.niFake_GetError.side_effect = self.side_effects_helper.niFake_GetError
        self.side_effects_helper['GetError']['errorCode'] = test_error_code
        self.side_effects_helper['GetError']['description'] = test_error_desc
        with nifake.Session('dev1') as session:
            try:
                session._get_attribute_vi_string("", 5)
                assert False
            except nifake.Error as e:
                assert e.code == test_error_code
                assert e.description == test_error_desc

    '''
    #TODO(marcoskirsch): unit test in which niFake_InitWithOptions returns an error.
    def test_session_error(self):
        pass
    '''

    def test_simple_function(self):
        self.patched_ctypes_library.niFake_SimpleFunction.side_effect = self.side_effects_helper.niFake_SimpleFunction
        with nifake.Session('dev1') as session:
            session.simple_function()
            self.patched_ctypes_library.niFake_SimpleFunction.assert_called_once_with(SESSION_NUM_FOR_TEST)

    '''
    def test_set_string_attribute(self):
        pass
    '''

    '''
    def test_get_string_attribute(self):
        self.patched_ctypes_library.niFake_GetAttributeViString.side_effect = self.side_effects_helper.niFake_GetAttributeViString
        self.side_effects_helper['GetAttributeViString']['attributeValue'] = 'A string'
        with nifake.Session('dev1') as session:
            assert(session.read_write_string == 'A string')
            #calls = [call(SESSION_NUM_FOR_TEST, '', 1000002, 0, ANY), call(SESSION_NUM_FOR_TEST, '', 1000002, 0, ANY)]
            #self.patched_ctypes_library.niFake_GetAttributeViString.assert_has_calls(calls)
    '''

    # TODO(marcoskirsch): Flesh out test coverage for all NI-FAKE functions and attributes.

    '''
    # Test with multiple pointer types, ensuring proper return values (i.e. parameters in correct order)
    def test_multiple_return_params(self):
        self.patched_ctypes_library.niFake_GetCalDateAndTime.side_effect = self.side_effects_helper.niFake_GetCalDateAndTime
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
            self.patched_ctypes_library.niFake_GetCalDateAndTime.assert_called_once_with(SESSION_NUM_FOR_TEST, 0, ANY, ANY, ANY, ANY, ANY)
            assert self.patched_errors._handle_error.call_count == 2
            self.patched_errors._handle_error.assert_called_with(session, self.patched_ctypes_library.niFake_GetCalDateAndTime.return_value)
    '''

    '''
    # Test getting a string attribute (IVI dance to get string)
    def test_get_string_attribute(self):
        self.patched_ctypes_library.niFake_GetAttributeViString.side_effect = self.side_effects_helper.niFake_GetAttributeViString
        self.side_effects_helper['GetAttributeViString']['attributeValue'] = 'Testing is fun?'
        with nifake.Session('dev1') as session:
            attr_string = session._get_attribute_vi_string("", 5)
            assert(attr_string == 'Testing is fun?')
            assert self.patched_errors._handle_error.call_count == 2
            assert self.patched_ctypes_library.niFake_GetAttributeViString.call_count == 2
    '''

    '''
    def test_acquisition_context_manager(self):
        self.patched_ctypes_library.niFake_Initiate.side_effect = self.side_effects_helper.niFake_Initiate
        self.patched_ctypes_library.niFake_Abort.side_effect = self.side_effects_helper.niFake_Abort
        with nifake.Session('dev1') as session:
            with session.initiate():
                self.patched_ctypes_library.niFake_Initiate.assert_called_once_with(SESSION_NUM_FOR_TEST)
            self.patched_ctypes_library.niFake_Abort.assert_called_once_with(SESSION_NUM_FOR_TEST)
        self.patched_ctypes_library.niFake_close.assert_called_once_with(SESSION_NUM_FOR_TEST)
    '''

    '''
    def test_cannot_add_properties_to_session(self):
        with nifake.Session('dev1') as session:
            try:
                session.nonexistent_property = 5
                assert False
            except TypeError as e:
                print(e)
                pass
            try:
                value = session.nonexistent_property  # noqa: F841
                assert False
            except AttributeError as e:
                print(e)
                pass
    '''
