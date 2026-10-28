#!/usr/bin/python

import argparse
import hightime
import niscope
import numpy as np
import pytest
import sys

TRIGGER_TYPES = ['IMMEDIATE', 'EDGE', 'DIGITAL', 'WINDOW', 'HYSTERESIS']
# niscope has no public enum for string trigger sources, so these mirror the VI's digital trigger source ring.
DIGITAL_TRIGGER_SOURCES = [
    'VAL_IMMEDIATE', 'VAL_SW_TRIG_FUNC', 'VAL_PXI_STAR',
    *[f'VAL_RTSI_{i}' for i in range(7)],
    *[f'VAL_PFI_{i}' for i in range(3)],
    *[f'VAL_TTL{i}' for i in range(7)],
    *[f'VAL_AUX_0_PFI_{i}' for i in range(8)],
]


def _create_chart(plt):
    figure, axes = plt.subplots()
    axes.set_title('Waveform(s)')
    axes.set_xlabel('Time (s)')
    axes.set_ylabel('Voltage (V)')
    axes.grid(True)
    return figure, axes


def _update_chart(axes, waveforms):
    if not axes.lines:
        for waveform in waveforms:
            axes.plot([], [], label=waveform.channel)
        axes.legend(loc='upper right')
    for line, waveform in zip(axes.lines, waveforms):
        x = waveform.relative_initial_x + np.arange(len(waveform.samples)) * waveform.x_increment
        # Samples may be a memoryview, which matplotlib cannot copy
        line.set_data(x, list(waveform.samples))
    axes.relim()
    axes.autoscale_view()


def example(resource_name, options, channel_name, vertical_range, vertical_offset, vertical_coupling, probe_attenuation,
            input_impedance, max_input_frequency, min_sample_rate, min_record_length, reference_position, enforce_realtime,
            trigger_modifier, trigger_type, trigger_source, digital_trigger_source, trigger_level, trigger_slope, trigger_coupling,
            window_low_level, window_high_level, window_mode, hysteresis, trigger_delay, timeout, total_iterations):
    import matplotlib.pyplot as plt

    figure, axes = _create_chart(plt)
    acquisition_count = 1
    try:
        # 1. Opening session
        with niscope.Session(resource_name=resource_name, options=options) as session:
            channel = session.channels[channel_name]
            # Run until the chart is closed, Ctrl+C is pressed, or the iteration limit is reached.
            while plt.fignum_exists(figure.number) and (total_iterations is None or acquisition_count <= total_iterations):
                # 2. Configuring vertical
                channel.configure_vertical(range=vertical_range, coupling=niscope.VerticalCoupling[vertical_coupling], offset=vertical_offset,
                                           probe_attenuation=probe_attenuation, enabled=True)
                # 3. Configuring channel characteristics
                channel.configure_chan_characteristics(input_impedance=input_impedance, max_input_frequency=max_input_frequency)
                # 4. Configuring horizontal
                session.configure_horizontal_timing(min_sample_rate=min_sample_rate, min_num_pts=min_record_length, ref_position=reference_position,
                                                    num_records=1, enforce_realtime=enforce_realtime)
                # 5. Configuring auto trigger
                session.trigger_modifier = niscope.TriggerModifier[trigger_modifier]
                # 6. Configuring trigger
                delay = hightime.timedelta(seconds=trigger_delay)
                match trigger_type:
                    case 'IMMEDIATE':
                        session.configure_trigger_immediate()
                    case 'EDGE':
                        session.configure_trigger_edge(trigger_source, trigger_level, niscope.TriggerCoupling[trigger_coupling], slope=niscope.TriggerSlope[trigger_slope], delay=delay)
                    case 'DIGITAL':
                        session.configure_trigger_digital(digital_trigger_source, slope=niscope.TriggerSlope[trigger_slope], delay=delay)
                    case 'WINDOW':
                        session.configure_trigger_window(trigger_source, window_low_level, window_high_level, niscope.TriggerWindowMode[window_mode], niscope.TriggerCoupling[trigger_coupling], delay=delay)
                    case 'HYSTERESIS':
                        session.configure_trigger_hysteresis(trigger_source, trigger_level, hysteresis, niscope.TriggerCoupling[trigger_coupling], slope=niscope.TriggerSlope[trigger_slope], delay=delay)
                # 7. Initiating and 8. fetching
                with session.initiate():
                    waveforms = channel.fetch(timeout=hightime.timedelta(seconds=timeout))
                # 9. Querying actual (coerced) values
                print(f'Acquisition {acquisition_count}:')
                print(f'Actual Sample Rate: {session.horz_sample_rate}')
                print(f'Actual Record Length: {session.horz_record_length}')
                _update_chart(axes, waveforms)
                acquisition_count += 1
                plt.pause(0.02)
        # Keep the final plot window open after acquisition stops until the user closes it.
        if total_iterations is not None and plt.fignum_exists(figure.number):
            plt.show()
    except KeyboardInterrupt:
        pass
    finally:
        plt.close(figure)


