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
    parser.add_argument('-f', '--function', default='DC_VOLTS', choices=supported_functions, type=str.upper, help='Specifies the measurement function.')
    parser.add_argument('-r', '--range', default=0.1, type=float, help='Specifies the measurement range. Use positive values to represent the absolute value of the maximum expected measurement, in units appropriate for the measurement function (for example, volts for DC_VOLTS).')
    parser.add_argument('-d', '--digits', default=6.5, type=float, help='Specifies the measurement resolution in digits. Higher values increase measurement accuracy; lower values increase measurement speed. The aperture time below overrides the default aperture selected by this setting.')
    parser.add_argument('--auto-zero', default='OFF', choices=nidmm.AutoZero.__members__.keys(), type=str.upper, help='Specifies the AutoZero mode. AUTO: the driver chooses based on the function and resolution. OFF: AutoZero is disabled. ON: the DMM takes a zero reading after each measurement and subtracts it from the preceding reading. ONCE: the DMM takes a zero reading for the first measurement and subtracts it from all readings.')
    parser.add_argument('-a', '--aperture-time', default=0.1, type=float, help='Specifies the measurement aperture time in seconds. It is applied after the measurement is configured, overriding the default aperture.')
    parser.add_argument('--dc-noise-rejection', default='NORMAL', choices=supported_noise_rejection_modes, type=str.upper, help='Specifies the DC noise rejection mode. AUTO: the driver chooses based on the function and resolution. NORMAL: all samples are weighted equally. SECOND_ORDER: samples in the middle of the aperture time are weighted more than those at the ends, using a triangular weighting function. HIGH_ORDER: the same, using a bell-curve weighting function. Not supported on the NI 4050 and NI 4060.')
    parser.add_argument('-s', '--sample-count', default=10, type=int, help='Specifies the number of measurements the DMM takes in the multiple point acquisition.')
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
