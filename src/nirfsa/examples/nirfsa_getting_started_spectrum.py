import argparse
import nirfsa
import numpy as np
import sys


def example(resource_name, options, center_frequency, span, reference_level):
    with nirfsa.Session(resource_name=resource_name, id_query=False, reset_device=False, options=options) as rfsa_session:
        # Configurations
        rfsa_session.acquisition_type = nirfsa.AcquisitionType.SPECTRUM
        rfsa_session.reference_level = reference_level
        rfsa_session.resolution_bandwidth = 10e3
        rfsa_session.configure_spectrum_frequency(center_frequency=center_frequency, span=span)

        spectrum_buffer = np.zeros(rfsa_session.number_of_spectral_lines, dtype=np.float64)

        spectrum_info = rfsa_session.read_power_spectrum_into(spectrum_buffer, timeout=10.0)

        # Do something useful with the data.
        # We will find the highest peak in a bin, which is not the actual highest
        # peak and frequency we could find in the acquisition. For an accurate
        # peak search, we can analyze the data with the Spectral Measurements Toolset.
        samples = np.asarray(spectrum_info.samples)
        greatest_peak_index = int(np.argmax(samples))
        greatest_peak_power = samples[greatest_peak_index]
        greatest_peak_frequency = spectrum_info.initial_frequency + spectrum_info.frequency_increment * greatest_peak_index

        print(
            'The highest peak in a bin is %0.1f dBm at %0.3f MHz.'
            % (greatest_peak_power, greatest_peak_frequency / 1e6)
        )


def _main(argsv):
    parser = argparse.ArgumentParser(description='Acquires a power spectrum using NI-RFSA.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Resource name of the NI RF signal analyzer.')
    parser.add_argument('-c', '--center-frequency', default=1e9, type=float, help='Center frequency in Hz.')
    parser.add_argument('-s', '--span', default=100e6, type=float, help='Span in Hz.')
    parser.add_argument('-r', '--reference-level', default=0.0, type=float, help='Reference level in dBm.')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Option string for the session.')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.option_string, args.center_frequency, args.span, args.reference_level)


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '5841', }, }
    example('simulated5841', options, 1e9, 100e6, -10.0)


def test_main():
    cmd_line = ['--resource-name', 'simulated5841', '--center-frequency', '1e9', '--span', '100e6', '--reference-level', '-10', '--option-string', 'Simulate=1, DriverSetup=Model:5841']
    _main(cmd_line)


if __name__ == '__main__':
    main()
