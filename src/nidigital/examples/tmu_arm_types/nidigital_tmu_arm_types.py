"""
Demonstrates the difference between Immediate and Edge arm types for TMU
measurements using the NI-Digital Pattern Driver API. This example shows:
        - Immediate arm: the TMU begins looking for start/stop events as soon as
            tmu_initiate is called. When start and stop events differ (e.g., duty
            cycle), the detection order is not guaranteed on a free-running signal,
            which can produce negative measurements
        - Edge arm: the TMU waits for a specific arm event before looking for
            start/stop events, guaranteeing deterministic event ordering and
            consistent (positive) measurements
        - The constraint that edge arm source/event/polarity must match either the
            start or stop source configuration

Both sections measure the same quantity (duty cycle high) on the same channel
so the behavioral difference between the two arm types is clearly visible.

Note: The DUT must be generating signals on the configured channel for TMU
measurements to complete. In simulate mode, the driver returns simulated
measurement values.
"""

from pathlib import Path

import nidigital


RESOURCE_NAME = "PXI1Slot5"
OPTIONS = {"Simulate": True, "DriverSetup": {"Model": "6571"}}
PIN_MAP_PATH = Path(__file__).with_name("PinMap.pinmap")


def main():
    # Initial Device Values
    dut_pin1 = "DUTPin1"

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

        # Select each TMU from its instrument context so nimi-python constructs
        # the fully qualified names PXI1Slot5/tmu0 and PXI1Slot5/tmu1.
        instrument = session.instruments[RESOURCE_NAME]
        immediate_tmu = instrument.time_measurement_units[0]
        edge_tmu = instrument.time_measurement_units[1]

        # ===================================================================
        # Part 1: Duty Cycle High with Immediate Arm
        # ===================================================================
        # With Immediate arm, the TMU begins looking for start and stop events
        # as soon as tmu_initiate is called. Because the start event (VOH Rising
        # Edge) and stop event (VOH Falling Edge) are different, the first
        # event detected after initiation could be either one.
        #
        # If the stop event (Falling Edge) happens to be detected first, the
        # measurement result will be NEGATIVE, indicating the stop timestamp
        # preceded the start timestamp. This is the fundamental ambiguity of
        # Immediate arm with non-identical start/stop events on a free-running
        # periodic signal.
        print("=== Part 1: Duty Cycle High with IMMEDIATE Arm (TMU0) ===\n")
        immediate_tmu.tmu_enabled = True
        immediate_tmu.tmu_arm_type = nidigital.enums.TMUArmType.IMMEDIATE

        # Configure Immediate arm type on TMU0.
        immediate_tmu.tmu_start_source = dut_pin1
        immediate_tmu.tmu_start_source_event = nidigital.enums.TMUSourceEvent.VOH
        immediate_tmu.tmu_start_source_event_polarity = nidigital.enums.TMUPolarity.RISING
        immediate_tmu.tmu_stop_source = dut_pin1
        immediate_tmu.tmu_stop_source_event = nidigital.enums.TMUSourceEvent.VOH
        immediate_tmu.tmu_stop_source_event_polarity = nidigital.enums.TMUPolarity.FALLING
        immediate_tmu.tmu_samples_to_acquire = 100
        immediate_tmu.tmu_sample_timeout = 10.0

        # ===================================================================
        # Part 2: Duty Cycle High with Edge Arm
        # ===================================================================
        # With Edge arm, the TMU waits for a specific arm event before it begins
        # looking for start/stop events. This eliminates the ambiguity of
        # Immediate arm by establishing a known starting point in the signal
        # cycle.
        #
        # Here we configure the arm to match the start source (DUTPin1, VOH,
        # Rising Edge). The sequence is:
        #   1. TMU waits for arm event (Rising Edge at VOH on DUTPin1)
        #   2. Arm event is captured as the start event
        #   3. TMU then waits for the stop event (Falling Edge at VOH)
        #   4. Measurement = stop timestamp - start timestamp (always positive)
        #
        # IMPORTANT CONSTRAINT: The edge arm source, event, and polarity must
        # match either the start or stop source configuration. If they do not
        # match, the driver returns an error.
        print("\n=== Part 2: Duty Cycle High with EDGE Arm (TMU1) ===\n")
        edge_tmu.tmu_enabled = True
        edge_tmu.tmu_arm_type = nidigital.enums.TMUArmType.EDGE

        # Configure Edge arm type on TMU1.
        edge_tmu.tmu_start_source = dut_pin1
        edge_tmu.tmu_start_source_event = nidigital.enums.TMUSourceEvent.VOH
        edge_tmu.tmu_start_source_event_polarity = nidigital.enums.TMUPolarity.RISING
        edge_tmu.tmu_stop_source = dut_pin1
        edge_tmu.tmu_stop_source_event = nidigital.enums.TMUSourceEvent.VOH
        edge_tmu.tmu_stop_source_event_polarity = nidigital.enums.TMUPolarity.FALLING
        edge_tmu.tmu_samples_to_acquire = 100
        edge_tmu.tmu_sample_timeout = 10.0

        # Configure the edge arm to match the start source. This guarantees the
        # rising edge (start) is always captured before the falling edge (stop),
        # producing a consistent positive measurement.
        edge_tmu.tmu_edge_arm_source = dut_pin1
        edge_tmu.tmu_edge_arm_source_event = nidigital.enums.TMUSourceEvent.VOH
        edge_tmu.tmu_edge_arm_polarity = nidigital.enums.TMUPolarity.RISING

        # Initiate both TMUs back-to-back. By initiating both TMUs consecutively,
        # they begin acquiring measurements on the same signal nearly
        # simultaneously.
        immediate_tmu.tmu_initiate()
        edge_tmu.tmu_initiate()
        immediate_measurement = immediate_tmu.tmu_fetch_averaged_measurement(10.0)
        edge_measurement = edge_tmu.tmu_fetch_averaged_measurement(10.0)

        # The Immediate arm result may be positive or negative. A negative value
        # means the falling edge (stop) was detected before the rising edge
        # (start). This is expected with Immediate arm on a free-running signal
        # when start and stop events differ.
        print(f"Immediate Arm (TMU0) - Duty Cycle High: {immediate_measurement:.6e} seconds")

        # With Edge arm, the result is always positive because the arm event
        # guarantees the start event is captured before the stop event.
        print(f"Edge Arm (TMU1) - Duty Cycle High: {edge_measurement:.6e} seconds")

        immediate_tmu.tmu_abort()
        edge_tmu.tmu_abort()

        # Disconnect all channels using programmable onboard switching.
        session.pins[""].selected_function = nidigital.enums.SelectedFunction.DISCONNECT


if __name__ == "__main__":
    main()
