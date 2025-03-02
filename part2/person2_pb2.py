# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: person2.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='person2.proto',
  package='user',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\rperson2.proto\x12\x04user\"&\n\x08LoveGame\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\"[\n\x08UserInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03\x61ge\x18\x02 \x01(\x05\x12\x1c\n\x04game\x18\x03 \x03(\x0b\x32\x0e.user.LoveGame\x12\x16\n\x03sex\x18\x04 \x01(\x0e\x32\t.user.Sex*\x1b\n\x03Sex\x12\x08\n\x04male\x10\x00\x12\n\n\x06\x66\x65male\x10\x01\x62\x06proto3'
)

_SEX = _descriptor.EnumDescriptor(
  name='Sex',
  full_name='user.Sex',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='male', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='female', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=156,
  serialized_end=183,
)
_sym_db.RegisterEnumDescriptor(_SEX)

Sex = enum_type_wrapper.EnumTypeWrapper(_SEX)
male = 0
female = 1



_LOVEGAME = _descriptor.Descriptor(
  name='LoveGame',
  full_name='user.LoveGame',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='user.LoveGame.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='user.LoveGame.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=23,
  serialized_end=61,
)


_USERINFO = _descriptor.Descriptor(
  name='UserInfo',
  full_name='user.UserInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='user.UserInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='age', full_name='user.UserInfo.age', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='game', full_name='user.UserInfo.game', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sex', full_name='user.UserInfo.sex', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=63,
  serialized_end=154,
)

_USERINFO.fields_by_name['game'].message_type = _LOVEGAME
_USERINFO.fields_by_name['sex'].enum_type = _SEX
DESCRIPTOR.message_types_by_name['LoveGame'] = _LOVEGAME
DESCRIPTOR.message_types_by_name['UserInfo'] = _USERINFO
DESCRIPTOR.enum_types_by_name['Sex'] = _SEX
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LoveGame = _reflection.GeneratedProtocolMessageType('LoveGame', (_message.Message,), {
  'DESCRIPTOR' : _LOVEGAME,
  '__module__' : 'person2_pb2'
  # @@protoc_insertion_point(class_scope:user.LoveGame)
  })
_sym_db.RegisterMessage(LoveGame)

UserInfo = _reflection.GeneratedProtocolMessageType('UserInfo', (_message.Message,), {
  'DESCRIPTOR' : _USERINFO,
  '__module__' : 'person2_pb2'
  # @@protoc_insertion_point(class_scope:user.UserInfo)
  })
_sym_db.RegisterMessage(UserInfo)


# @@protoc_insertion_point(module_scope)
