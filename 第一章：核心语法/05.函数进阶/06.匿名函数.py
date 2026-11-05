# 匿名函数指的是没有名称的函数,需要通过lambda表达式来声明函数,可以简化简单函数的编写(单行表达式)。
# 注意:函数逻辑比较简单(单行表达式)且只在一个地方使用时,可以考虑使用匿名函数,简化书写(通常作为高阶函数的参数使用)。

# 1. 打印一行分割线
def out_line():
    print("-------------------------命名函数-------------------------")
# 函数调用
out_line()

# 匿名函数
line = lambda: print("-------------------------匿名函数-------------------------")
# 函数调用
line()


# 2. 计算两个数之和
def num_add(a,b):
    return a+b
print(num_add(10,20))

# 匿名函数
add = lambda a, b : a+b
print(add(10,20))




# 需求3:完成如下列表的排序操作,按照每一个元素的字符个数,从小到大排序;
data_list = ["C++", "C", "Python", "Jack", "PHP", "Java", "Go", "JavaScript", "Rust"]

data_list.sort(key=lambda item: len(item))
print(data_list)