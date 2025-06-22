#!/usr/bin/python

import argparse
import nidcpower
import sys


def example(
    resource_name,
    options,
    output_function,
    constant_resistance_level,
    constant_resistance_level_range,
    constant_resistance_current_limit,
    constant_power_level,
    constant_power_level_range,
    constant_power_current_limit,
    source_delay,
):
    assert output_function in (
        nidcpower.OutputFunction.CONSTANT_RESISTANCE, nidcpower.OutputFunction.CONSTANT_POWER
    ), 'This example only supports CONSTANT_RESISTANCE and CONSTANT_POWER output functions.'

    with nidcpower.Session(resource_name=resource_name, options=options) as session:
        # Configure the session.
        session.source_mode = nidcpower.SourceMode.SINGLE_POINT
        session.output_function = output_function
        if output_function == nidcpower.OutputFunction.CONSTANT_RESISTANCE:
            session.constant_resistance_level = constant_resistance_level
            session.constant_resistance_level_range = constant_resistance_level_range
            session.constant_resistance_current_limit = constant_resistance_current_limit
        else:
            session.constant_power_level = constant_power_level
            session.constant_power_level_range = constant_power_level_range
            session.constant_power_current_limit = constant_power_current_limit
        # Configure the source_delay to allow for sufficient startup delay for the input to sink to
        # the desired level. When starting from a 0 A or Off state, the electronic load requires
        # additional startup delay before the input begins to sink the desired level. The default
        # source_delay in this example takes this startup delay into account. In cases where
        # the electronic load is already sinking, less settling time may be needed.
        session.source_delay = source_delay

        with session.initiate():
            session.wait_for_event(event_id=nidcpower.Event.SOURCE_COMPLETE)
            measurement = session.measure_multiple()[0]
            in_compliance = session.query_in_compliance()
            print(f'Channel                   : {measurement.channel}')
            print(f'Voltage Measurement       : {measurement.voltage:f} V')
            print(f'Current Measurement       : {measurement.current:f} A')
            print(f'Compliance / Limit Reached: {in_compliance}')
            print(f'Resistance Measurement    : {measurement.voltage / measurement.current:f} Ω')
            print(f'Power Measurement         : {measurement.voltage * measurement.current:f} W')

        session.reset()


def _main(argsv):
    parser = argparse.ArgumentParser(
        description=(
            'Demonstrates how to use the Constant Resistance Output Function to force a resistance'
            ' level on the electronic load and how to use the Constant Power Output Function to'
            ' force a power level on the electronic load.'
        ),
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2/0', help='Resource names of NI electronic loads')
    parser.add_argument('-o', '--output-function', default='CONSTANT_RESISTANCE', type=str, choices=('CONSTANT_RESISTANCE', 'CONSTANT_POWER'), help='Output function')
    parser.add_argument('-rl', '--constant-resistance-level', default=15.0, type=float, help='Constant resistance level (Ω)')
    parser.add_argument('-rr', '--constant-resistance-level-range', default=1.0e3, type=float, help='Constant resistance level range (Ω)')
    parser.add_argument('-rc', '--constant-resistance-current-limit', default=800.0e-3, type=float, help='Constant resistance current limit (A)')
    parser.add_argument('-pl', '--constant-power-level', default=7.0, type=float, help='Constant power level (W)')
    parser.add_argument('-pr', '--constant-power-level-range', default=300.0, type=float, help='Constant power level range (W)')
    parser.add_argument('-pc', '--constant-power-current-limit', default=800.0e-3, type=float, help='Constant power current limit (A)')
    parser.add_argument('-s', '--source-delay', default=1.0, type=float, help='Source delay (s)')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Option String')
    args = parser.parse_args(argsv)
    example(
        resource_name=args.resource_name,
        options=args.option_string,
        output_function=getattr(nidcpower.OutputFunction, args.output_function),
        constant_resistance_level=args.constant_resistance_level,
        constant_resistance_level_range=args.constant_resistance_level_range,
        constant_resistance_current_limit=args.constant_resistance_current_limit,
        constant_power_level=args.constant_power_level,
        constant_power_level_range=args.constant_power_level_range,
        constant_power_current_limit=args.constant_power_current_limit,
        source_delay=args.source_delay,
    )


def main():
    _main(sys.argv[1:])


def test_example():
    example(
        resource_name='PXI1Slot2/0',
        options={'simulate': True, 'driver_setup': {'Model': '4051', 'BoardType': 'PXIe', }, },
        output_function=nidcpower.OutputFunction.CONSTANT_RESISTANCE,
        constant_resistance_level=15.0,
        constant_resistance_level_range=1.0e3,
        constant_resistance_current_limit=800.0e-3,
        constant_power_level=7.0,
        constant_power_level_range=300.0,
        constant_power_current_limit=800.0e-3,
        source_delay=1.0,
    )


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:4051; BoardType:PXIe', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()
