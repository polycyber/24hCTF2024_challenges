import socket
import sys
import socketserver
import re
import struct
import time
import doorman_pb2
from proto_req import ProtobufSocket, ProtobufSocketException
from dataclasses import dataclass
import secrets
import config
from utils import xor, is_ip_address

prison_log = '''
[Date: January 30, 2024]
[Time: 08:00]
[Location: Sector 7]
[Event: Security Protocol Delta]

- [07:58] - Operator X accessed Door A1 for routine inspection.
- [08:05] - Door A1 initiated automatic protocol for meal distribution.
- [08:10] - Subject 56789 transitioned from Dormitory 101 to designated recreational area.
- [08:15] - Subject 12345 utilized Door B1 for medical assessment.
- [08:20] - Door B1 granted access to medical personnel.
- [08:25] - Subject 98765 returned to Dormitory 102 post-medical evaluation.
- [08:30] - Door C1 activated for maintenance personnel.
- [08:35] - Subject 24680 utilized Door C1 for authorized visitation.
- [08:40] - Door C1 reverted to secure mode upon completion of visitation.
- [08:45] - Subject 13579 accessed Door D1 for therapeutic session.
- [08:50] - Door D1 granted access to authorized counselor.
- [08:55] - Subject 24680 exited designated counseling area.
- [09:00] - Door D1 resealed post-counseling session.
'''

g_port = 0

@dataclass
class Session:
    key: bytes
    logged_in: bool

    def get_otp(self):
        return str(self.key[0])

class DoormanTCPHandler(socketserver.BaseRequestHandler):
    def _setup_session(self):
        self.session = Session(key=secrets.token_bytes(config.KEY_SIZE), logged_in=False)
        announcement = doorman_pb2.Response(is_error=False, message='KEY:' + self.session.key.hex())

        self.proto_request.send(announcement)

        if self.client_address[0] == '127.0.0.1':
            self.session.logged_in = True

    def _handle_login(self):
        login_request = self.parsed_request.body_login

        if not self.session.logged_in:
            if login_request.username != config.USERNAME or xor(self.session.key, login_request.password) != config.PASSWORD.encode():
                return doorman_pb2.Response(is_error=True, message='Invalid password or username')

            if login_request.otp != self.session.get_otp():
                return doorman_pb2.Response(is_error=True, message=f'Invalid OTP: was {self.session.get_otp()}')

            self.session.logged_in = True

        return doorman_pb2.Response(is_error=False, message='Login successful')
    
    def _handle_door(self):
        if not self.session.logged_in:
            return doorman_pb2.Response(is_error=True, message='Not localhost. Authentication required.')
        
        door_request = self.parsed_request.body_door

        message = f'Door {door_request.id} has been {"un" if door_request.should_unlock else ""}locked'
        if door_request.id == config.CHAL_DOOR_ID and door_request.should_unlock:
            message += ' ' + config.CHAL_DOOR_FLAG

        return doorman_pb2.Response(is_error=False, message=message)

    def _handle_logs(self):
        if not self.session.logged_in:
            return doorman_pb2.Response(is_error=True, message='Not localhost. Authentication required.')
        
        logs_request = self.parsed_request.body_logs

        error_msg = 'cannot open \'%s\': Permission denied'

        fake_fs = {
            'flag.txt': config.CHAL_LOGS_FLAG,
            config.CHAL_SSRF_FILENAME: config.CHAL_SSRF_FLAG,
            'log_0.txt': prison_log
        }

        if logs_request.should_list:
            return doorman_pb2.Response(is_error=False, message='\n'.join(fake_fs.keys()))
        elif logs_request.id not in fake_fs.keys() or (logs_request.id == config.CHAL_SSRF_FILENAME and self.client_address[0] != '127.0.0.1'):
            error_msg = f'cannot open \'{str(logs_request.id)}\': Permission denied'
            return doorman_pb2.Response(is_error=True, message=error_msg)

        return doorman_pb2.Response(is_error=False, message=fake_fs[logs_request.id])

    def _handle_notify(self):
        if not self.session.logged_in:
            return doorman_pb2.Response(is_error=True, message='Not localhost. Authentication required.')
        
        notify_request = self.parsed_request.body_notify

        hostname_regex = r'^[0-9A-Za-z\.]+\.[A-Za-z]+$'
        if not re.fullmatch(hostname_regex, notify_request.host):
            return doorman_pb2.Response(is_error=True, message=f'Hostname does not match Regex: {hostname_regex}')
        elif 'localhost' in notify_request.host:
            return doorman_pb2.Response(is_error=True, message='No localhost!!!')
        
        try:
            resp = b''
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((notify_request.host, g_port))
                sock.sendall(notify_request.notification)
                stop_time = time.time() + 1
                while time.time() < stop_time:
                    try:
                        resp += sock.recv(256, socket.MSG_DONTWAIT)
                    except:
                        pass
        except TimeoutError:
            pass
        except:
            return doorman_pb2.Response(is_error=True, message=f'Error with socket')

        return doorman_pb2.Response(is_error=False, message=resp.decode('latin1'))

    def handle(self):
        self.proto_request = ProtobufSocket(self.request)
        self._setup_session()

        print(f'> {self.client_address}')
        
        while True:
            try:
                self.parsed_request = doorman_pb2.Request()
                self.proto_request.recv(self.parsed_request)

                handlers = {
                    doorman_pb2.REQUEST_LOGIN: self._handle_login,
                    doorman_pb2.REQUEST_DOOR: self._handle_door,
                    doorman_pb2.REQUEST_LOGS: self._handle_logs,
                    doorman_pb2.REQUEST_NOTIFY: self._handle_notify,
                }

                response = handlers.get(
                    self.parsed_request.type,
                    lambda: doorman_pb2.Response(is_error=True, message='Invalid request')
                )()

                self.proto_request.send(response)

                if self.parsed_request.type == doorman_pb2.REQUEST_LOGIN and response.is_error:
                    break
            except ProtobufSocketException:
                break

        print(f'< {self.client_address}')

def main(argv):
    global g_port
    if len(argv) != 3:
        print(f'Usage: {argv[0]} HOST PORT')
        return 1

    print('hello')
    HOST = argv[1]
    PORT = g_port = int(argv[2])

    with socketserver.ThreadingTCPServer((HOST, PORT), DoormanTCPHandler) as server:
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass

    return 0

if __name__ == '__main__':
    exit(main(sys.argv))