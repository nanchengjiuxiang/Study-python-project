# 魔法方法是指Python中提供的以双下划线开头和结尾的特殊方法, 用于定义类的特殊行为, 比如: __init__
# 魔法方法是不需要我们手动调用的, Python会在合适的时机自动调用。

# 定义类
class Car:
    # __ init __: 初始化方法,对象创建后自动调用,主要用于设置对象的初始状态(设置对象属性)
    # self:方法的第一个参数,表示当前创建的实例对象
    def __init__(self, color, brand, name, price):
        self.color = color
        self.brand = brand
        self.name = name
        self.price = price

    # 定义实例方法
    def running(self, rate):
        print(f"{self.color}的{self.brand}{self.name}正在以{rate}速度行驶！")

    def __str__(self):
        return f"{self.color}的{self.brand}{self.name}价格为{self.price}"

    def __eq__(self, other):
        return self.color == other.color and self.brand == other.brand and self.name == other.name

    def __lt__(self, other):
        return self.price < other.price

c1 = Car("白色", "BMW", "X7", 500000)
print(c1)
print(c1.__dict__)
c2 = Car("红色", "奔驰", "E300L", 1000000)
print(c2)
print(c2.__dict__)

print(c1 == c2)   # False

c3 = Car("白色", "BMW", "X7", 500000)
print(c1 == c3)

print(c1 > c2)   # False
print(c1 < c2)   # True