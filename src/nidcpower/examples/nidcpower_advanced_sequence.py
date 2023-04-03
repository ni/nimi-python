#!/usr/bin/python

import argparse
import hightime
import nidcpower
import sys


def example(resource_name, options, voltage_max, current_max, points_per_output_function, delay_in_seconds):
    timeout = hightime.timedelta(seconds=(delay_in_seconds + 1.0))

    with nidcpower.Session(resource_name=resource_name, options=options) as session:
        # Configure the session.
        session.source_mode = nidcpower.SourceMode.SEQUENCE
        session.voltage_level_autorange = True
        session.current_limit_autorange = True
        session.source_delay = hightime.timedelta(seconds=delay_in_seconds)
        properties_used = ['output_function', 'voltage_level', 'current_level']
        session.create_advanced_sequence(sequence_name='my_sequence', property_names=properties_used, set_as_active_sequence=True)

        voltage_per_step = voltage_max / points_per_output_function
        for i in range(points_per_output_function):
            session.create_advanced_sequence_step(set_as_active_step=False)
            session.output_function = nidcpower.OutputFunction.DC_VOLTAGE
            session.voltage_level = voltage_per_step * i

        current_per_step = current_max / points_per_output_function
        for i in range(points_per_output_function):
            session.create_advanced_sequence_step(set_as_active_step=False)
            session.output_function = nidcpower.OutputFunction.DC_CURRENT
            session.current_level = current_per_step * i

        with session.initiate():
            session.wait_for_event(nidcpower.Event.SEQUENCE_ENGINE_DONE)
            channel_indices = '0-{0}'.format(session.channel_count - 1)
            channels = session.get_channel_names(channel_indices)
            measurement_group = [session.channels[name].fetch_multiple(points_per_output_function * 2, timeout=timeout) for name in channels]

        session.delete_advanced_sequence(sequence_name='my_sequence')
        line_format = '{:<15} {:<4} {:<10} {:<10} {:<6}'
        print(line_format.format('Channel', 'Num', 'Voltage', 'Current', 'In Compliance'))
        for i, measurements in enumerate(measurement_group):
            num = 0
            channel_name = channels[i].strip()
            for measurement in measurements:
                print(line_format.format(channel_name, num, measurement.voltage, measurement.current, str(measurement.in_compliance)))
                num += 1


def _main(argsv):
    parser = argparse.ArgumentParser(description='Output ramping voltage to voltage max, then ramping current to current max.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2/0, PXI1Slot3/0-1', help='Resource names of NI SMUs.')
    parser.add_argument('-s', '--number-steps', default=256, help='Number of steps per output function')
    parser.add_argument('-v', '--voltage-max', default=1.0, type=float, help='Maximum voltage (V)')
    parser.add_argument('-i', '--current-max', default=0.001, type=float, help='Maximum Current (I)')
    parser.add_argument('-d', '--delay', default=0.05, type=float, help='Source delay (s)')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Option string')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.option_string, args.voltage_max, args.current_max, args.number_steps, args.delay)


def main():
    _main(sys.argv[1:])


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:4162; BoardType:PXIe', ]
    _main(cmd_line)


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '4162', 'BoardType': 'PXIe', }, }
    example('PXI1Slot2/0, PXI1Slot3/1', options, 1.0, 0.001, 256, 0.05)


if __name__ == '__main__':
    main()


