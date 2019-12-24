#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind(('0.0.0.0', 8888))
    server.listen()
    sock, addr = server.accept()
    with sock:
        print('Connected by', addr)
        while True:
            data = sock.recv(1024)
            if not data:
                break
            print(type(data))
            print(data.decode('utf-8'))
            sock.sendall(data)
