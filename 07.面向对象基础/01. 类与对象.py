# 说明:类名的命名规范, 遵循大驼峰命名法, 每个单词的首字母都是大写, 单词之间没有分隔符, 比如:UserInfo, UserAccount。
# 说明 :__ dict __ 是Python中用户自定义类实例的一个特殊属性, 用于以字典形式存储对象的属性。
from idlelib.multicall import MC_COLORMAP


# 定义类(方法一) ---> 不推荐 动态的为对象添加属性
class Car:
    pass

# 创建对象
c1 = Car()
# 动态的为对象添加属性
c1.color = "red"
c1.brand = "BMW"
c1.name = "X5"
c1.price = 500000
print(c1)
print(c1.__dict__)


# 定义类(方法二)
class Car:
    # __ init __: 初始化方法,对象创建后自动调用,主要用于设置对象的初始状态(设置对象属性)
    # self:方法的第一个参数,表示当前创建的实例对象
    def __init__(self, color, brand, name, price):
        self.color = color
        self.brand = brand
        self.name = name
        self.price = price
        print("Car类型对象初始化完毕，对象属性添加完毕")

# 为对象添加属性
c2 = Car("white", "BMW", "X8", 1000000)
print(c2)
print(c2.__dict__)

c3 = Car("white", "奔驰", "E300L", 700000)
print(c3)
print(c3.__dict__)