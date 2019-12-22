#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import threading

def handle_sock(sock, addr):
    sock.send('welcome to server!'.encode('UTF-8'))
    while True:
        client_data = sock.recv(1024).decode('UTF-8')
        if client_data == 'q!':
            sock.send('q!'.encode('UTF-8'))
        print('client said:\n\t' + client_data)
        input_data = input('My server:\n\t')
        if input_data == 'q!':
            # sock.send('q!'.encode('UTF-8'))
            break
        # sock.send(input_data.encode('UTF-8'))
    sock.close()

server = socket.socket()
# 绑定端口
server.bind(('0.0.0.0', 8888))
# 监听端口
server.listen()

# 阻塞等待连接
while True:
    sock, addr = server.accept()
    client_thread = threading.Thread(target=handle_sock, args=(sock, addr))
    client_thread.start()
