#!/usr/bin/python

import argparse
from collections import deque
from contextlib import redirect_stdout
import io
import nidmm
import signal
import sys


class LiveChart:
    """Live matplotlib chart of a rolling window of measurements with a Stop button.

    `stopped` becomes True when the Stop button is clicked, the window is closed, or Ctrl+C is pressed.
    """

    def __init__(self, title, max_points=250):
        import matplotlib.pyplot as plt
        from matplotlib.widgets import Button

        self._plt = plt
        self.stopped = False
        self._y = deque(maxlen=max_points)
        self._x = deque(maxlen=max_points)
        self._count = 0

        self.figure, self.axes = plt.subplots()
        self.figure.subplots_adjust(bottom=0.3)
        (self._line,) = self.axes.plot([], [])
        self.axes.set_title(title)
        self.axes.set_xlabel('Samples')
        self.axes.set_ylabel('Amplitude (Volts)')
        self.axes.grid(True)

        self._button = Button(self.figure.add_axes([0.4, 0.05, 0.2, 0.08]), 'Stop')
        self._button.on_clicked(self._stop)
        self.figure.canvas.mpl_connect('close_event', self._stop)
        # Tk swallows KeyboardInterrupt raised inside draw callbacks, so Ctrl+C sets the flag instead.
        self._previous_sigint_handler = signal.signal(signal.SIGINT, self._stop)
        plt.show(block=False)

    def _stop(self, *_args):
        self.stopped = True

    def update(self, measurements):
        for value in measurements:
            self._x.append(self._count)
            self._y.append(value)
            self._count += 1
        self._line.set_data(self._x, self._y)
        self.axes.relim()
        self.axes.autoscale_view()
        self._plt.pause(0.001)

    def close(self):
        signal.signal(signal.SIGINT, self._previous_sigint_handler)
        self._plt.close(self.figure)


def print_measurements(measurements):
    text = 'Measurements: {}'.format(list(measurements))
    # \r returns to the line start and \033[K erases leftovers from a longer previous line
    print('\r' + text + '\033[K', end='', flush=True)


def example(resource_name, options, function, measurement_range, digits, fetch_size):
    if fetch_size < 1:
        raise ValueError('fetch_size must be greater than zero')

    total_samples = 0

    with nidmm.Session(resource_name=resource_name, options=options) as session:
        session.configure_measurement_digits(
            measurement_function=nidmm.Function[function],
            range=measurement_range,
            resolution_digits=digits,
        )
        # One trigger with sample_count=0 acquires continuously until the session is aborted.
        session.configure_multi_point(trigger_count=1, sample_count=0)

        # Opens the live chart window with its Stop button.
        chart = LiveChart('NI-DMM continuous acquisition chart multiple samples ({})'.format(function))
        try:
            with session.initiate():
                while not chart.stopped:
                    measurement = session.fetch_multi_point(array_size=fetch_size)
                    total_samples += len(measurement)
                    print_measurements(measurement)
                    chart.update(measurement)
        except KeyboardInterrupt:
            pass
        finally:
            chart.close()

    print('\nAcquisition stopped. Total measurements: {}'.format(total_samples))

    return total_samples


def _main(argsv):
    parser = argparse.ArgumentParser(description='Configures a continuous multipoint acquisition and fetches measurements using the NI-DMM API.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Contains the resource_name of the device to initialize.')
    parser.add_argument('-f', '--function', default='DC_VOLTS', choices=nidmm.Function.__members__.keys(), type=str.upper, help='Specifies the measurement_function used to acquire the measurement.')
    parser.add_argument('-r', '--range', default=10, type=float, help='Specifies the range for the function specified in the Measurement_Function parameter.')
    parser.add_argument('-d', '--digits', default=5.5, type=float, help='Specifies the resolution of the measurement in digits.')
    parser.add_argument('-s', '--fetch-size', default=4, type=int, help='Specifies the number of measurements to acquire.')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Sets the initial value of certain attributes for the session.')
    args = parser.parse_args(argsv)
    if args.fetch_size < 1:
        parser.error('--fetch-size must be greater than zero')
    return example(args.resource_name, args.option_string, args.function, args.range, args.digits, args.fetch_size)


def main():
    _main(sys.argv[1:])


class _StubChart:
    # Simulates the user clicking Stop after two batches.
    def __init__(self, title):
        self.stopped = False
        self._updates = 0

    def update(self, measurements):
        self._updates += 1
        self.stopped = self._updates >= 2

    def close(self):
        pass


def test_example(monkeypatch, capsys):
    monkeypatch.setattr(sys.modules[__name__], 'LiveChart', _StubChart)
    options = {'simulate': True, 'driver_setup': {'Model': '4082', 'BoardType': 'PXIe', }, }
    total_samples = example('Dev1', options, 'DC_VOLTS', 10, 5.5, 4)
    assert total_samples == 8
    assert 'Total measurements: 8' in capsys.readouterr().out


class _InterruptingChart(_StubChart):
    def update(self, measurements):
        raise KeyboardInterrupt


def test_example_keyboard_interrupt(monkeypatch, capsys):
    monkeypatch.setattr(sys.modules[__name__], 'LiveChart', _InterruptingChart)
    options = {'simulate': True, 'driver_setup': {'Model': '4082', 'BoardType': 'PXIe', }, }
    total_samples = example('Dev1', options, 'DC_VOLTS', 10, 5.5, 4)
    assert total_samples == 4
    assert 'Total measurements: 4' in capsys.readouterr().out


def test_main(monkeypatch):
    monkeypatch.setattr(sys.modules[__name__], 'LiveChart', _StubChart)
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:4082; BoardType:PXIe']
    assert _main(cmd_line) == 8


def test_print_measurements():
    output = io.StringIO()
    with redirect_stdout(output):
        print_measurements([1.0, 2.0])
        print_measurements([3.0, 4.0])
    assert output.getvalue() == '\rMeasurements: [1.0, 2.0]\033[K\rMeasurements: [3.0, 4.0]\033[K'


if __name__ == '__main__':
    main()
