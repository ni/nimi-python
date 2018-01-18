from nidcpower import visatype

import datetime


def _convert_timedelta(value, library_type, scaling):
    scaled_value = value.total_seconds() * scaling

    if not library_type == visatype.ViReal64 and not library_type == visatype.ViReal32:  # ctype integer types don't convert to int from float so we need to
        scaled_value = int(scaled_value + 0.5)

    return library_type(scaled_value)


def convert_timedelta_to_seconds(value, library_type):
    return _convert_timedelta(value, library_type, 1)


def convert_timedelta_to_milliseconds(value, library_type):
    return _convert_timedelta(value, library_type, 1000)


def convert_timedelta_to_microseconds(value, library_type):
    return _convert_timedelta(value, library_type, 1000000)


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



