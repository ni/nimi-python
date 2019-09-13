# -*- coding: utf-8 -*-
# This file was generated
import nidmm._visatype as _visatype


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


def convert_timedelta_to_milliseconds(value, library_type):
    return _convert_timedelta(value, library_type, 1000)


def convert_month_to_timedelta(months):
    import datetime
    return datetime.timedelta(days=(30.4167 * months))


# This converter is not called from the normal codegen path for function. Instead it is
# call from init and is a special case. Also, it just returns a string rather than a ctype object
def convert_init_with_options_dictionary(values, encoding):
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


# Let's run some tests
def test_convert_init_with_options_dictionary():
    assert convert_init_with_options_dictionary('', 'ascii') == ''
    assert convert_init_with_options_dictionary('Simulate=1', 'ascii') == 'Simulate=1'
    assert convert_init_with_options_dictionary({'Simulate': True, }, 'ascii') == 'Simulate=1'
    assert convert_init_with_options_dictionary({'Simulate': False, }, 'ascii') == 'Simulate=0'
    assert convert_init_with_options_dictionary({'Simulate': True, 'Cache': False}, 'ascii') == 'Cache=0,Simulate=1'
    assert convert_init_with_options_dictionary({'DriverSetup': {'Model': '5162 (4CH)', 'Bitfile': 'CustomProcessing'}}, 'ascii') == 'DriverSetup=Bitfile:CustomProcessing;Model:5162 (4CH)'
    assert convert_init_with_options_dictionary({'Simulate': True, 'DriverSetup': {'Model': '5162 (4CH)', 'Bitfile': 'CustomProcessing'}}, 'ascii') == 'DriverSetup=Bitfile:CustomProcessing;Model:5162 (4CH),Simulate=1'
    assert convert_init_with_options_dictionary({'simulate': True, 'cache': False}, 'ascii') == 'Cache=0,Simulate=1'
    assert convert_init_with_options_dictionary({'driver_setup': {'Model': '5162 (4CH)', 'Bitfile': 'CustomProcessing'}}, 'ascii') == 'DriverSetup=Bitfile:CustomProcessing;Model:5162 (4CH)'
    assert convert_init_with_options_dictionary({'simulate': True, 'driver_setup': {'Model': '5162 (4CH)', 'Bitfile': 'CustomProcessing'}}, 'ascii') == 'DriverSetup=Bitfile:CustomProcessing;Model:5162 (4CH),Simulate=1'


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


def test_convert_timedelta_to_milliseconds_double():
    import datetime

    test_result = convert_timedelta_to_milliseconds(datetime.timedelta(seconds=10), _visatype.ViReal64)
    assert test_result.value == 10000.0
    assert isinstance(test_result, _visatype.ViReal64)
    test_result = convert_timedelta_to_milliseconds(datetime.timedelta(seconds=-1), _visatype.ViReal64)
    assert test_result.value == -1000.0
    assert isinstance(test_result, _visatype.ViReal64)
    test_result = convert_timedelta_to_milliseconds(10.5, _visatype.ViReal64)
    assert test_result.value == 10500.0
    assert isinstance(test_result, _visatype.ViReal64)
    test_result = convert_timedelta_to_milliseconds(-1, _visatype.ViReal64)
    assert test_result.value == -1000.0
    assert isinstance(test_result, _visatype.ViReal64)


def test_convert_timedelta_to_milliseconds_int():
    import datetime

    test_result = convert_timedelta_to_milliseconds(datetime.timedelta(seconds=10), _visatype.ViInt32)
    assert test_result.value == 10000
    assert isinstance(test_result, _visatype.ViInt32)
    test_result = convert_timedelta_to_milliseconds(datetime.timedelta(seconds=-1), _visatype.ViInt32)
    assert test_result.value == -1000
    assert isinstance(test_result, _visatype.ViInt32)
    test_result = convert_timedelta_to_milliseconds(10.5, _visatype.ViInt32)
    assert test_result.value == 10500
    assert isinstance(test_result, _visatype.ViInt32)
    test_result = convert_timedelta_to_milliseconds(-1, _visatype.ViInt32)
    assert test_result.value == -1000
    assert isinstance(test_result, _visatype.ViInt32)


