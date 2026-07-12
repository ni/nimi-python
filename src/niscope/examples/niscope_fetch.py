#!/usr/bin/python

import argparse
import atexit
import faulthandler
import niscope
import pprint
import sys
import threading
import traceback

# Dump Python tracebacks automatically on fatal signals
faulthandler.enable(all_threads=True)


@atexit.register
def dump_thread_info():
    print("\n" + "=" * 100)
    print("THREAD DUMP AT EXIT")
    print("=" * 100)

    threads = threading.enumerate()
    frames = sys._current_frames()

    print(f"Total threads: {len(threads)}")

    for idx, t in enumerate(threads, 1):
        print("\n" + "-" * 100)
        print(f"Thread #{idx}")
        print(f"Name      : {t.name}")
        print(f"Ident     : {t.ident}")
        print(f"Native ID : {getattr(t, 'native_id', 'N/A')}")
        print(f"Alive     : {t.is_alive()}")
        print(f"Daemon    : {t.daemon}")
        print(f"Type      : {type(t).__name__}")

        frame = frames.get(t.ident)
        if frame:
            print("\nStack Trace:")
            traceback.print_stack(frame, file=sys.stdout)

    print("\n" + "=" * 100)
    print("END THREAD DUMP")
    print("=" * 100)


pp = pprint.PrettyPrinter(indent=4, width=80)


def example(resource_name, channels, options, length, voltage):
    with niscope.Session(resource_name=resource_name, options=options) as session:
        session.configure_vertical(range=voltage, coupling=niscope.VerticalCoupling.AC)
        session.configure_horizontal_timing(min_sample_rate=50000000, min_num_pts=length, ref_position=50.0, num_records=1, enforce_realtime=True)
        with session.initiate():
            waveforms = session.channels[channels].fetch(num_samples=length)
        for i in range(len(waveforms)):
            print(f'Waveform {i} information:')
            print(str(waveforms[i]) + '\n\n')


def _main(argsv):
    parser = argparse.ArgumentParser(description='Acquires one record from the given channels.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Resource name of an NI digitizer.')
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

