1.可迭代对象（Iterable）

    一类是集合数据类型，如list、tuple、dict、set、str等；
    
    一类是generator，包括生成器和带yield的generator function。
    
    这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
    
    可以使用isinstance()判断一个对象是否是Iterable对象：
    
    >>> from collections import Iterable
    
    >>> isinstance([], Iterable)
    
    True
    
    >>> isinstance({}, Iterable)
    
    True
    
    >>> isinstance('abc', Iterable)
    
    True
    
    >>> isinstance((x for x in range(10)), Iterable)
    
    True
    
    >>> isinstance(100, Iterable)
    
    False

2.迭代器（Iterator）

    可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
    
    可以使用isinstance()判断一个对象是否是Iterator对象：
    
    >>> from collections import Iterator
    
    >>> isinstance((x for x in range(10)), Iterator)
    
    True
    
    >>> isinstance([], Iterator)
    
    False
    
    >>> isinstance({}, Iterator)
    
    False
    
    >>> isinstance('abc', Iterator)
    
    False
    
3.迭代（Iteration）

    当我们使用一个循环来遍历某个东西时，这个过程本身就叫迭代。
    
生成器（Generators）：一边循环一边计算的机制。

    创建一个生成器：
    
    第一种方法很简单，只要把一个列表生成式的[]改成();
    
    列表:
    
    L = [x * x for x in range(10)]
    
    生成器：
    
    g = (x * x for x in range(10))
    
    生成器使用next()函数获得generator的下一个返回值;
    
    一个个打印，next(g)，太变态。。。
    
    使用for循环，因为生成器也是可迭代对象。
    
    for n in g:
    
        print(n)
        
    第二种方法，如果一个函数定义中包含yield关键字，那么这个这个函数就是一个生成器
    
    著名的斐波拉契数列
    
    普通函数：
    
    def fib(max):
        
        n, a, b = 0, 0, 1
        
        while n < max:
        
            print(b)
            
            a, b = b, a + b
            
            n = n + 1
        
        return 'done'
       
      生成器：
       
       def fib(max):
        
           n, a, b = 0, 0, 1
        
           while n < max:
        
               yield b
            
               a, b = b, a + b
            
               n = n + 1
        
            return 'done'
        
        注意：使用next()函数不断获得下一个返回值，
        
        注意：使用for循环调用generator时，拿不到返回值：
        
        for n in fib(6):
        
            print(n)
        
        如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
        
        g = fib(6)
        
        while True:
        
            try:
            
                x = next(g)
                
                print('g:', x)
                
            except StopIteration as e:
                
                print('Generator return value:', e.value)
                
                break
