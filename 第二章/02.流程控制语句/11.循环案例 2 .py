# 猜数字小游戏
import random
num = random.randint(1,100)
while True :
    guess_num = int(input("输入猜测的数字"))
    if num == guess_num :
        print("你猜对啦~~")
        break
    elif num < guess_num :
        print("你猜大了！！！")
    elif num > guess_num :
        print("你猜小了！！！")
print(f"随机生成的数字为{num}")


# 将1到1000（包含1000）所有5的倍数的数字累加起来
total = 0
for i in range(1,1001):
    if i % 5 == 0:
        total += i
print(f"1到1000（包含1000）所有5的倍数的数字累加起来为 {total}")