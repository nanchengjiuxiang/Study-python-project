"""
break:不能单独书写，只能出现在循环中，表示结束 跳出的意思
continue:不能单独书写，只能出现在循环中，表示中断本次循环，直接进入下一次循环"""


#根据用户输入的账号和密码执行登录操作--->正确的用户名和密码为admin/666888  zhangsan/123456  taoge/888666
while True:
#接受输入的用户名和密码
    account = input("请输入用户名：")
    password = input("请输入密码：")

#校验：输入的用户名或密码不能为空
    if account == "" or password == "" :
        print("账号或密码不能为空,重新输入")
        continue  #中断本次循环，直接进入下一次循环

#判断用户名和密码正确性
    if account == "admin" and password == "666888" :
        print("登陆成功~~~~")
        break #跳出循环
    elif account == "zhangsan" and password == "123456":
        print("登陆成功~~~~")
        break #跳出循环
    elif account == "taoge" and password == "888666":
        print("登陆成功~~~~")
        break #跳出循环
    else :
        print("账号或密码错误")

