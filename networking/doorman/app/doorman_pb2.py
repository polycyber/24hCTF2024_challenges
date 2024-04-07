# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: doorman.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rdoorman.proto\x12\x07\x64oorman\"<\n\tLoginBody\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\x0c\x12\x0b\n\x03otp\x18\x03 \x01(\t\"-\n\x08\x44oorBody\x12\n\n\x02id\x18\x01 \x01(\r\x12\x15\n\rshould_unlock\x18\x02 \x01(\x08\"L\n\x08LogsBody\x12\x0f\n\x02id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x18\n\x0bshould_list\x18\x02 \x01(\x08H\x01\x88\x01\x01\x42\x05\n\x03_idB\x0e\n\x0c_should_list\"0\n\nNotifyBody\x12\x14\n\x0cnotification\x18\x01 \x01(\x0c\x12\x0c\n\x04host\x18\x02 \x01(\t\"\xdb\x01\n\x07Request\x12\"\n\x04type\x18\x01 \x01(\x0e\x32\x14.doorman.RequestType\x12(\n\nbody_login\x18\x02 \x01(\x0b\x32\x12.doorman.LoginBodyH\x00\x12&\n\tbody_door\x18\x03 \x01(\x0b\x32\x11.doorman.DoorBodyH\x00\x12&\n\tbody_logs\x18\x04 \x01(\x0b\x32\x11.doorman.LogsBodyH\x00\x12*\n\x0b\x62ody_notify\x18\x05 \x01(\x0b\x32\x13.doorman.NotifyBodyH\x00\x42\x06\n\x04\x62ody\"-\n\x08Response\x12\x10\n\x08is_error\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t*X\n\x0bRequestType\x12\x11\n\rREQUEST_LOGIN\x10\x00\x12\x10\n\x0cREQUEST_DOOR\x10\x01\x12\x10\n\x0cREQUEST_LOGS\x10\x02\x12\x12\n\x0eREQUEST_NOTIFY\x10\x03\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doorman_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_REQUESTTYPE']._serialized_start=532
  _globals['_REQUESTTYPE']._serialized_end=620
  _globals['_LOGINBODY']._serialized_start=26
  _globals['_LOGINBODY']._serialized_end=86
  _globals['_DOORBODY']._serialized_start=88
  _globals['_DOORBODY']._serialized_end=133
  _globals['_LOGSBODY']._serialized_start=135
  _globals['_LOGSBODY']._serialized_end=211
  _globals['_NOTIFYBODY']._serialized_start=213
  _globals['_NOTIFYBODY']._serialized_end=261
  _globals['_REQUEST']._serialized_start=264
  _globals['_REQUEST']._serialized_end=483
  _globals['_RESPONSE']._serialized_start=485
  _globals['_RESPONSE']._serialized_end=530
# @@protoc_insertion_point(module_scope)
