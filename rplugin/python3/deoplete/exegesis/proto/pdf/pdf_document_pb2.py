# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: exegesis/proto/pdf/pdf_document.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='exegesis/proto/pdf/pdf_document.proto',
  package='exegesis.pdf',
  syntax='proto3',
  serialized_pb=_b('\n%exegesis/proto/pdf/pdf_document.proto\x12\x0c\x65xegesis.pdf\"P\n\rPdfDocumentId\x12\r\n\x05title\x18\x01 \x01(\t\x12\x15\n\rcreation_date\x18\x02 \x01(\t\x12\x19\n\x11modification_date\x18\x03 \x01(\t\"\xd1\x01\n\x0bPdfDocument\x12\x30\n\x0b\x64ocument_id\x18\x01 \x01(\x0b\x32\x1b.exegesis.pdf.PdfDocumentId\x12$\n\x05pages\x18\x02 \x03(\x0b\x32\x15.exegesis.pdf.PdfPage\x12\x39\n\x08metadata\x18\x03 \x03(\x0b\x32\'.exegesis.pdf.PdfDocument.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xf1\x01\n\x07PdfPage\x12\x0e\n\x06number\x18\x01 \x01(\x05\x12\r\n\x05width\x18\x02 \x01(\x05\x12\x0e\n\x06height\x18\x03 \x01(\x05\x12.\n\ncharacters\x18\x04 \x03(\x0b\x32\x1a.exegesis.pdf.PdfCharacter\x12.\n\x08segments\x18\x05 \x03(\x0b\x32\x1c.exegesis.pdf.PdfTextSegment\x12*\n\x06\x62locks\x18\x06 \x03(\x0b\x32\x1a.exegesis.pdf.PdfTextBlock\x12+\n\x04rows\x18\x07 \x03(\x0b\x32\x1d.exegesis.pdf.PdfTextTableRow\"\xbc\x01\n\x0cPdfCharacter\x12\x11\n\tcodepoint\x18\x01 \x01(\r\x12\x0c\n\x04utf8\x18\x02 \x01(\t\x12\x11\n\tfont_size\x18\x03 \x01(\x02\x12.\n\x0borientation\x18\x04 \x01(\x0e\x32\x19.exegesis.pdf.Orientation\x12/\n\x0c\x62ounding_box\x18\x05 \x01(\x0b\x32\x19.exegesis.pdf.BoundingBox\x12\x17\n\x0f\x66ill_color_hash\x18\x06 \x01(\r\"\xc6\x01\n\x0ePdfTextSegment\x12/\n\x0c\x62ounding_box\x18\x01 \x01(\x0b\x32\x19.exegesis.pdf.BoundingBox\x12.\n\x0borientation\x18\x02 \x01(\x0e\x32\x19.exegesis.pdf.Orientation\x12\x11\n\tfont_size\x18\x03 \x01(\x02\x12\x17\n\x0f\x66ill_color_hash\x18\x04 \x01(\r\x12\x0c\n\x04text\x18\x05 \x01(\t\x12\x19\n\x11\x63haracter_indices\x18\x06 \x03(\r\"\xaa\x01\n\x0cPdfTextBlock\x12/\n\x0c\x62ounding_box\x18\x02 \x01(\x0b\x32\x19.exegesis.pdf.BoundingBox\x12.\n\x0borientation\x18\x03 \x01(\x0e\x32\x19.exegesis.pdf.Orientation\x12\x11\n\tfont_size\x18\x04 \x01(\x02\x12\x0c\n\x04text\x18\x05 \x01(\t\x12\x0b\n\x03row\x18\x06 \x01(\x05\x12\x0b\n\x03\x63ol\x18\x07 \x01(\x05\"n\n\x0fPdfTextTableRow\x12*\n\x06\x62locks\x18\x01 \x03(\x0b\x32\x1a.exegesis.pdf.PdfTextBlock\x12/\n\x0c\x62ounding_box\x18\x02 \x01(\x0b\x32\x19.exegesis.pdf.BoundingBox\"G\n\x0b\x42oundingBox\x12\x0c\n\x04left\x18\x01 \x01(\x02\x12\x0b\n\x03top\x18\x02 \x01(\x02\x12\r\n\x05right\x18\x03 \x01(\x02\x12\x0e\n\x06\x62ottom\x18\x04 \x01(\x02\"r\n\x0cPdfPagePatch\x12\x0b\n\x03row\x18\x01 \x01(\x05\x12\x0b\n\x03\x63ol\x18\x02 \x01(\x05\x12\x10\n\x08\x65xpected\x18\x03 \x01(\t\x12\x15\n\x0breplacement\x18\x04 \x01(\tH\x00\x12\x15\n\x0bremove_cell\x18\x05 \x01(\x08H\x00\x42\x08\n\x06\x61\x63tion\"=\n\x1cPdfPagePreventSegmentBinding\x12\r\n\x05\x66irst\x18\x01 \x01(\t\x12\x0e\n\x06second\x18\x02 \x01(\t\"\xa0\x01\n\x0ePdfPageChanges\x12\x13\n\x0bpage_number\x18\x01 \x01(\x05\x12+\n\x07patches\x18\x02 \x03(\x0b\x32\x1a.exegesis.pdf.PdfPagePatch\x12L\n\x18prevent_segment_bindings\x18\x03 \x03(\x0b\x32*.exegesis.pdf.PdfPagePreventSegmentBinding\"s\n\x12PdfDocumentChanges\x12\x30\n\x0b\x64ocument_id\x18\x01 \x01(\x0b\x32\x1b.exegesis.pdf.PdfDocumentId\x12+\n\x05pages\x18\x02 \x03(\x0b\x32\x1c.exegesis.pdf.PdfPageChanges\"J\n\x13PdfDocumentsChanges\x12\x33\n\tdocuments\x18\x01 \x03(\x0b\x32 .exegesis.pdf.PdfDocumentChanges\"z\n\x0fPdfParseRequest\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x12\n\nfirst_page\x18\x02 \x01(\r\x12\x11\n\tlast_page\x18\x03 \x01(\r\x12.\n\x0brestrict_to\x18\x04 \x01(\x0b\x32\x19.exegesis.pdf.BoundingBox*7\n\x0bOrientation\x12\t\n\x05NORTH\x10\x00\x12\x08\n\x04\x45\x41ST\x10\x01\x12\t\n\x05SOUTH\x10\x02\x12\x08\n\x04WEST\x10\x03\x62\x06proto3')
)

