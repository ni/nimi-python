import _mock_helper

import nidigital

import pytest
from unittest.mock import patch

session_id_for_test = 42


class TestSession(object):
    def setup_method(self, method):
        self.patched_library_patcher = patch(
            "nidigital._library.Library", autospec=True
        )
        self.patched_library = self.patched_library_patcher.start()
        self.patched_library_singleton_get = patch(
            "nidigital.session._library_singleton.get",
            return_value=self.patched_library,
        )
        self.patched_library_singleton_get.start()

        self.side_effects_helper = _mock_helper.SideEffectsHelper()
        self.side_effects_helper.set_side_effects_and_return_values(
            self.patched_library
        )

        self.patched_library.niDigital_InitWithOptions.side_effect = (
            self.side_effects_helper.niDigital_InitWithOptions
        )
        self.side_effects_helper["InitWithOptions"]["newVi"] = session_id_for_test

        self.patched_library.niDigital_close.side_effect = (
            self.side_effects_helper.niDigital_close
        )

        self.patched_library.niDigital_LockSession.side_effect = (
            self.side_effects_helper.niDigital_LockSession
        )
        self.side_effects_helper["LockSession"]["callerHasLock"] = True

        self.patched_library.niDigital_UnlockSession.side_effect = (
            self.side_effects_helper.niDigital_UnlockSession
        )
        self.side_effects_helper["UnlockSession"]["callerHasLock"] = True

        # for niDigital_FetchHistoryRAMCycleInformation_looping
        self.pattern_indices_looping = [0, 0, 0, 0, 0, 0, 0]
        self.time_set_indices_looping = [0, 1, 1, 2, 2, 2, 0]
        self.vector_numbers_looping = [5, 6, 6, 7, 7, 8, 9]
        self.cycle_numbers_looping = [5, 6, 7, 8, 9, 10, 11]
        self.num_duty_cycles_looping = [1, 1, 1, 2, 2, 2, 1]

        # for niDigital_GetTimeSetName_looping
        self.time_set_name_looping = ["t0", "tScan", "t2X"]

        # for niDigital_FetchHistoryRAMScanCycleNumber_looping
        self.scan_cycle_number_looping = [-1, 0, 1, -1, -1, -1, -1]

        # for niDigital_FetchHistoryRAMCyclePinData_looping
        self.expected_pin_states_looping = [
            [
                [
                    nidigital.PinState.ZERO,
                    nidigital.PinState.H,
                    nidigital.PinState.X,
                    nidigital.PinState.X,
                    nidigital.PinState.H,
                    nidigital.PinState.ZERO,
                    nidigital.PinState.X,
                    nidigital.PinState.X,
                ]
            ],
            [
                [
                    nidigital.PinState.X,
                    nidigital.PinState.X,
                    nidigital.PinState.ZERO,
                    nidigital.PinState.ONE,
                    nidigital.PinState.X,
                    nidigital.PinState.X,
                    nidigital.PinState.L,
                    nidigital.PinState.H,
                ]
            ],
            [
                [
                    nidigital.PinState.X,
                    nidigital.PinState.X,
                    nidigital.PinState.ONE,
                    nidigital.PinState.ZERO,
                    nidigital.PinState.X,
                    nidigital.PinState.X,
                    nidigital.PinState.H,
                    nidigital.PinState.L,
                ]
            ],
            [
                [
                    nidigital.PinState.ONE,
                    nidigital.PinState.ONE,
                    nidigital.PinState.X,
                    nidigital.PinState.X,
                    nidigital.PinState.H,
                    nidigital.PinState.H,
                    nidigital.PinState.X,
                    nidigital.PinState.X,
                ],
                [
                    nidigital.PinState.ZERO,
                    nidigital.PinState.ZERO,
                    nidigital.PinState.X,
                    nidigital.PinState.X,
                    nidigital.PinState.L,
                    nidigital.PinState.L,
                    nidigital.PinState.X,
                    nidigital.PinState.X,
                ],
            ],
            [
                [
                    nidigital.PinState.ONE,
                    nidigital.PinState.ONE,
                    nidigital.PinState.X,
                    nidigital.PinState.X,
                    nidigital.PinState.H,
                    nidigital.PinState.H,
                    nidigital.PinState.X,
                    nidigital.PinState.X,
                ],
                [
                    nidigital.PinState.ZERO,
                    nidigital.PinState.ZERO,
                    nidigital.PinState.X,
                    nidigital.PinState.X,
                    nidigital.PinState.L,
                    nidigital.PinState.L,
                    nidigital.PinState.X,
                    nidigital.PinState.X,
                ],
            ],
            [
                [
                    nidigital.PinState.ZERO,
                    nidigital.PinState.ONE,
                    nidigital.PinState.X,
                    nidigital.PinState.X,
                    nidigital.PinState.L,
                    nidigital.PinState.H,
                    nidigital.PinState.X,
                    nidigital.PinState.X,
                ],
                [
                    nidigital.PinState.ONE,
                    nidigital.PinState.ZERO,
                    nidigital.PinState.X,
                    nidigital.PinState.X,
                    nidigital.PinState.H,
                    nidigital.PinState.L,
                    nidigital.PinState.X,
                    nidigital.PinState.X,
                ],
            ],
            [
                [
                    nidigital.PinState.X,
                    nidigital.PinState.X,
                    nidigital.PinState.X,
                    nidigital.PinState.X,
                    nidigital.PinState.X,
                    nidigital.PinState.X,
                    nidigital.PinState.X,
                    nidigital.PinState.X,
                ]
            ],
        ]
        self.actual_pin_states_looping = [
            [
                [
                    nidigital.PinState.L,
                    nidigital.PinState.L,
                    nidigital.PinState.X,
                    nidigital.PinState.X,
                    nidigital.PinState.L,
                    nidigital.PinState.L,
                    nidigital.PinState.X,
                    nidigital.PinState.X,
                ]
            ],
            [
                [
                    nidigital.PinState.X,
                    nidigital.PinState.X,
                    nidigital.PinState.L,
                    nidigital.PinState.H,
                    nidigital.PinState.X,
                    nidigital.PinState.X,
                    nidigital.PinState.L,
                    nidigital.PinState.H,
                ]
            ],
            [
                [
                    nidigital.PinState.X,
                    nidigital.PinState.X,
                    nidigital.PinState.H,
                    nidigital.PinState.L,
                    nidigital.PinState.X,
                    nidigital.PinState.X,
                    nidigital.PinState.H,
                    nidigital.PinState.L,
                ]
            ],
            [
                [
                    nidigital.PinState.H,
                    nidigital.PinState.H,
                    nidigital.PinState.X,
                    nidigital.PinState.X,
                    nidigital.PinState.H,
                    nidigital.PinState.H,
                    nidigital.PinState.X,
                    nidigital.PinState.X,
                ],
                [
                    nidigital.PinState.L,
                    nidigital.PinState.L,
                    nidigital.PinState.X,
                    nidigital.PinState.X,
                    nidigital.PinState.L,
                    nidigital.PinState.L,
                    nidigital.PinState.X,
                    nidigital.PinState.X,
                ],
            ],
            [
                [
                    nidigital.PinState.H,
                    nidigital.PinState.H,
                    nidigital.PinState.X,
                    nidigital.PinState.X,
                    nidigital.PinState.H,
                    nidigital.PinState.H,
                    nidigital.PinState.X,
                    nidigital.PinState.X,
                ],
                [
                    nidigital.PinState.L,
                    nidigital.PinState.L,
                    nidigital.PinState.X,
                    nidigital.PinState.X,
                    nidigital.PinState.L,
                    nidigital.PinState.L,
                    nidigital.PinState.X,
                    nidigital.PinState.X,
                ],
            ],
            [
                [
                    nidigital.PinState.L,
                    nidigital.PinState.H,
                    nidigital.PinState.X,
                    nidigital.PinState.X,
                    nidigital.PinState.L,
                    nidigital.PinState.H,
                    nidigital.PinState.X,
                    nidigital.PinState.X,
                ],
                [
                    nidigital.PinState.H,
                    nidigital.PinState.L,
                    nidigital.PinState.X,
                    nidigital.PinState.X,
                    nidigital.PinState.H,
                    nidigital.PinState.L,
                    nidigital.PinState.X,
                    nidigital.PinState.X,
                ],
            ],
            [
                [
                    nidigital.PinState.X,
                    nidigital.PinState.X,
                    nidigital.PinState.X,
                    nidigital.PinState.X,
                    nidigital.PinState.X,
                    nidigital.PinState.X,
                    nidigital.PinState.X,
                    nidigital.PinState.X,
                ]
            ],
        ]
        self.per_pin_pass_fail_looping = [
            [[True, False, True, True, False, True, True, True]],
            [[True, True, True, True, True, True, True, True]],
            [[True, True, True, True, True, True, True, True]],
            [
                [True, True, True, True, True, True, True, True],
                [True, True, True, True, True, True, True, True],
            ],
            [
                [True, True, True, True, True, True, True, True],
                [True, True, True, True, True, True, True, True],
            ],
            [
                [True, True, True, True, True, True, True, True],
                [True, True, True, True, True, True, True, True],
            ],
            [[True, True, True, True, True, True, True, True]],
        ]

        # for niDigital_FetchHistoryRAMCyclePinData_check_pins_looping
        self.expected_pin_list_check_pins_looping = None
        self.expected_pin_states_check_pins_looping = [
            [[nidigital.PinState.ZERO, nidigital.PinState.H]]
        ]
        self.actual_pin_states_check_pins_looping = [
            [[nidigital.PinState.L, nidigital.PinState.L]]
        ]
        self.per_pin_pass_fail_check_pins_looping = [[[True, False]]]

        # for niDigital_GetHistoryRAMSampleCount_check_site_looping
        self.iteration_check_site_looping = 0
        self.site_numbers_looping = [0, 1, 2]

    def teardown_method(self, method):
        self.patched_library_singleton_get.stop()
        self.patched_library_patcher.stop()

    # API Tests

    # TODO(sbethur): When nidigital driver provides better simulation support (internal bug# 992370),
    #  this test should be converted to a system test. (GitHub issue# 1353).
    def test_fetch_history_ram_cycle_information_position_out_of_bound(self):

        self.patched_library.niDigital_GetHistoryRAMSampleCount.side_effect = (
            self.side_effects_helper.niDigital_GetHistoryRAMSampleCount
        )
        self.side_effects_helper["GetHistoryRAMSampleCount"]["sampleCount"] = 7
        with nidigital.Session("") as session:
            with pytest.raises(
                ValueError, match="position: Specified value = 8, Maximum value = 6."
            ):
                session.sites[1].fetch_history_ram_cycle_information(
                    position=8, samples_to_read=-1
                )

    # TODO(sbethur): When nidigital driver provides better simulation support (internal bug# 992370),
    #  this test should be converted to a system test. (GitHub issue# 1353).
    def test_fetch_history_ram_cycle_information_position_last(self):

        self.patched_library.niDigital_GetHistoryRAMSampleCount.side_effect = (
            self.side_effects_helper.niDigital_GetHistoryRAMSampleCount
        )
        self.side_effects_helper["GetHistoryRAMSampleCount"]["sampleCount"] = 7
        self.patched_library.niDigital_GetAttributeViBoolean.side_effect = (
            self.side_effects_helper.niDigital_GetAttributeViBoolean
        )
        self.side_effects_helper["GetAttributeViBoolean"][
            "value"
        ] = True  # history_ram_number_of_samples_is_finite
        self.patched_library.niDigital_FetchHistoryRAMCycleInformation.side_effect = (
            self.side_effects_helper.niDigital_FetchHistoryRAMCycleInformation
        )
        self.side_effects_helper["FetchHistoryRAMCycleInformation"]["patternIndex"] = 0
        self.side_effects_helper["FetchHistoryRAMCycleInformation"]["timeSetIndex"] = 0
        self.side_effects_helper["FetchHistoryRAMCycleInformation"]["vectorNumber"] = 9
        self.side_effects_helper["FetchHistoryRAMCycleInformation"]["cycleNumber"] = 11
        self.side_effects_helper["FetchHistoryRAMCycleInformation"]["numDutCycles"] = 1
        self.patched_library.niDigital_GetPatternName.side_effect = (
            self.side_effects_helper.niDigital_GetPatternName
        )
        self.side_effects_helper["GetPatternName"]["name"] = "new_pattern"
        self.patched_library.niDigital_GetTimeSetName.side_effect = (
            self.side_effects_helper.niDigital_GetTimeSetName
        )
        self.side_effects_helper["GetTimeSetName"]["name"] = "t0"
        self.patched_library.niDigital_FetchHistoryRAMScanCycleNumber.side_effect = (
            self.side_effects_helper.niDigital_FetchHistoryRAMScanCycleNumber
        )
        self.side_effects_helper["FetchHistoryRAMScanCycleNumber"][
            "scanCycleNumber"
        ] = -1
        self.patched_library.niDigital_FetchHistoryRAMCyclePinData.side_effect = (
            self.side_effects_helper.niDigital_FetchHistoryRAMCyclePinData
        )
        self.side_effects_helper["FetchHistoryRAMCyclePinData"]["actualNumPinData"] = 8
        self.side_effects_helper["FetchHistoryRAMCyclePinData"]["expectedPinStates"] = [
            nidigital.PinState.X.value
        ] * 8
        self.side_effects_helper["FetchHistoryRAMCyclePinData"]["actualPinStates"] = [
            nidigital.PinState.NOT_A_PIN_STATE.value
        ] * 8
        self.side_effects_helper["FetchHistoryRAMCyclePinData"]["perPinPassFail"] = [
            True
        ] * 8
        with nidigital.Session("") as session:
            history_ram_cycle_info = session.sites[
                1
            ].fetch_history_ram_cycle_information(position=6, samples_to_read=-1)
            self.patched_library.niDigital_FetchHistoryRAMCycleInformation.assert_called_once()
            assert self.patched_library.niDigital_GetPatternName.call_count == 2
            assert self.patched_library.niDigital_GetTimeSetName.call_count == 2
            self.patched_library.niDigital_FetchHistoryRAMScanCycleNumber.assert_called_once()
            assert (
                self.patched_library.niDigital_FetchHistoryRAMCyclePinData.call_count
                == 2
            )

        assert len(history_ram_cycle_info) == 1
        assert history_ram_cycle_info[0].vector_number == 9
        assert history_ram_cycle_info[0].cycle_number == 11

    # TODO(sbethur): When nidigital driver provides better simulation support (internal bug# 992370),
    #  this test should be converted to a system test. (GitHub issue# 1353).
    def test_fetch_history_ram_cycle_information_samples_to_read_too_much(self):

        self.patched_library.niDigital_GetHistoryRAMSampleCount.side_effect = (
            self.side_effects_helper.niDigital_GetHistoryRAMSampleCount
        )
        self.side_effects_helper["GetHistoryRAMSampleCount"]["sampleCount"] = 7
        self.patched_library.niDigital_GetAttributeViBoolean.side_effect = (
            self.side_effects_helper.niDigital_GetAttributeViBoolean
        )
        self.side_effects_helper["GetAttributeViBoolean"][
            "value"
        ] = True  # history_ram_number_of_samples_is_finite

        with nidigital.Session("") as session:
            assert session.sites[1].get_history_ram_sample_count() == 7

            expected_error_description = "position: Specified value = 3, samples_to_read: Specified value = 5; Samples available = 4."
            with pytest.raises(ValueError, match=expected_error_description):
                session.sites[1].fetch_history_ram_cycle_information(
                    position=3, samples_to_read=5
                )

    # Helper function for mocking multiple calls
    def niDigital_FetchHistoryRAMCycleInformation_looping(
        self,
        vi,
        site,
        sample_index,
        pattern_index,
        time_set_index,
        vector_number,
        cycle_number,
        num_dut_cycles,
    ):  # noqa: N802
        sample_index_int = int(sample_index.value)
        pattern_index.contents.value = self.pattern_indices_looping[sample_index_int]
        time_set_index.contents.value = self.time_set_indices_looping[sample_index_int]
        vector_number.contents.value = self.vector_numbers_looping[sample_index_int]
        cycle_number.contents.value = self.cycle_numbers_looping[sample_index_int]
        num_dut_cycles.contents.value = self.num_duty_cycles_looping[sample_index_int]
        return 0

    # Helper function for mocking multiple calls
    def niDigital_GetTimeSetName_looping(
        self, vi, time_set_index, name_buffer_size, name
    ):  # noqa: N802
        time_set_index_int = int(time_set_index.value)
        if int(name_buffer_size.value) == 0:
            return len(self.time_set_name_looping[time_set_index_int])
        bytes_to_copy = self.time_set_name_looping[time_set_index_int].encode("ascii")
        for i in range(0, len(bytes_to_copy)):
            name[i] = bytes_to_copy[i]
        return 0

    # Helper function for mocking multiple calls
    def niDigital_FetchHistoryRAMScanCycleNumber_looping(
        self, vi, site, sample_index, scan_cycle_number
    ):  # noqa: N802
        sample_index_int = int(sample_index.value)
        scan_cycle_number.contents.value = self.scan_cycle_number_looping[
            sample_index_int
        ]
        return 0

    # Helper function for mocking multiple calls
    def niDigital_FetchHistoryRAMCyclePinData_looping(
        self,
        vi,
        site,
        pin_list,
        sample_index,
        dut_cycle_index,
        pin_data_buffer_size,
        expected_pin_states,
        actual_pin_states,
        per_pin_pass_fail,
        actual_num_pin_data,
    ):  # noqa: N802
        sample_index_int = int(sample_index.value)
        dut_cycle_index_int = int(dut_cycle_index.value)
        if int(pin_data_buffer_size.value) == 0:
            actual_num_pin_data.contents.value = len(
                self.expected_pin_states_looping[sample_index_int][dut_cycle_index_int]
            )
            return actual_num_pin_data.contents.value
        for i in range(0, int(pin_data_buffer_size.value)):
            expected_pin_states[i] = self.expected_pin_states_looping[sample_index_int][
                dut_cycle_index_int
            ][i].value
            actual_pin_states[i] = self.actual_pin_states_looping[sample_index_int][
                dut_cycle_index_int
            ][i].value
            per_pin_pass_fail[i] = self.per_pin_pass_fail_looping[sample_index_int][
                dut_cycle_index_int
            ][i]
        return 0

    # TODO(sbethur): When nidigital driver provides better simulation support (internal bug# 992370),
    #  this test should be converted to a system test. (GitHub issue# 1353).
    def test_fetch_history_ram_cycle_information_samples_to_read_all(self):

        self.patched_library.niDigital_GetHistoryRAMSampleCount.side_effect = (
            self.side_effects_helper.niDigital_GetHistoryRAMSampleCount
        )
        self.side_effects_helper["GetHistoryRAMSampleCount"]["sampleCount"] = 7
        self.patched_library.niDigital_GetAttributeViBoolean.side_effect = (
            self.side_effects_helper.niDigital_GetAttributeViBoolean
        )
        self.side_effects_helper["GetAttributeViBoolean"][
            "value"
        ] = True  # history_ram_number_of_samples_is_finite
        self.patched_library.niDigital_FetchHistoryRAMCycleInformation.side_effect = (
            self.niDigital_FetchHistoryRAMCycleInformation_looping
        )
        self.patched_library.niDigital_GetPatternName.side_effect = (
            self.side_effects_helper.niDigital_GetPatternName
        )
        self.side_effects_helper["GetPatternName"]["name"] = "new_pattern"
        self.patched_library.niDigital_GetTimeSetName.side_effect = (
            self.niDigital_GetTimeSetName_looping
        )
        self.patched_library.niDigital_FetchHistoryRAMScanCycleNumber.side_effect = (
            self.niDigital_FetchHistoryRAMScanCycleNumber_looping
        )
        self.patched_library.niDigital_FetchHistoryRAMCyclePinData.side_effect = (
            self.niDigital_FetchHistoryRAMCyclePinData_looping
        )
        self.patched_library.niDigital_GetPatternPinList.side_effect = (
            self.side_effects_helper.niDigital_GetPatternPinList
        )
        pin_list = ["LO" + str(i) for i in range(4)] + ["HI" + str(i) for i in range(4)]
        self.side_effects_helper["GetPatternPinList"]["pinList"] = ",".join(pin_list)
        with nidigital.Session("") as session:
            history_ram_cycle_info = session.sites[
                1
            ].fetch_history_ram_cycle_information(position=0, samples_to_read=-1)
            assert (
                self.patched_library.niDigital_FetchHistoryRAMCycleInformation.call_count
                == 7
            )
            assert (
                self.patched_library.niDigital_GetPatternName.call_count == 2
            )  # there's only one pattern, so this is a 2
            assert (
                self.patched_library.niDigital_GetTimeSetName.call_count == 6
            )  # 3 time sets, so this is a 6
            assert (
                self.patched_library.niDigital_FetchHistoryRAMScanCycleNumber.call_count
                == 7
            )
            assert (
                self.patched_library.niDigital_FetchHistoryRAMCyclePinData.call_count
                == 20
            )  # 10 DUT cycles

            assert len(history_ram_cycle_info) == 7
            assert all(
                [i.pattern_name == "new_pattern" for i in history_ram_cycle_info]
            )

            time_set_names = [i.time_set_name for i in history_ram_cycle_info]
            assert time_set_names == ["t0", "tScan", "tScan", "t2X", "t2X", "t2X", "t0"]

            vector_numbers = [i.vector_number for i in history_ram_cycle_info]
            assert vector_numbers == [5, 6, 6, 7, 7, 8, 9]

            cycle_numbers = [i.cycle_number for i in history_ram_cycle_info]
            assert cycle_numbers == list(range(5, 12))

            scan_cycle_numbers = [i.scan_cycle_number for i in history_ram_cycle_info]
            assert scan_cycle_numbers == [-1, 0, 1, -1, -1, -1, -1]

            pin_names = session.get_pattern_pin_names("new_pattern")
            assert self.patched_library.niDigital_GetPatternPinList.call_count == 2
            assert pin_names == pin_list

        expected_pin_states = [i.expected_pin_states for i in history_ram_cycle_info]
        assert expected_pin_states == self.expected_pin_states_looping

        # If test expects actual pin state to be 'X', then value returned by the API can be anything.
        # So, need to skip those pin states while comparing.
        actual_pin_states = [i.actual_pin_states for i in history_ram_cycle_info]
        assert len(actual_pin_states) == len(self.actual_pin_states_looping)
        for vector_pin_states, vector_pin_states_expected_by_test in zip(
            actual_pin_states, self.actual_pin_states_looping
        ):
            for cycle_pin_states, cycle_pin_states_expected_by_test in zip(
                vector_pin_states, vector_pin_states_expected_by_test
            ):
                for pin_state, pin_state_expected_by_test in zip(
                    cycle_pin_states, cycle_pin_states_expected_by_test
                ):
                    if pin_state_expected_by_test is not nidigital.PinState.X:
                        assert pin_state == pin_state_expected_by_test

        # Only the first cycle returned is expected to have failures
        per_pin_pass_fail = [i.per_pin_pass_fail for i in history_ram_cycle_info]
        assert per_pin_pass_fail == self.per_pin_pass_fail_looping

    # Helper function for validating pin list behavior in fetch_history_ram_cycle_information.
    def niDigital_FetchHistoryRAMCyclePinData_check_pins_looping(
        self,
        vi,
        site,
        pin_list,
        sample_index,
        dut_cycle_index,
        pin_data_buffer_size,
        expected_pin_states,
        actual_pin_states,
        per_pin_pass_fail,
        actual_num_pin_data,
    ):  # noqa: N802
        sample_index_int = int(sample_index.value)
        dut_cycle_index_int = int(dut_cycle_index.value)
        if int(pin_data_buffer_size.value) == 0:
            actual_num_pin_data.contents.value = len(
                self.expected_pin_states_check_pins_looping[sample_index_int][
                    dut_cycle_index_int
                ]
            )
            return actual_num_pin_data.contents.value
        for i in range(0, int(pin_data_buffer_size.value)):
            expected_pin_states[i] = self.expected_pin_states_check_pins_looping[
                sample_index_int
            ][dut_cycle_index_int][i].value
            actual_pin_states[i] = self.actual_pin_states_check_pins_looping[
                sample_index_int
            ][dut_cycle_index_int][i].value
            per_pin_pass_fail[i] = self.per_pin_pass_fail_check_pins_looping[
                sample_index_int
            ][dut_cycle_index_int][i]
        assert self.expected_pin_list_check_pins_looping is not None
        assert (
            pin_list.value.decode("ascii") == self.expected_pin_list_check_pins_looping
        )
        return 0

    def test_fetch_history_ram_cycle_information_pin_list(self):

        self.patched_library.niDigital_GetHistoryRAMSampleCount.side_effect = (
            self.side_effects_helper.niDigital_GetHistoryRAMSampleCount
        )
        self.side_effects_helper["GetHistoryRAMSampleCount"]["sampleCount"] = 1
        self.patched_library.niDigital_GetAttributeViBoolean.side_effect = (
            self.side_effects_helper.niDigital_GetAttributeViBoolean
        )
        self.side_effects_helper["GetAttributeViBoolean"][
            "value"
        ] = True  # history_ram_number_of_samples_is_finite
        self.patched_library.niDigital_FetchHistoryRAMCycleInformation.side_effect = (
            self.side_effects_helper.niDigital_FetchHistoryRAMCycleInformation
        )
        self.side_effects_helper["FetchHistoryRAMCycleInformation"]["patternIndex"] = 0
        self.side_effects_helper["FetchHistoryRAMCycleInformation"]["timeSetIndex"] = 0
        self.side_effects_helper["FetchHistoryRAMCycleInformation"]["vectorNumber"] = 0
        self.side_effects_helper["FetchHistoryRAMCycleInformation"]["cycleNumber"] = 0
        self.side_effects_helper["FetchHistoryRAMCycleInformation"]["numDutCycles"] = 1
        self.patched_library.niDigital_GetPatternName.side_effect = (
            self.side_effects_helper.niDigital_GetPatternName
        )
        self.side_effects_helper["GetPatternName"]["name"] = "new_pattern"
        self.patched_library.niDigital_GetTimeSetName.side_effect = (
            self.side_effects_helper.niDigital_GetTimeSetName
        )
        self.side_effects_helper["GetTimeSetName"]["name"] = "t0"
        self.patched_library.niDigital_FetchHistoryRAMScanCycleNumber.side_effect = (
            self.side_effects_helper.niDigital_FetchHistoryRAMScanCycleNumber
        )
        self.side_effects_helper["FetchHistoryRAMScanCycleNumber"][
            "scanCycleNumber"
        ] = -1
        self.patched_library.niDigital_FetchHistoryRAMCyclePinData.side_effect = (
            self.niDigital_FetchHistoryRAMCyclePinData_check_pins_looping
        )
        with nidigital.Session("") as session:
            self.expected_pin_list_check_pins_looping = "PinA,PinB"
            session.sites[0].pins["PinA", "PinB"].fetch_history_ram_cycle_information(
                position=0, samples_to_read=-1
            )
            self.expected_pin_list_check_pins_looping = ""
            session.sites[0].fetch_history_ram_cycle_information(
                position=0, samples_to_read=-1
            )
            assert (
                self.patched_library.niDigital_FetchHistoryRAMCyclePinData.call_count
                == 4
            )

    # Helper function for validating site behavior in fetch_history_ram_cycle_information.
    def niDigital_GetHistoryRAMSampleCount_check_site_looping(
        self, vi, site, sample_count
    ):  # noqa: N802
        assert site.value.decode("ascii") == "site{}".format(
            self.site_numbers_looping[self.iteration_check_site_looping]
        )
        sample_count.contents.value = (
            0  # we don't care if this is right as long as the fetch does not error
        )
        self.iteration_check_site_looping += 1
        return 0

    def test_fetch_history_ram_cycle_information_site_n(self):

        self.patched_library.niDigital_GetHistoryRAMSampleCount.side_effect = (
            self.niDigital_GetHistoryRAMSampleCount_check_site_looping
        )
        self.side_effects_helper["GetHistoryRAMSampleCount"]["sampleCount"] = 1

        with nidigital.Session("") as session:
            for s in self.site_numbers_looping:
                session.sites[s].fetch_history_ram_cycle_information(
                    position=0, samples_to_read=0
                )
            assert (
                self.patched_library.niDigital_GetHistoryRAMSampleCount.call_count
                == len(self.site_numbers_looping)
            )

    def test_pin_state_enum_print(self):

        assert str(nidigital.PinState.ZERO) == "0"
        assert str(nidigital.PinState.ONE) == "1"
        assert str(nidigital.PinState.NOT_A_PIN_STATE) == "Not a Pin State"
        assert (
            str(nidigital.PinState.PIN_STATE_NOT_ACQUIRED) == "Pin State Not Acquired"
        )
        assert str(nidigital.PinState.L) == "L"
        assert str(nidigital.PinState.H) == "H"
        assert str(nidigital.PinState.X) == "X"
        assert str(nidigital.PinState.M) == "M"
        assert str(nidigital.PinState.V) == "V"
        assert str(nidigital.PinState.D) == "D"
        assert str(nidigital.PinState.E) == "E"

    def test_write_static_pin_state_enum_print(self):

        assert str(nidigital.WriteStaticPinState.ZERO) == "0"
        assert str(nidigital.WriteStaticPinState.ONE) == "1"
        assert str(nidigital.WriteStaticPinState.X) == "X"
