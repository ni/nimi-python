#!/usr/bin/python

import argparse
import nidmm
import sys


def example(resource_name, options, range, digits, min_ac_frequency, max_ac_frequency):
    with nidmm.Session(resource_name=resource_name, options=options) as session:
        session.configure_measurement_digits(measurement_function=nidmm.Function.AC_VOLTS, range=range, resolution_digits=digits)
        session.ac_min_freq = min_ac_frequency
        session.ac_max_freq = max_ac_frequency
        measurement = session.read()
        print('AC voltage: {} V'.format(measurement))


def _main(argsv):
    parser = argparse.ArgumentParser(description='Measures AC voltage using the NI-DMM API.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Resource name of an NI digital multimeter.')
    parser.add_argument('-r', '--range', default=10, type=float, help='Measurement range in volts.')
    parser.add_argument('-d', '--digits', default=6.5, type=float, help='Digits of resolution for the measurement.')
    parser.add_argument('--min-ac-frequency', default=1, type=float, help='Minimum frequency component of the AC input signal in hertz.')
    parser.add_argument('--max-ac-frequency', default=300000, type=float, help='Maximum frequency component of the AC input signal in hertz.')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Option string')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.option_string, args.range, args.digits, args.min_ac_frequency, args.max_ac_frequency)


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '4082', 'BoardType': 'PXIe', }, }
    example('PXI1Slot2', options, 10, 6.5, 1, 300000)


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:4082; BoardType:PXIe', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()
