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





# 






































