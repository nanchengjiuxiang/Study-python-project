# 异常传递就是异常在函数调用中层层上报的过程,直到有人处理它,或者程序崩溃。

def fun1():
    print("fun1 --- running ---")
    fun2()

def fun2():
    print("fun2 --- running ---")
    fun3()

def fun3():
    print("fun3 --- running ---")
    print(name)

try:
    fun1()
except:
    print("程序出错")