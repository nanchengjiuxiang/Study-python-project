# 计算圆的面积以及圆的周长---> 如果返回值有多个，会封装到元组中
def circle_area_len(radius):
    """
    该函数用于根据圆的半径，计算圆的面积和周长
    :param radius:圆的半径
    :return:圆的面积，圆的周长
    """
    area = 3.14 * radius * radius
    perimeter = round(2 * radius * 3.14, 2)
    return area, perimeter

# 调用函数
print(f"圆的面积为 {circle_area_len(5)[0]} ,圆的周长为 {circle_area_len(5)[1]}")


# 计算长方形的面积---> 多个参数时用“ ，”分隔
def rectangle(width,length):
    """
    该函数用于根据长方形的长度和宽度，计算长方形的面积
    :param width: 宽度
    :param length: 长度
    :return: 长方形的面积
    """
    area = width * length
    return area
# 调用函数
r_area = rectangle(5,5)
print("长方形的面积为：", r_area)