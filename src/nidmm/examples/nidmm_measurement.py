#!/usr/bin/python

import argparse
import nidmm
import sys


def example(argsv):
    supported_functions = list(nidmm.Function.__members__.keys())
    parser = argparse.ArgumentParser(description='Performs a single measurement using the NI-DMM API.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource_name', default='PXI1Slot2', help='Resource name of a National Instruments Digital Multimeter.')
    parser.add_argument('-f', '--function', default=supported_functions[0], choices=supported_functions, type=str.upper, help='Measurement function.')
    parser.add_argument('-r', '--range', default=10, type=float, help='Measurement range.')
    parser.add_argument('-d', '--digits', default=6.5, type=float, help='Digits of resolution for the measurement.')
    parser.add_argument('-op', '--option_string', default='', type=str, help='Option string')
    args = parser.parse_args(argsv)

    with nidmm.Session(resource_name=args.resource_name, option_string=args.option_string) as session:
        session.configure_measurement_digits(measurement_function=nidmm.Function[args.function], range=args.range, resolution_digits=args.digits)
        print(session.read())


def _main():
    example(sys.argv)


def test_example():
    cmd_line = ['-op', 'Simulate=1, DriverSetup=Model:4082; BoardType:PXIe', ]
    example(cmd_line)


if __name__ == '__main__':
    _main()


