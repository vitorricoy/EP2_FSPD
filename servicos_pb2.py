# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: servicos.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='servicos.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0eservicos.proto\":\n\x12RequisicaoRegistro\x12\x0f\n\x07servico\x18\x01 \x01(\t\x12\x13\n\x0blistaChaves\x18\x02 \x03(\x04\"-\n\x10RespostaRegistro\x12\x19\n\x11\x63havesProcessadas\x18\x01 \x01(\x04\"%\n\x14RequisicaoMapeamento\x12\r\n\x05\x63have\x18\x01 \x01(\x04\"%\n\x12RespostaMapeamento\x12\x0f\n\x07servico\x18\x01 \x01(\t\"\x13\n\x11RequisicaoTermino\",\n\x0fRespostaTermino\x12\x19\n\x11\x63havesRegistradas\x18\x01 \x01(\x04\"&\n\x14RespostaTerminoPares\x12\x0e\n\x06status\x18\x01 \x01(\x04\"2\n\x12RequisicaoInsercao\x12\r\n\x05\x63have\x18\x01 \x01(\x05\x12\r\n\x05valor\x18\x02 \x01(\t\"\"\n\x10RespostaInsercao\x12\x0e\n\x06status\x18\x01 \x01(\x04\"#\n\x12RequisicaoConsulta\x12\r\n\x05\x63have\x18\x01 \x01(\x04\"%\n\x10RespostaConsulta\x12\x11\n\tresultado\x18\x01 \x01(\t\"%\n\x12RequisicaoAtivacao\x12\x0f\n\x07servico\x18\x01 \x01(\t\"-\n\x10RespostaAtivacao\x12\x19\n\x11\x63havesProcessadas\x18\x01 \x01(\x04\x32\xb7\x01\n\x13ServerCentralizador\x12\x35\n\tRegistrar\x12\x13.RequisicaoRegistro\x1a\x11.RespostaRegistro\"\x00\x12\x36\n\x06Mapear\x12\x15.RequisicaoMapeamento\x1a\x13.RespostaMapeamento\"\x00\x12\x31\n\x07Termina\x12\x12.RequisicaoTermino\x1a\x10.RespostaTermino\"\x00\x32\xe2\x01\n\x0bServerPares\x12\x32\n\x06Insere\x12\x13.RequisicaoInsercao\x1a\x11.RespostaInsercao\"\x00\x12\x34\n\x08\x43onsulta\x12\x13.RequisicaoConsulta\x1a\x11.RespostaConsulta\"\x00\x12\x31\n\x05\x41tiva\x12\x13.RequisicaoAtivacao\x1a\x11.RespostaAtivacao\"\x00\x12\x36\n\x07Termina\x12\x12.RequisicaoTermino\x1a\x15.RespostaTerminoPares\"\x00\x62\x06proto3'
)




_REQUISICAOREGISTRO = _descriptor.Descriptor(
  name='RequisicaoRegistro',
  full_name='RequisicaoRegistro',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='servico', full_name='RequisicaoRegistro.servico', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='listaChaves', full_name='RequisicaoRegistro.listaChaves', index=1,
      number=2, type=4, cpp_type=4, label=3,
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
  serialized_start=18,
  serialized_end=76,
)


_RESPOSTAREGISTRO = _descriptor.Descriptor(
  name='RespostaRegistro',
  full_name='RespostaRegistro',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='chavesProcessadas', full_name='RespostaRegistro.chavesProcessadas', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=78,
  serialized_end=123,
)


_REQUISICAOMAPEAMENTO = _descriptor.Descriptor(
  name='RequisicaoMapeamento',
  full_name='RequisicaoMapeamento',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='chave', full_name='RequisicaoMapeamento.chave', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=125,
  serialized_end=162,
)


_RESPOSTAMAPEAMENTO = _descriptor.Descriptor(
  name='RespostaMapeamento',
  full_name='RespostaMapeamento',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='servico', full_name='RespostaMapeamento.servico', index=0,
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
  serialized_start=164,
  serialized_end=201,
)


_REQUISICAOTERMINO = _descriptor.Descriptor(
  name='RequisicaoTermino',
  full_name='RequisicaoTermino',
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
  serialized_start=203,
  serialized_end=222,
)


_RESPOSTATERMINO = _descriptor.Descriptor(
  name='RespostaTermino',
  full_name='RespostaTermino',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='chavesRegistradas', full_name='RespostaTermino.chavesRegistradas', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=224,
  serialized_end=268,
)


_RESPOSTATERMINOPARES = _descriptor.Descriptor(
  name='RespostaTerminoPares',
  full_name='RespostaTerminoPares',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='RespostaTerminoPares.status', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=270,
  serialized_end=308,
)


_REQUISICAOINSERCAO = _descriptor.Descriptor(
  name='RequisicaoInsercao',
  full_name='RequisicaoInsercao',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='chave', full_name='RequisicaoInsercao.chave', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='valor', full_name='RequisicaoInsercao.valor', index=1,
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
  serialized_start=310,
  serialized_end=360,
)


