#!/usr/bin/python

import argparse
import nidmm
import sys


def example(resource_name, options, function, transducer_type, rtd_type, rtd_resistance, rtd_a, rtd_b, rtd_c, range, digits):
    with nidmm.Session(resource_name=resource_name, options=options) as session:
        session.configure_measurement_digits(measurement_function=nidmm.Function[function], range=range, resolution_digits=digits)
        session.temp_transducer_type = nidmm.TransducerType[transducer_type]
        session.configure_rtd_type(nidmm.RTDType[rtd_type], rtd_resistance)
        # The A, B, and C coefficients apply only to the CUSTOM RTD type; the driver chooses them for the other types
        if rtd_type == 'CUSTOM':
            session.configure_rtd_custom(rtd_a, rtd_b, rtd_c)
        measurement = session.read()
        print(f'Measurement (Celsius): {measurement}')


def _main(argsv):
    supported_functions = list(nidmm.Function.__members__.keys())
    supported_transducer_types = list(nidmm.TransducerType.__members__.keys())
    supported_rtd_types = list(nidmm.RTDType.__members__.keys())
    parser = argparse.ArgumentParser(description='Performs a single temperature measurement using an RTD with the NI-DMM API.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Contains the resource_name of the device to initialize.')
    parser.add_argument('-f', '--function', default='TEMPERATURE', choices=supported_functions, type=str.upper, help='Specifies the measurement_function used to acquire the measurement.')
    parser.add_argument('--transducer-type', default='TWO_WIRE_RTD', choices=supported_transducer_types, type=str.upper, help='Specifies the type of device used to measure the temperature.')
    parser.add_argument('-t', '--rtd-type', default='PT3851', choices=supported_rtd_types, type=str.upper, help='Specifies the type of RTD used to measure the temperature resistance.')
    parser.add_argument('--rtd-resistance', default=100.0, type=float, help='Specifies the RTD resistance in ohms at 0 degrees Celsius.')
    parser.add_argument('--rtd-a', default=0.0039083, type=float, help='Specifies the Callendar-Van Dusen A coefficient for RTD scaling when RTD Type parameter is set to Custom in the configure_rtd_type method.')
    parser.add_argument('--rtd-b', default=-5.775e-7, type=float, help='Specifies the Callendar-Van Dusen B coefficient for RTD scaling when RTD Type parameter is set to Custom in the configure_rtd_type method.')
    parser.add_argument('--rtd-c', default=-4.183e-12, type=float, help='Specifies the Callendar-Van Dusen C coefficient for RTD scaling when RTD Type parameter is set to Custom in the configure_rtd_type method.')
    parser.add_argument('-r', '--range', default=10000.0, type=float, help='Specifies the range of the measurement in ohms.')
    parser.add_argument('-d', '--digits', default=5.5, type=float, help='Specifies the resolution of the measurement in digits.')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Sets the initial value of certain attributes for the session.')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.option_string, args.function, args.transducer_type, args.rtd_type, args.rtd_resistance, args.rtd_a, args.rtd_b, args.rtd_c, args.range, args.digits)


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '4082', 'BoardType': 'PXIe', }, }
    example('PXI1Slot2', options, 'TEMPERATURE', 'TWO_WIRE_RTD', 'PT3851', 100.0, 0.0039083, -5.775e-7, -4.183e-12, 10000.0, 5.5)


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:4082; BoardType:PXIe', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()
