# set是一种无序的，不可重复的，可修改的数据容器
# 注意：{}定义的不是集合，而是空字典；由于集合是无序的因此是不支持索引访问的---->定义空集合: s = set()
s1 = {0,10,20,50,1,0,50,2,0}
print(s1)
print(s1)
print(type(s1))

#定义空集合
s2 = set()
print(type(s2))




# --------------------------------------------------常用方法----------------------------------------------
s1 = {100,200,300,400,500,600,700,800,900}

#add(item)	添加单个元素
s1.add(1000)
print(s1)

#remove(item)	删除指定元素
s1.remove(200)
print(s1)

# pop()	随机删除并返回一个元素
e = s1.pop()
print(s1)
print(e)

#clear()	清空集合所有元素
s1.clear()
print(s1)

#并集（Union）  两个集合的所有元素，自动去重。  运算符：|  方法：union()
s2 = {"A","B","C","D","E","X","Y"}
s3 = {"C","E","Y","Z"}
print(s2.union(s3))

#交集（Intersection）  两个集合共同拥有的元素。  运算符：&  方法：intersection()
print(s2.intersection(s3))

# 差集（Difference）  属于 A 但不属于 B 的元素。  运算符：-  方法：difference()
print(s2.difference(s3))
print(s3.difference(s2))
print(s2-s3)
print(s3-s2)







# -------------------------------------------------案例------------------------------------------------------
# 选修足球学生名单
football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
# 选修篮球学生名单
basketball_set = {"张铁", "墨居仁", "王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
# 选修法语学生名单
french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子", "红蝶", "厉飞雨", "韩立", "曾牛"}
# 选修艺术学生名单
art_set = {"遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}

# 找出同时选修法语和艺术的学生---> 交集 intersection   &
# french_art = french_set.intersection(art_set)
# print(f"同时选修法语和艺术的学生有：{french_art}")
french_art_2 = french_set & art_set
print(f"同时选修法语和艺术的学生有：{french_art_2}")

# 找出同时选修了四门课程的学生---> 交集 intersection   &
# four_class = football_set.intersection(basketball_set).intersection(art_set).intersection(french_set)
# print(f"同时选修了四门课程的学生有{four_class}")
four_class_2 = football_set & basketball_set & art_set & french_set
print(f"同时选修了四门课程的学生有{four_class_2}")

# 找出选修了足球但是没有选修篮球的学生---> 差集 difference   -
# 方式一
# football_not_basketball = football_set.difference(basketball_set)
# print(f"选修了足球但是没有选修篮球的学生{football_not_basketball}")
# 方式二
football_not_basketball_2 = football_set - basketball_set
print(f"选修了足球但是没有选修篮球的学生{football_not_basketball_2}")
# 方式三---> 集合推导式  快速构建集合    语法: {s for s in set if 条件}
# football_not_basketball_3 = {i for i in football_set if i not in basketball_set}
# print(f"选修了足球但是没有选修篮球的学生{football_not_basketball_3}")

# 统计每一位学生选修的课程数量
# 1.获取到学生名单---> 并集  |
students = football_set | basketball_set | art_set | french_set

# 2.获取每一位学生选修的课程数量
all_list = [*football_set, *basketball_set, *art_set, *french_set]
for s in students:
    print(f"{s} 同学选修了 {all_list.count(s)} 个课程")















