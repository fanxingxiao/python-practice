调试（Debugging）
Python debugger(pdb)

1.从外部命令行debug运行一个脚本

    $ python -m pdb my_script.py

2.从脚本内部运行

    import pdb
    
    def make_bread():
        pdb.set_trace()
        return "I don't have time."
    
    print(make_bread())
    
    c: 继续执行
    w: 显示当前正在执行的代码行的上下文信息
    a: 打印当前函数的参数列表
    s: 执行当前代码行，并停在第一个能停的地方（相当于单步进入）
    n: 继续执行到当前函数的下一行，或者当前行直接返回（单步跳过）
    
    s: 单步进入，会进入当前行调用的函数内部并停在里面
    n: 单步跳过，会执行完毕当前行调用的函数，停在当前函数的下一行