_ORIENTATION = _descriptor.EnumDescriptor(
  name='Orientation',
  full_name='exegesis.pdf.Orientation',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NORTH', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EAST', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOUTH', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WEST', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2002,
  serialized_end=2057,
)
_sym_db.RegisterEnumDescriptor(_ORIENTATION)

Orientation = enum_type_wrapper.EnumTypeWrapper(_ORIENTATION)
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3



_PDFDOCUMENTID = _descriptor.Descriptor(
  name='PdfDocumentId',
  full_name='exegesis.pdf.PdfDocumentId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='exegesis.pdf.PdfDocumentId.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='creation_date', full_name='exegesis.pdf.PdfDocumentId.creation_date', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='modification_date', full_name='exegesis.pdf.PdfDocumentId.modification_date', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=55,
  serialized_end=135,
)


_PDFDOCUMENT_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='exegesis.pdf.PdfDocument.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='exegesis.pdf.PdfDocument.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='exegesis.pdf.PdfDocument.MetadataEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=300,
  serialized_end=347,
)

_PDFDOCUMENT = _descriptor.Descriptor(
  name='PdfDocument',
  full_name='exegesis.pdf.PdfDocument',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='document_id', full_name='exegesis.pdf.PdfDocument.document_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pages', full_name='exegesis.pdf.PdfDocument.pages', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='exegesis.pdf.PdfDocument.metadata', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_PDFDOCUMENT_METADATAENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=138,
  serialized_end=347,
)


_PDFPAGE = _descriptor.Descriptor(
  name='PdfPage',
  full_name='exegesis.pdf.PdfPage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='number', full_name='exegesis.pdf.PdfPage.number', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='width', full_name='exegesis.pdf.PdfPage.width', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='height', full_name='exegesis.pdf.PdfPage.height', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='characters', full_name='exegesis.pdf.PdfPage.characters', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='segments', full_name='exegesis.pdf.PdfPage.segments', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='blocks', full_name='exegesis.pdf.PdfPage.blocks', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rows', full_name='exegesis.pdf.PdfPage.rows', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=350,
  serialized_end=591,
)


