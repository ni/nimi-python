from build.helper.metadata_filters import filter_parameters
from build.helper.parameter_usage_options import ParameterUsageOptions


def _parameter(name, direction='in', mechanism='passed-in', size_value=None):
    size = {'mechanism': mechanism}
    if size_value is not None:
        size['value'] = size_value

    return {
        'name': name,
        'direction': direction,
        'size': size,
        'is_session_handle': False,
        'is_repeated_capability': False,
        'enum': None,
        'numpy': False,
        'use_in_python_api': True,
        'complex_array_representation': None,
    }


def test_filter_parameters_mixed_usage_ivi_dance_and_len():
    parameters = [
        _parameter('ivi_size'),
        _parameter('out_waveform', direction='out', mechanism='ivi-dance', size_value='ivi_size'),
        _parameter('len_size'),
        _parameter('len_data', mechanism='len', size_value='len_size'),
        _parameter('timeout'),
    ]

    filtered = filter_parameters(parameters, ParameterUsageOptions.SESSION_METHOD_DECLARATION)
    filtered_names = [parameter['name'] for parameter in filtered]

    assert filtered_names == ['len_data', 'timeout']


def test_filter_parameters_multiple_len_sizes():
    parameters = [
        _parameter('len_a_size'),
        _parameter('len_b_size'),
        _parameter('len_a_data', mechanism='len', size_value='len_a_size'),
        _parameter('len_b_data', mechanism='len', size_value='len_b_size'),
        _parameter('timeout'),
    ]

    filtered = filter_parameters(parameters, ParameterUsageOptions.INTERPRETER_METHOD_DECLARATION)
    filtered_names = [parameter['name'] for parameter in filtered]

    assert filtered_names == ['len_a_data', 'len_b_data', 'timeout']
