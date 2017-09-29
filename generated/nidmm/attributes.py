# -*- coding: utf-8 -*-
# This file was generated


class Attribute(object):
    '''Base class for all typed attributes.'''

    def __init__(self, attribute_id):
        self._attribute_id = attribute_id


class AttributeViInt32(Attribute):

    def __get__(self, session, session_type):
        return session._get_attribute_vi_int32(self._attribute_id)

    def __set__(self, session, value):
        session._set_attribute_vi_int32(self._attribute_id, value)


class AttributeViReal64(Attribute):

    def __get__(self, session, session_type):
        return session._get_attribute_vi_real64(self._attribute_id)

    def __set__(self, session, value):
        session._set_attribute_vi_real64(self._attribute_id, value)


class AttributeViString(Attribute):

    def __get__(self, session, session_type):
        return session._get_attribute_vi_string(self._attribute_id)

    def __set__(self, session, value):
        session._set_attribute_vi_string(self._attribute_id, value)


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
            raise TypeError('must be nidmm.' + str(self._attribute_type.__name__) + ' not ' + str(type(value).__name__))
        return self._underlying_attribute.__set__(session, value.value)


