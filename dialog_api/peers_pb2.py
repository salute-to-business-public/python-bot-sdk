# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: peers.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from . import definitions_pb2 as definitions__pb2
from .scalapb import scalapb_pb2 as scalapb_dot_scalapb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='peers.proto',
  package='dialog',
  syntax='proto3',
  serialized_options=b'\n\024im.dlg.grpc.servicesZ\006dialog',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0bpeers.proto\x12\x06\x64ialog\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x11\x64\x65\x66initions.proto\x1a\x15scalapb/scalapb.proto\"\x8d\x01\n\x04Peer\x12-\n\x04type\x18\x01 \x01(\x0e\x32\x10.dialog.PeerTypeB\r\x8a\xea\x30\t\n\x07visible\x12\x19\n\x02id\x18\x02 \x01(\x05\x42\r\x8a\xea\x30\t\n\x07visible\x12;\n\x06str_id\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValueB\r\x8a\xea\x30\t\n\x07visible\"\xb3\x01\n\x07OutPeer\x12-\n\x04type\x18\x01 \x01(\x0e\x32\x10.dialog.PeerTypeB\r\x8a\xea\x30\t\n\x07visible\x12\x19\n\x02id\x18\x02 \x01(\x05\x42\r\x8a\xea\x30\t\n\x07visible\x12!\n\x0b\x61\x63\x63\x65ss_hash\x18\x03 \x01(\x03\x42\x0c\x8a\xea\x30\x08\n\x06\x64\x61nger\x12;\n\x06str_id\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValueB\r\x8a\xea\x30\t\n\x07visible\"L\n\x0bUserOutPeer\x12\x1a\n\x03uid\x18\x01 \x01(\x05\x42\r\x8a\xea\x30\t\n\x07visible\x12!\n\x0b\x61\x63\x63\x65ss_hash\x18\x02 \x01(\x03\x42\x0c\x8a\xea\x30\x08\n\x06\x64\x61nger\"R\n\x0cGroupOutPeer\x12\x1f\n\x08group_id\x18\x01 \x01(\x05\x42\r\x8a\xea\x30\t\n\x07visible\x12!\n\x0b\x61\x63\x63\x65ss_hash\x18\x02 \x01(\x03\x42\x0c\x8a\xea\x30\x08\n\x06\x64\x61nger\"T\n\rThreadOutPeer\x12 \n\tthread_id\x18\x01 \x01(\x05\x42\r\x8a\xea\x30\t\n\x07visible\x12!\n\x0b\x61\x63\x63\x65ss_hash\x18\x02 \x01(\x03\x42\x0c\x8a\xea\x30\x08\n\x06\x64\x61nger*\x90\x01\n\x08PeerType\x12\x14\n\x10PEERTYPE_UNKNOWN\x10\x00\x12\x14\n\x10PEERTYPE_PRIVATE\x10\x01\x12\x12\n\x0ePEERTYPE_GROUP\x10\x02\x12\x1d\n\x19PEERTYPE_ENCRYPTEDPRIVATE\x10\x03\x12\x10\n\x0cPEERTYPE_SIP\x10\x04\x12\x13\n\x0fPEERTYPE_THREAD\x10\x05\x42\x1e\n\x14im.dlg.grpc.servicesZ\x06\x64ialogb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,definitions__pb2.DESCRIPTOR,scalapb_dot_scalapb__pb2.DESCRIPTOR,])

_PEERTYPE = _descriptor.EnumDescriptor(
  name='PeerType',
  full_name='dialog.PeerType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PEERTYPE_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PEERTYPE_PRIVATE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PEERTYPE_GROUP', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PEERTYPE_ENCRYPTEDPRIVATE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PEERTYPE_SIP', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PEERTYPE_THREAD', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=672,
  serialized_end=816,
)
_sym_db.RegisterEnumDescriptor(_PEERTYPE)

PeerType = enum_type_wrapper.EnumTypeWrapper(_PEERTYPE)
PEERTYPE_UNKNOWN = 0
PEERTYPE_PRIVATE = 1
PEERTYPE_GROUP = 2
PEERTYPE_ENCRYPTEDPRIVATE = 3
PEERTYPE_SIP = 4
PEERTYPE_THREAD = 5



_PEER = _descriptor.Descriptor(
  name='Peer',
  full_name='dialog.Peer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='dialog.Peer.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\t\n\007visible', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='dialog.Peer.id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\t\n\007visible', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='str_id', full_name='dialog.Peer.str_id', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\t\n\007visible', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=98,
  serialized_end=239,
)


