# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from proto import diff_img_pb2 as proto_dot_diff__img__pb2


class DiffImgStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getDiff = channel.unary_unary(
                '/Diff.DiffImg/getDiff',
                request_serializer=proto_dot_diff__img__pb2.DiffRequest.SerializeToString,
                response_deserializer=proto_dot_diff__img__pb2.DiffResponse.FromString,
                )


class DiffImgServicer(object):
    """Missing associated documentation comment in .proto file."""

    def getDiff(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DiffImgServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getDiff': grpc.unary_unary_rpc_method_handler(
                    servicer.getDiff,
                    request_deserializer=proto_dot_diff__img__pb2.DiffRequest.FromString,
                    response_serializer=proto_dot_diff__img__pb2.DiffResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Diff.DiffImg', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DiffImg(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def getDiff(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Diff.DiffImg/getDiff',
            proto_dot_diff__img__pb2.DiffRequest.SerializeToString,
            proto_dot_diff__img__pb2.DiffResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
