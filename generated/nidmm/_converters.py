import nidmm._errors as _errors
import nidmm._visatype as _visatype

import datetime
import six


# These parsing functions duplicate the parsing in the driver, so if changes are made there, they will need to be replicated here.
def _repeated_capability_string_to_list(repeated_capability, prefix):
    '''Convert a IVI string format range into a list of repeated capabilities numbers I.e. no prefix

    '0' becomes [0]
    '0-2' becomes [0, 1, 2]
    '0:2' becomes [0, 1, 2]
    '0,1,2' not allowed
    '''
    assert ',' not in repeated_capability, "',' should have been handled at a higher level"
    repeated_capability_list = []
    for r in repeated_capability:
        # We remove any prefix and change ':' to '-'
        r = r.strip().replace(prefix, '').replace(':', '-')
        rc = r.split('-')
        if len(rc) > 1:
            if len(rc) > 2:
                raise _errors.InvalidRepeatedCapabilityError("Multiple '-' or ':'", repeated_capability)
            start = rc[0]
            end = rc[1]
            if int(end) < int(start):
                for i in range(int(start), int(end) - 1, -1):
                    repeated_capability_list.append(str(i))
            else:
                for i in range(int(start), int(end) + 1):
                    repeated_capability_list.append(str(i))
        else:
            repeated_capability_list.append(r)

    return repeated_capability_list


def convert_repeated_capabilities(repeated_capability, prefix=''):
    '''Convert a repeated capabilities object to a comma delimited list

    Args:
        repeated_capability (str, list, tuple) -
            str - single string that follows driver repeated capabilities format
            list - call back into this function with each item
            slice - turn it in to a list
            tuple - call back into this function with each item
        prefix (str) - common prefix for all strings

    Returns:
        rep_cal_list (list of str) - list of each repeated capability item with ranges expanded and prefix added
    '''
    rep_cap_list = []
    if isinstance(repeated_capability, tuple):
        # If we recieved a tuple, then call ourselves with each item
        # print('Case #1')
        for r in repeated_capability:
            rep_cap_list += convert_repeated_capabilities(r, prefix)

    elif isinstance(repeated_capability, six.text_type) or isinstance(repeated_capability, six.string_types):
        # Look for a string. Remove any prefix and split on ','
        # print('Case #2')
        rep_cap_list = repeated_capability.replace(prefix, '').split(',')

    else:
        try:
            # Try as an iterable, call ourselves with each item
            # print('Case #3')
            for r in repeated_capability:
                rep_cap_list += convert_repeated_capabilities(r, prefix)

        except TypeError:
            try:
                # If that doesn't work, then try it as a slice
                def ifnone(a, b):
                    return b if a is None else a
                # Turn the slice into a list so we can iterate over it
                # print('Case #4')
                rep_cap_list = [str(r) for r in list(range(ifnone(repeated_capability.start, 0), repeated_capability.stop, ifnone(repeated_capability.step, 1)))]

            except (TypeError, AttributeError):
                # Otherwise it must be a single item that is not a string
                # print('Case #5')
                rep_cap_list = [str(repeated_capability).replace(prefix, '')]

    rep_cap_list = [prefix + r for r in _repeated_capability_string_to_list(rep_cap_list, prefix)]
    return rep_cap_list


def _convert_timedelta(value, library_type, scaling):
    scaled_value = value.total_seconds() * scaling

    # ctype integer types don't convert to int from float so we need to
    if library_type in [_visatype.ViInt64, _visatype.ViInt32, _visatype.ViUInt32, _visatype.ViInt16, _visatype.ViUInt16, _visatype.ViInt8]:
        scaled_value = int(scaled_value)

    return library_type(scaled_value)


def convert_timedelta_to_seconds(value, library_type):
    return _convert_timedelta(value, library_type, 1)


def convert_timedelta_to_milliseconds(value, library_type):
    return _convert_timedelta(value, library_type, 1000)


def convert_timedelta_to_microseconds(value, library_type):
    return _convert_timedelta(value, library_type, 1000000)


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
    test_result = convert_timedelta_to_seconds(datetime.timedelta(seconds=10), _visatype.ViReal64)
    assert test_result.value == 10.0
    assert isinstance(test_result, _visatype.ViReal64)
    test_result = convert_timedelta_to_seconds(datetime.timedelta(seconds=-1), _visatype.ViReal64)
    assert test_result.value == -1
    assert isinstance(test_result, _visatype.ViReal64)


def test_convert_timedelta_to_seconds_int():
    test_result = convert_timedelta_to_seconds(datetime.timedelta(seconds=10), _visatype.ViInt32)
    assert test_result.value == 10
    assert isinstance(test_result, _visatype.ViInt32)
    test_result = convert_timedelta_to_seconds(datetime.timedelta(seconds=-1), _visatype.ViInt32)
    assert test_result.value == -1
    assert isinstance(test_result, _visatype.ViInt32)


