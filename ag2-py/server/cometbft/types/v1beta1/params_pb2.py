# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: cometbft/types/v1beta1/params.proto
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
    'cometbft/types/v1beta1/params.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#cometbft/types/v1beta1/params.proto\x12\x16\x63ometbft.types.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto\"\xb0\x02\n\x0f\x43onsensusParams\x12?\n\x05\x62lock\x18\x01 \x01(\x0b\x32#.cometbft.types.v1beta1.BlockParamsB\x04\xc8\xde\x1f\x00R\x05\x62lock\x12H\n\x08\x65vidence\x18\x02 \x01(\x0b\x32&.cometbft.types.v1beta1.EvidenceParamsB\x04\xc8\xde\x1f\x00R\x08\x65vidence\x12K\n\tvalidator\x18\x03 \x01(\x0b\x32\'.cometbft.types.v1beta1.ValidatorParamsB\x04\xc8\xde\x1f\x00R\tvalidator\x12\x45\n\x07version\x18\x04 \x01(\x0b\x32%.cometbft.types.v1beta1.VersionParamsB\x04\xc8\xde\x1f\x00R\x07version\"e\n\x0b\x42lockParams\x12\x1b\n\tmax_bytes\x18\x01 \x01(\x03R\x08maxBytes\x12\x17\n\x07max_gas\x18\x02 \x01(\x03R\x06maxGas\x12 \n\x0ctime_iota_ms\x18\x03 \x01(\x03R\ntimeIotaMs\"\xa9\x01\n\x0e\x45videnceParams\x12+\n\x12max_age_num_blocks\x18\x01 \x01(\x03R\x0fmaxAgeNumBlocks\x12M\n\x10max_age_duration\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01R\x0emaxAgeDuration\x12\x1b\n\tmax_bytes\x18\x03 \x01(\x03R\x08maxBytes\"?\n\x0fValidatorParams\x12\"\n\rpub_key_types\x18\x01 \x03(\tR\x0bpubKeyTypes:\x08\xb8\xa0\x1f\x01\xe8\xa0\x1f\x01\"+\n\rVersionParams\x12\x10\n\x03\x61pp\x18\x01 \x01(\x04R\x03\x61pp:\x08\xb8\xa0\x1f\x01\xe8\xa0\x1f\x01\"Z\n\x0cHashedParams\x12&\n\x0f\x62lock_max_bytes\x18\x01 \x01(\x03R\rblockMaxBytes\x12\"\n\rblock_max_gas\x18\x02 \x01(\x03R\x0b\x62lockMaxGasB=Z7github.com/cometbft/cometbft/api/cometbft/types/v1beta1\xa8\xe2\x1e\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cometbft.types.v1beta1.params_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z7github.com/cometbft/cometbft/api/cometbft/types/v1beta1\250\342\036\001'
  _globals['_CONSENSUSPARAMS'].fields_by_name['block']._loaded_options = None
  _globals['_CONSENSUSPARAMS'].fields_by_name['block']._serialized_options = b'\310\336\037\000'
  _globals['_CONSENSUSPARAMS'].fields_by_name['evidence']._loaded_options = None
  _globals['_CONSENSUSPARAMS'].fields_by_name['evidence']._serialized_options = b'\310\336\037\000'
  _globals['_CONSENSUSPARAMS'].fields_by_name['validator']._loaded_options = None
  _globals['_CONSENSUSPARAMS'].fields_by_name['validator']._serialized_options = b'\310\336\037\000'
  _globals['_CONSENSUSPARAMS'].fields_by_name['version']._loaded_options = None
  _globals['_CONSENSUSPARAMS'].fields_by_name['version']._serialized_options = b'\310\336\037\000'
  _globals['_EVIDENCEPARAMS'].fields_by_name['max_age_duration']._loaded_options = None
  _globals['_EVIDENCEPARAMS'].fields_by_name['max_age_duration']._serialized_options = b'\310\336\037\000\230\337\037\001'
  _globals['_VALIDATORPARAMS']._loaded_options = None
  _globals['_VALIDATORPARAMS']._serialized_options = b'\270\240\037\001\350\240\037\001'
  _globals['_VERSIONPARAMS']._loaded_options = None
  _globals['_VERSIONPARAMS']._serialized_options = b'\270\240\037\001\350\240\037\001'
  _globals['_CONSENSUSPARAMS']._serialized_start=118
  _globals['_CONSENSUSPARAMS']._serialized_end=422
  _globals['_BLOCKPARAMS']._serialized_start=424
  _globals['_BLOCKPARAMS']._serialized_end=525
  _globals['_EVIDENCEPARAMS']._serialized_start=528
  _globals['_EVIDENCEPARAMS']._serialized_end=697
  _globals['_VALIDATORPARAMS']._serialized_start=699
  _globals['_VALIDATORPARAMS']._serialized_end=762
  _globals['_VERSIONPARAMS']._serialized_start=764
  _globals['_VERSIONPARAMS']._serialized_end=807
  _globals['_HASHEDPARAMS']._serialized_start=809
  _globals['_HASHEDPARAMS']._serialized_end=899
# @@protoc_insertion_point(module_scope)
