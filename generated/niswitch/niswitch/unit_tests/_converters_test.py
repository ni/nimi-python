# This file was generated
import niswitch._converters as _converters
import niswitch._visatype as _visatype
import niswitch.errors as errors

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


# Tests - repeated capabilities
def test_repeated_capabilies_string_channel():
    test_result_list = _converters.convert_repeated_capabilities('0')
    assert test_result_list == ['0']
    test_result_list = _converters.convert_repeated_capabilities('r0')
    assert test_result_list == ['r0']
    test_result_list = _converters.convert_repeated_capabilities('0,1')
    assert test_result_list == ['0', '1']


def test_repeated_capabilies_string_prefix():
    test_result_list = _converters.convert_repeated_capabilities('0', prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0']


def test_repeated_capabilies_list_channel():
    test_result_list = _converters.convert_repeated_capabilities(['0'])
    assert test_result_list == ['0']
    test_result_list = _converters.convert_repeated_capabilities(['r0'])
    assert test_result_list == ['r0']
    test_result_list = _converters.convert_repeated_capabilities(['0', '1'])
    assert test_result_list == ['0', '1']
    test_result_list = _converters.convert_repeated_capabilities([0, 1])
    assert test_result_list == ['0', '1']
    test_result_list = _converters.convert_repeated_capabilities([0, 1, '3'])
    assert test_result_list == ['0', '1', '3']


def test_repeated_capabilies_list_prefix():
    test_result_list = _converters.convert_repeated_capabilities(['ScriptTrigger0', 'ScriptTrigger1'], prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']
    test_result_list = _converters.convert_repeated_capabilities(['0'], prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0']
    test_result_list = _converters.convert_repeated_capabilities(['0', '1'], prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']
    test_result_list = _converters.convert_repeated_capabilities([0, 1], prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']


def test_repeated_capabilies_tuple_channel():
    test_result_list = _converters.convert_repeated_capabilities(('0'))
    assert test_result_list == ['0']
    test_result_list = _converters.convert_repeated_capabilities(('0,1'))
    assert test_result_list == ['0', '1']
    test_result_list = _converters.convert_repeated_capabilities(('0', '1'))
    assert test_result_list == ['0', '1']
    test_result_list = _converters.convert_repeated_capabilities((0, 1))
    assert test_result_list == ['0', '1']
    test_result_list = _converters.convert_repeated_capabilities((0, 1, '3'))
    assert test_result_list == ['0', '1', '3']


def test_repeated_capabilies_tuple_prefix():
    test_result_list = _converters.convert_repeated_capabilities(('ScriptTrigger0,ScriptTrigger1'), prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']
    test_result_list = _converters.convert_repeated_capabilities(('0'), prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0']
    test_result_list = _converters.convert_repeated_capabilities(('0', '1'), prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']
    test_result_list = _converters.convert_repeated_capabilities((0, 1), prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']


def test_repeated_capabilies_unicode():
    test_result_list = _converters.convert_repeated_capabilities(u'ScriptTrigger0,ScriptTrigger1', prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']
    test_result_list = _converters.convert_repeated_capabilities(u'ScriptTrigger0,ScriptTrigger1', prefix=u'ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']
    test_result_list = _converters.convert_repeated_capabilities('ScriptTrigger0,ScriptTrigger1', prefix=u'ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']


def test_repeated_capabilies_raw():
    test_result_list = _converters.convert_repeated_capabilities(r'ScriptTrigger0,ScriptTrigger1', prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']
    test_result_list = _converters.convert_repeated_capabilities(r'ScriptTrigger0,ScriptTrigger1', prefix=r'ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']
    test_result_list = _converters.convert_repeated_capabilities('ScriptTrigger0,ScriptTrigger1', prefix=r'ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']
    test_result_list = _converters.convert_repeated_capabilities(r'ScriptTrigger0,ScriptTrigger1', prefix=u'ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']
    test_result_list = _converters.convert_repeated_capabilities(r'ScriptTrigger0,ScriptTrigger1', prefix=r'ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']
    test_result_list = _converters.convert_repeated_capabilities(u'ScriptTrigger0,ScriptTrigger1', prefix=r'ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']


def test_repeated_capabilies_slice_channel():
    test_result_list = _converters.convert_repeated_capabilities(slice(0, 1))
    assert test_result_list == ['0']
    test_result_list = _converters.convert_repeated_capabilities(slice(0, 2))
    assert test_result_list == ['0', '1']
    test_result_list = _converters.convert_repeated_capabilities(slice(None, 2))
    assert test_result_list == ['0', '1']


def test_repeated_capabilies_mixed_channel():
    test_result_list = _converters.convert_repeated_capabilities((slice(0, 1), '2', [4, '5-6'], '7-9', '11:14', '16, 17'))
    assert test_result_list == ['0', '2', '4', '5', '6', '7', '8', '9', '11', '12', '13', '14', '16', '17']
    test_result_list = _converters.convert_repeated_capabilities([slice(0, 1), '2', [4, '5-6'], '7-9', '11:14', '16, 17'])
    assert test_result_list == ['0', '2', '4', '5', '6', '7', '8', '9', '11', '12', '13', '14', '16', '17']


def test_repeated_capabilies_mixed_prefix():
    test_result_list = _converters.convert_repeated_capabilities((slice(0, 1), '2', [4, '5-6'], '7-9', '11:14', '16, 17'), prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger2', 'ScriptTrigger4', 'ScriptTrigger5', 'ScriptTrigger6', 'ScriptTrigger7', 'ScriptTrigger8', 'ScriptTrigger9', 'ScriptTrigger11', 'ScriptTrigger12', 'ScriptTrigger13', 'ScriptTrigger14', 'ScriptTrigger16', 'ScriptTrigger17']
    test_result_list = _converters.convert_repeated_capabilities([slice(0, 1), '2', [4, '5-6'], '7-9', '11:14', '16, 17'], prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger2', 'ScriptTrigger4', 'ScriptTrigger5', 'ScriptTrigger6', 'ScriptTrigger7', 'ScriptTrigger8', 'ScriptTrigger9', 'ScriptTrigger11', 'ScriptTrigger12', 'ScriptTrigger13', 'ScriptTrigger14', 'ScriptTrigger16', 'ScriptTrigger17']


def test_invalid_repeated_capabilies():
    try:
        _converters.convert_repeated_capabilities('6-8-10')
        assert False
    except errors.InvalidRepeatedCapabilityError:
        pass
    try:
        _converters.convert_repeated_capabilities(['5', '6-8-10'])
        assert False
    except errors.InvalidRepeatedCapabilityError:
        pass
    try:
        _converters.convert_repeated_capabilities(('5', '6-8-10'))
        assert False
    except errors.InvalidRepeatedCapabilityError:
        pass
    try:
        _converters.convert_repeated_capabilities('5,6-8-10')
        assert False
    except errors.InvalidRepeatedCapabilityError:
        pass
    try:
        _converters.convert_repeated_capabilities(5.0)
        assert False
    except errors.InvalidRepeatedCapabilityError:
        pass
    try:
        _converters.convert_repeated_capabilities([5.0, '0'])
        assert False
    except errors.InvalidRepeatedCapabilityError:
        pass
    try:
        _converters.convert_repeated_capabilities((5.0, '0'))
        assert False
    except errors.InvalidRepeatedCapabilityError:
        pass


def test_repeated_capabilies_slice_prefix():
    test_result_list = _converters.convert_repeated_capabilities(slice(0, 1), prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0']
    test_result_list = _converters.convert_repeated_capabilities(slice(0, 2), prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']
    test_result_list = _converters.convert_repeated_capabilities(slice(None, 2), prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']


def test_repeated_capabilies_without_prefix():
    test_result = _converters.convert_repeated_capabilities_without_prefix((slice(0, 1), '2', [4, '5-6'], '7-9', '11:14', '16, 17'))
    assert test_result == '0,2,4,5,6,7,8,9,11,12,13,14,16,17'


def test_convert_chained_repeated_capability_to_parts_three_parts():
    chained_rep_cap = ('site0/test/PinA,site0/test/PinB,site0/test/PinC,'
                       'site1/test/PinA,site1/test/PinB,site1/test/PinC')
    rep_cap_list = _converters.convert_chained_repeated_capability_to_parts(chained_rep_cap)
    assert rep_cap_list == ['site0,site1', 'test', 'PinA,PinB,PinC']


def test_convert_chained_repeated_capability_to_parts_single_part():
    rep_cap_list = _converters.convert_chained_repeated_capability_to_parts('site0, site1')
    assert rep_cap_list == ['site0,site1']


def test_convert_chained_repeated_capability_to_parts_empty_string():
    rep_cap_list = _converters.convert_chained_repeated_capability_to_parts('')
    assert rep_cap_list == ['']


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
