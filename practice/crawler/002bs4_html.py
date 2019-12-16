#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup

# html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
# bsObj = BeautifulSoup(html, features='lxml')
# # print(bsObj.h1)
# nameList = bsObj.findAll('span', {'class': 'green'})
# for name in nameList:
    # print(name.get_text()) 

# # '''
    # # BeautifulSoup的find()和findAll()
    # # findAll(tag, attributes, recursive, text, limit, keywords)
    # # find(tag, attributes, recursive, text, keywords)
# # '''

# # tag - 标签
# nameList_tag = bsObj.findAll(['h1', 'h2'])
# # print(nameList_tag)

# # attributes - 属性
# nameList_attr = bsObj.findAll('span', {'class': ['green', 'red']})
# # print(nameList_attr)

# # recursive - 深度，递归
# nameList_recur = bsObj.findAll('head', recursive=False)
# # print(nameList_recur)

# # text - 通过标签的文本内容匹配
# nameList_text = bsObj.findAll(text='the prince')
# # print(nameList_text)

# # limit - 范围限制参数
# nameList_limit = bsObj.findAll(text='the prince', limit=1)
# # print(nameList_limit)

# # keyword - 选择具有指定属性的标签
# # class 在python中具有特殊的含义，使用keyword定位class，python会出错
# # 使用.findAll('', {'class': 'red'})
# nameList_keyword = bsObj.findAll('', {'id': 'text'})
# # print(nameList_keyword)

# ----------------------------------------------------------------------

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bsObj = BeautifulSoup(html, features='lxml')
# # 子标签 - 一个父级标签的下一级的标签
# chs = bsObj.find('table', {'id': 'giftList'}).children
# for ch in chs:
    # print(ch)
    
# # 后代标签 - 一个父级标签下面所有级别的标签
# css = bsObj.find('table', {'id': 'giftList'}).descendants
# for cs in css:
    # print(cs)
    
# # 处理兄弟标签 
# # next_siblings - 可以选择表格中除了标题行以外的所有行
# # previous_sibling - 可以选择表格中除了标题行以前的行
# for sibling in bsObj.find("table", {"id": "giftList"}).tr.next_siblings:
    # print(sibling)
    
# # 父标签的处理
# print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"
                        # }).parent.previous_sibling.get_text())
                        
# ----------------------------------------------------------------------

# 正则表达式
# '''
    # 字母a至少出现一次
    # 后面跟着字母b重复5次
    # 后面再跟着字母c重复任意偶数次（0是一个偶数）
    # 最后一位是字母d，也可以没有
# '''


