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

    # TODO(sbethur): When nidigital driver provides better simulation support (internal bug# 992370),
    #  this test should be converted to a system test.
    def test_fetch_history_ram_cycle_information_position_negative(self):

        self.patched_library.niDigital_GetHistoryRAMSampleCount.side_effect = self.side_effects_helper.niDigital_GetHistoryRAMSampleCount
        self.side_effects_helper['GetHistoryRAMSampleCount']['sampleCount'] = 7
        with nidigital.Session('') as session:
            with pytest.raises(ValueError, match='position should be greater than or equal to 0.'):
                session.fetch_history_ram_cycle_information(
                    site='site1',
                    position=-1,
                    samples_to_read=-1)

    # TODO(sbethur): When nidigital driver provides better simulation support (internal bug# 992370),
    #  this test should be converted to a system test. (GitHub issue# 1353).
    def test_fetch_history_ram_cycle_information_position_out_of_bound(self):

        self.patched_library.niDigital_GetHistoryRAMSampleCount.side_effect = self.side_effects_helper.niDigital_GetHistoryRAMSampleCount
        self.side_effects_helper['GetHistoryRAMSampleCount']['sampleCount'] = 7
        with nidigital.Session('') as session:
            with pytest.raises(ValueError, match='position: Specified value = 8, Maximum value = 6.'):
                session.fetch_history_ram_cycle_information(
                    site='site1',
                    position=8,
                    samples_to_read=-1)

    # TODO(sbethur): When nidigital driver provides better simulation support (internal bug# 992370),
    #  this test should be converted to a system test.  
    def test_fetch_history_ram_cycle_information_is_finite_invalid(self):

        self.patched_library.niDigital_GetHistoryRAMSampleCount.side_effect = self.side_effects_helper.niDigital_GetHistoryRAMSampleCount
        self.side_effects_helper['GetHistoryRAMSampleCount']['sampleCount'] = 7
        self.patched_library.niDigital_GetAttributeViBoolean.side_effect = self.side_effects_helper.niDigital_GetAttributeViBoolean
        self.side_effects_helper['GetAttributeViBoolean']['value'] = False # history_ram_number_of_samples_is_finite

        expected_error_description = (
            'Specifying -1 to fetch all History RAM samples is not supported when the digital pattern instrument '
            'is configured for continuous History RAM acquisition. You must specify an exact number of samples to fetch.')
        with nidigital.Session('') as session:
            with pytest.raises(RuntimeError, match=expected_error_description):
                session.fetch_history_ram_cycle_information(
                    site='site1',
                    position=0,
                    samples_to_read=-1)

    # TODO(sbethur): When nidigital driver provides better simulation support (internal bug# 992370),
    #  this test should be converted to a system test.  
    def test_fetch_history_ram_cycle_information_samples_to_read_too_much(self):

        self.patched_library.niDigital_GetHistoryRAMSampleCount.side_effect = self.side_effects_helper.niDigital_GetHistoryRAMSampleCount
        self.side_effects_helper['GetHistoryRAMSampleCount']['sampleCount'] = 7
        self.patched_library.niDigital_GetAttributeViBoolean.side_effect = self.side_effects_helper.niDigital_GetAttributeViBoolean
        self.side_effects_helper['GetAttributeViBoolean']['value'] = True # history_ram_number_of_samples_is_finite

        with nidigital.Session('') as session:
            site = 'site1'
            assert session.get_history_ram_sample_count(site) == 7

            expected_error_description = (
                'position: Specified value = 3, samples_to_read: Specified value = 5; Samples available = 4.')
            with pytest.raises(ValueError, match=expected_error_description):
                session.fetch_history_ram_cycle_information(
                    site=site,
                    position=3,
                    samples_to_read=5)

    # TODO(sbethur): When nidigital driver provides better simulation support (internal bug# 992370),
    #  this test should be converted to a system test.  
    def test_fetch_history_ram_cycle_information_samples_to_read_zero(self):

        self.patched_library.niDigital_GetHistoryRAMSampleCount.side_effect = self.side_effects_helper.niDigital_GetHistoryRAMSampleCount
        self.side_effects_helper['GetHistoryRAMSampleCount']['sampleCount'] = 7

        with nidigital.Session('') as session:
            history_ram_cycle_info = session.fetch_history_ram_cycle_information(
                site='site1',
                position=0,
                samples_to_read=0)

        assert len(history_ram_cycle_info) == 0
