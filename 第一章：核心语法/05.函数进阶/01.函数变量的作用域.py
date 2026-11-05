# 全局变量
num = 10

# 计算圆的面积---> radius 形参(形式参数)：函数定义时括号内的参数，只能在函数内使用（局部变量）；调用函数时传入的参数为实参(实际参数)
def circle_area(radius):
    # 局部变量 : 只能在函数内部使用
    pi = 3.14
    area = pi * radius * radius

    num = 10000
    print("num = ",num)

    return area

# 调用函数---> 5 实参(实际参数)：函数调用时传入的参数，实参可以是常量、变量、表达式等
c_area = circle_area(num)
print("圆的面积为：", c_area)

print("num = ", num)






# 定义全局变量
num1 = 1

# 定义函数
def func():
    # 函数中使用全局变量num1---> global (在基于global声明全局变量时，要先声明，再使用)
    global num1
    num1 = 1000   # 全局变量
    print("num1 = ",num1)

func()
print("num1 = ",num1)




# 定义全局变量
num2 = 1

# 定义函数
def func2():
    num2 = 1000   # 局部变量
    print("num2 = ",num2)

func2()
print("num2 = ",num2)