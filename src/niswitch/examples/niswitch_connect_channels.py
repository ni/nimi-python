#!/usr/bin/python

import argparse
import atexit
import faulthandler
import niswitch
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


def example(resource_name, channel1, channel2, topology, simulate):
    # if we are simulating resource name must be blank
    resource_name = '' if simulate else resource_name

    with niswitch.Session(resource_name=resource_name, topology=topology, simulate=simulate) as session:
        session.connect(channel1=channel1, channel2=channel2)
        print('Channel ', channel1, ' and ', channel2, ' are now connected.')
        session.disconnect(channel1=channel1, channel2=channel2)
        print('Channel ', channel1, ' and ', channel2, ' are now disconnected.')


def _main(argsv):
    parser = argparse.ArgumentParser(description='Performs a connection with NI-SWITCH Channels.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Resource name of an NI switch.')
    parser.add_argument('-ch1', '--channel1', default='c0', help='Channel One.')
    parser.add_argument('-ch2', '--channel2', default='r0', help='Channel Two.')
    parser.add_argument('-t', '--topology', default='Configured Topology', help='Topology.')
    parser.add_argument('-s', '--simulate', default=False, action='store_true', help='Simulate device.')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.channel1, args.channel2, args.topology, args.simulate)


def test_example():
    example('', 'c0', 'r0', '2737/2-Wire 4x64 Matrix', True)


def test_main():
    cmd_line = ['--topology', '2737/2-Wire 4x64 Matrix', '--simulate']
    _main(cmd_line)


def main():
    _main(sys.argv[1:])


if __name__ == '__main__':
    main()