_PDFCHARACTER = _descriptor.Descriptor(
  name='PdfCharacter',
  full_name='exegesis.pdf.PdfCharacter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='codepoint', full_name='exegesis.pdf.PdfCharacter.codepoint', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='utf8', full_name='exegesis.pdf.PdfCharacter.utf8', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='font_size', full_name='exegesis.pdf.PdfCharacter.font_size', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='orientation', full_name='exegesis.pdf.PdfCharacter.orientation', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bounding_box', full_name='exegesis.pdf.PdfCharacter.bounding_box', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fill_color_hash', full_name='exegesis.pdf.PdfCharacter.fill_color_hash', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=594,
  serialized_end=782,
)


_PDFTEXTSEGMENT = _descriptor.Descriptor(
  name='PdfTextSegment',
  full_name='exegesis.pdf.PdfTextSegment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bounding_box', full_name='exegesis.pdf.PdfTextSegment.bounding_box', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='orientation', full_name='exegesis.pdf.PdfTextSegment.orientation', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='font_size', full_name='exegesis.pdf.PdfTextSegment.font_size', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fill_color_hash', full_name='exegesis.pdf.PdfTextSegment.fill_color_hash', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='text', full_name='exegesis.pdf.PdfTextSegment.text', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='character_indices', full_name='exegesis.pdf.PdfTextSegment.character_indices', index=5,
      number=6, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=785,
  serialized_end=983,
)


_PDFTEXTBLOCK = _descriptor.Descriptor(
  name='PdfTextBlock',
  full_name='exegesis.pdf.PdfTextBlock',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bounding_box', full_name='exegesis.pdf.PdfTextBlock.bounding_box', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='orientation', full_name='exegesis.pdf.PdfTextBlock.orientation', index=1,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='font_size', full_name='exegesis.pdf.PdfTextBlock.font_size', index=2,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='text', full_name='exegesis.pdf.PdfTextBlock.text', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row', full_name='exegesis.pdf.PdfTextBlock.row', index=4,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='col', full_name='exegesis.pdf.PdfTextBlock.col', index=5,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=986,
  serialized_end=1156,
)


_PDFTEXTTABLEROW = _descriptor.Descriptor(
  name='PdfTextTableRow',
  full_name='exegesis.pdf.PdfTextTableRow',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='blocks', full_name='exegesis.pdf.PdfTextTableRow.blocks', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bounding_box', full_name='exegesis.pdf.PdfTextTableRow.bounding_box', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1158,
  serialized_end=1268,
)


_BOUNDINGBOX = _descriptor.Descriptor(
  name='BoundingBox',
  full_name='exegesis.pdf.BoundingBox',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='left', full_name='exegesis.pdf.BoundingBox.left', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='top', full_name='exegesis.pdf.BoundingBox.top', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='right', full_name='exegesis.pdf.BoundingBox.right', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bottom', full_name='exegesis.pdf.BoundingBox.bottom', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1270,
  serialized_end=1341,
)


_PDFPAGEPATCH = _descriptor.Descriptor(
  name='PdfPagePatch',
  full_name='exegesis.pdf.PdfPagePatch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row', full_name='exegesis.pdf.PdfPagePatch.row', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='col', full_name='exegesis.pdf.PdfPagePatch.col', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='expected', full_name='exegesis.pdf.PdfPagePatch.expected', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='replacement', full_name='exegesis.pdf.PdfPagePatch.replacement', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='remove_cell', full_name='exegesis.pdf.PdfPagePatch.remove_cell', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='action', full_name='exegesis.pdf.PdfPagePatch.action',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1343,
  serialized_end=1457,
)


_PDFPAGEPREVENTSEGMENTBINDING = _descriptor.Descriptor(
  name='PdfPagePreventSegmentBinding',
  full_name='exegesis.pdf.PdfPagePreventSegmentBinding',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='first', full_name='exegesis.pdf.PdfPagePreventSegmentBinding.first', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='second', full_name='exegesis.pdf.PdfPagePreventSegmentBinding.second', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1459,
  serialized_end=1520,
)


