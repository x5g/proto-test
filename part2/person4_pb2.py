# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: person4.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='person4.proto',
  package='protobuf_data',
  syntax='proto3',
  serialized_options=b'Z\017.;protobuf_data',
  serialized_pb=b'\n\rperson4.proto\x12\rprotobuf_data\"c\n\x06Person\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03\x61ge\x18\x02 \x01(\x05\x12>\n\x13socialMediaProfiles\x18\x03 \x01(\x0b\x32!.protobuf_data.SocialMediaProfile\"7\n\x12SocialMediaProfile\x12\x10\n\x08linkedin\x18\x01 \x01(\t\x12\x0f\n\x07twitter\x18\x02 \x01(\tB\x11Z\x0f.;protobuf_datab\x06proto3'
)




_PERSON = _descriptor.Descriptor(
  name='Person',
  full_name='protobuf_data.Person',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='protobuf_data.Person.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='age', full_name='protobuf_data.Person.age', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='socialMediaProfiles', full_name='protobuf_data.Person.socialMediaProfiles', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=32,
  serialized_end=131,
)


_SOCIALMEDIAPROFILE = _descriptor.Descriptor(
  name='SocialMediaProfile',
  full_name='protobuf_data.SocialMediaProfile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='linkedin', full_name='protobuf_data.SocialMediaProfile.linkedin', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='twitter', full_name='protobuf_data.SocialMediaProfile.twitter', index=1,
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
  serialized_start=133,
  serialized_end=188,
)

_PERSON.fields_by_name['socialMediaProfiles'].message_type = _SOCIALMEDIAPROFILE
DESCRIPTOR.message_types_by_name['Person'] = _PERSON
DESCRIPTOR.message_types_by_name['SocialMediaProfile'] = _SOCIALMEDIAPROFILE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Person = _reflection.GeneratedProtocolMessageType('Person', (_message.Message,), {
  'DESCRIPTOR' : _PERSON,
  '__module__' : 'person4_pb2'
  # @@protoc_insertion_point(class_scope:protobuf_data.Person)
  })
_sym_db.RegisterMessage(Person)

SocialMediaProfile = _reflection.GeneratedProtocolMessageType('SocialMediaProfile', (_message.Message,), {
  'DESCRIPTOR' : _SOCIALMEDIAPROFILE,
  '__module__' : 'person4_pb2'
  # @@protoc_insertion_point(class_scope:protobuf_data.SocialMediaProfile)
  })
_sym_db.RegisterMessage(SocialMediaProfile)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
