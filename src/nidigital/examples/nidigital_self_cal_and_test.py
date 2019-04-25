#!/usr/bin/python

import argparse
import nidigital
import sys
import time


def example(resource_name, options):
    with nidigital.Session(resource_name=resource_name, options=options) as session:
        print('Calling self_calibrate')
        session.self_calibrate()
        print('self_calibrate successful')
        print('Calling self_test')
        session.self_test()
        print('self_test successful')


def _main(argsv):
    parser = argparse.ArgumentParser(description='Performs a waveform acquisition using the NI-Digital API.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Resource name of a <>.')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Option string')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.option_string)


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '6570', 'BoardType': 'PXIe', }, }
    example('PXI1Slot2', options)


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:6570;BoardType:PXIe', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()


