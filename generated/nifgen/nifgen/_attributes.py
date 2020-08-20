# -*- coding: utf-8 -*-
# This file was generated
import nifgen._converters as _converters

import hightime


class Attribute(object):
    '''Base class for all typed attributes.'''

    def __init__(self, attribute_id):
        self._attribute_id = attribute_id


class AttributeViInt32(Attribute):

    def __get__(self, session, session_type):
        return session._get_attribute_vi_int32(self._attribute_id)

    def __set__(self, session, value):
        session._set_attribute_vi_int32(self._attribute_id, value)


class AttributeViInt32TimeDeltaMilliseconds(Attribute):

    def __get__(self, session, session_type):
        return hightime.timedelta(milliseconds=session._get_attribute_vi_int32(self._attribute_id))

    def __set__(self, session, value):
        session._set_attribute_vi_int32(self._attribute_id, _converters.convert_timedelta_to_milliseconds_int32(value).value)


class AttributeViInt64(Attribute):

    def __get__(self, session, session_type):
        return session._get_attribute_vi_int64(self._attribute_id)

    def __set__(self, session, value):
        session._set_attribute_vi_int64(self._attribute_id, value)


class AttributeViReal64(Attribute):

    def __get__(self, session, session_type):
        return session._get_attribute_vi_real64(self._attribute_id)

    def __set__(self, session, value):
        session._set_attribute_vi_real64(self._attribute_id, value)


class AttributeViReal64TimeDeltaSeconds(Attribute):

    def __get__(self, session, session_type):
        return hightime.timedelta(seconds=session._get_attribute_vi_real64(self._attribute_id))

    def __set__(self, session, value):
        session._set_attribute_vi_real64(self._attribute_id, _converters.convert_timedelta_to_seconds_real64(value).value)


class AttributeViString(Attribute):

    def __get__(self, session, session_type):
        return session._get_attribute_vi_string(self._attribute_id)

    def __set__(self, session, value):
        session._set_attribute_vi_string(self._attribute_id, value)


class AttributeViStringRepeatedCapability(Attribute):

    def __get__(self, session, session_type):
        return session._get_attribute_vi_string(self._attribute_id)

    def __set__(self, session, value):
        session._set_attribute_vi_string(self._attribute_id, _converters.convert_repeated_capabilities_without_prefix(value))


class AttributeViBoolean(Attribute):

    def __get__(self, session, session_type):
        return session._get_attribute_vi_boolean(self._attribute_id)

    def __set__(self, session, value):
        session._set_attribute_vi_boolean(self._attribute_id, value)


class AttributeEnum(object):

    def __init__(self, underlying_attribute_meta_class, enum_meta_class, attribute_id):
        self._underlying_attribute = underlying_attribute_meta_class(attribute_id)
        self._attribute_type = enum_meta_class
        self._attribute_id = attribute_id

    def __get__(self, session, session_type):
        return self._attribute_type(self._underlying_attribute.__get__(session, session_type))

    def __set__(self, session, value):
        if type(value) is not self._attribute_type:
            raise TypeError('must be ' + str(self._attribute_type.__name__) + ' not ' + str(type(value).__name__))
        return self._underlying_attribute.__set__(session, value.value)


# nitclk specific attribute type
class AttributeSessionReference(Attribute):

    def __get__(self, session, session_type):
        # Import here to avoid a circular dependency when initial import happens
        from nifgen.session import SessionReference
        return SessionReference(session._get_attribute_vi_session(self._attribute_id))

    def __set__(self, session, value):
        session._set_attribute_vi_session(self._attribute_id, _converters.convert_to_nitclk_session_number(value))



