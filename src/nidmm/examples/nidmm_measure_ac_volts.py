#!/usr/bin/python

import argparse
import math
import nidmm
import sys


def example(resource_name, options, function, range, digits, min_ac_frequency, max_ac_frequency):
    with nidmm.Session(resource_name=resource_name, options=options) as session:
        session.configure_measurement_digits(measurement_function=nidmm.Function[function], range=range, resolution_digits=digits)
        session.ac_min_freq = min_ac_frequency
        session.ac_max_freq = max_ac_frequency
        measurement = session.read()
        out_of_range = math.isnan(measurement) or (math.isinf(measurement) and measurement > 0)
        print(f'Measurement (volts): {measurement}')
        print(f'Signal Out of Range: {out_of_range}')


def _main(argsv):
    supported_functions = list(nidmm.Function.__members__.keys())
    parser = argparse.ArgumentParser(description='Performs a single AC voltage measurement using the NI-DMM API.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Contains the resource_name of the device to initialize.')
    parser.add_argument('-f', '--function', default='AC_VOLTS', choices=supported_functions, type=str.upper, help='Specifies the measurement_function used to acquire the measurement.')
    parser.add_argument('-r', '--range', default=2, type=float, help='Specifies the range for the function specified in the Measurement_Function parameter.')
    parser.add_argument('-d', '--digits', default=5.5, type=float, help='Specifies the resolution of the measurement in digits.')
    parser.add_argument('--min-ac-frequency', default=40, type=float, help='Specifies the minimum frequency component of the input signal for AC measurements.')
    parser.add_argument('--max-ac-frequency', default=250000, type=float, help='Specifies the maximum frequency component of the input signal for AC measurements.')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Sets the initial value of certain attributes for the session.')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.option_string, args.function, args.range, args.digits, args.min_ac_frequency, args.max_ac_frequency)


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '4082', 'BoardType': 'PXIe', }, }
    example('PXI1Slot2', options, 'AC_VOLTS', 10, 6.5, 1, 300000)


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:4082; BoardType:PXIe', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()