_RESPOSTAINSERCAO = _descriptor.Descriptor(
  name='RespostaInsercao',
  full_name='RespostaInsercao',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='RespostaInsercao.status', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=362,
  serialized_end=396,
)


_REQUISICAOCONSULTA = _descriptor.Descriptor(
  name='RequisicaoConsulta',
  full_name='RequisicaoConsulta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='chave', full_name='RequisicaoConsulta.chave', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=398,
  serialized_end=433,
)


_RESPOSTACONSULTA = _descriptor.Descriptor(
  name='RespostaConsulta',
  full_name='RespostaConsulta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resultado', full_name='RespostaConsulta.resultado', index=0,
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
  serialized_start=435,
  serialized_end=472,
)


_REQUISICAOATIVACAO = _descriptor.Descriptor(
  name='RequisicaoAtivacao',
  full_name='RequisicaoAtivacao',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='servico', full_name='RequisicaoAtivacao.servico', index=0,
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
  serialized_start=474,
  serialized_end=511,
)


_RESPOSTAATIVACAO = _descriptor.Descriptor(
  name='RespostaAtivacao',
  full_name='RespostaAtivacao',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='chavesProcessadas', full_name='RespostaAtivacao.chavesProcessadas', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=513,
  serialized_end=558,
)

DESCRIPTOR.message_types_by_name['RequisicaoRegistro'] = _REQUISICAOREGISTRO
DESCRIPTOR.message_types_by_name['RespostaRegistro'] = _RESPOSTAREGISTRO
DESCRIPTOR.message_types_by_name['RequisicaoMapeamento'] = _REQUISICAOMAPEAMENTO
DESCRIPTOR.message_types_by_name['RespostaMapeamento'] = _RESPOSTAMAPEAMENTO
DESCRIPTOR.message_types_by_name['RequisicaoTermino'] = _REQUISICAOTERMINO
DESCRIPTOR.message_types_by_name['RespostaTermino'] = _RESPOSTATERMINO
DESCRIPTOR.message_types_by_name['RespostaTerminoPares'] = _RESPOSTATERMINOPARES
DESCRIPTOR.message_types_by_name['RequisicaoInsercao'] = _REQUISICAOINSERCAO
DESCRIPTOR.message_types_by_name['RespostaInsercao'] = _RESPOSTAINSERCAO
DESCRIPTOR.message_types_by_name['RequisicaoConsulta'] = _REQUISICAOCONSULTA
DESCRIPTOR.message_types_by_name['RespostaConsulta'] = _RESPOSTACONSULTA
DESCRIPTOR.message_types_by_name['RequisicaoAtivacao'] = _REQUISICAOATIVACAO
DESCRIPTOR.message_types_by_name['RespostaAtivacao'] = _RESPOSTAATIVACAO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequisicaoRegistro = _reflection.GeneratedProtocolMessageType('RequisicaoRegistro', (_message.Message,), {
  'DESCRIPTOR' : _REQUISICAOREGISTRO,
  '__module__' : 'servicos_pb2'
  # @@protoc_insertion_point(class_scope:RequisicaoRegistro)
  })
_sym_db.RegisterMessage(RequisicaoRegistro)

RespostaRegistro = _reflection.GeneratedProtocolMessageType('RespostaRegistro', (_message.Message,), {
  'DESCRIPTOR' : _RESPOSTAREGISTRO,
  '__module__' : 'servicos_pb2'
  # @@protoc_insertion_point(class_scope:RespostaRegistro)
  })
_sym_db.RegisterMessage(RespostaRegistro)

RequisicaoMapeamento = _reflection.GeneratedProtocolMessageType('RequisicaoMapeamento', (_message.Message,), {
  'DESCRIPTOR' : _REQUISICAOMAPEAMENTO,
  '__module__' : 'servicos_pb2'
  # @@protoc_insertion_point(class_scope:RequisicaoMapeamento)
  })
_sym_db.RegisterMessage(RequisicaoMapeamento)

RespostaMapeamento = _reflection.GeneratedProtocolMessageType('RespostaMapeamento', (_message.Message,), {
  'DESCRIPTOR' : _RESPOSTAMAPEAMENTO,
  '__module__' : 'servicos_pb2'
  # @@protoc_insertion_point(class_scope:RespostaMapeamento)
  })
_sym_db.RegisterMessage(RespostaMapeamento)

RequisicaoTermino = _reflection.GeneratedProtocolMessageType('RequisicaoTermino', (_message.Message,), {
  'DESCRIPTOR' : _REQUISICAOTERMINO,
  '__module__' : 'servicos_pb2'
  # @@protoc_insertion_point(class_scope:RequisicaoTermino)
  })
_sym_db.RegisterMessage(RequisicaoTermino)

RespostaTermino = _reflection.GeneratedProtocolMessageType('RespostaTermino', (_message.Message,), {
  'DESCRIPTOR' : _RESPOSTATERMINO,
  '__module__' : 'servicos_pb2'
  # @@protoc_insertion_point(class_scope:RespostaTermino)
  })
