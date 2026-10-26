#!/usr/bin/python

import argparse
import math
import nidmm
import sys


def example(resource_name, options, range, digits, current_source):
    with nidmm.Session(resource_name=resource_name, options=options) as session:
        session.configure_measurement_digits(measurement_function=nidmm.Function.DIODE, range=range, resolution_digits=digits)
        session.current_source = current_source
        measurement = session.read()
        out_of_range = math.isnan(measurement) or (math.isinf(measurement) and measurement > 0)
        print(f'Measurement (volts): {measurement}')
        print(f'Signal Out of Range: {out_of_range}')


def _main(argsv):
    parser = argparse.ArgumentParser(description='Performs a single diode measurement using the NI-DMM API.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Contains the resource_name of the device to initialize.')
    parser.add_argument('-r', '--range', default=2, type=float, help='Specifies the range for the function specified in the measurement_function parameter.')
    parser.add_argument('-d', '--digits', default=5.5, type=float, help='Specifies the resolution of the measurement in digits.')
    parser.add_argument('-c', '--current-source', default=0.001, type=float, help='Specifies the current source provided during diode measurements.')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Sets the initial value of certain attributes for the session.')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.option_string, args.range, args.digits, args.current_source)


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '4082', 'BoardType': 'PXIe', }, }
    example('PXI1Slot2', options, 2, 5.5, 0.001)


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:4082; BoardType:PXIe', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()
