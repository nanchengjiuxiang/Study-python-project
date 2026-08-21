#while循环语法结构
# a = 0
# while a <= 50:
#     print(a,end=" ")
#     print("循环第一次")
#     a += 1
# else :
#     print("循环结束")


#打印十遍，人生苦短，我用python
# i = 0
# while i < 10:
#     print("人生苦短，我用python~~~")
#     i += 1
# else :
#     print("循环正常结束")


#计算1——100之间的偶数累加
total = 0   #记录累加之和
i = 1   #循环开始的数字
while i <= 100:
        if i % 2 == 0:
            total += i
        i += 1
else:
    print(f"累加之和为{total}")


a = 1
b = 0
if a % 2 == 0:
    while a <= 100:
        b += a
        a += 2
    else :
        print(f"累加之和为{b}")
else:
    a +=1
    while a <= 100:
        b += a
        a += 2
    else :
        print(f"累加之和为{b}")















