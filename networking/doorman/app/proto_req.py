import struct
import socket
from google.protobuf.message import Message

class ProtobufSocketException(Exception):
    pass

class ProtobufSocket:
    def __init__(self, sock: socket.socket):
        self._sock = sock
    
    def send(self, message: Message):
        serialized = message.SerializeToString()

        try:
            self._sock.sendall(struct.pack('!H', len(serialized)) + serialized)
        except:
            raise ProtobufSocketException()

    def recv(self, message: Message):
        try:
            size = struct.unpack('!H', self._sock.recv(2))[0]
            message.ParseFromString(self._sock.recv(size))
        except:
            raise ProtobufSocketException()