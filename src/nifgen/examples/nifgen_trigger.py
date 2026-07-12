import argparse
import atexit
import faulthandler
import nifgen
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


def example(resource_name1, resource_name2, options, waveform, gen_time):
    with nifgen.Session(resource_name=resource_name1, options=options) as session1, nifgen.Session(resource_name=resource_name2, options=options) as session2:
        session_list = [session1, session2]
        for session in session_list:
            session.output_mode = nifgen.OutputMode.FUNC
            session.configure_standard_waveform(waveform=nifgen.Waveform[waveform], amplitude=1.0, frequency=1000, dc_offset=0.0, start_phase=0.0)
        session1.start_trigger_type = nifgen.StartTriggerType.SOFTWARE_EDGE
        session2.start_trigger_type = nifgen.StartTriggerType.DIGITAL_EDGE
        session2.digital_edge_start_trigger_edge = nifgen.StartTriggerDigitalEdgeEdge.RISING
        session2.digital_edge_start_trigger_source = '/' + resource_name1 + '/0/StartTrigger'
        with session2.initiate():
            with session1.initiate():
                session1.send_software_edge_trigger(nifgen.Trigger.START)
                time.sleep(gen_time)


def _main(argsv):
    supported_waveforms = list(nifgen.Waveform.__members__.keys())[:-1]  # no support for user-defined waveforms in example
    parser = argparse.ArgumentParser(description='Triggers one device on the start trigger of another device.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n1', '--resource-name1', default='PXI1Slot2', help='Resource name of an NI function generator.')
    parser.add_argument('-n2', '--resource-name2', default='PXI1Slot3', help='Resource name of an NI function generator.')
    parser.add_argument('-w', '--waveform', default=supported_waveforms[0], choices=supported_waveforms, type=str.upper, help='Standard waveform')
    parser.add_argument('-t', '--time', default=5.0, type=float, help='Generation time (s)')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Option string')
    args = parser.parse_args(argsv)
    example(args.resource_name1, args.resource_name2, args.option_string, args.waveform, args.time)


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '5433 (2CH)', 'BoardType': 'PXIe', }, }
    example('PXI1Slot2', 'PXI1Slot3', options, 'SINE', 5.0)


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:5433 (2CH);BoardType:PXIe', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()
