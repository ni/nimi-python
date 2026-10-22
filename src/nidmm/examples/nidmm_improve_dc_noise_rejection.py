#!/usr/bin/python

import argparse
import nidmm
import sys


def example(resource_name, options, range, digits, aperture_time, dc_noise_rejection, sample_count, auto_zero, number_of_averages):
    with nidmm.Session(resource_name=resource_name, options=options) as session:
        session.configure_measurement_digits(measurement_function=nidmm.Function.DC_VOLTS, range=range, resolution_digits=digits)
        session.configure_multi_point(trigger_count=1, sample_count=sample_count)
        # For aperture times over 100 ms, enable Auto Zero to compensate for drift.
        session.auto_zero = nidmm.AutoZero[auto_zero]
        session.aperture_time_units = nidmm.ApertureTimeUnits.SECONDS
        # To reject noise at frequency f, choose the aperture time based on the weighting mode:
        # NORMAL: a multiple of 1/f; SECOND_ORDER: a multiple of 2/f;
        # HIGH_ORDER: at least 4/f, with no benefit to going above 4.5/f.
        session.aperture_time = aperture_time
        # NORMAL weighs all samples equally; SECOND_ORDER and HIGH_ORDER weigh samples in the middle of the aperture more.
        session.dc_noise_rejection = nidmm.DCNoiseRejection[dc_noise_rejection]
        # The DMM averages shorter measurements to produce each returned reading.
        session.number_of_averages = number_of_averages
        measurements = session.read_multi_point(array_size=sample_count)
        print(f'Measurements for {sample_count} Samples: {measurements}')


def _main(argsv):
    supported_noise_rejection_modes = list(nidmm.DCNoiseRejection.__members__.keys())
    parser = argparse.ArgumentParser(description='Performs a multipoint DC voltage measurement with configurable DC noise rejection.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Contains the resource_name of the device to initialize.')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Sets the initial value of certain attributes for the session.')
    parser.add_argument('-r', '--range', default=0.1, type=float, help='Specifies the range for the function specified in the Measurement_Function parameter.')
    parser.add_argument('-d', '--digits', default=6.5, type=float, help='Specifies the resolution of the measurement in digits.')
    parser.add_argument('--auto-zero', default='OFF', choices=nidmm.AutoZero.__members__.keys(), type=str.upper, help='Specifies the Auto Zero mode.')
    parser.add_argument('-a', '--aperture-time', default=0.1, type=float, help='Specifies the measurement aperture time for the current configuration, in seconds.')
    parser.add_argument('--dc-noise-rejection', default='NORMAL', choices=supported_noise_rejection_modes, type=str.upper, help='Specifies the DC noise rejection mode.')
    parser.add_argument('-s', '--sample-count', default=10, type=int, help='Specifies the number of measurements the DMM takes each time it receives a trigger in a multiple point acquisition.')
    parser.add_argument('--number-of-averages', default=8, type=int, help='Specifies the number of averages to perform in a measurement.')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.option_string, args.range, args.digits, args.aperture_time, args.dc_noise_rejection, args.sample_count, args.auto_zero, args.number_of_averages)


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '4082', 'BoardType': 'PXIe', }, }
    example('PXI1Slot2', options, 0.1, 6.5, 0.1, 'NORMAL', 10, 'OFF', 8)


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:4082; BoardType:PXIe', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()
