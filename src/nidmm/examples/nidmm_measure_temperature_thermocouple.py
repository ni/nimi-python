#!/usr/bin/python

import argparse
import nidmm
import sys


def example(resource_name, options, function, transducer_type, thermocouple_type, reference_junction_type, fixed_reference_junction, range, digits):
    with nidmm.Session(resource_name=resource_name, options=options) as session:
        session.configure_measurement_digits(measurement_function=nidmm.Function[function], range=range, resolution_digits=digits)
        session.temp_transducer_type = nidmm.TransducerType[transducer_type]
        session.configure_thermocouple(nidmm.ThermocoupleType[thermocouple_type], nidmm.ThermocoupleReferenceJunctionType[reference_junction_type])
        # Reference junction temperature, in degrees Celsius, used with the FIXED reference junction type
        session.temp_tc_fixed_ref_junc = fixed_reference_junction
        measurement = session.read()
        print(f'Measurement (Celsius): {measurement}')


def _main(argsv):
    supported_functions = list(nidmm.Function.__members__.keys())
    supported_transducer_types = list(nidmm.TransducerType.__members__.keys())
    supported_thermocouple_types = list(nidmm.ThermocoupleType.__members__.keys())
    parser = argparse.ArgumentParser(description='Performs a single temperature measurement using a thermocouple with the NI-DMM API.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Contains the resource_name of the device to initialize.')
    parser.add_argument('-f', '--function', default='TEMPERATURE', choices=supported_functions, type=str.upper, help='Specifies the measurement_function used to acquire the measurement.')
    parser.add_argument('--transducer-type', default='THERMOCOUPLE', choices=supported_transducer_types, type=str.upper, help='Specifies the type of device used to measure the temperature.')
    parser.add_argument('-t', '--thermocouple-type', default='J', choices=supported_thermocouple_types, type=str.upper, help='Specifies the type of thermocouple used to measure the temperature.')
    parser.add_argument('--reference-junction-type', default='FIXED', choices=nidmm.ThermocoupleReferenceJunctionType.__members__.keys(), type=str.upper, help='Specifies the type of reference junction to be used in the reference junction compensation of a thermocouple measurement.')
    parser.add_argument('--fixed-reference-junction', default=25.0, type=float, help='Specifies the reference junction temperature when a fixed reference junction is used to take a thermocouple measurement.')
    parser.add_argument('-r', '--range', default=0.1, type=float, help='Specifies the range of the measurement in volts.')
    parser.add_argument('-d', '--digits', default=5.5, type=float, help='Specifies the resolution of the measurement in digits.')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Sets the initial value of certain attributes for the session.')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.option_string, args.function, args.transducer_type, args.thermocouple_type, args.reference_junction_type, args.fixed_reference_junction, args.range, args.digits)


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '4082', 'BoardType': 'PXIe', }, }
    example('PXI1Slot2', options, 'TEMPERATURE', 'THERMOCOUPLE', 'J', 'FIXED', 25.0, 0.1, 5.5)


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:4082; BoardType:PXIe', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()
