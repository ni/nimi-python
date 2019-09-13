${template_parameters['encoding_tag']}
# This file was generated
<%
    module_name = template_parameters['metadata'].config['module_name']
    attribute_classes_used = template_parameters['metadata'].config['attribute_classes_used']
%>\


class Attribute(object):
    '''Base class for all typed attributes.'''

    def __init__(self, attribute_id):
        self._attribute_id = attribute_id


% if 'AttributeViInt32' in attribute_classes_used:
class AttributeViInt32(Attribute):

    def __get__(self, session, session_type):
        return session._get_attribute_vi_int32(self._attribute_id)

    def __set__(self, session, value):
        session._set_attribute_vi_int32(self._attribute_id, value)


% endif
% if 'AttributeViInt32TimeDeltaSeconds' in attribute_classes_used:
class AttributeViInt32TimeDeltaSeconds(Attribute):

    def __get__(self, session, session_type):
        import datetime
        return datetime.timedelta(seconds=session._get_attribute_vi_int32(self._attribute_id))

    def __set__(self, session, value):
        import ${module_name}._converters as _converters
        session._set_attribute_vi_int32(self._attribute_id, _converters.convert_timedelta_to_seconds(value, int))


% endif
% if 'AttributeViInt32TimeDeltaMilliseconds' in attribute_classes_used:
class AttributeViInt32TimeDeltaMilliseconds(Attribute):

    def __get__(self, session, session_type):
        import datetime
        return datetime.timedelta(milliseconds=session._get_attribute_vi_int32(self._attribute_id))

    def __set__(self, session, value):
        import ${module_name}._converters as _converters
        session._set_attribute_vi_int32(self._attribute_id, _converters.convert_timedelta_to_milliseconds(value, int))


% endif
% if 'AttributeViInt64' in attribute_classes_used:
class AttributeViInt64(Attribute):

    def __get__(self, session, session_type):
        return session._get_attribute_vi_int64(self._attribute_id)

    def __set__(self, session, value):
        session._set_attribute_vi_int64(self._attribute_id, value)


% endif
% if 'AttributeViReal64' in attribute_classes_used:
class AttributeViReal64(Attribute):

    def __get__(self, session, session_type):
        return session._get_attribute_vi_real64(self._attribute_id)

    def __set__(self, session, value):
        session._set_attribute_vi_real64(self._attribute_id, value)


% endif
% if 'AttributeViReal64TimeDeltaSeconds' in attribute_classes_used:
class AttributeViReal64TimeDeltaSeconds(Attribute):

    def __get__(self, session, session_type):
        import datetime
        return datetime.timedelta(seconds=session._get_attribute_vi_real64(self._attribute_id))

    def __set__(self, session, value):
        import ${module_name}._converters as _converters
        session._set_attribute_vi_real64(self._attribute_id, _converters.convert_timedelta_to_seconds(value, float))


% endif
% if 'AttributeViReal64TimeDeltaMilliseconds' in attribute_classes_used:
class AttributeViReal64TimeDeltaMilliseconds(Attribute):

    def __get__(self, session, session_type):
        import datetime
        return datetime.timedelta(milliseconds=session._get_attribute_vi_real64(self._attribute_id))

    def __set__(self, session, value):
        import ${module_name}._converters as _converters
        session._set_attribute_vi_real64(self._attribute_id, _converters.convert_timedelta_to_milliseconds(value, float))


% endif
% if 'AttributeViString' in attribute_classes_used:
class AttributeViString(Attribute):

    def __get__(self, session, session_type):
        return session._get_attribute_vi_string(self._attribute_id)

    def __set__(self, session, value):
        session._set_attribute_vi_string(self._attribute_id, value)


% endif
% if 'AttributeViBoolean' in attribute_classes_used:
class AttributeViBoolean(Attribute):

    def __get__(self, session, session_type):
        return session._get_attribute_vi_boolean(self._attribute_id)

    def __set__(self, session, value):
        session._set_attribute_vi_boolean(self._attribute_id, value)


% endif
% if 'AttributeEnum' in attribute_classes_used:
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


% endif

