#!/usr/bin/python

import argparse
import hightime
import niscope
import numpy as np
import pprint
import sys


pp = pprint.PrettyPrinter(indent=4, width=80)


# We use fetch_into which allows us to allocate a single buffer per channel and "fetch into" it a section at a time without having to
# reconstruct the waveform once we are done
def example(resource_name, options, total_acquisition_time_in_seconds, voltage, sample_rate_in_hz, samples_per_fetch):
    total_samples = int(total_acquisition_time_in_seconds * sample_rate_in_hz)
    # 1. Opening session
    with niscope.Session(resource_name=resource_name, options=options) as session:
        # We will acquire on all channels of the device
        channel_list = [c for c in range(session.channel_count)]  # Need an actual list and not a range

        # 2. Creating numpy arrays
        waveforms = [np.ndarray(total_samples, dtype=np.float64) for c in channel_list]

        # 3. Configuring
        session.configure_horizontal_timing(min_sample_rate=sample_rate_in_hz, min_num_pts=1, ref_position=0.0, num_records=1, enforce_realtime=True)
        session.channels[channel_list].configure_vertical(voltage, coupling=niscope.VerticalCoupling.DC, enabled=True)
        # Configure software trigger, but never send the trigger.
        # This starts an infinite acquisition, until you call session.abort() or session.close()
        session.configure_trigger_software()
        current_pos = 0
        # 4. initiating
        with session.initiate():
            while current_pos < total_samples:
                # We fetch each channel at a time so we don't have to de-interleave afterwards
                # We do not keep the wfm_info returned from fetch_into
                for channel, waveform in zip(channel_list, waveforms):
                    # 5. fetching - we return the slice of the waveform array that we want to "fetch into"
                    session.channels[channel].fetch_into(waveform[current_pos:current_pos + samples_per_fetch], relative_to=niscope.FetchRelativeTo.READ_POINTER,
                                                         offset=0, record_number=0, num_records=1, timeout=hightime.timedelta(seconds=5.0))
                current_pos += samples_per_fetch


def _main(argsv):
    parser = argparse.ArgumentParser(description='Fetch more samples than will fit in memory.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Resource name of an NI Digitizer module.')
    parser.add_argument('-t', '--time', default=10, type=int, help='Time to sample (s)')
    parser.add_argument('-v', '--voltage', default=1.0, type=float, help='Voltage range (V)')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Option string')
    parser.add_argument('-r', '--sample-rate', default=1000.0, type=float, help='Sample Rate (Hz)')
    parser.add_argument('-s', '--samples-per-fetch', default=100, type=int, help='Samples per fetch')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.option_string, args.time, args.voltage, args.sample_rate, args.samples_per_fetch)


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '5164', 'BoardType': 'PXIe', }, }
    example('PXI1Slot2', options, 10, 1.0, 1000.0, 100)


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:5164; BoardType:PXIe', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()

