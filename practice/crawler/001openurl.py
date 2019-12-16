#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from urllib import request
from fake_useragent import UserAgent
from urllib.error import HTTPError
from bs4 import BeautifulSoup

# '''
    # 综合上面两种异常，下面代码避免上叙错误
# '''

def getTitle(url):
    ua = UserAgent()
    # print(type(ua.random))
    headers = {
        'User-Agent': ua.random,
    }
    try:
        rq = request.Request(url, headers=headers, method='GET')
        response = request.urlopen(rq)
        html = response.read().decode('utf-8')
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html, features='lxml')
        title = bsObj.title
    except AttributeError as e:
        return None
    return title

# '''
    # 参数过多，或者希望参数名和参数对应，可以考虑使用**kwargs
# '''

kwargs = {
    'url': 'https://www.baidu.com/',
    # 'url': 'https://pixabay.com/zh/',
    # 'url': 'https://pixabay.com/zh/images/download/milky-way-2695569.jpg?attachment',
}

title = getTitle(**kwargs)
if title == None:
    print("Title could not be found")
else:
    print(title)
