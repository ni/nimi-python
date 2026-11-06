import nirfsa._converters as _converters
import nirfsa.errors
import nirfsa.session
import pytest


def test_invalid_repeated_capability_error_is_not_defined():
    assert not hasattr(nirfsa.errors, 'InvalidRepeatedCapabilityError')


def test_string_with_multiple_separators_is_passed_through_unchanged():
    assert _converters.convert_repeated_capabilities('calplane::plane1/port::if1') == ['calplane::plane1/port::if1']
    assert _converters.convert_repeated_capabilities('1-2-3') == ['1-2-3']


def test_string_with_prefix_is_passed_through_unchanged():
    assert _converters.convert_repeated_capabilities('plane1', prefix='calplane::') == ['calplane::plane1']
    assert _converters.convert_repeated_capabilities('calplane::plane1', prefix='calplane::') == ['calplane::plane1']


def test_simple_ranges_and_lists_are_still_expanded():
    assert _converters.convert_repeated_capabilities('0-2', prefix='LO') == ['LO0', 'LO1', 'LO2']
    assert _converters.convert_repeated_capabilities('LO0:LO2', prefix='LO') == ['LO0', 'LO1', 'LO2']
    assert _converters.convert_repeated_capabilities('0,1', prefix='LO') == ['LO0', 'LO1']
    assert _converters.convert_repeated_capabilities([0, '1'], prefix='LO') == ['LO0', 'LO1']
    assert _converters.convert_repeated_capabilities(range(2), prefix='LO') == ['LO0', 'LO1']
    assert _converters.convert_repeated_capabilities(None) == []


@pytest.mark.parametrize('invalid_repeated_capability', [1.5, {}, object()])
def test_unsupported_type_raises_type_error(invalid_repeated_capability):
    with pytest.raises(TypeError):
        _converters.convert_repeated_capabilities(invalid_repeated_capability)


def test_session_repeated_capabilities_send_selector_to_driver_as_written():
    session = nirfsa.session._SessionBase(repeated_capability_list=[], all_channels_in_session=None, interpreter=None)
    assert session.ports['if1']._repeated_capability == 'if1'
    assert session.ports['calplane::plane1/port::if1']._repeated_capability == 'calplane::plane1/port::if1'
    assert session.channels['calplane::plane1/port::if1']._repeated_capability == 'calplane::plane1/port::if1'
    assert session.calplanes['plane1']._repeated_capability == 'calplane::plane1'
    assert session.calplanes['plane1'].ports['port::if1']._repeated_capability == 'calplane::plane1/port::if1'
