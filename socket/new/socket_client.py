#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect(('127.0.0.1', 8888))
    while True:
        data_input = input() # 注意：input()空值校验，防止发生阻塞
        if '' == data_input:
            continue
        else:
            client.sendall(data_input.encode('utf-8'))
            data = client.recv(1024)
            
            print(type(data))
            print(data.decode('utf-8'))
