import argparse
import atexit
import faulthandler
import niscope
import nitclk
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


def example(resource_name1, resource_name2, options):
    with niscope.Session(resource_name=resource_name1, options=options) as session1, niscope.Session(resource_name=resource_name2, options=options) as session2:
        session_list = [session1, session2]
        for session in session_list:
            session.configure_vertical(range=1.0, coupling=niscope.VerticalCoupling.DC)
            session.configure_horizontal_timing(min_sample_rate=50000000, min_num_pts=1000, ref_position=50.0, num_records=1, enforce_realtime=True)
        session1.trigger_type = niscope.TriggerType.SOFTWARE
        nitclk.configure_for_homogeneous_triggers(session_list)
        nitclk.synchronize(session_list, 200e-9)
        nitclk.initiate(session_list)
        time.sleep(100)
        session1.send_software_trigger_edge(niscope.WhichTrigger.START)
        waveforms = session2.channels[0].fetch(num_samples=1000)
        for i in range(len(waveforms)):
            print(f'Waveform {i} information:')
            print(str(waveforms[i]) + '\n\n')


def _main(argsv):
    parser = argparse.ArgumentParser(description='Synchronizes multiple instruments to one trigger.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n1', '--resource-name1', default='PXI1Slot2', help='Resource name of a NI Digitizer')
    parser.add_argument('-n2', '--resource-name2', default='PXI1Slot3', help='Resource name of a NI Digitizer')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Option string')
    args = parser.parse_args(argsv)
    example(args.resource_name1, args.resource_name2, args.option_string)


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '5164', 'BoardType': 'PXIe', }, }
    example('PXI1Slot2', 'PXI1Slot13', options)


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:5164; BoardType:PXIe', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()

