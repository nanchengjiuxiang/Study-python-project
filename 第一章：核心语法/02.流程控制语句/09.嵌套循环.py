"""外层循环控制行数，而内层循环控制每行数目"""

# 打印长为m，宽为n的长方形
m = int(input("请输入长度："))
n = int(input("请输入宽度："))
for i in range(n):   #控制行数
    for j in range(m):   #控制每行数目
        print("*",end=" ")
    print()


# 打印99乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j} * {i} = {j * i}",end="\t")
    print()


# 根据输入的边长，生等腰直角三角形
l = int(input("请输入边长："))
for i in range(1,l+1):
    for j in range(1,i):
        print("*",end="\t")
    print("*")


# 根据输入的数字打印对应的数字金字塔
num = int(input("输入数字："))

for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


