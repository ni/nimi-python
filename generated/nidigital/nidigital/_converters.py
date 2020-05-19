# -*- coding: utf-8 -*-
# This file was generated
import nidigital._visatype as _visatype
import nidigital.errors as errors

import array
import collections
import hightime
import numbers
import pytest

from functools import singledispatch


@singledispatch
def _convert_repeated_capabilities(arg, prefix):  # noqa: F811
    '''Base version that should not be called

    Overall purpose is to convert the repeated capabilities to a list of strings with prefix from what ever form

    Supported types:
    - str - List (comma delimited)
    - str - Range (using '-' or ':')
    - str - single item
    - int
    - tuple
    - range
    - slice

    Each instance should return a list of strings, without prefix
    - '0' --> ['0']
    - 0 --> ['0']
    - '0, 1' --> ['0', '1']
    - 'ScriptTrigger0, ScriptTrigger1' --> ['0', '1']
    - '0-1' --> ['0', '1']
    - '0:1' --> ['0', '1']
    - '0-1,4' --> ['0', '1', '4']
    - range(0, 2) --> ['0', '1']
    - slice(0, 2) --> ['0', '1']
    - (0, 1, 4) --> ['0', '1', '4']
    - ('0-1', 4) --> ['0', '1', '4']
    - (slice(0, 1), '2', [4, '5-6'], '7-9', '11:14', '16, 17') -->
        ['0', '2', '4', '5', '6', '7', '8', '9', '11', '12', '13', '14', '16', '17']
    '''
    raise errors.InvalidRepeatedCapabilityError('Invalid type', type(arg))


@_convert_repeated_capabilities.register(numbers.Integral)  # noqa: F811
def _(repeated_capability, prefix):
    '''Integer version'''
    return [str(repeated_capability)]


# This parsing function duplicate the parsing in the driver, so if changes to the allowed format are made there, they will need to be replicated here.
@_convert_repeated_capabilities.register(str)  # noqa: F811
def _(repeated_capability, prefix):
    '''String version (this is the most complex)

    We need to deal with a range ('0-3' or '0:3'), a list ('0,1,2,3') and a single item
    '''
    # First we deal with a list
    rep_cap_list = repeated_capability.split(',')
    if len(rep_cap_list) > 1:
        # We have a list so call ourselves again to let the iterable instance handle it
        return _convert_repeated_capabilities(rep_cap_list, prefix)

    # Now we deal with ranges
    # We remove any prefix and change ':' to '-'
    r = repeated_capability.strip().replace(prefix, '').replace(':', '-')
    rc = r.split('-')
    if len(rc) > 1:
        if len(rc) > 2:
            raise errors.InvalidRepeatedCapabilityError("Multiple '-' or ':'", repeated_capability)
        start = int(rc[0])
        end = int(rc[1])
        if end < start:
            rng = range(start, end - 1, -1)
        else:
            rng = range(start, end + 1)
        return _convert_repeated_capabilities(rng, prefix)

    # If we made it here, it must be a simple item so we remove any prefix and return
    return [repeated_capability.replace(prefix, '').strip()]


# We cannot use collections.abc.Iterable here because strings are also iterable and then this
# instance is what gets called instead of the string one.
@_convert_repeated_capabilities.register(list)  # noqa: F811
@_convert_repeated_capabilities.register(range)  # noqa: F811
@_convert_repeated_capabilities.register(tuple)  # noqa: F811
def _(repeated_capability, prefix):
    '''Iterable version - can handle lists, ranges, and tuples'''
    rep_cap_list = []
    for r in repeated_capability:
        rep_cap_list += _convert_repeated_capabilities(r, prefix)
    return rep_cap_list


@_convert_repeated_capabilities.register(slice)  # noqa: F811
def _(repeated_capability, prefix):
    '''slice version'''
    def ifnone(a, b):
        return b if a is None else a
    # Turn the slice into a list and call ourselves again to let the iterable instance handle it
    rng = range(ifnone(repeated_capability.start, 0), repeated_capability.stop, ifnone(repeated_capability.step, 1))
    return _convert_repeated_capabilities(rng, prefix)


