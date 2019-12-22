#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

client = socket.socket()
client.connect(('127.0.0.1', 8888))
# 接受server的信息
server_data = client.recv(1024)
print('server response:\n\t{}'.format(server_data.decode('UTF-8')))
while True:
    input_data = input('My client:\n\t').encode('UTF-8')
    client.send(input_data)
    server_data = client.recv(1024).decode('UTF-8')
    if server_data == 'q!':
        break
    print('server response: {}\n\t'.format(server_data))
    
client.close()
