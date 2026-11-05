# 切片
str1 = "python"
str2 = "hello"
print(str1[0:4:2])
print(str2[0:])

print(str1[-1:-6:-1])

print(str1[0:6:1])
print(str1[0:6:])
print(str1[0:6])
print(str1[:6])

#获取元素
print(str1[4])
print(str2[-2])

#迭代
for i in str1:
    print(i)








# ------------------------------------------常用方法-------------------------------------
s = "Hello-Python-Hello-World"

#find() 查找指定字符串第一次出现的位置
index = s.find("Python")
print(index)  #6

#count() 统计子字符串在字符串中出现的次数
c = s.count("o")
print(c)  #4

#upper() 转换为大写
su = s.upper()
print(su)  #HELLO-PYTHON-HELLO-WORLD

#lower() 转换为小写
sl = s.lower()
print(sl)  #hello-python-hello-world

#split() 将字符串按照指定位置切割--列表
slist = s.split("-")
print(slist)

#strip() 去除字符串两端的空格
ss = s.strip()
print(ss)

#replace() 用另一段字符串来替换字符串
sr = s.replace("-","_")
print(sr)

#startswith()/endswith() 判断字符串是否以指定字符开头/结尾--布尔值
print(s.startswith("Hello"))
print(s.endswith("Python"))




# --------------------------------案例-----------------------------------
# 邮箱格式判断
mail = input("输入你的邮箱：")
if mail.count("@") == 1 and "." in mail:
    print("邮箱格式正确")
else:
    print("格式错误")





str = "hello"
lis = list(str)
print(lis)
print(type(lis))