def convert_repeated_capabilities(repeated_capability, prefix=''):
    '''Convert a repeated capabilities object to a comma delimited list

    Args:
        repeated_capability (str, list, tuple, slice, None) -
        prefix (str) - common prefix for all strings

    Returns:
        rep_cap_list (list of str) - list of each repeated capability item with ranges expanded and prefix added
    '''
    # We need to explicitly handle None here. Everything else we can pass on to the singledispatch functions
    if repeated_capability is None:
        return []
    return [prefix + r for r in _convert_repeated_capabilities(repeated_capability, prefix)]


def convert_repeated_capabilities_without_prefix(repeated_capability):
    '''Convert a repeated capabilities object, without any prefix, to a comma delimited list

    Args:
        repeated_capability - Supported types:
            - str - list (comma-delimited)
            - str - range (using '-' or ':')
            - str - single item
            - int
            - list of str
            - tuple of str
            - range of str
            - slice of str
            - None

    Returns:
        rep_cap (str) - comma delimited string of each repeated capability item with ranges expanded
    '''
    return ','.join(convert_repeated_capabilities(repeated_capability, ''))


def _convert_timedelta(value, library_type, scaling):
    try:
        # We first assume it is a timedelta object
        scaled_value = value.total_seconds() * scaling
    except AttributeError:
        # If that doesn't work, assume it is a value in seconds
        # cast to float so scaled_value is always a float. This allows `timeout=10` to work as expected
        scaled_value = float(value) * scaling

    # ctype integer types don't convert to int from float so we need to
    if library_type in [_visatype.ViInt64, _visatype.ViInt32, _visatype.ViUInt32, _visatype.ViInt16, _visatype.ViUInt16, _visatype.ViInt8]:
        scaled_value = int(scaled_value)

    return library_type(scaled_value)


def convert_timedelta_to_seconds_real64(value):
    return _convert_timedelta(value, _visatype.ViReal64, 1)


def convert_timedelta_to_milliseconds_int32(value):
    return _convert_timedelta(value, _visatype.ViInt32, 1000)


def convert_timedeltas_to_seconds_real64(values):
    return [convert_timedelta_to_seconds_real64(i) for i in values]


def convert_seconds_real64_to_timedelta(value):
    return hightime.timedelta(seconds=value)


def convert_seconds_real64_to_timedeltas(values):
    return [convert_seconds_real64_to_timedelta(i) for i in values]


def convert_month_to_timedelta(months):
    return hightime.timedelta(days=(30.4167 * months))


# This converter is not called from the normal codegen path for function. Instead it is
# call from init and is a special case.
def convert_init_with_options_dictionary(values):
    if type(values) is str:
        init_with_options_string = values
    else:
        good_keys = {
            'rangecheck': 'RangeCheck',
            'queryinstrstatus': 'QueryInstrStatus',
            'cache': 'Cache',
            'simulate': 'Simulate',
            'recordcoercions': 'RecordCoercions',
            'interchangecheck': 'InterchangeCheck',
            'driversetup': 'DriverSetup',
            'range_check': 'RangeCheck',
            'query_instr_status': 'QueryInstrStatus',
            'record_coercions': 'RecordCoercions',
            'interchange_check': 'InterchangeCheck',
            'driver_setup': 'DriverSetup',
        }
        init_with_options = []
        for k in sorted(values.keys()):
            value = None
            if k.lower() in good_keys and not good_keys[k.lower()] == 'DriverSetup':
                value = good_keys[k.lower()] + ('=1' if values[k] is True else '=0')
            elif k.lower() in good_keys and good_keys[k.lower()] == 'DriverSetup':
                if not isinstance(values[k], dict):
                    raise TypeError('DriverSetup must be a dictionary')
                value = 'DriverSetup=' + (';'.join([key + ':' + values[k][key] for key in sorted(values[k])]))
            else:
                value = k + ('=1' if values[k] is True else '=0')

            init_with_options.append(value)

        init_with_options_string = ','.join(init_with_options)

    return init_with_options_string


