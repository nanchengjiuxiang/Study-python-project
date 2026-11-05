# 定义一个函数,根据传入的数字,计算该数字阶乘的结果 ---> f(n) = n * f(n - 1)
# 递归(Recursion)调用:指的是在函数中自己调用自己的情况 (先层层递进,再逐层回归) ---> 终结点

def factorial(n):   # f(n) = n * f(n - 1)
    """
    根据传入的数字,计算该数字阶乘的结果
    :param n: 需要计算的数字
    :return: 阶乘结果
    """
    if n == 1:   # 终结点为1，f(1) = 1
        return 1
    else:
        return n * factorial(n - 1)

print(f"10 的阶乘为 {factorial(10)}")