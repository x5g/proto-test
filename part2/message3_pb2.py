# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message3.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='message3.proto',
  package='message',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=b'\n\x0emessage3.proto\x12\x07message\"\x81\x01\n\x04Test\x12\r\n\x05label\x18\x01 \x02(\t\x12\x10\n\x04type\x18\x02 \x01(\x05:\x02\x37\x37\x12\x0c\n\x04reps\x18\x03 \x03(\x03\x12,\n\nsomebutton\x18\x04 \x02(\n2\x18.message.Test.Somebutton\x1a\x1c\n\nSomebutton\x12\x0e\n\x06\x62utton\x18\x05 \x02(\t'
)




_TEST_SOMEBUTTON = _descriptor.Descriptor(
  name='Somebutton',
  full_name='message.Test.Somebutton',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='button', full_name='message.Test.Somebutton.button', index=0,
      number=5, type=9, cpp_type=9, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=129,
  serialized_end=157,
)

_TEST = _descriptor.Descriptor(
  name='Test',
  full_name='message.Test',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='label', full_name='message.Test.label', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='message.Test.type', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=77,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reps', full_name='message.Test.reps', index=2,
      number=3, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='somebutton', full_name='message.Test.somebutton', index=3,
      number=4, type=10, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TEST_SOMEBUTTON, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=157,
)

_TEST_SOMEBUTTON.containing_type = _TEST
_TEST.fields_by_name['somebutton'].message_type = _TEST_SOMEBUTTON
DESCRIPTOR.message_types_by_name['Test'] = _TEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Test = _reflection.GeneratedProtocolMessageType('Test', (_message.Message,), {

  'Somebutton' : _reflection.GeneratedProtocolMessageType('Somebutton', (_message.Message,), {
    'DESCRIPTOR' : _TEST_SOMEBUTTON,
    '__module__' : 'message3_pb2'
    # @@protoc_insertion_point(class_scope:message.Test.Somebutton)
    })
  ,
  'DESCRIPTOR' : _TEST,
  '__module__' : 'message3_pb2'
  # @@protoc_insertion_point(class_scope:message.Test)
  })
_sym_db.RegisterMessage(Test)
_sym_db.RegisterMessage(Test.Somebutton)


# @@protoc_insertion_point(module_scope)
