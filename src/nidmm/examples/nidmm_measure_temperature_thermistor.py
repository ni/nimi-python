#!/usr/bin/python

import argparse
import nidmm
import sys


def example(resource_name, options, function, transducer_type, thermistor_type, thermistor_a, thermistor_b, thermistor_c, range, digits):
    with nidmm.Session(resource_name=resource_name, options=options) as session:
        session.configure_measurement_digits(measurement_function=nidmm.Function[function], range=range, resolution_digits=digits)
        session.temp_transducer_type = nidmm.TransducerType[transducer_type]
        # The Python API has no configure_thermistor_type method, so the type is set through its property
        session.temp_thermistor_type = nidmm.ThermistorType[thermistor_type]
        # The A, B, and C coefficients apply only to the CUSTOM thermistor type; the driver chooses them for the other types
        if thermistor_type == 'CUSTOM':
            session.configure_thermistor_custom(thermistor_a, thermistor_b, thermistor_c)
        measurement = session.read()
        print(f'Measurement (Celsius): {measurement}')


def _main(argsv):
    supported_functions = list(nidmm.Function.__members__.keys())
    supported_transducer_types = list(nidmm.TransducerType.__members__.keys())
    supported_thermistor_types = list(nidmm.ThermistorType.__members__.keys())
    parser = argparse.ArgumentParser(description='Performs a single temperature measurement using a thermistor with the NI-DMM API.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Contains the resource_name of the device to initialize.')
    parser.add_argument('-f', '--function', default='TEMPERATURE', choices=supported_functions, type=str.upper, help='Specifies the measurement_function used to acquire the measurement.')
    parser.add_argument('--transducer-type', default='THERMISTOR', choices=supported_transducer_types, type=str.upper, help='Specifies the type of device used to measure the temperature.')
    parser.add_argument('-t', '--thermistor-type', default='THERMISTOR_44006', choices=supported_thermistor_types, type=str.upper, help='Specifies the type of thermistor used to measure the temperature.')
    parser.add_argument('--thermistor-a', default=0.0010295, type=float, help='Specifies the Steinhart-Hart A coefficient for thermistor scaling when the Thermistor Type property is set to Custom.')
    parser.add_argument('--thermistor-b', default=0.0002391, type=float, help='Specifies the Steinhart-Hart B coefficient for thermistor scaling when the Thermistor Type property is set to Custom.')
    parser.add_argument('--thermistor-c', default=1.568e-7, type=float, help='Specifies the Steinhart-Hart C coefficient for thermistor scaling when the Thermistor Type property is set to Custom.')
    parser.add_argument('-r', '--range', default=100000.0, type=float, help='Specifies the range of the measurement in ohms.')
    parser.add_argument('-d', '--digits', default=5.5, type=float, help='Specifies the resolution of the measurement in digits.')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Sets the initial value of certain attributes for the session.')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.option_string, args.function, args.transducer_type, args.thermistor_type, args.thermistor_a, args.thermistor_b, args.thermistor_c, args.range, args.digits)


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '4082', 'BoardType': 'PXIe', }, }
    example('PXI1Slot2', options, 'TEMPERATURE', 'THERMISTOR', 'THERMISTOR_44006', 0.0010295, 0.0002391, 1.568e-7, 100000.0, 5.5)


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:4082; BoardType:PXIe', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()
