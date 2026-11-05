#!/usr/bin/python

import argparse
import nidigital
import os
import sys


def example(resource_name, options, source_waveform_type='PARALLEL', data_mapping='BROADCAST', waveform_name='new_waveform', start_label='new_pattern',
            parallel_channel_list='PinGroup1', serial_channel_list='DUTPin1', sample_width=32, bit_order='MSB', waveform_file=None, write_waveform_data=True):

    with nidigital.Session(resource_name=resource_name, options=options) as session:

        dir = os.path.join(os.path.dirname(__file__))
        if waveform_file is None:
            waveform_file = os.path.join(dir, 'SourceWaveform.tdms')

        session.load_pin_map(os.path.join(dir, 'PinMap.pinmap'))

        spec_filename = os.path.join(dir, 'Specifications.specs')
        levels_filename = os.path.join(dir, 'PinLevels.digilevels')
        timing_filename = os.path.join(dir, 'Timing.digitiming')
        session.load_specifications_levels_and_timing(spec_filename, levels_filename, timing_filename)

        session.apply_levels_and_timing(levels_filename, timing_filename)

        session.load_pattern(os.path.join(dir, 'Pattern.digipat'))

        mapping = nidigital.SourceDataMapping[data_mapping]

        # Configure the source waveform type
        if source_waveform_type == 'PARALLEL':
            session.pins[parallel_channel_list].create_source_waveform_parallel(waveform_name, mapping)
        elif source_waveform_type == 'SERIAL':
            session.pins[serial_channel_list].create_source_waveform_serial(waveform_name, mapping, sample_width, nidigital.BitOrder[bit_order])
        elif source_waveform_type == 'TDMS':
            # Waveform configuration and data are read from the TDMS file
            session.create_source_waveform_from_file_tdms(waveform_name, waveform_file, write_waveform_data)

        # Write the source waveform data
        if source_waveform_type != 'TDMS':
            # Placeholder ramp data for illustration; replace with your own waveform samples
            sample_count = 2 ** min(sample_width, 8) if source_waveform_type == 'SERIAL' else 256
            samples = [i % sample_count for i in range(sample_count)]
            if mapping == nidigital.SourceDataMapping.BROADCAST:
                session.write_source_waveform_broadcast(waveform_name, samples)
            else:
                # Site-unique data is a dict of site number to samples; both sites use the same placeholder data here
                session.write_source_waveform_site_unique(waveform_name, {0: samples, 1: samples})

        print('Start bursting pattern')
        session.burst_pattern(start_label=start_label)

        session.selected_function = nidigital.SelectedFunction.DISCONNECT
    print('Done bursting pattern')


def _main(argsv):
    parser = argparse.ArgumentParser(description='Demonstrates how to configure, write, and burst a source waveform using NI-Digital source memory.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2,PXI1Slot3', help='The specified resource name shown in Measurement & Automation Explorer (MAX) for a digital pattern instrument, for example, PXI1Slot3, where PXI1Slot3 is an instrument resource name.')
    parser.add_argument('-s', '--simulate', default='True', choices=['True', 'False'], help='Whether to run on simulated hardware or real hardware')
    parser.add_argument('-w', '--waveform-name', default='new_waveform', help='The name to assign to the waveform. Use the waveform_name with source_start opcode in your pattern.')
    parser.add_argument('-l', '--start-label', default='new_pattern', help='Pattern name or exported pattern label from which to start bursting the pattern.')
    parser.add_argument('-d', '--data-mapping', default='BROADCAST', choices=nidigital.SourceDataMapping.__members__.keys(), type=str.upper, help='Parameter that specifies how to map data on multiple sites.')
    parser.add_argument('-t', '--source-waveform-type', default='PARALLEL', choices=['PARALLEL', 'SERIAL', 'TDMS'], type=str.upper, help='Type of source waveform to configure.')
    parser.add_argument('--parallel-channel-list', default='PinGroup1', help='Pins that source data for a parallel waveform.')
    parser.add_argument('--serial-channel-list', default='DUTPin1', help='Pins that source data for a serial waveform.')
    parser.add_argument('--sample-width', default=32, type=int, help='Width in bits of each serial sample. Valid values are between 1 and 32.')
    parser.add_argument('--bit-order', default='MSB', choices=nidigital.BitOrder.__members__.keys(), type=str.upper, help='Order in which to shift the bits.')
    parser.add_argument('--waveform-file', default=None, help='Absolute file path to the load source waveform file (.tdms). Defaults to SourceWaveform.tdms next to this example.')
    parser.add_argument('--write-waveform-data', default='True', choices=['True', 'False'], help='A Boolean that writes waveform data to source memory if True and the waveform data is in the file.')
    args = parser.parse_args(argsv)

    example(args.resource_name,
            'Simulate=1, DriverSetup=Model:6571' if args.simulate == 'True' else '',
            args.source_waveform_type, args.data_mapping, args.waveform_name, args.start_label,
            args.parallel_channel_list, args.serial_channel_list, args.sample_width, args.bit_order,
            args.waveform_file, args.write_waveform_data == 'True')


def main():
    _main(sys.argv[1:])


def test_main():
    _main([])
    _main(['--source-waveform-type', 'SERIAL', '--data-mapping', 'SITE_UNIQUE'])
    _main(['--source-waveform-type', 'TDMS'])


def test_example():
    resource_name = 'PXI1Slot2,PXI1Slot3'
    options = {'simulate': True, 'driver_setup': {'Model': '6571'}, }
    example(resource_name, options)
    example(resource_name, options, 'SERIAL', 'SITE_UNIQUE')
    example(resource_name, options, 'TDMS')


if __name__ == '__main__':
    main()
