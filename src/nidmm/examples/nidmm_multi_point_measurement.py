#!/usr/bin/python

import argparse
import nidmm
import sys


def example(argsv):
    parser = argparse.ArgumentParser(description='Performs a multipoint measurement using the NI-DMM API.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource_name', default='PXI1Slot2', help='Resource name of a National Instruments Digital Multimeter.')
    parser.add_argument('-f', '--function', default='DC_VOLTS', choices=nidmm.Function.__members__.keys(), type=str.upper, help='Measurement function.')
    parser.add_argument('-r', '--range', default=10, type=float, help='Measurement range.')
    parser.add_argument('-d', '--digits', default=6.5, type=float, help='Digits of resolution for the measurement.')
    parser.add_argument('-s', '--samples', default=10, type=int, help='The number of measurements the DMM makes.')
    parser.add_argument('-t', '--triggers', default=1, type=int, help='Sets the number of triggers you want the DMM to receive before returning to the Idle state.')
    parser.add_argument('-op', '--option_string', default='', type=str, help='Option string')
    args = parser.parse_args(argsv)

    with nidmm.Session(resource_name=args.resource_name, options=args.option_string) as session:
        session.configure_measurement_digits(measurement_function=nidmm.Function[args.function], range=args.range, resolution_digits=args.digits)
        session.configure_multi_point(trigger_count=args.triggers, sample_count=args.samples)
        measurements = session.read_multi_point(array_size=args.samples)
        print('Measurements: ', measurements)


def _main():
    example(sys.argv)


def test_example():
    cmd_line = ['-op', 'Simulate=1, DriverSetup=Model:4082; BoardType:PXIe', ]
    example(cmd_line)


if __name__ == '__main__':
    _main()


