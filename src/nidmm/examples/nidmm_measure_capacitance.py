#!/usr/bin/python

import argparse
import math
import nidmm
import re
import sys

# Only these models support capacitance measurements.
SUPPORTED_MODELS = ('4072', '4082')


def example(resource_name, options, function, range, measurements_to_average):
    with nidmm.Session(resource_name=resource_name, options=options) as session:
        model_match = re.search('[0-9]+', session.instrument_model)
        model = model_match.group() if model_match else ''
        if model not in SUPPORTED_MODELS:
            print(f'{session.instrument_model} does not support capacitance measurements.\r\nSupported models: NI {", NI ".join(SUPPORTED_MODELS)}.')
            return
        # Resolution is ignored for capacitance and inductance, but the driver still validates it (3.5, 4.5, 5.5 or 6.5).
        session.configure_measurement_digits(measurement_function=nidmm.Function[function], range=range, resolution_digits=5.5)
        session.lc_number_meas_to_average = measurements_to_average
        measurement = session.read()
        # NI-DMM reports an underrange condition as negative infinity.
        under_range = math.isinf(measurement) and measurement < 0
        print(f'Measurement (Farads): {measurement}')
        print(f'Signal Under Range: {under_range}')


def _main(argsv):
    supported_functions = list(nidmm.Function.__members__.keys())
    parser = argparse.ArgumentParser(description='Performs a single capacitance measurement using the NI-DMM API (NI 4072/4082 only).', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Contains the resource_name of the device to initialize.')
    parser.add_argument('-f', '--function', default='CAPACITANCE', choices=supported_functions, type=str.upper, help='Specifies the measurement_function used to acquire the measurement.')
    parser.add_argument('-r', '--range', default=3e-10, type=float, help='Specifies the range for the function specified in the Measurement_Function parameter.')
    parser.add_argument('-a', '--measurements-to-average', default=1, type=int, help='For the NI 4072 only, specifies the number of LC measurements that are averaged to produce one reading.')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Sets the initial value of certain attributes for the session.')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.option_string, args.function, args.range, args.measurements_to_average)


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '4082', 'BoardType': 'PXIe', }, }
    example('PXI1Slot2', options, 'CAPACITANCE', 3e-10, 1)


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:4082; BoardType:PXIe', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()
