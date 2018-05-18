#!/usr/bin/python

import argparse
import niscope
import pprint
import sys

pp = pprint.PrettyPrinter(indent=4, width=80)


def example(resource_name, channels, options, length, voltage):
    sample_rate = 1000000
    chunk_size = 500000
    sample_time = 100  # in seconds
    total_samples = sample_time * sample_rate
    print('1. Opening session')
    with niscope.Session("5122") as session:
        print('2. Configuring')
        session.configure_horizontal_timing(min_sample_rate=sample_rate, min_num_pts=1, ref_position=0.0, num_records=1, enforce_realtime=True)
        session.configure_trigger_software()
        session.channels['0,1'].configure_vertical(5.0, coupling=niscope.VerticalCoupling.DC, enabled=True)
        print('3. Creating arrays')
        wfm0 = np.ndarray(total_samples, dtype=np.float64)
        wfm1 = np.ndarray(total_samples, dtype=np.float64)
        current_pos = 0
        print('4. initating')
        with session.initiate():
            while current_pos < total_samples:
                # We fetch each channel at a time so we don't have to de-interleave afterwards
                # If it takes more than one second to fetch, we are in trouble
                print('5.0 fetching [{}:{}]'.format(current_pos, chunk_size))
                session.channels[0].fetch_into(wfm0[current_pos:chunk_size], relative_to=niscope.FetchRelativeTo.READ_POINTER, offset=0, record_number=0, num_records=1, timeout=datetime.timedelta(seconds=1.0))
                print('5.1 fetching [{}:{}]'.format(current_pos, chunk_size))
                session.channels[1].fetch_into(wfm1[current_pos:chunk_size], relative_to=niscope.FetchRelativeTo.READ_POINTER, offset=0, record_number=0, num_records=1, timeout=datetime.timedelta(seconds=1.0))
                current_pos += chunk_size

        print('6 fetch complete')
    print('7 session closed')


def _main(argsv):
    parser = argparse.ArgumentParser(description='Acquires one record from the given channels.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Resource name of a National Instruments Digitizer')
    parser.add_argument('-c', '--channels', default='0', help='Channel(s) to use')
    parser.add_argument('-l', '--length', default=1000, type=int, help='Measure record length')
    parser.add_argument('-v', '--voltage', default=1.0, type=float, help='Voltage range (V)')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Option string')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.channels, args.option_string, args.length, args.voltage)


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '5164', 'BoardType': 'PXIe', }, }
    example('PXI1Slot2', '0', options, 1000, 1.0)


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:5164; BoardType:PXIe', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()

