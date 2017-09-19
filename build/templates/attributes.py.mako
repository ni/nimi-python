<%
# Have to put this in a variable and add it that way because mako keeps thinking it is for it, not for the output file
encoding_tag = '# -*- coding: utf-8 -*-'
%>\
${encoding_tag}
# This file was generated
<%
    module_name = template_parameters['metadata'].config['module_name']
%>\


class Attribute(object):
    '''Base class for all typed attributes.'''

    def __init__(self, attribute_id):
        self._attribute_id = attribute_id

    def __get__(self, session, session_type):
        return self.get(session, session._repeated_capability)

    def __set__(self, session, value):
        return self.set(session, session._repeated_capability, value)


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

    def __init__(self, underlying_attribute_meta_class, enum_meta_class, attribute_id):
        self._underlying_attribute = underlying_attribute_meta_class(attribute_id)
        self._attribute_type = enum_meta_class
        self._attribute_id = attribute_id

    def __get__(self, obj, objtype):
        return self._attribute_type(self._underlying_attribute.get(obj, session._repeated_capability))

    def __set__(self, obj, value):
        if type(value) is not self._attribute_type:
            raise TypeError('must be ${module_name}.' + str(self._attribute_type.__name__) + ' not ' + str(type(value).__name__))
        return self._underlying_attribute.set(obj, session._repeated_capability, value.value)


