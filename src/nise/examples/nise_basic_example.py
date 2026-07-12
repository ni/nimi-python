#!/usr/bin/python
import argparse
import atexit
import faulthandler
import nise
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


def example(virtual_device_name, connection):
    with nise.Session(virtual_device_name=virtual_device_name) as session:
        session.connect(connection)
        print(connection, ' is now connected.')


def _main(argsv):
    parser = argparse.ArgumentParser(description='Connects the specified connection specification', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--virtual-device', default='SwitchExecutiveExample', help='NI Switch Executive Virtual Device name')
    parser.add_argument('-c', '--connection', default='DIOToUUT', help='Connection Specification')
    args = parser.parse_args(argsv)
    example(args.virtual_device, args.connection)


def main():
    _main(sys.argv[1:])


def test_example():
    example('SwitchExecutiveExample', 'DIOToUUT')


def test_main():
    cmd_line = []
    _main(cmd_line)


if __name__ == '__main__':
    main()


