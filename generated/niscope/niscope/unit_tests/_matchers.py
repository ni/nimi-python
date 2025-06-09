# -*- coding: utf-8 -*-
# This file was generated
'''Matcher classes used by unit tests in order to set mock expectations.
These work well with our visatype definitions.
'''

import ctypes
import niscope._visatype as _visatype
import pprint

pp = pprint.PrettyPrinter(indent=4)


# Base classes


class _ScalarMatcher(object):
    def __init__(self, expected_type, expected_value):
        self.expected_type = expected_type
        self.expected_value = expected_value

    def __eq__(self, other):
        if not isinstance(other, self.expected_type):
            print("{}: Unexpected type. Expected: {}. Received: {}".format(self.__class__.__name__, self.expected_type, type(other)))
            return False
        if other.value != self.expected_value:
            print("{}: Unexpected value. Expected: {}. Received: {}".format(self.__class__.__name__, self.expected_value, other.value))
            return False
        return True

    def __repr__(self):
        return '{}({}, {})'.format(self.__class__.__name__, pp.pformat(self.expected_type), pp.pformat(self.expected_value))


class _PointerMatcher(object):
    def __init__(self, expected_type):
        self.expected_type = expected_type

    def __eq__(self, other):
        if not isinstance(other, ctypes.POINTER(self.expected_type)):
            print("Unexpected type. Expected: {}. Received: {}".format(ctypes.POINTER(self.expected_type), type(other)))
            return False
        return True

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, pp.pformat(self.expected_type))


class _BufferMatcher(object):
    def __init__(self, expected_element_type, expected_size_or_value):
        if isinstance(expected_size_or_value, int):
            # Were given the size of the buffer
            self.expected_value = None
            self.expected_size = expected_size_or_value
        else:
            # Were given a list or something that behaves like a list
            self.expected_value = expected_size_or_value
            self.expected_size = len(expected_size_or_value)
        self.expected_type = expected_element_type * self.expected_size
        # Store params for __repr__
        self._expected_element_type = expected_element_type
        self._expected_size_or_value = expected_size_or_value

    def __eq__(self, other):
        if not isinstance(other, self.expected_type):
            # We try to "dereference" this in case it is a pointer and then do the check again. Only then saying they don't match
            try:
                other = other.contents
            except AttributeError:
                pass

            # Because of object lifetimes, we may need to mock the other instance and provide lists instead of the actual array
            if not isinstance(other, self.expected_type) and not isinstance(other, list):
                print("Unexpected type. Expected: {} or {}. Received: {}".format(self.expected_type, list, type(other)))
                return False
        if self.expected_size != len(other):
            print("Unexpected length. Expected: {}. Received: {}".format(self.expected_size, len(other)))
            return False
        if self.expected_value is not None:
            # Can't compare the objects directly because they're different types (one is list, another is ctypes array).
            # Go element by element, which allows for reporting the first index where different values were found.
            for i in range(0, len(self.expected_value)):
                if self.expected_value[i] != other[i]:
                    print("Unexpected value at index {}. Expected: {}. Received: {}".format(i, self.expected_value[i], other[i]))
                    return False
        return True

    def __repr__(self):
        return '{}({}, {})'.format(self.__class__.__name__, pp.pformat(self._expected_element_type), pp.pformat(self._expected_size_or_value))

    def __str__(self):
        ret_str = self.__repr__() + '\n'
        ret_str += '    expected_type  = ' + str(self.expected_type) + '\n'
        ret_str += '    expected_value = ' + str(self.expected_value) + '\n'
        ret_str += '    expected_size  = ' + str(self.expected_size) + '\n'
        return ret_str


# Strings


class ViStringMatcher(object):
    def __init__(self, expected_string_value):
        self.expected_string_value = expected_string_value

    def __eq__(self, other):
        if not isinstance(other, ctypes.Array):
            # We try to "dereference" this in case it is a pointer and then do the check again. Only then saying they don't match
            try:
                other = other.contents
            except AttributeError:
                pass

            if not isinstance(other, ctypes.Array):
                print("Unexpected type. Expected: {}. Received: {}".format(self.expected_type, type(other)))
                return False
        if len(other) < len(self.expected_string_value) + 1:  # +1 for NULL terminating character
            print("Unexpected length in C string. Expected at least: {}. Received {}".format(len(other), len(self.expected_string_value) + 1))
            return False
        if not isinstance(other[0], bytes):
            print("Unexpected type. Not a string. Received: {}".format(type(other[0])))
            return False
        if other.value.decode("ascii") != self.expected_string_value:
            print("Unexpected value. Expected {}. Received: {}".format(self.expected_string_value, other.value.decode))
            return False
        return True

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, pp.pformat(self.expected_string_value))


# Custom Type


