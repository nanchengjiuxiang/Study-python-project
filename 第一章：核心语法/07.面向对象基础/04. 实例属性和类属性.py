# 实例属性: 实例属性属于每个具体对象的属性, 每个对象都是独立的。(各个对象特有的数据)
# 类属性: 类属性是属于类本身的属性, 所有实例共享的。(所有对象共享的数据或配置)

# 定义类
class Car:
    # 类属性
    wheel_num = 4
    cost_rate = 0.1
    def __init__(self, color, brand, name, price):
        # 实例属性
        self.color = color
        self.brand = brand
        self.name = name
        self.price = price

    # 定义实例方法
    def running(self, rate):
        print(f"{self.color}的{self.brand}{self.name}正在以{rate}速度行驶！")

    def total_cost(self, discount, cost_rate):
        """
        用于计算车辆购买的总价
        :param discount: 车辆折扣
        :param rate: 车辆购置税
        :return: 车辆购买的总价
        """
        cost = self.price  * discount + self.price * cost_rate
        return cost


c1 = Car("白色", "奔驰", "E300L", 500000)
print(c1.brand)
print(c1.wheel_num)
print(c1.cost_rate)

# 通过类名访问类属性
print(Car.wheel_num)
print(Car.cost_rate)