# 加法运算
def add(a,b):
    return a+b
# 减法运算
def subtract(a,b):
    return a-b
# 乘法运算
def multiply(a,b):
    return a*b
# 除法运算
def divide(a,b):
    return a/b

# 计算
def calc(x, y, oper):
    return oper(x,y)

print(calc(10, 20, add))
print(calc(10, 20, subtract))
print(calc(10, 20, multiply))
print(calc(10, 20, divide))
