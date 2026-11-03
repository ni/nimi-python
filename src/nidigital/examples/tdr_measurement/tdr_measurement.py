#!/usr/bin/python

import argparse
import os
import sys

import nidigital

def example(resource_name, options, channel_list, endpoint_termination, apply_offsets):
    directory = os.path.dirname(os.path.abspath(__file__))

    with nidigital.Session(
        resource_name=resource_name, options=options, reset_device=True
    ) as session:
        try:
            # Load the pin map (.pinmap) created using the Digital Pattern Editor
            pin_map_filename = os.path.join(directory, "PinMap.pinmap")
            session.load_pin_map(pin_map_filename)

            # Configure whether the TDR endpoint is open or shorted to ground
            session.tdr_endpoint_termination = endpoint_termination

            # Measure propagation delays for the selected channels or pins.
            # apply_offsets=True (automatically applies the measured offsets to the instrument).
            print("Start TDR Measurement")

            offsets = session.channels[channel_list].tdr(apply_offsets=apply_offsets)
            offsets_in_seconds = [offset.total_seconds() for offset in offsets]

            print("TDR Offsets (seconds): {}".format(offsets_in_seconds))
        finally:
            # Disconnect all the selected channels using programmable onboard switching.
            session.channels[channel_list].selected_function = (
                nidigital.SelectedFunction.DISCONNECT
            )

        print("Done TDR Measurement")
        return offsets


def _main(argsv):
    parser = argparse.ArgumentParser(description='Demonstrates how to use Time-Domain Reflectometry (TDR) to measure propagation delays through cables, connectors, and load boards. Use a 50 ohm controlled-impedance system and ensure an open or short exists at the selected TDR plane.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2,PXI1Slot3', help='The specified resource name shown in Measurement & Automation Explorer (MAX) for a digital pattern instrument, for example, PXI1Slot3, where PXI1Slot3 is an instrument resource name.')
    parser.add_argument('-s', '--simulate', default='True', choices=['True', 'False'], help='Whether to run on simulated hardware or real hardware')
    parser.add_argument('-c', '--channel-list', default='PinGroup1', help='List of channels or pins to measure.')
    parser.add_argument('-e', '--tdr-endpoint-termination', default='OPEN', type=str.upper, choices=nidigital.TDREndpointTermination.__members__, help='Specifies whether TDR Channels are connected to an open circuit or a short to ground.')
    parser.add_argument('-a', '--apply-offsets', default='True', choices=['True', 'False'], help='A Boolean that specifies whether to apply the measured TDR offsets.')
    args = parser.parse_args(argsv)

    example(args.resource_name,
            'Simulate=1, DriverSetup=Model:6570' if args.simulate == 'True' else '',
            args.channel_list,
            nidigital.TDREndpointTermination[args.tdr_endpoint_termination],
            args.apply_offsets == 'True')

def main():
    _main(sys.argv[1:])


def test_main():
    _main([])
    _main(['--tdr-endpoint-termination', 'SHORT_TO_GROUND', '--apply-offsets', 'False'])


def test_example():
    resource_name = "PXI1Slot2,PXI1Slot3"
    options = {"simulate": True, "driver_setup": {"Model": "6570"}}
    channel_list = "PinGroup1"

    tdr_endpoint_termination = nidigital.TDREndpointTermination.OPEN

    example(resource_name, options, channel_list, tdr_endpoint_termination, apply_offsets=True)
    example(resource_name, options, channel_list, tdr_endpoint_termination, apply_offsets=False)

    tdr_endpoint_termination = nidigital.TDREndpointTermination.SHORT_TO_GROUND
    example(resource_name, options, channel_list, tdr_endpoint_termination, apply_offsets=True)
    example(resource_name, options, channel_list, tdr_endpoint_termination, apply_offsets=False)


if __name__ == '__main__':
    main()