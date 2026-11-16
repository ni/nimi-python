#!/usr/bin/python

import argparse
import nidigital
import os
import random
import shutil
import sys
import tempfile
from xml.etree import ElementTree

SPECS_NAMESPACE = 'http://www.ni.com/schemas/Semiconductor/Specifications.xsd'
FORMULA_NAMESPACE = 'http://www.ni.com/schemas/Semiconductor/Formula.xsd'
NAMESPACES = {'s': SPECS_NAMESPACE, 'f': FORMULA_NAMESPACE}
ElementTree.register_namespace('', SPECS_NAMESPACE)
ElementTree.register_namespace('f', FORMULA_NAMESPACE)

SOURCE_WAVEFORM_NAME = 'demo_src_wfm'
CAPTURE_WAVEFORM_NAME = 'demo_waveform'
SOURCE_PIN = 'SDATA'
SAMPLE_WIDTH = 32
NUMBER_OF_SAMPLES = 32


def _sweep_values(start, stop, steps):
    if steps == 1:
        return [start]
    return [start + i * (stop - start) / (steps - 1) for i in range(steps)]


def _update_specification_values(specs_file_path, new_values):
    # new_values maps '<Section>.<Symbol>' to the new definition for that specification
    specs_tree = ElementTree.parse(specs_file_path)
    for spec_name, value in new_values.items():
        section_name, formula_symbol = spec_name.split('.')
        definition_element = specs_tree.find("s:Section[@name='{}']/f:Formula[@symbol='{}']/f:Definition".format(section_name, formula_symbol), NAMESPACES)
        definition_element.text = repr(value)
    specs_tree.write(specs_file_path, encoding='utf-8', xml_declaration=True)


def _count_mismatched_bits(expected_words, actual_words):
    return sum(bin(expected_word ^ actual_word).count('1') for expected_word, actual_word in zip(expected_words, actual_words))


def example(resource_name, options, x_spec_name, x_start, x_stop, x_steps, y_spec_name, y_start, y_stop, y_steps):
    example_dir = os.path.join(os.path.dirname(__file__))

    pin_map_filename = os.path.join(example_dir, 'PinMap.pinmap')
    pattern_filename = os.path.join(example_dir, 'demo_pattern_no_hw.digipat')
    capture_waveform_filename = os.path.join(example_dir, 'demo_waveform.digicapture')
    original_spec_filename = os.path.join(example_dir, 'Specifications.specs')
    levels_filename = os.path.join(example_dir, 'PinLevels.digilevels')
    timing_filename = os.path.join(example_dir, 'Timing.digitiming')

    # Work on a temporary copy so the specifications file shipped with the example is never modified
    with tempfile.TemporaryDirectory() as temp_dir, \
            nidigital.Session(resource_name=resource_name, options=options) as session:
        temp_spec_filename = os.path.join(temp_dir, 'Specifications.specs')
        shutil.copy(original_spec_filename, temp_spec_filename)

        session.load_pin_map(pin_map_filename)
        session.load_pattern(pattern_filename)

        # Source random data; reg0 sets the number of source and capture loops used by the pattern
        source_waveform_data = [random.getrandbits(SAMPLE_WIDTH) for _ in range(NUMBER_OF_SAMPLES)]
        session.write_sequencer_register(nidigital.SequencerRegister.REGISTER0, len(source_waveform_data) * SAMPLE_WIDTH)
        session.pins[SOURCE_PIN].create_source_waveform_serial(SOURCE_WAVEFORM_NAME, nidigital.SourceDataMapping.BROADCAST, SAMPLE_WIDTH, nidigital.BitOrder.MSB)
        session.write_source_waveform_broadcast(SOURCE_WAVEFORM_NAME, source_waveform_data)

        session.create_capture_waveform_from_file_digicapture(CAPTURE_WAVEFORM_NAME, capture_waveform_filename)

        session.load_specifications_levels_and_timing(temp_spec_filename, levels_filename, timing_filename)
        session.apply_levels_and_timing(levels_filename, timing_filename)

        total_bits = len(source_waveform_data) * SAMPLE_WIDTH
        print('Start sweeping specifications')
        print('Fraction of mismatched capture bits for each ({}, {}) pair:'.format(x_spec_name, y_spec_name))
        for y_value in _sweep_values(y_start, y_stop, y_steps):
            for x_value in _sweep_values(x_start, x_stop, x_steps):
                # Only the specifications are unloaded, so reload only them; the levels and timing sheets are still loaded
                session.unload_specifications(temp_spec_filename)
                _update_specification_values(temp_spec_filename, {x_spec_name: x_value, y_spec_name: y_value})
                session.load_specifications_levels_and_timing(specifications_file_paths=temp_spec_filename)
                session.apply_levels_and_timing(levels_filename, timing_filename)

                session.burst_pattern(start_label='startdemo')
                captured_waveforms = session.fetch_capture_waveform(CAPTURE_WAVEFORM_NAME, len(source_waveform_data))
                for site_number, captured_waveform in captured_waveforms.items():
                    mismatch_fraction = _count_mismatched_bits(source_waveform_data, captured_waveform) / total_bits
                    print('Site {}: {}={:g}, {}={:g}: {:.4f}'.format(site_number, x_spec_name, x_value, y_spec_name, y_value, mismatch_fraction))

        session.selected_function = nidigital.SelectedFunction.DISCONNECT
        print('Done sweeping specifications')


def _main(argsv):
    parser = argparse.ArgumentParser(description='Demonstrates how to unload and reload a specifications file while sweeping two specification values and measuring the capture waveform bit errors at each point.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2,PXI1Slot3', help='Resource name of a NI digital pattern instrument. Ensure the resource name matches the instrument name in the pinmap file.')
    parser.add_argument('-s', '--simulate', default='True', choices=['True', 'False'], help='Whether to run on simulated hardware or real hardware')
    parser.add_argument('-xn', '--x-spec-name', default='AC.Strobe', help='Specification to sweep along the X axis, as <Section>.<Symbol>.')
    parser.add_argument('-xs', '--x-start', default=0.0, type=float, help='First value of the X axis sweep.')
    parser.add_argument('-xe', '--x-stop', default=1e-8, type=float, help='Last value of the X axis sweep.')
    parser.add_argument('-xc', '--x-steps', default=5, type=int, help='Number of values in the X axis sweep.')
    parser.add_argument('-yn', '--y-spec-name', default='DC.Voh', help='Specification to sweep along the Y axis, as <Section>.<Symbol>.')
    parser.add_argument('-ys', '--y-start', default=0.0, type=float, help='First value of the Y axis sweep.')
    parser.add_argument('-ye', '--y-stop', default=5.0, type=float, help='Last value of the Y axis sweep.')
    parser.add_argument('-yc', '--y-steps', default=5, type=int, help='Number of values in the Y axis sweep.')
    args = parser.parse_args(argsv)

    example(args.resource_name,
            'Simulate=1, DriverSetup=Model:6571' if args.simulate == 'True' else '',
            args.x_spec_name, args.x_start, args.x_stop, args.x_steps,
            args.y_spec_name, args.y_start, args.y_stop, args.y_steps)


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '6571'}, }
    example('PXI1Slot2,PXI1Slot3', options, 'AC.Strobe', 0.0, 1e-8, 2, 'DC.Voh', 0.0, 5.0, 2)


def test_main():
    _main(['--x-steps', '2', '--y-steps', '2'])


if __name__ == '__main__':
    main()
