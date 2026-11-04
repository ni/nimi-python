#!/usr/bin/python

import argparse
import nidigital
import os
import sys


CAPTURE_WAVEFORM_TYPES = ('Serial', 'Parallel', 'From File: Digicapture')
WAVEFORM_NAME = 'new_waveform'


def example(resource_name, options, samples_to_read, pin_list, capture_waveform_type, sample_width, bit_order, waveform_file_path):

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

        try:
            if capture_waveform_type == 'Serial':
                session.pins[pin_list].create_capture_waveform_serial(waveform_name=WAVEFORM_NAME, sample_width=sample_width, bit_order=bit_order)
            elif capture_waveform_type == 'Parallel':
                session.pins[pin_list].create_capture_waveform_parallel(waveform_name=WAVEFORM_NAME)
            elif capture_waveform_type == 'From File: Digicapture':
                capture_file_path = os.path.abspath(os.path.join(directory, waveform_file_path))
                session.create_capture_waveform_from_file_digicapture(waveform_name=WAVEFORM_NAME, waveform_file_path=capture_file_path)
            else:
                raise ValueError('Unsupported capture waveform type: {}'.format(capture_waveform_type))

            print('Start bursting pattern')
            session.burst_pattern(start_label='new_pattern')

            waveforms = session.fetch_capture_waveform(waveform_name=WAVEFORM_NAME, samples_to_read=samples_to_read)
            captured_waveforms = {site: list(data) for site, data in waveforms.items()}
            print('Captured data:')
            for site, samples in sorted(captured_waveforms.items()):
                print('Site {} ({} samples): {}'.format(site, len(samples), samples))
        finally:
            session.pins[pin_list].selected_function = nidigital.SelectedFunction.DISCONNECT

    print('Done capturing waveform')


def _main(argsv):
    parser = argparse.ArgumentParser(description='Demonstrates how to configure a capture waveform and capture data on the digital pattern instrument.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2,PXI1Slot3', help='The specified resource name shown in Measurement & Automation Explorer (MAX) for a digital pattern instrument, for example, PXI1Slot3, where PXI1Slot3 is an instrument resource name.')
    parser.add_argument('-s', '--simulate', default='True', choices=['True', 'False'], help='Whether to run on simulated hardware or real hardware')
    parser.add_argument('-r', '--samples-to-read', default=4, type=int, help='Number of samples to fetch.')
    parser.add_argument('-p', '--pin-list', default='DUTPin1', help='List of pins to capture.')
    parser.add_argument('-t', '--capture-waveform-type', default='Serial', type=str.title, choices=CAPTURE_WAVEFORM_TYPES, help='Selects the capture waveform configuration to use.')
    parser.add_argument('-sw', '--sample-width', default=32, type=int, help='Width in bits of each serial sample. Valid values are between 1 and 32.')
    parser.add_argument('-bo', '--bit-order', default='MSB', type=str.upper, choices=nidigital.BitOrder.__members__, help='Order in which to shift the bits.')
    parser.add_argument('-wf', '--waveform-file', default='CaptureWaveform.digicapture', help='Absolute file path to the capture waveform file (.digicapture) you want to load.')
    args = parser.parse_args(argsv)

    example(args.resource_name,
            'Simulate=1, DriverSetup=Model:6570' if args.simulate == 'True' else '',
            args.samples_to_read, args.pin_list, args.capture_waveform_type,
            args.sample_width, nidigital.BitOrder[args.bit_order], args.waveform_file)


def main():
    _main(sys.argv[1:])


def test_main():
    _main([])
    _main(['--capture-waveform-type', 'Parallel'])
    _main(['--capture-waveform-type', 'From File: Digicapture'])
    _main(['--sample-width', '8', '--bit-order', 'LSB'])


def test_example():
    resource_name = 'PXI1Slot2,PXI1Slot3'
    options = {'simulate': True, 'driver_setup': {'Model': '6570'}}
    samples_to_read = 4
    pin_list = 'DUTPin1'
    sample_width = 32
    bit_order = nidigital.BitOrder.MSB
    waveform_file_path = 'CaptureWaveform.digicapture'

    example(resource_name, options, samples_to_read, pin_list, 'Serial', sample_width, bit_order, waveform_file_path)
    example(resource_name, options, samples_to_read, pin_list, 'Parallel', sample_width, bit_order, waveform_file_path)
    example(resource_name, options, samples_to_read, pin_list, 'From File: Digicapture', sample_width, bit_order, waveform_file_path)
    example(resource_name, options, samples_to_read, pin_list, 'Serial', 8, nidigital.BitOrder.LSB, waveform_file_path)


if __name__ == '__main__':
    main()
