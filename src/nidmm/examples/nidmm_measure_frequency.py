#!/usr/bin/python

import argparse
import nidmm
import sys
import warnings

SIGNAL_NOT_DETECTED_WARNING_CODE = 0x3FFA4F80


def example(resource_name, options, function, min_frequency, max_period, voltage_range, digits):
    # Frequency mode takes the minimum frequency as its range; period mode takes the maximum period.
    range = min_frequency if function == 'FREQUENCY' else max_period
    units = 'Hz' if function == 'FREQUENCY' else 's'
    with nidmm.Session(resource_name=resource_name, options=options) as session:
        session.configure_measurement_digits(measurement_function=nidmm.Function[function], range=range, resolution_digits=digits)
        session.freq_voltage_range = voltage_range
        # The driver reports warnings through the warnings module, with the code in the message text.
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter('always')
            measurement = session.read()
        signal_not_detected = any(f'Warning {SIGNAL_NOT_DETECTED_WARNING_CODE} occurred' in str(word.message) for word in caught)
        print(f'Measurement ({units}): {measurement}')
        print(f'Signal not Detected: {signal_not_detected}')


def _main(argsv):
    parser = argparse.ArgumentParser(description='Performs a single frequency or period measurement using the NI-DMM API.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Contains the resource_name of the device to initialize.')
    parser.add_argument('-f', '--function', default='FREQUENCY', choices=['FREQUENCY', 'PERIOD'], type=str.upper, help='Specifies the measurement_function used to acquire the measurement.')
    parser.add_argument('--min-frequency', default=100, type=float, help='Minimum frequency expected, in Hz. Used as the range in FREQ mode.')
    parser.add_argument('--max-period', default=0.01, type=float, help='Maximum period expected, in seconds. Used as the range in PERIOD mode.')
    parser.add_argument('--voltage-range', default=50, type=float, help='Specifies the voltage range of the input signal for frequency measurements.')
    parser.add_argument('-d', '--digits', default=5.5, type=float, help='Specifies the resolution of the measurement in digits.')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Sets the initial value of certain attributes for the session.')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.option_string, args.function, args.min_frequency, args.max_period, args.voltage_range, args.digits)


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '4082', 'BoardType': 'PXIe', }, }
    example('PXI1Slot2', options, 'FREQ', 100, 0.01, 10, 5.5)
    example('PXI1Slot2', options, 'PERIOD', 100, 0.01, 10, 5.5)


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:4082; BoardType:PXIe', ]
    _main(cmd_line)
    _main(cmd_line + ['--function', 'period', '--max-period', '0.02'])


if __name__ == '__main__':
    main()
