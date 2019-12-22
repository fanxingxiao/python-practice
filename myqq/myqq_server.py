#!/usr/bin/env python
# -*- coding: utf-8 -*-

# qq服务器
# 1.转发消息
# 2.处理登陆
# 3.处理退出
# 4.维护历史消息，维护在线用户和维护用户的连接

import socket
import collections import defaultdict

# 1.维护用户连接