def test_convert_timedelta_to_milliseconds_double():
    test_result = convert_timedelta_to_milliseconds(datetime.timedelta(seconds=10), _visatype.ViReal64)
    assert test_result.value == 10000.0
    assert isinstance(test_result, _visatype.ViReal64)
    test_result = convert_timedelta_to_milliseconds(datetime.timedelta(seconds=-1), _visatype.ViReal64)
    assert test_result.value == -1000.0
    assert isinstance(test_result, _visatype.ViReal64)


def test_convert_timedelta_to_milliseconds_int():
    test_result = convert_timedelta_to_milliseconds(datetime.timedelta(seconds=10), _visatype.ViInt32)
    assert test_result.value == 10000
    assert isinstance(test_result, _visatype.ViInt32)
    test_result = convert_timedelta_to_milliseconds(datetime.timedelta(seconds=-1), _visatype.ViInt32)
    assert test_result.value == -1000
    assert isinstance(test_result, _visatype.ViInt32)


def test_convert_timedelta_to_microseconds_double():
    test_result = convert_timedelta_to_microseconds(datetime.timedelta(seconds=10), _visatype.ViReal64)
    assert test_result.value == 10000000.0
    assert isinstance(test_result, _visatype.ViReal64)
    test_result = convert_timedelta_to_microseconds(datetime.timedelta(seconds=-1), _visatype.ViReal64)
    assert test_result.value == -1000000.0
    assert isinstance(test_result, _visatype.ViReal64)


def test_convert_timedelta_to_microseconds_int():
    test_result = convert_timedelta_to_microseconds(datetime.timedelta(seconds=10), _visatype.ViInt32)
    assert test_result.value == 10000000
    assert isinstance(test_result, _visatype.ViInt32)
    test_result = convert_timedelta_to_microseconds(datetime.timedelta(seconds=-1), _visatype.ViInt32)
    assert test_result.value == -1000000
    assert isinstance(test_result, _visatype.ViInt32)


# Tests - repeated capabilities
def test_repeated_capabilies_string_channel():
    test_result_list = convert_repeated_capabilities('0')
    assert test_result_list == ['0']
    test_result_list = convert_repeated_capabilities('0,1')
    assert test_result_list == ['0', '1']


def test_repeated_capabilies_string_prefix():
    test_result_list = convert_repeated_capabilities('0', prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0']


def test_repeated_capabilies_list_channel():
    test_result_list = convert_repeated_capabilities(['0'])
    assert test_result_list == ['0']
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
    except _errors.InvalidRepeatedCapabilityError:
        pass
    try:
        convert_repeated_capabilities(['5', '6-8-10'])
        assert False
    except _errors.InvalidRepeatedCapabilityError:
        pass
    try:
        convert_repeated_capabilities(('5', '6-8-10'))
        assert False
    except _errors.InvalidRepeatedCapabilityError:
        pass
    try:
        convert_repeated_capabilities('5,6-8-10')
        assert False
    except _errors.InvalidRepeatedCapabilityError:
        pass


def test_repeated_capabilies_slice_prefix():
    test_result_list = convert_repeated_capabilities(slice(0, 1), prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0']
    test_result_list = convert_repeated_capabilities(slice(0, 2), prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']
    test_result_list = convert_repeated_capabilities(slice(None, 2), prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']


def test_string_to_list_channel():
    test_result = _repeated_capability_string_to_list(['0-2'], '')
    assert test_result == ['0', '1', '2']
    test_result = _repeated_capability_string_to_list(['3:7'], '')
    assert test_result == ['3', '4', '5', '6', '7']
    test_result = _repeated_capability_string_to_list(['2-0'], '')
    assert test_result == ['2', '1', '0']
    test_result = _repeated_capability_string_to_list(['2:0'], '')
    assert test_result == ['2', '1', '0']


def test_string_to_list_prefix():
    test_result = _repeated_capability_string_to_list(['ScriptTrigger0-ScriptTrigger2'], 'ScriptTrigger')
    assert test_result == ['0', '1', '2']
    test_result = _repeated_capability_string_to_list(['ScriptTrigger3-ScriptTrigger7'], 'ScriptTrigger')
    assert test_result == ['3', '4', '5', '6', '7']
    test_result = _repeated_capability_string_to_list(['ScriptTrigger3:ScriptTrigger7'], 'ScriptTrigger')
    assert test_result == ['3', '4', '5', '6', '7']
    test_result = _repeated_capability_string_to_list(['ScriptTrigger2-ScriptTrigger0'], 'ScriptTrigger')
    assert test_result == ['2', '1', '0']
    test_result = _repeated_capability_string_to_list(['ScriptTrigger2:ScriptTrigger0'], 'ScriptTrigger')
    assert test_result == ['2', '1', '0']

