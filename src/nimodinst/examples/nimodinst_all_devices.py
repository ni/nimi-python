#!/usr/bin/python

import atexit
import faulthandler
import nimodinst
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


def example():
    with nimodinst.Session('') as session:
        if len(session) > 0:
            print("%d items" % len(session))
            print("{: >20} {: >15} {: >10}".format('Name', 'Model', 'S/N'))
        for d in session:
            print(f"{d.device_name: >20} {d.device_model: >15} {d.serial_number: >10}")


def _main():
    example()


def test_example():
    example()


if __name__ == '__main__':
    _main()


