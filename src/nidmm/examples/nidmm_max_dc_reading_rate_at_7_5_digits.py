#!/usr/bin/python

import argparse
import collections
import nidmm
import pytest
import sys
import time


SUPPORTED_MODELS = ('4071', '4081')

CHART_HISTORY_SIZE = 250


def _create_chart(plt):
    figure, axes = plt.subplots()
    (line,) = axes.plot([])
    axes.set_xlabel('Sample Number')
    axes.set_ylabel('Reading Value')
    axes.grid(True)
    return figure, axes, line


def _update_chart(plt, figure, axes, line, measurements, new_samples, samples_fetched, reads_per_sec):
    if new_samples:
        measurements.extend(new_samples)
        samples_fetched += len(new_samples)
        # Offset X values to account for readings removed from the history buffer
        first_sample = samples_fetched - len(measurements)
        line.set_data(range(first_sample, samples_fetched), measurements)
        axes.set_title(f'Reads/sec: {reads_per_sec:.0f}')
        axes.relim()
        axes.autoscale_view()
    plt.pause(0.001)
    return samples_fetched, plt.fignum_exists(figure.number)


def example(device_name, options, powerline_frequency, measurement_range, aperture_time, adc_calibration, auto_zero, number_of_averages, total_samples):
    # Imported lazily because matplotlib is unavailable on some platforms (e.g. 32-bit Python)
    import matplotlib.pyplot as plt

    with nidmm.Session(resource_name=device_name, reset_device=True, options=options) as session:
        if not session.instrument_model.endswith(SUPPORTED_MODELS):
            raise ValueError(f'{session.instrument_model} is not supported. This example requires an NI PXI-4071 or NI PXIe-4081.')

        # Powerline frequency defines the timebase for aperture values in PLCs.
        session.powerline_freq = powerline_frequency
        session.configure_measurement_digits(measurement_function=nidmm.Function.DC_VOLTS, range=measurement_range, resolution_digits=7.5)
        # A sample count of zero selects continuous acquisition.
        session.configure_multi_point(trigger_count=1, sample_count=0)
        session.aperture_time_units = nidmm.ApertureTimeUnits.POWER_LINE_CYCLES
        session.aperture_time = aperture_time
        session.number_of_averages = number_of_averages
        session.auto_zero = nidmm.AutoZero[auto_zero]
        # Disabling ADC calibration avoids the gain-reference measurement and increases reading rate.
        session.adc_calibration = nidmm.ADCCalibration[adc_calibration]

        figure, axes, line = _create_chart(plt)
        measurements = collections.deque(maxlen=CHART_HISTORY_SIZE)
        samples_fetched = 0
        start_time = time.perf_counter()
        try:
            with session.initiate():
                chart_open = True
                while chart_open and (total_samples is None or samples_fetched < total_samples):
                    backlog, _ = session.read_status()
                    if total_samples is not None:
                        backlog = min(backlog, total_samples - samples_fetched)
                    new_samples = session.fetch_multi_point(array_size=backlog) if backlog > 0 else ()
                    reads_per_sec = (samples_fetched + len(new_samples)) / (time.perf_counter() - start_time)
                    samples_fetched, chart_open = _update_chart(
                        plt, figure, axes, line, measurements, new_samples, samples_fetched, reads_per_sec,
                    )

            # The acquisition has stopped; keep the final chart on screen until its window is closed
            if total_samples is not None and plt.fignum_exists(figure.number):
                plt.show()
        except KeyboardInterrupt:
            pass
        finally:
            plt.close(figure)


def _main(argsv):
    parser = argparse.ArgumentParser(description='Achieves the higher DC voltage reading rate at 7.5 digits of resolution with a PXI-4071 or PXIe-4081 and charts the readings.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--device-name', default='PXI1Slot2', help='Contains the resource_name of the device to initialize.')
    parser.add_argument('-p', '--powerline-frequency', default=60.0, type=float, choices=[50.0, 60.0], help='Specifies the powerline frequency.')
    parser.add_argument('-r', '--range', default=10.0, type=float, help='Specifies the range for the function specified in the Measurement_Function parameter.')
    parser.add_argument('-a', '--aperture-time', default=1.0, type=float, help='Specifies the measurement aperture time for the current configuration, in powerline cycles (PLCs).')
    parser.add_argument('-c', '--adc-calibration', default='OFF', choices=nidmm.ADCCalibration.__members__.keys(), type=str.upper, help='Specifies the ADC calibration mode.')
    parser.add_argument('-z', '--auto-zero', default='ON', choices=nidmm.AutoZero.__members__.keys(), type=str.upper, help='Specifies the AutoZero mode.')
    parser.add_argument('-v', '--number-of-averages', default=4, type=int, help='Specifies the number of averages to perform in a measurement.')
    parser.add_argument('--total-samples', default=None, type=int, help='Stops fetching after this many samples and keeps the chart open until its window is closed; omit to run until the chart window is closed.')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Sets the initial value of certain attributes for the session.')
    args = parser.parse_args(argsv)
    example(args.device_name, args.option_string, args.powerline_frequency, args.range, args.aperture_time, args.adc_calibration, args.auto_zero, args.number_of_averages, args.total_samples)


def main():
    _main(sys.argv[1:])


def test_example():
    plt = pytest.importorskip('matplotlib.pyplot')
    plt.switch_backend('Agg')  # Avoid opening a chart window during the test
    options = {'simulate': True, 'driver_setup': {'Model': '4081', 'BoardType': 'PXIe', }, }
    example('PXI1Slot2', options, 60.0, 10.0, 1.0, 'OFF', 'ON', 4, 100)


def test_main():
    plt = pytest.importorskip('matplotlib.pyplot')
    plt.switch_backend('Agg')  # Avoid opening a chart window during the test
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:4081; BoardType:PXIe', '--total-samples', '100', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()
