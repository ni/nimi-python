#!/usr/bin/python

import argparse
import niscope
import sys

TRIGGER_TYPES = ('EDGE', 'IMMEDIATE')


def example(resource_name, options, channel, vertical_range, min_sample_rate, min_record_length, num_records, trigger_type):
    print(f'Starting acquisition on resource {resource_name}, for {num_records} records.')
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

    print('Acquired {} records.'.format(len(waveforms)))
    return waveforms


def _main(argsv):
    parser = argparse.ArgumentParser(description='Acquires multiple triggered records from a channel.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Specifies the resource name of the device to initialize.')
    parser.add_argument('-c', '--channel', default='0', help='Channel to use')
    parser.add_argument('-T', '--trigger-type', default='EDGE', choices=TRIGGER_TYPES, type=str.upper, help='EDGE configures the digitizer for edge triggering (channel 0, 0 V, DC coupling, rising slope). IMMEDIATE triggers as soon as the pretrigger samples are acquired.')
    parser.add_argument('-v', '--vertical-range', default=5.0, type=float, help='Specifies the absolute value of the input range for a channel in volts.')
    parser.add_argument('-r', '--min-sample-rate', default=1e7, type=float, help='The sampling rate for the acquisition.')
    parser.add_argument('-N', '--num-records', default=2, type=int, help='The number of records to acquire')
    parser.add_argument('-l', '--min-record-length', default=256, type=int, help='The minimum number of points you need in the record for each channel.')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Specifies the initial value of certain properties for the session.')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.option_string, args.channel, args.vertical_range, args.min_sample_rate, args.min_record_length, args.num_records,
            args.trigger_type)


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '5164', 'BoardType': 'PXIe', }, }
    waveforms = example('PXI1Slot2', options, '0', 5.0, 1e7, 256, 3, 'EDGE')
    assert len(waveforms) == 3


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:5164; BoardType:PXIe', '--num-records', '2', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()
