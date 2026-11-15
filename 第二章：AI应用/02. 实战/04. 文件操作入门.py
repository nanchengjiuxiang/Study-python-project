# 读取文件
# 1. 打开文件
f = open("Resources/text.txt", "r", encoding="utf-8")

# 2. 读取文件内容
# text = f.read()
# print(text)

content = f.readlines()
for line in content:
    print(line.strip())

# 3. 关闭文件
f.close()


# 写入文件
# 1. 打开文件
f = open("Resources/静夜思.txt", "w", encoding="utf-8")

# 2. 写入文件内容
f.write("静夜思（李白）\n\n")
f.write("床前明月光\n")
f.write("疑是地上霜\n")
f.write("举头望明月\n")
f.write("低头思故乡")

# 3. 关闭文件
f.close()




# ===========================================资源释放 --> 防止代码异常导致无法关闭文件=========================================
# 方式一：try
# 1. 打开文件
f = open("Resources/静夜思.txt", "w", encoding="utf-8")

# 2. 写入文件内容
try:
    f.write("静夜思（李白）\n\n")
    f.write("床前明月光\n")
    f.write("疑是地上霜\n")
    f.write("举头望明月\n")
    f.write("低头思故乡")

# 3. 关闭文件
finally:
    f.close()



# 方式二：with（推荐） ---> 上下文管理
with open("Resources/静夜思.txt", "w", encoding="utf-8") as f:
    f.write("静夜思（李白）\n\n")
    f.write("床前明月光\n")
    f.write("疑是地上霜\n")
    f.write("举头望明月\n")
    f.write("低头思故乡")
