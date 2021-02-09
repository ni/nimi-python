#!/usr/bin/python

import argparse
import nidigital
import os
import sys


class VoltageLevelsAndTerminationConfig():
    def __init__(self, vil, vih, vol, voh, vterm, termination_mode, iol, ioh, vcom):
        self.vil = vil
        self.vih = vih
        self.vol = vol
        self.voh = voh
        self.vterm = vterm
        self.termination_mode = termination_mode
        self.iol = iol
        self.ioh = ioh
        self.vcom = vcom


class TimeSetConfig():
    def __init__(self, time_set_name, period, drive_format, drive_on, drive_data, drive_return, drive_off, strobe_edge):
        self.time_set_name = time_set_name
        self.period = period
        self.drive_format = drive_format
        self.drive_on = drive_on
        self.drive_data = drive_data
        self.drive_return = drive_return
        self.drive_off = drive_off
        self.strobe_edge = strobe_edge


def convert_drive_format(drive_format):
    converter = {'NR': nidigital.DriveFormat.NR,
                 'RL': nidigital.DriveFormat.RL,
                 'RH': nidigital.DriveFormat.RH,
                 'SBC': nidigital.DriveFormat.SBC}
    return converter.get(drive_format, None)


def example(resource_name,
            options,
            channels,
            voltage_config,
            time_set_config):

    with nidigital.Session(resource_name=resource_name, options=options) as session:

        dir = os.path.dirname(__file__)

        # Load pin map (.pinmap) created using Digital Pattern Editor
        pin_map_filename = os.path.join(dir, 'PinMap.pinmap')
        session.load_pin_map(pin_map_filename)

        # Configure voltage levels and terminal voltage through driver API
        session.channels[channels].configure_voltage_levels(voltage_config.vil, voltage_config.vih, voltage_config.vol, voltage_config.voh, voltage_config.vterm)
        if voltage_config.termination_mode == 'High_Z':
            session.channels[channels].termination_mode = nidigital.TerminationMode.HIGH_Z
        elif voltage_config.termination_mode == 'Active_Load':
            session.channels[channels].termination_mode = nidigital.TerminationMode.ACTIVE_LOAD
            session.channels[channels].configure_active_load_levels(voltage_config.iol, voltage_config.ioh, voltage_config.vcom)
        else:
            session.channels[channels].termination_mode = nidigital.TerminationMode.VTERM

        # Configure time set through driver API
        session.create_time_set(time_set_config.time_set_name)  # Must match time set name in pattern file
        session.configure_time_set_period(time_set_config.time_set_name, time_set_config.period)
        session.channels[channels].configure_time_set_drive_edges(time_set_config.time_set_name, convert_drive_format(time_set_config.drive_format),
                                                                  time_set_config.drive_on, time_set_config.drive_data,
                                                                  time_set_config.drive_return, time_set_config.drive_off)
        session.channels[channels].configure_time_set_compare_edges_strobe(time_set_config.time_set_name, time_set_config.strobe_edge)

        # Load the pattern file (.digipat) created using Digital Pattern Editor
        pattern_filename = os.path.join(dir, 'Pattern.digipat')
        session.load_pattern(pattern_filename)

        # Burst pattern, blocks until the pattern is done bursting
        session.burst_pattern(start_label='new_pattern')
        print('Start bursting pattern')

        # Disconnect all channels using programmable onboard switching
        session.selected_function = nidigital.SelectedFunction.DISCONNECT
    print('Done bursting pattern')


