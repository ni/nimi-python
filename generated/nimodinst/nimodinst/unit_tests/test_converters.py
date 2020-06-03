# This file was generated
import nimodinst._converters as _converters
import nimodinst._visatype as _visatype

import hightime
import pytest


def test_convert_init_with_options_dictionary():
    assert _converters.convert_init_with_options_dictionary('') == ''
    assert _converters.convert_init_with_options_dictionary('Simulate=1') == 'Simulate=1'
    assert _converters.convert_init_with_options_dictionary({'Simulate': True, }) == 'Simulate=1'
    assert _converters.convert_init_with_options_dictionary({'Simulate': False, }) == 'Simulate=0'
    assert _converters.convert_init_with_options_dictionary({'Simulate': True, 'Cache': False}) == 'Cache=0,Simulate=1'
    assert _converters.convert_init_with_options_dictionary({'DriverSetup': {'Model': '5162 (4CH)', 'Bitfile': 'CustomProcessing'}}) == 'DriverSetup=Bitfile:CustomProcessing;Model:5162 (4CH)'
    assert _converters.convert_init_with_options_dictionary({'Simulate': True, 'DriverSetup': {'Model': '5162 (4CH)', 'Bitfile': 'CustomProcessing'}}) == 'DriverSetup=Bitfile:CustomProcessing;Model:5162 (4CH),Simulate=1'
    assert _converters.convert_init_with_options_dictionary({'simulate': True, 'cache': False}) == 'Cache=0,Simulate=1'
    assert _converters.convert_init_with_options_dictionary({'driver_setup': {'Model': '5162 (4CH)', 'Bitfile': 'CustomProcessing'}}) == 'DriverSetup=Bitfile:CustomProcessing;Model:5162 (4CH)'
    assert _converters.convert_init_with_options_dictionary({'simulate': True, 'driver_setup': {'Model': '5162 (4CH)', 'Bitfile': 'CustomProcessing'}}) == 'DriverSetup=Bitfile:CustomProcessing;Model:5162 (4CH),Simulate=1'


# Tests - time
def test_convert_timedelta_to_seconds_double():
    test_result = _converters.convert_timedelta_to_seconds_real64(hightime.timedelta(seconds=10))
    assert test_result.value == 10.0
    assert isinstance(test_result, _visatype.ViReal64)
    test_result = _converters.convert_timedelta_to_seconds_real64(hightime.timedelta(nanoseconds=-0.5))
    assert test_result.value == pytest.approx(-5e-10)
    assert isinstance(test_result, _visatype.ViReal64)
    test_result = _converters.convert_timedelta_to_seconds_real64(10.5)
    assert test_result.value == 10.5
    assert isinstance(test_result, _visatype.ViReal64)
    test_result = _converters.convert_timedelta_to_seconds_real64(-1)
    assert test_result.value == -1
    assert isinstance(test_result, _visatype.ViReal64)


def test_convert_timedelta_to_milliseconds_int32():
    test_result = _converters.convert_timedelta_to_milliseconds_int32(hightime.timedelta(seconds=10))
    assert test_result.value == 10000
    assert isinstance(test_result, _visatype.ViInt32)
    test_result = _converters.convert_timedelta_to_milliseconds_int32(hightime.timedelta(seconds=-5))
    assert test_result.value == -5000
    assert isinstance(test_result, _visatype.ViInt32)
    test_result = _converters.convert_timedelta_to_milliseconds_int32(10.5)
    assert test_result.value == 10500
    assert isinstance(test_result, _visatype.ViInt32)
    test_result = _converters.convert_timedelta_to_milliseconds_int32(-1)
    assert test_result.value == -1000
    assert isinstance(test_result, _visatype.ViInt32)


def test_convert_timedeltas_to_seconds_real64():
    time_values = [10.5, -5e-10]
    test_result = _converters.convert_timedeltas_to_seconds_real64(time_values)
    assert all([actual.value == pytest.approx(expected) for actual, expected in zip(test_result, time_values)])
    assert all([isinstance(i, _visatype.ViReal64) for i in test_result])
    test_input = [hightime.timedelta(seconds=10.5), hightime.timedelta(nanoseconds=-0.5)]
    test_result = _converters.convert_timedeltas_to_seconds_real64(test_input)
    assert all([actual.value == pytest.approx(expected) for actual, expected in zip(test_result, time_values)])
    assert all([isinstance(i, _visatype.ViReal64) for i in test_result])


def test_convert_seconds_real64_to_timedelta():
    time_value = -5e-10
    test_result = _converters.convert_seconds_real64_to_timedelta(time_value)
    assert test_result.total_seconds() == pytest.approx(time_value)
    assert isinstance(test_result, hightime.timedelta)


def test_convert_seconds_real64_to_timedeltas():
    time_values = [10.5, -5e-10]
    test_result = _converters.convert_seconds_real64_to_timedeltas(time_values)
    assert all([actual.total_seconds() == pytest.approx(expected) for actual, expected in zip(test_result, time_values)])
    assert all([isinstance(x, hightime.timedelta) for x in test_result])


def test_string_to_list_channel():
    test_result = _converters._convert_repeated_capabilities('r0', '')
    assert test_result == ['r0']
    test_result = _converters._convert_repeated_capabilities(['0-2'], '')
    assert test_result == ['0', '1', '2']
    test_result = _converters._convert_repeated_capabilities(['3:7'], '')
    assert test_result == ['3', '4', '5', '6', '7']
    test_result = _converters._convert_repeated_capabilities(['2-0'], '')
    assert test_result == ['2', '1', '0']
    test_result = _converters._convert_repeated_capabilities(['2:0'], '')
    assert test_result == ['2', '1', '0']


def test_string_to_list_prefix():
    test_result = _converters._convert_repeated_capabilities(['ScriptTrigger3-ScriptTrigger7'], 'ScriptTrigger')
    assert test_result == ['3', '4', '5', '6', '7']
    test_result = _converters._convert_repeated_capabilities(['ScriptTrigger3:ScriptTrigger7'], 'ScriptTrigger')
    assert test_result == ['3', '4', '5', '6', '7']
    test_result = _converters._convert_repeated_capabilities(['ScriptTrigger2-ScriptTrigger0'], 'ScriptTrigger')
    assert test_result == ['2', '1', '0']
    test_result = _converters._convert_repeated_capabilities(['ScriptTrigger2:ScriptTrigger0'], 'ScriptTrigger')
    assert test_result == ['2', '1', '0']


def test_convert_comma_separated_string_to_list():
    out_list = _converters.convert_comma_separated_string_to_list(' PinA ,  PinB , PinC  ')
    assert out_list == ['PinA', 'PinB', 'PinC']
