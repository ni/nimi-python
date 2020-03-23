import _mock_helper

import nidigital

from mock import patch
import pytest

session_id_for_test = 42


class TestSession(object):
    def setup_method(self, method):
        self.patched_library_patcher = patch('nidigital._library.Library', autospec=True)
        self.patched_library = self.patched_library_patcher.start()
        self.patched_library_singleton_get = patch('nidigital.session._library_singleton.get', return_value=self.patched_library)
        self.patched_library_singleton_get.start()

        self.side_effects_helper = _mock_helper.SideEffectsHelper()
        self.side_effects_helper.set_side_effects_and_return_values(self.patched_library)

        self.patched_library.niDigital_InitWithOptions.side_effect = self.side_effects_helper.niDigital_InitWithOptions
        self.side_effects_helper['InitWithOptions']['newVi'] = session_id_for_test

        self.patched_library.niDigital_close.side_effect = self.side_effects_helper.niDigital_close

        self.patched_library.niDigital_LockSession.side_effect = self.side_effects_helper.niDigital_LockSession
        self.side_effects_helper['LockSession']['callerHasLock'] = True

        self.patched_library.niDigital_UnlockSession.side_effect = self.side_effects_helper.niDigital_UnlockSession
        self.side_effects_helper['UnlockSession']['callerHasLock'] = True

    def teardown_method(self, method):
        self.patched_library_singleton_get.stop()
        self.patched_library_patcher.stop()

    # API Tests

    def test_fetch_history_ram_cycle_information_position_out_of_bound(self):

        self.patched_library.niDigital_GetHistoryRAMSampleCount.side_effect = self.side_effects_helper.niDigital_GetHistoryRAMSampleCount
        self.side_effects_helper['GetHistoryRAMSampleCount']['sampleCount'] = 7
        with nidigital.Session('') as session:
            with pytest.raises(ValueError, match='position: Specified value = 8, Maximum value = 6.'):
                session.fetch_history_ram_cycle_information(
                    site='site1',
                    position=8,
                    samples_to_read=-1)
