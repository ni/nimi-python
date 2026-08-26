import grpc
import nitlsconfig.channel_tag
import pytest


@pytest.fixture
def nitls_tagged_channel():
    """A real gRPC channel tagged the way nitlsconfig.create_grpc_device_channel tags one.

    The factory itself shells out to the NI-installed nitlsconfig CLI, so it cannot run here.
    """
    target = 'localhost:31763'
    with grpc.insecure_channel(target) as channel:
        nitlsconfig.channel_tag.tag_channel_target(channel, target)
        assert nitlsconfig.channel_tag.is_nitls_channel(channel), 'nitlsconfig no longer recognizes a channel it tagged'
        yield channel
