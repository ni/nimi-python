#!/usr/bin/env python3
"""NI-Switch Software Scanning.

This example demonstrates how to scan a series of channels on an NI-SWITCH
module using software scanning. The session is configured with a scan list,
a trigger input source, and continuous scan mode. A software trigger is then
sent to advance through the scan sequence.

Note : This example supports only single channel scanning, for example,
"ch0->com0;". Multi-channel scanning requires additional configuration
and is not covered in this example.

The example uses the default resource name and scan parameters.
Modify these values as needed for your measurement setup.

HOW TO RUN:
-----------
i.   From terminal (with default values):
        python niswitch_software_scanning.py

ii.  From terminal (with custom values):
        python niswitch_software_scanning.py \
            -n "PXI2568" -tp "2568/31-SPST" -sl "ch0->com0;"

iii. To simulate without hardware:
        PowerShell:  python niswitch_software_scanning.py -sim
        cmd.exe:     python niswitch_software_scanning.py -sim

"""

# Module imports
import argparse    # For parsing command-line arguments
import sys         # For accessing command-line arguments via sys.argv

import niswitch    # NI-SWITCH instrument driver


def example(
    resource_name, topology, scan_list, continuous_scan, simulate, reset_device
):
    """Perform software scanning on an NI-SWITCH module.

    Args:
        resource_name (str):
            NI-SWITCH device identifier
            eg: "PXI2568"

        topology (str):
            Switch topology string
            eg: "2568/31-SPST"

        scan_list (str):
            Semicolon-delimited list of channel connections to scan
            eg: "ch0->com0;" -> close relay 0 (ch0 to com0)
                "ch1->com1;" -> close relay 1 (ch1 to com1)
                "ch2->com2;" -> close relay 2 (ch2 to com2)

        continuous_scan (bool):
            If True, the scan loops continuously until aborted
            If False, the scan completes a single pass and stops

        simulate (bool):
            If True, the session runs in simulation mode (no real hardware needed)

        reset_device (bool):
            If True, resets the device at session open

    Returns:
        None — result is printed to console
    """
    # trigger_input is set to SOFTWARE_TRIG, which means the scan advances
    # on each call to send_software_trigger()
    trig = niswitch.TriggerInput.SOFTWARE_TRIG

    # -> Open NI-SWITCH Session
    # - Opens communication with the switch module using the specified topology
    # - 'with' ensures automatic cleanup of session resources
    with niswitch.Session(
        resource_name=resource_name,
        topology=topology,
        simulate=simulate,
        reset_device=reset_device,
    ) as session:

        # -> Configure Scan Settings
        # - scan_list      → defines the channel connections to scan through
        # - trigger_input  → SOFTWARE_TRIG: scan advances on each send_software_trigger() call
        # - continuous_scan → controls whether the scan loops or runs once
        session.scan_list = scan_list
        session.trigger_input = trig
        session.continuous_scan = continuous_scan

        # -> Initiate Scan
        # - Arms the switch module and waits for the first trigger
        session.initiate()

        # -> Send Software Trigger
        # - Advances the scan to the next step in the scan list
        session.send_software_trigger()

        # - print confirmation message to console
        print(f"Software trigger sent. Scan '{scan_list}' initiated on '{resource_name}'.")


def _main(argsv):
    """Parses command-line arguments and calls example() with the parsed values."""
    parser = argparse.ArgumentParser(
        description='NI-SWITCH Software Scanning: scan a series of channels using a configurable trigger source.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('-n', '--resource-name', default='PXI2568', help='NI-SWITCH device resource name')
    parser.add_argument('-tp', '--topology', default='2568/31-SPST', help='Switch topology string')
    parser.add_argument('-sl', '--scan-list', default='ch0->com0;', help='Scan list of channel connections (eg: "ch0->com0;")')
    parser.add_argument('-cs', '--continuous-scan', action='store_true', default=False, help='Enable continuous scan (loops until aborted; default: single pass)')
    parser.add_argument('-sim', '--simulate', action='store_true', default=False, help='Run in simulation mode (no hardware required)')
    parser.add_argument('-rst', '--reset-device', action='store_true', default=False, help='Reset device at session open')
    args = parser.parse_args(argsv)
    example(
        resource_name=args.resource_name,
        topology=args.topology,
        scan_list=args.scan_list,
        continuous_scan=args.continuous_scan,
        simulate=args.simulate,
        reset_device=args.reset_device,
    )


def main():
    """Entry point — passes real CLI args to _main()."""
    _main(sys.argv[1:])


def test_example():
    """Simulated hardware test — runs example() with virtual NI-2568 switch (no real HW needed)."""
    example(
        resource_name='',
        topology='2568/31-SPST',
        scan_list='ch0->com0;',
        continuous_scan=True,
        simulate=True,
        reset_device=False,
    )


def test_main():
    """Simulated CLI test — runs _main() with simulate flag."""
    cmd_line = ['--simulate', '--continuous-scan']
    _main(cmd_line)


# ------------------------------------------------------------
# Script execution starts here
# ------------------------------------------------------------
if __name__ == '__main__':
    main()
