#运算符  >  <  !=  ==  <=  >=
print("100==100吗",100==100)  # True
print("100>100吗",100>100)   # False
print("100<100吗",100<100)   # False
print("100!=100吗",100!=100)  # False
print("100>=100吗",100>=100)  # True
print("100<=100吗",100<=100)  # True

# #判断一个数的奇偶
num = int(input("请输入一个整数:"))
if num%2==0:
    print(num,"是偶数")
else:
    print(num,"是奇数")


# 输入一个值，判断是否在10到20之间
num1 = int(input("请输入一个数："))
print(f"{num1}在10到20之间：", 10 < num1 < 20)
#输入一个数，判断是否在10到20之外
num2 = int(input("请输入一个数："))
print(f"{num2}在10到20之外：", num2 < 10 or num2 > 20)









