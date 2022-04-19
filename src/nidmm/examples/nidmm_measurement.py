#!/usr/bin/python

import argparse
import nidmm
import sys


def example(resource_name, option_string, function, range, digits):
    with nidmm.Session(resource_name=resource_name, options=option_string) as session:
        session.configure_measurement_digits(measurement_function=nidmm.Function[function], range=range, resolution_digits=digits)
        print(session.read())


def _main(argsv):
    supported_functions = list(nidmm.Function.__members__.keys())
    parser = argparse.ArgumentParser(description='Performs a single measurement using the NI-DMM API.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Resource name of an NI-Digital Multimeter module.')
    parser.add_argument('-f', '--function', default=supported_functions[0], choices=supported_functions, type=str.upper, help='Measurement function.')
    parser.add_argument('-r', '--range', default=10, type=float, help='Measurement range.')
    parser.add_argument('-d', '--digits', default=6.5, type=float, help='Digits of resolution for the measurement.')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Option string')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.option_string, args.function, args.range, args.digits)


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '4082', 'BoardType': 'PXIe', }, }
    example('PXI1Slot2', options, 'DC_VOLTS', 10, 6.5)


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:4082; BoardType:PXIe', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()


