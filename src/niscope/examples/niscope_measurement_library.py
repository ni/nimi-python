#!/usr/bin/python

import argparse
import niscope
import pytest
import sys


def _create_chart(plt):
    figure, axes = plt.subplots()
    axes.set_title('Waveform Graph')
    axes.set_xlabel('Time (s)')
    axes.set_ylabel('Amplitude (V)')
    axes.grid(True)
    figure.tight_layout()
    return figure, axes


def _update_chart(axes, waveforms):
    while len(axes.lines) < len(waveforms):
        axes.plot([], [], label=waveforms[len(axes.lines)].channel)
        axes.legend(loc='upper right')
    for line, waveform in zip(axes.lines, waveforms):
        x = [waveform.relative_initial_x + i * waveform.x_increment for i in range(len(waveform.samples))]
        # read() returns samples as a memoryview, which matplotlib cannot copy
        line.set_data(x, list(waveform.samples))
    axes.relim()
    axes.autoscale_view()


def example(resource_name, channels, options, vertical_range, vertical_coupling, min_sample_rate, min_record_length,
            enforce_realtime, trigger_type, trigger_source, trigger_level, trigger_slope, trigger_coupling, timeout,
            scalar_measurement, reference_level_units, low_ref, mid_ref, high_ref, iterations):
    import matplotlib.pyplot as plt

    with niscope.Session(resource_name=resource_name, options=options) as session:
        session.configure_vertical(range=vertical_range, coupling=niscope.VerticalCoupling[vertical_coupling])
        session.configure_horizontal_timing(min_sample_rate=min_sample_rate, min_num_pts=min_record_length, ref_position=50.0, num_records=1, enforce_realtime=enforce_realtime)
        if trigger_type == 'EDGE':
            session.configure_trigger_edge(trigger_source, trigger_level, niscope.TriggerCoupling[trigger_coupling], niscope.TriggerSlope[trigger_slope])
        else:
            session.configure_trigger_immediate()

        channel = session.channels[channels]
        channel.meas_ref_level_units = niscope.RefLevelUnits[reference_level_units]
        channel.meas_chan_low_ref_level = low_ref
        channel.meas_chan_mid_ref_level = mid_ref
        channel.meas_chan_high_ref_level = high_ref

        figure, axes = _create_chart(plt)

        iteration = 0
        try:
            # Run until the chart is closed, Ctrl+C is pressed, or the iteration limit is reached.
            while plt.fignum_exists(figure.number) and (iterations is None or iteration < iterations):
                # The statistics accumulate once per acquisition, so read a new waveform before each fetch.
                waveforms = channel.read(num_samples=min_record_length, timeout=timeout)
                _update_chart(axes, waveforms)
                stats = channel.fetch_measurement_stats(niscope.ScalarMeasurement[scalar_measurement])
                print(f'Acquisition {iteration}: {scalar_measurement}')
                for stat in stats:
                    print(stat)
                iteration += 1
                plt.pause(0.02)

            # Keep the final plot window open after acquisition stops until the user closes it.
            if iterations is not None and plt.fignum_exists(figure.number):
                plt.show()
        except KeyboardInterrupt:
            pass
        finally:
            plt.close(figure)


def _main(argsv):
    parser = argparse.ArgumentParser(description='Fetches scalar measurements and their statistics from an NI digitizer.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot3', help='Specifies the resource name of the device to initialize')
    parser.add_argument('-m', '--scalar-measurement', default='FFT_FREQUENCY', choices=niscope.ScalarMeasurement.__members__.keys(), type=str.upper, help='The scalar measurement to be performed on each fetched waveform.')
    parser.add_argument('--reference-level-units', default='PERCENTAGE', choices=niscope.RefLevelUnits.__members__.keys(), type=str.upper, help='Specifies the units of the reference levels.')
    parser.add_argument('--low-ref', default=10.0, type=float, help='Stores the low reference level used in many scalar measurements.')
    parser.add_argument('--mid-ref', default=50.0, type=float, help='Stores the mid reference level used in many scalar measurements.')
    parser.add_argument('--high-ref', default=90.0, type=float, help='Stores the high reference level used in many scalar measurements.')
    parser.add_argument('-s', '--min-sample-rate', default=1000000.0, type=float, help='Specify the sampling rate for the acquisition in Samples per second.')
    parser.add_argument('-l', '--min-record-length', default=1000, type=int, help='Specifies the minimum number of points you require in the waveform record for each channel.')
    parser.add_argument('--enforce-realtime', action=argparse.BooleanOptionalAction, default=True, help='Indicates whether the digitizer enforces real-time measurements or allows equivalent-time measurements.')
    parser.add_argument('-c', '--channels', default='0', help='Comma-separated list of channels to plot, one line per channel')
    parser.add_argument('-v', '--vertical-range', default=2.0, type=float, help='Specifies the absolute value of the input range for a channel in volts.')
    parser.add_argument('--vertical-coupling', default='DC', choices=niscope.VerticalCoupling.__members__.keys(), type=str.upper, help='Specifies how the digitizer couples the input signal for the channel.')
    parser.add_argument('--trigger-type', default='EDGE', choices=['EDGE', 'IMMEDIATE'], type=str.upper, help='Selects edge or immediate triggering.')
    parser.add_argument('--trigger-source', default='0', help='Specifies the source the digitizer monitors for the trigger event.')
    parser.add_argument('--trigger-level', default=0.0, type=float, help='Specifies the voltage threshold for the trigger subsystem.')
    parser.add_argument('--trigger-slope', default='POSITIVE', choices=niscope.TriggerSlope.__members__.keys(), type=str.upper, help='Specifies if a rising or a falling edge triggers the digitizer.')
    parser.add_argument('--trigger-coupling', default='DC', choices=niscope.TriggerCoupling.__members__.keys(), type=str.upper, help='Specifies how the digitizer couples the trigger source.')
    parser.add_argument('-t', '--timeout', default=5.0, type=float, help='The time to wait in seconds for data to be acquired; using 0 for this parameter tells NI-SCOPE to fetch whatever is currently available.')
    parser.add_argument('--total-iterations', default=None, type=int, help='Stops after this many acquisitions and keeps the chart open until its window is closed; omit to run until the chart window is closed or Ctrl+C is pressed.')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Specifies the initial value of certain properties for the session.')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.channels, args.option_string, args.vertical_range, args.vertical_coupling,
            args.min_sample_rate, args.min_record_length, args.enforce_realtime, args.trigger_type, args.trigger_source,
            args.trigger_level, args.trigger_slope, args.trigger_coupling, args.timeout, args.scalar_measurement,
            args.reference_level_units, args.low_ref, args.mid_ref, args.high_ref, args.total_iterations)


def main():
    _main(sys.argv[1:])


def test_example():
    plt = pytest.importorskip('matplotlib.pyplot')
    plt.switch_backend('Agg')  # Avoid opening a chart window during the test
    options = {'simulate': True, 'driver_setup': {'Model': '5164', 'BoardType': 'PXIe', }, }
    example('PXI1Slot2', '0', options, 2.0, 'DC', 1000000.0, 1000, True, 'IMMEDIATE', '0', 0.0, 'POSITIVE', 'DC', 5.0,
            'FREQUENCY', 'PERCENTAGE', 10.0, 50.0, 90.0, 2)


def test_main():
    plt = pytest.importorskip('matplotlib.pyplot')
    plt.switch_backend('Agg')  # Avoid opening a chart window during the test
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:5164; BoardType:PXIe', '--trigger-type', 'immediate', '--total-iterations', '2', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()
