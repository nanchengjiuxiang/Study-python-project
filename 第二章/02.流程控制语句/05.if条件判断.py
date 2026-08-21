# #if条件判断案例   如果分数超过680，那么就去读清华
# score = 700
# if score >680:
#     print("我要去读清华")
#     print("欢迎")
# print("--------------------------------------------")
#
#
# #案例，登录页面 : 账号/密码为 188888888/666888
# account = int(input("请输入你的账号："))
# password = int(input("请输入你的密码："))
# if password == 666888:
#     print("密码正确")
# else:
#     print("密码错误")
# if account == 188888888:
#     print("账号正确")
# else:
#     print("账号错误")
# if account == 188888888 and password == 666888:
#     print("登录成功")
#
from xml.sax.handler import feature_external_ges

# #根据用户输入的年份，判断是闰年还是平年
# year = int(input("请输入年份："))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print(f"{year}年份为闰年")
# else:
#     print(f"{year}年份是平年")



# #根据用户输入的数字，判断是奇数还是偶数
# num = int(input("请输入数字："))
# if num % 2 == 0 :
#     print(f"{num}是偶数")
# else:
#     print(f"{num}是奇数")
#


#
# #根据用户输入的数字判断是正数还是负数----->if...elif...else
# num = int(input("请输入数字："))
# if num > 0:   #判断是否为正数
#     print(f"{num}是正数")
# elif num == 0:   #判断是否为0
#     print(f"{num}既不是正数也不是负数")
# else:   #既不是0也不是正数，那就是负数
#     print(f"{num}是负数")


# 登录系统---->账号密码为admin/666888或root/547527或hangman/123456
# ture_account01 = "admin"
# ture_password01 = "666888"
# ture_account02 = "root"
# ture_password02 = "547527"
# ture_account03 = "hangman"
# ture_password03 = "123456"
# account = input("请输入账号：")
# password = input("请输入密码：")
# if account == ture_account01 and password == ture_password01:
#     print("登录成功")
# elif account == ture_account02 and password == ture_password02:
#     print("登录成功")
# elif account == ture_account03 and password == ture_password03:
#     print("登录成功")
# else:
#     print("账号或密码错误")



# # 案例：三角形类型判断--->版本1
# len01 = int(input("请输入边长01："))
# len02 = int(input("请输入边长02："))
# len03 = int(input("请输入边长03："))   #获取三边长
# if len01 + len02 < len03 or len01 + len03 < len02 or len03 + len02 < len01:   #判断是否可以组成三角形
#     print("该三边不构成三角形")
# elif len01 == len02 == len03:   #三边相等为等边三角形
#     print("该三角形为等边三角形")
# elif len01 == len03 or len01 == len02 or len02 == len03:   #任意两边相等为等腰三角形
#     print("该三角形为等腰三角形")
# else:
#     print("该三角形为普通三角形")


# #版本2
# a = int(input("输入边长："))
# b = int(input("输入边长："))
# c = int(input("输入边长："))
# if a + b > c and b + c > a and c + a > b:
#     print("可以构成三角形")
#     if a == b == c:
#         print("该三角形为等边三角形")
#     elif a == b or b == c or c == a:
#         print("该三角形为等腰三角形")
#     else:
#         print("该三角形为普通三角形")
# else:
#     print(f"{a} {b} {c} 不构成三角形")



#根据输入的用电度数，计算电费
kwh = int(input("请输入用电度数："))
if kwh <= 2880:
    fee = kwh * 0.4883
elif 2880 < kwh <= 4000:
    fee = (kwh-2880) * 0.5383 + 2880 * 0.4883
else:
    fee = (kwh-4000) * 0.7883 + 2880 * 0.4883 +(4000-2880)*0.5383
print(f"用电费用为{fee}")















