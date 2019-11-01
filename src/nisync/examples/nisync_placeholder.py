#!/usr/bin/python

import argparse
import nisync
import sys
import time


def example(resource_name, options, function, range, points, rate):
    pass


def _main(argsv):
    parser = argparse.ArgumentParser(description='Performs a waveform acquisition using the NI-DMM API.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Resource name of a National Instruments Digital Multimeter.')
    parser.add_argument('-f', '--function', default='WAVEFORM_VOLTAGE', choices=nidmm.Function.__members__.keys(), type=str.upper, help='Measurement function.')
    parser.add_argument('-r', '--range', default=10, type=float, help='Measurement range.')
    parser.add_argument('-p', '--points', default=10, type=int, help='Specifies the number of points to acquire before the waveform acquisition completes.')
    parser.add_argument('-s', '--rate', default=1000, type=int, help='Specifies the rate of the acquisition in samples per second.')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Option string')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.option_string, args.function, args.range, args.points, args.rate)


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '4082', 'BoardType': 'PXIe', }, }
    example('PXI1Slot2', options, 'WAVEFORM_VOLTAGE', 10, 10, 1000)


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:4082; BoardType:PXIe', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()


