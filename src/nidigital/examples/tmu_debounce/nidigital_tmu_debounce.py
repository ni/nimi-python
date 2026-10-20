"""
Demonstrates how to use the NI-Digital Pattern Driver API to configure TMU
input debounce filtering. This example shows:
        - Configuring debounce times for start and stop inputs
        - The constraint that when the start source and stop source are the same
            channel, the start and stop debounce times must be equal
        - When start and stop sources are different channels, the debounce times
            can be configured independently

Debounce filtering helps reject noise and glitches on the TMU input signals by
requiring the signal to remain stable for the configured debounce time before a
threshold crossing is recognized as a valid event.

Note: In simulate mode, the driver returns simulated measurement values.
"""

from pathlib import Path

import nidigital


RESOURCE_NAME = "PXI1Slot5"
OPTIONS = {"Simulate": True, "DriverSetup": {"Model": "6571"}}
PIN_MAP_PATH = Path(__file__).with_name("PinMap.pinmap")


def main():
    # Initial Device Values
    dut_pin1 = "DUTPin1"
    dut_pin2 = "DUTPin2"

    # Initialize the digital pattern instrument session. The reset input is
    # TRUE to ensure the instrument starts in a known state.
    with nidigital.Session(
        RESOURCE_NAME, id_query=True, reset_device=True, options=OPTIONS
    ) as session:
        # Load the pin map for the instrument to allow referencing of pin names
        # in the channel list of select driver functions.
        session.load_pin_map(str(PIN_MAP_PATH))

        # Configure voltage levels for all channels. The VOL and VOH levels
        # define the thresholds used by the TMU for SOURCE_EVENT_VOL and
        # SOURCE_EVENT_VOH events respectively.
        session.configure_voltage_levels(0.0, 5.0, 0.5, 2.4, 0.0)

        instrument = session.instruments[RESOURCE_NAME]
        tmu = instrument.time_measurement_units[0]

        # ===================================================================
        # Example 1: Same Channel - Debounce Times Must Be Equal
        # ===================================================================
        # When the TMU start source and stop source are configured to the same
        # channel, the start input debounce time and stop input debounce time
        # MUST be set to the same value. If they differ, the driver returns an
        # error.
        #
        # This constraint exists because the same physical input path is used
        # for both start and stop events when they share a channel, so only one
        # debounce filter setting can be applied.
        print("--- Example 1: Same Channel Debounce (Equal Times) ---")
        tmu.tmu_enabled = True
        tmu.tmu_arm_type = nidigital.enums.TMUArmType.IMMEDIATE

        # Configure start and stop to the SAME channel (DUTPin1). This is a
        # Period measurement configuration.
        tmu.tmu_start_source = dut_pin1
        tmu.tmu_start_source_event = nidigital.enums.TMUSourceEvent.VOL
        tmu.tmu_start_source_event_polarity = nidigital.enums.TMUPolarity.RISING
        tmu.tmu_stop_source = dut_pin1
        tmu.tmu_stop_source_event = nidigital.enums.TMUSourceEvent.VOL
        tmu.tmu_stop_source_event_polarity = nidigital.enums.TMUPolarity.RISING
        tmu.tmu_samples_to_acquire = 100
        tmu.tmu_sample_timeout = 10.0

        # Set debounce times for both start and stop inputs to the SAME value.
        # Since start and stop sources are on the same channel, these must be
        # equal. Setting different values would cause an error. A debounce time
        # of 200ns filters out glitches shorter than 200ns.
        tmu.tmu_start_input_debounce_time = 200e-9
        tmu.tmu_stop_input_debounce_time = 200e-9
        print("Same channel (DUTPin1): start debounce = 200 ns, stop debounce = 200 ns")
        tmu.tmu_initiate()
        measurement1 = tmu.tmu_fetch_averaged_measurement(10.0)
        print(f"Period measurement with debounce: {measurement1:.6e} seconds")
        tmu.tmu_abort()

        # ===================================================================
        # Example 2: Different Channels - Independent Debounce Times
        # ===================================================================
        # When the TMU start source and stop source are configured to different
        # channels, the start and stop debounce times can be configured
        # independently. Each channel has its own physical input path, so each
        # can have a different debounce filter setting.
        print("\n--- Example 2: Different Channels Debounce (Independent Times) ---")
        tmu.tmu_enabled = True
        tmu.tmu_arm_type = nidigital.enums.TMUArmType.IMMEDIATE

        # Configure start and stop to DIFFERENT channels. This is a Skew
        # measurement configuration.
        tmu.tmu_start_source = dut_pin1
        tmu.tmu_start_source_event = nidigital.enums.TMUSourceEvent.VOL
        tmu.tmu_start_source_event_polarity = nidigital.enums.TMUPolarity.RISING
        tmu.tmu_stop_source = dut_pin2
        tmu.tmu_stop_source_event = nidigital.enums.TMUSourceEvent.VOL
        tmu.tmu_stop_source_event_polarity = nidigital.enums.TMUPolarity.RISING
        tmu.tmu_samples_to_acquire = 100
        tmu.tmu_sample_timeout = 10.0

        # Set DIFFERENT debounce times for start and stop inputs. This is
        # allowed because the start and stop sources are on different channels.
        # Each channel's input path has its own independent debounce filter.
        # Start debounce: 200ns - signal on DUTPin1 must be stable for 200ns.
        # Stop debounce: 500ns - signal on DUTPin2 must be stable for 500ns.
        tmu.tmu_start_input_debounce_time = 200e-9
        tmu.tmu_stop_input_debounce_time = 500e-9
        print("Different channels: start (DUTPin1) debounce = 200 ns, stop (DUTPin2) debounce = 500 ns")
        tmu.tmu_initiate()
        measurement2 = tmu.tmu_fetch_averaged_measurement(10.0)
        print(f"Skew measurement with independent debounce: {measurement2:.6e} seconds")
        tmu.tmu_abort()

        session.pins[""].selected_function = nidigital.enums.SelectedFunction.DISCONNECT


if __name__ == "__main__":
    main()