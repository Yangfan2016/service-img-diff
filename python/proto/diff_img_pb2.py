# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/diff-img.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/diff-img.proto',
  package='Diff',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14proto/diff-img.proto\x12\x04\x44iff\",\n\x0b\x44iffRequest\x12\r\n\x05\x66irst\x18\x01 \x01(\t\x12\x0e\n\x06second\x18\x02 \x01(\t\")\n\x0c\x44iffResponse\x12\x0b\n\x03res\x18\x01 \x01(\t\x12\x0c\n\x04ssim\x18\x02 \x01(\x02\x32=\n\x07\x44iffImg\x12\x32\n\x07getDiff\x12\x11.Diff.DiffRequest\x1a\x12.Diff.DiffResponse\"\x00\x62\x06proto3'
)




_DIFFREQUEST = _descriptor.Descriptor(
  name='DiffRequest',
  full_name='Diff.DiffRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='first', full_name='Diff.DiffRequest.first', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='second', full_name='Diff.DiffRequest.second', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=30,
  serialized_end=74,
)


_DIFFRESPONSE = _descriptor.Descriptor(
  name='DiffResponse',
  full_name='Diff.DiffResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='Diff.DiffResponse.res', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ssim', full_name='Diff.DiffResponse.ssim', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=76,
  serialized_end=117,
)

DESCRIPTOR.message_types_by_name['DiffRequest'] = _DIFFREQUEST
DESCRIPTOR.message_types_by_name['DiffResponse'] = _DIFFRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DiffRequest = _reflection.GeneratedProtocolMessageType('DiffRequest', (_message.Message,), {
  'DESCRIPTOR' : _DIFFREQUEST,
  '__module__' : 'proto.diff_img_pb2'
  # @@protoc_insertion_point(class_scope:Diff.DiffRequest)
  })
_sym_db.RegisterMessage(DiffRequest)

DiffResponse = _reflection.GeneratedProtocolMessageType('DiffResponse', (_message.Message,), {
  'DESCRIPTOR' : _DIFFRESPONSE,
  '__module__' : 'proto.diff_img_pb2'
  # @@protoc_insertion_point(class_scope:Diff.DiffResponse)
  })
_sym_db.RegisterMessage(DiffResponse)



_DIFFIMG = _descriptor.ServiceDescriptor(
  name='DiffImg',
  full_name='Diff.DiffImg',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=119,
  serialized_end=180,
  methods=[
  _descriptor.MethodDescriptor(
    name='getDiff',
    full_name='Diff.DiffImg.getDiff',
    index=0,
    containing_service=None,
    input_type=_DIFFREQUEST,
    output_type=_DIFFRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DIFFIMG)

DESCRIPTOR.services_by_name['DiffImg'] = _DIFFIMG

# @@protoc_insertion_point(module_scope)