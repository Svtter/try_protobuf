# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='test.proto',
  package='lm',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=b'\n\ntest.proto\x12\x02lm\"2\n\nhelloworld\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0b\n\x03str\x18\x02 \x02(\t\x12\x0b\n\x03opt\x18\x03 \x01(\x05'
)




_HELLOWORLD = _descriptor.Descriptor(
  name='helloworld',
  full_name='lm.helloworld',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='lm.helloworld.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='str', full_name='lm.helloworld.str', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='opt', full_name='lm.helloworld.opt', index=2,
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
  serialized_start=18,
  serialized_end=68,
)

DESCRIPTOR.message_types_by_name['helloworld'] = _HELLOWORLD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

helloworld = _reflection.GeneratedProtocolMessageType('helloworld', (_message.Message,), {
  'DESCRIPTOR' : _HELLOWORLD,
  '__module__' : 'test_pb2'
  # @@protoc_insertion_point(class_scope:lm.helloworld)
  })
_sym_db.RegisterMessage(helloworld)


# @@protoc_insertion_point(module_scope)
