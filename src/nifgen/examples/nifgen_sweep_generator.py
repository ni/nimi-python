#!/usr/bin/python

import argparse
import nifgen
import sys
import time


def _create_frequency_array(start_frequency, stop_frequency, frequency_steps):
    frequency_step = (stop_frequency - start_frequency) / frequency_steps
    return [start_frequency + index * frequency_step for index in range(frequency_steps)]


def example(resource_name, options, waveform, start_frequency, amplitude,
            stop_frequency, frequency_steps, duration_per_step, dc_offset,
            trigger_type, trigger_mode, trigger_source, gen_time):
    frequency_array = _create_frequency_array(start_frequency, stop_frequency, frequency_steps)
    duration_array = [duration_per_step] * frequency_steps

    with nifgen.Session(resource_name=resource_name, channel_name='0', options=options) as session:
        session.output_mode = nifgen.OutputMode.FREQ_LIST
        session.clear_freq_list(-1)
        frequency_list_handle = session.create_freq_list(nifgen.Waveform[waveform], frequency_array, duration_array)
        session.configure_freq_list(frequency_list_handle, amplitude, dc_offset=dc_offset)
        session.trigger_mode = nifgen.TriggerMode[trigger_mode]
        session.start_trigger_type = nifgen.StartTriggerType[trigger_type]
        if trigger_type == 'DIGITAL_EDGE':
            session.digital_edge_start_trigger_source = trigger_source
            session.digital_edge_start_trigger_edge = nifgen.StartTriggerDigitalEdgeEdge.RISING
        session.output_enabled = True

        with session.initiate():
            print('Generating {} sweep: {}-{} Hz.'.format(waveform, start_frequency, stop_frequency))
            if trigger_type == 'SOFTWARE_EDGE':
                session.send_software_edge_trigger(nifgen.Trigger.START, 'None')
            time.sleep(gen_time)


def _main(argsv):
    supported_waveforms = list(nifgen.Waveform.__members__.keys())[:-1]  # no support for user-defined waveforms in example
    supported_trigger_types = ['TRIG_NONE', 'SOFTWARE_EDGE', 'DIGITAL_EDGE']
    supported_trigger_modes = list(nifgen.TriggerMode.__members__.keys())
    parser = argparse.ArgumentParser(description='Generates a frequency sweep.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Specifies the NI-FGEN resource name to initialize.')
    parser.add_argument('-w', '--waveform', default='SINE', choices=supported_waveforms, type=str.upper, help='Specifies the standard waveform shape to generate.')
    parser.add_argument('-sf', '--start-frequency', default=1000.0, type=float, help='Specifies the starting sweep frequency in hertz.')
    parser.add_argument('-a', '--amplitude', default=2.0, type=float, help='Specifies the peak-to-peak waveform amplitude in volts.')
    parser.add_argument('-ef', '--stop-frequency', default=1000000.0, type=float, help='Specifies the upper frequency limit in hertz.')
    parser.add_argument('-s', '--frequency-steps', default=512, type=int, help='Specifies the number of frequency steps in the sweep.')
    parser.add_argument('-d', '--duration-per-step', default=0.01, type=float, help='Specifies each frequency duration in seconds.')
    parser.add_argument('-o', '--dc-offset', '--offset', dest='dc_offset', default=0.0, type=float, help='Specifies the waveform DC offset in volts.')
    parser.add_argument('-tt', '--trigger-type', default='TRIG_NONE', choices=supported_trigger_types, type=str.upper, help='Specifies the start trigger: none, software edge, or digital edge.')
    parser.add_argument('-tm', '--trigger-mode', default='CONTINUOUS', choices=supported_trigger_modes, type=str.upper, help='Specifies how generation advances through the frequency list.')
    parser.add_argument('-ts', '--trigger-source', default='PFI0', help='Specifies the terminal for a digital-edge Start trigger.')
    parser.add_argument('-t', '--time', default=5.0, type=float, help='Specifies how long to generate the sweep before stopping, in seconds.')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Specifies NI-FGEN initialization options, such as simulation and driver setup.')
    args = parser.parse_args(argsv)
    example(
        resource_name=args.resource_name, options=args.option_string, waveform=args.waveform,
        start_frequency=args.start_frequency, amplitude=args.amplitude, stop_frequency=args.stop_frequency,
        frequency_steps=args.frequency_steps, duration_per_step=args.duration_per_step, dc_offset=args.dc_offset,
        trigger_type=args.trigger_type, trigger_mode=args.trigger_mode,
        trigger_source=args.trigger_source, gen_time=args.time)


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '5433 (2CH)', 'BoardType': 'PXIe', }, }
    example(
        resource_name='PXI1Slot2', options=options, waveform='SINE', start_frequency=1000,
        amplitude=2.0, stop_frequency=1000000, frequency_steps=512,
        duration_per_step=0.01, dc_offset=0.0, trigger_type='TRIG_NONE',
        trigger_mode='CONTINUOUS', trigger_source='PFI0', gen_time=0.1)


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:5433 (2CH);BoardType:PXIe', '--time', '0.1', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()
