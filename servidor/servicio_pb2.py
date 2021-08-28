# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: servicio.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='servicio.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0eservicio.proto\"\x1f\n\x0fTipoMedicamento\x12\x0c\n\x04tipo\x18\x01 \x01(\t\"\x99\x01\n\x0bMedicamento\x12\x18\n\x10\x63odigoAlfabetico\x18\x01 \x01(\t\x12\x16\n\x0e\x63odigoNumerico\x18\x02 \x01(\x05\x12\x19\n\x11\x64igitoVerificador\x18\x03 \x01(\x05\x12\x0e\n\x06nombre\x18\x04 \x01(\t\x12\r\n\x05\x64roga\x18\x05 \x01(\t\x12\x1e\n\x04tipo\x18\x06 \x01(\x0b\x32\x10.TipoMedicamento\"7\n\x11ListaMedicamentos\x12\"\n\x0cmedicamentos\x18\x01 \x03(\x0b\x32\x0c.Medicamento\"$\n\x0c\x43onfirmacion\x12\x14\n\x0c\x63onfirmacion\x18\x01 \x01(\t\"\x06\n\x04Nulo2\x80\x02\n\x17LaboratorioFarmaceutico\x12\x15\n\x05Listo\x12\x05.Nulo\x1a\x05.Nulo\x12\x36\n\x13\x41ltaTipoMedicamento\x12\x10.TipoMedicamento\x1a\r.Confirmacion\x12\x36\n\x13\x42\x61jaTipoMedicamento\x12\x10.TipoMedicamento\x1a\r.Confirmacion\x12.\n\x0f\x41ltaMedicamento\x12\x0c.Medicamento\x1a\r.Confirmacion\x12.\n\x11TraerMedicamentos\x12\x05.Nulo\x1a\x12.ListaMedicamentosb\x06proto3'
)




_TIPOMEDICAMENTO = _descriptor.Descriptor(
  name='TipoMedicamento',
  full_name='TipoMedicamento',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tipo', full_name='TipoMedicamento.tipo', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=18,
  serialized_end=49,
)


_MEDICAMENTO = _descriptor.Descriptor(
  name='Medicamento',
  full_name='Medicamento',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='codigoAlfabetico', full_name='Medicamento.codigoAlfabetico', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='codigoNumerico', full_name='Medicamento.codigoNumerico', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='digitoVerificador', full_name='Medicamento.digitoVerificador', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nombre', full_name='Medicamento.nombre', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='droga', full_name='Medicamento.droga', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tipo', full_name='Medicamento.tipo', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=52,
  serialized_end=205,
)


_LISTAMEDICAMENTOS = _descriptor.Descriptor(
  name='ListaMedicamentos',
  full_name='ListaMedicamentos',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='medicamentos', full_name='ListaMedicamentos.medicamentos', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=207,
  serialized_end=262,
)


_CONFIRMACION = _descriptor.Descriptor(
  name='Confirmacion',
  full_name='Confirmacion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='confirmacion', full_name='Confirmacion.confirmacion', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=264,
  serialized_end=300,
)


_NULO = _descriptor.Descriptor(
  name='Nulo',
  full_name='Nulo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=302,
  serialized_end=308,
)

_MEDICAMENTO.fields_by_name['tipo'].message_type = _TIPOMEDICAMENTO
_LISTAMEDICAMENTOS.fields_by_name['medicamentos'].message_type = _MEDICAMENTO
DESCRIPTOR.message_types_by_name['TipoMedicamento'] = _TIPOMEDICAMENTO
DESCRIPTOR.message_types_by_name['Medicamento'] = _MEDICAMENTO
DESCRIPTOR.message_types_by_name['ListaMedicamentos'] = _LISTAMEDICAMENTOS
DESCRIPTOR.message_types_by_name['Confirmacion'] = _CONFIRMACION
DESCRIPTOR.message_types_by_name['Nulo'] = _NULO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TipoMedicamento = _reflection.GeneratedProtocolMessageType('TipoMedicamento', (_message.Message,), {
  'DESCRIPTOR' : _TIPOMEDICAMENTO,
  '__module__' : 'servicio_pb2'
  # @@protoc_insertion_point(class_scope:TipoMedicamento)
  })
_sym_db.RegisterMessage(TipoMedicamento)

Medicamento = _reflection.GeneratedProtocolMessageType('Medicamento', (_message.Message,), {
  'DESCRIPTOR' : _MEDICAMENTO,
  '__module__' : 'servicio_pb2'
  # @@protoc_insertion_point(class_scope:Medicamento)
  })
_sym_db.RegisterMessage(Medicamento)

ListaMedicamentos = _reflection.GeneratedProtocolMessageType('ListaMedicamentos', (_message.Message,), {
  'DESCRIPTOR' : _LISTAMEDICAMENTOS,
  '__module__' : 'servicio_pb2'
  # @@protoc_insertion_point(class_scope:ListaMedicamentos)
  })
_sym_db.RegisterMessage(ListaMedicamentos)

Confirmacion = _reflection.GeneratedProtocolMessageType('Confirmacion', (_message.Message,), {
  'DESCRIPTOR' : _CONFIRMACION,
  '__module__' : 'servicio_pb2'
  # @@protoc_insertion_point(class_scope:Confirmacion)
  })
_sym_db.RegisterMessage(Confirmacion)

Nulo = _reflection.GeneratedProtocolMessageType('Nulo', (_message.Message,), {
  'DESCRIPTOR' : _NULO,
  '__module__' : 'servicio_pb2'
  # @@protoc_insertion_point(class_scope:Nulo)
  })
_sym_db.RegisterMessage(Nulo)



_LABORATORIOFARMACEUTICO = _descriptor.ServiceDescriptor(
  name='LaboratorioFarmaceutico',
  full_name='LaboratorioFarmaceutico',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=311,
  serialized_end=567,
  methods=[
  _descriptor.MethodDescriptor(
    name='Listo',
    full_name='LaboratorioFarmaceutico.Listo',
    index=0,
    containing_service=None,
    input_type=_NULO,
    output_type=_NULO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AltaTipoMedicamento',
    full_name='LaboratorioFarmaceutico.AltaTipoMedicamento',
    index=1,
    containing_service=None,
    input_type=_TIPOMEDICAMENTO,
    output_type=_CONFIRMACION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='BajaTipoMedicamento',
    full_name='LaboratorioFarmaceutico.BajaTipoMedicamento',
    index=2,
    containing_service=None,
    input_type=_TIPOMEDICAMENTO,
    output_type=_CONFIRMACION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AltaMedicamento',
    full_name='LaboratorioFarmaceutico.AltaMedicamento',
    index=3,
    containing_service=None,
    input_type=_MEDICAMENTO,
    output_type=_CONFIRMACION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='TraerMedicamentos',
    full_name='LaboratorioFarmaceutico.TraerMedicamentos',
    index=4,
    containing_service=None,
    input_type=_NULO,
    output_type=_LISTAMEDICAMENTOS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_LABORATORIOFARMACEUTICO)

DESCRIPTOR.services_by_name['LaboratorioFarmaceutico'] = _LABORATORIOFARMACEUTICO

# @@protoc_insertion_point(module_scope)
