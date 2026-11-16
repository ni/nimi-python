#!/usr/bin/python

import argparse
import nidmm
import sys

# Maximum points a single fetch_multi_point call can return in a continuous acquisition, per the array_size documentation
MAX_SAMPLES_PER_FETCH = 100000


def example(resource_name, options, function, measurement_range, digits, trigger_source, total_samples):
    print(f'Starting acquisition on resource {resource_name}, for {total_samples} samples.')
    with nidmm.Session(resource_name=resource_name, reset_device=True, options=options) as session:
        session.configure_measurement_digits(measurement_function=nidmm.Function[function], range=measurement_range, resolution_digits=digits)
        # Trigger slopes use driver defaults because the public API has no slope configuration (#875).
        session.configure_trigger(trigger_source=nidmm.TriggerSource[trigger_source])
        # The sample trigger uses the same source as the trigger; a sample_count of 0 configures a continuous acquisition
        session.configure_multi_point(trigger_count=1, sample_count=0, sample_trigger=nidmm.SampleTrigger[trigger_source])

        samples_fetched = 0
        with session.initiate():
            while samples_fetched < total_samples:
                backlog, _ = session.read_status()
                if backlog > 0:
                    new_samples = session.fetch_multi_point(array_size=min(backlog, MAX_SAMPLES_PER_FETCH))
                    samples_fetched += len(new_samples)

        print(f'Fetched {samples_fetched} readings.')


def _main(argsv):
    parser = argparse.ArgumentParser(description='Acquires measurements on each trigger using the NI-DMM API.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Contains the resource_name of the device to initialize.')
    parser.add_argument('-f', '--function', default='DC_VOLTS', choices=nidmm.Function.__members__.keys(), type=str.upper, help='Specifies the measurement_function used to acquire the measurement.')
    parser.add_argument('-r', '--range', default=10, type=float, help='Specifies the range for the function specified in the Measurement_Function parameter.')
    parser.add_argument('-d', '--digits', default=5.5, type=float, help='Specifies the resolution of the measurement in digits.')
    parser.add_argument('-t', '--trigger-source', default='EXTERNAL', choices=nidmm.TriggerSource.__members__.keys(), type=str.upper, help='Specifies the trigger source that initiates the acquisition.')
    parser.add_argument('--total-samples', default=100, type=int, help='Number of readings to fetch before stopping.')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Sets the initial value of certain attributes for the session.')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.option_string, args.function, args.range, args.digits, args.trigger_source, args.total_samples)


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '4082', 'BoardType': 'PXIe', }, }
    example('PXI1Slot2', options, 'DC_VOLTS', 10, 5.5, 'IMMEDIATE', 10)


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:4082; BoardType:PXIe', '--trigger-source', 'IMMEDIATE', '--total-samples', '10', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()
