from nimodinst import visatype

import datetime


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


def convert_seconds_to_timedelta(value):
    return datetime.timedelta(seconds=value)


def convert_milliseconds_to_timedelta(value):
    return datetime.timedelta(milliseconds=value)


def convert_microseconds_to_timedelta(value):
    return datetime.timedelta(microseconds=value)


# Tests
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


def test_convert_seconds_to_timedelta():
    test_result = convert_seconds_to_timedelta(1)
    assert test_result.total_seconds() == 1.0
    test_result = convert_seconds_to_timedelta(1.5)
    assert test_result.total_seconds() == 1.5


def test_convert_milliseconds_to_timedelta():
    test_result = convert_milliseconds_to_timedelta(1)
    assert test_result.total_seconds() == 0.001
    test_result = convert_milliseconds_to_timedelta(1.5)
    assert test_result.total_seconds() == 0.0015


def test_convert_microseconds_to_timedelta():
    test_result = convert_microseconds_to_timedelta(1)
    assert test_result.total_seconds() == 0.000001
    test_result = convert_microseconds_to_timedelta(15)
    assert test_result.total_seconds() == 0.000015

