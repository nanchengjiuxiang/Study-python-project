# -----------------------------------------------------案例一--------------------------------------------------------
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