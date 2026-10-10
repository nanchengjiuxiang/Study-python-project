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

    def total_cost(self, discount, rate):
        """
        用于计算车辆购买的总价
        :param discount: 车辆折扣
        :param rate: 车辆购置税
        :return: 车辆购买的总价
        """
        cost = self.price  * discount + self.price * rate
        return cost


c1 = Car("白色", "奔驰", "E300L", 500000)
c1.running(120)
print(c1.total_cost(0.5, 0.75))