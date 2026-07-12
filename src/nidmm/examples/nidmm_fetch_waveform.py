#!/usr/bin/python

import argparse
import atexit
import faulthandler
import nidmm
import sys
import threading
import time
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


def example(resource_name, options, function, range, points, rate):
    with nidmm.Session(resource_name=resource_name, options=options) as session:
        session.configure_waveform_acquisition(measurement_function=nidmm.Function[function], range=range, rate=rate, waveform_points=points)
        with session.initiate():
            while True:
                time.sleep(0.1)
                backlog, acquisition_state = session.read_status()
                if acquisition_state == nidmm.AcquisitionStatus.FINISHED_WITH_NO_BACKLOG:
                    break
                measurements = session.fetch_waveform(array_size=backlog)
                print(measurements)


def _main(argsv):
    parser = argparse.ArgumentParser(description='Performs a waveform acquisition using the NI-DMM API.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Resource name of an NI digital multimeter.')
    parser.add_argument('-f', '--function', default='WAVEFORM_VOLTAGE', choices=nidmm.Function.__members__.keys(), type=str.upper, help='Measurement function.')
    parser.add_argument('-r', '--range', default=10, type=float, help='Measurement range.')
    parser.add_argument('-p', '--points', default=10, type=int, help='Specifies the number of points to acquire before the waveform acquisition completes.')
    parser.add_argument('-s', '--rate', default=1000, type=int, help='Specifies the rate of the acquisition in samples per second.')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Option string')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.option_string, args.function, args.range, args.points, args.rate)


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '4082', 'BoardType': 'PXIe', }, }
    example('PXI1Slot2', options, 'WAVEFORM_VOLTAGE', 10, 10, 1000)


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:4082; BoardType:PXIe', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()


