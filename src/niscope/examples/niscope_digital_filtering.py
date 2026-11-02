#!/usr/bin/python

import argparse
import niscope
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


def example(
    resource_name, channels, options, min_sample_rate, min_record_length,
    filter_name, filter_type, cutoff_frequency, center_frequency, width,
    fir_taps, fir_window, iir_order, fft_function, total_iterations,
):
    print(f'Starting acquisition on resource {resource_name}, for {total_iterations if total_iterations is not None else "continuous"} iterations.')
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

        iterations = 0
        try:
            # A total_iterations of None runs until Ctrl+C is pressed
            while total_iterations is None or iterations < total_iterations:
                # The filter runs as a processing step before any other measurement; it is added and cleared on every acquisition
                channel_session.add_waveform_processing(FILTERS[filter_name])
                try:
                    with session.initiate():
                        channel_session.fetch_array_measurement(niscope.ArrayMeasurement.NO_MEASUREMENT)
                        channel_session.fetch_array_measurement(FFT_FUNCTIONS[fft_function])
                finally:
                    channel_session.clear_waveform_processing()
                iterations += 1
        except KeyboardInterrupt:
            pass

        print('Completed {} acquisitions.'.format(iterations))


def _main(argsv):
    parser = argparse.ArgumentParser(description='Applies a digital filter to acquired waveforms and computes the filtered waveform and its FFT amplitude spectrum.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot3', help='Specifies the resource name of the device to initialize.')
    parser.add_argument('-c', '--channels', default='0', help='Comma-separated list of channels to acquire')
    parser.add_argument('-l', '--min-record-length', default=4096, type=int, help='Specifies the minimum number of points you require in the waveform record for each channel.')
    parser.add_argument('-sr', '--min-sample-rate', default=10000000.0, type=float, help='Specify the sampling rate for the acquisition in Samples per second.')
    parser.add_argument('-f', '--filter', default='CHEBYSHEV', choices=FILTERS.keys(), type=str.upper, help='Filter to apply')
    parser.add_argument('-fft', '--fft-function', default='DB', choices=FFT_FUNCTIONS.keys(), type=str.upper, help='FFT amplitude spectrum function')
    parser.add_argument('-ft', '--filter-type', default='LOWPASS', choices=niscope.FilterType.__members__.keys(), type=str.upper, help='Specifies the type of filter, for both IIR and FIR filters.')
    parser.add_argument('-cf', '--cutoff-frequency', default=2500000.0, type=float, help='Specifies the cutoff frequency in hertz for filters of type lowpass and highpass.')
    parser.add_argument('-cc', '--center-frequency', default=500000.0, type=float, help='The center frequency in hertz for filters of type bandpass and bandstop.')
    parser.add_argument('-w', '--width', default=100000.0, type=float, help='Specifies the width of bandpass and bandstop type filters in hertz.')
    parser.add_argument('-t', '--fir-taps', default=25, type=int, help='Defines the number of taps (coefficients) for an FIR filter.')
    parser.add_argument('-fw', '--fir-window', default='HANNING', choices=niscope.FIRFilterWindow.__members__.keys(), type=str.upper, help='Specifies the FIR window type.')
    parser.add_argument('-o', '--iir-order', default=2, type=int, help='Specifies the order of an IIR filter.')
    parser.add_argument('--total-iterations', default=100, type=int, help='Number of acquisitions to perform before stopping.')
    parser.add_argument('--continuous', action='store_true', help='Acquire until Ctrl+C is pressed; overrides --total-iterations.')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Specifies initialization commands.')
    args = parser.parse_args(argsv)
    example(
        args.resource_name, args.channels, args.option_string, args.min_sample_rate, args.min_record_length,
        args.filter, args.filter_type, args.cutoff_frequency, args.center_frequency, args.width,
        args.fir_taps, args.fir_window, args.iir_order, args.fft_function, None if args.continuous else args.total_iterations,
    )


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '5164', 'BoardType': 'PXIe', }, }
    example(
        'PXI1Slot2', '0', options, 10000000.0, 4096,
        'CHEBYSHEV', 'LOWPASS', 2500000.0, 500000.0, 100000.0,
        25, 'HANNING', 2, 'DB', 2,
    )


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:5164; BoardType:PXIe', '--total-iterations', '2', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()
