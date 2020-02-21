#!/usr/bin/python

import argparse
import datetime
import nidcpower
import sys


def example(resource_name, channels, options, voltage_max, current_max, points_per_output_function, delay):
    timeout = datetime.timedelta(seconds=(delay + 1.0))

    with nidcpower.Session(resource_name=resource_name, channels=channels, options=options) as session:

        my_advanced_sequence = []

        voltage_per_step = voltage_max / points_per_output_function
        for i in range(points_per_output_function):
            my_advanced_sequence.append({"output_function": nidcpower.OutputFunction.DC_VOLTAGE, "voltage_level": voltage_per_step * i, })

        current_per_step = current_max / points_per_output_function
        for i in range(points_per_output_function):
            my_advanced_sequence.append({"output_function": nidcpower.OutputFunction.DC_CURRENT, "current_level": current_per_step * i, })

        # Configure the session.
        session.source_mode = nidcpower.SourceMode.SEQUENCE
        session.voltage_level_autorange = True
        session.current_limit_autorange = True
        session.source_delay = datetime.timedelta(seconds=delay)
        session.create_advanced_sequence(sequence_name='my_sequence', sequence=my_advanced_sequence, set_as_active_sequence=True)

        with session.initiate():
            session.wait_for_event(nidcpower.Event.SEQUENCE_ENGINE_DONE)
            measurements = session.fetch_multiple(points_per_output_function * 2, timeout=timeout)

        session.delete_sequence(sequence_name='my_sequence')
        line_format = '{:,<4} {:,.6g<10} {:,.6g<10} {:<6}\n'
        print('{:<4} {:<10} {:,<10} {:<6}'.format('Num', 'Voltage', 'Current', 'In Compliance'))
        i = 0
        for measurement in measurements:
            print(line_format.format(i, measurement.voltage, measurement.current, str(measurement.in_compliance)))
            i += 1


def _main(argsv):
    parser = argparse.ArgumentParser(description='Outputs voltage 1, waits for source delay, and then takes a measurement. Then orepeat with voltage 2.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Resource name of a National Instruments SMU')
    parser.add_argument('-c', '--channels', default='0', help='Channel(s) to use')
    parser.add_argument('-p', '--number-points', default=256, help='Number of points per output function')
    parser.add_argument('-v', '--voltage-max', default=1.0, type=float, help='Maximum voltage (V)')
    parser.add_argument('-i', '--current-max', default=0.02, type=float, help='Maximum Current (I)')
    parser.add_argument('-d', '--delay', default=0.05, type=float, help='Source delay (s)')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Option string')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.channels, args.option_string, args.voltage_max, args.current_max, args.number_points, args.delay)


def main():
    _main(sys.argv[1:])


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:4162; BoardType:PXIe', ]
    _main(cmd_line)


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '4162', 'BoardType': 'PXIe', }, }
    example('PXI1Slot2', '0', options, 1.0, 0.5, 256, 0.05)


if __name__ == '__main__':
    main()


