#!/usr/bin/python

import argparse
import nifgen
import numpy as np
from scipy import signal
import sys
import time

number_of_points = 256


def calculate_sinewave():
    time = np.linspace(start=0, stop=10, num=number_of_points)    # np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
    amplitude = np.sin(time)
    sinewave = amplitude.tolist()                               # List of Float
    return sinewave


def calculate_rampup():
    ramp = np.linspace(start=0, stop=0.5, num=number_of_points)   # np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
    ramp_up = ramp.tolist()                                     # List of Float
    return ramp_up


def calculate_rampdown():
    ramp = np.linspace(start=0, stop=0.5, num=number_of_points)   # np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
    ramp_down = ramp.tolist()                                   # List of Float
    ramp_down.reverse()                                         # Reverse list to get a ramp down
    return ramp_down


def calculate_square():
    time = np.linspace(start=0, stop=10, num=number_of_points)    # np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
    square_build = signal.square(t=time, duty=0.5)              # signal.square(t, duty=0.5)
    square = square_build.tolist()                              # List of Float
    return square


def calculate_triangle():
    time = np.linspace(start=0, stop=1, num=number_of_points)     # np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
    triangle_build = signal.sawtooth(t=time)                    # signal.sawtooth(t, width=1)
    triangle = triangle_build.tolist()                          # List of Float
    return triangle


def calculate_gaussian_noise():
    random_noise = np.random.normal(loc=0, scale=0.1, size=number_of_points)  # random.normal(loc=0.0, scale=1.0, size=None)
    noise = random_noise.tolist()                                           # List of Float
    return noise


SCRIPT_ALL = '''
script scriptmulti
  repeat until scriptTrigger0
    generate rampup
    generate sine
    generate rampdown
  end repeat
  repeat until scriptTrigger0
    generate rampdown
    generate square
    generate rampup
  end repeat
  repeat until scriptTrigger0
    generate rampup
    generate rampdown
  end repeat
  repeat until scriptTrigger0
    generate sine
  end repeat
  repeat until scriptTrigger0
    generate triangle
  end repeat
  repeat until scriptTrigger0
    generate rampdown
    generate noise
    generate rampup
  end repeat
end script

script scriptsine
  repeat until scriptTrigger0
    generate sine
  end repeat
end script

script scriptrampup
  repeat until scriptTrigger0
    generate rampup
  end repeat
end script

script scriptrampdown
  repeat until scriptTrigger0
    generate rampdown
  end repeat
end script

script scriptsquare
  repeat until scriptTrigger0
    generate square
  end repeat
end script

script scripttriangle
  repeat until scriptTrigger0
    generate triangle
  end repeat
end script

script scriptnoise
  repeat until scriptTrigger0
    generate noise
  end repeat
end script
'''


def example(resource_name, options, shape, channel):
    with nifgen.Session(resource_name=resource_name, options=options, channel_name=channel) as session:
        # CONFIGURATION
        # 1 - Set the mode to Script
        session.output_mode = nifgen.OutputMode.SCRIPT

        # 2 - Configure Trigger:
        # SOFTWARE TRIGGER: used in the script
        session.script_triggers[0].script_trigger_type = nifgen.ScriptTriggerType.SOFTWARE_EDGE  # TRIG_NONE / DIGITAL_EDGE / DIGITAL_LEVEL / SOFTWARE_EDGE
        session.script_triggers[0].digital_edge_script_trigger_edge = nifgen.ScriptTriggerDigitalEdgeEdge.RISING  # RISING / FAILING

        # 3 - Calculate and write different waveform data to the device's onboard memory
        session.channels[channel].write_waveform('sine', calculate_sinewave())        # (waveform_name, data)
        session.channels[channel].write_waveform('rampup', calculate_rampup())
        session.channels[channel].write_waveform('rampdown', calculate_rampdown())
        session.channels[channel].write_waveform('square', calculate_square())
        session.channels[channel].write_waveform('triangle', calculate_triangle())
        session.channels[channel].write_waveform('noise', calculate_gaussian_noise())

        # 4 - Script to generate
        # supported shapes: SINE / SQUARE / TRIANGLE / RAMPUP / RAMPDOWN / NOISE / MULTI
        script_name = 'script{}'.format(shape.lower())
        num_triggers = 6 if shape.upper() == 'MULTI' else 1  # Only multi needs two triggers, all others need one

        session.channels[channel].write_script(SCRIPT_ALL)
        session.script_to_generate = script_name

        # LAUNCH
        with session.initiate():
            for x in range(num_triggers):
                time.sleep(10)
                session.script_triggers[0].send_software_edge_trigger()


def _main(argsv):
    parser = argparse.ArgumentParser(description='Generate different shape waveforms.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Resource name of a National Instruments Arbitrary Waveform Generator')
    parser.add_argument('-s', '--shape', default='SINE', help='Shape of the signal to generate')
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