# convert value to bytes
@singledispatch
def _convert_to_bytes(value):  # noqa: F811
    pass


@_convert_to_bytes.register(list)  # noqa: F811
@_convert_to_bytes.register(bytes)  # noqa: F811
@_convert_to_bytes.register(bytearray)  # noqa: F811
@_convert_to_bytes.register(array.array)  # noqa: F811
def _(value):
    return value


@_convert_to_bytes.register(str)  # noqa: F811
def _(value):
    return value.encode()


def convert_to_bytes(value):  # noqa: F811
    return bytes(_convert_to_bytes(value))


def convert_comma_separated_string_to_list(comma_separated_string):
    return [x.strip() for x in comma_separated_string.split(',')]


def convert_chained_repeated_capability_to_parts(chained_repeated_capability):
    '''Convert a chained repeated capabilities string to a list of comma-delimited repeated capabilities string.

    Converter assumes that the input contains the full cartesian product of its parts.
    e.g. If chained_repeated_capability is 'site0/PinA,site0/PinB,site1/PinA,site1/PinB',
    ['site0,site1', 'PinA,PinB'] is returned.

    Args:
        chained_repeated_capability (str) - comma-delimited repeated capabilities string where each
        item is a chain of slash-delimited repeated capabilities

    Returns:
        rep_cap_list (list of str) - list of comma-delimited repeated capabilities string
    '''
    chained_repeated_capability_items = convert_comma_separated_string_to_list(chained_repeated_capability)
    repeated_capability_lists = [[] for _ in range(chained_repeated_capability_items[0].count('/') + 1)]
    for item in chained_repeated_capability_items:
        repeated_capability_lists = [x + [y] for x, y in zip(repeated_capability_lists, item.split('/'))]
    return [','.join(collections.OrderedDict.fromkeys(x)) for x in repeated_capability_lists]


# Let's run some tests
def test_convert_init_with_options_dictionary():
    assert convert_init_with_options_dictionary('') == ''
    assert convert_init_with_options_dictionary('Simulate=1') == 'Simulate=1'
    assert convert_init_with_options_dictionary({'Simulate': True, }) == 'Simulate=1'
    assert convert_init_with_options_dictionary({'Simulate': False, }) == 'Simulate=0'
    assert convert_init_with_options_dictionary({'Simulate': True, 'Cache': False}) == 'Cache=0,Simulate=1'
    assert convert_init_with_options_dictionary({'DriverSetup': {'Model': '5162 (4CH)', 'Bitfile': 'CustomProcessing'}}) == 'DriverSetup=Bitfile:CustomProcessing;Model:5162 (4CH)'
    assert convert_init_with_options_dictionary({'Simulate': True, 'DriverSetup': {'Model': '5162 (4CH)', 'Bitfile': 'CustomProcessing'}}) == 'DriverSetup=Bitfile:CustomProcessing;Model:5162 (4CH),Simulate=1'
    assert convert_init_with_options_dictionary({'simulate': True, 'cache': False}) == 'Cache=0,Simulate=1'
    assert convert_init_with_options_dictionary({'driver_setup': {'Model': '5162 (4CH)', 'Bitfile': 'CustomProcessing'}}) == 'DriverSetup=Bitfile:CustomProcessing;Model:5162 (4CH)'
    assert convert_init_with_options_dictionary({'simulate': True, 'driver_setup': {'Model': '5162 (4CH)', 'Bitfile': 'CustomProcessing'}}) == 'DriverSetup=Bitfile:CustomProcessing;Model:5162 (4CH),Simulate=1'


# Tests - time
def test_convert_timedelta_to_seconds_double():
    test_result = convert_timedelta_to_seconds_real64(hightime.timedelta(seconds=10))
    assert test_result.value == 10.0
    assert isinstance(test_result, _visatype.ViReal64)
    test_result = convert_timedelta_to_seconds_real64(hightime.timedelta(nanoseconds=-0.5))
    assert test_result.value == pytest.approx(-5e-10)
    assert isinstance(test_result, _visatype.ViReal64)
    test_result = convert_timedelta_to_seconds_real64(10.5)
    assert test_result.value == 10.5
    assert isinstance(test_result, _visatype.ViReal64)
    test_result = convert_timedelta_to_seconds_real64(-1)
    assert test_result.value == -1
    assert isinstance(test_result, _visatype.ViReal64)


