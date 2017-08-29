import functools
import copy

class Attribute(object):

    def __init__(self, attribute_id, default_channel = ''):
        #print("Attribute.__init__")
        self.attribute_id = attribute_id
        self.default_channel = default_channel

    def __get__(self, obj, objtype):
        #print("Attribute.__get__")
        assert objtype is Session
        return self.get(session, self.default_channel)

    def __set__(self, obj, value):
        #print("Attribute.__set__")
        assert type(obj) is Session
        self.set(obj, self.default_channel, value)

# TODO: One per type...
class AttributeViInt32(Attribute):

    def get(self, session, channel):
        #print("AttributeViInt32.get")
        return session._get_attribute_vi_int32(channel, self.attribute_id)

    def set(self, session, channel, value):
        #print("AttributeViInt32.set")
        session._set_attribute_vi_int32(channel, self.attribute_id, value)

class Session(object):

    voltage_level = AttributeViInt32(42)

    def __init__(self):
        #print("Session.__init__")
        self.voltage_level_value = 0

    def _get_attribute_vi_int32(self, channel, attribute_id):
        print("Session._get_attribute_vi_int32('{0}', {1})".format(channel, attribute_id))
        return self.voltage_level_value

    def _set_attribute_vi_int32(self, channel, attribute_id, value):
        print("Session._set_attribute_vi_int32('{0}', {1}, {2})".format(channel, attribute_id, value))
        self.voltage_level_value = value

    def channel(self, channel):
        #print("Session.channel({0})".format(channel))
        return SessionWithChannels(self, channel)

    def _get_session_member(self, name):
        #print("Session._get_session_member('{0}')".format(name))
        return type(self).__dict__[name]

    def read_from_channel(self, channel = ''):
        print("Session.read_from_channel('{0}')".format(channel))
        return 5.1

    def read(self):
        print("Session.read()")
        return 3.14159

    def read_temperature(self, sensor, channel = ''):
        print("Session.read_temperature({0}, '{1}')".format(sensor, channel))
        return 30

class SessionWithChannels(object):

    def __init__(self, session, channel):
        #print("SessionWithChannels.__init__")
        self.session = session
        self.channel = channel
        self.initialization_complete = True

    def __enter__(self):
        #print("SessionWithChannels.__enter__")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        #print("SessionWithChannels.__exit__")
        pass

    def __setattr__(self, name, value):
        #print("SessionWithChannels.__setattr__({0}, {1})".format(name, value))
        if 'initialization_complete' not in self.__dict__ or name in self.__dict__:
            # Allow normal behavior on __init__ or for attributes that exist.
            return dict.__setattr__(self, name, value)
        else:
            # Get item from session
            #print("Forward attribute set to Session")
            attr = self.session._get_session_member(name)
            #print(attr)
            if(isinstance(attr, Attribute)):
                return attr.set(self.session, self.channel, value)
            else:
                # invoke function but use self.channel
                return functools.partial(attr, self=self.session, channel=self.channel)

    def __getattr__(self, name):
        #print("SessionWithChannels.__getattr__({0})".format(name))
        if 'initialization_complete' not in self.__dict__ or name in self.__dict__:
            # Allow normal behavior on __init__ or for attributes that exist.
            assert False, 'dead code'
            return dict.__getattr__(self, name)
        else:
            # Get item from session
            #print("Forward attribute get to Session")
            attr = self.session._get_session_member(name)
            #print(attr)
            if(isinstance(attr, Attribute)):
                return attr.get(self.session, self.channel)
            else:
                # invoke function but use self.channel
                return functools.partial(attr, self=self.session, channel=self.channel)

session = Session()

print("")
print("Setting attributes")
session.voltage_level = 10
with session.channel('0,1') as session_with_channel:
    print("Channel operations")
    session_with_channel.voltage_level = 2

print("")
print("Getting attributes")
print(session.voltage_level)
with session.channel('2') as session_with_channel:
    print("Channel operations")
    print (session_with_channel.voltage_level)

print("")
print("Calling method")
print(session.read_from_channel())
print(session.read_from_channel('Potato'))
print(session.read())
with session.channel('3') as session_with_channel:
    print("Channel operations")
    session_with_channel.read_from_channel()

print("")
print("Calling method with more parameters")
print(session.read_temperature(1))
with session.channel('0,1') as session_with_channel:
    # This works:
    print(session_with_channel.read_temperature(sensor=2))
    # This doesn't work, and that's a problem.
    print(session_with_channel.read_temperature(2))

