#!/usr/bin/python

import argparse
import nidmm
import sys


# Maximum points a single fetch_multi_point call can return in a continuous acquisition, per the array_size documentation
MAX_SAMPLES_PER_FETCH = 100000


def example(resource_name, options, function, measurement_range, digits, samples_to_fetch, total_samples):
    print(f'Starting acquisition on resource {resource_name}.')
    with nidmm.Session(resource_name=resource_name, options=options) as session:
        session.configure_measurement_digits(measurement_function=nidmm.Function[function], range=measurement_range, resolution_digits=digits)
        # A sample_count of 0 configures a continuous acquisition
        session.configure_multi_point(trigger_count=1, sample_count=0)

        samples_fetched = 0
        try:
            with session.initiate():
                # A total_samples of None runs until Ctrl+C is pressed
                while total_samples is None or samples_fetched < total_samples:
                    # Fetch the whole backlog when it exceeds samples_to_fetch so the buffer does not overflow
                    backlog, _ = session.read_status()
                    samples_in_this_fetch = min(max(samples_to_fetch, backlog), MAX_SAMPLES_PER_FETCH)

                    new_samples = session.fetch_multi_point(array_size=samples_in_this_fetch)

                    samples_fetched += len(new_samples)
        except KeyboardInterrupt:
            pass

        print(f'Fetched {samples_fetched} measurements')


def _main(argsv):
    parser = argparse.ArgumentParser(description='Continuously acquires measurements and prints a summary using the NI-DMM API.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Contains the resource_name of the device to initialize.')
    parser.add_argument('-f', '--function', default='DC_VOLTS', choices=nidmm.Function.__members__.keys(), type=str.upper, help='Specifies the measurement_function used to acquire the measurement.')
    parser.add_argument('-r', '--range', default=10, type=float, help='Specifies the range for the function specified in the Measurement_Function parameter.')
    parser.add_argument('-d', '--digits', default=5.5, type=float, help='Specifies the resolution of the measurement in digits.')
    parser.add_argument('-s', '--samples-to-fetch', default=4, type=int, help='Specifies the minimum number of measurements to fetch at a time.')
    parser.add_argument('--total-samples', default=100, type=int, help='Number of measurements to fetch before stopping.')
    parser.add_argument('--continuous', action='store_true', help='Fetch measurements until Ctrl+C is pressed; overrides --total-samples.')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Sets the initial value of certain attributes for the session.')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.option_string, args.function, args.range, args.digits, args.samples_to_fetch, None if args.continuous else args.total_samples)


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '4082', 'BoardType': 'PXIe', }, }
    example('PXI1Slot2', options, 'DC_VOLTS', 10, 5.5, 4, 10)


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:4082; BoardType:PXIe', '--total-samples', '10', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()
