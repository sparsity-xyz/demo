# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: cometbft/rpc/grpc/v1beta2/types.proto
# Protobuf Python Version: 5.29.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    2,
    '',
    'cometbft/rpc/grpc/v1beta2/types.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cometbft.rpc.grpc.v1beta1 import types_pb2 as cometbft_dot_rpc_dot_grpc_dot_v1beta1_dot_types__pb2
from cometbft.abci.v1beta2 import types_pb2 as cometbft_dot_abci_dot_v1beta2_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%cometbft/rpc/grpc/v1beta2/types.proto\x12\x19\x63ometbft.rpc.grpc.v1beta2\x1a%cometbft/rpc/grpc/v1beta1/types.proto\x1a!cometbft/abci/v1beta2/types.proto\"\xa1\x01\n\x13ResponseBroadcastTx\x12\x41\n\x08\x63heck_tx\x18\x01 \x01(\x0b\x32&.cometbft.abci.v1beta2.ResponseCheckTxR\x07\x63heckTx\x12G\n\ndeliver_tx\x18\x02 \x01(\x0b\x32(.cometbft.abci.v1beta2.ResponseDeliverTxR\tdeliverTx2\xd5\x01\n\x0c\x42roadcastAPI\x12W\n\x04Ping\x12&.cometbft.rpc.grpc.v1beta1.RequestPing\x1a\'.cometbft.rpc.grpc.v1beta1.ResponsePing\x12l\n\x0b\x42roadcastTx\x12-.cometbft.rpc.grpc.v1beta1.RequestBroadcastTx\x1a..cometbft.rpc.grpc.v1beta2.ResponseBroadcastTxB<Z:github.com/cometbft/cometbft/api/cometbft/rpc/grpc/v1beta2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cometbft.rpc.grpc.v1beta2.types_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z:github.com/cometbft/cometbft/api/cometbft/rpc/grpc/v1beta2'
  _globals['_RESPONSEBROADCASTTX']._serialized_start=143
  _globals['_RESPONSEBROADCASTTX']._serialized_end=304
  _globals['_BROADCASTAPI']._serialized_start=307
  _globals['_BROADCASTAPI']._serialized_end=520
# @@protoc_insertion_point(module_scope)
