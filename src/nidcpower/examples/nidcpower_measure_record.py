#!/usr/bin/python

import argparse
import nidcpower
import sys


def example(resource_name, options, voltage, length):
    with nidcpower.Session(resource_name=resource_name, options=options) as session:
        # Configure the session.
        session.measure_record_length = length
        session.measure_record_length_is_finite = True
        session.measure_when = nidcpower.MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE
        session.output_function = nidcpower.OutputFunction.DC_VOLTAGE
        session.voltage_level = voltage

        session.commit()
        print('Effective measurement rate: {0} S/s'.format(session.measure_record_delta_time / 1))

        print('Channel           Num  Voltage    Current    In Compliance')
        row_format = '{0:15} {1:3d}    {2:8.6f}   {3:8.6f}   {4}'
        with session.initiate():
            channel_indices = '0-{0}'.format(session.channel_count - 1)
            channels = session.get_channel_names(channel_indices)
            for i, channel_name in enumerate(channels):
                samples_acquired = 0
                while samples_acquired < length:
                    measurements = session.channels[channel_name].fetch_multiple(count=session.fetch_backlog)
                    samples_acquired += len(measurements)
                    for i in range(len(measurements)):
                        print(row_format.format(channel_name, i, measurements[i].voltage, measurements[i].current, measurements[i].in_compliance))


def _main(argsv):
    parser = argparse.ArgumentParser(description='Outputs the specified voltage, then takes the specified number of voltage and current readings.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2/0, PXI1Slot3/0-1', help='Resource names of NI SMUs.')
    parser.add_argument('-l', '--length', default='20', type=int, help='Measure record length per channel')
    parser.add_argument('-v', '--voltage', default=5.0, type=float, help='Voltage level (V)')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Option string')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.option_string, args.voltage, args.length)


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '4162', 'BoardType': 'PXIe', }, }
    example('PXI1Slot2/0, PXI1Slot3/1', options, 5.0, 20)


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:4162; BoardType:PXIe', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()
