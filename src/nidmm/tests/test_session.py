import mock_helper
import nidmm

from mock import ANY
from mock import patch

SESSION_NUM_FOR_TEST = 42


class TestSession(object):
    def setup_method(self, method):
        self.patched_ctypes_library_patcher = patch('nidmm.ctypes_library.NidmmCtypesLibrary', autospec=True)
        self.patched_ctypes_library = self.patched_ctypes_library_patcher.start()
        self.patched_get_library_patcher = patch('nidmm.session.library.get_library', return_value=self.patched_ctypes_library)
        self.patched_get_library_patcher.start()
        self.errors_patcher = patch('nidmm.session.errors', spec_set=['_handle_error', '_is_error'])
        self.patched_errors = self.errors_patcher.start()
        self.patched_errors._is_error.return_value = 0

        self.side_effects_helper = mock_helper.SideEffectsHelper()
        self.side_effects_helper.set_side_effects_and_return_values(self.patched_ctypes_library)
        self.patched_ctypes_library.niDMM_InitWithOptions.side_effect = self.side_effects_helper.niDMM_InitWithOptions
        self.disallow_close = self.patched_ctypes_library.niDMM_close.side_effect
        self.patched_ctypes_library.niDMM_close.side_effect = self.side_effects_helper.niDMM_close

        self.side_effects_helper['InitWithOptions']['vi'] = SESSION_NUM_FOR_TEST

    def teardown_method(self, method):
        self.errors_patcher.stop()
        self.patched_get_library_patcher.stop()
        self.patched_ctypes_library_patcher.stop()

    def test_init_with_options(self):
        self.patched_ctypes_library.niDMM_close.side_effect = self.disallow_close
        session = nidmm.Session('dev1')
        assert(session.vi == SESSION_NUM_FOR_TEST)
        self.patched_ctypes_library.niDMM_InitWithOptions.assert_called_once_with(b'dev1', 0, False, b'', ANY)
        self.patched_errors._handle_error.assert_called_once_with(session, self.patched_ctypes_library.niDMM_InitWithOptions.return_value)

    def test_close(self):
        session = nidmm.Session('dev1')
        session.close()
        self.patched_ctypes_library.niDMM_close.assert_called_once_with(SESSION_NUM_FOR_TEST)

    def test_session_context_manager(self):
        with nidmm.Session('dev1') as session:
            assert(session.vi == SESSION_NUM_FOR_TEST)
            self.patched_ctypes_library.niDMM_InitWithOptions.assert_called_once_with(b'dev1', 0, False, b'', ANY)
            self.patched_errors._handle_error.assert_called_once_with(session, self.patched_ctypes_library.niDMM_InitWithOptions.return_value)
        self.patched_ctypes_library.niDMM_close.assert_called_once_with(SESSION_NUM_FOR_TEST)

    def test_reset(self):
        self.patched_ctypes_library.niDMM_reset.side_effect = self.side_effects_helper.niDMM_reset
        with nidmm.Session('dev1') as session:
            session.reset()
            self.patched_ctypes_library.niDMM_reset.assert_called_once_with(SESSION_NUM_FOR_TEST)
            assert self.patched_errors._handle_error.call_count == 2
            self.patched_errors._handle_error.assert_called_with(session, self.patched_ctypes_library.niDMM_reset.return_value)

    # Additional tests

    # Test with multiple pointer types, ensuring proper return values (i.e. parameters in correct order)
    def test_multiple_return_params(self):
        self.patched_ctypes_library.niDMM_GetCalDateAndTime.side_effect = self.side_effects_helper.niDMM_GetCalDateAndTime
        self.side_effects_helper['GetCalDateAndTime']['month'] = 6
        self.side_effects_helper['GetCalDateAndTime']['day'] = 30
        self.side_effects_helper['GetCalDateAndTime']['year'] = 2017
        self.side_effects_helper['GetCalDateAndTime']['hour'] = 10
        self.side_effects_helper['GetCalDateAndTime']['minute'] = 12
        with nidmm.Session('dev1') as session:
            month, day, year, hour, minute = session.get_cal_date_and_time(0)
            assert(month == 6)
            assert(day == 30)
            assert(year == 2017)
            assert(hour == 10)
            assert(minute == 12)
            self.patched_ctypes_library.niDMM_GetCalDateAndTime.assert_called_once_with(SESSION_NUM_FOR_TEST, 0, ANY, ANY, ANY, ANY, ANY)
            assert self.patched_errors._handle_error.call_count == 2
            self.patched_errors._handle_error.assert_called_with(session, self.patched_ctypes_library.niDMM_GetCalDateAndTime.return_value)

    # Test getting a string attribute (IVI dance to get string)
    def test_get_string_attribute(self):
        self.patched_ctypes_library.niDMM_GetAttributeViString.side_effect = self.side_effects_helper.niDMM_GetAttributeViString
        self.side_effects_helper['GetAttributeViString']['attributeValue'] = 'Testing is fun?'
        with nidmm.Session('dev1') as session:
            attr_string = session._get_attribute_vi_string("", 5)
            assert(attr_string == 'Testing is fun?')
            assert self.patched_errors._handle_error.call_count == 2
            assert self.patched_ctypes_library.niDMM_GetAttributeViString.call_count == 2

    # Get string attribute works from attribute type
    def test_get_string_attribute_type(self):
        self.patched_ctypes_library.niDMM_GetAttributeViString.side_effect = self.side_effects_helper.niDMM_GetAttributeViString
        self.side_effects_helper['GetAttributeViString']['attributeValue'] = '0x12345678'
        with nidmm.Session('dev1') as session:
            sn = session.instrument_serial_number
            assert(sn == '0x12345678')

    def test_acquisition_context_manager(self):
        self.patched_ctypes_library.niDMM_Initiate.side_effect = self.side_effects_helper.niDMM_Initiate
        self.patched_ctypes_library.niDMM_Abort.side_effect = self.side_effects_helper.niDMM_Abort
        with nidmm.Session('dev1') as session:
            with session.initiate():
                self.patched_ctypes_library.niDMM_Initiate.assert_called_once_with(SESSION_NUM_FOR_TEST)
            self.patched_ctypes_library.niDMM_Abort.assert_called_once_with(SESSION_NUM_FOR_TEST)
        self.patched_ctypes_library.niDMM_close.assert_called_once_with(SESSION_NUM_FOR_TEST)

    def test_cannot_add_properties_to_session(self):
        with nidmm.Session('dev1') as session:
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

