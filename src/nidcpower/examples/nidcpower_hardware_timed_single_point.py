#!/usr/bin/env python3
"""NI-DCPower Hardware-Timed Single Point.

This example demonstrates how to set up a hardware-timed Single Point operation.

The hardware is configured to source a voltage, wait for a specified delay and
then take a measurement.

The example uses the default resource name, channel, current level,
and voltage limit. Modify these values as needed for your measurement setup

HOW TO RUN:
-----------
i.   From terminal (with default values):
        python nidcpower_hardware_timed_single_point.py

ii.  From terminal (with custom values):
        python nidcpower_hardware_timed_single_point.py -n "PXI1Slot1" \
            -vl1 3.0 -vl2 5.0 -sd 0.1

iii. To simulate without hardware:
        PowerShell:  python nidcpower_hardware_timed_single_point.py \
            -op 'Simulate=1, DriverSetup=Model:4163; BoardType:PXIe'
        cmd.exe:     python nidcpower_hardware_timed_single_point.py \
            -op "Simulate=1, DriverSetup=Model:4163; BoardType:PXIe"

"""

# Module imports
import argparse  # For parsing command-line arguments
import sys  # For accessing command-line arguments via sys.argv

import nidcpower  # NI-DCPower instrument driver


def example(resource_name, options, voltage_level_1, voltage_level_2,
            voltage_level_range, current_limit, current_limit_range,
            source_delay):
    """Core measurement logic — sources two voltage levels sequentially and returns both measurements.

    Args:
        resource_name (str)         : NI-MAX resource name, eg: "PXI1Slot1"
        options (str or dict)       : Driver options, eg: "" for real HW or simulate dict for simulation
        voltage_level_1 (float)     : First voltage level to source (V) —  must be <= voltage_level_range
        voltage_level_2 (float)     : Second voltage level to source (V) —  must be <= voltage_level_range
        voltage_level_range (float) : Voltage range — must be >= both voltage levels (V)
        current_limit (float)       : Current limit (A) — must be <= current_limit_range
        current_limit_range (float) : Current range — must be >= current_limit (A)
        source_delay (float)        : Delay before Source Complete Event fires(s)
    """
    # 'with' block ensures session.abort() + session.close() are called automatically on exit.
    # channels=0 targets channel 0; reset=True clears any previous session state.
    with nidcpower.Session(resource_name=resource_name, reset=True, channels=0, options=options) as session:

        # Configure source mode and output function.
        # SINGLE_POINT: sources one value and holds; voltage_level can be changed mid-session.
        # measure_when = AUTOMATICALLY_AFTER_SOURCE_COMPLETE: required for fetch_multiple().
        session.source_mode = nidcpower.SourceMode.SINGLE_POINT
        session.output_function = nidcpower.OutputFunction.DC_VOLTAGE
        session.voltage_level = voltage_level_1
        session.voltage_level_range = voltage_level_range
        session.current_limit = current_limit
        session.current_limit_range = current_limit_range
        session.source_delay = source_delay
        session.measure_when = nidcpower.MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE

        # Commit sends all settings to hardware before initiate.
        session.commit()

        # Initiate output, fetch at voltage_level_1, change to voltage_level_2, fetch again.
        # timeout=1.0 s — adjust if source_delay is longer than 1 s.
        with session.initiate():
            measurements1 = session.fetch_multiple(count=1, timeout=1.0)
            session.voltage_level = voltage_level_2
            measurements2 = session.fetch_multiple(count=1, timeout=1.0)

        print(f'Measurements 1: \n- Voltage: {measurements1[0][0]:f} V'
              f'\n- Current: {measurements1[0][1]:f} A'
              f'\n- In Compliance: {measurements1[0][2]}')
        print(f'Measurements 2: \n- Voltage: {measurements2[0][0]:f} V'
              f'\n- Current: {measurements2[0][1]:f} A'
              f'\n- In Compliance: {measurements2[0][2]}')

    return measurements1, measurements2


def _main(argsv):
    """Parses command-line arguments and calls example() with the parsed values."""
    parser = argparse.ArgumentParser(
        description='Hardware-timed single point: source two voltage levels and measure.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('-n', '--resource-name', default='PXI1Slot1', help='Resource name of NI SMU')
    parser.add_argument('-vl1', '--voltage-level-1', default=2.0, type=float, help='First voltage level (V)')
    parser.add_argument('-vl2', '--voltage-level-2', default=4.0, type=float, help='Second voltage level (V)')
    parser.add_argument('-vr', '--voltage-level-range', default=10.0, type=float, help='Voltage level range — must be >= both voltage levels (V)')
    parser.add_argument('-cl', '--current-limit', default=0.01, type=float, help='Current limit (A)')
    parser.add_argument('-clr', '--current-limit-range', default=0.01, type=float, help='Current limit range — must be >= current-limit (A)')
    parser.add_argument('-sd', '--source-delay', default=0.05, type=float, help='Source delay in seconds')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Driver option string, eg: "Simulate=1, DriverSetup=Model:4163; BoardType:PXIe"')
    args = parser.parse_args(argsv)
    example(
        resource_name=args.resource_name,
        options=args.option_string,
        voltage_level_1=args.voltage_level_1,
        voltage_level_2=args.voltage_level_2,
        voltage_level_range=args.voltage_level_range,
        current_limit=args.current_limit,
        current_limit_range=args.current_limit_range,
        source_delay=args.source_delay,
    )


def main():
    """Entry point — passes real CLI args to _main()."""
    _main(sys.argv[1:])


def test_example():
    """Simulated hardware test — runs example() with a virtual PXIe-4163 (no real HW needed)."""
    options = {'simulate': True, 'driver_setup': {'Model': '4163', 'BoardType': 'PXIe'}}
    example('PXI1Slot1', options, 2.0, 4.0, 10.0, 0.01, 0.01, 0.05)


def test_main():
    """Simulated CLI test — runs _main() with simulate option string."""
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:4163; BoardType:PXIe']
    _main(cmd_line)


# ------------------------------------------------------------
# Script execution starts here
# ------------------------------------------------------------
if __name__ == '__main__':
    main()
