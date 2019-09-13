# -*- coding: utf-8 -*-
# This file was generated
import nitclk._visatype as _visatype


def _convert_timedelta(value, library_type, scaling):
    try:
        # We first assume it is a datetime.timedelta object
        scaled_value = value.total_seconds() * scaling
    except AttributeError:
        # If that doesn't work, assume it is a value in seconds
        # cast to float so scaled_value is always a float. This allows `timeout=10` to work as expected
        scaled_value = float(value) * scaling

    # ctype integer types don't convert to int from float so we need to
    if library_type in [_visatype.ViInt64, _visatype.ViInt32, _visatype.ViUInt32, _visatype.ViInt16, _visatype.ViUInt16, _visatype.ViInt8]:
        scaled_value = int(scaled_value)

    return library_type(scaled_value)


def convert_timedelta_to_seconds(value, library_type):
    return _convert_timedelta(value, library_type, 1)


# Tests - time
def test_convert_timedelta_to_seconds_double():
    import datetime

    test_result = convert_timedelta_to_seconds(datetime.timedelta(seconds=10), _visatype.ViReal64)
    assert test_result.value == 10.0
    assert isinstance(test_result, _visatype.ViReal64)
    test_result = convert_timedelta_to_seconds(datetime.timedelta(seconds=-1), _visatype.ViReal64)
    assert test_result.value == -1
    assert isinstance(test_result, _visatype.ViReal64)
    test_result = convert_timedelta_to_seconds(10.5, _visatype.ViReal64)
    assert test_result.value == 10.5
    assert isinstance(test_result, _visatype.ViReal64)
    test_result = convert_timedelta_to_seconds(-1, _visatype.ViReal64)
    assert test_result.value == -1
    assert isinstance(test_result, _visatype.ViReal64)


def test_convert_timedelta_to_seconds_int():
    import datetime

    test_result = convert_timedelta_to_seconds(datetime.timedelta(seconds=10), _visatype.ViInt32)
    assert test_result.value == 10
    assert isinstance(test_result, _visatype.ViInt32)
    test_result = convert_timedelta_to_seconds(datetime.timedelta(seconds=-1), _visatype.ViInt32)
    assert test_result.value == -1
    assert isinstance(test_result, _visatype.ViInt32)
    test_result = convert_timedelta_to_seconds(10.5, _visatype.ViInt32)
    assert test_result.value == 10
    assert isinstance(test_result, _visatype.ViInt32)
    test_result = convert_timedelta_to_seconds(-1, _visatype.ViInt32)
    assert test_result.value == -1
    assert isinstance(test_result, _visatype.ViInt32)


