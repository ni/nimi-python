#!/usr/bin/python

import argparse
import nidcpower
import sys


def example(
    resource_name,
    options,
    current_level,
    current_level_range,
    voltage_limit_range,
    source_delay,
    output_shorted,
    conduction_voltage_mode,
    conduction_voltage_on_threshold,
    conduction_voltage_off_threshold,
    current_level_rising_slew_rate,
    current_level_falling_slew_rate,
):
    with nidcpower.Session(resource_name=resource_name, options=options) as session:
        # Configure the session.
        session.source_mode = nidcpower.SourceMode.SINGLE_POINT

        session.output_function = nidcpower.OutputFunction.DC_CURRENT
        session.current_level = current_level
        session.current_level_range = current_level_range
        session.voltage_limit_range = voltage_limit_range
        # Note that the voltage_limit property is not applicable for electronic loads and is not
        # configured in this example. If you change the output_function, configure the appropriate
        # level, limit and range properties corresponding to your selected output_function.

        session.source_delay = source_delay

        # Configure the output_shorted property to specify whether to simulate a short circuit in
        # the electronic load.
        session.output_shorted = output_shorted

        # If you set the output_function property to nidcpower.OutputFunction.DC_CURRENT or
        # nidcpower.OutputFunction.CONSTANT_POWER, set the conduction_voltage_mode to
        # nidcpower.ConductionVoltageMode.AUTOMATIC or nidcpower.ConductionVoltageMode.ENABLED to
        # enable Conduction Voltage.
        # If you set the output_function property to nidcpower.OutputFunction.DC_VOLTAGE or
        # nidcpower.OutputFunction.CONSTANT_RESISTANCE, set the conduction_voltage_mode to
        # nidcpower.ConductionVoltageMode.AUTOMATIC or nidcpower.ConductionVoltageMode.DISABLED to
        # disable Conduction Voltage.
        # If Conduction Voltage is enabled, set the conduction_voltage_on_threshold to configure the
        # electronic load to start sinking current when the input voltage exceeds the configured
        # threshold, and set the conduction_voltage_off_threshold to configure the electronic load
        # to stop sinking current when the input voltage falls below the threshold.
        # If Conduction Voltage is disabled, the electronic load attempts to sink the desired level
        # regardless of the input voltage.
        session.conduction_voltage_mode = conduction_voltage_mode
        session.conduction_voltage_on_threshold = conduction_voltage_on_threshold
        session.conduction_voltage_off_threshold = conduction_voltage_off_threshold

        # If you set the output_function property to nidcpower.OutputFunction.DC_CURRENT, configure
        # the current_level_rising_slew_rate and current_level_falling_slew_rate, in amps per
        # microsecond, to control the rising and falling current slew rates of the electronic load
        # while sinking current.
        # When the output_function property is set to a value other than
        # nidcpower.OutputFunction.DC_CURRENT, these properties have no effect.
        session.current_level_rising_slew_rate = current_level_rising_slew_rate
        session.current_level_falling_slew_rate = current_level_falling_slew_rate

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
            'Demonstrates how to use the DC Current Output Function to force a current into the'
            ' electronic load and how to configure the electronic load with the Output Shorted,'
            ' Conduction Voltage and Current Level Slew Rate features.'
        ),
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2/0', help='Resource names of NI electronic loads')
    parser.add_argument('-cl', '--current-level', default=1.0, type=float, help='Current level (A)')
    parser.add_argument('-cr', '--current-level-range', default=40.0, type=float, help='Current level range (A)')
    parser.add_argument('-vr', '--voltage-limit-range', default=60.0, type=float, help='Voltage limit range (V)')
    parser.add_argument('-s', '--source-delay', default=0.5, type=float, help='Source delay (s)')
    parser.add_argument('-os', '--output-shorted', default=False, action='store_true', help='Output shorted')
    parser.add_argument('-cv', '--conduction-voltage-mode', default='AUTOMATIC', type=str, choices=tuple(nidcpower.ConductionVoltageMode.__members__.keys()), help='Conduction voltage mode')
    parser.add_argument('-nt', '--conduction-voltage-on-threshold', default=1.0, type=float, help='Conduction voltage on threshold (V)')
    parser.add_argument('-ot', '--conduction-voltage-off-threshold', default=0.0, type=float, help='Conduction voltage off threshold (V)')
    parser.add_argument('-rs', '--current-level-rising-slew-rate', default=24.0, type=float, help='Current level rising slew rate (A/µs)')
    parser.add_argument('-fs', '--current-level-falling-slew-rate', default=24.0, type=float, help='Current level falling slew rate (A/µs)')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Option String')
    args = parser.parse_args(argsv)
    example(
        resource_name=args.resource_name,
        options=args.option_string,
        current_level=args.current_level,
        current_level_range=args.current_level_range,
        voltage_limit_range=args.voltage_limit_range,
        source_delay=args.source_delay,
        output_shorted=args.output_shorted,
        conduction_voltage_mode=getattr(nidcpower.ConductionVoltageMode, args.conduction_voltage_mode),
        conduction_voltage_on_threshold=args.conduction_voltage_on_threshold,
        conduction_voltage_off_threshold=args.conduction_voltage_off_threshold,
        current_level_rising_slew_rate=args.current_level_rising_slew_rate,
        current_level_falling_slew_rate=args.current_level_falling_slew_rate,
    )


def main():
    _main(sys.argv[1:])


def test_example():
    example(
        resource_name='PXI1Slot2/0',
        options={'simulate': True, 'driver_setup': {'Model': '4051', 'BoardType': 'PXIe', }, },
        current_level=1.0,
        current_level_range=40.0,
        voltage_limit_range=60.0,
        source_delay=0.5,
        output_shorted=False,
        conduction_voltage_mode=nidcpower.ConductionVoltageMode.AUTOMATIC,
        conduction_voltage_on_threshold=1.0,
        conduction_voltage_off_threshold=0.0,
        current_level_rising_slew_rate=24.0,
        current_level_falling_slew_rate=24.0,
    )


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:4051; BoardType:PXIe', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()
