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


