# -*- coding: utf-8 -*-
# This file was generated

from enum import IntEnum


# This constant specifies the gRPC package and service used by this API.
# MeasurementLink customers should pass this value to the discovery manager to resolve the server instance that provides this interface.
GRPC_SERVICE_INTERFACE = 'nifgen_grpc.NiFgen'


class SessionInitializationBehavior(IntEnum):
    AUTO = 0
    r'''
    Attach to an existing session with the specified name if it exists, otherwise intialize a new session.

    Note:
    If this initializes a new session on the NI gRPC Device Server, then when the Python session goes out of scope,
    it will automatically close the server session. If this attaches to an existing session on the NI gRPC Device Server,
    then when the Python session goes out of scope, it will detach from the server session and leave it open.
    '''
    INITIALIZE_SERVER_SESSION = 1
    r'''
    Require the NI gRPC Device Server to initialize a new session with the specified name.

    Note:
    When the Python session goes out of scope, it will automatically close the server session.
    '''
    ATTACH_TO_SERVER_SESSION = 2
    r'''
    Require the NI gRPC Device Server to attach to an existing session with the specified name.

    Note:
    When the Python session goes out of scope, it will detach from the server session and leave it open.
    '''


class GrpcSessionOptions(object):
    '''Collection of options that specifies session behaviors related to gRPC.'''

    def __init__(self, grpc_channel, session_name, initialization_behavior=SessionInitializationBehavior.AUTO):
        r'''Collection of options that specifies session behaviors related to gRPC.

        Creates and returns an object you can pass to a session constructor.

        Args:
            grpc_channel (grpc.Channel): Specifies the channel to the NI gRPC Device Server.

            session_name (str): Specifies the **session name** to be used in the gRPC Device Server.
                This is different from the resource name parameter many APIs take as a separate
                parameter. Specifying a name makes it easy to share sessions across multiple gRPC
                clients. You can use an empty string if you want to always initialize a new session
                and then close it when the Python session goes out of scope.

            initialization_behavior (enum): Specifies whether it is acceptable to initialize a new
                session or attach to an existing one, or if only one of the behaviors is desired.
                To attach to an existing session, you must specify a non-empty session name.
        '''
        self.grpc_channel = grpc_channel
        self.session_name = session_name
        self.initialization_behavior = initialization_behavior
