gRPC Support
============

Support for using NI-Digital Pattern Driver over gRPC

.. py:currentmodule:: nidigital



Creating a gRPC channel
-----------------------

Using NI-Digital Pattern Driver over gRPC requires the ``grpc`` extra::

  $ python -m pip install nidigital[grpc]

Every NI-Digital Pattern Driver gRPC session is created from a ``grpc.Channel`` that you build and pass to
:py:class:`nidigital.GrpcSessionOptions`. You own the channel, not the session, so you must
close it after the last session using it is closed.

The recommended way to create a gRPC channel to a remote system running NI gRPC Device Server is
``create_grpc_device_channel`` from the `nitlsconfig <https://pypi.org/project/nitlsconfig/>`_ package,
which the ``grpc`` extra installs for you. It reads the nitlsconfig client configuration installed
with the NI-Digital Pattern Driver runtime and by default will attempt to build an encrypted gRPC channel using mTLS.

Before ``create_grpc_device_channel`` can succeed, you must use NI Hardware Manager to perform a
certificate exchange with the remote system.
See `Managing mTLS <https://www.ni.com/docs/en-US/bundle/hardwaremanager/page/mtls-manage.html>`_ for
additional information.

For example::

  import nidigital
  import nitlsconfig

  with nitlsconfig.create_grpc_device_channel('remote_grpc_device', 31763) as channel:
      options = nidigital.GrpcSessionOptions(channel, '')
      with nidigital.Session('dev1', grpc_options=options) as session:
          # Calls to session over the encrypted channel

.. note:: From NI Hardware Manager, you can disable TLS to make ``create_grpc_device_channel``
    produce an insecure channel.

.. note:: ``create_grpc_device_channel`` also accepts an ``options`` parameter for gRPC channel
    arguments such as ``grpc.ssl_target_name_override``, and a ``retry_policy`` parameter. Channel
    arguments cannot be changed after the channel is built, so they must be supplied here.

.. note:: NI gRPC Device Server must be configured to accept remote connections and to take its
    TLS settings from nitlsconfig. See
    `Bind Address Support <https://github.com/ni/grpc-device#bind-address-support>`_ and
    `NI TLS Config Integration <https://github.com/ni/grpc-device#ni-tls-config-integration>`_ for details.

You can also build the gRPC channel yourself with ``grpc.insecure_channel`` or ``grpc.secure_channel``
if you need full control over how credentials are supplied.


SessionInitializationBehavior
-----------------------------

.. py:class:: SessionInitializationBehavior

    .. py:attribute:: SessionInitializationBehavior.AUTO


        The NI gRPC Device Server will attach to an existing session with the specified name if it exists,
        otherwise the server will initialize a new session.

        .. note:: When using the Session as a context manager and the context exits, the behavior depends on what happened when the constructor
            was called. If it resulted in a new session being initialized on the NI gRPC Device Server, then it will automatically close the
            server session. If it instead attached to an existing session, then it will detach from the server session and leave it open.


    .. py:attribute:: SessionInitializationBehavior.INITIALIZE_SERVER_SESSION


        Require the NI gRPC Device Server to initialize a new session with the specified name.

        .. note:: When using the Session as a context manager and the context exits, it will automatically close the
            server session.


    .. py:attribute:: SessionInitializationBehavior.ATTACH_TO_SERVER_SESSION


        Require the NI gRPC Device Server to attach to an existing session with the specified name.

        .. note:: When using the Session as a context manager and the context exits, it will detach from the server session
            and leave it open.



GrpcSessionOptions
------------------


.. py:class:: GrpcSessionOptions(self, grpc_channel, session_name, initialization_behavior=SessionInitializationBehavior.AUTO)


    Collection of options that specifies session behaviors related to gRPC.

    Creates and returns an object you can pass to a Session constructor.


    :param grpc_channel:


        Specifies the channel to the NI gRPC Device Server.



    :type grpc_channel: grpc.Channel


    :param session_name:


        User-specified name that identifies the driver session on the NI gRPC Device Server.

        This is different from the resource name parameter many APIs take as a separate
        parameter. Specifying a name makes it easy to share sessions across multiple gRPC clients.
        You can use an empty string if you want to always initialize a new session on the server.
        To attach to an existing session, you must specify the session name it was initialized with.



    :type session_name: str


    :param initialization_behavior:


        Specifies whether it is acceptable to initialize a new session or attach to an existing one, or if only one of the behaviors is desired.

        The driver session exists on the NI gRPC Device Server.



    :type initialization_behavior: :py:data:`nidigital.SessionInitializationBehavior`
