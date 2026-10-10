"""
嵌套调用指的是在一个函数中,又调用了另外一个函数。
函数调用遵循栈结构,最后被调用的函数最先返回LIFO(Last In First Out,后进先出)
"""
def function_a() :
    print("a...before")
    function_b()
    print("a...after")

def function_b() :
    print("b...before")
    function_c()
    print("b...after")

def function_c() :
    print("c...")

function_a()
print("函数调用完毕")