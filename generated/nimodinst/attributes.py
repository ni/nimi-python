# -*- coding: utf-8 -*-
# This file was generated


class Attribute(object):
    '''Base class for all typed attributes.'''

    def __init__(self, attribute_id):
        self._attribute_id = attribute_id

    def __get__(self, session, session_type):
        return self.get(session, session._default_channel)

    def __set__(self, session, value):
        return self.set(session, session._default_channel, value)


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


class AttributeEnum(AttributeViInt32):

    def __init__(self, attribute_id, enum_meta_class):
        super(AttributeEnum, self).__init__(attribute_id)
        self._attribute_type = enum_meta_class

    def get(self, session, channel):
        return self._attribute_type(super(AttributeEnum, self).get(session, channel))

    def set(self, session, channel, value):
        if type(value) is not self._attribute_type:
            raise TypeError('must be nimodinst.' + str(self._attribute_type.__name__) + ' not ' + str(type(value).__name__))
        return super(AttributeEnum, self).set(session, channel, value.value)