def _main(argsv):
    parser = argparse.ArgumentParser(description='Configures the vertical, horizontal, and trigger properties before every acquisition and displays the waveform(s).',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Specifies the resource name of the device to initialize')
    parser.add_argument('-c', '--channel-name', default='0', help='Comma-separated list of channels to plot, one line per channel')
    parser.add_argument('--timeout', default=5.0, type=float, help='The time to wait for data to be acquired; using 0 for this parameter tells NI-SCOPE to fetch whatever is currently available.')
    parser.add_argument('--vertical-range', default=5.0, type=float, help='Specifies the absolute value of the input range for a channel in volts.')
    parser.add_argument('--probe-attenuation', default=1.0, type=float, help='Specifies the probe attenuation for the input channel.')
    parser.add_argument('--vertical-offset', default=0.0, type=float, help='Specifies the location of the center of the range.')
    parser.add_argument('--vertical-coupling', default='DC', choices=niscope.VerticalCoupling.__members__.keys(), type=str.upper,
                        help='Specifies how the digitizer couples the input signal for the channel.')
    parser.add_argument('--max-input-frequency', default=0.0, type=float,
                        help='The bandwidth for the channel; NI-SCOPE sets max_input_frequency to this value. Pass 0 for this value to use the hardware default bandwidth.')
    parser.add_argument('--input-impedance', default=1000000.0, type=float, help='The input impedance for the channel; NI-SCOPE sets input_impedance to this value.')
    parser.add_argument('--min-sample-rate', default=10000000.0, type=float,
                        help='Specify the sampling rate for the acquisition in Samples per second.')
    parser.add_argument('--min-record-length', default=1000, type=int, help='Specifies the minimum number of points you require in the waveform record for each channel.')
    parser.add_argument('--trigger-type', default='IMMEDIATE', choices=TRIGGER_TYPES, type=str.upper,
                        help='Selects the trigger configuration method to call.')
    parser.add_argument('--trigger-source', default='0', help='Specifies the source the digitizer monitors for the trigger event.')
    parser.add_argument('--trigger-slope', default='POSITIVE', choices=niscope.TriggerSlope.__members__.keys(), type=str.upper,
                        help='Specifies whether you want a rising edge or a falling edge to trigger the digitizer.')
    parser.add_argument('--trigger-coupling', default='DC', choices=niscope.TriggerCoupling.__members__.keys(), type=str.upper,
                        help='Applies coupling and filtering options to the trigger signal.')
    parser.add_argument('--trigger-level', default=0.0, type=float, help='The voltage threshold for the trigger.')
    parser.add_argument('--digital-trigger-source', default='VAL_PFI_1', choices=DIGITAL_TRIGGER_SOURCES, type=str.upper,
                        help='Specifies the source the digitizer monitors for the trigger event.')
    parser.add_argument('--window-mode', default='ENTERING', choices=niscope.TriggerWindowMode.__members__.keys(), type=str.upper,
                        help='Specifies whether you want the trigger to occur when the signal enters or leaves a window.')
    parser.add_argument('--window-low-level', default=-0.10, type=float, help='Passes the voltage threshold you want the digitizer to use for low triggering.')
    parser.add_argument('--window-high-level', default=0.10, type=float, help='Passes the voltage threshold you want the digitizer to use for high triggering.')
    parser.add_argument('--hysteresis', default=0.05, type=float, help='Specifies the size of the hysteresis window on either side of the trigger level.')
    parser.add_argument('--trigger-delay', default=0.0, type=float, help='Specifies the trigger delay time in seconds.')
    parser.add_argument('--reference-position', default=50.0, type=float, help='The position of the Reference Event in the waveform record specified as a percentage.')
    parser.add_argument('--trigger-modifier', default='AUTO', choices=niscope.TriggerModifier.__members__.keys(), type=str.upper,
                        help='Configures the device to automatically complete an acquisition if a trigger has not been received.')
    parser.add_argument('--enforce-realtime', action=argparse.BooleanOptionalAction, default=True,
                        help='Indicates whether the digitizer enforces real-time measurements or allows equivalent-time (RIS) measurements.')
    parser.add_argument('--total-iterations', default=None, type=int, help='Specifies the maximum number of acquisitions; omit to run until the chart closes or Ctrl+C is pressed.')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Specifies the initial value of certain properties for the session.')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.option_string, args.channel_name, args.vertical_range, args.vertical_offset, args.vertical_coupling,
            args.probe_attenuation, args.input_impedance, args.max_input_frequency, args.min_sample_rate, args.min_record_length, args.reference_position,
            args.enforce_realtime, args.trigger_modifier, args.trigger_type, args.trigger_source, args.digital_trigger_source, args.trigger_level,
            args.trigger_slope, args.trigger_coupling, args.window_low_level, args.window_high_level, args.window_mode, args.hysteresis, args.trigger_delay,
            args.timeout, args.total_iterations)


def main():
    _main(sys.argv[1:])


def test_example():
    plt = pytest.importorskip('matplotlib.pyplot')
    plt.switch_backend('Agg')  # Avoid opening a chart window during the test
    options = {'simulate': True, 'driver_setup': {'Model': '5164', 'BoardType': 'PXIe', }, }
    example('PXI1Slot2', options, '0', 5.0, 0.0, 'DC', 1.0, 1000000.0, 0.0, 10000000.0, 1000, 50.0, True,
            'AUTO', 'EDGE', '0', 'VAL_PFI_1', 0.0, 'POSITIVE', 'DC', 0.0, 0.0, 'ENTERING', 0.0, 0.0, 5.0, 2)


def test_main():
    plt = pytest.importorskip('matplotlib.pyplot')
    plt.switch_backend('Agg')  # Avoid opening a chart window during the test
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:5164; BoardType:PXIe', '--total-iterations', '2']
    _main(cmd_line)


if __name__ == '__main__':
    main()
