import grpc
import nitlsconfig.channel_tag
import pytest


@pytest.fixture
def nitls_tagged_channel():
    """A real gRPC channel tagged the way nitlsconfig.create_grpc_device_channel tags one.

    nitlsconfig.create_grpc_device_channel itself requires the nitlsconfig library to be
    installed on the system in order to access the CLI. As a result, we are unable to directly
    leverage it in our unit tests. But, this can at least allow us to unit-test our code
    that relies on channels being created from nitlsconfig.create_grpc_device_channel.
    """
    target = 'localhost:31763'
    with grpc.insecure_channel(target) as channel:
        nitlsconfig.channel_tag.tag_channel_target(channel, target)
        assert nitlsconfig.channel_tag.is_nitls_channel(channel), 'nitlsconfig no longer recognizes a channel it tagged'
        yield channel
