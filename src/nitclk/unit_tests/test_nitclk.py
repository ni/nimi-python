import _matchers
import _mock_helper

import datetime
import nitclk

from mock import patch

SESSION_NUM_FOR_TEST = 42
single_session = [SESSION_NUM_FOR_TEST]
multiple_sessions = [SESSION_NUM_FOR_TEST, SESSION_NUM_FOR_TEST * 10, SESSION_NUM_FOR_TEST * 100, SESSION_NUM_FOR_TEST + 1]


class NitclkSessionTest(object):
    '''Fake Session objects for drivers that support NI-TClk are expected to have a property of tyep nitclk.SessionReference called tclk.'''
    def __init__(self, session_number):
        self.tclk = nitclk.SessionReference(session_number)


class TestNitclkApi(object):
    def setup_method(self, method):
        self.patched_library_patcher = patch('nitclk._library.Library', autospec=True)
        self.patched_library = self.patched_library_patcher.start()
        self.patched_library_singleton_get = patch('nitclk.session._library_singleton.get', return_value=self.patched_library)
        self.patched_library_singleton_get.start()

        self.side_effects_helper = _mock_helper.SideEffectsHelper()
        self.side_effects_helper.set_side_effects_and_return_values(self.patched_library)

    def teardown_method(self, method):
        self.patched_library_singleton_get.stop()
        self.patched_library_patcher.stop()

    # API Tests

    def test_initialize_one_session(self):
        self.patched_library.niTClk_Initiate.side_effect = self.side_effects_helper.niTClk_Initiate
        nitclk.initiate(single_session)
        self.patched_library.niTClk_Initiate.assert_called_once_with(_matchers.ViUInt32Matcher(len(single_session)), _matchers.ViSessionBufferMatcher(single_session))
        return

    def test_initialize_multiple_sessions(self):
        self.patched_library.niTClk_Initiate.side_effect = self.side_effects_helper.niTClk_Initiate
        nitclk.initiate(multiple_sessions)
        self.patched_library.niTClk_Initiate.assert_called_once_with(_matchers.ViUInt32Matcher(len(multiple_sessions)), _matchers.ViSessionBufferMatcher(multiple_sessions))
        return

    def test_configure_for_homogeneous_triggers(self):
        self.patched_library.niTClk_ConfigureForHomogeneousTriggers.side_effect = self.side_effects_helper.niTClk_ConfigureForHomogeneousTriggers
        nitclk.configure_for_homogeneous_triggers(multiple_sessions)
        self.patched_library.niTClk_ConfigureForHomogeneousTriggers.assert_called_once_with(_matchers.ViUInt32Matcher(len(multiple_sessions)), _matchers.ViSessionBufferMatcher(multiple_sessions))
        return

    def test_finish_sync_pulse_sender_synchronize(self):
        min_time = 0.042
        self.patched_library.niTClk_FinishSyncPulseSenderSynchronize.side_effect = self.side_effects_helper.niTClk_FinishSyncPulseSenderSynchronize
        nitclk.finish_sync_pulse_sender_synchronize(multiple_sessions, min_time)
        self.patched_library.niTClk_FinishSyncPulseSenderSynchronize.assert_called_once_with(_matchers.ViUInt32Matcher(len(multiple_sessions)), _matchers.ViSessionBufferMatcher(multiple_sessions), _matchers.ViReal64Matcher(min_time))
        return

    def test_is_done(self):
        expected_result = True
        self.side_effects_helper['IsDone']['done'] = expected_result

        self.patched_library.niTClk_IsDone.side_effect = self.side_effects_helper.niTClk_IsDone
        actual_result = nitclk.is_done(multiple_sessions)
        assert actual_result == expected_result
        self.patched_library.niTClk_IsDone.assert_called_once_with(_matchers.ViUInt32Matcher(len(multiple_sessions)), _matchers.ViSessionBufferMatcher(multiple_sessions), _matchers.ViBooleanPointerMatcher())
        return

    def test_setup_for_sync_pulse_sender_synchronize(self):
        min_time = 0.042
        self.patched_library.niTClk_SetupForSyncPulseSenderSynchronize.side_effect = self.side_effects_helper.niTClk_SetupForSyncPulseSenderSynchronize
        nitclk.setup_for_sync_pulse_sender_synchronize(multiple_sessions, min_time)
        self.patched_library.niTClk_SetupForSyncPulseSenderSynchronize.assert_called_once_with(_matchers.ViUInt32Matcher(len(multiple_sessions)), _matchers.ViSessionBufferMatcher(multiple_sessions), _matchers.ViReal64Matcher(min_time))
        return

    def test_synchronize(self):
        min_time = 0.042
        self.patched_library.niTClk_Synchronize.side_effect = self.side_effects_helper.niTClk_Synchronize
        nitclk.synchronize(multiple_sessions, min_time)
        self.patched_library.niTClk_Synchronize.assert_called_once_with(_matchers.ViUInt32Matcher(len(multiple_sessions)), _matchers.ViSessionBufferMatcher(multiple_sessions), _matchers.ViReal64Matcher(min_time))
        return

    def test_synchronize_timedelta(self):
        min_time = datetime.timedelta(seconds=0.042)
        self.patched_library.niTClk_Synchronize.side_effect = self.side_effects_helper.niTClk_Synchronize
        nitclk.synchronize(multiple_sessions, min_time)
        self.patched_library.niTClk_Synchronize.assert_called_once_with(_matchers.ViUInt32Matcher(len(multiple_sessions)), _matchers.ViSessionBufferMatcher(multiple_sessions), _matchers.ViReal64Matcher(min_time.total_seconds()))
        return

    def test_synchronize_to_sync_pulse_sender(self):
        min_time = 0.042
        self.patched_library.niTClk_SynchronizeToSyncPulseSender.side_effect = self.side_effects_helper.niTClk_SynchronizeToSyncPulseSender
        nitclk.synchronize_to_sync_pulse_sender(multiple_sessions, min_time)
        self.patched_library.niTClk_SynchronizeToSyncPulseSender.assert_called_once_with(_matchers.ViUInt32Matcher(len(multiple_sessions)), _matchers.ViSessionBufferMatcher(multiple_sessions), _matchers.ViReal64Matcher(min_time))
        return

    def test_wait_until_done(self):
        min_time = 4.2
        self.patched_library.niTClk_WaitUntilDone.side_effect = self.side_effects_helper.niTClk_WaitUntilDone
        nitclk.wait_until_done(multiple_sessions, min_time)
        self.patched_library.niTClk_WaitUntilDone.assert_called_once_with(_matchers.ViUInt32Matcher(len(multiple_sessions)), _matchers.ViSessionBufferMatcher(multiple_sessions), _matchers.ViReal64Matcher(min_time))
        return

    # API error handling

    def test_api_error(self):
        error_string = 'Error'
        self.patched_library.niTClk_Synchronize.side_effect = self.side_effects_helper.niTClk_Synchronize
        self.side_effects_helper['Synchronize']['return'] = -1
        self.patched_library.niTClk_GetExtendedErrorInfo.side_effect = self.side_effects_helper.niTClk_GetExtendedErrorInfo
        self.side_effects_helper['GetExtendedErrorInfo']['errorString'] = error_string
        try:
            nitclk.synchronize(multiple_sessions, 0.42)
        except nitclk.Error as e:
            assert e.code == -1
            assert e.description == error_string

    def test_api_get_error_description_fails(self):
        self.patched_library.niTClk_Synchronize.side_effect = self.side_effects_helper.niTClk_Synchronize
        self.side_effects_helper['Synchronize']['return'] = -1
        self.patched_library.niTClk_GetExtendedErrorInfo.side_effect = self.side_effects_helper.niTClk_GetExtendedErrorInfo
        self.side_effects_helper['GetExtendedErrorInfo']['return'] = -2
        try:
            nitclk.synchronize(multiple_sessions, 0.42)
        except nitclk.Error as e:
            assert e.code == -1  # we want the original error code from getting the attribute.
            assert e.description == "Failed to retrieve error description."

    # SessionReference error handling

    def test_session_reference_error(self):
        session = nitclk.SessionReference(SESSION_NUM_FOR_TEST)
        error_string = 'Error'
        self.patched_library.niTClk_GetAttributeViReal64.side_effect = self.side_effects_helper.niTClk_GetAttributeViReal64
        self.side_effects_helper['GetAttributeViReal64']['return'] = -1
        self.patched_library.niTClk_GetExtendedErrorInfo.side_effect = self.side_effects_helper.niTClk_GetExtendedErrorInfo
        self.side_effects_helper['GetExtendedErrorInfo']['errorString'] = error_string
        try:
            test = session.sample_clock_delay
            print(test)  # Get rid of flake8 F841
            assert False
        except nitclk.Error as e:
            assert e.code == -1
            assert e.description == error_string

    def test_session_reference_get_error_description_fails(self):
        session = nitclk.SessionReference(SESSION_NUM_FOR_TEST)
        self.patched_library.niTClk_GetAttributeViReal64.side_effect = self.side_effects_helper.niTClk_GetAttributeViReal64
        self.side_effects_helper['GetAttributeViReal64']['return'] = -1
        self.patched_library.niTClk_GetExtendedErrorInfo.side_effect = self.side_effects_helper.niTClk_GetExtendedErrorInfo
        self.side_effects_helper['GetExtendedErrorInfo']['return'] = -2
        try:
            test = session.sample_clock_delay
            print(test)  # Get rid of flake8 F841
            assert False
        except nitclk.Error as e:
            assert e.code == -1  # we want the original error code from getting the attribute.
            assert e.description == "Failed to retrieve error description."

    # Session Reference

    def test_set_vi_real64(self):
        session = nitclk.SessionReference(SESSION_NUM_FOR_TEST)
        self.patched_library.niTClk_SetAttributeViReal64.side_effect = self.side_effects_helper.niTClk_SetAttributeViReal64
        attribute_id = 11
        test_number = 4.2
        session.sample_clock_delay = test_number
        self.patched_library.niTClk_SetAttributeViReal64.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViReal64Matcher(test_number))

    def test_get_vi_real64(self):
        session = nitclk.SessionReference(SESSION_NUM_FOR_TEST)
        self.patched_library.niTClk_GetAttributeViReal64.side_effect = self.side_effects_helper.niTClk_GetAttributeViReal64
        attribute_id = 11
        test_number = 4.2
        self.side_effects_helper['GetAttributeViReal64']['value'] = test_number
        attr_float = session.sample_clock_delay
        assert(attr_float == test_number)
        self.patched_library.niTClk_GetAttributeViReal64.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViReal64PointerMatcher())

    def test_set_vi_string(self):
        session = nitclk.SessionReference(SESSION_NUM_FOR_TEST)
        self.patched_library.niTClk_SetAttributeViString.side_effect = self.side_effects_helper.niTClk_SetAttributeViString
        attribute_id = 13
        test_string = "The answer to the ultimate question is 42"
        session.sync_pulse_sender_sync_pulse_source = test_string
        self.patched_library.niTClk_SetAttributeViString.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViStringMatcher(test_string))

    def test_get_vi_string(self):
        session = nitclk.SessionReference(SESSION_NUM_FOR_TEST)
        self.patched_library.niTClk_GetAttributeViString.side_effect = self.side_effects_helper.niTClk_GetAttributeViString
        attribute_id = 13
        test_string = "The answer to the ultimate question is 42"
        self.side_effects_helper['GetAttributeViString']['value'] = test_string
        attr_string = session.sync_pulse_sender_sync_pulse_source
        assert(attr_string == test_string)

        from mock import call
        calls = [call(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViInt32Matcher(0), None), call(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViInt32Matcher(len(test_string)), _matchers.ViCharBufferMatcher(len(test_string)))]
        self.patched_library.niTClk_GetAttributeViString.assert_has_calls(calls)
        assert self.patched_library.niTClk_GetAttributeViString.call_count == 2

    # All ViInt32 attributes are really sessions references
    def test_set_vi_session_with_int(self):
        session = nitclk.SessionReference(SESSION_NUM_FOR_TEST)
        self.patched_library.niTClk_SetAttributeViSession.side_effect = self.side_effects_helper.niTClk_SetAttributeViSession
        attribute_id = 3
        other_session_number = 43
        session.start_trigger_master_session = other_session_number
        self.patched_library.niTClk_SetAttributeViSession.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViSessionMatcher(other_session_number))

    def test_set_vi_session_with_session(self):
        session = nitclk.SessionReference(SESSION_NUM_FOR_TEST)
        self.patched_library.niTClk_SetAttributeViSession.side_effect = self.side_effects_helper.niTClk_SetAttributeViSession
        attribute_id = 3
        other_session_number = 43
        other_session = NitclkSessionTest(other_session_number)
        session.start_trigger_master_session = other_session
        self.patched_library.niTClk_SetAttributeViSession.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViSessionMatcher(other_session_number))

    def test_get_vi_session(self):
        session = nitclk.SessionReference(SESSION_NUM_FOR_TEST)
        self.patched_library.niTClk_GetAttributeViSession.side_effect = self.side_effects_helper.niTClk_GetAttributeViSession
        attribute_id = 3
        other_session_number = 43
        self.side_effects_helper['GetAttributeViSession']['value'] = other_session_number
        attr_session_reference = session.start_trigger_master_session
        assert type(attr_session_reference) is nitclk.SessionReference
        assert(attr_session_reference._get_session_number() == other_session_number)
        self.patched_library.niTClk_GetAttributeViSession.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViSessionPointerMatcher())




