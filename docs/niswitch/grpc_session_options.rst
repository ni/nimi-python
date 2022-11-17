gRPC Support
============

Support for gRPC used in NI-SWITCH

.. py:currentmodule:: niswitch


Enums
=====


SessionInitializationBehavior
-----------------------------

.. py:class:: SessionInitializationBehavior

    .. py:attribute:: SessionInitializationBehavior.AUTO



        Attach to an existing session with the specified name if it exists, otherwise intialize a new session.

        .. note:: If this initializes a new session on the NI gRPC Device Server, then when the Python session goes out of scope,
            it will automatically close the server session. If this attaches to an existing session on the NI gRPC Device Server,
            then when the Python session goes out of scope, it will detach from the server session and leave it open.

        


    .. py:attribute:: SessionInitializationBehavior.INITIALIZE_SERVER_SESSION



        Require the NI gRPC Device Server to initialize a new session with the specified name.

        .. note:: When the Python session goes out of scope, it will automatically close the server session.

        



    .. py:attribute:: SessionInitializationBehavior.ATTACH_TO_SERVER_SESSION



        Require the NI gRPC Device Server to attach to an existing session with the specified name.

        .. note:: When the Python session goes out of scope, it will detach from the server session and leave it open.

        


Classes
=======


.. py:class:: GrpcSessionOptions(self, grpc_channel, session_name, initialization_behavior=SessionInitializationBehavior.AUTO)

    

    Collection of options that specifies session behaviors related to gRPC.

    Creates and returns an object you can pass to a session constructor.


    :param grpc_channel:
        

        Specifies the channel to the NI gRPC Device Server.

        


    :type grpc_channel: grpc.Channel

    :param session_name:
        

        Specifies the **session name** to be used in the gRPC Device Server.

                This is different from the resource name parameter many APIs take as a separate parameter. Specifying a name makes it easy to share sessions across multiple gRPC clients. You can use an empty string if you want to always initialize a new session and then close it when the Python session goes out of scope.

        


    :type session_name: str

    :param initialization_behavior:
        

        Specifies whether it is acceptable to initialize a new session or attach to an existing one, or if only one of the behaviors is desired. To attach to an existing session, you must specify a non-empty session name.

        


    :type initialization_behavior: enum