def test_convert_timedelta_to_milliseconds_int32():
    test_result = convert_timedelta_to_milliseconds_int32(hightime.timedelta(seconds=10))
    assert test_result.value == 10000
    assert isinstance(test_result, _visatype.ViInt32)
    test_result = convert_timedelta_to_milliseconds_int32(hightime.timedelta(seconds=-5))
    assert test_result.value == -5000
    assert isinstance(test_result, _visatype.ViInt32)
    test_result = convert_timedelta_to_milliseconds_int32(10.5)
    assert test_result.value == 10500
    assert isinstance(test_result, _visatype.ViInt32)
    test_result = convert_timedelta_to_milliseconds_int32(-1)
    assert test_result.value == -1000
    assert isinstance(test_result, _visatype.ViInt32)


def test_convert_timedeltas_to_seconds_real64():
    time_values = [10.5, -5e-10]
    test_result = convert_timedeltas_to_seconds_real64(time_values)
    assert all([actual.value == pytest.approx(expected) for actual, expected in zip(test_result, time_values)])
    assert all([isinstance(i, _visatype.ViReal64) for i in test_result])
    test_input = [hightime.timedelta(seconds=10.5), hightime.timedelta(nanoseconds=-0.5)]
    test_result = convert_timedeltas_to_seconds_real64(test_input)
    assert all([actual.value == pytest.approx(expected) for actual, expected in zip(test_result, time_values)])
    assert all([isinstance(i, _visatype.ViReal64) for i in test_result])


def test_convert_seconds_real64_to_timedelta():
    time_value = -5e-10
    test_result = convert_seconds_real64_to_timedelta(time_value)
    assert test_result.total_seconds() == pytest.approx(time_value)
    assert isinstance(test_result, hightime.timedelta)


def test_convert_seconds_real64_to_timedeltas():
    time_values = [10.5, -5e-10]
    test_result = convert_seconds_real64_to_timedeltas(time_values)
    assert all([actual.total_seconds() == pytest.approx(expected) for actual, expected in zip(test_result, time_values)])
    assert all([isinstance(x, hightime.timedelta) for x in test_result])


# Tests - repeated capabilities
def test_repeated_capabilies_string_channel():
    test_result_list = convert_repeated_capabilities('0')
    assert test_result_list == ['0']
    test_result_list = convert_repeated_capabilities('r0')
    assert test_result_list == ['r0']
    test_result_list = convert_repeated_capabilities('0,1')
    assert test_result_list == ['0', '1']


