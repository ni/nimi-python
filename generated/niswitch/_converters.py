from niswitch import visatype


def _timedelta_converter(value, library_type, scaling):
    if str(type(value)).find("'datetime.timedelta'") != -1:
        scaled_value = value.total_seconds() * scaling
    else:
        scaled_value = value

    if not library_type == visatype.ViReal64:  # ctype integer types don't convert to int from float so we need to
        scaled_value = int(scaled_value)

    return library_type(scaled_value)


def timedelta_converter_seconds(value, library_type):
    return _timedelta_converter(value, library_type, 1)


def timedelta_converter_milliseconds(value, library_type):
    return _timedelta_converter(value, library_type, 1000)


def timedelta_converter_microseconds(value, library_type):
    return _timedelta_converter(value, library_type, 1000000)


# This converter is not called from the normal codegen path for function. Instead it is
# call from init and is a special case. Also, it just returns a string rather than a ctype object
def init_with_options_converter(value, encoding):
    if type(value) is str:
        init_with_options_string = value
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
        # First we validate that only allowed keys are in the incoming dictionary
        init_with_options = []
        for k in sorted(value.keys()):
            assert k.lower() in good_keys
            if good_keys[k.lower()] == 'DriverSetup':
                assert isinstance(value[k], dict)
                init_with_options.append('DriverSetup=' + (';'.join([key + ':' + value[k][key] for key in sorted(value[k])])))
            else:
                init_with_options.append(good_keys[k.lower()] + ('=1' if value[k] is True else '=0'))

        init_with_options_string = ','.join(init_with_options)

    return init_with_options_string


# Let's run some tests
def test_init_with_options_converter():
    assert init_with_options_converter('', 'ascii') == ''
    assert init_with_options_converter('Simulate=1', 'ascii') == 'Simulate=1'
    assert init_with_options_converter({'Simulate': True, }, 'ascii') == 'Simulate=1'
    assert init_with_options_converter({'Simulate': False, }, 'ascii') == 'Simulate=0'
    assert init_with_options_converter({'Simulate': True, 'Cache': False}, 'ascii') == 'Cache=0,Simulate=1'
    assert init_with_options_converter({'DriverSetup': {'Model': '5162 (4CH)', 'Bitfile': 'CustomProcessing'}}, 'ascii') == 'DriverSetup=Bitfile:CustomProcessing;Model:5162 (4CH)'
    assert init_with_options_converter({'Simulate': True, 'DriverSetup': {'Model': '5162 (4CH)', 'Bitfile': 'CustomProcessing'}}, 'ascii') == 'DriverSetup=Bitfile:CustomProcessing;Model:5162 (4CH),Simulate=1'

