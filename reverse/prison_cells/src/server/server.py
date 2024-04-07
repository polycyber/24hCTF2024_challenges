#!/usr/bin/env python3

import argparse
import os
import subprocess
from flask import Flask, request, jsonify, send_file
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["180 per minute"],
    storage_uri="memory://",
)

@app.route('/get_flag_328cd65f3ec16a7c64bebdd90d2e2b3c', methods=['GET'])
def serve_html():
    return "polycyber{GU4RD5_CH4NG3_SH1F7_47_M1DN1GH7}"

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', type=str, default='0.0.0.0', help='IP address to bind to')
    parser.add_argument('--port', type=int, default=1337, help='Port to listen on')
    args = parser.parse_args()
    app.run(host=args.ip, port=args.port)

