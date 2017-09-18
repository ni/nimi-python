# -*- coding: utf-8 -*-
# This file was generated


class Attribute(object):
    '''Base class for all typed attributes.'''

    def __init__(self, attribute_id, default_channel=''):
        self._attribute_id = attribute_id
        self._default_channel = default_channel

    def __get__(self, obj, objtype):
        return self.get(obj, self._default_channel)

    def __set__(self, obj, value):
        return self.set(obj, self._default_channel, value)


class AttributeViInt32(Attribute):

    def get(self, session, channel):
        return session._get_attribute_vi_int32(channel, self._attribute_id)

    def set(self, session, channel, value):
        session._set_attribute_vi_int32(channel, self._attribute_id, value)


class AttributeViReal64(Attribute):

    def get(self, session, channel):
        return session._get_attribute_vi_real64(channel, self._attribute_id)

    def set(self, session, channel, value):
        session._set_attribute_vi_real64(channel, self._attribute_id, value)


class AttributeViString(Attribute):

    def get(self, session, channel):
        return session._get_attribute_vi_string(channel, self._attribute_id)

    def set(self, session, channel, value):
        session._set_attribute_vi_string(channel, self._attribute_id, value)


class AttributeViBoolean(Attribute):

    def get(self, session, channel):
        return session._get_attribute_vi_boolean(channel, self._attribute_id)

    def set(self, session, channel, value):
        session._set_attribute_vi_boolean(channel, self._attribute_id, value)


class AttributeEnum(object):

    def __init__(self, underlying_attr_type, enum_meta_class, attribute_id, default_channel=''):
        self._underlying_attribute = underlying_attr_type(attribute_id, default_channel)
        self._attribute_type = enum_meta_class
        self._attribute_id = attribute_id
        self._default_channel = default_channel

    def __get__(self, obj, objtype):
        return self._attribute_type(self._underlying_attribute.get(obj, self._default_channel))

    def __set__(self, obj, value):
        if type(value) is not self._attribute_type:
            raise TypeError('must be niswitch.' + str(self._attribute_type.__name__) + ' not ' + str(type(value).__name__))
        return self._underlying_attribute.set(obj, self._default_channel, value.value)


