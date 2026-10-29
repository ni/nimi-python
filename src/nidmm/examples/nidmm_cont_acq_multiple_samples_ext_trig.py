#!/usr/bin/python

import argparse
import collections
import nidmm
import pytest
import sys


# Number of most recent measurements kept on the chart
CHART_HISTORY_SIZE = 250

# Maximum points a single fetch_multi_point call can return in a continuous acquisition, per the array_size documentation
MAX_SAMPLES_PER_FETCH = 100000


def _create_chart(plt):
    figure, axes = plt.subplots()
    (line,) = axes.plot([])
    axes.set_title('Measurements')
    axes.set_xlabel('Samples')
    axes.set_ylabel('Measured value')
    axes.grid(True)
    return figure, axes, line


def _update_chart(plt, axes, line, measurements, new_samples, samples_fetched):
    measurements.extend(new_samples)
    first_sample = samples_fetched - len(measurements)
    line.set_data(range(first_sample, samples_fetched), measurements)
    axes.relim()
    axes.autoscale_view()
    plt.pause(0.001)


def example(resource_name, options, function, measurement_range, digits, trigger_source, total_samples):
    import matplotlib.pyplot as plt

    with nidmm.Session(resource_name=resource_name, reset_device=True, options=options) as session:
        session.configure_measurement_digits(measurement_function=nidmm.Function[function], range=measurement_range, resolution_digits=digits)
        # Trigger slopes use driver defaults because the public API has no slope configuration (#875).
        try:
            session.configure_trigger(trigger_source=nidmm.TriggerSource[trigger_source])
            # The sample trigger uses the same source as the trigger; a sample_count of 0 configures a continuous acquisition
            session.configure_multi_point(trigger_count=1, sample_count=0, sample_trigger=nidmm.SampleTrigger[trigger_source])
        except nidmm.errors.DriverError as e:
            # Not every device supports every trigger source (for example, NI 408x devices have no external trigger)
            sys.exit('The device does not support trigger source {}.\n{}'.format(trigger_source, e.description))

        figure, axes, line = _create_chart(plt)
        measurements = collections.deque(maxlen=CHART_HISTORY_SIZE)

        samples_fetched = 0
        try:
            with session.initiate():
                # A total_samples of None runs until the chart window is closed or Ctrl+C is pressed
                while plt.fignum_exists(figure.number) and (
                    total_samples is None or samples_fetched < total_samples
                ):
                    backlog, _ = session.read_status()
                    if backlog > 0:
                        new_samples = session.fetch_multi_point(array_size=min(backlog, MAX_SAMPLES_PER_FETCH))
                        samples_fetched += len(new_samples)
                        _update_chart(plt, axes, line, measurements, new_samples, samples_fetched)
                    else:
                        # Process chart events while waiting for the next trigger.
                        plt.pause(0.001)

            # The acquisition has stopped; keep the final chart on screen until its window is closed
            if total_samples is not None and plt.fignum_exists(figure.number):
                plt.show()
        except KeyboardInterrupt:
            pass
        finally:
            plt.close(figure)


def _main(argsv):
    parser = argparse.ArgumentParser(description='Continuously acquires measurements on each trigger and displays them on a chart using the NI-DMM API.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Contains the resource_name of the device to initialize.')
    parser.add_argument('-f', '--function', default='DC_VOLTS', choices=nidmm.Function.__members__.keys(), type=str.upper, help='Specifies the measurement_function used to acquire the measurement.')
    parser.add_argument('-r', '--range', default=10, type=float, help='Specifies the range for the function specified in the Measurement_Function parameter.')
    parser.add_argument('-d', '--digits', default=5.5, type=float, help='Specifies the resolution of the measurement in digits.')
    parser.add_argument('-t', '--trigger-source', default='EXTERNAL', choices=nidmm.TriggerSource.__members__.keys(), type=str.upper, help='Specifies the trigger source that initiates the acquisition.')
    parser.add_argument('--total-samples', default=None, type=int, help='Specifies the maximum number of samples to acquire; omit to run until the chart closes or Ctrl+C is pressed.')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Sets the initial value of certain attributes for the session.')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.option_string, args.function, args.range, args.digits, args.trigger_source, args.total_samples)


def main():
    _main(sys.argv[1:])


def test_example():
    plt = pytest.importorskip('matplotlib.pyplot')
    plt.switch_backend('Agg')  # Avoid opening a chart window during the test
    options = {'simulate': True, 'driver_setup': {'Model': '4082', 'BoardType': 'PXIe', }, }
    example('PXI1Slot2', options, 'DC_VOLTS', 10, 5.5, 'IMMEDIATE', 10)


def test_main():
    plt = pytest.importorskip('matplotlib.pyplot')
    plt.switch_backend('Agg')  # Avoid opening a chart window during the test
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:4082; BoardType:PXIe', '--trigger-source', 'IMMEDIATE', '--total-samples', '10', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()
