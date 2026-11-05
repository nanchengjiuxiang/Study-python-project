# __ all __ 是一个模块级别的特殊变量,用于指定 from 模块名 import *时会导入哪些功能(*通配了哪些功能)。
__all__ = ["separator1", "separator2", "separator4", "PI"]

# 定义常量
PI = 3.1415926

# 定义函数
def separator1():
    print("_ " * 30)

def separator2():
    print("# " * 30)

def separator3():
    print("* " * 30)

def separator4():
    print("^ " * 30)


# 测试函数
# __name__ ---> python中的内置变量，表示当前模块的名字
# 直接运行当前模块，__name__的值为"__main__"; 当模块被导入是__name__的值就是模块的名称
if __name__ == "__main__":
    separator1()

