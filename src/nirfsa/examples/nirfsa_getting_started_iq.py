import argparse
import nirfsa
import numpy as np
import sys


def example(resource_name, options, iq_carrier_frequency, reference_level, number_of_samples):
    with nirfsa.Session(resource_name=resource_name, id_query=False, reset_device=False, options=options) as rfsa_session:
        # Configurations
        rfsa_session.acquisition_type = nirfsa.AcquisitionType.IQ

        rfsa_session.reference_level = reference_level
        rfsa_session.iq_carrier_frequency = iq_carrier_frequency
        rfsa_session.number_of_samples = number_of_samples

        # Do something useful with the data.
        # We will present average power: 10log(((I^2 + Q ^2) / 2R) * 1000), where
        # R = 50 Ohms.

        iq_data_array = np.zeros(number_of_samples, dtype=np.complex128)
        wfm_info = rfsa_session.read_iq_single_record_into(iq_data_array)
        samples = np.asarray(wfm_info.samples)
        accumulator = 0.0
        if len(samples) > 0:
            for sample in samples:
                magnitude_squared = sample.real * sample.real + sample.imag * sample.imag
                # we need to handle this because log(0) return a range error.
                if magnitude_squared == 0.0:
                    magnitude_squared = 0.00000001
                accumulator += 10.0 * np.log10((magnitude_squared / (2.0 * 50.0)) * 1000.0)
            print('Average power = %0.1f dBm' % (accumulator / len(samples)))


def _main(argsv):
    parser = argparse.ArgumentParser(description='Acquires IQ data using NI-RFSA.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Resource name of the NI RF signal analyzer.')
    parser.add_argument('-c', '--iq-carrier-frequency', default=1e9, type=float, help='IQ carrier frequency in Hz.')
    parser.add_argument('-r', '--reference-level', default=0.0, type=float, help='Reference level in dBm.')
    parser.add_argument('-s', '--number-of-samples', default=1024, type=int, help='Number of IQ samples to acquire.')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Option string for the session.')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.option_string, args.iq_carrier_frequency, args.reference_level, args.number_of_samples)


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '5841', }, }
    example('simulated5841', options, 1e9, -10.0, 1024)


def test_main():
    cmd_line = ['--resource-name', 'simulated5841', '--iq-carrier-frequency', '1e9', '--reference-level', '-10', '--option-string', 'Simulate=1, DriverSetup=Model:5841']
    _main(cmd_line)


if __name__ == '__main__':
    main()
