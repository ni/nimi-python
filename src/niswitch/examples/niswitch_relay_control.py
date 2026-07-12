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


def example(resource_name, topology, simulate, relay, action):
    # if we are simulating resource name must be blank
    resource_name = '' if simulate else resource_name

    with niswitch.Session(resource_name=resource_name, topology=topology, simulate=simulate) as session:
        session.relay_control(relay_name=relay, relay_action=niswitch.RelayAction[action])
        print('Relay ', relay, ' has had the action ', action, ' performed.')


def _main(argsv):
    parser = argparse.ArgumentParser(description='Performs relay control with NI-SWITCH relays.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Resource name of an NI switch.')
    parser.add_argument('-r', '--relay', default='k0', help='Relay Name.')
    parser.add_argument('-a', '--action', default='OPEN', choices=niswitch.RelayAction.__members__.keys(), type=str.upper, help='Relay Action.')
    parser.add_argument('-t', '--topology', default='Configured Topology', help='Topology.')
    parser.add_argument('-s', '--simulate', default=False, action='store_true', help='Simulate device.')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.topology, args.simulate, args.relay, args.action)


def test_example():
    example('', '2737/2-Wire 4x64 Matrix', True, 'kr0c0', 'OPEN')


def test_main():
    cmd_line = ['--topology', '2737/2-Wire 4x64 Matrix', '--simulate', '--relay', 'kr0c0']
    _main(cmd_line)


def main():
    _main(sys.argv[1:])


if __name__ == '__main__':
    main()


