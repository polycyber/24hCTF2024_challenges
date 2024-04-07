from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RequestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REQUEST_LOGIN: _ClassVar[RequestType]
    REQUEST_DOOR: _ClassVar[RequestType]
    REQUEST_LOGS: _ClassVar[RequestType]
    REQUEST_NOTIFY: _ClassVar[RequestType]
REQUEST_LOGIN: RequestType
REQUEST_DOOR: RequestType
REQUEST_LOGS: RequestType
REQUEST_NOTIFY: RequestType

class LoginBody(_message.Message):
    __slots__ = ("username", "password", "otp")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    OTP_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: bytes
    otp: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[bytes] = ..., otp: _Optional[str] = ...) -> None: ...

class DoorBody(_message.Message):
    __slots__ = ("id", "should_unlock")
    ID_FIELD_NUMBER: _ClassVar[int]
    SHOULD_UNLOCK_FIELD_NUMBER: _ClassVar[int]
    id: int
    should_unlock: bool
    def __init__(self, id: _Optional[int] = ..., should_unlock: bool = ...) -> None: ...

class LogsBody(_message.Message):
    __slots__ = ("id", "should_list")
    ID_FIELD_NUMBER: _ClassVar[int]
    SHOULD_LIST_FIELD_NUMBER: _ClassVar[int]
    id: str
    should_list: bool
    def __init__(self, id: _Optional[str] = ..., should_list: bool = ...) -> None: ...

class NotifyBody(_message.Message):
    __slots__ = ("notification", "host")
    NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    notification: bytes
    host: str
    def __init__(self, notification: _Optional[bytes] = ..., host: _Optional[str] = ...) -> None: ...

class Request(_message.Message):
    __slots__ = ("type", "body_login", "body_door", "body_logs", "body_notify")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    BODY_LOGIN_FIELD_NUMBER: _ClassVar[int]
    BODY_DOOR_FIELD_NUMBER: _ClassVar[int]
    BODY_LOGS_FIELD_NUMBER: _ClassVar[int]
    BODY_NOTIFY_FIELD_NUMBER: _ClassVar[int]
    type: RequestType
    body_login: LoginBody
    body_door: DoorBody
    body_logs: LogsBody
    body_notify: NotifyBody
    def __init__(self, type: _Optional[_Union[RequestType, str]] = ..., body_login: _Optional[_Union[LoginBody, _Mapping]] = ..., body_door: _Optional[_Union[DoorBody, _Mapping]] = ..., body_logs: _Optional[_Union[LogsBody, _Mapping]] = ..., body_notify: _Optional[_Union[NotifyBody, _Mapping]] = ...) -> None: ...

class Response(_message.Message):
    __slots__ = ("is_error", "message")
    IS_ERROR_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    is_error: bool
    message: str
    def __init__(self, is_error: bool = ..., message: _Optional[str] = ...) -> None: ...