def test_repeated_capabilies_string_prefix():
    test_result_list = convert_repeated_capabilities('0', prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0']


def test_repeated_capabilies_list_channel():
    test_result_list = convert_repeated_capabilities(['0'])
    assert test_result_list == ['0']
    test_result_list = convert_repeated_capabilities(['r0'])
    assert test_result_list == ['r0']
    test_result_list = convert_repeated_capabilities(['0', '1'])
    assert test_result_list == ['0', '1']
    test_result_list = convert_repeated_capabilities([0, 1])
    assert test_result_list == ['0', '1']
    test_result_list = convert_repeated_capabilities([0, 1, '3'])
    assert test_result_list == ['0', '1', '3']


def test_repeated_capabilies_list_prefix():
    test_result_list = convert_repeated_capabilities(['ScriptTrigger0', 'ScriptTrigger1'], prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']
    test_result_list = convert_repeated_capabilities(['0'], prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0']
    test_result_list = convert_repeated_capabilities(['0', '1'], prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']
    test_result_list = convert_repeated_capabilities([0, 1], prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']


def test_repeated_capabilies_tuple_channel():
    test_result_list = convert_repeated_capabilities(('0'))
    assert test_result_list == ['0']
    test_result_list = convert_repeated_capabilities(('0,1'))
    assert test_result_list == ['0', '1']
    test_result_list = convert_repeated_capabilities(('0', '1'))
    assert test_result_list == ['0', '1']
    test_result_list = convert_repeated_capabilities((0, 1))
    assert test_result_list == ['0', '1']
    test_result_list = convert_repeated_capabilities((0, 1, '3'))
    assert test_result_list == ['0', '1', '3']


def test_repeated_capabilies_tuple_prefix():
    test_result_list = convert_repeated_capabilities(('ScriptTrigger0,ScriptTrigger1'), prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']
    test_result_list = convert_repeated_capabilities(('0'), prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0']
    test_result_list = convert_repeated_capabilities(('0', '1'), prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']
    test_result_list = convert_repeated_capabilities((0, 1), prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']


def test_repeated_capabilies_unicode():
    test_result_list = convert_repeated_capabilities(u'ScriptTrigger0,ScriptTrigger1', prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']
    test_result_list = convert_repeated_capabilities(u'ScriptTrigger0,ScriptTrigger1', prefix=u'ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']
    test_result_list = convert_repeated_capabilities('ScriptTrigger0,ScriptTrigger1', prefix=u'ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']


def test_repeated_capabilies_raw():
    test_result_list = convert_repeated_capabilities(r'ScriptTrigger0,ScriptTrigger1', prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']
    test_result_list = convert_repeated_capabilities(r'ScriptTrigger0,ScriptTrigger1', prefix=r'ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']
    test_result_list = convert_repeated_capabilities('ScriptTrigger0,ScriptTrigger1', prefix=r'ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']
    test_result_list = convert_repeated_capabilities(r'ScriptTrigger0,ScriptTrigger1', prefix=u'ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']
    test_result_list = convert_repeated_capabilities(r'ScriptTrigger0,ScriptTrigger1', prefix=r'ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']
    test_result_list = convert_repeated_capabilities(u'ScriptTrigger0,ScriptTrigger1', prefix=r'ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']


def test_repeated_capabilies_slice_channel():
    test_result_list = convert_repeated_capabilities(slice(0, 1))
    assert test_result_list == ['0']
    test_result_list = convert_repeated_capabilities(slice(0, 2))
    assert test_result_list == ['0', '1']
    test_result_list = convert_repeated_capabilities(slice(None, 2))
    assert test_result_list == ['0', '1']


def test_repeated_capabilies_mixed_channel():
    test_result_list = convert_repeated_capabilities((slice(0, 1), '2', [4, '5-6'], '7-9', '11:14', '16, 17'))
    assert test_result_list == ['0', '2', '4', '5', '6', '7', '8', '9', '11', '12', '13', '14', '16', '17']
    test_result_list = convert_repeated_capabilities([slice(0, 1), '2', [4, '5-6'], '7-9', '11:14', '16, 17'])
    assert test_result_list == ['0', '2', '4', '5', '6', '7', '8', '9', '11', '12', '13', '14', '16', '17']


def test_repeated_capabilies_mixed_prefix():
    test_result_list = convert_repeated_capabilities((slice(0, 1), '2', [4, '5-6'], '7-9', '11:14', '16, 17'), prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger2', 'ScriptTrigger4', 'ScriptTrigger5', 'ScriptTrigger6', 'ScriptTrigger7', 'ScriptTrigger8', 'ScriptTrigger9', 'ScriptTrigger11', 'ScriptTrigger12', 'ScriptTrigger13', 'ScriptTrigger14', 'ScriptTrigger16', 'ScriptTrigger17']
    test_result_list = convert_repeated_capabilities([slice(0, 1), '2', [4, '5-6'], '7-9', '11:14', '16, 17'], prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger2', 'ScriptTrigger4', 'ScriptTrigger5', 'ScriptTrigger6', 'ScriptTrigger7', 'ScriptTrigger8', 'ScriptTrigger9', 'ScriptTrigger11', 'ScriptTrigger12', 'ScriptTrigger13', 'ScriptTrigger14', 'ScriptTrigger16', 'ScriptTrigger17']


def test_invalid_repeated_capabilies():
    try:
        convert_repeated_capabilities('6-8-10')
        assert False
    except errors.InvalidRepeatedCapabilityError:
        pass
    try:
        convert_repeated_capabilities(['5', '6-8-10'])
        assert False
    except errors.InvalidRepeatedCapabilityError:
        pass
    try:
        convert_repeated_capabilities(('5', '6-8-10'))
        assert False
    except errors.InvalidRepeatedCapabilityError:
        pass
    try:
        convert_repeated_capabilities('5,6-8-10')
        assert False
    except errors.InvalidRepeatedCapabilityError:
        pass
    try:
        convert_repeated_capabilities(5.0)
        assert False
    except errors.InvalidRepeatedCapabilityError:
        pass
    try:
        convert_repeated_capabilities([5.0, '0'])
        assert False
    except errors.InvalidRepeatedCapabilityError:
        pass
    try:
        convert_repeated_capabilities((5.0, '0'))
        assert False
    except errors.InvalidRepeatedCapabilityError:
        pass


def test_repeated_capabilies_slice_prefix():
    test_result_list = convert_repeated_capabilities(slice(0, 1), prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0']
    test_result_list = convert_repeated_capabilities(slice(0, 2), prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']
    test_result_list = convert_repeated_capabilities(slice(None, 2), prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']


def test_repeated_capabilies_without_prefix():
    test_result = convert_repeated_capabilities_without_prefix((slice(0, 1), '2', [4, '5-6'], '7-9', '11:14', '16, 17'))
    assert test_result == '0,2,4,5,6,7,8,9,11,12,13,14,16,17'


def test_convert_chained_repeated_capability_to_parts_three_parts():
    chained_rep_cap = ('site0/test/PinA,site0/test/PinB,site0/test/PinC,'
                       'site1/test/PinA,site1/test/PinB,site1/test/PinC')
    rep_cap_list = convert_chained_repeated_capability_to_parts(chained_rep_cap)
    assert rep_cap_list == ['site0,site1', 'test', 'PinA,PinB,PinC']


def test_convert_chained_repeated_capability_to_parts_single_part():
    rep_cap_list = convert_chained_repeated_capability_to_parts('site0, site1')
    assert rep_cap_list == ['site0,site1']


def test_convert_chained_repeated_capability_to_parts_empty_string():
    rep_cap_list = convert_chained_repeated_capability_to_parts('')
    assert rep_cap_list == ['']


def test_string_to_list_channel():
    test_result = _convert_repeated_capabilities('r0', '')
    assert test_result == ['r0']
    test_result = _convert_repeated_capabilities(['0-2'], '')
    assert test_result == ['0', '1', '2']
    test_result = _convert_repeated_capabilities(['3:7'], '')
    assert test_result == ['3', '4', '5', '6', '7']
    test_result = _convert_repeated_capabilities(['2-0'], '')
    assert test_result == ['2', '1', '0']
    test_result = _convert_repeated_capabilities(['2:0'], '')
    assert test_result == ['2', '1', '0']


def test_string_to_list_prefix():
    test_result = _convert_repeated_capabilities(['ScriptTrigger3-ScriptTrigger7'], 'ScriptTrigger')
    assert test_result == ['3', '4', '5', '6', '7']
    test_result = _convert_repeated_capabilities(['ScriptTrigger3:ScriptTrigger7'], 'ScriptTrigger')
    assert test_result == ['3', '4', '5', '6', '7']
    test_result = _convert_repeated_capabilities(['ScriptTrigger2-ScriptTrigger0'], 'ScriptTrigger')
    assert test_result == ['2', '1', '0']
    test_result = _convert_repeated_capabilities(['ScriptTrigger2:ScriptTrigger0'], 'ScriptTrigger')
    assert test_result == ['2', '1', '0']


def test_convert_comma_separated_string_to_list():
    out_list = convert_comma_separated_string_to_list(' PinA ,  PinB , PinC  ')
    assert out_list == ['PinA', 'PinB', 'PinC']
