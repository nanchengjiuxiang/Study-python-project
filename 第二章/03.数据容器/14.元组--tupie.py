#元组是不可变序列，类似于列表，但创建后不能修改----可重复，有序，不可修改

# t1 = (20,22,55,56,45,55,54,85,669,55)
# print(t1)
# print(type(t1))   # <class 'tuple'>
#
# #索引访问
# print(t1[0])
# print(t1[5])
# print(t1[-2])
#
# #切片
# print(t1[:-5])
# print(t1[0:5:2])
#
# #count() 统计元素串在元组中出现的次数
# print(t1.count(55))
# print(t1.count(56))
# print(t1.count(00))
#
# #index() 查找元素在元组中出现的位置
# print(t1.index(55))
# print(t1.index(56))

#定义空元组----注意:如果需要定义单元素元组，那单元素后面需要加上逗号，   (100,)
# t2 = ()
# print(t2)
# print(type(t2))   #<class 'tuple'>
#
# t3 = (100)
# print(t3)
# print(type(t3))   # <class 'int'>
#
# t4 = (100,)
# print(t4)
# print(type(t4))   #<class 'tuple'>




#--------------------------------------组包(packing)与解包(unpacking)--------------------------------------------------

#定义元组，组包
# t1 = (5,7,9,10,2,23,12)
# #定义元组，组包
# t2 = 5,7,9,10,2,23,12
#
# print(t1)
# print(t2)
#
# #基础解包
# a , b , c , d , e , f , g = t1
# print(a , b , c , d , e , f , g )
#
# # (*)扩展解包--->在扩展解包时，*表示收集剩余的所有元素，允许我们处理不确定的元素（生成列表，以便可以进一步地处理）
# h,i,*j,k = t1
# print(h,i,j,k)
# l,m,*n = t1
# print(l,m,n)



# 变量值互换
# a = 10
# b = 20
# a, b = b, a
# print(a, b)



# -----------------------------------------------案例--------------------------------------------------------
print("学号\t姓名\t语文\t数学\t英语\t总分\t均分")
students = (
    ("S001", "王林", 85, 92, 78),
    ("S002", "李慕婉", 92, 88, 95),
    ("S003", "十三", 78, 85, 82),
    ("S004", "曾牛", 88, 79, 91),
    ("S005", "周轶", 95, 96, 89),
    ("S006", "王卓", 76, 82, 77),
    ("S007", "红蝶", 89, 91, 94),
    ("S008", "徐立国", 75, 69, 82),
    ("S009", "许木", 86, 89, 98),
    ("S010", "遁天", 66, 59, 72),
)
#统计各学生的均分和总分
#方式一
# for s in students:
#     total = s[2] + s[3] + s[4]
#     ave = total / 3
#     print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{total}\t{ave:.1f}")

#方式二---> 元组解包
for nid,name,ch,ma,en in students:
    total = ch + ma + en
    ave = total / 3
    print(f"{nid}\t{name}\t{ch}\t{ma}\t{en}\t{total}\t{ave:.1f}")
print()


#获取各科分数列表
ch_scores = [i[2] for i in students]
ma_scores = [i[3] for i in students]
en_scores = [i[4] for i in students]

#输出最低分最高分和均分
print(f"语文最高分为{max(ch_scores)}，最低分为{min(ch_scores)}，均分为{sum(ch_scores) / len(ch_scores)}")
print(f"数学最高分为{max(ma_scores)},最低分为{min(ma_scores)}，均分为{sum(ma_scores) / len(ma_scores)}")
print(f"英语最高分为{max(en_scores)},最低分为{min(en_scores)}，均分为{sum(en_scores) / len(en_scores)}")
print()

#判断优秀学生（均分大于90）
for s in students:
    total = s[2] + s[3] + s[4]
    ave = total / 3
    if ave >90 :
            print(f"优秀学生为 {s[1]} ，均分为 {ave:.1f} ")