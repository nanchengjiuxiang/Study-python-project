# 计算圆的面积---> radius 形参(形式参数)：函数定义时括号内的参数，只能在函数内使用（局部变量）；调用函数时传入的参数为实参(实际参数)
def circle_area(radius):
    area = 3.14 * radius * radius
    return area
# 调用函数---> 5 实参(实际参数)：函数调用时传入的参数，实参可以是常量、变量、表达式等
c_area = circle_area(5)
print("圆的面积为：", c_area)


# 计算长方形的面积---> 多个参数时用“ ，”分隔
def rectangle(width,hight):
    area = width * hight
    return area
# 调用函数
r_area = rectangle(5,5)
print("长方形的面积为：", r_area)