#!/usr/bin/python

import argparse
import hightime
import nidcpower
import sys


def create_sweep(begin_value, end_value, number_of_steps):
    sweep = []
    step_size = (end_value - begin_value) / number_of_steps
    for i in range(number_of_steps):
        sweep.append(begin_value + i * step_size)
    return sweep


def example(resource_name, channels, options, steps, voltage_start, voltage_final, current_start, current_final):

    # The Python API should provide these values. But it doesn't. Issue #504. For now, put magic values here.
    attribute_ids = [
        1150008,  # output_function
        1250001,  # voltage_level
        1150009,  # current_level
    ]

    with nidcpower.Session(resource_name=resource_name, channels=channels, options=options) as session:

        session.source_mode = nidcpower.SourceMode.SEQUENCE
        session.source_delay = hightime.timedelta(seconds=0.1)
        session.voltage_level_autorange = True
        session.current_level_autorange = True
        session._create_advanced_sequence(sequence_name='my_sequence', attribute_ids=attribute_ids)
        voltages = create_sweep(voltage_start, voltage_final, steps)
        currents = create_sweep(current_start, current_final, steps)

        for v in voltages:
            session._create_advanced_sequence_step()
            session.output_function = nidcpower.OutputFunction.DC_VOLTAGE
            session.voltage_level = v

        for c in currents:
            session._create_advanced_sequence_step()
            session.output_function = nidcpower.OutputFunction.DC_CURRENT
            session.current_level = c

        with session.initiate():
            session.wait_for_event(nidcpower.Event.SEQUENCE_ENGINE_DONE)
            measurements = session.fetch_multiple(count=steps * 2)

        # Print a table with the measurements
        programmed_levels = voltages + currents
        units = ['V'] * steps + ['A'] * steps
        row_format = '{:<8} {:4} {:<25} {:<25} {}'
        print(row_format.format('Sourced', '', 'Measured voltage', 'Measured current', 'In-compliance'))
        for i in range(steps * 2):
            print(row_format.format(programmed_levels[i], units[i], measurements[i].voltage, measurements[i].current, measurements[i].in_compliance))


def _main(argsv):
    parser = argparse.ArgumentParser(description='Performs voltage sweep then a current sweep.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Resource name of a NI SMU')
    parser.add_argument('-c', '--channels', default='0', help='Channel(s) to use')
    parser.add_argument('-s', '--steps', default='10', type=int, help='Number of steps per sweep')
    parser.add_argument('-v0', '--voltage-start', default=1.0, type=float, help='Voltage level at which sweep starts (V)')
    parser.add_argument('-vf', '--voltage-final', default=3.0, type=float, help='Voltage level at which sweep ends (V)')
    parser.add_argument('-c0', '--current-start', default=100e-6, type=float, help='Current level at which sweep starts (A)')
    parser.add_argument('-cf', '--current-final', default=300e-6, type=float, help='Current level at which sweep ends (A)')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Option string')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.channels, args.option_string, args.steps, args.voltage_start, args.voltage_final, args.current_start, args.current_final)


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '4162', 'BoardType': 'PXIe', }, }
    example('PXI1Slot2', '0', options, 10, 1.0, 3.0, 100e-6, 300e-6)


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:4162; BoardType:PXIe', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()


