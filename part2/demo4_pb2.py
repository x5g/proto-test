# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: demo4.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='demo4.proto',
  package='caffe',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=b'\n\x0b\x64\x65mo4.proto\x12\x05\x63\x61\x66\x66\x65\"3\n\x07Student\x12\x0b\n\x03\x61ge\x18\x01 \x02(\x05\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\r\n\x05grade\x18\x03 \x01(\x05\"-\n\x07WorkDay\x12\x10\n\x08isworker\x18\x01 \x02(\x08\x12\x10\n\x08isjiaban\x18\x02 \x02(\x08\"B\n\x07Teacher\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x1c\n\x04work\x18\x02 \x02(\x0b\x32\x0e.caffe.WorkDay\x12\x0b\n\x03\x61ge\x18\x03 \x01(\x05\"S\n\x05\x43lass\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x1b\n\x03stu\x18\x02 \x03(\x0b\x32\x0e.caffe.Student\x12\x1f\n\x07teacher\x18\x03 \x03(\x0b\x32\x0e.caffe.Teacher'
)




_STUDENT = _descriptor.Descriptor(
  name='Student',
  full_name='caffe.Student',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='age', full_name='caffe.Student.age', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='caffe.Student.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='grade', full_name='caffe.Student.grade', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=22,
  serialized_end=73,
)


_WORKDAY = _descriptor.Descriptor(
  name='WorkDay',
  full_name='caffe.WorkDay',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='isworker', full_name='caffe.WorkDay.isworker', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isjiaban', full_name='caffe.WorkDay.isjiaban', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
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
  serialized_start=75,
  serialized_end=120,
)


_TEACHER = _descriptor.Descriptor(
  name='Teacher',
  full_name='caffe.Teacher',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='caffe.Teacher.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='work', full_name='caffe.Teacher.work', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='age', full_name='caffe.Teacher.age', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=122,
  serialized_end=188,
)


_CLASS = _descriptor.Descriptor(
  name='Class',
  full_name='caffe.Class',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='caffe.Class.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stu', full_name='caffe.Class.stu', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='teacher', full_name='caffe.Class.teacher', index=2,
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
  serialized_start=190,
  serialized_end=273,
)

_TEACHER.fields_by_name['work'].message_type = _WORKDAY
_CLASS.fields_by_name['stu'].message_type = _STUDENT
_CLASS.fields_by_name['teacher'].message_type = _TEACHER
DESCRIPTOR.message_types_by_name['Student'] = _STUDENT
DESCRIPTOR.message_types_by_name['WorkDay'] = _WORKDAY
DESCRIPTOR.message_types_by_name['Teacher'] = _TEACHER
DESCRIPTOR.message_types_by_name['Class'] = _CLASS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Student = _reflection.GeneratedProtocolMessageType('Student', (_message.Message,), {
  'DESCRIPTOR' : _STUDENT,
  '__module__' : 'demo4_pb2'
  # @@protoc_insertion_point(class_scope:caffe.Student)
  })
_sym_db.RegisterMessage(Student)

WorkDay = _reflection.GeneratedProtocolMessageType('WorkDay', (_message.Message,), {
  'DESCRIPTOR' : _WORKDAY,
  '__module__' : 'demo4_pb2'
  # @@protoc_insertion_point(class_scope:caffe.WorkDay)
  })
_sym_db.RegisterMessage(WorkDay)

Teacher = _reflection.GeneratedProtocolMessageType('Teacher', (_message.Message,), {
  'DESCRIPTOR' : _TEACHER,
  '__module__' : 'demo4_pb2'
  # @@protoc_insertion_point(class_scope:caffe.Teacher)
  })
_sym_db.RegisterMessage(Teacher)

Class = _reflection.GeneratedProtocolMessageType('Class', (_message.Message,), {
  'DESCRIPTOR' : _CLASS,
  '__module__' : 'demo4_pb2'
  # @@protoc_insertion_point(class_scope:caffe.Class)
  })
_sym_db.RegisterMessage(Class)


# @@protoc_insertion_point(module_scope)
