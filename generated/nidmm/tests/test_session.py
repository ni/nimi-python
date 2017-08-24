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

        self.side_effects_helper = mock_helper.SideEffectsHelper()
        self.side_effects_helper.set_side_effects_and_return_values(self.patched_ctypes_library)
        self.patched_ctypes_library.niDMM_InitWithOptions.side_effect = self.side_effects_helper.niDMM_InitWithOptions
        self.disallow_close = self.patched_ctypes_library.niDMM_close.side_effect
        self.patched_ctypes_library.niDMM_close.side_effect = self.side_effects_helper.niDMM_close

        self.side_effects_helper['InitWithOptions']['vi'] = SESSION_NUM_FOR_TEST

    def teardown_method(self, method):
        self.patched_get_library_patcher.stop()
        self.patched_ctypes_library_patcher.stop()

    def test_init_with_options(self):
        self.errors_patcher = patch('nidmm.session.errors', spec_set=['_handle_error', '_is_error'])
        self.patched_errors = self.errors_patcher.start()
        self.patched_errors._is_error.return_value = 0

        self.patched_ctypes_library.niDMM_close.side_effect = self.disallow_close
        session = nidmm.Session('dev1')
        assert(session.vi == SESSION_NUM_FOR_TEST)
        self.patched_ctypes_library.niDMM_InitWithOptions.assert_called_once_with(b'dev1', 0, False, b'', ANY)
        self.patched_errors._handle_error.assert_called_once_with(session, self.patched_ctypes_library.niDMM_InitWithOptions.return_value)

        self.errors_patcher.stop()

    def test_close(self):
        session = nidmm.Session('dev1')
        session.close()
        self.patched_ctypes_library.niDMM_close.assert_called_once_with(SESSION_NUM_FOR_TEST)

    def test_session_context_manager(self):
        with nidmm.Session('dev1') as session:
            assert(session.vi == SESSION_NUM_FOR_TEST)
            self.patched_ctypes_library.niDMM_InitWithOptions.assert_called_once_with(b'dev1', 0, False, b'', ANY)
        self.patched_ctypes_library.niDMM_close.assert_called_once_with(SESSION_NUM_FOR_TEST)

    def test_reset(self):
        self.patched_ctypes_library.niDMM_reset.side_effect = self.side_effects_helper.niDMM_reset
        with nidmm.Session('dev1') as session:
            session.reset()
            self.patched_ctypes_library.niDMM_reset.assert_called_once_with(SESSION_NUM_FOR_TEST)

    def test_with_error(self):
        self.patched_ctypes_library.niDMM_reset.side_effect = self.side_effects_helper.niDMM_reset
        self.side_effects_helper['reset']['return'] = -42
        self.patched_ctypes_library.niDMM_GetError.side_effect = self.side_effects_helper.niDMM_GetError
        self.side_effects_helper['GetError']['errorCode'] = -42
        self.side_effects_helper['GetError']['description'] = "The answer to the ultimate question"
        with nidmm.Session('dev1') as session:
            try:
                session.reset()
                assert False
            except nidmm.Error as e:
                assert e.code == -42
                assert e.description == "The answer to the ultimate question"

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

    # Test getting a string attribute (IVI dance to get string)
    def test_get_string_attribute(self):
        self.patched_ctypes_library.niDMM_GetAttributeViString.side_effect = self.side_effects_helper.niDMM_GetAttributeViString
        self.side_effects_helper['GetAttributeViString']['attributeValue'] = 'Testing is fun?'
        with nidmm.Session('dev1') as session:
            attr_string = session._get_attribute_vi_string("", 5)
            assert attr_string == 'Testing is fun?'

    def test_get_string_attribute_with_error(self):
        self.patched_ctypes_library.niDMM_GetAttributeViString.side_effect = self.side_effects_helper.niDMM_GetAttributeViString
        self.side_effects_helper['GetAttributeViString']['attributeValue'] = 'Testing is fun?'
        self.side_effects_helper['GetAttributeViString']['return'] = -1234
        self.patched_ctypes_library.niDMM_GetError.side_effect = self.side_effects_helper.niDMM_GetError
        self.side_effects_helper['GetError']['errorCode'] = -1234
        self.side_effects_helper['GetError']['description'] = "ascending order"
        with nidmm.Session('dev1') as session:
            try:
                session._get_attribute_vi_string("", 5)
                assert False
            except nidmm.Error as e:
                assert e.code == -1234
                assert e.description == "ascending order"

    # Get string attribute works from attribute type
    def test_get_string_attribute_type(self):
        self.patched_ctypes_library.niDMM_GetAttributeViString.side_effect = self.side_effects_helper.niDMM_GetAttributeViString
        self.side_effects_helper['GetAttributeViString']['attributeValue'] = '0x12345678'
        with nidmm.Session('dev1') as session:
            sn = session.serial_number
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

    def test_bool_return_type(self):
        self.patched_ctypes_library.niDMM_GetSelfCalSupported = self.side_effects_helper.niDMM_GetSelfCalSupported
        self.side_effects_helper['GetSelfCalSupported']['selfCalSupported'] = 1
        with nidmm.Session('dev1') as session:
            self_cal_supported = session.get_self_cal_supported()
            assert str(self_cal_supported) == 'True'

    def test_enum_return_type(self):
        self.patched_ctypes_library.niDMM_ReadStatus = self.side_effects_helper.niDMM_ReadStatus
        self.side_effects_helper['ReadStatus']['acquisitionBacklog'] = 0
        self.side_effects_helper['ReadStatus']['acquisitionStatus'] = 4
        with nidmm.Session('dev1') as session:
            (backlog, status) = session.read_status()
            assert backlog == 0
            assert type(status) is nidmm.AcquisitionStatus
            assert status == nidmm.AcquisitionStatus.NO_ACQUISITION_IN_PROGRESS


