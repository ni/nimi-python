#!/usr/bin/python

import argparse
import niscope
import pytest
import sys

FILTERS = {
    'NONE': niscope.ArrayMeasurement.NO_MEASUREMENT,
    'FIR': niscope.ArrayMeasurement.WINDOWED_FIR_FILTER,
    'BESSEL': niscope.ArrayMeasurement.BESSEL_FILTER,
    'BUTTERWORTH': niscope.ArrayMeasurement.BUTTERWORTH_FILTER,
    'CHEBYSHEV': niscope.ArrayMeasurement.CHEBYSHEV_FILTER,
}
FFT_FUNCTIONS = {
    'VOLTS_RMS': niscope.ArrayMeasurement.FFT_AMP_SPECTRUM_VOLTS_RMS,
    'DB': niscope.ArrayMeasurement.FFT_AMP_SPECTRUM_DB,
}


def _create_chart(plt):
    figure, (waveform_axes, spectrum_axes) = plt.subplots(2, 1)
    (waveform_line,) = waveform_axes.plot([])
    (spectrum_line,) = spectrum_axes.plot([])
    waveform_axes.set_title('Filtered Waveform')
    waveform_axes.set_xlabel('Time (s)')
    waveform_axes.set_ylabel('Amplitude')
    spectrum_axes.set_title('Spectrum')
    spectrum_axes.set_xlabel('Frequency (Hz)')
    spectrum_axes.set_ylabel('Amplitude')
    for axes in (waveform_axes, spectrum_axes):
        axes.grid(True)
    figure.tight_layout()
    return figure, waveform_axes, waveform_line, spectrum_axes, spectrum_line


def _update_chart(waveform_axes, waveform_line, filtered, spectrum_axes, spectrum_line, spectrum):
    for axes, line, waveforms in ((waveform_axes, waveform_line, filtered), (spectrum_axes, spectrum_line, spectrum)):
        for waveform in waveforms:
            x = [waveform.relative_initial_x + i * waveform.x_increment for i in range(len(waveform.samples))]
            line.set_data(x, waveform.samples)
        axes.relim()
        axes.autoscale_view()


def example(
    resource_name, channels, options, min_sample_rate, min_record_length,
    filter_name, filter_type, cutoff_frequency, center_frequency, width,
    fir_taps, fir_window, iir_order, fft_function, total_iterations,
):
    # Imported lazily because matplotlib is unavailable on some platforms (e.g. 32-bit Python)
    import matplotlib.pyplot as plt

    with niscope.Session(resource_name=resource_name, options=options) as session:
        session.configure_vertical(range=2.0, coupling=niscope.VerticalCoupling.DC)
        session.configure_horizontal_timing(min_sample_rate=min_sample_rate, min_num_pts=min_record_length, ref_position=50.0, num_records=1, enforce_realtime=True)

        channel_session = session.channels[channels]
        channel_session.meas_filter_type = niscope.FilterType[filter_type]
        channel_session.meas_filter_cutoff_freq = cutoff_frequency
        channel_session.meas_filter_center_freq = center_frequency
        channel_session.meas_filter_width = width
        channel_session.meas_filter_taps = fir_taps
        channel_session.meas_fir_filter_window = niscope.FIRFilterWindow[fir_window]
        channel_session.meas_filter_order = iir_order
        channel_session.meas_filter_transient_waveform_percent = 20.0
        channel_session.meas_filter_ripple = 0.5

        figure, waveform_axes, waveform_line, spectrum_axes, spectrum_line = _create_chart(plt)

        iterations = 0
        try:
            # A total_iterations of None runs until the chart window is closed or Ctrl+C is pressed
            while plt.fignum_exists(figure.number) and (total_iterations is None or iterations < total_iterations):
                # The filter runs as a processing step before any other measurement; it is added and cleared on every acquisition
                channel_session.add_waveform_processing(FILTERS[filter_name])
                try:
                    with session.initiate():
                        filtered = channel_session.fetch_array_measurement(niscope.ArrayMeasurement.NO_MEASUREMENT)
                        spectrum = channel_session.fetch_array_measurement(FFT_FUNCTIONS[fft_function])
                finally:
                    channel_session.clear_waveform_processing()

                _update_chart(waveform_axes, waveform_line, filtered, spectrum_axes, spectrum_line, spectrum)
                iterations += 1
                plt.pause(0.02)

            # The acquisition has stopped; keep the final chart on screen until its window is closed
            if total_iterations is not None and plt.fignum_exists(figure.number):
                plt.show()
        except KeyboardInterrupt:
            pass
        finally:
            plt.close(figure)


