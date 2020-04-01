import _mock_helper

import nidigital
from nidigital.enums import PinState

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

    # TODO(sbethur): When nidigital driver provides better simulation support (internal bug# 992370),
    #  this test should be converted to a system test. (GitHub issue# 1353).
    def test_fetch_history_ram_cycle_information_position_out_of_bound(self):

        self.patched_library.niDigital_GetHistoryRAMSampleCount.side_effect = self.side_effects_helper.niDigital_GetHistoryRAMSampleCount
        self.side_effects_helper['GetHistoryRAMSampleCount']['sampleCount'] = 7
        with nidigital.Session('') as session:
            with pytest.raises(ValueError, match='position: Specified value = 8, Maximum value = 6.'):
                session.sites[1].fetch_history_ram_cycle_information(position=8, samples_to_read=-1)

    # TODO(sbethur): When nidigital driver provides better simulation support (internal bug# 992370),
    #  this test should be converted to a system test. (GitHub issue# 1353).
    def test_fetch_history_ram_cycle_information_position_last(self):

        self.patched_library.niDigital_GetHistoryRAMSampleCount.side_effect = self.side_effects_helper.niDigital_GetHistoryRAMSampleCount
        self.side_effects_helper['GetHistoryRAMSampleCount']['sampleCount'] = 7
        self.patched_library.niDigital_GetAttributeViBoolean.side_effect = self.side_effects_helper.niDigital_GetAttributeViBoolean
        self.side_effects_helper['GetAttributeViBoolean']['value'] = True  # history_ram_number_of_samples_is_finite
        self.patched_library.niDigital_FetchHistoryRAMCycleInformation.side_effect = self.side_effects_helper.niDigital_FetchHistoryRAMCycleInformation
        self.side_effects_helper['FetchHistoryRAMCycleInformation']['patternIndex'] = 0
        self.side_effects_helper['FetchHistoryRAMCycleInformation']['timeSetIndex'] = 0
        self.side_effects_helper['FetchHistoryRAMCycleInformation']['vectorNumber'] = 9
        self.side_effects_helper['FetchHistoryRAMCycleInformation']['cycleNumber'] = 11
        self.side_effects_helper['FetchHistoryRAMCycleInformation']['numDutCycles'] = 1
        self.patched_library.niDigital_GetPatternName.side_effect = self.side_effects_helper.niDigital_GetPatternName
        self.side_effects_helper['GetPatternName']['name'] = 'new_pattern'
        self.patched_library.niDigital_GetTimeSetName.side_effect = self.side_effects_helper.niDigital_GetTimeSetName
        self.side_effects_helper['GetTimeSetName']['name'] = 't0'
        self.patched_library.niDigital_FetchHistoryRAMScanCycleNumber.side_effect = self.side_effects_helper.niDigital_FetchHistoryRAMScanCycleNumber
        self.side_effects_helper['FetchHistoryRAMScanCycleNumber']['scanCycleNumber'] = -1
        self.patched_library.niDigital_FetchHistoryRAMCyclePinData.side_effect = self.side_effects_helper.niDigital_FetchHistoryRAMCyclePinData
        self.side_effects_helper['FetchHistoryRAMCyclePinData']['actualNumPinData'] = 8
        self.side_effects_helper['FetchHistoryRAMCyclePinData']['expectedPinStates'] = [PinState.X.value] * 8
        self.side_effects_helper['FetchHistoryRAMCyclePinData']['actualPinStates'] = [PinState.NOT_A_PIN_STATE.value] * 8
        self.side_effects_helper['FetchHistoryRAMCyclePinData']['perPinPassFail'] = [True] * 8
        with nidigital.Session('') as session:
            history_ram_cycle_info = session.sites[1].fetch_history_ram_cycle_information(
                position=6,
                samples_to_read=-1)
            self.patched_library.niDigital_FetchHistoryRAMCycleInformation.assert_called_once()
            self.patched_library.niDigital_GetPatternName.assert_called()
            self.patched_library.niDigital_GetTimeSetName.assert_called()
            self.patched_library.niDigital_FetchHistoryRAMScanCycleNumber.assert_called_once()
            self.patched_library.niDigital_FetchHistoryRAMCyclePinData.assert_called()

        assert len(history_ram_cycle_info) == 1
        assert history_ram_cycle_info[0].vector_number == 9
        assert history_ram_cycle_info[0].cycle_number == 11

    # TODO(sbethur): When nidigital driver provides better simulation support (internal bug# 992370),
    #  this test should be converted to a system test. (GitHub issue# 1353).
    def test_fetch_history_ram_cycle_information_samples_to_read_too_much(self):

        self.patched_library.niDigital_GetHistoryRAMSampleCount.side_effect = self.side_effects_helper.niDigital_GetHistoryRAMSampleCount
        self.side_effects_helper['GetHistoryRAMSampleCount']['sampleCount'] = 7
        self.patched_library.niDigital_GetAttributeViBoolean.side_effect = self.side_effects_helper.niDigital_GetAttributeViBoolean
        self.side_effects_helper['GetAttributeViBoolean']['value'] = True  # history_ram_number_of_samples_is_finite

        with nidigital.Session('') as session:
            assert session.sites[1].get_history_ram_sample_count() == 7

            expected_error_description = (
                'position: Specified value = 3, samples_to_read: Specified value = 5; Samples available = 4.')
            with pytest.raises(ValueError, match=expected_error_description):
                session.sites[1].fetch_history_ram_cycle_information(position=3, samples_to_read=5)
