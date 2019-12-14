变量前面一个星[*args]

主要用于函数定义，你可以将不定量的参数传递给一个函数。
用于预先不知道函数使用者会传递多少个参数的场景。

变量前面两个星[**kwargs]

可以用于函数定义，函数参数key / value对应的写法。

例如：

def people(name, age, sex):

    print("姓名：", name)
    
    print("\n年龄", age)
    
    print("\n性别", sex)

kwargs = {

    'name': 'xiaomi',
    
    'age': 20,
    
    'sex': '男'
    
}

people(**kwargs)
