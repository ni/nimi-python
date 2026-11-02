#!/usr/bin/python

import argparse
import niscope
import sys


def example(resource_name, channels, options, min_record_length, voltage_range, voltage_offset, source, rate, divisor, multiplier, total_iterations):
    print(f'Starting acquisition on resource {resource_name}, for {total_iterations if total_iterations is not None else "continuous"} iterations.')
    with niscope.Session(resource_name=resource_name, options=options) as session:
        channel_session = session.channels[channels]
        channel_session.configure_vertical(range=voltage_range, coupling=niscope.VerticalCoupling.DC, offset=voltage_offset)
        session.configure_trigger_immediate()
        session.horz_min_num_pts = min_record_length
        session.samp_clk_timebase_src = source
        session.samp_clk_timebase_rate = rate
        session.samp_clk_timebase_div = divisor
        session.sample_clock_timebase_multiplier = multiplier

        iterations = 0
        try:
            # Run until Ctrl+C is pressed or the iteration limit is reached.
            while total_iterations is None or iterations < total_iterations:
                # read() initiates the acquisition, waits for it to complete and fetches the data
                channel_session.read(num_samples=min_record_length)
                iterations += 1
        except KeyboardInterrupt:
            pass

        print('Completed {} acquisitions.'.format(iterations))


def _main(argsv):
    parser = argparse.ArgumentParser(description='Continuously acquires a waveform using an external sample clock.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot3', help='Specifies the resource name of the device to initialize.')
    parser.add_argument('-c', '--channels', default='0', help='Comma-separated list of channels to acquire')
    parser.add_argument('-v', '--voltage-range', default=1.0, type=float, help='Specifies the absolute value of the input range for a channel in volts.')
    parser.add_argument('--voltage-offset', default=0.0, type=float, help='Specifies the location of the center of the range. The value is with respect to ground and is in volts.')
    parser.add_argument('-l', '--min-record-length', default=1000, type=int, help='Specifies the minimum number of points you require in the waveform record for each channel.')
    parser.add_argument('-s', '--source', default='VAL_CLK_IN', type=str, help='Specifies the source of the sample clock timebase, which is the timebase used to control waveform sampling.')
    parser.add_argument('-r', '--rate', default=1e8, type=float, help='Specifies the frequency in hertz of the external clock used as the timebase source.')
    parser.add_argument('-d', '--divisor', default=1, type=int, help='Specifies the ratio between the sample clock timebase rate and the actual sample rate, which can be slower.')
    parser.add_argument('-m', '--multiplier', default=1, type=int, help='Specifies the ratio between the samp_clk_timebase_rate and the actual sample rate, which can be higher.')
    parser.add_argument('--total-iterations', default=100, type=int, help='Number of acquisitions to perform before stopping.')
    parser.add_argument('--continuous', action='store_true', help='Acquire until Ctrl+C is pressed; overrides --total-iterations.')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Specifies the initial value of certain properties for the session.')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.channels, args.option_string, args.min_record_length, args.voltage_range, args.voltage_offset, args.source, args.rate, args.divisor, args.multiplier, None if args.continuous else args.total_iterations)


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '5164', 'BoardType': 'PXIe', }, }
    # The simulated PXIe-5164 only accepts a 1 GHz sample clock timebase
    example('PXI1Slot2', '0', options, 1000, 1.0, 0.0, 'VAL_CLK_IN', 1e9, 1, 1, 2)


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:5164; BoardType:PXIe', '--rate', '1e9', '--total-iterations', '2', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()
