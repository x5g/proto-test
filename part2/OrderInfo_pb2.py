# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: OrderInfo.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='OrderInfo.proto',
  package='com.pinkpig.entity.protobuf',
  syntax='proto3',
  serialized_options=b'B\016OrderInfoProto',
  serialized_pb=b'\n\x0fOrderInfo.proto\x12\x1b\x63om.pinkpig.entity.protobuf\"\x9b\x02\n\tOrderInfo\x12\x0f\n\x07orderId\x18\x01 \x01(\t\x12\x0e\n\x06userId\x18\x02 \x01(\t\x12\x12\n\norderPrice\x18\x03 \x01(\x01\x12\x15\n\rdeliveryPrice\x18\x04 \x01(\x01\x12\x15\n\rdiscountPrice\x18\x05 \x01(\x01\x12\x15\n\rorderDatetime\x18\x06 \x01(\t\x12\x11\n\tpayMethod\x18\x07 \x01(\t\x12\x13\n\x0bpayDatetime\x18\x08 \x01(\t\x12\x16\n\x0e\x64\x65liveryMethod\x18\t \x01(\t\x12\x14\n\x0creceiverName\x18\n \x01(\t\x12\x17\n\x0freceiverAddress\x18\x0b \x01(\t\x12\x15\n\rreceiverPhone\x18\x0c \x01(\t\x12\x0e\n\x06remark\x18\x63 \x01(\tB\x10\x42\x0eOrderInfoProtob\x06proto3'
)




_ORDERINFO = _descriptor.Descriptor(
  name='OrderInfo',
  full_name='com.pinkpig.entity.protobuf.OrderInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='orderId', full_name='com.pinkpig.entity.protobuf.OrderInfo.orderId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userId', full_name='com.pinkpig.entity.protobuf.OrderInfo.userId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orderPrice', full_name='com.pinkpig.entity.protobuf.OrderInfo.orderPrice', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deliveryPrice', full_name='com.pinkpig.entity.protobuf.OrderInfo.deliveryPrice', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='discountPrice', full_name='com.pinkpig.entity.protobuf.OrderInfo.discountPrice', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orderDatetime', full_name='com.pinkpig.entity.protobuf.OrderInfo.orderDatetime', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payMethod', full_name='com.pinkpig.entity.protobuf.OrderInfo.payMethod', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payDatetime', full_name='com.pinkpig.entity.protobuf.OrderInfo.payDatetime', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deliveryMethod', full_name='com.pinkpig.entity.protobuf.OrderInfo.deliveryMethod', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='receiverName', full_name='com.pinkpig.entity.protobuf.OrderInfo.receiverName', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='receiverAddress', full_name='com.pinkpig.entity.protobuf.OrderInfo.receiverAddress', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='receiverPhone', full_name='com.pinkpig.entity.protobuf.OrderInfo.receiverPhone', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remark', full_name='com.pinkpig.entity.protobuf.OrderInfo.remark', index=12,
      number=99, type=9, cpp_type=9, label=1,
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
  serialized_start=49,
  serialized_end=332,
)

DESCRIPTOR.message_types_by_name['OrderInfo'] = _ORDERINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OrderInfo = _reflection.GeneratedProtocolMessageType('OrderInfo', (_message.Message,), {
  'DESCRIPTOR' : _ORDERINFO,
  '__module__' : 'OrderInfo_pb2'
  # @@protoc_insertion_point(class_scope:com.pinkpig.entity.protobuf.OrderInfo)
  })
_sym_db.RegisterMessage(OrderInfo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
