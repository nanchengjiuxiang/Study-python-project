"""
介绍:不定长参数也叫可变参数,用于函数定义及调用时参数个数不确定(0个或多个)的场景。

类型:
 1. 位置传递(*args)---> 注意:传递的所有匹配的位置参数都会被变量收集,这些参数会合并封装为一个元组,是元组类型(注意并不会封装关键字参数)。
 2. 关键字传递(**kwargs)---> 注意:传递的所有匹配的关键字参数都会被变量收集,这些参数会合并封装为一个字典,是字典类型(注意并不会封装位置参数)
。"""

# 位置传递
def calc_date(*arges):
    max_value = max(arges)
    min_value = min(arges)
    average = round(sum(arges) / len(arges) , 2)
    return max_value, min_value, average

max_d,min_d,avg_d = calc_date(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(f"最大值:{max_d},最小值:{min_d},平均值:{avg_d}")



# 关键字传递
def calc_value(*arges, **kwargs):
    """
    根据传入的数据计算数据的最大值，最小值，平均值
    :param arges: 要计算的数据（不定长位置参数）
    :param kwargs: 不定长关键字参数
        round: 保留的小数位个数
        print: 是否打印结果（True or False）
    :return: 最大值，最小值，平均值
    """
    max_value = max(arges)
    min_value = min(arges)
    ave_value = sum(arges) / len(arges)

    if kwargs.get("round") is not None:
        ave_value =  round(sum(arges) / len(arges), kwargs.get("round"))
    if kwargs.get("print") :
        print(f"最大值:{max_value},最小值:{min_value},平均值:{ave_value}")

    return max_value, min_value, ave_value

print(calc_value( 2, 3, 4, 5, 6, 7, 8, 9, 10, round = 3, print =True))