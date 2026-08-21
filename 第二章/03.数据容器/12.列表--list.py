"""
特点:可以存储不同类型的元素
    元素有序，可以重复，元素可以修改
"""

# #定义列表--list
# s = [55,58,88,90,"a","hello",True]
# #查询类型
# print(type(s))

#访问列表中的元素
# #获取--s[ ]
# print(s[0])  #获取第一个元素--55,正向索引
# print(s[-7]) #反向索引

# print(s[5])  #获取第六个元素--"hello",正向索引
# print(s[-2]) #反向索引

# print(s[6])  #获取第六个元素--True,正向索引
# print(s[-1]) #反向索引

# print(len(s))   #获取列表长度--->len( )

# #修改
# s[4] = "ABC"  #指定位置修改；如果指定的索引超出范围，将会报错--IndexError: list assignment index out of range
# print(s)

# #删除--del
# del s[5]   #删除元素"hello"
# print(s)

# #遍历列表
# for item in s :
#     print(item,end="  ")




# #切片：指的是对操作的数据截取一部分来操作--->序列数据[开始索引 : 结束索引 : 步长]  不包含结束索引索位置的数据
# s = ["a","b","c","d","e","f","g","h","i","j"]
# cut_s01 = s[0:5]   #切片，取其中索引0到5之间(不包含5)的数据
# cut_s02 = s[:10:2]
# print(cut_s01)
# print(cut_s02)
# print(type(cut_s01))





# """列表的常见方法
# 1. append()--->在列表的尾部追加元素
# 2. insert()--->在指定索引之前，插入该元素
# 3. remove()--->移除列表中第一个匹配到的值
# 4. pop()--->删除列表中指定索引位置的元素（如未指定元素，默认删最后一个）
# 5. sort()--->对列表进行排序（列表元素类型一致，才可以进行排序）
# 6. reverse()--->反转列表元素"""

# #定义列表
# s = [56,90,88,65,90,100,209,72,145]
# print(s)

# #append()--->在列表的尾部追加元素
# s.append(188)
# print(s)   #[56,90,88,65,90,100,209,72,145,188]

# #insert()--->在指定索引之前，插入该元素
# s.insert(2,88)
# print(s)   #[56,90,88,88,65,90,100,209,72,145,188]

# #remove()--->移除列表中第一个匹配到的值
# s.remove(90)
# print(s)   #[56,88,88,65,90,100,209,72,145,188]

# #pop()--->删除列表中指定索引位置的元素（如未指定元素，默认删最后一个）
# e = s.pop(1)
# print(e)   #88
# s.pop()
# print(s)   #[56,88,65,90,100,209,72,145]

# #sort()--->对列表进行排序（列表元素类型一致，才可以进行排序）
# s.sort()
# print(s)   #[56,65,72,88,90,100,145,209]

# #reverse()--->反转列表元素
# s.reverse()
# print(s)    #[209,145,100,90,88,72,65,56]




#案例1--->sum() 求和 ； len() 获取元素个数 ； min() 最小值 ； max() 最大值
# num_list = []
# num = int(input("输入你要输入的数字总数目："))
# for i in range(num):
#     e = int(input(f"请输入第{i+1}数字："))
#     num_list.append(e)
# average = sum(num_list) / len(num_list)
# num_list.sort()
# print("数字列表：",num_list)
# print(f"输入数字中最小值为 {num_list[0]} ,最大值为 {num_list[-1]} ,平均值为 {average}")



#案例2:合并列表并去重
# num_list1 = [19,23,54,64,875,20,109,232,123,54]
# num_list2 = [55,80,72,35,60,123,54,29,91]
#
# #合并列表
# for num in num_list2:
#     num_list1.append(num)
# print(f"合并后的列表为 {num_list1}")
#
# #将列表转化为集合进行去重------>方法一
# num_set = set(num_list1)
# list_new = list(num_set)
# list_new.sort()
# print(f"去重后列表为{list_new}")
#
# #去重------>方法二
# new_list = [] #去重后的列表
# for j in num_list1:
#     if j not in new_list:  #判断元素j是否在列表new_list中
#         new_list.append(j)
# new_list.sort()
# print(f"去重后列表为{new_list}")


#简化

# num_list1 = [19,23,54,64,875,20,109,232,123,54]
# num_list2 = [55,80,72,35,60,123,54,29,91]



# #合并列表---->解包：将列表这一个容器解包成一个一个独立的元素
# #组包：将多个值合并为一个整体
# num_list = [*num_list1 , *num_list2]
# print(f"合并后的列表为 {num_list}")



# #去重------>方法二
# new_list = [] #去重后的列表
# for j in num_list:
#     if j not in new_list:  #判断元素j是否在列表new_list中
#         new_list.append(j)
# new_list.sort()
# print(f"去重后列表为{new_list}")


#简化
# num_list1 = [19,23,54,64,875,20,109,232,123,54]
# num_list2 = [55,80,72,35,60,123,54,29,91]
#
# #合并
# num_list = num_list1 + num_list2
# print(f"合并后的列表为 {num_list}")
#
# #去重
# new_list = [] #去重后的列表
# for j in num_list:
#     if j not in new_list:  #判断元素j是否在列表new_list中
#         new_list.append(j)
# new_list.sort()
# print(f"去重后列表为{new_list}")



#生成1-20的平方列表
# s = []
# for i in range(1,21):
#     s.append(i**2)
# print(f"1到20的平方列表为 {s} ")

#方式二：列表推导式--->[要插入的值 for i in 序列/列表]
# s2 = [i**2 for i in range(1,21)]
# print(f"1到20的平方列表为 {s2} ")


#
# #提取表中所有偶数，并计算其平方，组成新的列表
# num_list = [19,23,54,64,87,109,232,123,43,26,55,72]
# new_list = []
# for num in num_list:
#     if num % 2 == 0:
#         num = num ** 2
#         new_list.append(num)
# print(f"原列表为 {num_list} ,提取偶数并计算平方后的新列表为 {new_list}")

# num_list = [19,23,54,64,87,109,232,123,43,26,55,72]
# new_list = [i**2 for i in num_list if i%2 == 0]
# print(new_list)