_OUTPEER = _descriptor.Descriptor(
  name='OutPeer',
  full_name='dialog.OutPeer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='dialog.OutPeer.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\t\n\007visible', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='dialog.OutPeer.id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\t\n\007visible', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='access_hash', full_name='dialog.OutPeer.access_hash', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\010\n\006danger', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='str_id', full_name='dialog.OutPeer.str_id', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\t\n\007visible', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=242,
  serialized_end=421,
)


_USEROUTPEER = _descriptor.Descriptor(
  name='UserOutPeer',
  full_name='dialog.UserOutPeer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='dialog.UserOutPeer.uid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\t\n\007visible', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='access_hash', full_name='dialog.UserOutPeer.access_hash', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\010\n\006danger', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=423,
  serialized_end=499,
)


_GROUPOUTPEER = _descriptor.Descriptor(
  name='GroupOutPeer',
  full_name='dialog.GroupOutPeer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='group_id', full_name='dialog.GroupOutPeer.group_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\t\n\007visible', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='access_hash', full_name='dialog.GroupOutPeer.access_hash', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\010\n\006danger', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=501,
  serialized_end=583,
)


_THREADOUTPEER = _descriptor.Descriptor(
  name='ThreadOutPeer',
  full_name='dialog.ThreadOutPeer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='thread_id', full_name='dialog.ThreadOutPeer.thread_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\t\n\007visible', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='access_hash', full_name='dialog.ThreadOutPeer.access_hash', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\010\n\006danger', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=585,
  serialized_end=669,
)

_PEER.fields_by_name['type'].enum_type = _PEERTYPE
_PEER.fields_by_name['str_id'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_OUTPEER.fields_by_name['type'].enum_type = _PEERTYPE
_OUTPEER.fields_by_name['str_id'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
DESCRIPTOR.message_types_by_name['Peer'] = _PEER
DESCRIPTOR.message_types_by_name['OutPeer'] = _OUTPEER
DESCRIPTOR.message_types_by_name['UserOutPeer'] = _USEROUTPEER
DESCRIPTOR.message_types_by_name['GroupOutPeer'] = _GROUPOUTPEER
DESCRIPTOR.message_types_by_name['ThreadOutPeer'] = _THREADOUTPEER
DESCRIPTOR.enum_types_by_name['PeerType'] = _PEERTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Peer = _reflection.GeneratedProtocolMessageType('Peer', (_message.Message,), {
  'DESCRIPTOR' : _PEER,
  '__module__' : 'peers_pb2'
  # @@protoc_insertion_point(class_scope:dialog.Peer)
  })
_sym_db.RegisterMessage(Peer)

OutPeer = _reflection.GeneratedProtocolMessageType('OutPeer', (_message.Message,), {
  'DESCRIPTOR' : _OUTPEER,
  '__module__' : 'peers_pb2'
  # @@protoc_insertion_point(class_scope:dialog.OutPeer)
  })
_sym_db.RegisterMessage(OutPeer)

UserOutPeer = _reflection.GeneratedProtocolMessageType('UserOutPeer', (_message.Message,), {
  'DESCRIPTOR' : _USEROUTPEER,
  '__module__' : 'peers_pb2'
  # @@protoc_insertion_point(class_scope:dialog.UserOutPeer)
  })
_sym_db.RegisterMessage(UserOutPeer)

GroupOutPeer = _reflection.GeneratedProtocolMessageType('GroupOutPeer', (_message.Message,), {
  'DESCRIPTOR' : _GROUPOUTPEER,
  '__module__' : 'peers_pb2'
  # @@protoc_insertion_point(class_scope:dialog.GroupOutPeer)
  })
_sym_db.RegisterMessage(GroupOutPeer)

ThreadOutPeer = _reflection.GeneratedProtocolMessageType('ThreadOutPeer', (_message.Message,), {
  'DESCRIPTOR' : _THREADOUTPEER,
  '__module__' : 'peers_pb2'
  # @@protoc_insertion_point(class_scope:dialog.ThreadOutPeer)
  })
_sym_db.RegisterMessage(ThreadOutPeer)


DESCRIPTOR._options = None
_PEER.fields_by_name['type']._options = None
_PEER.fields_by_name['id']._options = None
_PEER.fields_by_name['str_id']._options = None
_OUTPEER.fields_by_name['type']._options = None
_OUTPEER.fields_by_name['id']._options = None
_OUTPEER.fields_by_name['access_hash']._options = None
_OUTPEER.fields_by_name['str_id']._options = None
_USEROUTPEER.fields_by_name['uid']._options = None
_USEROUTPEER.fields_by_name['access_hash']._options = None
_GROUPOUTPEER.fields_by_name['group_id']._options = None
_GROUPOUTPEER.fields_by_name['access_hash']._options = None
_THREADOUTPEER.fields_by_name['thread_id']._options = None
_THREADOUTPEER.fields_by_name['access_hash']._options = None
# @@protoc_insertion_point(module_scope)