def _main(argsv):
    parser = argparse.ArgumentParser(description='Continuously applies a digital filter to acquired waveforms and plots the filtered waveform and its FFT amplitude spectrum.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot3', help='Specifies the resource name of the device to initialize.')
    parser.add_argument('-c', '--channels', default='0', help='Channel to plot')
    parser.add_argument('-sr', '--min-sample-rate', default=10000000.0, type=float, help='Specify the sampling rate for the acquisition in Samples per second.')
    parser.add_argument('-l', '--min-record-length', default=4096, type=int, help='Specifies the minimum number of points you require in the waveform record for each channel.')
    parser.add_argument('-f', '--filter', default='CHEBYSHEV', choices=FILTERS.keys(), type=str.upper, help='Filter to apply')
    parser.add_argument('-ft', '--filter-type', default='LOWPASS', choices=niscope.FilterType.__members__.keys(), type=str.upper, help='Specifies the type of filter, for both IIR and FIR filters.')
    parser.add_argument('-cf', '--cutoff-frequency', default=2500000.0, type=float, help='Specifies the cutoff frequency in hertz for filters of type lowpass and highpass.')
    parser.add_argument('-cc', '--center-frequency', default=500000.0, type=float, help='The center frequency in hertz for filters of type bandpass and bandstop.')
    parser.add_argument('-w', '--width', default=100000.0, type=float, help='Specifies the width of bandpass and bandstop type filters in hertz.')
    parser.add_argument('-t', '--fir-taps', default=25, type=int, help='Defines the number of taps (coefficients) for an FIR filter.')
    parser.add_argument('-fw', '--fir-window', default='HANNING', choices=niscope.FIRFilterWindow.__members__.keys(), type=str.upper, help='Specifies the FIR window type.')
    parser.add_argument('-o', '--iir-order', default=2, type=int, help='Specifies the order of an IIR filter.')
    parser.add_argument('-fft', '--fft-function', default='DB', choices=FFT_FUNCTIONS.keys(), type=str.upper, help='FFT amplitude spectrum function')
    parser.add_argument('--total-iterations', default=None, type=int, help='Stops after this many acquisitions and keeps the chart open until its window is closed; omit to run until the chart window is closed or Ctrl+C is pressed.')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Specifies initialization commands.')
    args = parser.parse_args(argsv)
    example(
        args.resource_name, args.channels, args.option_string, args.min_sample_rate, args.min_record_length,
        args.filter, args.filter_type, args.cutoff_frequency, args.center_frequency, args.width,
        args.fir_taps, args.fir_window, args.iir_order, args.fft_function, args.total_iterations,
    )


def main():
    _main(sys.argv[1:])


def test_example():
    plt = pytest.importorskip('matplotlib.pyplot')
    plt.switch_backend('Agg')  # Avoid opening a chart window during the test
    options = {'simulate': True, 'driver_setup': {'Model': '5164', 'BoardType': 'PXIe', }, }
    example(
        'PXI1Slot2', '0', options, 10000000.0, 4096,
        'CHEBYSHEV', 'LOWPASS', 2500000.0, 500000.0, 100000.0,
        25, 'HANNING', 2, 'DB', 2,
    )


def test_main():
    plt = pytest.importorskip('matplotlib.pyplot')
    plt.switch_backend('Agg')  # Avoid opening a chart window during the test
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:5164; BoardType:PXIe', '--total-iterations', '2', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()