_PDFPAGECHANGES = _descriptor.Descriptor(
  name='PdfPageChanges',
  full_name='exegesis.pdf.PdfPageChanges',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page_number', full_name='exegesis.pdf.PdfPageChanges.page_number', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='patches', full_name='exegesis.pdf.PdfPageChanges.patches', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='prevent_segment_bindings', full_name='exegesis.pdf.PdfPageChanges.prevent_segment_bindings', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1523,
  serialized_end=1683,
)


_PDFDOCUMENTCHANGES = _descriptor.Descriptor(
  name='PdfDocumentChanges',
  full_name='exegesis.pdf.PdfDocumentChanges',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='document_id', full_name='exegesis.pdf.PdfDocumentChanges.document_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pages', full_name='exegesis.pdf.PdfDocumentChanges.pages', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1685,
  serialized_end=1800,
)


_PDFDOCUMENTSCHANGES = _descriptor.Descriptor(
  name='PdfDocumentsChanges',
  full_name='exegesis.pdf.PdfDocumentsChanges',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='documents', full_name='exegesis.pdf.PdfDocumentsChanges.documents', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1802,
  serialized_end=1876,
)


_PDFPARSEREQUEST = _descriptor.Descriptor(
  name='PdfParseRequest',
  full_name='exegesis.pdf.PdfParseRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filename', full_name='exegesis.pdf.PdfParseRequest.filename', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='first_page', full_name='exegesis.pdf.PdfParseRequest.first_page', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_page', full_name='exegesis.pdf.PdfParseRequest.last_page', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='restrict_to', full_name='exegesis.pdf.PdfParseRequest.restrict_to', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1878,
  serialized_end=2000,
)

_PDFDOCUMENT_METADATAENTRY.containing_type = _PDFDOCUMENT
_PDFDOCUMENT.fields_by_name['document_id'].message_type = _PDFDOCUMENTID
_PDFDOCUMENT.fields_by_name['pages'].message_type = _PDFPAGE
_PDFDOCUMENT.fields_by_name['metadata'].message_type = _PDFDOCUMENT_METADATAENTRY
_PDFPAGE.fields_by_name['characters'].message_type = _PDFCHARACTER
_PDFPAGE.fields_by_name['segments'].message_type = _PDFTEXTSEGMENT
_PDFPAGE.fields_by_name['blocks'].message_type = _PDFTEXTBLOCK
_PDFPAGE.fields_by_name['rows'].message_type = _PDFTEXTTABLEROW
_PDFCHARACTER.fields_by_name['orientation'].enum_type = _ORIENTATION
_PDFCHARACTER.fields_by_name['bounding_box'].message_type = _BOUNDINGBOX
_PDFTEXTSEGMENT.fields_by_name['bounding_box'].message_type = _BOUNDINGBOX
_PDFTEXTSEGMENT.fields_by_name['orientation'].enum_type = _ORIENTATION
_PDFTEXTBLOCK.fields_by_name['bounding_box'].message_type = _BOUNDINGBOX
_PDFTEXTBLOCK.fields_by_name['orientation'].enum_type = _ORIENTATION
_PDFTEXTTABLEROW.fields_by_name['blocks'].message_type = _PDFTEXTBLOCK
_PDFTEXTTABLEROW.fields_by_name['bounding_box'].message_type = _BOUNDINGBOX
_PDFPAGEPATCH.oneofs_by_name['action'].fields.append(
  _PDFPAGEPATCH.fields_by_name['replacement'])
_PDFPAGEPATCH.fields_by_name['replacement'].containing_oneof = _PDFPAGEPATCH.oneofs_by_name['action']
_PDFPAGEPATCH.oneofs_by_name['action'].fields.append(
  _PDFPAGEPATCH.fields_by_name['remove_cell'])
