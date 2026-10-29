#!/usr/bin/python

import argparse
import niscope
import pytest
import sys

PLOT_STYLES = {'LINE': '-', 'POINTS': '.'}
PLOT_RELATIVE_TO = ('TRIGGER', 'ABSOLUTE')
TRIGGER_TYPES = ('EDGE', 'IMMEDIATE')


def _plot_records(plt, waveforms, plot_style, plot_relative_to):
    figure, axes = plt.subplots()
    axes.set_title('Scope Multi Record')
    axes.set_xlabel('Time relative to trigger (s)' if plot_relative_to == 'TRIGGER' else 'Absolute time (s)')
    axes.set_ylabel('Amplitude (V)')
    axes.grid(True)
    for waveform in waveforms:
        initial_x = waveform.relative_initial_x if plot_relative_to == 'TRIGGER' else waveform.absolute_initial_x
        samples = waveform.samples.tolist()  # samples is a memoryview, which matplotlib cannot plot
        x = [initial_x + i * waveform.x_increment for i in range(len(samples))]
        axes.plot(x, samples, PLOT_STYLES[plot_style], label=f'Record {waveform.record}')
    axes.legend(loc='upper right')
    return figure


def example(resource_name, options, channel, vertical_range, min_sample_rate, min_record_length, num_records, plot_style, plot_relative_to,
            trigger_type):
    import matplotlib.pyplot as plt

    with niscope.Session(resource_name=resource_name, options=options) as session:
        session.channels[channel].configure_vertical(range=vertical_range, coupling=niscope.VerticalCoupling.DC)
        session.configure_horizontal_timing(min_sample_rate=min_sample_rate, min_num_pts=min_record_length, ref_position=50.0, num_records=num_records, enforce_realtime=True)
        # Configure the selected trigger here; add other trigger types to this block as needed.
        if trigger_type == 'EDGE':
            session.configure_trigger_edge(trigger_source='0', level=0.0, trigger_coupling=niscope.TriggerCoupling.DC, slope=niscope.TriggerSlope.POSITIVE)
        else:
            session.configure_trigger_immediate()
        with session.initiate():
            # Wait for num_records to be acquired, then return their waveforms.
            waveforms = session.channels[channel].fetch(num_records=num_records)

    figure = _plot_records(plt, waveforms, plot_style, plot_relative_to)
    try:
        if plt.fignum_exists(figure.number):
            plt.show()
    finally:
        plt.close(figure)
    return waveforms


def _main(argsv):
    parser = argparse.ArgumentParser(description='Acquires multiple triggered records from a channel and plots them.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Specifies the resource name of the device to initialize.')
    parser.add_argument('-c', '--channel', default='0', help='Channel to use')
    parser.add_argument('-T', '--trigger-type', default='EDGE', choices=TRIGGER_TYPES, type=str.upper, help='EDGE configures the digitizer for edge triggering (channel 0, 0 V, DC coupling, rising slope). IMMEDIATE triggers as soon as the pretrigger samples are acquired.')
    parser.add_argument('-v', '--vertical-range', default=5.0, type=float, help='Specifies the absolute value of the input range for a channel in volts.')
    parser.add_argument('-r', '--min-sample-rate', default=1e7, type=float, help='The sampling rate for the acquisition.')
    parser.add_argument('-N', '--num-records', default=2, type=int, help='The number of records to acquire')
    parser.add_argument('-l', '--min-record-length', default=256, type=int, help='The minimum number of points you need in the record for each channel.')
    parser.add_argument('-R', '--plot-relative-to', default='TRIGGER', choices=PLOT_RELATIVE_TO, type=str.upper, help='Time reference for the plot; ABSOLUTE requires a device that supports absolute timestamps.')
    parser.add_argument('-p', '--plot-style', default='POINTS', choices=PLOT_STYLES.keys(), type=str.upper, help='Plot the records as a continuous line or as individual points.')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Specifies the initial value of certain properties for the session.')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.option_string, args.channel, args.vertical_range, args.min_sample_rate, args.min_record_length, args.num_records, args.plot_style, args.plot_relative_to,
            args.trigger_type)


def main():
    _main(sys.argv[1:])


def test_example():
    plt = pytest.importorskip('matplotlib.pyplot')
    plt.switch_backend('Agg')  # Avoid opening a chart window during the test
    options = {'simulate': True, 'driver_setup': {'Model': '5164', 'BoardType': 'PXIe', }, }
    waveforms = example('PXI1Slot2', options, '0', 5.0, 1e7, 256, 3, 'POINTS', 'TRIGGER', 'EDGE')
    assert len(waveforms) == 3


def test_main():
    plt = pytest.importorskip('matplotlib.pyplot')
    plt.switch_backend('Agg')  # Avoid opening a chart window during the test
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:5164; BoardType:PXIe', '--num-records', '2', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()
