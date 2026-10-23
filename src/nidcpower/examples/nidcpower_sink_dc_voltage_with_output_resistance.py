#!/usr/bin/python

import argparse
import nidcpower
import sys


def example(
    resource_name,
    options,
    voltage_level,
    voltage_level_range,
    current_limit,
    current_limit_range,
    source_delay,
    output_shorted,
    output_resistance,
):
    with nidcpower.Session(resource_name=resource_name, options=options) as session:
        # Configure the session.
        session.source_mode = nidcpower.SourceMode.SINGLE_POINT

        session.output_function = nidcpower.OutputFunction.DC_VOLTAGE
        session.voltage_level = voltage_level
        session.voltage_level_range = voltage_level_range
        session.current_limit = current_limit
        session.current_limit_range = current_limit_range
        # If you change the output_function, configure the appropriate level, limit and range
        # properties corresponding to your selected output_function.

        session.source_delay = source_delay

        # Configure the output_shorted property to specify whether to simulate a short circuit in
        # the electronic load.
        session.output_shorted = output_shorted

        # Configure the output_resistance, in ohms, to force a voltage across the configured
        # output resistance in series with the electronic load.
        session.output_resistance = output_resistance

        with session.initiate():
            session.wait_for_event(event_id=nidcpower.Event.SOURCE_COMPLETE)
            measurement = session.measure_multiple()[0]
            in_compliance = session.query_in_compliance()
            print(f'Channel                   : {measurement.channel}')
            print(f'Voltage Measurement       : {measurement.voltage:f} V')
            print(f'Current Measurement       : {measurement.current:f} A')
            print(f'Compliance / Limit Reached: {in_compliance}')

        session.reset()


def _main(argsv):
    parser = argparse.ArgumentParser(
        description=(
            'Demonstrates how to use the DC Voltage Output Function to force a voltage into the'
            ' electronic load and how to configure the electronic load with the Output Resistance'
            ' and Output Shorted features.'
        ),
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2/0', help='Resource names of NI electronic loads')
    parser.add_argument('-vl', '--voltage-level', default=1.0, type=float, help='Voltage level (V)')
    parser.add_argument('-vr', '--voltage-level-range', default=6.0, type=float, help='Voltage level range (V)')
    parser.add_argument('-cl', '--current-limit', default=4.0, type=float, help='Current limit (A)')
    parser.add_argument('-cr', '--current-limit-range', default=4.0, type=float, help='Current limit range (A)')
    parser.add_argument('-s', '--source-delay', default=0.5, type=float, help='Source delay (s)')
    parser.add_argument('-os', '--output-shorted', default=False, action='store_true', help='Output shorted')
    parser.add_argument('-or', '--output-resistance', default=1.0, type=float, help='Output resistance (Ω)')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Option String')
    args = parser.parse_args(argsv)
    example(
        resource_name=args.resource_name,
        options=args.option_string,
        voltage_level=args.voltage_level,
        voltage_level_range=args.voltage_level_range,
        current_limit=args.current_limit,
        current_limit_range=args.current_limit_range,
        source_delay=args.source_delay,
        output_shorted=args.output_shorted,
        output_resistance=args.output_resistance,
    )


def main():
    _main(sys.argv[1:])


def test_example():
    example(
        resource_name='PXI1Slot2/0',
        options={'simulate': True, 'driver_setup': {'Model': '4051', 'BoardType': 'PXIe', }, },
        voltage_level=1.0,
        voltage_level_range=6.0,
        current_limit=4.0,
        current_limit_range=4.0,
        source_delay=0.5,
        output_shorted=False,
        output_resistance=1.0,
    )


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:4051; BoardType:PXIe', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()
