#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

'''
    网址不存在异常
   
    下面代码避免上叙的错误
'''

# try:
    # html = urlopen('https://www.baidu.com/1')
    # if html is not None:
        # print(html.read())
# except HTTPError as e:
    # print(e)

'''
    html中没有nonExistingTag标签 - 返回None对象
    再调用None对象的子标签 - 返回AttributeError异常
    
    下面代码避免上叙的错误
'''

# bsObj = BeautifulSoup(html.read(), features='lxml')
# try:
    # badContent = bsObj.nonExistingTag.anotherTag
# except AttributeError as e:
    # print("Tag was not found")
# else:
    # if badContent == None:
        # print ("Tag was not found")
    # else:
        # print(badContent)
        
'''
    本地html文本测试
'''

# with open('C:\\Users\\admin\\Desktop\\html\\1.html', 'rb') as text:
    # # print(text.read().decode('utf-8'))
    # bsObj = BeautifulSoup(text.read().decode('utf-8'), features="lxml")
    # print(bsObj.title)

'''
    综合上面两种异常，下面代码避免上叙错误
'''

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), features='lxml')
        title = bsObj.title
    except AttributeError as e:
        return None
    return title

'''
    参数过多，或者希望参数名和参数对应，可以考虑使用**kwargs
'''

kwargs = {
    'url': 'https://www.baidu.com/',
}

title = getTitle(**kwargs)
if title == None:
    print("Title could not be found")
else:
    print(title)
