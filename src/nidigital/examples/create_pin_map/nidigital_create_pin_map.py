#!/usr/bin/python

import argparse
import nidigital
import os
import sys
import tempfile
from xml.etree import ElementTree


def _create_pin_map(resource_name, file_path):
    instruments = [name.strip() for name in resource_name.split(',')]
    if len(instruments) != 2 or not all(instruments) or instruments[0] == instruments[1]:
        raise ValueError('This example requires two distinct instrument resource names, for example PXI1Slot2,PXI1Slot3.')

    # Python does not expose the LabVIEW pin/channel map creation APIs, so create an XML file for load_pin_map.
    # The bundled PinMap.pinmap is the equivalent reference map for create_pin_map.digiproj.
    pin_map = ElementTree.Element('PinMap', xmlns='http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd', schemaVersion='1.5')
    instrument_list = ElementTree.SubElement(pin_map, 'Instruments')
    for instrument in instruments:
        ElementTree.SubElement(instrument_list, 'NIDigitalPatternInstrument', name=instrument, numberOfChannels='32', group='Digital')

    # Pin and group names must match the bundled levels, timing, and pattern files.
    dut_pins = ('SCL', 'SDA', 'CS')
    pins = ElementTree.SubElement(pin_map, 'Pins')
    for pin in dut_pins:
        ElementTree.SubElement(pins, 'DUTPin', name=pin)
    ElementTree.SubElement(pins, 'SystemPin', name='Vcc')

    pin_groups = ElementTree.SubElement(pin_map, 'PinGroups')
    pin_group = ElementTree.SubElement(pin_groups, 'PinGroup', name='I2C_bus')
    for pin in ('Vcc',) + dut_pins:
        ElementTree.SubElement(pin_group, 'PinReference', pin=pin)

    sites = ElementTree.SubElement(pin_map, 'Sites')
    connections = ElementTree.SubElement(pin_map, 'Connections')
    # Both sites share CS on the first instrument; Vcc is a system pin, not a per-site pin.
    ElementTree.SubElement(connections, 'Connection', pin='CS', siteNumber='0,1', instrument=instruments[0], channel='30')
    for site, instrument in enumerate(instruments):
        ElementTree.SubElement(sites, 'Site', siteNumber=str(site))
        for pin, channel in (('SCL', '0'), ('SDA', '1')):
            ElementTree.SubElement(connections, 'Connection', pin=pin, siteNumber=str(site), instrument=instrument, channel=channel)
    ElementTree.SubElement(connections, 'SystemConnection', pin='Vcc', instrument=instruments[0], channel='3')

    ElementTree.ElementTree(pin_map).write(file_path, encoding='utf-8', xml_declaration=True)


def example(resource_name, options):
    # Keep the generated pin map outside the example directory and remove it after closing the session.
    with tempfile.TemporaryDirectory() as temp_dir:
        pin_map_filename = os.path.join(temp_dir, 'PinMap.pinmap')
        _create_pin_map(resource_name, pin_map_filename)

        with nidigital.Session(resource_name=resource_name, options=options) as session:
            # Load the pin map created at runtime, rather than the bundled reference map.
            session.load_pin_map(pin_map_filename)

            dir = os.path.dirname(os.path.abspath(__file__))
            levels_filename = os.path.join(dir, 'PinLevels.digilevels')
            timing_filename = os.path.join(dir, 'Timing.digitiming')
            session.load_specifications_levels_and_timing(levels_file_paths=levels_filename, timing_file_paths=timing_filename)

            session.apply_levels_and_timing(levels_filename, timing_filename)

            pattern_filename = os.path.join(dir, 'Pattern.digipat')
            session.load_pattern(pattern_filename)

            print('Start bursting pattern')
            try:
                session.burst_pattern(start_label='new_pattern')
            finally:
                session.selected_function = nidigital.SelectedFunction.DISCONNECT
    print('Done bursting pattern')


def _main(argsv):
    parser = argparse.ArgumentParser(description='Demonstrates how to create a pin map file, load levels and timing, and burst a pattern on the digital pattern instrument.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2,PXI1Slot3', help='The specified resource name of a digital pattern instrument, for example, PXI1Slot3, where PXI1Slot3 is an instrument resource name. This example requires two distinct instrument resource names in site order.')
    parser.add_argument('-s', '--simulate', default='True', choices=['True', 'False'], help='Whether to run on simulated hardware or real hardware')
    args = parser.parse_args(argsv)
    example(args.resource_name, 'Simulate=1, DriverSetup=Model:6571' if args.simulate == 'True' else '')


def main():
    _main(sys.argv[1:])


def test_example():
    resource_name = 'PXI1Slot2,PXI1Slot3'
    options = {'simulate': True, 'driver_setup': {'Model': '6571'}, }
    example(resource_name, options)


def test_main():
    _main([])
    _main(['--resource-name', 'PXI1Slot4,PXI1Slot5', '--simulate', 'True'])


if __name__ == '__main__':
    main()
