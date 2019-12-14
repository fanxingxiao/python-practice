#!/usr/bin/env python
# -*- coding: utf-8 -*-

# '''
# 
# 使用*args发送一个非键值对的可变数量的参数列表给一个参数。
# 
# 使用**kwargs允许将不定长的键值对，作为参数传递给一个函数
# 适用于在一个函数里处理  '''带名字的参数'''  的场景。
#
# '''


# 标准参数，知道具体传递几个参数

def count_2(number_1, number_2):
    print("The sum of two Numbers:\n", number_1 + number_2)

count_2(1, 2)

# 不知道具体传递几个参数

def counts(*numbers):
    count = 0
    for number in numbers:
        count += number
        
    print("Sum of multiple Numbers:\n", count)
    
counts(10, 20, 20, 50, 10)
counts()

# 必须传递的参数之外，还有可以选择传递的参数

def counts_2(number_1, number_2, *numbers):
    count = number_1 + number_2
    for number in numbers:
        count += number
    
    print("The sum of at least two Numbers:\n", count)

counts_2(1, 2)

# 必须传递的参数之外，还有可以选择传递的参数，还有指定名称的参数

def counts_3(number_1, *numbers, **kwargs):
    count = number_1
    for number in numbers:
        count += number
        
    print("The sum of at least one Numbers:\n", count)
    
    for k, v in kwargs.items():
        print("{0}: {1}".format(k, v))
    

counts_3(1, 2, principal=100)
counts_3(1)
