#!/usr/bin/python

import argparse
import nidmm
import sys


def example(resource_name, options, function, range, digits, aperture_time, dc_noise_rejection, sample_count, auto_zero='OFF'):
    with nidmm.Session(resource_name=resource_name, options=options) as session:
        session.configure_measurement_digits(measurement_function=nidmm.Function[function], range=range, resolution_digits=digits)
        session.configure_multi_point(trigger_count=1, sample_count=sample_count)
        session.auto_zero = nidmm.AutoZero[auto_zero]
        session.aperture_time_units = nidmm.ApertureTimeUnits.SECONDS
        session.aperture_time = aperture_time
        session.dc_noise_rejection = nidmm.DCNoiseRejection[dc_noise_rejection]
        measurements = session.read_multi_point(array_size=sample_count)
        print('Measurements: ', measurements)


def _main(argsv):
    supported_functions = list(nidmm.Function.__members__.keys())
    supported_noise_rejection_modes = list(nidmm.DCNoiseRejection.__members__.keys())
    parser = argparse.ArgumentParser(description='Performs a multipoint measurement with improved DC noise rejection using the NI-DMM API.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Resource name of an NI digital multimeter.')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Option string')
    parser.add_argument('-f', '--function', default='DC_VOLTS', choices=supported_functions, type=str.upper, help='Measurement function.')
    parser.add_argument('-r', '--range', default=0.1, type=float, help='Measurement range.')
    parser.add_argument('-d', '--digits', default=6.5, type=float, help='Digits of resolution for the measurement.')
    parser.add_argument('--auto-zero', default='OFF', choices=nidmm.AutoZero.__members__.keys(), type=str.upper, help='AutoZero mode.')
    parser.add_argument('-a', '--aperture-time', default=0.1, type=float, help='Measurement aperture time in seconds.')
    parser.add_argument('--dc-noise-rejection', default='NORMAL', choices=supported_noise_rejection_modes, type=str.upper, help='DC noise rejection mode.')
    parser.add_argument('-s', '--sample-count', default=10, type=int, help='The number of measurements the DMM makes.')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.option_string, args.function, args.range, args.digits, args.aperture_time, args.dc_noise_rejection, args.sample_count, args.auto_zero)


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '4082', 'BoardType': 'PXIe', }, }
    example('PXI1Slot2', options, 'DC_VOLTS', 0.1, 6.5, 0.1, 'NORMAL', 10, 'OFF')


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:4082; BoardType:PXIe', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()
