#!/usr/bin/python
import argparse
import nifgen
import numpy as np
from scipy import signal
import sys
import time


def generate_sinewave():
    time = np.arange(0, 10, 0.01)                # np.arange(Start, Stop, Step)
    amplitude = np.sin(time)
    sinewave = amplitude.tolist()               # List of Float
    return sinewave


def generate_rampup():
    ramp = np.arange(0, 0.5, 0.01)                # numpy.arange([start,]stop, [step,]dtype=None(
    ramp_up = ramp.tolist()                     # List of Float
    return ramp_up


def generate_ramdown():
    ramp = np.arange(0, 0.5, 0.01)                # numpy.arange([start,]stop, [step,]dtype=None)
    ramp_down = ramp.tolist()                   # List of Float
    ramp_down.reverse()                         # Reverse list to get a ramp down
    return ramp_down


def generate_square():
    time = np.arange(0, 10, 0.01)                # np.arange(Start, Stop, Step)
    square_build = signal.square(time, 0.5)      # signal.square(time,duty_cycle)
    square = square_build.tolist()              # List of Float
    return square


def generate_triangle():
    time = np.linspace(0, 1, 200)               # np.arange(Start, Stop, Step)
    triangle_build = signal.sawtooth(time)      # signal.square(time,width)
    triangle = triangle_build.tolist()          # List of Float
    return triangle


def generate_gaussian_noise():
    random_noise = np.random.normal(0, 0.1, 300)  # random.normal(center, scale, size)
    noise = random_noise.tolist()
    return noise


def example(resource_name, options, shape, channel):
    with nifgen.Session(resource_name=resource_name, options=options, channel_name=channel) as session:
        # CONFIGURATION
        # 1-Set the mode to Script
        session.output_mode = nifgen.OutputMode.SCRIPT

        # 2-Configure Trigger:
        # SOFTWARE TRIGGER: used in the script
        session.script_triggers[0].script_trigger_type = nifgen.ScriptTriggerType.SOFTWARE_EDGE  # TRIG_NONE / DIGITAL_EDGE / DIGITAL_LEVEL / SOFTWARE_EDGE
        session.script_triggers[0].digital_edge_script_trigger_edge = nifgen.ScriptTriggerDigitalEdgeEdge.RISING  # RISING / FAILING
        # PFI TRIGGER: not used right now
        # session.script_triggers[1].script_trigger_type = nifgen.script_triggers[0].ScriptTriggerType.DIGITAL_EDGE
        # session.script_triggers[1].digital_edge_script_trigger_source = 'PFI0'
        # session.script_triggers[1].digital_edge_script_trigger_edge = session.script_triggers[0].ScriptTriggerDigitalEdgeEdge.RISING

        # 3-Generate Signal
        sine = generate_sinewave()
        ramp_up = generate_rampup()
        ramp_down = generate_ramdown()
        square = generate_square()
        triangle = generate_triangle()
        noise = generate_gaussian_noise()

        # 4-Writes data to the waveform in onboard memory.
        session.channels[channel].write_waveform('sine', sine)        # (waveform_name, data)
        session.channels[channel].write_waveform('rampup', ramp_up)
        session.channels[channel].write_waveform('rampdown', ramp_down)
        session.channels[channel].write_waveform('square', square)
        session.channels[channel].write_waveform('triangle', triangle)
        session.channels[channel].write_waveform('noise', noise)

        # 5-Write Script
        script_sine = 'script Script\nrepeat until scriptTrigger0\nGenerate sine \nend repeat\nend script'
        script_ramp_up = 'script Script\nrepeat until scriptTrigger0\nGenerate rampup\nend repeat\nend script'
        script_ramp_down = 'script Script\nrepeat until scriptTrigger0\nGenerate rampdown\nend repeat\nend script'
        script_square = 'script Script\nrepeat until scriptTrigger0\nGenerate square\nend repeat\nend script'
        script_triangle = 'script Script\nrepeat until scriptTrigger0\nGenerate triangle\nend repeat\nend script'
        script_noise = 'script Script\nrepeat until scriptTrigger0\nGenerate noise \nend repeat\nend script'
        script_multi = 'script Script\nrepeat until scriptTrigger0\nGenerate triangle\nend repeat\nrepeat until scriptTrigger0\nGenerate sine\nend repeat\nend script'

        # 6-Script to generate
        ''' SINE / SQUARE / TRIANGLE / RAMP_UP / RAMP_DOWN / NOISE / MULTI '''
        if shape is 'SINE':
            session.channels[0].write_script(script_sine)
        elif shape is 'RAMP_UP':
            session.channels[0].write_script(script_ramp_up)
        elif shape is 'RAMP_DOWN':
            session.channels[0].write_script(script_ramp_down)
        elif shape is 'SQUARE':
            session.channels[0].write_script(script_square)
        elif shape is 'TRIANGLE':
            session.channels[0].write_script(script_triangle)
        elif shape is 'NOISE':
            session.channels[0].write_script(script_noise)
        elif shape is 'MULTI':
            session.channels[0].write_script(script_multi)

        session.channels[channel].write_script(script)
        session.script_to_generate = 'Script'

        # LAUNCH
        with session.initiate():
            time.sleep(10)
            if shape is 'MULTI':
                for x in range(2):
                    time.sleep(2)
                    session.script_triggers[0].send_software_edge_trigger()
            else:
                session.script_triggers[0].send_software_edge_trigger()


def _main(argsv):
    parser = argparse.ArgumentParser(description='Continuously generates an arbitrary waveform.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='AWG2', help='Resource name of a National Instruments Arbitrary Waveform Generator')
    parser.add_argument('-s', '--shape', default='NOISE', help='Shape of the signal to generate')
    parser.add_argument('-c', '--channel', default='0', help='Channel to use when generating')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Option string')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.option_string, args.shape.upper(), args.channel)


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '5433 (2CH)', 'BoardType': 'PXIe', }, }
    example('PXI1Slot2', options, 'SINE', '0')


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:5433 (2CH);BoardType:PXIe', '--channel', '0', ]
    _main(cmd_line)


def main():
    _main(sys.argv[1:])


if __name__ == '__main__':
    main()




