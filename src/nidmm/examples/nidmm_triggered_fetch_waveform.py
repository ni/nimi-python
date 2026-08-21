#!/usr/bin/env python3
"""NI-DMM Triggered Fetch Waveform.

This example demonstrates how to take a waveform voltage measurement on two
NI-DMMs synchronized via PXI_TRIG0.

Since DMMs are incapable of sourcing a trigger by themselves, an NI-DCPower
SMU is used to route its SourceCompleteEvent to PXI_TRIG0. Both DMMs wait
on this trigger line before starting their waveform acquisition.

The SMU is configured in Sequence source mode with a single voltage step.
When the SMU completes sourcing, it fires the trigger that starts both DMMs.

Note: SMU and DMMs must be in the same PXI chassis to share PXI_TRIG0. Also,
preferably on the same bus of the PXI chassis, to avoid any issues with timing
and synchronization.

The example uses the default resource names and measurement parameters.
Modify these values as needed for your measurement setup.

HOW TO RUN:
-----------
i.   From terminal (with default values):
        python nidmm_triggered_fetch_waveform.py

ii.  From terminal (with custom values):
        python nidmm_triggered_fetch_waveform.py \
            -srn "PXI1Slot1" -d1rn "PXI1Slot2" -d2rn "PXI1Slot3" \
            -vl 2.0 -cl 0.01 -mrl 100 -at 0.1 -dr 10 -drt 1e6 -dwp 50

iii. To simulate without hardware:
        PowerShell:  python nidmm_triggered_fetch_waveform.py \
            -sop 'Simulate=1, DriverSetup=Model:4139; BoardType:PXIe' \
            -dop 'Simulate=1, DriverSetup=Model:4081'
        cmd.exe:     python nidmm_triggered_fetch_waveform.py \
            -sop "Simulate=1, DriverSetup=Model:4139; BoardType:PXIe" \
            -dop "Simulate=1, DriverSetup=Model:4081"

"""

# Module imports
import argparse    # For parsing command-line arguments
import sys         # For accessing command-line arguments via sys.argv

import nidcpower   # NI-DCPower instrument driver (SMU trigger source)

import nidmm       # NI-DMM instrument driver


def example(
    smu_resource_name, dmm1_resource_name, dmm2_resource_name,
    smu_options, dmm_options,
    voltage_level, current_limit, measure_record_length, aperture_time,
    dmm_range, dmm_rate, dmm_waveform_points
):
    """Perform a triggered waveform voltage measurement on two NI-DMMs via PXI_TRIG0.

    Synchronized via PXI_TRIG0 sourced by an NI-DCPower SMU SourceCompleteEvent.

    Args:
        smu_resource_name (str):
            NI-DCPower device identifier for the SMU (eg: "PXI1Slot1")

        dmm1_resource_name (str):
            NI-DMM device identifier for DMM 1 (eg: "PXI1Slot2")

        dmm2_resource_name (str):
            NI-DMM device identifier for DMM 2 (eg: "PXI1Slot3")

        smu_options (str or dict):
            SMU driver options, eg: "" for real HW or simulate string for simulation

        dmm_options (str or dict):
            DMM driver options, eg: "" for real HW or simulate string for simulation

        voltage_level (float):
            SMU output voltage level (V)
            eg: 2.0 → 2 V

        current_limit (float):
            SMU current limit (A)
            eg: 0.01 → 10 mA

        measure_record_length (int):
            Number of measurement samples in the SMU measure record
            eg: 100 → 100 samples

        aperture_time (float):
            SMU aperture time per sample (s)
            eg: 0.1 → 100 ms

        dmm_range (float):
            DMM voltage measurement range (V)
            eg: 10 → ±10 V range

        dmm_rate (float):
            DMM waveform acquisition rate (S/s)
            eg: 1e6 → 1 MS/s

        dmm_waveform_points (int):
            Number of waveform points per DMM acquisition
            eg: 50 → 50 points per acquisition

    Returns:
        None — results are printed to console
    """

    # -> Initialize SMU and DMM Sessions
    # - Opens communication with all three instruments
    # - 'with' ensures automatic cleanup of session resources
    with (
        nidcpower.Session(
            resource_name=smu_resource_name,
            channels=None,
            reset=False,
            options=smu_options,
            independent_channels=True,
        ) as smu_session,
        nidmm.Session(
            resource_name=dmm1_resource_name,
            id_query=False,
            reset_device=False,
            options=dmm_options,
        ) as dmm1_session,
        nidmm.Session(
            resource_name=dmm2_resource_name,
            id_query=False,
            reset_device=False,
            options=dmm_options,
        ) as dmm2_session,
    ):

        # -> Configure SMU Channel Settings
        # - source_mode     → SEQUENCE (single-point sequence fires SourceCompleteEvent)
        # - output_function → DC_VOLTAGE
        # - Single voltage step; source_delays=[0.0] — no delay before sourcing
        smu_session.source_mode = nidcpower.SourceMode.SEQUENCE
        smu_session.output_function = nidcpower.OutputFunction.DC_VOLTAGE
        smu_session.voltage_level_autorange = True
        smu_session.current_limit_autorange = True
        smu_session.current_limit = current_limit
        smu_session.set_sequence(values=[voltage_level], source_delays=[0.0])

        smu_session.measure_record_length = measure_record_length
        smu_session.aperture_time = aperture_time

        # -> Configure SMU Trigger Settings
        # - source_trigger_type → NONE (SMU advances without waiting for an external trigger)
        # - Route SourceCompleteEvent to PXI_TRIG0 to synchronize both DMMs
        smu_session.source_trigger_type = nidcpower.TriggerType.NONE
        smu_session.source_complete_event_output_terminal = f"/{smu_resource_name}/PXI_Trig0"

        # -> Configure DMM Measurement Settings.
        # - WAVEFORM_VOLTAGE acquisition mode on both DMMs
        # - Both DMMs wait on PXI_TRIG0 with zero trigger delay before acquiring their waveform
        for dmm_session in [dmm1_session, dmm2_session]:
            dmm_session.configure_waveform_acquisition(
                measurement_function=nidmm.Function.WAVEFORM_VOLTAGE,
                range=dmm_range,
                rate=dmm_rate,
                waveform_points=dmm_waveform_points,
            )
            dmm_session.configure_trigger(
                trigger_source=nidmm.TriggerSource.PXI_TRIG0,
                trigger_delay=0.0,  # no delay after trigger before starting acquisition
            )

        # -> Initiate and Acquire
        # - DMMs initiate first (waiting for PXI_TRIG0 from the SMU)
        # - SMU initiates last and fires SourceCompleteEvent to PXI_TRIG0,
        # when it completes sourcing the voltage step.
        for dmm_session in [dmm1_session, dmm2_session]:
            dmm_session.initiate()

        # Commit SMU settings (ensures trigger routing is applied before initiate)
        smu_session.commit()

        smu_session.initiate()

        # -> Fetch and Print Results
        # - fetch waveform from both DMMs based on the number of points specified in dmm_waveform_points
        # - print DMM1 and DMM2 measurements to console.
        dmm1_measurements = dmm1_session.fetch_waveform(dmm_waveform_points)
        dmm2_measurements = dmm2_session.fetch_waveform(dmm_waveform_points)

        print("DMM1: ", dmm1_measurements,
              "\n\nDMM2: ", dmm2_measurements)