def _compare_ctype_structs(expected, actual):
    # From https://stackoverflow.com/questions/20986330/print-all-fields-of-ctypes-structure-with-introspection
    for field in expected._fields_:
        field_name = field[0]
        expected_val = getattr(expected, field_name)
        actual_val = getattr(actual, field_name)
        if expected_val != actual_val:
            print("Unexpected value field {}. Expected: {}. Received: {}".format(field_name, expected_val, actual_val))
            return False
    return True


class CustomTypeMatcher(object):
    def __init__(self, expected_type, expected_value):
        self.expected_type = expected_type
        self.expected_value = expected_value

    def __eq__(self, actual):
        if not isinstance(actual, self.expected_type):
            print("Unexpected type. Expected: {}. Received: {}".format(self.expected_type, type(actual)))
            return False
        return _compare_ctype_structs(self.expected_value, actual)

    def __repr__(self):
        return '{}({}, {})'.format(self.__class__.__name__, pp.pformat(self.expected_type), pp.pformat(self.expected_value))


class CustomTypeBufferMatcher(object):
    def __init__(self, expected_element_type, expected_value):
        self.expected_value = expected_value
        self.expected_size = len(expected_value)
        self.expected_type = expected_element_type * self.expected_size
        self.expected_element_type = expected_element_type

    def __eq__(self, actual):
        if not isinstance(actual, self.expected_type):
            print("Unexpected array type. Expected: {}. Received: {}".format(self.expected_type, type(actual)))
            return False
        if self.expected_size != len(actual):
            print("Unexpected length. Expected: {}. Received: {}".format(self.expected_size, len(actual)))
            return False
        if self.expected_value is not None:
            # Can't compare the objects directly because they're different types (one is list, another is ctypes array).
            # Go element by element, which allows for reporting the first index where different values were found.
            for a, e in zip(actual, self.expected_value):
                if not isinstance(a, self.expected_element_type):
                    print("Unexpected type. Expected: {}. Received: {}".format(self.expected_element_type, type(a)))
                    return False
                if not _compare_ctype_structs(e, a):
                    return False
        return True

    def __repr__(self):
        expected_val_repr = '[' + ', '.join([x.__repr__() for x in self.expected_value]) + ']'
        return '{}({}, {})'.format(self.__class__.__name__, pp.pformat(self.expected_element_type), expected_val_repr)

    def __str__(self):
        ret_str = self.__repr__() + '\n'
        ret_str += '    expected_type = ' + str(self.expected_type) + '\n'
        ret_str += '    expected_size = ' + str(self.expected_size) + '\n'
        return ret_str


# Scalars


class ViBooleanMatcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, _visatype.ViBoolean, 1 if expected_value is True else 0)


class ViSessionMatcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, _visatype.ViSession, expected_value)


class ViInt16Matcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, _visatype.ViInt16, expected_value)


class ViInt32Matcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, _visatype.ViInt32, expected_value)


class ViUInt32Matcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, _visatype.ViUInt32, expected_value)


class ViAttrMatcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, _visatype.ViAttr, expected_value)


class ViInt64Matcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, _visatype.ViInt64, expected_value)


class ViReal64Matcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, _visatype.ViReal64, expected_value)


# Pointers


class ViBooleanPointerMatcher(_PointerMatcher):
    def __init__(self):
        _PointerMatcher.__init__(self, _visatype.ViBoolean)


class ViSessionPointerMatcher(_PointerMatcher):
    def __init__(self):
        _PointerMatcher.__init__(self, _visatype.ViSession)


class ViInt16PointerMatcher(_PointerMatcher):
    def __init__(self):
        _PointerMatcher.__init__(self, _visatype.ViInt16)


class ViInt32PointerMatcher(_PointerMatcher):
    def __init__(self):
        _PointerMatcher.__init__(self, _visatype.ViInt32)


class ViInt64PointerMatcher(_PointerMatcher):
    def __init__(self):
        _PointerMatcher.__init__(self, _visatype.ViInt64)


class ViReal64PointerMatcher(_PointerMatcher):
    def __init__(self):
        _PointerMatcher.__init__(self, _visatype.ViReal64)


# Buffers


class ViBooleanBufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, _visatype.ViBoolean, expected_size_or_value)


class ViCharBufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, _visatype.ViChar, expected_size_or_value)


class ViInt8BufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, _visatype.ViInt8, expected_size_or_value)


class ViInt16BufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, _visatype.ViInt16, expected_size_or_value)


class ViInt32BufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, _visatype.ViInt32, expected_size_or_value)


class ViInt64BufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, _visatype.ViInt64, expected_size_or_value)


class ViReal64BufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, _visatype.ViReal64, expected_size_or_value)


class ViSessionBufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, _visatype.ViSession, expected_size_or_value)



