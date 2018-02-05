from niswitch import visatype

import datetime


def convert_repeated_capabilities(repeated_capability, prefix=''):
    # First try it as a list
    if isinstance(repeated_capability, list):
        rep_cap_list = [str(r) if str(r).lower().startswith(prefix.lower()) else prefix + str(r) for r in repeated_capability]
    else:
        # Then try it as a slice
        try:
            def ifnone(a, b):
                return b if a is None else a
            # Turn the slice into a list so we can iterate over it
            rep_cap_list = list(range(ifnone(repeated_capability.start, 0), repeated_capability.stop, ifnone(repeated_capability.step, 1)))
            # Add prefix to each entry
            rep_cap_list = [prefix + str(r) for r in rep_cap_list]
        # Otherwise it must be a single item
        except (TypeError, AttributeError):
            rep_cap_list = [str(repeated_capability) if str(repeated_capability).lower().startswith(prefix.lower()) else prefix + str(repeated_capability)]

    return ','.join(rep_cap_list)


def _convert_timedelta(value, library_type, scaling):
    scaled_value = value.total_seconds() * scaling

    # ctype integer types don't convert to int from float so we need to
    if library_type in [visatype.ViInt64, visatype.ViInt32, visatype.ViUInt32, visatype.ViInt16, visatype.ViUInt16, visatype.ViInt8]:
        scaled_value = int(scaled_value)

    return library_type(scaled_value)


def convert_timedelta_to_seconds(value, library_type):
    return _convert_timedelta(value, library_type, 1)


def convert_timedelta_to_milliseconds(value, library_type):
    return _convert_timedelta(value, library_type, 1000)


def convert_timedelta_to_microseconds(value, library_type):
    return _convert_timedelta(value, library_type, 1000000)


# Tests - time
def test_convert_timedelta_to_seconds_double():
    test_result = convert_timedelta_to_seconds(datetime.timedelta(seconds=10), visatype.ViReal64)
    assert test_result.value == 10.0
    assert isinstance(test_result, visatype.ViReal64)


def test_convert_timedelta_to_seconds_int():
    test_result = convert_timedelta_to_seconds(datetime.timedelta(seconds=10), visatype.ViInt32)
    assert test_result.value == 10
    assert isinstance(test_result, visatype.ViInt32)


def test_convert_timedelta_to_milliseconds_double():
    test_result = convert_timedelta_to_milliseconds(datetime.timedelta(seconds=10), visatype.ViReal64)
    assert test_result.value == 10000.0
    assert isinstance(test_result, visatype.ViReal64)


def test_convert_timedelta_to_milliseconds_int():
    test_result = convert_timedelta_to_milliseconds(datetime.timedelta(seconds=10), visatype.ViInt32)
    assert test_result.value == 10000
    assert isinstance(test_result, visatype.ViInt32)


def test_convert_timedelta_to_microseconds_double():
    test_result = convert_timedelta_to_microseconds(datetime.timedelta(seconds=10), visatype.ViReal64)
    assert test_result.value == 10000000.0
    assert isinstance(test_result, visatype.ViReal64)


def test_convert_timedelta_to_microseconds_int():
    test_result = convert_timedelta_to_microseconds(datetime.timedelta(seconds=10), visatype.ViInt32)
    assert test_result.value == 10000000
    assert isinstance(test_result, visatype.ViInt32)


# Tests - repeated capabilities
def test_repeated_capabilies_string_channel():
    test_result = convert_repeated_capabilities('0')
    assert test_result == '0'
    test_result = convert_repeated_capabilities('0,1')
    assert test_result == '0,1'


def test_repeated_capabilies_string_prefix():
    test_result = convert_repeated_capabilities('0', prefix='ScriptTrigger')
    assert test_result == 'ScriptTrigger0'


def test_repeated_capabilies_list_channel():
    test_result = convert_repeated_capabilities(['0'])
    assert test_result == '0'
    test_result = convert_repeated_capabilities(['0,1'])
    assert test_result == '0,1'
    test_result = convert_repeated_capabilities(['0', '1'])
    assert test_result == '0,1'
    test_result = convert_repeated_capabilities([0, 1])
    assert test_result == '0,1'


def test_repeated_capabilies_list_prefix():
    test_result = convert_repeated_capabilities(['ScriptTrigger0,ScriptTrigger1'], prefix='ScriptTrigger')
    assert test_result == 'ScriptTrigger0,ScriptTrigger1'
    test_result = convert_repeated_capabilities(['0'], prefix='ScriptTrigger')
    assert test_result == 'ScriptTrigger0'
    test_result = convert_repeated_capabilities(['0', '1'], prefix='ScriptTrigger')
    assert test_result == 'ScriptTrigger0,ScriptTrigger1'
    test_result = convert_repeated_capabilities([0, 1], prefix='ScriptTrigger')
    assert test_result == 'ScriptTrigger0,ScriptTrigger1'


def test_repeated_capabilies_slice_channel():
    test_result = convert_repeated_capabilities(slice(0, 1))
    assert test_result == '0'
    test_result = convert_repeated_capabilities(slice(0, 2))
    assert test_result == '0,1'
    test_result = convert_repeated_capabilities(slice(None, 2))
    assert test_result == '0,1'


def test_repeated_capabilies_slice_prefix():
    test_result = convert_repeated_capabilities(slice(0, 1), prefix='ScriptTrigger')
    assert test_result == 'ScriptTrigger0'
    test_result = convert_repeated_capabilities(slice(0, 2), prefix='ScriptTrigger')
    assert test_result == 'ScriptTrigger0,ScriptTrigger1'
    test_result = convert_repeated_capabilities(slice(None, 2), prefix='ScriptTrigger')
    assert test_result == 'ScriptTrigger0,ScriptTrigger1'

