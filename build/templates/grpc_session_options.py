# -*- coding: utf-8 -*-
from enum import IntEnum


class SessionInitializationBehavior(IntEnum):
    UNSPECIFIED = 0
    r'''
    It is acceptable to either initialize a new session or attach to an existing one.
    '''
    INITIALIZE_NEW = 1
    r'''
    This requires the NI gRPC Device Server to initialize a new session with the specified name.
    '''
    ATTACH_TO_EXISTING = 2
    r'''
    This requires the NI gRPC Device Server to attach to an existing session with the specified name.
    '''


class GrpcSessionOptions(object):
    '''Collection of options that specifies session behaviors related to gRPC.'''

    def __init__(self, grpc_channel, session_name, initialization_behavior=SessionInitializationBehavior.UNSPECIFIED, auto_close_grpc_session=True):
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

            auto_close_grpc_session (bool): Specifies whether to have the NI gRPC Device Server close
                the session when the Python session goes out of scope.
        '''
        self.grpc_channel = grpc_channel
        self.session_name = session_name
        self.initialization_behavior = initialization_behavior
        self.auto_close_grpc_session = auto_close_grpc_session
