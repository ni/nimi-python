#!/usr/bin/python

import argparse
import collections
import nidmm
import pytest
import sys


# Number of most recent measurements kept on the chart
CHART_HISTORY_SIZE = 250


def example(resource_name, options, function, measurement_range, digits, trigger_source, fetch_count):
    # Imported lazily because matplotlib is unavailable on some platforms (e.g. 32-bit Python)
    import matplotlib.pyplot as plt

    with nidmm.Session(resource_name=resource_name, options=options) as session:
        session.configure_measurement_digits(measurement_function=nidmm.Function[function], range=measurement_range, resolution_digits=digits)
        session.configure_trigger(trigger_source=nidmm.TriggerSource[trigger_source])
        # The sample trigger uses the same source as the trigger; a sample_count of 0 configures a continuous acquisition
        session.configure_multi_point(trigger_count=1, sample_count=0, sample_trigger=nidmm.SampleTrigger[trigger_source])

        figure, axes = plt.subplots()
        (line,) = axes.plot([])
        axes.set_title('Measurements')
        axes.set_xlabel('Samples')
        axes.set_ylabel('Measured value')
        axes.grid(True)

        measurements = collections.deque(maxlen=CHART_HISTORY_SIZE)
        total_samples = 0
        fetches = 0
        try:
            with session.initiate():
                # A fetch_count of None runs until the chart window is closed or Ctrl+C is pressed
                while plt.fignum_exists(figure.number) and (fetch_count is None or fetches < fetch_count):
                    backlog, _ = session.read_status()
                    if backlog > 0:
                        new_samples = session.fetch_multi_point(array_size=backlog)
                        measurements.extend(new_samples)
                        total_samples += len(new_samples)
                        first_sample = total_samples - len(measurements)
                        line.set_data(range(first_sample, total_samples), measurements)
                        axes.relim()
                        axes.autoscale_view()
                        fetches += 1
                    plt.pause(0.001)
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
    parser.add_argument('--fetch-count', default=None, type=int, help='Stops after this many fetches; omit to run until the chart window is closed or Ctrl+C is pressed.')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Sets the initial value of certain attributes for the session.')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.option_string, args.function, args.range, args.digits, args.trigger_source, args.fetch_count)


def main():
    _main(sys.argv[1:])


def test_example():
    plt = pytest.importorskip('matplotlib.pyplot')
    plt.switch_backend('Agg')  # Avoid opening a chart window during the test
    options = {'simulate': True, 'driver_setup': {'Model': '4082', 'BoardType': 'PXIe', }, }
    example('PXI1Slot2', options, 'DC_VOLTS', 10, 5.5, 'IMMEDIATE', 2)


def test_main():
    plt = pytest.importorskip('matplotlib.pyplot')
    plt.switch_backend('Agg')  # Avoid opening a chart window during the test
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:4082; BoardType:PXIe', '--trigger-source', 'IMMEDIATE', '--fetch-count', '2', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()
