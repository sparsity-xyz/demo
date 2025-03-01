# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: cometbft/services/block/v1/block.proto
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
    'cometbft/services/block/v1/block.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cometbft.types.v1 import types_pb2 as cometbft_dot_types_dot_v1_dot_types__pb2
from cometbft.types.v1 import block_pb2 as cometbft_dot_types_dot_v1_dot_block__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&cometbft/services/block/v1/block.proto\x12\x1a\x63ometbft.services.block.v1\x1a\x1d\x63ometbft/types/v1/types.proto\x1a\x1d\x63ometbft/types/v1/block.proto\",\n\x12GetByHeightRequest\x12\x16\n\x06height\x18\x01 \x01(\x03R\x06height\"|\n\x13GetByHeightResponse\x12\x35\n\x08\x62lock_id\x18\x01 \x01(\x0b\x32\x1a.cometbft.types.v1.BlockIDR\x07\x62lockId\x12.\n\x05\x62lock\x18\x02 \x01(\x0b\x32\x18.cometbft.types.v1.BlockR\x05\x62lock\"\x18\n\x16GetLatestHeightRequest\"1\n\x17GetLatestHeightResponse\x12\x16\n\x06height\x18\x01 \x01(\x03R\x06heightB=Z;github.com/cometbft/cometbft/api/cometbft/services/block/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cometbft.services.block.v1.block_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z;github.com/cometbft/cometbft/api/cometbft/services/block/v1'
  _globals['_GETBYHEIGHTREQUEST']._serialized_start=132
  _globals['_GETBYHEIGHTREQUEST']._serialized_end=176
  _globals['_GETBYHEIGHTRESPONSE']._serialized_start=178
  _globals['_GETBYHEIGHTRESPONSE']._serialized_end=302
  _globals['_GETLATESTHEIGHTREQUEST']._serialized_start=304
  _globals['_GETLATESTHEIGHTREQUEST']._serialized_end=328
  _globals['_GETLATESTHEIGHTRESPONSE']._serialized_start=330
  _globals['_GETLATESTHEIGHTRESPONSE']._serialized_end=379
# @@protoc_insertion_point(module_scope)