_PDFPAGEPATCH.fields_by_name['remove_cell'].containing_oneof = _PDFPAGEPATCH.oneofs_by_name['action']
_PDFPAGECHANGES.fields_by_name['patches'].message_type = _PDFPAGEPATCH
_PDFPAGECHANGES.fields_by_name['prevent_segment_bindings'].message_type = _PDFPAGEPREVENTSEGMENTBINDING
_PDFDOCUMENTCHANGES.fields_by_name['document_id'].message_type = _PDFDOCUMENTID
_PDFDOCUMENTCHANGES.fields_by_name['pages'].message_type = _PDFPAGECHANGES
_PDFDOCUMENTSCHANGES.fields_by_name['documents'].message_type = _PDFDOCUMENTCHANGES
_PDFPARSEREQUEST.fields_by_name['restrict_to'].message_type = _BOUNDINGBOX
DESCRIPTOR.message_types_by_name['PdfDocumentId'] = _PDFDOCUMENTID
DESCRIPTOR.message_types_by_name['PdfDocument'] = _PDFDOCUMENT
DESCRIPTOR.message_types_by_name['PdfPage'] = _PDFPAGE
DESCRIPTOR.message_types_by_name['PdfCharacter'] = _PDFCHARACTER
DESCRIPTOR.message_types_by_name['PdfTextSegment'] = _PDFTEXTSEGMENT
DESCRIPTOR.message_types_by_name['PdfTextBlock'] = _PDFTEXTBLOCK
DESCRIPTOR.message_types_by_name['PdfTextTableRow'] = _PDFTEXTTABLEROW
DESCRIPTOR.message_types_by_name['BoundingBox'] = _BOUNDINGBOX
DESCRIPTOR.message_types_by_name['PdfPagePatch'] = _PDFPAGEPATCH
DESCRIPTOR.message_types_by_name['PdfPagePreventSegmentBinding'] = _PDFPAGEPREVENTSEGMENTBINDING
DESCRIPTOR.message_types_by_name['PdfPageChanges'] = _PDFPAGECHANGES
DESCRIPTOR.message_types_by_name['PdfDocumentChanges'] = _PDFDOCUMENTCHANGES
DESCRIPTOR.message_types_by_name['PdfDocumentsChanges'] = _PDFDOCUMENTSCHANGES
DESCRIPTOR.message_types_by_name['PdfParseRequest'] = _PDFPARSEREQUEST
DESCRIPTOR.enum_types_by_name['Orientation'] = _ORIENTATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PdfDocumentId = _reflection.GeneratedProtocolMessageType('PdfDocumentId', (_message.Message,), dict(
  DESCRIPTOR = _PDFDOCUMENTID,
  __module__ = 'exegesis.proto.pdf.pdf_document_pb2'
  # @@protoc_insertion_point(class_scope:exegesis.pdf.PdfDocumentId)
  ))
_sym_db.RegisterMessage(PdfDocumentId)

PdfDocument = _reflection.GeneratedProtocolMessageType('PdfDocument', (_message.Message,), dict(

  MetadataEntry = _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), dict(
    DESCRIPTOR = _PDFDOCUMENT_METADATAENTRY,
    __module__ = 'exegesis.proto.pdf.pdf_document_pb2'
    # @@protoc_insertion_point(class_scope:exegesis.pdf.PdfDocument.MetadataEntry)
    ))
  ,
  DESCRIPTOR = _PDFDOCUMENT,
  __module__ = 'exegesis.proto.pdf.pdf_document_pb2'
  # @@protoc_insertion_point(class_scope:exegesis.pdf.PdfDocument)
  ))
_sym_db.RegisterMessage(PdfDocument)
_sym_db.RegisterMessage(PdfDocument.MetadataEntry)

PdfPage = _reflection.GeneratedProtocolMessageType('PdfPage', (_message.Message,), dict(
  DESCRIPTOR = _PDFPAGE,
  __module__ = 'exegesis.proto.pdf.pdf_document_pb2'
  # @@protoc_insertion_point(class_scope:exegesis.pdf.PdfPage)
  ))
_sym_db.RegisterMessage(PdfPage)

PdfCharacter = _reflection.GeneratedProtocolMessageType('PdfCharacter', (_message.Message,), dict(
  DESCRIPTOR = _PDFCHARACTER,
  __module__ = 'exegesis.proto.pdf.pdf_document_pb2'
  # @@protoc_insertion_point(class_scope:exegesis.pdf.PdfCharacter)
  ))
_sym_db.RegisterMessage(PdfCharacter)

PdfTextSegment = _reflection.GeneratedProtocolMessageType('PdfTextSegment', (_message.Message,), dict(
  DESCRIPTOR = _PDFTEXTSEGMENT,
  __module__ = 'exegesis.proto.pdf.pdf_document_pb2'
  # @@protoc_insertion_point(class_scope:exegesis.pdf.PdfTextSegment)
  ))
