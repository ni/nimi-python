#!/usr/bin/python

import argparse
import collections
import nidmm
import pytest
import sys


# Number of most recent measurements kept on the chart
CHART_HISTORY_SIZE = 250


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
    samples_fetched += len(new_samples)
    # The x-axis keeps absolute sample numbers, so it starts after the samples dropped from the history
    first_sample = samples_fetched - len(measurements)
    line.set_data(range(first_sample, samples_fetched), measurements)
    axes.relim()
    axes.autoscale_view()
    plt.pause(0.001)
    return samples_fetched


def example(resource_name, options, function, measurement_range, digits, trigger_source, total_samples):
    # Imported lazily because matplotlib is unavailable on some platforms (e.g. 32-bit Python)
    import matplotlib.pyplot as plt

    with nidmm.Session(resource_name=resource_name, options=options) as session:
        session.configure_measurement_digits(measurement_function=nidmm.Function[function], range=measurement_range, resolution_digits=digits)
        # Trigger and sample trigger slope are not configured: the slope properties and enums are not in the Python API (#875)
        session.configure_trigger(trigger_source=nidmm.TriggerSource[trigger_source])
        # The sample trigger uses the same source as the trigger; a sample_count of 0 configures a continuous acquisition
        session.configure_multi_point(trigger_count=1, sample_count=0, sample_trigger=nidmm.SampleTrigger[trigger_source])

        # Create an empty chart; the line is filled in as samples arrive
        figure, axes, line = _create_chart(plt)
        # Only the most recent CHART_HISTORY_SIZE measurements are kept
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
                        # The last fetch only takes the samples still needed to reach total_samples
                        samples_in_this_fetch = backlog
                        if total_samples is not None:
                            samples_in_this_fetch = min(backlog, total_samples - samples_fetched)

                        new_samples = session.fetch_multi_point(array_size=samples_in_this_fetch)

                        # Add the new samples to the chart and get the updated total sample count
                        samples_fetched = _update_chart(plt, axes, line, measurements, new_samples, samples_fetched)
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
    parser.add_argument('--total-samples', default=None, type=int, help='Stops fetching after this many samples and keeps the chart open until its window is closed; omit to run until the chart window is closed or Ctrl+C is pressed.')
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