def _main(argsv):
    parser = argparse.ArgumentParser(description='Demonstrates how to create an instrument session, configure time set and voltage levels, and burst a pattern on the digital pattern instrument.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2,PXI1Slot3', help='Resource name of a NI digital pattern instrument, ensure the resource name matches the instrument name in the pinmap file.')
    parser.add_argument('-s', '--simulate', default='True', choices=['True', 'False'], help='Whether to run on simulated hardware or on real hardware')
    parser.add_argument('-c', '--channels', default='PinGroup1', help='Channel(s)/Pin(s) to configure')

    # Parameters to configure voltage
    parser.add_argument('--vil', default=0, type=float, help='The voltage that the instrument will apply to the input of the DUT when the pin driver drives a logic low (0)')
    parser.add_argument('--vih', default=3.3, type=float, help='The voltage that the instrument will apply to the input of the DUT when the test instrument drives a logic high (1)')
    parser.add_argument('--vol', default=1.6, type=float, help='The output voltage below which the comparator on the pin driver interprets a logic low (L)')
    parser.add_argument('--voh', default=1.7, type=float, help='The output voltage above which the comparator on the pin driver interprets a logic high (H)')
    parser.add_argument('--vterm', default=2, type=float, help='The termination voltage the instrument applies during non-drive cycles when the termination mode is set to Vterm')
    parser.add_argument('-term-mode', '--termination-mode', default='High_Z', choices=['High_Z', 'Active_Load', 'Three_Level_Drive'])
    parser.add_argument('--iol', default=0.002, type=float, help='The maximum current that the DUT sinks while outputting a voltage below VCOM')
    parser.add_argument('--ioh', default=-0.002, type=float, help='The maximum current that the DUT sources while outputting a voltage above VCOM')
    parser.add_argument('--vcom', default=0.0, type=float, help='The commutating voltage level at which the active load circuit switches between sourcing current and sinking current')

    # Parameters to configure timeset
    parser.add_argument('--period', default=0.00000002, type=float, help='Period in second')
    parser.add_argument('-format', '--drive-format', default='NR', choices=['NR', 'RL', 'RH', 'SBC'], help='Non-return | Return to low | Return to high | Surround by complement')
    parser.add_argument('--drive-on', default=0, type=float, help='The delay in seconds from the beginning of the vector period for turning on the pin driver')
    parser.add_argument('--drive-data', default=0, type=float, help='The delay in seconds from the beginning of the vector period until the pattern data is driven to the pattern value')
    parser.add_argument('--drive-return', default=0.000000015, type=float, help='The delay in seconds from the beginning of the vector period until the pin changes from the pattern data to the return value, as specified in the format.')
    parser.add_argument('--drive-off', default=0.00000002, type=float, help='The delay in seconds from the beginning of the vector period to turn off the pin driver when the next vector period uses a non-drive symbol (L, H, X, V, M, E).')
    parser.add_argument('--strobe-edge', default=0.00000001, type=float, help='The time in second when the comparison happens within a vector period')

    args = parser.parse_args(argsv)
    voltage_config = VoltageLevelsAndTerminationConfig(args.vil, args.vih, args.vol, args.voh, args.vterm, args.termination_mode, args.iol, args.ioh, args.vcom)
    time_set_config = TimeSetConfig("tset0", args.period, args.drive_format, args.drive_on, args.drive_data, args.drive_return, args.drive_off, args.strobe_edge)
    example(args.resource_name,
            'Simulate=1, DriverSetup=Model:6571' if args.simulate == 'True' else '',
            args.channels,
            voltage_config,
            time_set_config)


def main():
    _main(sys.argv[1:])


def test_main():
    _main([])


def test_example():
    resource_name = 'PXI1Slot2,PXI1Slot3'
    options = {'simulate': True, 'driver_setup': {'Model': '6571'}, }
    channels = 'PinGroup1'
    voltage_config = VoltageLevelsAndTerminationConfig(vil=0, vih=3.3, vol=1.6, voh=1.7, vterm=2,
                                                       termination_mode='Active_Load', iol=0.002, ioh=-0.002, vcom=0)
    time_set_config = TimeSetConfig(time_set_name="tset0",
                                    period=0.00000002,
                                    drive_format='NR',
                                    drive_on=0, drive_data=0, drive_return=0.000000015, drive_off=0.00000002, strobe_edge=0.00000001)
    example(resource_name, options, channels, voltage_config, time_set_config)


if __name__ == '__main__':
    main()
