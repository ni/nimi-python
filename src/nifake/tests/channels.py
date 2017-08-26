import functools

# Promising for methods: https://docs.python.org/3/library/functools.html#functools.partial

class AttributeViInt32(object):

    def __init__(self, attribute_id, channel = ''):
        print("AttributeViInt32.__init__")
        self.attribute_id = attribute_id
        self.channel = channel

    def __get__(self, obj, objtype):
        print("AttributeViInt32.__get__")
        assert objtype is Session
        return obj._get_attribute_vi_int32(self.channel, self.attribute_id)

    def __set__(self, obj, value):
        print("AttributeViInt32.__set__")
        obj._set_attribute_vi_int32(self.channel, self.attribute_id, value)


class Session(object):

    foo = AttributeViInt32(55)

    def __init__(self):
        print("Session.__init__")
        self.foo_value = 0

    def _get_attribute_vi_int32(self, channel, attribute_id):
        print("Session._get_attribute_vi_int32({0}, {1})".format(channel, attribute_id))
        return self.foo_value

    def _set_attribute_vi_int32(self, channel, attribute_id, value):
        print("Session._set_attribute_vi_int32({0}, {1}, {2})".format(channel, attribute_id, value))
        self.foo_value = value

    def channel(self, channel):
        print("Session.channel({0})".format(channel))
        return SessionWithChannels(self, channel)


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
        if not self.__dict__.has_key('initialization_complete') or self.__dict__.has_key(name):
            # Allow normal behavior on __init__ or for attributes that exist.
            return dict.__setattr__(self, name, value)
        else:
            # Get item from session
            print("Forward attribute set to main Session")
            return setattr(self.session, name, value)
            #return self.session.__setattr__(name, value)

    def __getattr__(self, name):
        print("SessionWithChannels.__getattr__({0})".format(name))
        if not self.__dict__.has_key('initialization_complete') or self.__dict__.has_key(name):
            # Allow normal behavior on __init__ or for attributes that exist.
            return dict.__getattr__(self, name)
        else:
            # Get item from session
            print("Forward attribute get to main Session")
            return getattr(self.session, name)
            #return self.session.dict[name].__get__(self.session, type(self.session))


session = Session()
print(session.foo)
session.foo = 10
print(session.foo)
with session.channel(5) as c:
    print("Channel operations")
    c.foo = 5
    print (c.foo)

