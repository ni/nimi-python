import _matchers
import _mock_helper

import nitclk

from mock import patch

SESSION_NUM_FOR_TEST = 42


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
        sessions = [SESSION_NUM_FOR_TEST]
        self.patched_library.niTClk_Initiate.side_effect = self.side_effects_helper.niTClk_Initiate
        nitclk.initiate(sessions)
        self.patched_library.niTClk_Initiate.assert_called_once_with(_matchers.ViUInt32Matcher(len(sessions)), _matchers.ViSessionBufferMatcher(sessions))
        return

    def test_initialize_multiple_sessions(self):
        sessions = [SESSION_NUM_FOR_TEST, SESSION_NUM_FOR_TEST+1, SESSION_NUM_FOR_TEST+2]
        self.patched_library.niTClk_Initiate.side_effect = self.side_effects_helper.niTClk_Initiate
        nitclk.initiate(sessions)
        self.patched_library.niTClk_Initiate.assert_called_once_with(_matchers.ViUInt32Matcher(len(sessions)), _matchers.ViSessionBufferMatcher(sessions))
        return

    def test_configure_for_homogeneous_triggers(self):
        sessions = [SESSION_NUM_FOR_TEST, SESSION_NUM_FOR_TEST+1, SESSION_NUM_FOR_TEST+2]
        self.patched_library.niTClk_ConfigureForHomogeneousTriggers.side_effect = self.side_effects_helper.niTClk_ConfigureForHomogeneousTriggers
        nitclk.configure_for_homogeneous_triggers(sessions)
        self.patched_library.niTClk_ConfigureForHomogeneousTriggers.assert_called_once_with(_matchers.ViUInt32Matcher(len(sessions)), _matchers.ViSessionBufferMatcher(sessions))
        return

    def test_finish_sync_pulse_sender_synchronize(self):
        sessions = [SESSION_NUM_FOR_TEST, SESSION_NUM_FOR_TEST+1, SESSION_NUM_FOR_TEST+2]
        min_time = 0.042
        self.patched_library.niTClk_FinishSyncPulseSenderSynchronize.side_effect = self.side_effects_helper.niTClk_FinishSyncPulseSenderSynchronize
        nitclk.finish_sync_pulse_sender_synchronize(sessions, min_time)
        self.patched_library.niTClk_FinishSyncPulseSenderSynchronize.assert_called_once_with(_matchers.ViUInt32Matcher(len(sessions)), _matchers.ViSessionBufferMatcher(sessions), _matchers.ViReal64Matcher(min_time))
        return


