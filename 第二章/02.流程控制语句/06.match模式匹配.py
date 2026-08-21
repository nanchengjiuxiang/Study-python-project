# day = int(input("输入星期几（1-7）："))
# match day:
#     case 1:
#         print("星期一")
#     case 2:
#         print("星期二")
#     case 3:
#         print("星期三")
#     case 4:
#         print("星期四")
#     case 5:
#         print("星期五")
#     case 6|7:
#         print("周末")
#     case _ :
#         print("格式错误")


#简易计算器
num1 = float(input("请输入第一个数："))
num2 = float(input("请输入第二个数："))
oper = input("请输入运算符（* / - + **）：")
match oper:
    case "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    case "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    case "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    case "/" if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    case "**":
        print(f"{num1} ** {num2} = {num1 ** num2}")
    case _ :
        print("请按照要求输入运算符或数字")




















