# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: example2.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='example2.proto',
  package='example',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=b'\n\x0e\x65xample2.proto\x12\x07\x65xample\"\x10\n\x02LD\x12\n\n\x02ip\x18\x01 \x02(\r\"=\n\x03Set\x12\n\n\x02id\x18\x01 \x02(\r\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\x1c\n\x07ld_list\x18\x03 \x03(\x0b\x32\x0b.example.LD'
)




_LD = _descriptor.Descriptor(
  name='LD',
  full_name='example.LD',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip', full_name='example.LD.ip', index=0,
      number=1, type=13, cpp_type=3, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=43,
)


_SET = _descriptor.Descriptor(
  name='Set',
  full_name='example.Set',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='example.Set.id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='example.Set.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ld_list', full_name='example.Set.ld_list', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=45,
  serialized_end=106,
)

_SET.fields_by_name['ld_list'].message_type = _LD
DESCRIPTOR.message_types_by_name['LD'] = _LD
DESCRIPTOR.message_types_by_name['Set'] = _SET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LD = _reflection.GeneratedProtocolMessageType('LD', (_message.Message,), {
  'DESCRIPTOR' : _LD,
  '__module__' : 'example2_pb2'
  # @@protoc_insertion_point(class_scope:example.LD)
  })
_sym_db.RegisterMessage(LD)

Set = _reflection.GeneratedProtocolMessageType('Set', (_message.Message,), {
  'DESCRIPTOR' : _SET,
  '__module__' : 'example2_pb2'
  # @@protoc_insertion_point(class_scope:example.Set)
  })
_sym_db.RegisterMessage(Set)


# @@protoc_insertion_point(module_scope)