_sym_db.RegisterMessage(RespostaTermino)

RespostaTerminoPares = _reflection.GeneratedProtocolMessageType('RespostaTerminoPares', (_message.Message,), {
  'DESCRIPTOR' : _RESPOSTATERMINOPARES,
  '__module__' : 'servicos_pb2'
  # @@protoc_insertion_point(class_scope:RespostaTerminoPares)
  })
_sym_db.RegisterMessage(RespostaTerminoPares)

RequisicaoInsercao = _reflection.GeneratedProtocolMessageType('RequisicaoInsercao', (_message.Message,), {
  'DESCRIPTOR' : _REQUISICAOINSERCAO,
  '__module__' : 'servicos_pb2'
  # @@protoc_insertion_point(class_scope:RequisicaoInsercao)
  })
_sym_db.RegisterMessage(RequisicaoInsercao)

RespostaInsercao = _reflection.GeneratedProtocolMessageType('RespostaInsercao', (_message.Message,), {
  'DESCRIPTOR' : _RESPOSTAINSERCAO,
  '__module__' : 'servicos_pb2'
  # @@protoc_insertion_point(class_scope:RespostaInsercao)
  })
_sym_db.RegisterMessage(RespostaInsercao)

RequisicaoConsulta = _reflection.GeneratedProtocolMessageType('RequisicaoConsulta', (_message.Message,), {
  'DESCRIPTOR' : _REQUISICAOCONSULTA,
  '__module__' : 'servicos_pb2'
  # @@protoc_insertion_point(class_scope:RequisicaoConsulta)
  })
_sym_db.RegisterMessage(RequisicaoConsulta)

RespostaConsulta = _reflection.GeneratedProtocolMessageType('RespostaConsulta', (_message.Message,), {
  'DESCRIPTOR' : _RESPOSTACONSULTA,
  '__module__' : 'servicos_pb2'
  # @@protoc_insertion_point(class_scope:RespostaConsulta)
  })
_sym_db.RegisterMessage(RespostaConsulta)

RequisicaoAtivacao = _reflection.GeneratedProtocolMessageType('RequisicaoAtivacao', (_message.Message,), {
  'DESCRIPTOR' : _REQUISICAOATIVACAO,
  '__module__' : 'servicos_pb2'
  # @@protoc_insertion_point(class_scope:RequisicaoAtivacao)
  })
_sym_db.RegisterMessage(RequisicaoAtivacao)

RespostaAtivacao = _reflection.GeneratedProtocolMessageType('RespostaAtivacao', (_message.Message,), {
  'DESCRIPTOR' : _RESPOSTAATIVACAO,
  '__module__' : 'servicos_pb2'
  # @@protoc_insertion_point(class_scope:RespostaAtivacao)
  })
_sym_db.RegisterMessage(RespostaAtivacao)



_SERVERCENTRALIZADOR = _descriptor.ServiceDescriptor(
  name='ServerCentralizador',
  full_name='ServerCentralizador',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=561,
  serialized_end=744,
  methods=[
  _descriptor.MethodDescriptor(
    name='Registrar',
    full_name='ServerCentralizador.Registrar',
    index=0,
    containing_service=None,
    input_type=_REQUISICAOREGISTRO,
    output_type=_RESPOSTAREGISTRO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Mapear',
    full_name='ServerCentralizador.Mapear',
    index=1,
    containing_service=None,
    input_type=_REQUISICAOMAPEAMENTO,
    output_type=_RESPOSTAMAPEAMENTO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Termina',
    full_name='ServerCentralizador.Termina',
    index=2,
    containing_service=None,
    input_type=_REQUISICAOTERMINO,
    output_type=_RESPOSTATERMINO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SERVERCENTRALIZADOR)

DESCRIPTOR.services_by_name['ServerCentralizador'] = _SERVERCENTRALIZADOR


_SERVERPARES = _descriptor.ServiceDescriptor(
  name='ServerPares',
  full_name='ServerPares',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=747,
  serialized_end=973,
  methods=[
  _descriptor.MethodDescriptor(
    name='Insere',
    full_name='ServerPares.Insere',
    index=0,
    containing_service=None,
    input_type=_REQUISICAOINSERCAO,
    output_type=_RESPOSTAINSERCAO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Consulta',
    full_name='ServerPares.Consulta',
    index=1,
    containing_service=None,
    input_type=_REQUISICAOCONSULTA,
    output_type=_RESPOSTACONSULTA,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Ativa',
    full_name='ServerPares.Ativa',
    index=2,
    containing_service=None,
    input_type=_REQUISICAOATIVACAO,
    output_type=_RESPOSTAATIVACAO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Termina',
    full_name='ServerPares.Termina',
    index=3,
    containing_service=None,
    input_type=_REQUISICAOTERMINO,
    output_type=_RESPOSTATERMINOPARES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SERVERPARES)

DESCRIPTOR.services_by_name['ServerPares'] = _SERVERPARES

# @@protoc_insertion_point(module_scope)
