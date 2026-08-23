# 字典储存的是键值对(key:value)类型数据，可以更具键（key）找到对应的值(value)
# 字典是一种可变、无序（Python 3.7+ 为插入有序）、键唯一的键值对集合。
# 字典当中得到value可以为任意数据类型，而key不能为可变类型（如 不能为列表list，集合set，字典dict）---unhashable type: 'list'

# 定义字典---key不能重复(如果重复，后面的值会覆盖前面的值)
# dict1 = {"王林":670, "李慕婉":608, "徐立国":580, "韩立":688}
# print(dict1)
# print(type(dict1))
#
# # 访问
# print(dict1["李慕婉"])
# dict1["李慕婉"] = 700
# print(dict1["李慕婉"])


# ---------------------------------------------常用操作------------------------------------------------------
# dict1 = {"王林":670, "李慕婉":608, "徐立国":580, "韩立":688}
# print(dict1)
# # 1.添加---字典名称[key]= value   往指定字典中添加key-value键值对
# dict1["涛哥"] = 550
# print(dict1)
#
# # 2.删除---pop(key)   删除字典中指定的key,并返回该key对应的value
# score = dict1.pop("徐立国")
# print(score)
# print(dict1)
# #      ---del 字典名称[key]   删除字典中指定的键值对
# del dict1["韩立"]
# print(dict1)
#
#
# # 3.修改---字典名称[key]= value   修改字典中指定的key对应的值
# dict1["涛哥"] = 620
# print(dict1)
#
# # 4.查询---字典名称[key]   根据key获取value
# print(dict1["涛哥"])
# #      ---字典名称.get(key)    根据key获取value
# print(dict1.get("涛哥"))
# #      ---字典名称.keys()    获取所有的key
# print(dict1.keys())
# #      ---字典名称.values()    获取所有value
# print(dict1.values())
# #      ---字典名称.items()    获取所有的key-value键值对
# print(dict1.items())


# 遍历
# dict1 = {"王林":670, "李慕婉":608, "徐立国":580, "韩立":688}
# # 方法一
# for k in dict1.keys():
#     print(f"{k} : {dict1.get(k)}")
# print()
# # 方法二
# for k , v in dict1.items():
#     print(f"{k} : {v}")
# print()
# # 方法三
# for item in dict1.items():
#     print(f"{item[0]} : {item[1]}")



# -----------------------------------------------------案例--------------------------------------------------------

# 开发一个购物车管理系统,实现商品信息的添加、修改、删除、查询功能。系统使用字典结构存储商品数据,
# 通过控制台菜单与用户交互。具体功能如下:
#   1. 添加购物车:用户根据提示录入商品名称、以及该商品的价格、数量,保存该商品信息到购物车。
#   2. 修改购物车:要求用户输入要修改的购物车商品名称,然后再提示输入该商品的价格、数量,输入完成后修改该商品信息。
#   3. 删除购物车:要求用户输入要删除的购物车名称,根据名称删除购物车中的商品。
#   4. 查询购物车:将购物车中的商品信息展示出来,格式为:“商品名称:xxx,商品价格:xxx,商品数量:xxx"。
#   5. 退出购物车

shopping_cart = {}

# 制作菜单
print("欢迎使用购物车管理系统~")
mune = """
##########购物车系统##########
#        1. 添加购物车        #
#        2. 修改购物车        #
#        3. 删除购物车        #
#        4. 查询购物车        #
#        5. 退出购物车        #
#############################
"""

# 执行的操作
while True:
    print(mune)   # 输出菜单
    operation = input("请输入你要执行的操作(1-5):")

    match operation :   # 匹配要执行的操作

        # 1. 添加购物车
        case "1":
           goods_name = input("输入添加的商品名称:")

            # 判断商品是否存在
           if goods_name in shopping_cart:
               print(f"{goods_name} 已经存在，请重新选择")
               continue

           goods_prise = float(input("输入商品价格:"))
           goods_num = int(input("输入商品数量:"))
           shopping_cart[goods_name] = {"prise": goods_prise, "num": goods_num}
           print(f"商品 {goods_name} 添加成功")

        # 2. 修改购物车
        case "2":
            goods_name = input("输入要修改商品的名称:")
            if goods_name in shopping_cart:
                new_goods_prise = float(input("输入修改后的价格:"))
                new_goods_num = int(input("输入修改后的数量:"))
                shopping_cart[goods_name] = {"prise": new_goods_prise, "num": new_goods_num}
            else :
                print("商品不存在!!!!!")

        # 3. 删除购物车
        case "3":
            goods_name  =input("输入要删除的商品名称:")
            if goods_name in shopping_cart:
                del shopping_cart[goods_name]
                print("删除成功~")
            else :
                print("商品不存在!!!!!")

        # 4. 查询购物车
        case "4":
            for name in shopping_cart.keys():
                goods_items = shopping_cart[name]
                print(f"商品名称：{name}  商品价格：{goods_items["prise"]}  商品数量：{goods_items["num"]}")

        # 5.退出购物车
        case "5":
            print("购物车已退出")
            break
        case _:
            print("错误选择")






















