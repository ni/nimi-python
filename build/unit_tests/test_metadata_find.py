from build.helper.metadata_find import find_len_size_parameter_names


def _parameter(name, mechanism='passed-in', size_value=None):
    size = {'mechanism': mechanism}
    if size_value is not None:
        size['value'] = size_value

    return {
        'name': name,
        'size': size,
    }


def test_find_len_size_parameter_names_multiple_sizes():
    parameters = [
        _parameter('len_a_size'),
        _parameter('len_b_size'),
        _parameter('len_a_data', mechanism='len', size_value='len_a_size'),
        _parameter('len_b_data', mechanism='len', size_value='len_b_size'),
        _parameter('timeout'),
    ]

    size_names = find_len_size_parameter_names(parameters)

    assert size_names == {'len_a_size', 'len_b_size'}


def test_find_len_size_parameter_names_empty_when_no_len_parameters():
    parameters = [
        _parameter('value'),
        _parameter('timeout'),
    ]

    size_names = find_len_size_parameter_names(parameters)

    assert size_names == set()
