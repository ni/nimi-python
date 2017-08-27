import functools
import copy

# Promising for methods: https://docs.python.org/3/library/functools.html#functools.partial

class AttributeViInt32(object):

    def __init__(self, attribute_id, default_channel = ''):
        print("AttributeViInt32.__init__")
        self.attribute_id = attribute_id
        self.default_channel = default_channel

    def __get__(self, obj, objtype):
        print("AttributeViInt32.__get__")
        assert objtype is Session
        return self.get(session, self.default_channel)

    def __set__(self, obj, value):
        print("AttributeViInt32.__set__")
        assert type(obj) is Session
        self.set(obj, self.default_channel, value)

    def get(self, session, channel):
        print("AttributeViInt32.get")
        return session._get_attribute_vi_int32(channel, self.attribute_id)

    def set(self, session, channel, value):
        print("AttributeViInt32.set")
        session._set_attribute_vi_int32(channel, self.attribute_id, value)

class Session(object):

    foo = AttributeViInt32(42)

    def __init__(self):
        print("Session.__init__")
        super().__init__()
        self.foo_value = 0

    def _get_attribute_vi_int32(self, channel, attribute_id):
        print("Session._get_attribute_vi_int32('{0}', {1})".format(channel, attribute_id))
        return self.foo_value

    def _set_attribute_vi_int32(self, channel, attribute_id, value):
        print("****Session._set_attribute_vi_int32('{0}', {1}, {2})".format(channel, attribute_id, value))
        self.foo_value = value

    def channel(self, channel):
        print("Session.channel({0})".format(channel))
        return SessionWithChannels(self, channel)

    def _get_attribute_object(self, name):
        print("Session._get_attribute_object('{0}')".format(name))
        return type(self).__dict__[name]

class SessionWithChannels(object):

    def __init__(self, session, channel):
        print("SessionWithChannels.__init__")
        self.session = session
        self.channel = channel
        self.initialization_complete = True

    def __enter__(self):
        print("SessionWithChannels.__enter__")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("SessionWithChannels.__exit__")

    def __setattr__(self, name, value):
        print("SessionWithChannels.__setattr__({0}, {1})".format(name, value))
        if 'initialization_complete' not in self.__dict__ or name in self.__dict__:
            # Allow normal behavior on __init__ or for attributes that exist.
            return dict.__setattr__(self, name, value)
        else:
            # Get item from session
            print("Forward attribute set to Session")
            return self.session._get_attribute_object(name).set(self.session, self.channel, value)

    def __getattr__(self, name):
        print("SessionWithChannels.__getattr__({0})".format(name))
        if 'initialization_complete' not in self.__dict__ or name in self.__dict__:
            # Allow normal behavior on __init__ or for attributes that exist.
            assert False, 'dead code'
            return dict.__getattr__(self, name)
        else:
            # Get item from session
            print("Forward attribute get to Session")
            return self.session._get_attribute_object(name).get(self.session, self.channel)

session = Session()

print("")
print("Setting attributes")
session.foo = 10
with session.channel(5) as c:
    print("Channel operations")
    c.foo = 1

print("")
print("Getting attributes")
print(session.foo)
with session.channel(2) as c:
    print("Channel operations")
    c.foo = 1
    print (c.foo)
