import _matchers
import _mock_helper

import datetime
import nitclk

from mock import patch

SESSION_NUM_FOR_TEST = 42
single_session = [SESSION_NUM_FOR_TEST]
multiple_sessions = [SESSION_NUM_FOR_TEST, SESSION_NUM_FOR_TEST * 10, SESSION_NUM_FOR_TEST * 100, SESSION_NUM_FOR_TEST + 1]


class TestSession(object):
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