_sym_db.RegisterMessage(PdfTextSegment)

PdfTextBlock = _reflection.GeneratedProtocolMessageType('PdfTextBlock', (_message.Message,), dict(
  DESCRIPTOR = _PDFTEXTBLOCK,
  __module__ = 'exegesis.proto.pdf.pdf_document_pb2'
  # @@protoc_insertion_point(class_scope:exegesis.pdf.PdfTextBlock)
  ))
_sym_db.RegisterMessage(PdfTextBlock)

PdfTextTableRow = _reflection.GeneratedProtocolMessageType('PdfTextTableRow', (_message.Message,), dict(
  DESCRIPTOR = _PDFTEXTTABLEROW,
  __module__ = 'exegesis.proto.pdf.pdf_document_pb2'
  # @@protoc_insertion_point(class_scope:exegesis.pdf.PdfTextTableRow)
  ))
_sym_db.RegisterMessage(PdfTextTableRow)

BoundingBox = _reflection.GeneratedProtocolMessageType('BoundingBox', (_message.Message,), dict(
  DESCRIPTOR = _BOUNDINGBOX,
  __module__ = 'exegesis.proto.pdf.pdf_document_pb2'
  # @@protoc_insertion_point(class_scope:exegesis.pdf.BoundingBox)
  ))
_sym_db.RegisterMessage(BoundingBox)

PdfPagePatch = _reflection.GeneratedProtocolMessageType('PdfPagePatch', (_message.Message,), dict(
  DESCRIPTOR = _PDFPAGEPATCH,
  __module__ = 'exegesis.proto.pdf.pdf_document_pb2'
  # @@protoc_insertion_point(class_scope:exegesis.pdf.PdfPagePatch)
  ))
_sym_db.RegisterMessage(PdfPagePatch)

PdfPagePreventSegmentBinding = _reflection.GeneratedProtocolMessageType('PdfPagePreventSegmentBinding', (_message.Message,), dict(
  DESCRIPTOR = _PDFPAGEPREVENTSEGMENTBINDING,
  __module__ = 'exegesis.proto.pdf.pdf_document_pb2'
  # @@protoc_insertion_point(class_scope:exegesis.pdf.PdfPagePreventSegmentBinding)
  ))
_sym_db.RegisterMessage(PdfPagePreventSegmentBinding)

PdfPageChanges = _reflection.GeneratedProtocolMessageType('PdfPageChanges', (_message.Message,), dict(
  DESCRIPTOR = _PDFPAGECHANGES,
  __module__ = 'exegesis.proto.pdf.pdf_document_pb2'
  # @@protoc_insertion_point(class_scope:exegesis.pdf.PdfPageChanges)
  ))
_sym_db.RegisterMessage(PdfPageChanges)

PdfDocumentChanges = _reflection.GeneratedProtocolMessageType('PdfDocumentChanges', (_message.Message,), dict(
  DESCRIPTOR = _PDFDOCUMENTCHANGES,
  __module__ = 'exegesis.proto.pdf.pdf_document_pb2'
  # @@protoc_insertion_point(class_scope:exegesis.pdf.PdfDocumentChanges)
  ))
_sym_db.RegisterMessage(PdfDocumentChanges)

PdfDocumentsChanges = _reflection.GeneratedProtocolMessageType('PdfDocumentsChanges', (_message.Message,), dict(
  DESCRIPTOR = _PDFDOCUMENTSCHANGES,
  __module__ = 'exegesis.proto.pdf.pdf_document_pb2'
  # @@protoc_insertion_point(class_scope:exegesis.pdf.PdfDocumentsChanges)
  ))
_sym_db.RegisterMessage(PdfDocumentsChanges)

PdfParseRequest = _reflection.GeneratedProtocolMessageType('PdfParseRequest', (_message.Message,), dict(
  DESCRIPTOR = _PDFPARSEREQUEST,
  __module__ = 'exegesis.proto.pdf.pdf_document_pb2'
  # @@protoc_insertion_point(class_scope:exegesis.pdf.PdfParseRequest)
  ))
_sym_db.RegisterMessage(PdfParseRequest)


_PDFDOCUMENT_METADATAENTRY.has_options = True
_PDFDOCUMENT_METADATAENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
