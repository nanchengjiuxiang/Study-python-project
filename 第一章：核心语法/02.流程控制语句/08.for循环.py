# 定义所需要遍历的字符串
msg = input("输入要遍历的字符串：")
#遍历字符串并处理
for i in msg :   # i 表示遍历出来的元素，msg 表示需要遍历的数据
    print(f"{msg}含有的元素有{i}")
else :
    print("遍历完成",)


# 计算1-100内所有奇数的之和

"""range语句：生成指定规则的数据序列
range(end)--->获取一个从0开始，到end结束的数字序列（不含end本身）
range（start，end）--->获取一个从start开始，到end结束的数字序列（不含end本身）
range(start,end,step)--->获取一个从start开始，到end结束的数字序列,step步长（不含end本身）"""

total01 =0   #记录累加之和
for i in range(1,101,):
    if i % 2 != 0:   #判断是否奇数
        total01 +=i
print(f"1到100之间所有奇数之和为{total01}")


#计算100-500之间3的倍数之和
total02 = 0
for s in range(100,501):
    if s % 3 ==0 :
        total02 += s
print(f"100到500之间所有3的倍数之和为{total02}")








