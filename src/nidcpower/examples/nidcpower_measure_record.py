#!/usr/bin/python

import argparse
import nidcpower
import sys


def example(resource_name, channels, options, voltage, length):
    with nidcpower.Session(resource_name=resource_name, channels=channels, options=options) as session:

        # Configure the session.
        session.measure_record_length = length
        session.measure_record_length_is_finite = True
        session.measure_when = nidcpower.MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE
        session.voltage_level = voltage

        session.commit()
        print('Effective measurement rate: {0} S/s'.format(session.measure_record_delta_time / 1))

        samples_acquired = 0
        print('  #    Voltage    Current    In Compliance')
        row_format = '{0:3d}:   {1:8.6f}   {2:8.6f}   {3}'
        with session.initiate():
            while samples_acquired < length:
                measurements = session.fetch_multiple(count=session.fetch_backlog)
                samples_acquired += len(measurements)
                for i in range(len(measurements)):
                    print(row_format.format(i, measurements[i].voltage, measurements[i].current, measurements[i].in_compliance))


def _main(argsv):
    parser = argparse.ArgumentParser(description='Outputs the specified voltage, then takes the specified number of voltage and current readings.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Resource name of a NI SMU')
    parser.add_argument('-c', '--channels', default='0', help='Channel(s) to use')
    parser.add_argument('-l', '--length', default='20', type=int, help='Measure record length')
    parser.add_argument('-v', '--voltage', default=5.0, type=float, help='Voltage level (V)')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Option string')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.channels, args.option_string, args.voltage, args.length)


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '4162', 'BoardType': 'PXIe', }, }
    example('PXI1Slot2', '0', options, 5.0, 20)


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:4162; BoardType:PXIe', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()


