#!/usr/bin/python

import argparse
import nidigital
import os
import sys


def example(resource_name, options, trigger_type, trigger_source, trigger_edge, send_software_trigger):

    with nidigital.Session(resource_name=resource_name, reset_device=True, options=options) as session:

        directory = os.path.dirname(os.path.abspath(__file__))

        pin_map_filename = os.path.join(directory, 'PinMap.pinmap')
        session.load_pin_map(pin_map_filename)

        spec_filename = os.path.join(directory, 'Specifications.specs')
        levels_filename = os.path.join(directory, 'PinLevels.digilevels')
        timing_filename = os.path.join(directory, 'Timing.digitiming')
        session.load_specifications_levels_and_timing(spec_filename, levels_filename, timing_filename)

        session.apply_levels_and_timing(levels_filename, timing_filename)

        pattern_filename = os.path.join(directory, 'Pattern.digipat')
        session.load_pattern(pattern_filename)

        trigger_identifier = 'conditionalJumpTrigger0'
        conditional_trigger = session.conditional_jump_triggers[trigger_identifier]
        conditional_trigger.conditional_jump_trigger_type = trigger_type
        if trigger_type == nidigital.TriggerType.DIGITAL_EDGE:
            conditional_trigger.digital_edge_conditional_jump_trigger_source = trigger_source
            conditional_trigger.digital_edge_conditional_jump_trigger_edge = trigger_edge

        try:
            print('Start bursting pattern')
            if trigger_type == nidigital.TriggerType.SOFTWARE:
                # Start the burst without blocking so the software conditional trigger can be sent
                session.burst_pattern(start_label='new_pattern', wait_until_done=False)
                if not send_software_trigger:
                    print('Pattern burst stopped without sending a software trigger')
                    return

                session.send_software_edge_trigger(nidigital.SoftwareTrigger.CONDITIONAL_JUMP, trigger_identifier)
                session.wait_until_done()
            else:
                session.burst_pattern(start_label='new_pattern')
        finally:
            try:
                session.abort()
            finally:
                session.selected_function = nidigital.SelectedFunction.DISCONNECT
    print('Done bursting pattern')


def _main(argsv):
    parser = argparse.ArgumentParser(description='Demonstrates how to burst a pattern on the digital pattern instrument using a conditional trigger.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2,PXI1Slot3', help='The specified resource name of a digital pattern instrument, for example, PXI1Slot3, where PXI1Slot3 is an instrument resource name.')
    parser.add_argument('-s', '--simulate', default='True', choices=['True', 'False'], help='Whether to run on simulated hardware or real hardware')
    parser.add_argument('-tt', '--trigger-type', default='SOFTWARE', type=str.upper, choices=nidigital.TriggerType.__members__, help='Disables the conditional jump trigger or configures it for either hardware triggering or software triggering.')
    parser.add_argument('-ts', '--trigger-source', default='/PXI1Slot2/PXI_Trig0', help='Configures the digital trigger source terminal for a conditional jump trigger instance.')
    parser.add_argument('-te', '--trigger-edge', default='RISING', type=str.upper, choices=nidigital.DigitalEdge.__members__, help='Configures the active edge of the incoming trigger signal for the conditional jump trigger instance.')
    parser.add_argument('--send-software-trigger', default='True', choices=['True', 'False'], help='Whether to send the software conditional trigger or stop the burst without sending it; applies only to SOFTWARE mode.')
    args = parser.parse_args(argsv)

    example(args.resource_name,
            'Simulate=1, DriverSetup=Model:6570' if args.simulate == 'True' else '',
            nidigital.TriggerType[args.trigger_type], args.trigger_source,
            nidigital.DigitalEdge[args.trigger_edge], args.send_software_trigger == 'True')


def main():
    _main(sys.argv[1:])


def test_main():
    _main([])
    _main(['--trigger-type', 'NONE'])
    _main(['--trigger-type', 'DIGITAL_EDGE'])
    _main(['--trigger-type', 'DIGITAL_EDGE', '--trigger-edge', 'FALLING'])
    _main(['--send-software-trigger', 'False'])


def test_example():
    resource_name = 'PXI1Slot2,PXI1Slot3'
    options = {'simulate': True, 'driver_setup': {'Model': '6570'}}
    trigger_source = '/PXI1Slot2/PXI_Trig0'
    trigger_edge = nidigital.DigitalEdge.RISING

    trigger_type = nidigital.TriggerType.SOFTWARE
    example(resource_name, options, trigger_type, trigger_source, trigger_edge, send_software_trigger=True)
    example(resource_name, options, trigger_type, trigger_source, trigger_edge, send_software_trigger=False)

    trigger_type = nidigital.TriggerType.NONE
    example(resource_name, options, trigger_type, trigger_source, trigger_edge, send_software_trigger=True)

    trigger_type = nidigital.TriggerType.DIGITAL_EDGE
    example(resource_name, options, trigger_type, trigger_source, trigger_edge, send_software_trigger=True)

    trigger_edge = nidigital.DigitalEdge.FALLING
    example(resource_name, options, trigger_type, trigger_source, trigger_edge, send_software_trigger=True)


if __name__ == '__main__':
    main()
