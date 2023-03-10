# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import greeting_pb2 as greeting__pb2


class InventoryServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateBook = channel.unary_unary(
                '/InventoryService/CreateBook',
                request_serializer=greeting__pb2.CreateRequest.SerializeToString,
                response_deserializer=greeting__pb2.CreateResponse.FromString,
                )
        self.GetBook = channel.unary_unary(
                '/InventoryService/GetBook',
                request_serializer=greeting__pb2.GetRequest.SerializeToString,
                response_deserializer=greeting__pb2.GetResponse.FromString,
                )


class InventoryServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateBook(self, request, context):
        """Create a book
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBook(self, request, context):
        """Get a book - given ISBN, retrieve book details
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InventoryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateBook': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateBook,
                    request_deserializer=greeting__pb2.CreateRequest.FromString,
                    response_serializer=greeting__pb2.CreateResponse.SerializeToString,
            ),
            'GetBook': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBook,
                    request_deserializer=greeting__pb2.GetRequest.FromString,
                    response_serializer=greeting__pb2.GetResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'InventoryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class InventoryService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateBook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/InventoryService/CreateBook',
            greeting__pb2.CreateRequest.SerializeToString,
            greeting__pb2.CreateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/InventoryService/GetBook',
            greeting__pb2.GetRequest.SerializeToString,
            greeting__pb2.GetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