def _main(argsv):
    """Parses command-line arguments and calls example() with the parsed values."""
    parser = argparse.ArgumentParser(
        description='Triggered waveform fetch: synchronize two DMMs via PXI_TRIG0 from an SMU SourceCompleteEvent.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('-srn', '--smu-resource-name', default='PXI1Slot1', help='SMU resource name')
    parser.add_argument('-d1rn', '--dmm1-resource-name', default='PXI1Slot2', help='DMM 1 resource name')
    parser.add_argument('-d2rn', '--dmm2-resource-name', default='PXI1Slot3', help='DMM 2 resource name')
    parser.add_argument('-vl', '--voltage-level', default=2.0, type=float, help='SMU output voltage level (V)')
    parser.add_argument('-cl', '--current-limit', default=0.01, type=float, help='SMU current limit (A)')
    parser.add_argument('-mrl', '--measure-record-length', default=100, type=int, help='SMU measure record length (samples)')
    parser.add_argument('-at', '--aperture-time', default=0.1, type=float, help='SMU aperture time per sample (s)')
    parser.add_argument('-dr', '--dmm-range', default=10.0, type=float, help='DMM voltage range (V)')
    parser.add_argument('-drt', '--dmm-rate', default=1e6, type=float, help='DMM waveform rate (S/s)')
    parser.add_argument('-dwp', '--dmm-waveform-points', default=50, type=int, help='DMM waveform points per acquisition')
    parser.add_argument('-sop', '--smu-option-string', default='', type=str, help='SMU driver option string, eg: "Simulate=1, DriverSetup=Model:4139; BoardType:PXIe"')
    parser.add_argument('-dop', '--dmm-option-string', default='', type=str, help='DMM driver option string, eg: "Simulate=1, DriverSetup=Model:4081"')
    args = parser.parse_args(argsv)
    example(
        smu_resource_name=args.smu_resource_name,
        dmm1_resource_name=args.dmm1_resource_name,
        dmm2_resource_name=args.dmm2_resource_name,
        smu_options=args.smu_option_string,
        dmm_options=args.dmm_option_string,
        voltage_level=args.voltage_level,
        current_limit=args.current_limit,
        measure_record_length=args.measure_record_length,
        aperture_time=args.aperture_time,
        dmm_range=args.dmm_range,
        dmm_rate=args.dmm_rate,
        dmm_waveform_points=args.dmm_waveform_points,
    )


def main():
    """Entry point — passes real CLI args to _main()."""
    _main(sys.argv[1:])


def test_example():
    """Simulated hardware test — runs example() with virtual NI-4139 SMU and NI-4080 DMMs (no real HW needed)."""
    smu_options = {'simulate': True, 'driver_setup': {'Model': '4139', 'BoardType': 'PXIe'}}
    dmm_options = {'simulate': True, 'driver_setup': {'Model': '4081'}}
    example(
        smu_resource_name='PXI1Slot1',
        dmm1_resource_name='PXI1Slot2',
        dmm2_resource_name='PXI1Slot3',
        smu_options=smu_options,
        dmm_options=dmm_options,
        voltage_level=2.0,
        current_limit=0.01,
        measure_record_length=100,
        aperture_time=0.1,
        dmm_range=10.0,
        dmm_rate=1e6,
        dmm_waveform_points=50,
    )


def test_main():
    """Simulated CLI test — runs _main() with simulate option strings."""
    cmd_line = [
        '--smu-option-string', 'Simulate=1, DriverSetup=Model:4139; BoardType:PXIe',
        '--dmm-option-string', 'Simulate=1, DriverSetup=Model:4081',
    ]
    _main(cmd_line)


# ------------------------------------------------------------
# Script execution starts here
# ------------------------------------------------------------
if __name__ == '__main__':
    main()
